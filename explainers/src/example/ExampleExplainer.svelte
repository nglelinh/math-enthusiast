<script>
  // Svelte 5 runes. Visible UI text in Vietnamese; label it "Minh hoạ", never "Explainer".
  import * as d3 from 'd3';
  import Stepper from '../shared/Stepper.svelte';
  import { PRESETS, steps } from './example.js';

  let { preset = 'sum', n: nProp = 6 } = $props();
  let pid = $state(PRESETS.some((p) => p.id === preset) ? preset : 'sum');
  let n = $state(Number(nProp) || 6);
  let step = $state(0);
  $effect(() => { pid; n; step = 0; });          // reset when inputs change

  const P = $derived(PRESETS.find((p) => p.id === pid));
  const S = $derived(steps(pid, n));
  const cur = $derived(S[Math.min(step, S.length - 1)]);

  // D3 for scales/paths; Svelte owns the DOM (no d3.select needed for simple charts).
  const W = 520, H = 220, M = 28;
  const x = $derived(d3.scaleBand().domain(S.map((s) => s.k)).range([M, W - M]).padding(0.15));
  const y = $derived(d3.scaleLinear().domain([0, S.at(-1)?.acc ?? 1]).range([H - M, M]));
</script>

<div class="dx">
  <h4>Minh hoạ: tổng dồn và công thức đóng</h4>
  <p class="dx-help">Chọn dãy, bấm <b>Bước tiếp</b> để cộng từng số hạng và so với công thức {P.formula}.</p>
  <div class="dx-bar">
    <label>Dãy <select bind:value={pid}>{#each PRESETS as p}<option value={p.id}>{p.name}</option>{/each}</select></label>
    <label>n = <b>{n}</b> <input type="range" min="2" max="12" bind:value={n} /></label>
  </div>
  <Stepper bind:step total={S.length} />
  <div class="dx-msg">
    k = {cur.k}: cộng thêm {cur.term}, tổng = <b>{cur.acc}</b>; công thức cho {cur.closed}
    <span class={cur.ok ? 'dx-ok' : 'dx-bad'}>{cur.ok ? '✓ khớp' : '✗ lệch'}</span>
  </div>
  <svg class="dx-svg" viewBox="0 0 {W} {H}" role="img" aria-label="Biểu đồ tổng dồn">
    {#each S as s, i}
      <rect x={x(s.k)} y={y(s.acc)} width={x.bandwidth()} height={H - M - y(s.acc)}
            fill={i === step ? '#f59e0b' : i < step ? '#60a5fa' : '#e2e8f0'} rx="3" />
      <text x={x(s.k) + x.bandwidth() / 2} y={H - 8} text-anchor="middle" font-size="11">{s.k}</text>
    {/each}
  </svg>
</div>
