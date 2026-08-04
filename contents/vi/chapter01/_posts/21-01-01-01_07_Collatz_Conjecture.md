---
layout: post
title: "Giả thuyết Collatz"
chapter: '01'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

**Giả thuyết Collatz** (còn gọi là bài toán $$3x+1$$) phát biểu cực kỳ sơ cấp và vẫn mở một cách ương ngạnh. Paul Erdős được cho là đã nói toán học có thể chưa sẵn sàng cho những bài toán như vậy; Jeffrey Lagarias gọi nó cực kỳ khó dù bề ngoài đơn giản.

Trong seminar Math Enthusiast, Collatz đóng hai vai: trên trang Chương 1 này, nó là **mẫu bài mở sơ cấp** để luyện LO1 và đạo đức verification ≠ proof; trong [studio Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), nó là đối tượng **A5** mặc định để thí nghiệm có kỷ luật—không phải để “chứng minh Collatz trong portfolio.”

**Lộ trình:** quy tắc → giả thuyết → quỹ đạo và thời gian dừng → kiểm chứng so với chứng minh → toán từng phần → độ khó bằng lời → vai trò khóa học → nhầm lẫn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ánh xạ Collatz $$T$$ và giả thuyết mọi số nguyên dương rơi vào chu trình $$4\to 2\to 1$$.
- Tính quỹ đạo và **thời gian dừng** (total stopping time) cho hạt giống nhỏ; mô tả hành vi “lên–xuống” điển hình.
- Giải thích vì sao kiểm tra máy tới biên cực lớn chỉ là **bằng chứng**, không phải chứng minh.
- Kể một dạng kết quả từng phần: heuristic xác suất; mật độ các số đạt 1; ràng buộc chu trình; survey Lagarias như cửa vào.
- Phát biểu **định lý almost-all của Tao (2019)** ở mức khẩu hiệu và giải thích vì sao **không** phải chứng minh Collatz đầy đủ.
- Phân biệt map chuẩn $$T$$ với dạng **tăng tốc / Syracuse** khi so sánh nguồn.
- Dùng Collatz làm đối tượng **A5** mà không tuyên bố lời giải; phân biệt trang Ch.1 (giải thích) với studio Ch.7 (thí nghiệm).
- Tránh LO6: “đã kiểm tới $$10^{20}$$ nên đúng,” “Tao đã giải Collatz,” “dãy ngẫu nhiên,” tin đồn disproof trên mạng.

**Tiên quyết.** Số nguyên và tính chẵn lẻ. Không cần giải tích; một chút tư duy “lặp” và đồ thị đủ cho studio.

**Liên kết seminar.** **LO1** và **LO5**; [Studio lặp Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/); [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) (verification vs proof); so sơ cấp–độ sâu với [sinh đôi]({{ site.baseurl }}/contents/vi/chapter01/01_06_Twin_Prime_Conjecture/).

---

## 1. Quy tắc

Với số nguyên dương $$n$$, đặt

$$
T(n) =
\begin{cases}
n/2 & \text{nếu } n \text{ chẵn},\\
3n+1 & \text{nếu } n \text{ lẻ}.
\end{cases}
$$

Lặp: $$n,\; T(n),\; T(T(n)),\; \ldots$$

**Ví dụ.** $$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1 \to 4 \to \cdots$$

**Giả thuyết Collatz.** Mọi số nguyên dương cuối cùng đạt chu trình $$4 \to 2 \to 1$$.

Các phát biểu tương đương nói về việc đạt 1, hoặc về việc chu trình duy nhất trong số dương là chu trình tầm thường (tùy biến thể map $$3n+1$$ đầy đủ hay map tăng tốc gộp các bước chia 2).

**Nhiều tên, một bài.** $$3x+1$$, Syracuse, Ulam, Kakutani, Thwaites, Hasse—thường chỉ cùng câu chuyện số dương cổ điển; luôn kiểm map chính xác.

**Ký hiệu nghiên cứu.** $$\operatorname{Col}_{\min}(N)=\inf_{k\ge 0}T^{k}(N)$$; giả thuyết là $$\operatorname{Col}_{\min}(N)=1$$ với mọi $$N$$ dương (ngôn ngữ bài giảng Tao).

**Thời gian dừng.** *Total stopping time* của $$n$$ thường hiểu là số bước tới khi chạm 1 (hoặc chạm chu trình tầm thường)—định nghĩa chính xác nên cố định một lần trong báo cáo A5 của bạn. *Stopping time* đôi khi chỉ số bước tới giá trị nhỏ hơn $$n$$. Hãy nhất quán thuật ngữ trong portfolio.

