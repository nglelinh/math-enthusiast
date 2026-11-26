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
    "s1_tag": {"vi": "GIẢ THUYẾT ANDRÉ–OORT", "en": "ANDRÉ–OORT"},
    "s1_t": {"vi": "Điểm CM trên Đa tạp Shimura A_g", "en": "CM Points on A_g"},
    "s1_c1": {"vi": "Điểm đặc biệt (CM) ứng với đường cong elliptic\ncó phép nhân phức (nhiều đối xứng hơn bình thường).", "en": "CM points"},
    "s1_c2": {"vi": "André–Oort: Bao đóng Zariski của tập điểm CM\nphải là hợp hữu hạn các đa tạp con đặc biệt!", "en": "Zariski closure"},
    "s2_tag": {"vi": "CHỨNG MINH TOÀN PHẦN", "en": "FULL PROOF"},
    "s2_t": {"vi": "Tsimerman (2018) & Pila–Shankar–Tsimerman", "en": "Tsimerman 2018"},
    "s2_c1": {"vi": "Nút thắt từng kẹt: Cận dưới quỹ đạo Galois\nchỉ mới biết cho g = 1 (định lý Brauer–Siegel).", "en": "g = 1 bottleneck"},
    "s2_c2": {"vi": "Tsimerman (2018) chứng minh cận dưới cho A_g\nnhờ định lý Andreatta–Goren–Howard–Madapusi Pera!\n→ Khóa chặt André–Oort cho mọi đa tạp Shimura (2024).", "en": "All Shimura varieties"},
    "s3_tag": {"vi": "MỞ RỘNG SANG GRIFFITHS", "en": "GRIFFITHS"},
    "s3_t": {"vi": "Bakker–Brunebarbe–Tsimerman (2020–2023)", "en": "BBT"},
    "s3_c1": {"vi": "Xây dựng cấu trúc o-tối tiểu cho ánh xạ chu kỳ:\nchứng minh giả thuyết Griffiths về tính đại số!", "en": "Griffiths conjecture"},
}

class TsimermanAndreOort(Scene):
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
        c2 = card(6.3, 2.0, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, RED).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, RED), 5.9).move_to(c1)
        c2 = card(6.3, 2.2, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=1.0)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, VIOLET).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, FG), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 7.0)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
