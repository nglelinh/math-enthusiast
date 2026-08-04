# Mode B — Video / research analysis: Mathematics of AI / Deep Learning

**Disclaimer:** No full machine transcripts are claimed in this pack unless separately extracted.  
Claims are cross-checked against standard references (Wikipedia, arXiv, textbooks, institute pages).  
Popular-video details are role/metadata level unless noted.

---

## 1. Metadata — recommended videos

| ID | Title | Role | URL |
|----|-------|------|-----|
| V1 | 3Blue1Brown — But what is a neural network? | ORIENTATION | https://www.youtube.com/watch?v=aircAruvnKk |
| V2 | 3Blue1Brown — Gradient descent, how neural networks learn | CORE | https://www.youtube.com/watch?v=IHZwWFHWa-w |
| V3 | 3Blue1Brown — What is backpropagation really doing? | CORE | https://www.youtube.com/watch?v=Ilg3gGewQ5U |
| V4 | 3Blue1Brown — Backpropagation calculus | FOUNDATION | https://www.youtube.com/watch?v=tIeHLnjs5U8 |
| V5 | 3Blue1Brown Neural Networks playlist | META | https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi |

---

## 2. Key definitions

### Layer map

$$x\mapsto \sigma(Wx+b)$$ with nonlinearity $$\sigma$$.

### Empirical risk

$$\frac1n\sum_i \ell(f_\theta(x_i),y_i)$$ vs true risk $$\mathbb{E}\ell$$.


---

## 3. Formal status / theorem (seminar honesty)

**Status:** **Active research field.** Core engineering practice is mature; mathematical understanding of deep learning (generalization, optimization landscapes, feature learning) remains partial as of 2026.

**Statement / slogan:**

Universal approximation (classical) is a *representation* theorem, not a training theorem. Training is empirical risk minimization via SGD on nonconvex $$L(\theta)$$. Generalization of overparameterized nets is not settled by classical VC alone.

---

## 4. Proof or theory architecture (slogan only)

See course lesson body for the pedagogical reconstruction used in Math Enthusiast.  
Videos supply orientation, culture, and visual intuition; primary texts supply formal statements.

**Techniques / themes (labels):** listed in lesson LOs and common confusions.

---

## 5. Popular videos — claims hygiene

| Watch-out |
|-----------|
| Popular channels may compress hypotheses or overstate open problems as solved (or vice versa). |
| Prefer primary papers / Clay / NIST / standard textbooks when a claim is load-bearing. |

**Common confusions to preempt:**

- Universal approximation ⇒ training finds the approximator.
- Equating product demos with mathematical theorems.

---

## 6. Knowledge gaps (honest)

| Gap | Severity | How to close |
|-----|----------|--------------|
| Full timestamped transcripts of long lectures | Medium | Optional extract-video-knowledge on CORE URLs |
| Frame captures of slides | Low for text course | Optional `img/video_research/mathematics-of-ai/` |
| Frontier numerical constants / latest bounds | Medium | Update from current papers when assigning work |

---

## 7. People (math-relevant only)

Listed in course essay and primary references; see Wikipedia subject pages for historical lineage.

---

## 8. Cross-check log

| Claim type | Policy |
|------------|--------|
| Theorem vs open problem | Labeled in Status section |
| Popular wording vs formal statement | Prefer papers / Clay / NIST / textbooks |
| Fabricated transcripts | **None** in this pack |

---

## 9. All discovered URLs

See **[`references.md`](references.md)** for the complete bibliography.
