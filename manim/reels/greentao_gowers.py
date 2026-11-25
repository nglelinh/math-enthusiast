from common_b import *
import json

TX = {
    "title": {"vi": "Hàm trội ν & Chuẩn Gowers\n(Vũ khí giải tích của Green–Tao)", "en": "Majorant ν & Gowers Norms\n(The Green–Tao Toolkit)"},
    "s1_a": {"vi": "Vì sao không dùng thẳng hàm chỉ thị số nguyên tố?\nTrọng số von Mangoldt Λ(n) quá gai góc!", "en": "Why not use primes directly?\nThe von Mangoldt weight Λ(n) is too spiky!"},
    "s1_b": {"vi": "Sàng bao (kiểu Selberg) tạo hàm trội ν(n):\nν(n) ≥ 0, mượt mà và Λ(n) ≤ C · ν(n)!", "en": "Enveloping sieve (Selberg-type) builds ν(n):\nν(n) ≥ 0, smooth, and Λ(n) ≤ C · ν(n)!"},
    "s2_a": {"vi": "Chuẩn Gowers U^(k−1): thước đo độ ngẫu nhiên\nPhát hiện cấu trúc cấp số cộng độ dài k!", "en": "Gowers norm U^(k−1): randomness detector\nSpots structure behind k-term progressions!"},
    "s2_b": {"vi": "Định lý ngược Gowers:\n‖f‖ lớn ⇔ f tương quan với pha đa thức!", "en": "Inverse Gowers Theorem:\nLarge ‖f‖ ⇔ f correlates with polynomial phase!"},
    "s3_a": {"vi": "Nguyên lý chuyển (Transference):\nTách hàm thành Cấu trúc + Ngẫu nhiên dưới ν", "en": "Transference Principle:\nSplit into Structured + Uniform parts under ν"},
    "s3_b": {"vi": "Phần cấu trúc dùng Szemerédi cổ điển\nPhần ngẫu nhiên bị triệt tiêu ⇒ có AP thật!", "en": "Structured part uses classical Szemerédi\nUniform part vanishes ⇒ real prime APs!"},
}

assert 2 + 3 == 5


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class GreenTaoTransference(Scene):
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

        base = Line([-3.0, 0.2, 0], [3.0, 0.2, 0], color=WHITE, stroke_width=3)
        spikes = VGroup(*[
            Line([x, 0.2, 0], [x, h, 0], color=PINK, stroke_width=5)
            for x, h in [(-2.4, 2.0), (-1.8, 2.2), (-0.8, 2.3), (0.3, 2.1), (1.7, 2.4), (2.5, 1.9)]
        ])
        env = FunctionGraph(lambda x: 2.55 - 0.03 * x**2, x_range=[-3.0, 3.0], color=MINT, stroke_width=5)
        lbl_l = T("Λ(n): gai góc" if LANG == "vi" else "Λ(n): spiky", 21, PINK).move_to([-1.8, -0.4, 0])
        lbl_n = T("ν(n): hàm trội mượt" if LANG == "vi" else "ν(n): smooth majorant", 21, MINT).move_to([1.5, 2.9, 0])

        self.play(Create(base), FadeIn(spikes, lag_ratio=0.15), FadeIn(lbl_l), run_time=1.2)
        self.play(Create(env), FadeIn(lbl_n), run_time=1.0)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, SUN, -1.7)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 24, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        g_box = RoundedRectangle(corner_radius=0.14, width=7.4, height=1.6, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 1.6, 0])
        g_t = T("‖f‖_U² ≈ 0  ⇒  Không lệch nhiều so với ngẫu nhiên\n‖f‖_U^(k−1) lớn  ⇒  Có cấu trúc AP độ dài k!" if LANG == "vi" else "‖f‖_U² ≈ 0  ⇒  Pseudorandom behavior\nLarge ‖f‖_U^(k−1)  ⇒  k-term AP structure!", 21, SUN).move_to(g_box)
        self.play(FadeIn(g_box), FadeIn(g_t), run_time=1.0)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 24, MINT, -0.9)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 24, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        eq_card = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.1, fill_color=CARD, fill_opacity=1, stroke_color=WHITE, stroke_width=2.5).move_to([0, 2.3, 0])
        eq_t = T("f  =  f_cấu_trúc (bị chặn)  +  f_ngẫu_nhiên" if LANG == "vi" else "f  =  f_structured (bounded)  +  f_uniform", 22, WHITE).move_to(eq_card)

        b_st = RoundedRectangle(corner_radius=0.14, width=3.5, height=1.3, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([-2.0, 0.5, 0])
        t_st = T("f_cấu_trúc\n⇒ Szemerédi" if LANG == "vi" else "f_structured\n⇒ Szemerédi", 21, MINT).move_to(b_st)

        b_un = RoundedRectangle(corner_radius=0.14, width=3.5, height=1.3, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([2.0, 0.5, 0])
        t_un = T("f_ngẫu_nhiên\n⇒ Sai số ≈ 0" if LANG == "vi" else "f_uniform\n⇒ Error ≈ 0", 21, PINK).move_to(b_un)

        self.play(FadeIn(eq_card), FadeIn(eq_t), run_time=0.9)
        self.play(FadeIn(b_st), FadeIn(t_st), FadeIn(b_un), FadeIn(t_un), run_time=1.0)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 24, SUN, -1.7)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
