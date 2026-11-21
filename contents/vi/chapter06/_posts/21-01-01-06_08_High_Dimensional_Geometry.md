---
layout: post
title: "Hình học Cao chiều"
chapter: '06'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Ở chiều 2 và 3, hình học khớp với trực giác hằng ngày: quả cầu tròn, thể tích nằm "bên trong", khoảng cách thay đổi êm. Ở chiều $$n=1000$$, thể tích, diện tích mặt, góc và khoảng cách điển hình đều khác hẳn. **Hình học nhiều chiều**, cùng với xác suất và hiện tượng tập trung độ đo, là nền tảng ít được nhắc tên của phân tích dữ liệu, cảm biến nén, phép chiếu ngẫu nhiên và nhiều lý thuyết học thống kê. Nó cũng tạo ra những nghịch lý phá vỡ các "kinh nghiệm" từ chiều thấp.

Bài này trình bày các hiệu ứng chính: thể tích tập trung ở lớp vỏ, các vectơ ngẫu nhiên gần như trực giao, tập trung cho hàm Lipschitz, phép chiếu Johnson–Lindenstrauss, liên hệ với học máy. Mỗi ý được ghi rõ là định lý, lập luận gần đúng, hay lời quảng cáo.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao hầu hết thể tích của quả cầu nhiều chiều nằm gần lớp vỏ và gần xích đạo.
- Ước lượng chuẩn và tích vô hướng điển hình của các vectơ có tọa độ độc lập cùng phân phối (i.i.d.).
- Nêu ý chính của hiện tượng **tập trung**: một hàm Lipschitz của nhiều biến độc lập gần như là hằng số với xác suất cao.
- Phát biểu bổ đề **Johnson–Lindenstrauss** ở mức không hình thức: có thể nhúng vào $$O(\varepsilon^{-2}\log N)$$ chiều mà giữ khoảng cách trong phạm vi $$1\pm\varepsilon$$.
- Nối các ý trên với bài toán láng giềng gần nhất, "lời nguyền của số chiều", đặc trưng ngẫu nhiên, mà không khẳng định giảm chiều lúc nào cũng tốt.
- Phê phán cụm từ "lời nguyền của số chiều" vì nó gộp nhiều hiện tượng khác nhau.

**Kiến thức nền.** Chuẩn Euclid; kỳ vọng, phương sai; $$\mathbb{R}^n$$. Không bắt buộc lý thuyết độ đo; các lập luận về thể tích là cổ điển hoặc gần đúng.

---

## 1. Thể tích: lớp vỏ và xích đạo

Quả cầu đơn vị $$B_2^n=\{x:\|x\|_2\le 1\}$$ có thể tích

$$
\mathrm{Vol}(B_2^n)=\frac{\pi^{n/2}}{\Gamma(n/2+1)},
$$

đại lượng này đạt cực đại rồi giảm nhanh hơn hàm mũ theo $$n$$. Điều đó gợi ý rằng ở nhiều chiều, "quả cầu đơn vị" là một vật rất "mỏng". Nói theo hình học: với $$r<1$$ gần 1, lớp vỏ $$B_2^n\setminus r B_2^n$$ chứa gần như toàn bộ thể tích khi $$n$$ lớn. Tương tự, hầu hết thể tích nằm trong một dải hẹp quanh "xích đạo" vuông góc với bất kỳ hướng cố định nào.

**Hệ quả.** Phương pháp Monte Carlo, tính tích phân, khái niệm "tập điển hình" đều phải tính đến điều này: **điểm điển hình nằm gần mặt**, không nằm gần gốc. Chuẩn của một vectơ Gauss chuẩn tập trung quanh $$\sqrt{n}$$.

---

## 2. Vectơ ngẫu nhiên: chuẩn và góc

Với các tọa độ i.i.d. có kỳ vọng 0, phương sai $$\sigma^2$$:

$$
\mathbb{E}\|X\|_2^2=n\sigma^2,
$$

