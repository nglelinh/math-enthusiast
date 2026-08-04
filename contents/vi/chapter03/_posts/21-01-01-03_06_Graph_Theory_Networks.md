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

Đường sá, siêu liên kết, phân tử, quan hệ xã hội, dây chip và đồ thị phụ thuộc gói phần mềm—cho đến khi nhãn khác đi—đều cùng một loại đối tượng: **đỉnh** nối bởi **cạnh**. Lý thuyết đồ thị—từng là anh em giải trí của tổ hợp—nay định tuyến gói tin, xếp hạng trang web, phân bổ luồng và phân tích dịch.

**Lộ trình:** đồ thị như mô hình → đường đi & liên thông → cây & chu trình → luồng & cắt → bước ngẫu nhiên & PageRank → expander → thuật toán quy mô → nhầm lẫn.

Bài này vẽ **cơ chế**: ý tưởng đồ thị nào thành công nghệ mạng nào, và vì sao đại số tuyến tính trên ma trận kề ngồi cạnh thuật toán rời rạc.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô hình hóa hệ thật như $$G=(V,E)$$ (có hướng/không, có trọng/không) và nói đỉnh–cạnh là gì.
- Giải thích liên thông, đường ngắn nhất, vì sao BFS/Dijkstra quan trọng cho định tuyến và logistics.
- Nêu ý max-flow min-cut mức khẩu hiệu và một ứng dụng.
- Mô tả **PageRank** như bước ngẫu nhiên / vector riêng trên đồ thị web.
- Nói expander mua gì (liên thông tốt với ít cạnh) mức trực giác.
- Tránh “đồ thị chỉ mạng xã hội” và “PageRank chỉ đếm liên kết vào.”

