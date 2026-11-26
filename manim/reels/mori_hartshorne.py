# -*- coding: utf-8 -*-
from common_b import *
import os, json, numpy as np

BG = "#10121a"
FG = WHITE
MUTED = DIM
ACCENT = SKY
RED = PINK
VIOLET = ORANGE
GOLD = SUN

def card(w, h, color=SKY):
    return RoundedRectangle(width=w, height=h, corner_radius=0.22,
                            fill_color=CARD, fill_opacity=0.92,
                            stroke_color=color, stroke_width=2.5)

def make_scene_header(tag, title):
    t1 = fit(T(tag, 22, GOLD), 7.6)
    t2 = fit(T(title, 32, WHITE), 7.8)
    return VGroup(t1, t2).arrange(DOWN, buff=0.14).move_to([0, 6.2, 0])

def setup_vo(scene):
    vo_durs = json.load(open(os.environ["VO_DUR_JSON"])) if os.environ.get("VO_DUR_JSON") else {}
    tl_path = os.environ.get("VO_TIMELINE_JSON")
    timeline = []
    def end_vo(sid, t0, fb):
        dur = vo_durs.get(sid)
        if dur is not None:
            rem = dur - (scene.time - t0) + 0.45
            if rem > 0.05:
                scene.wait(rem)
        else:
            scene.wait(fb)
    def save_tl():
        if tl_path:
            with open(tl_path, "w") as f:
                json.dump({"timeline": timeline, "total": float(scene.time)}, f)
    return timeline, end_vo, save_tl

class MoriHartshorne(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Canonical class K_X = (d - 5)H in P^4
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("LỚP CHÍNH TẮC K_X", "Nhiệt kế đo độ cong: Siêu mặt bậc d trong P⁴")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        formula = fit(T("Công thức phụ hợp:  K_X = (d − 5) H", 28, SUN), 7.4).move_to([0, 4.3, 0])
        self.play(FadeIn(formula), run_time=0.6)

        cases = [
            ("d ≤ 4  (K_X < 0)", "Thế giới Fano — cong dương", "Chứa đầy đường cong hữu tỷ", SKY),
            ("d = 5  (K_X = 0)", "Calabi–Yau — bậc 5 trong P⁴", "Độ cong cân bằng", MINT),
            ("d ≥ 6  (K_X > 0)", "Kiểu tổng quát (General Type)", "Thể tích hình học dương", PINK),
        ]
        cards = VGroup()
        for t1, t2, t3, col in cases:
            b = card(7.6, 2.0, col)
            g = VGroup(fit(T(t1, 25, col), 7.0), fit(T(t2, 23, WHITE), 7.0), fit(T(t3, 21, DIM), 7.0)).arrange(DOWN, buff=0.12).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.3).move_to([0, -0.2, 0])

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in cards], lag_ratio=0.25), run_time=1.8)
        end_vo("s1", t0, 9.5)

        # s2: Bend-and-Break & Hartshorne Conjecture (1979)
        self.play(FadeOut(hdr), FadeOut(formula), FadeOut(cards), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("GIẢ THUYẾT HARTSHORNE (1979)", "Kỹ thuật Uốn và Bẻ (Bend-and-Break)")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        c_curve = Arc(radius=2.0, start_angle=0.2, angle=2.7, color=SKY, stroke_width=5).move_to([0, 2.1, 0])
        p_fix = Dot([0, 1.3, 0], color=SUN, radius=0.12)
        l1 = Line([-2.2, 0.2, 0], [0, 1.8, 0], color=MINT, stroke_width=4)
        l2 = Line([0, 1.8, 0], [2.2, 0.2, 0], color=PINK, stroke_width=4)
        lbl_bb = fit(T("Biến dạng đường cong giữ chặt 1 điểm → tự gãy thành đường cong hữu tỷ P¹!", 22, WHITE), 7.6).move_to([0, -0.6, 0])

        box_h = card(7.6, 3.0, SUN).move_to([0, -2.9, 0])
        bh_txt = VGroup(
            fit(T("Định lý Mori (chứng minh qua đặc số p > 0):", 24, SUN), 7.0),
            fit(T("Mọi đa tạp xạ ảnh trơn X có phân thớ tiếp xúc", 23, WHITE), 7.0),
            fit(T("ample bắt buộc đẳng cấu với không gian xạ ảnh P^n!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box_h)

        self.play(Create(c_curve), FadeIn(p_fix), run_time=0.9)
        self.play(Transform(c_curve, VGroup(l1, l2)), FadeIn(lbl_bb), run_time=1.0)
        self.play(FadeIn(box_h), FadeIn(bh_txt), run_time=0.9)
        end_vo("s2", t0, 10.0)
        save_tl()
