---
layout: post
title: "Masaki Kashiwara: D-Module, Crystal, Lý thuyết Biểu diễn (Abel 2025)"
chapter: '08'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

Khi giải một hệ phương trình vi phân tuyến tính, phản xạ tự nhiên của hầu hết chúng ta là tìm nghiệm $$u(x)$$ bằng tích phân, chuỗi lũy thừa hay ước lượng giải tích. Thế nhưng năm 1970, một cậu sinh viên thạc sĩ 23 tuổi tại Đại học Tokyo tên là **Masaki Kashiwara**—dưới sự dẫn dắt của bậc thầy Mikio Sato—lại đặt ra một câu hỏi ngược đời: *tại sao ta cứ mãi đi săn lùng từng nghiệm riêng lẻ, thay vì nghiên cứu chính **cấu trúc đại số** của hệ phương trình vi phân đó?*

Từ luận văn thạc sĩ đặt nền móng ấy, Kashiwara đã xây dựng cả một ngôn ngữ mới kéo dài hơn nửa thế kỷ, nối liền phương trình vi phân với tôpô hình học và lý thuyết biểu diễn—đồng thời hai thập niên sau lại khám phá ra một cấu trúc tổ hợp đẹp như viên pha lê mang tên **crystal base** (cơ sở tinh thể) khi "đóng băng" các đối xứng lượng tử về nhiệt độ tuyệt đối! Năm **2025**, **Masaki Kashiwara** (RIMS, Đại học Kyoto; Viện Nghiên cứu Cao cấp Đại học Kyoto) trở thành **nhà toán học Nhật Bản đầu tiên** nhận **Giải Abel**:

> “for his fundamental contributions to algebraic analysis and representation theory, in particular the development of the theory of $$D$$-modules and the discovery of crystal graphs.”  
> — [Citation của ủy ban Abel](https://abelprize.no/citation/citation-abel-prize-committee-masaki-kashiwara)

(Tài liệu của giải cũng dùng cụm **crystal base**; “crystal graph” và “crystal base” chỉ cùng một bộ khung tổ hợp của các biểu diễn nhóm lượng tử.) Trang chính thức: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể giải thích $$D$$-module như ngôn ngữ đại số cho các hệ PDE tuyến tính; nêu ý tưởng **Riemann–Hilbert** tổng quát (module holonomic ↔ chùm perverse) ở mức khẩu hiệu; mô tả **crystal base** như mô hình tổ hợp của biểu diễn nhóm lượng tử; lập luận vì sao toán học hạ tầng xứng đáng với giải Abel; và so sánh giải tích đại số kiểu Kashiwara với một giải “xây dựng ngôn ngữ” khác (hình học perfectoid như hạ tầng của thời Fields).

**Kiến thức nền.** Đại số tuyến tính; toán tử vi phân như $$\frac{d}{dx}$$; sẵn sàng chấp nhận chùm (sheaf) và module như “không gian nghiệm được đóng gói bằng đại số”. Liên kết: [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Scholze và perfectoid]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/).

---

## Bản đồ kiến thức nền: Giải tích đại số, D-module và lý thuyết biểu diễn là gì và nghiên cứu những gì?

Ba cụm từ trong sự nghiệp của Kashiwara thường chỉ xuất hiện ở chương trình sau đại học, nhưng bản chất trực giác của chúng hoàn toàn có thể nắm bắt ngay từ kiến thức đại số tuyến tính và phương trình vi phân đại học:

