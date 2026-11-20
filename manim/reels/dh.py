from common_b import *

TX = {
    "title": {"vi": "Trao đổi khóa Diffie–Hellman", "en": "Diffie–Hellman key exchange"},
    "orb": {"vi": "5¹, 5², 5³, … (mod 23) nhảy lung tung", "en": "5¹, 5², 5³, … (mod 23) jump around"},
    "pub": {"vi": "Công khai: p = 23, g = 5", "en": "Public: p = 23, g = 5"},
    "al": {"vi": "An giữ bí mật a = 6 → gửi 5⁶ mod 23 = 8", "en": "Alice keeps a = 6 → sends 5⁶ mod 23 = 8"},
    "bo": {"vi": "Bình giữ bí mật b = 15 → gửi 5¹⁵ mod 23 = 19", "en": "Bob keeps b = 15 → sends 5¹⁵ mod 23 = 19"},
    "ka": {"vi": "An tính 19⁶ mod 23 = 2", "en": "Alice computes 19⁶ mod 23 = 2"},
    "kb": {"vi": "Bình tính 8¹⁵ mod 23 = 2", "en": "Bob computes 8¹⁵ mod 23 = 2"},
    "key": {"vi": "Cùng một khóa: 2", "en": "The same key: 2"},
    "eve": {"vi": "Kẻ nghe lén thấy 23, 5, 8, 19\nvà phải giải 5ˣ = 8 (log rời rạc)", "en": "An eavesdropper sees 23, 5, 8, 19\nand must solve 5ˣ = 8 (discrete log)"},
}
p, g, a, b = 23, 5, 6, 15
A, B = pow(g, a, p), pow(g, b, p)
assert (A, B) == (8, 19) and pow(B, a, p) == pow(A, b, p) == pow(g, a * b, p) == 2
orbit = [pow(g, k, p) for k in range(1, 23)]
assert sorted(orbit) == list(range(1, 23))        # 5 là căn nguyên thuỷ mod 23
assert orbit[a - 1] == 8 and orbit[b - 1] == 19 and orbit.index(8) + 1 == 6


class DH(Scene):
    def construct(self):
        self.add(line(TX["title"], 36, WHITE, 6.3))
        c = np.array([0, 2.6, 0]); R = 2.05
        pos = lambda r: c + R * np.array([math.sin(2 * math.pi * r / p), math.cos(2 * math.pi * r / p), 0])
        ring = VGroup(*[T(str(r), 18, DIM).move_to(c + (R + 0.42) * (pos(r) - c) / R) for r in range(0, 23)])
        base = VGroup(*[Dot(pos(r), radius=0.05, color=DIM) for r in range(0, 23)])
        o = line(TX["orb"], 28, WHITE, 5.75)
        self.play(FadeIn(ring), FadeIn(base), FadeIn(o), run_time=1.0)
        cols = color_gradient([SKY, MINT, SUN, PINK], 22)
        dots, segs = [], []
        for k in range(22):
            d = Dot(pos(orbit[k]), radius=0.11, color=cols[k])
            if k:
                s = Line(pos(orbit[k - 1]), pos(orbit[k]), color=cols[k], stroke_width=3, stroke_opacity=0.55)
                self.play(Create(s), FadeIn(d), run_time=0.14)
            else:
                self.play(FadeIn(d), run_time=0.14)
        self.wait(0.6)
        y = -0.35
        items = [("pub", WHITE), ("al", SKY), ("bo", PINK), ("ka", SKY), ("kb", PINK)]
        for key, col in items:
            m = line(TX[key], 27, col, y)
            self.play(FadeIn(m), run_time=0.6)
            self.wait(0.5)
            y -= 0.85
        k = line(TX["key"], 40, SUN, y - 0.1)
        self.play(FadeIn(k), run_time=0.7)
        e = line(TX["eve"], 28, ORANGE, y - 1.55)
        e.set_width(min(e.width, 7.8))
        self.play(FadeIn(e), run_time=0.7)
        self.wait(3.5)
