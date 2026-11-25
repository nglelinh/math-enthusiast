from common_b import *
import json

# Kiểm tra các ví dụ số 5-adic và Frobenius mod 3 từ bài 02_06
def v5(n):
    k = 0
    while n % 5 == 0 and n != 0:
        n //= 5
        k += 1
    return k

assert v5(26 - 1) == 2 and v5(626 - 1) == 4
# Kiểm tra (x+y)^3 ≡ x^3 + y^3 (mod 3)
for x in range(3):
    for y in range(3):
        assert ((x + y) ** 3 - (x ** 3 + y ** 3)) % 3 == 0

TX = {
    "title": {"vi": "Không gian Perfectoid (Scholze)\nHuy chương Fields 2018", "en": "Scholze's Perfectoid Spaces\nFields Medal 2018"},
    "s1_a": {"vi": "Hai thế giới anh em sinh đôi nhưng bị ngăn cách:\nĐặc số 0 (Q_p)  vs  Đặc số p (F_p((t)))", "en": "Two twin worlds separated by a stubborn wall:\nChar 0 (Q_p)  vs  Char p (F_p((t)))"},
    "s1_b": {"vi": "Năm 24 tuổi, Peter Scholze tạo ra Phép nghiêng\nbắc cầu nối thông suốt giữa hai thế giới!", "en": "At age 24, Peter Scholze built Tilting\nto bridge these two arithmetic worlds!"},
    "s2_a": {"vi": "Thế giới số 5-adic: hai số gần nhau nếu hiệu\nchia hết cho lũy thừa càng cao của 5!", "en": "5-adic numbers: two integers are close if their\ndifference is divisible by a high power of 5!"},
    "s2_b": {"vi": "Trong Z_5: 4 + 4·5 + 4·5² + ... = −1 !\nVì cộng thêm 1 tạo phép nhớ vô tận về 0!", "en": "In Z_5: 4 + 4·5 + 4·5² + ... = −1 !\nAdding 1 triggers an infinite cascade of carries!"},
    "s3_a": {"vi": "Đặc số p có siêu năng lực Frobenius:\n(x + y)³ ≡ x³ + y³ (mod 3) — bảo toàn phép cộng!", "en": "Char p has the Frobenius superpower:\n(x + y)³ ≡ x³ + y³ (mod 3) — preserves addition!"},
    "s3_b": {"vi": "Bức tường ngăn cách chính là PHÉP NHỚ:\n3 + 4 = 2 (trong F_5((t))) ≠ 2 + 1·5 (trong Q_5)!", "en": "The wall between them is CARRYING:\n3 + 4 = 2 (in F_5((t))) ≠ 2 + 1·5 (in Q_5)!"},
    "s4_a": {"vi": "Bước đột phá: Gắn thêm VÔ HẠN căn bậc p\np^(1/p), p^(1/p²), p^(1/p³), ... ⇒ Trường Perfectoid!", "en": "Breakthrough: Adjoin INFINITE p-power roots\np^(1/p), p^(1/p²), p^(1/p³), ... ⇒ Perfectoid Field!"},
    "s4_b": {"vi": "Biến 'cơn ác mộng' phân nhánh vô hạn\nthành chính chìa khóa xóa sạch phép nhớ!", "en": "Turning 'nightmare' infinite ramification\ninto the exact key that erases carrying!"},
    "s5_a": {"vi": "Tác động nền tảng của Peter Scholze:\nViết lại hạ tầng của hình học p-adic hiện đại!", "en": "Peter Scholze's foundational impact:\nRewriting the language of p-adic geometry!"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class ScholzePerfectoid(Scene):
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

        # --- Phần 1: Hai thế giới sinh đôi ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 24, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        b_left = RoundedRectangle(corner_radius=0.14, width=3.4, height=2.0, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([-2.1, 1.5, 0])
        t_left = T("Đặc số 0\nQ_p (số p-adic)\nKhó kiểm soát" if LANG == "vi" else "Char 0\nQ_p (p-adic)\nHarder to solve", 20, PINK).move_to(b_left)
        b_right = RoundedRectangle(corner_radius=0.14, width=3.4, height=2.0, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([2.1, 1.5, 0])
        t_right = T("Đặc số p\nF_p((t))\nCó Frobenius!" if LANG == "vi" else "Char p\nF_p((t))\nHas Frobenius!", 20, MINT).move_to(b_right)
        bridge = Arrow([-0.35, 1.5, 0], [0.35, 1.5, 0], color=SUN, buff=0)

        self.play(FadeIn(b_left, t_left), FadeIn(b_right, t_right), GrowArrow(bridge), run_time=1.3)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 24, SUN, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Tính tay số 5-adic ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 24, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        cards = VGroup()
        rows = [
            ("|26 − 1|_5  =  |5²|_5  =  1 / 25  =  0,04" if LANG == "vi" else "|26 − 1|_5  =  |5²|_5  =  1 / 25  =  0.04", MINT),
            ("|626 − 1|_5  =  |5⁴|_5  =  1 / 625  =  0,0016" if LANG == "vi" else "|626 − 1|_5  =  |5⁴|_5  =  1 / 625  =  0.0016", SKY),
            ("1 + (4 + 4·5 + 4·5² + ...)  =  0  ⇒  S = −1!" if LANG == "vi" else "1 + (4 + 4·5 + 4·5² + ...)  =  0  ⇒  S = −1!", SUN),
        ]
        for i, (txt, col) in enumerate(rows):
            y = 2.4 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.92, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.3), run_time=1.4)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 23, WHITE, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Phép màu Frobenius vs Bức tường Phép nhớ ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, MINT, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        c1 = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.25, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 2.2, 0])
        t1 = T("Trong F_5((t)):   3 + 4 = 2   (KHÔNG có nhớ)" if LANG == "vi" else "In F_5((t)):   3 + 4 = 2   (NO carry!)", 22, MINT).move_to(c1)

        c2 = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.25, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 0.5, 0])
        t2 = T("Trong Q_5:   3 + 4 = 2 + 1·5   (NHỚ 1 sang hàng 5!)" if LANG == "vi" else "In Q_5:   3 + 4 = 2 + 1·5   (CARRIES 1!)", 22, PINK).move_to(c2)

        self.play(FadeIn(c1, t1), FadeIn(c2, t2), run_time=1.3)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 23, SUN, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 4: Gắn vô hạn căn bậc p ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 23, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        pf_box = RoundedRectangle(corner_radius=0.16, width=7.6, height=2.2, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=3).move_to([0, 1.5, 0])
        pf_t = T("K  =  hoàn thiện của  Q_p(p^(1/p), p^(1/p²), ...)\n\nPhép nghiêng:   K^♭  ≃  F_p((t^(1/p^∞))) !" if LANG == "vi" else "K  =  completion of  Q_p(p^(1/p), p^(1/p²), ...)\n\nTilting:   K^♭  ≃  F_p((t^(1/p^∞))) !", 21, SUN).move_to(pf_box)
        self.play(FadeIn(pf_box, pf_t), run_time=1.2)
        self.wait(2.0)

        s4b = line(TX["s4_b"], 23, MINT, -1.7)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 5: Di sản & phân biệt ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 24, SKY, 4.6)
        self.play(FadeIn(s5a), run_time=0.8)

        leg = VGroup()
        l_data = [
            ("1. Giả thuyết đơn đạo trọng số (Deligne → đặc số 0)" if LANG == "vi" else "1. Weight-Monodromy (Deligne → char 0)", MINT),
            ("2. Đối đồng điều lăng trụ (Bhatt–Scholze) & Langlands" if LANG == "vi" else "2. Prismatic Cohomology (Bhatt–Scholze) & Langlands", SKY),
            ("3. Sau 2018: Toán học cô đặc (cùng Dustin Clausen)" if LANG == "vi" else "3. Post-2018: Condensed Math (with Clausen)", SUN),
        ]
        for i, (txt, col) in enumerate(l_data):
            y = 2.1 - i * 1.4
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=1.0, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 20, col).move_to([0, y, 0])
            leg.add(VGroup(b, t))
        self.play(FadeIn(leg, lag_ratio=0.25), run_time=1.4)
        end_vo("s5", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
