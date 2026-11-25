---
layout: post
title: "Hình bất khả"
chapter: '04'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
---

Hãy nhìn bức tranh *Ascending and Descending* hay *Waterfall* của danh họa M. C. Escher. Từng góc tường vuông vức, từng bậc cầu thang đá, từng dòng nước đổ xuống bánh xe gỗ đều trông vững chãi và hợp lý đến từng milimét. Thế nhưng các tu sĩ cứ leo cầu thang đi lên mãi mà vẫn quay lại đúng bậc ban đầu, còn dòng nước đổ xuống lại chảy ngược lên đỉnh thác. Làm thế nào một bức vẽ có thể **nói dối trắng trợn đến thế mà không hề có lấy một nét mực nào sai**?

Đó là sức hút của **hình bất khả** (impossible figures): tam giác Penrose, tam giác Reutersvärd (có trước đó năm 1934), cầu thang bất tận của Escher. Đằng sau trò đánh lừa thị giác ấy là một trong những nguyên lý sâu sắc nhất của toán học hiện đại: **những điều hoàn toàn nhất quán ở từng vùng nhỏ không nhất thiết ghép lại được thành một vật thể toàn cục**. Cùng một cấu trúc chướng ngại đó xuất hiện trong tôpô đại số và hình học vi phân dưới cái tên *đối đồng điều* (cohomology) — nơi một chu trình khép kín mang theo một "độ lệch" không thể xóa bỏ.

**Lộ trình:** "bất khả" nghĩa là gì → tam giác Penrose và các dấu hiệu chiều sâu → Escher và những vòng khép kín mâu thuẫn → sự mơ hồ của phép chiếu → mô hình toán học (ghép dán, ý tưởng đối đồng điều) → các ảo giác thị giác liên quan → nhầm lẫn thường gặp, hướng đi tiếp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích sự khác nhau giữa **nhất quán cục bộ và khả thi toàn cục** đối với bản vẽ một vật rắn.
- Mô tả **tam giác Penrose** và vì sao từng góc đều hợp lý nhưng cả khối thì không.
- Liên hệ hình bất khả với **phép chiếu** từ 3 chiều xuống 2 chiều và việc gán chiều sâu không rõ ràng.
- Phát biểu bài học toán học bằng ngôn ngữ ghép dán dữ liệu cục bộ (phần nói về đối đồng điều là tùy chọn).
- Phân biệt hình vẽ bất khả với **mặt** không định hướng được (dải Möbius) vốn có tồn tại.
- Tránh những câu khẩu hiệu chưa kiểm chứng như "Escher chứng minh hình học sai" hay "hình bất khả tồn tại trong chiều thứ tư".

**Kiến thức cần có.** Khả năng hình dung không gian 3 chiều cơ bản; ý tưởng về phép chiếu song song. Phần tôpô dải Möbius trong bài Hình học lạ sẽ giúp so sánh.

---

## Kiến thức cần nhớ: Nguyên lý cục bộ – toàn cục và Đối đồng điều là gì?

Trong nhiều ngành toán học bậc cao — từ hình học vi phân, tôpô đại số đến vật lý lý thuyết (lý thuyết trường chuẩn — gauge theory) và thị giác máy tính (dựng hình 3D từ ảnh 2D) — có một câu hỏi lặp đi lặp lại không ngừng: **nếu ta ghép nhiều mảnh lời giải cục bộ hoàn toàn hợp lệ lại với nhau, liệu chúng có khớp thành một lời giải toàn cục không?**

Người tốt nghiệp đại học từng gặp hiện tượng này trong giải tích vectơ: một trường vectơ có thể có $$\mathrm{curl}\, \mathbf{F} = 0$$ ở mọi điểm cục bộ (nên cục bộ luôn viết được thành gradient $$\mathbf{F} = \nabla \phi$$), nhưng nếu đi quanh một lỗ thủng trong miền, tích phân đường $$\oint \mathbf{F}\cdot d\mathbf{r}$$ vẫn khác $$0$$ nên **không tồn tại hàm thế toàn cục $$\phi$$**!

Hình bất khả chính là **phiên bản trực quan bằng mắt thường** của hiện tượng đó. Khi nhìn một bản vẽ 2D, não người làm bài toán giải ngược từ phép chiếu $$\pi:\mathbb{R}^3 \to \mathbb{R}^2$$: tại mỗi góc nối, ta dựng được một mảnh 3D hoàn toàn hợp lệ. Nhưng khi đi hết một vòng khép kín, độ sâu hoặc độ cao không khớp lại với điểm xuất phát. Trong tôpô đại số, đại lượng đo "sự lệch pha không thể sửa khi đi hết một vòng" đó gọi là **lớp đối đồng điều** (cohomology class) — và Roger Penrose từng viết hẳn một bài báo toán học năm 1992 chứng minh hình bất khả là hiện thân cụ thể của nhóm đối đồng điều thứ nhất $$H^1$$!