và nếu phân phối không có đuôi quá nặng, $$\|X\|_2$$ tập trung quanh $$\sigma\sqrt{n}$$. Với hai vectơ đẳng hướng độc lập, tích vô hướng dao động cỡ $$\sigma^2\sqrt{n}$$ trong khi mỗi chuẩn cỡ $$\sigma\sqrt{n}$$. Vì vậy cosin của góc giữa chúng thường cỡ $$n^{-1/2}$$: hai vectơ **gần như trực giao**.

Đây là một hiện tượng có định lý đi kèm, dưới các giả thiết rõ ràng về phân phối (với các cận tập trung định lượng), chứ không phải điều huyền bí của "dữ liệu lớn".

---

## 3. Tập trung độ đo

Nếu $$f:\mathbb{R}^n\to\mathbb{R}$$ là hàm Lipschitz với hằng số $$L$$ (theo khoảng cách Euclid) và $$X$$ là vectơ Gauss chuẩn, thì $$f(X)$$ tập trung quanh trung vị, với đuôi dưới Gauss (sub-Gaussian):

$$
\mathbb{P}\bigl(\lvert f(X)-\mathrm{Med}\rvert > t\bigr) \le 2e^{-t^2/(2L^2)}
$$

(có nhiều dạng phát biểu tương đương). Kết quả tương tự đúng trên mặt cầu nhiều chiều (bổ đề Lévy) và với một số độ đo tích.

**Vì sao quan trọng.** Ở nhiều chiều, các đối tượng *ngẫu nhiên* thường trở nên **cứng nhắc**: khoảng cách, giá trị kỳ dị của ma trận ngẫu nhiên, trung bình thực nghiệm đều trở nên dự đoán được. Lý thuyết ma trận ngẫu nhiên (định luật Marchenko–Pastur, định luật nửa đường tròn) là chủ đề họ hàng.

---

## 4. Giảm chiều: Johnson–Lindenstrauss

**Bổ đề JL (không hình thức).** Với $$0<\varepsilon<1$$ và mọi tập $$N$$ điểm trong không gian Euclid có số chiều bất kỳ, tồn tại một ánh xạ tuyến tính vào không gian có số chiều

$$
k=O(\varepsilon^{-2}\log N)
$$

giữ mọi khoảng cách giữa các cặp điểm trong phạm vi $$1\pm\varepsilon$$. Một phép chiếu Gauss ngẫu nhiên (hoặc một ánh xạ thưa có cấu trúc) đạt được điều này với xác suất cao.

**Cách đọc đúng.** JL bảo toàn **khoảng cách Euclid giữa các cặp điểm** cho một tập **hữu hạn**. Nó không tự động bảo toàn mọi cấu trúc đa tạp, các cụm theo một khoảng cách tùy ý, hay "ý nghĩa" của dữ liệu. Đây là một định lý về nhúng metric, không phải thứ miễn phí cho mọi quy trình học máy.

---

## 5. Nhiều "lời nguyền", không phải một

| Hiện tượng | Nội dung đại thể |
|------------|--------------|
| Thể tích trống rỗng | Phủ bằng lưới cần số mẫu tăng theo hàm mũ |
| Tập trung khoảng cách | Điểm gần nhất và điểm xa nhất có khoảng cách xấp xỉ nhau |
| Chi phí thống kê | Tốc độ ước lượng xấu đi theo số chiều của không gian hoặc số chiều nội tại |
| Chi phí tính toán | Thuật toán mở rộng kém nếu không khai thác cấu trúc |
| Bề mặt tối ưu | Hàm mất mát không lồi trong nhiều chiều (liên quan nhưng là chuyện khác) |

Một số việc lại **dễ hơn** khi số chiều tăng (tập trung, chiếu ngẫu nhiên, một số kết quả hình học lồi). "Lời nguyền" là danh sách những cách một phương pháp có thể thất bại khi nó dựa vào trực giác chiều thấp, chứ không phải một nỗi khổ chung cho mọi bài toán.

---

## 6. Số chiều nội tại và số chiều của không gian chứa

