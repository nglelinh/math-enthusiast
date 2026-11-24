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

Năm 1736, cư dân thành phố Königsberg đố nhau một câu đố vui: liệu có thể đi dạo qua cả bảy cây cầu bắc qua sông Pregel, mỗi cây cầu đúng một lần rồi quay về không? Leonhard Euler không cần đi bộ một bước nào. Ông gạt bỏ bản đồ phố phường, rút gọn mỗi bờ sông và hòn đảo thành một chấm tròn, mỗi cây cầu thành một nét nối — và chỉ bằng vài dòng đếm số nét chạm vào mỗi chấm, ông chứng minh chuyến đi ấy bất khả thi. Khoa học về mạng lưới ra đời từ khoảnh khắc trừu tượng hóa giản dị đó.

Gần ba thế kỷ sau, bài toán không còn dừng ở bảy cây cầu. Thành phố không chỉ có nhà mà còn có mạng giao thông. Não không chỉ có nơ-ron mà còn có hàng trăm nghìn tỷ khớp nối synapse. Dịch bệnh không chỉ là câu chuyện của virus mà là câu chuyện *ai gặp ai*. **Khoa học mạng** (Network Science) nghiên cứu cấu trúc và các quá trình động lực diễn ra trên những đồ thị khổng lồ của xã hội, hạ tầng, sinh học và thông tin. Lĩnh vực này có những thành tựu rất thật — từ thuật toán PageRank định hình internet đến lý thuyết ngưỡng dịch trên đồ thị tiếp xúc — nhưng cũng đầy những khẩu hiệu bị phóng đại quá mức kiểu “mọi mạng trong tự nhiên đều scale-free” hay “một chỉ số độ trung tâm là đủ tìm ra người quan trọng nhất”.

Bài này đi dọc theo trục chính của ngành: đồ thị và ma trận → mô hình ngẫu nhiên → phân bố bậc và small world → động lực học trên mạng → suy luận đồ thị từ dữ liệu → giới hạn của cách nhìn mạng lưới.

---

## Bản đồ kiến thức nền: Khoa học mạng là gì và nghiên cứu những gì?

Nếu lý thuyết đồ thị cổ điển trong toán rời rạc thường xét các đồ thị nhỏ hoặc có cấu trúc đối xứng chặt chẽ, thì **Khoa học Mạng** (Network Science) lại đứng ở ngã tư của **lý thuyết đồ thị, xác suất, đại số tuyến tính và vật lý thống kê** để nghiên cứu các mạng có hàng nghìn đến hàng tỷ đỉnh. Ngành này xoay quanh bốn câu hỏi trung tâm:

1. **Cấu trúc tĩnh (Topology & Ma trận):** Một mạng lưới trông như thế nào khi ta không thể vẽ hết nó lên giấy? Ta dùng ma trận kề $$A$$, phân bố bậc $$P(k)$$, độ dài đường đi ngắn nhất, hệ số cụm (mức độ "bạn của bạn cũng là bạn") và các chỉ số độ trung tâm (centrality).
2. **Mô hình sinh ngẫu nhiên (Random Graph Models):** Cơ chế nào sinh ra hình dạng của mạng thực? Ta so sánh dữ liệu thật với các "mô hình chuẩn" như Erdős–Rényi (nối hoàn toàn ngẫu nhiên), Watts–Strogatz (thế giới nhỏ) và Barabási–Albert (gắn kết ưu tiên tạo hub).
3. **Động lực trên mạng (Dynamics on Networks):** Cấu trúc kết nối làm thay đổi quá trình diễn ra trên nó ra sao? Đó là sự lan truyền dịch bệnh (SIS/SIR), khuếch tán nhiệt và đồng thuận thông qua phổ của ma trận Laplacian $$L = D - A$$, hay bước đi ngẫu nhiên dẫn đến PageRank.
4. **Suy luận từ dữ liệu (Network Inference):** Ngoài đời, ta hiếm khi thấy trọn vẹn đồ thị thật — dữ liệu đo luôn thiếu cạnh, nhiễu và có thiên lệch lấy mẫu. Làm sao phát hiện cộng đồng (community detection) hay khôi phục mạng gốc mà không bị đánh lừa bởi nhiễu?

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Định nghĩa $$G=(V,E)$$ và các thống kê cơ bản (bậc, độ dài đường đi, hệ số cụm).
- Đối chiếu mô hình Erdős–Rényi, mô hình cấu hình (đuôi nặng) và small-world ở mức cơ chế.
- Giải thích sự lan truyền hay dịch bệnh trên mạng, và vì sao ngưỡng trong xấp xỉ trường trung bình có thể phụ thuộc vào cấu trúc bậc.
- Hiểu rằng độ trung tâm theo bậc, theo betweenness và theo vector riêng là những câu hỏi toán khác nhau.
- Nêu được từ đồ thị phân bố bậc ta kết luận được gì và không kết luận được gì.
- Phê phán quan niệm dân gian về scale-free và “sáu bậc xa cách”; đừng gộp khẩu hiệu với một thống kê được khớp.

