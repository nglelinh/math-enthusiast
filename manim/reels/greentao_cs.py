from common_b import *
import json

TX = {
    "title": {"vi": "Terence Tao (Fields 2006) &\nKỹ thuật Lấy mẫu Nén (MRI)", "en": "Terence Tao (Fields 2006) &\nCompressed Sensing (MRI)"},
    "s1_a": {"vi": "Huy chương Fields 2006 không chỉ vì Green–Tao!\nTao đóng góp trải rộng 6 trụ cột toán học", "en": "Fields 2006 wasn't only Green–Tao!\nTao spans harmonic analysis, PDEs & primes"},
    "s1_b": {"vi": "Một câu chuyện bất ngờ: Chụp cộng hưởng từ (MRI)\nvà bài toán tái tạo ảnh siêu nhanh!", "en": "An unexpected story: MRI scans\nand ultra-fast image reconstruction!"},
    "s2_a": {"vi": "Chụp MRI thường: đo đủ góc cho bình phương tối thiểu\n⇒ Bệnh nhân phải nằm yên nhiều phút!", "en": "Standard MRI: many scans for least squares\n⇒ Patients must lie still for minutes!"},
    "s2_b": {"vi": "Thử chụp ít phép đo + cực tiểu hóa Total Variation\n⇒ Tái tạo gần như hoàn hảo như ô chữ tự điền!", "en": "Fewer scans + Total Variation minimization\n⇒ Near-perfect recovery like a crossword!"},
    "s3_a": {"vi": "Tao ban đầu tưởng 'nhầm lẫn vì thiếu thông tin'\nnhưng lại chứng minh được phép tái tạo hoạt động!", "en": "Tao first thought 'impossible—too little data!'\nthen proved why sparse recovery works!"},
    "s3_b": {"vi": "Lấy mẫu nén (Compressed Sensing) thống nhất\ncác mẹo của y học, địa chấn, thiên văn & vô tuyến!", "en": "Compressed Sensing unified tricks across\nMRI, seismology, astronomy & radio!"},
}

assert 1 + 1 == 2


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class TaoCompressedSensing(Scene):
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

        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 24, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        pillars = VGroup()
        for i, (txt, col) in enumerate([
            ("Giải tích điều hòa & PDE" if LANG == "vi" else "Harmonic Analysis & PDEs", SKY),
            ("Tổ hợp cộng tính & Số nguyên tố" if LANG == "vi" else "Additive Combinatorics & Primes", MINT),
            ("Lấy mẫu nén (Compressed Sensing)" if LANG == "vi" else "Compressed Sensing (MRI)", SUN),
        ]):
            y = 2.4 - i * 1.2
            b = RoundedRectangle(corner_radius=0.14, width=7.2, height=0.88, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 22, col).move_to([0, y, 0])
            pillars.add(VGroup(b, t))
        self.play(FadeIn(pillars, lag_ratio=0.25), run_time=1.4)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, WHITE, -1.7)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 24, PINK, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        b_ls = RoundedRectangle(corner_radius=0.14, width=3.5, height=2.0, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([-2.0, 1.4, 0])
        t_ls = T("Ít phép đo\n+ Bình phương tối thiểu\n⇒ Ảnh bị nhòe!" if LANG == "vi" else "Few scans\n+ Least Squares\n⇒ Blurry image!", 20, PINK).move_to(b_ls)

        b_tv = RoundedRectangle(corner_radius=0.14, width=3.5, height=2.0, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([2.0, 1.4, 0])
        t_tv = T("Ít phép đo\n+ Cực tiểu TV (thưa)\n⇒ Ảnh sắc nét!" if LANG == "vi" else "Few scans\n+ Min Total Variation\n⇒ Sharp image!", 20, MINT).move_to(b_tv)

        self.play(FadeIn(b_ls), FadeIn(t_ls), FadeIn(b_tv), FadeIn(t_tv), run_time=1.1)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 24, SUN, -1.4)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 24, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        cs_box = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.8, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([0, 1.5, 0])
        cs_t = T("Tính thưa (Sparsity) + Ma trận đo thiết kế tốt\n⇒ Khôi phục tín hiệu từ rất ít mẫu đo!" if LANG == "vi" else "Sparsity + Well-designed measurement matrix\n⇒ Recover signals from far fewer samples!", 21, MINT).move_to(cs_box)
        self.play(FadeIn(cs_box), FadeIn(cs_t), run_time=1.0)
        self.wait(2.5)

        s3b = line(TX["s3_b"], 24, SUN, -1.2)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
