---
layout: post
title: "Hình bất khả"
chapter: '04'
order: 11
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
---

**Hình bất khả** trông nhất quán địa phương nhưng không thể tồn tại toàn cục như vật thể thông thường trong không gian Euclid 3D—tam giác Penrose, tam giác Reutersvärd sớm hơn, cầu thang Escher bất tận, và cả phòng trưng bày “vật thể” đánh lừa tri giác chiều sâu. Chúng làm hữu hình một chủ đề hình học sâu: **chân lý địa phương không nhất thiết dán được thành đối tượng toàn cục**. Chủ đề đó tái xuất trong hình học và tôpô nâng cao mỗi khi cocycle không phải coboundary—điều kiện nhất quán trên phần chồng.

**Lộ trình:** “bất khả” nghĩa là gì → tam giác Penrose và tín hiệu chiều sâu → Escher và chu trình mâu thuẫn → mơ hồ chiếu → mô hình toán (gluing, ý cohomology) → nghịch lý thị giác liên quan → nhầm lẫn, bài tập, hướng đi tiếp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích **nhất quán địa phương vs khả thi toàn cục** cho bản vẽ vật rắn.
- Mô tả **tam giác Penrose** và vì sao mỗi góc ổn nhưng cả khối thì không.
- Nối hình bất khả với **chiếu** từ 3D xuống 2D và gán chiều sâu mơ hồ.
- Phát biểu đạo đức toán bằng ngôn ngữ dán dữ liệu địa phương (slogan cohomology tùy chọn).
- Phân biệt hình vẽ bất khả với **mặt** không định hướng (Möbius) có tồn tại.
- Tránh “Escher chứng minh hình học sai” và “hình bất khả tồn tại ở chiều thứ tư” như slogan chưa kiểm.

**Kiến thức cần có.** Hình dung 3D cơ bản; ý chiếu song song. Tôpô dải Möbius từ hình học lạ giúp tương phản.

---

## 1. Địa phương ổn, toàn cục bất khả

Bản vẽ lập phương là sắp xếp đường 2D ta diễn giải như vật 3D. Hầu hết bản vẽ đường chấp nhận hiện thực 3D: tồn tại chiều sâu và mặt trong không gian chiếu thành hình vẽ. **Hình bất khả** là bản vẽ *gợi* vật 3D với khớp nối địa phương hợp lý—song không có vật đa diện rắn trong không gian Euclid 3D chiếu thành cả hình trong khi tôn trọng cấu trúc mặt và che khuất dự định.

Bất khả không phải mực không vẽ được; mực phẳng và có thật. Bất khả là **khả năng hiện thực như một thân 3D mạch lạc duy nhất**.

---

## 2. Tam giác Penrose

**Tam giác Penrose** (phổ biến hóa bởi Roger Penrose; Reutersvärd dự báo) cho ba dầm gặp vuông góc trong chu trình tam giác. Mỗi góc, che bằng tay, trông như khớp dầm vuông hợp pháp. Cả hình buộc định hướng “ra khỏi trang” vs “vào trang” không nhất quán khi đi vòng.

Một cách thấy mâu thuẫn: gán hàm cao dọc dầm khớp với khớp nối vẽ; sau một vòng đầy đủ cao không khớp. Chướng ngại là toàn cục—sống trên đường đóng—trong khi mọi đường con thực sự đều ổn.

“Tam giác Penrose” vật lý trong công viên điêu khắc hoạt động nhờ **phối cảnh cưỡng bức**: từ một góc nhìn chiếu khớp bản vẽ; bước sang ngang dầm tách ra. Vật 3D không phải lăng trụ dầm tam giác đóng; đó là cấu hình mở có chiếu đặc biệt.

---

## 3. Cầu thang Escher và tự sự thị giác

Thạch bản của M. C. Escher (*Ascending and Descending*, *Waterfall*) biến cấu hình bất khả thành thế giới kiến trúc. Cầu thang leo mãi vẫn về điểm xuất phát; nước đổ chạy bánh xe rồi chảy ngược lên. Nghệ thuật chặt về hình học: **đồ thị chiếu** chứa chu trình với thay đổi độ cao không nhất quán.

Escher hợp tác ý tưởng toán (Penrose, Coxeter) mà không tuyên bố hình học Euclid sai. Ông minh họa **gán chiều sâu đa ổn định và không nhất quán**—hệ thị giác người cố hoàn thiện tín hiệu địa phương thành mô hình 3D toàn cục và thất bại đủ duyên để vẫn đẹp.

---

## 4. Chiếu, mơ hồ, họ hàng Necker

Ngay vật *khả thi* cũng có bản vẽ mơ hồ: **lập phương Necker** lật giữa hai diễn giải chiều sâu. Hình bất khả đi xa hơn trên phổ: không gán chiều sâu đơn nào khớp cả hình.

Chiếu trực giao hoặc phối cảnh

$$
\pi:\mathbb{R}^3\to\mathbb{R}^2
$$

sụp một chiều. Nhiều tiền ảnh chia sẻ cùng bóng. Bản vẽ đường underdetermine cấu trúc 3D; giả định thêm (mặt phẳng, góc vuông, đục) vẫn có thể không có nghiệm. Thị giác máy tính và giải ràng buộc hình học hình thức hóa thành hệ phương trình trên tọa độ đỉnh và liên thuộc—đôi khi overconstrained và không nhất quán.

