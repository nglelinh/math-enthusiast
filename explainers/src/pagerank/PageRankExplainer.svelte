<script>
  import * as d3 from 'd3';
  import Stepper from '../shared/Stepper.svelte';
  import { PRESETS, steps } from './pagerank.js';

  let { preset: initPreset = 'dangling', alpha: initAlpha = 0.85, lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let alpha = $state(Number(initAlpha));
  let fixDangling = $state(true);
  let step = $state(0);

  const trace = $derived(steps(preset, alpha, fixDangling, lang, 20));
  const cur = $derived(trace[Math.min(step, trace.length - 1)]);
  const graph = $derived(PRESETS[preset] || PRESETS.dangling);

  $effect(() => {
    preset; alpha; fixDangling;
    step = 0;
  });

  const POS = [
    { x: 60,  y: 70 },
    { x: 185, y: 70 },
    { x: 122, y: 165 },
    { x: 205, y: 215 },
  ];

  const yScale = d3.scaleLinear().domain([0, 0.55]).range([205, 35]);
  const barX = [285, 340, 395, 450];
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Lặp lũy thừa PageRank & bẫy nút cụt' : 'Interactive: PageRank Power Iteration & Dead-End Trap'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'Đổi hệ số teleport α hoặc tắt chế độ sửa nút cụt D để xem phân phối dừng thay đổi.'
      : 'Adjust teleport α or toggle dead-end D repair to watch the stationary distribution.'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <label>
      α = {alpha.toFixed(2)}
      <input type="range" min="0.10" max="0.99" step="0.01" bind:value={alpha} />
    </label>
    <label>
      <input type="checkbox" bind:checked={fixDangling} />
      {lang === 'vi' ? 'Sửa nút cụt (1/4)' : 'Fix dead-end (1/4)'}
    </label>
  </div>

  <Stepper bind:step total={trace.length} />

  <div class="dx-msg">
    {cur.msg}
    <span class={cur.sum > 0.99 ? 'dx-ok' : 'dx-bad'} style="margin-left:8px;">
      Σπ = {cur.sum.toFixed(3)}
    </span>
  </div>

  <svg class="dx-svg" viewBox="0 0 510 250">
    <defs>
      <marker id="pr-arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#7b8294" />
      </marker>
    </defs>

    {#each graph.edges as [u, v]}
      {@const dx = POS[v].x - POS[u].x}
      {@const dy = POS[v].y - POS[u].y}
      {@const len = Math.hypot(dx, dy) || 1}
      {@const ux = dx / len}
      {@const uy = dy / len}
      {@const off = (u === 0 && v === 2) || (u === 2 && v === 0) ? 6 : 0}
      {@const px = -uy * off}
      {@const py = ux * off}
      <line
        x1={POS[u].x + ux * 20 + px} y1={POS[u].y + uy * 20 + py}
        x2={POS[v].x - ux * 22 + px} y2={POS[v].y - uy * 22 + py}
        stroke="#7b8294" stroke-width="2" marker-end="url(#pr-arr)"
      />
    {/each}

    {#each graph.nodes as name, i}
      {@const r = 15 + cur.pi[i] * 26}
      {@const isDangling = i === graph.danglingIdx}
      <circle cx={POS[i].x} cy={POS[i].y} r={r} fill={isDangling ? '#3b1f2b' : '#1d2130'} stroke={isDangling ? '#ff7eb6' : '#4cc9f0'} stroke-width="2.5" />
      <text x={POS[i].x} y={POS[i].y + 5} text-anchor="middle" fill="#fff" font-size="14" font-weight="700">{name}</text>
    {/each}

    <line x1="270" y1="205" x2="490" y2="205" stroke="#4a5064" stroke-width="1.5" />
    {#each graph.nodes as name, i}
      {@const topY = yScale(Math.min(0.55, cur.pi[i]))}
      {@const h = Math.max(2, 205 - topY)}
      <rect x={barX[i]} y={topY} width="34" height={h} rx="4" fill={i === 0 ? '#ffd166' : i === 2 ? '#80ed99' : '#4cc9f0'} />
      <text x={barX[i] + 17} y={topY - 6} text-anchor="middle" fill="#e5e7eb" font-size="11">{cur.pi[i].toFixed(3)}</text>
      <text x={barX[i] + 17} y="224" text-anchor="middle" fill="#9ca3af" font-size="13" font-weight="600">{name}</text>
    {/each}
  </svg>
</div>
