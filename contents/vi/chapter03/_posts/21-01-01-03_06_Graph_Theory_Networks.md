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

Năm 1736, cư dân thành phố Königsberg (Đông Phổ) thích đố nhau một câu đố giải trí cuối tuần: thành phố có hai hòn đảo nối với hai bờ sông bằng bảy cây cầu — liệu có thể đi dạo một vòng qua *đúng mỗi cây cầu một lần* rồi quay về không? Leonhard Euler nhận ra một điều thiên tài: chiều dài cây cầu hay hình dáng con sông hoàn toàn vô nghĩa. Nếu gom mỗi vùng đất thành một **chấm tròn (đỉnh)** và mỗi cây cầu thành một **nét nối (cạnh)**, lời giải hiện ra ngay trong vài dòng — và **lý thuyết đồ thị** ra đời từ câu đố dạo phố đó.

Gần ba thế kỷ sau, khi ta bóc bỏ lớp vỏ vật lý của bản đồ giao thông, mạng lưới siêu liên kết trên web, cấu trúc phân tử thuốc, sơ đồ dây dẫn trong vi mạch hay mạng xã hội hàng tỷ người, tất cả đều hiện nguyên hình là cùng một đối tượng toán học của Euler: các đỉnh nối với nhau bằng cạnh. Từ một trò tiêu khiển tổ hợp, lý thuyết đồ thị ngày nay định tuyến từng gói tin Internet, xếp hạng hàng tỷ trang web, điều phối chuỗi cung ứng và dự báo đường lây lan của dịch bệnh.

Bài này mở rõ **cơ chế**: chính xác ý tưởng nào của lý thuyết đồ thị biến thành công nghệ mạng nào, và vì sao đại số tuyến tính trên ma trận kề lại bắt tay chặt chẽ với các thuật toán rời rạc.

**Lộ trình:** bản đồ lý thuyết đồ thị → đồ thị làm mô hình → đường đi và tính liên thông → cây và chu trình → luồng và lát cắt → bước ngẫu nhiên và PageRank → phổ đồ thị (Laplacian) → đồ thị giãn nở (expander) → mạng thực tế và độ phức tạp → nhầm lẫn thường gặp.

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

## Bản đồ kiến thức nền: Lý thuyết đồ thị là gì và nghiên cứu những gì?

Khác với hình học cổ điển vốn quan tâm đến độ dài, góc nhọn và tọa độ trong không gian liên tục, **lý thuyết đồ thị (graph theory)** nghiên cứu **tính kết nối thuần túy** giữa các đối tượng rời rạc. Một sơ đồ tàu điện ngầm đẹp không cần vẽ đúng tỉ lệ địa lý; điều hành khách cần biết chỉ là *ga nào nối với ga nào* và *đổi tuyến ở đâu*.

Ở bậc đại học và trong công nghệ, lý thuyết đồ thị phát triển theo bốn hướng lớn bổ trợ nhau:

1. **Đồ thị thuật toán & Tối ưu tổ hợp:** tìm đường đi ngắn nhất (Dijkstra, A\*), cây khung rẻ nhất (MST), luồng vận chuyển cực đại (Max-Flow), ghép cặp tối ưu.
2. **Lý thuyết đồ thị phổ (Spectral Graph Theory):** viết đồ thị thành ma trận (ma trận kề $$A$$, ma trận Laplace $$L$$) rồi dùng giá trị riêng và vectơ riêng để xếp hạng nút (PageRank), chia cụm cộng đồng và thiết kế mạng bền vững (expander).
3. **Đồ thị ngẫu nhiên & Khoa học mạng:** dùng xác suất để giải thích vì sao mạng xã hội hay Internet có quy luật "sáu bước phân cách" (thế giới nhỏ) và xuất hiện những nút siêu kết nối (hub).
4. **Học sâu trên đồ thị (GNN):** truyền thông điệp giữa các nút lân cận để dự đoán tính chất của phân tử thuốc, phát hiện gian lận tài chính hay gợi ý bạn bè.

