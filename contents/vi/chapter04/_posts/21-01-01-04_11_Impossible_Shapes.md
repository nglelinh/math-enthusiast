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

**Hình bất khả** (impossible figures) là những hình vẽ trông hợp lý ở từng phần nhưng không thể tồn tại trọn vẹn như một vật thể bình thường trong không gian Euclid ba chiều. Ví dụ: tam giác Penrose, tam giác Reutersvärd (có trước đó), cầu thang bất tận của Escher, và cả một bộ sưu tập "vật thể" đánh lừa cảm nhận chiều sâu. Chúng cho ta thấy tận mắt một ý tưởng hình học sâu sắc: **những điều đúng ở từng vùng nhỏ không nhất thiết ghép lại được thành một vật thể toàn cục**. Ý tưởng này xuất hiện lại trong hình học và tôpô nâng cao mỗi khi một cocycle không phải là coboundary, tức là khi các điều kiện tương thích trên phần chồng nhau không thể thỏa mãn đồng thời.

**Lộ trình:** "bất khả" nghĩa là gì → tam giác Penrose và các dấu hiệu chiều sâu → Escher và những vòng khép kín mâu thuẫn → sự mơ hồ của phép chiếu → mô hình toán học (ghép dán, ý tưởng đối đồng điều) → các ảo giác thị giác liên quan → nhầm lẫn thường gặp, bài tập, hướng đi tiếp.

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

## 1. Từng phần thì ổn, toàn thể thì bất khả

Bản vẽ một hình lập phương là một cách sắp xếp các đường 2 chiều mà ta hiểu thành một vật 3 chiều. Phần lớn bản vẽ nét đều có một vật 3 chiều tương ứng: có một cách gán chiều sâu và các mặt trong không gian sao cho chiếu xuống thì được đúng hình vẽ. **Hình bất khả** là bản vẽ *gợi ra* một vật 3 chiều với các chỗ nối hợp lý ở từng chỗ, nhưng không có khối đa diện rắn nào trong không gian Euclid 3 chiều chiếu xuống thành toàn bộ hình vẽ mà vẫn giữ đúng cấu trúc các mặt và cách che khuất như hình vẽ muốn thể hiện.

"Bất khả" không có nghĩa là không vẽ được; nét mực trên giấy là có thật. Cái bất khả là **việc hiện thực hóa hình vẽ thành một vật thể 3 chiều duy nhất, nhất quán**.

---

## 2. Tam giác Penrose

**Tam giác Penrose** (được Roger Penrose phổ biến; Reutersvärd đã vẽ trước đó) gồm ba thanh dầm nối với nhau vuông góc theo một vòng tam giác. Lấy tay che phần còn lại, mỗi góc trông như một chỗ nối dầm vuông góc hoàn toàn hợp lệ. Nhưng khi đi hết một vòng, cả hình buộc ta phải hiểu các hướng "nhô ra khỏi trang giấy" và "lùi vào trong" một cách mâu thuẫn.

Một cách để thấy mâu thuẫn: gán một hàm độ cao dọc theo các thanh dầm sao cho phù hợp với các chỗ nối trong hình vẽ; đi hết một vòng, độ cao không khớp với lúc xuất phát. Chướng ngại này mang tính toàn cục, nằm trên đường khép kín, trong khi mọi đoạn đường con đều ổn.

Những "tam giác Penrose" thật trong các công viên điêu khắc hoạt động nhờ **phối cảnh cưỡng bức**: từ một góc nhìn duy nhất, hình chiếu khớp với bản vẽ; bước sang một bên, các thanh dầm tách rời nhau. Vật thể 3 chiều đó không phải là một vòng dầm tam giác khép kín, mà là một cấu hình hở có hình chiếu đặc biệt.

---

## 3. Cầu thang Escher và câu chuyện bằng hình

Các bản in thạch bản của M. C. Escher (*Ascending and Descending*, *Waterfall*) biến những cấu hình bất khả thành cả một thế giới kiến trúc. Cầu thang đi lên mãi mà vẫn quay về điểm xuất phát; dòng nước đổ xuống làm quay bánh xe rồi lại chảy ngược lên. Đây là nghệ thuật có tính hình học chặt chẽ: **đồ thị của hình chiếu** chứa một chu trình với độ cao thay đổi không nhất quán.

