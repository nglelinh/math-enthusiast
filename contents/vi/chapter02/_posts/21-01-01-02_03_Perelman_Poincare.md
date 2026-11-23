---
layout: post
title: "Perelman và Giả thuyết Poincaré (Huy chương Fields 2006)"
chapter: '02'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Grigori Perelman** được trao **Huy chương Fields 2006** (và ông đã **từ chối nhận**) vì những đóng góp cho hình học và những hiểu biết mang tính cách mạng về cấu trúc giải tích và hình học của **dòng Ricci** (Ricci flow). Thành tựu gắn với giải thưởng nhất là chứng minh **giả thuyết hình học hóa của Thurston** (geometrization), từ đó suy ra **giả thuyết Poincaré** cổ điển trong 3 chiều. Về sau, cũng công trình đó mang lại cho ông Giải thưởng Thiên niên kỷ của Viện Clay (và ông cũng từ chối).

Nội dung bài:

**Câu hỏi tô pô → đa tạp 3 chiều → dòng Ricci → điểm kỳ dị → phẫu thuật → hình học hóa → Fields (bị từ chối).**

Mục tiêu không phải là dựng lại toàn bộ chứng minh giải tích, mà là hiểu **bài toán hỏi gì**, **vì sao một thế kỷ tô pô lại cần đến một "phương trình truyền nhiệt" hình học**, và **phần toán học nào nằm bên dưới**.

Trong số các câu hỏi về phân loại đa tạp 3 chiều đóng, có câu: mọi đa tạp 3 chiều đóng, đơn liên có đồng phôi với mặt cầu 3 chiều $$S^3$$ không (Poincaré, 1904)? Cách tiếp cận hiện đại cho metric Riemann biến đổi theo **dòng Ricci**
$$\partial_t g_{ij} = -2\operatorname{Ric}_{ij}(g),$$
một phương trình phi tuyến kiểu phương trình truyền nhiệt do **Richard Hamilton** đưa ra (1982). Trong điều kiện thuận lợi, metric trở nên đều hơn; khi xuất hiện điểm kỳ dị, phải hiểu các mô hình của chúng và cắt bỏ chúng bằng **phẫu thuật** (*surgery*).

Perelman đưa vào **phiếm hàm entropy**, lý thuyết về **nghiệm cổ xưa** (ancient solution) và tính chất **không suy biến κ** (κ-noncollapsing), cùng một quy trình **phẫu thuật** chi tiết để tiếp tục dòng Ricci qua các điểm kỳ dị. Loạt bài đăng trên arXiv (2002–2003) hoàn tất chứng minh giả thuyết hình học hóa. Huy chương Fields 2006 (bị từ chối).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu giả thuyết Poincaré và giả thuyết hình học hóa bằng ngôn ngữ thông thường và các thuật ngữ tô pô cơ bản.
- Giải thích dòng Ricci như một quá trình biến đổi hình học của metric, và vì sao người ta so sánh nó với phương trình truyền nhiệt.
- Mô tả sơ lược hiện tượng **thắt cổ chai** (*neck pinch*) buộc phải dùng **phẫu thuật**, và phẫu thuật nhằm mục đích gì.
- Phân biệt **Poincaré** (một trường hợp đặc biệt) với **hình học hóa** (định lý tổng quát).
- Đặt công trình của Perelman vào chương trình của Hamilton và kể tên các bản trình bày chi tiết chuẩn (Kleiner–Lott, Morgan–Tian, …).
- Ghi nhận chính xác rằng Huy chương Fields và Giải Clay đều bị **từ chối**.

**Kiến thức cần có.** Đa tạp, nhóm cơ bản $$\pi_1$$, metric Riemann (tích trong trên không gian tiếp xúc). Không cần biết trước về dòng Ricci; độ cong sẽ được giới thiệu sơ lược trước.

---

## 1. Câu hỏi của Poincaré: phát biểu đơn giản, nhưng rất khó

Năm 1904, Henri Poincaré hỏi (theo ngôn ngữ hiện đại):

> Nếu $$M$$ là một đa tạp 3 chiều đóng có nhóm cơ bản tầm thường, thì $$M$$ có đồng phôi với $$S^3$$ không?

"Đóng" nghĩa là compact và không có biên. "Đơn liên" nghĩa là mọi vòng kín đều co liên tục được về một điểm: $$\pi_1(M)=\{e\}$$. Mặt cầu 3 chiều là tập các vectơ đơn vị trong $$\mathbb{R}^4$$, ví dụ mẫu của một đa tạp 3 chiều đơn liên.

