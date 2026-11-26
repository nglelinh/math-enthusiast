from common_b import *
import json
import math

# Kiểm tra các ví dụ chòm chấp nhận được & cận dưới M(k) của Maynard
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def is_admissible(shifts):
    k = len(shifts)
    for p in range(2, k + 1):
        if is_prime(p):
            residues = {h % p for h in shifts}
            if len(residues) == p:
                return False
    return True

BAD_TUPLE = (0, 2, 4)
GOOD_TUPLE = (0, 2, 6)
assert not is_admissible(BAD_TUPLE)
assert {h % 3 for h in BAD_TUPLE} == {0, 1, 2}
assert is_admissible(GOOD_TUPLE)
assert {h % 2 for h in GOOD_TUPLE} == {0}
assert {h % 3 for h in GOOD_TUPLE} == {0, 2}

GOOD_INSTANCES = [(n, n + 2, n + 6) for n in (5, 11, 17, 41)]
for tup in GOOD_INSTANCES:
    assert all(is_prime(x) for x in tup)

# Cận dưới Maynard: M(k) > ln(k) - 2*ln(ln(k)) - 2
def maynard_lower(k):
    return math.log(k) - 2.0 * math.log(math.log(k)) - 2.0

assert maynard_lower(1000) > 1.0
assert maynard_lower(100_000) > 4.6  # vượt hẳn chặn cứng 4 của GPY

