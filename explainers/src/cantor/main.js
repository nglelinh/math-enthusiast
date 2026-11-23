import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import CantorExplainer from './CantorExplainer.svelte';

mountAll('[data-demo="cantor-explainer"]', CantorExplainer, (el) => ({
  preset: attr(el, 'preset', 'safeFlip'),
  lang: attr(el, 'lang', 'vi'),
}));
