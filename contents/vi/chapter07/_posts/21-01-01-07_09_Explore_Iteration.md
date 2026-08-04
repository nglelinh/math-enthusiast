---
layout: post
title: "Studio khám phá: Lặp và ánh xạ Collatz"
chapter: '07'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

Đây là **studio cờ đầu** Mục 7 cho portfolio khám phá seminar (**A5** / **LO5**). Bạn **không** chứng minh giả thuyết Collatz. Bạn **thiết kế thí nghiệm**, **giữ log nghiên cứu**, và **báo cáo điều đã học**—kể cả thất bại, ngõ cụt, định nghĩa đã sửa.

**Chủ đề.** Điều gì xảy ra khi một quy tắc tất định đơn giản được lặp mãi mãi?

**Trang bài toán kèm.** [Collatz Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/) · [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/) · [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) (verification vs proof).

---

## Mục tiêu học tập

- Phát biểu quy tắc **Collatz ($$3n+1$$)** và giả thuyết mở bằng ngôn ngữ chính xác.
- Định nghĩa và tính **total stopping time** (hoặc biến thể ghi rõ: số bước đến 1, đến giá trị nhỏ hơn…).
- Thiết kế ≥2 thí nghiệm có tham số đóng băng (phạm vi $$n$$, thống kê, đồ thị).
- Giữ **log có ngày** với giả thuyết, kết quả, bất ngờ, nhãn (định lý / conjecture / quan sát / heuristic).
- Viết báo cáo ngắn tách **định lý**, **conjecture**, **quan sát số**, **suy đoán**.
- Giải thích vì sao kiểm chứng cực lớn không phải chứng minh (Collatz song song RH).
- Chuyển phương pháp studio sang prompt Mục 7 khác nếu đổi đề (có OK giảng viên).

**Tiên quyết.** Số nguyên, modulo, chương trình ngắn hoặc CAS, vẽ đồ thị.

---

## 1. Toán nền

### 1.1 Ánh xạ

Với số nguyên dương $$n$$:

$$
T(n)=
\begin{cases}
n/2 & \text{nếu }n\text{ chẵn},\\
3n+1 & \text{nếu }n\text{ lẻ}.
\end{cases}
$$

(Một số tài liệu gộp $$(3n+1)/2$$ khi $$n$$ lẻ—**đóng băng quy ước** trong đề xuất, không trộn đếm bước.)

Lặp $$n,T(n),T(T(n)),\ldots$$. **Giả thuyết Collatz:** mọi $$n$$ dương có iterate bằng 1 (tương đương vào chu trình $$4\to 2\to 1\to 4\to\cdots$$).

![Quy tắc Collatz]({{ site.baseurl }}/img/chapter_img/collatz_tree.svg)

*Hình. Một bước của map; conjecture nói về mọi quỹ đạo.*

### 1.2 Stopping times

- **Total stopping time** $$\sigma_\infty(n)$$: số lần áp $$T$$ để đến 1.  
- **Stopping time** $$\sigma(n)$$: số bước đến giá trị **strictly nhỏ hơn** $$n$$.  
- **Maximum excursion:** giá trị lớn nhất trên quỹ đạo trước khi về 1.

Ghi công thức trong code và log.

### 1.3 Vì sao khó (mức studio)

Map trộn co (chia 2) và giãn ($$3n+1$$). Heuristic trung bình gợi ý quỹ đạo thường giảm—nhưng heuristic ≠ chứng minh. Quy tắc tất định; thống kê stopping time vẫn “lởm chởm”. Có kết quả từng phần (mật độ số rơi xuống dưới chính nó; kiểm đến cận khổng lồ)—**trích dẫn**, không bịa.

**Từ gói video/nghiên cứu (slogan bắt buộc khi viết A5).**

