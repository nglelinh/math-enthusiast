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

class WernerBrownian(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Mandelbrot 4/3 conjecture & LSW proof
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("GIẢ THUYẾT 4/3 CỦA MANDELBROT", "Chiều fractal của biên ngoài chuyển động Brown")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        blob = Circle(radius=1.7, color=DIM, fill_color=SKY, fill_opacity=0.3, stroke_width=2).move_to([0, 1.9, 0])
        frontier = DashedVMobject(Circle(radius=1.75, color=PINK, stroke_width=5).move_to([0, 1.9, 0]), num_dashes=32)
        lbl1 = fit(T("Bên trong đặc chiều = 2, nhưng biên ngoài có chiều = 4/3!", 23, PINK), 7.6).move_to([0, -0.3, 0])

        box1 = card(7.6, 3.0, MINT).move_to([0, -2.4, 0])
        b1_txt = VGroup(
            fit(T("Bộ ba Lawler–Schramm–Werner (LSW, 2001):", 24, SUN), 7.0),
            fit(T("1. Tính chất hạn chế nối biên Brown với SLE₆", 22, WHITE), 7.0),
            fit(T("2. Giải tích Itô trên Loewner → số mũ tách rời ξ(2,0) = 2/3", 21, WHITE), 7.0),
            fit(T("3. Suy ra chiều Hausdorff = 2 − 2/3 = 4/3!", 24, MINT), 7.0),
        ).arrange(DOWN, buff=0.16).move_to(box1)

        self.play(FadeIn(blob), Create(frontier), FadeIn(lbl1), run_time=1.4)
        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=0.9)
        end_vo("s1", t0, 11.0)

        # s2: Fields 2006 & credit to Schramm
        self.play(FadeOut(hdr), FadeOut(blob), FadeOut(frontier), FadeOut(lbl1), FadeOut(box1), FadeOut(b1_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("FIELDS MEDAL 2006", "Ngôn ngữ liên tục cho CFT & Ghi công Schramm")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box2 = card(7.6, 3.8, SKY).move_to([0, 0.2, 0])
        b2_txt = VGroup(
            fit(T("• Oded Schramm (2000): người phát minh ra SLE", 23, SUN), 7.0),
            fit(T("• Wendelin Werner (Fields 2006): phát triển SLE,", 23, SKY), 7.0),
            fit(T("  hình học Brown 2D & cầu nối Lý thuyết trường bảo giác (CFT)", 21, WHITE), 7.0),
            fit(T("• Khớp khít với chứng minh trên lưới của Smirnov!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.28).move_to(box2)

        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        end_vo("s2", t0, 9.5)
        save_tl()
