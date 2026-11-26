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
    "s1_tag": {"vi": "GIẢ THUYẾT BAB", "en": "THE BAB CONJECTURE"},
    "s1_t": {"vi": "Vì sao Tính bị chặn lại khó?", "en": "Why Is Boundedness So Hard?"},
    "s1_c1": {"vi": "Vô hạn hình dạng Fano ở chiều d bất kỳ:\nliệu có thể xếp vào hữu hạn họ đại số?", "en": "Infinitely many Fano shapes in dim d:\ncan finitely many families hold them all?"},
    "s1_c2": {"vi": "Điều kiện ε-lc: chặn mức độ kỳ dị\n(không cho góc nhọn quá gắt ε → 0).", "en": "ε-lc condition: bound singularity severity\n(forbid arbitrarily sharp cusps ε → 0)."},
    "s2_tag": {"vi": "CỖ MÁY CHỨNG MINH", "en": "THE PROOF ENGINE"},
    "s2_t": {"vi": "Chặn thể tích & Bù n-bị chặn", "en": "Volume Bounds & n-Complements"},
    "s2_b1": {"vi": "Bước 1: Chứng minh thể tích (−K_X)^d ≤ M\nbị chặn trên theo d và ε.", "en": "Step 1: Bound anti-canonical volume\n(−K_X)^d ≤ M(d, ε)."},
    "s2_b2": {"vi": "Bước 2: Dựng phần bù n-bị chặn (n-complement)\nbằng quy nạp MMP theo số chiều.", "en": "Step 2: Build bounded n-complements\nvia MMP induction on dimension."},
    "s3_tag": {"vi": "TỪ ĐỊA PHƯƠNG ĐẾN TOÀN CỤC", "en": "LOCAL TO GLOBAL FINITENESS"},
    "s3_t": {"vi": "ACC cho ngưỡng chính tắc log", "en": "ACC for Log Canonical Thresholds"},
    "s3_c1": {"vi": "HMX (2014): Tập các ngưỡng lct thỏa ACC\n(không có dãy tăng nghiêm ngặt vô hạn).", "en": "HMX (2014): Log canonical thresholds\nsatisfy ACC (no infinite ascending chain)."},
    "s3_c2": {"vi": "Birkar (2016) khóa chặt BAB:\nmở đường xây không gian mô-đun K-moduli!", "en": "Birkar (2016) seals BAB:\nunlocking K-moduli spaces of Fano varieties!"},
    "s3_bot": {"vi": "Huy chương Fields 2018 · Caucher Birkar", "en": "2018 Fields Medal · Caucher Birkar"},
}

class BirkarBAB(Scene):
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
        c1 = card(6.3, 2.0, ACCENT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 24, FG), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, RED).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 24, RED), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 8.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        # s2
        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        b1 = card(6.3, 2.0, MINT).move_to([0, 1.8, 0])
        k1 = fit(T(tr(TX["s2_b1"]), 24, MINT), 5.9).move_to(b1)
        arr = Arrow([0, 0.7, 0], [0, -0.1, 0], color=GOLD, buff=0.05)
        b2 = card(6.3, 2.0, GOLD).move_to([0, -1.2, 0])
        k2 = fit(T(tr(TX["s2_b2"]), 24, GOLD), 5.9).move_to(b2)
        self.play(FadeIn(b1, k1), run_time=0.9)
        self.play(GrowArrow(arr), FadeIn(b2, k2), run_time=1.0)
        end_vo("s2", t0, 8.5)
        self.play(FadeOut(hdr, b1, k1, arr, b2, k2), run_time=0.5)

        # s3
        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.0, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, GOLD).move_to([0, -0.9, 0])
        t2 = fit(T(tr(TX["s3_c2"]), 23, GOLD), 5.9).move_to(c2)
        bot = line(TX["s3_bot"], 22, MINT, -3.2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        self.play(FadeIn(bot), run_time=0.7)
        end_vo("s3", t0, 8.5)

        if tl_path:
            json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
