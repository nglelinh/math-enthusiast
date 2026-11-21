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

Ảnh JPEG, các hệ thống nén âm thanh, máy chụp MRI và bộ dò đài radio đều dựa trên cùng một ý tưởng: **lấy một tín hiệu biến thiên theo thời gian hoặc không gian và viết lại nó thành tổng của các thành phần tần số**, rồi giữ lại, bỏ đi, lọc hoặc lấy mẫu các tần số đó tùy theo mục đích.

**Nội dung bài:** trực giác về tần số → chuỗi Fourier → biến đổi Fourier → DFT/FFT → lọc và lấy mẫu → JPEG, âm thanh, MRI → nguyên lý bất định và cửa sổ → hiểu lầm thường gặp.

Bài này nối giải tích điều hòa cổ điển với xử lý tín hiệu trong đời sống. Về các hướng nghiên cứu thuần túy (bài toán hạn chế, Kakeya), xem [Hong Wang (Chương 2)]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/); ở đây ta tập trung vào **cơ chế trong công nghệ**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích một tín hiệu là tổng chồng chập của các dao động (sin/cos hoặc hàm mũ phức).
- Nêu ý tưởng của **chuỗi Fourier** trên đường tròn hay một khoảng, và của **biến đổi Fourier** trên đường thẳng.
- Mô tả **biến đổi Fourier rời rạc (DFT)** và giải thích vì sao **thuật toán FFT** làm cho xử lý tín hiệu số trở nên khả thi.
- Mô tả cơ chế của từng bước trong nén ảnh (kiểu JPEG), lọc tín hiệu và thu ảnh MRI trong miền tần số.
- Giải thích ngắn gọn mối liên hệ giữa tốc độ lấy mẫu và các tần số có thể biểu diễn được (ý tưởng Nyquist).
- Tránh hai hiểu lầm: "Fourier chỉ dùng để chỉnh âm sắc nhạc" và "JPEG xóa ngẫu nhiên các điểm ảnh".

**Kiến thức cần có.** Tích phân; biết công thức $$e^{i\theta}=\cos\theta+i\sin\theta$$ sẽ có ích. Xem bài [Giải tích]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/).

---

## 1. Tần số như một hệ tọa độ

Một âm thanh thuần là một sóng sin. Một mẫu sọc thuần trong không gian là một sóng sin hai chiều. Tín hiệu thật là tổ hợp của nhiều sóng như vậy. Giải tích Fourier cho ta một **cơ sở gồm các dao động** cùng với hệ số cho biết mỗi tần số đóng góp bao nhiêu. Phép đổi cơ sở này không làm mất thông tin vì nó khả nghịch; nó chỉ **sắp xếp lại** thông tin, giúp việc nén, khử nhiễu, điều chế tín hiệu hay giải phương trình đạo hàm riêng hệ số hằng trở nên dễ hơn.

**Ý chính.** *Nhiều phép toán phức tạp trong miền thời gian hoặc không gian trở thành phép nhân hay phép che (mask) đơn giản trong miền tần số, và ngược lại (định lý tích chập).*

---

## 2. Chuỗi Fourier: tín hiệu tuần hoàn

$$
f(\theta)\sim\sum_n \hat f(n)e^{in\theta},\qquad
\hat f(n)=\frac1{2\pi}\int_0^{2\pi}f(\theta)e^{-in\theta}\,d\theta.
$$

