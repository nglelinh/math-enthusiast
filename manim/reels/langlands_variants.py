from common_b import *
import json

TX = {
    "title": {"vi": "Langlands Số học vs Hình học\n& Những hiểu lầm thường gặp", "en": "Arithmetic vs Geometric Langlands\n& Common Misconceptions"},
    "s1_a": {"vi": "Đừng gọi chung chung là 'Langlands'!\nCó hai chương trình song song khác nhau:", "en": "Don't just say 'Langlands'!\nThere are two distinct parallel programs:"},
    "s1_b": {"vi": "Cả hai cùng chia sẻ nhóm đối ngẫu G^∨\nnhưng đối tượng & bối cảnh hoàn toàn khác!", "en": "Both share the dual group G^∨\nbut objects & settings differ completely!"},
    "s2_a": {"vi": "Cầu nối Vật lý (Kapustin–Witten 2007):\nĐối ngẫu S trong siêu Yang–Mills N = 4", "en": "Physics Bridge (Kapustin–Witten 2007):\nS-duality in N = 4 Super Yang–Mills"},
    "s2_b": {"vi": "Đây là 'bộ từ điển' truyền cảm hứng mạnh,\nnhưng KHÔNG thay thế chứng minh toán học!", "en": "A powerful dictionary & inspiration,\nbut NOT a substitute for mathematical proof!"},
    "s3_a": {"vi": "Kiểm tra nhanh 4 hiểu lầm phổ biến\nkhi đọc về Huy chương Fields 2010:", "en": "Quick check: 4 common myths\nabout the 2010 Fields Medal:"},
}

assert 4 == 2 + 2  # 4 hiểu lầm kinh điển


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class LanglandsVariants(Scene):
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

        title = line(TX["title"], 34, WHITE, 6.2)
        self.add(title)

        # --- s1: Số học vs Hình học ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 25, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        c1 = RoundedRectangle(corner_radius=0.14, width=3.55, height=2.9, fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([-2.1, 1.3, 0])
        t1 = T("Langlands Số học\n• Trường số / Adele\n• Tự đẳng cấu G(A)\n• Biểu diễn Galois\n• Bổ đề Cơ bản Ngô" if LANG == "vi" else "Arithmetic\n• Number fields\n• Automorphic G(A)\n• Galois reps\n• Ngô's Lemma", 19, SKY).move_to(c1)

        c2 = RoundedRectangle(corner_radius=0.14, width=3.55, height=2.9, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([2.1, 1.3, 0])
        t2 = T("Langlands Hình học\n• Đường cong C\n• D-môđun Bun_G(C)\n• Hệ địa phương G^∨\n• Khác định lý Ngô" if LANG == "vi" else "Geometric\n• Complex curve C\n• D-modules Bun_G\n• G^∨ local systems\n• Different theorem", 19, MINT).move_to(c2)

        self.play(FadeIn(c1), FadeIn(t1), FadeIn(c2), FadeIn(t2), run_time=1.2)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, SUN, -1.5)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- s2: Đối ngẫu S & Vật lý ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 25, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        phy_box = RoundedRectangle(corner_radius=0.14, width=7.4, height=2.2, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 1.5, 0])
        phy_t = T("Điện ↔ Từ  (Đối ngẫu S: G ↔ G^∨)\nĐối xứng gương của không gian Hitchin" if LANG == "vi" else "Electric ↔ Magnetic  (S-duality: G ↔ G^∨)\nMirror symmetry of Hitchin spaces", 22, SUN).move_to(phy_box)
        self.play(FadeIn(phy_box), FadeIn(phy_t), run_time=1.0)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 24, PINK, -1.2)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- s3: 4 hiểu lầm cần tránh ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        myths = VGroup()
        m_data = [
            ("✗ Ngô sáng lập Langlands  →  ✓ Langlands đề xuất", PINK),
            ("✗ Bổ đề nhỏ nhặt  →  ✓ Gỡ nút thắt hàng thập kỷ", SUN),
            ("✗ Chỉ biến đổi p-adic  →  ✓ Hình học là then chốt", SKY),
            ("✗ Xong toàn bộ Langlands  →  ✓ Còn nhiều giả thuyết mở", MINT),
        ]
        for i, (txt, col) in enumerate(m_data):
            y = 2.5 - i * 1.15
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.88, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 18, col).move_to([0, y, 0])
            myths.add(VGroup(b, t))
        self.play(FadeIn(myths, lag_ratio=0.25), run_time=1.5)
        end_vo("s3", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
