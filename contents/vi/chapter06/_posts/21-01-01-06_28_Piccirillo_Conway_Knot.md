---
layout: post
title: "Piccirillo và nút Conway: Khi ‘bài tập về nhà’ thành Annals"
chapter: '06'
order: 28
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Mùa hè 2018, tại một hội nghị về tôpô chiều thấp, nghiên cứu sinh **Lisa Piccirillo** (Đại học Texas tại Austin) nghe kể về một "bài toán nhỏ dễ thương" liên quan đến **nút Conway**. Đây là một nút có 11 điểm giao, nổi tiếng đến mức sơ đồ của nó được khắc trên cổng Viện Isaac Newton ở Cambridge. Cô chỉ làm bài này vào **buổi tối**. Theo lời cô, cô không dành giờ ban ngày cho nó, vì không coi đó là "toán thật"; nó giống một bài tập về nhà.

Trong **chưa đầy một tuần**, cô có chứng minh: nút Conway **không slice trơn**. Câu hỏi về tính slice trơn của nút này đã làm khó các chuyên gia khoảng **năm mươi năm**. Trong các nút có **không quá 12 điểm giao**, mọi trường hợp khác đã được giải quyết; chỉ còn lại nút Conway. Định lý đã công bố **hoàn tất việc phân loại các nút slice có dưới mười ba điểm giao**.

Khi cô tình cờ kể với nhà tôpô kỳ cựu **Cameron Gordon**, ông hỏi vì sao cô không phấn khích hơn, và nói bài này phải được đăng trên *Annals of Mathematics*. Bài báo ra năm 2020. Khoảng **mười bốn tháng** sau khi nhận bằng tiến sĩ, cô đã có vị trí giảng dạy dài hạn tại MIT.

Bài này biến câu chuyện thành nội dung toán học cho một buổi thảo luận: tính slice, vì sao nút Conway đặc biệt khó, **chuyển qua 0-vết** (0-trace) và **bất biến $$s$$ của Rasmussen**, liên hệ với cấu trúc trơn lạ trong không gian 4 chiều, và cách nói chính xác, tránh thổi phồng. Nên đọc kèm [Donaldson–Seiberg–Witten]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/) và [bài thực hành về chiều thứ tư]({{ site.baseurl }}/contents/vi/chapter07/07_06_Explore_Fourth_Dimension/).

**Nguồn gốc.** Lisa Piccirillo, "The Conway knot is not slice," *Annals of Mathematics* **191** (2020), 581–591; [arXiv:1808.02923](https://arxiv.org/abs/1808.02923) (gửi ngày 8 tháng 8 năm 2018).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa **nút** trong $$S^3$$, và phân biệt **slice trơn** với **slice tôpô**.
- Phát biểu định lý Piccirillo và hai hệ quả của nó (hoàn tất phân loại nút có ít điểm giao; ví dụ đầu tiên về một nút slice tôpô, là đột biến dương của một nút slice, nhưng không slice trơn).
- Giải thích vì sao nút Conway vượt qua được nhiều **vật cản slice** (đa thức Alexander bằng $$1$$; là đột biến dương của nút Kinoshita–Terasaka, vốn slice).
- Trình bày lại **ý tưởng chứng minh**: cùng **0-vết** $$X(K)\cong X(K')$$ ⇒ cùng tính slice; chỉ ra $$s(K')=2\neq 0$$ ⇒ $$K'$$ không slice ⇒ nút Conway không slice.
- Phát biểu **bổ đề nhúng vết** ở mức ý chính: $$K$$ slice ⇔ $$X(K)$$ nhúng trơn được vào $$S^4$$.
- Đặt kết quả vào khoảng cách giữa thế giới trơn và thế giới tôpô ở **chiều bốn** (các cấu trúc trơn lạ trên $$\mathbb{R}^4$$).
- Nói chính xác: thời gian giải ngắn không có nghĩa là bài dễ; bài báo phổ biến khoa học không phải là toàn bộ định lý.

**Kiến thức nền.** Hình dung được "đường tròn, đĩa, quả cầu 4 chiều được nhúng". Không cần giáo trình lý thuyết nút. Phép tính handle được nhắc tên nhưng không cần để theo dõi khung chứng minh.

---

## 1. Nút, quan hệ concordance, và hai loại đĩa

Một **nút** là một đường tròn nhúng trơn trong $$S^3$$ (một vòng kín trong không gian, xét sai khác một phép đồng luân đẳng cấu, tức là biến dạng mà không cắt dây).

Theo nghĩa cổ điển, một nút là tầm thường trong không gian 3 chiều nếu nó là biên của một đĩa nhúng trong $$S^3$$. **Concordance** (Fox) là phiên bản bốn chiều: ta hỏi nút có là biên của một đĩa nhúng trong **quả cầu 4 chiều** $$B^4$$, có biên là $$S^3$$, hay không.

| Khái niệm | Loại đĩa được phép |
|-----------|-------------------|
| **Slice trơn** (các bài báo hiện đại thường chỉ gọi là "slice") | Đĩa nhúng **trơn** $$\Delta\subset B^4$$, $$\partial\Delta=K$$ |
| **Slice tôpô** | Đĩa **phẳng địa phương** theo nghĩa tôpô (cho phép các đĩa "nhăn" kiểu Freedman) |

Có nhiều nút slice khác nút tầm thường, và có nhiều nút slice tôpô nhưng **không** slice trơn. Sự khác biệt này là dấu hiệu, ở chiều thấp, của cùng hiện tượng làm cho đa tạp 4 chiều trơn "hoang dã" hơn đa tạp tôpô; xem §8 và [Donaldson–SW]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/).

