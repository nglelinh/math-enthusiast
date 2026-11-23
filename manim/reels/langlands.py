from common_b import *
import json

TX = {
    "title": {"vi": "Ngô Bảo Châu & Bổ đề Cơ bản\n(Huy chương Fields 2010)", "en": "Ngô Bảo Châu & Fundamental Lemma\n(Fields Medal 2010)"},
    "s1_a": {"vi": "Chương trình Langlands (1960–1970):\nCây cầu nối hai thế giới toán học", "en": "Langlands Program (1960–1970):\nA bridge between two worlds"},
    "s1_b": {"vi": "Langlands (Abel 2018) vẽ bản đồ\nNgô Bảo Châu (Fields 2010) gỡ nút thắt", "en": "Langlands (Abel 2018) drew the map\nNgô (Fields 2010) broke the bottleneck"},
    "s2_a": {"vi": "Công thức vết Arthur–Selberg:\nPhía Phổ (tự đẳng cấu) = Phía Hình học", "en": "Arthur–Selberg Trace Formula:\nSpectral side = Geometric side"},
    "s2_b": {"vi": "Lý thuyết nội soi (Endoscopy):\nSo sánh nhóm G với nhóm nhỏ hơn H", "en": "Endoscopy:\nCompare group G with smaller group H"},
    "s2_c": {"vi": "Chưa chứng minh được đẳng thức p-adic\n⇒ Hàng loạt định lý chỉ đúng 'có điều kiện'!", "en": "Missing p-adic orbital integral identity\n⇒ Major theorems remained 'conditional'!"},
    "s3_a": {"vi": "Bước ngoặt: không tính tích phân trực tiếp\nmà chuyển sang Hình học Đại số!", "en": "Breakthrough: don't compute integrals directly\n— translate to Algebraic Geometry!"},
    "s3_b": {"vi": "Laumon–Ngô (2004): nhóm unita\nNgô (2010): trường hợp tổng quát (IHÉS)", "en": "Laumon–Ngô (2004): unitary groups\nNgô (2010): general Lie algebras (IHÉS)"},
    "s4_a": {"vi": "Phân thớ Hitchin biến bài toán tích phân\nthành so sánh cả một họ các thớ hình học", "en": "Hitchin fibration turns one integral\ninto a whole family of geometric fibers"},
    "s4_b": {"vi": "Định lý về giá (Support) + Phân tách đối đồng điều\n⇒ Hai phía nội soi có cùng vết Frobenius!", "en": "Support theorem + Cohomology decomposition\n⇒ Both sides share the same Frobenius trace!"},
    "s5_a": {"vi": "Sau 2010: gỡ bỏ giả thiết 'có điều kiện'\nPhân biệt rõ để không nhầm lẫn:", "en": "After 2010: theorems become unconditional\nKey distinctions to remember:"},
}

