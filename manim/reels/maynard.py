from common_b import *
import json
import math

# Kiểm tra các hằng số và ví dụ toán học từ bài 02_09
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

PRIMES_120 = [n for n in range(2, 120) if is_prime(n)]
TWIN_EXAMPLES = [(3, 5), (11, 13), (29, 31), (101, 103)]
for a, b in TWIN_EXAMPLES:
    assert is_prime(a) and is_prime(b) and b - a == 2

SAMPLE_PRIMES = [29, 31, 37, 41, 43, 47]
assert all(is_prime(p) for p in SAMPLE_PRIMES)
SAMPLE_GAPS = [SAMPLE_PRIMES[i + 1] - SAMPLE_PRIMES[i] for i in range(len(SAMPLE_PRIMES) - 1)]
assert SAMPLE_GAPS == [2, 6, 4, 2, 4]

AVG_GAP_100 = math.log(10 ** 100)
assert 230.0 < AVG_GAP_100 < 230.5

BOUNDS = [
    ("Zhang (2013)", 70_000_000, PINK),
    ("Polymath8a (2013)", 4_680, ORANGE),
    ("Maynard (2013)", 600, SKY),
    ("Polymath8b (2014)", 246, MINT),
]
assert [b[1] for b in BOUNDS] == [70_000_000, 4_680, 600, 246]
assert BOUNDS[0][1] // BOUNDS[-1][1] > 284_000

