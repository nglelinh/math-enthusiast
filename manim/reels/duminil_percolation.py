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
    "s1_tag": {"vi": "THẤM & TỰ TRÁNH", "en": "PERCOLATION & SAW"},
    "s1_t": {"vi": "Hằng số liên kết tổ ong √(2+√2)", "en": "Connective Constant"},
    "s1_c1": {"vi": "Duminil-Copin & Smirnov (2012): Chứng minh\nhằng số liên kết đường tự tránh trên lưới tổ ong = √(2+√2)!", "en": "Exact honeycomb constant"},
    "s1_c2": {"vi": "Sử dụng biến quan sát parafermion rời rạc\nvà bất đẳng thức tích phân biên!", "en": "Parafermionic observable"},
    "s2_tag": {"vi": "BẤT ĐẲNG THỨC SẮC BÉN", "en": "SHARP THRESHOLDS"},
    "s2_t": {"vi": "Chuyển pha sắc bén trên lưới tùy ý", "en": "Sharpness on Graphs"},
    "s2_c1": {"vi": "Chứng minh dưới ngưỡng p < p_c, xác suất cụm\nlớn giảm theo hàm mũ e^(−c·n) với mọi mô hình FK!", "en": "Exponential decay below p_c"},
    "s2_c2": {"vi": "Giải quyết tính bất biến quay ở chiều 2 cho\nmô hình cluster ngẫu nhiên FK!", "en": "2D rotational invariance"},
    "s3_tag": {"vi": "ĐƯỜNG CHÂN TRỜI MỞ", "en": "OPEN HORIZON"},
    "s3_t": {"vi": "Thấm 3D tại đúng ngưỡng p_c", "en": "3D Percolation at p_c"},
    "s3_c1": {"vi": "Bài toán lớn vẫn mở: Chứng minh không có cụm\nvô hạn tại đúng p = p_c cho thấm Bernoulli 3D!", "en": "3D critical percolation"},
}

class DuminilPercolation(Scene):
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
        c1 = card(6.3, 2.0, GOLD).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 22, GOLD), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, ACCENT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, FG), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, MINT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, MINT), 5.9).move_to(c1)
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