Nói ngắn gọn: **bất cứ khi nào mối quan hệ giữa các đối tượng quan trọng hơn bản thân từng đối tượng đứng riêng lẻ, lý thuyết đồ thị là ngôn ngữ tự nhiên nhất.**

---

## 1. Đồ thị: ngôn ngữ của sự kết nối

Một đồ thị $$G=(V,E)$$ gồm tập đỉnh $$V$$ và tập cạnh $$E$$ (mỗi cạnh là một cặp đỉnh vô hướng, hoặc một mũi tên có hướng). Cạnh thường gắn thêm **trọng số** biểu diễn khoảng cách, thời gian đi lại, dung lượng đường truyền hay chi phí.

| Hệ thống | Đỉnh | Cạnh |
|----|------|------|
| Bản đồ đường | Giao lộ | Đoạn đường |
| Web | Trang | Siêu liên kết (có hướng) |
| Mạng xã hội | Người, tài khoản | Theo dõi, kết bạn |
| Mạch điện | Linh kiện, nút mạch | Dây dẫn |
| Học máy | Tensor, phép toán | Phụ thuộc dữ liệu |

**Ý chính.** *Khi câu hỏi "cái gì nối với cái gì" quan trọng hơn câu hỏi "nằm ở đâu trong không gian", ngôn ngữ đồ thị là hệ tọa độ phù hợp.*

Biểu diễn đồ thị bằng **ma trận kề** $$A$$ ($$A_{ij}=1$$ nếu có cạnh nối $$i$$ tới $$j$$) mở ra một phép màu đại số: phần tử $$(i,j)$$ của lũy thừa $$A^k$$ đếm *chính xác* số đường đi có độ dài $$k$$ bước từ $$i$$ tới $$j$$!

---

## 2. Đường đi, khoảng cách và tính liên thông

**Khoảng cách** $$d(u,v)$$ là tổng trọng số nhỏ nhất của đường đi từ $$u$$ đến $$v$$. **Tính liên thông** hỏi mọi cặp đỉnh có thể đi tới nhau hay không. Những cạnh hay đỉnh mà chỉ cần cắt bỏ là đồ thị bị đứt đôi gọi là **cầu (bridge)** và **đỉnh khớp (articulation point)** — trong kỹ thuật viễn thông và điện lực, đây chính là các điểm lỗi đơn (single points of failure) bắt buộc phải có phương án dự phòng.

**Vì sao không thể chỉ đếm số bước?** Hãy tưởng tượng bạn đi từ nhà tới sân bay: tuyến đường thẳng xuyên trung tâm chỉ qua 1 giao lộ nhưng kẹt xe mất 45 phút; tuyến đường vành đai qua 3 giao lộ nhưng chạy thông thoáng chỉ mất 20 phút. Nếu không có trọng số, tìm kiếm theo chiều rộng (**BFS**) chọn tuyến 1 bước. Khi gắn trọng số thời gian, **thuật toán Dijkstra** (lõi của Google Maps và giao thức định tuyến OSPF trên Internet) và **A\*** (kết hợp thêm ước lượng khoảng cách chim bay để tìm nhanh hơn nhiều lần) luôn chọn tuyến 20 phút. Với mạng có trọng số âm (như chênh lệch tỉ giá tiền tệ để tìm cơ hội kinh doanh chênh lệch giá), ta dùng **Bellman–Ford**.

**Ý chính.** *Định tuyến là tìm kiếm tối ưu trên đồ thị; "đường tốt nhất" là một bài toán tối ưu tổ hợp được đặt đúng, không phải chuyện nhìn bản đồ cho đẹp.*

---

## 3. Cây, cây khung và chu trình

**Cây** là đồ thị liên thông, không chứa chu trình nào; nó là cấu trúc kết nối tiết kiệm tối đa với đúng $$\lvert E\rvert = \lvert V\rvert - 1$$ cạnh (bỏ bớt 1 cạnh là đứt mạng, thêm 1 cạnh là sinh chu trình).