TX = {
    "title": {
        "vi": "James Maynard (Fields 2022)\nKhoảng cách giữa các Số nguyên tố",
        "en": "James Maynard (Fields 2022)\nBounded Gaps Between Primes",
    },
    "s1_a": {
        "vi": "Số nguyên tố càng đi xa càng thưa dần\nnhưng thỉnh thoảng vẫn đứng sát cạnh nhau!",
        "en": "Primes grow sparser as numbers get larger,\nyet close pairs keep popping up!",
    },
    "s1_b": {
        "vi": "Khoảng cách trung bình quanh x là ln(x)\nGần 10^100: trung bình ≈ 230, nhưng vẫn có gap = 2!",
        "en": "Average gap near x is ln(x)\nNear 10^100: average ≈ 230, yet gap 2 persists!",
    },
    "s2_a": {
        "vi": "Bước ngoặt lịch sử — Yitang Zhang (2013):\nLần đầu chứng minh tồn tại chặn hữu hạn!",
        "en": "Historic breakthrough — Yitang Zhang (2013):\nFirst proof of a finite gap bound!",
    },
    "s2_b": {
        "vi": "Zhang vượt qua ngưỡng θ = 1/2 với môđun trơn\nMở tung bức tường đóng kín suốt hàng thế kỷ!",
        "en": "Zhang pushed past θ = 1/2 for smooth moduli,\ncracking open a centuries-old wall!",
    },
    "s3_a": {
        "vi": "Cuộc đua hạ chặn sau Zhang (2013–2014):\nSàng đa chiều của Maynard & Terence Tao",
        "en": "The race to shrink the bound (2013–2014):\nMaynard & Terence Tao's multidimensional sieve",
    },
    "s3_b": {
        "vi": "Chỉ dùng Bombieri–Vinogradov (θ = 1/2)\nMaynard kéo xuống 600, Polymath8b hạ còn 246!",
        "en": "Using only Bombieri–Vinogradov (θ = 1/2),\nMaynard reached 600, Polymath8b reached 246!",
    },
    "s4_a": {
        "vi": "Cẩn thận nhầm lẫn: 246 ≠ Số nguyên tố sinh đôi!\nGiả thuyết gap = 2 vẫn CÒN MỞ",
        "en": "Careful: 246 ≠ Twin Prime Conjecture!\nInfinitely many gap-2 pairs remain OPEN",
    },
    "s4_b": {
        "vi": "Rào cản chẵn lẻ (Parity barrier):\nSàng khó phân biệt 1 số nguyên tố với tích 2 số!",
        "en": "The parity barrier of sieve theory:\nSieves cannot tell 1 prime from a product of 2!",
    },
    "s5_a": {
        "vi": "Chiến thắng của cả cộng đồng toán học\nvà sức mạnh chiếc sàng của James Maynard:",
        "en": "A triumph of mathematical collaboration\nand the power of Maynard's sieve:",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class MaynardOverview(Scene):
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
                self.wait(max(0.7, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 33, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Khoảng cách giữa các số nguyên tố ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 24, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.7)

        # Trục số từ 28 đến 48 minh họa số nguyên tố và khoảng cách
        nl = Line([-3.7, 1.8, 0], [3.7, 1.8, 0], color=DIM, stroke_width=3)
        self.play(Create(nl), run_time=0.6)

        def x_pos(val):
            return -3.5 + (val - 28) * (7.0 / 20.0)

        p_dots = VGroup()
        p_lbls = VGroup()
        for p in SAMPLE_PRIMES:
            x = x_pos(p)
            col = MINT if p in (29, 31, 41, 43) else SKY
            dot = Dot([x, 1.8, 0], radius=0.11, color=col)
            lbl = T(str(p), 20, col).move_to([x, 1.32, 0])
            p_dots.add(dot)
            p_lbls.add(lbl)
        self.play(FadeIn(p_dots, lag_ratio=0.15), FadeIn(p_lbls, lag_ratio=0.15), run_time=1.0)

        arcs = VGroup()
        for i in range(len(SAMPLE_PRIMES) - 1):
            p1, p2 = SAMPLE_PRIMES[i], SAMPLE_PRIMES[i + 1]
            g = p2 - p1
            col = SUN if g == 2 else DIM
            a = ArcBetweenPoints([x_pos(p1), 1.95, 0], [x_pos(p2), 1.95, 0], angle=-1.1, color=col, stroke_width=2.5)
            gl = T(f"+{g}", 18, col).move_to([(x_pos(p1) + x_pos(p2)) / 2, 2.55 if g > 2 else 2.38, 0])
            arcs.add(VGroup(a, gl))
        self.play(FadeIn(arcs, lag_ratio=0.2), run_time=1.0)

        tw_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.15, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 0.1, 0])
        tw_txt = T(
            "Cặp sinh đôi (gap = 2):  (3, 5), (11, 13), (29, 31), (101, 103)..."
            if LANG == "vi" else
            "Twin pairs (gap = 2):  (3, 5), (11, 13), (29, 31), (101, 103)...",
            20, SUN,
        ).move_to(tw_card)
        fit(tw_txt, 7.1)
        self.play(FadeIn(tw_card, tw_txt), run_time=0.8)

        s1b = line(TX["s1_b"], 22, WHITE, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 8.5)
        wipe(self, keep=[title])

        # --- Phần 2: Đột phá Yitang Zhang (2013) ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 24, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.7)

        z_box = RoundedRectangle(corner_radius=0.16, width=7.6, height=2.5, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=3).move_to([0, 1.5, 0])
        z_head = T("Định lý Yitang Zhang (4/2013)" if LANG == "vi" else "Yitang Zhang's Theorem (Apr 2013)", 24, PINK).move_to([0, 2.25, 0])
        z_eq = T("liminf (p(n+1) − p(n))  ≤  70.000.000" if LANG == "vi" else "liminf (p(n+1) − p(n))  ≤  70,000,000", 26, WHITE).move_to([0, 1.4, 0])
        fit(z_eq, 7.1)
        z_sub = T(
            "Có vô hạn cặp số nguyên tố cách nhau ≤ 70 triệu"
            if LANG == "vi" else
            "Infinitely many prime pairs at most 70 million apart",
            20, SUN,
        ).move_to([0, 0.65, 0])
        fit(z_sub, 7.1)
        self.play(FadeIn(z_box, z_head), run_time=0.8)
        self.play(FadeIn(z_eq), FadeIn(z_sub), run_time=1.0)

        s2b = line(TX["s2_b"], 22, WHITE, -1.5)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 8.0)
        wipe(self, keep=[title])

        # --- Phần 3: Cuộc đua hạ chặn 70M -> 4680 -> 600 -> 246 ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 24, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.7)

        # Thanh log10 biểu diễn độ sụt giảm ấn tượng
        max_log = math.log10(70_000_000)
        bars = VGroup()
        for i, (label, val, col) in enumerate(BOUNDS):
            y = 2.65 - i * 1.18
            w_bar = max(1.15, 6.2 * (math.log10(val) / max_log))
            bg = RoundedRectangle(corner_radius=0.1, width=7.5, height=0.88, fill_color=CARD, fill_opacity=1, stroke_color=DIM, stroke_width=1.2).move_to([0, y, 0])
            bar = RoundedRectangle(corner_radius=0.08, width=w_bar, height=0.38, fill_color=col, fill_opacity=0.88, stroke_width=0)
            bar.align_to([-3.5, 0, 0], LEFT).set_y(y - 0.16)
            val_str = f"{val:,}".replace(",", ".") if LANG == "vi" else f"{val:,}"
            t_lbl = T(f"{label}:  ≤ {val_str}", 20, col).align_to([-3.5, 0, 0], LEFT).set_y(y + 0.21)
            bars.add(VGroup(bg, bar, t_lbl))
        self.play(FadeIn(bars, lag_ratio=0.3), run_time=1.6)

        s3b = line(TX["s3_b"], 22, MINT, -2.3)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 8.5)
        wipe(self, keep=[title])

        # --- Phần 4: Phân biệt với Giả thuyết Số nguyên tố sinh đôi ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 24, PINK, 4.6)
        self.play(FadeIn(s4a), run_time=0.7)

        c_twin = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.2, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 2.55, 0])
        t_twin = T(
            "Số nguyên tố sinh đôi (MỞ):  liminf (p(n+1) − p(n)) = 2"
            if LANG == "vi" else
            "Twin Primes (OPEN):  liminf (p(n+1) − p(n)) = 2",
            21, SUN,
        ).move_to(c_twin)
        fit(t_twin, 7.1)

        arr_down = T("⇓   (suy ra được)" if LANG == "vi" else "⇓   (implies)", 22, MINT).move_to([-1.6, 1.45, 0])
        arr_up = T("⇎   (KHÔNG đảo được!)" if LANG == "vi" else "⇎   (does NOT reverse!)", 22, PINK).move_to([1.6, 1.45, 0])

        c_bnd = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.2, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 0.35, 0])
        t_bnd = T(
            "Khoảng cách bị chặn (ĐÃ CHỨNG MINH):  liminf ≤ 246"
            if LANG == "vi" else
            "Bounded Gaps (PROVED):  liminf ≤ 246",
            21, MINT,
        ).move_to(c_bnd)
        fit(t_bnd, 7.1)

        self.play(FadeIn(c_twin, t_twin), run_time=0.8)
        self.play(FadeIn(c_bnd, t_bnd), FadeIn(arr_down, arr_up), run_time=1.0)

        s4b = line(TX["s4_b"], 22, WHITE, -1.65)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 8.5)
        wipe(self, keep=[title])

        # --- Phần 5: Tổng kết cộng đồng & Di sản ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 24, SKY, 4.6)
        self.play(FadeIn(s5a), run_time=0.7)

        rows = [
            (
                "1. Zhang (2013): mở cửa với chặn ≤ 70.000.000"
                if LANG == "vi" else
                "1. Zhang (2013): opened the door with ≤ 70,000,000",
                PINK,
            ),
            (
                "2. Maynard & Tao: sàng đa chiều → 600 (Polymath8b: 246)"
                if LANG == "vi" else
                "2. Maynard & Tao: 2D+ sieve → 600 (Polymath8b: 246)",
                MINT,
            ),
            (
                "3. Tổng quát: vô hạn khoảng bị chặn chứa m số nguyên tố!"
                if LANG == "vi" else
                "3. Beyond pairs: bounded intervals with m primes for any m!",
                SUN,
            ),
        ]
        cards = VGroup()
        for i, (txt, col) in enumerate(rows):
            y = 2.15 - i * 1.45
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=1.05, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 20, col).move_to(b)
            fit(t, 7.2)
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.25), run_time=1.3)
        end_vo("s5", t0, 8.5)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
