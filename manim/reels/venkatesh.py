from common_b import *
import json
import math

# Kiểm tra toán học cho bài 02_07: Động lực học thuần nhất, Chặn lồi 1/4 và Tổng ba bình phương
def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def count_sphere_points(D):
    r = int(math.isqrt(D))
    cnt = 0
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            rem = D - x * x - y * y
            if rem < 0:
                continue
            z = int(math.isqrt(rem))
            if z * z == rem:
                cnt += 1 if z == 0 else 2
    return cnt

# 1. Định thức dòng trắc địa a(t) và dòng horocycle u(s)
for t_val in (0.0, 0.5, 1.2):
    assert abs(det2([[math.exp(t_val), 0.0], [0.0, math.exp(-t_val)]]) - 1.0) < 1e-12
for s_val in (0.0, 1.0, 2.5):
    assert abs(det2([[1.0, s_val], [0.0, 1.0]]) - 1.0) < 1e-12

# 2. Chặn lồi Phragmén-Lindelöf cho hàm zeta Riemann: trung bình của 0 và 1/2
EXP_RIGHT = 0.0
EXP_LEFT = 0.5
EXP_CONVEX = 0.5 * (EXP_RIGHT + EXP_LEFT)
assert abs(EXP_CONVEX - 0.25) < 1e-12

# 3. Số nghiệm nguyên của x² + y² + z² = D
N_D3 = count_sphere_points(3)
N_D5 = count_sphere_points(5)
N_D14 = count_sphere_points(14)
assert N_D3 == 8 and N_D5 == 24 and N_D14 == 48

