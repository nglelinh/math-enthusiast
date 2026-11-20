from common import *

TX = {
    "title": {"vi": "Hỗn độn: hai quỹ đạo gần như nhau", "en": "Chaos: two almost equal orbits"},
    "rule": {"vi": "Mỗi bước: x → 3,9·x(1 − x)", "en": "Each step: x → 3.9·x(1 − x)"},
    "a": {"vi": "Bắt đầu 0,2000", "en": "Start 0.2000"},
    "b": {"vi": "Bắt đầu 0,2001", "en": "Start 0.2001"},
    "gap": {"vi": "Chênh lệch", "en": "Difference"},
    "step": {"vi": "bước", "en": "step"},
    "end": {"vi": "Sai lệch một phần chục nghìn lớn dần đến cỡ 1", "en": "A 0.0001 gap grows to order 1"},
    "end2": {"vi": "Tất định, nhưng không thể dự báo xa", "en": "Deterministic, yet unpredictable"},
}
f = lambda x: 3.9 * x * (1 - x)
N = 40
xa, xb = [0.2], [0.2001]
for _ in range(N):
    xa.append(f(xa[-1])); xb.append(f(xb[-1]))
d = [abs(p - q) for p, q in zip(xa, xb)]
assert d[0] < 2e-4 and max(d[20:]) > 0.5 and d[5] < 0.01
assert all(0 <= v <= 1 for v in xa + xb)


class Logistic(Scene):
    def construct(self):
        c = cap(TX["title"], 34)
        self.add(c)
        r = fit(T(tr(TX["rule"]), 38, SUN)).move_to([0, 5.0, 0])
        self.play(FadeIn(r), run_time=0.8)
        la = fit(T(tr(TX["a"]), 30, SKY), 3.6).move_to([-2.0, 3.9, 0])
        lb = fit(T(tr(TX["b"]), 30, PINK), 3.6).move_to([2.0, 3.9, 0])
        self.play(FadeIn(la), FadeIn(lb), run_time=0.6)
        ax = Axes(x_range=[0, 40, 10], y_range=[0, 1, 0.5], x_length=7.2, y_length=4.4,
                  axis_config={"color": DIM, "stroke_width": 3, "tick_size": 0.06}, tips=False).move_to([0.2, 0.6, 0])
        yl = VGroup(*[T(s, 20, DIM).next_to(ax.c2p(0, v), LEFT, buff=0.12) for s, v in (("0", 0), ("0,5" if LANG == "vi" else "0.5", 0.5), ("1", 1))])
        xl = VGroup(*[T(str(v), 20, DIM).next_to(ax.c2p(v, 0), DOWN, buff=0.12) for v in (0, 10, 20, 30, 40)])
        self.play(Create(ax), FadeIn(yl), FadeIn(xl), run_time=1.0)
        kt = ValueTracker(0)
        K = lambda: int(kt.get_value())
        la_line = always_redraw(lambda: VMobject(color=SKY, stroke_width=5).set_points_as_corners([ax.c2p(i, xa[i]) for i in range(max(K(), 1) + 1)]))
        lb_line = always_redraw(lambda: VMobject(color=PINK, stroke_width=5).set_points_as_corners([ax.c2p(i, xb[i]) for i in range(max(K(), 1) + 1)]))
        da = always_redraw(lambda: Dot(ax.c2p(K(), xa[K()]), radius=0.09, color=SKY))
        db = always_redraw(lambda: Dot(ax.c2p(K(), xb[K()]), radius=0.09, color=PINK))
        fmt = (lambda v: ("%.4f" % v).replace(".", ",")) if LANG == "vi" else (lambda v: "%.4f" % v)
        gap = always_redraw(lambda: T("%s: %s" % (tr(TX["gap"]), fmt(d[K()])), 40, WHITE).move_to([0, -3.1, 0]))
        stp = always_redraw(lambda: T("%s %d" % (tr(TX["step"]), K()), 32, DIM).move_to([0, -3.9, 0]))
        self.add(la_line, lb_line, da, db, gap, stp)
        self.play(kt.animate.set_value(N), run_time=11.0, rate_func=linear)
        e1 = fit(T(tr(TX["end"]), 30, SUN)).move_to([0, -4.9, 0])
        e2 = fit(T(tr(TX["end2"]), 34, MINT)).move_to([0, -5.7, 0])
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.5)