Tổng riêng là một xấp xỉ chỉ chứa các tần số đến một mức nhất định. Gần điểm gián đoạn xuất hiện hiện tượng Gibbs: cắt bỏ tần số cao tạo ra phần vọt lố trong miền không gian. **Phương trình nhiệt:** khai triển Fourier biến $$\partial_t u=\kappa\partial_{xx}u$$ thành các phương trình vi phân thường độc lập cho từng thành phần tần số; tần số càng cao thì tắt càng nhanh. Xem bài [Phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

---

### Video ngắn: Dựng sóng vuông từ các sóng sin

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/square-wave-fourier_vi.mp4"></video>
</div>

Cộng các sóng sin có tần số lẻ với biên độ giảm dần, ta dựng được sóng vuông. Phần vọt lên ở chỗ gãy (hiện tượng Gibbs) không biến mất dù thêm bao nhiêu sóng.


### Tự tay thử: Tự cộng các sóng sin

<div class="mex-explainer" data-mex="fourier" data-lang="vi"></div>


## 3. Biến đổi Fourier: tín hiệu không tuần hoàn

$$
\hat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx,\qquad
f(x)=\int\hat f(\xi)e^{2\pi i x\xi}\,d\xi
$$

(với các giả thiết phù hợp; vị trí của hệ số $$2\pi$$ tùy theo quy ước). Phép lấy đạo hàm tương ứng với phép nhân với đa thức theo $$\xi$$; tích chập tương ứng với tích; phép tịnh tiến tương ứng với nhân với một thừa số pha. **Lọc tín hiệu** là nhân $$\hat f$$ với một hàm $$H(\xi)$$ (lọc thông thấp, thông cao, thông dải); radio và bộ chỉnh âm (equalizer) đều hoạt động theo cách này.

---

## 4. Trong thực tế rời rạc: DFT và FFT

Với các mẫu $$x_0,\ldots,x_{N-1}$$:

$$
\hat x_k=\sum_{n=0}^{N-1}x_n e^{-2\pi i kn/N},
\qquad
x_n=\frac1N\sum_{k=0}^{N-1}\hat x_k e^{2\pi i kn/N}.
$$

Tính trực tiếp mất $$O(N^2)$$ phép tính. **FFT** tính DFT trong $$O(N\log N)$$; đây là một trong những kết quả thuật toán quan trọng nhất của thế kỷ XX. Xử lý âm thanh thời gian thực, viễn thông băng rộng, nhân số nguyên lớn và tính toán khoa học đều dựa vào hiệu năng của FFT.

**Cơ chế.** *Xử lý tín hiệu số phổ biến vì các thuật toán trong miền tần số không chỉ đẹp về lý thuyết mà còn đủ rẻ để chạy ở quy mô lớn nhờ FFT.*

**Ví dụ trong viễn thông.** OFDM, nền tảng của Wi-Fi và lớp vật lý của mạng di động hiện đại, truyền dữ liệu trên nhiều sóng mang con cách đều nhau và trực giao với nhau trong một chu kỳ ký hiệu. Ở đầu thu, FFT tách các sóng mang này ra. Một lần nữa, kỹ thuật vô tuyến trong công nghiệp chính là giải tích Fourier được viết thành tiêu chuẩn kỹ thuật.

---

## 5. Lấy mẫu và ý tưởng Nyquist

Không thể lưu một tín hiệu liên tục với vô hạn giá trị trên một con chip. **Lấy mẫu** là ghi lại giá trị của tín hiệu với tốc độ $$f_s$$ mẫu mỗi giây. Ý tưởng của định lý **Nyquist–Shannon:** để ghi được các tần số đến $$B$$ Hz mà không bị chồng phổ, cần lấy mẫu nhanh hơn $$2B$$ (với giả thiết lý tưởng là tín hiệu có dải tần giới hạn).

**Chồng phổ** (aliasing) là hiện tượng một tần số cao "giả dạng" thành tần số thấp sau khi lấy mẫu, ví dụ bánh xe quay ngược trong video hay vân moiré trong ảnh. Bộ lọc chống chồng phổ (lọc thông thấp trước khi lấy mẫu) là một kỹ thuật Fourier thiết yếu, không phải chi tiết phụ.

Cảm biến nén (compressed sensing) hiện đại cho phép lấy ít mẫu hơn mức cổ điển khi tín hiệu thưa, nhờ kết hợp tối ưu hóa và giải tích điều hòa ([Tối ưu hóa]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/)). Không phải lúc nào lấy mẫu nhanh hơn cũng tốt hơn: lấy mẫu vượt quá nhu cầu Nyquist của dải tần là tốn kém, và vẫn cần chống chồng phổ.

---

## 6. JPEG, âm thanh và các hệ thống nén

**JPEG (ý tưởng).** Chia ảnh thành các khối; áp dụng biến đổi cosin rời rạc (DCT), một biến thể của biến đổi Fourier dùng cơ sở cosin, phù hợp với tín hiệu thực và điều kiện biên; lượng tử hóa các hệ số (bỏ bớt chi tiết tần số cao mà mắt ít nhạy cảm); sau đó mã hóa entropy phần còn lại. Khi giải nén, thực hiện biến đổi ngược.