Dữ liệu trong $$\mathbb{R}^n$$ thường nằm gần một cấu trúc ít chiều: không gian con, đa tạp, vectơ thưa. **Số chiều nội tại** quyết định số mẫu cần thiết khi thuật toán khai thác được cấu trúc đó (khôi phục tín hiệu thưa, học đa tạp, PCA). Cảm biến nén: một vectơ $$s$$-thưa trong $$\mathbb{R}^n$$ có thể khôi phục từ $$m=O(s\log(n/s))$$ phép đo tuyến tính khi thỏa tính chất đẳng cự hạn chế (RIP). Đây là sự kết hợp giữa hình học nhiều chiều và tối ưu lồi hoặc thuật toán tham lam.

**Cảnh báo.** "Giả thuyết đa tạp" đôi khi đủ hữu ích, đôi khi chỉ là hình vẽ minh họa. Việc ước lượng số chiều nội tại từ dữ liệu thực tế rất dễ sai.

---

## 7. Liên hệ với học máy và thuật toán

1. **Láng giềng gần nhất:** hiện tượng tập trung khoảng cách có thể làm phương pháp láng giềng gần nhất cổ điển kém đi nếu các đặc trưng ít thông tin.  
2. **Hàm nhân / đặc trưng ngẫu nhiên:** xấp xỉ tích vô hướng trong không gian đặc trưng nhiều chiều nhờ hiện tượng tập trung.  
3. **Mạng nơ-ron:** chế độ quá tham số hóa nằm trong không gian tham số rất nhiều chiều; độ lệch ngầm (implicit bias) và hình học của các tập mức là đề tài nghiên cứu (xem Lý thuyết học máy, Toán học của AI).  
4. **Tối ưu:** các vật lồi nhiều chiều có thể có hình học chiếu dễ chịu (hàm mục tiêu Lipschitz tập trung).  
5. **Quyền riêng tư / băm:** băm nhạy địa phương (LSH) dựa trên xác suất va chạm theo hình học.

---

## 8. Hướng nghiên cứu

1. Hình học phi Euclid nhiều chiều (đồ thị, nhúng hyperbolic, khoảng cách vận chuyển tối ưu).  
2. Mô tả hình học chính xác của biên quyết định trong mạng nơ-ron.  
3. Thống nhất lý thuyết ma trận ngẫu nhiên với ma trận Hessian / Jacobian trong học sâu.  
4. Hình học thuật toán: tìm láng giềng gần nhất, cận dưới cho bài toán phân cụm.  
5. Giải tích hàm hình học (định lý Dvoretzky: mọi vật lồi nhiều chiều có lát cắt gần với hình cầu Euclid). Đây là toán thuần túy sâu nhưng có tiếng vang trong ứng dụng.

### Tính tỉ lệ lớp vỏ

$$
\frac{\mathrm{Vol}(r B_2^n)}{\mathrm{Vol}(B_2^n)}=r^n.
$$

Với $$r=0.9$$, $$n=100$$: $$0.9^{100}\approx 2.7\times 10^{-5}$$. Gần như toàn bộ "khối lượng" của quả cầu đơn vị nằm trong một lớp vỏ mỏng. Các thuật toán giả định "điểm nằm gần tâm" theo trực giác chiều thấp sẽ sai ở nhiều chiều.

### Phác họa phép chiếu ngẫu nhiên

JL cho $$k\sim C\varepsilon^{-2}\log N$$. Với $$N=10^6$$, $$\varepsilon=0.1$$: $$\log N$$ cỡ 14, nên $$k$$ cỡ vài nghìn. Đây là thông điệp về bậc độ lớn, không phải một hằng số chính xác không phụ thuộc chứng minh; nhưng nó đủ cho thấy số chiều cần để giữ **khoảng cách** chỉ tăng theo logarit của $$N$$ và không phụ thuộc số chiều ban đầu. Còn vẽ dữ liệu ra 2 chiều thì luôn mất thông tin, theo cách riêng của nó.

### Bài thực hành thảo luận

Lấy mẫu 200 vectơ Gauss ở các chiều $$d\in\{2,20,200\}$$. Vẽ biểu đồ tần suất của $$\|X\|_2/\sqrt{d}$$ và của $$|\cos|$$ giữa các cặp vectơ độc lập. Thảo luận: khẳng định "mọi điểm trong dữ liệu nhiều chiều đều cách đều nhau" đúng dưới mô hình nào, và sai khi dữ liệu không đẳng hướng hoặc có cấu trúc?

