from common_b import *
import itertools

TX = {
    "title": {"vi": "Vận chuyển tối ưu trên đường thẳng", "en": "Optimal transport on a line"},
    "rule": {"vi": "Chuyển mỗi đống cát vào một hố\nChi phí = (quãng đường)²", "en": "Move each sand pile into one hole\nCost = (distance)²"},
    "cost": {"vi": "Tổng chi phí", "en": "Total cost"},
    "swap": {"vi": "Hai đường cắt nhau → đổi chỗ hai hố", "en": "Two paths cross → swap the two holes"},
    "end": {"vi": "Hết đường chéo: chi phí nhỏ nhất", "en": "No crossings left: the cost is the smallest"},
    "end2": {"vi": "Trên đường thẳng, tối ưu = ghép theo thứ tự", "en": "On a line, optimal = match in sorted order"},
}
SRC = [-3.5, -2.4, -1.1, 0.4, 1.9, 3.3]
DST = [-3.0, -1.8, 0.0, 1.2, 2.6, 3.6]
START = [2, 0, 3, 1, 5, 4]
cost = lambda sg: sum((SRC[i] - DST[j]) ** 2 for i, j in enumerate(sg))
best = min(itertools.permutations(range(6)), key=cost)
assert list(best) == list(range(6))
seq = [list(START)]
sg = list(START)
while True:
    k = next((i for i in range(5) if sg[i] > sg[i + 1]), None)
    if k is None: break
    sg[k], sg[k + 1] = sg[k + 1], sg[k]
    assert cost(sg) < cost(seq[-1]) - 1e-9
    seq.append(list(sg))
assert len(seq) == 5 and abs(cost(seq[-1]) - cost(list(range(6)))) < 1e-12
YS, YD = 2.2, -0.2


def pS(i): return np.array([SRC[i], YS, 0])
def pD(j): return np.array([DST[j], YD, 0])


class OT(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        self.add(line(TX["rule"], 28, WHITE, 5.3))
        self.add(T("▲ " + ("đống cát" if LANG == "vi" else "sand"), 28, SKY).move_to([-1.6, 3.7, 0]), T("● " + ("hố" if LANG == "vi" else "holes"), 28, PINK).move_to([1.6, 3.7, 0]))
        axs = Line([-4, YS, 0], [4, YS, 0], color=DIM, stroke_width=2); axd = Line([-4, YD, 0], [4, YD, 0], color=DIM, stroke_width=2)
        ds = VGroup(*[VGroup(Triangle(color=SKY, fill_opacity=1, stroke_width=0).scale(0.2).move_to(pS(i) + UP * 0.1)) for i in range(6)])
        dd = VGroup(*[Dot(pD(j), radius=0.14, color=PINK) for j in range(6)])
        self.play(Create(axs), Create(axd), FadeIn(ds), FadeIn(dd), run_time=1.0)

        def arrows(sg):
            return VGroup(*[Line(pS(i) + DOWN * 0.15, pD(sg[i]) + UP * 0.12, color=MINT if abs(i - sg[i]) == 0 else SUN, stroke_width=5) for i in range(6)])

        cur = arrows(seq[0])
        cost_t = lambda sg: T("%s: %s" % (tr(TX["cost"]), nf(cost(sg), 1)), 36, WHITE).move_to([0, -1.5, 0])
        ct = cost_t(seq[0])
        self.play(Create(cur), FadeIn(ct), run_time=1.2)
        self.wait(1.0)
        sw = line(TX["swap"], 28, ORANGE, -2.5)
        self.play(FadeIn(sw), run_time=0.5)
        for s_ in seq[1:]:
            na, nc = arrows(s_), cost_t(s_)
            self.play(Transform(cur, na), Transform(ct, nc), run_time=1.2)
            self.wait(0.5)
        self.play(FadeOut(sw), run_time=0.3)
        e1 = line(TX["end"], 32, MINT, -2.6)
        e2 = line(TX["end2"], 30, SUN, -3.5)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.5)
