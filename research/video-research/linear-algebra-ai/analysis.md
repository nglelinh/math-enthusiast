# Mode B — Video / research analysis: Linear Algebra → AI

**Disclaimer:** Full machine transcripts were not loaded for every URL in this pack. Claims below are cross-checked against standard textbooks, course essays, and primary video metadata/slogans. Popular videos are for orientation unless marked CORE.

---

## 1. Metadata — primary focus source

| Field | Value |
|-------|--------|
| Title | But what is a neural network? | Deep learning chapter 1 |
| Speaker / channel | 3Blue1Brown (Grant Sanderson) |
| URL | https://www.youtube.com/watch?v=aircAruvnKk |
| Duration | ~19 min |
| Level | 1–2 |
| Role | ORIENTATION + CORE (layers as matrix maps + nonlinearities) |

---

## 2. Key definitions (course-aligned)

### Affine layer

$$x\mapsto Wx+b$$; compositions of affine maps stay affine — hence nonlinear activations.

### SVD/PCA

Best low-rank approximation in Frobenius/spectral norms; PCA via top right singular vectors of centered data.

### Backprop

Reverse-mode automatic differentiation / chain rule on a computational graph.

### Attention slogan

Core mixing is matrix products + softmax; still linear-algebra-centric.

---

## 3. Extracted slogans / takeaways

- Neural nets are affine *plus* nonlinearities; pure linear depth collapses.
- Backprop is systematic chain rule, not a new algebra.
- Attention/transformers are structured matrix multiplies at scale.
- Strang 18.06 gives the geometric foundation; 3B1B DL series shows the ML pipeline.

---

## 4. Popular videos — claims hygiene

| Source tier | Useful for | Watch-out |
|-------------|------------|-----------|
| ORIENTATION popular (Numberphile, Veritasium, Vsauce) | Motivation, pictures, culture | May omit hypotheses, edge cases, or overstate certainty |
| 3Blue1Brown | Geometric intuition | Not a full theorem course; pair with OCW/texts |
| MIT OCW / university | Foundations | Longer; sample lectures, don't binge entire terms mid-essay |
| FRONTIER / news | Open problems and breakthroughs | Check primary papers for precise statements |

---

## 5. Knowledge gaps (honest)

| Gap | Severity | How to close |
|-----|----------|--------------|
| Timestamped full transcripts for every URL | Medium | Optional `extract-video-knowledge` on top 2–3 URLs |
| Frame captures for slides | Low for text course | Optional `img/video_research/linear-algebra-ai/` |
| Rapidly moving frontiers (e.g. monotile variants, PQC standards) | Medium | Re-check arXiv/NIST when assigning |

---

## 6. Curriculum map

- Chapter: **03**
- Lesson order: **3**
- Pack path: `research/video-research/linear-algebra-ai/`
- Enrich EN/VI lessons with Video sources + References pointing here.