**Cây khung nhỏ nhất (MST — thuật toán Kruskal, Prim).** Giả sử một công ty viễn thông cần kéo cáp quang nối 4 trung tâm dữ liệu với chi phí lắp đặt giữa từng cặp đã biết. Ta chỉ cần đúng 3 tuyến cáp tạo thành một cây nối cả 4 trung tâm sao cho tổng chi phí nhỏ nhất. Điều kỳ diệu là chiến lược tham lam cực đơn giản của Kruskal — *cứ chọn dần tuyến cáp rẻ nhất chưa tạo thành vòng khép kín* — lại được chứng minh luôn cho nghiệm tối ưu toàn cục!

Ngược lại, **chu trình** tạo ra đường dự phòng giúp mạng chịu lỗi (nếu 1 tuyến cáp biển đứt, gói tin đi vòng theo chiều còn lại), nhưng cũng làm bài toán phức tạp hơn hẳn: tìm chu trình đi qua mỗi đỉnh đúng một lần (**chu trình Hamilton**, nền tảng của bài toán người giao hàng TSP) là NP-đầy đủ — xem [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

---

## 4. Luồng và lát cắt

Gán cho mỗi cạnh một **dung lượng** $$c(e)\ge 0$$ (ví dụ số xe tối đa mỗi giờ trên một đoạn đường, hay băng thông tối đa của tuyến cáp). Một **luồng** đi từ nguồn $$s$$ đến đích $$t$$ không được vượt dung lượng từng cạnh và phải bảo toàn (vào bằng ra) tại mọi nút trung gian.

**Định lý luồng cực đại – lát cắt cực tiểu (Ford–Fulkerson):**

$$
\max\mathrm{flow}(s,t)=\min\mathrm{cut}(s,t).
$$

**Ví dụ số trực quan.** Giả sử bạn chuyển hàng từ kho $$s$$ đến cảng $$t$$ qua hai trạm trung chuyển $$A, B$$: đường $$s\to A$$ chở tối đa 10 tấn/ngày, $$s\to B$$ chở tối đa 10 tấn/ngày, nhưng từ $$A\to t$$ cầu yếu chỉ chịu 3 tấn/ngày và $$B\to t$$ chịu 2 tấn/ngày. Dù hai đường đầu rất rộng, lát cắt tách $$\{s,A,B\}$$ khỏi $$\{t\}$$ có tổng dung lượng chỉ là $$3+2=5$$ tấn/ngày. Vì vậy không tài nào chuyển quá 5 tấn/ngày — và lát cắt cực tiểu chính là **chứng nhận toán học** chỉ đích danh nút thắt cổ chai cần nâng cấp!

Định lý này không chỉ dành cho đường ống: bài toán **ghép cặp tối ưu** trên đồ thị hai phía (ghép tài xế với hành khách, ghép sinh viên với ký túc xá) và **phân tách nền/vật thể trong ảnh (graph cut)** đều quy gọn về tìm luồng cực đại. Nó mang đúng tinh thần đối ngẫu trong bài [tối ưu hóa]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).

---

## 5. Bước ngẫu nhiên và PageRank

Trước khi Google ra đời năm 1998, các công cụ tìm kiếm xếp hạng trang web chủ yếu bằng cách đếm số lần từ khóa xuất hiện — và lập tức bị đánh lừa bởi những trang nhồi nhét hàng nghìn từ khóa ẩn. Larry Page và Sergey Brin đã đặt ra một góc nhìn đồ thị đột phá: **một siêu liên kết từ trang A sang trang B là một phiếu bầu tín nhiệm** — và phiếu bầu từ một trang uy tín phải nặng ký hơn phiếu bầu từ một trang vô danh.

