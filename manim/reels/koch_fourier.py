"""Reel: vẽ bông tuyết Koch (bậc 4) bằng vòng tròn quay = chuỗi Fourier phức.
Render: REEL_LANG=vi|en manim -qh koch_fourier.py KochFourier   (math ở koch_math.py, lời đọc ở koch_vo.py)"""
from common import *
import json, os
from koch_math import (NS, M, C, FREQ, ORDER, REC, ERRP, Z, Vn, DENSE, recon, TIP, EDGE, LEVEL, T as TT)

TX = {
    "title": {"vi": "Vẽ bông tuyết Koch bằng vòng tròn quay", "en": "Drawing the Koch snowflake with spinning circles"},
    "sub": {"vi": "Koch bậc %d: %d cạnh" % (LEVEL, 3 * 4 ** LEVEL), "en": "Koch level %d: %d edges" % (LEVEL, 3 * 4 ** LEVEL)},
    "rad": {"vi": "|c(k)| = bán kính vòng tròn", "en": "|c(k)| = radius of the circle"},
    "rot": {"vi": "k = số vòng quay trong một chu kỳ", "en": "k = turns per period"},
    "fft1": {"vi": "%d điểm cách đều theo độ dài cung" % M, "en": "%d points evenly spaced along the boundary" % M},
    "fft2": {"vi": "FFT cho các hệ số c(k)", "en": "FFT gives the coefficients c(k)"},
    "fft3": {"vi": "Giữ N hệ số có |c(k)| lớn nhất", "en": "Keep the N coefficients with largest |c(k)|"},
    "circ": {"vi": "vòng tròn", "en": "circles"},
    "err": {"vi": "Sai số", "en": "Error"},
    "def1": {"vi": "Sai số = khoảng cách trung bình giữa hai đường", "en": "Error = mean distance between the two curves"},
    "def2": {"vi": "(tính hai chiều) ÷ bán kính trung bình của hình", "en": "(both directions) ÷ mean radius of the shape"},
    "zoom": {"vi": "Phóng to khoảng %d lần quanh một đỉnh nhọn", "en": "Zoomed in about %dx around one tip"},
    "zoom2": {"vi": "Ít vòng: góc bị bo tròn. Nhiều vòng: sát hơn, vẫn trơn.", "en": "Few circles: the corner is rounded. Many: closer, still smooth."},
    "zoom3": {"vi": "Quanh góc còn gợn rất nhỏ (kiểu hiệu ứng Gibbs)", "en": "Tiny ripples remain near the corner (Gibbs-like)"},
    "kochl": {"vi": "đa giác Koch", "en": "Koch polygon"},
    "cav1": {"vi": "Dựng lại được đa giác Koch bậc %d," % LEVEL, "en": "We rebuild the level-%d Koch polygon," % LEVEL},
    "cav2": {"vi": "không phải fractal thật (cần vô hạn bậc)", "en": "not the true fractal (it needs infinite levels)"},
    "end": {"vi": "Mỗi vòng tròn = một hệ số Fourier = một tần số", "en": "Each circle = one Fourier coefficient = one frequency"},
    "tab": {"vi": "N vòng → sai số", "en": "N circles → error"},
}
VO_KEYS = ["intro", "formula", "fft", "n1", "n5", "n20", "n100", "n500", "zoom", "caveat", "outro"]
WORDS_PS = 2.4   # tốc độ đọc ước lượng khi không có giọng (bản en)
VO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo", "koch")

CX, CY, S = 0.0, 2.15, 2.7
ZW = 0.07                                  # cửa sổ phóng to (đơn vị dữ liệu)
INS_W, INS_H, INS_CY = 5.2, 3.6, -2.5
ZH = ZW * INS_H / INS_W
ZF = INS_W / ZW / S
assert 25 < ZF < 30, ZF


def pct(x):
    s = "%.2f%%" % x
    return s.replace(".", ",") if LANG == "vi" else s


def mp(z):
    z = np.asarray(z)
    return np.c_[CX + S * z.real, CY + S * z.imag, np.zeros(z.shape)]


def polyline(pts3, color, w, closed=False):
    m = VMobject(stroke_color=color, stroke_width=w)
    P = pts3 if not closed else np.vstack([pts3, pts3[:1]])
    m.set_points_as_corners(P)
    return m


