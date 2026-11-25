"""Lời đọc tiếng Việt cho reel gamma-function-factorial (Gemini TTS, skill course-manim-voice).
  python gamma_vo.py synth | python gamma_vo.py mux in.mp4 out.mp4   (cần: source ~/.config/gemini/tts.env)"""
import hashlib, json, os, sys

SK = os.path.expanduser("~/teaching/skills/course-manim-voice/scripts")
VO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo", "gamma")

VO = {
    "intro": "Giai thừa chỉ có ở số nguyên. Không giai thừa bằng một, một giai thừa bằng một, hai giai thừa bằng hai, ba giai thừa bằng sáu, bốn giai thừa bằng hai mươi bốn. Vậy một phần hai giai thừa là bao nhiêu? Năm một nghìn bảy trăm hai mươi chín, trong những lá thư gửi Goldbach, Euler tìm ra một đường cong trơn đi qua tất cả các điểm này. Đó là hàm Gamma.",
    "integral": "Gamma của z là tích phân từ không đến vô cùng của t mũ z trừ một, nhân e mũ trừ t, theo t. Với z bằng bốn, diện tích dưới đường cong là sáu, đúng bằng ba giai thừa. Tích phân từng phần cho ra hệ thức Gamma của x cộng một bằng x nhân Gamma của x, giống hệt quy tắc của giai thừa.",
    "poles": "Dùng hệ thức này theo chiều ngược lại, Gamma của x bằng Gamma của x cộng một, chia cho x, ta mở rộng đồ thị sang phía âm. Tại không, ta chia cho không, nên Gamma có cực. Tương tự tại âm một, âm hai, âm ba, và cứ thế mãi. Giữa hai cực liên tiếp, đồ thị đổi dấu.",
    "bm": "Nhưng đường qua các điểm giai thừa không phải duy nhất. Đường màu hồng cũng thỏa hệ thức này và cũng đi qua các điểm đó, chỉ là nó gợn sóng. Định lý Bohr–Mollerup nói rằng, nếu đòi thêm logarit của hàm phải lồi, thì trên nửa trục dương chỉ còn đúng một hàm. Đó chính là Gamma.",
    "half": "Giá trị đặc biệt nhất là Gamma của một phần hai. Đổi biến t bằng u bình phương, tích phân trở thành tích phân của e mũ trừ u bình phương, và bằng căn pi, khoảng một phẩy bảy bảy hai bốn. Nói theo ngôn ngữ giai thừa, âm một phần hai giai thừa bằng căn pi. Số pi của hình tròn bất ngờ xuất hiện trong giai thừa.",
    "nozero": "Gamma không bao giờ bằng không. Công thức phản xạ, Gamma của z nhân Gamma của một trừ z bằng pi chia sin pi z, cho thấy điều đó: vế phải không bao giờ bằng không. Hình màu này vẽ Gamma trên mặt phẳng phức. Màu cho biết góc của giá trị, và các cực là những điểm mà mọi màu cùng gặp nhau.",
    "zeta": "Gamma còn nằm ngay trong hàm zeta. Hàm xi của Riemann bằng một nửa s nhân s trừ một, nhân pi mũ trừ s trên hai, nhân Gamma của s trên hai, nhân zeta của s, và thỏa xi của s bằng xi của một trừ s. Hàm xi là hàm nguyên, không có cực. Gamma của s trên hai có cực tại không, âm hai, âm bốn, âm sáu. Vì vậy, tại âm hai, âm bốn, âm sáu, zeta bắt buộc phải bằng không để cân bằng. Đó chính là các không điểm tầm thường của zeta.",
    "ball": "Cuối cùng, thể tích quả cầu đơn vị trong không gian n chiều bằng pi mũ n trên hai, chia Gamma của n trên hai cộng một. Với n bằng năm, thể tích là tám pi bình phương trên mười lăm, khoảng năm phẩy hai sáu ba tám, lớn nhất trong các số chiều nguyên. Sau đó thể tích giảm dần về không.",
    "outro": "Tóm lại, Gamma nối giai thừa với tích phân, với số pi, với các không điểm của hàm zeta, và với hình học nhiều chiều. Một đường cong, rất nhiều bất ngờ.",
}


def wav_path(key):
    return os.path.join(VO_DIR, "%s_%s.wav" % (key, hashlib.md5(VO[key].encode()).hexdigest()[:8]))


def synth():
    sys.path.insert(0, SK)
    from vo_gemini import synth_segment, QuotaExhausted
    os.makedirs(VO_DIR, exist_ok=True)
    dpath = os.path.join(VO_DIR, "durations.json")
    dur = json.load(open(dpath)) if os.path.exists(dpath) else {}
    for k, text in VO.items():
        try:
            d, used = synth_segment(text, wav_path(k))
        except QuotaExhausted as e:
            print("QUOTA EXHAUSTED at", k); json.dump(dur, open(dpath, "w")); sys.exit(2)
        dur[k] = d
        print(k, "%.1fs" % d, used)
        json.dump(dur, open(dpath, "w"))


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
    synth() if sys.argv[1] == "synth" else mux(sys.argv[2], sys.argv[3])
