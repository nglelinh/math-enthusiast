from common_b import *

TX = {
    "title": {"vi": "Tô màu bản đồ:\nBốn màu và số Heawood", "en": "Map coloring:\nFour colors & Heawood"},
    "k4": {"vi": "4 nước đôi một chung biên\n⇒ đồ thị đối ngẫu là K₄", "en": "4 mutually adjacent regions\n⇒ dual graph is K₄"},
    "fail3": {"vi": "3 màu không đủ: đỉnh thứ 4\nkề cả Đỏ, Xanh, Vàng ⇒ cần màu 4", "en": "3 colors fail: the 4th vertex\ntouches all 3 ⇒ needs color 4"},
    "euler": {"vi": "Đồ thị phẳng: e ≤ 3v − 6\n⇒ luôn có đỉnh bậc ≤ 5", "en": "Planar graphs: e ≤ 3v − 6\n⇒ always a vertex of deg ≤ 5"},
    "five": {"vi": "Định lý 5 màu: bỏ đỉnh bậc ≤ 5,\ndùng xích Kempe giải phóng 1 màu", "en": "5-color theorem: remove deg ≤ 5,\nKempe chain frees one color"},
    "heawood": {"vi": "Trên mặt có giống g (xuyến g = 1):\nH(g) = ⌊(7 + √(1 + 48g)) / 2⌋", "en": "On a genus-g surface (torus g = 1):\nH(g) = ⌊(7 + √(1 + 48g)) / 2⌋"},
    "end": {"vi": "Mặt phẳng: 4 màu (Appel–Haken 1976)\nMặt xuyến: cần tới 7 màu", "en": "Plane: 4 colors (Appel–Haken 1976)\nTorus: up to 7 colors needed"},
}

# Kiểm tra toán học: cạnh tối đa K4 và công thức Heawood
v_k4, e_k4 = 4, 6
assert e_k4 == 3 * v_k4 - 6
H = lambda g: math.floor((7 + math.sqrt(1 + 48 * g)) / 2)
assert H(0) == 4 and H(1) == 7 and H(2) == 8


class FourColor(Scene):
    def construct(self):
        self.add(line(TX["title"], 38, WHITE, 6.2))
        c1 = line(TX["k4"], 28, SKY, 4.9)
        self.play(FadeIn(c1), run_time=0.6)

        # Vẽ K4: 3 đỉnh ngoài + 1 đỉnh tâm
        pts = [
            np.array([0.0, 2.7, 0]),
            np.array([-2.2, -0.3, 0]),
            np.array([2.2, -0.3, 0]),
            np.array([0.0, 0.85, 0]),
        ]
        edges = VGroup()
        for i in range(4):
            for j in range(i + 1, 4):
                edges.add(Line(pts[i], pts[j], color=DIM, stroke_width=3.5))

        nodes = VGroup()
        for i, p in enumerate(pts):
            circ = Circle(0.4, color=WHITE, fill_color=CARD, fill_opacity=1, stroke_width=3.5).move_to(p)
            lbl = T(str(i + 1), 26, WHITE).move_to(p)
            nodes.add(VGroup(circ, lbl))

        self.play(Create(edges), FadeIn(nodes), run_time=1.0)
        self.wait(0.8)

        # Tô màu từng đỉnh của K4
        c2 = line(TX["fail3"], 28, PINK, -1.6)
        self.play(FadeIn(c2), run_time=0.5)
        cols = [PINK, SKY, SUN, MINT]
        for i in range(4):
            self.play(nodes[i][0].animate.set_fill(cols[i], opacity=0.9).set_stroke(cols[i]),
                      nodes[i][1].animate.set_color(BLACK), run_time=0.55)
        self.wait(1.3)

        # Chuyển sang Euler + Định lý 5 màu + Heawood
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(edges), FadeOut(nodes), run_time=0.5)
        c3 = line(TX["euler"], 30, SUN, 4.4)
        self.play(FadeIn(c3), run_time=0.6)
        c4 = line(TX["five"], 28, MINT, 2.7)
        self.play(FadeIn(c4), run_time=0.6)
        self.wait(1.4)

        # Bảng số Heawood H(g)
        c5 = line(TX["heawood"], 28, SKY, 0.7)
        self.play(FadeIn(c5), run_time=0.6)

        rows = VGroup()
        for idx, g in enumerate((0, 1, 2)):
            y = -1.0 - idx * 1.05
            box = RoundedRectangle(corner_radius=0.12, width=6.8, height=0.82,
                                   fill_color=CARD, fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([0, y, 0])
            txt = T(f"g = {g}   ⇒   H({g}) = {H(g)}", 28, SUN if g == 1 else WHITE).move_to([0, y, 0])
            rows.add(VGroup(box, txt))
        self.play(FadeIn(rows, lag_ratio=0.15), run_time=1.0)
        self.wait(1.2)

        end_c = line(TX["end"], 28, WHITE, -5.2)
        self.play(FadeIn(end_c), run_time=0.6)
        self.wait(2.5)