**Kiến thức nền.** Toán rời rạc cơ bản. Hữu ích: [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

**Liên kết.** [Khoa học mạng (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), [Định lý bốn màu]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/).

---

## 1. Đồ thị: đại số của kết nối

$$G=(V,E)$$: đỉnh và cạnh (cặp hoặc cặp có thứ tự). Cạnh có thể mang **trọng** (khoảng cách, dung lượng, ái lực).

| Hệ | Đỉnh | Cạnh |
|----|------|------|
| Bản đồ đường | Giao lộ | Đoạn đường |
| Web | Trang | Siêu liên kết (có hướng) |
| Xã hội | Người/tài khoản | Follow, bạn bè |
| Mạch | Linh kiện/net | Dây |
| ML | Tensor/op | Phụ thuộc dữ liệu |

**Khẩu hiệu.** *Khi “ai nối ai” lấn át “ở đâu trong không gian Euclid,” ngôn ngữ đồ thị là hệ tọa độ đúng.*

Ma trận kề $$A$$: $$A^k$$ đếm đường đi dài $$k$$; khe phổ điều khiển trộn.

---

## 2. Đường đi, khoảng cách, liên thông

**Khoảng cách** $$d(u,v)$$ là độ dài đường ngắn nhất. **Liên thông** hỏi mọi cặp có đường nối không; đồ thị có hướng tinh chỉnh thành thành phần liên thông mạnh/yếu. Cầu và đỉnh cắt là điểm thất bại đơn.

**Thuật toán xây ngành.** BFS (không trọng); Dijkstra (trọng không âm—lõi GPS); A\* (heuristic); Bellman–Ford / Floyd–Warshall (tổng quát hơn, đắt hơn).

**Cơ chế.** *Định tuyến là tìm kiếm tối ưu trên đồ thị; “đường tốt nhất” là bài tối ưu tổ hợp được đặt đúng, không phải thẩm mỹ bản đồ.*

---

## 3. Cây, khung, chu trình

**Cây:** liên thông, không chu trình; $$|E|=|V|-1$$. **Cây khung cực tiểu (MST)** (Kruskal, Prim) thiết kế hạ tầng nối rẻ. Chu trình tạo dự phòng (tốt cho chịu lỗi) và phức tạp. Hamilton khó NP—văn hóa [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

---

## 4. Luồng và cắt

Gán **dung lượng** $$c(e)\ge 0$$. **Luồng** chuyển từ nguồn $$s$$ tới đích $$t$$ không vượt dung lượng, bảo toàn tại nút giữa. **Định lý max-flow min-cut:**

$$
\max\mathrm{flow}(s,t)=\min\mathrm{cut}(s,t).
$$

Ứng dụng: giao thông, logistics; matching hai phía; phân đoạn ảnh (graph cut); độ tin cậy.

**Cơ chế.** *Nút thắt là cắt; thuật toán tìm cấu trúc tăng luồng đến khi một cắt chứng nhận tối ưu.*

Tinh thần dual giống [tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).

---

## 5. Bước ngẫu nhiên và PageRank

Bước ngẫu nhiên trên đồ thị có hướng di chuyển từ nút theo cạnh ra (đều hoặc theo trọng). Dưới điều kiện ôn hòa, bước có **phân phối dừng** $$\pi$$ thỏa $$\pi^\top=\pi^\top P$$ với ma trận chuyển $$P$$—bài vector riêng trái với giá trị riêng $$1$$.

**PageRank** (Brin–Page) mô hình người lướt web: thường theo liên kết, thỉnh thoảng nhảy (teleport) sang trang ngẫu nhiên. Vector xếp hạng là phân phối dừng—tương đương nghiệm hệ tuyến tính

$$
\pi=\alpha P^\top\pi+(1-\alpha)v,
$$

với damping $$\alpha$$ và vector teleport $$v$$. Tầm quan trọng không phải in-degree thô: liên kết từ trang hạng cao nặng hơn, và cấu trúc liên thông mạnh tương tác với bước ngẫu nhiên.

**Cơ chế.** *Tầm quan trọng toàn cục trồi lên từ cấu trúc liên kết cục bộ qua vector riêng / giải tuyến tính—không phải bảng điểm viết tay.*

Biến thể nuôi gợi ý, chỉ số trích dẫn học thuật (có cảnh báo), và các độ trung tâm nút trong khoa học mạng ([Ch.6]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/)). PageRank cá nhân hóa (teleport thiên về tập seed) là ngựa thồ cho clustering đồ thị cục bộ và tính năng “trang liên quan.”

**Văn hóa lặp lũy thừa.** Thực tế hiếm khi dựng solver riêng dày: lặp tích ma trận–vector thưa với ma trận Google (hoặc giải tuyến tính tương đương) tính xếp hạng trên đồ thị tỷ cạnh. Khả năng mở rộng không phải hậu quả phụ; đó là lý do công thức vector riêng thắng lịch sử so với quy tắc chấm điểm cầu kỳ không lặp nhanh được.

---

## 6. Phổ đồ thị: Laplacian và cắt

Laplacian tổ hợp $$L=D-A$$ (ma trận bậc trừ kề) nửa xác định dương với $$L\mathbf{1}=0$$ trên đồ thị vô hướng. Giá trị riêng nhỏ thứ hai (liên thông đại số, giá trị Fiedler) khống chế mức “dính”; vector riêng gợi phân hoạch hai phần.

Spectral clustering, vẽ đồ thị, graph signal processing dùng cơ sở riêng của $$L$$ như phân tích Fourier dùng mũ phức—thật ra có loại suy chính xác (biến đổi Fourier trên đồ thị). Sparsifier xấp xỉ dạng toàn phương $$x^\top Lx$$ với ít cạnh hơn—lý thuyết đồ thị thuật toán gặp đại số tuyến tính số.

Công thức hữu ích:

$$
x^\top Lx=\sum_{ij\in E}(x_i-x_j)^2
$$

đo mức hàm $$x$$ trên đỉnh “nhảy” dọc cạnh: trơn trên đồ thị thì dạng toàn phương nhỏ.

---

## 7. Expander: thưa mà liên thông cực tốt

Họ **expander** là dãy đồ thị thưa với liên thông mạnh: mọi tập đỉnh có biên lớn tương đối kích thước (edge expansion). Tương đương gần đúng: bước ngẫu nhiên trộn nhanh; khe phổ bị chặn khỏi 0.

**Vì sao công nghệ quan tâm.**

- Mạng bền: ít cạnh, khó cắt rời.  
- Derandomization và lý thuyết mã.  
- Topology giao tiếp hiệu quả.  
- Chặn thời gian trộn cho MCMC.

Bạn không cần thuộc các xây dựng expander (Margulis, đồ thị Ramanujan LPS, regular ngẫu nhiên) để nắm khẩu hiệu: **expansion = dạng định lượng của “không có nút thắt.”** Thêm cạnh không luôn cải thiện mạng: chi phí, tắc nghẽn và bề mặt tấn công tăng; expander tối ưu hóa đánh đổi.

---

## 8. Quy mô, small-world và khoa học mạng

Mạng thực nghiệm thường hiện:

- **Bậc đuôi nặng** (hub),  
- **Khoảng cách small-world** (đường ngắn dù có clustering),  
- **Cấu trúc cộng đồng** (dày trong, thưa ngoài).

Đây là mô hình đồ thị xác suất (Erdős–Rényi, configuration model, preferential attachment, stochastic block model) nhiều như lý thuyết đồ thị thuần—[xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) quay lại. Ngưỡng dịch, marketing lan truyền, sụp đổ dây chuyền là động lực *trên* đồ thị.

**GNN** học đặc trưng bằng truyền tin theo cạnh—đại số tuyến tính cấu trúc bởi $$E$$—nối bài này với ML hiện đại ([Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/)). Xem [Network Science]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/).