**Hạt giống 27.** Quỹ đạo của 27 nổi tiếng đi lên cao trước khi về 1; đếm bước là bài tập chuẩn. Hiện tượng “nhỏ mà đi xa” là một lý do trực quan người ta không tin kiểm tra tay vài chục số là đủ.
---

## 2. Vì sao người ta quan tâm

- **Tiếp cận được:** ai cũng thử được bằng giấy hoặc vài dòng code.
- **Độ sâu:** không có chứng minh dù nỗ lực khổng lồ; kết quả từng phần dùng ý tưởng ergodic, xác suất, và tính toán không tầm thường.
- **Văn hóa bài toán mở:** cho thấy khó ≠ phát biểu phức tạp (tương phản ngôn ngữ [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/)).
- **Toán thực nghiệm:** đồ thị thời gian dừng, thống kê thặng dư, cây ngược (inverse tree)—studio seminar lý tưởng.
- **Rèn đạo đức bằng chứng:** cùng bài học với kiểm không điểm zeta trên đường tới hạn.

Collatz là “bài toán cửa”—dễ vào, khó ra—và khóa học cố ý đặt nó cạnh các bài Thiên niên kỷ để bạn thấy phổ phát biểu.

---

## 3. Kiểm chứng không phải chứng minh

Giả thuyết đã được kiểm cho mọi giá trị khởi đầu tới biên **cực lớn**. Các dự án tính toán đã đẩy qua $$2^{68}$$, $$2^{70}$$, $$2^{71}$$, và các mốc liên quan; văn liệu tiến hóa—khi viết A3/A5 hãy trích một survey hoặc bài verification cập nhật (ví dụ dòng Barina và kế tiếp) thay vì nhớ một số magics.

Không phản ví dụ nào được biết trong phạm vi đã kiểm.

Vẫn:

- Phản ví dụ *có thể* nằm ngoài tầm đã kiểm.
- Một quỹ đạo phân kỳ, hoặc một **chu trình lạ** khác $$4\to 2\to 1$$, sẽ phủ định giả thuyết.
- Kiểm **hữu hạn** giá trị khởi đầu không bao giờ kết thúc phát biểu **vô hạn**.

**Cùng đạo đức** với kiểm nhiều không điểm của zeta trên đường tới hạn trong [bài Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/): **bằng chứng mạnh, chưa phải định lý.**

Trong A5, bạn được khuyến khích kiểm và vẽ—nhưng câu kết luận phải phân biệt “trong mẫu của tôi” với “với mọi số nguyên dương.”

---

## 4. Map tăng tốc và Syracuse

Video phổ biến thường dùng $$T$$ đầy đủ. Bài giảng nghiên cứu (Tao, survey Lagarias, Chamberland) hay chuyển sang map trên số **lẻ**:

$$
\operatorname{Syr}(N)=\frac{3N+1}{2^{a(N)}},
$$

với $$2^{a(N)}$$ là lũy thừa cao nhất của $$2$$ chia hết $$3N+1$$ (kết quả lại lẻ). Mỗi bước đúng **một** phép nhân $$3$$—thuận cho thống kê 3-adic. **Cảnh báo seminar:** đếm bước theo $$T$$ và theo $$\operatorname{Syr}$$ khác nhau; cố định quy ước trước khi so sánh số.

Hằng số heuristic / mật độ hay gặp:

$$
\frac{\log 3}{\log 4}\approx 0.7925
$$

(xuất hiện ở dòng Allouche–Korec và heuristic cân bằng nhân 3 với chia 2 trung bình).

---

## 5. Toán từng phần (không đầy đủ)

### 5.1 Dòng mật độ / almost-all (khẩu hiệu)

| Dòng | Khẩu hiệu | Loại mật độ |
|------|-----------|-------------|
| Krasikov–Lagarias | Nhiều $$N\le x$$ đã có $$\operatorname{Col}_{\min}(N)=1$$ | đếm tới $$x$$ |
| Terras | Hầu hết $$N$$ hạ xuống dưới $$N$$ | natural density |
| Allouche / Korec | Hầu hết $$N$$: $$\operatorname{Col}_{\min}(N)<N^\theta$$ ($$\theta$$ tới gần $$\log 3/\log 4$$) | natural density |
| **Tao (2019)** | Hầu hết $$N$$: $$\operatorname{Col}_{\min}(N)<f(N)$$ với **mọi** $$f\to\infty$$ dù chậm | **logarithmic density** |

