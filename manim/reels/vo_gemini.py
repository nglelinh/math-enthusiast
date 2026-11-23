"""Reusable Gemini TTS (single & 1-call batch) + Google Cloud TTS (Service Account) helper."""
import base64
import json
import os
import re
import ssl
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import wave

DEFAULT_MODELS = (
    "gemini-2.5-flash-preview-tts",
    "gemini-3.1-flash-tts-preview",
    "gemini-3.8-flash-tts",
    "gemini-3.8-flash-lite-tts",
)
UA = "Mozilla/5.0 (compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent)"


def _ssl_ctx():
    cafile = "/etc/ssl/certs/ca-certificates.crt"
    return ssl.create_default_context(cafile=cafile) if os.path.exists(cafile) else ssl.create_default_context()


def probe_duration(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        text=True,
    ).strip()
    return float(out)


def _normalize_wav(raw_wav, out_wav):
    subprocess.run(
        [
            "ffmpeg", "-y", "-v", "error", "-i", raw_wav,
            "-af", "silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.35:stop_threshold=-45dB,loudnorm=I=-16:TP=-1.5:LRA=11",
            out_wav,
        ],
        check=True,
    )
    os.remove(raw_wav)
    return probe_duration(out_wav)


def _gcloud_access_token(sa_path):
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding

    sa = json.load(open(sa_path, "r", encoding="utf-8"))
    now = int(time.time())
    b64 = lambda d: base64.urlsafe_b64encode(json.dumps(d, separators=(",", ":")).encode()).rstrip(b"=").decode()
    header = b64({"alg": "RS256", "typ": "JWT"})
    claim = b64({
        "iss": sa["client_email"],
        "scope": "https://www.googleapis.com/auth/cloud-platform",
        "aud": "https://oauth2.googleapis.com/token",
        "iat": now,
        "exp": now + 3600,
    })
    signing_input = f"{header}.{claim}".encode()
    key = serialization.load_pem_private_key(sa["private_key"].encode(), password=None)
    sig = base64.urlsafe_b64encode(key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())).rstrip(b"=").decode()
    jwt_tok = f"{header}.{claim}.{sig}"

    body = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_tok,
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body, headers={"User-Agent": UA}, method="POST")
    with urllib.request.urlopen(req, context=_ssl_ctx(), timeout=30) as resp:
        return json.loads(resp.read().decode())["access_token"]


def synth_gcloud_sa(text, out_wav, voice_name="vi-VN-Neural2-D", speaking_rate=1.02):
    sa_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")
    if not sa_path or not os.path.exists(sa_path):
        raise RuntimeError("Missing GOOGLE_APPLICATION_CREDENTIALS Service Account JSON")
    tok = _gcloud_access_token(sa_path)
    payload = {
        "input": {"text": text},
        "voice": {"languageCode": "vi-VN", "name": voice_name},
        "audioConfig": {"audioEncoding": "LINEAR16", "speakingRate": speaking_rate, "sampleRateHertz": 24000},
    }
    req = urllib.request.Request(
        "https://texttospeech.googleapis.com/v1/text:synthesize",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {tok}", "User-Agent": UA},
        method="POST",
    )
    with urllib.request.urlopen(req, context=_ssl_ctx(), timeout=60) as resp:
        audio_b64 = json.loads(resp.read().decode())["audioContent"]
    raw_wav = out_wav + ".raw.wav"
    with open(raw_wav, "wb") as f:
        f.write(base64.b64decode(audio_b64))
    return _normalize_wav(raw_wav, out_wav)


