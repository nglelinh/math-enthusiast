---
layout: post
title: "Dennis Sullivan: Tôpô, Động lực và Hình học (Abel 2022)"
chapter: '08'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

**Dennis Parnell Sullivan** (Đại học Stony Brook; CUNY Graduate Center) nhận **Giải Abel 2022**

> “for his groundbreaking contributions to topology in its broadest sense, and in particular its algebraic, geometric and dynamical aspects.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2022)

Ủy ban mô tả ông liên tục thay đổi cảnh quan của tôpô, dùng các ý tưởng đại số, giải tích, hình học “như một nghệ sĩ bậc thầy thực thụ”. Bài này đặt Sullivan giữa tôpô **và** động lực học; nêu định lý **không có miền lang thang** (no wandering domains) cho ánh xạ hữu tỉ; và so sánh một sự nghiệp “bậc thầy” trọn đời với bản hùng ca của một định lý (Poincaré qua dòng Ricci). Tài liệu: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể đặt Sullivan vào ba mảng: tôpô đại số, tôpô hình học và động lực phức; nêu được định lý không có miền lang thang và thành phần Fatou lang thang là gì; giải thích “cấu trúc hình học trên không gian” như chủ đề thống nhất; so sánh tôpô của cả một đời với bản hùng ca một định lý ([Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)); và tránh việc rút gọn giải Abel 2022 thành một kết quả duy nhất.

**Kiến thức nền.** Ánh xạ liên tục; từ vựng cơ bản của tôpô; ý niệm lặp hàm $$f$$, $$f\circ f$$, $$f^{\circ n}$$. Giải tích phức, ngoài việc biết “có hàm biến phức”, không bắt buộc ở lần đọc đầu.

---

## 1. Tôpô theo nghĩa rộng

Sự nghiệp của Sullivan trải qua lý thuyết phẫu thuật (surgery), đồng luân hữu tỉ, lý thuyết đa tạp, ánh xạ tựa bảo giác, và hệ động lực. Tài liệu của giải Abel nhấn mạnh một tầm nhìn nhất quán: **cấu trúc hình học trên không gian**, dù đó là đa tạp trơn hay một tập Julia dạng fractal.

“Topology in its broadest sense” không phải là lời quảng cáo:

- Công cụ **đại số** (đồng luân, các toán tử đồng điều, mô hình hữu tỉ);  
- Công cụ **hình học** (cấu trúc trên đa tạp, hình học tựa bảo giác);  
- Công cụ **động lực** (phép lặp, tính cứng của các ánh xạ phức).

Rất ít người đi thông thạo cả ba suốt nhiều thập niên. Giải Abel 2022 vinh danh cung đường đó. Citation là lời mời **đừng dựng tường ngăn động lực học ra khỏi toán thuần túy**.

---

## 2. Các chủ đề cột mốc (chọn lọc)

Không có bài báo nào là toàn bộ câu chuyện. Đây là một bản đồ một phần:

### Phẫu thuật và đa tạp

Lý thuyết phẫu thuật hỏi khi nào một đa tạp có thể được sửa thành một đa tạp khác bằng cách cắt và dán các mảnh chuẩn, nối thông tin đồng luân với phân loại hình học. Sullivan có đóng góp trong việc định hình ngôn ngữ của tôpô chiều cao hiện đại.

### Đồng luân hữu tỉ và mô hình đại số

Đồng luân hữu tỉ nghiên cứu các không gian sau khi “bỏ phần xoắn”, thường qua các mô hình đại số (DGA). Cách tiếp cận của Sullivan biến mô hình đại số thành một ngôn ngữ thực dụng cho kiểu đồng luân trên $$\mathbb{Q}$$.

### Tựa bảo giác và cấu trúc hình học

Ánh xạ tựa bảo giác làm méo góc ở mức có kiểm soát: đủ linh hoạt để biến dạng, đủ cứng để cho kết luận hình học. Sullivan dùng chúng như cầu nối giữa giải tích và tôpô.