---

## 1. Từng phần thì ổn, toàn thể thì bất khả

Bản vẽ một hình lập phương là một cách sắp xếp các đường 2 chiều mà ta hiểu thành một vật 3 chiều. Phần lớn bản vẽ nét đều có một vật 3 chiều tương ứng: có một cách gán chiều sâu và các mặt trong không gian sao cho chiếu xuống thì được đúng hình vẽ. **Hình bất khả** là bản vẽ *gợi ra* một vật 3 chiều với các chỗ nối hợp lý ở từng chỗ, nhưng không có khối đa diện rắn nào trong không gian Euclid 3 chiều chiếu xuống thành toàn bộ hình vẽ mà vẫn giữ đúng cấu trúc các mặt và cách che khuất như hình vẽ muốn thể hiện.

"Bất khả" không có nghĩa là không vẽ được; nét mực trên giấy là có thật. Cái bất khả là **việc hiện thực hóa hình vẽ thành một vật thể 3 chiều duy nhất, nhất quán**.

---

## 2. Tam giác Penrose

**Tam giác Penrose** (được Roger Penrose phổ biến năm 1958; nghệ sĩ Thụy Điển Oscar Reutersvärd đã vẽ từ năm 1934) gồm ba thanh dầm nối với nhau vuông góc theo một vòng tam giác. Lấy tay che hai góc, góc còn lại trông như một chỗ nối dầm vuông góc hoàn toàn hợp lệ. Nhưng khi đi hết một vòng, cả hình buộc ta phải hiểu các hướng "nhô ra khỏi trang giấy" và "lùi vào trong" một cách mâu thuẫn.

### Ví dụ ma trận làm từng bước: đại số tuyến tính "bắt quả tang" tam giác Penrose!

Giả sử tại ba góc $$A, B, C$$ ta muốn gán các giá trị chiều sâu (hoặc độ cao) $$h_A, h_B, h_C$$ sao cho đi dọc mỗi thanh dầm đều tiến thêm $$+1$$ đơn vị như hình vẽ gợi ý. Hệ phương trình viết dưới dạng ma trận $$D\mathbf{h} = \mathbf{b}$$:

