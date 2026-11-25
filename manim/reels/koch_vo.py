"""Lời đọc tiếng Việt cho reel koch-fourier-epicycles (Gemini TTS, xem ~/teaching/skills/course-manim-voice).
  python koch_vo.py synth            -> vo/koch/*.wav + vo/koch/durations.json
  python koch_vo.py mux in.mp4 out.mp4   -> ghép giọng theo vo/koch/starts.json (do scene ghi khi render vi)
Cần: source ~/.config/gemini/tts.env (GEMINI_API_KEY). Không in/commit khóa. vo/ không commit."""
import hashlib, json, os, sys
from koch_math import ERRP

SK = os.path.expanduser("~/teaching/skills/course-manim-voice/scripts")
VO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo", "koch")


def p(x):  # phần trăm đọc tiếng Việt: 8.93 -> "8,93 phần trăm"
    return ("%.2f" % x).replace(".", ",") + " phần trăm"


VO = {
    "intro": "Đây là bông tuyết Koch ở bậc bốn, gồm bảy trăm sáu mươi tám cạnh. Ta sẽ thử vẽ lại đường biên của nó, chỉ bằng những vòng tròn đang quay.",
    "formula": "Ý tưởng của chuỗi Fourier là thế này. Mỗi số hạng, c k nhân e mũ hai pi i k t, là một vòng tròn. Độ lớn của c k là bán kính, còn k là số vòng nó quay trong một chu kỳ. Nối các vòng tròn đuôi nối đầu, thì đầu mút cuối cùng sẽ vẽ ra một đường cong.",
    "fft": "Để tìm các hệ số c k, ta lấy bốn nghìn không trăm chín mươi sáu điểm cách đều dọc đường biên, rồi chạy FFT. Sau đó chỉ giữ lại N hệ số có độ lớn lớn nhất.",
    "n1": "Một vòng tròn thì chỉ cho ra một đường tròn. Sai số khoảng %s. Ở đây sai số là khoảng cách trung bình giữa đường dựng lại và đường Koch thật, tính hai chiều, chia cho bán kính trung bình của hình." % p(ERRP[1]),
    "n5": "Năm vòng tròn, và hình sáu cánh đã hiện ra. Các tần số k được chọn đều có dạng một cộng sáu m, vì bông tuyết đối xứng sáu lần. Sai số còn %s." % p(ERRP[5]),
    "n20": "Hai mươi vòng tròn, các nhánh nhỏ bắt đầu rõ. Sai số %s." % p(ERRP[20]),
    "n100": "Một trăm vòng tròn, hai đường gần như trùng nhau. Sai số khoảng %s." % p(ERRP[100]),
    "n500": "Năm trăm vòng tròn, sai số còn %s. Chú ý là từ một trăm lên năm trăm, ta thêm bốn trăm vòng mà sai số chỉ giảm rất ít." % p(ERRP[500]),
    "zoom": "Giờ ta phóng to một đỉnh nhọn. Với ít vòng tròn, góc bị bo tròn. Càng nhiều vòng thì càng sát, nhưng đường dựng lại vẫn luôn trơn, và quanh góc còn những gợn rất nhỏ, kiểu hiệu ứng Gibbs. Một tổng hữu hạn các vòng tròn thì không thể có góc nhọn thật.",
    "caveat": "Vì vậy, thứ ta dựng lại là đa giác Koch bậc bốn, chứ không phải fractal thật. Muốn tới fractal thật, phải đi qua vô hạn bậc, chứ không dừng lại ở số vòng tròn hữu hạn nào.",
    "outro": "Tóm lại, mỗi vòng tròn là một hệ số Fourier, tức một tần số. Càng nhiều số hạng thì xấp xỉ càng tốt, nhưng đó luôn là xấp xỉ của một đường cụ thể.",
}


def wav_path(key):
    h = hashlib.md5(VO[key].encode()).hexdigest()[:8]
    return os.path.join(VO_DIR, "%s_%s.wav" % (key, h))


def synth():
    sys.path.insert(0, SK)
    from vo_gemini import synth_segment
    os.makedirs(VO_DIR, exist_ok=True)
    dur = {}
    for k, text in VO.items():
        d, used = synth_segment(text, wav_path(k))
        dur[k] = d
        print(k, "%.1fs" % d, used)
    json.dump(dur, open(os.path.join(VO_DIR, "durations.json"), "w"))


def mux(vin, vout):
    sys.path.insert(0, SK)
    from vo_gemini import build_vo_track, mux as _mux, probe_duration
    starts = json.load(open(os.path.join(VO_DIR, "starts_vi.json")))
    segs = [(wav_path(k), starts[k]) for k in VO]
    total = probe_duration(vin)
    for (w, s), k in zip(segs, VO):
        end = s + probe_duration(w)
        nxt = [starts[j] for j in VO if starts[j] > s]
        assert end <= min(nxt + [total]) + 0.01, ("lời đọc dài hơn cảnh", k, end)
    m4a = os.path.join(VO_DIR, "track.m4a")
    build_vo_track(segs, total, m4a)
    _mux(vin, m4a, vout)


if __name__ == "__main__":
    if sys.argv[1] == "synth":
        synth()
    else:
        mux(sys.argv[2], sys.argv[3])