**Ý chính.** *Nút slice là nút trở thành "nút tầm thường khi nhìn từ bốn chiều"; nhưng phải nói rõ đĩa có trơn hay không.*

---

## 2. Hồ sơ nút Conway (vì sao đây là trường hợp nhỏ cuối cùng)

| Sự kiện | Chi tiết |
|---------|----------|
| Sơ đồ | **11 điểm giao**; ký hiệu Rolfsen **11n34** |
| Lịch sử | Conway lập bảng nút (khoảng 1970), đầy đủ đến 11 điểm giao |
| Nút anh em | Là **đột biến dương** (positive mutant) của nút **Kinoshita–Terasaka (KT)**; đây là cặp đột biến dương nhỏ nhất |
| Đa thức Alexander | $$\Delta=1$$ (thuộc nhóm nút không tầm thường nhỏ nhất có tính chất này) |
| Slice tôpô | Cả nút Conway và nút KT đều **slice tôpô** (Freedman, thập niên 1980) |
| KT, slice trơn | Dễ chỉ ra là **slice trơn** |
| Conway, slice trơn | **Còn mở cho đến Piccirillo (2018)** |

**Đột biến dương.** Một *mặt cầu Conway* cắt nút tại bốn điểm và chia nút thành hai "tangle". Cắt ra, xoay một tangle bằng một phép đối hợp rồi dán lại, ta được một **đột biến** (mutant). Đột biến dương là đột biến giữ được hướng một cách nhất quán. Phép đột biến bảo toàn một danh sách dài các bất biến 3 chiều (đa thức Alexander, Jones, HOMFLY, Kauffman; thể tích hyperbolic; phủ rẽ nhánh hai lá; …). Một số bất biến hiện đại được *giả thuyết* là bất biến dưới phép đột biến. Vì vậy, nghiên cứu tính slice của **một đột biến dương của nút slice** đặc biệt khó: nhiều vật cản tự triệt tiêu.

**Vì sao $$\Delta=1$$ gây khó.** Các vật cản abel và hầu hết vật cản metabel đều triệt tiêu. Về tính slice tôpô, định lý đĩa của Freedman đã cho câu trả lời; câu hỏi còn lại là về tính **trơn**.

**Phát biểu phân loại (trong bài báo).** Giải quyết nút Conway là hoàn tất phân loại **nút slice dưới 13 điểm giao** (bảng Cha–Livingston). Các bài phổ biến khoa học nói: trong các nút có **không quá 12 điểm giao**, chỉ còn tính slice trơn của nút Conway là chưa biết. Hai cách nói cho cùng một bức tranh.

**Ví dụ đầu tiên (trong bài báo, không phụ thuộc câu chuyện cá nhân).** Piccirillo cho **ví dụ đầu tiên** về một nút đồng thời:

1. không slice trơn,  
2. **slice tôpô**, và  
3. là **đột biến dương của một nút slice**.

Các ví dụ đột biến không slice trước đó (Kirk–Livingston, …) dùng phương pháp metabel, vốn cũng cản trở tính slice *tôpô*. Vì thế chúng không áp dụng được cho những nút đã slice tôpô theo Freedman như nút Conway.

