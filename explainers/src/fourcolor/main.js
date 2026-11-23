import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import FourColorExplainer from './FourColorExplainer.svelte';

mountAll('[data-demo="fourcolor-explainer"]', FourColorExplainer, (el) => ({
  preset: attr(el, 'preset', 'k4'),
  lang: attr(el, 'lang', 'vi'),
}));
