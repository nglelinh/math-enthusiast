from common_b import *
import json

assert 2012 - 1980 == 32

TX = {
    "title": {"vi": "Đơn đạo Trọng số, Lăng trụ &\nToán học Cô đặc", "en": "Weight-Monodromy, Prisms &\nCondensed Mathematics"},
    "s1_a": {"vi": "Ứng dụng kinh điển ngay năm 2012:\nGiả thuyết Đơn đạo Trọng số (Weight-Monodromy)!", "en": "Flagship 2012 application:\nThe Weight-Monodromy Conjecture!"},
    "s1_b": {"vi": "Deligne chứng minh ở đặc số p từ năm 1980,\nnhưng ở đặc số 0 bế tắc suốt hơn 30 năm!", "en": "Proved by Deligne in char p back in 1980,\nyet stuck in char 0 for over 30 years!"},
    "s2_a": {"vi": "Chiến lược 4 bước của Peter Scholze:\nĐưa bài toán qua cầu nghiêng rồi kéo kết quả về!", "en": "Peter Scholze's 4-step bridge:\nTilt to char p, invoke Deligne, transfer back!"},
    "s2_b": {"vi": "Không chỉ một định lý — perfectoid trở thành\nngôn ngữ chung của cả thế hệ hình học p-adic!", "en": "Not just one theorem — perfectoids became\nthe shared language of modern p-adic geometry!"},
    "s3_a": {"vi": "Ba chương tiếp nối sau bài báo 2012:\nThống nhất đối đồng điều, Langlands & giải tích!", "en": "Three major sequels after 2012:\nUnifying cohomology, Langlands & analysis!"},
    "s3_b": {"vi": "Lưu ý: Fields 2018 trao cho Perfectoid;\nToán học cô đặc (với Clausen) là chương sau 2018!", "en": "Note: Fields 2018 honored Perfectoids;\nCondensed Math (with Clausen) came after 2018!"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class ScholzeImpact(Scene):
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

        # --- Phần 1: Giả thuyết đơn đạo trọng số ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        b1 = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.2, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 2.1, 0])
        t1 = T("Đặc số p:  Deligne chứng minh (1980) ✓" if LANG == "vi" else "Char p:  Proved by Deligne (1980) ✓", 22, MINT).move_to(b1)
        b2 = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.2, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 0.5, 0])
        t2 = T("Đặc số 0:  Bế tắc > 30 năm → Scholze (2012) ✓" if LANG == "vi" else "Char 0:  Stuck > 30 yrs → Scholze (2012) ✓", 22, PINK).move_to(b2)

        self.play(FadeIn(b1, t1), FadeIn(b2, t2), run_time=1.3)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 23, SUN, -1.7)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Quy trình 4 bước ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        steps = VGroup()
        st_data = [
            ("1. Nhúng đa tạp (đặc số 0) vào P^(n, perf)" if LANG == "vi" else "1. Embed char-0 variety into P^(n, perf)", SKY),
            ("2. Nghiêng sang đặc số p bằng X ↦ X^♭" if LANG == "vi" else "2. Tilt to char p via X ↦ X^♭", MINT),
            ("3. Dùng định lý Deligne rồi kéo kết quả về!" if LANG == "vi" else "3. Apply Deligne's theorem & transfer back!", SUN),
        ]
        for i, (txt, col) in enumerate(st_data):
            y = 2.4 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.92, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            steps.add(VGroup(b, t))
        self.play(FadeIn(steps, lag_ratio=0.3), run_time=1.4)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 23, WHITE, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Ba chương tiếp nối ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        seq = VGroup()
        sq_data = [
            ("Đối đồng điều lăng trụ (Bhatt–Scholze)" if LANG == "vi" else "Prismatic Cohomology (Bhatt–Scholze)", MINT),
            ("Langlands địa phương hình học (Fargues–Scholze)" if LANG == "vi" else "Geometric Local Langlands (Fargues–Scholze)", SKY),
            ("Toán học cô đặc (Clausen–Scholze, sau 2018)" if LANG == "vi" else "Condensed Mathematics (Clausen–Scholze, post-2018)", SUN),
        ]
        for i, (txt, col) in enumerate(sq_data):
            y = 2.4 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.92, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 20, col).move_to([0, y, 0])
            seq.add(VGroup(b, t))
        self.play(FadeIn(seq, lag_ratio=0.3), run_time=1.4)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 23, SUN, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
