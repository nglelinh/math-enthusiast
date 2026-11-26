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
    t2 = fit(T(title, 32, WHITE), 7.8)
    return VGroup(t1, t2).arrange(DOWN, buff=0.14).move_to([0, 6.2, 0])

def setup_vo(scene):
    vo_durs = json.load(open(os.environ["VO_DUR_JSON"])) if os.environ.get("VO_DUR_JSON") else {}
    tl_path = os.environ.get("VO_TIMELINE_JSON")
    timeline = []
    def end_vo(sid, t0, fb):
        dur = vo_durs.get(sid)
        if dur is not None:
            rem = dur - (scene.time - t0) + 0.45
            if rem > 0.05:
                scene.wait(rem)
        else:
            scene.wait(fb)
    def save_tl():
        if tl_path:
            with open(tl_path, "w") as f:
                json.dump({"timeline": timeline, "total": float(scene.time)}, f)
    return timeline, end_vo, save_tl

class McMullenDynamics(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: f_c(z) = z^2 + c at c = 0, -2, -1
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("ĐỘNG LỰC CHỈNH HÌNH", "Lặp f_c(z) = z² + c: Fatou & Julia")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        rows = [
            ("c = 0", "Tập Julia: đường tròn |z| = 1", "Đĩa trong hút về 0", SKY),
            ("c = -2", "Tập Julia: đoạn thực [-2, 2]", "Hỗn loạn hoàn toàn", PINK),
            ("c = -1", "Chu kỳ hút bậc 2: 0 ↔ -1", "Hình thỏ / basilica", MINT),
        ]
        cards = VGroup()
        for c_txt, j_txt, d_txt, col in rows:
            box = card(7.6, 2.2, col)
            t_c = T(c_txt, 28, col)
            t_j = fit(T(j_txt, 24, WHITE), 6.8)
            t_d = fit(T(d_txt, 22, DIM), 6.8)
            inner = VGroup(t_c, t_j, t_d).arrange(DOWN, buff=0.14).move_to(box)
            cards.add(VGroup(box, inner))
        cards.arrange(DOWN, buff=0.35).move_to([0, 0.4, 0])

        cap1 = fit(T("Ba giá trị c cho thấy ranh giới ổn định (Fatou) & hỗn loạn (Julia)", 24, SUN), 7.8).move_to([0, -4.6, 0])
        self.play(LaggedStart(*[FadeIn(x, shift=UP*0.2) for x in cards], lag_ratio=0.25), run_time=1.8)
        self.play(FadeIn(cap1), run_time=0.6)
        end_vo("s1", t0, 9.0)

        # s2: Renormalization & tiny Mandelbrot copies
        self.play(FadeOut(hdr), FadeOut(cards), FadeOut(cap1), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("TÁI CHUẨN HÓA (RENORMALIZATION)", "Vì sao tập Mandelbrot tự lặp vô tận?")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        big_c = Circle(radius=2.2, color=SKY, stroke_width=4).move_to([0, 1.5, 0])
        small_c = Circle(radius=0.75, color=SUN, stroke_width=4).move_to([0, 1.5, 0])
        arr = Arrow([0.8, 1.5, 0], [2.2, 1.5, 0], color=MINT, stroke_width=4)
        lbl_m = fit(T("Phóng đại miền U → V bởi f^n", 24, WHITE), 7.4).move_to([0, -1.2, 0])
        box2 = card(7.6, 2.8, SUN).move_to([0, -3.3, 0])
        b2_txt = VGroup(
            fit(T("Ánh xạ tựa-bậc-hai (Douady–Hubbard)", 25, SUN), 7.0),
            fit(T("f^n trên U hành xử như một bản sao z² + c'", 23, WHITE), 7.0),
            fit(T("→ Sinh vô số bản sao Mandelbrot tí hon!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box2)

        self.play(Create(big_c), Create(small_c), GrowArrow(arr), run_time=1.2)
        self.play(FadeIn(lbl_m), FadeIn(box2), FadeIn(b2_txt), run_time=0.9)
        end_vo("s2", t0, 9.0)

        # s3: Sullivan Dictionary (2D <-> 3D)
        self.play(FadeOut(hdr2), FadeOut(big_c), FadeOut(small_c), FadeOut(arr), FadeOut(lbl_m), FadeOut(box2), FadeOut(b2_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s3", t0))
        hdr3 = make_scene_header("TỪ ĐIỂN SULLIVAN", "Cầu nối Động lực 2D ↔ Đa tạp Hyperbolic 3D")
        self.play(FadeIn(hdr3, shift=DOWN*0.2), run_time=0.6)

        c_left = card(3.5, 4.6, SKY).move_to([-2.0, 0.6, 0])
        c_right = card(3.5, 4.6, PINK).move_to([2.0, 0.6, 0])
        l_txt = VGroup(
            T("2D Phức", 26, SKY),
            T("Hàm hữu tỷ f(z)", 21, WHITE),
            T("Tập Julia J(f)", 21, WHITE),
            T("Không có dòng bất biến", 20, MINT),
        ).arrange(DOWN, buff=0.35).move_to(c_left)
        r_txt = VGroup(
            T("3D Hyperbolic", 26, PINK),
            T("Nhóm Klein Γ", 21, WHITE),
            T("Tập giới hạn Λ(Γ)", 21, WHITE),
            T("Tính cứng Mostow", 20, MINT),
        ).arrange(DOWN, buff=0.35).move_to(c_right)
        mid_arr = DoubleArrow([-0.2, 0.6, 0], [0.2, 0.6, 0], color=SUN, stroke_width=4)

        foot = fit(T("McMullen (Fields 1998): dùng tái chuẩn hóa chứng minh tính cứng 2D & 3D", 23, SUN), 7.8).move_to([0, -3.5, 0])
        self.play(FadeIn(c_left), FadeIn(c_right), FadeIn(l_txt), FadeIn(r_txt), GrowArrow(mid_arr), run_time=1.3)
        self.play(FadeIn(foot), run_time=0.7)
        end_vo("s3", t0, 9.0)
        save_tl()
