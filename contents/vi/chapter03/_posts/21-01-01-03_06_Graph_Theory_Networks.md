---
layout: post
title: "Lý thuyết Đồ thị → Mạng"
chapter: '03'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Đường sá, siêu liên kết, phân tử, quan hệ xã hội, dây dẫn trong chip, đồ thị phụ thuộc giữa các gói phần mềm: bỏ nhãn đi thì tất cả đều là cùng một loại đối tượng, gồm các **đỉnh** nối với nhau bởi các **cạnh**. Lý thuyết đồ thị từng chỉ là một nhánh tổ hợp mang tính giải trí. Ngày nay nó định tuyến gói tin, xếp hạng trang web, phân bổ luồng hàng và phân tích dịch bệnh.

**Lộ trình:** đồ thị làm mô hình → đường đi và tính liên thông → cây và chu trình → luồng và lát cắt → bước ngẫu nhiên và PageRank → đồ thị giãn nở (expander) → thuật toán cho mạng quy mô lớn → nhầm lẫn thường gặp.

Bài này chỉ ra **cơ chế**: ý tưởng nào trong lý thuyết đồ thị trở thành công nghệ mạng nào, và vì sao đại số tuyến tính trên ma trận kề lại đi cùng các thuật toán rời rạc.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô hình hóa một hệ thống thực tế bằng đồ thị $$G=(V,E)$$ (có hướng hoặc vô hướng, có trọng số hoặc không) và nói rõ đỉnh, cạnh là gì.
- Giải thích tính liên thông, đường đi ngắn nhất, và vì sao các thuật toán BFS, Dijkstra quan trọng trong định tuyến và logistics.
- Phát biểu ý tưởng của định lý luồng cực đại – lát cắt cực tiểu và nêu một ứng dụng.
- Mô tả **PageRank** như một bước ngẫu nhiên, hay một bài toán vectơ riêng, trên đồ thị web.
- Giải thích bằng trực giác đồ thị giãn nở mang lại gì (liên thông tốt với ít cạnh).
- Tránh hai nhầm lẫn: "đồ thị chỉ dùng cho mạng xã hội" và "PageRank chỉ đếm số liên kết trỏ đến".

