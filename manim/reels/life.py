from common_b import *
import numpy as np
from collections import Counter

TX = {
    "title": {"vi": "Game of Life: 5 ô và một quy tắc", "en": "Game of Life: 5 cells, one rule"},
    "rule": {"vi": "Ô sống giữ lại nếu có 2–3 hàng xóm sống;\nô chết sống lại nếu có đúng 3 hàng xóm", "en": "A live cell survives with 2–3 live neighbours;\na dead cell is born with exactly 3"},
    "gen": {"vi": "Thế hệ", "en": "Generation"},
    "pop": {"vi": "ô sống", "en": "live cells"},
    "end": {"vi": "Thế hệ 1103: ổn định ở 116 ô,\ntrong đó có 6 tàu lượn bay đi", "en": "Generation 1103: settles at 116 cells,\nincluding 6 gliders flying away"},
    "end2": {"vi": "Quy tắc cục bộ, hành vi toàn cục", "en": "Local rules, global behaviour"},
}


def step(s):
    c = Counter((x + dx, y + dy) for x, y in s for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy)
    return {k for k, v in c.items() if v == 3 or (v == 2 and k in s)}


GEN = 260
gens = [{(1, 0), (2, 0), (0, 1), (1, 1), (1, 2)}]
for _ in range(1110):
    gens.append(step(gens[-1]))
assert len(gens[0]) == 5 and all(len(gens[g]) == 116 for g in range(1103, 1111)) and len(gens[1102]) != 116
CX, CY = 3, 4
HW = [0]
for g in range(GEN + 1):
    ext = max(max(abs(x - CX), abs(y - CY)) for x, y in gens[g]) + 3
    HW.append(max(HW[-1], 8, ext))
HW = HW[1:]
assert HW[-1] <= 56
BG = np.array([22, 25, 36], dtype=np.uint8); LIVE = np.array([128, 237, 153], dtype=np.uint8); NEW = np.array([255, 209, 102], dtype=np.uint8)


def frame(g):
    h = HW[g]; n = 2 * h
    a = np.zeros((n, n, 3), dtype=np.uint8); a[:] = BG
    prev = gens[g - 1] if g else set()
    for (x, y) in gens[g]:
        i, j = x - CX + h, y - CY + h
        if 0 <= i < n and 0 <= j < n:
            a[n - 1 - j, i] = NEW if (x, y) not in prev and g else LIVE
    idx = (np.arange(448) * n) // 448
    return a[idx[:, None], idx[None, :]]


class Life(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        self.add(line(TX["rule"], 26, DIM, 5.45, 7.9))
        tk = ValueTracker(0)
        G = lambda: int(round(tk.get_value()))
        SZ = 7.0
        img = always_redraw(lambda: ImageMobject(frame(G())).set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"]).scale_to_fit_width(SZ).move_to([0, 1.5, 0]))
        border = Square(SZ + 0.05, color=DIM, stroke_width=3).move_to([0, 1.5, 0])
        cnt = always_redraw(lambda: T("%s %d     %d %s" % (tr(TX["gen"]), G(), len(gens[G()]), tr(TX["pop"])), 34, WHITE).move_to([0, -2.4, 0]))
        self.add(img, border, cnt)
        self.wait(1.5)
        self.play(tk.animate.set_value(GEN), run_time=13.0, rate_func=linear)
        self.wait(0.5)
        e1 = line(TX["end"], 30, MINT, -3.6)
        e2 = line(TX["end2"], 36, SUN, -4.8)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.5)
