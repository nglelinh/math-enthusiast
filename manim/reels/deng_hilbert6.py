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
    "s1_tag": {"vi": "BÀI TOÁN THỨ 6 HILBERT", "en": "HILBERT'S SIXTH PROBLEM"},
    "s1_t": {"vi": "Ba thang đo của chất khí", "en": "Three Scales of a Gas"},
    "s1_b1": {"vi": "Vi mô: 10²⁵ quả cầu cứng Newton\n(giới hạn Boltzmann–Grad: N·ε^(d−1) ~ 1)", "en": "Micro: 10²⁵ Newton hard spheres\n(Boltzmann–Grad limit: N·ε^(d−1) ~ 1)"},
    "s1_b2": {"vi": "Trung mô: Phương trình Boltzmann\n→ Vĩ mô: Euler & Navier–Stokes–Fourier", "en": "Meso: Boltzmann kinetic equation\n→ Macro: Euler & Navier–Stokes–Fourier"},
    "s2_tag": {"vi": "RÀO CẢN GIAI THỪA n!", "en": "THE FACTORIAL WALL n!"},
    "s2_t": {"vi": "Vì sao Lanford (1975) kẹt suốt 50 năm?", "en": "Why Lanford (1975) Stopped Short"},
    "s2_c1": {"vi": "Đếm lịch sử va chạm theo chuỗi khai triển:\nsố cây va chạm tăng như n! → phân kỳ sớm!", "en": "Expanding collision histories in one shot:\ncollision trees grow like n! → early divergence!"},
    "s2_c2": {"vi": "Chỉ chứng minh được trong một phần nhỏ\ncủa thời gian tự do trung bình t ≪ t_0!", "en": "Only proved for a tiny fraction\nof one mean free time t ≪ t_0!"},
    "s3_tag": {"vi": "ĐỘT PHÁ DENG–HANI–MA", "en": "DENG–HANI–MA BREAKTHROUGH"},
    "s3_t": {"vi": "Thuật toán Cắt Đồ thị (2024–2025)", "en": "The Cutting Algorithm (2024–2025)"},
    "s3_c1": {"vi": "1. Chia thời gian dài [0, T] thành nhiều lát ngắn\n2. Mã hóa tái va chạm bằng đồ thị 'phân tử'", "en": "1. Slice long time [0, T] into short layers\n2. Encode recollisions as graph 'molecules'"},
    "s3_c2": {"vi": "3. Thuật toán cắt đồ thị (Cutting Algorithm)\nchặt nhỏ chu trình tái va chạm → đúng tới mọi T!", "en": "3. Cutting algorithm chops giant graphs,\ntaming recollisions up to ANY regular time T!"},
    "s3_bot": {"vi": "Nối trọn cây cầu: Newton → Boltzmann → Chất lưu", "en": "Full bridge: Newton → Boltzmann → Fluids"},
}

class DengHilbert6(Scene):
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
        b1 = card(6.3, 2.0, ACCENT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s1_b1"]), 23, FG), 5.9).move_to(b1)
        arr = Arrow([0, 0.7, 0], [0, -0.1, 0], color=GOLD, buff=0.05)
        b2 = card(6.3, 2.0, MINT).move_to([0, -1.2, 0])
        t2 = fit(T(tr(TX["s1_b2"]), 23, MINT), 5.9).move_to(b2)
        self.play(FadeIn(b1, t1), run_time=0.9)
        self.play(GrowArrow(arr), FadeIn(b2, t2), run_time=1.0)
        end_vo("s1", t0, 8.5)
        self.play(FadeOut(hdr, b1, t1, arr, b2, t2), run_time=0.5)

        # s2
        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.0, RED).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, RED), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, VIOLET).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, FG), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 8.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        # s3
        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, ACCENT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, GOLD).move_to([0, -0.9, 0])
        t2 = fit(T(tr(TX["s3_c2"]), 23, GOLD), 5.9).move_to(c2)
        bot = line(TX["s3_bot"], 22, MINT, -3.2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        self.play(FadeIn(bot), run_time=0.7)
        end_vo("s3", t0, 8.5)

        if tl_path:
            json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
