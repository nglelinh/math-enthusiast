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

class SmirnovPercolation(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Hexagonal lattice & p_c = 1/2
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("THẤM ĐỈNH TRÊN LƯỚI TỔ ONG", "Trò chơi Hex & Ngưỡng tới hạn p_c = 1/2")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        hex_grid = VGroup()
        cols = [SUN, SKY, SUN, SUN, SKY, SUN, SKY, SUN, SKY, SUN, SKY, SUN]
        idx = 0
        for r in range(3):
            for c in range(4):
                x = -1.8 + c * 1.15 + (0.57 if r % 2 else 0)
                y = 2.6 - r * 1.0
                h = RegularPolygon(n=6, radius=0.6, color=WHITE, stroke_width=2.5,
                                   fill_color=cols[idx % len(cols)], fill_opacity=0.65).move_to([x, y, 0])
                hex_grid.add(h)
                idx += 1
        lbl_hex = fit(T("Mỗi ô lục giác tô Vàng hoặc Xanh với xác suất 1/2", 24, SUN), 7.6).move_to([0, -0.4, 0])

        box1 = card(7.6, 2.5, SKY).move_to([0, -2.5, 0])
        b1_txt = VGroup(
            fit(T("Tính đối xứng Vàng ↔ Xanh ép P(nối xuyên) = 1/2!", 24, WHITE), 7.0),
            fit(T("Đó là lý do p_c = 1/2 trên lưới tam giác / tổ ong.", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box1)

        self.play(LaggedStart(*[FadeIn(h) for h in hex_grid], lag_ratio=0.06), run_time=1.3)
        self.play(FadeIn(lbl_hex), FadeIn(box1), FadeIn(b1_txt), run_time=0.9)
        end_vo("s1", t0, 9.5)

        # s2: Cardy-Carleson & Smirnov's 2001 proof
        self.play(FadeOut(hdr), FadeOut(hex_grid), FadeOut(lbl_hex), FadeOut(box1), FadeOut(b1_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("BẤT BIẾN BẢO GIÁC (SMIRNOV 2001)", "Bài báo 6 trang & Công thức Cardy–Carleson")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        tri = Polygon([-2.2, 0.2, 0], [2.2, 0.2, 0], [0, 3.8, 0], color=SKY, stroke_width=4)
        lA = T("A", 26, SUN).next_to([-2.2, 0.2, 0], DL, buff=0.15)
        lB = T("B", 26, SUN).next_to([2.2, 0.2, 0], DR, buff=0.15)
        lC = T("C", 26, SUN).next_to([0, 3.8, 0], UP, buff=0.15)
        px = Dot([1.1, 2.0, 0], color=PINK, radius=0.12)
        lx = T("X(x)", 22, PINK).next_to(px, UR, buff=0.1)

        box2 = card(7.6, 3.2, MINT).move_to([0, -2.2, 0])
        b2_txt = VGroup(
            fit(T("Công thức Carleson trên tam giác đều: P(A→C trước X) = x", 23, SUN), 7.0),
            fit(T("Phép đổi màu rời rạc cho H_A, H_B, H_C thỏa Cauchy–Riemann!", 22, WHITE), 7.0),
            fit(T("Khi bước lưới δ → 0: hội tụ tới hàm chỉnh hình bất biến bảo giác.", 22, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box2)

        self.play(Create(tri), FadeIn(lA), FadeIn(lB), FadeIn(lC), FadeIn(px), FadeIn(lx), run_time=1.3)
        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=0.9)
        end_vo("s2", t0, 10.0)
        save_tl()