- **Giải tích đại số (Algebraic Analysis) và $$D$$-module:** Trong đại số tuyến tính, một hệ phương trình tuyến tính $$Ax = 0$$ không cần giải bằng từng tọa độ; ta nghiên cứu chính ma trận $$A$$ và không gian nhân $$\ker A$$. Tương tự, với một hệ phương trình vi phân tuyến tính, các phép toán "nhân với biến $$x$$" và "lấy đạo hàm $$\partial_x = \frac{d}{dx}$$" lập thành một **vành không giao hoán** ký hiệu là $$D$$ (vì theo quy tắc đạo hàm tích, $$\partial_x(x u) - x(\partial_x u) = u$$, tức $$\partial_x x - x \partial_x = 1 \neq 0$$!). Một **$$D$$-module** đơn giản là một đối tượng đại số chịu tác động của vành toán tử vi phân $$D$$—nó đóng gói trọn vẹn một hệ PDE tuyến tính mà không phụ thuộc vào việc bạn chọn nghiệm là hàm trơn, hàm phức hay phân bố!
- **Lý thuyết biểu diễn (Representation Theory):** Là nghệ thuật "biến đối xứng thành ma trận". Một nhóm đối xứng trừu tượng (như nhóm quay 3D) rất khó tính toán trực tiếp; lý thuyết biểu diễn cho nó tác động lên một không gian vector bằng các ma trận vuông, nhờ đó các bài toán đối xứng trong toán học và cơ học lượng tử trở thành đại số tuyến tính.
- **Nhóm lượng tử và Đồ thị tinh thể (Crystal Graph / Crystal Base):** Trong vật lý thống kê và lý thuyết biểu diễn hiện đại, người ta "biến dạng" các đại số đối xứng cổ điển theo một tham số $$q$$ (gần giống nhiệt độ trong mô hình vật lý), tạo ra **nhóm lượng tử (quantum group)**. Khi $$q = 1$$ ta quay về đối xứng cổ điển; nhưng công thức với $$q$$ tổng quát cực kỳ cồng kềnh. Ý tưởng thiên tài của Kashiwara: cho $$q \to 0$$ (như hạ nhiệt độ về không độ tuyệt đối để chất lỏng kết tinh thành tinh thể)! Ở giới hạn $$q = 0$$, toàn bộ không gian biểu diễn phức tạp bỗng "đông cứng" thành một **đồ thị có hướng gắn nhãn** (**crystal graph**), biến các phép tính đại số nặng nề thành bài toán đi theo mũi tên và đếm đường đi cực kỳ đơn giản!

---

## 1. Giải tích đại số

Giải tích cổ điển viết ra một phương trình đạo hàm riêng rồi dùng tích phân, chuỗi hay bất đẳng thức để ước lượng nghiệm. Trường phái **Mikio Sato** tại Nhật Bản—với Masaki Kashiwara là người kiến tạo trụ cột—chọn một góc nhìn hoàn toàn khác: xử lý các hệ PDE tuyến tính bằng **đại số**.

Một toán tử vi phân tuyến tính một biến có dạng:

$$
P = a_m(x)\frac{d^m}{dx^m} + \cdots + a_1(x)\frac{d}{dx} + a_0(x).
$$

**Ví dụ cụ thể giúp thấy $$D$$-module đang làm gì:** Xét phương trình vi phân cực kỳ đơn giản $$P u = 0$$ với $$P = x \frac{d}{dx} - \alpha$$ (trong đó $$\alpha \in \mathbb{C}$$ là một hằng số). Nghiệm của nó là $$u(x) = C x^\alpha$$. Thay vì chỉ giữ hàm $$x^\alpha$$ (vốn đa trị khi vòng quanh điểm kỳ dị $$x = 0$$ trên mặt phẳng phức), giải tích đại số xét thương của vành toán tử $$D$$ cho ideal sinh bởi $$P$$:

$$
M = D / D\cdot P.
$$

Điều kỳ diệu là: mọi nghiệm $$u$$ của phương trình $$P u = 0$$ (trong bất kỳ không gian hàm nào $$\mathcal{F}$$ bạn muốn—hàm chỉnh hình, phân bố hay hyperfunction) đều tương ứng 1–1 với các đồng cấu $$D$$-module từ $$M$$ vào $$\mathcal{F}$$, tức $$\mathrm{Hom}_D(M, \mathcal{F})$$! Nhờ đóng gói hệ phương trình thành module $$M$$, toàn bộ kho vũ khí mạnh nhất của **đại số đồng điều** và **hình học** bỗng có thể phóng thẳng vào phương trình vi phân.

---

## 2. $$D$$-module

**$$D$$-module** là module trên chùm (hoặc vành) $$D$$ các toán tử vi phân trên một đa tạp phức $$X$$. Khung lý thuyết mà Kashiwara phát triển từ thập niên 1970 mang lại bốn sức mạnh lớn:

