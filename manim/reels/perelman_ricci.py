from common_b import *
import json

TX = {
    "title": {"vi": "Dòng Ricci, Phóng to & Phẫu thuật\n(Hamilton 1982 → Perelman 2003)", "en": "Ricci Flow, Rescaling & Surgery\n(Hamilton 1982 → Perelman 2003)"},
    "s1_a": {"vi": "Phương trình dòng Ricci: ∂g/∂t = −2 Ric(g)\nHoạt động như phương trình truyền nhiệt:", "en": "Ricci flow equation: ∂g/∂t = −2 Ric(g)\nActs like a geometric heat equation:"},
    "s1_b": {"vi": "Vùng cong dương (Ric > 0) co lại\nVùng cong âm (Ric < 0) giãn ra ⇒ đều dần!", "en": "Positive curvature (Ric > 0) shrinks\nNegative curvature (Ric < 0) expands ⇒ evens out!"},
    "s2_a": {"vi": "Phóng to (Rescaling) tại điểm kỳ dị T:\nChuẩn hóa độ cong về 1 để soi cấu trúc cổ!", "en": "Rescaling near singularity time T:\nNormalize curvature to 1 to inspect the neck!"},
    "s2_b": {"vi": "Giới hạn thu được là Nghiệm cổ xưa\nMô hình thắt cổ chai chuẩn: hình trụ S² × ℝ", "en": "Limit is an Ancient Solution (t ∈ (−∞, 0])\nStandard neck-pinch model: cylinder S² × ℝ"},
    "s3_a": {"vi": "Quy trình Phẫu thuật (Surgery) của Perelman:\nKhông để cổ đứt gãy hỗn loạn!", "en": "Perelman's Surgery Procedure:\nPrevent chaotic blow-up at the neck!"},
    "s3_b": {"vi": "Cắt ngang mặt cầu S² → bỏ vùng kỳ dị\nBịt hai đầu bằng mũ tròn → chạy tiếp dòng Ricci!", "en": "Cut along S² → discard high-curvature horns\nCap with standard balls → restart Ricci flow!"},
}

assert 3 - 1 == 2  # mặt cắt S² trong đa tạp 3 chiều


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class PerelmanRicciFlow(Scene):
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

        # --- s1: Truyền nhiệt hình học ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 25, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        b_pos = RoundedRectangle(corner_radius=0.14, width=3.4, height=1.8, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([-2.0, 1.5, 0])
        t_pos = T("Ric > 0\nCo lại (→)" if LANG == "vi" else "Ric > 0\nShrinks (→)", 22, PINK).move_to(b_pos)
        b_neg = RoundedRectangle(corner_radius=0.14, width=3.4, height=1.8, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([2.0, 1.5, 0])
        t_neg = T("Ric < 0\nGiãn ra (← →)" if LANG == "vi" else "Ric < 0\nExpands (← →)", 22, MINT).move_to(b_neg)

        self.play(FadeIn(b_pos), FadeIn(t_pos), FadeIn(b_neg), FadeIn(t_neg), run_time=1.0)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, SUN, -1.3)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- s2: Phóng to & Nghiệm cổ xưa ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 25, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        cyl_top = Line([-2.2, 2.2, 0], [2.2, 2.2, 0], color=SUN, stroke_width=4)
        cyl_bot = Line([-2.2, 0.8, 0], [2.2, 0.8, 0], color=SUN, stroke_width=4)
        cyl_l = Ellipse(width=0.5, height=1.4, color=SUN, stroke_width=3).move_to([-2.2, 1.5, 0])
        cyl_r = Ellipse(width=0.5, height=1.4, color=SUN, stroke_width=3).move_to([2.2, 1.5, 0])
        cyl_lbl = T("Hình trụ S² × ℝ  (nghiệm cổ xưa)" if LANG == "vi" else "Cylinder S² × ℝ  (ancient solution)", 22, MINT).move_to([0, 0.0, 0])

        self.play(Create(cyl_top), Create(cyl_bot), Create(cyl_l), Create(cyl_r), run_time=1.2)
        self.play(FadeIn(cyl_lbl), run_time=0.8)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 24, WHITE, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- s3: Phẫu thuật hữu hạn lần ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        steps = VGroup()
        st_data = [
            ("1. Phát hiện cổ hẹp ε trên S² × ℝ" if LANG == "vi" else "1. Detect ε-neck modeled on S² × ℝ", PINK),
            ("2. Cắt dọc mặt cầu S² & bỏ phần sừng" if LANG == "vi" else "2. Cut along S² & discard horns", SUN),
            ("3. Gắn mũ trơn & chạy tiếp dòng Ricci" if LANG == "vi" else "3. Glue smooth caps & continue flow", MINT),
            ("4. Hữu hạn lần cắt trong mọi [0, T]" if LANG == "vi" else "4. Finitely many surgeries on [0, T]", SKY),
        ]
        for i, (txt, col) in enumerate(st_data):
            y = 2.6 - i * 1.15
            b = RoundedRectangle(corner_radius=0.14, width=7.5, height=0.88, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            steps.add(VGroup(b, t))
        self.play(FadeIn(steps, lag_ratio=0.25), run_time=1.5)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 24, WHITE, -2.5)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
