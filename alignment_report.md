# Alignment Gate Report — Math Enthusiast

**Mode:** `align-check` + redesign diagnostic (`course-designer` skill)  
**Date:** 2026-08-03  
**Auditor:** alignment_auditor_agent (manual; no Course Passport on disk)  
**Assurance:** Structural audit over site content + home outline; passport-backed checks are **NOT_EVALUABLE** where data is missing.  
**Scope:** Bilingual Jekyll collection `contents/{en,vi}/chapter01–07` + `home/_posts`

---

## Verdict (updated 2026-08-03): **PASS-WITH-WARNINGS** (design stage)

Professor confirmed: **undergraduate seminar**, **taught with deliverables**, **flagship-per-section first**. Design of record is now in `course_passport.yaml` (LO1–LO6, A1–A6, 15-week schedule). Content build for remaining flagships is still **todo**; institutional fields still need input.

**Earlier verdict (pre-passport):** FAIL as content map only — retained below for history.

### Historical note — first audit

This is **not** a judgment that the *mathematical ideas* are wrong. At first audit the collection was a **content map**, not a **backward-designed course** (Pedagogy Foundations §1–2). The passport now closes the triangle at design level.

| Layer | Status |
|-------|--------|
| Topic vision & section map | Strong |
| Measurable course outcomes | Weak / non-measurable |
| Assessment structure | Absent |
| Lesson depth & consistency | Highly uneven |
| Bilingual file coverage | Present (filename convention differs only for overviews) |
| Course Passport | Missing |

---

## Redesign diagnostic (6 questions)

### 1. What did students actually struggle with?

**No evidence.** There is no evaluation data, midcourse survey, or teaching-reflector output. Treat struggle hypotheses as provisional:

- **Depth cliff:** Wang/Kakeya (~2.5k words, LO + exercises + figures) vs most essays (~120–260 words) may confuse “what success looks like.”
- **Prerequisite fog:** Survey of modern math with no stated entry floor or “skip if…” paths.
- **Open-ended Section 7** without feedback loops may feel optional/decorative.

### 2. Are the outcomes still right for who takes the course?

Home “Course Objectives” are **aims**, not measurable outcomes:

| Current wording | Diagnosis (outcome_verbs) |
|-----------------|---------------------------|
| “Give learners a clear map…” | Instructor action, not learner performance |
| “Show how mathematicians think…” | Unobservable (“show”) |
| “Connect abstract ideas to the real world…” | Vague; no conditions or product |
| “Encourage exploration…” | Affective aim, not assessable capability |

**Learner profile is unspecified** (Passport Iron Rule 2): HS enrichment? undergrad seminar? self-learners on GitHub Pages? Outcomes cannot be fixed without that.

### 3. Where does alignment break?

| Triangle edge | Observation |
|---------------|-------------|
| Outcomes → teaching | Topics exist; outcomes do not drive them |
| Outcomes → assessment | No graded or even informal assessment plan |
| Teaching → assessment | Most lessons end in generic “Further directions,” not retrieval/practice |
| Taught but not assessed | Nearly all content |
| Assessed but not taught | N/A (nothing assessed) |

**Positive exception:** `02_15_Wang_Harmonic_Analysis` has learning objectives, exercises, references, and figures—closest to a full lesson prototype.

### 4. What does the AI era change?

- Unproctored “write an essay on Riemann” is trivial with AI; **process evidence** fits better: conjecture logs, figure annotations, compare-two-expositions, blind restatement of a proof *idea*.
- Explorations (ch.07) should demand **artifacts** (notebook, drawing, failed attempt + revision), not only answers.
- AI-use policy is **missing** on the public site (syllabus checklist).

### 5. Highest impact-to-effort change

1. **Write 4–6 measurable course LOs** + tag every chapter as `taught_in` for ≥1 LO.  
2. **Define a lightweight evidence structure** (even if ungraded): e.g. 3 exploration portfolios + 1 synthesis essay + optional peer discussion.  
3. **Adopt the Wang lesson as the depth template** for one “flagship” essay per section before expanding the rest.

### 6. What must NOT change?

- The **seven-section map** (problems → Fields → applications → beauty → proofs → future → explorations).  
- **Curiosity-first, non-sequential** navigation.  
- **Bilingual** commitment (en/vi).  
- Emphasis on **ideas of proofs/problems**, not technical drills.  
- Quality bar of the **Wang/Kakeya** essay as the north star for flagship lessons.

---

## Gate 1.5 checklist

### A. Constructive alignment triangle