---

## 3. Vì sao các bất biến dùng trực tiếp liên tục thất bại

Hãy coi mỗi công cụ phát hiện tính slice như một dụng cụ có **điểm mù**. Nút Conway nằm đúng ở chỗ giao nhau của các điểm mù đó:

- Là đột biến của một nút slice ⇒ nhiều bất biến 3 chiều và bất biến concordance cho kết quả "trông như slice".  
- $$\Delta=1$$ ⇒ các vật cản đại số cổ điển đều triệt tiêu.  
- Slice tôpô ⇒ các phép thử thuần tôpô không thể cho câu trả lời phủ định.  
- Trên chính sơ đồ nút Conway, bất biến $$s$$ của Rasmussen và các bất biến họ hàng không được biết là cho giá trị đủ để loại trừ trực tiếp (và $$s$$ thường được giả thuyết là triệt tiêu trên những đột biến kiểu này).

Joshua Greene (trích trên Quanta) gọi đây là "nút mà ta không xử lý nổi", một phép thử cho mọi bất biến mới. Mạng nơ-ron của Mark Hughes từng đoán khả năng nút Conway slice là khoảng **50–50**. Đây là giai thoại về độ "cứng đầu" của bài toán, không phải định lý.

**Bài học nghiên cứu.** Khi một đối tượng nổi tiếng như được thiết kế để đánh lừa mọi thước đo chuẩn, hãy **đổi sang một đối tượng khác** vẫn giữ tính chất bốn chiều mà ta quan tâm.

---

## 4. 0-vết và bổ đề chuyển

### 4.1. Định nghĩa

**Vết với khung 0** (0-framed knot trace), gọi tắt là **0-vết**, của nút $$K$$ là đa tạp 4 chiều trơn

$$
X(K) \;=\; B^4 \;\cup\; \text{(2-handle framing 0 gắn dọc $$K$$)}.
$$

Trực giác: lấy quả cầu 4 chiều, gắn thêm một "nắp" đặc dọc theo nút với khung bằng không. Vết **mã hóa nút theo một cách bốn chiều rất mạnh**.

### 4.2. Bổ đề nhúng (kết quả quen thuộc trong ngành; kiểu Kirby–Melvin)

<div class="textbook-lemma" markdown="1">
**Bổ đề (dạng dùng cho thảo luận).**  
Nút $$K$$ slice trơn **khi và chỉ khi** $$X(K)$$ nhúng trơn được vào $$S^4$$.
</div>

*Ý của một chiều.* Nếu $$K$$ là biên của một đĩa trơn trong quả cầu 4 chiều, ta dán quả cầu còn lại với một lân cận của đĩa để dựng một bản sao nhúng của vết trong $$S^4$$. Chiều ngược lại lấy lại đĩa trơn từ phép nhúng vết, bằng cách "tháo" lõi của 2-handle sau khi bỏ điểm đỉnh nón (cần cẩn thận về mặt PL; trơn ở ngoài một điểm).

### 4.3. Cùng vết ⇒ cùng tính slice