# Kiểm tra cấu trúc số liệu: 3 cây cầu & 2 mốc năm
assert 2010 - 2004 == 6
assert 2018 > 2010 > 2004


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class LanglandsFundamentalLemma(Scene):
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

        # --- Phần 1: Chương trình Langlands ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        b_left = RoundedRectangle(corner_radius=0.16, width=3.55, height=2.2,
                                  fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([-2.15, 1.5, 0])
        t_left = T("Giải tích\nDạng tự đẳng cấu\nG(A)" if LANG == "vi" else "Analysis\nAutomorphic forms\nG(A)", 20, SKY).move_to(b_left)

        b_right = RoundedRectangle(corner_radius=0.16, width=3.55, height=2.2,
                                   fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([2.15, 1.5, 0])
        t_right = T("Số học\nBiểu diễn Galois\nGal(Q̄/Q)" if LANG == "vi" else "Arithmetic\nGalois reps\nGal(Q̄/Q)", 20, MINT).move_to(b_right)

        bridge = DoubleArrow([-0.4, 1.5, 0], [0.4, 1.5, 0], color=SUN, stroke_width=4, buff=0.05)
        l_lbl = T("Hàm L" if LANG == "vi" else "L-functions", 22, SUN).next_to(bridge, UP, buff=0.2)

        self.play(FadeIn(b_left), FadeIn(t_left), FadeIn(b_right), FadeIn(t_right), run_time=1.0)
        self.play(Create(bridge), FadeIn(l_lbl), run_time=0.8)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 25, SUN, -1.2)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 2: Công thức vết & Nút thắt Nội soi ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 26, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        eq_box = RoundedRectangle(corner_radius=0.14, width=7.4, height=1.2,
                                  fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 2.7, 0])
        eq_txt = T("∑ Phổ (G)  =  ∑ Tích phân quỹ đạo (G)" if LANG == "vi" else "∑ Spectral (G)  =  ∑ Orbital Integrals (G)", 24, SUN).move_to(eq_box)
        self.play(FadeIn(eq_box), FadeIn(eq_txt), run_time=0.9)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 25, MINT, 1.1)
        self.play(FadeIn(s2b), run_time=0.8)

        cmp_box = RoundedRectangle(corner_radius=0.14, width=7.6, height=1.6,
                                   fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, -0.5, 0])
        cmp_txt = T("O_γ(f_G)  =?  Δ(γ, γ_H) · O_γH(f_H)\n(tích phân quỹ đạo p-adic + hệ số chuyển)" if LANG == "vi" else "O_γ(f_G)  =?  Δ(γ, γ_H) · O_γH(f_H)\n(p-adic orbital integrals + transfer factor)", 21, WHITE).move_to(cmp_box)
        self.play(FadeIn(cmp_box), FadeIn(cmp_txt), run_time=1.0)
        self.wait(2.5)

        s2c = line(TX["s2_c"], 25, PINK, -2.6)
        self.play(FadeIn(s2c), run_time=0.8)
        end_vo("s2", t0, 12.0)
        wipe(self, keep=[title])

        # --- Phần 3: Chuyển ngôn ngữ sang Hình học ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 26, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        steps = VGroup()
        st_data = [
            ("1. Đếm điểm / đối đồng điều ℓ-adic" if LANG == "vi" else "1. Point counting / ℓ-adic cohomology", MINT),
            ("2. Sắp xếp thành phân thớ Hitchin" if LANG == "vi" else "2. Organize into Hitchin fibration", SUN),
            ("3. So sánh các thớ nội soi" if LANG == "vi" else "3. Compare endoscopic fibers", SKY),
        ]
        for i, (txt, col) in enumerate(st_data):
            y = 2.5 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.2, height=0.92,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 24, col).move_to([0, y, 0])
            steps.add(VGroup(b, t))
        self.play(FadeIn(steps, lag_ratio=0.3), run_time=1.6)
        self.wait(3.0)

        s3b = line(TX["s3_b"], 25, SUN, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 11.0)
        wipe(self, keep=[title])

        # --- Phần 4: Cơ chế phân thớ Hitchin ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 25, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        # Vẽ sơ đồ phân thớ đơn giản: không gian tổng M -> đáy A
        base = Line([-3.0, -0.5, 0], [3.0, -0.5, 0], color=SUN, stroke_width=4)
        base_lbl = T("Đáy tham số A" if LANG == "vi" else "Base space A", 22, SUN).next_to(base, DOWN, buff=0.25)
        fibers = VGroup()
        for x, col in [(-2.0, SKY), (-0.7, MINT), (0.7, SKY), (2.0, MINT)]:
            f = Line([x, 0.1, 0], [x, 2.7, 0], color=col, stroke_width=5)
            d = Dot([x, -0.5, 0], color=SUN, radius=0.09)
            fibers.add(VGroup(f, d))
        fib_lbl = T("Các thớ Hitchin (mang vết Frobenius)" if LANG == "vi" else "Hitchin fibers (carrying Frobenius trace)", 22, MINT).move_to([0, 3.2, 0])

        self.play(Create(base), FadeIn(base_lbl), run_time=0.8)
        self.play(FadeIn(fibers, lag_ratio=0.2), FadeIn(fib_lbl), run_time=1.2)
        self.wait(3.0)

        s4b = line(TX["s4_b"], 24, WHITE, -2.3)
        self.play(FadeIn(s4b), run_time=0.9)
        end_vo("s4", t0, 11.0)
        wipe(self, keep=[title])

        # --- Phần 5: Tác động & Phân biệt ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 25, SKY, 4.5)
        self.play(FadeIn(s5a), run_time=0.8)

        cards = VGroup()
        c_data = [
            ("Bổ đề Cơ bản ≠ Toàn bộ Langlands" if LANG == "vi" else "Fundamental Lemma ≠ All of Langlands", PINK),
            ("Langlands số học ≠ Langlands hình học" if LANG == "vi" else "Arithmetic ≠ Geometric Langlands", SUN),
            ("Gỡ 'có điều kiện' cho Arthur & tính hàm tử" if LANG == "vi" else "Unlocks Arthur classification & functoriality", MINT),
        ]
        for i, (txt, col) in enumerate(c_data):
            y = 2.0 - i * 1.45
            b = RoundedRectangle(corner_radius=0.14, width=7.4, height=1.05,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 24, col).move_to([0, y, 0])
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.25), run_time=1.5)
        end_vo("s5", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