**Định lý Tao (blog/arXiv).** Với mọi $$f\to\infty$$,

$$
\operatorname{Col}_{\min}(N)<f(N)
$$

với hầu hết $$N$$ theo mật độ log. Ví dụ khẩu hiệu: hầu hết quỹ đạo có min nhỏ hơn $$\log\log\log\log N$$.

**Không phải:** mọi $$N$$ về 1; pure verification; natural density; “video đã giải Collatz.”

Nguồn chuẩn: [arXiv:1909.03562](https://arxiv.org/abs/1909.03562), [blog Tao](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/); định hướng phổ biến: [Quanta](https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/).

### 5.2 Kiến trúc chứng minh (slogan, không bắt chép)

1. Chuyển **Syracuse** trên số lẻ.  
2. Bất thường **3-adic** của lặp.  
3. Biến ngẫu nhiên Syracuse trên $$\mathbb{Z}/3^n\mathbb{Z}$$.  
4. Ổn định hóa luật khi $$n$$ lớn.  
5. Lặp descent almost-sure cục bộ → gần global almost-bounded.  
6. Fourier / characteristic function + **renewal process** (chi tiết trong paper).

Essay LO chỉ cần kết luận Theorem 2 + giả thuyết vẫn mở.

### 5.3 Chu trình, tổng quát, tính toán

- **Chu trình:** trong số dương chỉ $$4\to 2\to 1$$ được biết; âm / map khác có thể khác.  
- **Tổng quát $$mx+1$$:** một số biến thể liên quan undecidability—**không** đồng nhất “Collatz cổ điển đã chứng minh undecidable” (xem Easy Theory trong tài liệu video).  
- **Verification:** pruning cây, lọc modulo—kỹ thuật kỹ sư toán.  
- **Survey Lagarias** ([arXiv:2111.02635](https://arxiv.org/abs/2111.02635)): cửa vào văn liệu.

“Từng phần” ở Collatz mang tính *cấu trúc và mật độ*, không phải công thức đóng thời gian dừng.

---

## 6. Độ khó bằng lời

Map trộn **nhân** ($$3n+1$$) và **chia 2**, phá nhiều bất biến đơn giản. Quỹ đạo đi lang thang không đều; thời gian dừng dao động mạnh theo hạt giống. Không có hàm Lyapunov hiển nhiên giảm *mọi* bước cho *mọi* $$n$$. Các kỹ thuật cho hệ động lực trơn không chuyển dễ sang hybrid nguyên này.

Một cách nói khác: mỗi bước đơn giản; **tổ hợp toàn cục** của vô hạn quỹ đạo thì không. Đó là khoảng cách giữa “quy tắc trẻ em” và “định lý.”

So với [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): ở đó khó vì lớp bài toán và giới hạn thuật toán; ở Collatz khó vì một map cụ thể kháng chứng minh dù kiểm được từng điểm. Hai kiểu “kháng cự” khác nhau—cả hai đều dạy khiêm tốn.

---

## 7. Vai trò trong khóa học: trang bài toán so với studio

| Trang này (Ch.1) | Studio ([Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/)) |
|------------------|---------------|
| Phát biểu, văn hóa, tình trạng | Thí nghiệm, nhật ký, portfolio |
| Giải thích LO1 | Sáng tạo / khám phá LO5 |
| Không bắt buộc code | Khuyến khích code / vẽ |
| Không giải giả thuyết | Không giải giả thuyết—có kỷ luật giả thuyết nhỏ |

**Không** coi A5 là “chứng minh Collatz.” Coi A5 là khám phá có giả thuyết *có thể bác*: ví dụ “thời gian dừng trung bình trên $$[1,N]$$ tăng như …” rồi kiểm bằng dữ liệu. Giả thuyết nhỏ sai vẫn là khoa học tốt; tuyên bố đã giải Collatz thì không.

---

## 8. Biến thể map và cạm bẫy định nghĩa

Văn liệu dùng vài biến thể (xem thêm §4 Syracuse):

- Map đầy đủ $$T$$ như trên.
- Map “tăng tốc” gộp mọi phép chia 2 sau $$3n+1$$; map **Syracuse** trên số lẻ.
- Đôi khi xét số nguyên (có thể âm) hoặc vành khác—chu trình có thể khác.

Khi so sánh đồ thị với bạn bè hoặc paper, **cùng một định nghĩa bước** trước. Đây là lỗi kỹ thuật nhỏ nhưng hay làm lệch số bước.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Đã kiểm tới $$10^{20}$$ nên đúng.” | Chỉ bằng chứng trong phạm vi đó. |
| “Dãy là ngẫu nhiên.” | Tất định hoàn toàn; thống kê có thể trông lộn xộn. |
| “$$3n+1$$ luôn làm tăng.” | Kết hợp với các phép chia 2, quỹ đạo thường hạ—nói heuristic cho chính xác. |
| “Disproof Lean trên mạng đã xong.” | Claim bất thường cần kiểm cộng đồng; giả thuyết vẫn mở trong toán chuẩn (cẩn trọng bug formalization / trò đùa). |
| “A5 = chứng minh Collatz.” | A5 = khám phá có kỷ luật, không giải Millennium-style. |
| “Không có toán xung quanh vì phát biểu dễ.” | Có mật độ, chu trình, heuristic, verification—đọc Lagarias. |
| “Tao đã giải Collatz / almost all = mọi.” | Tao 2019: almost-all / almost-bounded (mật độ log), **không** giả thuyết đầy đủ. |
| “Collatz đã undecidable.” | Một số **tổng quát** liên quan undecidability; Collatz cổ điển vẫn mở—đừng overclaim từ clip phổ biến. |

---

## Bài tập

1. Tính quỹ đạo của 27 tới 1; đếm số bước (ghi rõ map bạn dùng).  
2. Định nghĩa total stopping time trong một câu, cố định thuật ngữ cho A5.  
3. Đưa một lý do verification ≠ proof áp dụng cho Collatz.  
4. **LO1 (≤250 từ):** phát biểu Collatz, vì sao khó, toán xung quanh (heuristic / mật độ / chu trình).  
5. Phác một giả thuyết A5 **có thể bác** bằng biểu đồ (ví dụ về thời gian dừng trung bình).  
6. Đọc abstract một survey Lagarias; liệt kê ba chủ đề con.  
7. **LO6:** sửa câu “Collatz đúng vì máy đã kiểm mọi số cần thiết.”  
8. Stretch: so sánh trong một đoạn Collatz với [sinh đôi]({{ site.baseurl }}/contents/vi/chapter01/01_06_Twin_Prime_Conjecture/): cả hai sơ cấp; tiến bộ từng phần trông khác nhau thế nào?  
9. **Tao hygiene (≤200 từ):** hai câu “Tao đã chứng minh…” và “Tao **không** chứng minh…,” nêu mật độ log và $$\operatorname{Col}_{\min}$$.  
10. **Biến thể map:** tính bốn số lẻ đầu trong quỹ đạo của $$7$$ dưới $$T$$; tính $$\operatorname{Syr}(7)$$; giải thích vì sao số bước khác.
---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh (chưa có). Chi tiết xếp hạng: `research/video-research/collatz/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Veritasium, *The Simplest Math Problem No One Can Solve – Collatz*: [YouTube](https://www.youtube.com/watch?v=094y1Z2wpJg).  
2. **Văn hóa** — Numberphile, *UNCRACKABLE?* (Eisenbud): [YouTube](https://www.youtube.com/watch?v=5mFpVDpKX70).  
3. **Survey** — Chamberland, *The 3x+1 Problem: Status and Recent Work* (Part 1): [YouTube](https://www.youtube.com/watch?v=t1I9uHF9X5Y).  
4. **Bài giảng nghiên cứu** — Tao, *The Notorious Collatz conjecture*: [mathtube](https://mathtube.org/lecture/video/notorious-collatz-conjecture) · [YouTube](https://www.youtube.com/watch?v=X2p5eMWyaFs) · [slides](https://terrytao.files.wordpress.com/2020/02/collatz.pdf).  
5. **Biên giới (tùy chọn)** — Tao @ IAS, *Almost all Collatz Orbits…*: [YouTube](https://www.youtube.com/watch?v=k-dtx8s2ehM) · [arXiv:1909.03562](https://arxiv.org/abs/1909.03562).  
6. **Vệ sinh logic (tùy chọn)** — Easy Theory về wording Veritasium: [YouTube](https://www.youtube.com/watch?v=Lr6qc_9M0Ks).

**Nhắc:** Tao (2019) là định lý **almost-all / almost-bounded** (mật độ log), **không** giải hết giả thuyết. Trạng thái vẫn **mở** (2026).

Transcript caption (để điều hướng, **không** thay nội dung bài) và frame mẫu trong gói:

- `research/video-research/collatz/transcripts/` · `TRANSCRIPT_STATUS.md`

![Bảng quỹ đạo Collatz (frame Numberphile)]({{ site.baseurl }}/img/video_research/collatz/5mFpVDpKX70_frame01.jpg)

*Hình. Frame mẫu Numberphile *UNCRACKABLE?* (~1 phút) — minh họa sư phạm.*

![Mẫu tô màu Collatz]({{ site.baseurl }}/img/video_research/collatz/LqKpkdRRLZw_frame01.jpg)

*Hình. Frame *Collatz in Color* — văn hóa hình ảnh, không phải chứng minh.*

---

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/collatz/references.md`.

### Bài báo và blog tác giả

1. Lagarias — *The 3x+1 Problem: An Overview*: [arXiv:2111.02635](https://arxiv.org/abs/2111.02635) · [PDF](https://arxiv.org/pdf/2111.02635).  
2. Lagarias — survey cổ điển: [SFU](http://www.cecm.sfu.ca/organics/papers/lagarias/); PDF *generalizations*: [Williams](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x+1AndItsGeneralizations.pdf).  
3. Tao — *Almost all Collatz orbits…*: [arXiv:1909.03562](https://arxiv.org/abs/1909.03562) · [PDF](https://arxiv.org/pdf/1909.03562) · [blog](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/).  
4. Tao — blog Collatz 2011: https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/  
5. Chamberland — survey 2003 PDF: http://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf  
6. Verification tính toán (Barina et al. …)—kiểm năm cho cận hiện hành.

### Video (lộ trình chính)

7. Veritasium: https://www.youtube.com/watch?v=094y1Z2wpJg  
8. Numberphile UNCRACKABLE: https://www.youtube.com/watch?v=5mFpVDpKX70 · trang: https://www.numberphile.com/videos/uncrackable-the-collatz-conjecture  
9. Chamberland Part 1: https://www.youtube.com/watch?v=t1I9uHF9X5Y  
10. Tao *Notorious Collatz*: https://mathtube.org/lecture/video/notorious-collatz-conjecture · YouTube: https://www.youtube.com/watch?v=X2p5eMWyaFs · slides: https://terrytao.files.wordpress.com/2020/02/collatz.pdf · listing: https://www.rism.it/rism-channel/2021/riemann-prize-week/the-notorious-collatz-conjecture-terence-tao  
11. Tao IAS almost-all: https://www.youtube.com/watch?v=k-dtx8s2ehM  
12. Easy Theory (đính chính wording): https://www.youtube.com/watch?v=Lr6qc_9M0Ks  

### Video (tìm thêm / phụ)

13. Tipping Point Math: https://www.youtube.com/watch?v=m4CjXk_b8zo  
14. Numberphile Collatz in Color: https://www.youtube.com/watch?v=LqKpkdRRLZw · extra: https://www.youtube.com/watch?v=O2_h3z1YgEU · realtime: https://youtu.be/wH141HLD57o  
15. Lex Clips — Tao Collatz: https://www.youtube.com/watch?v=vT4VJyXWHlo  

### Web / tin

16. Wikipedia: https://en.wikipedia.org/wiki/Collatz_conjecture  
17. Quanta 2019: https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/  
18. Chamberland hub: https://chamberland.math.grinnell.edu/3x.html  
19. Basel news: https://dmi.unibas.ch/en/news/details/lecture-in-basel-terence-tao-and-the-notorious-collatz-conjecture/  
20. Stanford event: https://mathematics.stanford.edu/events/kiddie-colloquium/almost-almost-collatz  
21. Pitt note: https://www.mathematics.pitt.edu/content/note-collatz-conjecture  
22. Study.com (độ tin cậy thấp cho claim nghiên cứu): https://study.com/academy/lesson/history-of-the-collatz-conjecture.html  

### Trong khóa

23. [Studio Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/); [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Gói: `research/video-research/collatz/` (đặc biệt `references.md`).

---

## Hướng đi tiếp

**A5 mặc định.** Đọc trang studio Ch.7, chọn một giả thuyết nhỏ, ghi nhật ký thí nghiệm, và giữ ranh giới “mẫu” vs “mọi $$n$$.” Tùy chọn thay thế studio: logistic map (chaos lite) nếu bạn muốn động lực trơn hơn. Quay lại trang này khi cần ngôn ngữ chuẩn cho phần “tình trạng bài toán mở” trong portfolio.