<div class="textbook-theorem" markdown="1">
**Hệ quả.** Nếu $$X(K)\cong X(K')$$ như các đa tạp 4 chiều trơn (vi phôi với nhau) thì

$$
K \text{ smoothly slice} \quad\Longleftrightarrow\quad K' \text{ smoothly slice}.
$$
</div>

**Điểm tinh tế quan trọng (trong bài báo).** Nút $$K'$$ như vậy **không cần** *concordant* với $$K$$. Hai nút có cùng vết chỉ chung nhau **tính slice**, không nhất thiết chung lớp concordance. Nhưng thế là đủ để chứng minh một nút không slice.

---

## 5. Dựng nút "sinh đôi" $$K'$$ của Piccirillo

### 5.1. Chiến lược (tóm tắt)

> Bỏ sơ đồ nút Conway sang một bên. Dựng một nút $$K'$$ có cùng vết. Phát hiện $$K'$$ không slice bằng một bất biến hiện đại, mà bất biến này không phát hiện được khi áp dụng trực tiếp lên nút Conway.

### 5.2. Mẫu đối ngẫu được và số tháo nút bằng một

Dựng các nút khác nhau có vết vi phôi là một kỹ thuật cổ điển nhưng ít được dùng: **mẫu đối ngẫu được** (dualizable patterns; Akbulut; Lickorish; Gompf–Miyazaki; Piccirillo viết lại trong các công trình của cô về vết và shake genus). Một trường hợp thuận tiện: với nút có **số tháo nút bằng một**, có một cách dựng tường minh bằng handle và link để tạo nút sinh đôi cùng vết.

Nút Conway có số tháo nút bằng một. Piccirillo áp dụng cách dựng này (biến đổi cẩn thận để sơ đồ gọn) và chỉ ra một nút sinh đôi $$K'$$ cụ thể:

$$
X(C) \;\cong\; X(K').
$$

(Hình 2 và Hình 4–5 trong bài báo là các phép tính handle; để thảo luận, chỉ cần biết nút sinh đôi tồn tại.)

### 5.3. Nhận xét trước đó cùng Miller

Cùng với **Allison Miller**, Piccirillo đã chỉ ra rằng hai nút cùng vết **không nhất thiết** giống nhau đối với mọi bất biến slice. Điều đó cho hy vọng: có thể $$s$$ (hoặc các số hạng hiệu chỉnh trong lý thuyết Floer) "thấy" được $$K'$$, dù không loại trừ được trực tiếp $$C$$.

---

## 6. Loại trừ $$K'$$ bằng bất biến $$s$$ của Rasmussen

### 6.1. $$s$$ là gì (bản đồ khái niệm)

- **Đồng điều Khovanov** là một phạm trù hóa của đa thức Jones (Khovanov, 2000).  
- **Biến dạng Lee** của vi phân cho một dãy phổ từ đồng điều Khovanov đến **đồng điều Lee**.  
- Với mọi nút, đồng điều Lee trên $$\mathbb{Q}$$ có chiều bằng hai, tập trung ở bậc đồng điều $$0$$.  
- **Rasmussen** rút ra một số nguyên $$s(K)$$ từ bậc lượng tử của các phần tử sinh đó.

<div class="textbook-theorem" markdown="1">
**Định lý (Rasmussen).** Nếu $$K$$ slice trơn thì $$s(K)=0$$.
</div>

(Tổng quát hơn, bất biến này cho cận dưới của giống slice trơn; ở đây ta chỉ cần nó bằng không khi nút slice.)

### 6.2. Tính toán cho nút sinh đôi

Piccirillo tính đồng điều Khovanov hữu tỷ của $$K'$$ (bằng chương trình FastKh của Bar-Natan, kiểu Knot Atlas), rồi dùng **song bậc của các vi phân trong dãy phổ** để chỉ ra phần tử sinh ở bậc $$(0,3)$$ còn sống sót. Kết luận:

$$
s(K') \;=\; 2 \;\neq\; 0.
$$

Vậy $$K'$$ **không** slice trơn. Theo hệ quả về cùng vết, nút Conway cũng không slice trơn.

**Nhận xét (trong bài báo).** Với *mọi* nút có cùng 0-vết với nút Conway, bất biến Heegaard Floer **$$\tau$$** chỉ có thể bằng không: $$\tau(K')=0$$. Vậy $$\tau$$ "mù" trên cả họ nút cùng vết này; **$$s$$ thì không**. Đó chính là lý do việc chuyển sang nút sinh đôi có giá trị.

### 6.3. Khung chứng minh

1. **Bổ đề:** slice ⇔ 0-vết nhúng trơn được vào $$S^4$$.  
2. **Dựng:** mẫu đối ngẫu được / số tháo nút bằng 1 ⇒ nút sinh đôi $$K'$$ với $$X(C)\cong X(K')$$.  
3. **Tính:** đồng điều Khovanov + dãy phổ Lee ⇒ $$s(K')=2$$.  
4. **Rasmussen:** $$s\neq 0$$ ⇒ $$K'$$ không slice.  
5. **Chuyển:** nút Conway không slice.

```text
Conway C  ── cùng 0-trace ──►  K'
     │                           │
     │                      s(K') = 2 ≠ 0
     │                           │
     └──── không smoothly slice ◄┘
```

---

## 7. Câu chuyện con người và cách kể cho đúng

| Cách nói trên báo chí | Đọc cẩn thận |
|------------------|--------------|
| "Giải trong chưa đầy một tuần." | Đúng theo lời cô kể, nhưng đó là sau nhiều năm làm việc với *vết*; còn bài toán thì đã mở hàng chục năm. |
| "Cô nghĩ đó là bài tập về nhà." | Đó là tự đánh giá về mức độ "danh giá", không phải độ khó; Gordon là người chỉnh lại đánh giá đó. |
| "Chỉ làm vào buổi tối." | Làm trong thời gian hạn chế không có nghĩa là việc không quan trọng. |
| "Một bài báo làm nên sự nghiệp." | Một kết quả nổi bật, *cộng với* một chương trình nghiên cứu mạch lạc (vết, shake genus, concordance). |

**Chuyên gia thấy gì.** Ô trống cuối cùng trong bảng các nút ít điểm giao là một **phép thử chuẩn** cho các công cụ. Lấp ô đó bằng một phương pháp có thể dùng lại (nút sinh đôi cùng vết + lý thuyết đồng điều hiện đại) là lý do cộng đồng cho rằng bài này xứng đáng đăng trên *Annals*.

**Một tuần đó đo cái gì.** Khi chiến lược "dựng một nút sinh đôi dễ xử lý hơn" đã nằm sẵn trong tay, phần tính toán có thể xong nhanh. **Nghĩ ra chiến lược** mới là phần nghiên cứu.

---

## 8. Vì sao chiều bốn phá vỡ quy luật

### 8.1. Freedman và Donaldson (thập niên 1980)

- **Freedman:** đa tạp 4 chiều tôpô và các đĩa phẳng địa phương linh hoạt đến bất ngờ.  
- **Donaldson:** đa tạp 4 chiều trơn bị **lý thuyết gauge** ràng buộc chặt (instanton; sau này là Seiberg–Witten). Xem [hình học gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/) và [Donaldson–SW]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/).

Kết hợp lại, chúng tạo ra cả một ngành về những đối tượng tồn tại theo nghĩa tôpô nhưng không tồn tại theo nghĩa trơn, trong đó có các nút **slice tôpô nhưng không slice trơn**.

### 8.2. Cấu trúc trơn lạ trên $$\mathbb{R}^4$$

Với mọi số chiều $$n\neq 4$$, mọi đa tạp trơn đồng phôi với không gian Euclid $$\mathbb{R}^n$$ đều vi phôi với cấu trúc trơn chuẩn. Ở **chiều bốn**, có **vô hạn không đếm được** cấu trúc trơn đôi một không vi phôi trên đa tạp tôpô $$\mathbb{R}^4$$ (các **$$\mathbb{R}^4$$ lạ**: Freedman, Donaldson, Casson, Taubes, Gompf…).

Không phải 3, không phải 5, không phải 11: chỉ có **bốn** là ngoại lệ. Tính slice của nút thường được gọi là **công cụ dò ở chiều thấp nhất** cho thế giới cấu trúc lạ đó.

### 8.3. Công cụ của Piccirillo và của Donaldson

| Chương trình | Công cụ dò cấu trúc trơn 4 chiều |
|--------------|----------------|
| Donaldson / SW | Không gian moduli các liên thông / đơn cực trên đa tạp 4 chiều đóng |
| Piccirillo (nút Conway) | Vết của nút + bất biến $$s$$ của Khovanov–Rasmussen |

Cùng loại câu hỏi (nhúng trơn trong chiều 4), nhưng công cụ khác nhau. Khóa học xếp cả hai dưới chủ đề "chiều bốn đặc biệt".

---

## 9. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Chỉnh lại |
|------------|------|-----|
| "Mọi nút có không quá 12 điểm giao từng là bài toán mở." | Sai | Trong các trường hợp nhỏ đó, chỉ còn tính slice *trơn* của nút Conway. |
| "Nút này không slice theo bất kỳ nghĩa nào." | Thiếu | Nó **có** slice tôpô; nó **không** slice trơn. |
| "Cô phát minh lại tôpô 4 chiều trong một tuần." | Nói quá | Cô giải quyết một trường hợp còn sót nổi tiếng bằng một phép quy gọn sắc sảo, dùng các công cụ đã có. |
| "$$s$$ triệt tiêu trên mọi đột biến nên không thể chứng minh." | Nhầm lẫn | Áp dụng trực tiếp lên nút Conway thì $$s$$ vô dụng; trên **nút sinh đôi cùng vết**, $$s(K')=2$$ thì dùng được. |
| "Cùng vết ⇒ cùng nút." | Sai | Hai nút sinh đôi có thể khác nhau (thậm chí không concordant). |
| "Vì chiều 4 kỳ lạ nên mọi bài toán về nút đều vô vọng." | Sai | Hầu hết các nút nhỏ *đã* được phân loại; nút Conway khó, nhưng không có gì huyền bí. |

---

## 10. Liên hệ trong khóa học

| Bài | Liên hệ |
|--------------|-----|
| [Donaldson–SW]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/) | Đa tạp 4 chiều trơn và tôpô; công cụ dò bằng lý thuyết gauge |
| [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/) | Kiểm soát giải tích không gian moduli (chủ đề họ hàng) |
| [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/) | Liên thông sau Donaldson |
| [Bài thực hành chiều 4]({{ site.baseurl }}/contents/vi/chapter07/07_06_Explore_Fourth_Dimension/) | Tọa độ và cấu trúc trơn lạ |
| [Chiều cao]({{ site.baseurl }}/contents/vi/chapter04/04_08_Higher_Dimensions/) | Hình học nhiều chiều $$D$$ (chủ đề khác) |

---

## Bài tập

1. **Định nghĩa (mỗi định nghĩa không quá 80 chữ).** Slice trơn và slice tôpô.  
2. **Vì sao khó?** Nêu ba lý do khiến nút Conway vượt qua các phép thử slice tiêu chuẩn.  
3. **Bổ đề vết.** Phát biểu đặc trưng của tính slice bằng phép nhúng; viết một câu giải thích trực giác cho một chiều.  
4. **Chuyển.** Nếu $$X(K)\cong X(K')$$ và $$s(K')=2$$, vì sao $$K$$ không slice trơn? Viết lập luận trong ba dòng.  
5. **Đột biến.** Đột biến dương là gì, và vì sao nó quan trọng khi nút anh em là slice?  
6. **$$s$$ và $$\tau$$.** Không quá 60 chữ: vì sao có thể cần $$s$$ khi $$\tau=0$$ trên cả họ nút cùng vết?  
7. **Nói chính xác.** Sửa câu: "Một nghiên cứu sinh giải câu đố nút dễ trong một cuối tuần, chứng tỏ tôpô 4 chiều bị đánh giá quá cao."  
8. **Đoạn nối.** Nối câu chuyện này với ý "cấu trúc trơn ở chiều 4 phát hiện được bằng các bất biến tinh tế", mà không khẳng định Piccirillo dùng không gian moduli Yang–Mills.  
9. **Mở rộng.** Xem bài nói của Borcherds (liên kết bên dưới); liệt kê ba định nghĩa ông nhấn mạnh có liên quan đến bài này.

---

## Nguồn video

Dùng để định hướng; các khẳng định mang tính định lý vẫn dựa vào bài báo.

1. **Richard E. Borcherds**, "Is the Conway knot slice? (After Lisa Piccirillo)": [YouTube](https://www.youtube.com/watch?v=XewXN4i5Or4) (khoảng 24 phút).  
2. **Quanta / phổ biến khoa học:** bài tường thuật của Klarreich (không bắt buộc).

---

## Tài liệu tham khảo

1. **Lisa Piccirillo**, “The Conway knot is not slice,” *Ann. of Math.* **191** (2) (2020), 581–591. DOI [10.4007/annals.2020.191.2.5](https://doi.org/10.4007/annals.2020.191.2.5). PDF [Annals](https://annals.math.princeton.edu/2020/191-2/p05).  
2. **arXiv:1808.02923** — cùng paper; HTML [ar5iv](https://ar5iv.labs.arxiv.org/html/1808.02923).  
3. **Erica Klarreich**, “Graduate Student Solves Decades-Old Conway Knot Problem,” *Quanta Magazine*, 19 May 2020 — câu chuyện; đối chiếu (1).  
4. **Jacob Rasmussen**, “Khovanov homology and the slice genus,” *Invent. Math.* **182** (2010) — bất biến $$s$$.  
5. **Allison N. Miller & Lisa Piccirillo**, “Knot traces and concordance,” *Journal of Topology* **11** (2018).  
6. **Lisa Piccirillo**, luận án / tài liệu “Knot traces and the slice genus” (UT Austin).  
7. Bảng sliceness Cha–Livingston (crossings nhỏ).  
8. Liên kết khóa ở §10.  
