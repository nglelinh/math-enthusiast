# Translation Review — Full Course (EN → VI)

**Skill:** `en-vi-translation-reviewer`  
**Date:** 2026-08-04  
**Scope:** All **100** lesson pairs (`chapter` + `order`), chapters 01–09.  
**Pairing:** complete (0 EN without VI, 0 VI without EN).  
**Detailed chapter reports:**

| Report | Path |
|--------|------|
| Ch.01–03 | `work/translation_review_ch01_03.md` |
| Ch.04–06 | `work/translation_review_ch04_06.md` |
| Ch.07–09 | `work/translation_review_ch07_09.md` |
| Structural scan | `work/translation_structural.json` |

---

## Overall Assessment

**Good** — with pockets of **Needs Revision**.

Across ~100 pairs, open vs proved status is generally honest, prize years (Abel 2003–2025, Fields contrast, major Turing years) are mostly correct, and proper names / URLs / math are largely intact. The main systemic risks were:

1. Condensed Vietnamese on some flagships (word ratio 0.69–0.82) → missing pedagogy, not inverted math.  
2. Systematic term errors: *thắc triển*, *đối số* (for proof argument), bare *chiều cao*, *đo được zero*, *Biên giới* for Frontiers.  
3. One **Critical** institutional omission (Turing Award start year **1966**).

---

## Issues Found (course-wide rollup)

| Severity | Theme | Count (approx.) | Status after this pass |
|----------|--------|----------------:|------------------------|
| 🔴 Critical | Wrong “measure zero” / titles / Turing 1966 | ~4 | **Fixed** |
| 🟠 Major | Term bugs + selective omissions (RH, BSD, AI, Crypto, Abel mini-tour, Levin, etc.) | ~25–35 | **Terms fixed**; some content-gap Majors **documented, not fully rewritten** |
| 🟡 Minor | Condensation, calques, mild style | many | Accept / future polish |

### Critical / high-priority fixes applied this pass

| Fix | Where |
|-----|--------|
| `thắc triển` → **`thác triển`** | RH, BSD (and any remaining VI) |
| `vùng không-không-điểm` → **`vùng không zero`** | RH |
| `đo được zero` → **`có độ đo bằng không`** | Fractals / related |
| `đối số đường chéo` → **`lập luận đường chéo`** | Infinity, Euclid–Cantor, Cantor title |
| Title **Chiều cao** → **Chiều cao hơn** | Ch.04 Higher Dimensions + overview list |
| Title **Mật mã (Biên giới)** → **(Tiên phong)** | Future cryptography |
| Turing Award: state **1966** + “Turing did not win the Turing Award” row | What Is Turing Award |
| Diffie–Hellman 2015 wording (not co-laureate with GCHQ) | Public-key crypto |
| Name **Leonid Levin** as independent related work | Cook–Karp |

### Major gaps left for a second pass (content parity, not wrong math)

These need **restored paragraphs/tables** from EN, not one-line term fixes:

- **Mathematics of AI** (VI ratio ~0.74) — LO/hype/confusion table rows  
- **Collatz / Kakeya** problem pages (ratio ~0.70) — optional depth parity  
- **Crypto (ch03)** — padding / Grover hygiene rows if EN has them  
- **Paradoxes** — EN end-section blocks  
- **What Is Abel Prize** — EN mini-tour 2016–2025 vs VI-only tail  
- **Euclid–Cantor** — micro-examples / cartoon detail  
- **Explore Kakeya** — missing `kakeya_needle_directions.svg` figure  
- Flagship **Mode-C** depth where EN grew after VI freeze  

---

## Final Verdict

| Axis | Score |
|------|------:|
| Accuracy (math status / years) | **8.5/10** |
| Completeness (flagship parity) | **7/10** |
| Terminology (after fixes) | **8.5/10** |
| Naturalness | **8/10** |
| Tone (academic seminar) | **9/10** |

**Verdict:** **Ready for teaching use after this Critical/term pass**, with the understanding that several flagships remain **shorter** than EN and should be expanded in a dedicated parity sprint (AI, Collatz, Kakeya, Paradoxes, Abel intro).

**Do not treat VI as sentence-level twins of EN on every page**—many are intentional condensations that still preserve load-bearing claims.

---

## How this review was run

1. Inventory 100 pairs (`work/translation_pairs.json`).  
2. Structural scan (ratios, headings, math delimiters, arXiv/YouTube).  
3. Parallel chapter reviews via `en-vi-translation-reviewer` criteria (ch01–03, 04–06, 07–09).  
4. Applied systematic term + Critical institutional fixes.  
5. Left large missing-section rewrites for a follow-up (list above).

---

## Parity sprint — flagships AI / Collatz / Kakeya (done)

| Lesson | Before ratio | After ratio | Restored |
|--------|-------------:|------------:|----------|
| Collatz 01.07 | ~0.70 | **~0.90** | Orbits & stopping times; full heuristics + caveats; Syracuse research motivation |
| Kakeya 01.08 | ~0.69 | **~0.81** | δ-tube volume/structure/sticky; HA care; misconceptions + exercises |
| Math of AI 06.02 | ~0.74 | **~0.96** | Expanded data/model/opt; OT/high-d rows; hype/confusion; VI Mode-C slogans |

## Recommended next

1. Restore Abel mini-tour in VI or mark VI-only sections as course-local enrichment.  
2. Optional: re-run skill on these three flagships.  
3. Commit report + fixes when you want them on `main`.
