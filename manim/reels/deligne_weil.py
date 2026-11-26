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
    "s1_tag": {"vi": "GIẢ THUYẾT WEIL (1949)", "en": "WEIL CONJECTURES"},
    "s1_t": {"vi": "Đếm điểm trên trường hữu hạn 𝔽_q", "en": "Counting Points"},
    "s1_c1": {"vi": "Với đường cong X trên 𝔽_5: số điểm N_m = |X(𝔽_{5^m})|\nđược mã hóa gọn trong hàm zeta Z(X, T).", "en": "Local zeta function"},
    "s1_c2": {"vi": "Tương tự Giả thuyết Riemann: mọi nghiệm α_i của\nđa thức tử đều có mô-đun đúng bằng q^(1/2)!", "en": "Riemann Hypothesis over F_q"},
    "s2_tag": {"vi": "CHỨNG MINH CỦA DELIGNE (1974)", "en": "DELIGNE'S PROOF"},
    "s2_t": {"vi": "Tính thuần khiết của trị riêng Frobenius", "en": "Purity of Frobenius"},
    "s2_c1": {"vi": "Grothendieck dựng đối đồng điều étale & viết\nN_m bằng vết phép lặp Frobenius Frob^m!", "en": "Etale cohomology"},
    "s2_c2": {"vi": "Deligne (1974): Dùng bút Lefschetz + tích tensor\nbậc chẵn (phương pháp Rankin–Selberg) khóa chặt |α_i|!", "en": "Lefschetz pencils"},
    "s3_tag": {"vi": "CHẶN RAMANUJAN–PETERSSON", "en": "RAMANUJAN–PETERSSON"},
    "s3_t": {"vi": "Hệ quả chấn động cho Lý thuyết số", "en": "Number Theory Impact"},
    "s3_c1": {"vi": "Từ Weil I, Deligne suy ra ngay |τ(p)| ≤ 2 p^(11/2)\ncho hàm tau Ramanujan — nhận Fields 1978!", "en": "Ramanujan tau bound"},
}

class DeligneWeil(Scene):
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
        c2 = card(6.3, 2.0, MINT).move_to([0, -1.0, 0])
        t2 = fit(T(tr(TX["s2_c2"]), 22, MINT), 5.9).move_to(c2)
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
