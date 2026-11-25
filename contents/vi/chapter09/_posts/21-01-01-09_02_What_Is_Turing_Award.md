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

Năm 1966, khi máy tính vẫn còn là những tủ sắt khổng lồ chiếm trọn cả căn phòng ở các trường đại học, Hiệp hội Máy tính ACM quyết định lập ra một giải thưởng thường niên để khẳng định rằng tin học không chỉ là nghề lắp ráp mạch điện hay viết mã thuê — nó đã trở thành một ngành khoa học có nền tảng lý thuyết ngang hàng với vật lý hay toán học. Họ đặt tên giải theo **Alan Mathison Turing** (1912–1954), người qua đời mười hai năm trước đó nhưng đã để lại di sản khái niệm vĩnh cửu qua bài báo *"On Computable Numbers"* (1936). (Vì vậy, cần nhớ một chi tiết lịch sử hay bị nhầm: chính Alan Turing **chưa từng** nhận giải thưởng mang tên mình!)

Ngày nay, **Giải A.M. Turing** được báo chí quen gọi là **"giải Nobel của tin học"**, với hồ sơ chính thức lưu trữ tại [amturing.acm.org](https://amturing.acm.org/). Nhưng bài viết này không nhằm liệt kê danh sách người đoạt giải. Mục đích của chúng ta là học cách **đọc một lời trích dẫn giải Turing bằng con mắt của người làm toán–tin**: hiểu giải này bổ sung gì cho Huy chương Fields và Giải Abel, nhận ra *đối tượng toán học* ẩn sau những câu khen trang trọng, và tránh bị cuốn vào hào quang danh tiếng mà bỏ quên cơ chế.

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- mô tả vai trò của giải Turing trong cộng đồng khoa học máy tính;
- so sánh chính xác giải Turing với Fields, Abel và giải Thiên niên kỷ của Clay về chu kỳ, độ tuổi và kiểu thành tựu;
- rút ra đối tượng toán–thuật toán từ một câu trích dẫn ngắn;
- giải thích vì sao một bộ công cụ (độ phức tạp, mật mã, phân tích thuật toán) có thể xứng đáng nhận giải dù không gắn với một định lý nổi tiếng;
- áp dụng cách đọc của chương (trích dẫn → đối tượng → một ý giải thích được → liên hệ với khóa học) cho bất kỳ người đoạt giải gần đây nào.

**Kiến thức cần có.** Không cần chuyên sâu. Chỉ cần đọc được một đoạn tiếng Anh kỹ thuật ngắn và nhận ra tên các lĩnh vực lớn (độ phức tạp, thuật toán, mật mã, học máy, đồ thị, logic). [Tổng quan chương]({{ site.baseurl }}/contents/vi/chapter09/09_00_Tong_quan/), [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/) và [Tổng quan Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/) giúp so sánh, nhưng không bắt buộc đọc trước.

---

## Kiến thức cần nhớ: Toán học tính toán là gì và các Giải Turing nghiên cứu những gì?

Khi một người tốt nghiệp đại học nhìn vào danh sách Giải Turing gần 60 năm qua, họ thường thấy một bức tranh tưởng chừng rất phân mảnh: người làm trình biên dịch, người làm hệ điều hành UNIX, người làm cơ sở dữ liệu quan hệ, người lại chứng minh định lý về đồ thị giãn hay số nguyên tố. Điểm chung sâu xa của họ là gì?

Khoa học máy tính hiện đại đứng trên **hai chân** bổ sung chặt chẽ cho nhau:
1. **Chân lý thuyết (Toán học tính toán):** xây dựng mô hình hình thức cho máy tính, định nghĩa lớp độ phức tạp (P, NP, #P, BPP, IP), chứng minh thuật toán đúng và nhanh, thiết kế giao thức mật mã có chứng minh an ninh, và đặt nền móng thống kê–logic cho học máy và suy luận nhân quả.
2. **Chân hệ thống (Kỹ nghệ tính toán):** hiện thực hóa những ý tưởng đó thành kiến trúc phần cứng (RISC, GPU), mạng Internet (TCP/IP), hệ quản trị dữ liệu, đồ họa máy tính và các thư viện học sâu chạy ở quy mô toàn cầu.

Trong khóa học *Math Enthusiast*, Chương 9 cố ý chọn lọc những Giải Turing **giàu cấu trúc toán học nhất** để làm nổi bật sợi dây nối giữa toán thuần túy và khoa học máy tính. Ví dụ rõ nhất là trường hợp **Avi Wigderson**: ông nhận **Giải Abel 2021** (toán thuần túy) và **Giải Turing 2023** (khoa học máy tính) cho cùng một cụm công trình về tính ngẫu nhiên, độ phức tạp và đồ thị giãn — chứng minh rằng khi câu hỏi đủ sâu, ranh giới giữa hai ngành tự khắc tan biến.

---

## 1. Vì sao có giải mang tên Turing

Trong nửa sau thế kỷ XX, tin học trở thành một ngành khoa học có định lý, mô hình và chuẩn mực chứng minh, chứ không chỉ là nghề chế tạo máy. Cộng đồng cần một sự ghi nhận hằng năm, mang tầm quốc tế, cho những **đóng góp nền tảng** đã thay đổi cách người khác làm việc: các lớp độ phức tạp, giao thức mật mã, cấu trúc dữ liệu, kiến trúc hệ thống, học từ dữ liệu, và cả những suy nghĩ về việc máy móc có thể làm được gì.

**Nobel** không có hạng mục cho tin học thuần túy. **Fields** vinh danh toán thuần túy, có giới hạn tuổi và bốn năm mới trao một lần. **Abel** vinh danh cả sự nghiệp toán học, không giới hạn tuổi, nhưng vẫn thuộc phạm vi toán học theo nghĩa truyền thống. Giải Turing của ACM lấp khoảng trống đó: vinh danh **khoa học máy tính** ở mức cao nhất, thường dành cho những ý tưởng đã được kiểm nghiệm qua nhiều năm và lan sang thực tiễn công nghiệp hoặc chương trình đào tạo trên toàn thế giới.

Việc đặt tên giải theo Turing cũng có ý nghĩa văn hóa. Năm 1936, khi máy tính điện tử chưa phổ biến, Turing đã tách **điều gì có thể tính được về nguyên tắc** ra khỏi chi tiết kỹ thuật của một thiết bị cụ thể. Ông chứng minh có những bài toán không quyết định được, dựng nên mô hình máy phổ quát, và về sau đặt ra những câu hỏi về học máy và trí tuệ nhân tạo. Giải mang tên ông không chỉ tôn vinh một người; nó khẳng định rằng tin học có **cốt lõi toán học và khái niệm** ngang tầm các ngành khoa học lớn khác.

---

## 2. Lời trích dẫn thường nhấn mạnh điều gì

Mở bất kỳ lời trích dẫn nào trên [amturing.acm.org](https://amturing.acm.org/), ta thường thấy các cụm như **nền tảng của một lĩnh vực**, **mô hình mới**, **công cụ mà mọi người dùng**, hoặc **cầu nối giữa lý thuyết và thực hành**. Hội đồng hiếm khi dừng ở một đoạn mã cụ thể. Một số ví dụ (tóm tắt theo tinh thần trích dẫn chính thức):

- **Cook (1982) / Karp (1985):** NP-đầy đủ và ngôn ngữ để nói về độ khó tổ hợp.  
- **Knuth (1974):** phân tích thuật toán; bộ sách *The Art of Computer Programming*.  
- **RSA (2002) / Diffie–Hellman (2015):** mật mã khóa công khai.  
- **Goldwasser & Micali (2012):** an toàn có chứng minh và chứng minh không tiết lộ tri thức (zero-knowledge).  
- **Yao (2000), nhóm học sâu (2018), Wigderson (2023):** độ phức tạp, học máy, tính ngẫu nhiên.

Các động từ hay gặp là *mở ra*, *tiên phong*, *định hình*, *đặt nền tảng*. Giải Turing ghi nhận những thay đổi cả một lĩnh vực tính toán, chứ không chỉ một sản phẩm phần mềm.

### Ví dụ làm từng bước: "Giải phẫu" một lời trích dẫn Giải Turing thành phép tính cụ thể

Khi đọc trích dẫn Giải Turing 2012 của Shafi Goldwasser và Silvio Micali (*"transformative work that laid the complexity-theoretic foundations for the science of cryptography"*), đừng chỉ đọc lướt qua các tính từ khen ngợi. Hãy bóc tách đúng một ý tưởng cốt lõi bên trong — **mã hóa xác suất** — bằng phép tính số nhỏ modulo $$N = 3 \times 5 = 15$$:

- Giả sử bạn muốn mã hóa một bit bí mật $$b \in \{0, 1\}$$ (ví dụ `0 = Mua`, `1 = Bán`).
- Nếu dùng hàm tất định (như RSA thuần không phần đệm), lần nào mã hóa `0` cũng ra đúng một số cố định — kẻ nghe lén chỉ cần thấy hai bản mã giống nhau là biết ngay hôm nay bạn lặp lại lệnh hôm qua!
- Goldwasser–Micali đảo ngược cách làm bằng **thặng dư bậc hai modulo $$N = 15$$**: chọn ngẫu nhiên một số $$r$$ nguyên tố cùng nhau với 15 (tập $$\{1,2,4,7,8,11,13,14\}$$):
  - Để mã hóa bit `0`, gửi $$c = r^2 \bmod 15$$ (với $$r=2 \implies c=4$$; với $$r=4 \implies c=1$$).
  - Để mã hóa bit `1`, nhân thêm một số không phải bình phương $$z = 2$$: gửi $$c = 2r^2 \bmod 15$$ (với $$r=2 \implies c=8$$; với $$r=4 \implies c=2$$).
- Kết quả: cùng gửi bit `0` hai lần nhưng bản mã lúc ra `4`, lúc ra `1`! Người biết thừa số $$p=3, q=5$$ kiểm tra bình phương modulo 3 và 5 trong chớp mắt, còn kẻ chỉ biết $$N$$ lớn hàng nghìn bit không thể phân biệt nổi bản mã của `0` và `1`. Từ một câu trích dẫn ngắn của Giải Turing, ta chạm thẳng vào một cơ chế toán học rõ mồn một!

### Giải thích: Quy trình 4 bước đọc một Giải Turing bằng con mắt người làm toán–tin

1. **Gạch chân các danh từ kỹ thuật trong lời trích dẫn:** tách khỏi lời khen xã giao để tìm đúng đối tượng toán học (máy Turing, phép quy dẫn, mã hóa xác suất, đồ thị nhân quả, bộ sinh giả ngẫu nhiên).
2. **Xác định tầng câu hỏi mà công trình trả lời:** nó thuộc tầng *tính được* (Turing), tầng *ranh giới P vs NP* (Cook–Karp), tầng *tối ưu bên trong P* (Knuth, Hopcroft–Tarjan), tầng *bảo mật/tương tác* (RSA, Goldwasser–Micali), hay tầng *học & nhân quả* (Valiant, Pearl)?
3. **Thử trên một ví dụ cỡ nhỏ bằng tay:** tự chạy một đồ thị 4 đỉnh, một ma trận $$2\times 2$$ hay một phép chia dư modulo 15 để thấy cơ chế thực sự vận hành chứ không chỉ nhớ khẩu hiệu.
4. **Kiểm tra giới hạn và câu hỏi còn mở:** mọi Giải Turing đều mở ra biên giới mới — hỏi xem giả định nào vẫn chưa chứng minh được (ví dụ $$\mathbf{P}\neq\mathbf{NP}$$, độ khó phân tích thừa số hay giả thiết khử ngẫu nhiên $$\mathbf{BPP}=\mathbf{P}$$).

**Kiểm tra nhanh.** Giải Turing vinh danh **nền tảng và ngôn ngữ làm việc mới của cả ngành**, không nhất thiết là lời giải của một bài toán Thiên niên kỷ (như Cook–Karp nhận giải dù P vs NP vẫn còn mở).

---

## 3. Giải Turing so với các giải khác

| Giải | Chu kỳ / tuổi | Điểm nhấn thường gặp |
|------|---------------|----------------------|
| **Fields** | 4 năm một lần; dưới 40 tuổi | Đột phá của toán thuần túy, thường là một định lý nổi bật |
| **Abel** | Hằng năm; không giới hạn tuổi | Cả sự nghiệp toán học, định hình một lĩnh vực |
| **Giải Turing** | Hằng năm (thường lệ); không giới hạn tuổi như Fields | Nền tảng khoa học máy tính; lý thuyết và/hoặc hệ thống |
| **Clay Millennium** | Dành cho bài toán, không phải cho người | Bảy bài toán mở có tiền thưởng cho lời giải (gồm P vs NP) |
| **Nobel** | Hằng năm theo từng hạng mục | Không có tin học thuần túy; có vật lý, hóa học, y học, … |

Có ba điểm khác biệt cần nhớ.

Thứ nhất, **giải Turing không phải "giải Abel của tin học"** theo nghĩa sao chép. Abel và Turing cùng ghi nhận tác động lâu dài, nhưng đối tượng và cộng đồng khác nhau: một bên là giới toán học, một bên là ACM và cộng đồng khoa học máy tính toàn cầu. Một số nhà khoa học (ví dụ Wigderson, Abel 2021 và Turing 2023) được cả hai cộng đồng ghi nhận. Đó là dấu hiệu của sự giao thoa giữa các ngành, không phải sự trùng lặp vô nghĩa.

Thứ hai, **Fields và giải Turing đo hai thứ khác nhau.** Fields bắt lấy những đột phá sớm trong toán thuần túy; giải Turing thường ghi nhận những ý tưởng đã trở thành **ngôn ngữ mặc định** của thuật toán, mật mã hoặc hệ thống, đôi khi sau nhiều thập kỷ lan rộng.

Thứ ba, **giải của Clay không trao cho người.** P vs NP là một bài toán Thiên niên kỷ; còn Cook–Karp là câu chuyện về **phương pháp và các lớp bài toán** khiến câu hỏi đó trở thành trung tâm. Khi học chương này, bạn cần giữ cả hai: bài toán còn mở và hệ thống khái niệm xung quanh nó.

---

## 4. “Nền tảng tính toán” hiểu như một ý tưởng toán học

Nó không chỉ có nghĩa là "nhiều bài báo" hay "công ty khởi nghiệp thành công". Nó có nghĩa là công cụ của nhà nghiên cứu trở thành **mặc định**: định nghĩa lớp độ phức tạp mà ai cũng trích dẫn, phép quy dẫn (reduction) mà sách giáo khoa nào cũng dạy, giao thức khóa công khai mà mọi trình duyệt dùng, cách phân tích thời gian–bộ nhớ mà khóa thuật toán nào cũng nhắc đến. Sau đó, ngôn ngữ của cả lĩnh vực thay đổi. Sinh viên học những môn chưa từng tồn tại trước đó; các ngành lân cận (toán, vật lý thống kê, kinh tế, sinh học tính toán) mượn từ vựng; các bài toán mở được phát biểu lại bằng "phương ngữ" mới.

Những ví dụ trong chương (sẽ được trình bày ở các bài sau): máy Turing và tính không quyết định được; định lý Cook–Levin và danh sách bài toán của Karp; phân tích tiệm cận theo kiểu Knuth; Diffie–Hellman và RSA; Goldwasser–Micali và zero-knowledge. Mỗi thứ là một phần của **hạ tầng** hơn là một "mẹo lập trình".

Có thể tự hỏi: *nếu xóa công trình này khỏi tài liệu, định lý hay hệ thống nào sau đó sẽ khó phát biểu hơn nhiều?* Đó là cách hiểu thực dụng về "nền tảng".

---

## 5. Cách học chương này

Bốn bước cho mỗi bài từ 09_03 trở đi:

1. **Đọc kỹ câu trích dẫn** (chép từ amturing.acm.org nếu được).  
2. **Nhận ra đối tượng toán–tin** (lớp bài toán, mô hình, giao thức, định lý).  
3. **Phát biểu một ý giải thích được** bằng lời thường (một đoạn).  
4. **Ghi một liên hệ với khóa học**: P vs NP ở ch.01, mật mã ch.03, độ phức tạp ch.06, Abel/Wigderson ch.08, AI ch.06.

Hãy tránh hai lỗi: **sùng bái cá nhân mà không hiểu cơ chế**, và **nói quá** (giải Turing cho học sâu không có nghĩa là "AI đã giải được bài toán ý thức"; NP-đầy đủ không có nghĩa là "mọi trường hợp thực tế đều không thể giải"; mật mã khóa công khai không có nghĩa là "an toàn tuyệt đối").

Chương 09 nằm cạnh [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Lý thuyết độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Lý thuyết số và mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), và [Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/). Hãy đọc để hiểu **cơ chế**, đừng đọc để nhớ năm trao giải.

---

## 6. Alan Turing trong bức tranh của giải thưởng

Năm 1936, Turing định nghĩa **hàm tính được** qua máy với băng và trạng thái, xây dựng **máy phổ quát** (hạt nhân của khái niệm "phần mềm"), và chứng minh **bài toán dừng** là không quyết định được. Công việc ở Bletchley Park gắn với mật mã thời chiến; bài báo năm 1950 về trí tuệ máy là một gợi ý mang tính triết học, **không** phải một định lý về độ phức tạp. Những người đoạt giải sau này không lặp lại năm 1936: họ mở ra các tầng **hiệu quả**, **an toàn**, **học máy** và **hệ thống** trên nền tảng "điều gì tính được". Chi tiết ở [bài 09_03]({{ site.baseurl }}/contents/vi/chapter09/09_03_Turing_Computability/).

---

## 7. Những nhầm lẫn thường gặp

| Nhận định | Chỉnh lại |
|-----------|-----------|
| “Alan Turing nhận giải Turing.” | **Sai.** Ông mất năm 1954; giải được trao từ **1966**. |
| “Giải Turing là Nobel của tin học.” | Chỉ là cách nói ví von của báo chí. Đây là giải của ACM, không phải hạng mục Nobel. |
| “Giải Turing chỉ dành cho lý thuyết.” | Nhiều năm giải ghi nhận hệ thống, kiến trúc máy tính, mạng, đồ họa, học máy thực nghiệm. Chương này chỉ chọn những năm giàu toán học. |
| “Fields hơn / giải Turing hạng hai.” | Hai giải đo những điều khác nhau và thuộc về cộng đồng khác nhau; không có xếp hạng tuyệt đối. |
| “Lời trích dẫn chứng minh mọi khẩu hiệu báo chí.” | Báo chí nén thông tin. Hãy tách định lý và giao thức khỏi các ẩn dụ. |
| “Clay giống giải Turing.” | Clay thưởng cho **bài toán**; giải Turing vinh danh **con người và công trình nghiên cứu**. |
| “Biết tên người đoạt giải là hiểu khoa học.” | Mục tiêu của khóa học là hiểu cơ chế: phép quy dẫn, máy Turing, hàm cửa sập, zero-knowledge. |

---

## Video và tài liệu

Hãy dùng video để làm quen với bối cảnh và văn hóa nghiên cứu, không dùng thay cho chứng minh.

Video gợi ý: danh sách các bài giảng nhận giải Turing của ACM: [https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6](https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6).

Trang chính thức và tài liệu:

- Trang chủ giải ACM A.M. Turing: https://amturing.acm.org/  
- Danh sách theo năm: https://amturing.acm.org/byyear.cfm  
- Danh sách theo vần: https://amturing.acm.org/alphabetical.cfm  
- Giải Abel (để đối chiếu): https://abelprize.no/  
- ACM giới thiệu về giải: https://www.acm.org/about-acm/acm-history/acm-awards/turing-award  
- Wikipedia, Turing Award: https://en.wikipedia.org/wiki/Turing_Award  
- Wikipedia, Alan Turing: https://en.wikipedia.org/wiki/Alan_Turing  
- Wikipedia, Association for Computing Machinery: https://en.wikipedia.org/wiki/Association_for_Computing_Machinery  

## Tài liệu tham khảo

1. [ACM A.M. Turing Award](https://amturing.acm.org/): trích dẫn, tiểu sử, bài giảng.  
2. Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem.  
3. [Tổng quan chương 09]({{ site.baseurl }}/contents/vi/chapter09/09_00_Tong_quan/); [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/); [Tổng quan Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
4. Sipser, M. *Introduction to the Theory of Computation*: giới thiệu máy Turing và độ phức tạp cho người mới học.

## Hướng đi tiếp

- So sánh bảng trong bài này với [Abel]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/) và [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/): nêu ba khác biệt chính xác.  
- Diễn đạt ý tưởng cốt lõi của giải Turing trong một đoạn cho người không học tin học.  
- Ghi một câu hỏi còn mở bên cạnh mỗi lời trích dẫn trong chương (P vs NP, an toàn cụ thể, khử ngẫu nhiên, …).  
- Bài tiếp theo: [Turing, Tính được và Bất khả quyết định]({{ site.baseurl }}/contents/vi/chapter09/09_03_Turing_Computability/).

Cách đọc một năm trao giải: gạch chân các danh từ, phân loại (tính toán được / độ phức tạp / thuật toán / mật mã / hệ thống / học máy), rồi nối với [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) hoặc [Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

## Video tham khảo

- **Xem trước** — [Celebrating 50 Years of the ACM A.M. Turing Award and Computing's Greatest Achievements](https://www.youtube.com/watch?v=MuTGa_xvCgc) — ACM, tiếng Anh. Giới thiệu về 50 năm giải Turing và những thành tựu lớn của ngành.
- [“Computer Science as a Major Body of Accumulated Knowledge,” at ACM Turing 50 Celebration](https://www.youtube.com/watch?v=ACsQ4ixtqTc) — ACM, tiếng Anh. Xem sau khi đã nắm ý chính.
- [Turing the Man](https://www.youtube.com/watch?v=nvwK-11uxSo) — ACM, tiếng Anh. Góc nhìn bổ sung về con người Turing.
