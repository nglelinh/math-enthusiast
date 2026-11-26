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
    "s1_tag": {"vi": "QUE SỐ HỌC", "en": "ARITHMETIC QUE"},
    "s1_t": {"vi": "Sóng riêng trên Mặt Hyperbolic có hội tụ đều?", "en": "Quantum Unique Ergodicity"},
    "s1_c1": {"vi": "Giả thuyết Rudnick–Sarnak (1994): Khi năng lượng λ → ∞,\nhàm riêng Maass |φ_λ|² dx dy phải trải đều trên mặt modular!", "en": "Equidistribution of eigenfunctions"},
    "s1_c2": {"vi": "Không có 'vết sẹo lượng tử' (quantum scars) tập trung\nquanh các quỹ đạo trắc địa đóng!", "en": "No quantum scars"},
    "s2_tag": {"vi": "ĐỊNH LÝ LINDENSTRAUSS (2006)", "en": "LINDENSTRAUSS 2006"},
    "s2_t": {"vi": "Dùng toán tử Hecke khóa chặt Giới hạn Lượng tử", "en": "Hecke Operators"},
    "s2_c1": {"vi": "Kết hợp tính bất biến dòng trắc địa với vô hạn\ntoán tử Hecke → entropy > 0 → bắt buộc là độ đo Lebesgue!", "en": "Positive entropy -> Lebesgue"},
    "s2_c2": {"vi": "Soundararajan (2010) bổ sung mảnh cuối cho mặt không\ncompact SL(2,ℝ)/SL(2,ℤ), hoàn tất QUE số học!", "en": "Completed by Soundararajan"},
    "s3_tag": {"vi": "NỐI TIẾP VENKATESH & AVILA", "en": "UNIFIED LANDSCAPE"},
    "s3_t": {"vi": "Sợi chỉ đỏ Động lực học Thuần nhất", "en": "Homogeneous Dynamics"},
    "s3_c1": {"vi": "Từ Ratner → Margulis → Lindenstrauss → Venkatesh:\nđộng lực học thuần nhất là vũ khí giải tích số học hiện đại!", "en": "Number theory via dynamics"},
}

class LindenstraussQUE(Scene):
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
        t1 = fit(T(tr(TX["s1_c1"]), 22, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, GOLD).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, GOLD), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, VIOLET).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, FG), 5.9).move_to(c2)
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
