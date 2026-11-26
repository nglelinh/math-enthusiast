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
    "s1_tag": {"vi": "HỆ ĐỘNG LỰC & SỐ MŨ LYAPUNOV", "en": "DYNAMICS"},
    "s1_t": {"vi": "Hỗn loạn có quy luật trong ánh xạ 1 chiều", "en": "1D Maps"},
    "s1_c1": {"vi": "Ánh xạ đơn đỉnh f_a(x) = 1 − ax²:\nhai trạng thái: Đều đặn (chu kỳ) hay Ngẫu nhiên (ergodic)?", "en": "Regular vs Stochastic"},
    "s1_c2": {"vi": "Định lý Avila–Lyubich–de Melo (2003):\nHầu hết mọi tham số a đều rơi vào đúng 1 trong 2 loại!", "en": "Dichotomy"},
    "s2_tag": {"vi": "KÍNH HIỂN VI TÁI CHUẨN HÓA", "en": "RENORMALIZATION"},
    "s2_t": {"vi": "Phóng đại & Kéo giãn để thấy tính phổ quát", "en": "Renormalization"},
    "s2_c1": {"vi": "Phép tái chuẩn hóa R(f): cắt miền nhỏ quanh 0,\nlặp k lần rồi phóng đại kích thước về [-1, 1].", "en": "Zoom & rescale"},
    "s2_c2": {"vi": "Mọi họ ánh xạ cùng hội tụ về một điểm bất động\nphổ quát — giải thích hằng số Feigenbaum!", "en": "Feigenbaum universality"},
    "s3_tag": {"vi": "FIELDS MEDAL 2014", "en": "FIELDS 2014"},
    "s3_t": {"vi": "Artur Avila — Bức tranh toàn cảnh Động lực", "en": "Artur Avila"},
    "s3_c1": {"vi": "Kết nối động lực 1 chiều, bề mặt phẳng\nvà phổ toán tử Schrödinger giả tuần hoàn!", "en": "Grand panorama"},
}

class AvilaRenormalization(Scene):
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
        ax, _ = mkaxes([-1.1, 1.1, 0.5], [-1.1, 1.1, 0.5], 4.2, 2.2, [0, 2.1, 0])
        par = ax.plot(lambda x: 1 - 1.7 * x * x, x_range=[-1, 1], color=GOLD, stroke_width=4)
        self.play(Create(ax), Create(par), run_time=1.1)
        c1 = card(6.3, 1.8, ACCENT).move_to([0, -0.3, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.8, MINT).move_to([0, -2.4, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, ax, par, c1, t1, c2, t2), run_time=0.5)

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
        c1 = card(6.3, 2.2, MINT).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 24, MINT), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
