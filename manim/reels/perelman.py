from common_b import *
import json

TX = {
    "title": {"vi": "Perelman & Giả thuyết Poincaré\n(Huy chương Fields 2006)", "en": "Perelman & Poincaré Conjecture\n(Fields Medal 2006)"},
    "s1_a": {"vi": "Poincaré (1904): Đa tạp 3 chiều đóng,\nđơn liên (π₁ = {e}) có phải là S³?", "en": "Poincaré (1904): Is every closed,\nsimply connected 3-manifold S³?"},
    "s1_b": {"vi": "Chiều 2 dễ • Chiều ≥ 5 (Smale) & 4 (Freedman)\nChiều 3 là khó nhất!", "en": "Dim 2 easy • Dim ≥ 5 (Smale) & 4 (Freedman)\nDimension 3 was the hardest!"},
    "s2_a": {"vi": "Giả thuyết Hình học hóa của Thurston:\nCắt đa tạp thành các mảnh thuần nhất", "en": "Thurston's Geometrization Conjecture:\nCut 3-manifolds into uniform pieces"},
    "s2_b": {"vi": "8 mô hình hình học (Cầu, Euclid, Hyperbolic…)\nHình học hóa ⇒ Giả thuyết Poincaré!", "en": "8 geometries (Spherical, Euclidean, Hyperbolic…)\nGeometrization ⇒ Poincaré Conjecture!"},
    "s3_a": {"vi": "Dòng Ricci của Hamilton (1982):\n∂g/∂t = −2 Ric(g) (truyền nhiệt hình học)", "en": "Hamilton's Ricci Flow (1982):\n∂g/∂t = −2 Ric(g) (geometric heat flow)"},
    "s3_b": {"vi": "Trở ngại: Xuất hiện điểm kỳ dị\nVí dụ: thắt cổ chai S² × ℝ co hẹp!", "en": "Obstacle: Finite-time singularities\nE.g. neck pinch S² × ℝ collapsing!"},
    "s4_a": {"vi": "Công cụ của Perelman (2002–2003):\nEntropy đơn điệu + Không suy biến κ", "en": "Perelman's tools (2002–2003):\nMonotone entropy + κ-noncollapsing"},
    "s4_b": {"vi": "Phẫu thuật (Surgery): Cắt cổ hẹp, bịt mũ\nrồi chạy tiếp dòng Ricci (hữu hạn lần cắt!)", "en": "Surgery: Cut thin neck, cap with balls\nand continue Ricci flow (finitely many times!)"},
    "s5_a": {"vi": "Kết quả: Hình học hóa ĐÚNG ⇒ Poincaré ĐÚNG\nLưu ý lịch sử quan trọng:", "en": "Result: Geometrization TRUE ⇒ Poincaré TRUE\nImportant historical notes:"},
}

