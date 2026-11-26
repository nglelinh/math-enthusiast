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

class OkounkovBridges(Scene):
    def construct(self):
        self.camera.background_color = BG
        timeline, end_vo, save_tl = setup_vo(self)

        # s1: Fock Space & Gromov-Witten on P^1
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_scene_header("KHÔNG GIAN FOCK & ĐẾM ĐƯỜNG CONG", "Cầu nối Okounkov–Pandharipande (Fields 2006)")
        self.play(FadeIn(hdr, shift=DOWN*0.2), run_time=0.6)

        box1 = card(7.6, 2.8, SKY).move_to([0, 2.2, 0])
        b1_txt = VGroup(
            fit(T("Biểu đồ Young λ  ↔  Trạng thái cơ sở |λ⟩ trong Fock", 24, SKY), 7.0),
            fit(T("Đếm đường cong (Gromov–Witten của P¹)", 24, WHITE), 7.0),
            fit(T("= Kỳ vọng chân không của toán tử Fock (hệ 2-Toda)!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box1)

        box2 = card(7.6, 2.8, SUN).move_to([0, -1.4, 0])
        b2_txt = VGroup(
            fit(T("Giả thuyết MNOP (Maulik–Nekrasov–Okounkov–Pandharipande)", 22, SUN), 7.0),
            fit(T("Đếm đường cong (GW)  ↔  Đếm bó lý tưởng (DT)", 24, WHITE), 7.0),
            fit(T("Liên kết qua mô hình tinh thể nóng chảy!", 23, PINK), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box2)

        self.play(FadeIn(box1), FadeIn(b1_txt), run_time=1.0)
        self.play(FadeIn(box2), FadeIn(b2_txt), run_time=1.0)
        end_vo("s1", t0, 10.0)

        # s2: Nekrasov-Okounkov & Schur process
        self.play(FadeOut(hdr), FadeOut(box1), FadeOut(b1_txt), FadeOut(box2), FadeOut(b2_txt), run_time=0.5)
        t0 = self.time; timeline.append(("s2", t0))
        hdr2 = make_scene_header("INSTANTON & QUÁ TRÌNH SCHUR", "Từ Vật lý N=2 tới Xác suất Định thức")
        self.play(FadeIn(hdr2, shift=DOWN*0.2), run_time=0.6)

        box3 = card(7.6, 3.0, PINK).move_to([0, 1.8, 0])
        b3_txt = VGroup(
            fit(T("Nekrasov–Okounkov (2006):", 25, PINK), 7.0),
            fit(T("Hàm phân hoạch instanton trong lý thuyết Seiberg–Witten", 22, WHITE), 7.0),
            fit(T("chính là độ đo xác suất trên các phân hoạch ngẫu nhiên!", 23, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(box3)

        box4 = card(7.6, 2.7, MINT).move_to([0, -1.8, 0])
        b4_txt = VGroup(
            fit(T("Quá trình Schur (Okounkov–Reshetikhin):", 25, SUN), 7.0),
            fit(T("Khung xác suất định thức chung cho tinh thể nóng chảy", 22, WHITE), 7.0),
            fit(T("và biên đóng băng (frozen boundary) đại số.", 22, SKY), 7.0),
        ).arrange(DOWN, buff=0.18).move_to(box4)

        self.play(FadeIn(box3), FadeIn(b3_txt), run_time=1.0)
        self.play(FadeIn(box4), FadeIn(b4_txt), run_time=1.0)
        end_vo("s2", t0, 9.5)
        save_tl()
