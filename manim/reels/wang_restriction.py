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
    "s1_tag": {"vi": "CẤU TRÚC HẠT DÍNH (STICKY)", "en": "STICKY KAKEYA"},
    "s1_t": {"vi": "Bốn bước loại trừ mọi ngoại lệ trong ℝ³", "en": "Four Steps"},
    "s1_b1": {"vi": "1. Quy về tập Kakeya có cấu trúc 'hạt' (grainy)\n2. Tách 3 kịch bản: tập trung tấm, dày đặc, hoặc tách rời", "en": "Grainy reduction"},
    "s1_b2": {"vi": "3. Dùng bất đẳng thức đa thang (multiscale) chặt đứt\nsự cộng hưởng giữa các ống ở nhiều tỷ lệ δ", "en": "Multiscale induction"},
    "s2_tag": {"vi": "GIẢ THUYẾT HẠN CHẾ FOURIER", "en": "RESTRICTION"},
    "s2_t": {"vi": "Từ Chiếc kim đến Sóng & PDE tán sắc", "en": "Fourier Restriction"},
    "s2_c1": {"vi": "Giả thuyết hạn chế Fourier (Stein): sóng tập trung\ntrên mặt cong (cầu/paraboloid) giao thoa ra sao?", "en": "Stein's conjecture"},
    "s2_c2": {"vi": "Hong Wang đẩy kỷ lục chặn hạn chế ℝ³,\ntiến sát ngưỡng tới hạn cho phương trình sóng!", "en": "New restriction bounds"},
    "s3_tag": {"vi": "BẢN ĐỒ LIÊN KẾT", "en": "HIERARCHY"},
    "s3_t": {"vi": "Kakeya ↔ Hạn chế Fourier ↔ PDE", "en": "Hierarchy"},
    "s3_c1": {"vi": "Thang phân cấp Bourgain–Stein:\nHạn chế Fourier ⇒ Bochner–Riesz ⇒ Kakeya!", "en": "Restriction -> Kakeya"},
}

class WangRestriction(Scene):
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
        b1 = card(6.3, 2.0, ACCENT).move_to([0, 1.8, 0])
        k1 = fit(T(tr(TX["s1_b1"]), 22, FG), 5.9).move_to(b1)
        b2 = card(6.3, 2.0, MINT).move_to([0, -1.0, 0])
        k2 = fit(T(tr(TX["s1_b2"]), 22, MINT), 5.9).move_to(b2)
        self.play(FadeIn(b1, k1), run_time=0.9)
        self.play(FadeIn(b2, k2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, b1, k1, b2, k2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, GOLD).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 24, GOLD), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
