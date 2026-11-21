/**
 * Interactive explainers for math-enthusiast (EN + VI, touch friendly, no dependencies)
 *   collatz   : Collatz orbit tracer             (chapter 01)
 *   logistic  : logistic map + bifurcation       (chapter 04, Chaos)
 *   fourier   : Fourier partial sums + Gibbs     (chapter 03)
 *   chaosgame : chaos game on a polygon          (chapter 04, Fractals)
 *   konigsberg: degree counter / bridge walker   (chapter 05)
 *   batch 2: zeta, twins, kakeya, clt, dh, hilbert, ball, catenoid, chsh, sir, ot (chapters 01, 03, 04, 06)
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

    /* ================================================== batch 2 explainers */
    function U(lang) { return function (en, vi) { return lang === 'vi' ? vi : en; }; }
    function setd(root, o) { for (var k in o) root.setAttribute('data-' + k, o[k]); }
    function mk(root) { var m = el('p', 'mex-msg'); m.setAttribute('aria-live', 'polite'); root.appendChild(m); return { set: function (txt, cls) { m.className = 'mex-msg ' + (cls || ''); m.textContent = txt; } }; }
    function txt(ctx, s, x, y, col, al, font) { ctx.fillStyle = col || COL.dim; ctx.textAlign = al || 'left'; ctx.font = font || '11px sans-serif'; ctx.fillText(s, x, y); }
    function sieve(n) { var s = new Uint8Array(n + 1); s[0] = s[1] = 1; for (var i = 2; i * i <= n; i++) if (!s[i]) for (var j = i * i; j <= n; j += i) s[j] = 1; return s; } /* 1 = composite */
    function kfmt(n, lang) { return n.toLocaleString(lang === 'vi' ? 'vi-VN' : 'en-US'); }

    /* ---- zeta: sum vs Euler product ---- */
    function initZeta(root, t, lang) {
        var tx = U(lang), XM = 300, Z = PI * PI / 6, cs = sieve(XM), S = [0], P = [1], np = [0], s = 0, p = 1, c = 0, x;
        for (x = 1; x <= XM; x++) { s += 1 / (x * x); if (x > 1 && !cs[x]) { p *= 1 / (1 - 1 / (x * x)); c++; } S.push(s); P.push(p); np.push(c); }
        shell(root, tx('Sum versus product', 'Tổng và tích cùng một giới hạn'));
        root.appendChild(el('p', 'mex-note', tx('Blue: add 1/n² over every whole number up to x. Pink: multiply 1/(1 − p⁻²) over the primes p up to x only.', 'Xanh: cộng 1/n² trên mọi số nguyên đến x. Hồng: nhân 1/(1 − p⁻²) chỉ trên các số nguyên tố p đến x.')));
        var cur = 60, sl = slider('x', 10, XM, 1, cur, function (v) { cur = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sl.wrap);
        var cv = canvas(0.7); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sS = stat(tx('sum', 'tổng')), sP = stat(tx('product', 'tích')), sZ = stat('π²/6'), sN = stat(tx('primes used', 'số nguyên tố dùng'));
        [sS, sP, sZ, sN].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root);
        var LO = 1.54, HI = 1.655;
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, L = 40, R = 10, T = 12, B = 22, w = W - L - R, h = H - T - B;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 6, 4);
            var X = function (i) { return L + w * (i - 10) / (XM - 10); }, Y = function (v) { return T + h - h * (v - LO) / (HI - LO); };
            ctx.setLineDash([5, 4]); ctx.strokeStyle = COL.sun; ctx.beginPath(); ctx.moveTo(L, Y(Z)); ctx.lineTo(L + w, Y(Z)); ctx.stroke(); ctx.setLineDash([]);
            txt(ctx, 'π²/6', L + 4, Y(Z) - 4, COL.sun);
            [[S, COL.sky], [P, COL.pink]].forEach(function (a) {
                ctx.strokeStyle = a[1]; ctx.lineWidth = 2; ctx.beginPath();
                for (var i = 10; i <= cur; i++) { if (i === 10) ctx.moveTo(X(i), Y(a[0][i])); else ctx.lineTo(X(i), Y(a[0][i])); } ctx.stroke();
                ctx.globalAlpha = 0.25; ctx.beginPath(); for (var j = cur; j <= XM; j++) { if (j === cur) ctx.moveTo(X(j), Y(a[0][j])); else ctx.lineTo(X(j), Y(a[0][j])); } ctx.stroke(); ctx.globalAlpha = 1;
                ctx.fillStyle = a[1]; ctx.beginPath(); ctx.arc(X(cur), Y(a[0][cur]), 5, 0, 2 * PI); ctx.fill();
            });
            [1.55, 1.6, 1.65].forEach(function (v) { txt(ctx, fmt(v, 2, lang), L - 4, Y(v) + 4, COL.dim, 'right'); });
            txt(ctx, '10', L, H - 6, COL.dim, 'center'); txt(ctx, String(XM), L + w, H - 6, COL.dim, 'center'); txt(ctx, 'x', L + w / 2, H - 6, COL.dim, 'center');
        };
        function upd() {
            sS.set(fmt(S[cur], 4, lang)); sP.set(fmt(P[cur], 4, lang)); sZ.set(fmt(Z, 4, lang)); sN.set(np[cur]);
            setd(root, { x: cur, sum: S[cur].toFixed(4), prod: P[cur].toFixed(4) });
            msg.set(tx('Up to ' + cur + ': both stay below π²/6 and creep toward it. The sum uses every integer, the product only primes, yet they meet at the same limit (Euler).',
                'Đến ' + cur + ': cả hai vẫn nhỏ hơn π²/6 và tiến dần tới nó. Tổng dùng mọi số nguyên, tích chỉ dùng số nguyên tố, vậy mà cùng một giới hạn (Euler).'), 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- twin primes: counts vs Hardy-Littlewood ---- */
    var TWIN = null;
    function twinData() {
        if (TWIN) return TWIN;
        var N = 1000000, cs = sieve(N), cnt = new Int32Array(N + 1), pr = new Float64Array(N + 1), n, C2 = 0.6601618158468696;
        for (n = 3; n <= N; n++) { cnt[n] = cnt[n - 1] + ((!cs[n] && !cs[n - 2]) ? 1 : 0); }
        var acc = 0, f = function (u) { return 1 / (Math.log(u) * Math.log(u)); };
        for (n = 3; n <= N; n++) { acc += (f(n - 1) + f(n)) / 2; pr[n] = 2 * C2 * acc; }
        TWIN = { cnt: cnt, pr: pr, N: N }; return TWIN;
    }
    function initTwins(root, t, lang) {
        var tx = U(lang), D = twinData();
        shell(root, tx('Counting twin primes', 'Đếm cặp số nguyên tố sinh đôi'));
        root.appendChild(el('p', 'mex-note', tx('A twin pair is two primes that differ by 2. Slide x from 100 to 1,000,000 and compare the real count with the Hardy–Littlewood prediction.', 'Cặp sinh đôi là hai số nguyên tố hơn kém nhau 2. Kéo x từ 100 đến 1.000.000 và so số đếm thật với dự đoán Hardy–Littlewood.')));
        var lv = 3, sl = slider('x', 2, 6, 0.01, lv, function (v) { lv = v; upd(); }, function (v) { return kfmt(Math.round(Math.pow(10, v)), lang); });
        root.appendChild(sl.wrap);
        var cv = canvas(0.72); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sA = stat(tx('twin pairs ≤ x', 'cặp sinh đôi ≤ x')), sP = stat(tx('predicted', 'dự đoán')), sR = stat(tx('real ÷ predicted', 'thật ÷ dự đoán'));
        [sA, sP, sR].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root);
        root.appendChild(el('p', 'mex-note', tx('A good fit is evidence, not a proof: nobody has proved there are infinitely many twin primes.', 'Khớp tốt là bằng chứng, chưa phải chứng minh: chưa ai chứng minh có vô hạn cặp sinh đôi.')));
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, L = 40, R = 10, T = 12, B = 22, w = W - L - R, h = H - T - B;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 4, 4);
            var X = function (v) { return L + w * (v - 2) / 4; }, Y = function (v) { return T + h - h * Math.log10(Math.max(v, 1)) / 4; };
            var i, lg, x;
            ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.beginPath();
            for (i = 0; i <= 200; i++) { lg = 2 + 4 * i / 200; x = Math.round(Math.pow(10, lg)); if (i === 0) ctx.moveTo(X(lg), Y(D.pr[x])); else ctx.lineTo(X(lg), Y(D.pr[x])); } ctx.stroke();
            ctx.fillStyle = COL.pink;
            for (i = 0; i <= 60; i++) { lg = 2 + 4 * i / 60; if (lg > lv) break; x = Math.round(Math.pow(10, lg)); ctx.beginPath(); ctx.arc(X(lg), Y(D.cnt[x]), 2.5, 0, 2 * PI); ctx.fill(); }
            x = Math.round(Math.pow(10, lv)); ctx.fillStyle = COL.sun; ctx.beginPath(); ctx.arc(X(lv), Y(D.cnt[x]), 6, 0, 2 * PI); ctx.fill();
            var sup = ['⁰', '¹', '²', '³', '⁴']; for (i = 0; i <= 4; i++) txt(ctx, '10' + sup[i], L - 4, Y(Math.pow(10, i)) + 4, COL.dim, 'right');
            for (i = 2; i <= 6; i++) txt(ctx, '10' + ['', '', '²', '³', '⁴', '⁵', '⁶'][i], X(i), H - 6, COL.dim, 'center');
            txt(ctx, tx('real', 'thật'), L + 8, T + 14, COL.pink); txt(ctx, tx('prediction', 'dự đoán'), L + 8, T + 30, COL.sky);
        };
        function upd() {
            var x = Math.round(Math.pow(10, lv)), a = D.cnt[x], p = D.pr[x];
            sA.set(kfmt(a, lang)); sP.set(kfmt(Math.round(p), lang)); sR.set(fmt(a / p, 3, lang));
            setd(root, { x: x, count: a, pred: Math.round(p) });
            msg.set(tx('Up to ' + kfmt(x, lang) + ' there are ' + kfmt(a, lang) + ' twin pairs; the heuristic predicts about ' + kfmt(Math.round(p), lang) + '.', 'Đến ' + kfmt(x, lang) + ' có ' + kfmt(a, lang) + ' cặp sinh đôi; heuristic dự đoán khoảng ' + kfmt(Math.round(p), lang) + '.'), 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- Kakeya: needle in a deltoid ---- */
    function initKakeya(root, t, lang) {
        var tx = U(lang), ang = 0, play = null;
        shell(root, tx('A needle that turns inside a deltoid', 'Chiếc kim quay trong một deltoid'));
        root.appendChild(el('p', 'mex-note', tx('The needle has length 1 and its two ends always lie on the three-cusped curve. Turn it by hand.', 'Kim dài 1 và hai đầu luôn nằm trên đường ba mũi nhọn. Hãy tự quay kim.')));
        var sl = slider(tx('Angle turned', 'Góc đã quay'), 0, 180, 1, 0, function (v) { ang = v; upd(); }, function (v) { return Math.round(v) + '°'; });
        root.appendChild(sl.wrap);
        var r2 = row(), pb = btn(tx('▶ Turn', '▶ Quay'), 'on', function () {
            if (play) { stop(); return; }
            if (ang >= 180) ang = 0; pb.textContent = tx('■ Stop', '■ Dừng');
            var t0 = performance.now(), a0 = ang;
            (function fr(ts) { var a = a0 + (ts - t0) / 25; if (a >= 180) { ang = 180; sl.set(180); upd(); stop(); return; } ang = a; sl.set(a); upd(); play = requestAnimationFrame(fr); })(t0);
        });
        function stop() { if (play) cancelAnimationFrame(play); play = null; pb.textContent = tx('▶ Turn', '▶ Quay'); }
        var dcb = document.createElement('input'); dcb.type = 'checkbox'; dcb.checked = true; dcb.id = 'mex-kk-' + Math.random().toString(36).slice(2, 7); dcb.style.cssText = 'width:26px;height:26px;accent-color:#ffd166';
        var dl = el('label', '', tx('Show the disc you get by spinning in place', 'Hiện đĩa khi quay tại chỗ')); dl.htmlFor = dcb.id; dcb.addEventListener('change', upd);
        r2.appendChild(pb); r2.appendChild(dcb); r2.appendChild(dl); root.appendChild(r2);
        var cv = canvas(1); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sD = stat(tx('deltoid area', 'diện tích deltoid')), sC = stat(tx('disc area', 'diện tích đĩa'));
        st.appendChild(sD.box); st.appendChild(sC.box); root.appendChild(st);
        var msg = mk(root);
        function z(tt, r) { return [2 * r * Math.cos(tt) + r * Math.cos(2 * tt), 2 * r * Math.sin(tt) - r * Math.sin(2 * tt)]; }
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, r = W * 0.19, cx = W / 2 - 0.75 * r, cy = H / 2, i;
            var P = function (q) { return [cx + q[0], cy - q[1]]; };
            ctx.clearRect(0, 0, W, H);
            ctx.strokeStyle = COL.sky; ctx.lineWidth = 3; ctx.beginPath();
            for (i = 0; i <= 360; i++) { var p = P(z(i * PI / 180, r)); if (i === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]); } ctx.stroke();
            var tt = ang * PI / 180;
            ctx.strokeStyle = 'rgba(255,209,102,0.28)'; ctx.lineWidth = 1.5;
            for (var a = 0; a <= ang; a += 3) { var u = a * PI / 180, A = P(z(u, r)), B = P(z(u + PI, r)); ctx.beginPath(); ctx.moveTo(A[0], A[1]); ctx.lineTo(B[0], B[1]); ctx.stroke(); }
            var E1 = P(z(tt, r)), E2 = P(z(tt + PI, r));
            if (dcb.checked) { ctx.setLineDash([6, 5]); ctx.strokeStyle = COL.orange; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc((E1[0] + E2[0]) / 2, (E1[1] + E2[1]) / 2, 2 * r, 0, 2 * PI); ctx.stroke(); ctx.setLineDash([]); }
            ctx.strokeStyle = COL.sun; ctx.lineWidth = 6; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(E1[0], E1[1]); ctx.lineTo(E2[0], E2[1]); ctx.stroke();
            ctx.fillStyle = COL.pink; [E1, E2].forEach(function (q) { ctx.beginPath(); ctx.arc(q[0], q[1], 6, 0, 2 * PI); ctx.fill(); });
        };
        function upd() {
            sD.set('π/8 ≈ ' + fmt(PI / 8, 3, lang)); sC.set('π/4 ≈ ' + fmt(PI / 4, 3, lang));
            setd(root, { angle: Math.round(ang) });
            msg.set(ang >= 179.5 ? tx('After 180° the needle has turned all the way round (it ends pointing the other way) and swept only half the disc area. Besicovitch later showed the area can be made as small as you like.', 'Sau 180° kim đã quay trọn (cuối cùng chỉ ngược hướng) mà chỉ quét một nửa diện tích đĩa. Về sau Besicovitch chứng minh diện tích có thể nhỏ tùy ý.')
                : tx('The needle slides and turns, but both ends stay on the curve and the whole needle stays inside it.', 'Kim vừa trượt vừa quay, hai đầu luôn nằm trên đường cong và cả kim luôn nằm trong hình.'), 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- CLT: sums of dice ---- */
    function pmfDice(n) { var out = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6], k, i, j; for (k = 1; k < n; k++) { var nx = new Array(out.length + 5).fill(0); for (i = 0; i < out.length; i++) for (j = 0; j < 6; j++) nx[i + j] += out[i] / 6; out = nx; } return out; }
    function Phi(z) { var a = Math.abs(z) / Math.SQRT2, tt = 1 / (1 + 0.3275911 * a), y = 1 - (((((1.061405429 * tt - 1.453152027) * tt) + 1.421413741) * tt - 0.284496736) * tt + 0.254829592) * tt * Math.exp(-a * a); return z >= 0 ? 0.5 * (1 + y) : 0.5 * (1 - y); }
    function initCLT(root, t, lang) {
        var tx = U(lang), n = 1, sample = null;
        shell(root, tx('Sum of dice → bell curve', 'Tổng các xúc xắc → đường chuông'));
        root.appendChild(el('p', 'mex-note', tx('Choose how many fair dice to add. Bars: exact chance of each total, stretched to a common scale. Blue: the normal bell curve.', 'Chọn số xúc xắc đều để cộng. Cột: xác suất chính xác của mỗi tổng, co giãn về cùng thang. Xanh: đường chuông chuẩn.')));
        var sl = slider(tx('Number of dice n', 'Số xúc xắc n'), 1, 30, 1, 1, function (v) { n = v; sample = null; upd(); }, function (v) { return String(v); });
        root.appendChild(sl.wrap);
        var r = row(); r.appendChild(btn(tx('Roll 3,000 times', 'Gieo 3.000 lần'), '', function () { roll(); })); r.appendChild(btn(tx('Clear rolls', 'Xóa lần gieo'), '', function () { sample = null; upd(); })); root.appendChild(r);
        var cv = canvas(0.62); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sK = stat(tx('largest gap to the bell', 'chênh lệch lớn nhất so với chuông'));
        st.appendChild(sK.box); root.appendChild(st);
        var msg = mk(root);
        function ks() { var p = pmfDice(n), mu = 3.5 * n, sd = Math.sqrt(35 * n / 12), c = 0, m = 0; for (var i = 0; i < p.length; i++) { c += p[i]; m = Math.max(m, Math.abs(c - Phi((n + i + 0.5 - mu) / sd))); } return m; }
        function roll() { var N = 3000, h = {}, i, j; for (i = 0; i < N; i++) { var s = 0; for (j = 0; j < n; j++) s += 1 + Math.floor(Math.random() * 6); h[s] = (h[s] || 0) + 1; } sample = { h: h, N: N }; upd(); }
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, L = 8, B = 20, T = 8, w = W - 2 * L, h = H - T - B;
            ctx.clearRect(0, 0, W, H);
            var p = pmfDice(n), mu = 3.5 * n, sd = Math.sqrt(35 * n / 12), X = function (z) { return L + w * (z + 3.5) / 7; }, Y = function (d) { return T + h - h * d / 0.46; };
            ctx.strokeStyle = '#2a3045'; ctx.beginPath(); ctx.moveTo(L, T + h); ctx.lineTo(L + w, T + h); ctx.stroke();
            ctx.fillStyle = 'rgba(255,209,102,0.85)'; var i;
            for (i = 0; i < p.length; i++) { var zc = (n + i - mu) / sd, x0 = X(zc - 0.5 / sd), x1 = X(zc + 0.5 / sd), y = Y(p[i] * sd); if (p[i] * sd < 1e-4) continue; ctx.fillRect(x0 + 0.5, y, Math.max(1, x1 - x0 - 1), T + h - y); }
            ctx.strokeStyle = COL.sky; ctx.lineWidth = 2.5; ctx.beginPath();
            for (i = 0; i <= 140; i++) { var zz = -3.5 + 7 * i / 140, d = Math.exp(-zz * zz / 2) / Math.sqrt(2 * PI); if (i === 0) ctx.moveTo(X(zz), Y(d)); else ctx.lineTo(X(zz), Y(d)); } ctx.stroke();
            if (sample) { ctx.fillStyle = COL.mint; for (var s in sample.h) { var zs = (+s - mu) / sd, dens = sample.h[s] / sample.N * sd; ctx.beginPath(); ctx.arc(X(zs), Y(dens), 3, 0, 2 * PI); ctx.fill(); } }
            txt(ctx, tx('total (rescaled)', 'tổng (đã co giãn)'), L + w / 2, H - 5, COL.dim, 'center');
        };
        function upd() {
            var k = ks(); sK.set(fmt(k, 3, lang)); setd(root, { n: n, ks: k.toFixed(3), rolled: sample ? 1 : 0 });
            msg.set(n === 1 ? tx('One die: all six faces are equally likely, so the bars are flat.', 'Một xúc xắc: sáu mặt đều khả năng như nhau nên các cột phẳng.')
                : n < 6 ? tx('With ' + n + ' dice the middle totals are already most likely.', 'Với ' + n + ' xúc xắc, các tổng ở giữa đã là khả dĩ nhất.')
                : tx('With ' + n + ' dice the bars hug the bell curve (largest gap ' + fmt(k, 3, lang) + ').', 'Với ' + n + ' xúc xắc, các cột bám sát đường chuông (chênh lệch lớn nhất ' + fmt(k, 3, lang) + ').'), 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- Diffie-Hellman toy ---- */
    function modpow(b, e, m) { var r = 1; b %= m; while (e > 0) { if (e & 1) r = (r * b) % m; b = (b * b) % m; e >>= 1; } return r; }
    function primRoot(p) { for (var g = 2; g < p; g++) { var ok = true, seen = 1, x = g; for (var k = 1; k < p - 1; k++) { if (x === 1) { ok = false; break; } x = (x * g) % p; } if (ok && x === 1) return g; } return 2; }
    function initDH(root, t, lang) {
        var tx = U(lang), p = 23, g = 5, a = 6, b = 15;
        shell(root, tx('Diffie–Hellman with small numbers', 'Diffie–Hellman với số nhỏ'));
        root.appendChild(el('p', 'mex-note', tx('Alice and Bob keep a and b secret and publish g^a and g^b (mod p). Pick a prime p, then choose their secrets.', 'An và Bình giữ bí mật a và b, công bố g^a và g^b (mod p). Chọn số nguyên tố p rồi chọn bí mật của họ.')));
        var rp = row(), pbtn = {};
        [23, 101, 1009].forEach(function (q) { pbtn[q] = btn('p = ' + q, q === 23 ? 'on' : '', function () { setP(q); }); rp.appendChild(pbtn[q]); }); root.appendChild(rp);
        var sa = slider(tx('Alice secret a', 'Bí mật của An a'), 2, 21, 1, a, function (v) { a = v; upd(); }, function (v) { return String(v); });
        var sb = slider(tx('Bob secret b', 'Bí mật của Bình b'), 2, 21, 1, b, function (v) { b = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sa.wrap); root.appendChild(sb.wrap);
        var st = el('div', 'mex-stats'), sg = stat('g'), sA = stat(tx('Alice sends', 'An gửi')), sB = stat(tx('Bob sends', 'Bình gửi')), kA = stat(tx('Alice key', 'Khóa của An')), kB = stat(tx('Bob key', 'Khóa của Bình')), sT = stat(tx('Eve’s tries', 'Số lần thử của kẻ nghe lén'));
        [sg, sA, sB, kA, kB, sT].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root);
        function setP(q) {
            p = q; g = primRoot(p); Object.keys(pbtn).forEach(function (k) { pbtn[k].className = (+k === p) ? 'on' : ''; });
            [sa, sb].forEach(function (s) { s.input.max = p - 2; });
            a = Math.min(a, p - 2); b = Math.min(b, p - 2); if (p === 101) { a = 37; b = 58; } if (p === 1009) { a = 411; b = 702; } if (p === 23) { a = 6; b = 15; }
            sa.set(a); sb.set(b); upd();
        }
        function upd() {
            var A = modpow(g, a, p), B = modpow(g, b, p), K1 = modpow(B, a, p), K2 = modpow(A, b, p), tries = 0, x = 1;
            do { x = (x * g) % p; tries++; } while (x !== A && tries < p);
            sg.set(g); sA.set(A); sB.set(B); kA.set(K1); kB.set(K2); sT.set(tries);
            setd(root, { p: p, g: g, a: a, b: b, senta: A, sentb: B, key: K1, match: K1 === K2 ? 1 : 0, tries: tries });
            msg.set(tx('Both get the same key ' + K1 + '. Eve sees only p, g, ' + A + ' and ' + B + '; here she finds a by trying powers of g, which took ' + tries + ' tries. With p of 2,000 bits that search is hopeless.', 'Cả hai có cùng khóa ' + K1 + '. Kẻ nghe lén chỉ thấy p, g, ' + A + ' và ' + B + '; ở đây hắn tìm a bằng cách thử các lũy thừa của g, mất ' + tries + ' lần. Với p dài 2.000 bit thì cách thử này vô vọng.'), 'mex-ok');
        }
        setP(23);
    }

    /* ---- Hilbert curve ---- */
    function d2xy(n, d) { var x = 0, y = 0, tt = d, s = 1, rx, ry, tmp; while (s < n) { rx = 1 & (tt >> 1); ry = 1 & (tt ^ rx); if (ry === 0) { if (rx === 1) { x = s - 1 - x; y = s - 1 - y; } tmp = x; x = y; y = tmp; } x += s * rx; y += s * ry; tt >>= 2; s <<= 1; } return [x, y]; }
    function xy2d(n, x, y) { var d = 0, s, rx, ry, tmp; for (s = n >> 1; s > 0; s >>= 1) { rx = (x & s) > 0 ? 1 : 0; ry = (y & s) > 0 ? 1 : 0; d += s * s * ((3 * rx) ^ ry); if (ry === 0) { if (rx === 1) { x = s - 1 - x; y = s - 1 - y; } tmp = x; x = y; y = tmp; } } return d; }
    function initHilbert(root, t, lang) {
        var tx = U(lang), k = 3, pos = 0;
        shell(root, tx('Hilbert curve explorer', 'Khám phá đường cong Hilbert'));
        root.appendChild(el('p', 'mex-note', tx('Raise the order, then slide along the curve or tap a cell to see where it sits on the path.', 'Tăng bậc, rồi kéo dọc đường cong hoặc chạm vào một ô để xem nó nằm ở đâu trên đường đi.')));
        var so = slider(tx('Order', 'Bậc'), 1, 6, 1, k, function (v) { k = v; pos = Math.min(pos, Math.pow(4, k) - 1); sp.input.max = Math.pow(4, k) - 1; sp.set(pos); upd(); }, function (v) { return String(v); });
        var sp = slider(tx('Position along the curve', 'Vị trí dọc đường cong'), 0, 63, 1, 0, function (v) { pos = v; upd(); }, function (v) { return String(v); });
        root.appendChild(so.wrap); root.appendChild(sp.wrap);
        var cv = canvas(1); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sC = stat(tx('cells', 'số ô')), sL = stat(tx('length (side = 1)', 'độ dài (cạnh = 1)')), sX = stat(tx('this cell', 'ô này'));
        [sC, sL, sX].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root);
        function geom() { var W = cv.w, m = 8, n = Math.pow(2, k), s = (W - 2 * m) / n; return { m: m, n: n, s: s }; }
        cv.c.addEventListener('pointerdown', function (e) { var r = cv.c.getBoundingClientRect(), G = geom(), px = (e.clientX - r.left) * cv.w / r.width, py = (e.clientY - r.top) * cv.h / r.height; var cx = Math.floor((px - G.m) / G.s), cy = G.n - 1 - Math.floor((py - G.m) / G.s); if (cx >= 0 && cy >= 0 && cx < G.n && cy < G.n) { pos = xy2d(G.n, cx, cy); sp.set(pos); upd(); } });
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, G = geom(), N = G.n * G.n, i, p, q;
            ctx.clearRect(0, 0, W, H);
            var C = function (xy) { return [G.m + (xy[0] + 0.5) * G.s, H - G.m - (xy[1] + 0.5) * G.s]; };
            if (k <= 4) { ctx.strokeStyle = '#1f2433'; ctx.lineWidth = 1; for (i = 0; i <= G.n; i++) { ctx.beginPath(); ctx.moveTo(G.m + i * G.s, G.m); ctx.lineTo(G.m + i * G.s, H - G.m); ctx.moveTo(G.m, G.m + i * G.s); ctx.lineTo(W - G.m, G.m + i * G.s); ctx.stroke(); } }
            ctx.lineWidth = k <= 3 ? 3.5 : k <= 5 ? 2 : 1.2; ctx.lineCap = 'round';
            p = C(d2xy(G.n, 0));
            for (i = 1; i < N; i++) { q = C(d2xy(G.n, i)); ctx.strokeStyle = 'hsl(' + Math.round(200 - 200 * i / N) + ',85%,62%)'; ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(q[0], q[1]); ctx.stroke(); p = q; }
            var cxy = d2xy(G.n, pos), c0 = C(cxy);
            ctx.fillStyle = 'rgba(255,255,255,0.9)'; ctx.beginPath(); ctx.arc(c0[0], c0[1], Math.max(4, G.s * 0.28), 0, 2 * PI); ctx.fill();
            ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; ctx.strokeRect(G.m + cxy[0] * G.s, H - G.m - (cxy[1] + 1) * G.s, G.s, G.s);
        };
        function upd() {
            var N = Math.pow(4, k), xy = d2xy(Math.pow(2, k), pos);
            sC.set(kfmt(N, lang)); sL.set(fmt((N - 1) / Math.pow(2, k), 2, lang)); sX.set(pos + ' → (' + xy[0] + ',' + xy[1] + ')');
            setd(root, { order: k, cells: N, pos: pos, x: xy[0], y: xy[1] });
            msg.set(tx('Order ' + k + ' visits all ' + kfmt(N, lang) + ' cells in one unbroken path, and consecutive cells are always neighbours. The length keeps roughly doubling with each order.', 'Bậc ' + k + ' đi qua cả ' + kfmt(N, lang) + ' ô trong một đường liền mạch, và hai ô liên tiếp luôn kề nhau. Độ dài gần như gấp đôi sau mỗi bậc.'), 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); sp.input.max = 63; upd(); });
    }

    /* ---- ball volume ---- */
    function ballV(n) { var v = n % 2 ? 2 : PI, i = n % 2 ? 3 : 4; if (n === 1) return 2; if (n === 2) return PI; for (; i <= n; i += 2) v *= 2 * PI / i; return v; }
    function initBall(root, t, lang) {
        var tx = U(lang), n = 3;
        shell(root, tx('Volume of the unit ball', 'Thể tích quả cầu đơn vị'));
        root.appendChild(el('p', 'mex-note', tx('Slide the dimension n. The cube [−1, 1]ⁿ always has volume 2ⁿ and just contains the ball.', 'Kéo số chiều n. Hình lập phương [−1, 1]ⁿ luôn có thể tích 2ⁿ và vừa chứa quả cầu.')));
        var sl = slider(tx('Dimension n', 'Số chiều n'), 1, 30, 1, n, function (v) { n = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sl.wrap);
        var cv = canvas(0.55); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sV = stat(tx('ball volume', 'thể tích quả cầu')), sF = stat(tx('share of the cube', 'tỉ lệ so với hình lập phương')), sD = stat(tx('corner distance', 'khoảng cách tới đỉnh'));
        [sV, sF, sD].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, L = 28, R = 6, T = 8, B = 20, w = W - L - R, h = H - T - B, i;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 6, 3);
            var bw = w / 30;
            for (i = 1; i <= 30; i++) { var v = ballV(i), hh = h * v / 6; ctx.fillStyle = i === n ? COL.sun : (i <= 5 ? COL.sky : COL.pink); ctx.fillRect(L + (i - 1) * bw + 1, T + h - hh, bw - 2, hh); }
            [0, 2, 4, 6].forEach(function (v) { txt(ctx, String(v), L - 4, T + h - h * v / 6 + 4, COL.dim, 'right'); });
            [1, 5, 10, 15, 20, 25, 30].forEach(function (v) { txt(ctx, String(v), L + (v - 0.5) * bw, H - 6, COL.dim, 'center'); });
        };
        function upd() {
            var v = ballV(n), f = v / Math.pow(2, n);
            sV.set(v >= 0.01 ? fmt(v, 3, lang) : v.toExponential(2).replace('e-', '·10⁻').replace('.', lang === 'vi' ? ',' : '.'));
            sF.set(f >= 0.001 ? fmt(f * 100, 2, lang) + ' %' : f.toExponential(1).replace('e-', '·10⁻').replace('.', lang === 'vi' ? ',' : '.'));
            sD.set('√' + n + ' ≈ ' + fmt(Math.sqrt(n), 2, lang));
            setd(root, { n: n, vol: v.toFixed(4) });
            msg.set(n < 5 ? tx('Still growing: each extra dimension adds more room than the ball loses.', 'Vẫn đang tăng: mỗi chiều thêm cho quả cầu nhiều chỗ hơn là nó mất.')
                : n === 5 ? tx('The peak: the unit ball is largest in dimension 5 (about 5.26).', 'Đỉnh: quả cầu đơn vị lớn nhất ở chiều 5 (khoảng 5,26).')
                : tx('Past the peak it shrinks toward 0, while the cube corners sit √n away from the centre: the ball misses almost the whole cube.', 'Qua đỉnh nó co về 0, còn các đỉnh hình lập phương cách tâm √n: quả cầu bỏ sót gần như cả hình lập phương.'), 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- catenoid ---- */
    function initCatenoid(root, t, lang) {
        var tx = U(lang), d = 0.5;
        var hf = function (a) { return a * Math.acosh(1 / a); }, lo = 1e-3, hi = 1, i;
        for (i = 0; i < 200; i++) { var m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3; if (hf(m1) < hf(m2)) lo = m1; else hi = m2; }
        var AC = (lo + hi) / 2, HC = hf(AC);
        var aOf = function (h) { var l = AC, r = 1, mid; for (var j = 0; j < 80; j++) { mid = (l + r) / 2; if (hf(mid) > h) l = mid; else r = mid; } return (l + r) / 2; };
        var area = function (h) { var a = aOf(h); return PI * (2 * a * h + a * a * Math.sinh(2 * h / a)); };
        var l2 = 0.01, r2 = HC; for (i = 0; i < 80; i++) { var md = (l2 + r2) / 2; if (area(md) < 2 * PI) l2 = md; else r2 = md; }
        var HG = (l2 + r2) / 2;
        shell(root, tx('A soap film between two rings', 'Màng xà phòng giữa hai vòng'));
        root.appendChild(el('p', 'mex-note', tx('Both rings have radius 1. Pull them apart and watch the film.', 'Hai vòng đều có bán kính 1. Kéo chúng ra xa và quan sát màng.')));
        var sl = slider(tx('Distance between rings', 'Khoảng cách hai vòng'), 0.05, 1.45, 0.01, d, function (v) { d = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        root.appendChild(sl.wrap);
        var cv = canvas(0.75); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sF = stat(tx('film area', 'diện tích màng')), sT = stat(tx('two flat discs', 'hai đĩa phẳng'));
        st.appendChild(sF.box); st.appendChild(sT.box); root.appendChild(st);
        var msg = mk(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, S = Math.min(W * 0.34, H * 0.5), cx = W / 2, cy = H / 2, h = d / 2, broken = h > HC, j;
            ctx.clearRect(0, 0, W, H);
            var P = function (r, z) { return [cx + r * S, cy - z * S]; };
            ctx.strokeStyle = COL.dim; ctx.lineWidth = 3; [h, -h].forEach(function (z) { var A = P(-1.12, z), B = P(1.12, z); ctx.beginPath(); ctx.moveTo(A[0], A[1]); ctx.lineTo(B[0], B[1]); ctx.stroke(); });
            if (!broken) {
                var a = aOf(h), R = [], Lf = [];
                for (j = 0; j <= 60; j++) { var z = -h + 2 * h * j / 60; R.push(P(a * Math.cosh(z / a), z)); Lf.push(P(-a * Math.cosh(z / a), z)); }
                ctx.fillStyle = 'rgba(76,201,240,0.28)'; ctx.beginPath(); R.forEach(function (q, k) { if (k) ctx.lineTo(q[0], q[1]); else ctx.moveTo(q[0], q[1]); }); Lf.slice().reverse().forEach(function (q) { ctx.lineTo(q[0], q[1]); }); ctx.closePath(); ctx.fill();
                ctx.strokeStyle = COL.sky; ctx.lineWidth = 3; [R, Lf].forEach(function (c) { ctx.beginPath(); c.forEach(function (q, k) { if (k) ctx.lineTo(q[0], q[1]); else ctx.moveTo(q[0], q[1]); }); ctx.stroke(); });
            } else { ctx.strokeStyle = COL.sky; ctx.lineWidth = 6; [h, -h].forEach(function (z) { var A = P(-1, z), B = P(1, z); ctx.beginPath(); ctx.moveTo(A[0], A[1]); ctx.lineTo(B[0], B[1]); ctx.stroke(); }); }
            ctx.fillStyle = COL.sun; [h, -h].forEach(function (z) { [-1, 1].forEach(function (s) { var q = P(s, z); ctx.beginPath(); ctx.arc(q[0], q[1], 5, 0, 2 * PI); ctx.fill(); }); });
        };
        function upd() {
            var h = d / 2, st_, A;
            if (h > HC) { st_ = 'broken'; A = null; } else { A = area(h); st_ = A < 2 * PI ? 'catenoid' : 'weak'; }
            sF.set(A === null ? '—' : fmt(A, 2, lang)); sT.set(fmt(2 * PI, 2, lang));
            setd(root, { d: d.toFixed(2), state: st_, area: A === null ? 'none' : A.toFixed(2) });
            msg.set(st_ === 'catenoid' ? tx('The film is a catenoid and has less area than two flat discs would.', 'Màng là một catenoid và có diện tích nhỏ hơn hai đĩa phẳng.')
                : st_ === 'weak' ? tx('The film still stands, but two flat discs would now have less area (from about ' + fmt(2 * HG, 2, lang) + ').', 'Màng vẫn đứng, nhưng hai đĩa phẳng giờ có diện tích nhỏ hơn (từ khoảng ' + fmt(2 * HG, 2, lang) + ').')
                : tx('Too far apart (beyond about ' + fmt(2 * HC, 2, lang) + '): no catenoid fits between the rings, so the film pops into two discs.', 'Quá xa (vượt khoảng ' + fmt(2 * HC, 2, lang) + '): không catenoid nào nằm giữa hai vòng, màng vỡ thành hai đĩa.'), st_ === 'broken' ? 'mex-bad' : st_ === 'weak' ? 'mex-warn' : 'mex-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- CHSH ---- */
    function initCHSH(root, t, lang) {
        var tx = U(lang), A = [0, 90, 45, -45];
        shell(root, tx('The CHSH game', 'Trò chơi CHSH'));
        root.appendChild(el('p', 'mex-note', tx('S = E(a₀,b₀) + E(a₀,b₁) + E(a₁,b₀) − E(a₁,b₁). Any fixed classical strategy gives |S| = 2, so no mixture beats 2. For an entangled pair, quantum theory predicts E = cos(angle difference).', 'S = E(a₀,b₀) + E(a₀,b₁) + E(a₁,b₀) − E(a₁,b₁). Mọi chiến lược cổ điển cố định cho |S| = 2, nên không hỗn hợp nào vượt 2. Với cặp vướng víu, lý thuyết lượng tử dự đoán E = cos(hiệu góc).')));
        var names = ['a₀', 'a₁', 'b₀', 'b₁'], sls = [];
        names.forEach(function (nm, i) { var s = slider(tx('Angle ', 'Góc ') + nm + (i < 2 ? tx(' (Alice)', ' (An)') : tx(' (Bob)', ' (Bình)')), -180, 180, 1, A[i], function (v) { A[i] = v; upd(); }, function (v) { return Math.round(v) + '°'; }); sls.push(s); root.appendChild(s.wrap); });
        var r = row(); r.appendChild(btn(tx('Best angles', 'Góc tốt nhất'), 'on', function () { A = [0, 90, 45, -45]; sync(); })); r.appendChild(btn(tx('All equal', 'Cùng một góc'), '', function () { A = [0, 0, 0, 0]; sync(); })); r.appendChild(btn(tx('Random', 'Ngẫu nhiên'), '', function () { A = A.map(function () { return Math.round(Math.random() * 360 - 180); }); sync(); })); root.appendChild(r);
        var cv = canvas(0.62); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sS = stat('S'); st.appendChild(sS.box); root.appendChild(st);
        var msg = mk(root);
        function sync() { sls.forEach(function (s, i) { s.set(A[i]); }); upd(); }
        var E = function (x, y) { return Math.cos((x - y) * PI / 180); };
        function val() { return E(A[0], A[2]) + E(A[0], A[3]) + E(A[1], A[2]) - E(A[1], A[3]); }
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, R = Math.min(H * 0.42, W * 0.22), cx = W * 0.27, cy = H * 0.5;
            ctx.clearRect(0, 0, W, H);
            ctx.strokeStyle = COL.dim; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx, cy, R, 0, 2 * PI); ctx.stroke();
            A.forEach(function (a, i) { var c = i < 2 ? COL.sky : COL.pink, x = cx + R * Math.cos(a * PI / 180), y = cy - R * Math.sin(a * PI / 180); ctx.strokeStyle = c; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(x, y); ctx.stroke(); ctx.fillStyle = c; ctx.beginPath(); ctx.arc(x, y, 5, 0, 2 * PI); ctx.fill(); txt(ctx, names[i], cx + (R + 16) * Math.cos(a * PI / 180), cy - (R + 16) * Math.sin(a * PI / 180) + 4, c, 'center', '13px sans-serif'); });
            var s = val(), bx = W * 0.58, bw = W * 0.38, sx = function (v) { return bx + bw * v / 3; }, by = cy - 14;
            ctx.fillStyle = '#1d2130'; ctx.fillRect(bx, by, bw, 28);
            ctx.fillStyle = Math.abs(s) > 2 + 1e-9 ? COL.mint : COL.sky; ctx.fillRect(bx, by, bw * Math.min(3, Math.abs(s)) / 3, 28);
            ctx.strokeStyle = COL.orange; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(sx(2), by - 8); ctx.lineTo(sx(2), by + 36); ctx.stroke();
            txt(ctx, '2', sx(2), by + 52, COL.orange, 'center', '12px sans-serif'); txt(ctx, '|S|', bx, by - 12, COL.dim, 'left', '12px sans-serif'); txt(ctx, '3', bx + bw, by + 52, COL.dim, 'right', '12px sans-serif');
            txt(ctx, tx('classical limit', 'giới hạn cổ điển'), sx(2), by + 68, COL.orange, 'center', '11px sans-serif');
        };
        function upd() {
            var s = val(); sS.set(fmt(s, 2, lang)); setd(root, { s: s.toFixed(2) });
            msg.set(Math.abs(s) > 2 + 1e-9 ? tx('|S| = ' + fmt(Math.abs(s), 2, lang) + ' is above 2: beyond every classical strategy. The most quantum theory allows is 2√2 ≈ 2.83.', '|S| = ' + fmt(Math.abs(s), 2, lang) + ' vượt 2: hơn mọi chiến lược cổ điển. Lý thuyết lượng tử cho phép tối đa 2√2 ≈ 2,83.')
                : tx('|S| = ' + fmt(Math.abs(s), 2, lang) + ': a classical strategy could do this well. Try “Best angles”.', '|S| = ' + fmt(Math.abs(s), 2, lang) + ': một chiến lược cổ điển cũng đạt được. Thử “Góc tốt nhất”.'), Math.abs(s) > 2 + 1e-9 ? 'mex-ok' : 'mex-warn');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- SIR ---- */
    function sirRun(R0, i0) {
        var s = 1 - i0, i = i0, dt = 0.02, steps = 2000, out = { t: [], S: [], I: [], R: [] }, pk = i0, pt = 0, k;
        var f = function (s, i) { return [-R0 * s * i, R0 * s * i - i]; };
        for (k = 0; k <= steps; k++) {
            if (k % 5 === 0) { out.t.push(k * dt); out.S.push(s); out.I.push(i); out.R.push(1 - s - i); }
            if (i > pk) { pk = i; pt = k * dt; }
            var a = f(s, i), b = f(s + dt / 2 * a[0], i + dt / 2 * a[1]), c = f(s + dt / 2 * b[0], i + dt / 2 * b[1]), d = f(s + dt * c[0], i + dt * c[1]);
            s += dt / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0]); i += dt / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1]);
        }
        out.peak = pk; out.tpeak = pt; out.total = 1 - s; return out;
    }
    function initSIR(root, t, lang) {
        var tx = U(lang), R0 = 2, i0 = 3;
        shell(root, tx('SIR epidemic', 'Dịch SIR'));
        root.appendChild(el('p', 'mex-note', tx('Time is measured in infectious periods. R₀ is how many people one case infects at the start.', 'Thời gian tính bằng số kỳ lây nhiễm. R₀ là số người một ca bệnh lây lúc đầu.')));
        var s1 = slider('R₀', 0.5, 4, 0.1, R0, function (v) { R0 = v; upd(); }, function (v) { return fmt(v, 1, lang); });
        var s2 = slider(tx('Initially infected', 'Nhiễm lúc đầu'), 1, 10, 1, i0, function (v) { i0 = v; upd(); }, function (v) { return Math.round(v) + ' %'; });
        root.appendChild(s1.wrap); root.appendChild(s2.wrap);
        var cv = canvas(0.62); root.appendChild(cv.c);
        var st = el('div', 'mex-stats'), sP = stat(tx('peak infected', 'đỉnh số ca')), sT = stat(tx('time of peak', 'thời điểm đỉnh')), sF = stat(tx('ever infected', 'tổng số từng nhiễm'));
        [sP, sT, sF].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root), run = null;
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, L = 34, Rr = 8, T = 10, B = 22, w = W - L - Rr, h = H - T - B, k;
            ctx.clearRect(0, 0, W, H); gridLines(ctx, L, T, w, h, 4, 4);
            [[run.S, COL.sky], [run.R, COL.mint], [run.I, COL.pink]].forEach(function (c) { ctx.strokeStyle = c[1]; ctx.lineWidth = 2.5; ctx.beginPath(); for (k = 0; k < run.t.length; k++) { var x = L + w * run.t[k] / 40, y = T + h - h * c[0][k]; if (k === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y); } ctx.stroke(); });
            [0, 0.5, 1].forEach(function (v) { txt(ctx, Math.round(v * 100) + '%', L - 4, T + h - h * v + 4, COL.dim, 'right'); });
            [0, 10, 20, 30, 40].forEach(function (v) { txt(ctx, String(v), L + w * v / 40, H - 6, COL.dim, 'center'); });
            txt(ctx, tx('susceptible', 'dễ nhiễm'), L + 6, T + 14, COL.sky); txt(ctx, tx('infected', 'đang nhiễm'), L + 6, T + 28, COL.pink); txt(ctx, tx('recovered', 'đã khỏi'), L + 6, T + 42, COL.mint);
        };
        function upd() {
            run = sirRun(R0, i0 / 100);
            sP.set(fmt(run.peak * 100, 1, lang) + ' %'); sT.set(fmt(run.tpeak, 1, lang)); sF.set(fmt(run.total * 100, 0, lang) + ' %');
            setd(root, { r0: R0.toFixed(1), peak: (run.peak * 100).toFixed(1), total: (run.total * 100).toFixed(0) });
            msg.set(R0 <= 1.0001 ? tx('R₀ at most 1: each case infects fewer than one other, so the outbreak fades away.', 'R₀ không quá 1: mỗi ca lây chưa tới một người khác nên dịch tắt dần.')
                : tx('R₀ above 1: the outbreak grows to a peak of ' + fmt(run.peak * 100, 1, lang) + ' % and in the end ' + fmt(run.total * 100, 0, lang) + ' % have been infected.', 'R₀ trên 1: dịch tăng tới đỉnh ' + fmt(run.peak * 100, 1, lang) + ' % và cuối cùng ' + fmt(run.total * 100, 0, lang) + ' % đã từng nhiễm.'), R0 <= 1.0001 ? 'mex-ok' : 'mex-warn');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---- optimal transport on a line ---- */
    function initOT(root, t, lang) {
        var tx = U(lang), SRC = [0.6, 1.9, 3.1, 4.6, 6.4, 8.3], DST = [1.2, 2.7, 4.0, 5.5, 7.2, 9.1], sg = [2, 0, 3, 1, 5, 4], sel = -1;
        shell(root, tx('Matching sand piles to holes', 'Ghép đống cát với hố'));
        root.appendChild(el('p', 'mex-note', tx('Each pile goes into one hole; the cost of a move is (distance)². Tap two piles to swap their holes.', 'Mỗi đống cát vào một hố; chi phí mỗi lần chuyển là (quãng đường)². Chạm hai đống cát để đổi hố của chúng.')));
        var cv = canvas(0.6); root.appendChild(cv.c);
        var r = row(); r.appendChild(btn(tx('Shuffle', 'Xáo trộn'), '', function () { for (var i = 5; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), q = sg[i]; sg[i] = sg[j]; sg[j] = q; } sel = -1; upd(); })); r.appendChild(btn(tx('Sort', 'Sắp xếp'), '', function () { sg = [0, 1, 2, 3, 4, 5]; sel = -1; upd(); })); root.appendChild(r);
        var st = el('div', 'mex-stats'), sC = stat(tx('your cost', 'chi phí của bạn')), sB = stat(tx('cheapest possible', 'rẻ nhất có thể')), sX = stat(tx('crossings', 'chỗ cắt nhau'));
        [sC, sB, sX].forEach(function (q) { st.appendChild(q.box); }); root.appendChild(st);
        var msg = mk(root), last = null;
        var cost = function (p) { var c = 0; for (var i = 0; i < 6; i++) c += (SRC[i] - DST[p[i]]) * (SRC[i] - DST[p[i]]); return c; };
        var xs = function (v) { return 14 + (cv.w - 28) * v / 9.8; };
        var YT = function () { return cv.h * 0.2; }, YB = function () { return cv.h * 0.8; };
        cv.c.addEventListener('pointerdown', function (e) {
            var rc = cv.c.getBoundingClientRect(), px = (e.clientX - rc.left) * cv.w / rc.width, py = (e.clientY - rc.top) * cv.h / rc.height, best = -1, bd = 1e9;
            for (var i = 0; i < 6; i++) { var d = Math.abs(px - xs(SRC[i])) + Math.abs(py - YT()) * 0.5; if (d < bd) { bd = d; best = i; } }
            if (bd > 40) return;
            if (sel < 0) { sel = best; upd(); }
            else if (sel === best) { sel = -1; upd(); }
            else { var before = cost(sg), q = sg[sel]; sg[sel] = sg[best]; sg[best] = q; sel = -1; var after_ = cost(sg); last = after_ < before - 1e-9 ? 'down' : after_ > before + 1e-9 ? 'up' : 'same'; upd(); }
        });
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx, W = cv.w, H = cv.h, i;
            ctx.clearRect(0, 0, W, H);
            ctx.strokeStyle = '#2a3045'; ctx.lineWidth = 2; [YT(), YB()].forEach(function (y) { ctx.beginPath(); ctx.moveTo(10, y); ctx.lineTo(W - 10, y); ctx.stroke(); });
            for (i = 0; i < 6; i++) { ctx.strokeStyle = sg[i] === i ? COL.mint : COL.sun; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(xs(SRC[i]), YT()); ctx.lineTo(xs(DST[sg[i]]), YB()); ctx.stroke(); }
            for (i = 0; i < 6; i++) { var x = xs(SRC[i]), y = YT(); ctx.fillStyle = i === sel ? COL.sun : COL.sky; ctx.beginPath(); ctx.moveTo(x, y - 14); ctx.lineTo(x - 11, y + 8); ctx.lineTo(x + 11, y + 8); ctx.closePath(); ctx.fill(); if (i === sel) { ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; ctx.stroke(); } }
            for (i = 0; i < 6; i++) { ctx.fillStyle = COL.pink; ctx.beginPath(); ctx.arc(xs(DST[i]), YB(), 9, 0, 2 * PI); ctx.fill(); }
            txt(ctx, tx('sand', 'cát'), 10, YT() - 22, COL.sky); txt(ctx, tx('holes', 'hố'), 10, YB() + 26, COL.pink);
        };
        function upd() {
            var c = cost(sg), best = cost([0, 1, 2, 3, 4, 5]), cr = 0, i, j;
            for (i = 0; i < 6; i++) for (j = i + 1; j < 6; j++) if (sg[i] > sg[j]) cr++;
            sC.set(fmt(c, 1, lang)); sB.set(fmt(best, 1, lang)); sX.set(cr);
            setd(root, { cost: c.toFixed(1), best: best.toFixed(1), cross: cr, sel: sel });
            msg.set(sel >= 0 ? tx('Now tap another pile to swap holes with it.', 'Giờ chạm một đống khác để đổi hố với nó.')
                : cr === 0 ? tx('No paths cross: this matching is in sorted order, and no other matching is cheaper.', 'Không đường nào cắt nhau: phép ghép này theo thứ tự và không phép ghép nào rẻ hơn.')
                : last === 'down' ? tx('Cheaper! Swapping two crossing paths lowers the cost.', 'Rẻ hơn! Đổi hai đường cắt nhau làm chi phí giảm.')
                : last === 'up' ? tx('More expensive: that swap made the paths cross more.', 'Đắt hơn: lần đổi đó làm các đường cắt nhau nhiều hơn.')
                : tx('Tap a pile, then another pile, to swap their holes.', 'Chạm một đống rồi một đống khác để đổi hố.'), cr === 0 ? 'mex-ok' : 'mex-warn');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    var INIT = { collatz: initCollatz, logistic: initLogistic, fourier: initFourier, chaosgame: initChaos, konigsberg: initKonigsberg,
        zeta: initZeta, twins: initTwins, kakeya: initKakeya, clt: initCLT, dh: initDH, hilbert: initHilbert, ball: initBall, catenoid: initCatenoid, chsh: initCHSH, sir: initSIR, ot: initOT };
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
