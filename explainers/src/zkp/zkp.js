export const PALETTE = ['#ff7eb6', '#4cc9f0', '#ffd166'];
export const COLOR_NAMES = {
  vi: ['Hồng', 'Xanh', 'Vàng'],
  en: ['Pink', 'Blue', 'Yellow'],
};

export const NODES = [
  { id: '1', x: 240, y: 40 },
  { id: '2', x: 105, y: 120 },
  { id: '3', x: 375, y: 120 },
  { id: '4', x: 155, y: 235 },
  { id: '5', x: 325, y: 235 },
];

export const EDGES = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4], [0, 3]];

export const PRESETS = {
  honest: {
    label: { vi: 'Peggy trung thực (3-tô màu hợp lệ)', en: 'Honest Peggy (valid 3-coloring)' },
    coloring: [0, 1, 2, 2, 0],
    badEdgeIdx: -1,
  },
  cheater: {
    label: { vi: 'Peggy gian dối (cạnh 3–5 trùng màu)', en: 'Cheating Peggy (bad edge 3–5)' },
    coloring: [2, 1, 0, 1, 0], // edge (2,4) = (3-5 in 1-based) both color 0 (Pink)
    badEdgeIdx: 4,
  },
};

export const PERMUTATIONS = [
  [0, 1, 2],
  [1, 2, 0],
  [2, 0, 1],
  [0, 2, 1],
  [2, 1, 0],
  [1, 0, 2],
];

export function catchProbability(k, m = EDGES.length) {
  return 1 - Math.pow(1 - 1 / m, k);
}

export function steps(presetKey = 'honest', permIdx = 0, challengeIdx = 3, lang = 'vi') {
  const p = PRESETS[presetKey] || PRESETS.honest;
  const perm = PERMUTATIONS[permIdx % PERMUTATIONS.length];
  const cn = COLOR_NAMES[lang] || COLOR_NAMES.vi;
  const permuted = p.coloring.map((c) => perm[c]);
  const eIdx = Math.max(0, Math.min(EDGES.length - 1, challengeIdx));
  const [u, v] = EDGES[eIdx];
  const validEdge = permuted[u] !== permuted[v];

  return [
    {
      phase: 'secret',
      visibleColors: p.coloring,
      locked: [false, false, false, false, false],
      challengeEdge: -1,
      ok: null,
      msg: lang === 'vi'
        ? (presetKey === 'honest'
            ? 'Bí mật của Peggy: cách tô 3 màu hợp lệ trên cả 7 cạnh (Victor chưa thấy).'
            : 'Peggy không có cách tô hợp lệ: cạnh 3–5 bị trùng màu Hồng!')
        : (presetKey === 'honest'
            ? 'Peggy’s secret: a valid 3-coloring across all 7 edges (hidden from Victor).'
            : 'Peggy has no valid coloring: edge 3–5 has both endpoints Pink!'),
    },
    {
      phase: 'commit',
      visibleColors: permuted,
      locked: [true, true, true, true, true],
      challengeEdge: -1,
      ok: null,
      msg: lang === 'vi'
        ? `Bước 1 (Cam kết): Hoán vị ngẫu nhiên 3 màu rồi khóa kín cả 5 đỉnh.`
        : `Step 1 (Commit): Randomly permute the 3 colors and lock all 5 vertices.`,
    },
    {
      phase: 'challenge',
      visibleColors: permuted,
      locked: [true, true, true, true, true],
      challengeEdge: eIdx,
      ok: null,
      msg: lang === 'vi'
        ? `Bước 2 (Thách thức): Victor chọn ngẫu nhiên cạnh (${u + 1}, ${v + 1}).`
        : `Step 2 (Challenge): Victor picks random edge (${u + 1}, ${v + 1}).`,
    },
    {
      phase: 'open',
      visibleColors: permuted,
      locked: [0, 1, 2, 3, 4].map((i) => i !== u && i !== v),
      challengeEdge: eIdx,
      ok: validEdge,
      msg: lang === 'vi'
        ? (validEdge
            ? `Bước 3 (Mở khóa): Đỉnh ${u + 1} (${cn[permuted[u]]}) ≠ Đỉnh ${v + 1} (${cn[permuted[v]]}) ⇒ Đạt vòng này, không lộ màu gốc!`
            : `Bước 3 (Bắt quả tang!): Đỉnh ${u + 1} và ${v + 1} cùng màu ${cn[permuted[u]]} ⇒ Victor từ chối ngay!`)
        : (validEdge
            ? `Step 3 (Open): Vertex ${u + 1} (${cn[permuted[u]]}) ≠ Vertex ${v + 1} (${cn[permuted[v]]}) ⇒ Round accepted, zero leak!`
            : `Step 3 (Caught!): Vertices ${u + 1} and ${v + 1} are both ${cn[permuted[u]]} ⇒ Victor rejects!`),
    },
  ];
}