### Động lực học: không có miền lang thang

Trong động lực phức, việc lặp một ánh xạ hữu tỉ trên mặt cầu Riemann sinh ra tập Fatou (phần có trật tự) và tập Julia (phần hỗn độn). Sullivan chứng minh rằng **ánh xạ hữu tỉ không có miền lang thang**, giải quyết một giả thuyết tồn tại lâu năm và nối động lực phức với tính cứng của tôpô.

---

## 3. Động lực gặp tôpô: không có miền lang thang

Cho $$f:\widehat{\mathbb{C}}\to\widehat{\mathbb{C}}$$ là một ánh xạ hữu tỉ (thương của hai đa thức) tác động trên mặt cầu Riemann. **Tập Fatou** là tập mở lớn nhất mà trên đó họ các phép lặp $$\{f^{\circ n}\}$$ là chuẩn tắc (đồng liên tục trên các tập compact, theo metric của mặt cầu). Các thành phần liên thông của tập Fatou được gọi là **thành phần Fatou**.

**Miền lang thang** sẽ là một thành phần Fatou $$U$$ sao cho các ảnh tiến

$$
U,\; f(U),\; f^{\circ 2}(U),\; \dots
$$

đều phân biệt, không bao giờ tuần hoàn. Sullivan chứng minh rằng miền lang thang **không tồn tại** với ánh xạ hữu tỉ.

### Vì sao đây là một kết quả về tính cứng

Người ta có thể tưởng tượng một vùng mở cứ trôi mãi dưới phép lặp mà không lặp lại. Định lý nói rằng: với ánh xạ hữu tỉ, cuối cùng mọi thành phần Fatou đều tuần hoàn. Tôpô và giải tích phức ràng buộc sự hỗn độn.

Chứng minh dùng **phẫu thuật và biến dạng tựa bảo giác**: tính linh hoạt của giải tích kết hợp với ràng buộc của tôpô. Nếu có miền lang thang, ta dựng được quá nhiều biến dạng độc lập, mâu thuẫn với hiện tượng chiều hữu hạn của không gian moduli các ánh xạ hữu tỉ. (Đây chỉ là mức khẩu hiệu; lập luận thật là một kiệt tác của động lực phức vào thập niên 1980.)

### Đối chiếu với hàm nguyên

Với một số hàm nguyên siêu việt, miền lang thang **có thể** tồn tại. Trường hợp hữu tỉ là đặc biệt. Nói chính xác về lớp ánh xạ là một phần của hiểu biết toán học: đừng nói “mọi ánh xạ phức”.

---

## 4. Tập Julia và “toán học đẹp”

Việc lặp trên mặt cầu sinh ra tập Julia, những bức chân dung fractal hay xuất hiện trong toán phổ thông. Vẻ đẹp là có thật; nhưng định lý thì chặt chẽ hơn nhiều. Kết quả của Sullivan không phải là một bức ảnh; đó là một ràng buộc phân loại trên tập mở, nơi động lực học “hiền lành”.

Trong khóa học, ta nối ảnh Julia với [toán học đẹp]({{ site.baseurl }}/contents/vi/chapter04/), đồng thời nhấn mạnh rằng citation của Abel 2022 nói về **tôpô và động lực học**, không phải về áp phích. Ảnh phổ thông là cánh cửa, không phải citation.

---

## 5. Vì sao đáng giải Abel: sự nghiệp của một bậc thầy

Câu chuyện Fields với một đột phá duy nhất (Poincaré qua dòng Ricci; tính modular và Fermat) nằm khá gần trong chương trình học. Giải Abel của Sullivan là **một cung dài**: ông liên tục đưa ra ngôn ngữ cho phép các bài toán đổi phạm trù: mô hình đại số cho đồng luân, công cụ tựa bảo giác cho hình học, tính cứng cho động lực học.

