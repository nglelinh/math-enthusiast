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
    "s1_tag": {"vi": "BÀI TOÁN CHIẾC KIM KAKEYA", "en": "KAKEYA"},
    "s1_t": {"vi": "Xoay kim độ dài 1 bằng diện tích 0?", "en": "Kakeya Needle"},
    "s1_c1": {"vi": "Besicovitch (1919): Có tập chứa đoạn thẳng\nđơn vị theo MỌI hướng nhưng diện tích bằng 0!", "en": "Zero area"},
    "s1_c2": {"vi": "Giả thuyết Kakeya: Trong ℝⁿ, tập Besicovitch\nvẫn bắt buộc có chiều Hausdorff bằng n!", "en": "dim_H = n"},
    "s2_tag": {"vi": "ĐỘT PHÁ 3 CHIỀU (2025)", "en": "3D KAKEYA"},
    "s2_t": {"vi": "Hong Wang & Joshua Zahl giải Kakeya ℝ³!", "en": "Wang & Zahl 2025"},
    "s2_c1": {"vi": "Sau khi Davies (1971) giải ℝ², chiều 3 treo suốt\nhơn 50 năm vì các ống δ-mảnh chồng chéo quá phức tạp.", "en": "50+ years open"},
    "s2_c2": {"vi": "Wang & Zahl (2025): Chứng minh dim_H(K) = 3\nbằng quy nạp đa thang & loại trừ cấu trúc 'hạt dính'!", "en": "Multiscale induction"},
    "s3_tag": {"vi": "FIELDS MEDAL 2026", "en": "FIELDS 2026"},
    "s3_t": {"vi": "Hong Wang — Giải tích Điều hòa", "en": "Hong Wang"},
    "s3_c1": {"vi": "Một trong những định lý hình học độ đo\nđược mong đợi nhất đầu thế kỷ XXI!", "en": "Landmark theorem"},
}

class WangKakeya(Scene):
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
        needles = VGroup(*[
            Line(
                [-1.3*np.cos(a), 2.1 - 1.3*np.sin(a), 0],
                [1.3*np.cos(a), 2.1 + 1.3*np.sin(a), 0],
                color=GOLD if i % 2 == 0 else ACCENT, stroke_width=3
            )
            for i, a in enumerate(np.linspace(0, np.pi, 9, endpoint=False))
        ])
        self.play(Create(needles), run_time=1.2)
        c1 = card(6.3, 1.8, ACCENT).move_to([0, -0.3, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.8, MINT).move_to([0, -2.4, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, needles, c1, t1, c2, t2), run_time=0.5)

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
        c1 = card(6.3, 2.2, MINT).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 24, MINT), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
