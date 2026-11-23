from common_b import *
import json

TX = {
    "title": {"vi": "Andrew Wiles & Định lý Fermat:\nTừ phương trình đến modular", "en": "Andrew Wiles & Fermat:\nFrom equations to modularity"},
    "s1_a": {"vi": "Năm 1637, Fermat khẳng định với n ≥ 3:\naⁿ + bⁿ = cⁿ vô nghiệm nguyên dương", "en": "In 1637, Fermat claimed for n ≥ 3:\naⁿ + bⁿ = cⁿ has no positive integer solutions"},
    "s1_b": {"vi": "Trái hẳn với n = 2 (Pytago):\n3² + 4² = 5²,  5² + 12² = 13², ... (vô hạn!)", "en": "Unlike n = 2 (Pythagoras):\n3² + 4² = 5²,  5² + 12² = 13², ... (infinitely many!)"},
    "s2_a": {"vi": "Bẫy 'suýt đúng':\n1782¹² + 1841¹²  vs  1922¹²", "en": "Near-miss trap:\n1782¹² + 1841¹²  vs  1922¹²"},
    "s2_b": {"vi": "Kiểm tra chẵn lẻ (mod 2):\nchẵn + lẻ = lẻ ≠ chẵn ⇒ sai ngay lập tức!", "en": "Parity check (mod 2):\neven + odd = odd ≠ even ⇒ false immediately!"},
    "s3_a": {"vi": "Bước ngoặt Frey (1985): nếu aᵖ + bᵖ = cᵖ,\ndựng đường cong elliptic E: y² = x(x − aᵖ)(x + bᵖ)", "en": "Frey (1985): if aᵖ + bᵖ = cᵖ,\nbuild elliptic curve E: y² = x(x − aᵖ)(x + bᵖ)"},
    "s3_b": {"vi": "Đường cong Frey nửa ổn định nhưng có\nbiệt thức Δ = 16(abc)²ᵖ cực kỳ bất thường!", "en": "The Frey curve is semistable yet has\nan impossibly strange discriminant Δ = 16(abc)²ᵖ!"},
    "s4_a": {"vi": "Chuỗi lập luận Ribet (1986) → Wiles (1995):\nMọi đường cong nửa ổn định đều phải modular", "en": "Ribet (1986) → Wiles (1995):\nEvery semistable elliptic curve is modular"},
    "s4_b": {"vi": "Hạ bậc Ribet ép E ứng với dạng modular\ncấp N = 2 — nhưng không có dạng nào như vậy!", "en": "Ribet level-lowering forces a level N = 2\nmodular form — none exists! ⇒ Contradiction!"},
    "end": {"vi": "Giải Abel 2016: không chỉ giải 1 phương trình,\nmà mở ra kỷ nguyên hình học số học mới", "en": "Abel Prize 2016: a new era connecting\nelliptic curves, Galois reps & modular forms"},
}