Escher lấy ý tưởng từ các nhà toán học (Penrose, Coxeter) mà không hề tuyên bố hình học Euclid là sai. Ông minh họa **cách gán chiều sâu vừa có nhiều trạng thái vừa không nhất quán**: hệ thị giác của con người cố ghép các dấu hiệu cục bộ thành một mô hình 3 chiều toàn cục, và thất bại một cách đủ duyên dáng để vẫn đẹp.

---

## 4. Phép chiếu, sự mơ hồ và hình lập phương Necker

Ngay cả vật *có thật* cũng có thể có bản vẽ mơ hồ: **hình lập phương Necker** lật qua lại giữa hai cách hiểu chiều sâu. Hình bất khả còn đi xa hơn: không có cách gán chiều sâu nào khớp với cả hình.

Phép chiếu vuông góc hoặc phép chiếu phối cảnh

$$
\pi:\mathbb{R}^3\to\mathbb{R}^2
$$

làm mất một chiều. Nhiều vật thể khác nhau có cùng một cái bóng. Bản vẽ nét không đủ thông tin để xác định cấu trúc 3 chiều; nhưng khi thêm giả thiết (các mặt phẳng, góc vuông, vật đặc không trong suốt) thì có thể lại không còn nghiệm nào. Thị giác máy tính và các phương pháp giải ràng buộc hình học viết điều này thành hệ phương trình theo tọa độ các đỉnh và quan hệ liên thuộc, đôi khi bị ràng buộc quá mức và vô nghiệm.

---

## 5. Ngôn ngữ toán học cho sự mâu thuẫn

Hãy xem hình bất khả như việc cố ghép các "bản đồ" 3 chiều cục bộ dọc theo những phần chồng nhau (các đoạn dầm, các mặt). Trên mỗi phần chồng, hai bản đồ liên hệ với nhau bằng một phép dời hình hoặc một phép dịch độ cao. Đi quanh một vòng khép kín các phần chồng, hợp của các ánh xạ chuyển tiếp phải là ánh xạ đồng nhất nếu vật thể toàn cục tồn tại. Nếu hợp đó là một phép tịnh tiến chiều sâu khác 0, ta có **một cocycle không tầm thường**, và không có lát cắt (section) toàn cục nào.

Không cần biết đầy đủ về đối đồng điều để nắm bài học:

> **Dữ liệu hình học cục bộ cùng với các quy tắc chuyển tiếp có thể vi phạm điều kiện vòng khép kín, vốn là điều kiện cần để hiện thực hóa toàn cục.**

Cùng một mô thức xuất hiện khi dựng đa tạp từ các bản đồ, khi một phân thớ (bundle) có tôpô không tầm thường, hay khi một hàm độ cao rời rạc trên đồ thị có chu trình không nhất quán. Hình bất khả là phiên bản "bàn cà phê" của các lớp chướng ngại.

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

## Bài tập

1. Che hai góc của bản phác tam giác Penrose; giải thích vì sao góc còn lại trông có vẻ khả thi.
2. Giải thích trong một đoạn văn cách làm tượng hình bất khả bằng phối cảnh cưỡng bức.
3. Hình lập phương Necker khác tam giác Penrose ở điểm nào?
4. Viết không quá 200 từ: bài học cục bộ – toàn cục qua lập luận hàm độ cao đi quanh một vòng.
5. So sánh hình bất khả với dải Möbius: cái nào tồn tại trong $$\mathbb{R}^3$$ đúng như đối tượng được gọi tên?
6. (Mở rộng) Một hệ nhỏ vô nghiệm: ba cạnh có độ cao thay đổi $$+1,+1,+1$$ quanh vòng tam giác dầm.
7. (Mở rộng) Tìm một bức tranh của Escher và chỉ ra đường khép kín có độ cao không nhất quán.
8. Liên hệ [phép lát]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/) (quy tắc khớp cục bộ) với [nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/) trong ba câu.

---

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
