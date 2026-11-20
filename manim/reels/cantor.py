from common import *
import random

TX = {
    "title": {"vi": "Đường chéo của Cantor", "en": "Cantor's diagonal"},
    "list": {"vi": "Giả sử có danh sách ĐẦY ĐỦ mọi dãy 0-1", "en": "Suppose a COMPLETE list of 0-1 sequences"},
    "diag": {"vi": "Lấy chữ số trên đường chéo", "en": "Take the diagonal digits"},
    "flip": {"vi": "Đổi mỗi chữ số: 0 thành 1, 1 thành 0", "en": "Flip each digit: 0 to 1, 1 to 0"},
    "new": {"vi": "Dãy mới", "en": "New"},
    "differ": {"vi": "Khác dãy thứ n ở vị trí thứ n", "en": "Differs from row n at place n"},
    "end": {"vi": "Nó không có trong danh sách. Mâu thuẫn!", "en": "It is not on the list. Contradiction!"},
    "res": {"vi": "Các số thực không thể đếm được", "en": "The reals cannot be listed"},
}
ROWS = ["010110", "110010", "001101", "101001", "011100", "100011"]
N = len(ROWS)
DIAG = [ROWS[i][i] for i in range(N)]
FLIP = ["1" if d == "0" else "0" for d in DIAG]
assert all(FLIP[i] != ROWS[i][i] for i in range(N))
assert all("".join(FLIP) != r for r in ROWS)


class Cantor(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        S = 0.95
        x0, y0 = -2.4, 3.6
        cap2 = fit(T(tr(TX["list"]), 30, WHITE)).move_to([0, 5.2, 0])
        self.play(FadeIn(cap2), run_time=0.6)
        cell = {}
        labels = VGroup()
        for i in range(N):
            lab = T("s%d" % (i + 1), 28, DIM).move_to([x0 - 1.0, y0 - i * S, 0])
            labels.add(lab)
            for j in range(N):
                t = T(ROWS[i][j], 40, WHITE).move_to([x0 + j * S, y0 - i * S, 0])
                cell[(i, j)] = t
        dots = T("⋮", 40, DIM).move_to([x0 + 2.5 * S, y0 - N * S + 0.1, 0])
        dots2 = T("…", 40, DIM).move_to([x0 + N * S + 0.1, y0 - 2.5 * S, 0])
        self.play(FadeIn(labels), LaggedStart(*[FadeIn(cell[(i, j)]) for i in range(N) for j in range(N)], lag_ratio=0.02),
                  FadeIn(dots), FadeIn(dots2), run_time=2.0)
        self.wait(0.5)
        cap3 = fit(T(tr(TX["diag"]), 30, SUN)).move_to([0, 5.2, 0])
        self.play(ReplacementTransform(cap2, cap3), run_time=0.4)
        boxes = VGroup(*[RoundedRectangle(corner_radius=0.1, width=S * 0.85, height=S * 0.85, color=SUN, stroke_width=4).move_to(cell[(i, i)])
                         for i in range(N)])
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.25), *[cell[(i, i)].animate.set_color(SUN) for i in range(N)], run_time=2.2)
        cap4 = fit(T(tr(TX["flip"]), 30, SUN)).move_to([0, 5.2, 0])
        self.play(ReplacementTransform(cap3, cap4), run_time=0.4)
        ny = y0 - N * S - 1.2
        nl = fit(T(tr(TX["new"]), 24, PINK), 1.15).move_to([x0 - 1.15, ny, 0])
        new = [T(FLIP[j], 40, PINK).move_to([x0 + j * S, ny, 0]) for j in range(N)]
        self.play(FadeIn(nl), run_time=0.4)
        self.play(LaggedStart(*[TransformFromCopy(cell[(j, j)], new[j]) for j in range(N)], lag_ratio=0.3), run_time=2.4)
        self.wait(0.5)
        cap5 = fit(T(tr(TX["differ"]), 30, PINK)).move_to([0, 5.2, 0])
        self.play(ReplacementTransform(cap4, cap5), run_time=0.4)
        for i in range(N):
            self.play(Indicate(new[i], color=WHITE, scale_factor=1.4), Indicate(cell[(i, i)], color=WHITE, scale_factor=1.4), run_time=0.45)
        end = fit(T(tr(TX["end"]), 34, MINT)).move_to([0, ny - 1.1, 0])
        self.play(FadeIn(end), run_time=0.6)
        res = fit(T(tr(TX["res"]), 36, SUN)).move_to([0, ny - 2.0, 0])
        self.play(FadeIn(res), run_time=0.6)
        self.wait(3.5)
