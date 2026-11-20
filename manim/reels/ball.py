from common_b import *

TX = {
    "title": {"vi": "Thể tích quả cầu đơn vị trong n chiều", "en": "Volume of the unit ball in n dimensions"},
    "ylab": {"vi": "thể tích", "en": "volume"},
    "xlab": {"vi": "số chiều n", "en": "dimension n"},
    "max": {"vi": "Lớn nhất ở n = 5 (≈ 5,26)", "en": "Largest at n = 5 (≈ 5.26)"},
    "then": {"vi": "Rồi co dần về 0", "en": "Then it shrinks towards 0"},
    "frac": {"vi": "Quả cầu chiếm bao nhiêu\nhình lập phương [−1, 1]ⁿ?", "en": "How much of the cube [−1, 1]ⁿ\ndoes the ball fill?"},
    "corner": {"vi": "Đỉnh hình lập phương cách tâm √n:\nn = 100 → 10 lần bán kính", "en": "A cube corner is √n from the centre:\nn = 100 → 10 radii"},
}
V = lambda n: math.pi ** (n / 2) / math.gamma(n / 2 + 1)
vals = {n: V(n) for n in range(1, 21)}
assert abs(vals[1] - 2) < 1e-12 and abs(vals[2] - math.pi) < 1e-12 and abs(vals[3] - 4 * math.pi / 3) < 1e-12
assert max(vals, key=vals.get) == 5 and abs(vals[5] - 5.2638) < 1e-3 and abs(vals[20] - 0.025807) < 1e-5
assert all(vals[n] > vals[n + 1] for n in range(5, 20))
FR = {n: V(n) / 2 ** n for n in (2, 3, 5, 10, 20)}
assert abs(FR[2] - math.pi / 4) < 1e-12 and abs(FR[3] - math.pi / 6) < 1e-12
assert abs(FR[10] * 100 - 0.2490) < 5e-4 and abs(FR[20] - 2.461e-8) < 1e-11


class Ball(Scene):
    def construct(self):
        self.add(line(TX["title"], 34, WHITE, 6.3))
        ax, lab = mkaxes([0, 21, 5], [0, 6, 1], 7.0, 4.3, [-0.2, 3.7, 0], xt=(1, 5, 10, 15, 20), yt=[(v, str(v)) for v in (0, 2, 4, 6)])
        xl = T("n", 26, DIM).next_to(ax.c2p(21, 0), RIGHT, buff=0.1)
        self.play(Create(ax), FadeIn(lab), FadeIn(xl), run_time=0.9)
        bars = {}
        for n in range(1, 21):
            a, b = ax.c2p(n - 0.38, 0), ax.c2p(n + 0.38, vals[n])
            bars[n] = Rectangle(width=b[0] - a[0], height=b[1] - a[1], stroke_width=0, fill_color=SKY if n <= 5 else PINK, fill_opacity=0.95).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])
        for n in range(1, 21):
            self.play(GrowFromEdge(bars[n], DOWN), run_time=0.22 if n < 6 else 0.14)
            if n == 5:
                m = line(TX["max"], 30, SUN, 0.75)
                self.play(FadeIn(m), bars[5].animate.set_fill(SUN), run_time=0.6)
                self.wait(0.6)
        t = line(TX["then"], 30, PINK, 0.05)
        self.play(FadeIn(t), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(m), FadeOut(t), run_time=0.4)
        f = line(TX["frac"], 30, WHITE, 0.35)
        self.play(FadeIn(f), run_time=0.6)
        rows = []
        sci = lambda v: (("%.1f·10⁻⁶ %%" % (v * 1e8)).replace(".", ",") if LANG == "vi" else "%.1f·10⁻⁶ %%" % (v * 1e8))
        txt = {2: nf(FR[2] * 100, 1) + " %", 3: nf(FR[3] * 100, 1) + " %", 5: nf(FR[5] * 100, 1) + " %", 10: nf(FR[10] * 100, 2) + " %", 20: sci(FR[20])}
        y = -0.5
        for n in (2, 3, 5, 10, 20):
            r = T("n = %2d :   %s" % (n, txt[n]), 32, SUN if n == 20 else WHITE).move_to([0, y, 0])
            self.play(FadeIn(r), run_time=0.5)
            y -= 0.66
        self.wait(0.4)
        c = line(TX["corner"], 30, MINT, -4.1)
        self.play(FadeIn(c), run_time=0.7)
        self.wait(3.5)
