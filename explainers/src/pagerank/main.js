import '../shared/ui.css';
import { attr, mountAll } from '../shared/mount.js';
import PageRankExplainer from './PageRankExplainer.svelte';

mountAll('[data-demo="pagerank-explainer"]', PageRankExplainer, (el) => ({
  preset: attr(el, 'preset', 'dangling'),
  alpha: Number(attr(el, 'alpha', '0.85')),
  lang: attr(el, 'lang', 'vi'),
}));
