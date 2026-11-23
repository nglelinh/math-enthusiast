from common_b import *

TX = {
    "title": {"vi": "Chứng minh không tiết lộ:\n3-tô màu đồ thị", "en": "Zero-knowledge proof:\nGraph 3-coloring"},
    "s1_a": {"vi": "Bài toán nghịch lý:\nThuyết phục bạn biết lời giải mà không lộ bí mật", "en": "The paradox:\nProve you know a solution without revealing it"},
    "s1_b": {"vi": "Gửi luôn lời giải ⇒ lộ sạch bí mật\nNói 'tin tôi đi' ⇒ không có độ tin cậy", "en": "Send the coloring ⇒ leaks everything\nSay 'trust me' ⇒ zero soundness"},
    "s2_a": {"vi": "Bí mật của Peggy: cách 3-tô màu\nhợp lệ cho đồ thị 5 đỉnh, 7 cạnh", "en": "Peggy's secret: a valid 3-coloring\nof a 5-vertex, 7-edge graph"},
    "s2_b": {"vi": "Mọi cạnh đều có 2 đầu khác màu\n(đây là witness Peggy giữ kín)", "en": "Every edge has two different colors\n(this is Peggy's private witness)"},
    "s3_a": {"vi": "Vòng 1 — Cam kết: hoán vị ngẫu nhiên\n3 màu (Hồng→Vàng, Xanh→Hồng, Vàng→Xanh)", "en": "Round 1 — Commit: randomly permute\n3 colors (Pink→Sun, Sky→Pink, Sun→Sky)"},
    "s3_b": {"vi": "Khóa kín cả 5 đỉnh; Victor chọn 1 cạnh (2,4)\nPeggy chỉ mở đúng 2 đỉnh đầu cạnh đó", "en": "Lock all 5 vertices; Victor picks edge (2,4)\nPeggy opens only those 2 endpoints"},
    "s3_ok": {"vi": "Hai màu khác nhau ⇒ Victor chấp nhận vòng 1\nnhưng không biết màu gốc là gì!", "en": "Different colors ⇒ Victor accepts Round 1\nyet learns zero about the original colors!"},
    "s3_c": {"vi": "Vòng 2: hoán vị màu mới hoàn toàn\nvà mở cạnh khác (1,3) — không lộ màu gốc", "en": "Round 2: fresh random permutation\nand open edge (1,3) — zero leak of original colors"},
    "s4_a": {"vi": "Bẫy: Nếu Peggy gian dối (tô sai cạnh 3–5)?", "en": "Pitfall: What if Peggy cheats (bad edge 3–5)?"},
    "s4_b": {"vi": "Ít nhất 1/7 cạnh trùng màu ⇒ mỗi vòng bị bắt ≥ 1/7\nLặp k vòng: xác suất thoát ≤ (6/7)^k", "en": "At least 1/7 edge is bad ⇒ caught ≥ 1/7 per round\nAfter k rounds: cheat probability ≤ (6/7)^k"},
    "s5_a": {"vi": "Vì sao không lộ gì? Ý tưởng Simulator:\nđoán trước cạnh e, tô 2 đầu khác màu, sai thì tua lại", "en": "Why zero-knowledge? The Simulator:\nguess edge e first, color its 2 ends, rewind if wrong"},
    "end": {"vi": "Completeness + Soundness + Zero-Knowledge\nGoldwasser–Micali–Rackoff & GMW", "en": "Completeness + Soundness + Zero-Knowledge\nGoldwasser–Micali–Rackoff & GMW"},
}

edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (0, 3)]
coloring = [0, 1, 2, 2, 0]  # 0: PINK, 1: SKY, 2: SUN
assert all(coloring[u] != coloring[v] for u, v in edges)
m = len(edges)
assert m == 7
rounds_stats = [(k, 1.0 - (1.0 - 1.0 / m) ** k) for k in (1, 7, 20, 50)]
assert rounds_stats[2][1] > 0.95 and rounds_stats[3][1] > 0.999


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class ZKP(Scene):
    def construct(self):
        title = line(TX["title"], 38, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Nghịch lý Zero-Knowledge (24s) ---
        s1a = line(TX["s1_a"], 28, SKY, 4.5)
        s1b = line(TX["s1_b"], 26, PINK, 2.7)
        self.play(FadeIn(s1a), run_time=0.8)
        self.wait(3.5)
        self.play(FadeIn(s1b), run_time=0.8)
        self.wait(5.5)

        peggy = VGroup(Circle(0.55, color=PINK, fill_color=CARD, fill_opacity=1).move_to([-2.2, -0.5, 0]),
                       T("Peggy", 24, PINK).move_to([-2.2, -0.5, 0]))
        victor = VGroup(Circle(0.55, color=SKY, fill_color=CARD, fill_opacity=1).move_to([2.2, -0.5, 0]),
                        T("Victor", 24, SKY).move_to([2.2, -0.5, 0]))
        ch_arr = DoubleArrow([-1.4, -0.5, 0], [1.4, -0.5, 0], color=SUN)
        ch_lbl = T("Thách thức ↔ Phản hồi" if LANG == "vi" else "Challenge ↔ Response", 22, SUN).next_to(ch_arr, UP, buff=0.15)
        self.play(FadeIn(peggy), FadeIn(victor), Create(ch_arr), FadeIn(ch_lbl), run_time=1.0)
        self.wait(8.0)
        wipe(self, keep=[title])

        # --- Phần 2: Đồ thị bí mật của Peggy (24s) ---
        s2a = line(TX["s2_a"], 28, SKY, 4.9)
        self.play(FadeIn(s2a), run_time=0.7)

        pts = [
            np.array([ 0.0,  2.7, 0]),
            np.array([-2.2,  1.2, 0]),
            np.array([ 2.2,  1.2, 0]),
            np.array([-1.5, -0.9, 0]),
            np.array([ 1.5, -0.9, 0]),
        ]
        palette = [PINK, SKY, SUN]
        perm1 = [SUN, PINK, SKY]
        perm2 = [SKY, SUN, PINK]

        edge_lines = VGroup(*[Line(pts[u], pts[v], color=DIM, stroke_width=3.5) for u, v in edges])
        nodes = VGroup()
        for i, p in enumerate(pts):
            col = palette[coloring[i]]
            circ = Circle(0.42, color=col, fill_color=col, fill_opacity=0.9, stroke_width=3.5).move_to(p)
            lbl = T(str(i + 1), 26, BLACK).move_to(p)
            nodes.add(VGroup(circ, lbl))

        self.play(Create(edge_lines), FadeIn(nodes), run_time=1.4)
        s2b = line(TX["s2_b"], 26, MINT, -2.5)
        self.play(FadeIn(s2b), run_time=0.8)
        self.wait(12.5)

        # --- Phần 3: Vòng 1 & Vòng 2 chi tiết (46s) ---
        self.play(FadeOut(s2a), FadeOut(s2b), run_time=0.5)
        s3a = line(TX["s3_a"], 25, SUN, 4.9)
        self.play(FadeIn(s3a), run_time=0.7)
        self.wait(4.0)

        self.play(*[nodes[i][0].animate.set_fill(CARD, opacity=1).set_stroke(DIM) for i in range(5)],
                  *[nodes[i][1].animate.set_color(DIM) for i in range(5)], run_time=1.0)
        s3b = line(TX["s3_b"], 25, MINT, -2.5)
        self.play(FadeIn(s3b), run_time=0.8)
        self.wait(3.0)

        hi_1 = Line(pts[1], pts[3], color=MINT, stroke_width=7)
        self.play(Create(hi_1), run_time=0.6)
        for idx in (1, 3):
            col = perm1[coloring[idx]]
            self.play(nodes[idx][0].animate.set_fill(col, opacity=0.95).set_stroke(col),
                      nodes[idx][1].animate.set_color(BLACK), run_time=0.7)
        s3ok = line(TX["s3_ok"], 24, WHITE, -4.1)
        self.play(FadeIn(s3ok), run_time=0.8)
        self.wait(7.5)

        # Vòng 2 với hoán vị mới & cạnh (0, 2)
        self.play(FadeOut(s3a), FadeOut(s3b), FadeOut(s3ok), FadeOut(hi_1), run_time=0.5)
        for idx in (1, 3):
            self.play(nodes[idx][0].animate.set_fill(CARD, opacity=1).set_stroke(DIM),
                      nodes[idx][1].animate.set_color(DIM), run_time=0.3)
        s3c = line(TX["s3_c"], 25, SKY, 4.9)
        self.play(FadeIn(s3c), run_time=0.7)
        hi_2 = Line(pts[0], pts[2], color=MINT, stroke_width=7)
        self.play(Create(hi_2), run_time=0.6)
        for idx in (0, 2):
            col = perm2[coloring[idx]]
            self.play(nodes[idx][0].animate.set_fill(col, opacity=0.95).set_stroke(col),
                      nodes[idx][1].animate.set_color(BLACK), run_time=0.7)
        self.wait(12.0)

        # --- Phần 4: Kẻ gian dối & Khuếch đại Soundness (34s) ---
        self.play(FadeOut(s3c), FadeOut(hi_2), run_time=0.5)
        s4a = line(TX["s4_a"], 28, PINK, 4.9)
        self.play(FadeIn(s4a), run_time=0.7)

        bad_cols = [SUN, SKY, PINK, SKY, PINK]
        self.play(*[nodes[i][0].animate.set_fill(bad_cols[i], opacity=0.9).set_stroke(bad_cols[i]) for i in range(5)],
                  *[nodes[i][1].animate.set_color(BLACK) for i in range(5)], run_time=0.9)
        bad_edge = Line(pts[2], pts[4], color=PINK, stroke_width=8)
        self.play(Create(bad_edge), run_time=0.6)
        self.wait(3.5)

        s4b = line(TX["s4_b"], 24, WHITE, -2.1)
        self.play(FadeIn(s4b), run_time=0.7)
        rows = VGroup()
        for r_idx, (k, p_catch) in enumerate(rounds_stats):
            y = -3.25 - r_idx * 0.78
            box = RoundedRectangle(corner_radius=0.1, width=6.6, height=0.62,
                                   fill_color=CARD, fill_opacity=1, stroke_color=DIM, stroke_width=1.5).move_to([0, y, 0])
            txt = T(f"k = {k:>2}  ⇒  " + (f"bị bắt ≥ {nf(p_catch*100, 1)}%" if LANG == "vi" else f"caught ≥ {nf(p_catch*100, 1)}%"),
                    23, MINT if k >= 20 else WHITE).move_to([0, y, 0])
            rows.add(VGroup(box, txt))
        self.play(FadeIn(rows, lag_ratio=0.18), run_time=1.4)
        self.wait(14.5)

        # --- Phần 5: Simulator & Tổng kết (28s) ---
        wipe(self, keep=[title])
        s5a = line(TX["s5_a"], 26, SUN, 3.8)
        sim_box = RoundedRectangle(corner_radius=0.16, width=7.5, height=2.7,
                                   fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([0, 0.5, 0])
        sim_txt = fit(VGroup(
            T("1. Chọn ngẫu nhiên 1 cạnh e = (u, v)" if LANG == "vi" else "1. Pick a random edge e = (u, v)", 24, WHITE),
            T("2. Tô u, v khác màu; các đỉnh khác tùy ý" if LANG == "vi" else "2. Color u ≠ v; remaining vertices arbitrary", 24, WHITE),
            T("3. Nếu Victor chọn đúng e ⇒ hợp lệ! Sai ⇒ lặp lại" if LANG == "vi" else "3. If Victor picks e ⇒ valid! Else ⇒ rewind", 24, MINT),
        ).arrange(DOWN, buff=0.25), 6.8).move_to(sim_box)
        self.play(FadeIn(s5a), FadeIn(sim_box), FadeIn(sim_txt), run_time=1.2)
        self.wait(14.5)

        end_c = line(TX["end"], 28, WHITE, -3.2)
        self.play(FadeIn(end_c), run_time=0.8)
        self.wait(14.5)
