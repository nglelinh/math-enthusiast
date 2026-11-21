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

**Giải Abel 2021** được trao chung cho **László Lovász** và **Avi Wigderson**

> “for their foundational contributions to theoretical computer science and discrete mathematics, and their leading role in shaping them into central fields of modern mathematics.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2021)

Bài này giải thích vì sao toán rời rạc và khoa học máy tính lý thuyết (TCS) được trao một giải thưởng “toán thuần túy cốt lõi” cho cả sự nghiệp: **bổ đề địa phương** của Lovász, lý thuyết đồ thị và tối ưu tổ hợp đóng góp gì; **tính ngẫu nhiên, khử ngẫu nhiên, expander và độ phức tạp** trong thế giới của Wigderson đóng góp gì; và đặt giải thưởng này cạnh [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), bài toán vẫn còn mở, mà không nhầm lẫn hai việc. Tài liệu: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể giải thích vì sao toán rời rạc và TCS xứng đáng với giải Abel như một phần trung tâm của toán học hiện đại; nêu bổ đề địa phương của Lovász và mục đích của nó (tồn tại cấu hình khi có nhiều sự kiện xấu gần như độc lập); nêu chủ đề tính ngẫu nhiên và khử ngẫu nhiên của Wigderson; mô tả expander như đồ thị thưa nhưng liên thông rất mạnh; và nối tất cả với P vs NP **mà không** tuyên bố bài toán đó đã được giải.

