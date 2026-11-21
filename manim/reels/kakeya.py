from common_b import *
import numpy as np

TX = {
    "title": {"vi": "Kim quay 180° trong một deltoid", "en": "A needle turning 180° inside a deltoid"},
    "needle": {"vi": "Kim dài 1 luôn nằm trọn trong hình", "en": "A needle of length 1 stays inside"},
    "ang": {"vi": "Góc quay", "en": "Angle turned"},
    "disk": {"vi": "Đĩa (quay quanh tâm): π/4 ≈ 0,785", "en": "Disc (spin about centre): π/4 ≈ 0.785"},
    "delt": {"vi": "Deltoid: chỉ π/8 ≈ 0,393 (một nửa)", "en": "Deltoid: only π/8 ≈ 0.393 (half)"},
    "bes": {"vi": "Besicovitch: nhỏ tùy ý", "en": "Besicovitch: arbitrarily small"},
}
r = 1.25
Lneedle = 4 * r
zf = lambda t: 2 * r * np.exp(1j * t) + r * np.exp(-2j * t)
tt = np.linspace(0, 2 * np.pi, 4001)
curve = zf(tt)
x, y = curve.real, curve.imag
area = 0.5 * abs(np.sum(x[:-1] * y[1:] - x[1:] * y[:-1]))
assert abs(area / Lneedle ** 2 - np.pi / 8) < 1e-4            # diện tích = π/8 · L²
assert abs(area / (np.pi * (Lneedle / 2) ** 2) - 0.5) < 1e-4  # đúng một nửa đĩa đường kính L
assert abs(abs(zf(1.0) - zf(1.0 + np.pi)) - Lneedle) < 1e-9    # dây luôn dài L
poly = (curve * 1.004)


def inside(p):
    c = False
    xs, ys = poly.real, poly.imag
    for i in range(len(xs) - 1):
        if (ys[i] > p.imag) != (ys[i + 1] > p.imag):
            if p.real < (xs[i + 1] - xs[i]) * (p.imag - ys[i]) / (ys[i + 1] - ys[i]) + xs[i]:
                c = not c
    return c


for t in np.linspace(0, np.pi, 41):
    a, b = zf(t), zf(t + np.pi)
    assert all(inside(a + (b - a) * s) for s in np.linspace(0.02, 0.98, 13)), t
d = np.angle(zf(0.0 + np.pi) - zf(0.0)), np.angle(zf(np.pi + np.pi) - zf(np.pi))
assert abs(abs(d[1] - d[0]) - np.pi) < 1e-9     # sau t từ 0 → π, kim quay đúng 180°
P = lambda z: np.array([z.real, z.imag, 0])


class Kakeya(Scene):
    def construct(self):
        self.add(line(TX["title"], 34, WHITE, 6.3))
        n = line(TX["needle"], 30, SUN, 5.3)
        self.play(FadeIn(n), run_time=0.6)
        outline = VMobject(color=SKY, stroke_width=5).set_points_as_corners([P(z) + UP * 0.6 for z in curve[::8]])
        shift = UP * 0.6
        self.play(Create(outline), run_time=2.0)
        tk = ValueTracker(0.0)
        T_ = lambda: tk.get_value()
        needle = always_redraw(lambda: Line(P(zf(T_())) + shift, P(zf(T_() + np.pi)) + shift, color=SUN, stroke_width=9))
        ends = always_redraw(lambda: VGroup(Dot(P(zf(T_())) + shift, radius=0.1, color=PINK), Dot(P(zf(T_() + np.pi)) + shift, radius=0.1, color=PINK)))
        ghosts = always_redraw(lambda: VGroup(*[Line(P(zf(s)) + shift, P(zf(s + np.pi)) + shift, color=SUN, stroke_width=2.5, stroke_opacity=0.28)
                                                for s in np.arange(0, T_(), np.pi / 90)]))
        ang = always_redraw(lambda: T("%s: %d°" % (tr(TX["ang"]), round(T_() * 180 / np.pi)), 34, WHITE).move_to([0, -3.6, 0]))
        self.add(ghosts, needle, ends, ang)
        self.play(tk.animate.set_value(np.pi), run_time=9.0, rate_func=smooth)
        self.wait(0.6)
        circ = DashedVMobject(Circle(radius=Lneedle / 2, color=ORANGE, stroke_width=4).move_to(shift + RIGHT * r), num_dashes=60)
        t1 = line(TX["disk"], 30, ORANGE, -4.5)
        t2 = line(TX["delt"], 30, MINT, -5.25)
        t3 = line(TX["bes"], 30, SUN, -6.0)
        self.play(Create(circ), FadeIn(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.7)
        self.play(FadeIn(t3), run_time=0.7)
        self.wait(3.0)
