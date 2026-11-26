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

class ZelmanovJordan(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: 4 steps from Hall-Higman & Kostrikin to Zelmanov
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("CHỨNG MINH ZELMANOV (1990–1991)", "Từ Đại số Lie & Đại số Jordan về Nhóm hữu hạn")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        steps = [
            ("1. Hall–Higman (1956)", "Rút gọn mọi số mũ n về lũy thừa nguyên tố p^k", SKY),
            ("2. Kostrikin (1959)", "Giải xong trường hợp số mũ nguyên tố n = p", MINT),
            ("3. Đột phá Zelmanov (n = p^k)", "Dùng Đại số Jordan giải bậc lũy thừa p^k (k ≥ 2)", SUN),
            ("4. Dịch ngược về Nhóm", "Đại số Lie lũy linh địa phương ⇒ |B₀(d, n)| bị chặn!", PINK),
        ]
        cards = VGroup()
        for t1, t2, col in steps:
            b = card(7.6, 1.75, col)
            g = VGroup(fit(T(t1, 24, col), 7.0), fit(T(t2, 21, WHITE), 7.0)).arrange(DOWN, buff=0.1).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.25).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.18) for c in cards], lag_ratio=0.22), run_time=1.9)
        end_vo("s1", t0, 11.0)

        # s2: Why it matters
        self.play(FadeOut(hdr), FadeOut(cards), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("FIELDS MEDAL 1994", "Sức mạnh của cú chuyển ngôn ngữ")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box = card(7.6, 3.6, SUN).move_to([0, 0.2, 0])
        b_txt = VGroup(
            fit(T("Nhóm hữu hạn có số mũ p^k  →  Đại số Lie tuyến tính", 22, SKY), 7.0),
            fit(T("Cấu trúc đại số Lie  →  Nhúng vào Đại số Jordan", 22, MINT), 7.0),
            fit(T("Kỹ thuật 'bánh sandwich' của Zelmanov khóa chặt", 22, WHITE), 7.0),
            fit(T("mọi chuỗi móc Lie → Khép lại bài toán gần 60 năm!", 23, SUN), 7.0),
        ).arrange(DOWN, buff=0.28).move_to(box)

        self.play(FadeIn(box), FadeIn(b_txt), run_time=1.0)
        end_vo("s2", t0, 9.0)
        save_tl()