**Cơ chế trong một câu.**  
*Ảnh tự nhiên thường thưa (nén được tốt) trong một cơ sở kiểu tần số; lượng tử hóa giữ lại các hệ số có năng lượng lớn và bỏ các hệ số có năng lượng nhỏ.*

**Âm thanh.** Các bộ mã hóa âm thanh dựa trên cảm nhận biến đổi từng đoạn ngắn (MDCT, …), phân bổ số bit dựa trên hiệu ứng che lấp của tai người, rồi biến đổi ngược. Các hệ thống đơn giản hơn dùng biến đổi Fourier thời gian ngắn (STFT) để phân tích và lọc.

**MP3 không phải là "dùng Fourier để xóa bớt nhạc".** Đó là mã hóa dựa trên cảm nhận trong miền tần số, được thiết kế kỹ thuật và chuẩn hóa cẩn thận.

---

## 7. MRI và ảnh khoa học

Máy cộng hưởng từ thu được dữ liệu vốn là các mẫu của **biến đổi Fourier** của ảnh cần chụp (gọi là không gian k). Việc tái tạo ảnh về cơ bản là biến đổi Fourier ngược bằng FFT (cộng thêm các hiệu chỉnh vật lý, xử lý lấy mẫu không đều, độ nhạy của cuộn thu). MRI lấy mẫu thưa dùng phương pháp tái tạo có ràng buộc, lại dựa trên tính thưa và tối ưu hóa.

**Cơ chế.** *Tính chất vật lý của spin mã hóa thông tin vị trí thành tần số; giải tích điều hòa là ngôn ngữ để giải mã.*

Các ứng dụng liên quan: tái tạo ảnh CT (biến đổi Radon, phương pháp chiếu ngược có lọc, cũng dựa trên tích phân và Fourier), radar, tinh thể học (ảnh nhiễu xạ cho biết độ lớn của biến đổi Fourier, và việc khôi phục pha là bài toán khó).

---

## 8. Nguyên lý bất định, cửa sổ và phân tích thời gian–tần số

Một sóng sin vô hạn xác định hoàn toàn tần số nhưng không cho biết gì về thời điểm. Xung Dirac thì ngược lại: xác định chính xác thời điểm nhưng trải đều trên mọi tần số. **Nguyên lý bất định kiểu Heisenberg** (phiên bản trong giải tích điều hòa) giới hạn khả năng tập trung đồng thời: không thể vừa chính xác tùy ý về thời gian vừa chính xác tùy ý về tần số.

**Biến đổi Fourier có cửa sổ (STFT)** và **wavelet** cho phép thay đổi độ phân giải theo tỉ lệ. STFT trượt một cửa sổ theo thời gian, lấy biến đổi Fourier của từng đoạn ngắn và xếp lại thành **phổ đồ** (spectrogram), công cụ hình ảnh để phân tích tiếng nói, âm nhạc hay chẩn đoán rung động. Cửa sổ dài thì tần số rõ nhưng thời gian mờ; cửa sổ ngắn thì ngược lại. Sự đánh đổi này không phải là lựa chọn giao diện, mà chính là nguyên lý bất định trong thực tế.

Wavelet (một họ cơ sở khác) giúp nén và khử nhiễu tốt hơn trong một số trường hợp, nhờ khả năng định vị ở nhiều tỉ lệ, phù hợp với các cạnh và xung; JPEG 2000 dùng wavelet. Ý tưởng chung của Fourier: chọn cơ sở phù hợp với loại tín hiệu và mức sai số chấp nhận được. Hệ số nhỏ không phải lúc nào cũng "không quan trọng": pha và sự kết hợp của nhiều hệ số có thể khiến các hệ số nhỏ mang thông tin cấu trúc.

---

## 9. Phương trình đạo hàm riêng và nghiên cứu thuần túy