Hình ảnh “bậc thầy” (virtuoso) là đúng nếu đọc theo nghĩa toán học: tài nghệ ở đây nghĩa là **chuyển kỹ thuật giữa các thể loại**, chứ không chỉ giỏi trong một thể loại.

Một bài kiểm tra thân thiện cho sinh viên: chọn hai trong số {phẫu thuật, đồng luân hữu tỉ, hình học tựa bảo giác, động lực phức} và viết một đoạn về cách một bài toán ở “phương ngữ” này có thể phát biểu lại ở “phương ngữ” kia. Nếu bạn cảm nhận được độ khó của việc dịch, và vì sao cả một đời xây “máy dịch” là điều quan trọng, thì bạn hiểu citation của Abel hơn là chỉ tóm tắt một dòng về định lý không có miền lang thang.

### Chu kỳ của thành phần Fatou (định lý cho ta điều gì)

Một khi miền lang thang bị loại, mọi thành phần Fatou $$U$$ của ánh xạ hữu tỉ đều **tiền tuần hoàn**: một ảnh tiến $$f^{\circ m}(U)$$ là tuần hoàn, và chu kỳ của thành phần rơi vào các kiểu cổ điển của Fatou–Julia và các hậu duệ (lưu vực hút, lưu vực parabolic, đĩa Siegel, vành Herman, với các ràng buộc thêm). Định lý không phân loại hết động lực học; nó **loại bỏ một lớp bệnh lý** để phần phân loại còn lại có thể tiến hành.

Đây là một mẫu hình tầm cỡ giải Abel: tính cứng **dọn dẹp cảnh quan** để các định lý cấu trúc trở nên khả thi. Hãy so với tính cứng kiểu Margulis, dọn sạch các đồng cấu hoang dại, hay tính modular, dọn xem đường cong elliptic nào được phép tồn tại. Khác lĩnh vực, cùng một hình thức logic: ràng buộc trước, phân loại sau.

---

## 6. So với Perelman (cẩn thận)

| | Sullivan (Abel 2022) | Perelman (Fields 2006) |
|--|----------------------|-------------------------|
| Điểm nhấn | Tôpô cả một sự nghiệp và động lực học | Dòng Ricci hoàn tất việc hình học hóa |
| Phong cách | Nhiều cảnh quan, nhiều ngôn ngữ | Hoàn tất chương trình của Hamilton một cách tập trung |
| Khẩu hiệu tiêu biểu | Không có miền lang thang (trong nhiều kết quả) | Hình học hóa ⇒ Poincaré |
| Loại giải thưởng | Abel, cả sự nghiệp | Fields (từ chối) và Clay (từ chối) |

Cả hai đều nối hình học và giải tích với tôpô. Đừng ép người này thành người kia.

---

## 7. Tôpô và hỗn độn như một nghề

Sự nghiệp của Sullivan lập luận rằng phân loại các không gian và phân loại các chuyển động dài hạn không đối lập nhau. Ánh xạ tựa bảo giác, phẫu thuật và tính cứng động lực cùng chia sẻ một thói quen: kiểm soát độ méo hình học cho đến khi kết luận tôpô tự theo sau. “Broadest sense” trong citation là lời mời bỏ những bức tường nhân tạo giữa động lực học và tôpô thuần túy.

**Gợi ý cho seminar.** Chọn một ảnh tập Julia và viết 150 từ nối sự hỗn độn nhìn thấy được với định nghĩa động lực học chính xác (quỹ đạo, tập Julia, tập Fatou), mà không tuyên bố đã chứng minh định lý không có miền lang thang.

---

## 8. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Giải Abel 2022 chỉ nói về tập Julia.” | Tập Julia là hình ảnh phổ thông; citation nói về tôpô theo nghĩa rộng. |
| “Không có miền lang thang cho mọi ánh xạ phức.” | Định lý nói về ánh xạ **hữu tỉ**; một số hàm nguyên thì khác. |
| “Sullivan chỉ là người làm động lực học.” | Động lực học là một nhánh; phẫu thuật, đồng luân hữu tỉ, tôpô hình học là những nhánh khác. |
| “Bậc thầy nghĩa là không sâu.” | Ở đây nghĩa là sâu trên nhiều “phương ngữ” của tôpô. |
| “Giải cho cả sự nghiệp thì không có định lý tiêu biểu.” | Thường có, và thường còn nhiều hơn một. |

