from common_b import *
import numpy as np

TX = {
    "title": {"vi": "Cộng xúc xắc: hình chuông hiện ra", "en": "Add many dice: a bell appears"},
    "n1": {"vi": "tổng của n xúc xắc", "en": "sum of n dice"},
    "bell": {"vi": "đường chuông chuẩn", "en": "normal bell curve"},
    "end": {"vi": "Một xúc xắc thì đều,\nnhưng tổng lại thành chuông", "en": "One die is flat,\nbut the sum becomes a bell"},
    "end2": {"vi": "Định lý giới hạn trung tâm", "en": "The central limit theorem"},
}
STAGES = [1, 2, 3, 5, 10, 30]


def pmf(n):
    p = np.ones(6) / 6
    out = p.copy()
    for _ in range(n - 1):
        out = np.convolve(out, p)
    return out            # chỉ số i ↔ tổng n+i


def Phi(z): return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def ks(n):
    p = pmf(n); mu = 3.5 * n; sd = math.sqrt(35 * n / 12); c = 0; m = 0
    for i, v in enumerate(p):
        c += v
        m = max(m, abs(c - Phi((n + i + 0.5 - mu) / sd)))
    return m


K = [ks(n) for n in STAGES]
assert all(abs(pmf(n).sum() - 1) < 1e-12 for n in STAGES)
assert all(K[i] > K[i + 1] for i in range(len(K) - 1)) and K[-1] < 0.005 and K[0] > 0.05, K


class CLT(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        ax, lab = mkaxes([-3.5, 3.5, 1], [0, 0.45, 0.1], 7.4, 6.2, [0, 1.7, 0], xt=(), yt=())
        W = lambda: None
        nf_ = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
        bell = ax.plot(nf_, x_range=[-3.5, 3.5], color=SKY, stroke_width=5)
        bl = fit(T(tr(TX["bell"]), 26, SKY), 4).move_to([2.2, 4.9, 0])
        self.play(Create(ax), Create(bell), FadeIn(bl), run_time=1.2)

        def bars(n):
            p = pmf(n); mu = 3.5 * n; sd = math.sqrt(35 * n / 12)
            g = VGroup()
            for i, v in enumerate(p):
                zc = (n + i - mu) / sd
                h = v * sd
                if h < 1e-4: continue
                a, b = ax.c2p(zc - 0.5 / sd, 0), ax.c2p(zc + 0.5 / sd, h)
                g.add(Rectangle(width=max(b[0] - a[0] - 0.02, 0.01), height=b[1] - a[1], stroke_width=0, fill_color=SUN, fill_opacity=0.9).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0]))
            return g
        def label(n):
            return T("%s: n = %d" % (tr(TX["n1"]), n), 32, WHITE).move_to([0, -2.0, 0])
        cur = bars(1); lb = label(1)
        self.play(FadeIn(cur), FadeIn(lb), run_time=0.8)
        self.wait(1.2)
        for n in STAGES[1:]:
            nb, nl = bars(n), label(n)
            self.play(ReplacementTransform(cur, nb), ReplacementTransform(lb, nl), run_time=1.3)
            cur, lb = nb, nl
            self.wait(1.1 if n < 30 else 0.4)
        e1 = line(TX["end"], 30, MINT, -3.5)
        e2 = line(TX["end2"], 36, SUN, -4.5)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.5)