---

## Những nhầm lẫn thường gặp

| Khẳng định | Chỉnh lại |
|----------|-----|
| "Nhiều chiều ⇒ không thể học được." | Cấu trúc của dữ liệu và hiện tượng tập trung có thể giúp ích. |
| "Mọi cặp điểm đều cách đều nhau." | Có thể đúng dưới mô hình đẳng hướng; dữ liệu thật thường lệch hướng. |
| "JL ⇒ luôn chiếu được xuống 2 chiều mà không mất gì." | $$k$$ phụ thuộc $$N,\varepsilon$$; hình 2 chiều chỉ để nhìn, không giữ đúng khoảng cách. |
| "Thể tích quả cầu đơn vị tăng theo $$n$$." | Sai; nó → 0 khi $$n\to\infty$$. |
| "Chiếu ngẫu nhiên giữ nguyên các lớp phân loại." | Chỉ là lập luận gần đúng; phép chiếu giữ khoảng cách xấp xỉ, còn nhãn thì cần phân tích riêng. |

---

## Bài tập

1. Vì sao $$r^n$$ với $$r=0.9$$ rất nhỏ khi $$n$$ lớn (tỉ lệ thể tích)?
2. Với $$X_i\sim\mathcal{N}(0,1)$$ i.i.d.: tính $$\mathbb{E}\|X\|_2^2$$. Vì sao $$\|X\|_2\approx\sqrt{n}$$?
3. Giải thích vì sao cosin của góc có bậc $$n^{-1/2}$$.
4. Với $$N=10^6$$, $$\varepsilon=0.1$$: ước lượng bậc của $$k$$ từ $$O(\varepsilon^{-2}\log N)$$.
5. Nêu hai "lời nguyền" khác nhau: ước lượng bằng biểu đồ tần suất và tìm láng giềng gần nhất.
6. Tạo dữ liệu trong $$\mathbb{R}^{1000}$$ có số chiều nội tại bằng 2; thuật toán nào "nhận ra" điều đó?
7. Tìm phát biểu chính xác của bổ đề JL; tính ngẫu nhiên tham gia vào chứng minh như thế nào (phương pháp xác suất)?

---

## Kiến thức rút ra từ nghiên cứu video

Tóm tắt dùng cho thảo luận (đã đối chiếu với nguồn viết; **không bịa nội dung phụ đề**). Gói: `research/video-research/high-dimensional-geometry/analysis.md`.

### Trạng thái

**Xác suất cổ điển và hiện đại.** Hiện tượng tập trung độ đo và bổ đề JL là định lý; các khía cạnh hình học của phân tích dữ liệu vẫn đang được nghiên cứu.

### Phát biểu cốt lõi

Tập trung: hàm Lipschitz trên mặt cầu nhiều chiều hoặc với phân phối Gauss nhiều chiều gần như là hằng số. Johnson–Lindenstrauss: $$n$$ điểm trong không gian Euclid nhúng được vào $$O(\varepsilon^{-2}\log n)$$ chiều mà giữ khoảng cách trong phạm vi $$1\pm\varepsilon$$.

### Định nghĩa cần nắm chắc

- **Tập trung.** Biến ngẫu nhiên $$X$$ tập trung nếu $$P(|X-\mathbb{E}X|>t)$$ giảm nhanh theo $$t$$.
- **Số chiều nội tại.** Số bậc tự do hiệu dụng của một tập dữ liệu, thường $$\ll$$ số chiều $$d$$ của không gian chứa.

### Những hiểu lầm cần tránh

- Nghĩ rằng mọi hiện tượng nhiều chiều đều là "lời nguyền" (hiện tượng tập trung cũng giúp tạo ra thuật toán).
- Bỏ qua việc dữ liệu thường nằm gần các cấu trúc ít chiều.

---

## Nguồn video