---

## 9. Trung thực về độ phức tạp

Nhiều bài trên đồ thị dễ (liên thông, MST, matching hai phía, max flow thực tế với thuật toán tốt). Nhiều bài khó (chu trình Hamilton, max cut tổng quát, nhiều mục tiêu cộng đồng, đẳng cấu đồ thị từng tinh tế—nay quasi-polynomial). Kỹ thuật thắng bằng:

1. Trường hợp đặc biệt đúng,  
2. Xấp xỉ,  
3. Khai thác cấu trúc (planar, treewidth thấp, thưa),  
4. Heuristic có kiểm chứng.

Lý thuyết đồ thị vừa cung cấp động cơ đa thức thời gian vừa cung cấp bản đồ độ cứng.

---

### Khẩu hiệu toán mạng (từ nghiên cứu video)

- **Max-flow min-cut:** dung lượng vừa là câu hỏi luồng vừa là câu hỏi cắt.
- **PageRank:** vector riêng trội / phân phối dừng của bước ngẫu nhiên có damping — đại số tuyến tính trên đồ thị web.
- **Expanders:** thưa nhưng kết nối cực tốt; khe phổ là trái tim định lượng.
- Bắt đầu MIT OCW rời rạc/thuật toán, rồi phần phổ trong bài Ch.3.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Đồ thị chỉ MXH.” | Mọi quan hệ cặp: logistics, chip, phân tử, code. |
| “PageRank = đếm in-link.” | Cân bằng bước ngẫu nhiên / vector riêng toàn cục. |
| “Đường ngắn nhất = ít hop.” | Chỉ khi không trọng; trọng mã hóa thời gian/chi phí. |
| “Max flow chỉ cho ống.” | Matching, segmentation, reliability quy về flow/cut. |
| “Bài trên đồ thị đều dễ.” | Nhiều NP-khó; cấu trúc quan trọng. |

---

## Bài tập

1. Vẽ 4 trang web, 6 liên kết; chỉ đỉnh in-degree 0.  
2. Vì sao BFS tìm đường ngắn nhất không trọng?  
3. Hai câu: max-flow min-cut và cắt min chứng nhận gì?  
4. Vì sao trang ít in-link vẫn có thể hơn trang nhiều in-link kém chất lượng?  
5. Mã hóa bản đồ metro nhỏ; “ngắn nhất” nghĩa gì với hành khách?  
6. $$x^\top Lx=\sum_{ij\in E}(x_i-x_j)^2$$ đo gì?  
7. Nâng cao: edge expansion và “expander tốt” bằng lời thường.

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
- [Network Science]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/).  
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
