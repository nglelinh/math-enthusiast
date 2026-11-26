from common_b import *
import json
import math

# Kiểm tra toán học cho bài 02_07: Tính trộn định lượng, Khe phổ và Dưới lồi GL(2)
KAPPA = 0.5
DECAY_T0 = math.exp(-KAPPA * 0.0)
DECAY_T4 = math.exp(-KAPPA * 4.0)
DECAY_T10 = math.exp(-KAPPA * 10.0)
assert abs(DECAY_T0 - 1.0) < 1e-12
assert DECAY_T4 < 0.15 and DECAY_T10 < 0.01

THETA_CONVEX = 0.25
DELTA_SAVE = 0.02
THETA_SUB = THETA_CONVEX - DELTA_SAVE
assert THETA_SUB < THETA_CONVEX

TX = {
    "title": {
        "vi": "Khe phổ, Tính trộn &\nĐịnh lý Michel–Venkatesh",
        "en": "Spectral Gap, Mixing &\nMichel–Venkatesh Theorem",
    },
    "s1_a": {
        "vi": "Bước 1: Chuyển giá trị |L(1/2, π)|²\nthành tích phân chu trình trên G / Γ",
        "en": "Step 1: Rewrite |L(1/2, π)|²\nas a period integral on G / Γ",
    },
    "s1_b": {
        "vi": "Công thức Waldspurger biến tổng số học\nthành trung bình sóng φ dọc theo quỹ đạo đóng!",
        "en": "Waldspurger's formula turns an arithmetic sum\ninto averaging a wave φ along a closed orbit!",
    },
    "s2_a": {
        "vi": "Bước 2: Khe phổ κ > 0 ép tính trộn định lượng\nTương quan suy giảm hàm mũ theo e^(−κt)",
        "en": "Step 2: Spectral gap κ > 0 forces mixing\nCorrelations decay exponentially like e^(−κt)",
    },
    "s2_b": {
        "vi": "Ngay cả trên dãy lấy mẫu thưa (sparse),\nkhe phổ vẫn ép dao động triệt tiêu đều!",
        "en": "Even along sparse sample sequences,\nthe spectral gap forces oscillations to cancel!",
    },
    "s3_a": {
        "vi": "Bước 3: Định lý Michel–Venkatesh (2010)\nPhá vỡ bức tường lồi thống nhất cho mọi GL(2)!",
        "en": "Step 3: Michel–Venkatesh Theorem (2010)\nUniform subconvexity for all GL(2) L-functions!",
    },
    "s3_b": {
        "vi": "Đúng trên mọi trường số, mọi tham số:\nMở khóa QUE, điểm Heegner & bài toán Hilbert 11!",
        "en": "Valid over every number field & aspect:\nUnlocks QUE, Heegner points & Hilbert's 11th!",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class VenkateshSubconvexity(Scene):
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

        title = line(TX["title"], 33, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Tích phân chu trình trên G/Γ ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        b_left = RoundedRectangle(
            corner_radius=0.14, width=3.3, height=1.7,
            fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5
        ).move_to([-2.15, 1.55, 0])
        t_left = T("|L(1/2, π)|²\n(Tổng số học)" if LANG == "vi" else "|L(1/2, π)|²\n(Arithmetic sum)", 20, PINK).move_to(b_left)

        arr = Arrow([-0.4, 1.55, 0], [0.4, 1.55, 0], color=WHITE, buff=0.05, stroke_width=4)

        b_right = RoundedRectangle(
            corner_radius=0.14, width=3.3, height=1.7,
            fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5
        ).move_to([2.15, 1.55, 0])
        t_right = T("|∫ φ(x) dx|²\n(Chu trình G/Γ)" if LANG == "vi" else "|∫ φ(x) dx|²\n(Period on G/Γ)", 20, MINT).move_to(b_right)

        self.play(FadeIn(b_left, t_left), GrowArrow(arr), FadeIn(b_right, t_right), run_time=1.3)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 22, WHITE, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Tính trộn định lượng & Khe phổ ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        ax, ax_lab = mkaxes(
            [0, 10, 2], [0, 1.1, 0.5], 6.2, 2.7, [0.2, 1.5, 0],
            xt=[0, 4, 8],
            yt=[(0.0, "0"), (0.5, "0.5"), (1.0, "1")],
        )
        curve = ax.plot(lambda t: math.exp(-KAPPA * t), x_range=[0, 9.5], color=MINT, stroke_width=4)
        lbl_exp = T("Sai số trộn ≤ C · e^(−κt)" if LANG == "vi" else "Mixing error ≤ C · e^(−κt)", 20, MINT).move_to([1.2, 2.55, 0])
        lbl_gap = T("Khe phổ κ > 0" if LANG == "vi" else "Spectral gap κ > 0", 19, SUN).move_to([1.2, 1.95, 0])

        self.play(Create(ax), FadeIn(ax_lab), run_time=0.8)
        self.play(Create(curve), FadeIn(lbl_exp, lbl_gap), run_time=1.2)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 22, SUN, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Định lý Michel-Venkatesh (2010) ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        m_box = RoundedRectangle(
            corner_radius=0.16, width=7.6, height=2.5,
            fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=3
        ).move_to([0, 1.5, 0])
        m_txt = T(
            "Michel – Venkatesh (2010):\n\n|L(1/2, π)|  ≪  C^(1/4 − δ)\n\nThống nhất cho mọi hàm L của GL(2)!"
            if LANG == "vi" else
            "Michel – Venkatesh (2010):\n\n|L(1/2, π)|  ≪  C^(1/4 − δ)\n\nUniform for all GL(2) L-functions!",
            22, MINT
        ).move_to(m_box)
        self.play(FadeIn(m_box, m_txt), run_time=1.3)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 22, WHITE, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