assert 3**2 + 4**2 == 5**2
assert 5**2 + 12**2 == 13**2
assert (1782**12 + 1841**12) % 2 == 1 and (1922**12) % 2 == 0
assert 1782**12 + 1841**12 != 1922**12


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class WilesFermat(Scene):
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
                rem = vo_durs[sid] - (float(self.time) - t0) + 1.0
                self.wait(max(0.6, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 36, WHITE, 6.2)
        self.add(title)

        # --- Phần 1 ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, PINK, 4.6)
        s1b = line(TX["s1_b"], 26, MINT, 2.5)
        self.play(FadeIn(s1a), run_time=0.8)
        self.wait(3.5)
        self.play(FadeIn(s1b), run_time=0.8)
        tri = Polygon([-1.8, -2.8, 0], [1.2, -2.8, 0], [-1.8, -0.5, 0], color=MINT, fill_color=CARD, fill_opacity=0.8, stroke_width=3.5)
        l_a = T("3", 28, MINT).next_to(tri, LEFT, buff=0.2)
        l_b = T("4", 28, MINT).next_to(tri, DOWN, buff=0.2)
        l_c = T("5", 28, SUN).move_to([0.1, -1.35, 0])
        self.play(Create(tri), FadeIn(l_a), FadeIn(l_b), FadeIn(l_c), run_time=1.2)
        end_vo("s1", t0, 8.0)
        wipe(self, keep=[title])

        # --- Phần 2 ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 28, SUN, 4.4)
        self.play(FadeIn(s2a), run_time=0.8)
        box = RoundedRectangle(corner_radius=0.14, width=7.2, height=2.2,
                               fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 1.2, 0])
        eq_t = VGroup(
            T("1782¹²  ⇒  chẵn (mod 2 ≡ 0)" if LANG == "vi" else "1782¹²  ⇒  even (mod 2 ≡ 0)", 25, SKY),
            T("1841¹²  ⇒  lẻ   (mod 2 ≡ 1)" if LANG == "vi" else "1841¹²  ⇒  odd  (mod 2 ≡ 1)", 25, SUN),
            T("1922¹²  ⇒  chẵn (mod 2 ≡ 0)" if LANG == "vi" else "1922¹²  ⇒  even (mod 2 ≡ 0)", 25, PINK),
        ).arrange(DOWN, buff=0.22).move_to(box)
        self.play(FadeIn(box), FadeIn(eq_t, lag_ratio=0.2), run_time=1.5)
        self.wait(3.0)
        s2b = line(TX["s2_b"], 26, PINK, -1.6)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 3 ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)
        ax, _ = mkaxes((-2.5, 2.5, 1), (-3.0, 3.0, 1), 6.2, 4.0, [0, 0.4, 0])
        # Đường cong elliptic mẫu y^2 = x^3 - x
        xs_pos = np.linspace(1.001, 2.1, 80)
        xs_mid = np.linspace(-0.999, 0.0, 80)
        g1 = ax.plot_line_graph(xs_pos, np.sqrt(xs_pos**3 - xs_pos), add_vertex_dots=False, line_color=SUN, stroke_width=3.5)
        g2 = ax.plot_line_graph(xs_pos, -np.sqrt(xs_pos**3 - xs_pos), add_vertex_dots=False, line_color=SUN, stroke_width=3.5)
        g3 = ax.plot_line_graph(xs_mid, np.sqrt(np.maximum(0, xs_mid**3 - xs_mid)), add_vertex_dots=False, line_color=SUN, stroke_width=3.5)
        g4 = ax.plot_line_graph(xs_mid, -np.sqrt(np.maximum(0, xs_mid**3 - xs_mid)), add_vertex_dots=False, line_color=SUN, stroke_width=3.5)
        self.play(Create(ax), Create(g1), Create(g2), Create(g3), Create(g4), run_time=1.8)
        s3b = line(TX["s3_b"], 25, PINK, -3.2)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 4 ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 25, MINT, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)
        steps_txt = [
            ("1. aᵖ + bᵖ = cᵖ", SKY),
            ("2. Đường cong Frey E" if LANG == "vi" else "2. Frey curve E", SUN),
            ("3. Wiles: E là modular" if LANG == "vi" else "3. Wiles: E is modular", MINT),
            ("4. Ribet: cấp N = 2 ⇒ ∅ (⊥)" if LANG == "vi" else "4. Ribet: level N = 2 ⇒ ∅ (⊥)", PINK),
        ]
        boxes = VGroup()
        for idx, (st, col) in enumerate(steps_txt):
            y = 2.5 - idx * 1.35
            b = RoundedRectangle(corner_radius=0.14, width=6.6, height=0.95,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(st, 26, col).move_to([0, y, 0])
            boxes.add(VGroup(b, t))
        self.play(FadeIn(boxes, lag_ratio=0.35), run_time=2.2)
        s4b = line(TX["s4_b"], 25, WHITE, -3.6)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 11.0)
        wipe(self, keep=[title])

        # --- Phần 5 ---
        t0 = start_vo("s5")
        end_c = line(TX["end"], 28, SUN, 1.0)
        sum_box = RoundedRectangle(corner_radius=0.16, width=7.2, height=2.5,
                                   fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, -2.0, 0])
        sum_t = VGroup(
            T("aⁿ + bⁿ = cⁿ (n ≥ 3) ⇒ Vô nghiệm!" if LANG == "vi" else "aⁿ + bⁿ = cⁿ (n ≥ 3) ⇒ No solutions!", 26, MINT),
            T("Elliptic Curves ↔ Modular Forms", 25, SKY),
        ).arrange(DOWN, buff=0.3).move_to(sum_box)
        self.play(FadeIn(end_c), FadeIn(sum_box), FadeIn(sum_t), run_time=1.2)
        end_vo("s5", t0, 8.0)

        tl_out = os.environ.get("VO_TIMELINE_JSON", "")
        if tl_out:
            with open(tl_out, "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