TX = {
    "title": {
        "vi": "Sàng Đa chiều Maynard–Tao\nTừ Bộ k số đến Vô hạn Cụm m Số",
        "en": "Maynard–Tao Multidimensional Sieve\nFrom k-Tuples to m-Prime Clusters",
    },
    "s1_a": {
        "vi": "Bước 1: Chòm chấp nhận được (Admissible k-tuple)\nKhông được phủ kín toàn bộ số dư theo bất kỳ p nào!",
        "en": "Step 1: Admissible k-tuples\nMust miss at least one residue class mod every prime p!",
    },
    "s1_b": {
        "vi": "{0, 2, 6} tránh được bội của 2 và 3:\ncho (5, 7, 11), (11, 13, 17), (17, 19, 23), (41, 43, 47)!",
        "en": "{0, 2, 6} avoids multiples of 2 and 3:\ngives (5, 7, 11), (11, 13, 17), (17, 19, 23), (41, 43, 47)!",
    },
    "s2_a": {
        "vi": "Bước 2: Vì sao sàng GPY 1 chiều (2005) bị kẹt\nngay sát vạch đích θ = 1/2?",
        "en": "Step 2: Why the 1D GPY sieve (2005) stalled\nright at the θ = 1/2 threshold",
    },
    "s2_b": {
        "vi": "GPY bị chặn cứng M(k) < 4 nên (θ/2)·M(k) < 1\nChạm đúng vạch 1 chứ không vượt qua nổi!",
        "en": "GPY caps at M(k) < 4, so (θ/2)·M(k) < 1:\nhits the wall at 1 without ever crossing it!",
    },
    "s3_a": {
        "vi": "Bước 3: Trọng số đa chiều F(t1, ..., tk)\ntrên đơn hình Δ(k) = {ti ≥ 0, ∑ti ≤ 1}",
        "en": "Step 3: Multidimensional weight F(t1, ..., tk)\non the simplex Δ(k) = {ti ≥ 0, ∑ti ≤ 1}",
    },
    "s3_b": {
        "vi": "M(k) > ln k − 2 ln ln k − 2 → ∞ !\nVới MỌI m ≥ 2, tồn tại vô hạn khoảng chứa m số nguyên tố!",
        "en": "M(k) > ln k − 2 ln ln k − 2 → ∞ !\nFor ANY m ≥ 2, bounded gaps hold m primes infinitely often!",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class MaynardSieve(Scene):
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

        title = line(TX["title"], 32, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Chòm chấp nhận được {0, 2, 4} vs {0, 2, 6} ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.7)

        # Thẻ bị loại: {0, 2, 4}
        bad_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.75, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 2.35, 0])
        bad_t1 = T("✗  BỊ LOẠI:  (n, n + 2, n + 4)" if LANG == "vi" else "✗  INADMISSIBLE:  (n, n + 2, n + 4)", 22, PINK).move_to([0, 2.8, 0])
        bad_t2 = T("mod 3:  {0, 2, 4} ≡ {0, 2, 1}  → phủ đủ 3/3 số dư!" if LANG == "vi" else "mod 3:  {0, 2, 4} ≡ {0, 2, 1}  → hits all 3 residues!", 20, WHITE).move_to([0, 2.25, 0])
        bad_t3 = T("Luôn có 1 số chia hết cho 3 (chỉ duy nhất (3, 5, 7))" if LANG == "vi" else "One term is always divisible by 3 (only (3, 5, 7) works)", 19, DIM).move_to([0, 1.75, 0])
        fit(bad_t2, 7.1)
        fit(bad_t3, 7.1)

        # Thẻ hợp lệ: {0, 2, 6}
        good_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.75, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 0.15, 0])
        good_t1 = T("✓  CHẤP NHẬN ĐƯỢC:  (n, n + 2, n + 6)" if LANG == "vi" else "✓  ADMISSIBLE:  (n, n + 2, n + 6)", 22, MINT).move_to([0, 0.6, 0])
        good_t2 = T("mod 2: chỉ {0}  |  mod 3: chỉ {0, 2} (tránh dư 1)" if LANG == "vi" else "mod 2: only {0}  |  mod 3: only {0, 2} (misses 1)", 20, WHITE).move_to([0, 0.05, 0])
        good_t3 = T("Chọn n ≡ 5 (mod 6) → tránh mọi bội của 2 và 3!" if LANG == "vi" else "Pick n ≡ 5 (mod 6) → avoids all multiples of 2 & 3!", 19, SUN).move_to([0, -0.45, 0])
        fit(good_t2, 7.1)
        fit(good_t3, 7.1)

        self.play(FadeIn(bad_card, bad_t1, bad_t2, bad_t3), run_time=1.1)
        self.play(FadeIn(good_card, good_t1, good_t2, good_t3), run_time=1.1)

        s1b = line(TX["s1_b"], 21, WHITE, -2.0)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Nút thắt 1 chiều của sàng GPY ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.7)

        gpy_box = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.45, fill_color=CARD, fill_opacity=1, stroke_color=ORANGE, stroke_width=2.5).move_to([0, 2.55, 0])
        gpy_t1 = T("Sàng GPY 1 chiều:  w(n) chỉ nhìn tích  d = d1·d2···dk" if LANG == "vi" else "1D GPY Sieve:  w(n) sees only the product  d = d1·d2···dk", 20, ORANGE).move_to([0, 2.85, 0])
        gpy_t2 = T("Không phân biệt ước thuộc về số hạng (n + hi) nào" if LANG == "vi" else "Cannot tell which divisor belongs to which shift (n + hi)", 19, WHITE).move_to([0, 2.25, 0])
        fit(gpy_t1, 7.1)
        fit(gpy_t2, 7.1)
        self.play(FadeIn(gpy_box, gpy_t1, gpy_t2), run_time=1.0)

        # Thước đo tiến tới vạch 1.0
        meter_bg = RoundedRectangle(corner_radius=0.12, width=7.5, height=1.85, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 0.35, 0])
        m_title = T("Điều kiện Dirichlet có trọng số:  (θ / 2) · M(k) > 1" if LANG == "vi" else "Weighted pigeonhole goal:  (θ / 2) · M(k) > 1", 20, WHITE).move_to([0, 0.92, 0])
        fit(m_title, 7.1)

        track = Rectangle(width=6.0, height=0.36, fill_color="#2c3247", fill_opacity=1, stroke_width=0).move_to([0, 0.25, 0])
        fill_bar = Rectangle(width=4.45, height=0.36, fill_color=PINK, fill_opacity=0.9, stroke_width=0).align_to(track, LEFT).set_y(0.25)
        wall = Line([1.5, -0.05, 0], [1.5, 0.62, 0], color=SUN, stroke_width=4)
        wall_lbl = T("Vạch 1,0" if LANG == "vi" else "Wall 1.0", 18, SUN).move_to([1.5, -0.28, 0])
        gpy_val = T("θ = 1/2, M(k) < 4  ⇒  < 1" if LANG == "vi" else "θ = 1/2, M(k) < 4  ⇒  < 1", 19, PINK).move_to([-1.1, -0.28, 0])

        self.play(FadeIn(meter_bg, m_title, track, wall, wall_lbl), run_time=0.8)
        self.play(GrowFromEdge(fill_bar, LEFT), FadeIn(gpy_val), run_time=1.0)

        s2b = line(TX["s2_b"], 22, WHITE, -1.9)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Trọng số đa chiều F(t1,...,tk) & M(k) -> ∞ ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.7)

        # Minh họa đơn hình Δ(2): t1 ≥ 0, t2 ≥ 0, t1 + t2 ≤ 1 (trái) + Công thức (phải)
        tri_card = RoundedRectangle(corner_radius=0.14, width=3.4, height=2.9, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([-2.0, 1.5, 0])
        orig = np.array([-3.0, 0.65, 0])
        ax_x = Line(orig, orig + [2.1, 0, 0], color=DIM, stroke_width=2.5)
        ax_y = Line(orig, orig + [0, 1.9, 0], color=DIM, stroke_width=2.5)
        simp = Polygon(orig, orig + [1.75, 0, 0], orig + [0, 1.6, 0], fill_color=MINT, fill_opacity=0.32, stroke_color=MINT, stroke_width=3)
        lbl_t1 = T("t1", 18, DIM).move_to(orig + [2.05, -0.22, 0])
        lbl_t2 = T("t2", 18, DIM).move_to(orig + [-0.28, 1.78, 0])
        lbl_d = T("Δ(k): ∑ti ≤ 1", 19, MINT).move_to([-2.0, 2.62, 0])

        info_card = RoundedRectangle(corner_radius=0.14, width=3.9, height=2.9, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([1.9, 1.5, 0])
        i1 = T("Tách riêng từng ước:" if LANG == "vi" else "Separate each divisor:", 19, SUN).move_to([1.9, 2.52, 0])
        i2 = T("d1 | (n+h1), ..., dk | (n+hk)", 18, WHITE).move_to([1.9, 2.02, 0])
        i3 = T("Quy về cực trị tích phân:" if LANG == "vi" else "Variational ratio:", 19, SKY).move_to([1.9, 1.42, 0])
        i4 = T("M(k) = sup  k·J(F) / I(F)", 19, MINT).move_to([1.9, 0.92, 0])
        i5 = T("k = 50 ⇒ H = 246 (m = 2)", 18, SUN).move_to([1.9, 0.38, 0])
        for m in (i1, i2, i3, i4, i5):
            fit(m, 3.6)

        self.play(FadeIn(tri_card, ax_x, ax_y, simp, lbl_t1, lbl_t2, lbl_d), run_time=1.1)
        self.play(FadeIn(info_card, i1, i2, i3, i4, i5), run_time=1.1)

        s3b = line(TX["s3_b"], 22, MINT, -1.75)
        self.play(FadeIn(s3b), run_time=0.9)
        end_vo("s3", t0, 9.5)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
