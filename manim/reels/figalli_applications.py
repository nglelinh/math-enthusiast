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
    t2 = fit(T(title, 34, WHITE), 7.8)
    return VGroup(t1, t2).arrange(DOWN, buff=0.14).move_to([0, 6.2, 0])

TX = {
    "s1_tag": {"vi": "BA ỨNG DỤNG ĐỈNH CAO", "en": "THREE APPLICATIONS"},
    "s1_t": {"vi": "Từ Tinh thể đến Khí quyển & Ma trận ngẫu nhiên", "en": "Crystals, Weather & Matrices"},
    "s1_b1": {"vi": "1. Bất đẳng thức đẳng chu tinh thể định lượng\n(hình dạng giọt tinh thể gần tối ưu Wulff)", "en": "Isoperimetric inequalities"},
    "s1_b2": {"vi": "2. Hệ bán địa chuyển trong khí tượng học\n3. Phổ ma trận ngẫu nhiên & thống kê đa chiều", "en": "Meteorology & random matrices"},
    "s2_tag": {"vi": "VILLANI vs FIGALLI", "en": "VILLANI vs FIGALLI"},
    "s2_t": {"vi": "Hai Huy chương Fields, hai phong cách", "en": "Two Fields Medals"},
    "s2_c1": {"vi": "Villani (2010): Độ cong Ricci trên không gian metric\n(Lott–Sturm–Villani) & tắt dần Landau.", "en": "Villani: Ricci curvature"},
    "s2_c2": {"vi": "Figalli (2018): Giải tích PDE sắc bén cho\nMonge–Ampère, tập kỳ dị & tinh thể định lượng.", "en": "Figalli: Monge-Ampere PDE"},
    "s3_tag": {"vi": "CHÌA KHÓA TƯ DUY", "en": "KEY INSIGHT"},
    "s3_t": {"vi": "Mọi cực trị tối ưu đều là PDE hình học", "en": "Optimal maps as PDE"},
    "s3_c1": {"vi": "Từ bài toán kinh tế Monge thế kỷ XVIII đến\nAI hiện đại: vận chuyển tối ưu là hình học gradient lồi!", "en": "Convex gradient geometry"},
}

class FigalliApplications(Scene):
    def construct(self):
        self.camera.background_color = BG
        vo_durs = json.load(open(os.environ["VO_DUR_JSON"])) if os.environ.get("VO_DUR_JSON") else {}
        tl_path = os.environ.get("VO_TIMELINE_JSON")
        timeline = []
        def end_vo(sid, t0, fb):
            dur = vo_durs.get(sid)
            if dur is not None:
                rem = dur - (self.time - t0) + 0.35
                if rem > 0.05: self.wait(rem)
            else:
                self.wait(fb)

        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header(tr(TX["s1_tag"]), tr(TX["s1_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        b1 = card(6.3, 1.9, ACCENT).move_to([0, 1.8, 0])
        k1 = fit(T(tr(TX["s1_b1"]), 22, FG), 5.9).move_to(b1)
        b2 = card(6.3, 1.9, MINT).move_to([0, -1.0, 0])
        k2 = fit(T(tr(TX["s1_b2"]), 22, MINT), 5.9).move_to(b2)
        self.play(FadeIn(b1, k1), run_time=0.9)
        self.play(FadeIn(b2, k2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, b1, k1, b2, k2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, MINT).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, MINT), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
