from common import *
import math

TX = {
    "title": {"vi": "Sóng sin dựng nên sóng vuông", "en": "Sine waves build a square wave"},
    "sum": {"vi": "Cộng các sóng sin lẻ với biên độ giảm dần", "en": "Add odd sine waves with shrinking amplitude"},
    "n": {"vi": "sóng sin", "en": "sine waves"},
    "gibbs": {"vi": "Chỗ gãy vẫn vọt lên khoảng 9% bước nhảy", "en": "The jump still overshoots by about 9% of the step"},
    "gibbs2": {"vi": "(hiệu ứng Gibbs)", "en": "(the Gibbs effect)"},
    "end": {"vi": "Tín hiệu phức tạp = tổng tần số đơn giản", "en": "Complex signal = sum of simple frequencies"},
}
def S(x, n):
    return 4 / math.pi * sum(math.sin((2 * k + 1) * x) / (2 * k + 1) for k in range(n))
peak = max(S(i * 0.0005, 11) for i in range(1, 6000))
assert 1.17 < peak < 1.19 and abs((peak - 1) / 2 - 0.0895) < 0.002


class Fourier(Scene):
    def construct(self):
        c = cap(TX["title"], 36)
        self.add(c)
        f = MathTex(r"\frac{4}{\pi}\Big(\sin x+\frac{\sin 3x}{3}+\frac{\sin 5x}{5}+\cdots\Big)", font_size=50, color=SUN).move_to([0, 4.6, 0])
        self.play(Write(f), run_time=1.5)
        sm = fit(T(tr(TX["sum"]), 28, WHITE)).move_to([0, 3.6, 0])
        self.play(FadeIn(sm), run_time=0.6)
        ax = Axes(x_range=[-math.pi, math.pi, math.pi / 2], y_range=[-1.5, 1.5, 1], x_length=7.4, y_length=4.2,
                  axis_config={"color": DIM, "stroke_width": 3, "include_ticks": False}, tips=False).move_to([0, 0.6, 0])
        tgt = VGroup(Line(ax.c2p(-math.pi, -1), ax.c2p(0, -1)), Line(ax.c2p(0, -1), ax.c2p(0, 1)),
                     Line(ax.c2p(0, 1), ax.c2p(math.pi, 1))).set_color(DIM).set_stroke(width=3)
        self.play(Create(ax), Create(tgt), run_time=1.0)
        eps = 0.0001
        plot = lambda n: ax.plot(lambda x: S(x, n), x_range=[-math.pi + eps, math.pi - eps, 0.01], color=SKY, stroke_width=5, use_smoothing=False)
        lab = lambda n: T("%d %s" % (n, ("sine wave" if (LANG == "en" and n == 1) else tr(TX["n"]))), 40, SKY).move_to([0, -2.6, 0])
        cur = plot(1); cl = lab(1)
        self.play(Create(cur), FadeIn(cl), run_time=1.2)
        self.wait(0.8)
        for n in (2, 3, 5, 11):
            nxt = plot(n); nl = lab(n)
            self.play(Transform(cur, nxt), Transform(cl, nl), run_time=1.1)
            self.wait(0.9)
        g1 = fit(T(tr(TX["gibbs"]), 28, ORANGE)).move_to([0, -3.7, 0])
        g2 = fit(T(tr(TX["gibbs2"]), 26, ORANGE)).move_to([0, -4.3, 0])
        ring = Circle(radius=0.35, color=ORANGE, stroke_width=5).move_to(ax.c2p(0.28, 1.18))
        self.play(FadeIn(g1), FadeIn(g2), Create(ring), run_time=0.8)
        self.wait(1.8)
        e = fit(T(tr(TX["end"]), 30, MINT)).move_to([0, -5.4, 0])
        self.play(FadeIn(e), run_time=0.6)
        self.wait(3.5)
