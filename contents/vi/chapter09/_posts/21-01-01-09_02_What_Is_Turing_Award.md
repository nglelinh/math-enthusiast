---
layout: post
title: "Giải Turing là gì?"
chapter: '09'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Giải A.M. Turing** (A.M. Turing Award) là vinh danh cao nhất của **Hiệp hội Máy tính ACM** (Association for Computing Machinery), thường được gọi là **Nobel của tin học**. Giải mang tên **Alan Mathison Turing** (1912–1954), người đã đặt nền khái niệm cho tính toán hiện đại qua bài “On Computable Numbers” (1936) và để lại dấu ấn sâu trong mật mã, triết học máy, và hình dung về máy thông minh. Tài liệu chính thức: [amturing.acm.org](https://amturing.acm.org/).

Bài này **không** liệt kê toàn bộ danh sách người thắng. Đó là bản đồ **Giải Turing để làm gì**, nó bổ sung Fields và Abel thế nào trong khóa *Math Enthusiast*, và cách **đọc citation** như người học toán–tin học chứ không như khán giả danh vọng. Đèn spotlight thuộc về giải thưởng; **toán học của tính toán** mới là sân khấu.

---

## Mục tiêu học tập

Sau bài, bạn có thể mô tả vai trò thể chế của Giải Turing trong cộng đồng khoa học máy tính; so sánh chính xác Turing Award với Fields, Abel và Clay Millennium theo nhịp, tuổi, và kiểu thành tựu; trích đối tượng toán–thuật toán từ một câu citation ngắn; giải thích vì sao một thân công cụ (độ phức tạp, mật mã, phân tích thuật toán) có thể đáng giải bằng một định lý nổi tiếng; và dùng phương pháp đọc của chương (citation → đối tượng → một ý giải thích được → liên kết khóa học) cho bất kỳ laureate gần đây.

**Tiên quyết.** Không cần chuyên sâu nghiên cứu. Cần đọc được đoạn tiếng Anh kỹ thuật ngắn và nhận tên lĩnh vực rộng (độ phức tạp, thuật toán, mật mã, học máy, đồ thị, logic). [Tổng quan chương]({{ site.baseurl }}/contents/vi/chapter09/09_00_Tong_quan/), [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/) và [Tổng quan Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/) giúp so sánh nhưng không bắt buộc lần đầu.

---

## 1. Vì sao có giải mang tên Turing

Suốt nửa sau thế kỷ XX, tin học trở thành ngành khoa học với định lý, mô hình, và chuẩn chứng minh—không chỉ nghề chế tạo máy. Cộng đồng cần một tín hiệu vinh danh hàng năm, tầm quốc tế, cho **đóng góp nền tảng** đã thay đổi cách người khác làm việc: lớp độ phức tạp, giao thức mật mã, cấu trúc dữ liệu, kiến trúc hệ thống, học từ dữ liệu, và cả triết lý về cái máy có thể làm được.

**Nobel** không có hạng mục tin học thuần. **Fields** vinh danh toán thuần với giới hạn tuổi và chu kỳ bốn năm. **Abel** vinh danh thân sự nghiệp toán, không giới hạn tuổi, nhưng trọng tâm vẫn là toán học theo nghĩa truyền thống của viện hàn lâm. Giải Turing của ACM lấp khoảng trống: vinh danh **khoa học máy tính** ở mức cao nhất, thường gắn với ý tưởng đã chín qua nhiều năm và lan sang thực hành công nghiệp hoặc chương trình đào tạo toàn cầu.

Đặt tên Turing là tuyên bố văn hóa. Năm 1936, trước khi có máy điện tử phổ biến, Turing đã tách **cái gì có thể tính được về nguyên lý** khỏi chi tiết kỹ thuật của một thiết bị cụ thể. Ông chứng minh tồn tại bài toán không quyết định được, dựng mô hình máy phổ quát, và sau này gợi ý các câu hỏi về học và trí tuệ nhân tạo. Giải thưởng mang tên ông không chỉ tôn vinh một người; nó tuyên bố rằng tin học có **cốt lõi toán học và khái niệm** ngang tầm các khoa học lớn khác.

---

## 2. Citation thường nhấn gì

Mở bất kỳ citation trên [amturing.acm.org](https://amturing.acm.org/) thường thấy ngôn ngữ về **nền tảng lĩnh vực**, **mô hình mới**, **công cụ mọi người dùng**, hoặc **cầu nối lý thuyết–thực hành**. Ủy ban hiếm khi dừng ở một dòng code. Ví dụ (gần tinh thần citation chính thức, tóm tắt sư phạm):

- **Cook (1982) / Karp (1985):** NP-đầy đủ và ngôn ngữ độ khó tổ hợp.  
- **Knuth (1974):** phân tích thuật toán; *The Art of Computer Programming*.  
- **RSA (2002) / Diffie–Hellman (2015):** mật mã khóa công khai.  
- **Goldwasser & Micali (2012):** an ninh có chứng minh và zero-knowledge.  
- **Yao (2000), deep learning (2018), Wigderson (cầu TCS/Abel):** complexity, learning, randomness.

Động từ: *mở*, *tiên phong*, *định hình*, *nền tảng*. Ngôn ngữ Turing Award là **đổi khí hậu lĩnh vực tính toán**, không chỉ một đỉnh núi phần mềm.

Bài tập hữu ích: khoanh **đối tượng toán–tin** trong citation (máy Turing, NP-đầy đủ, hàm một chiều, zero-knowledge, expander, attention, …) rồi viết một câu bạn cùng lớp hiểu được. Citation là cửa, không phải bằng tốt nghiệp.

---

## 3. Turing Award giữa các vinh danh khác

| Vinh danh | Nhịp / tuổi | Nhấn mạnh điển hình |
|-----------|-------------|---------------------|
| **Fields** | 4 năm; dưới 40 | Đột phá toán thuần, thường một định lý cờ đầu |
| **Abel** | Hàng năm; không giới hạn tuổi | Thân sự nghiệp toán / định hình lĩnh vực |
| **Turing Award** | Hàng năm (thường); không giới hạn tuổi kiểu Fields | Nền tảng khoa học máy tính; lý thuyết và/hoặc hệ thống |
| **Clay Millennium** | Bài toán, không phải người | Bảy bài mở với tiền thưởng cho lời giải (gồm P vs NP) |
| **Nobel** | Hàng năm theo hạng mục | Không có tin học thuần; vật lý/hóa/y/… |

Ba phân biệt sư phạm quan trọng.

Thứ nhất, **Turing Award không phải “Abel cho tin học” theo nghĩa sao chép.** Abel và Turing Award cùng vinh danh tác động dài hạn, nhưng đối tượng và cộng đồng khác: một bên viện hàn lâm toán, một bên ACM và hệ sinh thái CS toàn cầu. Một số sự nghiệp (ví dụ Wigderson) được cả hai cộng đồng nhìn thấy—đó là tín hiệu liên ngành, không phải trùng lặp vô nghĩa.

Thứ hai, **Fields và Turing Award tối ưu tín hiệu khác nhau.** Fields bắt tia chớp sớm trong toán thuần; Turing Award thường bắt ý tưởng đã trở thành **ngôn ngữ mặc định** của thuật toán, mật mã, hoặc hệ thống—đôi khi sau nhiều thập niên lan tỏa.

Thứ ba, **Clay Millennium không phải giải cho người.** P vs NP là bài toán Thiên niên kỷ; Cook–Karp là câu chuyện **phương pháp và lớp** làm bài toán đó trở thành trung tâm. Đọc chương này, bạn cần giữ cả hai: bài toán mở và hạ tầng khái niệm.

---

## 4. “Nền tảng tính toán” như ý tưởng toán

Không chỉ nghĩa “nhiều paper” hay “startup thành công.” Nghĩa là công cụ của nhà nghiên cứu trở thành **mặc định**: định nghĩa lớp độ phức tạp ai cũng trích, reduction mọi sách giáo khoa dạy, giao thức khóa công khai mọi trình duyệt dùng, chuẩn phân tích thời gian–không gian mọi khóa thuật toán nhắc tới. Sau đó ngôn ngữ lĩnh vực đổi. Sinh viên học các môn trước đó không tồn tại; ngành lân cận (toán, vật lý thống kê, kinh tế, sinh học tính toán) nhập từ vựng; bài mở được phát biểu lại bằng phương ngữ mới.

Ví dụ trong chương (phát triển ở các bài sau): máy Turing và bất khả quyết định; Cook–Levin và danh sách Karp; phân tích tiệm cận kiểu Knuth; Diffie–Hellman và RSA; Goldwasser–Micali và zero-knowledge. Mỗi cái là một mảnh **hạ tầng** hơn là một “mẹo lập trình.”

Hỏi phản thực: *Nếu xóa công trình này khỏi văn học, định lý hay hệ thống sau nào sẽ khó phát biểu hơn nhiều?* Đó là định nghĩa thực dụng của nền tảng.

---

## 5. Cách học chương này

Bốn bước cho mỗi bài từ 09_03 trở đi:

1. **Đọc câu citation** cẩn thận (copy từ amturing.acm.org nếu được).  
2. **Nhận diện đối tượng toán–tin** (lớp, mô hình, giao thức, định lý).  
3. **Phát biểu một ý giải thích được** bằng lời thường (một đoạn).  
4. **Ghi một liên kết khóa học**—P vs NP ch.01, mật mã ch.03, độ phức tạp ch.06, Abel/Wigderson ch.08, AI ch.06.

Tránh hai lỗi: **thờ phụng anh hùng không cơ chế**, và **overclaim** (Turing Award cho deep learning ≠ “AI đã giải được ý thức”; NP-đầy đủ ≠ “mọi instance thực tế bất khả”; mật mã khóa công khai ≠ “tuyệt đối an toàn”).

Chương 09 nằm cạnh [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Lý thuyết độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Lý thuyết số → mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), và [Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/). Hãy đọc vì **cơ chế**, không vì năm trao giải.

---

## 6. Alan Turing trong chân dung giải thưởng

Năm 1936, Turing định nghĩa **hàm tính được** qua máy băng–trạng thái, xây **máy phổ quát** (hạt nhân “phần mềm”), và chứng minh **bài toán dừng** không quyết định được. Bletchley Park gắn mật mã thời chiến; bài 1950 về trí tuệ máy là gợi ý triết học, **không** phải định lý độ phức tạp. Laureate sau không lặp 1936: họ mở tầng **hiệu quả**, **an ninh**, **học**, **hệ thống** trên nền “cái gì tính được.” Chi tiết ở [bài 09_03]({{ site.baseurl }}/contents/vi/chapter09/09_03_Turing_Computability/).

---

## 7. Nhầm lẫn thường gặp

| Khẳng định | Chỉnh |
|------------|-------|
| “Turing Award là Nobel tin học.” | Chỉ là ẩn dụ báo chí. Đó là giải của ACM, không phải hạng mục Nobel. |
| “Turing Award chỉ cho lý thuyết.” | Nhiều năm vinh danh hệ thống, kiến trúc, mạng, đồ họa, học máy thực nghiệm. Chương này nhấn các năm giàu toán. |
| “Fields hơn / Turing hạng hai.” | Tín hiệu và cộng đồng khác; không xếp hạng tuyệt đối. |
| “Citation chứng minh mọi slogan báo chí.” | Báo nén. Tách định lý và giao thức khỏi ẩn dụ. |
| “Clay giống Turing Award.” | Clay thưởng **bài toán**; Turing Award vinh danh **người và nghiên cứu**. |
| “Biết tên laureate = hiểu khoa học.” | Mục tiêu khóa học là cơ chế: reduction, máy Turing, hàm cửa sập, zero-knowledge. |

---

## Bài tập

1. Hai câu: so Giải Turing và Fields chỉ bằng sự kiện thể chế—không tên laureate.  
2. Mở [amturing.acm.org](https://amturing.acm.org/), chọn một laureate **không** nằm trong sáu bài sâu đầu chương, liệt kê ba danh từ đối tượng toán–tin trong citation.  
3. ≤150 từ: “nền tảng tính toán” là gì, lấy một ví dụ bạn đã gặp ở ch.01 hoặc ch.03.  
4. Vì sao sai khi nói Turing Award 1982 “giải P vs NP”? Giải đó nhấn gì thay vào đó?  
5. Lập bảng 3 cột so Turing Award / Abel / Clay: đối tượng vinh danh, nhịp, ví dụ một năm.  
6. **≤300 từ:** Lập luận xây công cụ (lớp NP, chuẩn phân tích thuật toán, giao thức khóa công khai) quan trọng không kém một định lý nổi tiếng.  
7. Viết một câu citation giả cho một ý tưởng bạn yêu thích trong khóa (không cần đúng lịch sử)—rồi gạch chân đối tượng toán.  
8. Studio: chọn hai năm Turing Award; bảng 4 cột: năm – tên – một câu thành tựu – loại (computability / complexity / algorithms / crypto / systems / learning).

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/what-is-turing-award/`.

**Khẩu hiệu từ gói nghiên cứu**

- Turing Award ACM: vinh dự cao nhất tin học; amturing.acm.org.
- So Fields/Abel; một số người nhận cả hai (Wigderson).

**Thứ tự xem gợi ý**

1. **ORIENTATION** — ACM Turing Award lectures playlist: [https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6](https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6).  

**Cổng chính thức / tài liệu**

- ACM A.M. Turing Award home: https://amturing.acm.org/  
- Winners by year: https://amturing.acm.org/byyear.cfm  
- Alphabetical listing: https://amturing.acm.org/alphabetical.cfm  
- Abel Prize (contrast): https://abelprize.no/  

Danh mục URL đầy đủ: `research/video-research/what-is-turing-award/references.md`.

## Tài liệu


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/what-is-turing-award/references.md`.

1. ACM A.M. Turing Award home — https://amturing.acm.org/  
2. Winners by year — https://amturing.acm.org/byyear.cfm  
3. Alphabetical listing — https://amturing.acm.org/alphabetical.cfm  
4. ACM about the award — https://www.acm.org/about-acm/acm-history/acm-awards/turing-award  
5. Wikipedia — Turing Award — https://en.wikipedia.org/wiki/Turing_Award  
6. Wikipedia — Alan Turing — https://en.wikipedia.org/wiki/Alan_Turing  
7. Wikipedia — Association for Computing Machinery — https://en.wikipedia.org/wiki/Association_for_Computing_Machinery  
8. ACM Turing Award lectures playlist — https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6  
9. Abel Prize (contrast) — https://abelprize.no/  
10. Thư mục gói: `research/video-research/what-is-turing-award/`.

1. [ACM A.M. Turing Award](https://amturing.acm.org/) — citation, tiểu sử, bài giảng.  
2. Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem.  
3. [Tổng quan chương 09]({{ site.baseurl }}/contents/vi/chapter09/09_00_Tong_quan/); [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/); [Tổng quan Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
4. Sipser, M. *Introduction to the Theory of Computation* — ngữ cảnh máy Turing và độ phức tạp cho người mới.

---

## Hướng đi tiếp

- So bảng bài này với [Abel]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/) và [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/): ba khác biệt chính xác.  
- Phát biểu lại ý tưởng cốt lõi Turing Award trong một đoạn cho người không học tin học.  
- Ghi một câu hỏi còn mở cạnh bất kỳ citation nào trong chương (P vs NP, an ninh concrete, derandomization, …).  
- Tiếp: [Turing, Tính được và Bất khả quyết định]({{ site.baseurl }}/contents/vi/chapter09/09_03_Turing_Computability/).

---

## Turing Award như bản đồ

Essay seminar: ưu tiên **citation chính thức** và **một cơ chế** (đối tượng, giả định, reduction/mô hình). Giải là spotlight; sân khấu là toán tính toán. Đọc một năm: gạch chân danh từ → phân loại (computability / complexity / algorithms / crypto / systems / learning) → nối [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), hoặc [Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).
