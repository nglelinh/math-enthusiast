"""Reel: hàm Gamma, giai thừa cho số thực/phức (Euler 1729 -> zeta -> thể tích quả cầu).
Render: REEL_LANG=vi|en manim -qh gamma_reel.py GammaReel  (toán: gamma_math.py, lời đọc: gamma_vo.py)
Chỉ dùng Text (Unicode), không cần LaTeX."""
from common import *
import json, os
import numpy as np
from scipy import special as sp
from PIL import Image
import gamma_math as gm
from gamma_math import G, V, XI_REAL, FACT, A as ALT_A, f_alt

TX = {
    "title": {"vi": "Hàm Gamma Γ(z)", "en": "The Gamma function Γ(z)"},
    "t1": {"vi": "Giai thừa chỉ có ở số nguyên", "en": "Factorials only exist for integers"},
    "t1b": {"vi": "Điểm (n+1, n!) nằm trên đồ thị y = Γ(x)", "en": "The point (n+1, n!) lies on the graph y = Γ(x)"},
    "euler": {"vi": "Euler, 1729: thư gửi Goldbach", "en": "Euler, 1729: letters to Goldbach"},
    "euler2": {"vi": "Một đường cong trơn đi qua mọi điểm", "en": "One smooth curve through every point"},
    "i_cap": {"vi": "Định nghĩa bằng tích phân", "en": "Defined by an integral"},
    "i_fn": {"vi": "z = 4: hàm dưới dấu tích phân t^(z−1) · e^(−t)", "en": "z = 4: the integrand t^(z−1) · e^(−t)"},
    "i_area": {"vi": "diện tích = 6 = 3!", "en": "area = 6 = 3!"},
    "i_rec": {"vi": "Γ(4) = 3 · Γ(3) = 3 · 2 = 6", "en": "Γ(4) = 3 · Γ(3) = 3 · 2 = 6"},
    "p_cap": {"vi": "Mở rộng sang x âm", "en": "Extending to negative x"},
    "p_rule": {"vi": "Γ(x) = Γ(x+1) ÷ x  ⇒  chia cho 0 tại x = 0", "en": "Γ(x) = Γ(x+1) ÷ x  ⇒  division by 0 at x = 0"},
    "p_poles": {"vi": "Cực tại x = 0, −1, −2, −3, …", "en": "Poles at x = 0, −1, −2, −3, …"},
    "p_sign": {"vi": "Giữa hai cực liên tiếp, Γ đổi dấu", "en": "Between consecutive poles, Γ changes sign"},
    "b_cap": {"vi": "Bohr–Mollerup: vì sao chỉ có một đường?", "en": "Bohr–Mollerup: why only one curve?"},
    "b_g": {"vi": "log Γ(x): lồi", "en": "log Γ(x): convex"},
    "b_f": {"vi": "log f(x): gợn sóng, không lồi", "en": "log f(x): wavy, not convex"},
    "b_rule": {"vi": "Cả hai: f(1) = 1 và f(x+1) = x · f(x)", "en": "Both: f(1) = 1 and f(x+1) = x · f(x)"},
    "b_f2": {"vi": "f(x) = Γ(x) · (1 + 0,3 · sin 2πx)", "en": "f(x) = Γ(x) · (1 + 0.3 · sin 2πx)"},
    "b_thm": {"vi": "f > 0, log f lồi ⇒ f = Γ", "en": "f > 0 and log f convex ⇒ f = Γ"},
    "h_cap": {"vi": "Giá trị đặc biệt: Γ(1/2)", "en": "A special value: Γ(1/2)"},
    "h_val": {"vi": "Γ(1/2) = √π ≈ 1,7725", "en": "Γ(1/2) = √π ≈ 1.7725"},
    "h_sub": {"vi": "đặt t = u²:  ∫ e^(−u²) du trên cả trục thực", "en": "put t = u²:  ∫ e^(−u²) du over the whole line"},
    "h_fact": {"vi": "(−1/2)! = Γ(1/2) = √π", "en": "(−1/2)! = Γ(1/2) = √π"},
    "n_cap": {"vi": "Γ không bao giờ bằng 0", "en": "Γ is never zero"},
    "n_refl": {"vi": "Γ(z) Γ(1−z) = π ÷ sin(πz)", "en": "Γ(z) Γ(1−z) = π ÷ sin(πz)"},
    "n_why": {"vi": "Vế phải ≠ 0 ⇒ Γ không có không điểm", "en": "Right side ≠ 0 ⇒ Γ has no zeros"},
    "n_img": {"vi": "Màu = góc của Γ(z), độ sáng = cỡ |Γ(z)|", "en": "Colour = angle of Γ(z), brightness = size of |Γ(z)|"},
    "n_pole": {"vi": "vòng cam = cực", "en": "orange rings = poles"},
    "z_cap": {"vi": "Γ nằm trong hàm zeta", "en": "Γ sits inside the zeta function"},
    "z_g": {"vi": "Γ(s/2): cực tại 0, −2, −4, −6", "en": "Γ(s/2): poles at 0, −2, −4, −6"},
    "z_z": {"vi": "ζ(s): bằng 0 tại −2, −4, −6", "en": "ζ(s): equals 0 at −2, −4, −6"},
    "z_ent": {"vi": "ξ là hàm nguyên: cực và không điểm triệt tiêu nhau", "en": "ξ is entire: poles and zeros cancel"},
    "z_triv": {"vi": "Không điểm tầm thường của ζ: −2, −4, −6, …", "en": "Trivial zeros of ζ: −2, −4, −6, …"},
    "z_xi": {"vi": "ξ(s) đối xứng qua s = 1/2", "en": "ξ(s) is symmetric about s = 1/2"},
    "z_pt": {"vi": "ξ(3) = ξ(−2) ≈ 0,5739", "en": "ξ(3) = ξ(−2) ≈ 0.5739"},
    "v_cap": {"vi": "Thể tích quả cầu đơn vị trong n chiều", "en": "Volume of the unit ball in n dimensions"},
    "v_peak": {"vi": "n = 5:  V = 8π²/15 ≈ 5,2638", "en": "n = 5:  V = 8π²/15 ≈ 5.2638"},
    "v_note": {"vi": "Lớn nhất trong các chiều nguyên", "en": "Largest among integer dimensions"},
    "v_note2": {"vi": "(đường liền: đỉnh thực ≈ 5,2777 tại n ≈ 5,257)", "en": "(smooth curve: true peak ≈ 5.2777 at n ≈ 5.257)"},
    "v_n": {"vi": "số chiều n", "en": "dimension n"},
    "o_cap": {"vi": "Một đường cong, nhiều bất ngờ", "en": "One curve, many surprises"},
    "o1": {"vi": "n! → Γ(z): giai thừa cho mọi số", "en": "n! → Γ(z): factorial for every number"},
    "o2": {"vi": "Γ(1/2) = √π: số π trong giai thừa", "en": "Γ(1/2) = √π: π inside factorials"},
    "o3": {"vi": "Γ(z)Γ(1−z) = π ÷ sin πz: không có không điểm", "en": "Γ(z)Γ(1−z) = π ÷ sin πz: no zeros"},
    "o4": {"vi": "Cực của Γ(s/2) = không điểm tầm thường của ζ", "en": "Poles of Γ(s/2) = trivial zeros of ζ"},
    "o5": {"vi": "V(n) = π^(n/2) ÷ Γ(n/2 + 1)", "en": "V(n) = π^(n/2) ÷ Γ(n/2 + 1)"},
}
VO_KEYS = ["intro", "integral", "poles", "bm", "half", "nozero", "zeta", "ball", "outro"]
WORDS_PS = 2.4
VO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo", "gamma")
LIGHT = "#c9cdd8"