**Kiến thức nền.** Xác suất và tổ hợp cơ bản; phổ của Laplacian nếu bạn đã biết đại số tuyến tính.

---

## 1. Đối tượng: đồ thị và ma trận

Đồ thị đơn vô hướng $$G=(V,E)$$; bậc $$k_i$$ là số cạnh nối với đỉnh $$i$$; ma trận kề $$A$$ có $$A_{ij}=1$$ nếu $$\{i,j\}\in E$$, và đối xứng khi đồ thị vô hướng. Đường đi, thành phần liên thông, khoảng cách $$d(i,j)$$, đường kính và hệ số cụm mô tả hình học rời rạc trên $$(V,E)$$.

Một chi tiết thú vị của ma trận kề là lũy thừa của nó có ý nghĩa tổ hợp ngay lập tức: phần tử $$(A^2)_{ij}$$ đếm đúng số đường đi độ dài 2 từ đỉnh $$i$$ đến đỉnh $$j$$, còn $$(A^3)_{ii}$$ đếm số tam giác đi qua đỉnh $$i$$. Nhờ cầu nối này, những câu hỏi hình học về đường đi và cụm trên đồ thị biến thành phép tính đại số tuyến tính.

Đồ thị có hướng, có trọng số, có cạnh theo thời gian, hay siêu đồ thị làm mô hình phong phú hơn. Việc quyết định “cạnh nghĩa là gì” đã là một lựa chọn khoa học: “mạng xã hội” có thể là bạn bè, cuộc gọi, đồng tác giả hoặc cùng địa điểm, và mỗi lựa chọn cho ra một đồ thị khác nhau.

---

## 2. Đồ thị ngẫu nhiên: các mô hình chuẩn

**Erdős–Rényi** $$G(n,p)$$: mỗi cạnh trong $$\binom{n}{2}$$ cạnh xuất hiện độc lập với xác suất $$p$$; bậc kỳ vọng là $$\lambda=(n-1)p$$. Ngưỡng nổi tiếng: xuất hiện **thành phần liên thông khổng lồ** khi $$\lambda$$ vượt qua $$1$$ (theo nghĩa tiệm cận, được phát biểu chặt chẽ bằng xác suất). Hãy hình dung bạn có 10.000 nút áo rải trên sàn và buộc ngẫu nhiên từng sợi dây giữa các cặp nút: khi trung bình mỗi nút mới có $$0.8$$ sợi dây, bạn chỉ thấy các cụm nhỏ rời rạc; nhưng vừa vượt qua ngưỡng trung bình $$1$$ sợi dây mỗi nút, một "mạng lưới khổng lồ" đột ngột kết tụ và gom một phần đáng kể toàn bộ số nút vào cùng một khối — giống hệt hiện tượng chuyển pha từ nước sang băng! Phân bố bậc của $$G(n,p)$$ có dạng Poisson khi $$\lambda$$ cố định (hiếm khi có đỉnh siêu nổi trội); hệ số cụm cũng thường rất thấp so với mạng xã hội thực.

**Mô hình cấu hình** lấy mẫu theo một dãy bậc cho trước, nên cho phép đuôi nặng. Gắn kết ưu tiên (Barabási–Albert và các mô hình cùng họ) tạo ra các hub và đuôi gần giống lũy thừa, dưới giả thiết của mô hình: đỉnh mới ưu tiên gắn vào đỉnh có bậc cao ("kẻ giàu càng giàu thêm").