| ID | Severity | Detail | Suggested direction |
|----|----------|--------|---------------------|
| A1 | **BLOCK** | No Course Passport; no LO ids with `assessed_by`. Home objectives are not LOs. | Draft LO1–LO6; each must name evidence (even ungraded). |
| A2 | **BLOCK** | No LO with `taught_in` mapping to chapters/posts. | Map each LO to specific `chapterXX` posts. |
| A3 | **BLOCK** | No assessments; nothing with `outcomes_assessed`. | Add assessment plan (weights may be 0% if non-credit). |
| A4 | **NOT_EVALUABLE** | No week-by-week schedule (collection is topic-based). | Either declare modality = self-paced map (schedule = modules), or add optional reading paths. |
| A5 | **NOT_EVALUABLE** | No teach/assess weeks. | Same as A4. |

### B. Outcome quality

| ID | Severity | Detail | Suggested direction |
|----|----------|--------|---------------------|
| B1 | **WARN** | Home verbs: give/show/connect/encourage — banned or non-measurable pattern. | Rewrite with explain / compare / formulate / critique / design. |
| B2 | **BLOCK** | No `bloom_level` on any course LO. | Tag each LO (Anderson & Krathwohl). |
| B3 | **WARN** | Implicit aim is mostly *understand*; little *create/evaluate* at course level—though ch.07 could host create. | Raise 1–2 outcomes to evaluate/create via explorations. |
| B4 | **WARN** | Effective “topic outcomes” ≫ 12 if every post is treated as an outcome; course-level count undefined. | Keep **3–8 course LOs**; treat posts as teaching episodes. |

### C. Assessment structure

| ID | Severity | Detail | Suggested direction |
|----|----------|--------|---------------------|
| C1 | **BLOCK** | No weights; cannot sum to 100%. | For non-credit: explicit “ungraded / self-check” plan still records 100% of *attention* design, or mark as enrichment with optional badges. |
| C2 | **NOT_EVALUABLE** | No high-stakes items. | When adding credit version, cap any single item ≤40%. |
| C3 | **WARN** | No low-stakes retrieval before any synthesis task. | Per-lesson “one-paragraph restatement” or 2–3 exercises (Wang model). |
| C4 | **WARN** | Explorations imply *create*; no assessment vehicle matches. | Portfolio rubric for ch.07. |

### D. Workload

| ID | Severity | Detail | Suggested direction |
|----|----------|--------|---------------------|
| D1 | **BLOCK** | No `workload_audit.estimated_hours_per_week`. | Estimate paths: “sampler 2h/wk”, “section deep-dive 5h/wk”, “full map 8–10h/wk”. |
| D2 | **NOT_EVALUABLE** | No credit hours / institution norms. | Declare self-paced open course; skip credit convention or invent paths. |
| D3 | **NOT_EVALUABLE** | No deadlines. | Keep open pacing; if cohort runs, avoid dual major deliverables same week. |

---

## Content-depth audit (EN corpus)

| Chapter | Posts | Approx. total words | Avg words/post | Pedagogical completeness |
|---------|------:|--------------------:|---------------:|--------------------------|
| 01 Great Problems | 9 | ~2.3k | ~260 | Mostly short encyclopedia-style |
| 02 Fields Medal | 15 | ~11k | ~730 | Skewed by Wang flagship + longer overviews |
| 03 World-changing | 9 | ~1.4k | ~160 | Thin |
| 04 Beautiful | 12 | ~1.5k | ~130 | Thin |
| 05 Famous proofs | 9 | ~1.4k | ~160 | Thin (idea-of-proof needs more) |
| 06 Future | 11 | ~1.3k | ~120 | Thin |
| 07 Explorations | 9 | ~1.3k | ~145 | Prompts present; weak scaffolding |

**Prototype quality:** Wang lesson demonstrates LO + figures + multi-section narrative + exercises + references. That pattern appears in a **minority** of posts (roughly LO ~15 EN files, Exercises ~14 EN files out of ~74 EN content posts).

**Cross-links:** Kakeya (ch.01) → Wang (ch.02) is good practice; most other cross-section bridges are missing.

---

## Bilingual (en/vi)

| Check | Result |
|-------|--------|
| Chapter 01–07 both languages | Yes |
| Topic files mirrored | Yes (overview slug `Overview` vs `Tong_quan` only intentional difference) |
| Depth parity | Not audited line-by-line; risk that future EN-only expansions leave VI behind |
| Language-switch alignment via `chapter` + `order` | Depends on front matter consistency (spot-check: Wang order 14 both langs) |

**Suggested direction:** When expanding a flagship lesson, ship **EN+VI in the same PR**.

---

## Strengths (protect these)

1. **Coherent public vision** — “map of modern mathematics,” not a fake undergrad analysis sequence.  
2. **Section architecture** matches the intellectual story (problems → breakthroughs → applications → beauty → proofs → frontiers → open work).  
3. **One gold-standard lesson** (Wang / Kakeya 3D) proves the format can work on this stack (MathJax, SVGs, bilingual).  
4. **Explorations section** is the right place for *create*-level work if scaffolded.  
5. **Honest open-problem framing** (esp. Kakeya n≥4 still open) models research culture.

---

## Prioritized change plan

### P0 — Design of record (1–2 sessions)

