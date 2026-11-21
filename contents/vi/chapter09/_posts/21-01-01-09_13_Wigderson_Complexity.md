---
layout: post
title: "Wigderson: Ngẫu nhiên, Chứng minh và Độ phức tạp (Turing 2023)"
chapter: '09'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Avi Wigderson** nhận **Giải Turing (A.M. Turing Award) năm 2023** vì những đóng góp nền tảng cho lý thuyết tính toán, đặc biệt là vai trò của **tính ngẫu nhiên trong tính toán**, lý thuyết độ phức tạp, và việc ông đưa khoa học máy tính lý thuyết trở thành một ngành toán học đúng nghĩa. Trước đó, ông đã cùng László Lovász chia sẻ **Giải Abel năm 2021**. Hiếm có ai nhận được cả hai: một bên là vinh dự cao nhất của ngành tính toán, bên kia là giải thưởng trọn đời của toán thuần túy, và hai bên cùng đặt trên một vùng tri thức chồng lấn nhau.

Bài này trình bày các chủ đề của Wigderson ở mức nhập môn: tính ngẫu nhiên như một loại tài nguyên; khử ngẫu nhiên (derandomization) và mô hình “độ cứng đổi lấy tính ngẫu nhiên” (hardness versus randomness); **chứng minh tương tác** và sức mạnh của việc kết hợp tương tác với ngẫu nhiên khi kiểm chứng; đồ thị giãn (expander) và tính giả ngẫu nhiên như cầu nối sang toán rời rạc; và cách đọc câu chuyện giải Turing *cùng với* [bài về giải Abel của Lovász và Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/). Tài liệu chính thức: [amturing.acm.org](https://amturing.acm.org/), [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- giải thích vì sao tính ngẫu nhiên được xem là tài nguyên tính toán, ngang với thời gian và bộ nhớ;
- phát biểu tóm tắt kết quả về khử ngẫu nhiên: nếu có những giả thiết thích hợp về độ cứng thì tồn tại bộ sinh giả ngẫu nhiên hiệu quả, và các lớp thuật toán ngẫu nhiên “sụp” về phía lớp tất định;
- mô tả hệ chứng minh tương tác như một mô hình kiểm chứng vượt ra ngoài chứng cứ tĩnh của lớp NP;
- gọi tên đồ thị giãn: đồ thị thưa nhưng trộn nhanh, dùng làm đối tượng giả ngẫu nhiên;
- nối giải Turing 2023 với giải Abel 2021 mà không nói rằng giải nào đã giải được [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

**Kiến thức cần có và các bài liên quan.** [Lý thuyết độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Yao: giao tiếp và minimax]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/), [giải Abel của Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/), [lý thuyết đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/). Trang tổng quan của chương: [Tổng quan Turing]({{ site.baseurl }}/contents/vi/chapter09/09_00_Tong_quan/).

---

## 1. Hai giải thưởng, một danh tính toán học

Giải Abel 2021 tôn vinh Lovász và Wigderson vì đã đưa toán rời rạc và khoa học máy tính lý thuyết vào vị trí trung tâm của toán học hiện đại. Giải Turing 2023 đặt ánh nhìn của cộng đồng tính toán vào vai trò dẫn dắt của Wigderson trong lý thuyết độ phức tạp: tính ngẫu nhiên, mối liên hệ với độ phức tạp mạch, hệ chứng minh, thuật toán, và nhiều thập niên xây dựng cả một lĩnh vực (kể cả cuốn sách phổ biến *Mathematics and Computation*).

Với khóa học này, việc một người nhận cả hai giải là ví dụ rất đáng giá. Nhiều sinh viên nghĩ “Turing là kỹ thuật” còn “Abel là toán thuần”, và đây là phản ví dụ: cùng một nhóm định lý về đồ thị giãn, khử ngẫu nhiên và chứng minh tương tác thuộc về **cả hai** thế giới.

---

## 2. Tính ngẫu nhiên như một tài nguyên

Thuật toán ngẫu nhiên có thể tung đồng xu. Lớp **BPP** gồm các ngôn ngữ quyết định được trong thời gian đa thức, với xác suất sai hai phía bị chặn. Trong lịch sử, tính ngẫu nhiên dường như mang lại sức mạnh thật: kiểm tra đồng nhất thức đa thức (polynomial identity testing), một số thuật toán trên đồ thị, hàm băm, lấy mẫu, và các giao thức giao tiếp ([Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/)).

Lý thuyết độ phức tạp đặt ra những câu hỏi sắc hơn:

- Ngẫu nhiên có *thật sự cần thiết* không, hay mọi thuật toán ngẫu nhiên hiệu quả đều có thể được mô phỏng hiệu quả mà không cần đồng xu?  
- Cần tối thiểu bao nhiêu bit ngẫu nhiên?  
- Ngẫu nhiên tác động qua lại thế nào với tương tác, với tính không đồng nhất (mạch), và với tính giả ngẫu nhiên trong mật mã?

Công trình của Wigderson xem các câu hỏi này là toán học về cấu trúc, chứ không chỉ là kỹ thuật thiết kế thuật toán.

---

## 3. Độ cứng đổi lấy tính ngẫu nhiên

### Bộ sinh giả ngẫu nhiên (PRG)

Một **bộ sinh giả ngẫu nhiên** (PRG) kéo dài một hạt giống (seed) ngẫu nhiên ngắn thành một chuỗi dài trông như ngẫu nhiên đối với một lớp phép thử hiệu quả (ví dụ các mạch có kích thước bị chặn). Nếu tồn tại PRG đủ mạnh, một thuật toán cần nhiều bit ngẫu nhiên có thể duyệt qua tất cả các seed, hoặc dùng chuỗi đã kéo dài, mà vẫn đạt bảo đảm tương đương. Đó là **khử ngẫu nhiên** (derandomization).

### Mô hình chung

Một ý tưởng sâu sắc của độ phức tạp hiện đại:

> **Độ cứng tính toán** có thể được biến thành **tính giả ngẫu nhiên**. Nếu có một hàm đủ khó đối với các mạch, ta dựng được PRG đánh lừa được các mạch nhỏ hơn, và suy ra hệ quả khử ngẫu nhiên, chẳng hạn $$\mathbf{BPP}$$ nằm trong lớp thời gian tất định dưới mũ, hoặc thậm chí thời gian đa thức, với giả thiết đủ mạnh.

Ngược lại, việc khử ngẫu nhiên không tầm thường thường kéo theo chặn dưới cho mạch. Độ cứng và tính ngẫu nhiên là hai mặt của cùng một lý thuyết.

**Lưu ý.** Đây là các định lý **có điều kiện** và là một chương trình nghiên cứu. Bản thân chúng **không** giải được P vs NP. Chúng cho thấy: nếu sống trong một thế giới có chặn dưới thì ta được lợi ích về thuật toán; ngược lại, tham vọng khử ngẫu nhiên thuật toán lại chồng lên nghiên cứu về chặn dưới.

---

## 4. Chứng minh tương tác

### Vượt ra ngoài chứng cứ của NP

Trong **NP**, người chứng minh (prover) có sức mạnh lớn gửi một chứng cứ ngắn, còn người kiểm tra (verifier) chạy trong thời gian đa thức để kiểm chứng. **Hệ chứng minh tương tác** cho phép nhiều vòng trao đổi, thường kèm tính ngẫu nhiên ở phía người kiểm tra. Kết quả **IP = PSPACE** (Shamir, dựa trên dòng công trình của Lund–Fortnow–Karloff–Nisan) là một cột mốc: tương tác cộng ngẫu nhiên có thể kiểm chứng những ngôn ngữ được tin là khó hơn NP rất nhiều.

### Chứng minh không tiết lộ tri thức và văn hóa chứng minh

**Chứng minh không tiết lộ tri thức** (zero-knowledge) thuyết phục người kiểm tra rằng một mệnh đề là đúng, mà không để lộ thêm điều gì khác ngoài những gì người đó vốn có thể tự tính được. Khái niệm này giữ vai trò trung tâm trong mật mã, và trong quan niệm hiện đại “chứng minh là một giao thức”. Các đóng góp và hợp tác của Wigderson giúp xây nền tảng độ phức tạp cho hệ chứng minh, cũng như cho việc kiểm chứng tiết kiệm bit ngẫu nhiên.

### Chứng minh như một giao thức

Trong khoa học máy tính lý thuyết, “chứng minh” không chỉ là một tệp PDF tĩnh gồm các bước suy luận. Nó có thể là một **giao thức** với sai số về tính đúng đắn (soundness) và sai số về tính đầy đủ (completeness), được phân tích như một thuật toán. Chính sự thay đổi về quan niệm này là tầm vóc của giải Turing.

---

## 5. Đồ thị giãn và các đối tượng giả ngẫu nhiên

Một họ vô hạn các đồ thị $$d$$-chính quy là **họ đồ thị giãn** (expander) nếu mọi tập đỉnh nhỏ đều giãn nở với một hệ số xác định. Điều này tương đương với việc khoảng cách phổ (spectral gap) bị chặn dưới, không phụ thuộc kích thước đồ thị. Đồ thị giãn làm bước đi ngẫu nhiên trộn rất nhanh dù đồ thị thưa. Chúng là những đối tượng tất định nhưng **cư xử như thể ngẫu nhiên**.

Ứng dụng gồm:

- khử ngẫu nhiên và khuếch đại xác suất thành công một cách tất định;  
- mã sửa lỗi;  
- thiết kế mạng có độ bền cao;  
- cầu nối sang toán thuần (lý thuyết nhóm, hình học phổ), cũng xuất hiện trong câu chuyện giải Abel cùng các cách dựng kiểu Margulis (xem thêm [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/)).

Trong thế giới của Wigderson, đồ thị giãn là công cụ chuẩn, giống như cơ sở Fourier đối với người làm giải tích. Xem thêm phần về đồ thị giãn trong [bài về giải Abel của Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

---

## 6. Độ phức tạp như hình học của tính toán hiệu quả

Các bài viết phổ biến của Wigderson trình bày những chủ đề của khoa học máy tính lý thuyết (mạch, phép quy dẫn, tính ngẫu nhiên, tối ưu, mật mã) như một ngành toán học thực thụ, có định nghĩa, định lý và những bài toán mở về độ khó giống như các bài toán của Hilbert. [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn chưa có lời giải, nhưng xung quanh nó đã có nhiều thành tựu lớn: IP = PSPACE, định lý PCP và độ cứng của xấp xỉ, các cách dựng đồ thị giãn, các định lý khử ngẫu nhiên có điều kiện, và các chặn dưới cho độ phức tạp giao tiếp.

Khi một bài báo phổ thông viết “lý thuyết độ phức tạp thất bại vì P vs NP còn mở”, hãy đáp lại bằng danh sách các định lý **không** cần đến kết quả đó. Giải thưởng trọn đời vinh danh **cả kiến trúc của một lĩnh vực**.

### Giảm sai số mà tiết kiệm bit ngẫu nhiên

Một chủ đề nhỏ nhưng cụ thể: giả sử một thuật toán BPP dùng nhiều bit ngẫu nhiên và sai với xác suất $$1/3$$. Nếu chạy lặp lại độc lập thì sai số giảm theo hàm mũ, nhưng số bit ngẫu nhiên cũng tăng theo. **Bước đi ngẫu nhiên trên đồ thị giãn** và các đối tượng giả ngẫu nhiên liên quan giảm được sai số mà tái sử dụng bit ngẫu nhiên tiết kiệm hơn nhiều: cấu trúc đồ thị tất định thay cho những đồng xu mới. Đây là phiên bản thu nhỏ của cả chương trình nghiên cứu: một cách dựng tổ hợp tiết kiệm tài nguyên, trong khi cách làm xác suất ngây thơ phải trả bằng các mẫu độc lập.

### Mạch, tính không đồng nhất và thông tin trợ giúp

Độ phức tạp phân biệt thuật toán **đồng nhất** (một máy dùng cho mọi độ dài đầu vào) với **họ mạch** (mỗi độ dài đầu vào có thể dùng một mạch khác). Các định lý khử ngẫu nhiên thường nói về ngôn ngữ của mạch, vì các “phép thử” mà PRG phải đánh lừa là không đồng nhất. Lý thuyết theo kiểu Wigderson di chuyển thoải mái giữa các lớp đồng nhất (P, BPP) và không đồng nhất (P/poly). Đây là kiến thức cần có để đọc các bài báo hiện đại, dù bài này không dựng PRG từ hàm khó theo từng bước.

### Không tiết lộ tri thức như một định nghĩa về “biết”

Ngoài IP = PSPACE, **không tiết lộ tri thức** là cách hình thức hóa việc thuyết phục người khác mà không dạy họ điều gì. Định nghĩa này đã thay đổi mật mã (các giao thức nhận dạng, hệ chứng minh hiện đại) và gợi ra những câu hỏi gần với triết học về tri thức. Đây là ví dụ điển hình về việc khoa học máy tính lý thuyết đưa ra một *định nghĩa* có sức nặng ngang một định lý: khi “không tiết lộ tri thức” đã được phát biểu chính xác, ta có thể chứng minh một giao thức đạt được tính chất đó dưới những giả thiết nhất định, ghép các giao thức lại với nhau, và kiểm tra những lời quảng cáo rằng hệ thống “không tiết lộ gì”.

### Đọc Wigderson bên cạnh Yao

[Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/) nhấn mạnh các chặn dưới cho giao tiếp và nguyên lý minimax nối độ phức tạp ngẫu nhiên với độ phức tạp theo phân bố. Wigderson nhấn mạnh khi nào có thể **bỏ** tính ngẫu nhiên và khi nào tương tác làm tăng sức mạnh của chứng minh. Đặt hai hướng cạnh nhau, ta thấy hai đầu của vấn đề: đôi khi đồng xu là cần thiết, xét theo thông tin hoặc theo độ phức tạp trong một mô hình nào đó; đôi khi độ cứng lại tạo ra những “đồng xu” đủ tốt cho một thuật toán hiệu quả. Câu hỏi tổng hợp: chọn một bài toán, rồi lập luận xem bạn đang ở trường hợp “ngẫu nhiên có ích, và có chặn dưới” hay “khử ngẫu nhiên được nhờ độ cứng”.

---

## 7. Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|--------|
| “Giải Turing 2023 hay giải Abel 2021 đã giải P vs NP.” | Không. Cả hai vinh danh những đóng góp nền tảng; P vs NP vẫn còn mở. |
| “BPP trong thực tế chỉ là P, nên tính ngẫu nhiên vô nghĩa.” | Khử ngẫu nhiên trong thực hành khác với việc chứng minh; lý thuyết có cấu trúc sâu và phần lớn kết quả mang tính có điều kiện. |
| “Chứng minh tương tác giống hệt chứng cứ của NP.” | Tương tác và ngẫu nhiên làm thay đổi mô hình của người kiểm tra; IP = PSPACE là một định lý lớn. |
| “Đồ thị giãn chỉ là đồ thị ngẫu nhiên.” | Đồ thị ngẫu nhiên thường là đồ thị giãn; điểm quan trọng còn là cách dựng **tường minh** và việc dùng chúng một cách tất định. |
| “Khử ngẫu nhiên nghĩa là bỏ xác suất ra khỏi khoa học.” | Nghĩa là gỡ sự phụ thuộc của thuật toán vào bit ngẫu nhiên dưới các ràng buộc tài nguyên, chứ không phủ nhận mô hình xác suất của dữ liệu. |
| “Wigderson chỉ làm về chặn dưới.” | Chương trình nghiên cứu của ông trải rộng: thuật toán, tính giả ngẫu nhiên, chứng minh và cả giáo dục. |

---

## Bài tập

1. Nêu (ở mức tóm tắt) một bài toán mà thuật toán ngẫu nhiên đơn giản hơn hoặc nhanh hơn.  
2. PRG đang cố đánh lừa điều gì, và vì sao điều đó giúp khử ngẫu nhiên một thuật toán?  
3. Độ cứng và tính ngẫu nhiên: giải thích con đường hai chiều giữa chúng trong không quá 150 từ.  
4. Chứng minh tương tác khác việc kiểm tra chứng cứ NP cổ điển ở điểm nào?  
5. Định nghĩa họ đồ thị giãn trong một câu (theo độ giãn nở hoặc theo khoảng cách phổ).  
6. **Tối đa 250 từ:** vì sao cùng một người có thể nhận cả giải Abel và giải Turing cho những công trình liên quan? Hãy dựa vào lời ghi nhận của hai giải.  
7. Liệt kê ba định lý của khoa học máy tính lý thuyết vẫn thú vị ngay cả khi P = NP (dùng lại cách nghĩ ở bài về giải Abel).  
8. Xem trang giải Turing của Wigderson tại [amturing.acm.org](https://amturing.acm.org/) và tài liệu về giải Abel 2021; viết ra bốn từ khóa xuất hiện ở cả hai nơi.

---


## Video và tài liệu

Video gợi ý, dùng để làm quen với bối cảnh chứ không thay cho chứng minh. Lưu ý: giải Turing của Wigderson là năm **2023** (không phải 2021); giải Abel chung với Lovász là năm **2021**.

1. **Nên xem trước:** bài giảng nhận giải Turing của Wigderson (ACM): [https://www.youtube.com/watch?v=f2NiGO8zC1c](https://www.youtube.com/watch?v=f2NiGO8zC1c).  
2. Hỏi đáp với Wigderson tại IAS: [https://www.youtube.com/watch?v=TK_vD-VnsFw](https://www.youtube.com/watch?v=TK_vD-VnsFw).  
3. Bài giới thiệu Wigderson trên CACM, 6/2024: [https://www.youtube.com/watch?v=Ur9XNF6TeYw](https://www.youtube.com/watch?v=Ur9XNF6TeYw).  
4. Liên quan: Wigderson, *Reading Alan Turing* (Berkeley): [https://www.youtube.com/watch?v=BiFSUniv70c](https://www.youtube.com/watch?v=BiFSUniv70c).  
5. Các bài giảng Abel của Lovász và Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/wigderson-complexity_f2NiGO8zC1c_thumb.jpg)

*Hình. Khung hình mẫu từ video đầu tiên.*

## Tài liệu tham khảo trực tuyến


1. Trang giải Turing 2023 của Wigderson — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
2. Trang bài giảng nhận giải Turing của Wigderson — https://amturing.acm.org/vp/wigderson_3844537.cfm  
3. Wigderson Turing Award Lecture (ACM) — https://www.youtube.com/watch?v=f2NiGO8zC1c  
4. IAS Q&A Wigderson Turing — https://www.youtube.com/watch?v=TK_vD-VnsFw  
5. CACM June 2024 Wigderson feature — https://www.youtube.com/watch?v=Ur9XNF6TeYw  
6. Wigderson — Reading Alan Turing (Berkeley) — https://www.youtube.com/watch?v=BiFSUniv70c  
7. Giải Abel 2021 của Lovász và Wigderson — https://abelprize.no/abel-prize-laureates/2021  
8. Các bài giảng Abel của Lovász và Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
9. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
10. Danh sách theo năm (xác nhận năm 2023) — https://amturing.acm.org/byyear.cfm  
11. Sách *Mathematics and Computation* — https://www.math.ias.edu/avi/book  

1. ACM Turing Award 2023 — Avi Wigderson — [amturing.acm.org](https://amturing.acm.org/).  
2. Abel Prize 2021 — Lovász & Wigderson — [abelprize.no](https://abelprize.no/).  
3. A. Wigderson, *Mathematics and Computation* (Princeton); Arora–Barak, *Computational Complexity*; bài tổng quan của Vadhan về tính giả ngẫu nhiên.  
4. Trong khóa: [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/); [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/); [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/).

---

## Hướng đi tiếp

- Đọc một chương của *Mathematics and Computation*, viết cho độc giả toán thuần.  
- So sánh phương pháp chặn dưới minimax của Yao với tham vọng khử ngẫu nhiên dựa trên PRG.  
- Tìm hiểu cách dựng một đồ thị giãn cụ thể (ít nhất là lịch sử về sự tồn tại và các cách dựng tường minh kiểu Margulis).  
- Sau khi nắm IP = PSPACE, xem thoáng qua vai trò của định lý PCP trong độ cứng của xấp xỉ.  
- Bài tiếp theo: [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/), gồm quyền riêng tư, tối ưu hóa và lý thuyết học máy, mã hóa, thuật toán lượng tử và kiểm chứng hình thức.

## Video tham khảo

- **Xem trước** — [Avi Wigderson Turing Award Lecture: “Alan Turing: A TCS Role Model”](https://www.youtube.com/watch?v=f2NiGO8zC1c) — Association for Computing Machinery (ACM), tiếng Anh. Xem trước để làm quen với chủ đề.
- [Avi Wigderson, 2023 Turing Award Laureate, Q&A with David Nirenberg | Institute for Advanced Study](https://www.youtube.com/watch?v=TK_vD-VnsFw) — Institute for Advanced Study, tiếng Anh. Xem sau khi đã nắm ý chính.
- [June 2024 CACM: Avi Wigderson, 2023 ACM A.M. Turing Awardee](https://www.youtube.com/watch?v=Ur9XNF6TeYw) — Association for Computing Machinery (ACM), tiếng Anh. Góc nhìn bổ sung.
