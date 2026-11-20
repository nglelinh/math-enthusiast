from common import *

TX = {
    "title": {"vi": "Quỹ đạo Collatz của số 97", "en": "The Collatz orbit of 97"},
    "even": {"vi": "Chẵn: chia 2", "en": "Even: halve it"},
    "odd": {"vi": "Lẻ: nhân 3 rồi cộng 1", "en": "Odd: triple it, add 1"},
    "go": {"vi": "Lặp lại cho đến khi về 1", "en": "Repeat until you reach 1"},
    "steps": {"vi": "bước", "en": "steps"},
    "peak": {"vi": "Đỉnh: 9232", "en": "Peak: 9232"},
    "end": {"vi": "118 bước, leo tới 9232 rồi mới rơi về 1", "en": "118 steps: up to 9232, then down to 1"},
    "open": {"vi": "Thử đâu cũng về 1, nhưng chưa ai chứng minh", "en": "Always reaches 1? Nobody can prove it"},
}
SEED = 97
vals = [SEED]
while vals[-1] != 1:
    n = vals[-1]
    vals.append(n // 2 if n % 2 == 0 else 3 * n + 1)
STEPS = len(vals) - 1
PEAK = max(vals)
PK = vals.index(PEAK)
assert STEPS == 118 and PEAK == 9232 and PK == 84


class Collatz(Scene):
    def construct(self):
        c = cap(TX["title"], 38)
        self.add(c)
        r1 = fit(T(tr(TX["even"]), 34, SKY)).move_to([0, 5.0, 0])
        r2 = fit(T(tr(TX["odd"]), 34, PINK)).move_to([0, 4.3, 0])
        self.play(FadeIn(r1), FadeIn(r2), run_time=0.8)
        seq = " → ".join(str(v) for v in vals[:6]) + " → …"
        s = fit(T(seq, 32, WHITE)).move_to([0, 3.4, 0])
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.2)
        go = fit(T(tr(TX["go"]), 30, SUN)).move_to([0, 3.4, 0])
        self.play(ReplacementTransform(s, go), run_time=0.5)

        ax = Axes(x_range=[0, 120, 20], y_range=[0, 10000, 2500], x_length=6.8, y_length=5.8,
                  axis_config={"color": DIM, "stroke_width": 3, "include_ticks": True, "tick_size": 0.06},
                  tips=False).move_to([0.3, -0.7, 0])
        ylab = VGroup(*[T(str(v), 20, DIM).next_to(ax.c2p(0, v), LEFT, buff=0.12) for v in (0, 5000, 10000)])
        xlab = VGroup(*[T(str(v), 20, DIM).next_to(ax.c2p(v, 0), DOWN, buff=0.12) for v in (0, 40, 80, 120)])
        self.play(Create(ax), FadeIn(ylab), FadeIn(xlab), run_time=1.0)

        kt = ValueTracker(0)
        K = lambda: int(kt.get_value())
        line = always_redraw(lambda: VMobject(color=SUN, stroke_width=4).set_points_as_corners(
            [ax.c2p(i, vals[i]) for i in range(max(K(), 1) + 1)]))
        dot = always_redraw(lambda: Dot(ax.c2p(K(), vals[K()]), radius=0.1, color=PINK))
        num = always_redraw(lambda: T("n = %d" % vals[K()], 44, WHITE).move_to([-1.6, -4.7, 0]))
        stp = always_redraw(lambda: T("%d %s" % (K(), tr(TX["steps"])), 36, SKY).move_to([2.2, -4.7, 0]))
        self.add(line, dot, num, stp)
        self.play(kt.animate.set_value(PK), run_time=7.0, rate_func=linear)
        pk = fit(T(tr(TX["peak"]), 34, ORANGE)).move_to(ax.c2p(PK, PEAK) + LEFT * 1.6 + DOWN * 0.1)
        self.play(FadeIn(pk), Indicate(dot, color=ORANGE, scale_factor=1.8), run_time=0.8)
        self.play(kt.animate.set_value(STEPS), run_time=2.0, rate_func=linear)
        c = swap_cap(self, c, cap(TX["end"], 28, SUN))
        self.wait(1.5)
        op = fit(T(tr(TX["open"]), 30, MINT)).move_to([0, -5.7, 0])
        self.play(FadeIn(op), run_time=0.6)
        self.wait(3.0)
