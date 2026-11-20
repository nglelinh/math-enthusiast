/**
 * Interactive explainers for math-enthusiast (EN + VI, touch friendly, no dependencies)
 *   collatz   : Collatz orbit tracer             (chapter 01)
 *   logistic  : logistic map + bifurcation       (chapter 04, Chaos)
 *   fourier   : Fourier partial sums + Gibbs     (chapter 03)
 *   chaosgame : chaos game on a polygon          (chapter 04, Fractals)
 *   konigsberg: degree counter / bridge walker   (chapter 05)
 * Usage: <div class="mex-explainer" data-mex="collatz" data-lang="en"></div>
 * Each explainer is a no-op when its container is absent.
 */
(function () {
    'use strict';
    var PI = Math.PI;
    var COL = { sun: '#ffd166', sky: '#4cc9f0', mint: '#80ed99', pink: '#ff7eb6', orange: '#ff9f43', dim: '#7b8294', card: '#1d2130', bg: '#0b0d14' };

    var CSS = [
        '.mex{max-width:640px;margin:1.5rem auto;padding:14px;border-radius:14px;background:#10121a;border:1px solid #2a3045;color:#e8ebf5;font-family:inherit;line-height:1.45;box-sizing:border-box;text-align:left}',
        '.mex *{box-sizing:border-box}',
        '.mex h4{margin:0 0 10px;font-size:1.1rem;color:#ffd166;text-align:center;border:0;padding:0}',
        '.mex canvas{width:100%;display:block;border-radius:10px;background:#0b0d14;margin:6px 0}',
        '.mex svg{width:100%;height:auto;display:block;border-radius:10px;background:#0b0d14;margin:6px 0}',
        '.mex button{min-height:44px;min-width:44px;border:1px solid #4a5896;border-radius:10px;padding:8px 12px;font-size:1rem;font-weight:700;font-family:inherit;cursor:pointer;background:#2f3a66;color:#fff;touch-action:manipulation;-webkit-tap-highlight-color:transparent}',
        '.mex button.on{background:#ffd166;color:#10121a;border-color:#ffd166}',
        '.mex button:disabled{opacity:.4;cursor:not-allowed}',
        '.mex button:focus-visible,.mex input:focus-visible{outline:3px solid #ffd166;outline-offset:2px}',
        '.mex input[type=number]{min-height:44px;width:8em;font-size:1rem;border-radius:10px;border:1px solid #4a5896;background:#1d2130;color:#fff;padding:0 10px;font-family:inherit}',
        '.mex input[type=range]{width:100%;min-height:44px;accent-color:#ffd166;margin:0}',
        '.mex label{font-weight:600}',
        '.mex-row{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;align-items:center;margin:8px 0}',
        '.mex-stats{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:6px 0}',
        '.mex-stats div{background:#1d2130;border-radius:10px;padding:6px 10px;text-align:center;min-width:5.6em;font-size:.85rem;color:#9aa3bd}',
        '.mex-stats b{display:block;font-size:1.3rem;color:#fff}',
        '.mex-msg{text-align:center;font-weight:600;min-height:2.9em;margin:6px 0;color:#e8ebf5}',
        '.mex-ok{color:#80ed99!important}.mex-bad{color:#ff7eb6!important}.mex-warn{color:#ffd166!important}',
        '.mex-note{color:#9aa3bd;font-size:.88rem;text-align:center;margin:4px 0}',
        '.mex-seq{font-family:monospace;font-size:.9rem;color:#cfd6ee;word-break:break-word;text-align:center;margin:4px 0}',
        '.mex-slide{margin:6px 0}',
        '.mex-slide .t{display:flex;justify-content:space-between;gap:8px;font-weight:600}',
        '.mex-slide .t span+span{color:#ffd166}'
    ].join('\n');

    var I18N = {
        en: {
            col_title: 'Collatz tracer', col_start: 'Start number', col_go: 'Trace', col_rand: 'Random', col_log: 'Log scale', col_lin: 'Linear scale',
            col_steps: 'steps to reach 1', col_peak: 'highest value', col_up: 'times 3n+1', col_down: 'halvings',
            col_rule: 'Even: halve it. Odd: triple it and add 1.', col_bad: 'Please enter a whole number from 1 to 1,000,000.',
            col_one: '1 is already at the end: 0 steps.', col_done: function (n, s, p) { return 'Start ' + n + ': it takes ' + s + ' steps and climbs as high as ' + p + ' before reaching 1.'; },
            col_open: 'Nobody has found a start that never reaches 1, but nobody has proved it.', col_try: 'Try:',
            log_title: 'Logistic map explorer', log_r: 'Growth rate r', log_x: 'Starting value', log_two: 'Second orbit starting 0.0001 higher', log_orbit: 'Orbits over time', log_bif: 'Where r sits in the bifurcation diagram',
            log_fixed: function (x) { return 'The orbit settles on a single value, about ' + x + '.'; },
            log_cycle: function (p) { return 'The orbit settles into a cycle of ' + p + ' values.'; },
            log_chaos: 'No repeating cycle: chaotic. Nearby starts drift apart.',
            log_note: 'Bifurcation diagram: each vertical slice shows where the orbit lives after a long time.',
            fou_title: 'Fourier partial sums', fou_square: 'Square', fou_saw: 'Sawtooth', fou_tri: 'Triangle', fou_n: 'Number of sine waves', fou_play: '\u25B6 Add waves', fou_stop: '\u25A0 Stop',
            fou_terms: 'sine waves', fou_over: 'overshoot', fou_none: 'none', fou_over_note: function (p) { return 'However many waves you add, the overshoot at the jump never disappears: it settles near ' + p + ' of the step height (the Gibbs effect).'; },
            fou_smooth: 'The triangle wave has no jump, so there is no overshoot: its sine waves shrink like 1/k\u00B2.', fou_target: 'target', fou_sum: 'sum',
            cg_title: 'Chaos game', cg_corners: 'Corners', cg_jump: 'Jump fraction', cg_add: 'Add 100', cg_add5: 'Add 5,000', cg_run: '\u25B6 Run', cg_pause: '\u25A0 Pause', cg_clear: 'Clear', cg_points: 'points',
            cg_pre: 'Presets:', cg_tri: 'Triangle \u00BD', cg_sq: 'Square \u00BD', cg_pent: 'Pentagon 0.618', cg_hex: 'Hexagon \u2154',
            cg_dim: function (c, d) { return 'Each copy shrinks by c = ' + c + '. Copies do not overlap, so the pattern has dimension ln n / ln(1/c) = ' + d + '.'; },
            cg_over: function (c) { return 'Each copy shrinks by c = ' + c + ', which is too big: the copies overlap and the picture fills in.'; },
            cg_rule: 'Rule: pick a random corner, jump that fraction of the way toward it, and plot.',
            kb_title: 'Bridges and degrees', kb_walk: 'Walk', kb_build: 'Edit bridges', kb_reset: 'Reset', kb_deg: 'degree', kb_odd: 'Dots with an odd number of bridges',
            kb_walk_help: 'Tap a dot to start, then tap bridges to cross. Each bridge once only.', kb_build_help: 'Tap a bridge to remove it or put it back.',
            kb_pick: 'Tap a dot to start walking.', kb_far: 'Tap a bridge that touches the dot you are on.', kb_used: 'That bridge is already crossed.', kb_gone: 'That bridge was removed.',
            kb_stuck: function (k) { return 'Stuck! ' + k + ' bridge' + (k === 1 ? '' : 's') + ' left uncrossed.'; }, kb_win: 'You crossed every bridge exactly once!',
            kb_none: 'No bridges left.', kb_cross: function (c, t) { return 'Crossed ' + c + ' of ' + t + ' bridges.'; },
            kb_a_none: function (k) { return k + ' odd dots: no walk crosses every bridge exactly once.'; },
            kb_a_two: 'Exactly 2 odd dots: a walk exists, and it must start at one odd dot and end at the other.',
            kb_a_zero: '0 odd dots: a walk exists that returns to where it started.',
            kb_a_disc: 'The bridges do not connect all the land, so no single walk can cross them all.'
        },
        vi: {
            col_title: 'M\u00E1y theo d\u00F5i Collatz', col_start: 'S\u1ED1 b\u1EAFt \u0111\u1EA7u', col_go: 'Theo d\u00F5i', col_rand: 'Ng\u1EABu nhi\u00EAn', col_log: 'Thang log', col_lin: 'Thang tuy\u1EBFn t\u00EDnh',
            col_steps: 'b\u01B0\u1EDBc \u0111\u1EC3 v\u1EC1 1', col_peak: 'gi\u00E1 tr\u1ECB cao nh\u1EA5t', col_up: 'l\u1EA7n nh\u00E2n 3 c\u1ED9ng 1', col_down: 'l\u1EA7n chia 2',
            col_rule: 'Ch\u1EB5n: chia 2. L\u1EBB: nh\u00E2n 3 r\u1ED3i c\u1ED9ng 1.', col_bad: 'H\u00E3y nh\u1EADp m\u1ED9t s\u1ED1 nguy\u00EAn t\u1EEB 1 \u0111\u1EBFn 1.000.000.',
            col_one: 'S\u1ED1 1 \u0111\u00E3 \u1EDF cu\u1ED1i r\u1ED3i: 0 b\u01B0\u1EDBc.', col_done: function (n, s, p) { return 'B\u1EAFt \u0111\u1EA7u t\u1EEB ' + n + ': m\u1EA5t ' + s + ' b\u01B0\u1EDBc v\u00E0 leo t\u1EDBi ' + p + ' tr\u01B0\u1EDBc khi v\u1EC1 1.'; },
            col_open: 'Ch\u01B0a ai t\u00ECm \u0111\u01B0\u1EE3c s\u1ED1 n\u00E0o kh\u00F4ng bao gi\u1EDD v\u1EC1 1, nh\u01B0ng c\u0169ng ch\u01B0a ai ch\u1EE9ng minh \u0111\u01B0\u1EE3c.', col_try: 'Th\u1EED:',
            log_title: 'Kh\u00E1m ph\u00E1 \u00E1nh x\u1EA1 logistic', log_r: 'T\u1ED1c \u0111\u1ED9 t\u0103ng r', log_x: 'Gi\u00E1 tr\u1ECB b\u1EAFt \u0111\u1EA7u', log_two: 'Qu\u1EF9 \u0111\u1EA1o th\u1EE9 hai b\u1EAFt \u0111\u1EA7u cao h\u01A1n 0,0001', log_orbit: 'Qu\u1EF9 \u0111\u1EA1o theo th\u1EDDi gian', log_bif: 'V\u1ECB tr\u00ED c\u1EE7a r tr\u00EAn bi\u1EC3u \u0111\u1ED3 r\u1EBD nh\u00E1nh',
            log_fixed: function (x) { return 'Qu\u1EF9 \u0111\u1EA1o d\u1EEBng l\u1EA1i \u1EDF m\u1ED9t gi\u00E1 tr\u1ECB, kho\u1EA3ng ' + x + '.'; },
            log_cycle: function (p) { return 'Qu\u1EF9 \u0111\u1EA1o r\u01A1i v\u00E0o chu k\u1EF3 g\u1ED3m ' + p + ' gi\u00E1 tr\u1ECB.'; },
            log_chaos: 'Kh\u00F4ng c\u00F3 chu k\u1EF3 l\u1EB7p l\u1EA1i: h\u1ED7n \u0111\u1ED9n. C\u00E1c \u0111i\u1EC3m \u0111\u1EA7u g\u1EA7n nhau s\u1EBD t\u00E1ch xa.',
            log_note: 'Bi\u1EC3u \u0111\u1ED3 r\u1EBD nh\u00E1nh: m\u1ED7i l\u00E1t d\u1ECDc cho th\u1EA5y qu\u1EF9 \u0111\u1EA1o n\u1EB1m \u1EDF \u0111\u00E2u sau r\u1EA5t l\u00E2u.',
            fou_title: 'T\u1ED5ng ri\u00EAng Fourier', fou_square: 'S\u00F3ng vu\u00F4ng', fou_saw: 'S\u00F3ng r\u0103ng c\u01B0a', fou_tri: 'S\u00F3ng tam gi\u00E1c', fou_n: 'S\u1ED1 s\u00F3ng sin', fou_play: '\u25B6 Th\u00EAm s\u00F3ng', fou_stop: '\u25A0 D\u1EEBng',
            fou_terms: 's\u00F3ng sin', fou_over: 'v\u1ECDt l\u00EAn', fou_none: 'kh\u00F4ng c\u00F3', fou_over_note: function (p) { return 'Th\u00EAm bao nhi\u00EAu s\u00F3ng \u0111i n\u1EEFa, ch\u1ED7 v\u1ECDt l\u00EAn \u1EDF b\u01B0\u1EDBc nh\u1EA3y v\u1EABn kh\u00F4ng bi\u1EBFn m\u1EA5t: n\u00F3 d\u1EA7n ti\u1EBFn t\u1EDBi kho\u1EA3ng ' + p + ' b\u1EADc nh\u1EA3y (hi\u1EC7u \u1EE9ng Gibbs).'; },
            fou_smooth: 'S\u00F3ng tam gi\u00E1c kh\u00F4ng c\u00F3 ch\u1ED7 nh\u1EA3y n\u00EAn kh\u00F4ng v\u1ECDt l\u00EAn: c\u00E1c s\u00F3ng sin gi\u1EA3m nh\u01B0 1/k\u00B2.', fou_target: 'm\u1EE5c ti\u00EAu', fou_sum: 't\u1ED5ng',
            cg_title: 'Tr\u00F2 ch\u01A1i h\u1ED7n \u0111\u1ED9n', cg_corners: 'S\u1ED1 \u0111\u1EC9nh', cg_jump: 'Ph\u1EA7n qu\u00E3ng \u0111\u01B0\u1EDDng nh\u1EA3y', cg_add: 'Th\u00EAm 100', cg_add5: 'Th\u00EAm 5.000', cg_run: '\u25B6 Ch\u1EA1y', cg_pause: '\u25A0 T\u1EA1m d\u1EEBng', cg_clear: 'X\u00F3a', cg_points: '\u0111i\u1EC3m',
            cg_pre: 'M\u1EABu:', cg_tri: 'Tam gi\u00E1c \u00BD', cg_sq: 'Vu\u00F4ng \u00BD', cg_pent: 'Ng\u0169 gi\u00E1c 0,618', cg_hex: 'L\u1EE5c gi\u00E1c \u2154',
            cg_dim: function (c, d) { return 'M\u1ED7i b\u1EA3n sao thu nh\u1ECF c = ' + c + '. C\u00E1c b\u1EA3n sao kh\u00F4ng ch\u1ED3ng nhau, n\u00EAn h\u00ECnh c\u00F3 chi\u1EC1u ln n / ln(1/c) = ' + d + '.'; },
            cg_over: function (c) { return 'M\u1ED7i b\u1EA3n sao thu nh\u1ECF c = ' + c + ', l\u1EDBn qu\u00E1: c\u00E1c b\u1EA3n sao ch\u1ED3ng nhau v\u00E0 h\u00ECnh b\u1ECB l\u1EA5p \u0111\u1EA7y.'; },
            cg_rule: 'Lu\u1EADt ch\u01A1i: ch\u1ECDn ng\u1EABu nhi\u00EAn m\u1ED9t \u0111\u1EC9nh, nh\u1EA3y m\u1ED9t ph\u1EA7n qu\u00E3ng \u0111\u01B0\u1EDDng v\u1EC1 ph\u00EDa \u0111\u00F3 v\u00E0 ch\u1EA5m \u0111i\u1EC3m.',
            kb_title: 'C\u00E2y c\u1EA7u v\u00E0 b\u1EADc', kb_walk: '\u0110i b\u1ED9', kb_build: 'S\u1EEDa c\u1EA7u', kb_reset: 'L\u00E0m l\u1EA1i', kb_deg: 'b\u1EADc', kb_odd: 'S\u1ED1 \u0111i\u1EC3m c\u00F3 s\u1ED1 c\u1EA7u l\u1EBB',
            kb_walk_help: 'Ch\u1EA1m m\u1ED9t \u0111i\u1EC3m \u0111\u1EC3 xu\u1EA5t ph\u00E1t, r\u1ED3i ch\u1EA1m c\u00E1c c\u00E2y c\u1EA7u \u0111\u1EC3 \u0111i qua. M\u1ED7i c\u1EA7u ch\u1EC9 m\u1ED9t l\u1EA7n.', kb_build_help: 'Ch\u1EA1m m\u1ED9t c\u00E2y c\u1EA7u \u0111\u1EC3 b\u1ECF n\u00F3 ho\u1EB7c \u0111\u1EB7t l\u1EA1i.',
            kb_pick: 'Ch\u1EA1m m\u1ED9t \u0111i\u1EC3m \u0111\u1EC3 b\u1EAFt \u0111\u1EA7u \u0111i.', kb_far: 'H\u00E3y ch\u1EA1m c\u00E2y c\u1EA7u n\u1ED1i v\u1EDBi \u0111i\u1EC3m b\u1EA1n \u0111ang \u0111\u1EE9ng.', kb_used: 'C\u00E2y c\u1EA7u n\u00E0y \u0111\u00E3 \u0111i qua r\u1ED3i.', kb_gone: 'C\u00E2y c\u1EA7u n\u00E0y \u0111\u00E3 b\u1ECB b\u1ECF.',
            kb_stuck: function (k) { return 'K\u1EB9t r\u1ED3i! C\u00F2n ' + k + ' c\u00E2y c\u1EA7u ch\u01B0a \u0111i qua.'; }, kb_win: 'B\u1EA1n \u0111\u00E3 \u0111i qua m\u1ED7i c\u00E2y c\u1EA7u \u0111\u00FAng m\u1ED9t l\u1EA7n!',
            kb_none: 'Kh\u00F4ng c\u00F2n c\u00E2y c\u1EA7u n\u00E0o.', kb_cross: function (c, t) { return '\u0110\u00E3 qua ' + c + ' tr\u00EAn ' + t + ' c\u00E2y c\u1EA7u.'; },
            kb_a_none: function (k) { return 'C\u00F3 ' + k + ' \u0111i\u1EC3m b\u1EADc l\u1EBB: kh\u00F4ng c\u00F3 \u0111\u01B0\u1EDDng \u0111i n\u00E0o qua m\u1ED7i c\u1EA7u \u0111\u00FAng m\u1ED9t l\u1EA7n.'; },
            kb_a_two: 'C\u00F3 \u0111\u00FAng 2 \u0111i\u1EC3m b\u1EADc l\u1EBB: c\u00F3 \u0111\u01B0\u1EDDng \u0111i, v\u00E0 ph\u1EA3i b\u1EAFt \u0111\u1EA7u \u1EDF m\u1ED9t \u0111i\u1EC3m l\u1EBB, k\u1EBFt th\u00FAc \u1EDF \u0111i\u1EC3m l\u1EBB c\u00F2n l\u1EA1i.',
            kb_a_zero: 'Kh\u00F4ng c\u00F3 \u0111i\u1EC3m b\u1EADc l\u1EBB: c\u00F3 \u0111\u01B0\u1EDDng \u0111i quay v\u1EC1 \u0111i\u1EC3m xu\u1EA5t ph\u00E1t.',
            kb_a_disc: 'C\u00E1c c\u00E2y c\u1EA7u kh\u00F4ng n\u1ED1i li\u1EC1n m\u1ECDi v\u00F9ng \u0111\u1EA5t, n\u00EAn kh\u00F4ng c\u00F3 \u0111\u01B0\u1EDDng \u0111i n\u00E0o qua h\u1EBFt.'
        }
    };

    /* ---------------------------------------------------------- helpers */
    function injectStyle() {
        if (document.getElementById('mex-style')) return;
        var s = document.createElement('style'); s.id = 'mex-style'; s.textContent = CSS; document.head.appendChild(s);
    }
    function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
    function btn(label, cls, fn) { var b = el('button', cls || '', label); b.type = 'button'; b.addEventListener('click', fn); return b; }
    function row() { return el('div', 'mex-row'); }
    function shell(root, title) { root.innerHTML = ''; root.classList.add('mex'); root.setAttribute('role', 'group'); root.setAttribute('aria-label', title); root.appendChild(el('h4', '', title)); }
    function fmt(x, d, lang) { var s = x.toFixed(d); return lang === 'vi' ? s.replace('.', ',') : s; }
    function slider(label, min, max, step, val, onInput, show) {
        var w = el('div', 'mex-slide'), t = el('div', 't'), l = el('span', '', label), v = el('span', '', '');
        t.appendChild(l); t.appendChild(v);
        var r = document.createElement('input'); r.type = 'range'; r.min = min; r.max = max; r.step = step; r.value = val; r.setAttribute('aria-label', label);
        function upd() { v.textContent = show(parseFloat(r.value)); }
        r.addEventListener('input', function () { upd(); onInput(parseFloat(r.value)); });
        w.appendChild(t); w.appendChild(r); upd();
        return { wrap: w, input: r, set: function (x) { r.value = x; upd(); } };
    }
    function stat(label) { var d = el('div'), b = el('b', '', '-'); d.appendChild(b); d.appendChild(document.createTextNode(label)); return { box: d, set: function (v) { b.textContent = String(v); } }; }
    function canvas(aspect) {
        var c = document.createElement('canvas'), api = { c: c, aspect: aspect, ctx: null, w: 300, h: 300 * aspect, draw: function () { } };
        function size() {
            var w = c.clientWidth || 300, dpr = Math.min(2, window.devicePixelRatio || 1);
            api.w = w; api.h = Math.round(w * aspect);
            c.width = Math.round(w * dpr); c.height = Math.round(api.h * dpr); c.style.height = api.h + 'px';
            api.ctx = c.getContext('2d'); api.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        }
        api.size = size; api.redraw = function () { size(); api.draw(); };
        var tm = null; window.addEventListener('resize', function () { clearTimeout(tm); tm = setTimeout(api.redraw, 120); });
        return api;
    }
    function after(fn) { setTimeout(fn, 0); }
    function gridLines(ctx, x0, y0, w, h, nx, ny) {
        ctx.strokeStyle = '#1f2433'; ctx.lineWidth = 1; ctx.beginPath();
        for (var i = 0; i <= nx; i++) { var x = x0 + w * i / nx; ctx.moveTo(x, y0); ctx.lineTo(x, y0 + h); }
        for (var j = 0; j <= ny; j++) { var y = y0 + h * j / ny; ctx.moveTo(x0, y); ctx.lineTo(x0 + w, y); }
        ctx.stroke();
    }

    /* ----------------------------------------------------------- collatz */
    function collatzOrbit(n) {
        var v = [n], up = 0, down = 0, peak = n;
        while (n !== 1) { if (n % 2 === 0) { n = n / 2; down++; } else { n = 3 * n + 1; up++; } v.push(n); if (n > peak) peak = n; }
        return { v: v, up: up, down: down, peak: peak, steps: v.length - 1 };
    }
    function initCollatz(root, t, lang) {
        shell(root, t.col_title);
        var logScale = true, orbit = null, anim = null;
        root.appendChild(el('p', 'mex-note', t.col_rule));
        var r1 = row();
        var inp = document.createElement('input'); inp.type = 'number'; inp.min = 1; inp.max = 1000000; inp.step = 1; inp.value = 97; inp.setAttribute('inputmode', 'numeric'); inp.setAttribute('aria-label', t.col_start);
        r1.appendChild(el('label', '', t.col_start)); r1.appendChild(inp);
        r1.appendChild(btn(t.col_go, 'on', function () { go(parseInt(inp.value, 10)); }));
        r1.appendChild(btn(t.col_rand, '', function () { var n = 2 + Math.floor(Math.random() * 9998); inp.value = n; go(n); }));
        root.appendChild(r1);
        inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(parseInt(inp.value, 10)); });
        var r2 = row(); r2.appendChild(el('span', 'mex-note', t.col_try));
        [7, 97, 871].forEach(function (n) { r2.appendChild(btn(String(n), '', function () { inp.value = n; go(n); })); });
        var sb = btn(t.col_lin, '', function () { logScale = !logScale; sb.textContent = logScale ? t.col_lin : t.col_log; draw(1); });
        sb.textContent = t.col_lin; r2.appendChild(sb);
        root.appendChild(r2);
        var cv = canvas(0.62); root.appendChild(cv.c);
        var stats = el('div', 'mex-stats'), sSteps = stat(t.col_steps), sPeak = stat(t.col_peak), sUp = stat(t.col_up), sDown = stat(t.col_down);
        [sSteps, sPeak, sUp, sDown].forEach(function (s) { stats.appendChild(s.box); }); root.appendChild(stats);
        var seq = el('div', 'mex-seq'); root.appendChild(seq);
        var msg = el('p', 'mex-msg'); msg.setAttribute('aria-live', 'polite'); root.appendChild(msg);
        root.appendChild(el('p', 'mex-note', t.col_open));
        function yOf(v, h, top) { var m = orbit.peak; if (m <= 1) return top + h; return logScale ? top + h - h * Math.log(v) / Math.log(m) * 0.999 : top + h - h * v / m; }
        function draw(frac) {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, L = 8, T = 18, w = W - 2 * L, h = H - T - 24;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 6, 4);
            if (!orbit) return;
            var n = orbit.steps, k = Math.max(1, Math.round(n * frac)), i;
            var px = function (i) { return L + (n === 0 ? 0 : w * i / n); };
            ctx.strokeStyle = COL.sun; ctx.lineWidth = 2; ctx.lineJoin = 'round'; ctx.beginPath();
            for (i = 0; i <= k && i <= n; i++) { var x = px(i), y = yOf(orbit.v[i], h, T); if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y); }
            ctx.stroke();
            var pk = orbit.v.indexOf(orbit.peak);
            ctx.fillStyle = COL.sky; ctx.beginPath(); ctx.arc(px(0), yOf(orbit.v[0], h, T), 4, 0, 2 * PI); ctx.fill();
            if (k >= pk) { ctx.fillStyle = COL.orange; ctx.beginPath(); ctx.arc(px(pk), yOf(orbit.peak, h, T), 5, 0, 2 * PI); ctx.fill(); ctx.font = '12px sans-serif'; ctx.textAlign = pk > n / 2 ? 'right' : 'left'; ctx.fillText(String(orbit.peak), px(pk) + (pk > n / 2 ? -8 : 8), yOf(orbit.peak, h, T) - 6); }
            ctx.fillStyle = COL.dim; ctx.font = '11px sans-serif'; ctx.textAlign = 'left'; ctx.fillText('0', L, H - 6); ctx.textAlign = 'right'; ctx.fillText(String(n), W - L, H - 6);
            if (k >= n) { ctx.fillStyle = COL.mint; ctx.beginPath(); ctx.arc(px(n), yOf(1, h, T), 4, 0, 2 * PI); ctx.fill(); }
        }
        function go(n) {
            if (!(n >= 1 && n <= 1000000) || n !== Math.floor(n)) { msg.className = 'mex-msg mex-bad'; msg.textContent = t.col_bad; return; }
            orbit = collatzOrbit(n);
            root.setAttribute('data-steps', orbit.steps); root.setAttribute('data-peak', orbit.peak); root.setAttribute('data-start', n);
            sSteps.set(orbit.steps); sPeak.set(orbit.peak.toLocaleString(lang === 'vi' ? 'vi-VN' : 'en-US')); sUp.set(orbit.up); sDown.set(orbit.down);
            var v = orbit.v, head = v.slice(0, 9).join(' \u2192 ');
            seq.textContent = v.length > 10 ? head + ' \u2192 \u2026 \u2192 ' + v.slice(-4).join(' \u2192 ') : v.join(' \u2192 ');
            msg.className = 'mex-msg mex-ok'; msg.textContent = orbit.steps === 0 ? t.col_one : t.col_done(n, orbit.steps, orbit.peak);
            if (anim) cancelAnimationFrame(anim);
            var t0 = null;
            function frame(ts) { if (t0 === null) t0 = ts; var f = Math.min(1, (ts - t0) / 1200); draw(f); if (f < 1) anim = requestAnimationFrame(frame); else anim = null; }
            anim = requestAnimationFrame(frame);
        }
        cv.draw = function () { draw(1); };
        after(function () { cv.size(); go(97); });
    }

    /* ---------------------------------------------------------- logistic */
    function initLogistic(root, t, lang) {
        shell(root, t.log_title);
        var r = 3.9, x0 = 0.2, two = true;
        var sr = slider(t.log_r, 2.4, 4, 0.01, r, function (v) { r = v; update(); }, function (v) { return fmt(v, 2, lang); });
        var sx = slider(t.log_x, 0.05, 0.95, 0.01, x0, function (v) { x0 = v; update(); }, function (v) { return fmt(v, 2, lang); });
        root.appendChild(sr.wrap); root.appendChild(sx.wrap);
        var rc = row(), cb = document.createElement('input'); cb.type = 'checkbox'; cb.checked = true; cb.id = 'mex-two-' + Math.random().toString(36).slice(2, 7); cb.style.cssText = 'width:26px;height:26px;accent-color:#ffd166';
        var lb = el('label', '', t.log_two); lb.htmlFor = cb.id; cb.addEventListener('change', function () { two = cb.checked; update(); });
        rc.appendChild(cb); rc.appendChild(lb); root.appendChild(rc);
        root.appendChild(el('p', 'mex-note', t.log_orbit));
        var oc = canvas(0.5); root.appendChild(oc.c);
        var msg = el('p', 'mex-msg'); msg.setAttribute('aria-live', 'polite'); root.appendChild(msg);
        root.appendChild(el('p', 'mex-note', t.log_bif));
        var bc = canvas(0.55); root.appendChild(bc.c);
        root.appendChild(el('p', 'mex-note', t.log_note));
        var N = 50, bifImg = null;
        function orbitOf(x, rr, n) { var a = [x]; for (var i = 0; i < n; i++) { x = rr * x * (1 - x); a.push(x); } return a; }
        function period(rr, x) {
            for (var i = 0; i < 4000; i++) x = rr * x * (1 - x);
            var seq = [x]; for (i = 0; i < 80; i++) { x = rr * x * (1 - x); seq.push(x); }
            for (var p = 1; p <= 32; p++) { var ok = true; for (i = 0; i + p < seq.length; i++) if (Math.abs(seq[i + p] - seq[i]) > 1e-6) { ok = false; break; } if (ok) return { p: p, x: seq[0] }; }
            return { p: 0, x: seq[0] };
        }
        function drawOrbits() {
            if (!oc.ctx) oc.size();
            var ctx = oc.ctx, W = oc.w, H = oc.h, L = 26, T = 8, w = W - L - 8, h = H - T - 18;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 10, 4);
            ctx.fillStyle = COL.dim; ctx.font = '11px sans-serif'; ctx.textAlign = 'right'; ctx.fillText('1', L - 4, T + 8); ctx.fillText('0', L - 4, T + h); ctx.textAlign = 'center'; ctx.fillText('0', L, H - 4); ctx.fillText(String(N), L + w, H - 4);
            function line(a, col) { ctx.strokeStyle = col; ctx.lineWidth = 2; ctx.lineJoin = 'round'; ctx.beginPath(); a.forEach(function (v, i) { var x = L + w * i / N, y = T + h * (1 - v); if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y); }); ctx.stroke(); ctx.fillStyle = col; a.forEach(function (v, i) { ctx.beginPath(); ctx.arc(L + w * i / N, T + h * (1 - v), 2.2, 0, 2 * PI); ctx.fill(); }); }
            if (two) line(orbitOf(Math.min(0.999, x0 + 0.0001), r, N), COL.pink);
            line(orbitOf(x0, r, N), COL.sky);
        }
        function buildBif() {
            var W = bc.w, H = bc.h, L = 26, T = 6, w = W - L - 8, h = H - T - 18, ctx = bc.ctx;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 8, 4);
            ctx.fillStyle = 'rgba(128,237,153,.55)';
            for (var px = 0; px <= w; px += 1) {
                var rr = 2.4 + 1.6 * px / w, x = 0.5, i;
                for (i = 0; i < 300; i++) x = rr * x * (1 - x);
                for (i = 0; i < 70; i++) { x = rr * x * (1 - x); ctx.fillRect(L + px, T + h * (1 - x), 1, 1); }
            }
            ctx.fillStyle = COL.dim; ctx.font = '11px sans-serif'; ctx.textAlign = 'center'; ctx.fillText('2.4', L, H - 4); ctx.fillText('4', L + w, H - 4); ctx.textAlign = 'right'; ctx.fillText('1', L - 4, T + 8); ctx.fillText('0', L - 4, T + h);
            bifImg = ctx.getImageData(0, 0, bc.c.width, bc.c.height);
        }
        function drawMarker() {
            if (!bc.ctx) bc.size();
            if (!bifImg || bifImg.width !== bc.c.width) buildBif();
            var ctx = bc.ctx, dpr = bc.c.width / bc.w, W = bc.w, H = bc.h, L = 26, T = 6, w = W - L - 8, h = H - T - 18;
            ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.putImageData(bifImg, 0, 0); ctx.restore();
            var x = L + w * (r - 2.4) / 1.6;
            ctx.strokeStyle = COL.sun; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x, T); ctx.lineTo(x, T + h); ctx.stroke();
            ctx.fillStyle = COL.sun; ctx.font = 'bold 12px sans-serif'; ctx.textAlign = x > W / 2 ? 'right' : 'left'; ctx.fillText('r = ' + fmt(r, 2, lang), x + (x > W / 2 ? -6 : 6), T + 14);
        }
        function update() {
            var pr = period(r, x0);
            root.setAttribute('data-period', pr.p); root.setAttribute('data-r', r.toFixed(3));
            if (pr.p === 1) { msg.className = 'mex-msg mex-ok'; msg.textContent = t.log_fixed(fmt(pr.x, 4, lang)); }
            else if (pr.p > 1) { msg.className = 'mex-msg mex-warn'; msg.textContent = t.log_cycle(pr.p); }
            else { msg.className = 'mex-msg mex-bad'; msg.textContent = t.log_chaos; }
            drawOrbits(); drawMarker();
        }
        oc.draw = drawOrbits; bc.draw = function () { bifImg = null; drawMarker(); };
        after(function () { oc.size(); bc.size(); buildBif(); update(); });
    }

    /* ----------------------------------------------------------- fourier */
    var WAVES = {
        square: { f: function (x) { return x < 0 ? -1 : 1; }, term: function (k, x) { var m = 2 * k + 1; return 4 / PI * Math.sin(m * x) / m; }, top: function (N) { return 2 * N - 1; }, jump: true,
            txt: '(4/\u03C0)(sin x + sin 3x / 3 + sin 5x / 5 + \u2026)' },
        saw: { f: function (x) { return x / PI; }, term: function (k, x) { var m = k + 1; return 2 / PI * (m % 2 ? 1 : -1) * Math.sin(m * x) / m; }, top: function (N) { return N; }, jump: true,
            txt: '(2/\u03C0)(sin x \u2212 sin 2x / 2 + sin 3x / 3 \u2212 \u2026)' },
        tri: { f: function (x) { return 2 / PI * Math.asin(Math.sin(x)); }, term: function (k, x) { var m = 2 * k + 1; return 8 / (PI * PI) * (k % 2 ? -1 : 1) * Math.sin(m * x) / (m * m); }, top: function (N) { return 2 * N - 1; }, jump: false,
            txt: '(8/\u03C0\u00B2)(sin x \u2212 sin 3x / 9 + sin 5x / 25 \u2212 \u2026)' }
    };
    function partial(w, N, x) { var s = 0; for (var k = 0; k < N; k++) s += w.term(k, x); return s; }
    function overshoot(w, N) {
        if (!w.jump) return 0;
        var mx = -9, steps = 1500;
        for (var i = 1; i < steps; i++) { var x = -PI + 2 * PI * i / steps, s = partial(w, N, x); if (s > mx) mx = s; }
        return Math.max(0, (mx - 1) / 2);
    }
    function initFourier(root, t, lang) {
        shell(root, t.fou_title);
        var kind = 'square', N = 3, timer = null;
        var rk = row(), kb = {};
        [['square', t.fou_square], ['saw', t.fou_saw], ['tri', t.fou_tri]].forEach(function (p) { kb[p[0]] = btn(p[1], p[0] === kind ? 'on' : '', function () { kind = p[0]; for (var q in kb) kb[q].className = q === kind ? 'on' : ''; update(); }); rk.appendChild(kb[p[0]]); });
        root.appendChild(rk);
        var sn = slider(t.fou_n, 1, 40, 1, N, function (v) { N = v; update(); }, function (v) { return String(v); });
        root.appendChild(sn.wrap);
        var rp = row(); var pb = btn(t.fou_play, '', toggle); rp.appendChild(pb); root.appendChild(rp);
        var cv = canvas(0.58); root.appendChild(cv.c);
        var form = el('div', 'mex-seq'); root.appendChild(form);
        var stats = el('div', 'mex-stats'), sT = stat(t.fou_terms), sO = stat(t.fou_over); stats.appendChild(sT.box); stats.appendChild(sO.box); root.appendChild(stats);
        var msg = el('p', 'mex-msg'); msg.setAttribute('aria-live', 'polite'); root.appendChild(msg);
        function toggle() {
            if (timer) { clearInterval(timer); timer = null; pb.textContent = t.fou_play; return; }
            if (N >= 40) { N = 1; }
            pb.textContent = t.fou_stop;
            timer = setInterval(function () { N++; sn.set(N); update(); if (N >= 40) { clearInterval(timer); timer = null; pb.textContent = t.fou_play; } }, 260);
        }
        function draw() {
            if (!cv.ctx) cv.size();
            var w = WAVES[kind], ctx = cv.ctx, W = cv.w, H = cv.h, L = 6, T = 10, pw = W - 2 * L, ph = H - 2 * T;
            var X = function (x) { return L + pw * (x + PI) / (2 * PI); }, Y = function (y) { return T + ph * (1 - (y + 1.4) / 2.8); };
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, pw, ph, 8, 4);
            ctx.strokeStyle = '#3a4260'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(L, Y(0)); ctx.lineTo(L + pw, Y(0)); ctx.moveTo(X(0), T); ctx.lineTo(X(0), T + ph); ctx.stroke();
            ctx.strokeStyle = COL.dim; ctx.lineWidth = 2; ctx.setLineDash([5, 4]); ctx.beginPath();
            var i, S = 400;
            if (kind === 'square') { ctx.moveTo(X(-PI), Y(-1)); ctx.lineTo(X(0), Y(-1)); ctx.moveTo(X(0), Y(1)); ctx.lineTo(X(PI), Y(1)); }
            else { for (i = 0; i <= S; i++) { var xx = -PI + 2 * PI * i / S; if (i === 0) ctx.moveTo(X(xx), Y(w.f(xx))); else ctx.lineTo(X(xx), Y(w.f(xx))); } }
            ctx.stroke(); ctx.setLineDash([]);
            ctx.strokeStyle = COL.sky; ctx.lineWidth = 3; ctx.lineJoin = 'round'; ctx.beginPath();
            var M = 480; for (i = 0; i <= M; i++) { var x = -PI + 2 * PI * i / M, y = partial(w, N, x); if (i === 0) ctx.moveTo(X(x), Y(y)); else ctx.lineTo(X(x), Y(y)); }
            ctx.stroke();
        }
        function update() {
            var w = WAVES[kind], ov = overshoot(w, N);
            form.textContent = w.txt; sT.set(N);
            root.setAttribute('data-kind', kind); root.setAttribute('data-n', N); root.setAttribute('data-overshoot', (ov * 100).toFixed(2));
            if (w.jump) { sO.set(fmt(ov * 100, 1, lang) + '%'); msg.className = 'mex-msg mex-warn'; msg.textContent = t.fou_over_note('9%'); }
            else { sO.set(t.fou_none); msg.className = 'mex-msg mex-ok'; msg.textContent = t.fou_smooth; }
            draw();
        }
        cv.draw = draw;
        after(function () { cv.size(); update(); });
    }

    /* ---------------------------------------------------------- chaosgame */
    function cmax(n) { var s = 1; for (var k = 1; k <= Math.floor(n / 4); k++) s += Math.cos(2 * PI * k / n); return 1 / (2 * s); }
    function initChaos(root, t, lang) {
        shell(root, t.cg_title);
        var n = 3, jump = 0.5, pts = [], cur = null, runner = null, MAXP = 120000;
        root.appendChild(el('p', 'mex-note', t.cg_rule));
        var rp = row(); rp.appendChild(el('span', 'mex-note', t.cg_pre));
        var PRE = [[t.cg_tri, 3, 0.5], [t.cg_sq, 4, 0.5], [t.cg_pent, 5, 0.618], [t.cg_hex, 6, 2 / 3]];
        PRE.forEach(function (p) { rp.appendChild(btn(p[0], '', function () { setN(p[1]); setJ(p[2]); clear(); updInfo(); add(5000); })); });
        root.appendChild(rp);
        var sc = slider(t.cg_corners, 3, 8, 1, n, function (v) { n = v; clear(); updInfo(); }, function (v) { return String(v); });
        var sj = slider(t.cg_jump, 0.3, 0.8, 0.001, jump, function (v) { jump = v; clear(); updInfo(); }, function (v) { return fmt(v, 3, lang); });
        root.appendChild(sc.wrap); root.appendChild(sj.wrap);
        var cv = canvas(1); root.appendChild(cv.c);
        var rb = row(), runB = btn(t.cg_run, '', toggleRun);
        rb.appendChild(btn(t.cg_add, '', function () { add(100); })); rb.appendChild(btn(t.cg_add5, '', function () { add(5000); })); rb.appendChild(runB); rb.appendChild(btn(t.cg_clear, '', clear)); root.appendChild(rb);
        var stats = el('div', 'mex-stats'), sP = stat(t.cg_points); stats.appendChild(sP.box); root.appendChild(stats);
        var msg = el('p', 'mex-msg'); msg.setAttribute('aria-live', 'polite'); root.appendChild(msg);
        var COLORS = [COL.sky, COL.pink, COL.mint, COL.sun, COL.orange, '#b79cff', '#7ef0e3', '#ff9a8b'];
        function verts() { var v = []; for (var i = 0; i < n; i++) { var a = -PI / 2 + 2 * PI * i / n; v.push([0.5 + 0.46 * Math.cos(a), 0.5 + 0.46 * Math.sin(a)]); } return v; }
        function setN(v) { n = v; sc.set(v); } function setJ(v) { jump = v; sj.set(v); }
        function px(p) { var m = 8, s = cv.w - 2 * m; return [m + p[0] * s, m + p[1] * s]; }
        function dot(p, c) { var q = px(p); cv.ctx.fillStyle = COLORS[c % COLORS.length]; cv.ctx.fillRect(q[0] - 0.8, q[1] - 0.8, 1.6, 1.6); }
        function drawAll() {
            if (!cv.ctx) cv.size();
            cv.ctx.clearRect(0, 0, cv.w, cv.h);
            var v = verts(); v.forEach(function (p, i) { var q = px(p); cv.ctx.fillStyle = COLORS[i % COLORS.length]; cv.ctx.beginPath(); cv.ctx.arc(q[0], q[1], 5, 0, 2 * PI); cv.ctx.fill(); });
            pts.forEach(function (p) { dot(p[0], p[1]); });
        }
        function add(k) {
            var v = verts(), i, c;
            if (!cur) cur = [0.5, 0.5];
            for (i = 0; i < k && pts.length < MAXP; i++) {
                c = Math.floor(Math.random() * n);
                cur = [cur[0] + (v[c][0] - cur[0]) * jump, cur[1] + (v[c][1] - cur[1]) * jump];
                pts.push([cur, c]); dot(cur, c);
            }
            root._pts = pts; root._verts = v; root.setAttribute('data-count', pts.length); sP.set(pts.length.toLocaleString(lang === 'vi' ? 'vi-VN' : 'en-US'));
        }
        function clear() { stopRun(); pts = []; cur = null; root._pts = pts; root.setAttribute('data-count', 0); sP.set(0); drawAll(); }
        function stopRun() { if (runner) { cancelAnimationFrame(runner); runner = null; runB.textContent = t.cg_run; runB.className = ''; } }
        function toggleRun() {
            if (runner) { stopRun(); return; }
            runB.textContent = t.cg_pause; runB.className = 'on';
            (function loop() { add(250); if (pts.length >= MAXP) { stopRun(); return; } runner = requestAnimationFrame(loop); })();
        }
        function updInfo() {
            var c = 1 - jump, cm = cmax(n);
            root.setAttribute('data-c', c.toFixed(3));
            if (c <= cm + 1e-3) { var d = Math.log(n) / Math.log(1 / c); root.setAttribute('data-dim', d.toFixed(3)); msg.className = 'mex-msg mex-ok'; msg.textContent = t.cg_dim(fmt(c, 3, lang), fmt(d, 3, lang)); }
            else { root.setAttribute('data-dim', ''); msg.className = 'mex-msg mex-warn'; msg.textContent = t.cg_over(fmt(c, 3, lang)); }
        }
        cv.draw = drawAll;
        after(function () { cv.size(); drawAll(); updInfo(); root._pts = pts; add(3000); });
    }

    /* -------------------------------------------------------- konigsberg */
    function initKonigsberg(root, t, lang) {
        shell(root, t.kb_title);
        var NODES = { A: [70, 150], B: [180, 40], C: [180, 260], D: [290, 150] };
        var NAMES = ['A', 'B', 'C', 'D'];
        var EDGES = [['B', 'A', 26], ['B', 'A', -26], ['C', 'A', 26], ['C', 'A', -26], ['A', 'D', 0], ['B', 'D', 0], ['C', 'D', 0]];
        var mode = 'walk', removed = {}, used = {}, order = [], cur = null, stuckMsg = null;
        var NS = 'http://www.w3.org/2000/svg';
        function S(tag, a) { var e = document.createElementNS(NS, tag); for (var k in a) e.setAttribute(k, a[k]); return e; }
        var rm = row(), bW = btn(t.kb_walk, 'on', function () { setMode('walk'); }), bB = btn(t.kb_build, '', function () { setMode('build'); }), bR = btn(t.kb_reset, '', function () { removed = {}; resetWalk(); render(); });
        rm.appendChild(bW); rm.appendChild(bB); rm.appendChild(bR); root.appendChild(rm);
        var help = el('p', 'mex-note', t.kb_walk_help); root.appendChild(help);
        var svg = S('svg', { viewBox: '0 0 360 300', role: 'img', 'aria-label': t.kb_title }); root.appendChild(svg);
        var msg = el('p', 'mex-msg'); msg.setAttribute('aria-live', 'polite'); root.appendChild(msg);
        var ana = el('p', 'mex-msg'); ana.style.minHeight = '3.2em'; root.appendChild(ana);
        function setMode(m) { mode = m; bW.className = m === 'walk' ? 'on' : ''; bB.className = m === 'build' ? 'on' : ''; help.textContent = m === 'walk' ? t.kb_walk_help : t.kb_build_help; resetWalk(); render(); }
        function resetWalk() { used = {}; order = []; cur = null; stuckMsg = null; msgSet(mode === 'walk' ? t.kb_pick : '', 'mex-msg'); }
        function msgSet(s, cls) { msg.textContent = s; msg.className = cls || 'mex-msg'; }
        function alive() { var a = []; EDGES.forEach(function (e, i) { if (!removed[i]) a.push(i); }); return a; }
        function degrees() { var d = { A: 0, B: 0, C: 0, D: 0 }; alive().forEach(function (i) { d[EDGES[i][0]]++; d[EDGES[i][1]]++; }); return d; }
        function connected() {
            var al = alive(); if (!al.length) return true;
            var seen = {}, st = [EDGES[al[0]][0]]; seen[st[0]] = 1;
            while (st.length) { var u = st.pop(); al.forEach(function (i) { var a = EDGES[i][0], b = EDGES[i][1], v = a === u ? b : b === u ? a : null; if (v && !seen[v]) { seen[v] = 1; st.push(v); } }); }
            return al.every(function (i) { return seen[EDGES[i][0]]; });
        }
        function path(i) {
            var e = EDGES[i], a = NODES[e[0]], b = NODES[e[1]], bend = e[2];
            var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1], len = Math.sqrt(dx * dx + dy * dy), nx = -dy / len, ny = dx / len;
            var cx = mx + nx * bend * 2, cy = my + ny * bend * 2;
            return { d: 'M' + a[0] + ' ' + a[1] + ' Q' + cx + ' ' + cy + ' ' + b[0] + ' ' + b[1], mx: 0.25 * a[0] + 0.5 * cx + 0.25 * b[0], my: 0.25 * a[1] + 0.5 * cy + 0.25 * b[1] };
        }
        function render() {
            while (svg.firstChild) svg.removeChild(svg.firstChild);
            var deg = degrees(), i;
            EDGES.forEach(function (e, idx) {
                var p = path(idx), g = S('g', { 'data-edge': idx, 'data-a': e[0], 'data-b': e[1], 'class': 'kb-edge' });
                var col = removed[idx] ? '#4a5170' : used[idx] ? COL.mint : COL.orange;
                g.appendChild(S('path', { d: p.d, fill: 'none', stroke: col, 'stroke-width': used[idx] ? 7 : 5, 'stroke-dasharray': removed[idx] ? '4 6' : '', 'stroke-linecap': 'round' }));
                var hit = S('path', { d: p.d, fill: 'none', stroke: 'transparent', 'stroke-width': 30 }); hit.style.cursor = 'pointer'; g.appendChild(hit);
                if (used[idx]) { var tx = S('text', { x: p.mx, y: p.my + 5, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 800, fill: '#10121a', stroke: COL.mint, 'stroke-width': 0.5 }); var circ = S('circle', { cx: p.mx, cy: p.my, r: 11, fill: COL.mint }); g.appendChild(circ); tx.textContent = String(order.indexOf(idx) + 1); g.appendChild(tx); }
                g.addEventListener('click', function () { onEdge(idx); });
                svg.appendChild(g);
            });
            NAMES.forEach(function (nm) {
                var p = NODES[nm], odd = deg[nm] % 2 === 1, g = S('g', { 'data-node': nm, 'class': 'kb-node' });
                if (cur === nm) g.appendChild(S('circle', { cx: p[0], cy: p[1], r: 29, fill: 'none', stroke: COL.sun, 'stroke-width': 4 }));
                g.appendChild(S('circle', { cx: p[0], cy: p[1], r: 22, fill: odd ? COL.pink : COL.sky, stroke: '#10121a', 'stroke-width': 3 }));
                var tx = S('text', { x: p[0], y: p[1] + 7, 'text-anchor': 'middle', 'font-size': 22, 'font-weight': 800, fill: '#10121a' }); tx.textContent = nm; g.appendChild(tx);
                var bx = p[0] + 30, by = nm === 'C' ? p[1] + 34 : p[1] - 22;
                var dl = S('text', { x: bx, y: by, 'text-anchor': 'middle', 'font-size': 22, 'font-weight': 800, fill: odd ? COL.pink : COL.sky, 'class': 'kb-deg' }); dl.textContent = String(deg[nm]); dl.setAttribute('aria-label', t.kb_deg + ' ' + deg[nm]); g.appendChild(dl);
                g.appendChild(S('circle', { cx: p[0], cy: p[1], r: 30, fill: 'transparent' })).style.cursor = 'pointer';
                g.addEventListener('click', function () { onNode(nm); });
                svg.appendChild(g);
            });
            var odds = NAMES.filter(function (nm) { return deg[nm] % 2 === 1; }), al = alive();
            root.setAttribute('data-odd', odds.length); root.setAttribute('data-degrees', NAMES.map(function (nm) { return deg[nm]; }).join(','));
            var m;
            if (!al.length) m = t.kb_none; else if (!connected()) m = t.kb_a_disc; else if (odds.length === 0) m = t.kb_a_zero; else if (odds.length === 2) m = t.kb_a_two; else m = t.kb_a_none(odds.length);
            ana.className = 'mex-msg ' + ((al.length && connected() && (odds.length === 0 || odds.length === 2)) ? 'mex-ok' : 'mex-bad');
            ana.textContent = t.kb_odd + ': ' + odds.length + '. ' + m;
            root.setAttribute('data-possible', (al.length && connected() && (odds.length === 0 || odds.length === 2)) ? '1' : '0');
        }
        function onNode(nm) {
            if (mode !== 'walk' || order.length) return;
            cur = nm; msgSet(t.kb_cross(0, alive().length), 'mex-msg mex-warn'); render();
        }
        function onEdge(i) {
            if (mode === 'build') { if (removed[i]) delete removed[i]; else removed[i] = 1; resetWalk(); msgSet('', 'mex-msg'); render(); return; }
            if (removed[i]) { msgSet(t.kb_gone, 'mex-msg mex-bad'); return; }
            if (cur === null) { msgSet(t.kb_pick, 'mex-msg mex-warn'); return; }
            if (used[i]) { msgSet(t.kb_used, 'mex-msg mex-bad'); return; }
            var e = EDGES[i]; if (e[0] !== cur && e[1] !== cur) { msgSet(t.kb_far, 'mex-msg mex-bad'); return; }
            used[i] = 1; order.push(i); cur = e[0] === cur ? e[1] : e[0];
            var total = alive().length, left = total - order.length;
            var can = alive().some(function (j) { return !used[j] && (EDGES[j][0] === cur || EDGES[j][1] === cur); });
            root.setAttribute('data-crossed', order.length);
            if (left === 0) { msgSet('\uD83C\uDF89 ' + t.kb_win, 'mex-msg mex-ok'); root.setAttribute('data-walk', 'win'); }
            else if (!can) { msgSet(t.kb_stuck(left), 'mex-msg mex-bad'); root.setAttribute('data-walk', 'stuck'); }
            else { msgSet(t.kb_cross(order.length, total), 'mex-msg mex-warn'); root.setAttribute('data-walk', 'going'); }
            render();
        }
        resetWalk(); render();
    }

    var INIT = { collatz: initCollatz, logistic: initLogistic, fourier: initFourier, chaosgame: initChaos, konigsberg: initKonigsberg };
    function initAll() {
        var nodes = document.querySelectorAll('.mex-explainer');
        if (!nodes.length) return;
        injectStyle();
        for (var i = 0; i < nodes.length; i++) {
            var root = nodes[i], kind = root.getAttribute('data-mex');
            var lang = (root.getAttribute('data-lang') || document.documentElement.lang || 'en') === 'vi' ? 'vi' : 'en';
            if (INIT[kind] && !root.getAttribute('data-mex-ready')) { root.setAttribute('data-mex-ready', '1'); INIT[kind](root, I18N[lang], lang); }
        }
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
