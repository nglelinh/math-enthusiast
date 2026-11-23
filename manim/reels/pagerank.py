from common_b import *
import json

TX = {
    "title": {"vi": "PageRank: bước ngẫu nhiên\nvà ma trận chuyển", "en": "PageRank: random walks\nand transition matrices"},
    "s1_a": {"vi": "Làm sao xếp hạng tầm quan trọng\ncủa một trang web?", "en": "How do we rank the importance\nof a web page?"},
    "s1_b": {"vi": "Đếm số liên kết trỏ tới dễ bị gian lận;\nliên kết từ trang quan trọng phải nặng ký hơn", "en": "Counting in-links is easy to game;\nlinks from key pages should count more"},
    "s2_a": {"vi": "Xét 4 trang web A, B, C, D\nvới D là nút cụt (0 liên kết ra)", "en": "Consider 4 pages A, B, C, D\nwhere D is a dead end (0 out-links)"},
    "s2_b": {"vi": "Ma trận chuyển thô P₀:\nA→(B,C)  B→(C,D)  C→(A)  D→(0)", "en": "Raw transition matrix P₀:\nA→(B,C)  B→(C,D)  C→(A)  D→(0)"},
    "s3_a": {"vi": "Bẫy 1: Nút cụt làm rò rỉ xác suất", "en": "Pitfall 1: Dead end leaks probability"},
    "s3_b": {"vi": "Bước ngẫu nhiên thuần:\nA → B → D rồi kẹt vĩnh viễn tại D", "en": "Naive random walk:\nA → B → D, trapped forever at D"},
    "s4_a": {"vi": "Bẫy 2: Thành phần rời / chu trình tuần hoàn\nCách sửa: thay hàng D bằng 1/4 + teleport", "en": "Pitfall 2: Cycles / disconnected parts\nFix: uniform row for D + teleportation"},
    "s4_b": {"vi": "Ma trận Google với α = 0,85:\nG = 0,85 P + 0,15 v eᵀ", "en": "Google matrix with α = 0.85:\nG = 0.85 P + 0.15 v eᵀ"},
    "s4_c": {"vi": "Tính thử bước k = 1 cho đỉnh A:\nπ₁(A) = 0,85×(0,25×1 + 0,25×0,25) + 0,0375", "en": "Step k = 1 for node A:\nπ₁(A) = 0.85×(0.25×1 + 0.25×0.25) + 0.0375"},
    "s5_a": {"vi": "Lặp lũy thừa πᵀ ← πᵀG từ phân phối đều\nhội tụ về phân phối dừng duy nhất π", "en": "Power iteration πᵀ ← πᵀG from uniform\nconverges to a unique stationary π"},
    "s5_b": {"vi": "A đứng đầu (0,327) vì nhận 100% từ C;\nC (0,300) nhận từ cả A và B", "en": "A leads (0.327) getting 100% of C;\nC (0.300) receives from both A and B"},
    "s6_a": {"vi": "Nếu giảm α từ 0,85 xuống 0,50?\nTeleport nhiều hơn ⇒ thứ hạng phẳng hơn", "en": "What if α drops from 0.85 to 0.50?\nMore teleport ⇒ flatter distribution"},
    "end": {"vi": "Đổi cạnh, v hay α sẽ đổi thứ hạng:\nđồ thị là một lựa chọn mô hình hóa", "en": "Change edges, v, or α, ranks shift:\nthe graph is a modeling choice"},
}

P = np.array([
    [0.0,  0.5,  0.5,  0.0],
    [0.0,  0.0,  0.5,  0.5],
    [1.0,  0.0,  0.0,  0.0],
    [0.25, 0.25, 0.25, 0.25],
], dtype=float)
alpha = 0.85
v = np.array([0.25, 0.25, 0.25, 0.25])
G = alpha * P + (1.0 - alpha) * np.outer(np.ones(4), v)
assert np.allclose(G.sum(axis=1), 1.0)

pi = v.copy()
history = [pi.copy()]
for _ in range(35):
    pi = pi @ G
    history.append(pi.copy())

assert abs(history[1][0] - (0.85 * (0.25 * 1.0 + 0.25 * 0.25) + 0.15 * 0.25)) < 1e-12
assert abs(pi.sum() - 1.0) < 1e-12
assert np.linalg.norm(pi @ G - pi, 1) < 1e-10
order = np.argsort(-pi)
assert list(order) == [0, 2, 1, 3]

G_low = 0.50 * P + 0.50 * np.outer(np.ones(4), v)
pi_low = v.copy()
for _ in range(35):
    pi_low = pi_low @ G_low
