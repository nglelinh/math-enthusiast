from common_b import *
import json

# Kiểm tra sai số phép nhớ bị triệt tiêu theo p^(-m) khi nâng lũy thừa p^m
p = 5
assert p ** (-3) == 1 / 125

TX = {
    "title": {"vi": "Phép nghiêng (Tilting) X ↦ X^♭\nXóa 'phép nhớ' như thế nào?", "en": "Tilting X ↦ X^♭\nHow Carrying Vanishes"},
    "s1_a": {"vi": "Mỗi phần tử của K^♭ là một dãy vô hạn tương thích\ncác căn bậc p:  x = (x^(0), x^(1), x^(2), ...)", "en": "An element of K^♭ is a compatible sequence\nof p-power roots:  x = (x^(0), x^(1), x^(2), ...)"},
    "s1_b": {"vi": "Điều kiện tương thích:  (x^(n+1))^p = x^(n)\nPhép nhân định nghĩa thẳng theo từng tọa độ!", "en": "Compatibility rule:  (x^(n+1))^p = x^(n)\nMultiplication works coordinate-by-coordinate!"},
    "s2_a": {"vi": "Phép cộng trong K^♭ — bí mật xóa phép nhớ:\nLấy giới hạn khi nâng lên lũy thừa p^m!", "en": "Addition in K^♭ — the secret erasing carries:\nTake the limit of p^m-th powers!"},
    "s2_b": {"vi": "Mọi sai số nhớ đều chia hết cho p^m\n⇒ Trong chuẩn p-adic, chúng co về 0 (p^(−m) → 0)!", "en": "Every carry error is divisible by p^m\n⇒ In the p-adic norm, it shrinks as p^(−m) → 0!"},
    "s3_a": {"vi": "Bước nhảy tầm Fields (Scholze 2012):\nNâng phép nghiêng từ trường lên KHÔNG GIAN hình học!", "en": "Fields-level leap (Scholze 2012):\nLift tilting from fields to GEOMETRIC SPACES!"},
    "s3_b": {"vi": "X (đặc số 0) và X^♭ (đặc số p) có cùng tô pô\nvà cùng phủ étale ⇒ cùng đối đồng điều étale!", "en": "X (char 0) and X^♭ (char p) share the exact same\ntopology & étale covers ⇒ same étale cohomology!"},
}


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class ScholzeTilting(Scene):
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

        # --- Phần 1: Dãy căn bậc p tương thích ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 23, SKY, 4.5)
        self.play(FadeIn(s1a), run_time=0.8)

        seq_box = RoundedRectangle(corner_radius=0.16, width=7.5, height=2.2, fill_color=CARD, fill_opacity=1, stroke_color=MINT, stroke_width=3).move_to([0, 1.5, 0])
        seq_t = T("p^♭  =  ( p ,  p^(1/p) ,  p^(1/p²) ,  p^(1/p³) , ... )\n\n(x · y)^(n)  =  x^(n) · y^(n)" if LANG == "vi" else "p^♭  =  ( p ,  p^(1/p) ,  p^(1/p²) ,  p^(1/p³) , ... )\n\n(x · y)^(n)  =  x^(n) · y^(n)", 21, MINT).move_to(seq_box)
        self.play(FadeIn(seq_box, seq_t), run_time=1.2)
        self.wait(2.0)

        s1b = line(TX["s1_b"], 23, WHITE, -1.6)
        self.play(FadeIn(s1b), run_time=0.8)
        end_vo("s1", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 2: Công thức cộng xóa phép nhớ ---
        t0 = start_vo("s2")
        s2a = line(TX["s2_a"], 23, SKY, 4.5)
        self.play(FadeIn(s2a), run_time=0.8)

        add_box = RoundedRectangle(corner_radius=0.16, width=7.6, height=2.3, fill_color=CARD, fill_opacity=1, stroke_color=SUN, stroke_width=3).move_to([0, 1.5, 0])
        add_t = T("(x + y)^(n)  =  lim_{m→∞} ( x^(n+m) + y^(n+m) )^(p^m)\n\n1 + 1 + ... + 1 (p lần)  =  lim p^(p^m)  =  0 !" if LANG == "vi" else "(x + y)^(n)  =  lim_{m→∞} ( x^(n+m) + y^(n+m) )^(p^m)\n\n1 + 1 + ... + 1 (p times)  =  lim p^(p^m)  =  0 !", 20, SUN).move_to(add_box)
        self.play(FadeIn(add_box, add_t), run_time=1.2)
        self.wait(2.0)

        s2b = line(TX["s2_b"], 23, MINT, -1.7)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s2", t0, 9.0)
        wipe(self, keep=[title])

        # --- Phần 3: Định lý tương đương nghiêng ---
        t0 = start_vo("s3")
        s3a = line(TX["s3_a"], 23, SKY, 4.5)
        self.play(FadeIn(s3a), run_time=0.8)

        eq_box = RoundedRectangle(corner_radius=0.16, width=7.5, height=2.1, fill_color=CARD, fill_opacity=1, stroke_color=SKY, stroke_width=3).move_to([0, 1.5, 0])
        eq_t = T("Định lý Tương đương Nghiêng:\n\n|X|  ≃  |X^♭|   (cùng không gian tô pô)\nX_ét  ≃  (X^♭)_ét   (cùng phạm trù phủ étale!)" if LANG == "vi" else "Tilting Equivalence Theorem:\n\n|X|  ≃  |X^♭|   (same topological space)\nX_ét  ≃  (X^♭)_ét   (equivalent étale sites!)", 21, SKY).move_to(eq_box)
        self.play(FadeIn(eq_box, eq_t), run_time=1.2)
        self.wait(2.0)

        s3b = line(TX["s3_b"], 23, SUN, -1.7)
        self.play(FadeIn(s3b), run_time=0.8)
        end_vo("s3", t0, 9.0)

        if os.environ.get("VO_TIMELINE_JSON"):
            with open(os.environ["VO_TIMELINE_JSON"], "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
