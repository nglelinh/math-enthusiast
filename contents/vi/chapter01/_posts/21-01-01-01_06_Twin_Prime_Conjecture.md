---
layout: post
title: "Giả thuyết Số nguyên tố sinh đôi"
chapter: '01'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

**Số nguyên tố sinh đôi** là các cặp số nguyên tố cách nhau đúng 2: $$(3,5)$$, $$(5,7)$$, $$(11,13)$$, $$(17,19)$$, $$(29,31)$$, $$(101,103)$$, …  

**Giả thuyết số nguyên tố sinh đôi** khẳng định có **vô hạn** cặp như vậy.

Đây không phải bài Thiên niên kỷ, nhưng là một trong những câu hỏi mở nổi tiếng nhất của lý thuyết số—và là nơi có tiến bộ rực rỡ thập niên 2010: **khoảng cách bị chặn** giữa các số nguyên tố liên tiếp. Zhang (2013), Maynard, và các dự án Polymath đã chứng minh rằng *một* khoảng chẵn bị chặn xuất hiện vô hạn lần; **khoảng đúng bằng 2** vẫn ngoài tầm.

Bài này giúp bạn phát biểu sạch, hiểu heuristic Hardy–Littlewood, phân biệt “gap bị chặn” với “sinh đôi,” và kể câu chuyện sàng mà không giả vờ đã giải giả thuyết.

**Lộ trình:** phát biểu → heuristic → rào cản sàng → Zhang–Maynard–Polymath → còn mở gì → toán xung quanh → nhầm lẫn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu giả thuyết số nguyên tố sinh đôi và đưa ví dụ cặp sinh đôi.
- Tương phản **vô hạn số nguyên tố** (Euclid, đã biết) với **vô hạn sinh đôi** (mở).
- Giải thích **khoảng cách bị chặn**: tồn tại $$H$$ sao cho $$p_{n+1}-p_n\le H$$ với vô hạn chỉ số $$n$$.
- Kể **Zhang (2013)** và **Maynard** (cùng cải tiến Polymath); bound vô điều kiện chuẩn trong tường thuật seminar là **$$H=246$$**.
- Giải thích vì sao gap 2 vẫn ngoài tầm sàng hiện tại (parity / giới hạn khẩu hiệu).
- Nối chủ đề mẫu tinh của nguyên tố với [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) và essay [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/).
- Tránh LO6: “Zhang chứng minh sinh đôi.”

**Tiên quyết.** Số nguyên tố; đồng dư cơ bản. Biết ý $$1/\log x$$ như mật độ thô của nguyên tố sẽ giúp đọc heuristic.

**Liên kết seminar.** **LO1**; [Maynard / Fields]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/); [Euclid vô hạn nguyên tố]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/); [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/).

---

## 1. Phát biểu

**Giả thuyết số nguyên tố sinh đôi.** Có vô hạn số nguyên tố $$p$$ sao cho $$p+2$$ cũng nguyên tố.

Tương đương: phương trình $$p'-p=2$$ có vô hạn nghiệm trong các số nguyên tố.

Giả thuyết rộng hơn của **Polignac** dự đoán mọi khoảng chẵn cố định $$2k$$ xuất hiện vô hạn lần giữa các cặp nguyên tố. Sinh đôi là trường hợp $$k=1$$—khoảng chẵn nhỏ nhất có thể (vì khoảng lẻ lớn hơn 2 không thể là hai số lẻ nguyên tố trừ case liên quan 2).

**Euclid đã biết có vô hạn nguyên tố**; chứng minh cổ điển xây $$N=P!+1$$ hoặc $$N=p_1\cdots p_k+1$$ để buộc một nguyên tố mới. Lập luận đó **không** buộc cặp cách 2. Vô hạn “điểm” không tự động cho vô hạn “cặp gần nhau.”

---

## 2. Heuristic: vì sao người ta tin

Các số nguyên tố thưa dần xấp xỉ như $$1/\log x$$ (định lý số nguyên tố). Xác suất heuristic rằng cả $$n$$ và $$n+2$$ đều nguyên tố có cỡ $$1/(\log n)^2$$ (sau khi chỉnh hệ số cho ràng buộc modulo nhỏ—Hardy–Littlewood). Chuỗi

$$
\sum_n \frac{1}{(\log n)^2}
$$

**phân kỳ**, nên người ta kỳ vọng vô hạn cặp sinh đôi, với tiệm cận chính xác hơn được đoán bởi **hằng số twin prime** trong giả thuyết Hardy–Littlewood về bộ nguyên tố (prime tuples).