$$
\begin{pmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ 1 & 0 & -1 \end{pmatrix}
\begin{pmatrix} h_A \\ h_B \\ h_C \end{pmatrix}
=
\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.
$$

Hãy kiểm tra trực tiếp bằng đại số tuyến tính năm nhất:
1. **Cục bộ luôn giải được:** Bỏ đi bất kỳ 1 hàng nào (tức cắt hở tam giác thành đoạn gấp khúc), 2 phương trình còn lại có vô số nghiệm — ví dụ bỏ hàng 3, ta chọn ngay $$(h_A, h_B, h_C) = (0, 1, 2)$$.
2. **Toàn cục vô nghiệm:** Cộng cả 3 hàng của ma trận $$D$$ lại, ta được hàng không $$(0, 0, 0)$$ (do đó $$\operatorname{rank}(D) = 2$$ và mọi vectơ $$\mathbf{y} = D\mathbf{h}$$ trong không gian ảnh $$\operatorname{Im}(D)$$ đều bắt buộc thỏa $$y_1 + y_2 + y_3 = 0$$). Thế nhưng vế phải $$\mathbf{b} = (1, 1, 1)^T$$ lại có tổng $$1 + 1 + 1 = \mathbf{3} \neq 0$$!
3. **Liên hệ thẳng tới đối đồng điều $$H^1$$:** Không gian thương $$\mathbb{R}^3 / \operatorname{Im}(D) \cong \mathbb{R}$$ chính là **nhóm đối đồng điều thứ nhất $$H^1$$** của đồ thị tam giác, và con số $$3 \neq 0$$ là **lớp đối đồng điều** đo mức độ "bất khả" toàn cục của bản vẽ!

Những "tam giác Penrose" thật trong các công viên điêu khắc hoạt động nhờ **phối cảnh cưỡng bức**: từ một góc nhìn duy nhất, hai đầu hở của khối chữ L khổng lồ trùng khít trên võng mạc nên trông như một vòng kín; bước sang một bên vài bước, các thanh dầm lập tức tách rời nhau.

---

## 3. Cầu thang Escher và câu chuyện bằng hình

Các bản in thạch bản của M. C. Escher (*Ascending and Descending*, *Waterfall*) biến những cấu hình bất khả thành cả một thế giới kiến trúc. Cầu thang đi lên mãi mà vẫn quay về điểm xuất phát; dòng nước đổ xuống làm quay bánh xe rồi lại chảy ngược lên. Đây là nghệ thuật có tính hình học chặt chẽ: **đồ thị của hình chiếu** chứa một chu trình với độ cao thay đổi không nhất quán.

Escher lấy ý tưởng từ các nhà toán học (Penrose, Coxeter) mà không hề tuyên bố hình học Euclid là sai. Ông minh họa **cách gán chiều sâu vừa có nhiều trạng thái vừa không nhất quán**: hệ thị giác của con người cố ghép các dấu hiệu cục bộ thành một mô hình 3 chiều toàn cục, và thất bại một cách đủ duyên dáng để vẫn đẹp.

---

## 4. Phép chiếu, sự mơ hồ và hình lập phương Necker

Ngay cả vật *có thật* cũng có thể có bản vẽ mơ hồ: **hình lập phương Necker** lật qua lại giữa hai cách hiểu chiều sâu (mặt nào ở phía trước, mặt nào ở phía sau — hệ phương trình có *nhiều nghiệm*). Hình bất khả còn đi xa hơn: hệ ràng buộc bị *quá xác định* nên **không có nghiệm nào**.

Phép chiếu vuông góc hoặc phép chiếu phối cảnh

$$
\pi:\mathbb{R}^3\to\mathbb{R}^2
$$

làm mất một chiều. Nhiều vật thể khác nhau có cùng một cái bóng. Bản vẽ nét không đủ thông tin để xác định cấu trúc 3 chiều; nhưng khi thêm giả thiết (các mặt phẳng, góc vuông, vật đặc không trong suốt) thì có thể lại không còn nghiệm nào. Thị giác máy tính và các phương pháp giải ràng buộc hình học (như thuật toán gắn nhãn đường Huffman–Clowes) viết điều này thành hệ phương trình theo tọa độ các đỉnh và quan hệ liên thuộc, đôi khi bị ràng buộc quá mức và vô nghiệm.

---

## 5. Ngôn ngữ toán học cho sự mâu thuẫn

Hãy xem hình bất khả như việc cố ghép các "bản đồ" 3 chiều cục bộ dọc theo những phần chồng nhau (các đoạn dầm, các mặt). Trên mỗi phần chồng, hai bản đồ liên hệ với nhau bằng một phép dời hình hoặc một phép dịch độ cao (như độ lệch $$+1$$ trên mỗi cạnh ở Mục 2). Đi quanh một vòng khép kín các phần chồng, hợp của các ánh xạ chuyển tiếp phải là ánh xạ đồng nhất (tổng độ dịch bằng $$0$$) nếu vật thể toàn cục tồn tại. Nếu hợp đó là một phép tịnh tiến chiều sâu khác 0, ta có **một cocycle không tầm thường**, và không có lát cắt (section) toàn cục nào.

### Giải thích: vì sao hình bất khả là minh họa trực quan nhất của đối đồng điều

Để nối từ bức tranh Escher sang công cụ toán học bậc cao mà không bị ngợp thuật ngữ, hãy đi chậm qua 4 bước:

1. **Chia vật thể thành các mảnh cục bộ (phủ mở):** Cắt bản vẽ tam giác Penrose thành 3 góc riêng lẻ $$U_A, U_B, U_C$$. Trên mỗi mảnh riêng, luôn tồn tại vật thể 3D hoàn toàn hợp lệ.
2. **Ghi lại "độ lệch ghép nối" trên phần chồng nhau (1-cocycle):** Tại mỗi đoạn thanh dầm nối hai góc kề nhau, ta ghi nhận độ chênh chiều sâu mà bản vẽ yêu cầu (ví dụ $$+1$$ trên mỗi cạnh).
3. **Thử "khử độ lệch" bằng cách gán độ cao $$h_A, h_B, h_C$$ (coboundary):** Một vật thể 3D nhất quán tồn tại khi và chỉ khi toàn bộ các độ lệch trên cạnh đều viết được thành hiệu $$h_j - h_i$$ (tức $$\mathbf{b} \in \operatorname{Im}(D)$$).
4. **Kiểm tra tổng trên chu trình khép kín (lớp đối đồng điều $$H^1$$):** Tổng các hiệu $$h_j - h_i$$ quanh vòng kín luôn bằng $$0$$. Vì tổng độ lệch của bản vẽ bằng $$3 \neq 0$$, ta gặp một **chướng ngại tôpô toàn cục** — không cách sửa cục bộ nào tại một góc xóa nổi con số $$3$$ đó nếu không cắt đứt vòng kín!

**Kiểm tra nhanh.** Hình lập phương Necker khác tam giác Penrose ở điểm nào trong ngôn ngữ hệ phương trình $$D\mathbf{h} = \mathbf{b}$$? Necker có *nhiều nghiệm* (mơ hồ chiều sâu), còn Penrose *vô nghiệm* (bất khả toàn cục).

Không cần biết đầy đủ về đối đồng điều để nắm bài học:

> **Dữ liệu hình học cục bộ cùng với các quy tắc chuyển tiếp có thể vi phạm điều kiện vòng khép kín, vốn là điều kiện cần để hiện thực hóa toàn cục.**

Cùng một mô thức xuất hiện khi dựng đa tạp từ các bản đồ, khi một phân thớ (bundle) có tôpô không tầm thường (như dải Möbius xoắn một vòng trên đường tròn), hay khi một hàm độ cao rời rạc trên đồ thị có chu trình không nhất quán. Hình bất khả là phiên bản "bàn cà phê" của các lớp chướng ngại.

Các cách hình thức hóa liên quan: hệ phương trình tuyến tính vô nghiệm cho tọa độ các đỉnh; metric đa diện không nhúng được với hình dạng mặt cho trước; phủ phân nhánh và chiều sâu đa trị.

---

## 6. Hình bất khả không phải là gì

- **Không phải** dải Möbius: dải Möbius tồn tại như một tập con của $$\mathbb{R}^3$$ (hoặc như một mặt trừu tượng). Tam giác bất khả thì không tồn tại như vật rắn khép kín mà nó mô tả.
- **Không phải** bằng chứng tự động về chiều cao hơn: đôi khi một phép nhúng vào 4 chiều hiện thực được điều mà 3 chiều không làm được, nhưng mỗi khẳng định như vậy cần một định lý chính xác, không phải một dòng chú thích trên áp phích.
- **Không phải** thất bại của logic: đó là thất bại của *một* bài toán khả thi cụ thể.

So sánh với [những đối tượng hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/) *có* tồn tại và thách thức trực giác bằng chính sự tồn tại của chúng.

---

## 7. Vì sao quan trọng

- **Hình học:** ràng buộc, tính cứng, phép chiếu.
- **Tôpô:** chướng ngại đối với việc ghép dán.
- **Khoa học thị giác:** bộ não suy ra hình 3 chiều từ tín hiệu 2 chiều như thế nào, và suy luận đó hỏng ở đâu.
- **Đồ họa máy tính:** dựng lại hình 3 chiều từ bản phác; phát hiện sự không nhất quán.
- **Sư phạm:** giới thiệu nguyên lý cục bộ – toàn cục một cách trực quan.

Điều thú vị về mặt toán học: hiểu chính xác vì sao một bản vẽ có thể **nói dối mà không có nét nào sai**.

---

## 8. Nhầm lẫn thường gặp

1. "Tam giác Penrose tồn tại đúng như hình vẽ." Nó chỉ tồn tại như hình 2 chiều hoặc trò phối cảnh, không phải như một vật rắn khép kín theo cách hiểu ngây thơ.
2. "Hình bất khả bác bỏ hình học Euclid." Nó chỉ bác bỏ cách diễn giải quá đà về bản vẽ, không bác bỏ Euclid.
3. "Giống như mặt không định hướng được." Đây là hai vấn đề khác nhau: một bên là vật có tồn tại, một bên là hình chiếu không nhất quán của vật được mô tả.
4. "Mọi bản vẽ lạ đều có ý nghĩa toán học sâu sắc." Chiều sâu toán học đến từ các quy tắc cục bộ rõ ràng và một chướng ngại cụ thể.
5. "Cầu thang Escher cao vô hạn." Trong cách diễn giải không nhất quán, độ cao là đa trị, chứ không phải một tòa nhà cao vô hạn.
6. "Sửa một góc là sửa được cả hình." Chướng ngại mang tính toàn cục; sửa cục bộ có thể dời mâu thuẫn sang chỗ khác nhưng không xóa được mâu thuẫn trên vòng nếu không thay đổi kiểu hình.

---

### Những ý chính về hình bất khả (từ phần tìm hiểu video)

- Từng chỗ nối có thể ổn trong khi đồ thị độ sâu/hướng toàn cục có chu trình mâu thuẫn.
- Khác với ảo giác về độ sáng; vấn đề toán học ở đây là **tính nhất quán hình học qua phép chiếu**.
- Cầu thang Escher làm nổi bật một vòng đi lên không nhất quán.

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/impossible-shapes/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — SparksMaths — Building the Impossible Penrose Triangle / Penrose triangle culture: [https://www.youtube.com/watch?v=QpwddAqYzkA](https://www.youtube.com/watch?v=QpwddAqYzkA).
2. **ORIENTATION** — Stand-up Maths impossible geometry demos: [https://www.youtube.com/watch?v=QpwddAqYzkA](https://www.youtube.com/watch?v=QpwddAqYzkA).
3. **CORE culture** — Veritasium — Infinite Pattern (Penrose/Escher-adjacent order) documentaries / talks: [https://www.youtube.com/watch?v=48sCx-wBs34](https://www.youtube.com/watch?v=48sCx-wBs34).
4. **INTUITION** — Necker cube / multistable perception science videos: [https://en.wikipedia.org/wiki/Necker_cube](https://en.wikipedia.org/wiki/Necker_cube).
5. **FOUNDATION** — Projective geometry intro lectures: [https://en.wikipedia.org/wiki/Projective_geometry](https://en.wikipedia.org/wiki/Projective_geometry).
6. **CORE** — Graphics / impossible 3D models from 2D projections: [https://en.wikipedia.org/wiki/Impossible_object](https://en.wikipedia.org/wiki/Impossible_object).

Danh mục URL đầy đủ: `research/video-research/impossible-shapes/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/impossible-shapes/transcripts/` · trạng thái: `research/video-research/impossible-shapes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/impossible-shapes_QpwddAqYzkA_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/impossible-shapes/references.md`.

### Video (lộ trình chính)

1. SparksMaths — Building the Impossible Penrose Triangle / Penrose triangle culture — https://www.youtube.com/watch?v=QpwddAqYzkA
2. Stand-up Maths impossible geometry demos — https://www.youtube.com/watch?v=QpwddAqYzkA
3. Veritasium — Infinite Pattern (Penrose/Escher-adjacent order) documentaries / talks — https://www.youtube.com/watch?v=48sCx-wBs34
4. Necker cube / multistable perception science videos — https://en.wikipedia.org/wiki/Necker_cube
5. Projective geometry intro lectures — https://en.wikipedia.org/wiki/Projective_geometry
6. Graphics / impossible 3D models from 2D projections — https://en.wikipedia.org/wiki/Impossible_object
7. Penrose stairs explainers — https://en.wikipedia.org/wiki/Penrose_stairs
8. Course strange geometry sibling (internal) (LINK).

### Video (tìm thêm / phụ)

9. Optical illusion math museum talks — https://en.wikipedia.org/wiki/Impossible_object

### Bài báo, sách, OCW và web

10. Penrose & Penrose — Impossible objects (classic note culture): https://en.wikipedia.org/wiki/Penrose_triangle
11. Wikipedia — Penrose triangle: https://en.wikipedia.org/wiki/Penrose_triangle
12. Wikipedia — Impossible object: https://en.wikipedia.org/wiki/Impossible_object
13. Wikipedia — Penrose stairs: https://en.wikipedia.org/wiki/Penrose_stairs
14. Wikipedia — Necker cube: https://en.wikipedia.org/wiki/Necker_cube
15. Wikipedia — M. C. Escher: https://en.wikipedia.org/wiki/M._C._Escher

### Trong khóa

16. Liên kết: [Hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/), [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/), [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/), [Lát]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/). Gói: `research/video-research/impossible-shapes/`.

## Hướng đi tiếp

Những đối tượng lạ có tồn tại: [Hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/). Nghịch lý logic: [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/). Quy tắc cục bộ dẫn đến hệ quả toàn cục: [Lát]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/) và [Hiện tượng nảy sinh]({{ site.baseurl }}/contents/vi/chapter04/04_12_Emergence/).

## Video tham khảo

- **Xem trước**: [Building the Impossible - A Penrose Triangle in Geogebra 3D](https://www.youtube.com/watch?v=QpwddAqYzkA) (SparksMaths, tiếng Anh). Dựng tam giác Penrose trong GeoGebra 3D, cho thấy nó chỉ "khép kín" từ một góc nhìn. Nên xem cùng §2.
- [The Infinite Pattern That Never Repeats](https://www.youtube.com/watch?v=48sCx-wBs34) (Veritasium, tiếng Anh). Video này nói về lát gạch Penrose không tuần hoàn, không phải hình bất khả; hữu ích để thấy quy tắc cục bộ quyết định cấu trúc toàn cục (xem thêm bài Lát).