### Góc nhìn vi địa phương (Microlocal Analysis)

Khi một nghiệm PDE có kỳ dị (chẳng hạn một mặt sóng truyền đi), giải tích vi địa phương (Sato–Kashiwara–Kawai) không chỉ hỏi kỳ dị nằm ở *điểm $$x$$ nào*, mà còn hỏi nó lan truyền theo *hướng đối tiếp tuyến $$\xi$$ nào* trong không gian pha $$T^*X$$. Tập hợp các cặp $$(x, \xi)$$ đó tạo nên **đa tạp đặc trưng** (*characteristic variety*)—biến bản chất kỳ dị của PDE thành một đối tượng hình học tường minh.

### Đại số đồng điều cho PDE và tính holonomic

Một lớp $$D$$-module đặc biệt đẹp gọi là **$$D$$-module holonomic**: đó là những hệ PDE "vừa đủ nhiều phương trình" (đa tạp đặc trưng có số chiều nhỏ nhất có thể theo bất đẳng thức Bernstein), bảo đảm không gian nghiệm cục bộ luôn **hữu hạn chiều**. Phạm trù dẫn xuất cho phép thao tác trên các hệ PDE bằng các hàm tử kéo về, đẩy tới, đối ngẫu giống hệt như trong hình học đại số.

### Lý thuyết biểu diễn hình học

Một trong những ứng dụng lừng danh nhất của $$D$$-module là **định lý địa phương hóa Beilinson–Bernstein** (đầu thập niên 1980), nối trực tiếp các biểu diễn của đại số Lie nửa đơn với $$D$$-module trên đa tạp cờ—từ đó giải quyết Giả thuyết Kazhdan–Lusztig, một cột mốc lớn của lý thuyết biểu diễn hiện đại.

### Các tương ứng kiểu Riemann–Hilbert

Riemann–Hilbert hiện đại nối dữ liệu giải tích của PDE với dữ liệu tôpô thuần túy của chùm, cụ thể là **chùm perverse (perverse sheaf)**—một lớp chùm có cấu trúc đối ngẫu tuyệt đẹp trên các không gian có kỳ dị. Giải tích trở thành tôpô của chùm.

---

## 3. Triết lý Riemann–Hilbert (bản đồ sâu hơn)

Bài toán Riemann–Hilbert cổ điển (bài toán thứ 21 của Hilbert) hỏi: nếu ta biết **đơn đạo (monodromy)**—tức cách nghiệm của một phương trình vi phân biến đổi khi ta đi một vòng tròn quanh các điểm kỳ dị—liệu ta có dựng lại được phương trình vi phân ban đầu không? Ví dụ với nghiệm $$u(x) = x^\alpha$$ ở trên, khi $$x$$ đi một vòng ngược chiều kim đồng hồ quanh gốc tọa độ $$0$$ (tức $$x \mapsto e^{2\pi i} x$$), nghiệm bị nhân thêm hằng số $$e^{2\pi i \alpha}$$—đó chính là monodromy.

Kashiwara (và Mebkhout độc lập) đã nâng cấp bài toán cổ điển ấy lên số chiều bất kỳ dưới dạng một **cuốn từ điển tương đương giữa hai phạm trù**:

$$
\{\text{holonomic }D\text{-module có kỳ dị chính quy}\}
\;\longleftrightarrow\;
\{\text{chùm perverse (perverse sheaves)}\}
$$

(trong bối cảnh đa tạp phức thích hợp). Phía bên trái là **giải tích / đại số** (hệ phương trình vi phân tuyến tính); phía bên phải là **tôpô** (dữ liệu chùm và monodromy). Cuốn từ điển Riemann–Hilbert này có cùng tầm vóc tư tưởng với tính modular của đường cong elliptic hay Chương trình Langlands: nối liền hai thế giới tưởng như nói hai thứ tiếng hoàn toàn khác nhau.

---

## 4. Crystal base và crystal graph

### Nhóm lượng tử