Heuristic **không phải chứng minh**, nhưng tổ chức dữ liệu: cặp sinh đôi tiếp tục xuất hiện trong tính toán tới tầm rất cao, thưa dần đúng “nhịp” kỳ vọng. Cùng đạo đức với kiểm không điểm zeta: bằng chứng mạnh, chưa phải định lý.

**Ghi chú trực quan.** “Nguyên tố ngẫu nhiên” với mật độ $$1/\log n$$ là mô hình; các đồng dư (ví dụ không chia hết cho 2, 3, …) tạo tương quan—hằng số twin prime chỉnh các tương quan đó. Bạn không cần thuộc công thức để dùng khẩu hiệu seminar.

---

## 3. Vì sao sàng khó với đúng hai lần nguyên tố

Phương pháp **sàng** giỏi phát hiện **gần nguyên tố** (số có ít thừa số nguyên tố). Biến “gần” thành “đúng nguyên tố *hai lần*” vướng các **parity problems**: sàng cổ điển khó phân biệt số có số thừa số chẵn hay lẻ trong một số bối cảnh—và sinh đôi đòi hỏi cả hai vị trí đều “nguyên tố đúng.”

Do đó sàng cổ điển cho các định lý kiểu **định lý Chen**: có vô hạn nguyên tố $$p$$ sao cho $$p+2$$ là nguyên tố *hoặc* tích hai nguyên tố—gần đến mức khó chịu, vẫn chưa phải sinh đôi.

Khẩu hiệu mang đi: **gần nguyên tố ≠ nguyên tố**; khoảng cách giữa “hầu như” và “đúng” có thể là cả một kỷ nguyên kỹ thuật.

---

## 4. Khoảng cách bị chặn: Zhang, Maynard, Polymath

Năm 2013, **Yitang Zhang** chứng minh

$$
\liminf_{n\to\infty} (p_{n+1}-p_n) < 70{,}000{,}000.
$$

Nghĩa là: một khoảng chẵn bị chặn bởi 70 triệu xuất hiện vô hạn lần giữa các nguyên tố *liên tiếp*. Con số lớn—nhưng **hữu hạn**. Đó là định lý dạng này đầu tiên: không còn chỉ “khoảng cách trung bình tăng như $$\log n$$,” mà có **cụm chặt vô hạn lần** với chặn tuyệt đối.

Năm **2013**, **Yitang Zhang** chứng minh

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) < 70{,}000{,}000.
$$

Tức: trong các gap giữa nguyên tố liên tiếp, một gap nhỏ hơn bảy mươi triệu xuất hiện **vô hạn lần**. Số lớn nhưng **hữu hạn**—định lý đầu tiên kiểu này. Trước Zhang, người ta không biết liminf gap liên tiếp có hữu hạn; nguyên tố có thể bị buộc cách nhau ngày càng xa theo nghĩa liminf.

Phương pháp xây trên ý **Goldston–Pintz–Yıldırım (GPY)** về phát hiện nguyên tố trong tuple admissible các dạng tuyến tính, kết hợp ước lượng phân bố nguyên tố trong cấp số cộng dạng trung bình tinh tế. Đột phá Zhang: đủ phân bố mà không cần giả thuyết mạnh nhất.

Cải tiến nhanh theo sau:

- **Polymath** (Polymath8) tối ưu cách tiếp cận Zhang, thu nhỏ bound admissible mạnh qua cộng tác cộng đồng.  
- **James Maynard** (và ý tưởng liên quan độc lập quanh Tao) đưa **trọng số sàng đa chiều** linh hoạt hơn—nhiều dạng tuyến tính được trọng số cùng lúc hiệu quả hơn. Khung Maynard thường đơn giản hóa và mạnh hóa kết quả gap, mở rộng sang mẫu nguyên tố phong phú hơn.

Sau tối ưu, bound vô điều kiện chuẩn

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\le H
$$

đứng ở **$$H=246$$** trong tường thuật chuẩn Maynard–Polymath (điểm tham chiếu seminar; văn liệu kỹ thuật có thể tinh chỉnh—trích survey khi viết A3). Dưới giả thuyết mạnh kiểu **Elliott–Halberstam** về phân bố nguyên tố trong cấp số cộng, phương pháp có thể đẩy về gap chẵn một chữ số (ví dụ 6), nhưng **đạt $$H=2$$**—sinh đôi thật—dường như cần ý tưởng vượt mô hình sàng hiện tại. **Parity barrier** là slogan thường dùng vì sao 2 đặc biệt.

Công trình Maynard về gap nhỏ, gap lớn và sàng là một phần **Fields Medal 2022**. Xem [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/).

---

