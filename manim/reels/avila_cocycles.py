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
    "s1_tag": {"vi": "COCYCLE MA TRẬN SL(2, ℝ)", "en": "SL(2,R) COCYCLES"},
    "s1_t": {"vi": "Phổ Cantor & Bài toán Mười ly Martini", "en": "Ten Martini Problem"},
    "s1_c1": {"vi": "Toán tử Almost Mathieu: (H_λ,α,θ u)_n =\nu_{n+1} + u_{n-1} + 2λ cos(2π(nα+θ)) u_n", "en": "Almost Mathieu"},
    "s1_c2": {"vi": "Avila–Jitomirskaya (2009): Với mọi α vô tỉ & λ ≠ 0,\nphổ của H luôn là TẬP CANTOR (đúng 10 ly Martini)!", "en": "Cantor spectrum"},
    "s2_tag": {"vi": "LÝ THUYẾT TOÀN CỤC CỦA AVILA", "en": "GLOBAL THEORY"},
    "s2_t": {"vi": "Lý thuyết một tần số & Tính trộn yếu", "en": "One-Frequency Theory"},
    "s2_c1": {"vi": "Phân tích phức hóa số mũ Lyapunov L(E + iε):\nhàm lồi từng khúc theo ε với hệ số góc NGUYÊN!", "en": "Quantized acceleration"},
    "s2_c2": {"vi": "Avila–Forni (2007): Hầu hết trao đổi khoảng\n(không phải xoay thuần túy) đều TRỘN YẾU!", "en": "Weak mixing"},
    "s3_tag": {"vi": "CÔNG TRÌNH ĐỒNG TÁC GIẢ", "en": "LANDMARKS"},
    "s3_t": {"vi": "Nối tiếp với Mirzakhani & Eskin", "en": "Moduli spaces"},
    "s3_c1": {"vi": "Cùng Viana chứng minh giả thuyết Zorich–Kontsevich\nvề tính đơn giản của phổ Lyapunov trên không gian mô-đun!", "en": "Simplicity of Lyapunov spectrum"},
}

class AvilaCocycles(Scene):
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
        c2 = card(6.3, 2.0, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, MINT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, MINT), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, VIOLET).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, FG), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, GOLD).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, GOLD), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
