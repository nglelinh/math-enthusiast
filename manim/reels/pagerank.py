from common_b import *

TX = {
    "title": {"vi": "PageRank: bước ngẫu nhiên\nvà ma trận chuyển", "en": "PageRank: random walks\nand transition matrices"},
    "graph": {"vi": "4 trang web: D là nút cụt\n(không có liên kết ra ngoài)", "en": "4 web pages: D is a dead end\n(no outgoing links)"},
    "stuck": {"vi": "Bước ngẫu nhiên thuần:\nA → B → D rồi kẹt tại D", "en": "Naive random walk:\nA → B → D, trapped at D"},
    "fix": {"vi": "Thêm teleport α = 0,85:\nπᵀ = πᵀ(αP + (1−α)veᵀ)", "en": "Add teleport α = 0.85:\nπᵀ = πᵀ(αP + (1−α)veᵀ)"},
    "iter": {"vi": "Lặp lũy thừa hội tụ về\nphân phối dừng duy nhất π", "en": "Power iteration converges to\na unique stationary π"},
    "end": {"vi": "Đổi cạnh hoặc α sẽ đổi hạng:\nđồ thị là một lựa chọn mô hình", "en": "Change edges or α, ranks shift:\nthe graph is a modeling choice"},
}

# Ma trận chuyển P (đã xử lý nút cụt D bằng phân phối đều 1/4)
P = np.array([
    [0.0,  0.5,  0.5,  0.0],   # A -> B, C
    [0.0,  0.0,  0.5,  0.5],   # B -> C, D
    [1.0,  0.0,  0.0,  0.0],   # C -> A
    [0.25, 0.25, 0.25, 0.25],  # D -> uniform teleport
], dtype=float)
alpha = 0.85
v = np.array([0.25, 0.25, 0.25, 0.25])
G = alpha * P + (1.0 - alpha) * np.outer(np.ones(4), v)
assert np.allclose(G.sum(axis=1), 1.0)

pi = v.copy()
history = [pi.copy()]
for _ in range(30):
    pi = pi @ G
    history.append(pi.copy())

assert abs(pi.sum() - 1.0) < 1e-12
assert np.linalg.norm(pi @ G - pi, 1) < 1e-10
# Kiểm tra thứ hạng: C > A > B > D
order = np.argsort(-pi)
assert list(order) == [0, 2, 1, 3], f"Unexpected order: {order}, pi={pi}"


class PageRank(Scene):
    def construct(self):
        self.add(line(TX["title"], 38, WHITE, 6.2))
        c1 = line(TX["graph"], 28, SKY, 4.9)
        self.play(FadeIn(c1), run_time=0.6)

        # Đồ thị 4 đỉnh A, B, C, D
        pos = {
            0: np.array([-2.2, 2.3, 0]),  # A
            1: np.array([ 2.2, 2.3, 0]),  # B
            2: np.array([ 0.0, 0.4, 0]),  # C
            3: np.array([ 2.5,-0.5, 0]),  # D (nút cụt)
        }
        names = ["A", "B", "C", "D"]
        nodes = VGroup()
        for i, nm in enumerate(names):
            col = PINK if i == 3 else SKY
            circ = Circle(0.45, color=col, fill_color=CARD, fill_opacity=1, stroke_width=3.5).move_to(pos[i])
            lbl = T(nm, 30, col).move_to(pos[i])
            nodes.add(VGroup(circ, lbl))

        edges_list = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 0)]
        arrows = VGroup()
        for u, w in edges_list:
            d = pos[w] - pos[u]
            d_unit = d / np.linalg.norm(d)
            start = pos[u] + d_unit * 0.52
            end = pos[w] - d_unit * 0.52
            if (u, w) in ((0, 2), (2, 0)):
                # dịch nhẹ để không đè lên nhau
                perp = np.array([-d_unit[1], d_unit[0], 0]) * 0.14
                start = start + perp
                end = end + perp
            arrows.add(Arrow(start, end, buff=0, stroke_width=3, color=DIM, max_tip_length_to_length_ratio=0.16))

        self.play(FadeIn(nodes), FadeIn(arrows), run_time=1.0)
        self.wait(1.0)

        # Bước ngẫu nhiên thuần bị kẹt tại D
        c2 = line(TX["stuck"], 28, PINK, -1.8)
        self.play(FadeIn(c2), run_time=0.5)
        walker = Dot(pos[0], radius=0.18, color=SUN)
        self.play(FadeIn(walker), run_time=0.3)
        self.play(walker.animate.move_to(pos[1]), run_time=0.7)
        self.play(walker.animate.move_to(pos[3]), run_time=0.7)
        ring = Circle(0.62, color=PINK, stroke_width=4).move_to(pos[3])
        self.play(Create(ring), run_time=0.5)
        self.wait(1.2)

        # Thêm teleport
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(ring), FadeOut(walker), run_time=0.5)
        c3 = line(TX["fix"], 28, SUN, 4.9)
        self.play(FadeIn(c3), run_time=0.6)
        tele = DashedLine(pos[3], pos[0], color=SUN, stroke_width=2.5)
        self.play(Create(tele), run_time=0.6)
        self.wait(0.8)

        # Biểu đồ cột hội tụ của pi
        c4 = line(TX["iter"], 28, MINT, -1.6)
        self.play(FadeIn(c4), run_time=0.5)
        base_y = -5.0
        max_h = 2.4
        xs = [-2.4, -0.8, 0.8, 2.4]
        bars = VGroup()
        val_txts = VGroup()
        bar_labels = VGroup()
        for i, nm in enumerate(names):
            h0 = (history[0][i] / 0.45) * max_h
            b = Rectangle(width=0.95, height=h0, fill_color=MINT if i == 0 else SKY, fill_opacity=0.85, stroke_width=0)
            b.move_to([xs[i], base_y + h0 / 2, 0])
            bars.add(b)
            vt = T(nf(history[0][i], 3), 24, WHITE).next_to(b, UP, buff=0.1)
            val_txts.add(vt)
            bar_labels.add(T(nm, 26, DIM).move_to([xs[i], base_y - 0.35, 0]))

        self.play(FadeIn(bars), FadeIn(val_txts), FadeIn(bar_labels), run_time=0.6)

        for step in (1, 3, 8, 30):
            anims = []
            for i in range(4):
                hi = (history[step][i] / 0.45) * max_h
                col = SUN if i == 0 else SKY
                nb = Rectangle(width=0.95, height=hi, fill_color=col, fill_opacity=0.9, stroke_width=0)
                nb.move_to([xs[i], base_y + hi / 2, 0])
                nt = T(nf(history[step][i], 3), 24, SUN if i == 0 else WHITE).next_to(nb, UP, buff=0.1)
                anims.append(Transform(bars[i], nb))
                anims.append(Transform(val_txts[i], nt))
            self.play(*anims, run_time=0.65)
            self.wait(0.3)

        self.wait(1.0)
        end_c = line(TX["end"], 28, WHITE, -6.1)
        self.play(FadeIn(end_c), run_time=0.6)
        self.wait(2.5)