Trong thập niên 1980, Drinfeld và Jimbo phát hiện ra **nhóm lượng tử** $$U_q(\mathfrak{g})$$—một phép biến dạng có tham số $$q$$ của đại số bao phổ dụng của đại số Lie $$\mathfrak{g}$$, xuất hiện tự nhiên trong các mô hình vật lý thống kê khả tích và lý thuyết nút thắt. Các biểu diễn của nhóm lượng tử rất giàu cấu trúc nhưng tính toán trực tiếp trên đa thức của $$q$$ vô cùng nặng nề.

### Crystal như một bộ khung tổ hợp

Năm 1990, Kashiwara tạo ra một ý tưởng làm ngỡ ngàng giới lý thuyết biểu diễn: **cho $$q \to 0$$** (giống như hạ nhiệt độ về 0 tuyệt đối trong vật lý tinh thể). Dưới một chuẩn hóa tinh tế, một biểu diễn phức tạp của nhóm lượng tử bỗng sụp đổ gọn gàng thành một **cơ sở tinh thể (crystal base)**, được vẽ lại thành **đồ thị tinh thể (crystal graph)**: các đỉnh biểu diễn vector cơ sở, còn các mũi tên có màu (gắn nhãn theo các gốc đơn giản) biểu diễn tác động của các toán tử nâng–hạ lượng tử.

> Crystal là “cái bóng” của biểu diễn tại $$q=0$$, giữ trọn linh hồn tổ hợp của đối xứng.

**Ví dụ cụ thể với $$\mathfrak{sl}_2$$ (đối xứng spin cơ bản nhất):** Biểu diễn chiều $$3$$ (spin 1) của $$\mathfrak{sl}_2$$ có 3 trạng thái trọng số $$+2, 0, -2$$. Đồ thị tinh thể của nó đơn giản là một chuỗi 3 đỉnh nối bởi mũi tên: $$\boxed{+2} \xrightarrow{\tilde{f}} \boxed{0} \xrightarrow{\tilde{f}} \boxed{-2}$$. Điều kỳ diệu xảy ra khi bạn lấy **tích tensor** của hai biểu diễn—một phép toán vốn rất rối trong đại số Lie: với crystal graph, quy tắc nhân tensor của Kashiwara trở thành một trò chơi tổ hợp cực kỳ giản đơn (chỉ cần đọc dãy dấu ngoặc và nối mũi tên!), từ đó lập tức đọc ra cách phân rã thành các biểu diễn bất khả quy (như quy tắc Littlewood–Richardson) mà không cần một dòng tính toán $$q$$-đại số nào!

---

## 5. Vì sao đáng giải Abel 2025

Lời trao giải Abel 2025 không tôn vinh một bài toán thi đơn lẻ mà tôn vinh hơn nửa thế kỷ **kiến tạo ngôn ngữ và hạ tầng** cho giải tích đại số và lý thuyết biểu diễn. Hãy đặt Kashiwara cạnh một nhà xây dựng ngôn ngữ lừng danh khác của thế hệ Fields:

| Hạ tầng | Tín hiệu của một thời đại | Ngôn ngữ được xây dựng |
|---------|---------------------------|------------------------|
| Hình học perfectoid (Scholze, Fields) | Bộ công cụ đột phá, đỉnh cao của sự nghiệp trẻ | Hình học $$p$$-adic |
| $$D$$-module và crystal (Kashiwara, Abel) | Giải tích đại số cả một sự nghiệp | PDE ↔ chùm; biểu diễn lượng tử ↔ crystal |

Cả hai đều chứng minh một sự thật: toán học bước sang trang mới mỗi khi có một "tiếng mẹ đẻ" mới cho phép diễn đạt những cấu trúc mà ngôn ngữ cũ không thể chạm tới.

### Giải hạ tầng và giải bài toán

Wiles và Định lý Fermat (Abel 2016) là câu chuyện chinh phục một ngọn núi có tên tuổi suốt 350 năm. Kashiwara (Abel 2025) là câu chuyện xây dựng mạng lưới xa lộ giúp hàng trăm nhà toán học chinh phục hàng loạt ngọn núi khác nhau. Đừng ép mọi chủ nhân Giải Abel vào cùng một khuôn mẫu "đã giải giả thuyết X"—hãy nhận ra sức mạnh bền bỉ của toán học hạ tầng.

---

## 6. Vị trí trong khóa học

