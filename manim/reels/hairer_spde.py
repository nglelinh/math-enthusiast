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
    "s1_tag": {"vi": "SPDE KỲ DỊ", "en": "SINGULAR SPDEs"},
    "s1_t": {"vi": "Tại sao δ₀² và (∂_x h)² bùng nổ?", "en": "Why Singular SPDEs Explode"},
    "s1_c1": {"vi": "Nhiễu trắng ξ quá gồ ghề (bậc chính quy −3/2 − ε):\nnghiệm u chỉ là phân phối, KHÔNG nhân được với nhau!", "en": "White noise is rough"},
    "s1_c2": {"vi": "Phương trình KPZ: ∂_t h = ∂_x² h + (∂_x h)² + ξ\n(∂_x h)² vô nghĩa theo giải tích cổ điển!", "en": "KPZ equation"},
    "s2_tag": {"vi": "CẤU TRÚC CHÍNH QUY", "en": "REGULARITY STRUCTURES"},
    "s2_t": {"vi": "Martin Hairer (Fields 2014): Đa thức mở rộng", "en": "Martin Hairer"},
    "s2_c1": {"vi": "Thay đa thức Taylor {1, x, x²,…} bằng tập ký hiệu\ncây ngẫu nhiên (model) Π_x τ mang sẵn dạng nhiễu ξ!", "en": "Trees as generalized polynomials"},
    "s2_c2": {"vi": "Định lý Tái dựng (Reconstruction): dán các xấp xỉ\nđịa phương thành nghiệm toàn cục duy nhất!", "en": "Reconstruction theorem"},
    "s3_tag": {"vi": "ĐÁNH GIÁ BẬC & Φ⁴₃", "en": "SUBCRITICALITY"},
    "s3_t": {"vi": "Tái chuẩn hóa đại số cho Φ⁴₃", "en": "Renormalization"},
    "s3_c1": {"vi": "Nhóm tái chuẩn hóa tác động lên cây trừ đi hằng số\nvô hạn C_ε → giới hạn ε → 0 hoàn toàn hữu hạn!", "en": "Finite limit"},
}

class HairerSPDE(Scene):
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
        c1 = card(6.3, 1.9, RED).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 22, RED), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, ACCENT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, FG), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, GOLD).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, GOLD), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, VIOLET).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, FG), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