**Kiến thức nền.** Đồ thị (đỉnh, cạnh); xác suất cơ bản; ý niệm một thuật toán tốn thời gian theo kích thước đầu vào. Liên kết: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [đồ thị và mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

---

## 1. Một giải thưởng về văn hóa cũng như về khoa học

Đồ thị, thuật toán và độ phức tạp từng bị coi là ngoại vi của “toán thuần túy cốt lõi” trong một số văn hóa thể chế: quan trọng, nhưng thuộc về khoa Khoa học máy tính. Giải Abel 2021 khẳng định công khai: các lĩnh vực này chứa **những định lý cấu trúc sâu** và tương tác với hình học, đại số, xác suất ở mức cao nhất.

Vế thứ hai của citation rất đáng chú ý: “shaping them into central fields.” Đó là việc xây dựng lĩnh vực: dìu dắt người đi sau, viết sách, lập danh sách các bài toán, và nhiều thập niên định lý, chứ không phải một dòng tít. Đọc citation của Abel 2021 là một bài luyện tập để phân biệt: giải vinh danh việc **định hình**, không nên nhầm với việc “đã chinh phục đỉnh Everest của lĩnh vực”.

---

## 2. Lovász: toán rời rạc như một khoa học toán học

### Đồ thị, tối ưu, hình học

Công trình của Lovász trải khắp lý thuyết đồ thị, tối ưu tổ hợp và biểu diễn hình học của đồ thị. Chủ đề lặp lại: các đối tượng rời rạc mang bóng dáng của cái liên tục, như phép nhúng, nới lỏng nửa xác định dương, thuật toán lattice, và về sau là văn hóa **giới hạn của đồ thị** (graphon) mà ông góp phần mở ra. Tối ưu trên các cấu trúc tổ hợp trở thành một khoa học toán học nghiêm túc, có đối ngẫu, thuật toán và các kết quả về độ khó.

### Bổ đề địa phương Lovász

**Bổ đề địa phương** (Erdős–Lovász) là một nguyên lý tồn tại sâu sắc. Giả sử có nhiều “sự kiện xấu” $$A_i$$, mỗi sự kiện có xác suất nhỏ và chỉ phụ thuộc vào hữu hạn sự kiện khác. Dưới các giả thiết định lượng, xác suất để **không** sự kiện xấu nào xảy ra vẫn dương:

$$
\mathbb{P}\Big(\bigcap_i A_i^c\Big) > 0.
$$

Chặn hợp (union bound) thất bại khi có quá nhiều sự kiện; độc lập hoàn toàn thất bại khi tồn tại phụ thuộc. Bổ đề địa phương sống ở chế độ giữa hai cực này: **phụ thuộc có giới hạn**. Nó là công cụ chủ lực của tổ hợp, phương pháp xác suất, và thiết kế thuật toán (kể cả các phiên bản thuật toán về sau).

### Xây dựng một lĩnh vực

Ngoài các định lý, ông còn định hình toán rời rạc với chuẩn mực chứng minh, các cây cầu sang hình học và tối ưu, và một cộng đồng toàn cầu. Cụm “leading role” của Abel chỉ vào chính điều này. Một sự nghiệp toán rời rạc trọn đời không chỉ là “chứng minh được nhiều bổ đề”, mà là làm cho ngôn ngữ của ngành trở thành mặc định cho thế hệ sau.

---

## 3. Wigderson: tính ngẫu nhiên, độ phức tạp, giả ngẫu nhiên

### Tính ngẫu nhiên như một tài nguyên

Chủ đề trung tâm của Wigderson: khi nào **thuật toán ngẫu nhiên** vượt trội thuật toán tất định, và sức mạnh của tính ngẫu nhiên như một tài nguyên tính toán là gì? Nhiều thuật toán tung đồng xu: kiểm tra số nguyên tố kiểu Monte Carlo trong lịch sử, băm, lấy mẫu, các giao thức giao tiếp. Độ phức tạp hỏi: tính ngẫu nhiên có thực sự cần thiết hay chỉ tiện lợi.

### Khử ngẫu nhiên

**Khử ngẫu nhiên** hỏi khi nào có thể gỡ bỏ tính ngẫu nhiên, thường dưới **giả thiết về độ khó**: một hàm đủ khó suy ra có bộ sinh giả ngẫu nhiên. Nếu thế giới có đủ độ khó tính toán thì có thể có những mô phỏng tất định hiệu quả cho thuật toán ngẫu nhiên. Cách nhìn này nối các chặn dưới của độ phức tạp với thiết kế thuật toán một cách sâu sắc: độ khó không chỉ là rào cản mà còn là nguyên liệu để xây bộ sinh giả ngẫu nhiên.

### Expander, chứng minh tương tác, và các cây cầu sang toán thuần túy

**Đồ thị expander** thưa nhưng liên thông rất mạnh: trộn giống như ngẫu nhiên mà chỉ cần ít cạnh. Chúng xuất hiện trong khử ngẫu nhiên, lý thuyết mã, mạng, và cả lý thuyết nhóm thuần túy (các cách dựng tường minh trong lịch sử gồm expander kiểu Margulis). Thế giới của Wigderson coi expander và các họ hàng của nó là **sự giả ngẫu nhiên hiện hình**.

Chứng minh tương tác, zero-knowledge và cấu trúc của các lớp độ phức tạp là những cây cầu nối logic, đại số và thuật toán. Cuốn sách *Mathematics and Computation* trình bày TCS như toán học dành cho cộng đồng toán học rộng.

---

## 4. Expander: bản đồ các giao điểm

Một họ vô hạn các đồ thị $$d$$-chính quy $$\{G_n\}$$ là một **họ expander** nếu khoảng cách phổ (hoặc hằng số Cheeger) bị chặn dưới độc lập với $$n$$. Tương đương: các tập nhỏ giãn ra, tức lân cận của chúng lớn lên theo một hệ số xác định.

Hệ quả: bước đi ngẫu nhiên trộn nhanh; lý thuyết mã và khử ngẫu nhiên có các đối tượng tường minh; toán thuần túy có lý thuyết đồ thị phổ và các phép dựng từ nhóm.

Lý thuyết đồ thị cấu trúc và hình học của Lovász gặp tính giả ngẫu nhiên của Wigderson ở expander. Giải Abel 2021 nằm ngay tại giao điểm đó, và giải Abel 2020 của Margulis cũng đã chạm vào expander từ phía động lực học và nhóm. Trong seminar có thể vẽ một tam giác: **cấu trúc đồ thị, tính ngẫu nhiên, động lực học/nhóm**.

---

## 5. Bên cạnh P vs NP

[P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn còn mở. Giải Abel 2021 **không** giải bài toán đó. Công trình của Lovász và Wigderson là **bộ công cụ và cách nhìn** xoay quanh độ khó tính toán: các kết quả khẳng định, lý thuyết cấu trúc, tính ngẫu nhiên, tối ưu, và việc khẳng định tính chính đáng toán học của độ phức tạp rời rạc.

Một thói quen lành mạnh trong seminar: liệt kê ba định lý “khẳng định” của TCS mà không cần lời giải của P vs NP (các ứng dụng của bổ đề địa phương; việc dựng expander; chứng minh tương tác; xấp xỉ dưới các giả thiết độ phức tạp; …). Toán học của cả một sự nghiệp gồm cả việc xây dựng kiến trúc cho lĩnh vực, không chỉ là leo lên đỉnh Everest.

### Độ khó như một đối tượng toán học

Dù P vs NP chưa ngã ngũ, độ phức tạp coi **độ khó** là thứ có thể *sử dụng*: phép quy dẫn, tính đầy đủ, các chặn dưới có điều kiện, các giả thiết mật mã. Chương trình của Wigderson thường biến độ khó thành một tài nguyên xây dựng, ví dụ bộ sinh giả ngẫu nhiên đánh lừa được mọi bài kiểm tra hiệu quả; nhờ đó thiết kế thuật toán và tư duy chặn dưới trở thành hai mặt của một chủ đề. Tối ưu tổ hợp của Lovász cũng nhìn các cấu trúc rời rạc như hình học: đa diện, đối ngẫu, các ngưỡng xấp xỉ là định lý chứ không chỉ là heuristic.

Đạo lý của khóa học khớp với chương 01: **một bài toán lớn còn mở không làm cho cả lĩnh vực trống rỗng**. Xung quanh P vs NP là cả một nền văn minh toán học trưởng thành.

---

## 6. Vì sao đáng một giải Abel

Hai sự nghiệp, một thông điệp: toán rời rạc và TCS không phải công dân hạng hai của toán thuần túy. Chúng có những định lý sâu mang nội dung hình học và đại số; những phương pháp được xuất khẩu sang nơi khác; những bài toán mở tầm cỡ Hilbert (P vs NP là một trong số đó); và một hạ tầng (expander, bộ sinh giả ngẫu nhiên, các bổ đề tổ hợp) được dùng xuyên suốt các ngành khoa học.

Lời của ủy ban, “central fields of modern mathematics”, chính là luận điểm của bài này. Giải Abel không “nâng cấp khoa học máy tính thành toán học”; nó **ghi nhận** rằng các lĩnh vực này đã là toán học trung tâm từ lâu, và sự nghiệp của hai laureate giúp cộng đồng toán học rộng hơn thấy rõ điều đó.

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
