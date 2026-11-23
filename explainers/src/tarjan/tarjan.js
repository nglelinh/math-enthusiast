export const SCC_COLORS = ['#80ed99', '#ffd166', '#ff7eb6', '#4cc9f0'];

export const PRESETS = {
  sixNode: {
    label: { vi: 'Đồ thị 6 đỉnh (3 SCC)', en: '6-vertex graph (3 SCCs)' },
    names: ['A', 'B', 'C', 'D', 'E', 'F'],
    pos: [
      { x: 75, y: 70 },
      { x: 185, y: 45 },
      { x: 135, y: 175 },
      { x: 270, y: 175 },
      { x: 365, y: 70 },
      { x: 365, y: 225 },
    ],
    adj: [[1], [2], [0, 3], [4], [3, 5], []],
  },
  twoCycles: {
    label: { vi: 'Hai chu trình nối tiếp (5 đỉnh, 2 SCC)', en: 'Two chained cycles (5 vertices, 2 SCCs)' },
    names: ['A', 'B', 'C', 'D', 'E'],
    pos: [
      { x: 85, y: 75 },
      { x: 195, y: 75 },
      { x: 140, y: 195 },
      { x: 300, y: 75 },
      { x: 375, y: 195 },
    ],
    adj: [[1], [2, 3], [0], [4], [3]],
  },
};

export function steps(presetKey = 'sixNode', lang = 'vi') {
  const p = PRESETS[presetKey] || PRESETS.sixNode;
  const n = p.names.length;
  const disc = Array(n).fill(-1);
  const low = Array(n).fill(-1);
  const onStack = Array(n).fill(false);
  const stack = [];
  const sccs = [];
  const sccOf = Array(n).fill(-1);
  let timer = 0;
  const out = [];

  function snap(activeNode, activeEdge, msg) {
    out.push({
      disc: disc.slice(),
      low: low.slice(),
      stack: stack.slice(),
      onStack: onStack.slice(),
      sccs: sccs.map((c) => c.slice()),
      sccOf: sccOf.slice(),
      activeNode,
      activeEdge,
      msg,
    });
  }

  snap(-1, null, lang === 'vi' ? 'Bắt đầu: chưa thăm đỉnh nào, ngăn xếp rỗng.' : 'Start: all vertices unvisited, stack empty.');

  function dfs(u) {
    disc[u] = low[u] = timer++;
    stack.push(u);
    onStack[u] = true;
    snap(u, null, lang === 'vi'
      ? `Thăm ${p.names[u]}: gán disc = low = ${disc[u]}, đẩy vào stack.`
      : `Visit ${p.names[u]}: set disc = low = ${disc[u]}, push to stack.`);

    for (const v of p.adj[u]) {
      if (disc[v] === -1) {
        dfs(v);
        if (low[v] < low[u]) {
          low[u] = low[v];
          snap(u, [u, v], lang === 'vi'
            ? `Quay lui từ ${p.names[v]} về ${p.names[u]}: cập nhật low[${p.names[u]}] = min(low, low[${p.names[v]}]) = ${low[u]}.`
            : `Return from ${p.names[v]} to ${p.names[u]}: update low[${p.names[u]}] = ${low[u]}.`);
        }
      } else if (onStack[v]) {
        const prev = low[u];
        low[u] = Math.min(low[u], disc[v]);
        snap(u, [u, v], lang === 'vi'
          ? `Cạnh ngược ${p.names[u]} → ${p.names[v]} (${p.names[v]} đang trên stack): low[${p.names[u]}] = min(${prev}, ${disc[v]}) = ${low[u]}.`
          : `Back-edge ${p.names[u]} → ${p.names[v]} (on stack): low[${p.names[u]}] = min(${prev}, ${disc[v]}) = ${low[u]}.`);
      } else {
        snap(u, [u, v], lang === 'vi'
          ? `Cạnh ${p.names[u]} → ${p.names[v]}: ${p.names[v]} đã rời stack (thuộc SCC khác) ⇒ bỏ qua!`
          : `Edge ${p.names[u]} → ${p.names[v]}: ${p.names[v]} is off stack (another SCC) ⇒ ignore!`);
      }
    }

    if (low[u] === disc[u]) {
      const comp = [];
      const cid = sccs.length;
      while (true) {
        const w = stack.pop();
        onStack[w] = false;
        sccOf[w] = cid;
        comp.push(w);
        if (w === u) break;
      }
      comp.sort((a, b) => a - b);
      sccs.push(comp);
      const lbl = comp.map((i) => p.names[i]).join(', ');
      snap(u, null, lang === 'vi'
        ? `low[${p.names[u]}] == disc[${p.names[u]}] == ${disc[u]} ⇒ pop khỏi stack tách trọn SCC {${lbl}}!`
        : `low[${p.names[u]}] == disc[${p.names[u]}] == ${disc[u]} ⇒ pop stack to emit SCC {${lbl}}!`);
    }
  }

  for (let i = 0; i < n; i++) {
    if (disc[i] === -1) dfs(i);
  }
  return out;
}
