---
layout: post
title: "Khoa học Mạng"
chapter: '06'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Thành phố không chỉ nhà; còn đường. Não không chỉ nơ-ron; còn synapse. Dịch bệnh không chỉ virus; còn ai gặp ai. **Khoa học mạng** nghiên cứu cấu trúc và động lực trên đồ thị—đỉnh và cạnh—qua xã hội, hạ tầng, sinh học, thông tin. Lĩnh vực nằm giữa lý thuyết đồ thị, xác suất, vật lý thống kê và phân tích dữ liệu. Thành công có thật (ngưỡng dịch trên đồ thị tiếp xúc, xếp hạng web). Overclaim cũng có thật (“mọi thứ scale-free”, “một chỉ số centrality tìm người quan trọng”).

Thang học: đồ thị → mô hình ngẫu nhiên → bậc → small world → động lực trên mạng → suy diễn từ dữ liệu → giới hạn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa $$G=(V,E)$$ và thống kê cơ bản (bậc, độ dài đường, clustering).
- Đối chiếu Erdős–Rényi, configuration/heavy-tail, small-world ở mức cơ chế.
- Giải thích lan truyền/dịch trên mạng và vì sao ngưỡng mean-field có thể phụ thuộc cấu trúc bậc.
- Hiểu degree, betweenness, eigenvector-centrality là câu hỏi toán khác nhau.
- Nêu được/không được kết luận gì từ một plot phân bố bậc.
- Phê folklore scale-free và “six degrees” (**LO6**: không gộp slogan với thống kê fit).

**Kiến thức nền.** Xác suất và tổ hợp cơ bản; phổ Laplacian nếu biết đại số tuyến tính.

---

## 1. Đối tượng: đồ thị và ma trận

Đồ thị vô hướng đơn $$G=(V,E)$$; bậc $$k_i$$ đếm cạnh tới; ma trận kề $$A$$ với $$A_{ij}=1$$ nếu $$\{i,j\}\in E$$, đối xứng khi vô hướng. Đường đi, thành phần liên thông, khoảng cách $$d(i,j)$$, đường kính, clustering đo hình học rời rạc trên $$(V,E)$$.

Đồ thị có hướng, trọng số, cạnh thời gian, siêu đồ thị làm giàu mô hình. Chọn “cạnh nghĩa là gì” đã là hành vi khoa học: “mạng xã hội” có thể là bạn bè, cuộc gọi, đồng tác giả, đồng vị trí—mỗi lựa chọn một đồ thị khác.

---

## 2. Đồ thị ngẫu nhiên: đường chuẩn

**Erdős–Rényi** $$G(n,p)$$: mỗi cạnh trong $$\binom{n}{2}$$ độc lập với xác suất $$p$$; bậc kỳ vọng $$\lambda=(n-1)p$$. Ngưỡng nổi tiếng: thành phần khổng lồ khi $$\lambda$$ vượt $$1$$ (tiệm cận, phát biểu xác suất chặt). Phân bố bậc kiểu Poisson khi $$\lambda$$ cố định; clustering thường yếu so với nhiều dữ liệu xã hội.

**Configuration model** lấy mẫu theo dãy bậc cho trước—cho phép đuôi nặng. Preferential attachment (Barabási–Albert và họ) sinh hub và đuôi gần power-law dưới giả thiết mô hình: đỉnh mới gắn ưu tiên đỉnh bậc cao.

**Biết đọc.** “Scale-free” hay bị lạm dụng. Claim thực nghiệm cần thống kê cẩn (kích thước hữu hạn, likelihood fit, họ đuôi nặng thay thế). Plot log-log trông thẳng **không** phải định lý $$P(k)\propto k^{-\gamma}$$.

---

## 3. Small world và cấu trúc trung bình

