import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import OtExplainer from './OtExplainer.svelte';

mountAll('[data-demo="ot-explainer"]', OtExplainer, (el) => ({
  preset: attr(el, 'preset', 'threeBars'),
  lang: attr(el, 'lang', 'vi'),
}));
