from common_b import *
import json

TX = {
    "title": {"vi": "Định lý Bất toàn Gödel (1931):\nGiới hạn của hệ tiên đề", "en": "Gödel's Incompleteness (1931):\nLimits of formal systems"},
    "s1_a": {"vi": "Giấc mơ Hilbert: xây hệ tiên đề T\nNhất quán + Đầy đủ + Kiểm tra bằng máy", "en": "Hilbert's dream: a formal theory T\nConsistent + Complete + Effective"},
    "s1_b": {"vi": "Gödel (1931): Mọi hệ T đủ mạnh (chứa số học)\nđều không thể vừa nhất quán vừa đầy đủ!", "en": "Gödel (1931): Any T strong enough for arithmetic\ncannot be both consistent and complete!"},
    "s2_a": {"vi": "Số hóa Gödel: biến công thức thành số\nVí dụ: ký hiệu '0' → 1,  '=' → 3", "en": "Gödel numbering: formulas become integers\nExample: '0' → 1,  '=' → 3"},
    "s2_b": {"vi": "Công thức '0 = 0' (mã 1, 3, 1):\n2¹ × 3³ × 5¹ = 2 × 27 × 5 = 270", "en": "Formula '0 = 0' (codes 1, 3, 1):\n2¹ × 3³ × 5¹ = 2 × 27 × 5 = 270"},
    "s2_c": {"vi": "Chứng minh cũng có mã m ⇒ quan hệ Proof_T(m, n)\ntrở thành bài toán số học thuần túy!", "en": "Proofs also get a code m ⇒ Proof_T(m, n)\nbecomes pure arithmetic!"},
    "s3_a": {"vi": "Tự quy chiếu: dựng câu G có mã g nói rằng\n'G không chứng minh được trong T'", "en": "Self-reference: build sentence G (code g)\nsaying 'G is not provable in T'"},
    "s3_b": {"vi": "Nếu T nhất quán: giả sử T ⊢ G ⇒ tồn tại chứng minh m\n⇒ T ⊢ Prov_T(g) ⇒ T ⊢ ¬G ⇒ Mâu thuẫn!", "en": "If T is consistent: suppose T ⊢ G ⇒ a proof m exists\n⇒ T ⊢ Prov_T(g) ⇒ T ⊢ ¬G ⇒ Contradiction!"},
    "s3_c": {"vi": "Vậy T ⊬ G! Nhưng G nói đúng sự thật\n⇒ G ĐÚNG nhưng KHÔNG chứng minh được trong T", "en": "Thus T ⊬ G! Yet G states the truth\n⇒ G is TRUE but UNPROVABLE in T"},
    "s4_a": {"vi": "Định lý thứ hai: bên trong T chứng minh được\nCon(T) → G", "en": "Second theorem: inside T one proves\nCon(T) → G"},
    "s4_b": {"vi": "Nếu T ⊢ Con(T) ⇒ T ⊢ G (vô lý!)\nThêm G làm tiên đề mới T' ⇒ lại sinh G' mới!", "en": "If T ⊢ Con(T) ⇒ T ⊢ G (impossible!)\nAdd G as a new axiom T' ⇒ a new G' appears!"},
    "s5_a": {"vi": "Bất toàn ≠ Không nhất quán ≠ 'Chân lý tương đối'\nCùng một phép đường chéo ở cả 3 đỉnh cao:", "en": "Incompleteness ≠ Inconsistency ≠ 'Relativism'\nOne diagonal trick across three landmarks:"},
}