Dùng video để **định hướng và hiểu không khí nghiên cứu**, không thay cho chứng minh hay bài báo gốc khi cần khẳng định điều then chốt. Chi tiết xếp hạng: `research/video-research/high-dimensional-geometry/`.

**Thứ tự gợi ý**

1. **Cốt lõi:** Roman Vershynin, Xác suất nhiều chiều, bài giảng 1: [https://www.youtube.com/watch?v=nKmYjFoiuYM](https://www.youtube.com/watch?v=nKmYjFoiuYM).  
2. **Nền tảng:** Simons Institute, Hình học nhiều chiều và hiện tượng tập trung, phần I: [https://www.youtube.com/watch?v=UHvT1MxFuvo](https://www.youtube.com/watch?v=UHvT1MxFuvo).  
3. **Tổng hợp:** trang khóa học của Vershynin (đủ các bài giảng): [https://www.math.uci.edu/~rvershyn/teaching/hdp/hdp.html](https://www.math.uci.edu/~rvershyn/teaching/hdp/hdp.html).  

**Nhắc lại trạng thái:** tập trung độ đo và bổ đề JL là định lý; khía cạnh hình học của phân tích dữ liệu vẫn đang được nghiên cứu.

---

### Phụ đề và khung hình

Phụ đề và các đơn vị kiến thức theo thời gian: `research/video-research/high-dimensional-geometry/transcripts/` · trạng thái: `research/video-research/high-dimensional-geometry/TRANSCRIPT_STATUS.md` · danh sách chung: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/high-dimensional-geometry_nKmYjFoiuYM_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói để biết mốc thời gian).*

## Tài liệu tham khảo

1. Vershynin — *High-Dimensional Probability*.
2. Boucheron–Lugosi–Massart — concentration.
3. Dasgupta & Gupta — JL; Ball — essay thể tích cao chiều.
4. [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/).

---

Danh mục URL đầy đủ: `research/video-research/high-dimensional-geometry/references.md`.

### Video (lộ trình gợi ý)

- Roman Vershynin, Xác suất nhiều chiều, bài giảng 1 (cốt lõi): https://www.youtube.com/watch?v=nKmYjFoiuYM
- Simons Institute, Hình học nhiều chiều và hiện tượng tập trung, phần I (nền tảng): https://www.youtube.com/watch?v=UHvT1MxFuvo
- Trang khóa học của Vershynin, đủ các bài giảng (tổng hợp): https://www.math.uci.edu/~rvershyn/teaching/hdp/hdp.html

### Bài báo và trang web (từ gói nghiên cứu)

- Vershynin — High-Dimensional Probability (book PDF via author): https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html
- Wikipedia — Concentration of measure: https://en.wikipedia.org/wiki/Concentration_of_measure
- Wikipedia — Johnson–Lindenstrauss lemma: https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma
- Wikipedia — Curse of dimensionality: https://en.wikipedia.org/wiki/Curse_of_dimensionality
- Wikipedia — High-dimensional statistics: https://en.wikipedia.org/wiki/High-dimensional_statistics

### Khóa học

- Gói: `research/video-research/high-dimensional-geometry/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- [Lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/); [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/).
- Bài chính của nhánh: [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/).
- Thực hành: lấy mẫu vectơ Gauss ở chiều 2, 20, 200; vẽ biểu đồ tần suất của chuẩn và của |cosin|.
- Lộ trình đọc: chương đầu sách Vershynin → bổ đề JL → một ví dụ về ma trận ngẫu nhiên.

## Video tham khảo

- **Xem trước:** [Lecture 1](https://www.youtube.com/watch?v=nKmYjFoiuYM) (Roman Vershynin, tiếng Anh). Bài giảng mở đầu khóa Xác suất nhiều chiều của Vershynin, trình bày các hiện tượng hình học lạ ở nhiều chiều. Nên xem trước khi đọc mục 1 đến 3.
- [High Dimensional Geometry and Concentration I](https://www.youtube.com/watch?v=UHvT1MxFuvo) (Simons Institute for the Theory of Computing, tiếng Anh). Bài giảng về hình học nhiều chiều và hiện tượng tập trung độ đo. Nên xem lần thứ hai, khi đã nắm ý chính.
