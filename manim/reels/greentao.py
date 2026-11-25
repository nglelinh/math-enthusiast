from common_b import *
import json

TX = {
    "title": {"vi": "Định lý Green–Tao (2004/2008):\nCấp số cộng trong Số nguyên tố", "en": "Green–Tao Theorem (2004/2008):\nArithmetic Progressions in Primes"},
    "s1_a": {"vi": "Với mọi k ≥ 1, tồn tại cấp số cộng độ dài k\ngồm toàn các số nguyên tố!", "en": "For every k ≥ 1, there is a k-term\narithmetic progression of primes!"},
    "s1_b": {"vi": "Lưu ý: Đây là định lý tồn tại —\nchỉ dãy tồn tại, chưa tìm số đầu nhỏ nhất", "en": "Note: Existence theorem —\ndoes not give the smallest starting prime"},
    "s2_a": {"vi": "Nghịch lý: π(x) ~ x / ln(x)\n⇒ Mật độ tự nhiên của số nguyên tố bằng 0!", "en": "Paradox: π(x) ~ x / ln(x)\n⇒ Natural density of primes is 0!"},
    "s2_b": {"vi": "Định lý Szemerédi (1975) cần mật độ d̄(A) > 0\n⇒ Không thể áp dụng thẳng cho số nguyên tố!", "en": "Szemerédi's Theorem (1975) needs d̄(A) > 0\n⇒ Cannot apply directly to the primes!"},
    "s3_a": {"vi": "Giải pháp: Xây hàm trội giả ngẫu nhiên ν(n)\nbọc lấy trọng số von Mangoldt Λ(n)", "en": "Solution: Build pseudorandom majorant ν(n)\nbounding the von Mangoldt weight Λ(n)"},
    "s3_b": {"vi": "ν(n) dựng từ sàng bao (kiểu Selberg):\nđủ mượt để chuẩn Gowers U^(k−1) kiểm soát!", "en": "ν(n) built from enveloping sieve (Selberg):\nsmooth enough for Gowers norms U^(k−1)!"},
    "s4_a": {"vi": "Nguyên lý chuyển (Transference):\nThưa trong ℤ, nhưng DÀY tương đối so với ν!", "en": "Transference Principle:\nSparse in ℤ, yet DENSE relative to ν!"},
    "s4_b": {"vi": "Áp dụng Szemerédi tương đối dưới ν\n⇒ Chuyển ngược về cấp số cộng nguyên tố thật", "en": "Apply relative Szemerédi under ν\n⇒ Transfer back to real prime progressions"},
    "s5_a": {"vi": "Phân biệt rõ những điều Green–Tao\nCÓ nói và KHÔNG nói:", "en": "What Green–Tao DOES and DOES NOT say:"},
}

# Kiểm tra các ví dụ cấp số cộng nguyên tố từ bài học
def is_prime(n):
    return n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