---

## Bài tập

1. Hệ động lực bằng phép lặp: một câu.  
2. Vì sao tôpô quan tâm đến việc lặp ánh xạ trên mặt cầu? Không quá 100 từ.  
3. So sánh Sullivan với [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) theo các trục của bảng, bằng lời của bạn.  
4. Đọc một bài phổ thông về Sullivan của giải Abel hoặc Quanta; liệt kê ba lĩnh vực nghiên cứu.  
5. **Không quá 200 từ:** sự nghiệp của một bậc thầy so với một định lý, dùng giải Abel và một ví dụ từ Fields.  
6. Phát biểu cẩn thận miền lang thang là gì, và Sullivan đã chứng minh điều *không* tồn tại nào cho ánh xạ hữu tỉ.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2022: tôpô theo nghĩa rộng, gồm đại số, hình học, động lực.
- Không có miền lang thang; mô hình của Sullivan; sự nghiệp của một bậc thầy.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: bài giảng Abel của Sullivan, Gathering chestnuts… fluid motion: [https://www.youtube.com/watch?v=RRMBRiyNcjI](https://www.youtube.com/watch?v=RRMBRiyNcjI).  
2. **Định hướng**: danh sách phát của giải Abel về Sullivan 2022: [https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw](https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw).  

**Cổng chính thức và tài liệu**

- Abel 2022 Sullivan: https://abelprize.no/abel-prize-laureates/2022  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/sullivan-topology_RRMBRiyNcjI_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2022 Sullivan — https://abelprize.no/abel-prize-laureates/2022  
2. Sullivan Abel lecture — Gathering chestnuts… fluid motion — https://www.youtube.com/watch?v=RRMBRiyNcjI  
3. Abel Prize playlist Sullivan 2022 — https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw  
4. Wikipedia — Dennis Sullivan — https://en.wikipedia.org/wiki/Dennis_Sullivan  
5. Wikipedia — No wandering domain theorem — https://en.wikipedia.org/wiki/No_wandering_domain_theorem  
6. Wikipedia — Rational homotopy theory — https://en.wikipedia.org/wiki/Rational_homotopy_theory  
7. Stony Brook / CUNY culture pages (search Sullivan Abel) — https://www.stonybrook.edu/  
8. Abel popular PDF topology (from laureate page materials) — https://abelprize.no/sites/default/files/2022-03/topolgy_eng.pdf  
9. Abel popular PDF no-wandering — https://abelprize.no/sites/default/files/2022-03/wanderingset_eng.pdf  

1. [Abel 2022](https://abelprize.no/abel-prize-laureates/2022).  
2. Sullivan, *Quasiconformal homeomorphisms and dynamics I…*, Ann. of Math. 1985 (miền lang thang).  
3. Các bài giới thiệu phổ thông (Quanta, PDF của giải Abel); luôn quay lại phát biểu của định lý.  
4. Trong khóa: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/); chương toán học đẹp (về tập Julia, cần cẩn thận).

---

## Hướng đi tiếp

- Seminar về hình ảnh: tập Julia và định lý đi kèm.  
- So tính cứng của Sullivan và của Margulis.  
- Ghi lại một hướng mở trong động lực phức hoặc tôpô hình học vẫn cuốn hút bạn.  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/).

## Video tham khảo

- **Xem trước** — [Dennis Sullivan: Gathering chestnuts of math related to fluid motion](https://www.youtube.com/watch?v=RRMBRiyNcjI) — The Abel Prize, tiếng Anh. Xem trước để nghe chính Sullivan nói về những ý tưởng toán học gắn với chuyển động của chất lỏng.
