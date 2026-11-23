<script>
  import { PRESETS, sinkhorn } from './ot.js';

  let { preset: initPreset = 'threeBars', lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let pExp = $state(2);
  let eps = $state(0.25);

  const res = $derived(sinkhorn(preset, pExp, eps, 35));

  const xPos = (val) => 70 + (val - 0.5) * 85;
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Vận chuyển tối ưu 1D & chuẩn hóa Sinkhorn' : 'Interactive: 1D Optimal Transport & Sinkhorn'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'Chọn bài toán tách khối lượng hoặc 3 nguồn→3 đích, chỉnh ε để xem ma trận coupling sắc nét dần.'
      : 'Switch between mass-splitting and 3→3 transport, and adjust ε to see the coupling sharpen.'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <label>
      p = {pExp}
      <select bind:value={pExp}>
        <option value={1}>L1 (|x−y|)</option>
        <option value={2}>L2 (|x−y|²)</option>
      </select>
    </label>
    <label>
      ε = {eps.toFixed(2)}
      <input type="range" min="0.04" max="1.50" step="0.02" bind:value={eps} />
    </label>
    <span class="dx-pill">Cost = {res.cost.toFixed(3)}</span>
  </div>

  <svg class="dx-svg" viewBox="0 0 480 230">
    {#each res.preset.x as xi, i}
      {#each res.preset.y as yj, j}
        {@const w = res.plan[i][j]}
        {#if w > 0.01}
          <line
            x1={xPos(xi)} y1="68"
            x2={xPos(yj)} y2="165"
            stroke="#ffd166"
            stroke-width={Math.max(1.2, w * 14)}
            stroke-opacity={Math.min(0.95, 0.25 + w)}
          />
          <text x={(xPos(xi) + xPos(yj)) / 2} y="118" text-anchor="middle" fill="#ffd166" font-size="11" font-weight="600">
            {w.toFixed(2)}
          </text>
        {/if}
      {/each}
    {/each}

    {#each res.preset.x as xi, i}
      <rect x={xPos(xi) - 18} y={62 - res.preset.a[i] * 42} width="36" height={res.preset.a[i] * 42} rx="4" fill="#4cc9f0" />
      <text x={xPos(xi)} y="78" text-anchor="middle" fill="#e5e7eb" font-size="12">x={xi} ({res.preset.a[i]})</text>
    {/each}

    {#each res.preset.y as yj, j}
      <rect x={xPos(yj) - 18} y="168" width="36" height={res.preset.b[j] * 42} rx="4" fill="#80ed99" />
      <text x={xPos(yj)} y="160" text-anchor="middle" fill="#e5e7eb" font-size="12">y={yj} ({res.preset.b[j]})</text>
    {/each}
  </svg>
</div>
