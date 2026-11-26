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

class MoriMMP(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: 4 steps of 3D MMP
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("CHƯƠNG TRÌNH MÔ HÌNH TỐI THIỂU", "4 bước chạy MMP ở chiều ba (Fields 1990)")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        steps = [
            ("1. Định lý Nón (Cone Theorem)", "Tìm tia cực biên có K_X < 0 cần cắt tỉa", SKY),
            ("2. Định lý Co (Contraction)", "3 nhánh: Co ước (divisorial), Thớ Mori, hoặc Co nhỏ", MINT),
            ("3. Phẫu thuật Flip (Mori 1988)", "Khi co nhỏ 1 đường P¹: thay bằng đường P¹ mới!", SUN),
            ("4. Tính dừng (Shokurov)", "Chuỗi Flip luôn kết thúc → Mô hình tối thiểu / Thớ Mori", PINK),
        ]
        cards = VGroup()
        for t1, t2, col in steps:
            b = card(7.6, 1.75, col)
            g = VGroup(fit(T(t1, 24, col), 7.0), fit(T(t2, 21, WHITE), 7.0)).arrange(DOWN, buff=0.1).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.25).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.18) for c in cards], lag_ratio=0.22), run_time=2.0)
        end_vo("s1", t0, 11.0)

        # s2: Atiyah flop / Flip geometry & higher dimensions
        self.play(FadeOut(hdr), FadeOut(cards), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("PHẪU THUẬT FLIP Ở CHIỀU BA", "Vì sao không thể chỉ co điểm như chiều hai?")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        p1_a = Line([-2.5, 2.3, 0], [-1.3, 1.1, 0], color=SKY, stroke_width=6)
        dot_mid = Dot([0, 1.7, 0], color=PINK, radius=0.16)
        p1_b = Line([1.3, 1.1, 0], [2.5, 2.3, 0], color=MINT, stroke_width=6)
        a1 = Arrow([-1.1, 1.7, 0], [-0.25, 1.7, 0], color=DIM, stroke_width=3)
        a2 = Arrow([0.25, 1.7, 0], [1.1, 1.7, 0], color=SUN, stroke_width=3)
        lbl_flip = fit(T("Co P¹ âm → điểm kỳ dị nặng → bung ra P¹ dương mới!", 23, SUN), 7.6).move_to([0, 0.1, 0])

        box_end = card(7.6, 3.0, PINK).move_to([0, -2.3, 0])
        be_txt = VGroup(
            fit(T("Kỳ dị nhẹ (terminal) là không thể tránh ở chiều 3", 23, WHITE), 7.0),
            fit(T("Mori (1988) hoàn tất chiều 3.", 23, MINT), 7.0),
            fit(T("Chiều cao n ≥ 4: BCHM (2010) & Caucher Birkar!", 23, PINK), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box_end)

        self.play(Create(p1_a), GrowArrow(a1), FadeIn(dot_mid), GrowArrow(a2), Create(p1_b), run_time=1.3)
        self.play(FadeIn(lbl_flip), FadeIn(box_end), FadeIn(be_txt), run_time=0.9)
        end_vo("s2", t0, 10.0)
        save_tl()
