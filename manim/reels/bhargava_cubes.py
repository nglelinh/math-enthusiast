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
    "s1_tag": {"vi": "KHỐI LẬP PHƯƠNG BHARGAVA", "en": "BHARGAVA CUBES"},
    "s1_t": {"vi": "Luật hợp thành Gauss từ khối 2×2×2", "en": "Gauss Composition"},
    "s1_c1": {"vi": "Cắt khối lập phương 8 số nguyên (a,b,c,d,e,f,g,h)\ntheo 3 cặp mặt đối diện → 3 dạng toàn phương Q₁, Q₂, Q₃!", "en": "3 quadratic forms"},
    "s1_c2": {"vi": "Trong nhóm lớp lý tưởng: [Q₁] + [Q₂] + [Q₃] = 0!\nMở rộng Gauss sang vành bậc 3, 4, 5!", "en": "Higher composition laws"},
    "s2_tag": {"vi": "ĐẾM VÀNH & TRƯỜNG SỐ", "en": "COUNTING RINGS"},
    "s2_t": {"vi": "Hình học các số trên không gian quỹ đạo", "en": "Geometry of Numbers"},
    "s2_c1": {"vi": "Mỗi quỹ đạo SL(n, ℤ) trên không gian đa thức\nđếm chính xác một lớp vành hoặc trường bậc n.", "en": "Orbits count rings"},
    "s2_c2": {"vi": "Dùng nguyên lý điểm lưới trong miền cơ bản\nđể tính mật độ tiệm cận của trường bậc 3, 4, 5!", "en": "Asymptotic density"},
    "s3_tag": {"vi": "FIELDS MEDAL 2014", "en": "FIELDS 2014"},
    "s3_t": {"vi": "Manjul Bhargava — Trực giác Hình học", "en": "Manjul Bhargava"},
    "s3_c1": {"vi": "Biến đại số trừu tượng của luật hợp thành\nthành hình học trực quan chỉ từ một khối Rubik!", "en": "Visualizing algebra"},
}

class BhargavaCubes(Scene):
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
        sq1 = Square(side_length=1.6, color=ACCENT, stroke_width=3).move_to([-0.3, 1.9, 0])
        sq2 = Square(side_length=1.6, color=GOLD, stroke_width=3).move_to([0.4, 2.4, 0])
        edges = VGroup(*[Line(sq1.get_corner(c), sq2.get_corner(c), color=MINT, stroke_width=2.5) for c in (UL, UR, DL, DR)])
        self.play(Create(sq1), Create(sq2), Create(edges), run_time=1.2)
        c1 = card(6.3, 1.8, ACCENT).move_to([0, -0.3, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 22, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.8, GOLD).move_to([0, -2.4, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, sq1, sq2, edges, c1, t1, c2, t2), run_time=0.5)

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
        c1 = card(6.3, 2.2, GOLD).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 24, GOLD), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
