import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import TarjanExplainer from './TarjanExplainer.svelte';

mountAll('[data-demo="tarjan-explainer"]', TarjanExplainer, (el) => ({
  preset: attr(el, 'preset', 'sixNode'),
  lang: attr(el, 'lang', 'vi'),
}));
