from common_b import *
import json

# Kiểm tra các hằng số toán học từ bài 02_05
def pants_count(g):
    return 2 * g - 2

def cut_count(g):
    return 3 * g - 3

def fn_dim(g):
    return 6 * g - 6

assert pants_count(2) == 2 and cut_count(2) == 3 and fn_dim(2) == 6
assert pants_count(3) == 4 and cut_count(3) == 6 and fn_dim(3) == 12

TX = {
    "title": {"vi": "Mirzakhani (Fields 2014) &\nKhông gian Mô-đun", "en": "Mirzakhani (Fields 2014) &\nModuli Spaces"},
    "s1_a": {"vi": "Không gian mô-đun là gì?\nMỗi điểm = một hình dạng hoàn chỉnh!", "en": "What is a moduli space?\nEach point = an entire geometric shape!"},
    "s1_b": {"vi": "Ví dụ mặt xuyến (g = 1): M(1) = H / SL(2, Z)\nτ = i và τ = i + 1 cho cùng một lưới vuông!", "en": "Torus example (g = 1): M(1) = H / SL(2, Z)\nτ = i and τ = i + 1 give the exact same lattice!"},
    "s2_a": {"vi": "Mặt hyperbolic giống g ≥ 2 (χ = 2 − 2g < 0)\nCắt thành 2g − 2 'chiếc quần' (χ = −1)!", "en": "Hyperbolic surface g ≥ 2 (χ = 2 − 2g < 0)\nCut into 2g − 2 'pairs of pants' (χ = −1)!"},
    "s2_b": {"vi": "3g − 3 độ dài + 3g − 3 góc xoắn\n⇒ Đúng 6g − 6 tọa độ Fenchel–Nielsen!", "en": "3g − 3 lengths + 3g − 3 twist angles\n⇒ Exactly 6g − 6 Fenchel–Nielsen coordinates!"},
    "s3_a": {"vi": "Đếm đường trắc địa đóng ĐƠN (không tự cắt)\ncó độ dài ≤ L trên một mặt X cố định:", "en": "Counting SIMPLE closed geodesics (no self-crossings)\nof length ≤ L on a fixed surface X:"},
    "s3_b": {"vi": "Số mũ 6g − 6 khớp đúng số chiều thực\ncủa không gian mô-đun M(g)!", "en": "The exponent 6g − 6 matches the exact\nreal dimension of moduli space M(g)!"},
    "s4_a": {"vi": "Tỉ lệ tô pô chính xác trên mặt 2 lỗ (g = 2):\nĐường cắt rời mặt vs đường không tách mặt", "en": "Exact topological ratio on a genus-2 surface:\nSeparating vs. non-separating simple curves"},
    "s4_b": {"vi": "Tỉ lệ là số hữu tỷ tuyệt đẹp: đúng 1 / 48\nđọc thẳng từ tỉ số thể tích không gian mô-đun!", "en": "An exact rational ratio: precisely 1 / 48\nread straight off moduli-space volumes!"},
    "s5_a": {"vi": "Di sản của Maryam Mirzakhani (1977–2017)\nNgười phụ nữ đầu tiên đoạt Huy chương Fields:", "en": "Legacy of Maryam Mirzakhani (1977–2017)\nFirst woman to win the Fields Medal:"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class MirzakhaniModuli(Scene):
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

        title = line(TX["title"], 34, WHITE, 6.2)
        self.add(title)

        # --- Phần 1: Không gian mô-đun là gì? ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 25, SKY, 4.6)
        self.play(FadeIn(s1a), run_time=0.8)

        b1 = RoundedRectangle(corner_radius=0.14, width=3.5, height=2.1, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=2.5).move_to([-2.0, 1.5, 0])
        sq = Square(side_length=1.0, color=MINT, stroke_width=3).move_to([-2.0, 1.85, 0])
        l1 = T("τ = i (hình vuông)" if LANG == "vi" else "τ = i (square)", 19, MINT).move_to([-2.0, 0.85, 0])

        b2 = RoundedRectangle(corner_radius=0.14, width=3.5, height=2.1, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([2.0, 1.5, 0])
        para = Polygon([1.2, 1.35, 0], [2.2, 1.35, 0], [2.8, 2.35, 0], [1.8, 2.35, 0], color=SUN, stroke_width=3)
        l2 = T("τ = i + 1 (nghiêng 45°)" if LANG == "vi" else "τ = i + 1 (sheared)", 19, SUN).move_to([2.0, 0.85, 0])

        eq_lbl = T("≅", 42, WHITE).move_to([0, 1.65, 0])
        self.play(FadeIn(b1, sq, l1), FadeIn(b2, para, l2), FadeIn(eq_lbl), run_time=1.3)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 23, WHITE, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Cắt mặt thành chiếc quần & tọa độ 6g - 6 ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 24, SKY, 4.6)
        self.play(FadeIn(s2a), run_time=0.8)

        cards = VGroup()
        rows = [
            ("g = 2 (mặt 2 lỗ):  2 chiếc quần, 3 đường cắt" if LANG == "vi" else "g = 2 (2 holes):  2 pairs of pants, 3 cuts", MINT),
            ("Tham số:  3 độ dài (l1, l2, l3) + 3 góc xoắn" if LANG == "vi" else "Params:  3 lengths (l1, l2, l3) + 3 twists", SUN),
            ("Tổng:  dim M(2) = 6  |  dim M(3) = 12" if LANG == "vi" else "Total:  dim M(2) = 6  |  dim M(3) = 12", SKY),
        ]
        for i, (txt, col) in enumerate(rows):
            y = 2.4 - i * 1.25
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=0.92, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            cards.add(VGroup(b, t))
        self.play(FadeIn(cards, lag_ratio=0.3), run_time=1.4)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 24, SUN, -1.8)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Đếm đường trắc địa đóng đơn ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 24, SKY, 4.6)
        self.play(FadeIn(s3a), run_time=0.8)

        c_all = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.35, fill_color=CARD, fill_opacity=1, stroke_color=PINK, stroke_width=2.5).move_to([0, 2.2, 0])
        t_all = T("Cho phép tự cắt:  tăng hàm mũ  ~ e^L / L" if LANG == "vi" else "Self-intersecting:  exponential  ~ e^L / L", 22, PINK).move_to(c_all)

        c_sim = RoundedRectangle(corner_radius=0.14, width=7.5, height=1.55, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=3).move_to([0, 0.3, 0])
        t_sim = T("Đường ĐƠN (Mirzakhani):\nN(X, L)  ~  c(X) · L^(6g − 6)" if LANG == "vi" else "SIMPLE geodesics (Mirzakhani):\nN(X, L)  ~  c(X) · L^(6g − 6)", 24, MINT).move_to(c_sim)

        self.play(FadeIn(c_all, t_all), run_time=1.0)
        self.play(FadeIn(c_sim, t_sim), run_time=1.1)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 24, WHITE, -1.9)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 4: Tỉ lệ 1 / 48 trên mặt giống 2 ---
        t0 = start_vo("s4")
        s4a = line(TX["s4_a"], 24, SKY, 4.6)
        self.play(FadeIn(s4a), run_time=0.8)

        bar_bg = RoundedRectangle(corner_radius=0.14, width=7.5, height=2.3, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=2.5).move_to([0, 1.5, 0])
        r_txt = T("Mặt 2 lỗ (g = 2), đường trắc địa đơn rất dài:\n\nKhông tách mặt : Tách mặt  =  48 : 1" if LANG == "vi" else "Genus-2 surface, long random simple geodesic:\n\nNon-separating : Separating  =  48 : 1", 22, SUN).move_to(bar_bg)
        self.play(FadeIn(bar_bg, r_txt), run_time=1.2)
        self.wait(2.0)

        s4b = line(TX["s4_b"], 23, MINT, -1.6)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 5: Di sản & Kết nối ---
        t0 = start_vo("s5")
        s5a = line(TX["s5_a"], 24, SKY, 4.6)
        self.play(FadeIn(s5a), run_time=0.8)

        leg = VGroup()
        l_data = [
            ("1. Thể tích Weil–Petersson & Đệ quy Mirzakhani" if LANG == "vi" else "1. Weil–Petersson Volumes & Recursion", MINT),
            ("2. Đếm đường trắc địa đơn: N(X, L) ~ c·L^(6g−6)" if LANG == "vi" else "2. Simple Geodesic Count: N(X, L) ~ c·L^(6g−6)", SKY),
            ("3. Dòng động đất & Cây đũa thần (cùng Eskin)" if LANG == "vi" else "3. Earthquake Flow & Magic Wand (with Eskin)", SUN),
        ]
        for i, (txt, col) in enumerate(l_data):
            y = 2.1 - i * 1.4
            b = RoundedRectangle(corner_radius=0.14, width=7.6, height=1.0, fill_color=CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5).move_to([0, y, 0])
            t = T(txt, 21, col).move_to([0, y, 0])
            leg.add(VGroup(b, t))
        self.play(FadeIn(leg, lag_ratio=0.25), run_time=1.4)
        end_vo("s5", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
