from common_b import *
import numpy as np

TX = {
    "title": {"vi": "Cặp số nguyên tố sinh đôi", "en": "Twin primes"},
    "grid": {"vi": "Số nguyên tố ≤ 100;\ncặp sinh đôi (p, p+2) tô hồng", "en": "Primes ≤ 100;\ntwin pairs (p, p+2) in pink"},
    "cnt": {"vi": "8 cặp sinh đôi ≤ 100", "en": "8 twin pairs ≤ 100"},
    "t2": {"vi": "Đếm cặp sinh đôi ≤ x", "en": "Counting twin pairs ≤ x"},
    "real": {"vi": "Đếm thật", "en": "Actual count"},
    "pred": {"vi": "Dự đoán Hardy–Littlewood", "en": "Hardy–Littlewood prediction"},
    "x": {"vi": "x", "en": "x"},
    "end": {"vi": "Dự đoán khớp số liệu tới 10⁶ …", "en": "The prediction fits the data up to 10⁶ …"},
    "end2": {"vi": "… nhưng chưa ai chứng minh\ncó vô hạn cặp", "en": "… yet nobody has proved there\nare infinitely many"},
}
N = 10 ** 6
sv = np.ones(N + 3, dtype=bool); sv[:2] = False
for i in range(2, int(N ** 0.5) + 2):
    if sv[i]: sv[i * i::i] = False
tw = sv[:-2] & sv[2:N + 1 + 0] if False else None
isp = sv
pairs = np.zeros(N + 1, dtype=np.int64)
for p in range(3, N - 1):
    pass
idx = np.nonzero(isp[:N - 1] & isp[2:N + 1])[0]            # p với p, p+2 nguyên tố, p+2 ≤ N
C2 = 0.6601618158468696
ts = np.linspace(2, N, 2000001)
integrand = 1 / np.log(ts) ** 2
cum = np.concatenate([[0], np.cumsum((integrand[1:] + integrand[:-1]) / 2 * (ts[1] - ts[0]))])


def actual(x): return int(np.searchsorted(idx + 2, x, side="right"))


def pred(x): return 2 * C2 * float(np.interp(x, ts, cum))


prm100 = [n for n in range(2, 101) if isp[n]]
twp = [(p, p + 2) for p in prm100 if isp[p + 2] and p + 2 <= 100]
assert len(twp) == 8 and twp[0] == (3, 5) and twp[-1] == (71, 73)
assert [actual(10 ** k) for k in (2, 3, 4, 5, 6)] == [8, 35, 205, 1224, 8169]
for k in (4, 5, 6):
    assert abs(pred(10 ** k) / actual(10 ** k) - 1) < 0.05, (k, pred(10 ** k))
XS = np.unique(np.round(10 ** np.linspace(2, 6, 60)).astype(int))
A = [actual(x) for x in XS]
Pd = [pred(x) for x in XS]


class Twins(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        g = line(TX["grid"], 28, DIM, 5.3)
        self.play(FadeIn(g), run_time=0.6)
        cell = 0.62
        cells, numbers = VGroup(), VGroup()
        tw_set = {n for pr_ in twp for n in pr_}
        for n in range(1, 101):
            r, c = divmod(n - 1, 10)
            pos = np.array([(c - 4.5) * cell, 3.3 - r * cell + 0.0, 0])
            isprime = bool(isp[n]) if n > 1 else False
            col = PINK if n in tw_set else (SKY if isprime else CARD)
            sq = Square(cell * 0.9, stroke_width=0, fill_color=col, fill_opacity=0.95 if isprime else 0.5).move_to(pos)
            cells.add(sq)
            numbers.add(T(str(n), 17, BLACK if isprime else DIM).move_to(pos))
        self.play(FadeIn(cells, lag_ratio=0.01), FadeIn(numbers, lag_ratio=0.01), run_time=2.0)
        c1 = line(TX["cnt"], 34, PINK, -3.45)
        self.play(FadeIn(c1), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(cells), FadeOut(numbers), FadeOut(g), FadeOut(c1), run_time=0.6)
        t2 = line(TX["t2"], 32, WHITE, 5.4)
        self.play(FadeIn(t2), run_time=0.5)
        ax, lab = mkaxes([2, 6, 1], [0, 4, 1], 6.6, 6.0, [0.4, 1.4, 0], xt=(2, 3, 4, 5, 6),
                         yt=[(v, "10^%d" % v if v > 0 else "1") for v in (0, 1, 2, 3, 4)], xfmt=lambda v: "10^%d" % v)
        # đơn giản hoá nhãn: dùng chỉ số trên unicode
        sup = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶"}
        lab = VGroup()
        for v in (2, 3, 4, 5, 6):
            lab.add(T("10" + sup[str(v)], 22, DIM).next_to(ax.c2p(v, 0), DOWN, buff=0.12))
        for v in (0, 1, 2, 3, 4):
            lab.add(T("10" + sup[str(v)] if v else "1", 22, DIM).next_to(ax.c2p(2, v), LEFT, buff=0.12))
        self.play(Create(ax), FadeIn(lab), run_time=0.9)
        lg1 = T(tr(TX["real"]), 28, PINK).move_to([-1.9, -3.3, 0])
        lg2 = fit(T(tr(TX["pred"]), 26, SKY), 4.6).move_to([1.8, -3.3, 0])
        self.play(FadeIn(lg1), FadeIn(lg2), run_time=0.5)
        pts = [(math.log10(x), math.log10(max(a, 1))) for x, a in zip(XS, A)]
        pp = [(math.log10(x), math.log10(p)) for x, p in zip(XS, Pd)]
        curve = VMobject(color=SKY, stroke_width=5).set_points_as_corners([ax.c2p(*q) for q in pp])
        dots = VGroup(*[Dot(ax.c2p(*q), radius=0.06, color=PINK) for q in pts])
        self.play(Create(curve), run_time=2.5)
        self.play(FadeIn(dots, lag_ratio=0.05), run_time=3.5)
        rows = VGroup()
        for k in (4, 6):
            rows.add(T("x = 10%s :  %s  vs  %s" % ("⁴" if k == 4 else "⁶", "{:,}".format(actual(10 ** k)).replace(",", "." if LANG == "vi" else ","),
                                                  "{:,}".format(round(pred(10 ** k))).replace(",", "." if LANG == "vi" else ",")), 28, WHITE))
        rows.arrange(DOWN, buff=0.15).move_to([0, -4.1, 0])
        self.play(FadeIn(rows), run_time=0.6)
        e1 = line(TX["end"], 28, MINT, -4.95)
        e2 = line(TX["end2"], 28, SUN, -5.75)
        self.play(FadeIn(e1), run_time=0.5)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(3.0)