![3-đa tạp đơn liên và 3-cầu]({{ site.baseurl }}/img/chapter_img/poincare_sphere_simply_connected.svg)

*Hình. Câu hỏi của Poincaré: điều kiện $$\pi_1=0$$ có buộc đa tạp phải có tô pô của $$S^3$$ không?*

### Vì sao chiều 3 đặc biệt

- Chiều 2: các mặt đóng được phân loại theo giống; điều kiện đơn liên chỉ để lại mặt cầu 2 chiều.
- Chiều $$\ge 5$$: giả thuyết Poincaré tổng quát được Smale chứng minh (và được hoàn thiện về sau); chiều 4 được Freedman chứng minh trong phạm trù tô pô.
- Chiều **3** là khó nhất: đủ thấp để xuất hiện những hiện tượng "kỳ quặc", nhưng đủ cao để các công cụ cổ điển dùng cho mặt không còn hiệu quả.

Câu hỏi này trở thành một trong **bảy Bài toán Thiên niên kỷ của Viện Clay** (2000).

---

## 2. Giả thuyết hình học hóa của Thurston: một bức tranh lớn hơn

Một nguyên lý mạnh hơn là **giả thuyết hình học hóa của Thurston** (thập niên 1980): mọi đa tạp 3 chiều đóng đều có thể cắt dọc theo các mặt cầu và mặt xuyến cốt yếu thành các mảnh, mỗi mảnh mang một trong **tám hình học thuần nhất** (cầu, Euclid, hyperbolic, và năm hình học khác như $$\mathrm{Nil}$$, $$\mathrm{Sol}$$, các hình học tích, và phủ phổ dụng của $$\mathrm{SL}_2(\mathbb{R})$$).

![Tám hình học (nhãn)]({{ site.baseurl }}/img/chapter_img/geometrization_eight.svg)

*Hình. Tám hình học mẫu của Thurston (chỉ ghi tên).*

**Quan hệ logic.**

$$
\text{Geometrization}
\;\Longrightarrow\;
\text{Giả thuyết Poincaré}.
$$

Nếu $$\pi_1(M)=0$$ thì không thể có một phân tách hình học phức tạp nào tránh được hình học cầu; mô hình đóng, đơn liên duy nhất là mặt cầu, do đó $$M\cong S^3$$.

Chiến lược của thế kỷ XX: chứng minh giả thuyết **lớn hơn** (hình học hóa), và Poincaré sẽ là hệ quả.

---

### Video ngắn 1: Perelman & Giả thuyết Poincaré (Tổng quan)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/perelman-poincare_vi.mp4"></video>
</div>

Video dài khoảng 2 phút 6 giây (có thuyết minh tiếng Việt giọng Algenib): câu hỏi Poincaré 1904, giả thuyết hình học hóa Thurston với 8 mô hình hình học, dòng Ricci có phẫu thuật, và cột mốc từ chối giải Fields 2006.

## 3. Dòng Ricci của Hamilton: một phương trình truyền nhiệt hình học

Năm 1982, Richard Hamilton đưa ra dòng Ricci: làm biến dạng metric $$g(t)$$ theo phương trình

$$
\frac{\partial}{\partial t} g_{ij} = -2 R_{ij},
$$

trong đó $$R_{ij}$$ là độ cong Ricci. Một cách hình dung gần đúng:

- vùng có độ cong Ricci **dương** có xu hướng **co lại**;
- vùng có độ cong Ricci **âm** có xu hướng **giãn ra**;
- metric có xu hướng trở nên **đều** hơn, giống như nhiệt làm cân bằng nhiệt độ.

![Sơ đồ Ricci flow làm mượt]({{ site.baseurl }}/img/chapter_img/ricci_flow_smoothing.svg)

*Hình. Phác thảo: một hình học không đều biến đổi dần về mô hình chuẩn khi dòng còn trơn.*

### Hamilton đạt được gì

- sự tồn tại trong thời gian ngắn và tính duy nhất với metric ban đầu trơn;
- nguyên lý cực đại cho các đại lượng độ cong;
- các định lý hội tụ khi **độ cong Ricci dương**, trong một số bối cảnh đặc biệt;
- một chương trình: chạy dòng Ricci trên đa tạp 3 chiều tổng quát và đọc ra tô pô từ hình học sau thời gian dài.

### Trở ngại: các điểm kỳ dị

