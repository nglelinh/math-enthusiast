from common_b import *
import json

TX = {
    "title": {"vi": "Entropy & Tính không suy biến κ\n(Vũ khí giải tích của Perelman)", "en": "Entropy & κ-Noncollapsing\n(Perelman's Analytical Toolkit)"},
    "s1_a": {"vi": "Làm sao kiểm soát một phương trình phi tuyến\nkhi phóng to đến điểm kỳ dị?", "en": "How to control a nonlinear PDE\nwhen zooming into a singularity?"},
    "s1_b": {"vi": "Cần một đại lượng ĐƠN ĐIỆU:\nkhông bao giờ giảm dọc theo dòng Ricci!", "en": "Need a MONOTONE quantity:\nnever decreases along Ricci flow!"},
    "s2_a": {"vi": "Phiếm hàm Entropy W(g, f, τ) của Perelman\n& Thể tích rút gọn: chặn hành vi xấu!", "en": "Perelman's Entropy W(g, f, τ)\n& Reduced Volume: rule out bad blow-ups!"},
    "s2_b": {"vi": "Tính không suy biến κ:\nNếu |Rm| ≤ r⁻² trên B(x, r) ⇒ Vol ≥ κ · r³", "en": "κ-Noncollapsing Theorem:\nIf |Rm| ≤ r⁻² on B(x, r) ⇒ Vol ≥ κ · r³"},
    "s3_a": {"vi": "Ý nghĩa: Không gian KHÔNG bị bẹp dí về 0\nkhi ta phóng to để lấy giới hạn trơn!", "en": "Meaning: Space CANNOT collapse to 0 dim\nwhen rescaling to take a smooth limit!"},
    "s3_b": {"vi": "Kết hợp: Entropy + Không suy biến κ + Phẫu thuật\n⇒ Phân loại tô pô 3 chiều qua biến đổi hình học!", "en": "Together: Entropy + κ-noncollapsing + Surgery\n⇒ 3D topology via evolving geometry!"},
}

assert 0.5**3 == 0.125  # kiểm tra tỉ lệ thể tích r³


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class PerelmanEntropyTools(Scene):
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

        # --- s1: Cần đại lượng đơn điệu ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 25, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        ax_x = Line([-2.8, 0.4, 0], [2.8, 0.4, 0], color=WHITE, stroke_width=3)
        ax_y = Line([-2.8, 0.4, 0], [-2.8, 2.8, 0], color=WHITE, stroke_width=3)
        curve = FunctionGraph(lambda x: 0.7 + 0.35 * (x + 2.5)**0.8, x_range=[-2.5, 2.4], color=MINT, stroke_width=5)
        lbl = T("d/dt Entropy ≥ 0  (đơn điệu tăng)" if LANG == "vi" else "d/dt Entropy ≥ 0  (monotone)", 22, MINT).move_to([0, 3.1, 0])
        self.play(Create(ax_x), Create(ax_y), Create(curve), FadeIn(lbl), run_time=1.4)
        self.wait(2.5)

        s1b = line(TX["s1_b"], 24, SUN, -1.3)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- s2: Không suy biến kappa ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 25, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        ball = Circle(radius=1.35, color=MINT, stroke_width=4, fill_color=MINT, fill_opacity=0.15).move_to([0, 1.5, 0])
        rad = Line([0, 1.5, 0], [1.35, 1.5, 0], color=SUN, stroke_width=3)
        rad_t = T("r", 22, SUN).next_to(rad, UP, buff=0.1)
        vol_t = T("Vol ≥ κ · r³", 26, MINT).move_to([0, 1.2, 0])
        self.play(Create(ball), Create(rad), FadeIn(rad_t), FadeIn(vol_t), run_time=1.3)
        self.wait(2.5)

        s2b = line(TX["s2_b"], 24, SUN, -1.5)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- s3: Kết nối Giải tích -> Tô pô ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 25, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        chain = VGroup()
        ch_data = [
            ("Entropy + Không suy biến κ" if LANG == "vi" else "Entropy + κ-Noncollapsing", MINT),
            ("Phân loại nghiệm cổ xưa (cầu, cổ, mũ)" if LANG == "vi" else "Classify ancient limits (sphere, neck, cap)", SKY),
            ("Dòng Ricci có phẫu thuật → 8 mảnh Thurston" if LANG == "vi" else "Ricci flow with surgery → 8 Thurston pieces", SUN),
        ]
        for i, (txt, col) in enumerate(ch_data):
            y = 2.3 - i * 1.4
            b = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.0, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            chain.add(VGroup(b, t))
        self.play(FadeIn(chain, lag_ratio=0.3), run_time=1.5)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 24, WHITE, -2.3)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
