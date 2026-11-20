from common_b import *
import itertools

TX = {
    "title": {"vi": "Trò chơi CHSH: vượt giới hạn 2", "en": "The CHSH game: beating the limit 2"},
    "cl": {"vi": "Cổ điển: 16 chiến lược xác định\nS = A₀B₀ + A₀B₁ + A₁B₀ − A₁B₁", "en": "Classical: 16 fixed strategies\nS = A₀B₀ + A₀B₁ + A₁B₀ − A₁B₁"},
    "cl2": {"vi": "Mọi chiến lược cho |S| = 2\n⇒ trung bình không vượt 2", "en": "Every strategy gives |S| = 2\n⇒ averages never exceed 2"},
    "q": {"vi": "Cặp vướng víu, bốn hướng đo\n(An: xanh, Bình: hồng)", "en": "Entangled pair, four angles\n(Alice: blue, Bob: pink)"},
    "sum": {"vi": "S = 4 × 0,71", "en": "S = 4 × 0.71"},
    "bar": {"vi": "giới hạn cổ điển", "en": "classical limit"},
    "end": {"vi": "Lượng tử dự đoán S = 2√2 ≈ 2,83", "en": "Quantum theory predicts S = 2√2 ≈ 2.83"},
    "end2": {"vi": "Các thí nghiệm Bell đo được S > 2", "en": "Bell experiments measure S > 2"},
}
vals = []
for a0, a1, b0, b1 in itertools.product((1, -1), repeat=4):
    vals.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
assert len(vals) == 16 and all(abs(v) == 2 for v in vals) and sum(1 for v in vals if v == 2) == 8
deg = lambda d: math.radians(d)
a, a_, b, b_ = 0, 90, 45, -45
E = lambda x, y: math.cos(deg(x - y))
S = E(a, b) + E(a, b_) + E(a_, b) - E(a_, b_)
assert abs(S - 2 * math.sqrt(2)) < 1e-12 and abs(E(a_, b_) + math.sqrt(2) / 2) < 1e-12
# kiểm tra bằng trạng thái Φ⁺: E(θa, θb) = <Φ⁺| A⊗B |Φ⁺> với A = cosθ Z + sinθ X
import numpy as np
Z = np.array([[1, 0], [0, -1]]); X = np.array([[0, 1], [1, 0]])
phi = np.array([1, 0, 0, 1]) / math.sqrt(2)
M = lambda t: math.cos(deg(t)) * Z + math.sin(deg(t)) * X
Eq = lambda x, y: float(phi @ np.kron(M(x), M(y)) @ phi)
Sq = Eq(a, b) + Eq(a, b_) + Eq(a_, b) - Eq(a_, b_)
assert abs(Sq - 2 * math.sqrt(2)) < 1e-12


class CHSH(Scene):
    def construct(self):
        self.add(line(TX["title"], 38, WHITE, 6.4))
        c1 = line(TX["cl"], 28, SKY, 5.55)
        self.play(FadeIn(c1), run_time=0.6)
        grid = VGroup()
        for k, v in enumerate(vals):
            r, c = divmod(k, 8)
            sq = Square(0.8, stroke_width=0, fill_color=CARD, fill_opacity=1).move_to([(c - 3.5) * 0.9, 4.0 - r * 0.9, 0])
            grid.add(VGroup(sq, T(("+%d" if v > 0 else "−%d") % abs(v), 30, MINT if v > 0 else PINK).move_to(sq)))
        self.play(FadeIn(grid, lag_ratio=0.05), run_time=1.6)
        c2 = line(TX["cl2"], 28, WHITE, 2.1)
        self.play(FadeIn(c2), run_time=0.6)
        self.wait(1.2)
        q = line(TX["q"], 28, SUN, 0.75)
        self.play(FadeIn(q), run_time=0.6)
        cen = np.array([0, -1.8, 0]); R = 1.3
        circ = Circle(radius=R, color=DIM, stroke_width=3).move_to(cen)
        self.play(Create(circ), run_time=0.6)
        def arrow(d, col, lbl):
            v = np.array([math.cos(deg(d)), math.sin(deg(d)), 0])
            ar = Arrow(cen, cen + v * R, buff=0, color=col, stroke_width=7, max_tip_length_to_length_ratio=0.18)
            t = T(lbl, 26, col).move_to(cen + v * (R + 0.5))
            return VGroup(ar, t)
        arrows = [arrow(a, SKY, "0°"), arrow(a_, SKY, "90°"), arrow(b, PINK, "45°"), arrow(b_, PINK, "−45°")]
        for ar in arrows:
            self.play(FadeIn(ar), run_time=0.5)
        self.wait(0.4)
        sm = line(TX["sum"], 34, WHITE, -2.9)
        eqs = T("E = cos(Δ):  +0,71  +0,71  +0,71  −(−0,71)" if LANG == "vi" else "E = cos(Δ):  +0.71  +0.71  +0.71  −(−0.71)", 28, DIM).move_to([0, -3.5, 0])
        self.play(FadeIn(eqs), run_time=0.6)
        self.play(FadeIn(sm.move_to([0, -4.1, 0])), run_time=0.6)
        # thanh S
        x0, x1 = -3.5, 3.5
        sc = lambda v: x0 + (x1 - x0) * v / 3.0
        bar = Line([x0, -4.95, 0], [x1, -4.95, 0], color=DIM, stroke_width=4)
        tick2 = Line([sc(2), -4.75, 0], [sc(2), -5.15, 0], color=ORANGE, stroke_width=5)
        t2 = fit(T(tr(TX["bar"]), 22, ORANGE), 3.2).move_to([sc(2) - 1.0, -5.4, 0])
        fill = Line([x0, -4.95, 0], [x0, -4.95, 0], color=MINT, stroke_width=14)
        self.play(Create(bar), Create(tick2), FadeIn(t2), run_time=0.6)
        self.play(fill.animate.put_start_and_end_on([x0, -4.95, 0], [sc(S), -4.95, 0]), run_time=1.8)
        lab = T(nf(S, 2), 30, MINT).move_to([sc(S) + 0.1, -4.55, 0])
        self.play(FadeIn(lab), run_time=0.4)
        e1 = line(TX["end"], 30, MINT, -5.9)
        e2 = line(TX["end2"], 28, SUN, -6.5)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(3.2)
