// Bundle list: key = Vite mode = output file name (public/js/explainers/<key>.js).
export const ENTRIES = {
  'pagerank-explainer': { entry: 'src/pagerank/main.js', name: 'PageRankExplainer' },
  'fourcolor-explainer': { entry: 'src/fourcolor/main.js', name: 'FourColorExplainer' },
  'zkp-explainer': { entry: 'src/zkp/main.js', name: 'ZkpExplainer' },
  'tarjan-explainer': { entry: 'src/tarjan/main.js', name: 'TarjanExplainer' },
};
