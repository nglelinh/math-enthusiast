export const PRESETS = {
  threeBars: {
    label: { vi: '3 nguồn → 3 đích (vận chuyển 1D)', en: '3 sources → 3 targets (1D transport)' },
    x: [1, 2, 4],
    a: [0.5, 0.3, 0.2],
    y: [2, 4, 5],
    b: [0.2, 0.5, 0.3],
  },
  mongeSplit: {
    label: { vi: 'Tách khối lượng (Monge thất bại, Kantorovich thắng)', en: 'Mass splitting (Monge fails, Kantorovich succeeds)' },
    x: [2],
    a: [1.0],
    y: [1, 3],
    b: [0.5, 0.5],
  },
};

export function sinkhorn(presetKey = 'threeBars', p = 2, eps = 0.25, iters = 30) {
  const pr = PRESETS[presetKey] || PRESETS.threeBars;
  const m = pr.x.length;
  const n = pr.y.length;
  const C = pr.x.map((xi) => pr.y.map((yj) => Math.pow(Math.abs(xi - yj), p)));
  const K = C.map((row) => row.map((c) => Math.exp(-c / Math.max(0.03, eps))));
  let u = Array(m).fill(1);
  let v = Array(n).fill(1);

  for (let it = 0; it < iters; it++) {
    for (let i = 0; i < m; i++) {
      let s = 0;
      for (let j = 0; j < n; j++) s += K[i][j] * v[j];
      u[i] = pr.a[i] / (s || 1e-12);
    }
    for (let j = 0; j < n; j++) {
      let s = 0;
      for (let i = 0; i < m; i++) s += K[i][j] * u[i];
      v[j] = pr.b[j] / (s || 1e-12);
    }
  }

  const plan = Array.from({ length: m }, (_, i) =>
    Array.from({ length: n }, (__, j) => u[i] * K[i][j] * v[j])
  );
  let cost = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) cost += plan[i][j] * C[i][j];
  }
  return { preset: pr, C, plan, cost };
}
