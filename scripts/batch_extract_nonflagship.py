#!/usr/bin/env python3
"""Batch caption extract for non-flagship video-research packs.

Pipeline:
  1. Load unique YouTube IDs from non-flagship pack references.md
  2. yt-dlp: metadata + en/vi auto/manual subs (skip full video by default)
  3. Parse VTT/SRT → cues, plain transcript, ~90s knowledge units
  4. Materialize per-pack transcripts/, TRANSCRIPT_STATUS.md, transcript_inventory.json
  5. Optional: sample frames for each pack's first captioned video
  6. Write research/video-research/NONFLAGSHIP_TRANSCRIPTS.md

Usage:
  python3 scripts/batch_extract_nonflagship.py              # full run
  python3 scripts/batch_extract_nonflagship.py --captions-only
  python3 scripts/batch_extract_nonflagship.py --materialize-only
  python3 scripts/batch_extract_nonflagship.py --frames-only --max-frames-packs 20
  python3 scripts/batch_extract_nonflagship.py --link-lessons
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = ROOT / "research" / "video-research"
WORK = ROOT / "work" / "batch_videos"
IMG = ROOT / "img" / "video_research" / "nonflagships"
JOB = ROOT / "work" / "batch_nonflagship_job.json"
STATE = ROOT / "work" / "batch_nonflagship_state.json"
MASTER = PACK_ROOT / "NONFLAGSHIP_TRANSCRIPTS.md"

FLAGSHIPS = {
    "Riemann_Hypothesis",
    "Kakeya_Conjecture",
    "Wang_Harmonic_Analysis",
    "number-theory-cryptography",
    "infinity",
    "euclid-infinite-primes",
    "cantor-diagonal",
    "mathematics-of-ai",
    "collatz",
}

ID_RE = re.compile(r"(?:youtube\.com/watch\?v=|youtu\.be/)([A-Za-z0-9_-]{6,})")
SUB_LANGS = "en.*,en,vi.*,vi"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"videos": {}, "updated": None}


def save_state(state: dict) -> None:
    state["updated"] = utc_now()
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def discover_job() -> dict:
    packs: dict[str, list[str]] = {}
    id_to_packs: dict[str, set[str]] = {}
    for d in sorted(PACK_ROOT.iterdir()):
        if not d.is_dir() or d.name in FLAGSHIPS:
            continue
        refs = d / "references.md"
        if not refs.exists():
            packs[d.name] = []
            continue
        ids: list[str] = []
        for m in ID_RE.finditer(refs.read_text(encoding="utf-8", errors="replace")):
            vid = m.group(1)
            if vid not in ids:
                ids.append(vid)
            id_to_packs.setdefault(vid, set()).add(d.name)
        packs[d.name] = ids
    job = {
        "packs": packs,
        "unique_ids": sorted(id_to_packs.keys()),
        "id_to_packs": {k: sorted(v) for k, v in id_to_packs.items()},
    }
    JOB.parent.mkdir(parents=True, exist_ok=True)
    JOB.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    return job


def parse_ts(ts: str) -> float:
    ts = ts.replace(",", ".")
    parts = [float(p) for p in ts.split(":")]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return float(parts[0])


def parse_vtt_or_srt(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw: list[dict] = []
    # normalize SRT-style to blocks
    blocks = re.split(r"\n\s*\n", text.strip())
    for b in blocks:
        lines = [
            ln
            for ln in b.splitlines()
            if ln.strip()
            and not ln.strip().startswith(("WEBVTT", "NOTE", "Kind:", "Language:", "STYLE"))
            and not re.fullmatch(r"\d+", ln.strip())
        ]
        tline = next((ln for ln in lines if "-->" in ln), None)
        if not tline:
            continue
        m = re.match(r"([\d:.]+)\s*-->\s*([\d:.]+)", tline.strip())
        if not m:
            continue
        t0, t1 = parse_ts(m.group(1)), parse_ts(m.group(2))
        after = False
        body: list[str] = []
        for ln in lines:
            if "-->" in ln:
                after = True
                continue
            if after:
                ln = re.sub(r"<[^>]+>", "", ln).replace("&nbsp;", " ").strip()
                if ln:
                    body.append(ln)
        if body:
            raw.append({"t_start": round(t0, 3), "t_end": round(t1, 3), "text": " ".join(body)})

    # collapse progressive auto-captions
    cues: list[dict] = []
    i = 0
    while i < len(raw):
        cur = dict(raw[i])
        j = i + 1
        while j < len(raw):
            nxt = raw[j]
            if nxt["text"].startswith(cur["text"]) or cur["text"] in nxt["text"]:
                longer = nxt["text"] if len(nxt["text"]) >= len(cur["text"]) else cur["text"]
                cur = {"t_start": cur["t_start"], "t_end": nxt["t_end"], "text": longer}
                j += 1
                continue
            pw, nw = set(cur["text"].split()), set(nxt["text"].split())
            if (
                pw
                and nw
                and len(pw & nw) / max(len(pw), 1) > 0.55
                and nxt["t_start"] - cur["t_start"] < 5
            ):
                longer = nxt["text"] if len(nxt["text"]) >= len(cur["text"]) else cur["text"]
                cur = {"t_start": cur["t_start"], "t_end": nxt["t_end"], "text": longer}
                j += 1
                continue
            break
        if cues and cues[-1]["text"] == cur["text"]:
            cues[-1]["t_end"] = cur["t_end"]
        else:
            cues.append(cur)
        i = j if j > i else i + 1
    return cues


def chunk_units(vid: str, cues: list[dict], window: float = 90.0) -> list[dict]:
    if not cues:
        return []
    units: list[dict] = []
    chunk_start = cues[0]["t_start"]
    chunk_end = chunk_start
    buf: list[str] = []
    for c in cues:
        if c["t_start"] - chunk_start >= window and buf:
            summary = " ".join(buf)
            if len(summary) > 600:
                summary = summary[:597] + "…"
            units.append(
                {
                    "id": f"ku_video_{vid}_{int(chunk_start)}",
                    "t_start": round(chunk_start, 1),
                    "t_end": round(chunk_end, 1),
                    "type": "overview",
                    "summary": summary,
                }
            )
            chunk_start = c["t_start"]
            buf = [c["text"]]
            chunk_end = c["t_end"]
        else:
            buf.append(c["text"])
            chunk_end = c["t_end"]
    if buf:
        summary = " ".join(buf)
        if len(summary) > 600:
            summary = summary[:597] + "…"
        units.append(
            {
                "id": f"ku_video_{vid}_{int(chunk_start)}",
                "t_start": round(chunk_start, 1),
                "t_end": round(chunk_end, 1),
                "type": "overview",
                "summary": summary,
            }
        )
    return units


def find_caption_file(wd: Path, vid: str) -> Path | None:
    # Prefer English manual/auto, then Vietnamese, then any
    patterns = [
        f"{vid}.en.vtt",
        f"{vid}.en-*.vtt",
        f"{vid}.en.srt",
        f"{vid}.en-*.srt",
        f"{vid}.vi.vtt",
        f"{vid}.vi-*.vtt",
        f"{vid}.*.vtt",
        f"{vid}.*.srt",
    ]
    for pat in patterns:
        hits = sorted(wd.glob(pat))
        # skip live_chat etc
        hits = [h for h in hits if "live_chat" not in h.name]
        if hits:
            # prefer shorter lang code files (en over en-US over en-orig sometimes)
            hits.sort(key=lambda p: (len(p.name), p.name))
            return hits[0]
    return None


def process_local_captions(vid: str, wd: Path, title: str = "") -> dict:
    cap = find_caption_file(wd, vid)
    if not cap:
        return {
            "id": vid,
            "status": "no_captions",
            "title": title,
            "chars": 0,
            "units": 0,
            "caption_file": None,
        }
    cues = parse_vtt_or_srt(cap)
    transcript = "\n".join(c["text"] for c in cues)
    units = chunk_units(vid, cues)
    (wd / "cues.json").write_text(json.dumps(cues, ensure_ascii=False, indent=2), encoding="utf-8")
    (wd / "transcript.txt").write_text(transcript, encoding="utf-8")
    (wd / "knowledge_units.json").write_text(
        json.dumps(units, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return {
        "id": vid,
        "status": "ok",
        "title": title,
        "chars": len(transcript),
        "units": len(units),
        "caption_file": cap.name,
        "cues": len(cues),
    }


def yt_dlp_fetch(vid: str, sleep_s: float = 4.0, retries: int = 3) -> dict:
    wd = WORK / f"video_{vid}"
    wd.mkdir(parents=True, exist_ok=True)
    url = f"https://www.youtube.com/watch?v={vid}"
    out_tmpl = str(wd / "%(id)s")
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-info-json",
        "--write-auto-sub",
        "--write-sub",
        "--sub-langs",
        SUB_LANGS,
        "--no-playlist",
        "-o",
        out_tmpl,
        url,
    ]
    last_err = ""
    for attempt in range(1, retries + 1):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            out = (r.stdout or "") + "\n" + (r.stderr or "")
            if r.returncode == 0 or "Writing video subtitles" in out or find_caption_file(wd, vid):
                title = ""
                info = wd / f"{vid}.info.json"
                if info.exists():
                    try:
                        meta = json.loads(info.read_text(encoding="utf-8"))
                        title = meta.get("title") or ""
                    except Exception:
                        pass
                result = process_local_captions(vid, wd, title=title)
                if result["status"] == "ok":
                    result["fetch"] = "ok"
                else:
                    # may have info but no subs
                    result["fetch"] = "no_subs"
                    result["log_tail"] = out[-500:]
                time.sleep(sleep_s)
                return result
            if "429" in out or "Too Many Requests" in out:
                last_err = "429"
                time.sleep(sleep_s * attempt * 3)
                continue
            last_err = out[-800:]
            time.sleep(sleep_s)
        except subprocess.TimeoutExpired:
            last_err = "timeout"
            time.sleep(sleep_s * attempt)
        except Exception as e:
            last_err = str(e)
            time.sleep(sleep_s)
    return {
        "id": vid,
        "status": "error",
        "title": "",
        "chars": 0,
        "units": 0,
        "error": last_err[:500],
    }


def materialize_pack(pack: str, video_ids: list[str], state: dict) -> dict:
    pdir = PACK_ROOT / pack
    tdir = pdir / "transcripts"
    tdir.mkdir(parents=True, exist_ok=True)
    videos_out = []
    ok = 0
    units_tot = 0
    rows = []
    for vid in video_ids:
        st = state.get("videos", {}).get(vid, {})
        wd = WORK / f"video_{vid}"
        title = st.get("title") or ""
        has = st.get("status") == "ok" and (wd / "transcript.txt").exists()
        chars = st.get("chars", 0)
        nunits = st.get("units", 0)
        if has:
            for src_name, dst_name in (
                ("transcript.txt", f"{vid}_transcript.txt"),
                ("cues.json", f"{vid}_cues.json"),
                ("knowledge_units.json", f"{vid}_knowledge_units.json"),
            ):
                src = wd / src_name
                if src.exists():
                    shutil.copy(src, tdir / dst_name)
            ok += 1
            units_tot += int(nunits)
            rows.append(f"| `{vid}` | {chars}c | {nunits} | {title} |")
        else:
            status = st.get("status") or "pending"
            err = st.get("error") or st.get("fetch") or status
            rows.append(f"| `{vid}` | none ({err}) | 0 | {title} |")
        videos_out.append(
            {
                "id": vid,
                "title": title,
                "has_transcript": bool(has),
                "chars": int(chars) if has else 0,
                "units": int(nunits) if has else 0,
                "url": f"https://www.youtube.com/watch?v={vid}",
            }
        )

    inv = {"slug": pack, "videos": videos_out}
    (pdir / "transcript_inventory.json").write_text(
        json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    status_md = [
        f"# {pack} — transcript extract status",
        "",
        f"Generated: {utc_now()}",
        "",
        "| ID | Transcript | Units | Title |",
        "|----|------------|------:|-------|",
        *rows,
        "",
        "## Notes",
        "",
        "- Captions via yt-dlp; not human-verified.",
        "- Units are ~90s caption chunks for navigation.",
        "- Batch: non-flagship extract (`scripts/batch_extract_nonflagship.py`).",
        "",
    ]
    (pdir / "TRANSCRIPT_STATUS.md").write_text("\n".join(status_md), encoding="utf-8")
    return {"pack": pack, "ok": ok, "total": len(video_ids), "units": units_tot}


def extract_primary_frames(pack: str, video_ids: list[str], state: dict, n_frames: int = 1) -> list[str]:
    """Prefer YouTube thumbnail (fast); fall back to mid-video still if media already local."""
    IMG.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    primary = None
    for vid in video_ids:
        st = state.get("videos", {}).get(vid, {})
        if st.get("status") == "ok":
            primary = vid
            break
    if not primary:
        # still try first id for thumbnail
        primary = video_ids[0] if video_ids else None
    if not primary:
        return written

    wd = WORK / f"video_{primary}"
    wd.mkdir(parents=True, exist_ok=True)
    safe_pack = re.sub(r"[^A-Za-z0-9_-]+", "_", pack)[:40]
    out = IMG / f"{safe_pack}_{primary}_thumb.jpg"

    # reuse existing thumbnail
    for cand in list(wd.glob(f"{primary}*.jpg")) + list(wd.glob(f"{primary}*.webp")) + list(wd.glob(f"{primary}*.png")):
        try:
            # convert webp/png to jpg via ffmpeg if needed
            if cand.suffix.lower() == ".jpg":
                shutil.copy(cand, out)
            else:
                subprocess.run(
                    ["ffmpeg", "-y", "-i", str(cand), "-q:v", "4", str(out)],
                    capture_output=True,
                    timeout=30,
                )
            if out.exists():
                written.append(str(out.relative_to(ROOT)))
                return written
        except Exception:
            pass

    # download thumbnail only
    url = f"https://www.youtube.com/watch?v={primary}"
    try:
        subprocess.run(
            [
                "yt-dlp",
                "--skip-download",
                "--write-thumbnail",
                "--convert-thumbnails",
                "jpg",
                "--no-playlist",
                "-o",
                str(wd / f"{primary}"),
                url,
            ],
            capture_output=True,
            text=True,
            timeout=90,
        )
        time.sleep(1.5)
        for cand in sorted(wd.glob(f"{primary}*")):
            if cand.suffix.lower() in {".jpg", ".jpeg", ".webp", ".png"}:
                if cand.suffix.lower() in {".jpg", ".jpeg"}:
                    shutil.copy(cand, out)
                else:
                    subprocess.run(
                        ["ffmpeg", "-y", "-i", str(cand), "-q:v", "4", str(out)],
                        capture_output=True,
                        timeout=30,
                    )
                if out.exists():
                    written.append(str(out.relative_to(ROOT)))
                    return written
    except Exception:
        pass

    # optional: if local media already present, grab one mid frame
    media = None
    for ext in (".mp4", ".webm", ".mkv"):
        cand = wd / f"{primary}{ext}"
        if cand.exists() and cand.stat().st_size > 100_000:
            media = cand
            break
    if media is None:
        return written
    try:
        dur_s = subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=nw=1:nk=1",
                str(media),
            ],
            text=True,
        ).strip()
        t = max(1.0, float(dur_s) * 0.35)
        out2 = IMG / f"{safe_pack}_{primary}_frame01.jpg"
        subprocess.run(
            ["ffmpeg", "-y", "-ss", str(t), "-i", str(media), "-frames:v", "1", "-q:v", "4", str(out2)],
            capture_output=True,
            check=True,
            timeout=60,
        )
        if out2.exists():
            written.append(str(out2.relative_to(ROOT)))
    except Exception:
        pass
    return written



def write_master(job: dict, state: dict, pack_stats: list[dict], frame_map: dict) -> None:
    lines = [
        "# Non-flagship transcript extract — master status",
        "",
        f"Generated: {utc_now()}",
        "",
        "Excludes seminar flagships (see `FLAGSHIP_TRANSCRIPTS.md`).",
        "",
        f"- Unique YouTube IDs: **{len(job['unique_ids'])}**",
        f"- Packs: **{len(job['packs'])}** ({sum(1 for v in job['packs'].values() if v)} with ≥1 YT URL)",
        f"- Captioned OK: **{sum(1 for v in state.get('videos', {}).values() if v.get('status')=='ok')}**",
        f"- No captions / errors: **{sum(1 for v in state.get('videos', {}).values() if v.get('status')!='ok')}**",
        "",
        "Workdir: `work/batch_videos/` (gitignored).",
        "Frames: `img/video_research/nonflagships/`.",
        "",
        "## Per-pack summary",
        "",
        "| Pack | Captions | Units | Frames |",
        "|------|----------|------:|--------|",
    ]
    frame_map = frame_map or {}
    stats_by = {s["pack"]: s for s in pack_stats}
    for pack in sorted(job["packs"].keys()):
        s = stats_by.get(pack, {"ok": 0, "total": len(job["packs"][pack]), "units": 0})
        fr = len(frame_map.get(pack, []))
        lines.append(f"| `{pack}` | {s['ok']}/{s['total']} | {s['units']} | {fr} |")
    lines += [
        "",
        "## Remaining failures (sample)",
        "",
    ]
    fails = [
        (vid, st)
        for vid, st in state.get("videos", {}).items()
        if st.get("status") != "ok"
    ]
    fails = sorted(fails, key=lambda x: x[0])[:40]
    if not fails:
        lines.append("_None recorded._")
    else:
        lines.append("| ID | Status |")
        lines.append("|----|--------|")
        for vid, st in fails:
            lines.append(f"| `{vid}` | {st.get('status')} {st.get('error','')[:40]} |")
    lines += [
        "",
        "## Notes",
        "",
        "- Captions are navigation aids, **not** proof substitutes.",
        "- Auto-captions may contain dual-line rollup noise and ASR errors.",
        "- Re-run: `python3 scripts/batch_extract_nonflagship.py`",
        "",
    ]
    MASTER.write_text("\n".join(lines), encoding="utf-8")


def map_pack_to_lessons(pack: str) -> list[Path]:
    """Heuristic map pack slug → lesson markdown files EN+VI."""
    # normalize slug to tokens for matching filenames
    # e.g. P_vs_NP → P_vs_NP; godel-incompleteness → Godel_Incompleteness
    candidates: list[Path] = []
    variants = {pack, pack.replace("-", "_"), pack.replace("_", "-")}
    # TitleCase from hyphens
    if "-" in pack:
        variants.add("_".join(p.capitalize() for p in pack.split("-")))
    if "_" in pack:
        variants.add("_".join(p.capitalize() if p.islower() else p for p in pack.split("_")))
        # Twin_Prime style already
        variants.add(pack)
    for lang in ("en", "vi"):
        base = ROOT / "contents" / lang
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            name = p.stem  # date-title
            # strip date prefix
            body = re.sub(r"^\d{2}-\d{2}-\d{2}-", "", name)
            # remove order prefix 01_02_
            body2 = re.sub(r"^\d{2}_\d{2}_", "", body)
            for v in variants:
                v_norm = v.replace("-", "_").lower()
                if v_norm in body2.replace("-", "_").lower() or v_norm in body.lower().replace("-", "_"):
                    candidates.append(p)
                    break
    # unique preserve order
    seen = set()
    out = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


TRANSCRIPT_BLOCK_EN = """
### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/{pack}/transcripts/` · status: `research/video-research/{pack}/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.
"""

TRANSCRIPT_BLOCK_VI = """
### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/{pack}/transcripts/` · trạng thái: `research/video-research/{pack}/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.
"""


def link_lessons(job: dict, frame_map: dict) -> int:
    n = 0
    for pack, vids in job["packs"].items():
        if not vids:
            continue
        lessons = map_pack_to_lessons(pack)
        frames = frame_map.get(pack) or []
        for lesson in lessons:
            text = lesson.read_text(encoding="utf-8")
            if f"research/video-research/{pack}/TRANSCRIPT_STATUS.md" in text and "batch extract" in text:
                continue
            if re.search(r"^### Transcript & frames \(batch extract\)", text, re.M):
                continue
            lang = "vi" if "/contents/vi/" in str(lesson) else "en"
            block = (TRANSCRIPT_BLOCK_VI if lang == "vi" else TRANSCRIPT_BLOCK_EN).format(pack=pack)
            if frames:
                rel = frames[0].lstrip("/")
                if lang == "en":
                    img_md = (
                        f"\n![Sample video frame]({{{{ site.baseurl }}}}/{rel})\n\n"
                        f"*Figure. Sample still from a pack primary video (see pack for timestamps).*\n"
                    )
                else:
                    img_md = (
                        f"\n![Frame mẫu video]({{{{ site.baseurl }}}}/{rel})\n\n"
                        f"*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*\n"
                    )
                block = block + img_md
            if re.search(r"^## References", text, re.M):
                text2 = re.sub(r"(^## References)", block + r"\n\1", text, count=1, flags=re.M)
            elif re.search(r"^## Tài liệu|^## Tham khảo", text, re.M):
                text2 = re.sub(
                    r"(^## (?:Tài liệu|Tham khảo))",
                    block + r"\n\1",
                    text,
                    count=1,
                    flags=re.M,
                )
            else:
                text2 = text.rstrip() + "\n" + block + "\n"
            if text2 != text:
                lesson.write_text(text2, encoding="utf-8")
                n += 1
    return n



def run_captions(job: dict, state: dict, sleep_s: float, limit: int | None) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    ids = job["unique_ids"]
    if limit:
        ids = ids[:limit]
    total = len(ids)
    for i, vid in enumerate(ids, 1):
        prev = state.get("videos", {}).get(vid, {})
        if prev.get("status") == "ok" and (WORK / f"video_{vid}" / "transcript.txt").exists():
            print(f"[{i}/{total}] SKIP ok {vid}", flush=True)
            continue
        # reprocess if captions already on disk
        wd = WORK / f"video_{vid}"
        if find_caption_file(wd, vid):
            title = prev.get("title") or ""
            info = wd / f"{vid}.info.json"
            if info.exists():
                try:
                    title = json.loads(info.read_text()).get("title") or title
                except Exception:
                    pass
            result = process_local_captions(vid, wd, title=title)
            state.setdefault("videos", {})[vid] = result
            save_state(state)
            print(f"[{i}/{total}] LOCAL {vid} {result['status']} units={result.get('units')}", flush=True)
            continue
        print(f"[{i}/{total}] FETCH {vid} ...", flush=True)
        result = yt_dlp_fetch(vid, sleep_s=sleep_s)
        state.setdefault("videos", {})[vid] = result
        save_state(state)
        print(
            f"[{i}/{total}] {result.get('status')} {vid} chars={result.get('chars')} units={result.get('units')}",
            flush=True,
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--captions-only", action="store_true")
    ap.add_argument("--materialize-only", action="store_true")
    ap.add_argument("--frames-only", action="store_true")
    ap.add_argument("--link-lessons", action="store_true")
    ap.add_argument("--sleep", type=float, default=4.0)
    ap.add_argument("--limit", type=int, default=None, help="Limit unique videos for caption fetch")
    ap.add_argument("--max-frames-packs", type=int, default=80)
    ap.add_argument("--skip-frames", action="store_true")
    args = ap.parse_args()

    job = discover_job()
    state = load_state()

    do_all = not any(
        [args.captions_only, args.materialize_only, args.frames_only, args.link_lessons]
    )

    if do_all or args.captions_only:
        run_captions(job, state, sleep_s=args.sleep, limit=args.limit)

    pack_stats = []
    frame_map: dict[str, list[str]] = {}

    if do_all or args.materialize_only or args.frames_only or args.link_lessons:
        # always rematerialize from state when not captions-only
        if not args.captions_only or do_all:
            for pack, vids in job["packs"].items():
                pack_stats.append(materialize_pack(pack, vids, state))
            print(f"Materialized {len(pack_stats)} packs", flush=True)

    if (do_all or args.frames_only) and not args.skip_frames:
        count = 0
        for pack, vids in sorted(job["packs"].items()):
            if not vids:
                frame_map[pack] = []
                continue
            if count >= args.max_frames_packs:
                frame_map[pack] = []
                continue
            print(f"FRAMES {pack} ...", flush=True)
            written = extract_primary_frames(pack, vids, state)
            frame_map[pack] = written
            if written:
                count += 1
                print(f"  -> {written}", flush=True)
            # soft limit sleep
            time.sleep(2)

    if do_all or args.materialize_only or args.frames_only:
        if not pack_stats:
            for pack, vids in job["packs"].items():
                pack_stats.append(materialize_pack(pack, vids, state))
        write_master(job, state, pack_stats, frame_map)
        # persist frame map
        (ROOT / "work" / "batch_nonflagship_frames.json").write_text(
            json.dumps(frame_map, indent=2) + "\n", encoding="utf-8"
        )

    if do_all or args.link_lessons:
        if not frame_map and (ROOT / "work" / "batch_nonflagship_frames.json").exists():
            frame_map = json.loads(
                (ROOT / "work" / "batch_nonflagship_frames.json").read_text(encoding="utf-8")
            )
        n = link_lessons(job, frame_map)
        print(f"Linked {n} lesson files", flush=True)

    ok = sum(1 for v in state.get("videos", {}).values() if v.get("status") == "ok")
    print(f"DONE captioned_ok={ok}/{len(job['unique_ids'])}", flush=True)


if __name__ == "__main__":
    main()
