---
layout: post
title: "Phân tích Fourier → Xử lý tín hiệu"
chapter: '03'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Ảnh JPEG, pipeline âm thanh kiểu nén, quét MRI và radio tuner đều làm cùng một bước trí tuệ: **lấy tín hiệu sống trong thời gian/không gian và viết lại như tổ hợp tần số**—rồi giữ, bỏ, lọc hoặc lấy mẫu các tần số đó cho một mục đích.

**Lộ trình:** trực giác tần số → chuỗi Fourier → biến đổi Fourier → DFT/FFT → lọc & lấy mẫu → JPEG/audio/MRI → bất định & cửa sổ → nhầm lẫn.

Bài này nối điều hòa cổ điển với xử lý tín hiệu đời thường. Biên giới thuần túy (restriction, Kakeya): [Hong Wang (Ch.2)]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/)—ở đây nhấn **cơ chế công nghệ**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích tín hiệu như chồng các mode dao động (sin/cos hoặc mũ phức).
- Nêu ý **chuỗi Fourier** trên vòng/khoảng và **biến đổi Fourier** trên đường thẳng.
- Mô tả **DFT** và vì sao **FFT** làm DSP số thực tiễn.
- Cho cơ chế một bước của nén (kiểu JPEG), lọc, và thu MRI trong không gian tần số.
- Nối tốc độ lấy mẫu với tần số biểu diễn được (ý Nyquist) mức khẩu hiệu.
- Tránh “Fourier chỉ EQ nhạc” và “JPEG xóa pixel ngẫu nhiên.”

**Kiến thức nền.** Tích phân; $$e^{i\theta}=\cos\theta+i\sin\theta$$ hữu ích. [Giải tích]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/).

---

## 1. Tần số như hệ tọa độ

Âm thuần là sin. Sọc không gian thuần là sin 2D. Tín hiệu thật là hỗn hợp. Fourier cung cấp **cơ sở dao động** và hệ số “bao nhiêu tần số mỗi loại.” Đổi cơ sở không mất thông tin khi khả nghịch; nó **tái tổ chức** để nén, khử nhiễu, điều chế, giải PDE hệ số hằng trở nên dễ.

**Khẩu hiệu.** *Nhiều phép phức tạp trong thời gian/không gian là nhân hoặc mask đơn giản trong tần số—và ngược lại (định lý convolution).*

---

## 2. Chuỗi Fourier: thế giới tuần hoàn

$$
f(\theta)\sim\sum_n \hat f(n)e^{in\theta},\qquad
\hat f(n)=\frac1{2\pi}\int_0^{2\pi}f(\theta)e^{-in\theta}\,d\theta.
$$