1. Create `course_passport.yaml` (use teaching-skills starter template).  
2. Write **5±1 course LOs**, Bloom-tagged, measurable. Example candidates:

   | ID | Draft outcome | Bloom |
   |----|---------------|-------|
   | LO1 | **Explain** a major open problem (statement, why hard, one mathematical tool grown around it) without solving it | understand |
   | LO2 | **Compare** measure-zero vs full dimension (or analogous size notions) using Kakeya or a fractal example | analyze |
   | LO3 | **Trace** the idea of a famous proof (Euclid / Cantor / etc.) in a short narrative with correct logical skeleton | understand/analyze |
   | LO4 | **Relate** a classical field (linear algebra, probability, …) to a named modern application | apply |
   | LO5 | **Formulate** a conjecture or exploration plan from a Section 7 prompt and document experiments | create |
   | LO6 | **Critique** a popular exposition of a breakthrough for precision vs hype | evaluate |

3. Assessment plan (non-credit OK):

   | Evidence | Weight* | Outcomes |
   |----------|--------:|----------|
   | Per-lesson self-check (restatement / 2 exercises) | 20% | LO1–4 |
   | Two “flagship” deep reads with exercise sets | 30% | LO1–3 |
   | Exploration portfolio (ch.07) | 30% | LO5 |
   | Synthesis essay / map of own interests | 20% | LO1, LO4, LO6 |

   \*Weights = relative emphasis if ungraded; still design the triangle.

### P1 — Content depth (iterative)

| Priority | Action |
|----------|--------|
| 1 | One **flagship lesson per section** at Wang depth (1500–3000 words, LO, 3–5 exercises, 3+ figures or worked sketches, references). |
| 2 | Keep other posts as **short map entries** but label them clearly (“overview card” vs “deep essay”) so learners know depth. |
| 3 | Add **cross-links** between related nodes (e.g. ch.05 Poincaré ↔ ch.02 Perelman; ch.03 crypto ↔ ch.01 P vs NP). |
| 4 | Section 7: add success criteria, starter experiments, and “what good looks like.” |

Suggested first flagship queue after Wang:

1. Ch.01 — Riemann Hypothesis or P vs NP  
2. Ch.05 — Euclid infinite primes + Cantor diagonal (paired short deeps)  
3. Ch.03 — Number theory → cryptography  
4. Ch.07 — one fully scaffolded exploration (Kakeya or Collatz)

### P2 — Modality & syllabus

- Declare modality: **self-paced open educational resource** (or hybrid seminar if you teach it).  
- Short syllabus page: audience, paths, AI policy, how to use bilingual switch, how to contribute.  
- Optional: async modules from `async_designer` if cohort-based.

---

## Suggested reading paths (schedule substitute)

Until a calendar exists, offer **paths** instead of weeks:

| Path | Duration (est.) | Sections | Primary LOs |
|------|-----------------|----------|-------------|
| A — Sampler | 2–3 weeks @ 3h | Intro + one problem + one Fields essay + one exploration prompt | LO1, LO5 |
| B — Problems & proofs | 6–8 weeks | Ch.01 + Ch.05 + Wang | LO1–3 |
| C — Math that touches the world | 4–6 weeks | Ch.03 + Ch.06 | LO4, LO6 |
| D — Full map | semester-scale | All chapters, 1 flagship deep/week | all |

Workload D1 (rough): Path A ≈ **3 h/week**; Path B ≈ **5–7 h/week** with deep reads; Path D ≈ **8–10 h/week** if all shorts + weekly deep.

---

## NOT_EVALUABLE summary

- Institution constraints, credit hours, grading scale, integrity sanctions  
- Prior student evaluation data  
- Official Course Passport fields (`assessed_by`, `taught_in`, weights, week map)  
- Full VI depth parity and scientific accuracy audit of every short essay  

---

## Honesty note (auditor scope)

This report checks **alignment structure and pedagogical completeness**, not whether every mathematical claim in every short post is research-accurate. Content merit reviews should be separate (e.g. domain expert pass on ch.02 Fields summaries).

---

## Checkpoint for professor

Please confirm or amend:

1. **Audience** (who is this for?)  
2. **Modality** (pure OER map vs taught seminar with deliverables?)  
3. **Accept draft LO1–LO6** (or rewrite)?  
4. **Depth strategy:** flagship-per-section vs thin full coverage first?  
5. **Create `course_passport.yaml` now?** (recommended next artifact)

---

## Artifacts

| Artifact | Status |
|----------|--------|
| `alignment_report.md` | **This file** |
| `course_passport.yaml` | Not created (await checkpoint) |
| `syllabus.md` | Not created (would invent policy without institution data) |
| `design_rationale.md` | Optional follow-up after LO confirmation |

---

*Generated under teaching-skills `course-designer` align-check + redesign diagnostic. Pedagogy Foundations §1 (backward design), §2 (constructive alignment), §3 (Bloom), §5 (retrieval/spacing).*
