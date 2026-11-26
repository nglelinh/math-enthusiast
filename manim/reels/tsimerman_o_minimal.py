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
    "s1_tag": {"vi": "TÍNH O-TỐI TIỂU", "en": "O-MINIMALITY"},
    "s1_t": {"vi": "Hình học 'ngoan' không dao động vô hạn", "en": "Tame Geometry"},
    "s1_c1": {"vi": "Cấu trúc ℝ_an,exp: tập định nghĩa chỉ có\nhữu hạn thành phần liên thông!", "en": "Finitely many components"},
    "s1_c2": {"vi": "sin(x) trên ℝ bị CẤM (vô hạn nghiệm),\nnhưng sin(x) trên [0, 2π] thì hợp lệ!", "en": "sin(x) on [0, 2pi] is tame"},
    "s2_tag": {"vi": "ĐỊNH LÝ PILA–WILKIE", "en": "PILA–WILKIE"},
    "s2_t": {"vi": "Đếm điểm hữu tỉ trên đường cong siêu việt", "en": "Pila–Wilkie"},
    "s2_c1": {"vi": "Trên phần siêu việt của tập o-tối tiểu:\nsố điểm hữu tỉ chiều cao ≤ H tăng CHẬM hơn H^ε!", "en": "o(H^eps) growth"},
    "s3_tag": {"vi": "CHIẾN LƯỢC PILA–ZANNIER", "en": "PILA–ZANNIER"},
    "s3_t": {"vi": "Kẹp giữa Cận dưới Galois & Cận trên Pila–Wilkie", "en": "Pila–Zannier"},
    "s3_c1": {"vi": "1. Liên hợp Galois ép số điểm ≥ c · H^δ (tăng đa thức)\n2. Pila–Wilkie chặn số điểm ≤ C · H^ε (ε < δ)\n→ Mâu thuẫn! Chỉ còn hữu hạn nghiệm!", "en": "Galois vs Pila-Wilkie"},
}

class TsimermanOMinimal(Scene):
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
        ax, _ = mkaxes([0, 6.5, 1.5], [-1.3, 1.3, 1], 5.6, 2.0, [0, 2.0, 0])
        g_tame = ax.plot(lambda x: np.sin(x), x_range=[0, 6.28], color=MINT, stroke_width=4)
        self.play(Create(ax), Create(g_tame), run_time=1.2)
        c1 = card(6.3, 1.8, ACCENT).move_to([0, -0.3, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.8, RED).move_to([0, -2.4, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, RED), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, ax, g_tame, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.4, GOLD).move_to([0, 0.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 24, GOLD), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.8, MINT).move_to([0, 0.6, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, MINT), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.1)
        end_vo("s3", t0, 7.0)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
