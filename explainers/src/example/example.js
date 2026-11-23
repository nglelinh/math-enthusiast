// Pure logic only (no Svelte, no DOM) so it can be unit-tested with `node --test`.
// Every number the UI shows should come from here, never be typed by hand in the component.

export const PRESETS = [
  { id: 'sum', name: '1 + 2 + … + n', term: (k) => k, closed: (n) => (n * (n + 1)) / 2, formula: 'n(n + 1)/2' },
  { id: 'odd', name: '1 + 3 + … + (2n − 1)', term: (k) => 2 * k - 1, closed: (n) => n * n, formula: 'n²' }
];

/** Steps of the walkthrough: one entry per added term. */
export function steps(presetId, n) {
  const P = PRESETS.find((p) => p.id === presetId) ?? PRESETS[0];
  const out = [];
  let acc = 0;
  for (let k = 1; k <= n; k++) {
    acc += P.term(k);
    out.push({ k, term: P.term(k), acc, closed: P.closed(k), ok: acc === P.closed(k) });
  }
  return out;
}
