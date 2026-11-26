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
    "s1_tag": {"vi": "HÌNH HỌC SONG HỮU TỈ", "en": "BIRATIONAL GEOMETRY"},
    "s1_t": {"vi": "Phép nổ & Phép phẫu thuật sạch", "en": "Blow-Ups & Clean Surgery"},
    "s1_c1": {"vi": "Đường tròn x² + y² = 1  ↔  Đường thẳng ℝ\n(chiếu nổi bỏ đúng 1 điểm)", "en": "Circle x² + y² = 1  ↔  Line ℝ\n(stereographic projection minus 1 point)"},
    "s1_c2": {"vi": "Phép nổ (Blow-up): tách điểm tự cắt\nthành 2 nhánh trơn riêng biệt!", "en": "Blow-up: separate a self-crossing node\ninto 2 smooth branches!"},
    "s2_tag": {"vi": "BẢNG TUẦN HOÀN HÌNH HỌC", "en": "GEOMETRIC PERIODIC TABLE"},
    "s2_t": {"vi": "Ba viên gạch qua lớp chính tắc K_X", "en": "Three Building Blocks via K_X"},
    "s2_b1": {"vi": "1. Fano (K_X < 0, cong dương)\nSiêu mặt bậc d < n+1 trong ℙⁿ", "en": "1. Fano (K_X < 0, positive curvature)\nDegree d < n+1 hypersurface in ℙⁿ"},
    "s2_b2": {"vi": "2. Calabi–Yau (K_X = 0, phẳng)\nSiêu mặt bậc d = n+1 trong ℙⁿ", "en": "2. Calabi–Yau (K_X = 0, Ricci-flat)\nDegree d = n+1 hypersurface in ℙⁿ"},
    "s2_b3": {"vi": "3. Kiểu tổng quát (K_X > 0, cong âm)\nSiêu mặt bậc d > n+1 trong ℙⁿ", "en": "3. General Type (K_X > 0, negative)\nDegree d > n+1 hypersurface in ℙⁿ"},
    "s2_bot": {"vi": "Ví dụ trong ℙ³: d=3 Fano · d=4 K3 · d≥5 Tổng quát", "en": "In ℙ³: d=3 Fano · d=4 K3 · d≥5 General Type"},
    "s3_tag": {"vi": "MMP & ĐỊNH LÝ BIRKAR", "en": "MMP & BIRKAR'S THEOREM"},
    "s3_t": {"vi": "Từ Flip đến Tính bị chặn Fano", "en": "From Flips to Fano Boundedness"},
    "s3_c1": {"vi": "Chiều 2: chỉ cần co đường cong (−1)\nChiều ≥ 3: co sinh kỳ dị xấu → cần FLIP!", "en": "Dim 2: just contract (−1)-curves\nDim ≥ 3: contractions fail → need FLIPS!"},
    "s3_c2": {"vi": "BCHM (2010): Flip luôn tồn tại\nvà vành chính tắc hữu hạn sinh.", "en": "BCHM (2010): Flips exist &\ncanonical rings are finitely generated."},
    "s3_c3": {"vi": "Birkar (2016, BAB): Mọi đa tạp ε-lc Fano\ncùng chiều thuộc hữu hạn họ đại số!", "en": "Birkar (2016, BAB): All ε-lc Fano varieties\nof fixed dim lie in finitely many families!"},
}

class BirkarMMP(Scene):
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
        circ = Circle(radius=1.15, color=ACCENT, stroke_width=4).move_to([-1.6, 2.2, 0])
        np_dot = Dot([-1.6, 3.35, 0], color=RED, radius=0.09)
        line_r = Line([0.2, 1.05, 0], [2.7, 1.05, 0], color=MINT, stroke_width=4)
        ray = DashedLine([-1.6, 3.35, 0], [1.6, 1.05, 0], color=GOLD, stroke_width=2.5)
        p_c = Dot([-0.68, 2.68, 0], color=GOLD, radius=0.08)
        p_l = Dot([1.6, 1.05, 0], color=GOLD, radius=0.08)
        self.play(Create(circ), Create(line_r), FadeIn(np_dot, ray, p_c, p_l), run_time=1.2)
        c1_box = card(6.2, 1.5, ACCENT).move_to([0, -0.3, 0])
        c1_txt = fit(T(tr(TX["s1_c1"]), 23, FG), 5.8).move_to(c1_box)
        c2_box = card(6.2, 1.7, MINT).move_to([0, -2.5, 0])
        c2_txt = fit(T(tr(TX["s1_c2"]), 23, MINT), 5.8).move_to(c2_box)
        self.play(FadeIn(c1_box, c1_txt), run_time=0.8)
        self.play(FadeIn(c2_box, c2_txt), run_time=0.9)
        end_vo("s1", t0, 8.0)
        self.play(FadeOut(hdr, circ, np_dot, line_r, ray, p_c, p_l, c1_box, c1_txt, c2_box, c2_txt), run_time=0.5)

        # s2
        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        b1 = card(6.3, 1.7, MINT).move_to([0, 2.5, 0])
        t1 = fit(T(tr(TX["s2_b1"]), 23, MINT), 5.9).move_to(b1)
        b2 = card(6.3, 1.7, GOLD).move_to([0, 0.3, 0])
        t2 = fit(T(tr(TX["s2_b2"]), 23, GOLD), 5.9).move_to(b2)
        b3 = card(6.3, 1.7, RED).move_to([0, -1.9, 0])
        t3 = fit(T(tr(TX["s2_b3"]), 23, RED), 5.9).move_to(b3)
        bot = line(TX["s2_bot"], 21, ACCENT, -3.7)
        self.play(FadeIn(b1, t1), run_time=0.8)
        self.play(FadeIn(b2, t2), run_time=0.8)
        self.play(FadeIn(b3, t3), run_time=0.8)
        self.play(FadeIn(bot), run_time=0.7)
        end_vo("s2", t0, 8.5)
        self.play(FadeOut(hdr, b1, t1, b2, t2, b3, t3, bot), run_time=0.5)

        # s3
        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.7, VIOLET).move_to([0, 2.4, 0])
        k1 = fit(T(tr(TX["s3_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.7, ACCENT).move_to([0, 0.1, 0])
        k2 = fit(T(tr(TX["s3_c2"]), 23, ACCENT), 5.9).move_to(c2)
        c3 = card(6.3, 1.9, GOLD).move_to([0, -2.3, 0])
        k3 = fit(T(tr(TX["s3_c3"]), 23, GOLD), 5.9).move_to(c3)
        self.play(FadeIn(c1, k1), run_time=0.9)
        self.play(FadeIn(c2, k2), run_time=0.9)
        self.play(FadeIn(c3, k3), run_time=1.0)
        end_vo("s3", t0, 9.0)

        if tl_path:
            json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