TX = {
    "title": {
        "vi": "Venkatesh (Fields 2018) &\nĐộng lực học Thuần nhất",
        "en": "Venkatesh (Fields 2018) &\nHomogeneous Dynamics",
    },
    "s1_a": {
        "vi": "Không gian lưới X2 = SL(2, R) / SL(2, Z)\nMỗi điểm là một lưới diện tích 1 trên R²!",
        "en": "Space of lattices X2 = SL(2, R) / SL(2, Z)\nEach point is a unit-area lattice in R²!",
    },
    "s1_b": {
        "vi": "Nhân phải bởi ma trận nguyên γ ∈ SL(2, Z)\nchỉ đổi cơ sở, giữ nguyên y hệt lưới cũ!",
        "en": "Multiplying on the right by γ ∈ SL(2, Z)\nchanges basis but keeps the exact same lattice!",
    },
    "s2_a": {
        "vi": "Hai dòng ma trận cơ bản trên X2:\nDòng trắc địa a(t) & Dòng horocycle u(s)",
        "en": "Two fundamental flows acting on X2:\nGeodesic flow a(t) & Horocycle flow u(s)",
    },
    "s2_b": {
        "vi": "Diện tích ô cơ sở luôn giữ bằng 1,\nnhưng quỹ đạo có thể cuốn dày đặc khắp X2!",
        "en": "Cell area always stays exactly 1,\nyet orbits can wind densely across all of X2!",
    },
    "s3_a": {
        "vi": "Chặn lồi 1/4 của hàm zeta Riemann:\nNội suy tuyến tính giữa hai biên σ = 0 và 1",
        "en": "The 1/4 convexity bound for Riemann zeta:\nLinear interpolation between σ = 0 and σ = 1",
    },
    "s3_b": {
        "vi": "Hạ số mũ xuống 1/4 − δ (dưới lồi)\nđòi hỏi sự triệt tiêu sâu sắc giữa các dao động!",
        "en": "Lowering the exponent to 1/4 − δ (subconvexity)\nproves deep cancellation among oscillations!",
    },
    "s4_a": {
        "vi": "Phân bố đều nghiệm nguyên x² + y² + z² = D\nkhi chiếu lên mặt cầu đơn vị S²:",
        "en": "Equidistribution of x² + y² + z² = D\nprojected onto the unit sphere S²:",
    },
    "s4_b": {
        "vi": "Khi D → ∞, các điểm trải đều khắp mặt cầu\n⇔ tương đương một ước lượng dưới lồi hàm L!",
        "en": "As D → ∞, points spread evenly across S²\n⇔ equivalent to a subconvexity bound!",
    },
    "s5_a": {
        "vi": "Phong cách tổng hợp của Akshay Venkatesh\n(Huy chương Fields 2018):",
        "en": "Akshay Venkatesh's synthesis method\n(2018 Fields Medal):",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class VenkateshOverview(Scene):
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

        # --- Phần 1: Không gian lưới SL(2, R) / SL(2, Z) ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        b1 = RoundedRectangle(
            corner_radius=0.14, width=3.55, height=2.4,
            fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5
        ).move_to([-2.0, 1.5, 0])
        sq = Square(side_length=1.05, color=MINT, stroke_width=3).move_to([-2.0, 1.9, 0])
        dots1 = VGroup(*[
            Dot([-2.0 + dx * 0.525, 1.9 + dy * 0.525, 0], radius=0.05, color=MINT)
            for dx in (-1, 1) for dy in (-1, 1)
        ])
        l1 = T("Cơ sở (1,0), (0,1)\ndet = 1" if LANG == "vi" else "Basis (1,0), (0,1)\ndet = 1", 18, MINT).move_to([-2.0, 0.8, 0])

        b2 = RoundedRectangle(
            corner_radius=0.14, width=3.55, height=2.4,
            fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5
        ).move_to([2.0, 1.5, 0])
        para = Polygon(
            [1.15, 1.38, 0], [2.2, 1.38, 0], [2.85, 2.43, 0], [1.8, 2.43, 0],
            color=SUN, stroke_width=3
        )
        dots2 = VGroup(*[Dot(p, radius=0.05, color=SUN) for p in ([1.15, 1.38, 0], [2.2, 1.38, 0], [2.85, 2.43, 0], [1.8, 2.43, 0])])
        l2 = T("Cơ sở (1,0), (1,1)\ncùng lưới Z²!" if LANG == "vi" else "Basis (1,0), (1,1)\nsame lattice Z²!", 18, SUN).move_to([2.0, 0.8, 0])

        eq_lbl = T("=", 38, WHITE).move_to([0, 1.65, 0])
        self.play(FadeIn(b1, sq, dots1, l1), FadeIn(b2, para, dots2, l2), FadeIn(eq_lbl), run_time=1.3)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 22, WHITE, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Dòng trắc địa a(t) và Dòng horocycle u(s) ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        c_geo = RoundedRectangle(
            corner_radius=0.14, width=7.6, height=1.7,
            fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5
        ).move_to([0, 2.15, 0])
        t_geo = T(
            "Dòng trắc địa a(t) = diag(e^t, e^(−t))\nKéo dài trục hoành e^t lần, nén trục tung e^(−t) lần"
            if LANG == "vi" else
            "Geodesic flow a(t) = diag(e^t, e^(−t))\nStretches x-axis by e^t, squeezes y-axis by e^(−t)",
            20, MINT
        ).move_to(c_geo)

        c_hor = RoundedRectangle(
            corner_radius=0.14, width=7.6, height=1.7,
            fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5
        ).move_to([0, 0.1, 0])
        t_hor = T(
            "Dòng horocycle u(s) = [[1, s], [0, 1]]\nTrượt nghiêng lưới ngang một đoạn s (tuần hoàn s = 1)"
            if LANG == "vi" else
            "Horocycle flow u(s) = [[1, s], [0, 1]]\nShears lattice horizontally by s (period 1 on Z²)",
            20, SUN
        ).move_to(c_hor)

        self.play(FadeIn(c_geo, t_geo), run_time=1.0)
        self.play(FadeIn(c_hor, t_hor), run_time=1.0)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 22, WHITE, -2.0)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Chặn lồi 1/4 của hàm zeta Riemann ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        ax, ax_lab = mkaxes(
            [0, 1.1, 0.5], [0, 0.6, 0.25], 6.0, 2.8, [0.2, 1.5, 0],
            xt=[0, 0.5, 1],
            yt=[(0.0, "0"), (0.25, "1/4"), (0.5, "1/2")],
            xfmt=lambda v: "0" if v == 0 else ("1/2" if v == 0.5 else "1"),
        )
        p_left = ax.c2p(0, 0.5)
        p_mid = ax.c2p(0.5, 0.25)
        p_right = ax.c2p(1, 0.0)
        conv_line = Line(p_left, p_right, color=PINK, stroke_width=4)
        d_left = Dot(p_left, color=SUN, radius=0.09)
        d_right = Dot(p_right, color=SUN, radius=0.09)
        d_mid = Dot(p_mid, color=PINK, radius=0.11)
        lbl_mid = T("Chặn lồi: 1/4" if LANG == "vi" else "Convexity: 1/4", 20, PINK).next_to(d_mid, UR, buff=0.12)

        p_sub = ax.c2p(0.5, 0.13)
        arr_sub = Arrow(p_mid, p_sub, color=MINT, buff=0.08, stroke_width=4)
        lbl_sub = T("Dưới lồi: 1/4 − δ" if LANG == "vi" else "Subconvex: 1/4 − δ", 20, MINT).next_to(p_sub, RIGHT, buff=0.15)

        self.play(Create(ax), FadeIn(ax_lab), run_time=0.9)
        self.play(Create(conv_line), FadeIn(d_left, d_right, d_mid, lbl_mid), run_time=1.0)
        self.play(GrowArrow(arr_sub), FadeIn(lbl_sub), run_time=0.9)
        self.wait(1.8)

        s3b = line(TX["s3_b"], 22, MINT, -2.0)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 4: Phân bố đều nghiệm nguyên x² + y² + z² = D trên mặt cầu ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 23, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        rows = [
            (f"D = 3:   {N_D3} nghiệm  (±1, ±1, ±1)  →  8 đỉnh lập phương" if LANG == "vi"
             else f"D = 3:   {N_D3} points  (±1, ±1, ±1)  →  cube vertices", MINT),
            (f"D = 5:   {N_D5} nghiệm  (hoán vị ±2, ±1, 0)" if LANG == "vi"
             else f"D = 5:   {N_D5} points  (permutations of ±2, ±1, 0)", SKY),
            (f"D = 14:  {N_D14} nghiệm  (hoán vị ±3, ±2, ±1)" if LANG == "vi"
             else f"D = 14:  {N_D14} points  (permutations of ±3, ±2, ±1)", SUN),
        ]
        cards = VGroup()
        for i, (txt, col) in enumerate(rows):
            y = 2.45 - i * 1.25
            b = RoundedRectangle(
                corner_radius=0.14, width=7.6, height=0.95,
                fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5
            ).move_to([0, y, 0])
            t = T(txt, 20, col).move_to([0, y, 0])
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.3), run_time=1.4)
        self.wait(2.0)

        s4b = line(TX["s4_b"], 22, WHITE, -1.9)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 5: Phong cách tổng hợp của Venkatesh (Fields 2018) ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 24, SKY, 4.6)
        self.play(FadeIn(s5a), run_time=0.8)

        pillars = VGroup()
        p_data = [
            ("1. Đặt bài toán số học lên không gian lưới G / Γ" if LANG == "vi"
             else "1. Move arithmetic problems onto G / Γ", MINT),
            ("2. Dùng tính trộn, khe phổ & tô pô để giải mã" if LANG == "vi"
             else "2. Use mixing, spectral gap & topology", SKY),
            ("3. Đưa kết quả về phá vỡ rào cản hàm L" if LANG == "vi"
             else "3. Translate back to break L-function walls", SUN),
        ]
        for i, (txt, col) in enumerate(p_data):
            y = 2.1 - i * 1.4
            b = RoundedRectangle(
                corner_radius=0.14, width=7.6, height=1.05,
                fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5
            ).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            pillars.add(VGroup(b, t))
        self.play(FadeIn(pillars, lag_ratio=0.25), run_time=1.4)
        end_vo("s5", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
