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

class VillaniLandau(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Phase mixing in 1D collisionless plasma
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("TẮT DẦN LANDAU (1946)", "Ma sát không va chạm qua Trộn pha")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        ax, lab = mkaxes([0, 6.28, 1.57], [-1.5, 1.5, 1], 6.4, 3.0, [0, 2.0, 0], xt=[0, 3, 6], yt=[(-1, "-v"), (1, "+v")])
        bars = VGroup(*[Line(ax.c2p(0, y), ax.c2p(6.2, y), color=SKY, stroke_width=4) for y in [-0.9, -0.3, 0.3, 0.9]])
        tilted = VGroup(*[Line(ax.c2p(0, y), ax.c2p(6.2, y), color=MINT, stroke_width=4).rotate(0.25*y) for y in [-0.9, -0.3, 0.3, 0.9]])
        lbl1 = fit(T("Vận tốc v khác nhau → sợi pha cuộn xoắn (Phase Mixing)", 23, SUN), 7.6).move_to([0, -0.2, 0])

        box1 = card(7.6, 2.7, SKY).move_to([0, -2.3, 0])
        b1_txt = VGroup(
            fit(T("Không cần va chạm, entropy vẫn giữ nguyên", 23, WHITE), 7.0),
            fit(T("Nhưng mật độ trung bình theo v → phẳng dần,", 23, WHITE), 7.0),
            fit(T("khiến điện trường E(t) tắt dần theo hàm mũ!", 24, MINT), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box1)

        self.play(Create(ax), FadeIn(lab), Create(bars), run_time=1.0)
        self.play(Transform(bars, tilted), FadeIn(lbl1), run_time=1.2)
        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=0.8)
        end_vo("s1", t0, 10.0)

        # s2: Plasma echoes & Mouhot-Villani (2011)
        self.play(FadeOut(hdr), FadeOut(ax), FadeOut(lab), FadeOut(bars), FadeOut(lbl1), FadeOut(box1), FadeOut(b1_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("MOUHOT–VILLANI (ACTA 2011)", "Vượt bẫy Tiếng vọng Plasma (Plasma Echoes)")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box2 = card(7.6, 3.0, PINK).move_to([0, 1.8, 0])
        b2_txt = VGroup(
            fit(T("Mối đe dọa phi tuyến: Tiếng vọng Plasma", 25, PINK), 7.0),
            fit(T("Các mode dao động cũ cộng hưởng ngược lại", 22, WHITE), 7.0),
            fit(T("có thể làm điện trường bùng nổ trở lại!", 23, SUN), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box2)

        box3 = card(7.6, 3.0, MINT).move_to([0, -1.9, 0])
        b3_txt = VGroup(
            fit(T("Đột phá Mouhot–Villani (2011):", 25, MINT), 7.0),
            fit(T("Dùng chuẩn giải tích Gevrey (trơn cực mạnh)", 23, WHITE), 7.0),
            fit(T("→ Khống chế toàn bộ chuỗi tiếng vọng cho Vlasov–Poisson!", 22, SKY), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box3)

        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        self.play(FadeIn(box3), FadeIn(b3_txt), run_time=1.0)
        end_vo("s2", t0, 10.0)
        save_tl()
