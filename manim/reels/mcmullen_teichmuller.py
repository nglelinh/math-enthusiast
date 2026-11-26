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

class McMullenTeichmuller(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Teichmuller space & pinching to a cusp (Bers conjecture)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("GIẢ THUYẾT BERS (FIELDS 1998)", "Bóp thắt mặt giống g = 2 thành điểm cusp")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        surf1 = Ellipse(width=4.6, height=2.2, color=SKY, stroke_width=4).move_to([0, 2.2, 0])
        hole1 = Ellipse(width=0.9, height=0.45, color=SKY, stroke_width=3).move_to([-1.0, 2.2, 0])
        hole2 = Ellipse(width=0.9, height=0.45, color=SKY, stroke_width=3).move_to([1.0, 2.2, 0])
        pinch = Line([0, 3.3, 0], [0, 1.1, 0], color=PINK, stroke_width=4)
        lbl1 = fit(T("Bóp độ dài đường cong đóng γ → 0", 24, PINK), 7.6).move_to([0, 0.4, 0])

        box1 = card(7.6, 3.0, SUN).move_to([0, -2.2, 0])
        b1_txt = VGroup(
            fit(T("Điểm cusp cực đại trên biên Bers ∂T(S)", 25, SUN), 7.0),
            fit(T("McMullen chứng minh: các điểm cusp TRÙ MẬT", 24, WHITE), 7.0),
            fit(T("trên toàn bộ biên của không gian Teichmüller!", 24, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box1)

        self.play(Create(surf1), Create(hole1), Create(hole2), run_time=1.0)
        self.play(Create(pinch), FadeIn(lbl1), run_time=0.8)
        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=0.9)
        end_vo("s1", t0, 10.0)

        # s2: Kra's theta-function conjecture & amenability
        self.play(FadeOut(hdr), FadeOut(surf1), FadeOut(hole1), FadeOut(hole2), FadeOut(pinch), FadeOut(lbl1), FadeOut(box1), FadeOut(b1_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("GIẢ THUYẾT HÀM THETA CỦA KRA", "Tiêu chuẩn khả trung bình (Amenability)")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box2 = card(7.6, 3.4, MINT).move_to([0, 1.4, 0])
        b2_txt = VGroup(
            fit(T("Toán tử chuỗi Poincaré Θ: Q(Δ) → Q(X)", 25, SKY), 7.0),
            fit(T("Giả thuyết Kra: ||Θ|| < 1 với mặt hyperbolic", 25, SUN), 7.0),
            fit(T("Định lý McMullen: ||Θ|| < 1 ⇔ Phủ Δ → X", 24, WHITE), 7.0),
            fit(T("KHÔNG khả trung bình (non-amenable)!", 25, MINT), 7.0),
        ).arrange(DOWN, buff=0.22).move_to(box2)

        box3 = card(7.6, 2.6, PINK).move_to([0, -2.4, 0])
        b3_txt = VGroup(
            fit(T("Đa tạp 3D phân thớ trên đường tròn S¹", 25, PINK), 7.0),
            fit(T("Tái chuẩn hóa cho phép đo độ co của ánh xạ Thurston", 22, WHITE), 7.0),
            fit(T("(Khác Perelman: Perelman giải trọn bộ hình học hóa)", 21, DIM), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box3)

        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        self.play(FadeIn(box3), FadeIn(b3_txt), run_time=1.0)
        end_vo("s2", t0, 10.0)
        save_tl()
