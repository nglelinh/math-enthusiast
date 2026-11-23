<script>
  import Stepper from '../shared/Stepper.svelte';
  import { COLORS, PRESETS, heawood, steps } from './fourcolor.js';

  let { preset: initPreset = 'k4', lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let genus = $state(1);
  let step = $state(0);

  const trace = $derived(steps(preset, lang));
  const cur = $derived(trace[Math.min(step, trace.length - 1)]);
  const hVal = $derived(heawood(genus));

  $effect(() => {
    preset;
    step = 0;
  });

  function isHighlighted(u, v) {
    return cur.highlight.some(([a, b]) => (a === u && b === v) || (a === v && b === u));
  }
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Tô màu bản đồ, xích Kempe & số Heawood' : 'Interactive: Map Coloring, Kempe Chains & Heawood Number'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'Chạy từng bước K₄ hoặc hai trường hợp xích Kempe, và kéo thanh giống mặt g để tính H(g).'
      : 'Step through K₄ or both Kempe-chain cases, and slide surface genus g to compute H(g).'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <label>
      {lang === 'vi' ? 'Giống mặt' : 'Genus'} g = {genus}
      <input type="range" min="0" max="10" step="1" bind:value={genus} />
    </label>
    <span class="dx-pill">H({genus}) = {hVal} {lang === 'vi' ? 'màu' : 'colors'}</span>
  </div>

  <Stepper bind:step total={trace.length} />

  <div class="dx-msg">
    {cur.msg}
    {#if cur.ok === true}
      <span class="dx-ok" style="margin-left:8px;">OK</span>
    {:else if cur.ok === false}
      <span class="dx-bad" style="margin-left:8px;">{lang === 'vi' ? '3 màu thất bại' : '3 colors fail'}</span>
    {/if}
  </div>

  <svg class="dx-svg" viewBox="0 0 480 265">
    {#each cur.edges as [u, v]}
      {@const hi = isHighlighted(u, v)}
      <line
        x1={cur.nodes[u].x} y1={cur.nodes[u].y}
        x2={cur.nodes[v].x} y2={cur.nodes[v].y}
        stroke={hi ? '#ffd166' : '#5c6478'}
        stroke-width={hi ? 4.5 : 2.2}
        stroke-dasharray={hi ? 'none' : '4 3'}
      />
    {/each}
    {#each cur.nodes as nd, i}
      {@const cIdx = cur.colors[i]}
      {@const fill = cIdx >= 0 ? COLORS[cIdx] : '#1d2130'}
      <circle cx={nd.x} cy={nd.y} r="20" fill={fill} stroke="#e5e7eb" stroke-width="2.5" />
      <text x={nd.x} y={nd.y + 5} text-anchor="middle" fill={cIdx >= 0 ? '#111827' : '#fff'} font-size="15" font-weight="700">{nd.id}</text>
    {/each}
  </svg>
</div>