- [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/): một nền văn hóa “từ điển” lớn khác (dạng tự đồng cấu ↔ Galois); khác đối tượng nhưng cùng tinh thần về sự tương ứng.  
- [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/): hình học làm hạ tầng cho số học.  
- Lý thuyết biểu diễn là sợi chỉ xuyên suốt toán thuần túy hiện đại; crystal là cánh cửa tổ hợp.  
- Tính chính quy của PDE (bài Caffarelli; flagship về Deng) hỏi những câu hỏi giải tích; $$D$$-module tổ chức lại PDE tuyến tính bằng đại số.  
- Độ phức tạp và hạ tầng chứng minh (Lovász–Wigderson) song song về ý tưởng rằng *phương pháp* cũng có thể là đối tượng được vinh danh.

### Cách đọc một citation của Abel

Mở bản PDF citation 2025 trên [abelprize.no](https://abelprize.no/). Gạch chân các danh từ: $$D$$-module, holonomic, crystal base, biểu diễn, kỳ dị. Viết lại citation thành ba gạch đầu dòng bằng lời của bạn, không chép lại. Bài tập đó luyện kỹ năng đọc citation cho cả chương 08.

---

## 7. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “$$D$$-module chỉ là phân bố.” | Phân bố có thể là nghiệm; $$D$$-module là gói đại số cho cả hệ. |
| “Crystal base là tinh thể trong hóa học.” | Đó là một cấu trúc tổ hợp thuần túy toán học cho biểu diễn. |
| “Riemann–Hilbert chỉ là bài toán ODE của thế kỷ 19.” | Riemann–Hilbert hiện đại là một tương ứng giữa phạm trù chùm và $$D$$-module. |
| “Giải Abel 2025 chỉ vì một bài báo.” | Đó là sự phát triển cả đời của những lý thuyết mà cả một lĩnh vực dùng. |
| “Đại số không giúp được giải tích.” | Giải tích đại số chính là phản ví dụ. |

---

## Hạ tầng như một thành tựu

Một số giải thưởng vinh danh những bài toán đã được giải. Giải Abel 2025 vinh danh **ngôn ngữ đã được xây dựng**: một khi $$D$$-module và crystal trở thành công cụ chuẩn, hàng trăm định lý trở nên có thể viết ra. Hãy so perfectoid (hạ tầng của thời Fields) với giải tích đại số (hạ tầng của thời Abel): khác thời đại, cùng một hiện tượng, đó là toán học tiến lên khi có một “tiếng mẹ đẻ” mới.

**Gợi ý cho seminar.** Nêu ba khái niệm “hạ tầng” bạn đã gặp trong khóa (dạng modular, expander, hiện tượng tập trung, …) và với mỗi khái niệm, nêu một định lý phụ thuộc vào nó.

---

## Bài tập

1. Phân biệt toán tử vi phân với phép nhân với một hàm: mỗi cái một câu.  
2. Vì sao đại số có thể giúp giải tích? Không quá 120 từ.  
3. Viết một câu về crystal base cho một bạn biết ma trận nhưng chưa biết nhóm lượng tử.  
4. Nối với [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) hoặc [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/): một điểm giống (từ điển, hạ tầng), một điểm khác (đối tượng).  
5. **Không quá 200 từ:** giải hạ tầng và giải bài toán, dùng Abel 2025 và một câu chuyện về Millennium hoặc FLT.  
6. Mở tài liệu về Kashiwara trên [abelprize.no](https://abelprize.no/); trích citation ngắn chính thức và gạch chân các danh từ toán học.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2025: Kashiwara, $$D$$-module, crystal base.
- Giải tích đại số cho PDE tuyến tính; biểu diễn lượng tử dạng tổ hợp.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: danh sách phát các bài giảng Abel 2025: [https://www.youtube.com/playlist?list=PLKeZo7pFBx1uGqwO463MpxuvxMpBCnddj](https://www.youtube.com/playlist?list=PLKeZo7pFBx1uGqwO463MpxuvxMpBCnddj).  
2. **Liên quan**: danh sách phát các bài giảng liên quan của IHES (các sự kiện về Kashiwara): [https://www.youtube.com/playlist?list=PLx5f8IelFRgEe8LACp8Pt3ijJb6PLIbgC](https://www.youtube.com/playlist?list=PLx5f8IelFRgEe8LACp8Pt3ijJb6PLIbgC).  

**Cổng chính thức và tài liệu**

- Abel 2025 Kashiwara: https://abelprize.no/abel-prize-laureates/2025  
- Announcement article 2025: https://abelprize.no/article/2025/japanese-mathematician-masaki-kashiwara-awarded-abel-prize-2025  

## Tài liệu

### Danh mục nguồn

1. Abel 2025 Kashiwara — https://abelprize.no/abel-prize-laureates/2025  
2. Announcement article 2025 — https://abelprize.no/article/2025/japanese-mathematician-masaki-kashiwara-awarded-abel-prize-2025  
3. Abel Lectures 2025 playlist — https://www.youtube.com/playlist?list=PLKeZo7pFBx1uGqwO463MpxuvxMpBCnddj  
4. IHES related lectures playlist (Kashiwara events) — https://www.youtube.com/playlist?list=PLx5f8IelFRgEe8LACp8Pt3ijJb6PLIbgC  
5. IHES news Kashiwara Abel — https://www.ihes.fr/en/abel-prize-2025/  
6. Wikipedia — Masaki Kashiwara — https://en.wikipedia.org/wiki/Masaki_Kashiwara  
7. Wikipedia — D-module — https://en.wikipedia.org/wiki/D-module  
8. Wikipedia — Crystal base — https://en.wikipedia.org/wiki/Crystal_base  
9. Abel popular — crystal bases PDF — https://abelprize.no/sites/default/files/2025-03/krystallENG.pdf  
10. Abel glimpse PDF Kashiwara — https://abelprize.no/sites/default/files/2025-03/MasakiKashiwara_s_work_for_non_mathematicians_AbelPrize_2025.pdf  

1. [Abel 2025 / Kashiwara](https://abelprize.no/citation/citation-abel-prize-committee-masaki-kashiwara).  
2. Bài khảo sát nhập môn về $$D$$-module và crystal base.  
3. Thông báo của IAS/RIMS để hiểu ngữ cảnh lịch sử.  
4. Trong khóa: Langlands; Scholze; các bài Fields gần với lý thuyết biểu diễn.

---

## Hướng đi tiếp

- Săn tìm hạ tầng: liệt kê những công cụ hình học gần Langlands nghe giống chùm hay module.  
- Crystal: tổ hợp như cái bóng của biểu diễn; thử xem hình crystal của $$\mathfrak{sl}_2$$ nhỏ trong bài khảo sát.  
- Ghi lại một hướng nghiên cứu mở trong lý thuyết biểu diễn hình học hoặc giải tích đại số mà vẫn đang kéo cả lĩnh vực đi.  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Kết chuỗi chủ đề của chương 08: quay lại [Tổng quan]({{ site.baseurl }}/contents/vi/chapter08/08_01_Tong_quan/) và đọc lại như một bản đồ thời tiết của cả một sự nghiệp: bão bài toán (FLT), khí hậu của giải tích hình học (Uhlenbeck, Sullivan, Caffarelli), mặt trận rời rạc và động lực (Furstenberg–Margulis, Lovász–Wigderson), số chiều cao trong xác suất (Talagrand), hạ tầng của giải tích đại số (Kashiwara). Trong portfolio, nên chọn một hệ thời tiết và báo cáo với nguồn chính, không liệt kê mọi đám mây.

## Video tham khảo

- **Xem trước** — [Andrea D'Agnolo: Algebraic Analysis for beginners](https://www.youtube.com/watch?v=m0LPDNDhfMc) — The Abel Prize, tiếng Anh. Xem trước để làm quen với giải tích đại số ở mức nhập môn.
- [Masaki Kashiwara: Monoidal categories (non-commutative case)](https://www.youtube.com/watch?v=FHn4WHPzjYw) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe chính Kashiwara nói về phạm trù monoidal.
- [David Nadler: Gaining momentum: On the global influence of Masaki Kashiwara's microlocal perspective](https://www.youtube.com/watch?v=tFswRJVXTpA) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, về ảnh hưởng của quan điểm vi địa phương của Kashiwara.
