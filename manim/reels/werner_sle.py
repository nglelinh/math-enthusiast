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

class WernerSLE(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Loewner encoding (1923) & xi(t)=0 example
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("MÃ HÓA LOEWNER (1923)", "Biến đường cong 2D thành điểm trượt 1D ξ(t)")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        base_line = Line([-3.4, 0.8, 0], [3.4, 0.8, 0], color=DIM, stroke_width=3)
        slit = Line([0, 0.8, 0], [0, 3.2, 0], color=SUN, stroke_width=6)
        dot_z = Dot([0, 3.2, 0], color=PINK, radius=0.11)
        lbl_ex = fit(T("Ví dụ ξ(t) ≡ 0:  g_t(z) = √(z² + 4t)  →  vẽ đoạn thẳng đứng [0, 2i√t]", 22, SUN), 7.6).move_to([0, -0.2, 0])

        box1 = card(7.6, 2.7, SKY).move_to([0, -2.3, 0])
        b1_txt = VGroup(
            fit(T("∂_t g_t(z) = 2 / (g_t(z) − ξ(t))", 26, SKY), 7.0),
            fit(T("Mọi đường cong đơn 2D trên nửa mặt phẳng trên H", 22, WHITE), 7.0),
            fit(T("đều được mã hóa gọn bởi 1 hàm thực liên tục ξ(t)!", 22, MINT), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box1)

        self.play(Create(base_line), Create(slit), FadeIn(dot_z), run_time=1.2)
        self.play(FadeIn(lbl_ex), FadeIn(box1), FadeIn(b1_txt), run_time=0.9)
        end_vo("s1", t0, 10.0)

        # s2: Schramm's 2000 breakthrough -> SLE_kappa
        self.play(FadeOut(hdr), FadeOut(base_line), FadeOut(slit), FadeOut(dot_z), FadeOut(lbl_ex), FadeOut(box1), FadeOut(b1_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("BƯỚC NGOẶT SCHRAMM (2000)", "Cắm chuyển động Brown ξ(t) = √κ · B_t")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        rows = [
            ("κ = 2", "Cây khung đồng đều / LERW", SKY),
            ("κ = 3", "Đường biên Mô hình Ising phẳng (Smirnov)", MINT),
            ("κ = 6", "Đường biên Thấm (Percolation) — tính địa phương", SUN),
            ("κ = 8/3", "Biên ngoài Brown & Đường đi tự tránh (dự đoán)", PINK),
        ]
        cards = VGroup()
        for k_t, d_t, col in rows:
            b = card(7.6, 1.55, col)
            g = VGroup(fit(T(k_t, 26, col), 1.8), fit(T(d_t, 22, WHITE), 5.2)).arrange(RIGHT, buff=0.3).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.24).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.18) for c in cards], lag_ratio=0.22), run_time=1.8)
        end_vo("s2", t0, 10.5)
        save_tl()