class KochFourier(Scene):
    def setup(self):
        self.durs = {}
        p = os.path.join(VO_DIR, "durations.json")
        if LANG == "vi" and os.path.exists(p):
            self.durs = json.load(open(p))
        self.starts = {}
        import koch_vo
        self.vo_text = koch_vo.VO

    def beat(self, key):
        """Bắt đầu lời đọc `key` tại thời điểm hiện tại; trả về hạn kết thúc."""
        self.starts[key] = float(self.time)
        d = self.durs.get(key) or len(self.vo_text[key].split()) / WORDS_PS
        return self.time + d + 0.5

    def hold(self, until):
        if until > self.time:
            self.wait(until - self.time)

    # --- các khối vẽ ---
    def chain(self, n, alpha, shown=12):
        idx = ORDER[:n]
        cs = C[idx] * np.exp(2j * np.pi * FREQ[idx] * alpha)
        pos = np.concatenate([[0], np.cumsum(cs[:shown])])
        g = VGroup()
        for i in range(min(shown, n)):
            r = S * abs(C[idx[i]])
            if r > 0.03:
                g.add(Circle(radius=r, stroke_color=MINT, stroke_width=2, stroke_opacity=0.55).move_to(mp(pos[i])[0]))
            g.add(Line(mp(pos[i])[0], mp(pos[i + 1])[0], stroke_color=WHITE, stroke_width=3))
        tip = REC[n][min(int(alpha * M), M - 1)] if n in REC else cs.sum()
        if n not in REC:
            tip = cs.sum()
        g.add(Dot(mp(tip)[0], radius=0.09, color=SUN))
        return g

    def draw_stage(self, n, rt):
        a = ValueTracker(0)
        trace = always_redraw(lambda: polyline(mp(REC[n][: max(2, int(a.get_value() * M) + 1)]), SKY, 5))
        ch = always_redraw(lambda: self.chain(n, a.get_value()))
        self.add(trace, ch)
        self.play(a.animate.set_value(1 - 1.0 / M), run_time=rt, rate_func=linear)
        full = polyline(mp(np.append(REC[n], REC[n][0])), SKY, 5)
        self.remove(trace, ch)
        self.add(full)
        return full

    def construct(self):
        title = cap(TX["title"], 34)
        sub = fit(T(tr(TX["sub"]), 26, DIM)).move_to([0, 5.7, 0])
        poly = polyline(mp(Vn), DIM, 2.5, closed=True)
        # --- 1. giới thiệu ---
        until = self.beat("intro")
        self.play(FadeIn(title), run_time=0.8)
        self.play(Create(poly), FadeIn(sub), run_time=3.5)
        self.hold(until)

        # --- 2. công thức + vòng tròn ---
        until = self.beat("formula")
        fa = T("zN(t) = c(0) + Σ c(k) · e", 38, SUN)
        fb = T("2πikt", 24, SUN).next_to(fa, RIGHT, buff=0.04).shift(UP * 0.17)
        f = VGroup(fa, fb).move_to([0, -1.7, 0])
        l1 = fit(T(tr(TX["rad"]), 28, MINT)).move_to([0, -2.8, 0])
        l2 = fit(T(tr(TX["rot"]), 28, SKY)).move_to([0, -3.5, 0])
        self.play(FadeIn(f), run_time=1.2)
        self.play(FadeIn(l1), run_time=0.6)
        self.play(FadeIn(l2), run_time=0.6)
        a = ValueTracker(0.0)
        demo = always_redraw(lambda: self.chain(3, a.get_value(), shown=3))
        self.add(demo)
        left = max(until - self.time, 3.0)
        self.play(a.animate.set_value(0.12), run_time=left, rate_func=linear)
        self.remove(demo)

        # --- 3. lấy mẫu + FFT ---
        until = self.beat("fft")
        dots = VGroup(*[Dot(p, radius=0.045, color=SUN) for p in mp(Z[::64])])
        f1 = fit(T(tr(TX["fft1"]), 28, SUN)).move_to([0, -2.8, 0])
        f2 = fit(T(tr(TX["fft2"]), 28, MINT)).move_to([0, -3.5, 0])
        f3 = fit(T(tr(TX["fft3"]), 28, SKY)).move_to([0, -4.2, 0])
        self.play(FadeOut(l1), FadeOut(l2), FadeIn(dots, lag_ratio=0.02), run_time=1.5)
        self.play(FadeIn(f1), run_time=0.5)
        self.play(FadeIn(f2), run_time=0.5)
        self.play(FadeIn(f3), run_time=0.5)
        self.hold(until)
        self.play(FadeOut(dots), FadeOut(f1), FadeOut(f2), FadeOut(f3), run_time=0.6)

        # --- 4. các giai đoạn N ---
        hist = []
        nlab = None
        defs = None
        hist_m = None
        prev = None
        for n in NS:
            until = self.beat("n%d" % n)
            new_lab = T("N = %d %s" % (n, tr(TX["circ"])), 40, SUN).move_to([0, -2.6, 0])
            if nlab is None:
                self.play(FadeIn(new_lab), run_time=0.4)
            else:
                self.play(Transform(nlab, new_lab), FadeOut(err_m), run_time=0.5)
                new_lab = nlab
            nlab = new_lab
            if prev is not None:
                self.remove(prev)
            rt = {1: 4.5, 5: 5.5, 20: 6.5, 100: 7.5, 500: 8.5}[n]
            prev = self.draw_stage(n, rt)
            err_m = T("%s: %s" % (tr(TX["err"]), pct(ERRP[n])), 34, MINT).move_to([0, -3.5, 0])
            self.play(FadeIn(err_m), run_time=0.5)
            if defs is None:
                defs = VGroup(fit(T(tr(TX["def1"]), 24, "#c9cdd8")).move_to([0, -4.4, 0]),
                              fit(T(tr(TX["def2"]), 24, "#c9cdd8")).move_to([0, -4.95, 0]))
                self.play(FadeIn(defs), run_time=0.5)
            hist.append("%d: %s" % (n, pct(ERRP[n])))
            nh = fit(T("  ·  ".join(hist), 24, DIM)).move_to([0, -5.9, 0])
            if hist_m is None:
                self.play(FadeIn(nh), run_time=0.4)
            else:
                self.play(Transform(hist_m, nh), run_time=0.4)
                nh = hist_m
            hist_m = nh
            self.hold(until)

        # --- 5. phóng to đỉnh nhọn ---
        until = self.beat("zoom")
        self.play(FadeOut(nlab), FadeOut(err_m), FadeOut(defs), FadeOut(hist_m), FadeOut(f), run_time=0.6)
        win_c = complex(TIP.real, TIP.imag - ZH * 0.25)
        box = Rectangle(width=ZW * S, height=ZH * S, stroke_color=ORANGE, stroke_width=3).move_to(mp([win_c])[0])
        x0, x1 = win_c.real - ZW / 2, win_c.real + ZW / 2
        y0, y1 = win_c.imag - ZH / 2, win_c.imag + ZH / 2
        tt = np.linspace(-0.004, 0.004, 8000)
        zp = DENSE

        def to_ins(z):
            return np.c_[(z.real - win_c.real) * INS_W / ZW, INS_CY + (z.imag - win_c.imag) * INS_W / ZW, np.zeros(len(z))]

        def runs(z, color, w):
            m = (z.real > x0) & (z.real < x1) & (z.imag > y0) & (z.imag < y1)
            g = VGroup()
            i = 0
            while i < len(z):
                if m[i]:
                    j = i
                    while j + 1 < len(z) and m[j + 1]:
                        j += 1
                    if j > i:
                        g.add(polyline(to_ins(z[i:j + 1]), color, w))
                    i = j + 1
                else:
                    i += 1
            return g

        frame = Rectangle(width=INS_W, height=INS_H, stroke_color=ORANGE, stroke_width=3).move_to([0, INS_CY, 0])
        assert abs(INS_W * ZH / ZW - INS_H) < 1e-6
        cols = [(20, PINK), (100, MINT), (500, SKY)]
        pg = runs(zp, "#e6e8ef", 5)
        cgs = [runs(recon(n, tt), c, 4) for n, c in cols]
        ly = INS_CY - INS_H / 2 - 0.4
        leg = VGroup(T(tr(TX["kochl"]), 22, "#e6e8ef"), *[T("N=%d" % n, 22, c) for n, c in cols])
        leg.arrange(RIGHT, buff=0.45).move_to([0, ly, 0])
        zt = fit(T(tr(TX["zoom"]) % round(ZF), 26, ORANGE)).move_to([0, ly - 0.55, 0])
        self.play(Create(box), run_time=0.6)
        self.play(FadeIn(frame), FadeIn(pg), FadeIn(zt), FadeIn(leg), run_time=0.8)
        for cg in cgs:
            self.play(Create(cg), run_time=1.8)
        z2 = fit(T(tr(TX["zoom2"]), 24, WHITE)).move_to([0, ly - 1.1, 0])
        z3 = fit(T(tr(TX["zoom3"]), 24, DIM)).move_to([0, ly - 1.6, 0])
        self.play(FadeIn(z2), FadeIn(z3), run_time=0.6)
        self.hold(until)

        # --- 6. lưu ý trung thực ---
        until = self.beat("caveat")
        self.play(FadeOut(frame), FadeOut(pg), *[FadeOut(c) for c in cgs], FadeOut(leg), FadeOut(zt), FadeOut(z2), FadeOut(z3), FadeOut(box), run_time=0.6)
        c1 = fit(T(tr(TX["cav1"]), 30, WHITE)).move_to([0, -1.8, 0])
        c2 = fit(T(tr(TX["cav2"]), 30, ORANGE)).move_to([0, -2.5, 0])
        self.play(FadeIn(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.6)
        self.hold(until)

        # --- 7. tổng kết ---
        until = self.beat("outro")
        e = fit(T(tr(TX["end"]), 30, MINT)).move_to([0, -3.7, 0])
        self.play(FadeIn(e), run_time=0.6)
        tb = VGroup(fit(T(tr(TX["tab"]), 26, DIM)).move_to([0, -4.6, 0]))
        for i, n in enumerate(NS):
            tb.add(T("N=%d" % n, 26, SUN).move_to([-3.2 + 1.6 * i, -5.25, 0]))
            tb.add(T(pct(ERRP[n]), 26, MINT).move_to([-3.2 + 1.6 * i, -5.8, 0]))
        self.play(FadeIn(tb), run_time=0.6)
        self.hold(until)
        self.wait(1.0)
        json.dump(self.starts, open(os.path.join(VO_DIR, "starts_%s.json" % LANG), "w"))