Tổng riêng là xấp xỉ band-limited. Gibbs gần bước nhảy: cắt tần số tạo overshoot không gian. **Nhiệt:** khai triển Fourier biến $$\partial_t u=\kappa\partial_{xx}u$$ thành ODE độc lập từng mode—tần số cao tắt nhanh hơn. Xem [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

---

## 3. Biến đổi Fourier: tín hiệu không tuần hoàn

$$
\hat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx,\qquad
f(x)=\int\hat f(\xi)e^{2\pi i x\xi}\,d\xi
$$

(dưới giả thiết; quy ước $$2\pi$$ thay đổi). Đạo hàm ↔ nhân đa thức theo $$\xi$$; convolution ↔ tích; tịnh tiến ↔ pha. **Lọc** nhân $$\hat f$$ với $$H(\xi)$$ (low/high/band-pass)—radio và equalizer sống ở đây.

---

## 4. Thực tế rời rạc: DFT và FFT

Mẫu $$x_0,\ldots,x_{N-1}$$:

$$
\hat x_k=\sum_{n=0}^{N-1}x_n e^{-2\pi i kn/N},
\qquad
x_n=\frac1N\sum_{k=0}^{N-1}\hat x_k e^{2\pi i kn/N}.
$$

Ngây thơ $$O(N^2)$$. **FFT** tính DFT trong $$O(N\log N)$$—một trong những sự thật thuật toán quan trọng nhất thế kỷ XX. Audio thời gian thực, viễn thông băng rộng, nhân số nguyên lớn, tính khoa học đều cưỡi hiệu năng FFT.

**Cơ chế.** *DSP số phổ biến vì thuật toán miền tần số không chỉ đẹp mà còn rẻ đủ ở quy mô nhờ FFT.*

**Phác viễn thông.** OFDM—xương sống Wi-Fi và lớp vật lý di động hiện đại—gửi dữ liệu trên nhiều sóng mang con cách đều, trực giao trên một chu kỳ ký hiệu. Ở thu, FFT tách các sóng mang. Một lần nữa: RF công nghiệp là phân tích Fourier mặc tài liệu chuẩn.

---

## 5. Lấy mẫu và ý Nyquist

Tín hiệu liên tục không thể ghi như continuum vô hạn trên chip. **Lấy mẫu** ghi giá trị với tốc độ $$f_s$$ mẫu mỗi giây. Khẩu hiệu **Nyquist–Shannon:** để bắt tần số tới $$B$$ Hz không aliasing, lấy mẫu nhanh hơn $$2B$$ (dưới giả thiết band-limited lý tưởng).

**Aliasing** là hiện tượng mạo danh: tần số cao giả dạng tần số thấp sau lấy mẫu—bánh xe trong video, moiré ảnh. Lọc chống alias (low-pass trước lấy mẫu) là kỹ thuật Fourier, không phải mỹ phẩm.

Compressed sensing hiện đại nới lấy mẫu cổ điển dưới giả thiết sparsity—tối ưu + điều hòa ([Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/)). “Lấy mẫu nhanh hơn luôn tốt” không đúng: vượt nhu cầu Nyquist của băng tốn kém; chống alias vẫn quan trọng.

---

## 6. JPEG, audio, pipeline nén

**JPEG (ý tưởng).** Chia khối; áp biến đổi cos rời rạc (DCT)—họ hàng Fourier với cơ sở cos phù hợp tín hiệu thực và biên; lượng tử hóa hệ số (bỏ chi tiết tần số cao mắt ít nhạy); mã entropy phần còn lại. Khôi phục đảo biến đổi.

**Cơ chế một câu.**  
*Ảnh tự nhiên thường thưa/nén được trong cơ sở kiểu tần số; lượng tử hóa giữ hệ số năng lượng cao, bỏ hệ số thấp.*

**Audio.** Codec tri giác biến đổi cửa sổ ngắn (MDCT, …), cấp bit theo che psychoacoustic, rồi đảo. Pipeline đơn giản hơn dùng STFT (biến đổi Fourier thời gian ngắn) cho phân tích và lọc.

**MP3 không phải “Fourier xóa nhạc.”** Đó là coding tri giác miền tần số có kỹ thuật và chuẩn cẩn thận.

---

## 7. MRI và ảnh khoa học

Cộng hưởng từ thu dữ liệu vốn là mẫu của **biến đổi Fourier** của ảnh không gian mong muốn (k-space). Tái tạo về cơ bản là iFFT (+ hiệu chỉnh vật lý, lấy mẫu không đều, độ nhạy cuộn). MRI under-sample dùng tái tạo ràng buộc—lại sparsity + tối ưu.

**Cơ chế.** *Vật lý spin mã hóa thông tin không gian thành tần số; điều hòa là ngôn ngữ giải mã.*

Họ hàng: tái tạo CT (biến đổi Radon, filtered back-projection—lại hình học tích phân / Fourier), radar, tinh thể học (mẫu nhiễu xạ như độ lớn Fourier—pha retrieval khó).

---

## 8. Bất định, cửa sổ, time–frequency

Sin vô hạn định vị hoàn hảo tần số, không định vị thời gian. Xung Dirac ngược lại: định vị thời gian, phẳng tần số. **Nguyên lý bất định kiểu Heisenberg** (dạng điều hòa) hạn chế tập trung đồng thời: không thể vừa sắc thời gian vừa sắc tần số tùy ý.

**Fourier cửa sổ / STFT** và **wavelet** đổi độ phân giải theo thang. STFT trượt cửa sổ theo thời gian, biến đổi Fourier từng đoạn ngắn, xếp thành **spectrogram**—ngôn ngữ hình ảnh của tiếng nói, nhạc, chẩn đoán rung. Cửa sổ dài: tần số sắc, thời gian mờ. Cửa sổ ngắn: ngược lại. Đánh đổi đó không phải sở thích UI; đó là bất định được vận hành.

Wavelet (họ cơ sở khác) cải thiện một số nén và khử nhiễu nhờ định vị đa thang khớp cạnh và xung; JPEG 2000 dùng wavelet. Ý Fourier tổng quát: chọn cơ sở khớp lớp tín hiệu và sai số bạn chịu được. Hệ số nhỏ không luôn “không quan trọng”—pha và tổng kết hợp có thể làm hệ số nhỏ mang cấu trúc.

---

## 9. PDE và biên giới thuần túy

Biến đổi Fourier biến nhiều PDE tuyến tính hệ số hằng trên $$\mathbb{R}^n$$ thành phương trình đại số theo tần số. Toán tử vi phân hệ số hằng trở thành nhân với ký hiệu $$p(\xi)$$; giải PDE (khi hợp pháp) là chia ký hiệu rồi biến đổi ngược. Nghiệm cơ bản và ước lượng tán sắc là chương nâng cao. Solver phần tử hữu hạn kỹ thuật có thể không FFT cả miền trên lưới bất quy tắc, nhưng phân tích mode trong kết cấu và âm học—tần số tự nhiên, dạng mode, đáp ứng cưỡng bức—là tư duy tần số thuần sau rời rạc hóa thành bài riêng ma trận.

Lý thuyết thuần—hội tụ chuỗi, định lý Carleson về đảo Fourier điểm, conjecture restriction nối mặt tần số cong với ước lượng không-thời gian—sâu hơn codec cần rất nhiều. [Wang (Ch.2)]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/) cho biên nghiên cứu nơi điều hòa gặp hình học đo; bài này cho vì sao cùng môn xuất hiện trong thư viện ảnh, radio điện thoại và phòng MRI.