Với metric ban đầu tổng quát, dòng Ricci có thể tạo ra **điểm kỳ dị sau thời gian hữu hạn**: độ cong tiến ra vô cùng, thể tích của những vùng nhỏ sụp xuống, và phương trình cho metric trơn không còn ý nghĩa theo nghĩa cổ điển. Nếu không có lý thuyết về điểm kỳ dị và cách đi tiếp, chương trình không phân loại được mọi đa tạp 3 chiều.

> Các điểm kỳ dị trông như thế nào, và làm sao đi tiếp sau chúng?

---

## 4. Phóng to, nghiệm cổ xưa và mô hình thắt cổ chai

Khi độ cong trở nên lớn gần thời điểm kỳ dị $$T$$, người ta **đổi tỉ lệ** metric và thời gian để chuẩn hóa độ cong. Giới hạn thu được (nếu tồn tại) là một **nghiệm cổ xưa**: một dòng Ricci xác định trên một khoảng thời gian kéo dài vô hạn về quá khứ.

Trong 3 chiều, các mô hình điểm kỳ dị dự kiến gồm:

- mặt cầu tròn co lại (một thành phần dạng cầu biến mất);
- **thắt cổ chai**, có mô hình là hình trụ $$S^2\times\mathbb{R}$$ đang co lại;
- các cấu trúc "mũ" hoặc cấu trúc suy biến tinh tế hơn, bị các ước lượng của Perelman ràng buộc.

![Thắt cổ chai và phẫu thuật]({{ site.baseurl }}/img/chapter_img/ricci_surgery_neck.svg)

*Hình. Minh họa thắt cổ chai: độ cong tăng vọt trên một cổ hẹp; phẫu thuật cắt bỏ rồi bịt lại.*

Để hiểu mô hình nào có thể xảy ra, cần tính **không suy biến** và entropy, sao cho giới hạn sau khi đổi tỉ lệ vẫn còn thể tích có nghĩa.

---

### Video ngắn 2: Dòng Ricci, Phóng to & Phẫu thuật

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/perelman-ricci-surgery_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 10 giây (có thuyết minh tiếng Việt giọng Algenib): cơ chế truyền nhiệt hình học của dòng Ricci, phép phóng to tại điểm kỳ dị cho mô hình cổ S² × ℝ, và quy trình phẫu thuật cắt cổ — bịt mũ diễn ra hữu hạn lần.

## 5. Các công cụ mới của Perelman

### 5.1 Entropy và thể tích rút gọn

Perelman định nghĩa các phiếm hàm đơn điệu dọc theo dòng Ricci, nổi tiếng nhất là **entropy** và **thể tích rút gọn** (reduced volume). Tính đơn điệu cho phép kiểm soát toàn cục: các hành vi xấu bị loại trừ vì chúng sẽ làm giảm một đại lượng không thể giảm.

### 5.2 Tính không suy biến κ

Định lý **không suy biến** (đại ý): nếu độ cong bị chặn bởi $$r^{-2}$$ trên một quả cầu bán kính $$r$$ thì thể tích của quả cầu nhỏ hơn cùng tâm bị chặn dưới bởi một bội của $$r^3$$. Điều này ngăn metric co thể tích quá nhanh so với thang độ cong, và là điều kiện thiết yếu để lấy được các giới hạn phóng to trơn.

### 5.3 Ràng buộc trong việc phân loại nghiệm cổ xưa

Nhờ tính không suy biến và entropy, Perelman ràng buộc được các giới hạn cổ xưa trong 3 chiều, từ đó biện minh cho bức tranh hình học (cầu, cổ, mũ) dùng trong phẫu thuật.

### 5.4 Dòng Ricci có phẫu thuật

Khi cổ đã thắt đủ hẹp, người ta **cắt** dọc theo một mặt cầu cắt ngang, bỏ đi phần "sừng" có độ cong lớn, gắn vào một cái mũ chuẩn, và được một đa tạp trơn mới (có thể không liên thông) để chạy tiếp dòng Ricci. Phần kỹ thuật cốt lõi:

- phẫu thuật được xác định tốt và chỉ thay đổi tô pô một cách có kiểm soát;
- trên đa tạp 3 chiều đóng, trong mọi khoảng thời gian hữu hạn chỉ có **hữu hạn** lần phẫu thuật;
- sau thời gian dài, các mảnh còn lại mang những cấu trúc hình học nằm trong danh sách của Thurston.

### 5.5 Biến mất sau thời gian hữu hạn và hành vi dài hạn