**Cần đọc cho kỹ.** “Scale-free” bị lạm dụng khá nhiều. Một khẳng định thực nghiệm cần thống kê cẩn thận (kích thước hữu hạn, khớp bằng hàm hợp lý, so với các họ đuôi nặng khác như log-normal). Một đồ thị log-log trông thẳng **không** phải là định lý $$P(k)\propto k^{-\gamma}$$.

---

## 3. Small world và cấu trúc trung bình

Nhiều mạng thực vừa có **đường đi rất ngắn** (giống đồ thị ngẫu nhiên), vừa có **hệ số cụm cao** (giống mạng lưới láng giềng địa phương): đó là **small world**. Mô hình Watts–Strogatz giải thích cơ chế này cực kỳ gọn: bắt đầu từ một vòng tròn nơi mỗi người chỉ quen hàng xóm cạnh nhà (cụm rất cao, nhưng đường đi vòng quanh rất dài), rồi chỉ cần nối lại ngẫu nhiên một tỷ lệ nhỏ cạnh thành vài "đường tắt" xuyên qua vòng tròn. Kết quả thật bất ngờ: độ dài đường đi trung bình sụp xuống theo hàm logarit gần như ngay lập tức, trong khi hệ số cụm gần như chưa kịp giảm! “Sáu bước xa cách” là hình bóng văn hóa của hiện tượng đường đi ngắn này; con số cụ thể phụ thuộc vào định nghĩa cạnh và cách lấy mẫu.

**Cộng đồng:** độ module (modularity), phân cụm phổ, mô hình khối ngẫu nhiên (SBM). SBM là mô hình sinh có nhãn nhóm; ngưỡng để khôi phục nhãn nối với ma trận ngẫu nhiên và lý thuyết thông tin. Không phải cực đại nào của modularity cũng là “cộng đồng thật”: giới hạn độ phân giải và việc chia quá nhỏ là những vấn đề đã biết.

---

## 4. Động lực trên mạng

**Dịch** SIS/SIR: bệnh đi theo các cạnh. Các xấp xỉ trường trung bình và truyền thông điệp cho ngưỡng liên quan đến các moment của bậc; mạng không đồng đều có thể dễ bị lan dịch vì có hub. Một trực giác nổi tiếng ở đây là **nghịch lý tình bạn**: trung bình, bạn bè của bạn có *nhiều bạn hơn chính bạn* — đơn giản vì người có 100 bạn xuất hiện trong danh sách bạn bè của 100 người, còn người có 1 bạn chỉ xuất hiện 1 lần. Do đó, virus khi đi dọc theo một cạnh ngẫu nhiên có xác suất rất cao va ngay vào một hub. Với mô hình cấu hình, heuristic thường dùng liên quan đến $$\langle k^2\rangle/\langle k\rangle$$. Đây là **một xấp xỉ có miền hợp lệ**, không phải luật chung cho mọi khảo sát tiếp xúc.

**Khuếch tán và đồng thuận:** $$\dot x=-Lx$$ với Laplacian $$L=D-A$$; phổ của nó quyết định tốc độ về cân bằng; độ liên thông đại số (giá trị riêng nhỏ thứ hai) đo mức “gắn kết” đối với khuếch tán.

**Bước ngẫu nhiên và xếp hạng:** phân phối dừng của bước ngẫu nhiên là nền tảng của việc xếp hạng (PageRank là bước ngẫu nhiên có damping); độ trung tâm vector riêng dùng vector riêng chính của $$A$$. Nói chung, bậc cao không kéo theo betweenness cao, và cũng không kéo theo PageRank cao — một đỉnh chỉ có bậc 2 nhưng là cây cầu duy nhất nối hai thành phố lớn sẽ có betweenness cực lớn dù bậc rất nhỏ.

### PageRank dưới góc nhìn đại số tuyến tính

Ý tưởng thô: một trang quan trọng nếu có những trang quan trọng trỏ tới nó. Với ma trận siêu liên kết ngẫu nhiên theo cột $$P$$ (hoặc quy ước theo hàng; miễn là nhất quán khi cài đặt), ta tìm phân phối xác suất $$\pi$$ thỏa:

