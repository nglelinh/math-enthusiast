from common_b import *
import json
import math

# Kiểm tra các hằng số toán học cho lưới Leech 24 chiều từ bài 02_08
KISSING_LEECH = 196560
MIN_LEN_LEECH = 2
R_LEECH = MIN_LEN_LEECH / 2.0
FACT_12 = math.factorial(12)
DELTA_LEECH = (math.pi ** 12) / FACT_12
SOLVED_DIMS = (1, 2, 3, 8, 24)
OPEN_DIMS = (4, 5, 6, 7)

assert FACT_12 == 479001600
assert R_LEECH == 1.0
assert abs(DELTA_LEECH * 100 - 0.19295743) < 1e-6
assert KISSING_LEECH == 196560
assert set(SOLVED_DIMS).isdisjoint(set(OPEN_DIMS))

TX = {
    "title": {
        "vi": "Lưới Leech 24 chiều &\nTính tối ưu phổ quát",
        "en": "The 24D Leech Lattice &\nUniversal Optimality",
    },
    "s1_a": {
        "vi": "Lưới Leech Λ24 trong không gian R^24:\nkhông có vectơ độ dài √2, đối xứng siêu việt!",
        "en": "Leech lattice Λ24 in 24-dimensional space:\nno length-√2 vectors, extraordinary symmetry!",
    },
    "s1_b": {
        "vi": "Ở chiều 24, mật độ tuy rất nhỏ (0,193%)\nnhưng Λ24 vẫn là kỷ lục tuyệt đối!",
        "en": "In 24D, density is tiny (0.193%),\nyet Λ24 still beats every other packing!",
    },
    "s2_a": {
        "vi": "Chỉ 1 tuần sau bài báo 8 chiều (3/2016):\nnhóm 5 tác giả CKMRV giải gọn chiều 24!",
        "en": "Just 1 week after the 8D preprint (Mar 2016):\nthe 5-author CKMRV team solved dimension 24!",
    },
    "s2_b": {
        "vi": "Không chỉ xếp cầu cứng — E8 và Λ24 còn là\ncấu trúc cực tiểu năng lượng hoàn hảo nhất!",
        "en": "Beyond hard spheres — E8 and Λ24 also\nminimize energy across all monotonic laws!",
    },
    "s3_a": {
        "vi": "Nghịch lý của bài toán xếp cầu:\nChiều càng cao KHÔNG hẳn càng khó!",
        "en": "The paradox of sphere packing:\nHigher dimension is NOT always harder!",
    },
    "s3_b": {
        "vi": "Chiều 8 và 24 là hai kỳ quan đối xứng\nnơi dạng modular mở khóa lời giải tuyệt đối!",
        "en": "Dims 8 and 24 are two symmetry miracles\nwhere modular forms unlock exact optimality!",
    },
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


def make_card(txt, col, y, w=7.6, h=1.22, size=21):
    b = RoundedRectangle(
        corner_radius=0.14,
        width=w,
        height=h,
        fill_color=CARD,
        fill_opacity=1,
        stroke_color=col,
        stroke_width=2.5,
    ).move_to([0, y, 0])
    parts = txt.split("\n")
    ts = [T(p, size, col) for p in parts]
    g = VGroup(*ts).arrange(DOWN, buff=0.12) if len(ts) > 1 else ts[0]
    fit(g, w - 0.35).move_to(b)
    return VGroup(b, g)


class ViazovskaLeech24D(Scene):
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
                rem = vo_durs[sid] - (float(self.time) - t0) + 1.0
                self.wait(max(0.6, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 33, WHITE, 6.2)
        self.add(title)

        # --- Đoạn 1: Lưới Leech 24D: 196.560 vectơ độ dài 2 & mật độ π^12/12! ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        kiss_str = "196.560" if LANG == "vi" else "196,560"
        pct_str = nf(DELTA_LEECH * 100, 3)

        c1 = make_card(
            "Vectơ ngắn nhất:  ||x|| = 2  (bán kính cầu r = 1)\nLưới unimodular chẵn duy nhất không có vectơ √2"
            if LANG == "vi"
            else "Shortest vectors:  ||x|| = 2  (ball radius r = 1)\nUnique even unimodular lattice with no length-√2 vectors",
            SKY,
            2.55,
            h=1.22,
            size=20,
        )
        c2 = make_card(
            f"Số hôn (hàng xóm chạm khít 1 quả cầu):\n{kiss_str} quả cầu tiếp xúc đồng thời!"
            if LANG == "vi"
            else f"Kissing number (neighbors touching 1 sphere):\n{kiss_str} spheres tangent simultaneously!",
            SUN,
            1.00,
            h=1.22,
            size=21,
        )
        c3 = make_card(
            f"Mật độ xếp cầu tối ưu trong R^24:\nδ(Λ24) = π¹² / 12! ≈ {pct_str}%"
            if LANG == "vi"
            else f"Optimal packing density in R^24:\nδ(Λ24) = π¹² / 12! ≈ {pct_str}%",
            MINT,
            -0.55,
            h=1.28,
            size=21,
        )

        self.play(FadeIn(c1), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(c2), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(c3), run_time=1.0)
        self.wait(1.2)

        s1b = line(TX["s1_b"], 23, WHITE, -2.55)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Đoạn 2: Hợp tác CKMRV một tuần sau & Tính tối ưu phổ quát ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        k1 = make_card(
            "Phân biệt công lao rõ ràng:\nChiều 8 (E8):  Viazovska (một mình)\nChiều 24 (Λ24):  Cohn · Kumar · Miller · Radchenko · Viazovska"
            if LANG == "vi"
            else "Keeping credit sharp:\nDim 8 (E8):  Viazovska (solo)\nDim 24 (Λ24):  Cohn · Kumar · Miller · Radchenko · Viazovska",
            SKY,
            2.45,
            h=1.48,
            size=19,
        )
        k2 = make_card(
            "Tính tối ưu phổ quát (Universal Optimality):\nE8 và Λ24 cực tiểu hóa năng lượng dưới MỌI\nhàm thế tương tác hoàn toàn đơn điệu!"
            if LANG == "vi"
            else "Universal Optimality (CKMRV 2019/2022):\nE8 and Λ24 minimize energy under EVERY\ncompletely monotonic interaction potential!",
            MINT,
            0.65,
            h=1.48,
            size=20,
        )
        k3 = make_card(
            "Mở rộng: Công thức nội suy Fourier\nkhôi phục hàm xuyên tâm từ giá trị tại √n"
            if LANG == "vi"
            else "Bonus: Fourier interpolation formulas\nrecover radial functions from values at √n",
            SUN,
            -1.05,
            h=1.18,
            size=20,
        )

        self.play(FadeIn(k1), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(k2), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(k3), run_time=0.9)
        self.wait(1.2)

        s2b = line(TX["s2_b"], 23, WHITE, -2.85)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- Đoạn 3: Chiều đã giải (1, 2, 3, 8, 24) vs Chiều còn mở (4, 5, 6, 7...) ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        # Hàng 1: chiều 1..5, Hàng 2: chiều 6, 7, 8, ..., 24
        row1_data = [
            ("1", True), ("2", True), ("3", True), ("4?", False), ("5?", False),
        ]
        row2_data = [
            ("6?", False), ("7?", False), ("8", True), ("...", False), ("24", True),
        ]

        badges = VGroup()
        for r_idx, row in enumerate((row1_data, row2_data)):
            y = 2.65 - r_idx * 1.45
            for c_idx, (lbl, solved) in enumerate(row):
                x = -3.0 + c_idx * 1.5
                col = MINT if solved else PINK
                box = RoundedRectangle(
                    corner_radius=0.14,
                    width=1.22,
                    height=1.08,
                    fill_color=CARD,
                    fill_opacity=1,
                    stroke_color=col,
                    stroke_width=3 if solved else 2,
                ).move_to([x, y, 0])
                txt = T(lbl, 28, col).move_to(box)
                badges.add(VGroup(box, txt))

        self.play(FadeIn(badges, lag_ratio=0.08), run_time=1.4)
        self.wait(1.2)

        c_solved = make_card(
            "Đã giải chính xác:  n = 1, 2, 3, 8 (E8), 24 (Leech)"
            if LANG == "vi"
            else "Solved exactly:  n = 1, 2, 3, 8 (E8), 24 (Leech)",
            MINT,
            -0.30,
            h=0.92,
            size=20,
        )
        c_open = make_card(
            "Vẫn còn mở:  n = 4, 5, 6, 7 và hầu hết mọi chiều!"
            if LANG == "vi"
            else "Still open:  n = 4, 5, 6, 7 and almost all dims!",
            PINK,
            -1.45,
            h=0.92,
            size=20,
        )
        self.play(FadeIn(c_solved), FadeIn(c_open), run_time=1.0)
        self.wait(1.2)

        s3b = line(TX["s3_b"], 23, WHITE, -3.10)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
