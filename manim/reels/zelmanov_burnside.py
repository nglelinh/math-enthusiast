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

class ZelmanovBurnside(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: 3 Burnside problems
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("BA BÀI TOÁN BURNSIDE (1902)", "Đừng bao giờ gộp chung!")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        rows = [
            ("1. Tổng quát (General)", "Mọi x có cấp hữu hạn → nhóm hữu hạn?", "SAI (Golod–Shafarevich)", PINK),
            ("2. Số mũ bị chặn B(d, n)", "Mọi x thỏa x^n = 1 → B(d,n) hữu hạn?", "SAI với n lẻ ≥ 665 (Novikov–Adian)", ORANGE),
            ("3. Hạn chế B₀(d, n)", "Chỉ xét các nhóm HỮU HẠN: cấp có bị chặn?", "ĐÚNG! (Zelmanov, Fields 1994)", MINT),
        ]
        cards = VGroup()
        for t1, t2, t3, col in rows:
            b = card(7.6, 2.05, col)
            g = VGroup(fit(T(t1, 24, col), 7.0), fit(T(t2, 21, WHITE), 7.0), fit(T(t3, 22, SUN), 7.0)).arrange(DOWN, buff=0.12).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.28).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in cards], lag_ratio=0.25), run_time=1.8)
        end_vo("s1", t0, 10.5)

        # s2: Worked examples n=2 and n=3
        self.play(FadeOut(hdr), FadeOut(cards), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("VÍ DỤ CẦM TAY", "n = 2 (giao hoán) vs. n = 3 (móc Lie)")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box1 = card(7.6, 2.6, SKY).move_to([0, 2.0, 0])
        b1_txt = VGroup(
            fit(T("Số mũ n = 2:  x² = 1  ⇒  x = x⁻¹", 25, SKY), 7.0),
            fit(T("ab = (ab)⁻¹ = b⁻¹a⁻¹ = ba  ⇒  Nhóm giao hoán!", 22, WHITE), 7.0),
            fit(T("⇒ B(d, 2) ≅ (Z/2Z)^d có cấp đúng bằng 2^d.", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box1)

        box2 = card(7.6, 2.8, SUN).move_to([0, -1.5, 0])
        b2_txt = VGroup(
            fit(T("Số mũ n = 3:  Không còn giao hoán!", 25, SUN), 7.0),
            fit(T("B(2, 3) có cấp 27 (nhóm Heisenberg trên F₃).", 22, WHITE), 7.0),
            fit(T("Hoán tử bậc 3 triệt tiêu → Đồng nhất thức Engel!", 22, PINK), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box2)

        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=1.0)
        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        end_vo("s2", t0, 10.0)
        save_tl()
