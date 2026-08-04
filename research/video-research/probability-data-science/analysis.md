# Mode B — Video / research analysis: Probability → Data Science

**Disclaimer:** Full machine transcripts were not loaded for every URL in this pack. Claims below are cross-checked against standard textbooks, course essays, and primary video metadata/slogans. Popular videos are for orientation unless marked CORE.

---

## 1. Metadata — primary focus source

| Field | Value |
|-------|--------|
| Title | Bayes theorem, the geometry of Bayesian update (3Blue1Brown) |
| Speaker / channel | 3Blue1Brown |
| URL | https://www.youtube.com/watch?v=HZGCoVF3YvM |
| Duration | ~15 min |
| Level | 1–2 |
| Role | CORE intuition (Bayes + geometric probability) |

---

## 2. Key definitions (course-aligned)

### Expectation

Linear operator $$\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y$$ (when defined).

### LLN

Sample averages converge to expectation under i.i.d. hypotheses.

### CLT

Normalized sums approach a Gaussian; explains many bell-shaped histograms.

### Bayes

$$P(H\mid D)=P(D\mid H)P(H)/P(D)$$ — update beliefs with evidence.

### Risk

ML risk is expected loss $$\mathbb{E}[\ell(f(X),Y)]$$; empirical risk approximates it.

---

## 3. Extracted slogans / takeaways

- Independence is a modeling assumption, not automatic from “different people.”
- Base-rate neglect is the main Bayes hygiene failure (Veritasium Bayesian trap).
- LLN ≠ CLT: one is about averages settling; the other about fluctuation shapes.
- Correlation is not causation — still true after fancy ML.

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
| Frame captures for slides | Low for text course | Optional `img/video_research/probability-data-science/` |
| Rapidly moving frontiers (e.g. monotile variants, PQC standards) | Medium | Re-check arXiv/NIST when assigning |

---

## 6. Curriculum map

- Chapter: **03**
- Lesson order: **4**
- Pack path: `research/video-research/probability-data-science/`
- Enrich EN/VI lessons with Video sources + References pointing here.