def dec(s):
    return s  # số thập phân đã viết sẵn theo từng ngôn ngữ trong TX


def fm(items, size=36, color=SUN):
    """Công thức một dòng: str | (str,'sup'|'sub'|'subs'[,màu]) | (str,'n',màu). 'subs' = chỉ số dưới xếp chồng ngay dưới số mũ trước."""
    g = VGroup()
    x = 0.0
    last_x = 0.0
    for it in items:
        txt, kind, col = (it, "n", color) if isinstance(it, str) else (it[0], it[1], it[2] if len(it) > 2 else color)
        sz = size if kind == "n" else size * 0.58
        dy = {"n": 0, "sup": size * 0.0050, "sub": -size * 0.0042, "subs": -size * 0.0042}[kind]
        m = T(txt, sz, col)
        pad = 0.16 if (kind == "n" and txt in ("=", "·", "÷")) else 0.0
        if kind == "subs":
            m.move_to([last_x + m.width / 2, dy, 0])
            x = max(x, last_x + m.width + 0.07)
        else:
            x += pad
            last_x = x
            m.move_to([x + m.width / 2, dy, 0])
            x += m.width + 0.07 + pad
        g.add(m)
    return g.move_to(ORIGIN)


def mapper(ax):
    o = ax.c2p(0, 0)
    ux = ax.c2p(1, 0) - o
    uy = ax.c2p(0, 1) - o
    return lambda xs, ys: o[None, :] + np.outer(xs, ux) + np.outer(ys, uy)


