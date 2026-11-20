from common import *

TX = {
    "title": {"vi": "Bảy cây cầu Königsberg", "en": "The seven bridges of Königsberg"},
    "q": {"vi": "Đi qua mỗi cầu đúng một lần được không?", "en": "Cross every bridge exactly once?"},
    "model": {"vi": "Vùng đất là điểm, cây cầu là cạnh", "en": "Land = dot, bridge = edge"},
    "deg": {"vi": "Đếm số cầu ở mỗi điểm (bậc)", "en": "Count the bridges at each dot (degree)"},
    "rule": {"vi": "Cần 0 hoặc 2 điểm bậc lẻ", "en": "Need 0 or 2 dots of odd degree"},
    "have": {"vi": "Ở đây có 4 điểm bậc lẻ: 5, 3, 3, 3", "en": "Here: 4 odd dots: 5, 3, 3, 3"},
    "end": {"vi": "Không tồn tại đường đi (Euler, 1736)", "en": "No such walk exists (Euler, 1736)"},
}
POS = {"A": np.array([-1.9, 0.6, 0]), "N": np.array([0.0, 3.4, 0]), "S": np.array([0.0, -2.2, 0]), "D": np.array([2.5, 0.6, 0])}
EDGES = [("N", "A", 0.4), ("N", "A", -0.4), ("S", "A", -0.4), ("S", "A", 0.4), ("A", "D", 0.0), ("N", "D", 0.0), ("S", "D", 0.0)]
deg = {k: 0 for k in POS}
for a, b, _ in EDGES:
    deg[a] += 1; deg[b] += 1
assert len(EDGES) == 7 and deg == {"A": 5, "N": 3, "S": 3, "D": 3} and sum(deg.values()) == 14
assert sum(1 for v in deg.values() if v % 2) == 4


class Konigsberg(Scene):
    def construct(self):
        c = cap(TX["title"], 36)
        self.add(c)
        q = fit(T(tr(TX["q"]), 32, WHITE)).move_to([0, 5.2, 0])
        self.play(FadeIn(q), run_time=0.8)
        nodes = {k: Dot(p, radius=0.28, color=SKY) for k, p in POS.items()}
        self.play(*[FadeIn(n, scale=0.5) for n in nodes.values()], run_time=1.0)
        m = fit(T(tr(TX["model"]), 30, SUN)).move_to([0, 4.5, 0])
        self.play(ReplacementTransform(q, m), run_time=0.5)
        edges = []
        for a, b, ang in EDGES:
            e = ArcBetweenPoints(POS[a], POS[b], angle=ang * 2, color=ORANGE, stroke_width=6) if ang else Line(POS[a], POS[b], color=ORANGE, stroke_width=6)
            edges.append(e)
        cnt = T("0 / 7", 34, DIM).move_to([0, -3.5, 0])
        self.add(cnt)
        for i, e in enumerate(edges):
            self.play(Create(e), run_time=0.5)
            n2 = T("%d / 7" % (i + 1), 34, DIM).move_to([0, -3.5, 0])
            self.remove(cnt); self.add(n2); cnt = n2
        self.add_foreground_mobjects(*nodes.values()) if hasattr(self, "add_foreground_mobjects") else None
        self.wait(0.6)
        d = fit(T(tr(TX["deg"]), 30, SUN)).move_to([0, 4.5, 0])
        self.play(ReplacementTransform(m, d), FadeOut(cnt), run_time=0.5)
        offs = {"A": np.array([-0.0, 0.65, 0]), "N": np.array([0.7, 0.2, 0]), "S": np.array([0.7, -0.2, 0]), "D": np.array([0.0, 0.65, 0])}
        degl = {k: T(str(deg[k]), 48, WHITE).move_to(POS[k] + offs[k]) for k in POS}
        self.play(LaggedStart(*[FadeIn(l, scale=1.4) for l in degl.values()], lag_ratio=0.35), run_time=2.0)
        self.play(*[nodes[k].animate.set_color(PINK) for k in POS], *[degl[k].animate.set_color(PINK) for k in POS], run_time=0.8)
        self.wait(0.6)
        r = fit(T(tr(TX["rule"]), 34, MINT)).move_to([0, -3.7, 0])
        self.play(FadeIn(r), run_time=0.6)
        self.wait(1.2)
        h = fit(T(tr(TX["have"]), 30, PINK)).move_to([0, -4.6, 0])
        self.play(FadeIn(h), run_time=0.6)
        self.wait(1.2)
        e = fit(T(tr(TX["end"]), 34, SUN)).move_to([0, -5.6, 0])
        self.play(FadeIn(e), run_time=0.6)
        self.wait(3.5)