---

## 5. Ngôn ngữ toán cho mâu thuẫn

Nghĩ hình bất khả như cố dán các chart 3D địa phương dọc chồng (đoạn dầm, mặt). Trên mỗi chồng, hai chart liên hệ bởi chuyển động cứng hoặc dịch cao. Quanh vòng đóng của chồng, hợp các map chuyển tiếp phải là đồng nhất nếu đối tượng toàn cục tồn tại. Nếu hợp là tịnh tiến chiều sâu không tầm thường, **cocycle không tầm thường**—không có section toàn cục.

Không cần cohomology đầy đủ để nắm đạo đức:

> **Dữ liệu hình học địa phương cộng quy tắc chuyển tiếp có thể thất bại điều kiện chu trình cần cho hiện thực toàn cục.**

Cùng mẫu xuất hiện khi dựng đa tạp từ chart, khi bundle có tôpô không tầm thường, khi hàm cao rời rạc trên đồ thị có chu trình không nhất quán. Hình bất khả là phiên bản bàn cà phê của lớp chướng ngại.

Hình thức liên quan: hệ tuyến tính không nhất quán cho tọa độ đỉnh; metric đa diện không nhúng được với hình dạng mặt cho trước; phủ phân nhánh và chiều sâu đa trị.

---

## 6. Hình bất khả không phải gì

- **Không phải** dải Möbius: Möbius tồn tại như tập con $$\mathbb{R}^3$$ (hoặc mặt trừu tượng). Tam giác bất khả không tồn tại như vật rắn đóng mà chúng mô tả.
- **Không phải** chứng minh tự động chiều cao hơn: đôi khi nhúng 4D hiện thực cấu hình 3D không làm được, nhưng mỗi tuyên bố cần định lý chính xác—không phải chú thích poster.
- **Không phải** thất bại logic: chúng là thất bại của *một* bài toán khả thi cụ thể.

Tương phản với [đối tượng hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/) *có* tồn tại và thách thức trực giác bằng chính sự tồn tại.

---

## 7. Vì sao quan trọng

- **Hình học:** ràng buộc, cứng nhắc, chiếu.
- **Tôpô:** chướng ngại dán.
- **Khoa học thị giác:** não suy 3D từ tín hiệu 2D; nơi suy luận gãy.
- **Đồ họa máy tính:** kỹ nghệ ngược 3D từ phác thảo; phát hiện không nhất quán.
- **Sư phạm:** giới thiệu nguyên lý địa phương–toàn cục một cách hữu hình.

Toán đẹp: cảm giác chính xác mà bản vẽ có thể **nói dối mà không có đường nào sai**.

---

## 8. Nhầm lẫn thường gặp

1. “Tam giác Penrose tồn tại như vẽ.” — Chỉ như hình 2D hoặc trò phối cảnh, không như vật rắn đóng ngây thơ.
2. “Hình bất khả bác bỏ hình học Euclid.” — Bác bỏ bản vẽ diễn giải quá mức, không bác Euclid.
3. “Giống mặt không định hướng.” — Vấn đề khác: tồn tại vs chiếu không nhất quán của vật được mô tả.
4. “Mọi bản vẽ lạ đều sâu về toán.” — Chiều sâu đến từ quy tắc địa phương sạch và chướng ngại rõ.
5. “Cầu thang Escher cao vô hạn.” — Trong diễn giải không nhất quán, cao đa trị, không phải tòa nhà vô hạn thật.
6. “Sửa một góc là sửa cả hình.” — Chướng ngại toàn cục; sửa địa phương có thể dời nhưng không xóa mâu thuẫn chu trình nếu không đổi kiểu hình.

---

### Khẩu hiệu hình bất khả (từ nghiên cứu video)

- Nút giao cục bộ có thể ổn trong khi đồ thị độ sâu/hướng toàn cục có chu trình mâu thuẫn.
- Khác ảo ảnh độ sáng; vấn đề toán là **tính nhất quán hình học dưới phép chiếu**.
- Cầu thang Escher kịch tính hóa vòng lên không nhất quán.

## Bài tập

1. Che hai góc bản phác tam giác Penrose; mô tả vì sao mỗi góc thấy được trông khả thi.
2. Giải thích điêu khắc phối cảnh cưỡng bức của hình bất khả trong một đoạn.
3. Lập phương Necker khác tam giác Penrose thế nào?
4. ≤200 từ: đạo đức địa phương–toàn cục với lập luận hàm cao quanh vòng.
5. Tương phản hình bất khả với dải Möbius: cái nào tồn tại trong $$\mathbb{R}^3$$ như đối tượng được gọi tên?
6. (Mở rộng) Hệ nhỏ không nhất quán: ba cạnh đổi cao $$+1,+1,+1$$ quanh tam giác dầm.
7. (Mở rộng) Tìm một tranh Escher và chỉ đường đóng độ cao không nhất quán.
8. Nối [lát]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/) (quy tắc khớp địa phương) và [nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/) trong ba câu.

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

Đối tượng lạ có tồn tại: [Hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/). Nghịch lý logic: [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/). Quy tắc địa phương–hệ quả toàn cục: [Lát]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/) và [Hiện tượng nảy sinh]({{ site.baseurl }}/contents/vi/chapter04/04_12_Emergence/).
