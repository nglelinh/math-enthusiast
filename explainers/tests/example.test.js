import test from 'node:test';
import assert from 'node:assert/strict';
import { PRESETS, steps } from '../src/example/example.js';

test('running sum matches the closed form for every preset and n', () => {
  for (const p of PRESETS)
    for (let n = 1; n <= 30; n++) {
      const s = steps(p.id, n);
      assert.equal(s.length, n);
      assert.ok(s.every((x) => x.ok), `${p.id} n=${n}`);
    }
});
