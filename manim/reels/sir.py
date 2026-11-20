from common_b import *
import numpy as np

TX = {
    "title": {"vi": "Dịch SIR: R₀ quyết định tất cả", "en": "SIR epidemic: R₀ decides it all"},
    "yl": {"vi": "tỉ lệ đang nhiễm", "en": "share infected now"},
    "xl": {"vi": "thời gian (đơn vị: một kỳ lây)", "en": "time (unit: one infectious period)"},
    "r08": {"vi": "R₀ = 0,8: tắt dần, không bùng phát", "en": "R₀ = 0.8: fades out, no outbreak"},
    "r15": {"vi": "R₀ = 1,5: đỉnh ≈ 8%, tổng cộng ≈ 61% nhiễm", "en": "R₀ = 1.5: peak ≈ 8%, ≈ 61% infected in total"},
    "r3": {"vi": "R₀ = 3: đỉnh ≈ 31%, tổng cộng ≈ 94% nhiễm", "en": "R₀ = 3: peak ≈ 31%, ≈ 94% infected in total"},
    "end": {"vi": "R₀ > 1: bùng phát\nR₀ < 1: tắt dần", "en": "R₀ > 1: outbreak\nR₀ < 1: dies out"},
}
I0 = 3e-2


def sim(R0, T_=30.0, dt=0.01):
    s, i = 1 - I0, I0
    ts, iv = [0.0], [i]
    for k in range(int(T_ / dt)):
        f = lambda s, i: (-R0 * s * i, R0 * s * i - i)
        k1 = f(s, i); k2 = f(s + dt / 2 * k1[0], i + dt / 2 * k1[1]); k3 = f(s + dt / 2 * k2[0], i + dt / 2 * k2[1]); k4 = f(s + dt * k3[0], i + dt * k3[1])
        s += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); i += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        ts.append((k + 1) * dt); iv.append(i)
    return ts, iv, s


def final_size(R0):
    z = 0.5
    for _ in range(200): z = 1 - math.exp(-R0 * z)
    return z


RUNS = {R0: sim(R0) for R0 in (0.8, 1.5, 3.0)}
for R0 in (1.5, 3.0):
    ts, iv, sinf = RUNS[R0]
    s0 = 1 - I0
    imax = I0 + s0 - (1 + math.log(R0 * s0)) / R0
    assert abs(max(iv) - imax) < 1e-4, (R0, max(iv), imax)
assert max(RUNS[0.8][1]) == I0 and RUNS[0.8][1][-1] < 1e-3
FIN = {R0: 1 - RUNS[R0][2] for R0 in (1.5, 3.0)}
PK = {R0: max(RUNS[R0][1]) for R0 in (1.5, 3.0)}
for R0 in (1.5, 3.0):                       # s∞ = s0 · exp(−R0 (1 − s∞))
    sinf = RUNS[R0][2]; assert abs(sinf - (1 - I0) * math.exp(-R0 * (1 - sinf))) < 1e-4
assert round(PK[1.5] * 100) == 8 and round(PK[3.0] * 100) == 31 and round(FIN[1.5] * 100) == 61 and round(FIN[3.0] * 100) == 94, (PK, FIN)
STEP = 5   # lấy mẫu mỗi 0.05


class SIR(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        ax, lab = mkaxes([0, 30, 10], [0, 0.35, 0.1], 7.0, 5.0, [0.1, 2.9, 0], xt=(0, 10, 20, 30),
                         yt=[(v, "%d%%" % round(v * 100)) for v in (0, 0.1, 0.2, 0.3)])
        yl = line(TX["yl"], 22, DIM, 5.7).set_x(-2.2)
        xl = line(TX["xl"], 22, DIM, -0.3)
        self.play(Create(ax), FadeIn(lab), FadeIn(yl), FadeIn(xl), run_time=0.9)
        tk = ValueTracker(0)
        cols = {0.8: ORANGE, 1.5: SKY, 3.0: PINK}
        mk = lambda R0: always_redraw(lambda: VMobject(color=cols[R0], stroke_width=6).set_points_as_corners(
            [ax.c2p(RUNS[R0][0][j], RUNS[R0][1][j]) for j in range(0, max(int(tk.get_value() * 100), 1) + 1, STEP)]))
        for R0 in (0.8, 1.5, 3.0): self.add(mk(R0))
        self.play(tk.animate.set_value(30), run_time=9.0, rate_func=linear)
        y = -1.2
        for k, col in (("r08", ORANGE), ("r15", SKY), ("r3", PINK)):
            m = line(TX[k], 28, col, y)
            self.play(FadeIn(m), run_time=0.6); y -= 0.8
        e = line(TX["end"], 38, SUN, y - 0.9)
        self.play(FadeIn(e), run_time=0.7)
        self.wait(3.5)
