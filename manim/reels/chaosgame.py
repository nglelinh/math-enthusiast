from common import *
import random

TX = {
    "title": {"vi": "Trò chơi hỗn độn", "en": "The chaos game"},
    "rule": {"vi": "Chọn đỉnh ngẫu nhiên, nhảy nửa đường", "en": "Pick a random corner, jump halfway"},
    "rule2": {"vi": "Rồi lặp lại, lặp lại…", "en": "Then repeat, and repeat…"},
    "end": {"vi": "Ngẫu nhiên mà ra hình chính xác", "en": "Pure chance, an exact fractal"},
    "dim": {"vi": "Tam giác Sierpiński: chiều ≈ 1,585", "en": "Sierpiński triangle: dimension ≈ 1.585"},
}
import math
assert abs(math.log(3) / math.log(2) - 1.585) < 1e-3
random.seed(7)
S = 7.2
H = S * math.sqrt(3) / 2
V = [np.array([0, 1.8 + H / 2, 0]), np.array([-S / 2, 1.8 - H / 2, 0]), np.array([S / 2, 1.8 - H / 2, 0])]
COL = [SKY, PINK, MINT]
P0 = V[0] * 0.3 + V[1] * 0.3 + V[2] * 0.4
pts, choice = [], []
p = P0.copy()
for _ in range(6000):
    i = random.randrange(3)
    p = (p + V[i]) / 2
    pts.append(p.copy()); choice.append(i)


class ChaosGame(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        r1 = fit(T(tr(TX["rule"]), 30, WHITE)).move_to([0, 5.2, 0])
        self.play(FadeIn(r1), run_time=0.8)
        vd = VGroup(*[Dot(v, radius=0.16, color=COL[i]) for i, v in enumerate(V)])
        self.play(FadeIn(vd), run_time=0.6)
        cur = Dot(P0, radius=0.09, color=WHITE)
        self.play(FadeIn(cur), run_time=0.4)
        trail = VGroup()
        p = P0.copy()
        for k in range(10):
            q = pts[k]
            ln = DashedLine(p, V[choice[k]], color=COL[choice[k]], stroke_width=3, dash_length=0.1)
            nd = Dot(q, radius=0.05, color=COL[choice[k]])
            self.play(Create(ln), run_time=0.22)
            self.play(cur.animate.move_to(q), FadeOut(ln), run_time=0.22)
            self.add(nd)
            trail.add(nd)
            p = q
        r2 = fit(T(tr(TX["rule2"]), 30, SUN)).move_to([0, 5.2, 0])
        self.play(ReplacementTransform(r1, r2), run_time=0.5)
        cnt = T("n = 10", 34, DIM).move_to([0, -3.1, 0])
        self.add(cnt)
        done = 10
        for size in [10, 20, 40, 80, 150, 300, 500, 800, 1200, 1500, 1500, 1500]:
            batch = VGroup(*[Dot(pts[j], radius=0.022, color=COL[choice[j]]) for j in range(done, min(done + size, len(pts)))])
            self.add(batch)
            done += size
            self.remove(cnt)
            cnt = T("n = %d" % done, 34, DIM).move_to([0, -3.1, 0])
            self.add(cnt)
            self.wait(0.45 if size < 500 else 0.6)
        self.remove(cur)
        e = fit(T(tr(TX["end"]), 38, SUN)).move_to([0, -4.3, 0])
        self.play(FadeOut(r2), run_time=0.3)
        self.play(FadeIn(e), run_time=0.6)
        dm = fit(T(tr(TX["dim"]), 30, MINT)).move_to([0, -5.2, 0])
        self.play(FadeIn(dm), run_time=0.6)
        self.wait(3.5)
