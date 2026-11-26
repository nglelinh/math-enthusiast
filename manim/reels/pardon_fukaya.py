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
    "s1_tag": {"vi": "PHẠM TRÙ FUKAYA", "en": "FUKAYA CATEGORY"},
    "s1_t": {"vi": "Đại số từ giao điểm Lagrangian", "en": "Fukaya Category"},
    "s1_c1": {"vi": "Vật thể: Đa tạp con Lagrangian L ⊂ M\nCấu xạ: Điểm giao L₀ ∩ L₁ (đồng điều Floer)", "en": "Objects & Morphisms"},
    "s1_c2": {"vi": "Phép hợp thành μ_k: đếm đĩa giả chỉnh hình\nk-góc nối các đỉnh giao điểm!", "en": "Composition"},
    "s2_tag": {"vi": "CHÍNH QUY DẪN XUẤT LOGA", "en": "LOG-DERIVED SMOOTHING"},
    "s2_t": {"vi": "Từ đa tạp góc sang Hình học dẫn xuất", "en": "Derived Geometry"},
    "s2_c1": {"vi": "Chu trình biên tạo ra đa tạp có góc (corners)\nvới cấu trúc tầng dày đặc.", "en": "Corners"},
    "s2_c2": {"vi": "Pardon xây dựng tính chính quy dẫn xuất loga:\nđồng nhất toàn bộ phép đếm Floer trên MỌI đa tạp!", "en": "Log-derived smoothing"},
    "s3_tag": {"vi": "ĐỐI XỨNG GƯƠNG & ICM 2026", "en": "MIRROR SYMMETRY"},
    "s3_t": {"vi": "Cầu nối Symplectic ↔ Đại số", "en": "Mirror Symmetry"},
    "s3_c1": {"vi": "Đối xứng gương đồng điều (Kontsevich):\nD^π Fuk(M) ≃ D^b Coh(M̌)", "en": "D^π Fuk(M) ≃ D^b Coh(M̌)"},
}

class PardonFukaya(Scene):
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
        c1 = card(6.3, 1.9, ACCENT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, GOLD).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 25, GOLD), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 7.0)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
