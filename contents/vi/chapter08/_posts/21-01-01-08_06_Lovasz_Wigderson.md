---
layout: post
title: "Lovász & Wigderson: Toán rời rạc và TCS (Abel 2021)"
chapter: '08'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

Có một thời, trong những giảng đường toán học cổ điển, các bài toán về đồ thị, mạng lưới hay tốc độ thuật toán từng bị xem là "vùng ngoại ô"—hữu ích cho kỹ sư máy tính, nhưng kém phần uy nghi so với hình học đại số hay giải tích hàm. Thế nhưng chính từ vùng ngoại ô ấy lại nảy sinh một trong những câu hỏi sâu sắc nhất của nhân loại ($$P \text{ vs } NP$$), cùng những cấu trúc làm rung chuyển cả mật mã học, tối ưu hóa và chính toán học thuần túy: làm sao chứng minh một cấu hình tổ hợp tồn tại giữa hàng triệu ràng buộc chồng chéo? Và liệu việc tung đồng xu có thật sự giúp máy tính thông minh hơn không?

Năm **2021**, **Giải Abel** được trao chung cho **László Lovász** và **Avi Wigderson** như một tuyên ngôn lịch sử của cộng đồng toán học:

> “for their foundational contributions to theoretical computer science and discrete mathematics, and their leading role in shaping them into central fields of modern mathematics.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2021)

Từ bổ đề địa phương Lovász và thuật toán rút gọn mạng lưới LLL cho đến cuộc cách mạng khử ngẫu nhiên, chứng minh không tiết lộ thông tin (*zero-knowledge*) và đồ thị expander của Wigderson, hai sự nghiệp này đã kéo toán rời rạc và khoa học máy tính lý thuyết (TCS) vào đúng trung tâm của toán học hiện đại—ngay bên cạnh [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), dù bài toán triệu đô ấy vẫn còn đang mở. Tài liệu chính thức: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể giải thích vì sao toán rời rạc và TCS xứng đáng với giải Abel như một phần trung tâm của toán học hiện đại; nêu bổ đề địa phương của Lovász và mục đích của nó (tồn tại cấu hình khi có nhiều sự kiện xấu gần như độc lập); nêu chủ đề tính ngẫu nhiên và khử ngẫu nhiên của Wigderson; mô tả expander như đồ thị thưa nhưng liên thông rất mạnh; và nối tất cả với P vs NP **mà không** tuyên bố bài toán đó đã được giải.