- **$$\operatorname{Col}_{\min}(N)$$** = giá trị nhỏ nhất trên quỹ đạo xuôi của $$N$$. Collatz đầy đủ: $$=1$$ với mọi $$N$$ dương (**mở**).  
- **Tao (2019):** hầu hết $$N$$ (mật độ log), $$\operatorname{Col}_{\min}(N)<f(N)$$ với mọi $$f\to\infty$$—**định lý almost-all**, không phải giải Collatz. Trích [arXiv:1909.03562](https://arxiv.org/abs/1909.03562) nếu nhắc.  
- **Syracuse / map tăng tốc** đổi số bước: cố định $$T$$ vs map lẻ trong đề xuất.  
- Hằng số $$\log 3/\log 4\approx 0.7925$$ (dòng Korec)—đọc tùy chọn.

Chi tiết: bài Collatz Ch.1 §4–5 và `research/video-research/collatz/analysis.md`.

### 1.4 Cây ngược

Mọi $$m$$ có preimage $$2m$$; điều kiện thêm cho $$(m-1)/3$$ tùy quy ước $$T$$. Cây số chảy về 1: bề rộng theo độ sâu $$k$$, mẫu modulo—đối tượng thí nghiệm phong phú.

### 1.5 Lặp ngoài Collatz

Logistic $$x\mapsto rx(1-x)$$; Newton; Babylonian căn… Đổi đề thì **giữ cấu trúc portfolio**. Collatz mặc định vì dễ code và thật sự mở.

### 1.6 Verification vs proof

Collatz đã kiểm mọi hạt đến cận cực lớn (trích nguồn tin cậy—cận đổi theo thời gian). Đạo đức song RH: zero cao trên đường tới hạn hỗ trợ niềm tin, không đóng bài toán. **Miền vô hạn không cạn bằng tìm kiếm hữu hạn.**

---

## 2. Cấu trúc portfolio (mốc A5)

| Mốc | Tuần (passport) | Sản phẩm |
|-----|-----------------|----------|
| Đề xuất | W11 | Câu hỏi, định nghĩa, phương pháp, công cụ, tiêu chí (1–2 trang) |
| Log quá trình | W13 | Mục có ngày; thí nghiệm; ngõ cụt |
| Báo cáo cuối | W15 | Tương đương 6–10 trang: phát hiện + giới hạn + câu hỏi tiếp |

**AI.** Hỗ trợ code được nếu disclose; **log thí nghiệm và diễn giải** phải là của bạn.

---

## 3. Conjecture / chứng minh / thí nghiệm

| Nhãn | Ví dụ |
|------|-------|
| **Định lý** | Lũy thừa 2 về 1 sau $$\log_2 n$$ lần chia đôi |
| **Conjecture** | Collatz đầy đủ |
| **Verification** | Kiểm $$n\le N$$ (trích) |
| **Quan sát** | “TB stopping time $$n\le 10^4$$ là …” |
| **Heuristic** | Mô hình nhân trung bình |

**Tiêu chí thành công (tùy chỉnh, phải cụ thể):**

1. Đề xuất được chấp nhận với định nghĩa đóng băng trước khi code lớn.  
2. ≥2 thí nghiệm §5 có hình/bảng.  
3. Log ≥8 mục, ≥2 thất bại.  
4. Báo cáo nêu rõ điều **không** chứng minh.  
5. Một conjecture số: sống/chết/không kết luận.  
6. Đoạn verification vs proof + trích cận tính toán.

Không phải mục tiêu: “chứng Collatz”, “tìm phản ví dụ nổi tiếng không phương pháp”.

---

## 4. Chuẩn log nghiên cứu

**Ngày · Ý định · Hành động · Kết quả · Nhãn · Diễn giải · Bước tiếp.**

Thất bại được tính. Bug off-by-one là sự kiện log, không sửa thầm. Ghi ngôn ngữ, overflow (Python big int vs độ rộng cố định), seed nếu lấy mẫu.

---

## 5. Thí nghiệm

Làm **≥2** trong A–G; sinh viên cờ đầu nên nhắm 3.

### A — Quỹ đạo tay (20–40′)
$$n=1..20$$; bảng bước đến 1. Giả thuyết trước: “lẻ luôn lâu hơn chẵn lân cận.”

### B — Plot stopping time (45–120′)
$$N=200$$ rồi $$10^4$$–$$10^5$$; đánh dấu kỷ lục.

![Phác stopping time]({{ site.baseurl }}/img/chapter_img/collatz_stopping_time.svg)

*Hình. Cartoon stopping time không đều—hãy làm plot thật trong log.*

### C — Mẫu modulo (40–90′)
$$n\bmod 8$$ hoặc $$16$$; so TB stopping time / max. Cẩn correlation ≠ luật; bias nhiều modulo.

### D — Cây ngược (mở rộng, 60–120′)
Số về 1 đúng $$k$$ bước, $$k\le K$$; đếm theo $$k$$; bất ngờ modulo.

### E — Literacy verification (30–45′)
Nguồn tin cậy: Collatz kiểm đến đâu; 3 câu verification vs proof + RH.

### F — Micro-model heuristic (45–90′)
Cartoon: lẻ → $$3n+1$$ rồi chia 2 đến lẻ; ước log-change kỳ vọng; so order-of-magnitude với data; banner “không phải chứng minh”.

### G — Lặp thay thế (nếu đổi đề)
Logistic $$r=4$$; Newton phức—chỉ với OK GV. Cùng chất lượng portfolio.

---

## 6. Mẫu đề xuất

1. **Câu hỏi.** VD: stopping time tăng thế nào với $$n\le N$$? Lớp modulo nào dài hơn?  
2. **Định nghĩa.** $$T$$, stopping time, map Syracuse rút gọn nếu có.  
3. **Phương pháp.** Ngôn ngữ, phạm vi, plot, phần cứng.  
4. **Tiêu chí.** Không “chứng Collatz”; VD plot $$N=10^5$$; hai conjecture số; giết một đoán ngây thơ.  
5. **Rủi ro.** Overflow; off-by-one; bias; p-hacking modulo; code AI không hiểu.  
6. **Disclose AI.**

Nộp đề xuất trước code lớn—tránh reverse-engineer câu hỏi từ plot.

---

## 7. Dàn báo cáo

1. Giới thiệu: phát biểu Collatz; điều không chứng minh.  
2. Định nghĩa và phương pháp.  
3. Thí nghiệm: thiết kế, kết quả, hình.  
4. Conjecture sống/chết dưới *bài kiểm của bạn*.  
5. Giới hạn (phạm vi, bias, bug).  
6. Nối chủ đề khóa học.  
7. Tài liệu + AI disclosure.

**Trọng tâm rubric:** câu hỏi rõ, log chất lượng, tính nhỏ đúng, trung thực về giới hạn—không “định lý Collatz mới”.

---

## 8. Nhầm lẫn thường gặp

1. Kiểm đến $$10^{18}$$ ⇒ Collatz đúng — bằng chứng trên đoạn, không ∀n.  
2. Quy tắc ngẫu nhiên — tất định; thống kê quỹ đạo có thể lởm chởm.  
3. $$3n+1$$ tăng mãi — kết hợp chia 2 thường giảm TB (heuristic).  
4. Đã biết chu trình khác 4–2–1 cho số dương — đừng tuyên bố không trích dẫn.  
5. Khám phá = không chuẩn — studio nghiêm hơn bài tính.  
6. Stopping time “chuẩn quốc tế” — không; lệch định nghĩa → bất đồng giả.  
7. “Tao đã giải Collatz” — Tao 2019 là almost-all / almost-bounded (mật độ log), không phải giả thuyết đầy đủ (xem Ch.1 §5).

---

## 9. Bài tập (khởi động trước đề xuất)

1. Quỹ đạo đầy đủ của $$27$$; đếm bước theo $$T$$ của bạn.  
2. Mọi lũy thừa 2 về 1; số bước đúng.  
3. Không có $$(p,p+2,p+4)$$ nguyên tố trừ $$(3,5,7)$$—và vì sao **không** phải Collatz (tách toolkit studio nguyên tố).  
4. Pseudocode `stopping_time(n)` + chính sách timeout/overflow.  
5. Một giả thuyết falsifiable về stopping time.  
6. Phác đề xuất §1–2 ≤200 từ.

---

## 10. Rubric checkpoint

| ☐ | Đề xuất + định nghĩa đóng băng + tiêu chí |
| ☐ | ≥2 thí nghiệm có hình/bảng |
| ☐ | Log ≥8 mục, ≥2 thất bại |
| ☐ | Verification vs proof + trích dẫn |
| ☐ | Báo cáo có nhãn định lý/conjecture/quan sát |
| ☐ | AI disclosure |
| ☐ | Câu hỏi mở cho việc sau |

---

## 11. Tài liệu và liên kết

Danh mục URL đầy đủ: `research/video-research/collatz/references.md`. **Không** coi video phổ biến là chứng minh.

1. Lagarias overview: https://arxiv.org/abs/2111.02635 · PDF https://arxiv.org/pdf/2111.02635 · SFU http://www.cecm.sfu.ca/organics/papers/lagarias/  
2. Tao almost-all: https://arxiv.org/abs/1909.03562 · PDF https://arxiv.org/pdf/1909.03562 · blog https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/  
3. Tao 2011: https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/  
4. Video chính: https://www.youtube.com/watch?v=094y1Z2wpJg · https://www.youtube.com/watch?v=5mFpVDpKX70 · https://www.youtube.com/watch?v=t1I9uHF9X5Y · https://mathtube.org/lecture/video/notorious-collatz-conjecture · https://www.youtube.com/watch?v=X2p5eMWyaFs · https://terrytao.files.wordpress.com/2020/02/collatz.pdf · https://www.youtube.com/watch?v=k-dtx8s2ehM · https://www.youtube.com/watch?v=Lr6qc_9M0Ks  
5. Video phụ: https://www.youtube.com/watch?v=m4CjXk_b8zo · https://www.youtube.com/watch?v=LqKpkdRRLZw · https://www.youtube.com/watch?v=O2_h3z1YgEU · https://youtu.be/wH141HLD57o · https://www.youtube.com/watch?v=vT4VJyXWHlo · https://www.numberphile.com/videos/uncrackable-the-collatz-conjecture  
6. Web: https://en.wikipedia.org/wiki/Collatz_conjecture · https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/ · https://chamberland.math.grinnell.edu/3x.html · https://dmi.unibas.ch/en/news/details/lecture-in-basel-terence-tao-and-the-notorious-collatz-conjecture/ · https://mathematics.stanford.edu/events/kiddie-colloquium/almost-almost-collatz · https://www.mathematics.pitt.edu/content/note-collatz-conjecture · http://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf · https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x+1AndItsGeneralizations.pdf · https://www.rism.it/rism-channel/2021/riemann-prize-week/the-notorious-collatz-conjecture-terence-tao  
7. [Collatz Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/), [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/), [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Gói: `research/video-research/collatz/`.  
8. Studio khác: tái sử dụng cấu trúc portfolio này.

---

## Hướng tiếp

W11–W13 seminar xoay quanh studio. Mang plot tới lớp; phản hồi nhắm phương pháp, không khoe khoang. Nếu Collatz “dính” tâm lý—đặt hard stop và viết về giới hạn tính toán như một **nội dung** của project, không phải thất bại cá nhân.

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/collatz/`.

**Khẩu hiệu từ gói nghiên cứu**

- Dùng gói Collatz: `research/video-research/collatz/`.
- Tao 2019 almost-all ≠ giải Collatz (vẫn **mở** 2026).

**Thứ tự xem gợi ý**

1. **ORIENTATION** — Veritasium — Collatz: [https://www.youtube.com/watch?v=094y1Z2wpJg](https://www.youtube.com/watch?v=094y1Z2wpJg).  
2. **INTUITION** — Numberphile — UNCRACKABLE Collatz: [https://www.youtube.com/watch?v=5mFpVDpKX70](https://www.youtube.com/watch?v=5mFpVDpKX70).  
3. **FOUNDATION** — Chamberland 3x+1 status Part 1: [https://www.youtube.com/watch?v=t1I9uHF9X5Y](https://www.youtube.com/watch?v=t1I9uHF9X5Y).  
4. **CORE** — Tao Notorious Collatz (mathtube): [https://mathtube.org/lecture/video/notorious-collatz-conjecture](https://mathtube.org/lecture/video/notorious-collatz-conjecture).  
5. **CORE** — Tao Notorious Collatz (YouTube): [https://www.youtube.com/watch?v=X2p5eMWyaFs](https://www.youtube.com/watch?v=X2p5eMWyaFs).  
6. **FRONTIER** — Tao IAS almost-all Collatz: [https://www.youtube.com/watch?v=k-dtx8s2ehM](https://www.youtube.com/watch?v=k-dtx8s2ehM).  

**Cổng chính thức / tài liệu**

- Tao arXiv:1909.03562: https://arxiv.org/abs/1909.03562  
- Lagarias overview arXiv:2111.02635: https://arxiv.org/abs/2111.02635  

Danh mục URL đầy đủ: `research/video-research/collatz/references.md`.

### Transcript & frames (extract flagship)

Transcript caption và unit theo thời gian cho gói Collatz: `research/video-research/collatz/transcripts/` · trạng thái: `research/video-research/collatz/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

**Frame mẫu** (định hướng studio):

![Frame mẫu video Collatz]({{ site.baseurl }}/img/video_research/collatz/5mFpVDpKX70_frame01.jpg)

*Hình. Frame mẫu từ video định hướng Collatz chính (xem pack cho timestamp).*

### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/collatz/references.md`.

1. Veritasium — Collatz — https://www.youtube.com/watch?v=094y1Z2wpJg  
2. Numberphile — UNCRACKABLE Collatz — https://www.youtube.com/watch?v=5mFpVDpKX70  
3. Chamberland 3x+1 status Part 1 — https://www.youtube.com/watch?v=t1I9uHF9X5Y  
4. Tao Notorious Collatz (mathtube) — https://mathtube.org/lecture/video/notorious-collatz-conjecture  
5. Tao Notorious Collatz (YouTube) — https://www.youtube.com/watch?v=X2p5eMWyaFs  
6. Tao IAS almost-all Collatz — https://www.youtube.com/watch?v=k-dtx8s2ehM  
7. Tao arXiv:1909.03562 — https://arxiv.org/abs/1909.03562  
8. Lagarias overview arXiv:2111.02635 — https://arxiv.org/abs/2111.02635  
9. Full bibliography (pack) — research/video-research/collatz/references.md  
10. Quanta Tao Collatz — https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/  
11. Thư mục gói: `research/video-research/collatz/`.

### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/explore-iteration/transcripts/` · trạng thái: `research/video-research/explore-iteration/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/explore-iteration_094y1Z2wpJg_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

