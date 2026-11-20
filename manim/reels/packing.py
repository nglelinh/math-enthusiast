from common import *
import math

TX = {
    "title": {"vi": "Xếp đĩa tròn sao cho khít nhất", "en": "Packing discs as tightly as possible"},
    "sq": {"vi": "Xếp ô vuông", "en": "Square grid"},
    "hx": {"vi": "Xếp tổ ong", "en": "Honeycomb"},
    "d1": {"vi": "phủ 78,5%", "en": "covers 78.5%"},
    "d2": {"vi": "phủ 90,7%", "en": "covers 90.7%"},
    "win": {"vi": "Tổ ong là tối ưu trong mặt phẳng", "en": "Honeycomb is optimal in the plane"},
    "hi": {"vi": "Chiều 3: 74% (Hales, kiểm chứng hình thức)", "en": "3D: 74% (Hales, formally verified)"},
    "hi2": {"vi": "Chiều 8 và 24: Viazovska và cộng sự", "en": "Dimensions 8 and 24: Viazovska and co-authors"},
}
sq = math.pi / 4
hx = math.pi / (2 * math.sqrt(3))
assert abs(sq - 0.785) < 1e-3 and abs(hx - 0.9069) < 1e-4
assert abs(math.pi / math.sqrt(18) - 0.7405) < 1e-4
R = 0.3
W, Hh = 7.2, 3.1


def discs(kind, cy):
    out = []
    if kind == "sq":
        nx, ny = int(W // (2 * R)), int(Hh // (2 * R))
        for j in range(ny):
            for i in range(nx):
                out.append([(-nx / 2 + i + 0.5) * 2 * R, cy + (ny / 2 - j - 0.5) * 2 * R])
    else:
        dy = 2 * R * math.sqrt(3) / 2
        ny = 1 + int((Hh - 2 * R) // dy)
        for j in range(ny):
            nx = int((W - (R if j % 2 else 0)) // (2 * R))
            nx = min(nx, int(W // (2 * R)) - (1 if j % 2 else 0))
            x0 = -(nx - 1) * R + (0 if j % 2 == 0 else 0)
            for i in range(nx):
                out.append([x0 + i * 2 * R, cy + (ny - 1) * dy / 2 - j * dy])
    return out


class Packing(Scene):
    def construct(self):
        c = cap(TX["title"], 34)
        self.add(c)
        res = {}
        for kind, cy, col, key, dk in (("sq", 2.9, SKY, "sq", "d1"), ("hx", -1.9, PINK, "hx", "d2")):
            lab = fit(T(tr(TX[key]), 34, col)).move_to([0, cy + Hh / 2 + 0.5, 0])
            frame = Rectangle(width=W + 0.2, height=Hh + 0.2, color=DIM, stroke_width=2).move_to([0, cy, 0])
            ds = VGroup(*[Circle(radius=R * 0.96, color=col, stroke_width=3, fill_color=col, fill_opacity=0.35).move_to([x, y, 0]) for x, y in discs(kind, cy)])
            # tất cả đĩa nằm trong khung
            for x, y in discs(kind, cy):
                assert abs(x) + R <= W / 2 + 0.1 + 1e-9 and abs(y - cy) + R <= Hh / 2 + 0.1 + 1e-9, (kind, x, y)
            pc = fit(T(tr(TX[dk]), 36, WHITE)).move_to([0, cy - Hh / 2 - 0.5, 0])
            self.play(FadeIn(lab), Create(frame), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in ds], lag_ratio=0.01), run_time=2.0)
            self.play(FadeIn(pc), run_time=0.5)
            self.wait(0.8)
            res[kind] = (ds, pc)
        w = fit(T(tr(TX["win"]), 32, SUN)).move_to([0, -4.9, 0])
        self.play(FadeIn(w), run_time=0.6)
        self.play(Indicate(res["hx"][1], color=SUN, scale_factor=1.2), run_time=0.8)
        self.wait(1.0)
        h1 = fit(T(tr(TX["hi"]), 28, MINT)).move_to([0, -5.6, 0])
        h2 = fit(T(tr(TX["hi2"]), 28, MINT)).move_to([0, -6.2, 0])
        self.play(FadeIn(h1), run_time=0.5)
        self.play(FadeIn(h2), run_time=0.5)
        self.wait(5.0)
