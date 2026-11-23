<script>
  import Stepper from '../shared/Stepper.svelte';
  import { PRESETS, steps } from './cantor.js';

  let { preset: initPreset = 'safeFlip', lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let step = $state(0);

  const trace = $derived(steps(preset, lang));
  const cur = $derived(trace[Math.min(step, trace.length - 1)]);
  const pr = $derived(PRESETS[preset] || PRESETS.safeFlip);

  $effect(() => {
    preset;
    step = 0;
  });
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Chứng minh đường chéo Cantor (ℝ không đếm được)' : 'Interactive: Cantor’s Diagonal Argument'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'Bước qua từng hàng để dựng số y ∈ (0, 1) khác mọi số trong danh sách bằng cách lật chữ số đường chéo sang {1, 2}.'
      : 'Step down the diagonal to build y ∈ (0, 1) differing from every row using only digits {1, 2}.'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <span class="dx-pill">
      y = {lang === 'vi' ? '0,' : '0.'}{cur.built.join('')}{cur.built.length < pr.rows.length ? '…' : '…'}
    </span>
  </div>

  <Stepper bind:step total={trace.length} />

  <div class="dx-msg">{cur.msg}</div>

  <svg class="dx-svg" viewBox="0 0 420 235">
    {#each pr.rows as row, r}
      {@const y = 26 + r * 30}
      {@const isRowDone = r <= cur.activeRow}
      <text x="24" y={y + 15} fill={r === cur.activeRow ? '#ffd166' : '#9ca3af'} font-size="13" font-weight="600">
        x{r + 1} = 0{lang === 'vi' ? ',' : '.'}
      </text>
      {#each row as d, c}
        {@const x = 92 + c * 36}
        {@const isDiag = r === c}
        <rect x={x} y={y - 2} width="28" height="24" rx="5"
          fill={isDiag ? (isRowDone ? '#ffd166' : '#2b3350') : '#161b26'}
          stroke={isDiag ? '#ffd166' : '#2d3748'} stroke-width={isDiag ? 2 : 1} />
        <text x={x + 14} y={y + 15} text-anchor="middle"
          fill={isDiag && isRowDone ? '#111827' : '#e5e7eb'} font-size="13" font-weight="700">{d}</text>
      {/each}
    {/each}

    <text x="335" y="45" fill="#80ed99" font-size="13" font-weight="700">{lang === 'vi' ? 'Số mới y:' : 'New y:'}</text>
    <text x="335" y="72" fill="#80ed99" font-size="16" font-weight="700">
      0{lang === 'vi' ? ',' : '.'}{cur.built.join('')}
    </text>
  </svg>
</div>
