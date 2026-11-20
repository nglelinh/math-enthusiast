from common_b import *

TX = {
    "title": {"vi": "Một số, hai cách tính", "en": "One number, two ways to build it"},
    "sum": {"vi": "Tổng 1/n² trên MỌI số n ≤ x", "en": "Sum of 1/n² over ALL n ≤ x"},
    "prod": {"vi": "Tích 1/(1 − p⁻²) chỉ qua số nguyên tố p ≤ x", "en": "Product of 1/(1 − p⁻²) over primes p ≤ x"},
    "lim": {"vi": "π²/6 ≈ 1,6449", "en": "π²/6 ≈ 1.6449"},
    "x": {"vi": "x", "en": "x"},
    "end": {"vi": "Euler: tổng trên mọi số tự nhiên\n= tích trên các số nguyên tố", "en": "Euler: the sum over all integers\n= the product over primes"},
    "end2": {"vi": "Cánh cửa từ ζ(s) tới các số nguyên tố", "en": "The door from ζ(s) to the primes"},
}
XM = 100
pr = [n for n in range(2, XM + 1) if all(n % q for q in range(2, int(n ** 0.5) + 1))]
S, P = [], []
s, p = 0.0, 1.0
for x in range(1, XM + 1):
    s += 1 / x ** 2
    if x in pr:
        p *= 1 / (1 - 1 / x ** 2)
    S.append(s); P.append(p)
Z = math.pi ** 2 / 6
assert len(pr) == 25
assert abs(sum(1 / n ** 2 for n in range(1, 400001)) - Z) < 1e-5
assert S[-1] < Z and P[-1] < Z and Z - S[-1] < 0.011 and Z - P[-1] < 0.005
# phần dư của tích ≈ Σ_{p>100} p^-2 → tích tiến tới Z
big = [n for n in range(101, 200000) if all(n % q for q in range(2, int(n ** 0.5) + 1))]
assert abs(P[-1] * math.prod(1 / (1 - 1 / q ** 2) for q in big) - Z) < 1e-4


class Euler(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        a = line(TX["sum"], 28, SKY, 5.3)
        b = line(TX["prod"], 26, PINK, 4.7)
        self.play(FadeIn(a), FadeIn(b), run_time=0.8)
        ax, lab = mkaxes([0, 100, 25], [0, 0.7, 0.1], 7.0, 5.2, [0.2, 0.9, 0],
                         xt=(0, 25, 50, 75, 100),
                         yt=[(v - 1, nf(v, 1)) for v in (1.0, 1.2, 1.4, 1.6)])
        zl = DashedLine(ax.c2p(0, Z - 1), ax.c2p(100, Z - 1), color=SUN, stroke_width=3)
        zt = T(tr(TX["lim"]), 26, SUN).next_to(zl, UP, buff=0.1).align_to(ax.c2p(0, 0), LEFT).shift(RIGHT * 0.1)
        self.play(Create(ax), FadeIn(lab), run_time=0.9)
        self.play(Create(zl), FadeIn(zt), run_time=0.7)
        kt = ValueTracker(1)
        K = lambda: int(round(kt.get_value()))
        ls = always_redraw(lambda: VMobject(color=SKY, stroke_width=5).set_points_as_corners(
            [ax.c2p(i, S[i - 1] - 1) for i in range(1, max(K(), 2) + 1)]))
        lp = always_redraw(lambda: VMobject(color=PINK, stroke_width=5).set_points_as_corners(
            [ax.c2p(i, P[i - 1] - 1) for i in range(1, max(K(), 2) + 1)]))
        ds = always_redraw(lambda: Dot(ax.c2p(K(), S[K() - 1] - 1), radius=0.09, color=SKY))
        dp = always_redraw(lambda: Dot(ax.c2p(K(), P[K() - 1] - 1), radius=0.09, color=PINK))
        rs = always_redraw(lambda: T("x = %d     %s  %s     %s  %s" % (K(), "Σ" if True else "", nf(S[K() - 1], 4), "Π", nf(P[K() - 1], 4)), 30, WHITE).move_to([0, -2.9, 0]))
        self.add(ls, lp, ds, dp, rs)
        self.play(kt.animate.set_value(XM), run_time=9.0, rate_func=smooth)
        e1 = line(TX["end"], 32, MINT, -4.3)
        e2 = line(TX["end2"], 28, SUN, -5.5)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.5)