**Nhắc cơ chế chương.** Trực giao trừu tượng của mũ → thuật toán rẻ (FFT) → hạ tầng nén, cảm biến và truyền thông. Vẻ đẹp và silicon chia một hệ tọa độ.

---

### Khẩu hiệu Fourier (từ nghiên cứu video)

Lộ trình: [3B1B Fourier series](https://www.youtube.com/watch?v=r6sGWTCMz2k) → [Fourier transform](https://www.youtube.com/watch?v=spUNpyF58BY).

- Series cho thế giới tuần hoàn; transform cho không tuần hoàn; DFT cho mẫu hữu hạn; FFT để tính DFT nhanh.
- Lấy mẫu dưới Nyquist làm alias tần số cao thành thấp — nhầm lẫn không đảo trong dữ liệu rời rạc.
- Nén giữ hệ số lớn trong cơ sở Fourier/DCT nơi năng lượng tập trung.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Fourier chỉ cho nhạc.” | Ảnh, MRI, radio, PDE, phân tích dữ liệu. |
| “JPEG xóa pixel ngẫu nhiên.” | Lượng tử hóa hệ số trong cơ sở kiểu tần số. |
| “FFT khác DFT.” | FFT là thuật toán nhanh cho DFT. |
| “Lấy mẫu nhanh hơn luôn tốt.” | Vượt nhu cầu Nyquist tốn kém; chống alias vẫn quan trọng. |
| “Low-pass luôn an toàn.” | Làm mờ cạnh; có thể phá nội dung tần số cao cần thiết. |

---

## Bài tập

1. Viết $$\cos\theta$$ bằng mũ phức.  
2. Vì sao hàm tuần hoàn trơn cần ít hệ số Fourier lớn hơn hàm gián đoạn?  
3. Lọc bằng convolution thời gian bằng gì trong tần số?  
4. So sánh độ phức tạp DFT $$O(N^2)$$ vs FFT $$O(N\log N)$$ với $$N=2^{20}$$.  
5. ≤5 câu: DCT khối + lượng tử hóa như nén.  
6. Tai ~20 kHz—vì sao CD 44.1 kHz?  
7. Nâng cao: ma trận DFT và $$F^*F=NI$$ (unitary tới scale).

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/fourier-signal-processing/`.

**Thứ tự xem gợi ý**

1. **CORE** — 3Blue1Brown — But what is a Fourier series?: [https://www.youtube.com/watch?v=r6sGWTCMz2k](https://www.youtube.com/watch?v=r6sGWTCMz2k).
2. **CORE** — 3Blue1Brown — But what is the Fourier Transform?: [https://www.youtube.com/watch?v=spUNpyF58BY](https://www.youtube.com/watch?v=spUNpyF58BY).
3. **SURVEY** — 3Blue1Brown — Fourier transform / series topic hub: [https://www.3blue1brown.com/topics/fourier-transform](https://www.3blue1brown.com/topics/fourier-transform).
4. **FOUNDATION** — Stanford EE261 / DSP culture (Oppenheim-style courses): [https://see.stanford.edu/Course/EE261](https://see.stanford.edu/Course/EE261).
5. **FOUNDATION** — MIT OCW 6.003 Signals and Systems: [https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
6. **INTUITION** — Veritasium — The Most Underrated Algorithm (FFT): [https://www.youtube.com/watch?v=nmgFG7PUHfo](https://www.youtube.com/watch?v=nmgFG7PUHfo).

Danh mục URL đầy đủ: `research/video-research/fourier-signal-processing/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/fourier-signal-processing/transcripts/` · trạng thái: `research/video-research/fourier-signal-processing/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/fourier-signal-processing_r6sGWTCMz2k_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/fourier-signal-processing/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — But what is a Fourier series? — https://www.youtube.com/watch?v=r6sGWTCMz2k
2. 3Blue1Brown — But what is the Fourier Transform? — https://www.youtube.com/watch?v=spUNpyF58BY
3. 3Blue1Brown — Fourier transform / series topic hub — https://www.3blue1brown.com/topics/fourier-transform
4. Stanford EE261 / DSP culture (Oppenheim-style courses) — https://see.stanford.edu/Course/EE261
5. MIT OCW 6.003 Signals and Systems — https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/
6. Veritasium — The Most Underrated Algorithm (FFT) — https://www.youtube.com/watch?v=nmgFG7PUHfo
7. Zach Star — Nyquist–Shannon Sampling Theorem intuition — https://www.youtube.com/watch?v=Jv5FU8oUWEY
8. Numberphile — Fourier culture / related — https://www.youtube.com/watch?v=r6sGWTCMz2k

### Video (tìm thêm / phụ)

9. JPEG compression math explainers — https://en.wikipedia.org/wiki/JPEG

### Bài báo, sách, OCW và web

10. Cooley & Tukey — An algorithm for the machine calculation of complex Fourier series (1965): https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/
11. Wikipedia — Fourier transform: https://en.wikipedia.org/wiki/Fourier_transform
12. Wikipedia — Fast Fourier transform: https://en.wikipedia.org/wiki/Fast_Fourier_transform
13. Wikipedia — Nyquist–Shannon sampling theorem: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
14. Wikipedia — Discrete cosine transform: https://en.wikipedia.org/wiki/Discrete_cosine_transform
15. 3Blue1Brown Fourier hub: https://www.3blue1brown.com/topics/fourier-transform

### Trong khóa

16. Khóa: [Giải tích]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/). Gói: `research/video-research/fourier-signal-processing/`.

## Hướng đi tiếp

- [PTVP → Ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).  
- Biên thuần: [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/), [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/).  
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