# Kiểm tra tính nhất quán: 8 hình học, mốc năm
assert 2006 - 1904 == 102
assert 8 == 3 + 5  # 3 hình học cơ bản + 5 hình học còn lại


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class PerelmanPoincare(Scene):
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

        title = line(TX["title"], 35, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Câu hỏi Poincaré ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        c_sphere = Circle(radius=1.35, color=MINT, stroke_width=4).move_to([-1.8, 1.4, 0])
        l_sphere = Circle(radius=0.55, color=SUN, stroke_width=3).move_to([-1.8, 1.6, 0])
        t_sphere = T("S³: mọi vòng co về 1 điểm" if LANG == "vi" else "S³: every loop shrinks", 21, MINT).next_to(c_sphere, DOWN, buff=0.25)

        c_torus = Ellipse(width=2.6, height=1.6, color=PINK, stroke_width=4).move_to([1.9, 1.4, 0])
        hole = Ellipse(width=0.9, height=0.45, color=PINK, stroke_width=3).move_to([1.9, 1.4, 0])
        t_torus = T("Xuyến: vòng vướng lỗ!" if LANG == "vi" else "Torus: loop gets stuck!", 21, PINK).next_to(c_torus, DOWN, buff=0.55)

        self.play(Create(c_sphere), Create(l_sphere), FadeIn(t_sphere), run_time=1.0)
        self.play(l_sphere.animate.scale(0.05), run_time=1.0)
        self.play(Create(c_torus), Create(hole), FadeIn(t_torus), run_time=1.0)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 24, SUN, -1.5)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 2: Hình học hóa Thurston ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 26, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        geoms = VGroup()
        g_data = [
            ("1. Cầu (Cong dương, +1)" if LANG == "vi" else "1. Spherical (+1 curvature)", MINT),
            ("2. Euclid (Phẳng, 0)" if LANG == "vi" else "2. Euclidean (Flat, 0)", SKY),
            ("3. Hyperbolic (Cong âm, −1)" if LANG == "vi" else "3. Hyperbolic (−1 curvature)", SUN),
            ("+ 5 hình học thuần nhất khác" if LANG == "vi" else "+ 5 other uniform geometries", WHITE),
        ]
        for i, (txt, col) in enumerate(g_data):
            y = 2.8 - i * 1.05
            b = RoundedRectangle(corner_radius=0.14, width=7.0, height=0.82,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 24, col).move_to([0, y, 0])
            geoms.add(VGroup(b, t))
        self.play(FadeIn(geoms, lag_ratio=0.22), run_time=1.4)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 25, MINT, -2.0)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 3: Dòng Ricci & Điểm kỳ dị ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        # Minh họa quả tạ thắt cổ chai: hai hình tròn nối bằng một cổ
        left_bell = Circle(radius=1.0, color=MINT, stroke_width=4).move_to([-2.0, 1.4, 0])
        right_bell = Circle(radius=1.0, color=MINT, stroke_width=4).move_to([2.0, 1.4, 0])
        neck_top = Line([-1.1, 1.85, 0], [1.1, 1.85, 0], color=PINK, stroke_width=4)
        neck_bot = Line([-1.1, 0.95, 0], [1.1, 0.95, 0], color=PINK, stroke_width=4)
        self.play(Create(left_bell), Create(right_bell), Create(neck_top), Create(neck_bot), run_time=1.0)
        self.wait(1.5)
        # Cổ thắt lại
        self.play(
            neck_top.animate.put_start_and_end_on([-1.1, 1.52, 0], [1.1, 1.52, 0]),
            neck_bot.animate.put_start_and_end_on([-1.1, 1.28, 0], [1.1, 1.28, 0]),
            run_time=1.5,
        )
        sing_lbl = T("Độ cong → ∞ (Điểm kỳ dị!)" if LANG == "vi" else "Curvature → ∞ (Singularity!)", 23, PINK).move_to([0, 0.0, 0])
        self.play(FadeIn(sing_lbl), run_time=0.7)
        self.wait(1.5)

        s3b = line(TX["s3_b"], 25, SUN, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 11.0)
        wipe(self, keep=[title])

        # --- Phần 4: Perelman & Phẫu thuật ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 25, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        tools = VGroup()
        t_data = [
            ("Entropy đơn điệu: chặn hành vi xấu" if LANG == "vi" else "Monotone entropy: rules out bad behavior", MINT),
            ("Không suy biến κ: thể tích ≥ c · r³" if LANG == "vi" else "κ-noncollapsing: volume ≥ c · r³", SUN),
        ]
        for i, (txt, col) in enumerate(t_data):
            y = 2.6 - i * 1.1
            b = RoundedRectangle(corner_radius=0.14, width=7.2, height=0.88,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 24, col).move_to([0, y, 0])
            tools.add(VGroup(b, t))
        self.play(FadeIn(tools, lag_ratio=0.3), run_time=1.2)
        self.wait(2.5)

        # Phẫu thuật: cắt cổ và bịt hai mũ tròn
        cut_l = Arc(radius=0.5, start_angle=-PI/2, angle=PI, color=MINT, stroke_width=5).move_to([-0.8, -0.3, 0])
        cut_r = Arc(radius=0.5, start_angle=PI/2, angle=PI, color=MINT, stroke_width=5).move_to([0.8, -0.3, 0])
        scis = T("✂ Cắt cổ  →  Bịt mũ S³" if LANG == "vi" else "✂ Cut neck  →  Cap with balls", 24, SUN).move_to([0, -1.2, 0])
        self.play(Create(cut_l), Create(cut_r), FadeIn(scis), run_time=1.0)
        self.wait(2.0)

        s4b = line(TX["s4_b"], 24, WHITE, -2.5)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 11.0)
        wipe(self, keep=[title])

        # --- Phần 5: Tổng kết & Lịch sử ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 25, SKY, 4.5)
        self.play(FadeIn(s5a), run_time=0.8)

        notes = VGroup()
        n_data = [
            ("Định lý chính: Hình học hóa (Poincaré là hệ quả)" if LANG == "vi" else "Main theorem: Geometrization (Poincaré follows)", MINT),
            ("Tiếp nối chương trình dòng Ricci của Hamilton" if LANG == "vi" else "Completes Hamilton's Ricci flow program", SKY),
            ("Perelman từ chối cả Fields (2006) & Clay" if LANG == "vi" else "Perelman declined both Fields (2006) & Clay", PINK),
        ]
        for i, (txt, col) in enumerate(n_data):
            y = 2.0 - i * 1.45
            b = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.05,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 23, col).move_to([0, y, 0])
            notes.add(VGroup(b, t))
        self.play(FadeIn(notes, lag_ratio=0.25), run_time=1.5)
        end_vo("s5", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
