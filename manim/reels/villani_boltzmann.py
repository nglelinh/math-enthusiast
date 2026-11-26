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

class VillaniBoltzmann(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Inhomogeneous Boltzmann & Hypocoercivity
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("PHƯƠNG TRÌNH BOLTZMANN", "Bẫy Cân bằng Địa phương & Hypocoercivity")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        box1 = card(7.6, 2.7, PINK).move_to([0, 2.1, 0])
        b1_txt = VGroup(
            fit(T("Va chạm chỉ làm hàm phân bố thành Maxwell theo v", 22, WHITE), 7.0),
            fit(T("Nhưng ở mỗi điểm x, mật độ vẫn có thể lệch nhau!", 23, PINK), 7.0),
            fit(T("→ Bị kẹt tại 'cân bằng địa phương' (local equilibrium).", 22, SUN), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box1)

        box2 = card(7.6, 3.0, MINT).move_to([0, -1.5, 0])
        b2_txt = VGroup(
            fit(T("Desvillettes–Villani (2005) & Hypocoercivity:", 24, MINT), 7.0),
            fit(T("Phối hợp toán tử vận chuyển v·∇_x với toán tử va chạm", 22, WHITE), 7.0),
            fit(T("→ Chứng minh hội tụ siêu đa thức (O(t⁻∞)) về cân bằng!", 22, SKY), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box2)

        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=1.0)
        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        end_vo("s1", t0, 10.0)

        # s2: Fields 2010 citation clarity
        self.play(FadeOut(hdr), FadeOut(box1), FadeOut(b1_txt), FadeOut(box2), FadeOut(b2_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("FIELDS MEDAL 2010", "Đọc đúng lời trao giải của Cédric Villani")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box3 = card(7.6, 4.0, SUN).move_to([0, 0.2, 0])
        b3_txt = VGroup(
            fit(T("✓ Tắt dần Landau phi tuyến (Vlasov–Poisson)", 23, MINT), 7.0),
            fit(T("✓ Hội tụ về cân bằng cho Boltzmann (có điều kiện)", 23, MINT), 7.0),
            fit(T("≠ Lời trao giải KHÔNG nêu Vận chuyển tối ưu", 23, PINK), 7.0),
            fit(T("(Dù 2 cuốn sách Optimal Transport rất kinh điển!)", 21, DIM), 7.0),
        ).arrange(DOWN, buff=0.32).move_to(box3)

        self.play(FadeIn(box3), FadeIn(b3_txt), run_time=1.1)
        end_vo("s2", t0, 9.0)
        save_tl()
