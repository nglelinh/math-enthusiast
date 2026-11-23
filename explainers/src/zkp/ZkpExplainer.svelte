<script>
  import Stepper from '../shared/Stepper.svelte';
  import { EDGES, NODES, PALETTE, PRESETS, catchProbability, steps } from './zkp.js';

  let { preset: initPreset = 'honest', lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let permIdx = $state(1);
  let challengeIdx = $state(3);
  let roundsK = $state(20);
  let step = $state(0);

  const trace = $derived(steps(preset, permIdx, challengeIdx, lang));
  const cur = $derived(trace[Math.min(step, trace.length - 1)]);
  const pCatch = $derived((catchProbability(roundsK) * 100).toFixed(1));

  $effect(() => {
    preset; permIdx; challengeIdx;
    step = 0;
  });

  function newRound() {
    permIdx = (permIdx + 1) % 6;
    challengeIdx = (challengeIdx + 2) % EDGES.length;
  }
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Chứng minh không tiết lộ (3-tô màu)' : 'Interactive: Zero-Knowledge Proof (3-Coloring)'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'Thử chế độ Trung thực vs Gian dối, chọn cạnh thách thức và bấm Thử vòng mới.'
      : 'Switch between Honest vs Cheater, pick a challenge edge, and test new random rounds.'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <label>
      {lang === 'vi' ? 'Cạnh thách thức' : 'Challenge'}
      <select bind:value={challengeIdx}>
        {#each EDGES as [u, v], i}
          <option value={i}>({u + 1}, {v + 1})</option>
        {/each}
      </select>
    </label>
    <button class="sec" onclick={newRound}>{lang === 'vi' ? '🎲 Thử vòng mới' : '🎲 New round'}</button>
  </div>

  <div class="dx-bar">
    <label>
      {lang === 'vi' ? 'Số vòng lặp' : 'Rounds'} k = {roundsK}
      <input type="range" min="1" max="50" step="1" bind:value={roundsK} />
    </label>
    <span class="dx-pill">
      {lang === 'vi' ? `Xác suất bắt kẻ gian ≥ ${pCatch}%` : `Catch probability ≥ ${pCatch}%`}
    </span>
  </div>

  <Stepper bind:step total={trace.length} />

  <div class="dx-msg">
    {cur.msg}
    {#if cur.ok === true}
      <span class="dx-ok" style="margin-left:8px;">{lang === 'vi' ? 'Hợp lệ' : 'Accepted'}</span>
    {:else if cur.ok === false}
      <span class="dx-bad" style="margin-left:8px;">{lang === 'vi' ? 'Từ chối' : 'Rejected'}</span>
    {/if}
  </div>

  <svg class="dx-svg" viewBox="0 0 480 275">
    {#each EDGES as [u, v], idx}
      {@const isCh = idx === cur.challengeEdge}
      <line
        x1={NODES[u].x} y1={NODES[u].y}
        x2={NODES[v].x} y2={NODES[v].y}
        stroke={isCh ? '#80ed99' : '#5c6478'}
        stroke-width={isCh ? 5 : 2.5}
      />
    {/each}
    {#each NODES as nd, i}
      {@const locked = cur.locked[i]}
      {@const col = locked ? '#1d2130' : PALETTE[cur.visibleColors[i]]}
      <circle cx={nd.x} cy={nd.y} r="22" fill={col} stroke={locked ? '#7b8294' : '#ffffff'} stroke-width="2.5" />
      <text x={nd.x} y={nd.y + 5} text-anchor="middle" fill={locked ? '#9ca3af' : '#111827'} font-size="15" font-weight="700">
        {locked ? '🔒' : nd.id}
      </text>
    {/each}
  </svg>
</div>
