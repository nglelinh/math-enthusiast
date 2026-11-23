from common_b import *
import json

TX = {
    "title": {"vi": "Phân thớ Hitchin & Đếm điểm\n(Cốt lõi chứng minh Ngô Bảo Châu)", "en": "Hitchin Fibration & Point Counting\n(Core of Ngô's Proof)"},
    "s1_a": {"vi": "Làm sao hình học 'biết' giá trị của một\ntích phân quỹ đạo trên trường p-adic?", "en": "How can geometry 'know' the value of\na p-adic orbital integral?"},
    "s1_b": {"vi": "Trên trường hữu hạn F_q: tích phân quỹ đạo\n= đếm số điểm (có trọng số) trên đa tạp!", "en": "Over a finite field F_q: orbital integral\n= weighted point count on a variety!"},
    "s2_a": {"vi": "Công thức vết Grothendieck–Lefschetz:\nSố điểm  =  Vết của phép Frobenius", "en": "Grothendieck–Lefschetz Trace Formula:\nPoint count  =  Trace of Frobenius"},
    "s2_b": {"vi": "Nếu hai phía nội soi có cùng 'gói đối đồng điều'\n⇒ Vết Frobenius bằng nhau ⇒ Tích phân bằng nhau!", "en": "If endoscopic sides share the same cohomology\n⇒ Equal Frobenius traces ⇒ Equal integrals!"},
    "s3_a": {"vi": "Tại sao cần cả một PHÂN THỚ Hitchin M → A\nthay vì xét từng đa tạp riêng lẻ?", "en": "Why a whole HITCHIN FIBRATION M → A\ninstead of isolated varieties?"},
    "s3_b": {"vi": "Định lý về giá (Ngô): Không có thành phần ẩn\nnằm ngoài vùng trơn ⇒ truyền thông tin theo tham số!", "en": "Support Theorem (Ngô): No hidden components\noutside the smooth locus ⇒ control across the family!"},
    "s4_a": {"vi": "Cuộc chạy tiếp sức lịch sử:\n1980s → Laumon–Ngô (2004) → Ngô (2010)", "en": "The historical relay:\n1980s → Laumon–Ngô (2004) → Ngô (2010)"},
}

# Kiểm tra tính nhất quán số lượng điểm đếm ví dụ trên F_q (q = 3, P¹ có q + 1 = 4 điểm)
q_ex = 3
assert q_ex + 1 == 4
assert 2010 - 2004 == 6


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class LanglandsHitchinFibration(Scene):
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

        # --- s1: Tích phân -> Đếm điểm ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 25, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        b1 = RoundedRectangle(corner_radius=0.14, width=6.8, height=1.1, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 2.3, 0])
        t1 = T("Tích phân quỹ đạo p-adic  O_γ(f)" if LANG == "vi" else "p-adic Orbital Integral  O_γ(f)", 24, PINK).move_to(b1)
        arr = Arrow([0, 1.6, 0], [0, 0.7, 0], color=SUN, stroke_width=4)
        b2 = RoundedRectangle(corner_radius=0.14, width=6.8, height=1.1, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 0.0, 0])
        t2 = T("# Điểm trên thớ Springer affine (F_q)" if LANG == "vi" else "# Points on affine Springer fiber (F_q)", 23, MINT).move_to(b2)
        self.play(FadeIn(b1), FadeIn(t1), run_time=0.9)
        self.play(Create(arr), FadeIn(b2), FadeIn(t2), run_time=1.0)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, SUN, -1.9)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- s2: Vết Frobenius & Đối đồng điều ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 25, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        frob_box = RoundedRectangle(corner_radius=0.14, width=7.4, height=1.5, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 1.8, 0])
        frob_t = T("# X(F_q)  =  ∑ (-1)^i · Tr( Frob | H^i(X, Q_ℓ) )", 22, SUN).move_to(frob_box)
        self.play(FadeIn(frob_box), FadeIn(frob_t), run_time=1.0)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 24, MINT, -0.5)
        self.play(FadeIn(s2b), run_time=0.9)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- s3: Phân thớ Hitchin & Định lý về giá ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        # Thớ trơn vs thớ kỳ dị trên đáy A
        base = Line([-3.1, -0.3, 0], [3.1, -0.3, 0], color=SUN, stroke_width=4)
        fibs = VGroup()
        for x, col, lbl in [(-2.1, MINT, "Trơn"), (-0.7, MINT, "Trơn"), (0.8, PINK, "Kỳ dị"), (2.1, MINT, "Trơn")]:
            f = Line([x, 0.2, 0], [x, 2.5, 0], color=col, stroke_width=5)
            d = Dot([x, -0.3, 0], color=col, radius=0.09)
            lt = T(lbl if LANG == "vi" else ("Smooth" if col == MINT else "Singular"), 19, col).next_to(d, DOWN, buff=0.2)
            fibs.add(VGroup(f, d, lt))
        self.play(Create(base), FadeIn(fibs, lag_ratio=0.2), run_time=1.4)
        self.wait(2.5)

        s3b = line(TX["s3_b"], 24, WHITE, -2.2)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 11.0)
        wipe(self, keep=[title])

        # --- s4: Cuộc chạy tiếp sức Laumon-Ngô -> Ngô ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 25, SKY, 4.5)
        self.play(FadeIn(s4a), run_time=0.8)

        cards = VGroup()
        c_data = [
            ("Langlands–Shelstad, Kottwitz, Waldspurger, Hales", SKY),
            ("Laumon–Ngô (2004): Đột phá cho nhóm unita U(n)" if LANG == "vi" else "Laumon–Ngô (2004): Breakthrough for U(n)", SUN),
            ("Ngô Bảo Châu (2010): Định lý tổng quát (IHÉS)" if LANG == "vi" else "Ngô Bảo Châu (2010): General Lie algebras (IHÉS)", MINT),
        ]
        for i, (txt, col) in enumerate(c_data):
            y = 2.2 - i * 1.4
            b = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.0, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.3), run_time=1.5)
        end_vo("s4", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
