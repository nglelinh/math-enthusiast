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
    "s1_tag": {"vi": "CỘNG HƯỞNG 4 SÓNG", "en": "4-WAVE RESONANCE"},
    "s1_t": {"vi": "Từ hạt khí sang sóng phi tuyến", "en": "From Gas Particles to Nonlinear Waves"},
    "s1_c1": {"vi": "k₁ + k₂ = k₃ + k₄  và  |k₁|² + |k₂|² = |k₃|² + |k₄|²\n→ 4 vectơ tần số tạo thành HÌNH CHỮ NHẬT!", "en": "k₁ + k₂ = k₃ + k₄  &  |k₁|² + |k₂|² = |k₃|² + |k₄|²\n→ 4 wave vectors form a RECTANGLE!"},
    "s2_tag": {"vi": "PHƯƠNG TRÌNH ĐỘNG HỌC SÓNG", "en": "WAVE KINETIC EQUATION"},
    "s2_t": {"vi": "Deng–Hani: Suy ra WKE từ NLS", "en": "Deng–Hani: Deriving WKE from NLS"},
    "s2_c1": {"vi": "Dùng tổ hợp giản đồ Feynman + PDE xác suất:\nkiểm soát hàng tỉ tương tác sóng ngẫu nhiên.", "en": "Using Feynman diagram combinatorics + random\nPDEs: taming billions of wave interactions."},
    "s2_c2": {"vi": "Đặt nền móng toán học chặt chẽ cho\nlý thuyết nhiễu loạn sóng (Wave Turbulence).", "en": "Placed wave turbulence theory on\nrigorous mathematical footing."},
    "s3_tag": {"vi": "FIELDS 2026 & BÀI TOÁN MỞ", "en": "2026 FIELDS & OPEN FRONTIERS"},
    "s3_t": {"vi": "Yu Deng & Những gì còn bỏ ngỏ", "en": "Yu Deng & What Remains Open"},
    "s3_c1": {"vi": "Đã mở: cầu nối dài hạn Newton → Boltzmann\nvà suy dẫn động học sóng (WKE).", "en": "Solved: long-time Newton → Boltzmann bridge\nand rigorous wave kinetic derivation."},
    "s3_c2": {"vi": "Vẫn còn mở: tính trơn toàn cục Navier–Stokes\n(Millennium) và dòng rối vượt ngoài thời gian trơn T.", "en": "Still open: global Navier–Stokes smoothness\n(Millennium) & turbulence past regular time T."},
}

class DengWaveKinetic(Scene):
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

        # s1
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header(tr(TX["s1_tag"]), tr(TX["s1_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        rect = Rectangle(width=3.2, height=1.8, color=GOLD, stroke_width=4).move_to([0, 2.0, 0])
        corners = [rect.get_corner(UL), rect.get_corner(DR), rect.get_corner(UR), rect.get_corner(DL)]
        labels = ["k₁", "k₂", "k₃", "k₄"]
        cols = [ACCENT, ACCENT, MINT, MINT]
        dots = VGroup(*[Dot(c, color=col, radius=0.12) for c, col in zip(corners, cols)])
        lbls = VGroup(*[T(l, 24, col).next_to(c, UP if i in (0,2) else DOWN, buff=0.16)
                        for i, (l, c, col) in enumerate(zip(labels, corners, cols))])
        self.play(Create(rect), FadeIn(dots, lbls), run_time=1.2)
        c1 = card(6.3, 2.0, ACCENT).move_to([0, -1.2, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 22, FG), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=0.9)
        end_vo("s1", t0, 8.5)
        self.play(FadeOut(hdr, rect, dots, lbls, c1, t1), run_time=0.5)

        # s2
        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.0, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 8.5)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        # s3
        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, GOLD).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, GOLD), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, RED).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s3_c2"]), 23, RED), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s3", t0, 8.5)

        if tl_path:
            json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