## 5. Còn mở gì?

| Phát biểu | Tình trạng |
|-----------|------------|
| Vô hạn nguyên tố | **Đã chứng** (Euclid, …) |
| Vô hạn cặp sinh đôi (gap = 2) | **Mở** |
| Một gap chẵn bị chặn xuất hiện vô hạn lần | **Đã chứng** (Zhang / Maynard / Polymath) |
| $$\liminf(p_{n+1}-p_n)\le 246$$ | **Đã chứng** (bound tham chiếu) |
| Gap = 2 vô hạn lần | **Mở** |
| Định lý Chen ($$p+2$$ nguyên tố hoặc bán nguyên tố) | **Đã chứng** |
| Asymptotic Hardy–Littlewood cho twins | **Mở** (giả thuyết) |
| Polignac mọi $$2k$$ | **Mở** (sinh đôi là $$k=1$$) |

**Khoảng cách bị chặn** chứng tỏ nguyên tố tạo cụm chặt vô hạn lần. **Sinh đôi** đòi cụm chẵn chặt nhất. Khoảng từ 246 đến 2 nhỏ như tỷ số số nguyên và khổng lồ như rào cản phương pháp. Đừng gộp hai hàng khi nói chuyện hay viết A3.

---

## 6. Toán học quanh bài toán (bản đồ toolkit)

- **Lý thuyết sàng:** sàng Selberg, sàng tổ hợp, GPY, trọng số Maynard.  
- **Nguyên tố trong cấp số cộng:** Bombieri–Vinogradov (trung bình sức GRH); giả thuyết Elliott–Halberstam (phân bố mạnh hơn).  
- **Tuple admissible** và tối ưu đường kính (tuple hẹp đến đâu vẫn admissible?).  
- **Lý thuyết số tính toán:** tìm twin lớn; so heuristic với data.

Không cần master các công cụ để phát biểu conjecture đúng—nhưng nêu tên chúng tránh ảo tưởng “chỉ thử chia đến $$N$$ lớn.”

Bạn có thể làm toán “xung quanh” sinh đôi cả đời (sàng, phân bố, pattern) mà chưa chạm gap 2. Đó là đặc trưng lành mạnh của bài mở lớn. RH ([Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/)) kiểm soát sai số đếm; sinh đôi hỏi cấu trúc cặp ở khoảng cố định—công cụ khác, cùng thế giới “nguyên tố sắp xếp thế nào.”

---

## 7. Polignac, prime tuples, và studio dữ liệu

**Giả thuyết de Polignac:** mọi chẵn dương $$2k$$ xuất hiện vô hạn lần như hiệu hai nguyên tố. Sinh đôi là $$k=1$$. Định lý gap bị chặn cho thấy *ít nhất một* hiệu chẵn trong một tập admissible hữu hạn xuất hiện vô hạn lần; chúng chưa ghim hiệu đó bằng 2.

**Prime tuples.** Tổng quát hơn: mẫu $$n+h_1,\ldots,n+h_m$$ đồng thời nguyên tố với shift admissible $$h_i$$ (admissible: không bị buộc phủ hết thặng dư mod $$p$$ nhỏ). Hardy–Littlewood dự đoán asymptotic. Green–Tao (cấp số cộng nguyên tố dài tùy ý) là chiến thắng khác—tổ hợp cộng tính hơn sàng gap thuần—nhưng cùng thế giới “nguyên tố chứa mẫu phong phú.”

**Studio nhẹ (không bắt buộc):** đếm số cặp sinh đôi tới $$N$$ và so với

$$
c\int_2^N\frac{dx}{(\log x)^2}
$$

(với hằng số twin prime, hoặc chỉ tỷ lệ thô). Mục tiêu **kỷ luật bằng chứng**, không “chứng minh bằng đồ thị.” Cùng tinh thần verification vs proof như [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/).

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Zhang chứng minh sinh đôi.” | Ông chứng minh *một* gap bị chặn, không phải gap 2. |
| “Khoảng cách bị chặn = sinh đôi.” | Bị chặn nghĩa $$\le H$$; sinh đôi cần $$H=2$$. |
| “Bảng chỉ có hữu hạn twin nên giả thuyết sai.” | Bảng hữu hạn; giả thuyết về vô hạn. |
| “Euclid dễ mở rộng sang sinh đôi.” | $$N=P+1$$ không buộc cặp cách 2. |
| “Maynard đã giảm xuống 2.” | Bound vô điều kiện tham chiếu ~246; 2 vẫn mở. |
| “Chen = sinh đôi.” | Chen cho phép $$p+2$$ là tích hai nguyên tố. |

---

