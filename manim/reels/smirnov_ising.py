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

class SmirnovIsing(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: SLE_6 & Discrete Holomorphic Fermions for Planar Ising
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("FIELDS MEDAL 2010", "Từ SLE₆ tới Fermion chỉnh hình cho Ising phẳng")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        box1 = card(7.6, 2.8, SKY).move_to([0, 2.2, 0])
        b1_txt = VGroup(
            fit(T("1. Thấm đỉnh lưới tam giác → đường biên hội tụ về SLE₆", 23, SKY), 7.0),
            fit(T("(Ghép khít khung Schramm–Lawler–Werner)", 22, DIM), 7.0),
            fit(T("→ Xác nhận giả thuyết phổ quát bằng chứng minh chặt chẽ!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box1)

        box2 = card(7.6, 2.9, SUN).move_to([0, -1.4, 0])
        b2_txt = VGroup(
            fit(T("2. Mô hình Ising phẳng (Smirnov; Chelkak–Smirnov):", 24, SUN), 7.0),
            fit(T("Fermion chỉnh hình rời rạc trên mọi đồ thị đẳng bán kính", 22, WHITE), 7.0),
            fit(T("→ Hội tụ bảo giác & đường biên hội tụ về SLE₃!", 23, PINK), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box2)

        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=1.0)
        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        end_vo("s1", t0, 10.5)

        # s2: Open frontiers
        self.play(FadeOut(hdr), FadeOut(box1), FadeOut(b1_txt), FadeOut(box2), FadeOut(b2_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("BIÊN GIỚI MỞ", "Những gì chưa giải xong (đọc đúng lời trao giải)")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box3 = card(7.6, 3.8, PINK).move_to([0, 0.2, 0])
        b3_txt = VGroup(
            fit(T("✓ Đã chứng minh: Thấm đỉnh lưới tam giác & Ising phẳng", 23, MINT), 7.0),
            fit(T("? Vẫn còn mở: Thấm cạnh trên lưới vuông Z²!", 24, PINK), 7.0),
            fit(T("? Đường đi tự tránh (Self-Avoiding Walk) → SLE₈/₃", 23, SUN), 7.0),
            fit(T("Mở đường cho học trò Hugo Duminil-Copin (Fields 2022)", 22, SKY), 7.0),
        ).arrange(DOWN, buff=0.32).move_to(box3)

        self.play(FadeIn(box3), FadeIn(b3_txt), run_time=1.1)
        end_vo("s2", t0, 9.5)
        save_tl()
