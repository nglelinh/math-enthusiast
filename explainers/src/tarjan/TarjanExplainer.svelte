<script>
  import Stepper from '../shared/Stepper.svelte';
  import { PRESETS, SCC_COLORS, steps } from './tarjan.js';

  let { preset: initPreset = 'sixNode', lang = 'vi' } = $props();
  let preset = $state(initPreset);
  let step = $state(0);

  const trace = $derived(steps(preset, lang));
  const cur = $derived(trace[Math.min(step, trace.length - 1)]);
  const graph = $derived(PRESETS[preset] || PRESETS.sixNode);

  $effect(() => {
    preset;
    step = 0;
  });
</script>

<div class="dx">
  <h4>{lang === 'vi' ? 'Minh hoạ: Thuật toán Tarjan tìm thành phần liên thông mạnh (SCC)' : 'Interactive: Tarjan’s Strongly Connected Components (SCC)'}</h4>
  <p class="dx-help">
    {lang === 'vi'
      ? 'Bấm Bước tiếp để xem cặp (disc, low), ngăn xếp và các SCC được tách ra sau một lần duyệt DFS.'
      : 'Step through DFS to watch (disc, low), the active stack, and popped SCCs.'}
  </p>

  <div class="dx-bar">
    <select bind:value={preset}>
      {#each Object.entries(PRESETS) as [k, p]}
        <option value={k}>{p.label[lang] || p.label.vi}</option>
      {/each}
    </select>
    <span class="dx-pill">
      Stack: [{cur.stack.map((i) => graph.names[i]).join(', ')}]
    </span>
    <span class="dx-pill">
      SCC: {cur.sccs.map((c) => '{' + c.map((i) => graph.names[i]).join(',') + '}').join('  ') || '∅'}
    </span>
  </div>

  <Stepper bind:step total={trace.length} />

  <div class="dx-msg">{cur.msg}</div>

  <svg class="dx-svg" viewBox="0 0 460 270">
    <defs>
      <marker id="tj-arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#7b8294" />
      </marker>
    </defs>

    {#each graph.adj as vs, u}
      {#each vs as v}
        {@const dx = graph.pos[v].x - graph.pos[u].x}
        {@const dy = graph.pos[v].y - graph.pos[u].y}
        {@const len = Math.hypot(dx, dy) || 1}
        {@const ux = dx / len}
        {@const uy = dy / len}
        {@const isAct = cur.activeEdge && cur.activeEdge[0] === u && cur.activeEdge[1] === v}
        {@const bidir = graph.adj[v].includes(u)}
        {@const off = bidir ? 5 : 0}
        {@const px = -uy * off}
        {@const py = ux * off}
        <line
          x1={graph.pos[u].x + ux * 20 + px} y1={graph.pos[u].y + uy * 20 + py}
          x2={graph.pos[v].x - ux * 22 + px} y2={graph.pos[v].y - uy * 22 + py}
          stroke={isAct ? '#ffd166' : '#64748b'}
          stroke-width={isAct ? 4 : 2.2}
          marker-end="url(#tj-arr)"
        />
      {/each}
    {/each}

    {#each graph.names as nm, i}
      {@const cid = cur.sccOf[i]}
      {@const fill = cid >= 0 ? SCC_COLORS[cid % SCC_COLORS.length] : (cur.onStack[i] ? '#2b3350' : '#1d2130')}
      {@const stroke = cur.activeNode === i ? '#ffd166' : (cid >= 0 ? fill : '#4cc9f0')}
      <circle cx={graph.pos[i].x} cy={graph.pos[i].y} r="20" fill={fill} stroke={stroke} stroke-width={cur.activeNode === i ? 4 : 2.5} />
      <text x={graph.pos[i].x} y={graph.pos[i].y + 5} text-anchor="middle" fill={cid >= 0 ? '#111827' : '#fff'} font-size="14" font-weight="700">{nm}</text>
      {#if cur.disc[i] >= 0}
        <text x={graph.pos[i].x} y={graph.pos[i].y + 34} text-anchor="middle" fill="#ffd166" font-size="12" font-weight="600">
          ({cur.disc[i]}, {cur.low[i]})
        </text>
      {/if}
    {/each}
  </svg>
</div>
