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
    "s1_tag": {"vi": "ĐA THỨC LORENTZ", "en": "LORENTZIAN POLYNOMIALS"},
    "s1_t": {"vi": "Brändén–Huh (2020): Một dấu Hessian", "en": "Brändén–Huh (2020): One Hessian Sign"},
    "s1_c1": {"vi": "Ma trận Hessian ∇²f có đúng MỘT trị riêng dương:\nchữ ký Lorentz (+, −, −, …, −)!", "en": "Hessian ∇²f has AT MOST ONE positive\neigenvalue: Lorentz signature (+, −, −, …, −)!"},
    "s1_c2": {"vi": "Chứng minh giả thuyết Mason siêu mạnh\nvà tính lõm loga chỉ bằng giải tích sơ cấp!", "en": "Proves the ultra-strong Mason conjecture\nand log-concavity via pure calculus!"},
    "s2_tag": {"vi": "NĂM CÂY CẦU LỚN", "en": "FIVE MAJOR BRIDGES"},
    "s2_t": {"vi": "Bản đồ Tổ hợp – Hình học Hiện đại", "en": "Map of Modern Combinatorics & Geometry"},
    "s2_b1": {"vi": "1. Tổ hợp cộng tính (Cấu trúc ↔ Ngẫu nhiên)\n2. Hình học liên thuộc (Điểm, đường, ống)", "en": "1. Additive combinatorics (Structure ↔ Random)\n2. Incidence geometry (Points, lines, tubes)"},
    "s2_b2": {"vi": "3. Đồ thị mở rộng & Khe phổ\n4. Phương pháp đa thức (Dvir, Guth–Katz)\n5. Bổ đề chính quy Szemerédi & Graphon", "en": "3. Expander graphs & spectral gaps\n4. Polynomial method (Dvir, Guth–Katz)\n5. Szemerédi regularity & graphons"},
    "s3_tag": {"vi": "TƯ DUY THỐNG NHẤT", "en": "UNIFYING INSIGHT"},
    "s3_t": {"vi": "Đếm rời rạc nhờ cấu trúc liên tục", "en": "Discrete Counting via Smooth Structure"},
    "s3_c1": {"vi": "Khi phép đếm thuần túy chạm tường:\nhãy nhìn nó như độ cong, phổ, hay dạng toàn phương!", "en": "When pure counting hits a wall:\nview it as curvature, spectrum, or quadratic forms!"},
    "s3_bot": {"vi": "Nối liền Green–Tao, Viazovska, Wang & Huh", "en": "Linking Green–Tao, Viazovska, Wang & Huh"},
}

class HuhLorentzian(Scene):
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
        c1 = card(6.3, 2.0, GOLD).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, GOLD), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 8.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        # s2
        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        b1 = card(6.3, 2.0, ACCENT).move_to([0, 1.8, 0])
        k1 = fit(T(tr(TX["s2_b1"]), 23, FG), 5.9).move_to(b1)
        b2 = card(6.3, 2.4, VIOLET).move_to([0, -1.2, 0])
        k2 = fit(T(tr(TX["s2_b2"]), 23, FG), 5.9).move_to(b2)
        self.play(FadeIn(b1, k1), run_time=0.9)
        self.play(FadeIn(b2, k2), run_time=1.0)
        end_vo("s2", t0, 8.5)
        self.play(FadeOut(hdr, b1, k1, b2, k2), run_time=0.5)

        # s3
        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.3, MINT).move_to([0, 0.8, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 24, MINT), 5.9).move_to(c1)
        bot = line(TX["s3_bot"], 22, GOLD, -2.0)
        self.play(FadeIn(c1, t1), run_time=1.0)
        self.play(FadeIn(bot), run_time=0.8)
        end_vo("s3", t0, 8.0)

        if tl_path:
            json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
