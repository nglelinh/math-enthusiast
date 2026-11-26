from common_b import *
import json
import math

# Kiểm tra các hằng số toán học cho lưới E8 từ bài 02_08
INT_VECTORS = math.comb(8, 2) * (2 ** 2)
HALF_VECTORS = (2 ** 8) // 2
KISSING_E8 = INT_VECTORS + HALF_VECTORS
R_E8 = math.sqrt(2) / 2
DELTA_E8 = (math.pi ** 4 / math.factorial(4)) * (R_E8 ** 8)

assert INT_VECTORS == 112
assert HALF_VECTORS == 128
assert KISSING_E8 == 240
assert abs(DELTA_E8 - math.pi ** 4 / 384) < 1e-12
assert abs(DELTA_E8 * 100 - 25.36695079) < 1e-5
for k in (1, 2, 3, 4):
    assert abs(math.sin(math.pi * (2 * k) / 2.0) ** 2) < 1e-15

TX = {
    "title": {
        "vi": "Viazovska (Fields 2022) &\nHàm kỳ diệu cho lưới E8",
        "en": "Viazovska (Fields 2022) &\nThe Magic Function for E8",
    },
    "s1_a": {
        "vi": "Lưới E8 trong R^8: tọa độ cùng nguyên\nhoặc cùng bán nguyên, tổng 8 tọa độ chẵn",
        "en": "E8 lattice in R^8: all integer or all\nhalf-integer coords, with an even sum",
    },
    "s1_b": {
        "vi": "Bán kính r = √2 / 2, ô cơ sở Vol = 1\n⇒ Mỗi quả cầu chạm khít 240 hàng xóm!",
        "en": "Radius r = √2 / 2, cell Vol = 1\n⇒ Every sphere touches 240 neighbors!",
    },
    "s2_a": {
        "vi": "Chặn trên Cohn–Elkies (2003):\n3 điều kiện dấu + Công thức tổng Poisson",
        "en": "Cohn–Elkies upper bound (2003):\n3 sign conditions + Poisson summation",
    },
    "s2_b": {
        "vi": "Mọi cách xếp (kể cả không phải lưới)\nđều có mật độ ≤ Vol(B(r / 2))!",
        "en": "Every packing (even non-lattice ones)\nhas density ≤ Vol(B(r / 2))!",
    },
    "s3_a": {
        "vi": "Để dấu bằng khớp đúng E8 (r = √2):\nf và f̂ phải có không điểm kép tại √2, √4, √6...",
        "en": "For equality to match E8 (r = √2):\nf and f̂ need double zeros at √2, √4, √6...",
    },
    "s3_b": {
        "vi": "Tách hàm riêng Fourier ±1:  f = (a + b) / 2\ncùng nhân tử sin²(π ||x||² / 2)!",
        "en": "Split ±1 Fourier eigenfunctions: f = (a + b)/2\nwith double-zero factor sin²(π ||x||² / 2)!",
    },
    "s4_a": {
        "vi": "Vũ khí bất ngờ: Biến đổi Laplace\nkết nối Fourier 8 chiều với Dạng modular!",
        "en": "The surprise weapon: Laplace transform\nlinks 8D Fourier symmetry to Modular Forms!",
    },
    "s4_b": {
        "vi": "Không cần siêu máy tính duyệt trường hợp:\nmột hàm kỳ diệu khóa chặt mọi cách xếp R^8!",
        "en": "No supercomputer casework needed:\none magic function seals all packings in R^8!",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


def make_card(txt, col, y, w=7.6, h=1.15, size=21):
    b = RoundedRectangle(
        corner_radius=0.14,
        width=w,
        height=h,
        fill_color=CARD,
        fill_opacity=1,
        stroke_color=col,
        stroke_width=2.5,
    ).move_to([0, y, 0])
    parts = txt.split("\n")
    ts = [T(p, size, col) for p in parts]
    g = VGroup(*ts).arrange(DOWN, buff=0.12) if len(ts) > 1 else ts[0]
    fit(g, w - 0.35).move_to(b)
    return VGroup(b, g)


class ViazovskaE8Magic(Scene):
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

        title = line(TX["title"], 33, WHITE, 6.2)
        self.add(title)

        # --- Đoạn 1: Đếm tay 240 vectơ ngắn nhất của E8 & mật độ π⁴/384 ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        pct_str = nf(DELTA_E8 * 100, 2)
        c1_txt = (
            f"1. Tọa độ nguyên: chọn 2 vị trí ±1, 6 vị trí 0\nC(8, 2) × 2² = 28 × 4 = {INT_VECTORS} vectơ"
            if LANG == "vi"
            else f"1. Integer type: two ±1, six 0s\nC(8, 2) × 2² = 28 × 4 = {INT_VECTORS} vectors"
        )
        c2_txt = (
            f"2. Bán nguyên: cả 8 tọa độ ±1/2 (số dấu − chẵn)\n2^8 / 2 = {HALF_VECTORS} vectơ   (||x||² = 2)"
            if LANG == "vi"
            else f"2. Half-integer: all eight ±1/2 (even # of −)\n2^8 / 2 = {HALF_VECTORS} vectors   (||x||² = 2)"
        )
        c3_txt = (
            f"Tổng số hôn:  {INT_VECTORS} + {HALF_VECTORS} = {KISSING_E8} vectơ ngắn nhất\nMật độ E8:  δ = π⁴ / 384 ≈ {pct_str}%"
            if LANG == "vi"
            else f"Kissing number:  {INT_VECTORS} + {HALF_VECTORS} = {KISSING_E8} shortest vectors\nE8 density:  δ = π⁴ / 384 ≈ {pct_str}%"
        )

        c1 = make_card(c1_txt, MINT, 2.55, h=1.22, size=20)
        c2 = make_card(c2_txt, SKY, 1.05, h=1.22, size=20)
        c3 = make_card(c3_txt, SUN, -0.50, h=1.32, size=21)

        self.play(FadeIn(c1), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(c2), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(c3), run_time=1.0)
        self.wait(1.2)

        s1b = line(TX["s1_b"], 23, WHITE, -2.55)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Đoạn 2: Chứng minh 4 dòng chặn trên Cohn–Elkies ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        cond = make_card(
            "Điều kiện:  f(0) = f̂(0) = 1\nf(x) ≤ 0 (khi ||x|| ≥ r)   và   f̂(ξ) ≥ 0 (mọi ξ)"
            if LANG == "vi"
            else "Conditions:  f(0) = f̂(0) = 1\nf(x) ≤ 0 (for ||x|| ≥ r)   and   f̂(ξ) ≥ 0 (all ξ)",
            SKY,
            2.90,
            h=1.10,
            size=20,
        )
        p1 = make_card(
            "1 = f(0)  ≥  ∑ f(x)    (vì f(x) ≤ 0 với x ≠ 0)"
            if LANG == "vi"
            else "1 = f(0)  ≥  ∑ f(x)    (since f(x) ≤ 0 for x ≠ 0)",
            MINT,
            1.50,
            h=0.92,
            size=20,
        )
        p2 = make_card(
            "=  (1 / Vol) · ∑ f̂(ξ)    [Công thức tổng Poisson]"
            if LANG == "vi"
            else "=  (1 / Vol) · ∑ f̂(ξ)    [Poisson summation]",
            SUN,
            0.35,
            h=0.92,
            size=20,
        )
        p3 = make_card(
            "≥  f̂(0) / Vol  =  1 / Vol    ⇒    Vol(R^n / Λ) ≥ 1!"
            if LANG == "vi"
            else "≥  f̂(0) / Vol  =  1 / Vol    ⇒    Vol(R^n / Λ) ≥ 1!",
            PINK,
            -0.80,
            h=0.95,
            size=21,
        )

        self.play(FadeIn(cond), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(p1), run_time=0.9)
        self.wait(1.0)
        self.play(FadeIn(p2), run_time=0.9)
        self.wait(1.0)
        self.play(FadeIn(p3), run_time=0.9)
        self.wait(1.2)

        s2b = line(TX["s2_b"], 23, WHITE, -2.65)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- Đoạn 3: Không điểm kép tại √2, √4, √6 & tách hàm riêng Fourier ±1 ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 22, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        ax, ax_lab = mkaxes(
            xr=[0, 2.8, 0.5],
            yr=[-0.45, 1.15, 0.5],
            w=6.8,
            h=3.0,
            c=[0.1, 1.85, 0],
            xt=(),
            yt=[(0, "0"), (1, "1")],
        )
        zero_line = DashedLine(
            ax.c2p(0, 0), ax.c2p(2.8, 0), color=DIM, stroke_width=2
        )

        def magic_vis(x):
            if x <= math.sqrt(2):
                return (1.0 - (x * x) / 2.0) * math.exp(-0.28 * x * x)
            return -0.36 * math.exp(-0.35 * (x - math.sqrt(2))) * (math.sin(math.pi * x * x / 2.0) ** 2)

        curve = ax.plot(magic_vis, x_range=[0.0, 2.72], color=MINT, stroke_width=4)

        zeros = VGroup()
        for val, lbl in [(math.sqrt(2), "√2"), (2.0, "√4"), (math.sqrt(6), "√6")]:
            pt = ax.c2p(val, 0)
            dot = Dot(pt, radius=0.09, color=SUN)
            t_lbl = T(lbl, 20, SUN).next_to(pt, UP, buff=0.16)
            zeros.add(VGroup(dot, t_lbl))

        f_tag = T("f(r)", 22, MINT).next_to(ax.c2p(0.35, 0.85), RIGHT, buff=0.12)
        self.play(FadeIn(ax, ax_lab, zero_line), run_time=0.8)
        self.play(Create(curve), FadeIn(f_tag), run_time=1.3)
        self.play(FadeIn(zeros, lag_ratio=0.3), run_time=1.0)
        self.wait(1.2)

        eig_card = make_card(
            "Viazovska tách:   f = (a + b) / 2\nâ = +a  (trị riêng +1)   |   b̂ = −b  (trị riêng −1)"
            if LANG == "vi"
            else "Viazovska splits:   f = (a + b) / 2\nâ = +a  (eigenvalue +1)  |  b̂ = −b  (eigenvalue −1)",
            SUN,
            -0.85,
            h=1.22,
            size=20,
        )
        self.play(FadeIn(eig_card), run_time=1.0)
        self.wait(1.0)

        s3b = line(TX["s3_b"], 22, WHITE, -2.75)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)
        wipe(self, keep=[title])

        # --- Đoạn 4: Dạng modular (E2, E4, E6, Δ) qua biến đổi Laplace ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 23, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        m1 = make_card(
            "Biến đổi Laplace trên nửa mặt phẳng trên:\na(x) = sin²(π||x||² / 2) · ∫ φ(it) e^(−π||x||²t) dt"
            if LANG == "vi"
            else "Laplace transform on the upper half-plane:\na(x) = sin²(π||x||² / 2) · ∫ φ(it) e^(−π||x||²t) dt",
            SKY,
            2.65,
            h=1.25,
            size=19,
        )
        arr1 = T("↓   τ ↦ −1/τ  khớp biến đổi Fourier 8D!" if LANG == "vi" else "↓   τ ↦ −1/τ  mirrors 8D Fourier transform!", 19, DIM).move_to([0, 1.65, 0])

        m2 = make_card(
            "φ(τ) viết tường minh từ  E2, E4, E6  và  Δ\nKhông gian dạng modular cực nhỏ ⇒ xác định duy nhất!"
            if LANG == "vi"
            else "φ(τ) built explicitly from  E2, E4, E6  and  Δ\nModular space is tiny ⇒ uniquely pinned down!",
            SUN,
            0.65,
            h=1.25,
            size=19,
        )
        arr2 = T("↓   Kiểm tra dấu chặt chẽ bằng giải tích" if LANG == "vi" else "↓   Sign conditions verified analytically", 19, DIM).move_to([0, -0.35, 0])

        m3 = make_card(
            "Định lý Viazovska (2016):  E8 tối ưu tuyệt đối!\nδ(E8) = π⁴ / 384  ·  Bài báo 23 trang  ·  Fields 2022"
            if LANG == "vi"
            else "Viazovska's Theorem (2016):  E8 is optimal!\nδ(E8) = π⁴ / 384  ·  23-page paper  ·  Fields 2022",
            MINT,
            -1.35,
            h=1.28,
            size=20,
        )

        self.play(FadeIn(m1), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(arr1), FadeIn(m2), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(arr2), FadeIn(m3), run_time=1.0)
        self.wait(1.2)

        s4b = line(TX["s4_b"], 22, WHITE, -3.20)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
