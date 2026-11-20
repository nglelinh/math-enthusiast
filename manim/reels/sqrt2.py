from common import *

TX = {
    "title": {"vi": "Vì sao √2 vô tỉ", "en": "Why √2 is irrational"},
    "assume": {"vi": "Giả sử a và b nguyên, nhỏ nhất, a² = 2b²", "en": "Suppose a, b are the smallest integers with a² = 2b²"},
    "big": {"vi": "Hình vuông cạnh a", "en": "Square of side a"},
    "two": {"vi": "Hai hình vuông cạnh b phủ kín nó", "en": "Two squares of side b cover it"},
    "same": {"vi": "Phần chồng = phần còn trống", "en": "Overlap = uncovered area"},
    "overlap": {"vi": "chồng", "en": "overlap"},
    "free": {"vi": "trống", "en": "gap"},
    "small": {"vi": "Cạnh nhỏ hơn: 2b − a và a − b, vẫn là số nguyên", "en": "Smaller sides 2b − a and a − b, still integers"},
    "contra": {"vi": "Vẫn đúng đẳng thức, nhưng b nhỏ hơn: mâu thuẫn!", "en": "Same equation with a smaller b: contradiction!"},
    "end": {"vi": "Vậy √2 không là phân số", "en": "So √2 is not a fraction"},
}
import math
A = 5.6
B = A / math.sqrt(2)
assert abs(A * A - 2 * B * B) < 1e-9
OV = 2 * B - A
GAP = A - B
assert abs(OV * OV - 2 * GAP * GAP) < 1e-9


class Sqrt2(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        top = fit(T(tr(TX["assume"]), 28, WHITE)).move_to([0, 5.3, 0])
        self.play(FadeIn(top), run_time=0.8)
        cx, cy = 0.0, 1.5
        L, Bt = cx - A / 2, cy - A / 2
        big = Square(A, color=WHITE, stroke_width=5).move_to([cx, cy, 0])
        lab_a = MathTex("a", color=WHITE, font_size=60).next_to(big, UP, buff=0.15)
        n1 = fit(T(tr(TX["big"]), 30, WHITE)).move_to([0, -2.6, 0])
        self.play(Create(big), FadeIn(lab_a), FadeIn(n1), run_time=1.2)
        self.wait(0.6)
        sq1 = Square(B, color=SKY, stroke_width=4, fill_color=SKY, fill_opacity=0.45).move_to([L + B / 2, Bt + B / 2, 0])
        sq2 = Square(B, color=PINK, stroke_width=4, fill_color=PINK, fill_opacity=0.45).move_to([L + A - B / 2, Bt + A - B / 2, 0])
        lb1 = MathTex("b", color=SKY, font_size=54).next_to(sq1, DOWN, buff=0.12).shift(LEFT * 0)
        lb1.move_to([L + B / 2, Bt - 0.4, 0])
        lb2 = MathTex("b", color=PINK, font_size=54).move_to([L + A + 0.4, Bt + A - B / 2, 0])
        n2 = fit(T(tr(TX["two"]), 30, SUN)).move_to([0, -2.6, 0])
        self.play(ReplacementTransform(n1, n2), run_time=0.4)
        self.play(FadeIn(sq1), FadeIn(lb1), run_time=1.0)
        self.play(FadeIn(sq2), FadeIn(lb2), run_time=1.0)
        self.wait(0.8)
        ov = Square(OV, color=MINT, stroke_width=4, fill_color=MINT, fill_opacity=0.8).move_to([L + A - B + OV / 2, Bt + A - B + OV / 2 - (A - B) + (A - B) - 0, 0])
        # vùng chồng: x in [L+A-B, L+B], y in [Bt+A-B, Bt+B]
        ov.move_to([(L + A - B + L + B) / 2, (Bt + A - B + Bt + B) / 2, 0])
        g1 = Square(GAP, color=ORANGE, stroke_width=4, fill_color=ORANGE, fill_opacity=0.8).move_to([L + A - GAP / 2, Bt + GAP / 2, 0])
        g2 = Square(GAP, color=ORANGE, stroke_width=4, fill_color=ORANGE, fill_opacity=0.8).move_to([L + GAP / 2, Bt + A - GAP / 2, 0])
        n3 = fit(T(tr(TX["same"]), 32, SUN)).move_to([0, -2.6, 0])
        self.play(ReplacementTransform(n2, n3), run_time=0.4)
        self.play(FadeIn(ov), run_time=0.8)
        self.play(FadeIn(g1), FadeIn(g2), run_time=0.8)
        t_ov = VGroup(MathTex("2b-a", color=BLACK, font_size=40).move_to(ov), MathTex("a-b", color=BLACK, font_size=40).move_to(g1), MathTex("a-b", color=BLACK, font_size=40).move_to(g2))
        self.play(FadeIn(t_ov), run_time=0.5)
        self.wait(0.8)
        eq = MathTex(r"(2b-a)^2=(a-b)^2+(a-b)^2", color=WHITE, font_size=46).move_to([0, -3.7, 0])
        self.play(Write(eq), run_time=1.6)
        self.wait(1.0)
        n4 = fit(T(tr(TX["small"]), 28, MINT)).move_to([0, -4.7, 0])
        self.play(FadeIn(n4), run_time=0.6)
        self.wait(1.5)
        n5 = fit(T(tr(TX["contra"]), 28, PINK)).move_to([0, -5.5, 0])
        self.play(FadeIn(n5), run_time=0.6)
        self.wait(2.0)
        end = fit(T(tr(TX["end"]), 40, SUN)).move_to([0, -6.2, 0])
        self.play(FadeIn(end), run_time=0.6)
        self.wait(3.0)
