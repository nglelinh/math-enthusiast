from common_b import *
import json
import math

# Kiểm tra công thức thể tích Weil-Petersson mặt xuyến khoét 1 lỗ V_{1,1}(L)
def V11(L):
    return (L**2 + 4 * math.pi**2) / 24.0

assert abs(V11(0.0) - math.pi**2 / 6.0) < 1e-12
assert abs(V11(2 * math.pi) - math.pi**2 / 3.0) < 1e-12

TX = {
    "title": {"vi": "Thể tích Weil–Petersson &\nCông thức Đệ quy Mirzakhani", "en": "Weil–Petersson Volumes &\nMirzakhani's Recursion"},
    "s1_a": {"vi": "Định lý Wolpert: Dạng thể tích tự nhiên\ntrên tọa độ Fenchel–Nielsen cực gọn!", "en": "Wolpert's Theorem: The natural volume form\nin Fenchel–Nielsen coordinates is astonishingly clean!"},
    "s1_b": {"vi": "Lấy lũy thừa ngoài cho ta thể tích V(g, n)\ncủa không gian các mặt có n biên dài L1..Ln", "en": "Its top exterior power gives the volume V(g, n)\nof surfaces with n geodesic boundaries L1..Ln"},
    "s2_a": {"vi": "Bắn tia trắc địa từ biên L1 ⇒ Đồng nhất thức McShane\nTích phân lên cho công thức đệ quy theo chiếc quần!", "en": "Shooting rays from boundary L1 ⇒ McShane identity\nIntegrating yields a pants-cutting recursion!"},
    "s2_b": {"vi": "Mọi V(g, n) là ĐA THỨC theo L1², ..., Ln²!\nHệ số bậc cao ⇒ chứng minh mới giả thuyết Witten!", "en": "Every V(g, n) is a POLYNOMIAL in L1², ..., Ln²!\nTop coefficients ⇒ geometric proof of Witten's conjecture!"},
    "s3_a": {"vi": "Phép màu đổi thứ tự tích phân:\nĐếm đường trên 1 mặt ⇒ Tích phân thể tích M(g)!", "en": "Magic of swapping integrals:\nCounting on 1 surface ⇒ Integrating WP volumes!"},
    "s3_b": {"vi": "Tích phân ∫ l · l^(6g − 8) dl\n⇒ Cho ngay bậc đa thức L^(6g − 6)!", "en": "Integrating ∫ l · l^(6g − 8) dl\n⇒ Immediately produces degree L^(6g − 6)!"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class MirzakhaniWPVolume(Scene):
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

        # --- Phần 1: Dạng symplectic Weil-Petersson ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 24, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        w_box = RoundedRectangle(corner_radius=0.16, width=7.4, height=1.9, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=3).move_to([0, 1.5, 0])
        w_t = T("ω(WP)  =  ∑  d(l_i) ∧ d(θ_i)\n(tổng chạy từ i = 1 đến 3g − 3)" if LANG == "vi" else "ω(WP)  =  ∑  d(l_i) ∧ d(θ_i)\n(summed over i = 1 to 3g − 3)", 23, SUN).move_to(w_box)
        self.play(FadeIn(w_box, w_t), run_time=1.1)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 23, WHITE, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Ví dụ cầm tay V(1,1)(L) ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        v_box = RoundedRectangle(corner_radius=0.16, width=7.5, height=2.5, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=3).move_to([0, 1.4, 0])
        v_t = T("Mặt xuyến khoét 1 lỗ (g = 1, n = 1):\n\nV(1,1)(L)  =  (L² + 4π²) / 24\n\nCho L → 0:   V(1,1)(0)  =  π² / 6 !" if LANG == "vi" else "One-holed torus (g = 1, n = 1):\n\nV(1,1)(L)  =  (L² + 4π²) / 24\n\nCusp limit L → 0:   V(1,1)(0)  =  π² / 6 !", 22, MINT).move_to(v_box)
        self.play(FadeIn(v_box, v_t), run_time=1.2)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 23, SUN, -1.7)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Đổi thứ tự tích phân ra L^(6g-6) ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 24, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        steps = VGroup()
        st_data = [
            ("1. Cắt mặt dọc theo đường cong độ dài l ≤ L" if LANG == "vi" else "1. Cut surface along a curve of length l ≤ L", SKY),
            ("2. Phần còn lại có thể tích bậc 6g − 8 theo l" if LANG == "vi" else "2. Remaining piece has volume degree 6g − 8", MINT),
            ("3. Nhân góc xoắn l rồi tích phân từ 0 đến L" if LANG == "vi" else "3. Multiply twist l and integrate from 0 to L", SUN),
        ]
        for i, (txt, col) in enumerate(st_data):
            y = 2.4 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.9, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            steps.add(VGroup(b, t))
        self.play(FadeIn(steps, lag_ratio=0.3), run_time=1.4)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 24, WHITE, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
