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
    "s1_tag": {"vi": "VẬT LÝ THỐNG KÊ TRÊN LƯỚI", "en": "STATISTICAL MECHANICS"},
    "s1_t": {"vi": "Chuyển pha & Bậc thang tới hạn", "en": "Phase Transitions"},
    "s1_c1": {"vi": "Trên lưới ℤ^d, khi nhiệt độ T tiến tới ngưỡng T_c:\nđộ từ hóa hay xác suất thấm thay đổi đột ngột!", "en": "Sharp transition at T_c"},
    "s1_c2": {"vi": "Chiều 2 có SLE & giải tích phức; nhưng chiều 3 & 4\nkhông có bất biến bảo giác → kẹt suốt hàng thập kỷ!", "en": "3D and 4D lacked conformal invariance"},
    "s2_tag": {"vi": "ĐỘT PHÁ KHÔNG CẦN CÔNG THỨC", "en": "NO EXACT FORMULA NEEDED"},
    "s2_t": {"vi": "Hugo Duminil-Copin (Fields 2022)", "en": "Hugo Duminil-Copin"},
    "s2_c1": {"vi": "Chứng minh tính liên tục của chuyển pha trên\nmô hình Ising 3D và mô hình Potts q-trạng thái!", "en": "Continuity in 3D Ising"},
    "s2_c2": {"vi": "Dùng bất đẳng thức vi phân OSSS & biểu diễn\ndòng ngẫu nhiên thay cho công thức nghiệm đúng!", "en": "OSSS & random currents"},
    "s3_tag": {"vi": "CHIỀU TỚI HẠN 4 CỦA φ⁴", "en": "TRIVIALITY IN 4D"},
    "s3_t": {"vi": "Aizenman–Duminil-Copin (2021)", "en": "Aizenman–Duminil-Copin"},
    "s3_c1": {"vi": "Chứng minh tính tầm thường (triviality) của\nmô hình Ising 4D & trường lượng tử φ⁴₄!", "en": "4D Ising triviality"},
}

class DuminilIsing(Scene):
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
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, RED).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, RED), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, MINT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, MINT), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, GOLD), 5.9).move_to(c2)
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
