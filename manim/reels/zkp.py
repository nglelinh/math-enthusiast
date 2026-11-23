from common_b import *

TX = {
    "title": {"vi": "Chứng minh không tiết lộ:\n3-tô màu đồ thị", "en": "Zero-knowledge proof:\nGraph 3-coloring"},
    "secret": {"vi": "Peggy biết cách 3-tô màu\nnhưng không muốn lộ cho Victor", "en": "Peggy knows a 3-coloring\nbut hides it from Victor"},
    "commit": {"vi": "1. Hoán vị ngẫu nhiên 3 màu\nvà khóa kín cả 5 đỉnh", "en": "1. Randomly permute 3 colors\nand lock all 5 vertices"},
    "open": {"vi": "2. Victor chọn 1 cạnh bất kỳ;\nPeggy chỉ mở 2 đầu cạnh đó", "en": "2. Victor picks one edge;\nPeggy opens only its 2 ends"},
    "sound": {"vi": "Đồ thị 7 cạnh: kẻ gian bị bắt\nmỗi vòng ≥ 1/7; 20 vòng ⇒ > 95%", "en": "7 edges: cheater caught\n≥ 1/7 per round; 20 rounds ⇒ > 95%"},
    "end": {"vi": "Đủ 3 tính chất: Đầy đủ (Completeness),\nTin cậy (Soundness), Không tiết lộ (ZK)", "en": "Completeness, Soundness,\nand Zero-Knowledge (Simulator)"},
}

edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (0, 3)]
coloring = [0, 1, 2, 2, 0]  # 0: PINK, 1: SKY, 2: SUN
assert all(coloring[u] != coloring[v] for u, v in edges)
m = len(edges)
p_escape_20 = (1.0 - 1.0 / m) ** 20
p_catch_20 = 1.0 - p_escape_20
assert p_catch_20 > 0.95 and m == 7


class ZKP(Scene):
    def construct(self):
        self.add(line(TX["title"], 38, WHITE, 6.2))
        c1 = line(TX["secret"], 28, SKY, 4.9)
        self.play(FadeIn(c1), run_time=0.6)

        pts = [
            np.array([ 0.0,  2.7, 0]),  # 0
            np.array([-2.2,  1.2, 0]),  # 1
            np.array([ 2.2,  1.2, 0]),  # 2
            np.array([-1.5, -0.9, 0]),  # 3
            np.array([ 1.5, -0.9, 0]),  # 4
        ]
        palette = [PINK, SKY, SUN]
        perm_palette = [SUN, PINK, SKY]  # hoán vị ngẫu nhiên

        edge_lines = VGroup(*[Line(pts[u], pts[v], color=DIM, stroke_width=3.5) for u, v in edges])
        nodes = VGroup()
        for i, p in enumerate(pts):
            col = palette[coloring[i]]
            circ = Circle(0.42, color=col, fill_color=col, fill_opacity=0.9, stroke_width=3.5).move_to(p)
            lbl = T(str(i + 1), 26, BLACK).move_to(p)
            nodes.add(VGroup(circ, lbl))

        self.play(Create(edge_lines), FadeIn(nodes), run_time=1.0)
        self.wait(1.0)

        # Bước 1: Hoán vị & khóa kín
        self.play(FadeOut(c1), run_time=0.4)
        c2 = line(TX["commit"], 28, SUN, 4.9)
        self.play(FadeIn(c2), run_time=0.5)
        self.play(*[
            nodes[i][0].animate.set_fill(CARD, opacity=1).set_stroke(DIM)
            for i in range(5)
        ], *[nodes[i][1].animate.set_color(DIM) for i in range(5)], run_time=0.8)
        self.wait(0.8)

        # Bước 2: Victor chọn cạnh (1, 3) -> mở 2 đỉnh 1 và 3
        c3 = line(TX["open"], 28, MINT, -2.3)
        self.play(FadeIn(c3), run_time=0.5)
        hi_edge = Line(pts[1], pts[3], color=MINT, stroke_width=7)
        self.play(Create(hi_edge), run_time=0.5)

        for idx in (1, 3):
            col = perm_palette[coloring[idx]]
            self.play(
                nodes[idx][0].animate.set_fill(col, opacity=0.95).set_stroke(col),
                nodes[idx][1].animate.set_color(BLACK),
                run_time=0.5,
            )
        self.wait(1.0)

        # Bước 3: Soundness & Tổng kết
        c4 = line(TX["sound"], 26, PINK, -3.9)
        self.play(FadeIn(c4), run_time=0.6)
        self.wait(1.2)
        end_c = line(TX["end"], 26, WHITE, -5.5)
        self.play(FadeIn(end_c), run_time=0.6)
        self.wait(2.5)