def line_pts(ax, f, x0, x1, color, w=4, n=1200, ylim=None, vec=True):
    mp_ = mapper(ax)
    xs = np.linspace(x0, x1, n)
    ys = f(xs) if vec else np.array([f(x) for x in xs])
    ok = np.isfinite(ys)
    if ylim is not None:
        ok &= (ys > ylim[0]) & (ys < ylim[1])
    g = VGroup()
    i = 0
    while i < n:
        if ok[i]:
            j = i
            while j + 1 < n and ok[j + 1]:
                j += 1
            if j > i:
                m = VMobject(stroke_color=color, stroke_width=w)
                m.set_points_as_corners(mp_(xs[i:j + 1], ys[i:j + 1]))
                g.add(m)
            i = j + 1
        else:
            i += 1
    return g


def mk_axes(xr, yr, w, h, cx, cy, xstep=1, ystep=5):
    ax = Axes(x_range=[xr[0], xr[1], xstep], y_range=[yr[0], yr[1], ystep], x_length=w, y_length=h,
              axis_config={"color": DIM, "stroke_width": 2.5, "include_ticks": False, "include_tip": False}, tips=False)
    return ax.move_to([cx, cy, 0])


def tick_labels(ax, vals, dy=-0.2, size=20, fmt=lambda v: str(v).replace("-", "−"), color=DIM, y0=0):
    return VGroup(*[T(fmt(v), size, color).move_to(ax.c2p(v, y0) + np.array([0, dy, 0])) for v in vals])


def domain_img(w=1520, h=1013, xr=(-4.5, 4.5), yr=(-3.0, 3.0)):
    x = np.linspace(xr[0], xr[1], w)
    y = np.linspace(yr[1], yr[0], h)
    Zc = x[None, :] + 1j * y[:, None]
    with np.errstate(all="ignore"):
        Gv = sp.gamma(Zc)
    hue = (np.angle(Gv) / (2 * np.pi)) % 1.0
    with np.errstate(all="ignore"):
        band = np.log2(np.abs(Gv)) % 1.0
    band = np.where(np.isfinite(band), band, 1.0)
    val = 0.40 + 0.60 * band
    sat = np.full_like(val, 0.80)
    hsv = np.stack([hue * 255, sat * 255, val * 255], axis=-1)
    hsv = np.nan_to_num(hsv).astype(np.uint8)
    return np.array(Image.fromarray(hsv, "HSV").convert("RGB"))