Biến đổi Fourier biến nhiều phương trình đạo hàm riêng tuyến tính hệ số hằng trên $$\mathbb{R}^n$$ thành phương trình đại số theo tần số. Một toán tử vi phân hệ số hằng trở thành phép nhân với ký hiệu $$p(\xi)$$; giải phương trình (khi hợp lệ) là chia cho ký hiệu rồi biến đổi ngược. Nghiệm cơ bản và các ước lượng tán sắc là nội dung nâng cao. Các phần mềm phần tử hữu hạn trong kỹ thuật có thể không dùng FFT trên toàn miền với lưới không đều, nhưng việc phân tích dao động trong kết cấu và âm học (tần số riêng, dạng dao động, đáp ứng cưỡng bức) vẫn là tư duy tần số, sau khi rời rạc hóa thành bài toán trị riêng của ma trận.

Lý thuyết thuần túy, như sự hội tụ của chuỗi Fourier, định lý Carleson về hội tụ hầu khắp nơi, hay giả thuyết hạn chế nối các mặt cong trong miền tần số với ước lượng không-thời gian, sâu hơn rất nhiều so với những gì một bộ mã hóa cần. Bài [Wang (Chương 2)]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/) giới thiệu hướng nghiên cứu nơi giải tích điều hòa gặp lý thuyết độ đo hình học; bài này giải thích vì sao cùng một môn học lại xuất hiện trong thư viện ảnh, radio điện thoại và phòng chụp MRI.

**Tóm tắt cơ chế của bài.** Tính trực giao của các hàm mũ → thuật toán rẻ (FFT) → hạ tầng cho nén, cảm biến và truyền thông. Lý thuyết đẹp và vi mạch dùng chung một hệ tọa độ.

---

### Tóm tắt nhanh (rút ra từ các video)

