export const PRESETS = {
  dangling: {
    label: { vi: 'Đồ thị 4 trang (D là nút cụt)', en: '4-page graph (D is a dead end)' },
    nodes: ['A', 'B', 'C', 'D'],
    edges: [[0, 1], [0, 2], [1, 2], [1, 3], [2, 0]],
    danglingIdx: 3,
  },
  cycle: {
    label: { vi: 'Đồ thị 4 trang liên thông mạnh (D → A)', en: '4-page strongly connected (D → A)' },
    nodes: ['A', 'B', 'C', 'D'],
    edges: [[0, 1], [0, 2], [1, 2], [1, 3], [2, 0], [3, 0]],
    danglingIdx: -1,
  },
  hub: {
    label: { vi: 'Mạng 4 trang tập trung vào C', en: '4-page hub pointing to C' },
    nodes: ['A', 'B', 'C', 'D'],
    edges: [[0, 2], [1, 2], [3, 2], [2, 0], [0, 1]],
    danglingIdx: -1,
  },
};

export function buildTransition(presetKey, fixDangling = true) {
  const p = PRESETS[presetKey] || PRESETS.dangling;
  const n = p.nodes.length;
  const P = Array.from({ length: n }, () => Array(n).fill(0));
  const outDeg = Array(n).fill(0);
  for (const [u, v] of p.edges) outDeg[u] += 1;
  for (const [u, v] of p.edges) P[u][v] += 1 / outDeg[u];
  if (fixDangling) {
    for (let i = 0; i < n; i++) {
      if (outDeg[i] === 0) {
        for (let j = 0; j < n; j++) P[i][j] = 1 / n;
      }
    }
  }
  return P;
}

export function steps(presetKey = 'dangling', alpha = 0.85, fixDangling = true, lang = 'vi', maxIter = 20) {
  const p = PRESETS[presetKey] || PRESETS.dangling;
  const n = p.nodes.length;
  const P = buildTransition(presetKey, fixDangling);
  const v = Array(n).fill(1 / n);
  let pi = v.slice();
  const out = [];

  for (let k = 0; k <= maxIter; k++) {
    const sum = pi.reduce((a, b) => a + b, 0);
    const ranked = pi
      .map((val, idx) => ({ name: p.nodes[idx], val }))
      .sort((a, b) => b.val - a.val)
      .map((x) => x.name)
      .join(' > ');

    let msg;
    if (k === 0) {
      msg = lang === 'vi'
        ? `Bước k = 0: Khởi tạo phân phối đều (mỗi trang 0,250).`
        : `Step k = 0: Start with uniform distribution (0.250 each).`;
    } else if (!fixDangling && p.danglingIdx >= 0) {
      msg = lang === 'vi'
        ? `Bước k = ${k}: Chưa sửa nút cụt D ⇒ tổng xác suất rò rỉ còn ${sum.toFixed(3)} (< 1).`
        : `Step k = ${k}: Unfixed dead-end D ⇒ total mass leaks to ${sum.toFixed(3)} (< 1).`;
    } else {
      msg = lang === 'vi'
        ? `Bước k = ${k} (α = ${alpha.toFixed(2)}): Thứ hạng hiện tại ${ranked}. Tổng = ${sum.toFixed(3)}.`
        : `Step k = ${k} (α = ${alpha.toFixed(2)}): Current rank ${ranked}. Sum = ${sum.toFixed(3)}.`;
    }

    out.push({ k, pi: pi.slice(), sum, ranked, msg });

    const next = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        next[j] += pi[i] * (alpha * P[i][j] + (fixDangling ? (1 - alpha) * v[j] : 0));
      }
    }
    pi = next;
  }
  return out;
}