$$
\pi^\top = \pi^\top \bigl(\alpha P + (1-\alpha)ve^\top\bigr)
$$

với hệ số damping $$\alpha\in(0,1)$$ và vector cá nhân hóa $$v$$ (bước “teleport” của Google xử lý các đỉnh cụt và bảo đảm phân phối dừng là duy nhất). Đây chỉ là chuyện vector riêng và xích Markov, không có phép màu nào. Thay đổi tập cạnh, cách teleport hay thời điểm chụp dữ liệu sẽ đổi thứ hạng: **đồ thị là một lựa chọn mô hình hóa**.

---

### Video ngắn: PageRank trên đồ thị 4 trang web với nút cụt và teleport α = 0,85

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/pagerank-markov_vi.mp4"></video>
</div>

Video dài khoảng 2 phút 03 giây (có thuyết minh tiếng Việt): ý tưởng xếp hạng qua liên kết, ma trận chuyển thô P₀ và bẫy nút cụt D, cách thêm teleport α = 0,85, tính tay bước k = 1, lặp lũy thừa hội tụ về π và so sánh α = 0,85 với α = 0,50.


<div class="interactive-demo" markdown="1">
<div data-demo="pagerank-explainer" data-preset="dangling" data-alpha="0.85" data-lang="vi"></div>
</div>
<script src="{{ '/public/js/explainers/pagerank-explainer.js' | relative_url }}"></script>

## 5. Độ bền vững, hiệu ứng dây chuyền và điều khiển

Thấm (percolation): mạng vỡ ra khi gỡ bỏ đỉnh hoặc cạnh, ngẫu nhiên hoặc nhắm vào hub. Trong mô hình lý tưởng, mạng đuôi nặng bền với lỗi ngẫu nhiên (vì phần lớn đỉnh có bậc thấp, mất vài đỉnh ngẫu nhiên ít ảnh hưởng toàn cục) nhưng lại cực kỳ mong manh trước tấn công nhắm thẳng vào hub. Hiệu ứng dây chuyền (lưới điện, tài chính) cần có động lực học của tải chứ không chỉ topology. Khả năng điều khiển theo cấu trúc dùng đến bài toán ghép cặp (matching); còn nói “nút điều khiển là người cần tác động trong xã hội” là một bước nhảy cần có ngữ cảnh nhân quả và thể chế.

---

## 6. Suy luận: từ dữ liệu đến đồ thị

Dựng lại mạng từ cảm biến, khảo sát hay dấu vết số đều có nhiễu và thiên lệch. Cạnh thiếu hoặc sai, và việc lấy mẫu đỉnh làm sai lệch phân bố bậc và độ dài đường đi. Mạng thời gian cần đường đi tôn trọng thứ tự thời gian; mạng đa lớp ghép nhiều kiểu tương tác.

Các mô hình thống kê (ERGM, SBM, graphon cho giới hạn của đồ thị dày) cho ta hàm hợp lý và kết quả tiệm cận. Graphon $$W:[0,1]^2\to[0,1]$$ mô tả giới hạn liên tục của một dãy đồ thị dày; với mạng thưa cần công cụ khác. Đây là toán thuần túy gặp dữ liệu bẩn, và bên nào cũng không thay thế được bên kia.

---

## 7. Ứng dụng (kèm lưu ý)

| Lĩnh vực | Đồ thị điển hình | Lưu ý |
|----------|------------------|-------|
| Dịch tễ | Tiếp xúc / di chuyển | Báo cáo thiếu; hành vi thay đổi |
| Thần kinh | Connectome | Thang đo; trọng số; động lực không chỉ là sơ đồ đi dây |
| Hạ tầng | Lưới điện, giao thông | Hiệu ứng dây chuyền cần vật lý của tải |
| Thông tin | Web, mạng xã hội | Bot, thiên lệch của nền tảng |
| Sinh học | Tương tác protein, điều hòa | Nhiễu, phụ thuộc ngữ cảnh |

Khoa học mạng là một **thấu kính**, không phải lý thuyết hoàn chỉnh về xã hội hay sự sống.

