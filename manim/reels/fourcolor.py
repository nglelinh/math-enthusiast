from common_b import *
import json

TX = {
    "title": {"vi": "Tô màu bản đồ:\nBốn màu và số Heawood", "en": "Map coloring:\nFour colors & Heawood"},
    "s1_a": {"vi": "Mỗi bản đồ phẳng tương ứng\nvới một đồ thị đối ngẫu phẳng", "en": "Every planar map gives\na planar dual graph"},
    "s1_b": {"vi": "1 nước = 1 đỉnh; chung biên = 1 cạnh\nTô màu bản đồ ≡ tô màu đỉnh đồ thị", "en": "1 country = 1 vertex; shared border = 1 edge\nMap coloring ≡ vertex coloring"},
    "s2_a": {"vi": "Vì sao 3 màu không đủ?", "en": "Why do 3 colors fail?"},
    "s2_b": {"vi": "4 nước đôi một chung biên tạo ra K₄;\nđỉnh 4 chạm cả 3 màu ⇒ buộc dùng màu 4", "en": "4 mutually adjacent regions form K₄;\nvertex 4 touches all 3 ⇒ needs color 4"},
    "s3_a": {"vi": "Vì sao Định lý 5 màu lại gọn hơn?", "en": "Why is the 5-color theorem easier?"},
    "s3_b": {"vi": "Công thức Euler v − e + f = 2 và 2e ≥ 3f\n⇒ e ≤ 3v − 6 ⇒ luôn có đỉnh bậc ≤ 5", "en": "Euler v − e + f = 2 and 2e ≥ 3f\n⇒ e ≤ 3v − 6 ⇒ a vertex of deg ≤ 5 exists"},
    "s4_a": {"vi": "Xích Kempe: bỏ đỉnh u (bậc 5), tô G − u\nbằng 5 màu rồi giải phóng 1 màu cho u", "en": "Kempe chain: remove deg-5 u, 5-color G − u,\nthen free one color for u"},
    "s4_b": {"vi": "TH1: Thành phần Đỏ–Vàng từ 1 không tới 3\n⇒ đổi Đỏ ↔ Vàng để giải phóng Đỏ", "en": "Case 1: Red–Yellow chain misses 3\n⇒ swap Red ↔ Yellow to free Red"},
    "s4_c": {"vi": "TH2: Nếu nối tới 3, xích 1–3 tạo rào chắn\n⇒ đổi Xanh ↔ Lục trên thành phần của 2", "en": "Case 2: If it hits 3, it forms a barrier\n⇒ swap Blue ↔ Green on 2's side"},
    "s5_a": {"vi": "Bẫy lịch sử (1879): thử dùng xích Kempe\ncho 4 màu bị lỗi hai xích giao nhau (Heawood 1890)", "en": "Historical pitfall (1879): Kempe's 4-color\nproof broke on crossing chains (Heawood 1890)"},
    "s5_b": {"vi": "Trên mặt có giống g (xuyến g = 1):\nH(g) = ⌊(7 + √(1 + 48g)) / 2⌋", "en": "On a genus-g surface (torus g = 1):\nH(g) = ⌊(7 + √(1 + 48g)) / 2⌋"},
    "end": {"vi": "Mặt phẳng: 4 màu (Appel–Haken 1976)\nMặt xuyến: 7 màu  |  Đế quốc rời: vô hạn", "en": "Plane: 4 colors (Appel–Haken 1976)\nTorus: 7 colors  |  Disconnected: unbounded"},
}

