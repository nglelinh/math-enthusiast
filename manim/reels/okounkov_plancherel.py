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

class OkounkovPlancherel(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Plancherel measure for S_3
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("ĐỘ ĐO PLANCHEREL CHO S₃", "Mỗi phân hoạch λ của n có xác suất (dim V_λ)² / n!")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        rows = [
            ("λ = (3)", "dim = 1", "P = 1/6", SKY),
            ("λ = (2, 1)", "dim = 2", "P = 4/6 = 2/3", SUN),
            ("λ = (1, 1, 1)", "dim = 1", "P = 1/6", PINK),
        ]
        cards = VGroup()
        for l_t, d_t, p_t, col in rows:
            b = card(7.6, 1.85, col)
            g = VGroup(fit(T(l_t, 26, col), 2.5), fit(T(d_t, 24, WHITE), 2.0), fit(T(p_t, 24, MINT), 2.4)).arrange(RIGHT, buff=0.4).move_to(b)
            cards.add(VGroup(b, g))
        cards.arrange(DOWN, buff=0.3).move_to([0, 1.0, 0])

        sum_t = fit(T("Tổng xác suất: 1/6 + 4/6 + 1/6 = 1  (RSK ↔ hoán vị ngẫu nhiên)", 23, SUN), 7.8).move_to([0, -2.5, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in cards], lag_ratio=0.25), run_time=1.6)
        self.play(FadeIn(sum_t), run_time=0.6)
        end_vo("s1", t0, 9.5)

        # s2: Limit shape & Tracy-Widom
        self.play(FadeOut(hdr), FadeOut(cards), FadeOut(sum_t), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("KHI n → ∞: HÌNH DẠNG GIỚI HẠN", "Từ bài xáo trộn tới Ma trận Ngẫu nhiên")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        ax, lab = mkaxes([-2.2, 2.2, 1], [0, 2.5, 1], 6.4, 3.4, [0, 1.4, 0], xt=[-2, 0, 2], yt=[(2, "2")])
        curve = ax.plot(lambda x: abs(x) if abs(x) >= 2 else (2/np.pi)*(x*np.arcsin(x/2) + np.sqrt(max(0, 4 - x*x))),
                        x_range=[-2.15, 2.15], color=SUN, stroke_width=5)
        lbl_vk = fit(T("Đường cong Vershik–Kerov & Logan–Shepp", 23, SUN), 7.4).move_to([0, -0.7, 0])

        box_tw = card(7.6, 2.8, MINT).move_to([0, -2.8, 0])
        bt_txt = VGroup(
            fit(T("Độ dài hàng đầu λ₁ = dãy con tăng dài nhất", 24, WHITE), 7.0),
            fit(T("Dao động quanh 2√n tuân theo luật Tracy–Widom!", 24, MINT), 7.0),
            fit(T("Okounkov (2000) chứng minh qua mặt ngẫu nhiên.", 22, DIM), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box_tw)

        self.play(Create(ax), FadeIn(lab), Create(curve), run_time=1.5)
        self.play(FadeIn(lbl_vk), FadeIn(box_tw), FadeIn(bt_txt), run_time=0.9)
        end_vo("s2", t0, 10.0)
        save_tl()