**Kiến thức nền.** Đồ thị (đỉnh, cạnh); xác suất cơ bản; ý niệm một thuật toán tốn thời gian theo kích thước đầu vào. Liên kết: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [đồ thị và mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

---

## Bản đồ kiến thức nền: Toán rời rạc và Lý thuyết độ phức tạp tính toán là gì và nghiên cứu những gì?

Nếu giải tích và hình học vi phân nghiên cứu thế giới **liên tục** (đường cong mượt, dòng chảy, đạo hàm), thì hai lĩnh vực của Lovász và Wigderson nghiên cứu thế giới **rời rạc**—nhưng ở tầng sâu cấu trúc không hề thua kém:

- **Toán rời rạc (Discrete Mathematics):** Nghiên cứu các đối tượng tách biệt có thể đếm được: đồ thị (các đỉnh và cạnh nối, mô hình hóa mạng xã hội, lưới điện hay phân tử), siêu đồ thị, tổ hợp, lưới điểm nguyên (*lattice*) và các bài toán tối ưu rời rạc (như tìm đường đi ngắn nhất, ghép cặp tối ưu, tô màu bản đồ). Điều thú vị mà Lovász chỉ ra là: muốn hiểu sâu một đồ thị rời rạc, cách hiệu quả nhất lại thường là **nhúng nó vào không gian hình học liên tục** (dùng ma trận, trị riêng, đa diện lồi và lập trình nửa xác định dương)!
- **Khoa học máy tính lý thuyết (Theoretical Computer Science – TCS) và Lý thuyết độ phức tạp (Computational Complexity):** Không quan tâm bạn viết code bằng Python hay C++, hay CPU chạy nhanh bao nhiêu GHz. Thay vào đó, ngành này hỏi về **giới hạn căn bản của tính toán**: một bài toán cần tối thiểu bao nhiêu thời gian, bộ nhớ, số bit ngẫu nhiên hay lượng giao tiếp để giải khi kích thước đầu vào $$n$$ tăng lên? Các lớp độ phức tạp như **P** (giải nhanh trong thời gian đa thức), **NP** (kiểm chứng đáp án nhanh), hay **BPP** (giải nhanh nếu được phép tung đồng xu) là bản đồ phân loại độ khó của toàn bộ vũ trụ bài toán.
- **Mối liên hệ bất ngờ:** Hóa ra "độ khó tính toán" không phải là điều xui xẻo—nó chính là **tài nguyên** để xây dựng mật mã bảo vệ Internet và tạo ra các bộ sinh số giả ngẫu nhiên đánh lừa được mọi thuật toán hiệu quả!

---

## 1. Một giải thưởng về văn hóa cũng như về khoa học

Trong nhiều thập niên, đồ thị, thuật toán và độ phức tạp từng bị xem là địa hạt riêng của khoa Khoa học máy tính, tách khỏi "toán thuần túy cốt lõi". Giải Abel 2021 chính thức khép lại ranh giới nhân tạo ấy: toán rời rạc và TCS chứa **những định lý cấu trúc sâu sắc** và tương tác bình đẳng với hình học, đại số, giải tích và xác suất ở trình độ cao nhất.

Hãy đọc kỹ vế thứ hai của lời tuyên dương: *"shaping them into central fields."* Đây là sự vinh danh dành cho những người **kiến tạo lĩnh vực**—qua hàng thập niên định lý nền tảng, những cuốn sách kinh điển, việc đào tạo thế hệ mới và dựng nên các cây cầu liên ngành. Cũng vì thế, đọc citation của Abel 2021 là một bài học về sự tỉnh táo: giải thưởng tôn vinh việc **định hình cả một ngành**, hoàn toàn khác với tin đồn rằng "bài toán P vs NP đã có lời giải".

---

## 2. Lovász: toán rời rạc như một khoa học toán học

### Đồ thị, tối ưu, hình học và thuật toán LLL

Sự nghiệp của László Lovász trải rộng từ lý thuyết đồ thị, tối ưu tổ hợp đến biểu diễn hình học của đồ thị. Một sợi chỉ đỏ xuyên suốt công trình của ông là đưa các công cụ liên tục vào giải quyết cấu trúc rời rạc: **hàm theta Lovász** (dùng lập trình nửa xác định dương để chặn dung lượng Shannon của đồ thị), **thuật toán LLL** (Lenstra–Lenstra–Lovász, tìm cơ sở ngắn cho lưới điểm nguyên—một công cụ lừng danh trong phân tích đa thức, phá mã RSA yếu và xây dựng mật mã hậu lượng tử), và lý thuyết **giới hạn của đồ thị (graphon)** giúp nhìn một đồ thị hàng tỷ đỉnh như một hàm giải tích liên tục.

### Bổ đề địa phương Lovász (Lovász Local Lemma)

Trong tổ hợp, một vũ khí cực mạnh là **phương pháp xác suất** của Paul Erdős: muốn chứng minh tồn tại một cấu hình "tốt" (ví dụ một cách tô màu đồ thị không có tam giác đơn sắc), ta cứ tô màu ngẫu nhiên rồi chứng minh xác suất xảy ra "sự kiện xấu" nhỏ hơn 1. Nhưng phương pháp ngây thơ (dùng bất đẳng thức cộng xác suất—*union bound*) lập tức thất bại khi số sự kiện xấu lên đến hàng tỷ!

**Bổ đề địa phương** (Erdős–Lovász, 1975) giải quyết ngoạn mục thế bế tắc này. Giả sử có rất nhiều "sự kiện xấu" $$A_1, A_2, \dots, A_m$$, mỗi sự kiện có xác suất xảy ra nhỏ ($$\le p$$) và chỉ phụ thuộc vào tối đa $$d$$ sự kiện xấu khác (tức là *phụ thuộc cục bộ*). Bổ đề khẳng định: miễn là $$e \cdot p \cdot (d + 1) \le 1$$, thì dù $$m$$ lớn đến hàng nghìn tỷ đi nữa, xác suất để **không một sự kiện xấu nào xảy ra** vẫn chắc chắn dương:

$$
\mathbb{P}\Big(\bigcap_{i=1}^m A_i^c\Big) > 0.
$$

**Ví dụ cụ thể (Bài toán $$k$$-SAT):** Giả sử bạn có một triệu mệnh đề logic, mỗi mệnh đề chứa $$k = 10$$ biến đúng/sai, và mỗi biến chỉ xuất hiện trong một vài mệnh đề (nên mỗi mệnh đề chỉ dùng chung biến với tối đa $$d$$ mệnh đề khác). Nếu gán Đúng/Sai ngẫu nhiên cho từng biến, xác suất một mệnh đề bị sai là $$p = 2^{-10} = 1/1024$$. Cộng xác suất cho một triệu mệnh đề sẽ vượt xa 1, nên union bound bó tay. Nhưng miễn là $$d \le 375$$, Bổ đề địa phương Lovász lập tức bảo đảm **chắc chắn tồn tại ít nhất một cách gán giá trị thỏa mãn đồng thời cả một triệu mệnh đề!** Về sau, Moser và Tardos còn biến bổ đề tồn tại này thành một thuật toán cực kỳ đơn giản và nhanh chóng để tìm ra nghiệm thật sự.

### Xây dựng một lĩnh vực

Vượt lên từng định lý cụ thể, Lovász đã thiết lập chuẩn mực chứng minh, xây cầu nối vững chắc giữa toán rời rạc với hình học, tối ưu và giải tích, đồng thời dẫn dắt cộng đồng toán học quốc tế (ông từng là Chủ tịch Liên đoàn Toán học Quốc tế IMU). Cụm *"leading role"* trong lời trao giải Abel chính là sự ghi nhận xứng đáng cho tầm vóc đó.

---

## 3. Wigderson: tính ngẫu nhiên, độ phức tạp, giả ngẫu nhiên

### Tính ngẫu nhiên như một tài nguyên

Câu hỏi lớn xuyên suốt sự nghiệp của Avi Wigderson nghe rất giản dị nhưng đầy thách thức: **liệu tung đồng xu có thật sự làm cho máy tính mạnh hơn không?** Nhiều thuật toán nổi tiếng trong thực tế dùng đến sự ngẫu nhiên—ví dụ kiểm tra xem một số 500 chữ số có phải số nguyên tố không (kiểu Miller–Rabin), kiểm tra hai đa thức khổng lồ có đồng nhất không bằng cách thay số ngẫu nhiên, hay băm dữ liệu (*hashing*). Lý thuyết độ phức tạp gọi lớp các bài toán giải nhanh bằng thuật toán ngẫu nhiên là **BPP**, và đặt câu hỏi: liệu $$\mathrm{BPP} = \mathrm{P}$$?

### Khử ngẫu nhiên và nguyên lý "Độ khó đổi lấy Ngẫu nhiên"

**Khử ngẫu nhiên (Derandomization)** là chương trình tìm cách thay thế đồng xu ngẫu nhiên thật bằng một **bộ sinh giả ngẫu nhiên (pseudorandom generator)** hoàn toàn tất định. Đột phá tư tưởng mang dấu ấn Wigderson (cùng Nisan, Impagliazzo và nhiều cộng sự) là nguyên lý **Hardness vs. Randomness**: *nếu tồn tại những bài toán thực sự khó tính toán (đòi hỏi mạch logic kích thước hàm mũ), ta có thể dùng chính độ khó đó để tạo ra các chuỗi bit giả ngẫu nhiên đủ tốt để đánh lừa mọi thuật toán thời gian đa thức!*

Nói cách khác, dưới các giả thiết độ phức tạp rất tự nhiên, **mọi thuật toán ngẫu nhiên nhanh đều có thể chuyển thành thuật toán tất định nhanh** ($$\mathrm{BPP} = \mathrm{P}$$). Thật trớ trêu và tuyệt đẹp: "độ khó tính toán"—thứ tưởng như rào cản của khoa học máy tính—lại biến thành nguyên liệu để loại bỏ nhu cầu tung đồng xu!

### Expander, chứng minh tương tác và Zero-Knowledge

Wigderson cùng cộng sự còn phát minh ra **tích zig-zag** cho đồ thị—một cách dựng hoàn toàn tổ hợp cho họ **đồ thị expander**, dẫn tới lời giải nổi tiếng về không gian bộ nhớ logarit cho bài toán liên thông đồ thị vô hướng ($$\mathrm{SL} = \mathrm{L}$$ của Reingold). Ông cũng là một trong những kiến trúc sư của **chứng minh tương tác** và **chứng minh không tiết lộ thông tin (Zero-Knowledge Proofs)**: chứng minh rằng mọi khẳng định trong lớp NP đều có thể thuyết phục người kiểm tra tin là đúng **mà không tiết lộ bất kỳ một bit bí mật nào về lời giải** (dưới giả thiết mật mã cơ bản)—ý tưởng ngày nay nằm ở trái tim của mật mã học hiện đại và công nghệ bảo mật riêng tư. Cuốn sách *Mathematics and Computation* của ông là bản tuyên ngôn tuyệt đẹp giới thiệu TCS như một nhánh toán học thuần túy cho toàn thể cộng đồng toán học.

---

## 4. Expander: bản đồ các giao điểm

Một họ vô hạn các đồ thị $$d$$-chính quy $$\{G_n\}$$ (mỗi đỉnh chỉ nối với đúng $$d$$ đỉnh khác, ví dụ $$d = 4$$, dù số đỉnh $$n$$ tăng lên hàng triệu) được gọi là **họ expander** nếu mọi tập con đỉnh nhỏ $$S$$ (chiếm không quá một nửa đồ thị) đều có số cạnh đi ra ngoài $$S$$ tỷ lệ thuận với kích thước $$\lvert S\rvert$$—tương đương với việc **khoảng cách phổ** giữa trị riêng lớn nhất và trị riêng lớn thứ hai của ma trận kề bị chặn dưới bởi một hằng số dương độc lập với $$n$$.

Hãy tưởng tượng một mạng truyền thông gồm 1 triệu nút, nhưng mỗi nút chỉ có đúng 4 sợi dây cáp nối ra ngoài. Nếu là lưới vuông thông thường, chỉ cần cắt vài nghìn sợi dây là mạng bị chia đôi; nhưng nếu đó là một **đồ thị expander**, bạn phải cắt tới hàng trăm nghìn sợi dây mới cô lập được một nửa mạng, và một bước đi ngẫu nhiên chỉ cần khoảng $$O(\log n)$$ bước đã lan tỏa gần như đều khắp cả triệu nút!

Hệ quả lan tỏa khắp nơi: bước đi ngẫu nhiên trộn cực nhanh; lý thuyết mã sửa lỗi và khử ngẫu nhiên có những công cụ tường minh; toán thuần túy có lý thuyết đồ thị phổ và các phép dựng từ lý thuyết nhóm. Đây chính là ngã tư nơi ba thế giới gặp nhau: **cấu trúc đồ thị (Lovász)**, **tính giả ngẫu nhiên (Wigderson)**, và **nhóm Lie / động lực học (Margulis, Abel 2020)**.

---

## 5. Bên cạnh P vs NP

[P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn là bài toán Thiên niên kỷ chưa có lời giải, và Giải Abel 2021 **không** giải quyết bài toán đó. Thay vào đó, sự nghiệp của Lovász và Wigderson cho thấy một chân lý sâu sắc về khoa học: **một bài toán lớn còn mở không hề làm cho cả lĩnh vực trở nên trống rỗng.** Xung quanh P vs NP là cả một nền văn minh toán học trưởng thành với vô số định lý khẳng định giá trị độc lập: Bổ đề địa phương, thuật toán LLL, tích zig-zag dựng expander, chứng minh tương tác và zero-knowledge, hay định lý PCP về giới hạn xấp xỉ.

### Độ khó như một đối tượng toán học

Dù P vs NP chưa ngã ngũ, lý thuyết độ phức tạp đối xử với **độ khó** như một đối tượng toán học có cấu trúc chặt chẽ và có thể *khai thác*: phép quy dẫn, tính đầy đủ, hàm một chiều cho mật mã, và nguyên lý biến độ khó thành tính giả ngẫu nhiên. Tương tự, tối ưu tổ hợp của Lovász biến các cấu trúc rời rạc thành hình học đa diện và đối ngẫu với những định lý chặt chẽ thay vì mẹo phỏng đoán (*heuristic*).

---

## 6. Vì sao đáng một giải Abel

Hai sự nghiệp, một thông điệp chung: toán rời rạc và khoa học máy tính lý thuyết không phải công dân hạng hai của toán học. Chúng sở hữu những định lý cấu trúc sâu mang nội dung hình học và đại số; xuất khẩu công cụ sang các ngành toán cổ điển; đặt ra những câu hỏi tầm cỡ Hilbert (như P vs NP); và cung cấp hạ tầng thiết yếu (expander, LLL, bộ sinh giả ngẫu nhiên, zero-knowledge) cho toàn bộ thời đại số.

Cụm từ *"central fields of modern mathematics"* trong lời trao giải không phải là sự "nâng hạng" cho khoa học máy tính—mà là sự **công nhận chính thức** cho vị thế trung tâm mà hai lĩnh vực này đã xác lập suốt nửa thế kỷ qua nhờ những người dẫn đường như Lovász và Wigderson.

---

## 7. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Abel 2021 giải P vs NP.” | Không. Giải vinh danh đóng góp nền tảng và việc định hình lĩnh vực. |
| “Toán rời rạc chỉ là thuật toán.” | Còn có cấu trúc đồ thị, tổ hợp cực trị, lý thuyết tối ưu, … |
| “Thuật toán ngẫu nhiên luôn tốt hơn.” | Tính ngẫu nhiên là một tài nguyên có giá, và có cả chương trình khử ngẫu nhiên. |
| “Expander chỉ là đồ thị ngẫu nhiên.” | Đồ thị ngẫu nhiên thường là expander; điểm quan trọng là dựng chúng **tường minh** và dùng theo cách tất định. |
| “Bổ đề địa phương cần độc lập hoàn toàn.” | Cần **phụ thuộc có giới hạn**, được kiểm soát định lượng cẩn thận. |

---

## Độ khó như cấu trúc, không chỉ như rào cản

TCS coi độ khó tính toán là một cấu trúc lý thuyết: hàm một chiều (nếu tồn tại) làm nền cho mật mã; độ khó trung bình khác với tính NP-đầy đủ trong trường hợp xấu nhất; các giả thiết độ phức tạp mịn tinh chỉnh P vs NP thành những rào cản tốc độ chính xác. Hình học tổ hợp của Lovász và cách nhìn độ phức tạp của Wigderson cùng cho thấy toán rời rạc sinh ra **những định nghĩa sâu không thua kém các lý thuyết liên tục**.

**Gợi ý cho seminar.** Liệt kê ba định lý của TCS vẫn thú vị ngay cả khi P = NP (ví dụ các chặn dưới của độ phức tạp giao tiếp, các giới hạn của lý thuyết mã). Giải thích mỗi định lý bằng hai câu: vì sao.

---

## Bài tập

1. Phát biểu bổ đề địa phương trong một câu cho người ngoài ngành.  
2. Cho một ví dụ trong đó tính ngẫu nhiên giúp chứng minh sự tồn tại hoặc cho một thuật toán (ví dụ đơn giản cũng được).  
3. Khử ngẫu nhiên muốn đạt được điều gì? Không quá 100 từ.  
4. **Không quá 250 từ:** lập luận rằng TCS là toán thuần túy bằng chính ngôn ngữ của citation Abel 2021.  
5. Nối với [đồ thị và mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/): một câu về expander và độ tin cậy của mạng.  
6. Sau bài P vs NP: nêu ba định lý TCS khẳng định mà không cần P ≠ NP.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2021: Lovász và Wigderson, TCS và toán rời rạc là những lĩnh vực trung tâm.
- Wigderson còn nhận **giải Turing 2023** (không phải 2021).
- Không giải P vs NP.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: các bài giảng Abel của Lovász và Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  
2. **Lịch sử**: phỏng vấn Lovász và Wigderson của giải Abel: [https://www.youtube.com/watch?v=VAk0rtlKtMA](https://www.youtube.com/watch?v=VAk0rtlKtMA).  
3. **Định hướng**: WFSJ gặp Lovász và Wigderson: [https://www.youtube.com/watch?v=J4yssMTZqC4](https://www.youtube.com/watch?v=J4yssMTZqC4).  
4. **Định hướng**: phỏng vấn ngắn với Lovász: [https://www.youtube.com/watch?v=wg0di8dK0eI](https://www.youtube.com/watch?v=wg0di8dK0eI).  
5. **Định hướng**: phỏng vấn ngắn với Wigderson: [https://www.youtube.com/watch?v=5VxOhzNv9To](https://www.youtube.com/watch?v=5VxOhzNv9To).  

**Cổng chính thức và tài liệu**

- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  
- ACM Turing — Wigderson 2023: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/lovasz-wigderson_zqiL57ebP-k_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
2. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
3. Abel interview Lovász & Wigderson — https://www.youtube.com/watch?v=VAk0rtlKtMA  
4. WFSJ meet Lovász & Wigderson — https://www.youtube.com/watch?v=J4yssMTZqC4  
5. Short interview Lovász — https://www.youtube.com/watch?v=wg0di8dK0eI  
6. Short interview Wigderson — https://www.youtube.com/watch?v=5VxOhzNv9To  
7. NYT Abel 2021 — https://www.nytimes.com/2021/03/17/science/abel-prize-mathematics.html  
8. Nature Abel 2021 — https://www.nature.com/articles/d41586-021-00694-9  
9. ACM Turing — Wigderson 2023 — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
10. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  

1. [Abel 2021](https://abelprize.no/abel-prize-laureates/2021).  
2. Wigderson, *Mathematics and Computation* (Princeton).  
3. Alon–Spencer, *The Probabilistic Method*; Arora–Barak, *Computational Complexity*.  
4. Trong khóa: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/); [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/).

---

## Hướng đi tiếp

- Bài tập về bổ đề địa phương: dựng một mô hình đơn giản gồm các sự kiện xấu (tô màu, xếp gói, lập lịch).  
- So sánh các cách dựng expander trong lịch sử (Margulis; zigzag; Ramanujan).  
- Ghi lại một bài toán mở chính xác: P vs NP; khử ngẫu nhiên mạnh hơn; dựng tường minh với tham số tối ưu.  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Sullivan]({{ site.baseurl }}/contents/vi/chapter08/08_07_Sullivan_Topology/).

## Video tham khảo

- **xem trước** — [VINIF 2021|BÀI GIẢNG ĐẠI CHÚNG VỀ GIẢI ABEL 2021-PGS. PHAN THỊ HÀ DƯƠNG: MỘT SỐ CT CỦA LÁSZLÓ LOVÁSZ](https://www.youtube.com/watch?v=ZKK46TpwscE) — VinBigData, tiếng Việt. Xem trước: bài giảng đại chúng tiếng Việt của PGS. Phan Thị Hà Dương về một số công trình Lovász (Abel 2021), trước các bài Abel Prize bằng tiếng Anh.
- [The Abel lectures: László Lovász and Avi Wigderson](https://www.youtube.com/watch?v=zqiL57ebP-k) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe chính hai laureate trình bày công trình của mình.
- [Avi Wigderson & László Lovász - The Abel Prize interview 2021](https://www.youtube.com/watch?v=VAk0rtlKtMA) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua cuộc phỏng vấn hai laureate.
