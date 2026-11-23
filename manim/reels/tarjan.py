from common_b import *
import json

TX = {
    "title": {"vi": "Thuật toán Tarjan:\nThành phần liên thông mạnh", "en": "Tarjan's algorithm:\nStrongly connected components"},
    "s1_a": {"vi": "Trong đồ thị có hướng, hai đỉnh u, v cùng\nmột SCC nếu đi được từ u → v và từ v → u", "en": "In a directed graph, u and v share an SCC\niff u reaches v and v reaches u"},
    "s1_b": {"vi": "Duyệt từ từng đỉnh tốn O(n(n+m));\nTarjan (1972) chỉ cần 1 lần DFS: O(n+m)", "en": "Naive search takes O(n(n+m));\nTarjan (1972) needs just 1 DFS: O(n+m)"},
    "s2_a": {"vi": "Mỗi đỉnh u lưu hai số: disc[u] (thời điểm thăm)\nvà low[u] (disc nhỏ nhất chạm tới trên stack)", "en": "Each u tracks disc[u] (discovery time)\nand low[u] (earliest disc reachable on stack)"},
    "s2_b": {"vi": "Quy tắc khi duyệt cạnh u → v:\n• chưa thăm ⇒ min(low[u], low[v])\n• đang trên stack ⇒ min(low[u], disc[v])", "en": "Update rule on edge u → v:\n• unvisited ⇒ min(low[u], low[v])\n• on stack ⇒ min(low[u], disc[v])"},
    "s3_a": {"vi": "Bước 1: DFS đi A → B → C\nNgăn xếp (Stack): [A, B, C]", "en": "Step 1: DFS visits A → B → C\nActive stack: [A, B, C]"},
    "s3_b": {"vi": "Cạnh ngược C → A cập nhật low[C] = min(2, 0) = 0,\nrồi lan ngược về B (low=0) và A (low=0)", "en": "Back-edge C → A sets low[C] = min(2, 0) = 0,\npropagating back to B (low=0) and A (low=0)"},
    "s3_c": {"vi": "Bước 2: Tiếp tục C → D → E → F\nTại F: low[F] == disc[F] == 5 ⇒ pop {F}", "en": "Step 2: Continue C → D → E → F\nAt F: low[F] == disc[F] == 5 ⇒ pop {F}"},
    "s3_d": {"vi": "Quay lui E: cạnh E → D kéo low[E] = min(4, 3) = 3\nTại D: low[D] == disc[D] == 3 ⇒ pop {D, E}", "en": "Back at E: E → D pulls low[E] = min(4, 3) = 3\nAt D: low[D] == disc[D] == 3 ⇒ pop {D, E}"},
    "s3_e": {"vi": "Quay lui A: low[A] == disc[A] == 0\n⇒ pop trọn {A, B, C}", "en": "Back at A: low[A] == disc[A] == 0\n⇒ pop {A, B, C}"},
    "s4_a": {"vi": "Bẫy kinh điển: vì sao phải kiểm tra on_stack[v]?", "en": "Classic pitfall: why check on_stack[v]?"},
    "s4_b": {"vi": "Nếu v đã thuộc SCC khác đã pop (như E → F),\nkhông được dùng disc[v] để hạ low[u] kẻo gộp nhầm 2 SCC", "en": "If v was popped into another SCC (like E → F),\nusing disc[v] would wrongly merge two distinct SCCs"},
    "s5_a": {"vi": "Co mỗi SCC thành 1 đỉnh ⇒ luôn thu được\nđồ thị có hướng không chu trình (DAG)", "en": "Contract each SCC to 1 node ⇒ always yields\na Directed Acyclic Graph (DAG)"},
    "end": {"vi": "Cấu trúc toàn cục chỉ từ 1 lần DFS:\nHopcroft & Tarjan (Giải Turing 1986)", "en": "Global structure from a single DFS:\nHopcroft & Tarjan (Turing Award 1986)"},
}

adj = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [3, 5], 5: []}
names = ["A", "B", "C", "D", "E", "F"]
disc = [-1] * 6
low = [0] * 6
on_stack = [False] * 6
stack = []
sccs = []
timer = [0]


def tarjan(u):
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    stack.append(u)
    on_stack[u] = True
    for v in adj[u]:
        if disc[v] == -1:
            tarjan(v)
            low[u] = min(low[u], low[v])
        elif on_stack[v]:
            low[u] = min(low[u], disc[v])
    if low[u] == disc[u]:
        comp = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            comp.append(w)
            if w == u:
                break
        sccs.append(sorted(comp))


tarjan(0)
assert sccs == [[5], [3, 4], [0, 1, 2]]
assert disc == [0, 1, 2, 3, 4, 5]
assert low == [0, 0, 0, 3, 3, 5]