**Kiến thức nền.** Toán rời rạc cơ bản. Sẽ có ích nếu biết [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

**Liên kết.** [Khoa học mạng (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), [Định lý bốn màu]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/).

---

## 1. Đồ thị: ngôn ngữ của sự kết nối

$$G=(V,E)$$ gồm tập đỉnh và tập cạnh (mỗi cạnh là một cặp đỉnh, hoặc một cặp có thứ tự nếu đồ thị có hướng). Cạnh có thể mang **trọng số** (khoảng cách, dung lượng, mức độ gắn kết).

| Hệ thống | Đỉnh | Cạnh |
|----|------|------|
| Bản đồ đường | Giao lộ | Đoạn đường |
| Web | Trang | Siêu liên kết (có hướng) |
| Mạng xã hội | Người, tài khoản | Theo dõi, kết bạn |
| Mạch điện | Linh kiện, nút mạch | Dây dẫn |
| Học máy | Tensor, phép toán | Phụ thuộc dữ liệu |

**Ý chính.** *Khi câu hỏi "cái gì nối với cái gì" quan trọng hơn câu hỏi "nằm ở đâu trong không gian", ngôn ngữ đồ thị là hệ tọa độ phù hợp.*

Với ma trận kề $$A$$: lũy thừa $$A^k$$ đếm số đường đi độ dài $$k$$; khoảng cách phổ (spectral gap) quyết định tốc độ trộn của bước ngẫu nhiên.

---

## 2. Đường đi, khoảng cách và tính liên thông

**Khoảng cách** $$d(u,v)$$ là độ dài của đường đi ngắn nhất. **Tính liên thông** hỏi mọi cặp đỉnh có được nối bởi một đường đi hay không; với đồ thị có hướng, ta phân biệt thành phần liên thông mạnh và liên thông yếu. Cầu và đỉnh khớp là những điểm mà chỉ cần một chỗ hỏng là mạng bị tách rời.

**Các thuật toán nền tảng.** BFS (đồ thị không trọng số); Dijkstra (trọng số không âm, là lõi của hệ thống chỉ đường GPS); A\* (dùng thêm hàm ước lượng heuristic); Bellman–Ford và Floyd–Warshall (tổng quát hơn nhưng tốn kém hơn).

**Ý chính.** *Định tuyến là tìm kiếm tối ưu trên đồ thị; "đường tốt nhất" là một bài toán tối ưu tổ hợp được đặt đúng, không phải chuyện nhìn bản đồ cho đẹp.*

---

## 3. Cây, cây khung và chu trình

**Cây:** đồ thị liên thông, không có chu trình; khi đó $$|E|=|V|-1$$. **Cây khung nhỏ nhất (MST)** (thuật toán Kruskal, Prim) dùng để thiết kế hạ tầng kết nối với chi phí thấp nhất. Chu trình tạo ra đường dự phòng (tốt cho khả năng chịu lỗi) nhưng cũng làm bài toán phức tạp hơn. Bài toán chu trình Hamilton là NP-đầy đủ, xem bối cảnh trong bài [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

---

## 4. Luồng và lát cắt

Gán cho mỗi cạnh một **dung lượng** $$c(e)\ge 0$$. Một **luồng** đi từ nguồn $$s$$ đến đích $$t$$, không vượt quá dung lượng của từng cạnh, và được bảo toàn tại mọi nút trung gian. **Định lý luồng cực đại – lát cắt cực tiểu:**

$$
\max\mathrm{flow}(s,t)=\min\mathrm{cut}(s,t).
$$

Ứng dụng: giao thông, logistics; bài toán ghép cặp trên đồ thị hai phía; phân vùng ảnh (graph cut); đánh giá độ tin cậy của mạng.

**Ý chính.** *Nút thắt cổ chai chính là một lát cắt; thuật toán liên tục tìm cách tăng luồng cho đến khi một lát cắt chứng nhận rằng luồng đã tối ưu.*

Đây cùng tinh thần đối ngẫu như trong bài [tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).

---

## 5. Bước ngẫu nhiên và PageRank

Một bước ngẫu nhiên trên đồ thị có hướng đi từ một nút sang nút khác theo các cạnh đi ra (chọn đều, hoặc theo trọng số). Với các điều kiện khá nhẹ, bước ngẫu nhiên có **phân phối dừng** $$\pi$$ thỏa mãn $$\pi^\top=\pi^\top P$$, trong đó $$P$$ là ma trận chuyển. Đây là bài toán tìm vectơ riêng trái ứng với giá trị riêng $$1$$.

**PageRank** (Brin và Page) mô hình hóa một người lướt web: phần lớn thời gian người đó đi theo liên kết, thỉnh thoảng nhảy (teleport) sang một trang ngẫu nhiên. Vectơ xếp hạng là phân phối dừng, tương đương với nghiệm của hệ tuyến tính

$$
\pi=\alpha P^\top\pi+(1-\alpha)v,
$$

với hệ số tắt dần (damping) $$\alpha$$ và vectơ teleport $$v$$. Mức độ quan trọng của một trang không phải là số liên kết trỏ đến nó: một liên kết từ trang có thứ hạng cao có trọng lượng lớn hơn, và cấu trúc liên thông của đồ thị ảnh hưởng đến kết quả của bước ngẫu nhiên.

**Ý chính.** *Mức độ quan trọng toàn cục nảy sinh từ cấu trúc liên kết cục bộ, thông qua vectơ riêng hay một hệ phương trình tuyến tính, chứ không phải từ một bảng điểm do người viết tay.*

Các biến thể của PageRank được dùng trong hệ gợi ý, các chỉ số trích dẫn học thuật (cần thận trọng), và các độ đo trung tâm trong khoa học mạng ([Ch.6]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/)). PageRank cá nhân hóa (teleport ưu tiên về một tập nút xuất phát) là công cụ chủ lực cho phân cụm đồ thị cục bộ và tính năng "trang liên quan".

**Phương pháp lặp lũy thừa.** Trong thực tế, người ta hiếm khi giải trực tiếp một hệ dày đặc. Thay vào đó, họ lặp lại phép nhân ma trận thưa với vectơ dùng ma trận Google (hoặc giải một hệ tuyến tính tương đương) để tính thứ hạng trên đồ thị hàng tỷ cạnh. Khả năng mở rộng không phải chuyện phụ: đó chính là lý do cách tiếp cận vectơ riêng thắng thế so với những quy tắc chấm điểm phức tạp không lặp nhanh được.

---

## 6. Phổ của đồ thị: ma trận Laplace và lát cắt

Ma trận Laplace tổ hợp $$L=D-A$$ (ma trận bậc trừ ma trận kề) của đồ thị vô hướng là nửa xác định dương và thỏa mãn $$L\mathbf{1}=0$$. Giá trị riêng nhỏ thứ hai (độ liên thông đại số, hay giá trị Fiedler) đo mức độ "gắn kết" của đồ thị; vectơ riêng tương ứng gợi ý cách chia đồ thị thành hai phần.

Phân cụm phổ, vẽ đồ thị và xử lý tín hiệu trên đồ thị dùng cơ sở gồm các vectơ riêng của $$L$$, giống như phân tích Fourier dùng các hàm mũ phức. Thực ra đây là một sự tương tự chính xác (biến đổi Fourier trên đồ thị). Các thuật toán làm thưa đồ thị (sparsifier) xấp xỉ dạng toàn phương $$x^\top Lx$$ bằng một đồ thị có ít cạnh hơn; đây là nơi lý thuyết đồ thị thuật toán gặp đại số tuyến tính số.

Một công thức hữu ích:

$$
x^\top Lx=\sum_{ij\in E}(x_i-x_j)^2
$$

đo mức độ hàm $$x$$ trên các đỉnh "nhảy" giá trị dọc theo các cạnh: hàm càng trơn trên đồ thị thì dạng toàn phương càng nhỏ.

---

## 7. Đồ thị giãn nở: thưa mà liên thông rất tốt

Một họ **đồ thị giãn nở (expander)** là một dãy đồ thị thưa nhưng liên thông rất mạnh: mọi tập đỉnh (không quá lớn) đều có số cạnh đi ra ngoài lớn so với kích thước của nó (độ giãn nở theo cạnh). Các cách phát biểu gần tương đương: bước ngẫu nhiên trộn nhanh; khoảng cách phổ bị chặn dưới, tránh xa 0.

**Vì sao ngành công nghệ quan tâm.**

- Mạng bền vững: ít cạnh nhưng khó bị cắt rời.  
- Giảm dùng tính ngẫu nhiên trong thuật toán (derandomization) và lý thuyết mã.  
- Cấu trúc mạng truyền thông hiệu quả.  
- Chặn thời gian trộn cho các thuật toán MCMC.

Bạn không cần thuộc các cách xây dựng đồ thị giãn nở (Margulis, đồ thị Ramanujan LPS, đồ thị chính quy ngẫu nhiên) để hiểu ý chính: **độ giãn nở là cách định lượng của "không có nút thắt cổ chai".** Thêm cạnh không phải lúc nào cũng làm mạng tốt hơn, vì chi phí, tắc nghẽn và bề mặt tấn công đều tăng; đồ thị giãn nở cân bằng tối ưu giữa các yếu tố này.

---

## 8. Quy mô, thế giới nhỏ và khoa học mạng

Các mạng thực tế thường có:

- **Phân phối bậc có đuôi nặng** (có các nút trung tâm, hub),  
- **Khoảng cách kiểu thế giới nhỏ** (đường đi ngắn dù các nút có xu hướng tụ cụm),  
- **Cấu trúc cộng đồng** (dày đặc bên trong, thưa thớt giữa các nhóm).

Để mô tả những điều này, ta cần các mô hình đồ thị ngẫu nhiên (Erdős–Rényi, mô hình cấu hình, gắn kết ưu tiên, mô hình khối ngẫu nhiên) không kém gì lý thuyết đồ thị thuần túy; [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) lại xuất hiện. Ngưỡng bùng phát dịch, tiếp thị lan truyền, sụp đổ dây chuyền đều là các quá trình động lực diễn ra *trên* đồ thị.

**Mạng nơ-ron đồ thị (GNN)** học đặc trưng bằng cách truyền thông tin dọc theo các cạnh, tức là đại số tuyến tính có cấu trúc theo $$E$$. Điều này nối bài này với học máy hiện đại ([Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/)). Xem thêm [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/).

---

## 9. Nói thật về độ phức tạp

Nhiều bài toán trên đồ thị là dễ (liên thông, cây khung nhỏ nhất, ghép cặp trên đồ thị hai phía, luồng cực đại với các thuật toán tốt). Nhiều bài toán khác là khó (chu trình Hamilton, lát cắt cực đại tổng quát, nhiều mục tiêu phát hiện cộng đồng). Bài toán đẳng cấu đồ thị từ lâu có vị trí đặc biệt, và nay đã có thuật toán thời gian tựa đa thức (quasi-polynomial). Trong thực tế, kỹ thuật vượt qua khó khăn bằng cách:

1. Nhận ra đúng các trường hợp đặc biệt,  
2. Dùng thuật toán xấp xỉ,  
3. Khai thác cấu trúc (đồ thị phẳng, độ rộng cây nhỏ, đồ thị thưa),  
4. Dùng heuristic có kiểm chứng.

Lý thuyết đồ thị vừa cung cấp các thuật toán thời gian đa thức, vừa vẽ ra bản đồ những bài toán khó.

---

### Tóm tắt toán học về mạng (từ phần tìm hiểu video)

- **Luồng cực đại – lát cắt cực tiểu:** dung lượng của mạng vừa là câu hỏi về luồng, vừa là câu hỏi về lát cắt.
- **PageRank:** vectơ riêng trội, hay phân phối dừng của bước ngẫu nhiên có hệ số tắt dần; đại số tuyến tính trên đồ thị web.
- **Đồ thị giãn nở:** thưa nhưng kết nối rất tốt; khoảng cách phổ là thước đo định lượng cốt lõi.
- Nên bắt đầu với các khóa toán rời rạc và thuật toán trên MIT OCW, rồi đến phần phổ trong bài này.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Đồ thị chỉ dùng cho mạng xã hội." | Đồ thị mô tả mọi quan hệ theo cặp: logistics, chip, phân tử, mã nguồn. |
| "PageRank là đếm số liên kết trỏ đến." | PageRank là trạng thái cân bằng của bước ngẫu nhiên, một vectơ riêng toàn cục. |
| "Đường ngắn nhất là đường qua ít nút nhất." | Chỉ đúng khi không có trọng số; trọng số biểu diễn thời gian hay chi phí. |
| "Luồng cực đại chỉ dùng cho đường ống." | Ghép cặp, phân vùng ảnh, độ tin cậy mạng đều quy về luồng và lát cắt. |
| "Bài toán trên đồ thị đều dễ." | Nhiều bài là NP-khó; cấu trúc đồ thị đóng vai trò quan trọng. |

---

## Bài tập

1. Vẽ 4 trang web với 6 liên kết; chỉ ra đỉnh không có liên kết nào trỏ đến.  
2. Vì sao BFS tìm được đường đi ngắn nhất trên đồ thị không trọng số?  
3. Viết hai câu về định lý luồng cực đại – lát cắt cực tiểu: lát cắt cực tiểu chứng nhận điều gì?  
4. Vì sao một trang có ít liên kết trỏ đến vẫn có thể xếp hạng cao hơn một trang có nhiều liên kết từ các trang kém chất lượng?  
5. Mô hình hóa một bản đồ tàu điện nhỏ bằng đồ thị. Với hành khách, "ngắn nhất" nghĩa là gì?  
6. Đại lượng $$x^\top Lx=\sum_{ij\in E}(x_i-x_j)^2$$ đo điều gì?  
7. Nâng cao: giải thích độ giãn nở theo cạnh và thế nào là "đồ thị giãn nở tốt" bằng lời thường.

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/graph-theory-networks/`.

**Thứ tự xem gợi ý**

1. **FOUNDATION** — MIT 6.042J Mathematics for Computer Science (graphs modules): [https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/).
2. **FOUNDATION** — MIT 6.006 Introduction to Algorithms (graph algorithms): [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
3. **ORIENTATION** — Numberphile — Graph theory / networks culture (search: graphs Numberphile): [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).
4. **ORIENTATION** — Numberphile — Seven Bridges of Königsberg culture: [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).
5. **INTUITION** — 3Blue1Brown — Eigenvectors and eigenvalues (spectral seeds): [https://www.youtube.com/watch?v=PFDu9oVAE-g](https://www.youtube.com/watch?v=PFDu9oVAE-g).
6. **CORE** — PageRank: A Trillion Dollar Algorithm (popular CS explainer): [https://www.youtube.com/watch?v=JGQe4kiPnrU](https://www.youtube.com/watch?v=JGQe4kiPnrU).

Danh mục URL đầy đủ: `research/video-research/graph-theory-networks/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/graph-theory-networks/transcripts/` · trạng thái: `research/video-research/graph-theory-networks/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/graph-theory-networks_W18FDEA1jRQ_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/graph-theory-networks/references.md`.

### Video (lộ trình chính)

1. MIT 6.042J Mathematics for Computer Science (graphs modules) — https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/
2. MIT 6.006 Introduction to Algorithms (graph algorithms) — https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
3. Numberphile — Graph theory / networks culture (search: graphs Numberphile) — https://www.youtube.com/watch?v=W18FDEA1jRQ
4. Numberphile — Seven Bridges of Königsberg culture — https://www.youtube.com/watch?v=W18FDEA1jRQ
5. 3Blue1Brown — Eigenvectors and eigenvalues (spectral seeds) — https://www.youtube.com/watch?v=PFDu9oVAE-g
6. PageRank: A Trillion Dollar Algorithm (popular CS explainer) — https://www.youtube.com/watch?v=JGQe4kiPnrU
7. Stanford / network science lectures (Barabási-style surveys) — https://en.wikipedia.org/wiki/Network_science
8. Spectral graph theory intro talks (Spielman culture) — https://cs-www.cs.yale.edu/homes/spielman/sagt/

### Video (tìm thêm / phụ)

9. Algorithms Illuminated / Roughgarden graph modules — https://www.algorithmsilluminated.org/

### Bài báo, sách, OCW và web

10. Brin & Page — The Anatomy of a Large-Scale Hypertextual Web Search Engine: http://infolab.stanford.edu/~backrub/google.html
11. Wikipedia — Graph theory: https://en.wikipedia.org/wiki/Graph_theory
12. Wikipedia — Max-flow min-cut theorem: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
13. Wikipedia — PageRank: https://en.wikipedia.org/wiki/PageRank
14. Wikipedia — Expander graph: https://en.wikipedia.org/wiki/Expander_graph
15. Spielman — Spectral Graph Theory notes: https://cs-www.cs.yale.edu/homes/spielman/sagt/

### Trong khóa

16. Khóa: [Network Science]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/). Gói: `research/video-research/graph-theory-networks/`.

## Hướng đi tiếp

- [Tối ưu → Vận hành & AI]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).  
- [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/).  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [The Seven Bridges of Königsberg - Numberphile](https://www.youtube.com/watch?v=W18FDEA1jRQ) (Numberphile, tiếng Anh). Bài toán bảy cây cầu Königsberg, khởi đầu lịch sử của lý thuyết đồ thị. Nên xem trước khi đọc §1.
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) (3Blue1Brown, tiếng Anh). Giải thích trực quan vectơ riêng và giá trị riêng, cần cho §5 và §6.
- [PageRank: A Trillion Dollar Algorithm](https://www.youtube.com/watch?v=JGQe4kiPnrU) (Reducible, tiếng Anh). Trình bày PageRank qua bước ngẫu nhiên và chuỗi Markov. Xem sau khi đọc §5.
