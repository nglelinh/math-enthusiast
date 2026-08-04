# Mode B — Video / research analysis: Machine Learning Theory

**Disclaimer:** No full machine transcripts are claimed in this pack unless separately extracted.  
Claims are cross-checked against standard references (Wikipedia, arXiv, textbooks, institute pages).  
Popular-video details are role/metadata level unless noted.

---

## 1. Metadata — recommended videos

| ID | Title | Role | URL |
|----|-------|------|-----|
| V1 | 3Blue1Brown neural network series (optimization/learning intuition) | ORIENTATION | https://www.youtube.com/watch?v=aircAruvnKk |
| V2 | 3Blue1Brown gradient descent | CORE | https://www.youtube.com/watch?v=IHZwWFHWa-w |
| V3 | Sipser / complexity contrast videos (hardness vs learnability culture) | SECONDARY | https://www.youtube.com/watch?v=msp2y_Y5MLE |

---

## 2. Key definitions

### PAC

Learn hypothesis with error $$\le\varepsilon$$ with probability $$\ge 1-\delta$$ from poly samples.

### VC dimension

Size of largest shattered set; measures binary classifier class complexity.


---

## 3. Formal status / theorem (seminar honesty)

**Status:** **Active.** Classical PAC/VC is theorem-complete for uniform convergence regimes; modern deep learning theory (interpolation, implicit bias, double descent) is incomplete.

**Statement / slogan:**

PAC learnability linked to finite VC dimension for binary classification (fundamental theorem of statistical learning, rough statement). Uniform convergence controls generalization for restricted classes; interpolating deep nets need other stories.

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

- Applying classical U-shaped bias-variance as universal law after the interpolation peak.
- Reading empirical scaling laws as theorems.

---

## 6. Knowledge gaps (honest)

| Gap | Severity | How to close |
|-----|----------|--------------|
| Full timestamped transcripts of long lectures | Medium | Optional extract-video-knowledge on CORE URLs |
| Frame captures of slides | Low for text course | Optional `img/video_research/ml-theory/` |
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
