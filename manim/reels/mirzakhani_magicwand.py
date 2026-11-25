from common_b import *
import json

# Kiểm tra định thức ma trận kéo giãn trong SL(2, R)
a = 2.0
assert abs(a * (1.0 / a) - 1.0) < 1e-12

TX = {
    "title": {"vi": "Bi-a Đa giác, Dòng Động đất &\nĐịnh lý Cây đũa thần", "en": "Polygonal Billiards, Earthquakes &\nThe Magic Wand Theorem"},
    "s1_a": {"vi": "Dòng động đất (Thurston): cắt mặt hyperbolic,\ntrượt lệch hai mép như đứt gãy địa chất rồi dán lại!", "en": "Earthquake flow (Thurston): cut a hyperbolic surface,\nshear along the fault line, and reglue!"},
    "s1_b": {"vi": "Mirzakhani chứng minh dòng động đất là ERGODIC\n⇒ Khớp đúng đếm đường cong trên từng mặt X!", "en": "Mirzakhani proved earthquake flow is ERGODIC\n⇒ Pins down curve counts on every surface X!"},
    "s2_a": {"vi": "Mẹo trải phẳng bàn bi-a đa giác:\nThay vì để bi bật lại, hãy lật phản chiếu cả bàn!", "en": "Unfolding a polygonal billiard table:\nInstead of bouncing the ball, reflect the table!"},
    "s2_b": {"vi": "Viên bi đi thẳng tắp trên một Mặt phẳng dịch chuyển\n(Translation surface) do dán các bản sao tạo thành!", "en": "The ball travels straight on a Translation Surface\nbuilt by gluing reflected copies of the table!"},
    "s3_a": {"vi": "Định lý Cây đũa thần (Eskin–Mirzakhani 2013):\nNhóm SL(2, R) kéo giãn–nén các mặt phẳng dịch chuyển", "en": "Magic Wand Theorem (Eskin–Mirzakhani 2013):\nSL(2, R) stretches and shears translation surfaces"},
    "s3_b": {"vi": "Mọi bao đóng quỹ đạo & độ đo bất biến đều cực 'cứng'\n(đa tạp con affine) — như định lý Ratner trên mô-đun!", "en": "Every orbit closure & invariant measure is rigid\n(affine submanifold) — Ratner-style rigidity!"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class MirzakhaniMagicWand(Scene):
    def construct(self):
        vo_path = os.environ.get("VO_DUR_JSON", "")
        vo_durs = json.load(open(vo_path)) if vo_path and os.path.exists(vo_path) else {}
        timeline = []

        def start_vo(sid):
            t0 = float(self.time)
            timeline.append((sid, t0))
            return t0

        def end_vo(sid, t0, fallback):
            if sid in vo_durs:
                rem = vo_durs[sid] - (float(self.time) - t0) + 1.2
                self.wait(max(0.8, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 33, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Dòng động đất ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        top_half = RoundedRectangle(corner_radius=0.12, width=5.6, height=0.95, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([-0.5, 2.0, 0])
        bot_half = RoundedRectangle(corner_radius=0.12, width=5.6, height=0.95, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0.5, 0.85, 0])
        fault = DashedLine([-3.4, 1.42, 0], [3.4, 1.42, 0], color=PINK, stroke_width=4)
        arr_r = Arrow([-1.5, 2.0, 0], [1.5, 2.0, 0], color=MINT, buff=0)
        arr_l = Arrow([1.5, 0.85, 0], [-1.5, 0.85, 0], color=SUN, buff=0)
        self.play(FadeIn(top_half, bot_half, fault), GrowArrow(arr_r), GrowArrow(arr_l), run_time=1.2)
        self.play(top_half.animate.shift(RIGHT * 0.6), bot_half.animate.shift(LEFT * 0.6), run_time=1.1)
        self.wait(1.5)

        s1b = line(TX["s1_b"], 23, SUN, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Trải phẳng bàn bi-a đa giác ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        r1 = Rectangle(width=2.8, height=1.8, color=SKY, stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([-1.4, 1.4, 0])
        r2 = Rectangle(width=2.8, height=1.8, color=MINT, stroke_width=3, fill_color=CARD, fill_opacity=0.6).move_to([1.4, 1.4, 0])
        bounce = VMobject(color=PINK, stroke_width=4).set_points_as_corners([[-2.5, 0.7, 0], [0.0, 1.5, 0], [-2.2, 2.2, 0]])
        straight = Line([-2.5, 0.7, 0], [2.2, 2.2, 0], color=SUN, stroke_width=4)
        lbl_u = T("Bàn gốc (bật lại)" if LANG == "vi" else "Original (bounce)", 18, PINK).move_to([-1.4, 0.15, 0])
        lbl_v = T("Bản phản chiếu (đi thẳng!)" if LANG == "vi" else "Reflected (straight!)", 18, MINT).move_to([1.4, 0.15, 0])

        self.play(FadeIn(r1, lbl_u), Create(bounce), run_time=1.1)
        self.play(FadeIn(r2, lbl_v), Create(straight), run_time=1.1)
        self.wait(1.8)

        s2b = line(TX["s2_b"], 23, WHITE, -1.7)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Định lý Cây đũa thần (Eskin-Mirzakhani) ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        mw_box = RoundedRectangle(corner_radius=0.16, width=7.5, height=2.2, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=3).move_to([0, 1.5, 0])
        mw_t = T("Tác động SL(2, R) lên Mặt phẳng dịch chuyển:\n\nQuỹ đạo KHÔNG hỗn loạn vô định\n⇒ Bao đóng luôn là đa tạp con affine!" if LANG == "vi" else "SL(2, R) action on Translation Surfaces:\n\nOrbits NEVER wander wildly\n⇒ Closures are rigid affine submanifolds!", 21, MINT).move_to(mw_box)
        self.play(FadeIn(mw_box, mw_t), run_time=1.2)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 23, SUN, -1.7)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
