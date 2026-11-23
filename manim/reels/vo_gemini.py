"""Helper tạo voiceover tiếng Việt qua Gemini TTS (đọc GEMINI_API_KEY từ biến môi trường)."""
import base64
import time
import urllib.error
import json
import os
import ssl
import subprocess
import urllib.request
import wave


def synth_segment(text, out_wav, voice="Orus", model="gemini-2.5-flash-preview-tts"):
    if os.path.exists(out_wav) and os.path.getsize(out_wav) > 1000:
        return probe_duration(out_wav)
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("Missing GEMINI_API_KEY in environment")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    prompt = (
        "Đọc bằng giọng nam tiếng Việt phổ thông miền Bắc, sôi nổi, giàu cảm xúc, nhiệt huyết, "
        "nhấn nhá tự nhiên và cuốn hút như một người thầy truyền cảm hứng. Chỉ đọc nguyên văn phần sau dấu hai chấm: "
        + text
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}
            },
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent)",
        },
        method="POST",
    )
    ctx = ssl.create_default_context(cafile="/etc/ssl/certs/ca-certificates.crt")
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
                res = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 5:
                time.sleep(22 * (attempt + 1))
            else:
                raise
    time.sleep(4)
    part = res["candidates"][0]["content"]["parts"][0]["inlineData"]
    pcm = base64.b64decode(part["data"])
    raw_wav = out_wav + ".raw.wav"
    with wave.open(raw_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm)
    # Cắt khoảng lặng đầu/cuối nhẹ và chuẩn hóa âm lượng
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


def probe_duration(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        text=True,
    ).strip()
    return float(out)


def build_vo_track(segments_with_start_sec, total_duration, out_m4a):
    """Ghép danh sách (wav_path, start_sec) thành 1 track AAC khớp độ dài video."""
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
