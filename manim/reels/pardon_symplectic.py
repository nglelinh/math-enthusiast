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
    "s1_tag": {"vi": "HÌNH HỌC SYMPLECTIC", "en": "SYMPLECTIC GEOMETRY"},
    "s1_t": {"vi": "Không gian pha & Dạng ω = dp ∧ dq", "en": "Phase Space & ω = dp ∧ dq"},
    "s1_c1": {"vi": "Định lý Liouville: Dòng Hamilton bảo toàn\nDIỆN TÍCH pha ω, không bảo toàn hình dạng!", "en": "Liouville's Theorem"},
    "s1_c2": {"vi": "Định lý Lạc đà Gromov (1985):\nKhông thể nhét cầu B⁴(R) vào trụ Z⁴(r) nếu R > r!", "en": "Gromov's Nonsqueezing"},
    "s2_tag": {"vi": "ĐƯỜNG CONG GIẢ CHỈNH HÌNH", "en": "PSEUDOHOLOMORPHIC CURVES"},
    "s2_t": {"vi": "Bài toán Không gian Mô-đun suy biến", "en": "Moduli Space Degeneration"},
    "s2_c1": {"vi": "Đếm đường cong J-chỉnh hình (Gromov–Witten\n& Floer) xác định bất biến symplectic.", "en": "Counting J-curves"},
    "s2_c2": {"vi": "Vấn đề lớn: Không gian mô-đun bị suy biến,\ncó kỳ dị và chiều không đồng đều!", "en": "Moduli spaces break"},
    "s3_tag": {"vi": "CHU TRÌNH CƠ BẢN ẢO", "en": "VIRTUAL FUNDAMENTAL CYCLES"},
    "s3_t": {"vi": "Đột phá của John Pardon (Fields 2026)", "en": "John Pardon (Fields 2026)"},
    "s3_c1": {"vi": "Thay vì làm trơn toàn cục không gian mô-đun,\nPardon dùng phân rã xấp xỉ Kuranishi + hàm ý ngầm.", "en": "Implicit atlases"},
    "s3_bot": {"vi": "Đặt nền móng vững chắc cho Phạm trù Fukaya", "en": "Foundation for Fukaya Categories"},
}

class PardonSymplectic(Scene):
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
        ball = Circle(radius=1.1, color=GOLD, fill_color=GOLD, fill_opacity=0.25, stroke_width=4).move_to([-1.6, 2.0, 0])
        cyl = RoundedRectangle(width=1.4, height=2.6, corner_radius=0.35, color=ACCENT, stroke_width=4).move_to([1.5, 2.0, 0])
        arr = Arrow([-0.3, 2.0, 0], [0.6, 2.0, 0], color=RED, buff=0.05)
        cross = T("✕", 38, RED).move_to([0.15, 2.55, 0])
        self.play(FadeIn(ball, cyl), GrowArrow(arr), FadeIn(cross), run_time=1.2)
        c1 = card(6.3, 1.8, ACCENT).move_to([0, -0.3, 0])
        t1 = fit(T(tr(TX["s1_c1"]), 23, FG), 5.9).move_to(c1)
        c2 = card(6.3, 1.8, RED).move_to([0, -2.4, 0])
        t2 = fit(T(tr(TX["s1_c2"]), 23, RED), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s1", t0, 7.0)
        self.play(FadeOut(hdr, ball, cyl, arr, cross, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s2", t0))
        hdr = make_scene_header(tr(TX["s2_tag"]), tr(TX["s2_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.0, MINT).move_to([0, 1.8, 0])
        t1 = fit(T(tr(TX["s2_c1"]), 23, MINT), 5.9).move_to(c1)
        c2 = card(6.3, 2.0, RED).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 23, RED), 5.9).move_to(c2)
        self.play(FadeIn(c1, t1), run_time=0.9)
        self.play(FadeIn(c2, t2), run_time=0.9)
        end_vo("s2", t0, 7.0)
        self.play(FadeOut(hdr, c1, t1, c2, t2), run_time=0.5)

        t0 = self.time; timeline.append(("s3", t0))
        hdr = make_scene_header(tr(TX["s3_tag"]), tr(TX["s3_t"]))
        self.play(FadeIn(hdr), run_time=0.7)
        c1 = card(6.3, 2.2, GOLD).move_to([0, 0.8, 0])
        t1 = fit(T(tr(TX["s3_c1"]), 23, GOLD), 5.9).move_to(c1)
        bot = line(TX["s3_bot"], 22, MINT, -2.0)
        self.play(FadeIn(c1, t1), run_time=1.0)
        self.play(FadeIn(bot), run_time=0.8)
        end_vo("s3", t0, 7.0)
        if tl_path: json.dump({"timeline": timeline, "total": self.time}, open(tl_path, "w"), indent=2)
