from common_b import *

TX = {
    "title": {"vi": "Thuật toán Tarjan:\nThành phần liên thông mạnh", "en": "Tarjan's algorithm:\nStrongly connected components"},
    "goal": {"vi": "Tìm mọi SCC trong O(n + m)\nbằng một lần duyệt DFS duy nhất", "en": "Find all SCCs in O(n + m)\nwith a single DFS pass"},
    "dfs": {"vi": "Mỗi đỉnh ghi (disc, low) và\nđưa vào ngăn xếp (stack)", "en": "Track (disc, low) per vertex\nand push onto a stack"},
    "pop": {"vi": "Khi low[u] == disc[u]: pop khỏi\nstack để tách trọn một SCC", "en": "When low[u] == disc[u]: pop\nthe stack to emit one SCC"},
    "dag": {"vi": "Co mỗi SCC thành 1 đỉnh\n⇒ thu được đồ thị không chu trình (DAG)", "en": "Contract each SCC to a node\n⇒ yields a condensation DAG"},
    "end": {"vi": "Cấu trúc toàn cục chỉ từ 1 lần DFS:\nHopcroft & Tarjan (Turing 1986)", "en": "Global structure from one DFS:\nHopcroft & Tarjan (Turing 1986)"},
}

# Tính chính xác Tarjan SCC bằng Python
adj = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [3, 5],
    5: [],
}
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
assert sccs == [[5], [3, 4], [0, 1, 2]], f"Unexpected SCCs: {sccs}"
assert disc == [0, 1, 2, 3, 4, 5]
assert low == [0, 0, 0, 3, 3, 5]


class TarjanSCC(Scene):
    def construct(self):
        self.add(line(TX["title"], 38, WHITE, 6.2))
        c1 = line(TX["goal"], 28, SKY, 4.9)
        self.play(FadeIn(c1), run_time=0.6)

        pos = {
            0: np.array([-2.6,  2.8, 0]),  # A
            1: np.array([-0.5,  3.3, 0]),  # B
            2: np.array([-1.5,  1.2, 0]),  # C
            3: np.array([ 1.2,  1.2, 0]),  # D
            4: np.array([ 2.6,  2.6, 0]),  # E
            5: np.array([ 2.6, -0.2, 0]),  # F
        }

        nodes = VGroup()
        for i, nm in enumerate(names):
            circ = Circle(0.4, color=SKY, fill_color=CARD, fill_opacity=1, stroke_width=3.5).move_to(pos[i])
            lbl = T(nm, 28, WHITE).move_to(pos[i])
            nodes.add(VGroup(circ, lbl))

        arrows = VGroup()
        for u, vs in adj.items():
            for v in vs:
                d = pos[v] - pos[u]
                du = d / np.linalg.norm(d)
                s = pos[u] + du * 0.46
                e = pos[v] - du * 0.46
                if (u, v) in ((3, 4), (4, 3)):
                    perp = np.array([-du[1], du[0], 0]) * 0.13
                    s = s + perp
                    e = e + perp
                arrows.add(Arrow(s, e, buff=0, stroke_width=3, color=DIM, max_tip_length_to_length_ratio=0.18))

        self.play(FadeIn(nodes), FadeIn(arrows), run_time=1.0)
        self.wait(0.8)

        # Hiện nhãn (disc, low) theo thứ tự DFS
        self.play(FadeOut(c1), run_time=0.4)
        c2 = line(TX["dfs"], 28, SUN, 4.9)
        self.play(FadeIn(c2), run_time=0.5)

        meta = VGroup()
        for i in range(6):
            dir_pos = UP if i in (1, 4) else (LEFT if i == 0 else DOWN)
            t = T(f"({disc[i]},{low[i]})", 20, SUN).next_to(nodes[i], dir_pos, buff=0.1)
            meta.add(t)
        self.play(FadeIn(meta, lag_ratio=0.15), run_time=1.4)
        self.wait(0.8)

        # Tô màu 3 SCC khi pop
        self.play(FadeOut(c2), run_time=0.4)
        c3 = line(TX["pop"], 28, MINT, 4.9)
        self.play(FadeIn(c3), run_time=0.5)

        scc_cols = [PINK, SUN, MINT]
        for comp, col in zip(sccs, scc_cols):
            self.play(*[
                nodes[u][0].animate.set_fill(col, opacity=0.9).set_stroke(col)
                for u in comp
            ], *[nodes[u][1].animate.set_color(BLACK) for u in comp], run_time=0.65)
            self.wait(0.4)

        # Vẽ DAG rút gọn ở phía dưới
        c4 = line(TX["dag"], 28, SKY, -1.7)
        self.play(FadeIn(c4), run_time=0.5)

        dag_x = [-2.4, 0.0, 2.4]
        dag_lbls = ["{A,B,C}", "{D,E}", "{F}"]
        dag_cols = [MINT, SUN, PINK]
        dag_boxes = VGroup()
        for x, lb, col in zip(dag_x, dag_lbls, dag_cols):
            b = RoundedRectangle(corner_radius=0.15, width=1.8, height=0.85,
                                 fill_color=col, fill_opacity=0.2, stroke_color=col, stroke_width=3).move_to([x, -3.3, 0])
            t = T(lb, 24, col).move_to([x, -3.3, 0])
            dag_boxes.add(VGroup(b, t))
        dag_arr1 = Arrow([-1.4, -3.3, 0], [-1.0, -3.3, 0], buff=0, color=WHITE, stroke_width=3.5)
        dag_arr2 = Arrow([1.0, -3.3, 0], [1.4, -3.3, 0], buff=0, color=WHITE, stroke_width=3.5)

        self.play(FadeIn(dag_boxes), Create(dag_arr1), Create(dag_arr2), run_time=0.9)
        self.wait(1.0)

        end_c = line(TX["end"], 26, WHITE, -5.2)
        self.play(FadeIn(end_c), run_time=0.6)
        self.wait(2.5)