Trên một số đa tạp, dòng Ricci (có phẫu thuật) có thể biến mất sau thời gian hữu hạn (thể tích → 0); điều này ứng với các tổng liên thông của những dạng không gian cầu. Trên các đa tạp khác, phân tích hành vi dài hạn cho ra các mảnh hyperbolic và các đa tạp đồ thị (graph manifold), đúng như giả thuyết hình học hóa.

---

### Video ngắn 3: Phiếm hàm Entropy & Tính không suy biến κ

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/perelman-entropy-kappa_vi.mp4"></video>
</div>

Video dài khoảng 57 giây (có thuyết minh tiếng Việt giọng Algenib): vai trò của đại lượng đơn điệu (entropy W, thể tích rút gọn) và định lý không suy biến κ ngăn không gian sụp thể tích khi phóng to.

## 6. Các bài đăng trên arXiv và quá trình kiểm chứng

Ba bài nổi tiếng trên arXiv:

1. *The entropy formula…* (math/0211159, 2002).  
2. *Ricci flow with surgery…* (math/0303109, 2003).  
3. *Finite extinction time…* (math/0307245, 2003).

Các bài này ngắn so với độ sâu của lập luận. Cộng đồng toán học đã viết các bản trình bày chi tiết:

- ghi chú của Kleiner–Lott;
- sách *Ricci Flow and the Poincaré Conjecture* của Morgan–Tian;
- bản trình bày của Cao–Zhu (và các làm rõ sau đó trong tài liệu);
- nhiều khóa giảng trên thế giới.

**Quá trình kiểm chứng**, với các bản viết độc lập kiểm tra kỹ các bài trên arXiv, là một phần trong câu chuyện bài toán Clay được công nhận là đã giải.

![Dòng thời gian]({{ site.baseurl }}/img/chapter_img/perelman_timeline.svg)

*Hình. Một số mốc chọn lọc, từ Poincaré (1904) đến quyết định về Huy chương Fields 2006.*

---

## 7. Đã chứng minh được gì: phát biểu cẩn thận

<div class="textbook-theorem" markdown="1">
**Định lý (Perelman, 2002–2003; các bản chi tiết do những người khác viết).**  
Giả thuyết hình học hóa của Thurston là đúng: mọi đa tạp 3 chiều đóng, định hướng được đều phân tách một cách tự nhiên thành các mảnh hình học thuộc tám kiểu mô hình.
</div>

<div class="textbook-theorem" markdown="1">
**Hệ quả.** Giả thuyết Poincaré là đúng: mọi đa tạp 3 chiều đóng, đơn liên đều đồng phôi với $$S^3$$.
</div>

### Lưu ý cho chính xác

- Định lý **chính** là hình học hóa, không "chỉ là Poincaré".
- Perelman **từ chối** Huy chương Fields (ICM Madrid 2006) và sau đó từ chối Giải thưởng Thiên niên kỷ của Clay.
- Lý thuyết của Hamilton là nền tảng không thể thiếu; Perelman hoàn tất chương trình đó chứ không thay thế nó.
- Tài liệu chuẩn ghi nhận chứng minh thuộc về Perelman, với các bản trình bày chi tiết của những tác giả kể trên, chứ không phải một "bài báo cuối cùng" theo kiểu truyền thống.

---

## 8. Vì sao kết quả này quan trọng hơn một giả thuyết đơn lẻ

- Cho thấy **phương trình đạo hàm riêng hình học phi tuyến** có thể giải một bài toán thuần tô pô ở tầm Bài toán Thiên niên kỷ.
- Entropy, tính không suy biến và phẫu thuật đã định hình lại ngành giải tích hình học.
- Thay đổi cách cộng đồng tiếp nhận lời giải cho các giả thuyết lớn: bài đăng trên arXiv cùng với sự kiểm chứng của cộng đồng có thể khép lại một bài toán Clay.

Liên hệ trong Math Enthusiast: so sánh với các câu chuyện khác về "giải tích chứng minh cấu trúc" (Viazovska dùng dạng modular cho bài toán xếp cầu; Wang dùng phân tích nhiều thang đo cho Kakeya). Một ý lặp lại trong chương: **hình học sâu thường cần đến công cụ từ hệ động lực hoặc giải tích**.

---

## 9. Nhìn lại điều nghịch lý

Tô pô hỏi một câu có/không về tính đồng phôi. Lời giải không dựng một phép đồng phôi cụ thể bằng tay. Thay vào đó:

1. đặt một metric tùy ý lên $$M$$;  
2. cho metric biến đổi theo dòng Ricci có phẫu thuật;  
3. đọc ra tô pô từ phân tách hình học xuất hiện.