Nhiều mạng thật: đường ngắn + clustering cao—**small world** (Watts–Strogatz: lattice vòng + rewire một phần cạnh; đường sụp, clustering giảm chậm hơn). “Sáu bước” là bóng văn hóa của đường ngắn; con số phụ thuộc định nghĩa cạnh và lấy mẫu.

**Cộng đồng:** modularity, spectral clustering, stochastic block model (SBM). SBM là mô hình sinh có nhãn nhóm; ngưỡng phục hồi nhãn nối ma trận ngẫu nhiên và lý thuyết thông tin. Không phải mọi đỉnh modularity là “cộng đồng thật”—resolution limit và overpartition là vấn đề đã biết.

---

## 4. Động lực trên mạng

**Dịch** SIS/SIR: nhiễm đi theo cạnh. Xấp xỉ mean-field/message-passing cho ngưỡng liên quan moment bậc; mạng dị thể có thể dễ bị lan vì hub. Trên configuration model, heuristic phổ biến liên quan $$\langle k^2\rangle/\langle k\rangle$$. Đây là **xấp xỉ có miền hợp lệ**, không luật phổ quát cho mọi khảo sát tiếp xúc.

**Khuếch tán/đồng thuận:** $$\dot x=-Lx$$ với Laplacian $$L=D-A$$; phổ điều khiển tốc độ thư giãn; algebraic connectivity (giá trị riêng thứ hai nhỏ nhất) đo “gắn kết” cho khuếch tán.

**Random walk / xếp hạng:** phân phối dừng của walk nền tảng ranking (PageRank như walk damped); eigenvector centrality dùng vector riêng chính của $$A$$. Bậc cao ≠ betweenness cao ≠ PageRank cao nói chung.

### PageRank như câu chuyện đại số tuyến tính

Ý thô: trang quan trọng nếu trang quan trọng trỏ tới. Với ma trận hyperlink cột-ngẫu nhiên $$P$$ (hoặc quy ước hàng—nhất quán khi cài), tìm $$\pi$$ xác suất:

$$
\pi^\top = \pi^\top \bigl(\alpha P + (1-\alpha)ve^\top\bigr)
$$

với damping $$\alpha\in(0,1)$$ và vector personalization $$v$$ (teleport Google sửa dangling node và bảo đảm duy nhất phân phối dừng). Đây là sự kiện eigenvector/Markov, không phép màu. Đổi tập cạnh, teleport hay snapshot crawl đổi hạng—**đồ thị là lựa chọn mô hình**.

---

## 5. Robust, cascade, điều khiển

Percolation: mạng vỡ khi gỡ đỉnh/cạnh—ngẫu nhiên hay nhắm hub. Mạng đuôi nặng có thể bền với lỗi ngẫu nhiên nhưng mong manh với tấn hub **trong mô hình lý tưởng**. Cascade (lưới điện, tài chính) cần động lực tải, không chỉ topology. Controllability cấu trúc dùng matching; “driver node = người cần ảnh hưởng xã hội” là bước nhảy cần ngữ cảnh nhân quả và thể chế.

---

## 6. Suy diễn: từ dữ liệu đến đồ thị

Tái tạo mạng: cảm biến, khảo sát, vết số—ồn và bias. Cạnh thiếu/sai, lấy mẫu đỉnh bóp phân bố bậc và đường. Mạng thời gian cần đường tôn trọng thời gian; mạng multilayer ghép mode tương tác.

Mô hình thống kê (ERGM, SBM, graphon giới hạn dày) cho likelihood và tiệm cận. Graphon $$W:[0,1]^2\to[0,1]$$ mô tả giới hạn continuum của dãy đồ thị dày; mạng thưa cần công cụ khác. Đây là toán thuần gặp dữ liệu bẩn—không bên nào xóa bên kia.

---

## 7. Ứng dụng (nhãn cảnh báo)