ap3 = [3, 5, 7]
ap5 = [5, 11, 17, 23, 29]
ap6 = [7, 37, 67, 97, 127, 157]
assert all(is_prime(x) for x in ap3 + ap5 + ap6)
assert all(ap5[i+1] - ap5[i] == 6 for i in range(4))
assert all(ap6[i+1] - ap6[i] == 30 for i in range(5))


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class GreenTaoTheorem(Scene):
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

        # --- Phần 1: Ví dụ cấp số cộng nguyên tố ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        aps = VGroup()
        ap_data = [
            ("k = 3, d = 2:   3,  5,  7", MINT),
            ("k = 5, d = 6:   5,  11,  17,  23,  29", SUN),
            ("k = 6, d = 30:  7,  37,  67,  97,  127,  157", SKY),
        ]
        for i, (txt, col) in enumerate(ap_data):
            y = 2.4 - i * 1.2
            b = RoundedRectangle(corner_radius=0.14, width=7.4, height=0.9,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            aps.add(VGroup(b, t))
        self.play(FadeIn(aps, lag_ratio=0.3), run_time=1.5)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, WHITE, -1.8)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 2: Mật độ 0 & Rào cản Szemerédi ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 26, PINK, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        # Minh họa mật độ giảm dần
        bars = VGroup()
        dens = [("≤ 10²: 25%", 2.5, MINT), ("≤ 10⁴: 12%", 1.5, SUN), ("≤ 10⁶: 7.8%", 0.9, PINK), ("x → ∞: 0%", 0.2, PINK)]
        for i, (lbl, w, col) in enumerate(dens):
            y = 2.5 - i * 0.85
            t = T(lbl, 22, WHITE).move_to([-2.3, y, 0])
            bar = Rectangle(width=w, height=0.45, fill_color=col, fill_opacity=0.85, stroke_width=0).align_to([-0.5, y, 0], LEFT).set_y(y)
            bars.add(VGroup(t, bar))
        self.play(FadeIn(bars, lag_ratio=0.25), run_time=1.5)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 25, SUN, -1.9)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 3: Hàm trội giả ngẫu nhiên ν ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        outer = RoundedRectangle(corner_radius=0.18, width=7.2, height=2.6,
                                 fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=3).move_to([0, 1.5, 0])
        outer_t = T("Hàm trội giả ngẫu nhiên ν(n)  (Sàng bao)" if LANG == "vi" else "Pseudorandom majorant ν(n)  (Enveloping sieve)", 23, SUN).move_to([0, 2.35, 0])
        inner = RoundedRectangle(corner_radius=0.14, width=6.0, height=1.1,
                                 fill_color="#1d2233", fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 1.0, 0])
        inner_t = T("Trọng số nguyên tố Λ(n) ≤ C · ν(n)" if LANG == "vi" else "Prime weight Λ(n) ≤ C · ν(n)", 24, MINT).move_to(inner)
        self.play(FadeIn(outer), FadeIn(outer_t), FadeIn(inner), FadeIn(inner_t), run_time=1.2)
        self.wait(2.5)

        s3b = line(TX["s3_b"], 25, WHITE, -1.6)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 4: Nguyên lý chuyển ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 25, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        flow = VGroup()
        f_data = [
            ("1. Tách Λ = phần cấu trúc + phần ngẫu nhiên" if LANG == "vi" else "1. Split Λ = structured + uniform", SKY),
            ("2. Áp dụng Szemerédi tương đối dưới ν" if LANG == "vi" else "2. Relative Szemerédi under ν", MINT),
            ("3. Chuyển AP về các số nguyên tố thật" if LANG == "vi" else "3. Transfer APs back to real primes", SUN),
        ]
        for i, (txt, col) in enumerate(f_data):
            y = 2.5 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.92,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            flow.add(VGroup(b, t))
        self.play(FadeIn(flow, lag_ratio=0.3), run_time=1.5)
        self.wait(2.5)

        s4b = line(TX["s4_b"], 25, WHITE, -1.8)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 5: Phân biệt & Bối cảnh ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 25, SKY, 4.5)
        self.play(FadeIn(s5a), run_time=0.8)

        facts = VGroup()
        fa_data = [
            ("✓ AP nguyên tố dài tùy ý (Green–Tao)" if LANG == "vi" else "✓ Arbitrarily long prime APs (Green–Tao)", MINT),
            ("✗ Chưa chứng minh sinh đôi p, p+2" if LANG == "vi" else "✗ Does NOT prove twin primes p, p+2", PINK),
            ("Tao (Fields 2006): cả PDE & Compressed Sensing" if LANG == "vi" else "Tao (Fields 2006): PDEs & Compressed Sensing too", SUN),
        ]
        for i, (txt, col) in enumerate(fa_data):
            y = 2.0 - i * 1.45
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=1.05,
                                 fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            facts.add(VGroup(b, t))
        self.play(FadeIn(facts, lag_ratio=0.25), run_time=1.5)
        end_vo("s5", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
