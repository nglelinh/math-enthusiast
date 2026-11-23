import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import ZkpExplainer from './ZkpExplainer.svelte';

mountAll('[data-demo="zkp-explainer"]', ZkpExplainer, (el) => ({
  preset: attr(el, 'preset', 'honest'),
  lang: attr(el, 'lang', 'vi'),
}));