| Lĩnh vực | Đồ thị điển hình | Cảnh báo |
|----------|------------------|----------|
| Dịch tễ | Tiếp xúc / di động | Thiếu báo; hành vi đổi |
| Thần kinh | Connectome | Thang; trọng số; động lực ≠ wiring |
| Hạ tầng | Lưới, giao thông | Cascade cần vật lý tải |
| Thông tin | Web, MXH | Bot, bias nền tảng |
| Sinh học | PPI, điều hòa | Nhiễu, ngữ cảnh |

Khoa học mạng là **thấu kính**, không phải lý thuyết đóng về xã hội hay sự sống.

---

## 8. Tiên phong

1. Tương tác bậc cao (hypergraph, phức simplicial) và khi nào chúng đổi động lực.  
2. Suy diễn nhân quả trên dữ liệu mạng quan sát.  
3. Mạng thời gian / thích nghi (cạnh rewire theo trạng thái).  
4. Riêng tư, công bằng, đạo đức đo trên mạng người.  
5. Thuật toán cộng đồng và graph learning quy mô lớn chặt.  
6. Geometric deep learning: học trên đồ thị mà không bỏ thống kê tỉnh táo.

### Branching process cho dịch (micro)

Trên configuration model, dịch sớm xấp xỉ branching process theo residual degree. Nếu kỳ vọng nhiễm thứ cấp từ láng giềng nhiễm > 1 thì bùng phát khổng lồ khả dĩ—liên quan $$\langle k(k-1)\rangle/\langle k\rangle$$, tức tỉ moment hai. Đuôi nặng thổi moment hai và có thể đẩy ngưỡng về 0 trong giới hạn vô hạn lý tưởng—**cơ chế toán**, không phải đạo đức “hub xấu”, và không tự động đúng cho mọi khảo sát tiếp xúc hữu hạn có clustering và hộ gia đình.

### Phổ Laplacian một đoạn

Giá trị riêng $$0=\lambda_1\le\lambda_2\le\cdots$$: $$\lambda_2>0$$ iff liên thông (đồ thị vô hướng đơn). $$\lambda_2$$ nhỏ = bottleneck, mixing chậm, “cộng đồng” yếu liên kết. Spectral clustering nhúng đỉnh rồi cluster Euclid—bước nhảy sang “cộng đồng xã hội học” vẫn cần kiểm chứng.

### Studio seminar

Tải (hoặc vẽ) một mạng nhỏ $$n\le 30$$: (a) phân bố bậc; (b) so ER cùng $$n$$ và bậc trung bình về clustering và đường trung bình; (c) chọn một centrality và viết *nhiệm vụ* mà nó đo. Thảo luận LO6: “gỡ hub chặn dịch” đúng trong mô hình nào, sai khi nào?

---

## Nhầm lẫn thường gặp

| Tuyên bố | Sửa |
|----------|-----|
| “Mạng thật luôn scale-free.” | Một số đuôi nặng; fit cẩn thận. |
| “Centrality = tầm quan trọng.” | Quan trọng cho *nhiệm vụ nào*? |
| “Small world ⇒ ai cũng có ảnh hưởng.” | Đường ngắn ≠ quyền lực đều. |
| “Gỡ hub luôn chặn dịch.” | Phụ thuộc mô hình và vận hành. |
| “Đồ thị quan sát đủ.” | Lấy mẫu bias là chuẩn. |
| “Mạng thay cơ chế miền.” | Topology ràng buộc; cơ chế miền vẫn cần. |

---

## Bài tập

