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
    "s1_tag": {"vi": "ĐỘ CỨNG ĐỘ ĐO", "en": "MEASURE RIGIDITY"},
    "s1_t": {"vi": "×2 vs ×3 trên vòng tròn & Ma trận 3×3", "en": "×2, ×3 & 3×3 Lattices"},
    "s1_c1": {"vi": "Phép ×2 đơn lẻ có vô vàn độ đo bất biến fractal;\nnhưng cùng lúc bất biến dưới ×2 VÀ ×3 (Furstenberg)?", "en": "x2 and x3 invariance"},
    "s1_c2": {"vi": "Tác động chéo bậc cao (rank ≥ 2) trên SL(3,ℝ)/SL(3,ℤ):\nEinsiedler–Katok–Lindenstrauss khóa chặt độ đo bất biến!", "en": "Higher-rank rigidity"},
    "s2_tag": {"vi": "GIẢ THUYẾT LITTLEWOOD", "en": "LITTLEWOOD CONJECTURE"},
    "s2_t": {"vi": "liminf n · ‖nα‖ · ‖nβ‖ = 0", "en": "Littlewood Conjecture"},
    "s2_c1": {"vi": "Từ độ cứng độ đo trên SL(3,ℝ)/SL(3,ℤ),\nEinsiedler–Katok–Lindenstrauss (2006) chứng minh:", "en": "EKL 2006 theorem"},
    "s2_c2": {"vi": "Tập ngoại lệ của giả thuyết Littlewood có\nCHIỀU HAUSDORFF BẰNG KHÔNG!", "en": "Hausdorff dimension zero"},
    "s3_tag": {"vi": "FIELDS MEDAL 2010", "en": "FIELDS 2010"},
    "s3_t": {"vi": "Elon Lindenstrauss — Cứng hóa Ergodic", "en": "Elon Lindenstrauss"},
    "s3_c1": {"vi": "Dùng entropy dương & cấu trúc đại số của nhóm Lie\nđể phân loại toàn bộ độ đo bất biến chéo!", "en": "Positive entropy rigidity"},
}

class LindenstraussRigidity(Scene):
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
        c2 = card(6.3, 1.9, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 22, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 24, MINT), 5.9).move_to(c2)
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
