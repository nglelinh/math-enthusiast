---
layout: post
title: "Bài toán Navier–Stokes"
chapter: '01'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

**Phương trình Navier–Stokes** mô hình chuyển động của chất lỏng nhớt không nén. Chúng là xương sống của cơ học chất lưu kỹ thuật—và đồng thời là bài toán Thiên niên kỷ của Viện Clay về lý thuyết **nghiệm trơn toàn cục** trong ba chiều.

Đây **không** phải câu hỏi “ta có chạy mô phỏng được không?” Kỹ sư chạy solver Navier–Stokes mỗi ngày cho máy bay, thời tiết, ống dẫn, sinh học. Câu hỏi Clay là: mô hình continuum toán học—hệ PDE lý tưởng—có được **bảo đảm** giữ trơn mọi thời gian từ dữ liệu ban đầu trơn (năng lượng hữu hạn), hay **singularity** (thổi phồng gradient / vorticity) có thể hình thành trong thời gian hữu hạn?

Bài này tách rõ **thực hành kỹ thuật**, **nghiệm yếu Leray**, và **bài toán chính quy Thiên niên kỷ**, kể kết quả từng phần có tên, và nối văn hóa đa thang (DNS, rối) mà không đồng nhất chi phí lưới với giải thưởng Clay.

**Lộ trình:** phương trình → ý nghĩa vật lý → Clay hỏi gì → điều đã biết → vì sao khó → Deng/kinetic → kỹ thuật vs Millennium → nhầm lẫn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết hệ Navier–Stokes **không nén** (vận tốc + áp suất, ràng buộc $$\nabla\cdot u=0$$) ở mức khẩu hiệu và gọi tên hạng phi tuyến, nhớt, áp suất.
- Phân biệt **dùng kỹ thuật** NS với **bài toán chính quy Thiên niên kỷ**.
- Giải thích nghiệm yếu **Leray** so với nghiệm trơn cổ điển (tồn tại yếu toàn cục ≠ chính quy/duy nhất đầy đủ).
- Phát biểu bài toán mở: tồn tại–duy nhất trơn 3D toàn cục, hoặc blow-up thời gian hữu hạn từ dữ liệu trơn.
- Kể một họ kết quả từng phần: Beale–Kato–Majda; dữ liệu nhỏ / mild solutions; partial regularity (Caffarelli–Kohn–Nirenberg); chính quy 2D.
- Nối với [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): suy dẫn continuum từ kinetic **khác** chính quy NS 3D.
- Tránh LO6: “máy bay bay được nên NS đã giải,” “mô phỏng blow-up = chứng minh.”

**Tiên quyết.** Giải tích nhiều biến; ý tưởng PDE như định luật cân bằng địa phương. Không cần khóa học PDE nâng cao—các định lý được kể ở mức khẩu hiệu có tên.