1. Vẽ đồ thị 5 đỉnh; tính bậc và một ma trận khoảng cách.
2. Vì sao bậc trung bình $$1$$ đặc biệt với liên thông ER lớn?
3. Xây đồ thị nhỏ: max degree ≠ max betweenness.
4. Viết $$L$$ cho path 3 đỉnh; nhận xét kernel / chiều không gian riêng 0.
5. Vì sao $$\langle k^2\rangle$$ lớn có thể hạ ngưỡng dịch mean-field?
6. Ba lý do đồ thị follow Twitter ≠ “mạng xã hội quốc gia”.
7. Đọc paper power-law; ghi phương pháp fit và phân bố thay thế.

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/network-science/analysis.md`.

### Trạng thái

**Active interdisciplinary field.** Erdős–Rényi, small-world, scale-free models are classical baselines; inference and dynamics on networks remain research-active.

### Phát biểu / slogan cốt lõi

ER random graphs $$G(n,p)$$ have giant component threshold $$p\sim 1/n$$. Preferential attachment (Barabási–Albert) yields power-law degree tails under stated mechanisms — empirical claims need careful statistics.

### Định nghĩa cần cố định

- **Degree distribution.** $$P(k)=$$ fraction of vertices of degree $$k$$.
- **Adjacency matrix.** $$A_{ij}=1$$ if edge $$ij$$ (weighted variants exist).

### Vệ sinh khái niệm

- Assuming all real networks are scale-free without statistical tests.
- Confusing correlation with causal influence on graphs.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/network-science/`.

**Thứ tự gợi ý**

1. **Cốt lõi** — Barabási — Network Science: From Abstract to Physical (UiO): [https://www.youtube.com/watch?v=oqOyTdLsq3o](https://www.youtube.com/watch?v=oqOyTdLsq3o).  
2. **Cốt lõi** — Barabási — DTU Ørsted Lecture: Architecture of Complexity: [https://www.youtube.com/watch?v=ZmJ9c-daNDY](https://www.youtube.com/watch?v=ZmJ9c-daNDY).  
3. **Định hướng** — Systems Innovation — Centralized & Scale Free Networks: [https://www.youtube.com/watch?v=qmCrtuS9vtU](https://www.youtube.com/watch?v=qmCrtuS9vtU).  

**Nhắc trạng thái:** **Active interdisciplinary field.** Erdős–Rényi, small-world, scale-free models are classical baselines; inference and dynamics on networks remain research-active.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/network-science/transcripts/` · trạng thái: `research/video-research/network-science/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/network-science_oqOyTdLsq3o_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo

1. Newman — *Networks*.
2. Bollobás — random graphs; Watts–Strogatz (1998).
3. Survey SBM / cộng đồng (Abbe; Decelle et al.).
4. Review dịch trên mạng phức tạp (Pastor-Satorras et al.).
5. [Sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/), [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/).

---


Danh mục URL đầy đủ: `research/video-research/network-science/references.md`.

### Video (lộ trình gợi ý)

- Barabási — Network Science: From Abstract to Physical (UiO) (CORE): https://www.youtube.com/watch?v=oqOyTdLsq3o
- Barabási — DTU Ørsted Lecture: Architecture of Complexity (CORE): https://www.youtube.com/watch?v=ZmJ9c-daNDY
- Systems Innovation — Centralized & Scale Free Networks (ORIENTATION): https://www.youtube.com/watch?v=qmCrtuS9vtU

### Bài báo và web (từ gói nghiên cứu)

- Barabási — Network Science (free book): http://networksciencebook.com/
- Chapter 4 scale-free property: https://networksciencebook.com/chapter/4
- Wikipedia — Network science: https://en.wikipedia.org/wiki/Network_science
- Wikipedia — Barabási–Albert model: https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model
- Wikipedia — Erdős–Rényi model: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model
- Wikipedia — Small-world network: https://en.wikipedia.org/wiki/Small-world_network

### Khóa học

- Gói: `research/video-research/network-science/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- [Sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/) cho kinetics sau cạnh tương tác.
- [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) cho hardness bài đồ thị.
- Thực hành: so một mạng thật nhỏ với ER cùng $$n$$ và bậc trung bình.
- Đọc: chương đầu Newman → một review dịch-trên-mạng → một paper phê scale-free statistics.
- Luôn hỏi: *Cạnh nghĩa gì, và ai vắng khỏi tập đỉnh?*