assert abs(pi_low.sum() - 1.0) < 1e-12


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class PageRank(Scene):
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
                rem = vo_durs[sid] - (float(self.time) - t0) + 0.7
                self.wait(max(0.6, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 38, WHITE, 6.2)
        self.add(title)

        # --- Phần 1 ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 30, SKY, 4.3)
        s1b = line(TX["s1_b"], 26, WHITE, 2.5)
        self.play(FadeIn(s1a), run_time=0.8)
        self.wait(2.5)
        self.play(FadeIn(s1b), run_time=0.8)
        self.wait(3.0)
        ex_a = Circle(0.42, color=DIM, fill_color=CARD, fill_opacity=1).move_to([-2.0, -0.5, 0])
        ex_b = Circle(0.58, color=SUN, fill_color=CARD, fill_opacity=1, stroke_width=4).move_to([0.0, -0.5, 0])
        ex_c = Circle(0.42, color=MINT, fill_color=CARD, fill_opacity=1).move_to([2.0, -0.5, 0])
        ar1 = Arrow([-1.5, -0.5, 0], [-0.65, -0.5, 0], buff=0, color=DIM)
        ar2 = Arrow([0.65, -0.5, 0], [1.5, -0.5, 0], buff=0, color=SUN)
        self.play(FadeIn(ex_a), FadeIn(ex_b), FadeIn(ex_c), Create(ar1), Create(ar2), run_time=1.0)
        end_vo("s1", t0, 7.5)
        wipe(self, keep=[title])

        # --- Phần 2 ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 28, SKY, 4.9)
        self.play(FadeIn(s2a), run_time=0.7)
        pos = {
            0: np.array([-2.2, 2.3, 0]),
            1: np.array([ 2.2, 2.3, 0]),
            2: np.array([ 0.0, 0.3, 0]),
            3: np.array([ 2.4,-0.7, 0]),
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
            du = d / np.linalg.norm(d)
            st, en = pos[u] + du * 0.52, pos[w] - du * 0.52
            if (u, w) in ((0, 2), (2, 0)):
                perp = np.array([-du[1], du[0], 0]) * 0.14
                st, en = st + perp, en + perp
            arrows.add(Arrow(st, en, buff=0, stroke_width=3, color=DIM, max_tip_length_to_length_ratio=0.16))
        self.play(FadeIn(nodes), FadeIn(arrows), run_time=1.2)
        self.wait(3.5)
        s2b = line(TX["s2_b"], 24, WHITE, -2.3)
        mat_box = RoundedRectangle(corner_radius=0.14, width=6.6, height=2.2,
                                   fill_color=CARD, fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([0, -4.3, 0])
        mat_rows = VGroup(
            T("A: [ 0,0   0,5   0,5   0,0 ]" if LANG == "vi" else "A: [ 0.0   0.5   0.5   0.0 ]", 22, WHITE),
            T("B: [ 0,0   0,0   0,5   0,5 ]" if LANG == "vi" else "B: [ 0.0   0.0   0.5   0.5 ]", 22, WHITE),
            T("C: [ 1,0   0,0   0,0   0,0 ]" if LANG == "vi" else "C: [ 1.0   0.0   0.0   0.0 ]", 22, WHITE),
            T("D: [ 0,0   0,0   0,0   0,0 ]" if LANG == "vi" else "D: [ 0.0   0.0   0.0   0.0 ]", 22, PINK),
        ).arrange(DOWN, buff=0.14).move_to(mat_box)
        self.play(FadeIn(s2b), FadeIn(mat_box), FadeIn(mat_rows, lag_ratio=0.2), run_time=1.5)
        end_vo("s2", t0, 12.5)

        # --- Phần 3 ---
        self.play(FadeOut(s2a), FadeOut(s2b), FadeOut(mat_box), FadeOut(mat_rows), run_time=0.5)
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 30, PINK, 4.9)
        s3b = line(TX["s3_b"], 26, WHITE, -2.5)
        self.play(FadeIn(s3a), FadeIn(s3b), run_time=0.8)
        walker = Dot(pos[0], radius=0.2, color=SUN)
        self.play(FadeIn(walker), run_time=0.4)
        self.wait(1.0)
        self.play(walker.animate.move_to(pos[1]), run_time=1.2)
        self.wait(0.8)
        self.play(walker.animate.move_to(pos[3]), run_time=1.2)
        ring = Circle(0.65, color=PINK, stroke_width=4).move_to(pos[3])
        self.play(Create(ring), run_time=0.8)
        end_vo("s3", t0, 11.0)

        # --- Phần 4 ---
        self.play(FadeOut(s3a), FadeOut(s3b), FadeOut(ring), FadeOut(walker), run_time=0.5)
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 26, SUN, 4.9)
        self.play(FadeIn(s4a), run_time=0.8)
        self.wait(3.5)
        tele_lines = VGroup(
            DashedLine(pos[3], pos[0], color=SUN, stroke_width=2.5),
            DashedLine(pos[3], pos[1], color=SUN, stroke_width=2.0),
            DashedLine(pos[3], pos[2], color=SUN, stroke_width=2.0),
        )
        self.play(Create(tele_lines), run_time=1.2)
        s4b = line(TX["s4_b"], 28, MINT, -2.3)
        self.play(FadeIn(s4b), run_time=0.8)
        self.wait(4.0)
        s4c = line(TX["s4_c"], 23, WHITE, -3.9)
        res1 = T(f"⇒ π₁(A) = {nf(history[1][0], 3)}", 28, SUN).move_to([0, -5.1, 0])
        self.play(FadeIn(s4c), FadeIn(res1), run_time=1.0)
        end_vo("s4", t0, 7.5)

        # --- Phần 5 ---
        self.play(FadeOut(s4a), FadeOut(s4b), FadeOut(s4c), FadeOut(res1), FadeOut(tele_lines), run_time=0.5)
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 26, MINT, 4.9)
        self.play(FadeIn(s5a), run_time=0.7)
        base_y = -4.5
        max_h = 2.3
        xs = [-2.4, -0.8, 0.8, 2.4]
        bars = VGroup()
        val_txts = VGroup()
        bar_labels = VGroup()
        for i, nm in enumerate(names):
            h0 = (history[0][i] / 0.42) * max_h
            b = Rectangle(width=0.95, height=h0, fill_color=SKY, fill_opacity=0.85, stroke_width=0)
            b.move_to([xs[i], base_y + h0 / 2, 0])
            bars.add(b)
            val_txts.add(T(nf(history[0][i], 3), 24, WHITE).next_to(b, UP, buff=0.1))
            bar_labels.add(T(nm, 26, DIM).move_to([xs[i], base_y - 0.35, 0]))
        step_lbl = T("k = 0", 26, SUN).move_to([0, -1.6, 0])
        self.play(FadeIn(bars), FadeIn(val_txts), FadeIn(bar_labels), FadeIn(step_lbl), run_time=0.9)
        self.wait(2.0)
        for step in (1, 2, 5, 10, 35):
            anims = [Transform(step_lbl, T(f"k = {step}", 26, SUN).move_to([0, -1.6, 0]))]
            for i in range(4):
                hi = (history[step][i] / 0.42) * max_h
                col = SUN if (step == 35 and i == 0) else (MINT if (step == 35 and i == 2) else SKY)
                nb = Rectangle(width=0.95, height=hi, fill_color=col, fill_opacity=0.9, stroke_width=0)
                nb.move_to([xs[i], base_y + hi / 2, 0])
                nt = T(nf(history[step][i], 3), 24, col if step == 35 and i in (0, 2) else WHITE).next_to(nb, UP, buff=0.1)
                anims.append(Transform(bars[i], nb))
                anims.append(Transform(val_txts[i], nt))
            self.play(*anims, run_time=0.8)
            self.wait(1.6)
        s5b = line(TX["s5_b"], 24, SUN, -5.55)
        self.play(FadeIn(s5b), run_time=0.8)
        end_vo("s5", t0, 6.5)

        # --- Phần 6 ---
        wipe(self, keep=[title])
        t0 = start_vo("s6")
        s6a = line(TX["s6_a"], 28, SKY, 4.0)
        comp_box = RoundedRectangle(corner_radius=0.16, width=7.2, height=2.6,
                                    fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([0, 0.8, 0])
        comp_lines = VGroup(
            T(f"α = {nf(0.85,2)}:  A={nf(pi[0],3)}  C={nf(pi[2],3)}  B={nf(pi[1],3)}  D={nf(pi[3],3)}", 23, SUN),
            T(f"α = {nf(0.50,2)}:  A={nf(pi_low[0],3)}  C={nf(pi_low[2],3)}  B={nf(pi_low[1],3)}  D={nf(pi_low[3],3)}", 23, MINT),
        ).arrange(DOWN, buff=0.35).move_to(comp_box)
        end_c = line(TX["end"], 28, WHITE, -2.5)
        self.play(FadeIn(s6a), FadeIn(comp_box), FadeIn(comp_lines), run_time=1.2)
        self.wait(4.5)
        self.play(FadeIn(end_c), run_time=0.8)
        end_vo("s6", t0, 13.0)

        tl_out = os.environ.get("VO_TIMELINE_JSON", "")
        if tl_out:
            with open(tl_out, "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