Họ mô hình hóa một "người lướt web ngẫu nhiên": với xác suất $$\alpha$$ (thường chọn $$\alpha = 0{,}85$$), người đó bấm ngẫu nhiên vào một liên kết trên trang hiện tại; với xác suất $$1-\alpha = 0{,}15$$, người đó chán và nhảy thẳng (teleport) sang một trang bất kỳ trên web (nhờ bước nhảy 15% này, người lướt web không bao giờ bị mắc kẹt ở trang cụt không có link ra ngoài).

Tỉ lệ thời gian dài hạn người đó có mặt tại mỗi trang chính là phân phối dừng $$\pi$$ của chuỗi Markov — tức là nghiệm của phương trình vectơ riêng:

$$
\pi=\alpha P^\top\pi+(1-\alpha)v,
$$

trong đó $$P$$ là ma trận chuyển xác suất và $$v$$ là vectơ teleport.

**Ý chính.** *Mức độ quan trọng toàn cục nảy sinh tự nhiên từ cấu trúc liên kết cục bộ, thông qua vectơ riêng trội của một ma trận thưa khổng lồ, chứ không cần con người chấm điểm bằng tay.*

**Phương pháp lặp lũy thừa.** Với đồ thị web hàng chục tỷ trang, ta không thể đảo ma trận trực tiếp. Thay vào đó, ta chỉ cần bắt đầu từ phân phối đều và lặp lại phép nhân ma trận thưa với vectơ khoảng 50–100 vòng là $$\pi$$ đã hội tụ đủ chính xác. Khả năng mở rộng (scalability) của phép lặp vectơ riêng chính là yếu tố biến ý tưởng đại số tuyến tính này thành công cụ tìm kiếm thống trị thế giới. Các biến thể như **PageRank cá nhân hóa** (teleport ưu tiên về tập nút bạn thích) ngày nay vẫn được dùng rộng rãi trong gợi ý bạn bè và sản phẩm.

---

## 6. Phổ của đồ thị: ma trận Laplace và lát cắt

Ma trận Laplace tổ hợp $$L=D-A$$ (ma trận đường chéo chứa bậc của các đỉnh trừ đi ma trận kề) của đồ thị vô hướng luôn đối xứng, nửa xác định dương và thỏa mãn $$L\mathbf{1}=0$$.

**Ví dụ 3 đỉnh nối thẳng ($$1 - 2 - 3$$):** bậc của ba đỉnh là $$(1,2,1)$$, nên

$$
L = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}.
$$

Với bất kỳ hàm gán giá trị $$x = (x_1, x_2, x_3)$$ lên các đỉnh, dạng toàn phương của $$L$$ có công thức cực kỳ đẹp mắt:

$$
x^\top Lx=\sum_{ij\in E}(x_i-x_j)^2.
$$

Công thức này đo **độ gồ ghề** của tín hiệu $$x$$ trên đồ thị: nếu hai đỉnh nối nhau có giá trị gần nhau thì $$x^\top Lx$$ nhỏ. Giá trị riêng nhỏ thứ hai $$\lambda_2$$ (gọi là **độ liên thông đại số** hay giá trị Fiedler) bằng 0 khi và chỉ khi đồ thị bị đứt thành ít nhất 2 mảnh rời nhau; còn dấu âm/dương của vectơ riêng ứng với $$\lambda_2$$ tự động gợi ý đường cắt tối ưu chia mạng lưới thành hai cộng đồng ít liên kết nhất! Đây là nền tảng của **phân cụm phổ (spectral clustering)** và biến đổi Fourier trên đồ thị.

---

## 7. Đồ thị giãn nở: thưa mà liên thông rất tốt

Hãy đặt một câu hỏi thiết kế hạ tầng tưởng như mâu thuẫn: *làm sao xây một mạng máy chủ ít dây nối (để rẻ tiền, mỗi nút chỉ nối với 4 hay 6 nút khác) nhưng lại cực kỳ khó bị cô lập — muốn cắt tách một nhóm nút ra khỏi phần còn lại phải cắt rất nhiều dây?*