Như vậy, **phân loại tô pô** đạt được bằng cách **quan sát hình học biến đổi theo thời gian**.

$$
\text{tôpô của } M
\quad\longleftrightarrow\quad
\text{Ricci flow thời gian dài của metric trên } M.
$$

---

## Hiểu lầm thường gặp (kiểm tra thông tin)

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Ông chỉ chứng minh Poincaré, không chứng minh hình học hóa." | **Sai** | Hình học hóa là định lý chính; Poincaré là hệ quả. |
| "Ông đã nhận Huy chương Fields." | **Sai** | Ông từ chối (2006). |
| "Dòng Ricci luôn hội tụ êm, không cần phẫu thuật." | **Sai** | Trong trường hợp tổng quát, phẫu thuật là thiết yếu. |
| "Chứng minh không cần đến lý thuyết có trước." | **Sai** | Nó hoàn tất chương trình của Hamilton. |
| "Giả thuyết Poincaré ở mọi số chiều đều còn mở cho đến Perelman." | **Sai** | Các chiều cao hơn phần lớn đã được giải sớm hơn; chiều 3 là trường hợp khó nổi tiếng. |

---

## Thử thách và mở rộng

1. **Nhóm cơ bản.** Vì sao điều kiện $$\pi_1=0$$ loại bỏ các mặt xuyến cốt yếu trong bức tranh hình học hóa (giải thích sơ lược)?  
2. **Đổi tỉ lệ.** Nếu nhân độ dài với $$\lambda$$ thì độ cong và thời gian của dòng phải đổi tỉ lệ thế nào?  
3. **Tô pô của phẫu thuật.** Khi cắt một cổ dạng $$S^2$$ rồi bịt lại, nhóm $$\pi_1$$ của các thành phần thay đổi ra sao?  
4. **Tám hình học.** Chọn hai hình học không có độ cong hằng ($$\mathrm{Nil}$$, $$\mathrm{Sol}$$) và tìm một tính chất phân biệt chúng với $$H^3$$.  
5. **Kiểm chứng.** Vì sao một bài đăng 40 trang có thể cần cả một cuốn sách ghi chú 500 trang?

---

## Bài tập

