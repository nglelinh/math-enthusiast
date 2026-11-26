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

class DonaldsonIntersection(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Intersection form Q_X as 4D fingerprint
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("TÔPÔ 4 CHIỀU & DẠNG GIAO Q_X", "Ma trận vân tay của đa tạp 4 chiều")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        rows = [
            ("CP²", "Q = (1)", "Chéo hóa được (dương xác định)", SKY),
            ("S² × S²", "Q = [[0, 1], [1, 0]]", "Không xác định dấu (chẵn)", MINT),
            ("Lưới E₈", "Ma trận 8×8 xác định dương", "Chẵn, định thức = 1, KHÔNG chéo hóa!", PINK),
        ]
        cards = VGroup()
        for t1, t2, t3, col in rows:
            b = card(7.6, 2.0, col)
            g = VGroup(fit(T(t1, 25, col), 7.0), fit(T(t2, 23, SUN), 7.0), fit(T(t3, 21, WHITE), 7.0)).arrange(DOWN, buff=0.12).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.28).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in cards], lag_ratio=0.25), run_time=1.8)
        end_vo("s1", t0, 10.0)

        # s2: Freedman vs Donaldson collision (1982-1983)
        self.play(FadeOut(hdr), FadeOut(cards), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("CUỘC VA CHẠM LỊCH SỬ (1982–1983)", "Tự do Tôpô (Freedman) vs. Cứng rắn Trơn (Donaldson)")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box1 = card(7.6, 2.5, SKY).move_to([0, 2.0, 0])
        b1_txt = VGroup(
            fit(T("Freedman (Fields 1986 — Thế giới Tôpô):", 24, SKY), 7.0),
            fit(T("Mọi dạng giao đối xứng unimodular đều tạo được", 22, WHITE), 7.0),
            fit(T("đa tạp 4 chiều tôpô — kể cả đa tạp E₈!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.16).move_to(box1)

        box2 = card(7.6, 2.7, PINK).move_to([0, -1.5, 0])
        b2_txt = VGroup(
            fit(T("Donaldson (Fields 1986 — Thế giới Trơn):", 24, PINK), 7.0),
            fit(T("Nếu X TRƠN và Q_X xác định dấu, Q_X BẮT BUỘC chéo hóa!", 22, WHITE), 7.0),
            fit(T("⇒ Đa tạp E₈ TỒN TẠI tôpô nhưng KHÔNG CÓ cấu trúc trơn!", 22, SUN), 7.0),
        ).arrange(DOWN, buff=0.16).move_to(box2)

        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=1.0)
        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        end_vo("s2", t0, 10.0)
        save_tl()
