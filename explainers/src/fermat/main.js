import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import FermatExplainer from './FermatExplainer.svelte';

mountAll('[data-demo="fermat-explainer"]', FermatExplainer, (el) => ({
  preset: attr(el, 'preset', 'frey'),
  lang: attr(el, 'lang', 'vi'),
}));
