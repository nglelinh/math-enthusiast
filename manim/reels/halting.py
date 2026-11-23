from common_b import *
import json

TX = {
    "title": {"vi": "Alan Turing (1936):\nMáy phổ quát & Bài toán Dừng", "en": "Alan Turing (1936):\nUniversal machine & Halting"},
    "s1_a": {"vi": "Máy Turing: băng vô hạn, đầu đọc–ghi\nvà bảng chuyển trạng thái hữu hạn", "en": "Turing machine: infinite tape, head,\nand finite transition table"},
    "s1_b": {"vi": "Máy phổ quát U(⟨M⟩, x) mô phỏng mọi máy M:\nchương trình chính là dữ liệu!", "en": "Universal machine U(⟨M⟩, x) simulates any M:\nprograms are just data!"},
    "s2_a": {"vi": "Bài toán Dừng (Halting Problem):\nCó tồn tại máy H(⟨M⟩, x) luôn dừng?", "en": "The Halting Problem:\nDoes a total decider H(⟨M⟩, x) exist?"},
    "s2_b": {"vi": "H(⟨M⟩, x) = 1 nếu M(x) dừng\nH(⟨M⟩, x) = 0 nếu M(x) lặp vô hạn", "en": "H(⟨M⟩, x) = 1 if M(x) halts\nH(⟨M⟩, x) = 0 if M(x) loops forever"},
    "s3_a": {"vi": "Phản chứng bằng đường chéo Cantor:\nDựng máy nghịch đảo D(⟨M⟩)", "en": "Cantor diagonal contradiction:\nBuild the opposite machine D(⟨M⟩)"},
    "s3_b": {"vi": "Nếu H(⟨M⟩, ⟨M⟩) = 1 ⇒ D lặp vô hạn!\nNếu H(⟨M⟩, ⟨M⟩) = 0 ⇒ D dừng ngay!", "en": "If H(⟨M⟩, ⟨M⟩) = 1 ⇒ D loops forever!\nIf H(⟨M⟩, ⟨M⟩) = 0 ⇒ D halts immediately!"},
    "s4_a": {"vi": "Chạy D trên chính mã của nó: D(⟨D⟩)", "en": "Run D on its own code: D(⟨D⟩)"},
    "s4_b": {"vi": "D(⟨D⟩) dừng ⇔ H = 1 ⇔ D(⟨D⟩) lặp vô hạn!\n⇒ Mâu thuẫn tuyệt đối! H không tồn tại!", "en": "D(⟨D⟩) halts ⇔ H = 1 ⇔ D(⟨D⟩) loops!\n⇒ Contradiction! H cannot exist!"},
    "end": {"vi": "Bất khả quyết định ≠ NP-khó:\nKhông tồn tại thuật toán nào cho mọi đầu vào", "en": "Undecidable ≠ NP-hard:\nNo algorithm exists for all inputs"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class HaltingProblem(Scene):
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

        title = line(TX["title"], 36, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Máy Turing & Máy phổ quát ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)
        cells = VGroup()
        syms = ["0", "1", "1", "0", "□", "1", "0"]
        for i, ch in enumerate(syms):
            sq = Square(0.85, color=DIM, fill_color=CARD, fill_opacity=1).move_to([(i - 3) * 0.9, 1.5, 0])
            tx = T(ch, 28, SUN if i == 2 else WHITE).move_to(sq)
            cells.add(VGroup(sq, tx))
        head = Triangle(color=MINT, fill_color=MINT, fill_opacity=0.9).scale(0.28).move_to([-0.9, 2.35, 0]).rotate(math.pi)
        self.play(FadeIn(cells), FadeIn(head), run_time=1.2)
        self.play(head.animate.shift(RIGHT * 0.9), run_time=0.8)
        s1b = line(TX["s1_b"], 25, MINT, -0.8)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 2: Bài toán Dừng ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 28, SUN, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)
        hbox = RoundedRectangle(corner_radius=0.16, width=4.4, height=2.2,
                                fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=3).move_to([0, 1.1, 0])
        htxt = T("H(⟨M⟩, x)", 32, SKY).move_to(hbox)
        in_arr = Arrow([-3.5, 1.1, 0], [-2.25, 1.1, 0], buff=0, color=WHITE)
        out1 = Arrow([2.25, 1.6, 0], [3.5, 1.6, 0], buff=0, color=MINT)
        out0 = Arrow([2.25, 0.6, 0], [3.5, 0.6, 0], buff=0, color=PINK)
        t1 = T("1", 26, MINT).next_to(out1, RIGHT, buff=0.1)
        t0_lbl = T("0", 26, PINK).next_to(out0, RIGHT, buff=0.1)
        self.play(FadeIn(hbox), FadeIn(htxt), Create(in_arr), Create(out1), Create(out0), FadeIn(t1), FadeIn(t0_lbl), run_time=1.3)
        s2b = line(TX["s2_b"], 26, WHITE, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 3: Máy nghịch đảo D ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 26, PINK, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)
        dbox = RoundedRectangle(corner_radius=0.16, width=6.8, height=2.6,
                                fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.8).move_to([0, 1.0, 0])
        dcode = VGroup(
            T("D(⟨M⟩):" if LANG == "vi" else "D(⟨M⟩):", 26, SUN),
            T("  if H(⟨M⟩, ⟨M⟩) == 1:  loop ∞", 23, PINK),
            T("  else:                 halt", 23, MINT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(dbox)
        self.play(FadeIn(dbox), FadeIn(dcode), run_time=1.2)
        s3b = line(TX["s3_b"], 25, WHITE, -2.0)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 4: Tự tham chiếu D(<D>) ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 30, SUN, 4.4)
        self.play(FadeIn(s4a), run_time=0.8)
        boom = RoundedRectangle(corner_radius=0.16, width=7.0, height=2.8,
                                fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=3).move_to([0, 1.0, 0])
        btxt = VGroup(
            T("D(⟨D⟩) dừng ⇒ H = 1 ⇒ D lặp ∞!" if LANG == "vi" else "D(⟨D⟩) halts ⇒ H = 1 ⇒ D loops!", 24, PINK),
            T("D(⟨D⟩) lặp  ⇒ H = 0 ⇒ D dừng!" if LANG == "vi" else "D(⟨D⟩) loops ⇒ H = 0 ⇒ D halts!", 24, MINT),
        ).arrange(DOWN, buff=0.35).move_to(boom)
        self.play(FadeIn(boom), FadeIn(btxt), run_time=1.3)
        s4b = line(TX["s4_b"], 25, PINK, -2.2)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 10.0)
        wipe(self, keep=[title])

        # --- Phần 5: Tổng kết ---
        t0 = start_vo("s5")
        end_c = line(TX["end"], 28, WHITE, 1.2)
        sum_box = RoundedRectangle(corner_radius=0.16, width=7.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=2.5).move_to([0, -1.8, 0])
        sum_t = VGroup(
            T("Turing 1936: Halting bất khả quyết định" if LANG == "vi" else "Turing 1936: Halting is undecidable", 25, SUN),
            T("Anh em với Cantor & Bất toàn Gödel" if LANG == "vi" else "Sibling to Cantor & Gödel incompleteness", 24, MINT),
        ).arrange(DOWN, buff=0.28).move_to(sum_box)
        self.play(FadeIn(end_c), FadeIn(sum_box), FadeIn(sum_t), run_time=1.2)
        end_vo("s5", t0, 8.0)

        tl_out = os.environ.get("VO_TIMELINE_JSON", "")
        if tl_out:
            with open(tl_out, "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