def wipe(scene, keep=()):
    keep_set = set(keep)
    outs = [m for m in list(scene.mobjects) if m not in keep_set]
    if outs:
        scene.play(*[FadeOut(m) for m in outs], run_time=0.5)


class TarjanSCC(Scene):
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
                self.wait(max(0.7, rem))
            else:
                self.wait(fallback)

        title = line(TX["title"], 38, WHITE, 6.2)
        self.add(title)

        # --- Phần 1 ---
        t0 = start_vo("s1")
        s1a = line(TX["s1_a"], 26, SKY, 4.3)
        s1b = line(TX["s1_b"], 26, MINT, 2.3)
        self.play(FadeIn(s1a), run_time=0.8)
        self.wait(4.0)
        self.play(FadeIn(s1b), run_time=0.8)
        self.wait(5.0)
        s2a = line(TX["s2_a"], 25, SUN, 0.3)
        s2b = line(TX["s2_b"], 23, WHITE, -1.7)
        self.play(FadeIn(s2a), run_time=0.8)
        self.wait(3.5)
        self.play(FadeIn(s2b), run_time=0.8)
        end_vo("s1", t0, 11.0)
        wipe(self, keep=[title])

        # --- Phần 2 ---
        t0 = start_vo("s2")
        pos = {
            0: np.array([-2.6,  2.7, 0]),
            1: np.array([-0.5,  3.2, 0]),
            2: np.array([-1.5,  1.0, 0]),
            3: np.array([ 1.2,  1.0, 0]),
            4: np.array([ 2.6,  2.5, 0]),
            5: np.array([ 2.6, -0.4, 0]),
        }
        nodes = VGroup(*[
            VGroup(Circle(0.4, color=SKY, fill_color=CARD, fill_opacity=1, stroke_width=3.5).move_to(pos[i]),
                   T(nm, 28, WHITE).move_to(pos[i]))
            for i, nm in enumerate(names)
        ])
        arrows = {}
        arrow_group = VGroup()
        for u, vs in adj.items():
            for v in vs:
                d = pos[v] - pos[u]
                du = d / np.linalg.norm(d)
                st, en = pos[u] + du * 0.46, pos[v] - du * 0.46
                if (u, v) in ((3, 4), (4, 3)):
                    perp = np.array([-du[1], du[0], 0]) * 0.13
                    st, en = st + perp, en + perp
                ar = Arrow(st, en, buff=0, stroke_width=3, color=DIM, max_tip_length_to_length_ratio=0.18)
                arrows[(u, v)] = ar
                arrow_group.add(ar)
        stack_box = RoundedRectangle(corner_radius=0.12, width=6.6, height=0.95,
                                     fill_color=CARD, fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([0, -2.3, 0])
        stack_txt = T("Stack: [ ]", 24, SUN).move_to(stack_box)
        self.play(FadeIn(nodes), FadeIn(arrow_group), FadeIn(stack_box), FadeIn(stack_txt), run_time=1.2)
        self.wait(2.0)

        c = line(TX["s3_a"], 26, SKY, 4.9)
        self.play(FadeIn(c), run_time=0.6)
        meta = {}
        for idx, s_str in ((0, "(0,0)"), (1, "(1,1)"), (2, "(2,2)")):
            dir_p = UP if idx == 1 else (LEFT if idx == 0 else DOWN)
            m_t = T(s_str, 20, SUN).next_to(nodes[idx], dir_p, buff=0.1)
            meta[idx] = m_t
            self.play(FadeIn(m_t), nodes[idx][0].animate.set_stroke(SUN, width=5), run_time=0.9)
        self.play(Transform(stack_txt, T("Stack: [ A, B, C ]", 24, SUN).move_to(stack_box)), run_time=0.6)
        self.wait(3.5)

        c_new = line(TX["s3_b"], 24, SUN, 4.9)
        self.play(ReplacementTransform(c, c_new), arrows[(2, 0)].animate.set_color(SUN).set_stroke(width=5), run_time=0.8)
        c = c_new
        for idx, s_str in ((2, "(2,0)"), (1, "(1,0)")):
            dir_p = UP if idx == 1 else DOWN
            self.play(Transform(meta[idx], T(s_str, 20, MINT).next_to(nodes[idx], dir_p, buff=0.1)), run_time=0.9)
        end_vo("s2", t0, 8.0)

        # --- Phần 3 ---
        t0 = start_vo("s3")
        c_new = line(TX["s3_c"], 25, PINK, 4.9)
        self.play(ReplacementTransform(c, c_new), run_time=0.6)
        c = c_new
        for idx, s_str in ((3, "(3,3)"), (4, "(4,4)"), (5, "(5,5)")):
            dir_p = UP if idx == 4 else DOWN
            m_t = T(s_str, 20, SUN).next_to(nodes[idx], dir_p, buff=0.1)
            meta[idx] = m_t
            self.play(FadeIn(m_t), nodes[idx][0].animate.set_stroke(SUN, width=5), run_time=0.8)
        self.play(Transform(stack_txt, T("Stack: [ A, B, C, D, E, F ]", 24, SUN).move_to(stack_box)), run_time=0.6)
        self.wait(2.5)
        self.play(nodes[5][0].animate.set_fill(PINK, opacity=0.9).set_stroke(PINK),
                  nodes[5][1].animate.set_color(BLACK),
                  Transform(stack_txt, T("Stack: [ A, B, C, D, E ]  →  {F}", 23, PINK).move_to(stack_box)), run_time=0.9)
        self.wait(4.0)

        c_new = line(TX["s3_d"], 24, SUN, 4.9)
        self.play(ReplacementTransform(c, c_new), arrows[(4, 3)].animate.set_color(SUN).set_stroke(width=5), run_time=0.8)
        c = c_new
        self.play(Transform(meta[4], T("(4,3)", 20, SUN).next_to(nodes[4], UP, buff=0.1)), run_time=0.8)
        self.wait(2.0)
        for u in (3, 4):
            self.play(nodes[u][0].animate.set_fill(SUN, opacity=0.9).set_stroke(SUN),
                      nodes[u][1].animate.set_color(BLACK), run_time=0.5)
        self.play(Transform(stack_txt, T("Stack: [ A, B, C ]  →  {D, E}", 23, SUN).move_to(stack_box)), run_time=0.7)
        self.wait(4.0)

        c_new = line(TX["s3_e"], 26, MINT, 4.9)
        self.play(ReplacementTransform(c, c_new), run_time=0.6)
        c = c_new
        for u in (0, 1, 2):
            self.play(nodes[u][0].animate.set_fill(MINT, opacity=0.9).set_stroke(MINT),
                      nodes[u][1].animate.set_color(BLACK), run_time=0.5)
        self.play(Transform(stack_txt, T("Stack: [ ]  →  {A, B, C}", 24, MINT).move_to(stack_box)), run_time=0.7)
        end_vo("s3", t0, 8.0)

        # --- Phần 4 ---
        t0 = start_vo("s4")
        c_new = line(TX["s4_a"], 28, PINK, 4.9)
        self.play(ReplacementTransform(c, c_new), arrows[(4, 5)].animate.set_color(PINK).set_stroke(width=6), run_time=0.7)
        c = c_new
        s4b = line(TX["s4_b"], 23, WHITE, -3.7)
        self.play(FadeIn(s4b), run_time=0.8)
        end_vo("s4", t0, 10.0)

        # --- Phần 5 ---
        t0 = start_vo("s5")
        self.play(FadeOut(s4b), FadeOut(stack_box), FadeOut(stack_txt), run_time=0.5)
        c_new = line(TX["s5_a"], 26, SKY, 4.9)
        self.play(ReplacementTransform(c, c_new), run_time=0.6)
        dag_x = [-2.4, 0.0, 2.4]
        dag_lbls = ["{A,B,C}", "{D,E}", "{F}"]
        dag_cols = [MINT, SUN, PINK]
        dag_boxes = VGroup()
        for x, lb, col in zip(dag_x, dag_lbls, dag_cols):
            b = RoundedRectangle(corner_radius=0.15, width=1.8, height=0.85,
                                 fill_color=col, fill_opacity=0.2, stroke_color=col, stroke_width=3).move_to([x, -2.5, 0])
            t = T(lb, 24, col).move_to([x, -2.5, 0])
            dag_boxes.add(VGroup(b, t))
        dag_arr1 = Arrow([-1.4, -2.5, 0], [-1.0, -2.5, 0], buff=0, color=WHITE, stroke_width=3.5)
        dag_arr2 = Arrow([1.0, -2.5, 0], [1.4, -2.5, 0], buff=0, color=WHITE, stroke_width=3.5)
        self.play(FadeIn(dag_boxes), Create(dag_arr1), Create(dag_arr2), run_time=1.2)
        self.wait(4.5)
        end_c = line(TX["end"], 26, WHITE, -4.5)
        self.play(FadeIn(end_c), run_time=0.8)
        end_vo("s5", t0, 11.0)

        tl_out = os.environ.get("VO_TIMELINE_JSON", "")
        if tl_out:
            with open(tl_out, "w") as f:
                json.dump({"timeline": timeline, "total": float(self.time)}, f, indent=2)