def _call_gemini_tts(full_prompt, voice="Algenib", models=DEFAULT_MODELS):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("Missing GEMINI_API_KEY in environment")
    payload = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    data = json.dumps(payload).encode("utf-8")
    ctx = _ssl_ctx()
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", "User-Agent": UA}, method="POST")
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=120) as resp:
                res = json.loads(resp.read().decode("utf-8"))
            return base64.b64decode(res["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2)
                continue
            raise
    raise RuntimeError("All Gemini TTS models returned HTTP 429")


def synth_segment(
    text,
    out_wav,
    voice="Algenib",
    models=DEFAULT_MODELS,
    style_prompt=(
        "Đọc bằng giọng nam tiếng Việt phổ thông miền Bắc, tự nhiên, rõ ràng, "
        "truyền cảm và gần gũi như một người thầy đang giảng bài. "
        "Chỉ đọc nguyên văn phần sau dấu hai chấm: "
    ),
):
    if os.path.exists(out_wav) and os.path.getsize(out_wav) > 1000:
        return probe_duration(out_wav)
    if os.environ.get("TTS_BACKEND") == "gcloud":
        return synth_gcloud_sa(text, out_wav)
    try:
        pcm = _call_gemini_tts(style_prompt + text, voice=voice, models=models)
    except RuntimeError:
        if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
            return synth_gcloud_sa(text, out_wav)
        raise
    raw_wav = out_wav + ".raw.wav"
    with wave.open(raw_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm)
    return _normalize_wav(raw_wav, out_wav)


def synth_batch(segments, out_dir, voice="Algenib", models=DEFAULT_MODELS):
    """Synthesize N (sid, text) segments in 1 Gemini TTS call and split via silencedetect."""
    os.makedirs(out_dir, exist_ok=True)
    if all(os.path.exists(os.path.join(out_dir, f"{sid}.wav")) for sid, _ in segments):
        return {sid: probe_duration(os.path.join(out_dir, f"{sid}.wav")) for sid, _ in segments}

    joined = "\n\n[pause 2 seconds]\n\n".join(txt for _, txt in segments)
    prompt = (
        "Đọc bằng giọng nam tiếng Việt phổ thông miền Bắc, tự nhiên, rõ ràng, gần gũi như người thầy đang giảng bài. "
        "Khi gặp ký hiệu [pause 2 seconds], hãy im lặng hoàn toàn khoảng 2 giây rồi mới đọc phần tiếp theo. "
        "Không đọc chữ pause. Chỉ đọc nội dung sau dấu hai chấm:\n" + joined
    )
    try:
        pcm = _call_gemini_tts(prompt, voice=voice, models=models)
        full_wav = os.path.join(out_dir, "_batch_full.wav")
        with wave.open(full_wav, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(pcm)
        total_dur = probe_duration(full_wav)
        p = subprocess.run(["ffmpeg", "-i", full_wav, "-af", "silencedetect=noise=-38dB:d=0.9", "-f", "null", "-"],
                           capture_output=True, text=True)
        raw_silences = [(float(a), float(b)) for a, b in re.findall(r"silence_start: ([0-9.]+).*?silence_end: ([0-9.]+)", p.stderr, re.S)]
        internal = [(a, b, b - a) for a, b in raw_silences if a > 1.0 and b < total_dur - 1.0]
        if len(internal) >= len(segments) - 1:
            cuts = sorted(sorted(internal, key=lambda x: -x[2])[:len(segments) - 1], key=lambda x: x[0])
            bounds = [0.0] + [(a + b) / 2.0 for a, b, _ in cuts] + [total_dur]
            durs = {}
            for idx, (sid, _) in enumerate(segments):
                raw_seg = os.path.join(out_dir, f"{sid}.raw.wav")
                out_wav = os.path.join(out_dir, f"{sid}.wav")
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{bounds[idx]:.3f}", "-to", f"{bounds[idx+1]:.3f}", "-i", full_wav, raw_seg], check=True)
                durs[sid] = _normalize_wav(raw_seg, out_wav)
            os.remove(full_wav)
            return durs
    except Exception:
        pass

    return {sid: synth_segment(txt, os.path.join(out_dir, f"{sid}.wav"), voice=voice, models=models) for sid, txt in segments}


def build_vo_track(segments_with_start_sec, total_duration, out_m4a):
    """Mix (wav_path, start_sec) pairs into one AAC track matching total_duration."""
    inputs = ["-f", "lavfi", "-t", f"{total_duration:.3f}", "-i", "anullsrc=r=24000:cl=mono"]
    filters = []
    mix_labels = ["[0:a]"]
    for idx, (wav_path, start_sec) in enumerate(segments_with_start_sec, start=1):
        inputs.extend(["-i", wav_path])
        ms = int(round(start_sec * 1000))
        filters.append(f"[{idx}:a]adelay={ms}|{ms}[a{idx}]")
        mix_labels.append(f"[a{idx}]")
    fc = ";".join(filters) + f";{''.join(mix_labels)}amix=inputs={len(mix_labels)}:duration=first:normalize=0[aout]"
    subprocess.run(
        [
            "ffmpeg", "-y", "-v", "error",
            *inputs,
            "-filter_complex", fc,
            "-map", "[aout]",
            "-c:a", "aac", "-b:a", "128k",
            out_m4a,
        ],
        check=True,
    )