---

## 8. Các hướng tiên phong

1. Tương tác bậc cao (siêu đồ thị, phức simplicial) và khi nào chúng làm đổi động lực.  
2. Suy luận nhân quả trên dữ liệu mạng quan sát được.  
3. Mạng thời gian và mạng thích nghi (cạnh nối lại theo trạng thái).  
4. Quyền riêng tư, công bằng và đạo đức khi đo đạc trên mạng người.  
5. Thuật toán cộng đồng và học trên đồ thị ở quy mô lớn, có bảo đảm chặt chẽ.  
6. Học sâu hình học: học trên đồ thị mà vẫn giữ được thống kê tỉnh táo.

### Quá trình phân nhánh cho dịch (bản rút gọn)

Trên mô hình cấu hình, giai đoạn đầu của dịch xấp xỉ một quá trình phân nhánh theo bậc dư (số cạnh còn lại của một láng giềng). Nếu số ca thứ cấp kỳ vọng từ một láng giềng nhiễm lớn hơn 1 thì có thể bùng phát thành dịch lớn; điều này liên quan đến $$\langle k(k-1)\rangle/\langle k\rangle$$, tức tỉ số moment bậc hai. Đuôi nặng làm moment bậc hai rất lớn và có thể kéo ngưỡng về 0 trong giới hạn vô hạn lý tưởng. Đó là một **cơ chế toán học**, không phải lời phán xét kiểu “hub là xấu”, và không tự động đúng cho mọi khảo sát tiếp xúc hữu hạn có hệ số cụm và hộ gia đình.

### Phổ Laplacian trong một đoạn

Các giá trị riêng $$0=\lambda_1\le\lambda_2\le\cdots$$: $$\lambda_2>0$$ khi và chỉ khi đồ thị liên thông (đồ thị đơn vô hướng). $$\lambda_2$$ nhỏ nghĩa là có nút thắt cổ chai, trộn chậm, các “cộng đồng” liên kết yếu với nhau. Phân cụm phổ nhúng các đỉnh vào không gian Euclid rồi phân cụm; để nói đó là “cộng đồng xã hội học” thì còn cần kiểm chứng thêm.

### Hoạt động nhóm

Tải (hoặc vẽ) một mạng nhỏ với $$n\le 30$$: (a) vẽ phân bố bậc; (b) so với mạng Erdős–Rényi có cùng $$n$$ và bậc trung bình, về hệ số cụm và độ dài đường đi trung bình; (c) chọn một chỉ số trung tâm và viết ra *nhiệm vụ* mà nó đo. Thảo luận: “gỡ hub để chặn dịch” đúng trong mô hình nào, và sai khi nào?

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|-----------|
| “Mạng thực luôn là scale-free.” | Một số mạng có đuôi nặng; cần khớp cẩn thận. |
| “Độ trung tâm chính là tầm quan trọng.” | Quan trọng cho *nhiệm vụ nào*? |
| “Small world nghĩa là ai cũng có ảnh hưởng.” | Đường đi ngắn không có nghĩa quyền lực đều nhau. |
| “Gỡ hub luôn chặn được dịch.” | Phụ thuộc vào mô hình và cách vận hành. |
| “Đồ thị quan sát được là đầy đủ.” | Thiên lệch do lấy mẫu là chuyện bình thường. |
| “Mạng thay thế cho cơ chế của chuyên ngành.” | Topology đặt ràng buộc; cơ chế của chuyên ngành vẫn cần. |

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**Một lĩnh vực liên ngành đang hoạt động.** Erdős–Rényi, small-world và scale-free là các mô hình cổ điển để đối chiếu; suy luận và động lực trên mạng vẫn đang được nghiên cứu.

### Phát biểu cốt lõi

Đồ thị ngẫu nhiên ER $$G(n,p)$$ có ngưỡng xuất hiện thành phần khổng lồ ở $$p\sim 1/n$$. Gắn kết ưu tiên (Barabási–Albert) tạo ra đuôi lũy thừa của phân bố bậc dưới các cơ chế đã nêu; còn khẳng định về dữ liệu thực cần thống kê cẩn thận.

