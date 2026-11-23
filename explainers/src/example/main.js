import '../shared/ui.css';
import ExampleExplainer from './ExampleExplainer.svelte';
import { mountAll, attr } from '../shared/mount.js';

// <div data-demo="example-explainer" data-preset="sum|odd" data-n="6"></div>
mountAll('[data-demo="example-explainer"]', ExampleExplainer, (el) => ({
  preset: attr(el, 'preset', 'sum'),
  n: Number(attr(el, 'n', '6'))
}));
