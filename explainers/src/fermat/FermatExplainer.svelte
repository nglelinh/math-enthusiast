<script>
  import Stepper from '../shared/Stepper.svelte';
  import { PRESETS, checkFermat, steps } from './fermat.js';

  let { preset: initPreset = 'frey', lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let step = $state(0);

  const trace = $derived(steps(preset, lang));
  const cur = $derived(trace[Math.min(step, trace.length - 1)]);
  const pr = $derived(PRESETS[preset] || PRESETS.frey);
  const chk = $derived(checkFermat(pr.a, pr.b, pr.c, pr.n));

  $effect(() => {
    preset;
    step = 0;
  });

  const STAGES = {
    vi: ['aᵖ + bᵖ = cᵖ', 'Đường cong Frey E', 'Hạ bậc Ribet (N=2)', 'Wiles: E modular ⇒ ⊥'],
    en: ['aᵖ + bᵖ = cᵖ', 'Frey curve E', 'Ribet level N=2', 'Wiles: E modular ⇒ ⊥'],
  };
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Chiến lược Wiles–Fermat & kiểm tra số mũ' : 'Interactive: Wiles–Fermat Proof Strategy & Exponent Check'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'So sánh n = 2 (Pytago) với n = 12 (suýt đúng) và chạy 4 bước chứng minh phản chứng của Wiles.'
      : 'Compare n = 2 (Pythagoras) vs n = 12 (near-miss) and step through Wiles’s 4-stage proof.'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <span class={chk.eq ? 'dx-ok' : 'dx-bad'}>
      {pr.a}^{pr.n} + {pr.b}^{pr.n} {chk.eq ? '=' : '≠'} {pr.c}^{pr.n}
    </span>
  </div>

  <Stepper bind:step total={trace.length} />

  <div class="dx-msg">{cur.msg}</div>

  <svg class="dx-svg" viewBox="0 0 520 120">
    {#each (STAGES[lang] || STAGES.vi) as lbl, i}
      {@const x = 14 + i * 126}
      {@const active = preset === 'frey' ? i <= cur.stage : i === 0}
      <rect x={x} y="28" width="112" height="58" rx="10"
        fill={active ? '#1d2130' : '#121520'}
        stroke={active ? (i === 3 ? '#80ed99' : '#4cc9f0') : '#374151'}
        stroke-width={active ? 2.5 : 1.5} />
      <text x={x + 56} y="62" text-anchor="middle" fill={active ? '#fff' : '#6b7280'} font-size="11.5" font-weight="600">{lbl}</text>
      {#if i < 3}
        <line x1={x + 114} y1="57" x2={x + 124} y2="57" stroke="#7b8294" stroke-width="2" />
      {/if}
    {/each}
  </svg>
</div>