**Liên kết seminar.** **LO1**; essay [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (nền tảng kinetic của chất lưu); ứng dụng phương trình vi phân trong khóa khi có.

---

## 1. Phương trình (dạng không nén)

Cho trường vận tốc $$u(x,t)\in\mathbb{R}^3$$ và áp suất $$p(x,t)$$,

$$
\begin{aligned}
\partial_t u + (u\cdot\nabla)u &= \nu \Delta u - \nabla p + f,\\
\nabla\cdot u &= 0,
\end{aligned}
$$

với độ nhớt $$\nu>0$$ và lực ngoài tùy chọn $$f$$. Hạng phi tuyến $$(u\cdot\nabla)u$$ **vận chuyển** động lượng theo dòng; hạng nhớt $$\nu\Delta u$$ **làm trơn**; áp suất $$-\nabla p$$ **ép** ràng buộc không nén $$\nabla\cdot u=0$$ (chất lỏng không “nén cục bộ” trong mô hình này).

Trên $$\mathbb{R}^3$$ hoặc xuyến (torus), với dữ liệu ban đầu trơn, không nén, suy giảm/tăng trưởng hợp lý, người ta hỏi liệu nghiệm trơn duy nhất có tồn tại cho mọi thời gian dương hay không.

**Đọc vật lý ngắn.** Số Reynolds lớn tương ứng nhớt tương đối nhỏ: quán tính và vận chuyển thắng khuếch tán—chế độ rối, nhiều thang không gian-thời gian. Clay không hỏi “rối trông như thế nào trên máy,” mà hỏi liệu mô hình continuum có thể tự tạo singularity toán học.

---

## 2. Bài toán Thiên niên kỷ hỏi gì

Đại ý (xem mô tả chính thức của Fefferman / Clay cho wording và không gian hàm chính xác):

Chứng minh một trong hai hướng:

- **Chính quy toàn cục:** dữ liệu trơn năng lượng hữu hạn cho nghiệm trơn mọi $$t>0$$, với kiểm soát tăng trưởng phù hợp; hoặc  
- **Blow-up:** tồn tại dữ liệu trơn sao cho nghiệm không thể tiếp tục trơn sau một thời gian hữu hạn.

Các vấn đề mở liên quan gồm duy nhất của nghiệm yếu và bản chất có thể có của singularity (tập kỳ dị “mỏng” cỡ nào, đại lượng nào thổi phồng).

**Tình trạng khoảng 2026:** **mở**. Một trong sáu bài Thiên niên kỷ chưa giải. Poincaré là bài Thiên niên kỷ duy nhất đã giải (Perelman).

Nhấn mạnh: “mở” ở đây là **định lý tồn tại/chính quy continuum**, không phải “chưa ai mô phỏng được nước.”

---

## 3. Điều *đã* biết

Lý thuyết không trống rỗng—đó là điểm quan trọng cho tóm tắt A3:

- **Hai chiều (2D):** chính quy toàn cục là cổ điển. Vorticity bị kiểm soát tốt hơn vì không có cơ chế **vortex stretching** theo cùng cách 3D.
- **3D thời gian ngắn:** dữ liệu trơn cho nghiệm trơn duy nhất trên một khoảng thời gian dương phụ thuộc dữ liệu. Vấn đề là *kéo dài đến vô hạn* hay *gặp singularity*.
- **Leray (1934):** tồn tại nghiệm **yếu** toàn cục trong 3D thỏa bất đẳng thức năng lượng—nhưng **duy nhất** và **chính quy đầy đủ** vẫn mở. Nghiệm yếu “tồn tại theo nghĩa tích phân / phân bố,” không tự động là trường trơn cổ điển.
- **Tiêu chí chính quy:** nếu một số chuẩn giữ hữu hạn—ví dụ tiêu chí **Beale–Kato–Majda** trên tích phân vorticity—thì nghiệm vẫn trơn. Khẩu hiệu: singularity, nếu có, phải “nhìn thấy” ở đại lượng xoáy/gradient đủ mạnh.
- **Dữ liệu nhỏ / mild solutions:** chính quy toàn cục khi dữ liệu ban đầu nhỏ trong không gian hàm thích hợp (nhớt thắng phi tuyến).
- **Partial regularity:** các lược đồ kiểm soát kích thước tập kỳ dị cho nghiệm yếu “phù hợp” (Caffarelli–Kohn–Nirenberg và công trình sau)—singularity không thể “quá dày” nếu xảy ra.

Vậy ta có bản đồ phong phú về *khi nào* nghiệm trơn và *singularity phải trông như thế nào*—nhưng thiếu định lý đóng cho mọi dữ liệu trơn 3D.

---

## 4. Vì sao khó

Kẻ thù trung tâm là **hạng phi tuyến trong 3D**, có thể tập trung năng lượng vào thang nhỏ qua **vortex stretching**. Ước lượng năng lượng kiểm soát chuẩn $$L^2$$ (và họ hàng) nhưng không tự động kiểm soát mọi đạo hàm cao. Singularity khả dĩ sẽ liên quan vorticity hoặc gradient vận tốc vô hạn—liệu mô hình continuum của “thiên nhiên lý tưởng” có cho phép điều đó là câu hỏi toán học.

**Numerics** cho thấy rối dữ dội nhưng **không** cấu thành chứng minh blow-up của PDE continuum: rời rạc hóa, dưới-độ-phân-giải, điều kiện biên, và giới hạn mô hình can thiệp. Một mô phỏng “nổ” có thể là artifact lưới. Ngược lại, mô phỏng êm cũng không chứng minh chính quy mọi dữ liệu.

So với [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/): ở đó kiểm máy hữu hạn không kết thúc phát biểu vô hạn; ở đây kiểm số trên PDE rời rạc không kết thúc phát biểu continuum. Cùng đạo đức **evidence ≠ proof**, khác đối tượng.

---

## 5. Quan hệ lý thuyết động học và công trình Deng

Công trình được cộng đồng ghi nhận của **Yu Deng** xây cầu chặt từ **hệ hạt** tới **Boltzmann** tới **phương trình chất lưu** trong một số chế độ. Điều đó hỗ trợ *suy dẫn* mô hình continuum—vì sao PDE chất lưu xuất hiện như giới hạn—**không** tự chứng minh chính quy Navier–Stokes 3D theo nghĩa phát biểu Millennium.

Dùng essay Deng để hiểu **vì sao phương trình chất lưu tồn tại như giới hạn**; dùng bài này để hiểu **liệu những PDE continuum đó có giữ trơn**. Hai câu hỏi xếp tầng: derivation ≠ regularity.

Xem [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

---

## 6. Kỹ thuật so với Millennium

| Thực tiễn kỹ thuật | Bài toán Clay |
|--------------------|---------------|
| Mô phỏng DNS / LES / RANS | Lý thuyết trơn toàn cục cho NS lý tưởng |
| Lưới, bước thời gian, mô hình rối | Định lý tồn tại / duy nhất / chính quy |
| Chi phí số Reynolds | Ước lượng giải tích và blow-up khả dĩ |
| So khớp thí nghiệm / thiết kế | Chứng minh trong không gian hàm chuẩn |

Cả hai quan tâm **cascade năng lượng đa thang**; chỉ một cái là bài Thiên niên kỷ. Khi viết A3, một đoạn tách bảng trên thường cứu bạn khỏi LO6.

**DNS** (Direct Numerical Simulation) cố gắng giải NS “trung thực” xuống thang nhớt—chi phí tăng nhanh với Reynolds. **LES/RANS** mô hình hóa thang nhỏ. Thành công kỹ thuật không trả lời Clay; thất bại tính toán cũng không.

---

## 7. Văn hóa toán học quanh NS

- **Tiêu chí chính quy** cho phép chứng minh “nếu singularity thì …” — dạng định lý điều kiện.
- **Nghiệm yếu** cho phép tồn tại toàn cục với ít chính quy hơn—rồi hỏi nâng cấp.
- **Dữ liệu nhỏ** cho thấy phi tuyến không phải lúc nào cũng thắng.
- **Partial regularity** gợi ý singularity, nếu có, “hiếm” theo nghĩa độ đo.

Đây là mẫu “toán học quanh bài toán mở” giống [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): câu hỏi gốc kháng cự, ngành thì đầy định lý.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “NS chưa giải nên máy bay không được bay.” | Mô hình kỹ thuật + thực nghiệm hoạt động; Clay hỏi định lý tồn tại/chính quy thuần. |
| “Ai đó mô phỏng blow-up thì bài toán xong.” | Mô phỏng ≠ chứng minh PDE continuum. |
| “Deng đã giải Navier–Stokes.” | Deng đẩy suy dẫn kinetic; chính quy NS 3D vẫn mở. |
| “2D và 3D như nhau.” | Chính quy 2D đã biết; 3D là case khó. |
| “Leray đã giải vì có nghiệm toàn cục.” | Nghiệm yếu; chính quy/duy nhất đầy đủ mở. |
| “Clay là về chọn bước lưới tối ưu.” | Không—là về lý thuyết giải tích PDE. |

---

## Bài tập

1. Trong hệ NS, chỉ rõ hạng phi tuyến và hạng nhớt; một câu vai trò mỗi hạng.  
2. $$\nabla\cdot u=0$$ nghĩa vật lý gì trong mô hình không nén?  
3. Đối chiếu nghiệm yếu Leray với nghiệm trơn cổ điển (tồn tại, chính quy, duy nhất).  
4. **LO1 (≤300 từ):** phát biểu bài toán Clay NS, vì sao khó, một kết quả từng phần có tên.  
5. Sau khi đọc [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): viết ba câu phân biệt *suy dẫn* NS và *chính quy* NS.  
6. **LO6:** sửa câu báo “Nhà toán học mô phỏng rối 3D, giải thưởng Clay sắp về tay.”  
7. Liệt kê hai lý do numerics không chứng minh blow-up continuum.  
8. Stretch: đọc mô tả Clay của Fefferman và ghi lại (khẩu hiệu) bối cảnh không gian hàm ông dùng.

---

## Từ các bài giảng: văn hóa blow-up (Tao) và văn hóa chính quy (Caffarelli)

Numberphile (Crawford), bài Clay của Caffarelli, và Einstein Lecture của Tao bổ sung khẩu hiệu:

- **Dòng Caffarelli:** chính quy từng phần (CKN) ràng buộc *mức độ xấu* của tập kỳ dị nghiệm yếu phù hợp—tập “nhỏ” không đồng nghĩa tập rỗng.  
- **Dòng Tao:** blow-up hữu hạn thời gian cho mô hình *trung bình* / toy nhấn mạnh **supercriticality**—ước lượng năng lượng không đủ scale để đóng bootstrap cho dữ liệu trơn lớn. Blow-up trên phương trình sửa đổi **không** là giải Clay cho NS thật.  
- **Đồng tồn kỹ thuật:** DNS/LES/RANS sống trong thế giới rời rạc; Clay hỏi định lý continuum.

**Tình trạng (2026):** chính quy toàn cục / blow-up 3D **mở** (Millennium).

---

## Nguồn video (gói math-video-researcher)

Xếp hạng: `research/video-research/Navier_Stokes/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *Navier-Stokes Equations* (Crawford): [YouTube](https://www.youtube.com/watch?v=ERBVFcutl3M).  
2. **Trực giác** — vcubingx, *The million dollar equation*: [YouTube](https://www.youtube.com/watch?v=Ra7aQlenTb8).  
3. **Nền** — Caffarelli, bài Clay về NS: [YouTube](https://www.youtube.com/watch?v=ta6Q70y6YVU).  
4. **Nghiên cứu** — Tao, *Can NS Blow Up in Finite Time?*: [YouTube](https://www.youtube.com/watch?v=DgmuGqeRTto).  
5. **Văn bản gốc** — Fefferman PDF: [navierstokes.pdf](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) · [Clay](https://www.claymath.org/millennium/navier-stokes-equation/).

**Sau video:** CFD thành công ≠ định lý Clay. Yếu ≠ trơn. Tình trạng **mở** năm 2026.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/Navier_Stokes/transcripts/` · trạng thái: `research/video-research/Navier_Stokes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Navier_Stokes_ERBVFcutl3M_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Thư mục URL: `research/video-research/Navier_Stokes/references.md`.

1. Clay — [NS](https://www.claymath.org/millennium/navier-stokes-equation/) · Fefferman PDF: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf  
2. Robinson — [survey](https://royalsocietypublishing.org/rsta/article/378/2174/20190526/111659/The-Navier-Stokes-regularity-problem).  
3. Wikipedia — [NS existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness).  
4. Numberphile: https://www.youtube.com/watch?v=ERBVFcutl3M  
5. vcubingx: https://www.youtube.com/watch?v=Ra7aQlenTb8  
6. Caffarelli: https://www.youtube.com/watch?v=ta6Q70y6YVU  
7. Tao: https://www.youtube.com/watch?v=DgmuGqeRTto  
8. [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/). Gói: `research/video-research/Navier_Stokes/`.

---

## Hướng đi tiếp

Ứng viên **A3**. Studio: cascade Kolmogorov như *heuristic*—không phải chứng minh. Đọc Deng cho “từ hạt tới continuum,” rồi giữ ranh giới kỹ thuật vs Clay.