v_k4, e_k4 = 4, 6
assert e_k4 == 3 * v_k4 - 6
H = lambda g: math.floor((7 + math.sqrt(1 + 48 * g)) / 2)
assert H(0) == 4 and H(1) == 7 and H(2) == 8


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class FourColor(Scene):
    def construct(self):
        vo_path = os.environ.get("VO_DUR_JSON", "")
        vo_durs = json.load(open(vo_path)) if vo_path and os.path.exists(vo_path) else {}
        timeline = []

        def start_vo(sid):
            t0 = float(self.time)
            timeline.append((sid, t0))
            return t0

        def end_vo(sid, t0, fallback):
            if sid in vo_durs:
                rem = vo_durs[sid] - (float(self.time) - t0) + 1.2
                self.wait(max(0.8, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 38, WHITE, 6.2)
        self.add(title)

        # --- Phần 1 ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 28, SKY, 4.6)
        s1b = line(TX["s1_b"], 26, WHITE, 3.0)
        self.play(FadeIn(s1a), run_time=0.8)
        self.wait(2.5)
        self.play(FadeIn(s1b), run_time=0.8)
        self.wait(2.5)
        r1 = Polygon([-2.5, 0.5, 0], [0, 0.5, 0], [0, -1.8, 0], [-2.5, -1.8, 0], color=SKY, fill_color=CARD, fill_opacity=0.8)
        r2 = Polygon([0, 0.5, 0], [2.5, 0.5, 0], [2.5, -1.8, 0], [0, -1.8, 0], color=PINK, fill_color=CARD, fill_opacity=0.8)
        r3 = Polygon([-2.5, -1.8, 0], [2.5, -1.8, 0], [2.5, -3.2, 0], [-2.5, -3.2, 0], color=SUN, fill_color=CARD, fill_opacity=0.8)
        self.play(Create(r1), Create(r2), Create(r3), run_time=1.2)
        self.wait(2.5)
        d1 = Dot([-1.25, -0.65, 0], radius=0.18, color=SKY)
        d2 = Dot([1.25, -0.65, 0], radius=0.18, color=PINK)
        d3 = Dot([0.0, -2.5, 0], radius=0.18, color=SUN)
        de = VGroup(Line(d1, d2, color=WHITE), Line(d2, d3, color=WHITE), Line(d1, d3, color=WHITE))
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(d3), Create(de), run_time=1.0)
        end_vo("s1", t0, 6.5)
        wipe(self, keep=[title])

        # --- Phần 2 ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 32, PINK, 4.8)
        self.play(FadeIn(s2a), run_time=0.7)
        pts = [
            np.array([0.0, 2.7, 0]),
            np.array([-2.2, -0.3, 0]),
            np.array([2.2, -0.3, 0]),
            np.array([0.0, 0.85, 0]),
        ]
        edges = VGroup(*[Line(pts[i], pts[j], color=DIM, stroke_width=3.5) for i in range(4) for j in range(i + 1, 4)])
        nodes = VGroup(*[
            VGroup(Circle(0.42, color=WHITE, fill_color=CARD, fill_opacity=1, stroke_width=3.5).move_to(p),
                   T(str(i + 1), 26, WHITE).move_to(p))
            for i, p in enumerate(pts)
        ])
        self.play(Create(edges), FadeIn(nodes), run_time=1.2)
        self.wait(2.5)
        cols = [PINK, SKY, SUN, MINT]
        for i in range(3):
            self.play(nodes[i][0].animate.set_fill(cols[i], opacity=0.9).set_stroke(cols[i]),
                      nodes[i][1].animate.set_color(BLACK), run_time=0.8)
            self.wait(1.0)
        s2b = line(TX["s2_b"], 26, WHITE, -2.2)
        self.play(FadeIn(s2b), run_time=0.8)
        self.wait(2.0)
        self.play(nodes[3][0].animate.set_fill(cols[3], opacity=0.95).set_stroke(cols[3]),
                  nodes[3][1].animate.set_color(BLACK), run_time=0.9)
        end_vo("s2", t0, 6.5)
        wipe(self, keep=[title])

        # --- Phần 3 ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 32, SUN, 4.7)
        s3b = line(TX["s3_b"], 26, WHITE, 2.9)
        self.play(FadeIn(s3a), run_time=0.7)
        self.wait(2.5)
        self.play(FadeIn(s3b), run_time=0.9)
        self.wait(4.5)
        e_box = RoundedRectangle(corner_radius=0.14, width=7.5, height=2.2,
                                 fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, -0.5, 0])
        e_txt = fit(VGroup(
            T("Bậc trung bình = 2e / v ≤ 6 − 12/v < 6" if LANG == "vi" else "Average degree = 2e / v ≤ 6 − 12/v < 6", 25, SUN),
            T("⇒ Luôn tồn tại đỉnh u với deg(u) ≤ 5" if LANG == "vi" else "⇒ A vertex u with deg(u) ≤ 5 must exist", 25, MINT),
        ).arrange(DOWN, buff=0.25), 6.8).move_to(e_box)
        self.play(FadeIn(e_box), FadeIn(e_txt), run_time=1.0)
        end_vo("s3", t0, 8.0)
        wipe(self, keep=[title])

        # --- Phần 4 ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 25, MINT, 4.7)
        self.play(FadeIn(s4a), run_time=0.8)
        cen = np.array([0, 0.7, 0])
        u_node = VGroup(Circle(0.38, color=WHITE, fill_color=CARD, fill_opacity=1, stroke_width=3).move_to(cen),
                        T("u", 26, WHITE).move_to(cen))
        nb_cols = [PINK, SKY, SUN, MINT, ORANGE]
        nb_nodes = VGroup()
        nb_lines = VGroup()
        nb_pts = []
        for k in range(5):
            ang = math.pi / 2 + k * 2 * math.pi / 5
            p = cen + np.array([2.15 * math.cos(ang), 2.15 * math.sin(ang), 0])
            nb_pts.append(p)
            nb_lines.add(DashedLine(cen, p, color=DIM, stroke_width=2.5))
            c = Circle(0.38, color=nb_cols[k], fill_color=nb_cols[k], fill_opacity=0.9, stroke_width=3).move_to(p)
            t = T(str(k + 1), 24, BLACK).move_to(p)
            nb_nodes.add(VGroup(c, t))
        self.play(Create(nb_lines), FadeIn(nb_nodes), FadeIn(u_node), run_time=1.2)
        self.wait(4.0)
        s4b = line(TX["s4_b"], 25, SUN, -2.9)
        self.play(FadeIn(s4b), run_time=0.8)
        self.wait(3.0)
        self.play(nb_nodes[0][0].animate.set_fill(SUN, opacity=0.9).set_stroke(SUN), run_time=1.0)
        self.wait(1.8)
        self.play(u_node[0].animate.set_fill(PINK, opacity=0.95).set_stroke(PINK),
                  u_node[1].animate.set_color(BLACK), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(s4b), run_time=0.4)
        self.play(nb_nodes[0][0].animate.set_fill(PINK, opacity=0.9).set_stroke(PINK),
                  u_node[0].animate.set_fill(CARD, opacity=1).set_stroke(WHITE),
                  u_node[1].animate.set_color(WHITE), run_time=0.6)
        barrier = ArcBetweenPoints(nb_pts[0], nb_pts[2], angle=-1.1, color=SUN, stroke_width=5)
        s4c = line(TX["s4_c"], 25, SKY, -2.9)
        self.play(Create(barrier), FadeIn(s4c), run_time=0.9)
        self.wait(2.5)
        self.play(nb_nodes[1][0].animate.set_fill(MINT, opacity=0.9).set_stroke(MINT), run_time=0.9)
        self.play(u_node[0].animate.set_fill(SKY, opacity=0.95).set_stroke(SKY),
                  u_node[1].animate.set_color(BLACK), run_time=0.9)
        end_vo("s4", t0, 6.0)
        wipe(self, keep=[title])

        # --- Phần 5 ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 25, PINK, 4.7)
        self.play(FadeIn(s5a), run_time=0.8)
        self.wait(6.5)
        s5b = line(TX["s5_b"], 26, SKY, 2.5)
        self.play(FadeIn(s5b), run_time=0.8)
        rows = VGroup()
        for idx, g in enumerate((0, 1, 2)):
            y = 0.2 - idx * 1.15
            box = RoundedRectangle(corner_radius=0.12, width=6.8, height=0.88,
                                   fill_color=CARD, fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([0, y, 0])
            txt = T(f"g = {g}   ⇒   H({g}) = {H(g)}", 28, SUN if g == 1 else WHITE).move_to([0, y, 0])
            rows.add(VGroup(box, txt))
        self.play(FadeIn(rows, lag_ratio=0.2), run_time=1.2)
        self.wait(6.0)
        end_c = line(TX["end"], 26, WHITE, -4.5)
        self.play(FadeIn(end_c), run_time=0.8)
        end_vo("s5", t0, 9.0)

        tl_out = os.environ.get("VO_TIMELINE_JSON", "")
        if tl_out:
            with open(tl_out, "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
