from common_b import *
import numpy as np

TX = {
    "title": {"vi": "Đường cong Hilbert", "en": "The Hilbert curve"},
    "ord": {"vi": "Bậc", "en": "Order"},
    "cells": {"vi": "ô", "en": "cells"},
    "len": {"vi": "độ dài ≈", "en": "length ≈"},
    "end": {"vi": "Mỗi bậc: dài gấp đôi, mịn gấp đôi", "en": "Each order: twice as long, twice as fine"},
    "end2": {"vi": "Giới hạn: một đường liên tục\nđi qua MỌI điểm của hình vuông", "en": "Limit: one continuous curve\nthrough EVERY point of the square"},
}
SUP = {1: "¹", 2: "²", 3: "³", 4: "⁴", 5: "⁵"}


def d2xy(n, d):
    x = y = 0; t = d; s = 1
    while s < n:
        rx = 1 & (t // 2); ry = 1 & (t ^ rx)
        if ry == 0:
            if rx == 1:
                x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        x += s * rx; y += s * ry; t //= 4; s *= 2
    return x, y


def curve(k):
    n = 2 ** k
    return [d2xy(n, d) for d in range(n * n)]


for k in range(1, 6):
    c = curve(k)
    assert len(set(c)) == 4 ** k
    assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(c, c[1:]))
    # bậc k+1 tinh chỉnh bậc k: ô bậc k+1 nằm trong ô bậc k cùng chỉ số (d // 4)
    if k > 1:
        c0 = curve(k - 1)
        assert all((c[d][0] // 2, c[d][1] // 2) == c0[d // 4] for d in range(4 ** k))
LEN = {k: (4 ** k - 1) / 2 ** k for k in range(1, 6)}
assert all(1.9 < LEN[k + 1] / LEN[k] <= 2.5 for k in range(1, 5)) and abs(LEN[5] - 31.96875) < 1e-9
SIDE = 6.4; CEN = np.array([0, 1.2, 0])


def build(k):
    c = curve(k); n = 2 ** k
    pts = [CEN + np.array([((x + 0.5) / n - 0.5) * SIDE, ((y + 0.5) / n - 0.5) * SIDE, 0]) for x, y in c]
    m = min(len(pts) - 1, 48)
    per = (len(pts) - 1) / m
    cols = color_gradient([SKY, MINT, SUN, ORANGE, PINK], m)
    g = VGroup()
    for i in range(m):
        a, b = int(round(i * per)), int(round((i + 1) * per))
        g.add(VMobject(color=cols[i], stroke_width=7 if k < 4 else 5).set_points_as_corners(pts[a:b + 1]))
    return g


class Hilbert(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        sq = Square(SIDE + 0.5, color=DIM, stroke_width=3).move_to(CEN)
        self.play(Create(sq), run_time=0.7)
        cur, info = None, None
        for k, rt in zip(range(1, 6), (1.2, 1.5, 2.0, 2.6, 3.4)):
            new = build(k)
            ni = T("%s %d: 4%s = %d %s · %s %s" % (tr(TX["ord"]), k, SUP[k], 4 ** k, tr(TX["cells"]), tr(TX["len"]), nf(LEN[k], 2)), 28, WHITE).move_to([0, -3.1, 0])
            if cur is None:
                self.play(Create(new, lag_ratio=1.0, run_time=rt), FadeIn(ni), run_time=rt)
            else:
                self.play(FadeOut(cur), FadeOut(info), run_time=0.3)
                self.play(Create(new, lag_ratio=1.0, run_time=rt), FadeIn(ni), run_time=rt)
            cur, info = new, ni
            self.wait(0.5 if k < 5 else 0.2)
        e1 = line(TX["end"], 30, MINT, -4.2)
        e2 = line(TX["end2"], 30, SUN, -5.3)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.5)