Câu trả lời là **đồ thị giãn nở (expander graph)**: một họ đồ thị thưa nhưng mọi tập con đỉnh (không quá nửa đồ thị) đều có rất nhiều cạnh vươn ra bên ngoài. Về mặt đại số, điều này tương đương với việc **khoảng cách phổ (spectral gap)** bị chặn dưới cách xa 0, khiến bước ngẫu nhiên trên đồ thị trộn đều chỉ sau $$O(\log n)$$ bước!

**Vì sao ngành công nghệ quan tâm.**

- **Mạng truyền thông & trung tâm dữ liệu bền vững:** ít cáp nối nhưng không có nút thắt cổ chai.  
- **Lý thuyết mã sửa sai & giảm ngẫu nhiên (derandomization):** giúp tiết kiệm bit ngẫu nhiên trong thuật toán và xây dựng mã sửa sai tốc độ cao.  
- **Thuật toán MCMC:** đảm bảo quá trình lấy mẫu hội tụ nhanh.

Tóm gọn: **độ giãn nở là thước đo định lượng của một mạng lưới "không có nút thắt cổ chai".**

---

## 8. Quy mô, thế giới nhỏ và khoa học mạng

Các mạng lưới tự nhiên ngoài đời (Internet, mạng xã hội, mạng tương tác protein, mạng sân bay) hiếm khi trông như lưới ô vuông đều đặn. Chúng thường đồng thời mang ba đặc trưng:

- **Phân phối bậc có đuôi nặng:** phần lớn nút có rất ít kết nối, nhưng tồn tại vài "siêu nút" (hub) có hàng triệu kết nối (như sân bay quốc tế lớn hay người nổi tiếng) — khiến mạng rất bền trước lỗi ngẫu nhiên nhưng lại cực kỳ dễ sập nếu tấn công có chủ đích vào các hub.  
- **Hiệu ứng thế giới nhỏ:** dù mạng có hàng tỷ nút và cụm bạn bè rất chặt, đường đi trung bình giữa hai người bất kỳ trên Trái Đất chỉ khoảng 5–6 bước.  
- **Cấu trúc cộng đồng:** kết nối dày đặc trong nhóm, thưa thớt giữa các nhóm.

Để mô hình hóa những hiện tượng này (như ngưỡng bùng phát dịch bệnh hay lan truyền tin giả), lý thuyết đồ thị kết hợp với [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) tạo ra các mô hình đồ thị ngẫu nhiên (Erdős–Rényi, gắn kết ưu tiên Barabási–Albert, mô hình khối ngẫu nhiên). Và ở giao điểm với AI, **Mạng nơ-ron đồ thị (GNN)** học biểu diễn của từng nút bằng cách tổng hợp đặc trưng từ các nút hàng xóm dọc theo cạnh — nối trực tiếp sang [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/) và [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/).

---

## 9. Nói thật về độ phức tạp

Trên cùng một đồ thị, ranh giới giữa "dễ" và "cực khó" đôi khi chỉ cách nhau một từ khóa: tìm **đường đi ngắn nhất** giải trong vài mili-giây (đa thức), nhưng tìm **đường đi dài nhất** (không lặp đỉnh) lại là bài toán NP-khó! Tương tự, tìm chu trình đi qua mọi *cạnh* (chu trình Euler) thì dễ, còn đi qua mọi *đỉnh* (chu trình Hamilton) lại là NP-đầy đủ.

Trong thực tế, kỹ sư vượt qua rào cản độ phức tạp bằng bốn vũ khí:

1. Nhận diện cấu trúc đặc biệt (đồ thị phẳng, cây, đồ thị hai phía),  
2. Dùng thuật toán xấp xỉ có bảo đảm sai số,  
3. Khai thác độ thưa của mạng thực tế,  
4. Dùng heuristic kết hợp kiểm chứng chặt chẽ.

Lý thuyết đồ thị vừa trao cho ta những thuật toán chạy trên hàng tỷ đỉnh, vừa vẽ rõ tấm bản đồ ranh giới để ta không lãng phí công sức đi tìm thuật toán đa thức cho một bài toán NP-khó.

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
