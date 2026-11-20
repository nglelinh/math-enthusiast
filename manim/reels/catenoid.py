from common_b import *
import numpy as np

TX = {
    "title": {"vi": "Màng xà phòng giữa hai vòng", "en": "A soap film between two rings"},
    "sep": {"vi": "Khoảng cách / bán kính", "en": "Distance / radius"},
    "cat": {"vi": "Diện tích màng", "en": "Film area"},
    "two": {"vi": "Hai đĩa phẳng", "en": "Two flat discs"},
    "weak": {"vi": "Màng còn đứng, nhưng hai đĩa\ncó diện tích nhỏ hơn", "en": "The film still stands, but\ntwo discs have less area"},
    "break": {"vi": "Xa quá ≈ 1,33 bán kính: hết catenoid.\nMàng vỡ thành hai đĩa", "en": "Past ≈ 1.33 radii: no catenoid left.\nThe film pops into two discs"},
}
hf = lambda a: a * math.acosh(1 / a)                      # h(a) với R = 1
# nhánh bền: a ≥ a_c, nơi h(a) cực đại
lo, hi = 1e-3, 1.0
for _ in range(200):
    m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
    if hf(m1) < hf(m2): lo = m1
    else: hi = m2
AC = (lo + hi) / 2; HC = hf(AC)


def a_of(h):
    l, r = AC, 1.0
    for _ in range(80):
        mid = (l + r) / 2
        if hf(mid) > h: l = mid
        else: r = mid
    return (l + r) / 2


area = lambda h: (lambda a: math.pi * (2 * a * h + a * a * math.sinh(2 * h / a)))(a_of(h))
assert abs(HC - 0.6627) < 5e-4 and abs(AC - 0.5524) < 5e-4
l, r = 0.01, HC
for _ in range(80):
    mid = (l + r) / 2
    if area(mid) < 2 * math.pi: l = mid
    else: r = mid
HG = (l + r) / 2
assert abs(HG - 0.5277) < 2e-3, HG                       # giao điểm Goldschmidt
assert area(0.2) < 2 * math.pi < area(0.6)
# kiểm tra số học diện tích bằng tích phân số
h0 = 0.4; a0 = a_of(h0); zz = np.linspace(-h0, h0, 200001)
num = 2 * math.pi * np.trapezoid(a0 * np.cosh(zz / a0) ** 2, zz)
assert abs(num - area(h0)) < 1e-6 and abs(a0 * math.cosh(h0 / a0) - 1) < 1e-9
S = 3.0; CEN = np.array([0, 1.7, 0])


def P(r, z): return CEN + np.array([r * S, z * S, 0])


class Catenoid(Scene):
    def construct(self):
        self.add(line(TX["title"], 38, WHITE, 6.3))
        tk = ValueTracker(0.03)
        H = lambda: tk.get_value()
        broken = [False]

        def film():
            h = H(); g = VGroup()
            if broken[0]:
                for z in (h, -h):
                    g.add(Line(P(-1, z), P(1, z), color=SKY, stroke_width=10))
                return g
            a = a_of(h)
            zs = np.linspace(-h, h, 60)
            right = [P(a * math.cosh(z / a), z) for z in zs]
            left = [P(-a * math.cosh(z / a), z) for z in zs]
            poly = Polygon(*(right + left[::-1]), stroke_width=0, fill_color=SKY, fill_opacity=0.28)
            g.add(poly, VMobject(color=SKY, stroke_width=6).set_points_as_corners(right), VMobject(color=SKY, stroke_width=6).set_points_as_corners(left))
            return g
        rings = always_redraw(lambda: VGroup(*[VGroup(Line(P(-1.12, z), P(1.12, z), color=DIM, stroke_width=3), Dot(P(-1, z), radius=0.09, color=SUN), Dot(P(1, z), radius=0.09, color=SUN)) for z in (H(), -H())]))
        fl = always_redraw(film)
        sep = always_redraw(lambda: T("%s: %s" % (tr(TX["sep"]), nf(2 * H(), 2)), 32, WHITE).move_to([0, -1.2, 0]))
        def areas():
            h = H(); g = VGroup()
            if broken[0]:
                g.add(T("%s: %s" % (tr(TX["cat"]), "—"), 30, DIM), T("%s: %s" % (tr(TX["two"]), nf(2 * math.pi, 2)), 30, MINT))
            else:
                ac = area(h)
                g.add(T("%s: %s" % (tr(TX["cat"]), nf(ac, 2)), 30, MINT if ac < 2 * math.pi else ORANGE), T("%s: %s" % (tr(TX["two"]), nf(2 * math.pi, 2)), 30, WHITE))
            return g.arrange(DOWN, buff=0.18).move_to([0, -2.4, 0])
        ar = always_redraw(areas)
        self.add(fl, rings, sep, ar)
        self.wait(1.0)
        self.play(tk.animate.set_value(HG), run_time=5.0, rate_func=linear)
        w = line(TX["weak"], 30, ORANGE, -4.1)
        self.play(FadeIn(w), run_time=0.5)
        self.play(tk.animate.set_value(HC - 0.002), run_time=3.5, rate_func=linear)
        self.wait(0.8)
        broken[0] = True
        tk.set_value(HC + 0.05)
        self.wait(0.2)
        b = line(TX["break"], 30, PINK, -4.3)
        b.set_width(min(b.width, 7.8))
        self.play(FadeOut(w), FadeIn(b), run_time=0.6)
        self.wait(3.5)
