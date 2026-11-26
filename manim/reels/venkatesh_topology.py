from common_b import *
import json

# Kiểm tra toán học cho bài 02_07: Không gian đối xứng địa phương & Phần xoắn đối đồng điều
# Ví dụ phần xoắn trong Z/nZ: phần tử c != 0 thỏa n*c = 0 (mod n)
N_TORSION = 5
C_ELEM = 1
assert C_ELEM % N_TORSION != 0 and (N_TORSION * C_ELEM) % N_TORSION == 0

# Khiếm khuyết hạng l0 = rank(G) - rank(K) cho SL(2, C) với K = SU(2)
RANK_SL2C = 2
RANK_SU2 = 1
DEFECT_L0 = RANK_SL2C - RANK_SU2
assert DEFECT_L0 == 1  # Xuất hiện ở l0 + 1 = 2 bậc đối đồng điều: H¹ và H²

TX = {
    "title": {
        "vi": "Tô pô Đa tạp Số học &\nPhần xoắn Đối đồng điều",
        "en": "Arithmetic Manifolds &\nTorsion in Cohomology",
    },
    "s1_a": {
        "vi": "Không gian đối xứng địa phương  X = Γ \\ G / K\nCây cầu nối nhóm số học với hình học đa tạp",
        "en": "Locally symmetric spaces  X = Γ \\ G / K\nBridging arithmetic groups and manifold topology",
    },
    "s1_b": {
        "vi": "Cùng một nhóm Γ sinh ra dạng tự đẳng cấu,\nđồng thời dựng nên đa tạp giàu cấu trúc tô pô!",
        "en": "The same group Γ produces automorphic forms\nand builds manifolds with rich topology!",
    },
    "s2_a": {
        "vi": "Đa tạp 3 chiều số học  M = Γ \\ H³:\nĐối đồng điều H¹(M, Z) chứa phần xoắn khổng lồ!",
        "en": "Arithmetic 3-manifolds  M = Γ \\ H³:\nCohomology H¹(M, Z) holds massive torsion!",
    },
    "s2_b": {
        "vi": "Phần xoắn (n · c = 0) tăng hàm mũ theo thể tích\n(Định lý Bergeron–Venkatesh)!",
        "en": "Torsion (n · c = 0) grows exponentially\nwith manifold volume (Bergeron–Venkatesh)!",
    },
    "s3_a": {
        "vi": "Bí ẩn: Cùng một biểu diễn Galois xuất hiện\nlặp lại ở cả H¹ và H² của đa tạp số học!",
        "en": "Mystery: The exact same Galois representation\nrepeats across both H¹ and H²!",
    },
    "s3_b": {
        "vi": "Giả thuyết Venkatesh: Đối đồng điều motivic\ntác động tự nhiên lên đối đồng điều đa tạp!",
        "en": "Venkatesh's conjecture: Motivic cohomology\nacts naturally on arithmetic cohomology!",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class VenkateshTopology(Scene):
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

        # --- Phần 1: Không gian đối xứng địa phương Γ\G/K ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        c2d = RoundedRectangle(
            corner_radius=0.14, width=7.6, height=1.45,
            fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5
        ).move_to([0, 2.25, 0])
        t2d = T(
            "2 chiều:  SL(2, Z) \\ H²  (Mặt modular hyperbolic)"
            if LANG == "vi" else
            "2D:  SL(2, Z) \\ H²  (Hyperbolic modular surface)",
            21, MINT
        ).move_to(c2d)

        c3d = RoundedRectangle(
            corner_radius=0.14, width=7.6, height=1.45,
            fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5
        ).move_to([0, 0.35, 0])
        t3d = T(
            "3 chiều:  SL(2, Z[i]) \\ H³  (Đa tạp 3D số học)"
            if LANG == "vi" else
            "3D:  SL(2, Z[i]) \\ H³  (Arithmetic 3-manifold)",
            21, SUN
        ).move_to(c3d)

        self.play(FadeIn(c2d, t2d), run_time=1.0)
        self.play(FadeIn(c3d, t3d), run_time=1.0)
        self.wait(1.8)

        s1b = line(TX["s1_b"], 22, WHITE, -1.8)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 8.0)
        wipe(self, keep=[title])

        # --- Phần 2: Phần xoắn khổng lồ trong H¹(Γ\H³, Z) ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        h_box = RoundedRectangle(
            corner_radius=0.16, width=7.6, height=2.45,
            fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=3
        ).move_to([0, 1.5, 0])
        h_txt = T(
            "H¹(Γ \\ H³, Z)  =  Z^r   ⊕   Phần xoắn (Torsion)\n\nPhần tự do Z^r: thường rất ít!\nPhần xoắn (n · c = 0): khổng lồ theo thể tích!"
            if LANG == "vi" else
            "H¹(Γ \\ H³, Z)  =  Z^r   ⊕   Torsion\n\nFree part Z^r: often tiny!\nTorsion (n · c = 0): grows massively with volume!",
            21, PINK
        ).move_to(h_box)
        self.play(FadeIn(h_box, h_txt), run_time=1.2)
        self.wait(1.8)

        s2b = line(TX["s2_b"], 22, SUN, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 8.0)
        wipe(self, keep=[title])

        # --- Phần 3: Tác động đối đồng điều motivic ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        b_h1 = RoundedRectangle(
            corner_radius=0.14, width=2.8, height=1.55,
            fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5
        ).move_to([-2.2, 1.5, 0])
        t_h1 = T("H¹(M)\nBậc 1" if LANG == "vi" else "H¹(M)\nDegree 1", 22, MINT).move_to(b_h1)

        b_h2 = RoundedRectangle(
            corner_radius=0.14, width=2.8, height=1.55,
            fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5
        ).move_to([2.2, 1.5, 0])
        t_h2 = T("H²(M)\nBậc 2" if LANG == "vi" else "H²(M)\nDegree 2", 22, SUN).move_to(b_h2)

        arr_m = Arrow([-0.7, 1.5, 0], [0.7, 1.5, 0], color=SKY, buff=0.05, stroke_width=4)
        lbl_m = T("Motivic" if LANG == "vi" else "Motivic", 19, SKY).next_to(arr_m, UP, buff=0.12)

        self.play(FadeIn(b_h1, t_h1), GrowArrow(arr_m), FadeIn(lbl_m), FadeIn(b_h2, t_h2), run_time=1.3)
        self.wait(1.8)

        s3b = line(TX["s3_b"], 22, WHITE, -1.8)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 8.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
