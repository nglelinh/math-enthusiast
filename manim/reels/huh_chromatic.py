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
    "s1_tag": {"vi": "ĐA THỨC SẮC SỐ", "en": "CHROMATIC POLYNOMIAL"},
    "s1_t": {"vi": "Tính lõm loga qua K₃ và K₄", "en": "Log-Concavity for K₃ and K₄"},
    "s1_c1": {"vi": "K₃: P(q) = q³ − 3q² + 2q\n|hệ số| = (1, 3, 2)  →  3² = 9 ≥ 1·2", "en": "K₃: P(q) = q³ − 3q² + 2q\n|coeffs| = (1, 3, 2)  →  3² = 9 ≥ 1·2"},
    "s1_c2": {"vi": "K₄: P(q) = q⁴ − 6q³ + 11q² − 6q\n(1, 6, 11, 6):  6²≥11,  11²=121≥36!", "en": "K₄: P(q) = q⁴ − 6q³ + 11q² − 6q\n(1, 6, 11, 6):  6²≥11,  11²=121≥36!"},
    "s2_tag": {"vi": "BÓNG DÁNG HODGE", "en": "THE SHADOW OF HODGE"},
    "s2_t": {"vi": "June Huh (2012): Hình học giải Tổ hợp", "en": "June Huh (2012): Geometry Solves Counting"},
    "s2_c1": {"vi": "Giả thuyết Read (1968) & Heron–Rota–Welsh:\na_k² ≥ a_{k−1} · a_{k+1} cho MỌI đồ thị & matroid.", "en": "Read (1968) & Heron–Rota–Welsh:\na_k² ≥ a_{k−1} · a_{k+1} for ALL graphs & matroids."},
    "s2_c2": {"vi": "Với đồ thị thực hiện được, hệ số a_k là\nsố giao điểm trên đa tạp đại số → Hodge–Riemann!", "en": "For realizable graphs, a_k are intersection\nnumbers on a variety → Hodge–Riemann!"},
    "s3_tag": {"vi": "LÝ THUYẾT HODGE TỔ HỢP", "en": "COMBINATORIAL HODGE THEORY"},
    "s3_t": {"vi": "Hodge KHÔNG cần đa tạp!", "en": "Hodge Theory WITHOUT a Variety!"},
    "s3_c1": {"vi": "Rào cản: Hầu hết matroid KHÔNG có\nđa tạp đại số nào phía sau!", "en": "Wall: Almost all matroids have NO\nunderlying algebraic variety!"},
    "s3_c2": {"vi": "Adiprasito–Huh–Katz (2018):\nChứng minh gói Hodge trực tiếp trên vành Chow A*(M)!", "en": "Adiprasito–Huh–Katz (2018):\nProved the Hodge package directly on Chow ring A*(M)!"},
    "s3_bot": {"vi": "Huy chương Fields 2022 · June Huh", "en": "2022 Fields Medal · June Huh"},
}

class HuhChromatic(Scene):
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
        # Draw K3 triangle with colored vertices
        v1 = [-1.2, 3.0, 0]; v2 = [-2.1, 1.5, 0]; v3 = [-0.3, 1.5, 0]
        tri = VGroup(Line(v1, v2, color=MUTED), Line(v2, v3, color=MUTED), Line(v3, v1, color=MUTED),
                     Dot(v1, color=RED, radius=0.14), Dot(v2, color=MINT, radius=0.14), Dot(v3, color=GOLD, radius=0.14))
        # Bar chart of (1, 6, 11, 6)
        bars = VGroup()
        vals = [1, 6, 11, 6]
        for i, v in enumerate(vals):
            h = v * 0.14
            r = Rectangle(width=0.38, height=h, fill_color=ACCENT if i != 2 else GOLD, fill_opacity=0.85, stroke_width=0)
            r.move_to([0.7 + i * 0.55, 1.45 + h / 2, 0])
            bars.add(r)
        self.play(FadeIn(tri, bars), run_time=1.0)
        c1 = card(6.3, 1.7, ACCENT).move_to([0, -0.2, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.7, GOLD).move_to([0, -2.3, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.8)
        self.play(FadeIn(c2, t2), run_time=0.8)
        end_vo("s1", t0, 8.5)
        self.play(FadeOut(hdr, tri, bars, c1, t1, c2, t2), run_time=0.5)

        # s2
        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.0, MINT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, MINT), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, VIOLET).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, FG), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 8.5)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        # s3
        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, RED).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 24, RED), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, GOLD).move_to([0, -0.9, 0])
        t2 = fit(T(tr(TX["s3_c2"]), 23, GOLD), 5.9).move_to(c2)
        bot = line(TX["s3_bot"], 22, MINT, -3.2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        self.play(FadeIn(bot), run_time=0.7)
        end_vo("s3", t0, 8.5)

        if tl_path:
            json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