Thứ tự xem: [3B1B về chuỗi Fourier](https://www.youtube.com/watch?v=r6sGWTCMz2k) → [biến đổi Fourier](https://www.youtube.com/watch?v=spUNpyF58BY).

- Chuỗi Fourier dùng cho tín hiệu tuần hoàn; biến đổi Fourier cho tín hiệu không tuần hoàn; DFT cho tập mẫu hữu hạn; FFT để tính DFT nhanh.
- Lấy mẫu dưới tần số Nyquist làm tần số cao bị chồng thành tần số thấp, và không thể khôi phục lại từ dữ liệu rời rạc.
- Nén giữ lại các hệ số lớn trong cơ sở Fourier/DCT, nơi năng lượng tập trung.

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Fourier chỉ dùng cho âm nhạc." | Ảnh, MRI, radio, phương trình đạo hàm riêng, phân tích dữ liệu. |
| "JPEG xóa ngẫu nhiên các điểm ảnh." | JPEG lượng tử hóa hệ số trong một cơ sở kiểu tần số. |
| "FFT khác DFT." | FFT là thuật toán nhanh để tính DFT. |
| "Lấy mẫu càng nhanh càng tốt." | Vượt quá nhu cầu Nyquist là tốn kém; vẫn cần chống chồng phổ. |
| "Lọc thông thấp luôn an toàn." | Nó làm mờ các cạnh và có thể làm mất thông tin tần số cao cần thiết. |

---

## Bài tập

1. Viết $$\cos\theta$$ dưới dạng hàm mũ phức.  
2. Vì sao một hàm tuần hoàn trơn cần ít hệ số Fourier lớn hơn một hàm gián đoạn?  
3. Lọc bằng tích chập trong miền thời gian tương ứng với phép toán gì trong miền tần số?  
4. So sánh độ phức tạp của DFT $$O(N^2)$$ và FFT $$O(N\log N)$$ với $$N=2^{20}$$.  
5. Viết không quá 5 câu: DCT theo khối kết hợp lượng tử hóa thực hiện việc nén như thế nào?  
6. Tai người nghe được đến khoảng 20 kHz; vì sao đĩa CD dùng tần số lấy mẫu 44.1 kHz?  
7. Nâng cao: ma trận DFT và $$F^*F=NI$$ (unita sai khác một hệ số).

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và xây dựng trực giác**, không thay thế chứng minh hay tài liệu chuẩn. Đánh giá chi tiết: `research/video-research/fourier-signal-processing/`.

**Thứ tự xem gợi ý**

1. **Cốt lõi** — 3Blue1Brown — But what is a Fourier series?: [https://www.youtube.com/watch?v=r6sGWTCMz2k](https://www.youtube.com/watch?v=r6sGWTCMz2k).
2. **Cốt lõi** — 3Blue1Brown — But what is the Fourier Transform?: [https://www.youtube.com/watch?v=spUNpyF58BY](https://www.youtube.com/watch?v=spUNpyF58BY).
3. **Tổng quan** — 3Blue1Brown — trang tổng hợp về Fourier: [https://www.3blue1brown.com/topics/fourier-transform](https://www.3blue1brown.com/topics/fourier-transform).
4. **Nền tảng** — Stanford EE261 (khóa học xử lý tín hiệu): [https://see.stanford.edu/Course/EE261](https://see.stanford.edu/Course/EE261).
5. **Nền tảng** — MIT OCW 6.003 Signals and Systems: [https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
6. **Trực giác** — Veritasium — The Most Underrated Algorithm (FFT): [https://www.youtube.com/watch?v=nmgFG7PUHfo](https://www.youtube.com/watch?v=nmgFG7PUHfo).

Danh sách URL đầy đủ: `research/video-research/fourier-signal-processing/references.md`.


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/fourier-signal-processing/transcripts/` · trạng thái: `research/video-research/fourier-signal-processing/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/fourier-signal-processing_r6sGWTCMz2k_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/fourier-signal-processing/references.md`.

### Video chính

1. 3Blue1Brown — But what is a Fourier series? — https://www.youtube.com/watch?v=r6sGWTCMz2k
2. 3Blue1Brown — But what is the Fourier Transform? — https://www.youtube.com/watch?v=spUNpyF58BY
3. 3Blue1Brown — Fourier transform / series topic hub — https://www.3blue1brown.com/topics/fourier-transform
4. Stanford EE261 / DSP culture (Oppenheim-style courses) — https://see.stanford.edu/Course/EE261
5. MIT OCW 6.003 Signals and Systems — https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/
6. Veritasium — The Most Underrated Algorithm (FFT) — https://www.youtube.com/watch?v=nmgFG7PUHfo
7. Zach Star — Nyquist–Shannon Sampling Theorem intuition — https://www.youtube.com/watch?v=Jv5FU8oUWEY
8. Numberphile — Fourier culture / related — https://www.youtube.com/watch?v=r6sGWTCMz2k

### Video bổ sung

9. Giải thích toán học của nén JPEG — https://en.wikipedia.org/wiki/JPEG

### Bài báo, sách, khóa học mở và trang web

10. Cooley & Tukey — An algorithm for the machine calculation of complex Fourier series (1965): https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/
11. Wikipedia — Fourier transform: https://en.wikipedia.org/wiki/Fourier_transform
12. Wikipedia — Fast Fourier transform: https://en.wikipedia.org/wiki/Fast_Fourier_transform
13. Wikipedia — Nyquist–Shannon sampling theorem: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
14. Wikipedia — Discrete cosine transform: https://en.wikipedia.org/wiki/Discrete_cosine_transform
15. 3Blue1Brown Fourier hub: https://www.3blue1brown.com/topics/fourier-transform

### Trong khóa học

16. Bài liên quan: [Giải tích]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/), [Phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/). Bộ tư liệu: `research/video-research/fourier-signal-processing/`.

## Hướng đi tiếp

- [Phương trình vi phân → Ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).  
- Nghiên cứu thuần túy: [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/), [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/).  
- Viết lại cơ chế cốt lõi trong một đoạn; ghi lại một câu hỏi còn mở.

## Video tham khảo

- **Xem trước:** [But what is a Fourier series? From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, tiếng Anh. Giới thiệu chuỗi Fourier từ bài toán truyền nhiệt; nên xem trước khi đọc bài.
- [But what is the Fourier Transform? A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, tiếng Anh. Giải thích trực quan biến đổi Fourier; nên xem sau khi đã nắm ý chính của bài.
- [The Most Underrated Algorithm](https://www.youtube.com/watch?v=nmgFG7PUHfo) — Veritasium, tiếng Anh. Xem thêm sau hai video trên, về thuật toán FFT.
