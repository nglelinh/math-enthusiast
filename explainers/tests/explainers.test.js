import test from 'node:test';
import assert from 'node:assert/strict';
import { steps as prSteps } from '../src/pagerank/pagerank.js';
import { heawood, steps as fcSteps } from '../src/fourcolor/fourcolor.js';
import { EDGES as ZKP_EDGES, catchProbability, steps as zkpSteps } from '../src/zkp/zkp.js';
import { steps as tarjanSteps } from '../src/tarjan/tarjan.js';

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
  const s1 = tarjanSteps('sixNode');
  assert.deepEqual(s1.at(-1).sccs, [[5], [3, 4], [0, 1, 2]]);
  const s2 = tarjanSteps('twoCycles');
  assert.deepEqual(s2.at(-1).sccs, [[3, 4], [0, 1, 2]]);
});
