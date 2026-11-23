export const COLORS = ['#ff7eb6', '#4cc9f0', '#ffd166', '#80ed99', '#ff9f43'];
export const COLOR_NAMES = {
  vi: ['Hồng', 'Xanh dương', 'Vàng', 'Xanh lục', 'Cam'],
  en: ['Pink', 'Blue', 'Yellow', 'Green', 'Orange'],
};

export const PRESETS = {
  k4: { label: { vi: 'Đồ thị K₄ (3 màu thất bại)', en: 'K₄ graph (3 colors fail)' } },
  kempeFree: { label: { vi: 'Xích Kempe TH1 (không nối 1–3)', en: 'Kempe chain Case 1 (1–3 disconnected)' } },
  kempeBarrier: { label: { vi: 'Xích Kempe TH2 (rào chắn 1–3)', en: 'Kempe chain Case 2 (1–3 barrier)' } },
};

export function heawood(g) {
  return Math.floor((7 + Math.sqrt(1 + 48 * g)) / 2);
}

export function steps(presetKey = 'k4', lang = 'vi') {
  const cn = COLOR_NAMES[lang] || COLOR_NAMES.vi;
  if (presetKey === 'k4') {
    const nodes = [
      { id: '1', x: 240, y: 45 },
      { id: '2', x: 100, y: 215 },
      { id: '3', x: 380, y: 215 },
      { id: '4', x: 240, y: 155 },
    ];
    const edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]];
    return [
      {
        nodes, edges, colors: [-1, -1, -1, -1], highlight: [], ok: null,
        msg: lang === 'vi' ? 'Đồ thị đối ngẫu K₄: 4 nước đôi một chung biên.' : 'Dual graph K₄: 4 mutually adjacent countries.',
      },
      {
        nodes, edges, colors: [0, -1, -1, -1], highlight: [], ok: null,
        msg: lang === 'vi' ? `Tô đỉnh 1 bằng màu ${cn[0]}.` : `Color vertex 1 ${cn[0]}.`,
      },
      {
        nodes, edges, colors: [0, 1, -1, -1], highlight: [], ok: null,
        msg: lang === 'vi' ? `Đỉnh 2 kề đỉnh 1 ⇒ dùng màu ${cn[1]}.` : `Vertex 2 touches 1 ⇒ use ${cn[1]}.`,
      },
      {
        nodes, edges, colors: [0, 1, 2, -1], highlight: [], ok: null,
        msg: lang === 'vi' ? `Đỉnh 3 kề 1 và 2 ⇒ dùng màu ${cn[2]}.` : `Vertex 3 touches 1 & 2 ⇒ use ${cn[2]}.`,
      },
      {
        nodes, edges, colors: [0, 1, 2, 3], highlight: [[0, 3], [1, 3], [2, 3]], ok: false,
        msg: lang === 'vi'
          ? `Đỉnh 4 kề cả 3 màu (${cn[0]}, ${cn[1]}, ${cn[2]}) ⇒ 3 màu thất bại, buộc dùng màu thứ 4 (${cn[3]})!`
          : `Vertex 4 touches all 3 colors ⇒ 3 colors fail, forced to use color 4 (${cn[3]})!`,
      },
    ];
  }

  // Kempe chain demos on degree-5 hub u (index 0) with neighbors 1..5 (indices 1..5)
  const nodes = [{ id: 'u', x: 240, y: 140 }];
  for (let k = 0; k < 5; k++) {
    const ang = -Math.PI / 2 + (k * 2 * Math.PI) / 5;
    nodes.push({ id: String(k + 1), x: 240 + 95 * Math.cos(ang), y: 140 + 95 * Math.sin(ang) });
  }
  const edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]];

  if (presetKey === 'kempeFree') {
    return [
      {
        nodes, edges, colors: [-1, 0, 1, 2, 3, 4], highlight: [], ok: null,
        msg: lang === 'vi'
          ? 'Đỉnh u (bậc 5) có 5 láng giềng dùng đủ 5 màu. Cần giải phóng 1 màu cho u.'
          : 'Degree-5 vertex u has 5 neighbors using all 5 colors. Need to free 1 color.',
      },
      {
        nodes, edges, colors: [-1, 2, 1, 2, 3, 4], highlight: [[0, 1]], ok: null,
        msg: lang === 'vi'
          ? `TH1: Thành phần ${cn[0]}–${cn[2]} từ đỉnh 1 không nối tới 3 ⇒ đổi màu đỉnh 1 sang ${cn[2]}.`
          : `Case 1: ${cn[0]}–${cn[2]} chain from 1 misses 3 ⇒ swap 1 to ${cn[2]}.`,
      },
      {
        nodes, edges, colors: [0, 2, 1, 2, 3, 4], highlight: [], ok: true,
        msg: lang === 'vi'
          ? `Màu ${cn[0]} đã trống! Tô đỉnh u bằng ${cn[0]} hoàn tất.`
          : `${cn[0]} is now free! Color u with ${cn[0]}.`,
      },
    ];
  }

  // kempeBarrier
  const edgesBar = [...edges, [1, 3]];
  return [
    {
      nodes, edges: edgesBar, colors: [-1, 0, 1, 2, 3, 4], highlight: [], ok: null,
      msg: lang === 'vi'
        ? 'Đỉnh u (bậc 5) có 5 láng giềng dùng đủ 5 màu.'
        : 'Degree-5 vertex u has 5 neighbors using all 5 colors.',
    },
    {
      nodes, edges: edgesBar, colors: [-1, 0, 1, 2, 3, 4], highlight: [[1, 3]], ok: null,
      msg: lang === 'vi'
        ? `TH2: Xích ${cn[0]}–${cn[2]} nối thông đỉnh 1 và 3 ⇒ tạo rào chắn tách rời đỉnh 2 khỏi đỉnh 4!`
        : `Case 2: ${cn[0]}–${cn[2]} chain connects 1 and 3 ⇒ creates a barrier separating 2 from 4!`,
    },
    {
      nodes, edges: edgesBar, colors: [-1, 0, 3, 2, 3, 4], highlight: [[1, 3], [0, 2]], ok: null,
      msg: lang === 'vi'
        ? `Do bị chắn, thành phần ${cn[1]}–${cn[3]} từ đỉnh 2 không chạm đỉnh 4 ⇒ đổi 2 sang ${cn[3]}.`
        : `Blocked by the barrier, ${cn[1]}–${cn[3]} from 2 misses 4 ⇒ swap 2 to ${cn[3]}.`,
    },
    {
      nodes, edges: edgesBar, colors: [1, 0, 3, 2, 3, 4], highlight: [[1, 3]], ok: true,
      msg: lang === 'vi'
        ? `Màu ${cn[1]} đã trống! Tô đỉnh u bằng ${cn[1]} hoàn tất.`
        : `${cn[1]} is now free! Color u with ${cn[1]}.`,
    },
  ];
}
