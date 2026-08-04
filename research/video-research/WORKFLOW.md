# Video → Lesson enrichment workflow

Canonical pipeline for Math Enthusiast (see skill `math-video-researcher` §53).

```text
TOPIC
  → find existing lesson(s)
  → research URLs (videos + papers + web)
  → research/video-research/<slug>/
       README.md | references.md (ALL urls) | analysis.md | learning_path.md
  → extract knowledge (definitions, theorems, status, confusions)
  → (optional) caption extract → transcripts/ + TRANSCRIPT_STATUS.md + sample frames
  → enrich contents/{en,vi}/... lessons + References + transcript links
  → curriculum.md note
  → jekyll build
```

**Example:** `collatz/` (full pipeline) · flagships: `FLAGSHIP_TRANSCRIPTS.md` · others: `NONFLAGSHIP_TRANSCRIPTS.md`

**Batch extract (non-flagship):**

```bash
python3 scripts/batch_extract_nonflagship.py --captions-only
python3 scripts/batch_extract_nonflagship.py --materialize-only --link-lessons
python3 scripts/batch_extract_nonflagship.py --frames-only --max-frames-packs 40
```

**Rules:** every discovered URL in References; extract into body; EN+VI when both exist; no fabricated proofs or transcripts. Captions are navigation aids, not proof substitutes.