### Định nghĩa cần nhớ

- **Phân bố bậc.** $$P(k)=$$ tỉ lệ các đỉnh có bậc $$k$$.
- **Ma trận kề.** $$A_{ij}=1$$ nếu có cạnh $$ij$$ (còn có các biến thể có trọng số).

### Cần phân biệt rõ

- Cho rằng mọi mạng thực đều scale-free mà không kiểm định thống kê.
- Nhầm tương quan với ảnh hưởng nhân quả trên đồ thị.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Cốt lõi**: Barabási, Network Science: From Abstract to Physical (UiO): [https://www.youtube.com/watch?v=oqOyTdLsq3o](https://www.youtube.com/watch?v=oqOyTdLsq3o).  
2. **Cốt lõi**: Barabási, DTU Ørsted Lecture: Architecture of Complexity: [https://www.youtube.com/watch?v=ZmJ9c-daNDY](https://www.youtube.com/watch?v=ZmJ9c-daNDY).  
3. **Định hướng**: Systems Innovation, Centralized & Scale Free Networks: [https://www.youtube.com/watch?v=qmCrtuS9vtU](https://www.youtube.com/watch?v=qmCrtuS9vtU).  

**Lưu ý về hiện trạng:** đây là lĩnh vực liên ngành đang hoạt động. Các mô hình Erdős–Rényi, small-world và scale-free là mốc so sánh cổ điển; suy luận và động lực trên mạng vẫn là chủ đề nghiên cứu.

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/network-science_oqOyTdLsq3o_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Newman — *Networks*.
2. Bollobás — đồ thị ngẫu nhiên; Watts–Strogatz (1998).
3. Bài khảo sát về SBM và cộng đồng (Abbe; Decelle và cộng sự).
4. Bài tổng quan về dịch trên mạng phức tạp (Pastor-Satorras và cộng sự).
5. [Sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/), [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/).

---

### Video (lộ trình gợi ý)

- Barabási, Network Science: From Abstract to Physical (UiO) (cốt lõi): https://www.youtube.com/watch?v=oqOyTdLsq3o
- Barabási, DTU Ørsted Lecture: Architecture of Complexity (cốt lõi): https://www.youtube.com/watch?v=ZmJ9c-daNDY
- Systems Innovation, Centralized & Scale Free Networks (định hướng): https://www.youtube.com/watch?v=qmCrtuS9vtU

### Bài báo và web

- Barabási — Network Science (free book): http://networksciencebook.com/
- Chapter 4 scale-free property: https://networksciencebook.com/chapter/4
- Wikipedia — Network science: https://en.wikipedia.org/wiki/Network_science
- Wikipedia — Barabási–Albert model: https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model
- Wikipedia — Erdős–Rényi model: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model
- Wikipedia — Small-world network: https://en.wikipedia.org/wiki/Small-world_network


## Hướng đi tiếp

- [Sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/) cho động học đằng sau các cạnh tương tác.
- [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) cho độ khó của các bài toán đồ thị.
- Thực hành: so một mạng thực nhỏ với mạng ER có cùng $$n$$ và bậc trung bình.
- Đọc: chương đầu của Newman, rồi một bài tổng quan về dịch trên mạng, rồi một bài phê phán thống kê scale-free.
- Luôn hỏi: *cạnh nghĩa là gì, và ai vắng mặt trong tập đỉnh?*

## Video tham khảo

- **Xem trước** — [Albert-László Barabási – Network Science: From Abstract to Physical Networks](https://www.youtube.com/watch?v=oqOyTdLsq3o) — UiO Realfagsbiblioteket, tiếng Anh. Xem trước để có cái nhìn chung về khoa học mạng, từ đồ thị trừu tượng đến mạng vật lý.
- [DTU Ørsted Lecture, Albert-László Barabási, Network Science: Decoding the Architecture of Complexity](https://www.youtube.com/watch?v=ZmJ9c-daNDY) — DTUdk, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để thấy bức tranh rộng hơn về kiến trúc của các hệ phức tạp.
- [Centralized & Scale Free Networks](https://www.youtube.com/watch?v=qmCrtuS9vtU) — Systems Innovation Network, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, về mạng tập trung và mạng scale-free.