class GammaReel(Scene):
    def setup(self):
        self.durs = {}
        p = os.path.join(VO_DIR, "durations.json")
        if LANG == "vi" and os.path.exists(p):
            self.durs = json.load(open(p))
        self.starts = {}
        import gamma_vo
        self.vo_text = gamma_vo.VO

    def beat(self, key):
        self.starts[key] = float(self.time)
        d = self.durs.get(key) or len(self.vo_text[key].split()) / WORDS_PS
        return self.time + d + 0.5

    def hold(self, until):
        if until > self.time:
            self.wait(until - self.time)

    def L(self, key, size, color, y, w=7.8):
        return fit(T(tr(TX[key]), size, color), w).move_to([0, y, 0])

    def construct(self):
        title = cap(TX["title"], 38)
        self.add(title)

        # ============ 1. giai thừa + Euler ============
        until = self.beat("intro")
        ax = mk_axes((-4.5, 5.5), (-6, 26), 7.6, 4.6, 0, 2.4)
        xl = VGroup(*[T(str(v).replace('-', '−'), 20, DIM).move_to(ax.c2p(v, -6) + np.array([0, -0.22, 0])) for v in [-4, -3, -2, -1, 1, 2, 3, 4, 5]])
        s1 = self.L("t1", 28, WHITE, 5.55)
        self.play(Create(ax), FadeIn(xl), FadeIn(s1), run_time=1.2)
        pts = VGroup()
        lab_y = {0: 8, 1: 12.5, 2: 17}
        for n, (x, y) in enumerate(FACT):
            d = Dot(ax.c2p(x, y), radius=0.11, color=SUN)
            if n in lab_y:
                lab = T("%d! = %d" % (n, y), 22, SUN).move_to(ax.c2p(x, lab_y[n]))
                ld = DashedLine(ax.c2p(x, lab_y[n] - 1.8), ax.c2p(x, y + 0.5), color=SUN, stroke_width=1.5, dash_length=0.08, stroke_opacity=0.6)
                pts.add(VGroup(d, lab, ld))
            else:
                lab = T("%d! = %d" % (n, y), 24, SUN).next_to(d, LEFT, buff=0.15)
                pts.add(VGroup(d, lab))
        for p_ in pts:
            self.play(FadeIn(p_, scale=1.4), run_time=0.45)
        q = T("(1/2)! = ?", 30, ORANGE).move_to(ax.c2p(-2.2, 15))
        qa = Arrow(ax.c2p(-1.1, 14), ax.c2p(1.35, 2.0), color=ORANGE, stroke_width=3, buff=0.0, max_tip_length_to_length_ratio=0.12)
        self.play(FadeIn(q), Create(qa), run_time=0.6)
        s1b = self.L("t1b", 24, LIGHT, -0.9)
        self.play(FadeIn(s1b), run_time=0.6)
        self.hold(until - 9.0)
        e1 = self.L("euler", 32, ORANGE, -2.2)
        e2 = self.L("euler2", 28, WHITE, -2.9)
        self.play(FadeIn(e1), run_time=0.6)
        curve_pos = line_pts(ax, lambda x: sp.gamma(x), 0.06, 5.05, SKY, 5, ylim=(-6, 26))
        self.play(FadeOut(q), FadeOut(qa), Create(curve_pos, lag_ratio=1.0), FadeIn(e2), run_time=3.0)
        glab = T("Γ(x)", 36, SKY).move_to(ax.c2p(4.35, 16))
        self.play(FadeIn(glab), run_time=0.5)
        self.hold(until)
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(s1b), run_time=0.5)

        # ============ 2. tích phân Euler + hệ thức ============
        until = self.beat("integral")
        s2 = self.L("i_cap", 28, WHITE, 5.55)
        self.play(ReplacementTransform(s1, s2), run_time=0.4)
        fi = fm(["Γ(z)", "=", "∫", ("∞", "sup"), ("0", "subs"), "t", ("z−1", "sup"), "e", ("−t", "sup"), "dt"], 40, SUN)
        fi.move_to([0, -0.75, 0])
        # ∫ với cận: đặt ∞ trên, 0 dưới
        self.play(FadeIn(fi), run_time=0.8)
        ax2 = mk_axes((0, 14), (0, 1.6), 7.0, 2.0, 0, -2.5, xstep=2, ystep=0.4)
        f4 = lambda t: t ** (gm.Z_INT - 1) * np.exp(-t)
        g4 = ax2.plot(f4, x_range=[0, 14, 0.05], color=SKY, stroke_width=5)
        area = ax2.get_area(g4, x_range=(0, 14), color=SKY, opacity=0.35)
        l2 = self.L("i_fn", 24, LIGHT, -1.25)
        t2 = tick_labels(ax2, [0, 4, 8, 12], dy=-0.2)
        self.play(Create(ax2), FadeIn(l2), FadeIn(t2), run_time=0.8)
        self.play(Create(g4), run_time=1.5)
        self.play(FadeIn(area), run_time=0.8)
        ar = fit(T(tr(TX["i_area"]), 28, MINT), 3.2).move_to(ax2.c2p(10.2, 0.85))
        ring = Circle(radius=0.2, color=MINT, stroke_width=4).move_to(ax.c2p(4, G(4)))
        self.play(FadeIn(ar), Create(ring), run_time=0.8)
        self.hold(until - 8.5)
        fr = fm(["Γ(x+1)", "=", "x", "·", "Γ(x)"], 42, ORANGE).move_to([0, -4.85, 0])
        self.play(FadeIn(fr), run_time=0.8)
        rr = self.L("i_rec", 28, LIGHT, -5.65)
        self.play(FadeIn(rr), run_time=0.6)
        self.hold(until)

        # ============ 3. cực ============
        until = self.beat("poles")
        s3 = self.L("p_cap", 28, WHITE, 5.55)
        self.play(FadeOut(VGroup(fi, ax2, g4, area, l2, t2, ar, rr, fr, ring)), ReplacementTransform(s2, s3), run_time=0.6)
        rule = self.L("p_rule", 30, ORANGE, -0.9)
        self.play(FadeIn(rule), run_time=0.6)
        mp_ = mapper(ax)
        vlines = VGroup()
        for n in range(0, 5):
            p0 = ax.c2p(-n, -6); p1 = ax.c2p(-n, 26)
            vlines.add(DashedLine(p0, p1, color=ORANGE, stroke_width=2, dash_length=0.12, stroke_opacity=0.7))
        segs = VGroup()
        for n in range(4):
            segs.add(line_pts(ax, lambda x: sp.gamma(x), -n - 1 + 0.0008, -n - 0.0008, SKY, 5, n=1500, ylim=(-6, 26)))
        self.play(Create(vlines, lag_ratio=0.15), run_time=1.8)
        for s_ in segs:
            self.play(Create(s_, lag_ratio=1.0), run_time=1.5)
        pl = self.L("p_poles", 32, ORANGE, -2.3)
        sg = self.L("p_sign", 28, WHITE, -3.1)
        self.play(FadeIn(pl), run_time=0.5)
        self.play(FadeIn(sg), run_time=0.5)
        self.hold(until)

        # ============ 4. Bohr–Mollerup ============
        until = self.beat("bm")
        s4 = self.L("b_cap", 28, WHITE, 5.55)
        self.play(FadeOut(VGroup(ax, xl, pts, glab, curve_pos, vlines, segs, rule, pl, sg)), ReplacementTransform(s3, s4), run_time=0.7)
        axb = mk_axes((0.5, 5.5), (-0.8, 3.9), 7.4, 4.6, 0, 2.4, xstep=1, ystep=1)
        xlb = tick_labels(axb, [1, 2, 3, 4, 5], dy=-0.2)
        lg = lambda x: np.log(sp.gamma(x))
        lf = lambda x: np.log(sp.gamma(x) * (1 + ALT_A * np.sin(2 * np.pi * x)))
        # trục x tại y = 0 nằm trong khung; đặt nhãn ngay dưới đường y = 0
        cg = line_pts(axb, lg, 0.5, 5.5, SKY, 6)
        cf = line_pts(axb, lf, 0.5, 5.5, PINK, 5)
        dots = VGroup(*[Dot(axb.c2p(x, np.log(y)), radius=0.11, color=SUN) for x, y in FACT])
        self.play(Create(axb), FadeIn(xlb), run_time=0.8)
        self.play(FadeIn(dots), Create(cg), run_time=2.0)
        tg = fit(T(tr(TX["b_g"]), 26, SKY), 3.6).move_to(axb.c2p(4.2, 0.55))
        self.play(FadeIn(tg), run_time=0.5)
        self.play(Create(cf), run_time=2.5)
        tf = fit(T(tr(TX["b_f"]), 24, PINK), 4.6).move_to(axb.c2p(2.35, 3.5))
        self.play(FadeIn(tf), run_time=0.5)
        br = self.L("b_rule", 28, WHITE, -0.9)
        bf = self.L("b_f2", 28, PINK, -1.7)
        self.play(FadeIn(br), run_time=0.5)
        self.play(FadeIn(bf), run_time=0.5)
        self.hold(until - 6.0)
        bt = self.L("b_thm", 38, MINT, -3.1)
        self.play(FadeIn(bt), run_time=0.8)
        self.hold(until)

        # ============ 5. Γ(1/2) = √π ============
        until = self.beat("half")
        s5 = self.L("h_cap", 28, WHITE, 5.55)
        self.play(FadeOut(VGroup(axb, xlb, cg, cf, dots, tg, tf, br, bf, bt)), ReplacementTransform(s4, s5), run_time=0.7)
        axh = mk_axes((0, 4), (0, 4), 6.6, 3.2, 0, 3.6, xstep=1, ystep=1)
        xlh = tick_labels(axh, [1, 2, 3, 4], dy=-0.2)
        ch = line_pts(axh, lambda x: sp.gamma(x), 0.2, 4.0, SKY, 5, ylim=(0, 4))
        sq = gm.SQRTPI
        dh = Dot(axh.c2p(0.5, sq), radius=0.12, color=SUN)
        hl = DashedLine(axh.c2p(0, sq), axh.c2p(0.5, sq), color=SUN, stroke_width=3)
        vl = DashedLine(axh.c2p(0.5, 0), axh.c2p(0.5, sq), color=SUN, stroke_width=3)
        hv = self.L("h_val", 34, SUN, 1.2)
        self.play(Create(axh), FadeIn(xlh), run_time=0.7)
        self.play(Create(ch), run_time=1.5)
        self.play(FadeIn(dh), Create(hl), Create(vl), FadeIn(hv), run_time=1.0)
        # Gauss: diện tích dưới e^(-u^2) = sqrt(pi)
        axg = mk_axes((-3, 3), (0, 1.15), 6.0, 1.9, 0, -2.0, xstep=1, ystep=0.5)
        gg = axg.plot(lambda u: np.exp(-u * u), x_range=[-3, 3, 0.02], color=MINT, stroke_width=5)
        ga = axg.get_area(gg, x_range=(-3, 3), color=MINT, opacity=0.35)
        hs = self.L("h_sub", 24, LIGHT, -0.55)
        self.play(FadeIn(hs), Create(axg), run_time=0.7)
        self.play(Create(gg), FadeIn(ga), run_time=1.5)
        self.hold(until - 6.0)
        hf = self.L("h_fact", 38, ORANGE, -4.1)
        self.play(FadeIn(hf), run_time=0.8)
        self.hold(until)

        # ============ 6. không có không điểm ============
        until = self.beat("nozero")
        s6 = self.L("n_cap", 28, WHITE, 5.55)
        self.play(FadeOut(VGroup(axh, xlh, ch, dh, hl, vl, hv, axg, gg, ga, hs, hf)), ReplacementTransform(s5, s6), run_time=0.7)
        W, H = 7.6, 7.6 * 6 / 9
        arr = domain_img()
        img = ImageMobject(arr).set_width(W).move_to([0, 2.15, 0])
        bx = Rectangle(width=W, height=H, stroke_color=DIM, stroke_width=2).move_to(img.get_center())
        def d2p(x, y):
            return img.get_center() + np.array([x / 9 * W, y / 6 * H, 0])
        xl6 = VGroup(*[T(str(v).replace("-", "−"), 20, WHITE).move_to(d2p(v, -3.0) + np.array([0, -0.22, 0])) for v in range(-4, 5)])
        rings = VGroup(*[Circle(radius=0.13, color=ORANGE, stroke_width=4).move_to(d2p(-n, 0)) for n in range(5)])
        axl = Line(d2p(-4.5, 0), d2p(4.5, 0), stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.35)
        self.play(FadeIn(img), FadeIn(bx), run_time=1.5)
        self.play(FadeIn(xl6), Create(axl), run_time=0.6)
        self.play(Create(rings, lag_ratio=0.2), run_time=1.0)
        c1 = self.L("n_img", 24, LIGHT, -1.25)
        c2 = self.L("n_pole", 24, ORANGE, -1.75)
        self.play(FadeIn(c1), FadeIn(c2), run_time=0.6)
        self.hold(until - 9.0)
        nr = fm(["Γ(z)", "Γ(1−z)", "=", "π", "÷", "sin(πz)"], 40, SUN).move_to([0, -3.0, 0])
        self.play(FadeIn(nr), run_time=0.8)
        nw = self.L("n_why", 30, MINT, -4.1)
        self.play(FadeIn(nw), run_time=0.8)
        self.hold(until)

        # ============ 7. zeta ============
        until = self.beat("zeta")
        s7 = self.L("z_cap", 28, WHITE, 5.55)
        self.play(FadeOut(Group(img, bx, xl6, rings, axl, c1, c2, nr, nw)), ReplacementTransform(s6, s7), run_time=0.7)
        fxi = fm(["ξ(s)", "=", "½", "s(s−1)", "π", ("−s/2", "sup"), ("Γ(s/2)", "n", ORANGE), "ζ(s)", "=", "ξ(1−s)"], 34, SUN)
        fxi.move_to([0, 4.85, 0])
        fxi = fit(fxi, 8.0)
        self.play(FadeIn(fxi), run_time=0.8)
        xr = (-7.2, 1.2)
        ag = mk_axes(xr, (-8, 8), 7.6, 1.7, 0, 2.7, xstep=1, ystep=4)
        az = mk_axes(xr, (-0.7, 0.35), 7.6, 1.5, 0, 0.5, xstep=1, ystep=0.5)
        gh = lambda s: sp.gamma(s / 2)
        zv = lambda s: np.array([float(gm.mp.zeta(float(x))) for x in s])
        cgh = line_pts(ag, gh, xr[0], xr[1] - 0.2, SKY, 4, n=2400, ylim=(-8, 8))
        czv = line_pts(az, zv, xr[0], 0.9, MINT, 4, n=500, ylim=(-0.7, 0.35))
        xlz = tick_labels(az, [-6, -4, -2, 0], dy=-0.48)
        pole_l = VGroup(*[DashedLine(ag.c2p(-k, -8), az.c2p(-k, -0.7), color=ORANGE, stroke_width=2, dash_length=0.12, stroke_opacity=0.8) for k in (0, 2, 4, 6)])
        zer = VGroup(*[Circle(radius=0.12, color=ORANGE, stroke_width=4).move_to(az.c2p(-k, 0)) for k in (2, 4, 6)])
        tg_ = fit(T(tr(TX["z_g"]), 24, SKY), 7.6).move_to([0, 3.85 + 0.55, 0]) 
        tg_.move_to([0, 3.9, 0])
        tz_ = fit(T(tr(TX["z_z"]), 24, MINT), 7.6).move_to([0, -0.75, 0])
        self.play(Create(ag), Create(az), FadeIn(xlz), run_time=0.7)
        self.play(Create(cgh, lag_ratio=0.3), FadeIn(tg_), run_time=2.0)
        self.play(Create(pole_l), run_time=1.0)
        self.play(Create(czv), FadeIn(tz_), FadeIn(zer), run_time=1.5)
        ze = self.L("z_ent", 26, WHITE, -1.7)
        self.play(FadeIn(ze), run_time=0.6)
        self.hold(until - 14.0)
        # pha B: ξ đối xứng
        self.play(FadeOut(VGroup(ag, az, cgh, czv, xlz, pole_l, zer, tg_, tz_, ze)), run_time=0.6)
        axx = mk_axes((-4, 5), (0.3, 1.6), 7.6, 3.2, 0, 1.2, xstep=1, ystep=0.5)
        xv = lambda s: XI_REAL(float(s) + 1e-9)
        cxi = line_pts(axx, xv, -4, 5, SKY, 5, n=181, vec=False)
        mid = DashedLine(axx.c2p(0.5, 0.3), axx.c2p(0.5, 1.6), color=DIM, stroke_width=2)
        xlx = tick_labels(axx, [-4, -2, 0, 2, 4], dy=-0.22, y0=0.3)
        v3 = XI_REAL(3.0)
        pA = Dot(axx.c2p(3, v3), radius=0.11, color=SUN)
        pB = Dot(axx.c2p(-2, v3), radius=0.11, color=SUN)
        hl2 = DashedLine(axx.c2p(-2, v3), axx.c2p(3, v3), color=SUN, stroke_width=2.5)
        lab3 = T("s = 3", 22, SUN).next_to(pA, UP, buff=0.1)
        labm2 = T("s = −2", 22, ORANGE).next_to(pB, UP, buff=0.1)
        self.play(Create(axx), FadeIn(xlx), Create(mid), run_time=0.8)
        self.play(Create(cxi), run_time=1.5)
        zx = self.L("z_xi", 26, WHITE, -1.2)
        self.play(FadeIn(zx), FadeIn(pA), FadeIn(pB), Create(hl2), FadeIn(lab3), FadeIn(labm2), run_time=1.0)
        zp = self.L("z_pt", 30, SUN, -2.0)
        zt = self.L("z_triv", 30, ORANGE, -2.9)
        self.play(FadeIn(zp), run_time=0.5)
        self.play(FadeIn(zt), run_time=0.6)
        self.hold(until)

        # ============ 8. thể tích quả cầu ============
        until = self.beat("ball")
        s8 = self.L("v_cap", 28, WHITE, 5.55)
        self.play(FadeOut(VGroup(axx, cxi, mid, xlx, pA, pB, hl2, lab3, labm2, zx, zp, zt, fxi)), ReplacementTransform(s7, s8), run_time=0.7)
        fv = fm(["V(n)", "=", "π", ("n/2", "sup"), "÷", "Γ(n/2 + 1)"], 42, SUN).move_to([0, 4.7, 0])
        self.play(FadeIn(fv), run_time=0.8)
        axv = mk_axes((0, 21), (0, 6), 7.4, 3.8, 0, 1.5, xstep=5, ystep=1)
        xv_ = tick_labels(axv, [1, 5, 10, 15, 20], dy=-0.2)
        vc = line_pts(axv, lambda x: np.pi ** (x / 2) / sp.gamma(x / 2 + 1), 0.02, 21, SKY, 5, n=800)
        vd = VGroup(*[Dot(axv.c2p(n, V(n)), radius=0.07, color=SUN) for n in range(1, 21)])
        self.play(Create(axv), FadeIn(xv_), run_time=0.7)
        self.play(Create(vc), run_time=1.8)
        self.play(LaggedStart(*[FadeIn(d, scale=1.5) for d in vd], lag_ratio=0.12), run_time=2.4)
        top = Circle(radius=0.2, color=ORANGE, stroke_width=4).move_to(axv.c2p(5, V(5)))
        vp = self.L("v_peak", 34, ORANGE, -1.5)
        self.play(Create(top), FadeIn(vp), run_time=0.8)
        n1 = self.L("v_note", 28, WHITE, -2.3)
        self.play(FadeIn(n1), run_time=0.5)
        n2 = self.L("v_note2", 24, DIM, -2.95)
        self.play(FadeIn(n2), run_time=0.5)
        vn = T(tr(TX["v_n"]), 22, DIM).move_to(axv.c2p(17.5, 0) + np.array([0, 0.35, 0]))
        self.add(vn)
        self.hold(until)

        # ============ 9. tổng kết ============
        until = self.beat("outro")
        s9 = self.L("o_cap", 32, SUN, 5.55)
        self.play(FadeOut(VGroup(axv, vc, vd, xv_, top, vp, n1, n2, fv, vn)), ReplacementTransform(s8, s9), run_time=0.7)
        big = fm(["Γ(z)", "=", "∫", ("∞", "sup"), ("0", "subs"), "t", ("z−1", "sup"), "e", ("−t", "sup"), "dt"], 44, SUN).move_to([0, 3.4, 0])
        self.play(FadeIn(big), run_time=0.8)
        lines = VGroup(*[self.L(k, 28, c, 1.2 - 0.95 * i) for i, (k, c) in enumerate(
            [("o1", WHITE), ("o2", SKY), ("o3", MINT), ("o4", ORANGE), ("o5", PINK)])])
        for ln in lines:
            self.play(FadeIn(ln), run_time=0.5)
        self.hold(until)
        self.wait(1.0)
        os.makedirs(VO_DIR, exist_ok=True)
        json.dump(self.starts, open(os.path.join(VO_DIR, "starts_%s.json" % LANG), "w"))