## Bài tập

1. Liệt kê năm cặp sinh đôi lớn hơn 100.  
2. Vì sao $$(2,4)$$ không phải cặp sinh đôi? $$(2,3)$$ thì sao?  
3. Phát biểu định lý Zhang bằng lời **không** cần số 70 triệu (“tồn tại chặn hữu hạn…”).  
4. **LO1 (≤300 từ):** giả thuyết sinh đôi, vì sao khó, toán xung quanh (sàng / khoảng cách bị chặn).  
5. So với [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/): phát biểu sơ cấp so với độ sâu kỹ thuật.  
6. **LO6:** sửa tiêu đề giả “Nhà toán học Trung Quốc chứng minh vô hạn cặp sinh đôi (2013).”  
7. Đọc một tường thuật phổ thông về Zhang 2013; liệt kê ba thành phần toán được nêu (sàng, GPY, phân bố cấp số cộng, …).  
8. Stretch: giải thích trong năm dòng vì sao Elliott–Halberstam giúp giảm $$H$$ nhưng vẫn chưa tự động cho $$H=2$$ (khẩu hiệu).

---

## Từ video: chuỗi 2013–2014 bằng khẩu hiệu

Numberphile (Zhang, Maynard), colloquium Maynard, và tường thuật Quanta 2013 tạo một câu chuyện LO1:

1. **GPY** dựng khung sàng *sẽ* cho khoảng cách bị chặn nếu phân bố nguyên tố trong cấp số cộng tốt hơn một chút so với Bombieri–Vinogradov.  
2. **Zhang (2013)** chứng minh mức phân bố yếu đủ mạnh để $$\liminf(p_{n+1}-p_n)\le 70{,}000{,}000$$ (Polymath tối ưu sau đó).  
3. **Maynard (và Tao độc lập)** tinh chỉnh trọng số sàng nhiều chiều; bound giảm mạnh; Polymath hướng tới **$$H=246$$** vô điều kiện.  
4. **Vẫn mở:** khoảng cách $$2$$ (sinh đôi) và **parity barrier**.

**Tình trạng (2026):** giả thuyết sinh đôi **mở**; khoảng cách bị chặn **đã chứng minh**.

---

## Nguồn video (gói math-video-researcher)

Xếp hạng: `research/video-research/Twin_Prime_Conjecture/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *Gaps between Primes*: [YouTube](https://www.youtube.com/watch?v=vkMXdShDdtY).  
2. **Cốt lõi phổ thông** — Numberphile, *Twin Prime Conjecture* (Maynard): [YouTube](https://www.youtube.com/watch?v=QKHKD8bRAro).  
3. **Bài nghiên cứu** — Maynard, *Small Gaps Between Primes*: [YouTube](https://www.youtube.com/watch?v=E-W47F9upkU).  
4. **Tường thuật** — Quanta (2013): [bài](https://www.quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/).  
5. **Bài báo** — Maynard [arXiv:1311.4600](https://arxiv.org/abs/1311.4600).

**Sau video:** khoảng cách bị chặn **đã chứng minh**; sinh đôi ($$H=2$$) **mở**. Không viết “Zhang chứng minh giả thuyết sinh đôi.”

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/Twin_Prime_Conjecture/transcripts/` · trạng thái: `research/video-research/Twin_Prime_Conjecture/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Twin_Prime_Conjecture_vkMXdShDdtY_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Thư mục URL: `research/video-research/Twin_Prime_Conjecture/references.md`.

1. Zhang — bounded gaps (*Annals*, 2014).  
2. Maynard — [arXiv:1311.4600](https://arxiv.org/abs/1311.4600) · [survey arXiv:1910.13450](https://arxiv.org/abs/1910.13450).  
3. Polymath8: http://bit.ly/polymath8  
4. Hardy–Littlewood; Wikipedia — [Twin prime](https://en.wikipedia.org/wiki/Twin_prime).  
5. Numberphile Zhang: https://www.youtube.com/watch?v=vkMXdShDdtY  
6. Numberphile Maynard: https://www.youtube.com/watch?v=QKHKD8bRAro  
7. Maynard colloquium: https://www.youtube.com/watch?v=E-W47F9upkU  
8. Quanta 2013: https://www.quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/  
9. [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), [Euclid]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/). Gói: `research/video-research/Twin_Prime_Conjecture/`.

---

## Hướng đi tiếp

Ứng viên **A3**. Studio: đếm twin tới $$N$$ so heuristic. Essay Maynard: Fields gắn *phương pháp*, không chỉ số $$H$$. Bảng §5 là xương sống—khoanh đúng ô còn mở.