1. **Khởi động.** Giải thích khái niệm "đơn liên" bằng cách so sánh các vòng kín trên mặt cầu và trên mặt xuyến.  
2. **Định nghĩa.** Viết định nghĩa trực quan cho: đa tạp đóng; độ cong Ricci (sơ lược); thời điểm kỳ dị của dòng Ricci.  
3. **Logic.** Chứng minh bằng lời: hình học hóa kéo theo Poincaré, với giả thiết rằng đa tạp 3 chiều hình học đóng, đơn liên duy nhất là mặt cầu.  
4. **So sánh với phương trình truyền nhiệt.** Nêu hai điểm giống và một điểm khó hơn (tính phi tuyến / điểm kỳ dị).  
5. **Trục thời gian.** Đặt Hamilton (1982), Thurston, Perelman (2002–03), ICM 2006 lên một trục thời gian và chú thích.  
6. **Đọc tài liệu nghiên cứu.** Mở arXiv:math/0211159; chỉ đọc hai trang đầu của phần mở đầu; liệt kê ba công cụ mà Perelman nói sẽ dùng.  
7. **Ghi nhận công lao.** Viết một đoạn mô tả quan hệ giữa đóng góp của Hamilton và của Perelman mà không xem nhẹ bên nào.

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Perelman_Poincare/`. Tài liệu gốc: ba bài của Perelman trên arXiv.

**Thứ tự xem gợi ý**

1. Numberphile *Poincaré Conjecture*: [YouTube](https://www.youtube.com/watch?v=GItmC9lxeco).  
2. Numberphile *Ricci Flow*: [YouTube](https://www.youtube.com/watch?v=hwOCqA9Xw6A).  
3. Tổng quan của Aleph 0: [YouTube](https://www.youtube.com/watch?v=PwRl5W-whTs).  
4. Đọc trên arXiv: [math/0211159](https://arxiv.org/abs/math/0211159) · [math/0303109](https://arxiv.org/abs/math/0303109) · [math/0307245](https://arxiv.org/abs/math/0307245).

**Nhắc lại:** giả thuyết Poincaré trong 3 chiều **đã được chứng minh**. Giải Fields và Giải Clay **bị từ chối**. Ghi nhận công lao của cả Hamilton và Perelman.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Perelman_Poincare/transcripts/` · trạng thái: `research/video-research/Perelman_Poincare/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Perelman_Poincare_GItmC9lxeco_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Perelman_Poincare/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=GItmC9lxeco  
2. https://www.youtube.com/watch?v=hwOCqA9Xw6A  
3. https://www.youtube.com/watch?v=PwRl5W-whTs  
4. https://www.youtube.com/watch?v=7eJleW0JcKg  
5. https://arxiv.org/abs/math/0211159  
6. https://arxiv.org/abs/math/0303109  
7. https://arxiv.org/abs/math/0307245  
8. https://terrytao.wordpress.com/2008/04/01/285g-lecture-2-the-ricci-flow-approach-to-the-poincare-conjecture/  
9. https://www.claymath.org/resource/ricci-flow-and-the-poincare-conjecture/  
10. https://www.claymath.org/millennium-problems/poincare-conjecture/  
11. https://www.numberphile.com/videos/poincar-conjecture  
12. https://www.numberphile.com/videos/ricci-flow  
13. https://en.wikipedia.org/wiki/Poincar%C3%A9_conjecture  
14. https://en.wikipedia.org/wiki/Grigori_Perelman  
15. https://math.berkeley.edu/~lott/ricciflow/perelman.html  
16. https://en.wikipedia.org/wiki/Ricci_flow  
17. https://en.wikipedia.org/wiki/Geometrization_conjecture  

### Bộ tư liệu nghiên cứu

18. Bộ tư liệu của khóa học: `research/video-research/Perelman_Poincare/`.

1. **G. Perelman** (2002). *The entropy formula…*. [arXiv:math/0211159](https://arxiv.org/abs/math/0211159).  
2. **G. Perelman** (2003). *Ricci flow with surgery…*. [arXiv:math/0303109](https://arxiv.org/abs/math/0303109).  
3. **G. Perelman** (2003). *Finite extinction time…*. [arXiv:math/0307245](https://arxiv.org/abs/math/0307245).  
4. **R. S. Hamilton** (1982). Three-manifolds with positive Ricci curvature.  
5. **W. P. Thurston.** Chương trình hình học hóa / các ghi chú về đa tạp 3 chiều.  
6. **J. Morgan & G. Tian.** *Ricci Flow and the Poincaré Conjecture*.  
7. **B. Kleiner & J. Lott.** Ghi chú về các bài của Perelman.  
8. **H.-D. Cao & X.-P. Zhu.** Bản trình bày (nên đọc kèm các làm rõ sau đó trong tài liệu).  
9. **Clay Mathematics Institute.** Giải thưởng Thiên niên kỷ — Poincaré.  
10. **IMU / ICM 2006.** Huy chương Fields 2006 (Perelman từ chối).  

*Ghi chú.* Các thông tin lịch sử và việc ghi nhận công lao theo các nguồn chuẩn (arXiv; Clay/IMU; các bản trình bày lớn). Các hình là minh họa sư phạm, không phải mô phỏng tính toán dòng Ricci.

---

## Hướng đi tiếp

- Xem lại phần **Các bài toán lớn** nếu khóa học có bàn rộng hơn về các Bài toán Thiên niên kỷ.  
- So sánh với câu chuyện **chứng minh có máy tính hỗ trợ** (bốn màu) và **công thức chính xác** (bài toán xếp cầu của Viazovska).  
- Bước kỹ thuật tiếp theo nếu muốn đi sâu: nguyên lý cực đại cho tensor của Hamilton, rồi công thức entropy của Perelman.  
- Ghi lại một câu hỏi cụ thể bạn vẫn còn thắc mắc; đặt được câu hỏi tốt là một phần của việc làm toán.

## Video tham khảo

- **Xem trước:** [Poincaré Conjecture - Numberphile](https://www.youtube.com/watch?v=GItmC9lxeco) — Numberphile, tiếng Anh. Giới thiệu giả thuyết Poincaré bằng hình ảnh trực quan; nên xem trước khi đọc bài.
- [Ricci Flow - Numberphile](https://www.youtube.com/watch?v=hwOCqA9Xw6A) — Numberphile, tiếng Anh. Giải thích ý tưởng của dòng Ricci; nên xem sau khi đã nắm ý chính của bài.
- [Poincare Conjecture and Ricci Flow | A Million Dollar Problem in Topology](https://www.youtube.com/watch?v=PwRl5W-whTs) — Aleph 0, tiếng Anh. Xem thêm sau hai video trên; tổng quan về giả thuyết Poincaré và dòng Ricci.
