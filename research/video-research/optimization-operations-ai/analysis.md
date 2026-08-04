# Mode B — Video / research analysis: Optimization → Operations & AI

**Disclaimer:** Full machine transcripts were not loaded for every URL in this pack. Claims below are cross-checked against standard textbooks, course essays, and primary video metadata/slogans. Popular videos are for orientation unless marked CORE.

---

## 1. Metadata — primary focus source

| Field | Value |
|-------|--------|
| Title | Gradient descent, how neural networks learn — 3Blue1Brown |
| Speaker / channel | 3Blue1Brown |
| URL | https://www.youtube.com/watch?v=IHZwWFHWa-w |
| Duration | ~21 min |
| Level | 1–2 |
| Role | CORE (first-order methods intuition) |

---

## 2. Key definitions (course-aligned)

### Template

Minimize $$f(x)$$ over $$x\in\mathcal{C}$$; constraints define feasible set.

### Convexity

Local min = global min for convex $$f$$ on convex set (under mild conditions).

### GD step

$$x_{k+1}=x_k-\eta\nabla f(x_k)$$.

### Duality slogan

Dual variables are prices / certificates of optimality.

---

## 3. Extracted slogans / takeaways

- Convexity is the reliability contract; deep learning often leaves it.
- SGD noise is a feature for large data, not only a bug.
- LP is the OR workhorse; integer programs jump complexity.
- A critical point is not automatically a global minimum outside convexity.

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
| Frame captures for slides | Low for text course | Optional `img/video_research/optimization-operations-ai/` |
| Rapidly moving frontiers (e.g. monotile variants, PQC standards) | Medium | Re-check arXiv/NIST when assigning |

---

## 6. Curriculum map

- Chapter: **03**
- Lesson order: **7**
- Pack path: `research/video-research/optimization-operations-ai/`
- Enrich EN/VI lessons with Video sources + References pointing here.
