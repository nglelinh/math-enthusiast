import test from 'node:test';
import assert from 'node:assert/strict';
import { steps as prSteps } from '../src/pagerank/pagerank.js';
import { heawood, steps as fcSteps } from '../src/fourcolor/fourcolor.js';
import { EDGES as ZKP_EDGES, catchProbability, steps as zkpSteps } from '../src/zkp/zkp.js';
import { steps as tarjanSteps } from '../src/tarjan/tarjan.js';
import { checkFermat, steps as fermatSteps } from '../src/fermat/fermat.js';
import { sinkhorn } from '../src/ot/ot.js';
import { PRESETS as CANTOR_PRESETS, diagonalDigits, steps as cantorSteps } from '../src/cantor/cantor.js';

test('pagerank converges to A > C > B > D and leaks if dangling unfixed', () => {
  const fixed = prSteps('dangling', 0.85, true, 'vi', 35);
  const last = fixed.at(-1);
  assert.ok(Math.abs(last.sum - 1) < 1e-9);
  assert.equal(last.ranked, 'A > C > B > D');
  assert.ok(Math.abs(last.pi[0] - 0.3272) < 1e-3);
  const leaked = prSteps('dangling', 0.85, false, 'vi', 20);
  assert.ok(leaked.at(-1).sum < 0.25);
});

test('fourcolor Heawood numbers and Kempe presets', () => {
  assert.equal(heawood(0), 4);
  assert.equal(heawood(1), 7);
  assert.equal(heawood(2), 8);
  assert.equal(fcSteps('k4').at(-1).ok, false);
  assert.equal(fcSteps('kempeFree').at(-1).ok, true);
  assert.equal(fcSteps('kempeBarrier').at(-1).ok, true);
});

test('zkp honest passes all edges, cheater caught on bad edge, soundness > 95% at k=20', () => {
  for (let p = 0; p < 6; p++) {
    for (let e = 0; e < ZKP_EDGES.length; e++) {
      assert.equal(zkpSteps('honest', p, e).at(-1).ok, true);
    }
  }
  assert.equal(zkpSteps('cheater', 0, 4).at(-1).ok, false);
  assert.ok(catchProbability(20) > 0.95);
});

test('tarjan produces exact SCCs for both presets', () => {
  assert.deepEqual(tarjanSteps('sixNode').at(-1).sccs, [[5], [3, 4], [0, 1, 2]]);
  assert.deepEqual(tarjanSteps('twoCycles').at(-1).sccs, [[3, 4], [0, 1, 2]]);
});

test('fermat checks exact BigInt arithmetic and Wiles stages', () => {
  assert.equal(checkFermat(3, 4, 5, 2).eq, true);
  assert.equal(checkFermat(1782, 1841, 1922, 12).eq, false);
  assert.equal(fermatSteps('frey').at(-1).ok, true);
});

test('optimal transport Sinkhorn preserves marginals', () => {
  const res = sinkhorn('mongeSplit', 2, 0.1, 40);
  assert.ok(Math.abs(res.plan[0][0] - 0.5) < 1e-3);
  assert.ok(Math.abs(res.plan[0][1] - 0.5) < 1e-3);
});

test('cantor diagonal differs from every row at diagonal index', () => {
  const rows = CANTOR_PRESETS.pitfall09.rows;
  const y = diagonalDigits(rows);
  rows.forEach((r, i) => {
    assert.notEqual(y[i], r[i]);
    assert.ok(y[i] === 1 || y[i] === 2);
  });
  assert.equal(cantorSteps('safeFlip').length, 8);
});
