# Mode B — Video / research analysis: Number Theory → Cryptography

**Disclaimer:** Full machine transcripts were not loaded for every URL in this pack. Claims below are cross-checked against standard textbooks, course essays, and primary video metadata/slogans. Popular videos are for orientation unless marked CORE.

---

## 1. Metadata — primary focus source

| Field | Value |
|-------|--------|
| Title | Encryption and HUGE numbers (RSA) — Numberphile |
| Speaker / channel | Numberphile (James Grime et al.) |
| URL | https://www.youtube.com/watch?v=M7kEpw1tn50 |
| Duration | ~9 min |
| Level | 1 |
| Role | ORIENTATION (RSA culture) |

---

## 2. Key definitions (course-aligned)

### Congruence

$$a\equiv b\pmod n$$ iff $$n\mid(a-b)$$.

### RSA slogan

$$c\equiv m^e\pmod n$$; decrypt with $$d$$ where $$ed\equiv 1\pmod{\varphi(n)}$$.

### DLP

Given $$g,g^a$$ in a group, recover $$a$$ (hard in good groups).

### Kerckhoffs

Security rests on key secrecy, not algorithm secrecy.

---

## 3. Extracted slogans / takeaways

- Textbook RSA without padding is not deployable security.
- Factoring hardness is an *assumption*, not a theorem.
- ECC is still discrete-log style hardness in a different group.
- Post-quantum: lattice/code/hash-based schemes replace factoring/DL assumptions under NIST migration.

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
| Frame captures for slides | Low for text course | Optional `img/video_research/number-theory-cryptography/` |
| Rapidly moving frontiers (e.g. monotile variants, PQC standards) | Medium | Re-check arXiv/NIST when assigning |

---

## 6. Curriculum map

- Chapter: **03**
- Lesson order: **5**
- Pack path: `research/video-research/number-theory-cryptography/`
- Enrich EN/VI lessons with Video sources + References pointing here.
