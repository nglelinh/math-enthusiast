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
    "s1_tag": {"vi": "LƯỢNG TỬ HÓA BIẾN DẠNG", "en": "DEFORMATION QUANTIZATION"},
    "s1_t": {"vi": "Tích sao Moyal trên Đa tạp Poisson", "en": "Moyal Star Product"},
    "s1_c1": {"vi": "Trong cơ học lượng tử, phép nhân giao hoán f·g biến\nthành tích sao không giao hoán: f ★ g = f·g + iℏ/2 {f, g} + …", "en": "f * g = fg + (ih/2){f,g} + ..."},
    "s1_c2": {"vi": "Câu hỏi mở suốt 20 năm: Mọi đa tạp Poisson\nđều lượng tử hóa biến dạng được không?", "en": "Exists for all Poisson manifolds?"},
    "s2_tag": {"vi": "ĐỊNH LÝ HÌNH THỨC (1997)", "en": "FORMALITY THEOREM"},
    "s2_t": {"vi": "Giải quyết trọn vẹn qua Giản đồ Nửa mặt phẳng", "en": "Feynman Diagrams on H_+"},
    "s2_c1": {"vi": "Kontsevich chứng minh đại số Lie vi phân phân bậc\nT_poly và D_poly đồng cấu L_∞ (hình thức) với nhau!", "en": "L_infty quasi-isomorphism"},
    "s2_c2": {"vi": "Các hệ số của tích sao ★ viết tường minh bằng\ntích phân trọng số trên đĩa nửa mặt phẳng trên!", "en": "Explicit diagram weights"},
    "s3_tag": {"vi": "ĐỐI XỨNG GƯƠNG & MOTIVIC", "en": "HMS & BEYOND"},
    "s3_t": {"vi": "Những di sản sau Fields 1998", "en": "Beyond 1998"},
    "s3_c1": {"vi": "Đối xứng gương đồng điều (1994), chu kỳ motivic\nvà giải tích phục sinh (resurgence) vẫn định hình toán học!", "en": "HMS & motivic periods"},
}

class KontsevichFormality(Scene):
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
        c2 = card(6.3, 1.9, RED).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, RED), 5.9).move_to(c2)
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
