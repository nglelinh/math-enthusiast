from common_b import *
import json
import math

# Kiểm tra các hằng số toán học về chữ số bị cấm & số nguyên tố không chứa chữ số 7
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

EXP_NO7 = math.log10(9)
assert 0.954 < EXP_NO7 < 0.955
assert 9 ** 6 == 531_441
assert (9 / 10) ** 50 < 0.0052

PRIMES_NO7 = [p for p in range(2, 100) if is_prime(p) and "7" not in str(p)]
assert 7 not in PRIMES_NO7 and 17 not in PRIMES_NO7 and 37 not in PRIMES_NO7
assert all(x in PRIMES_NO7 for x in (2, 3, 5, 11, 13, 19, 23, 29, 31, 41, 43, 83, 89))

TX = {
    "title": {
        "vi": "Số nguyên tố không chứa Chữ số 7\n& Bức tranh Fields 2022",
        "en": "Primes Missing the Digit 7\n& the 2022 Fields Medal Picture",
    },
    "s1_a": {
        "vi": "Định lý Maynard (2019): Có VÔ HẠN số nguyên tố\nkhông chứa chữ số 7 trong hệ thập phân!",
        "en": "Maynard (2019): There are INFINITELY MANY primes\nwith NO digit 7 in base 10!",
    },
    "s1_b": {
        "vi": "Tập số không có chữ số 7 cực mỏng: mật độ (9/10)^N → 0\nMaynard kết hợp giải tích Fourier đường tròn + phương pháp sàng!",
        "en": "7-free numbers are sparse: density (9/10)^N → 0\nMaynard fused Fourier circle method + sieve theory!",
    },
    "s2_a": {
        "vi": "Giả thuyết Duffin–Schaeffer (1941)\nKoukoulopoulos & Maynard chứng minh năm 2019!",
        "en": "Duffin–Schaeffer Conjecture (1941)\nProved by Koukoulopoulos & Maynard (2019)!",
    },
    "s2_b": {
        "vi": "Dùng 'đồ thị ƯCLN' (GCD graphs) đo chồng lấp phân số\nGiải trọn bài toán mở gần 80 năm của xấp xỉ Diophantine!",
        "en": "Using 'GCD graphs' to control rational overlaps,\nsettling an 80-year-old problem in Diophantine approximation!",
    },
    "s3_a": {
        "vi": "Bức tranh Huy chương Fields 2022 của James Maynard:\nKhông chỉ 246, mà là 4 trụ cột lý thuyết số!",
        "en": "James Maynard's 2022 Fields Medal:\nFar beyond 246 — four pillars of number theory!",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class MaynardDigits(Scene):
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

        # --- Phần 1: Số nguyên tố không chứa chữ số 7 ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.7)

        # Lưới 10 chữ số 0..9 (2 hàng x 5 cột), gạch chéo số 7
        tiles = VGroup()
        cross_7 = None
        for d in range(10):
            row = d // 5
            col_i = d % 5
            x = -2.8 + col_i * 1.4
            y = 2.65 - row * 1.25
            is_7 = (d == 7)
            box = RoundedRectangle(
                corner_radius=0.12, width=1.1, height=0.95,
                fill_color=CARD, fill_opacity=1,
                stroke_color=PINK if is_7 else MINT, stroke_width=2.5,
            ).move_to([x, y, 0])
            txt = T(str(d), 30, PINK if is_7 else WHITE).move_to(box)
            grp = VGroup(box, txt)
            if is_7:
                l1 = Line([x - 0.42, y - 0.36, 0], [x + 0.42, y + 0.36, 0], color=PINK, stroke_width=4)
                l2 = Line([x - 0.42, y + 0.36, 0], [x + 0.42, y - 0.36, 0], color=PINK, stroke_width=4)
                cross_7 = VGroup(l1, l2)
            tiles.add(grp)

        self.play(FadeIn(tiles, lag_ratio=0.06), run_time=1.0)
        self.play(Create(cross_7), run_time=0.6)

        dens_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.25, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, -0.05, 0])
        dens_t1 = T("Số ≤ 10^N không có chữ số 7:  chỉ còn 9^N ≈ (10^N)^0,954" if LANG == "vi" else "Integers ≤ 10^N without digit 7:  only 9^N ≈ (10^N)^0.954", 20, SUN).move_to([0, 0.22, 0])
        dens_t2 = T("Ví dụ nguyên tố:  2, 3, 5, 11, 13, 19, 23, 29, 31, 41, 43..." if LANG == "vi" else "Sample primes:  2, 3, 5, 11, 13, 19, 23, 29, 31, 41, 43...", 19, MINT).move_to([0, -0.32, 0])
        fit(dens_t1, 7.1)
        fit(dens_t2, 7.1)
        self.play(FadeIn(dens_card, dens_t1, dens_t2), run_time=0.9)

        s1b = line(TX["s1_b"], 21, WHITE, -1.95)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 8.5)
        wipe(self, keep=[title])

        # --- Phần 2: Giả thuyết Duffin–Schaeffer (2019) ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.7)

        ds_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.85, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 2.1, 0])
        ds_t1 = T("Xấp xỉ số thực α bằng phân số tối giản a/q:" if LANG == "vi" else "Approximating real α by reduced fractions a/q:", 20, SUN).move_to([0, 2.65, 0])
        ds_t2 = T("|α − a/q| < ψ(q)  vô hạn lần với hầu hết α" if LANG == "vi" else "|α − a/q| < ψ(q)  infinitely often for almost all α", 21, WHITE).move_to([0, 2.08, 0])
        ds_t3 = T("⟺  ∑ φ(q) · ψ(q) = ∞   (tiêu chuẩn 0–1)" if LANG == "vi" else "⟺  ∑ φ(q) · ψ(q) = ∞   (zero–one law)", 21, MINT).move_to([0, 1.5, 0])
        for m in (ds_t1, ds_t2, ds_t3):
            fit(m, 7.1)

        gcd_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.2, fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([0, 0.05, 0])
        gcd_t = T("Ý tưởng đột phá:  Đồ thị ƯCLN (GCD graphs)\nkiểm soát sự chồng lấp giữa các khoảng quanh a/q" if LANG == "vi" else "Key breakthrough:  GCD graphs\nmeasure overlap between intervals around a/q", 20, SKY).move_to(gcd_card)
        fit(gcd_t, 7.1)

        self.play(FadeIn(ds_card, ds_t1, ds_t2, ds_t3), run_time=1.1)
        self.play(FadeIn(gcd_card, gcd_t), run_time=0.9)

        s2b = line(TX["s2_b"], 21, WHITE, -1.85)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 8.5)
        wipe(self, keep=[title])

        # --- Phần 3: 4 trụ cột Huy chương Fields 2022 ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.7)

        pillars = [
            ("1. Khoảng cách nhỏ:  sàng đa chiều → ≤ 246 & cụm m số" if LANG == "vi" else "1. Small gaps:  multidim sieve → ≤ 246 & m-clusters", MINT),
            ("2. Khoảng cách lớn:  giải thưởng 10.000 USD của Erdős" if LANG == "vi" else "2. Large gaps:  solved Erdős's $10,000 prize problem", ORANGE),
            ("3. Chữ số bị cấm:  vô hạn số nguyên tố thiếu chữ số 7" if LANG == "vi" else "3. Restricted digits:  infinitely many primes missing 7", SKY),
            ("4. Duffin–Schaeffer:  xấp xỉ Diophantine (với Koukoulopoulos)" if LANG == "vi" else "4. Duffin–Schaeffer:  Diophantine approx (w/ Koukoulopoulos)", SUN),
        ]
        cards = VGroup()
        for i, (txt, col) in enumerate(pillars):
            y = 2.55 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.95, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 20, col).move_to(b)
            fit(t, 7.2)
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.22), run_time=1.3)
        end_vo("s3", t0, 8.5)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