# Kiểm tra toán học số Gödel
godel_0_eq_0 = (2**1) * (3**3) * (5**1)
assert godel_0_eq_0 == 270


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class GodelIncompleteness(Scene):
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

        title = line(TX["title"], 36, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Chương trình Hilbert ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)
        pillars = VGroup()
        p_data = [
            ("1. Nhất quán (Consistent)" if LANG == "vi" else "1. Consistent (no φ ∧ ¬φ)", MINT),
            ("2. Đầy đủ (Complete)" if LANG == "vi" else "2. Complete (φ or ¬φ)", SUN),
            ("3. Hiệu quả (Effective)" if LANG == "vi" else "3. Effective (checkable)", SKY),
        ]
        for i, (txt, col) in enumerate(p_data):
            y = 2.3 - i * 1.15
            b = RoundedRectangle(corner_radius=0.14, width=6.6, height=0.88,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 25, col).move_to([0, y, 0])
            pillars.add(VGroup(b, t))
        self.play(FadeIn(pillars, lag_ratio=0.25), run_time=1.5)
        self.wait(3.0)
        s1b = line(TX["s1_b"], 25, PINK, -1.9)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 2: Đánh số Gödel ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 26, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)
        sym_box = RoundedRectangle(corner_radius=0.14, width=7.0, height=2.6,
                                   fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 1.5, 0])
        s2b = line(TX["s2_b"], 26, SUN, 1.5)
        self.play(FadeIn(sym_box), FadeIn(s2b), run_time=1.2)
        self.wait(4.5)
        # Mũi tên phân tích ngược 270 -> '0 = 0'
        rev_t = T("270 = 2¹·3³·5¹  ⇒  [1, 3, 1]  ⇒  '0 = 0'", 24, MINT).move_to([0, -0.6, 0])
        self.play(FadeIn(rev_t), run_time=0.9)
        self.wait(3.0)
        s2c = line(TX["s2_c"], 25, WHITE, -2.5)
        self.play(FadeIn(s2c), run_time=0.8)
        end_vo("s2", t0, 12.0)
        wipe(self, keep=[title])

        # --- Phần 3: Câu tự quy chiếu G ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 26, SUN, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)
        g_box = RoundedRectangle(corner_radius=0.14, width=6.8, height=1.3,
                                 fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.8).move_to([0, 2.5, 0])
        g_txt = T("G  ⇔  ¬Prov_T(g)", 32, SUN).move_to(g_box)
        self.play(FadeIn(g_box), FadeIn(g_txt), run_time=1.0)
        self.wait(3.5)
        s3b = line(TX["s3_b"], 24, PINK, 0.3)
        self.play(FadeIn(s3b), run_time=0.8)
        self.wait(4.5)
        s3c = line(TX["s3_c"], 25, MINT, -2.1)
        self.play(FadeIn(s3c), run_time=0.8)
        end_vo("s3", t0, 12.0)
        wipe(self, keep=[title])

        # --- Phần 4: Định lý thứ hai Con(T) ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 28, SKY, 4.4)
        self.play(FadeIn(s4a), run_time=0.8)
        c_box = RoundedRectangle(corner_radius=0.14, width=6.8, height=1.8,
                                 fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([0, 1.8, 0])
        c_txt = VGroup(
            T("T ⊢ Con(T) → G", 28, SKY),
            T("T ⊢ Con(T)  ⇒  T ⊢ G  (⊥)" if LANG == "vi" else "T ⊢ Con(T)  ⇒  T ⊢ G  (⊥)", 26, PINK),
        ).arrange(DOWN, buff=0.25).move_to(c_box)
        self.play(FadeIn(c_box), FadeIn(c_txt), run_time=1.2)
        self.wait(4.0)
        s4b = line(TX["s4_b"], 25, SUN, -1.2)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 5: Tổng kết Cantor - Gödel - Turing ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 25, WHITE, 4.4)
        self.play(FadeIn(s5a), run_time=0.8)
        sibs = VGroup()
        sib_data = [
            ("Cantor (1891): ℝ thoát mọi danh sách" if LANG == "vi" else "Cantor (1891): ℝ escapes any list", SKY),
            ("Gödel (1931): G thoát mọi chứng minh trong T" if LANG == "vi" else "Gödel (1931): G escapes proofs in T", SUN),
            ("Turing (1936): D thoát mọi máy quyết định H" if LANG == "vi" else "Turing (1936): D escapes decider H", MINT),
        ]
        for i, (st, col) in enumerate(sib_data):
            y = 1.8 - i * 1.3
            b = RoundedRectangle(corner_radius=0.14, width=7.2, height=0.95,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = fit(T(st, 24, col), 6.6).move_to([0, y, 0])
            sibs.add(VGroup(b, t))
        self.play(FadeIn(sibs, lag_ratio=0.3), run_time=1.5)
        end_vo("s5", t0, 10.0)

        tl_out = os.environ.get("VO_TIMELINE_JSON", "")
        if tl_out:
            with open(tl_out, "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
