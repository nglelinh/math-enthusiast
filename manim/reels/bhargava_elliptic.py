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
    "s1_tag": {"vi": "ĐƯỜNG CONG ELLIPTIC", "en": "ELLIPTIC CURVES"},
    "s1_t": {"vi": "Hạng Mordell–Weil & Điểm hữu tỉ", "en": "Rank & Rational Points"},
    "s1_c1": {"vi": "Đường cong y² = x³ + Ax + B:\ntập điểm hữu tỉ lập thành nhóm ℤ^r ⊕ T.", "en": "y^2 = x^3 + Ax + B"},
    "s1_c2": {"vi": "Giả thuyết Goldfeld dự đoán hạng trung bình r\ncủa mọi đường cong elliptic đúng bằng 1/2!", "en": "Average rank = 1/2"},
    "s2_tag": {"vi": "BHARGAVA–SHANKAR (2015)", "en": "BHARGAVA–SHANKAR"},
    "s2_t": {"vi": "Chặn chặt Hạng trung bình < 0,885", "en": "Bounding Average Rank"},
    "s2_c1": {"vi": "Đếm nhóm Selmer bậc 2, 3, 4, 5 bằng cách\nquy về quỹ đạo dạng bậc 4 trên đường tròn!", "en": "Counting Selmer groups"},
    "s2_c2": {"vi": "Suy ra tỷ lệ dương đường cong có hạng 0\nvà hạng 1 — bước tiến lớn hướng về BSD!", "en": "Positive proportion rank 0 & 1"},
    "s3_tag": {"vi": "PHÂN BIỆT VỚI GIẢ THUYẾT BSD", "en": "BSD CONJECTURE"},
    "s3_t": {"vi": "Những gì đã chứng minh vs vẫn mở", "en": "Proved vs Open"},
    "s3_c1": {"vi": "Đã chứng minh: E[r] hữu hạn (< 0,885).\nVẫn mở: BSD cho từng đường cong riêng lẻ hạng ≥ 2!", "en": "BSD remains open for rank >= 2"},
}

class BhargavaElliptic(Scene):
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
        c2 = card(6.3, 1.9, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, MINT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, MINT), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, VIOLET).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, FG), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, RED).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, RED), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
