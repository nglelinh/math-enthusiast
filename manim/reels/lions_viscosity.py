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
    "s1_tag": {"vi": "NGHIỆM NHỚT (VISCOSITY)", "en": "VISCOSITY SOLUTIONS"},
    "s1_t": {"vi": "Nghiệm yếu KHÔNG cần tích phân từng phần!", "en": "Weak Without Integration by Parts"},
    "s1_c1": {"vi": "Phương trình eikonal |u'(x)| − 1 = 0 trên [-1, 1], u(±1) = 0\ncó vô số hàm răng cưa Lipschitz thỏa hầu khắp nơi!", "en": "Infinitely many Lipschitz solutions"},
    "s1_c2": {"vi": "Crandall–Lions (1983): Dùng nguyên lý cực đại & hàm thử\ntrơn φ chạm từ trên/dưới → chọn ra ĐÚNG 1 nghiệm vật lý u(x)=1−|x|!", "en": "Unique physical solution"},
    "s2_tag": {"vi": "PDE CẤP HAI PHI TUYẾN", "en": "SECOND-ORDER PDEs"},
    "s2_t": {"vi": "Định lý so sánh Ishii–Lions & Bellman", "en": "Ishii's Lemma"},
    "s2_c1": {"vi": "Mở rộng khái niệm siêu vi phân / hạ vi phân bậc hai\ncho các phương trình Hamilton–Jacobi–Bellman!", "en": "Subjets and superjets"},
    "s2_c2": {"vi": "Bổ đề Ishii (1989) bảo đảm tính duy nhất toàn cục\ncủa nghiệm nhớt cho mọi PDE elliptic suy biến!", "en": "Global uniqueness"},
    "s3_tag": {"vi": "FIELDS MEDAL 1994", "en": "FIELDS 1994"},
    "s3_t": {"vi": "Pierre-Louis Lions — Giải tích Phi tuyến", "en": "Pierre-Louis Lions"},
    "s3_c1": {"vi": "Từ điều khiển tối ưu, tài chính định lượng đến đồ họa\nmáy tính (Level Set): nghiệm nhớt là ngôn ngữ chuẩn!", "en": "Control, finance & level sets"},
}

class LionsViscosity(Scene):
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
        ax, _ = mkaxes([-1.2, 1.2, 1], [0, 1.2, 0.5], 4.4, 2.0, [0, 2.0, 0])
        tent = VGroup(Line(ax.c2p(-1, 0), ax.c2p(0, 1), color=GOLD, stroke_width=4),
                      Line(ax.c2p(0, 1), ax.c2p(1, 0), color=GOLD, stroke_width=4))
        self.play(Create(ax), Create(tent), run_time=1.1)
        c1 = card(6.3, 1.8, ACCENT).move_to([0, -0.3, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 22, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.8, MINT).move_to([0, -2.4, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 21, MINT), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, ax, tent, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 1.9, VIOLET).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 22, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.9, GOLD).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, GOLD), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, MINT).move_to([0, 0.5, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, MINT), 5.9).move_to(c1)
        self.play(FadeIn(c1, t1), run_time=1.0)
        end_vo("s3", t0, 6.5)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
