---
layout: post
title: "Lượng tử hóa, đường cong và nút của Kontsevich (Huy chương Fields 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Vào đầu thập niên 1990, vật lý lý thuyết liên tục ném sang giới toán học những "lời tiên tri" gây choáng váng: từ hấp dẫn lượng tử hai chiều, Edward Witten dự đoán các số giao hình học trên không gian moduli đường cong phải tuân theo phương trình sóng nước nông KdV; từ lý thuyết trường lượng tử Chern–Simons, các nhà vật lý gợi ý những tích phân đường tưởng chừng vô nghĩa lại mã hóa toàn bộ bất biến của các nút thắt trong không gian ba chiều; và từ cơ học lượng tử, một câu hỏi mở suốt hàng chục năm vẫn treo lơ lửng: liệu *mọi* không gian pha Poisson cổ điển đều có thể "lượng tử hóa biến dạng" được hay không?

**Maxim Kontsevich** bước vào đúng ngã ba giông bão ấy với một thứ vũ khí vừa quen thuộc vừa sắc lẹm: **đồ thị và tích phân trên không gian cấu hình**. Ông biến từng lời tiên tri rời rạc đó thành định lý toán học chặt chẽ, và nhận **Huy chương Fields 1998**:

> “For his contributions to algebraic geometry, topology, and mathematical physics, including the proof of Witten's conjecture of intersection numbers in moduli spaces of stable curves, construction of the universal Vassiliev invariant of knots, and formal quantization of Poisson manifolds.”
> — Citation IMU, ICM 1998 (như được ghi trong hồ sơ [Fields Medal](https://www.mathunion.org/imu-awards/fields-medal) và các nguồn tiểu sử chuẩn)

*Tạm dịch: vì những đóng góp cho hình học đại số, tôpô và vật lý toán, trong đó có chứng minh giả thuyết Witten về số giao trên không gian moduli các đường cong ổn định, xây dựng bất biến Vassiliev phổ dụng của nút, và lượng tử hóa hình thức các đa tạp Poisson.*

Vì Kontsevich (sinh năm 1964, giáo sư thường trực tại IHÉS) sau này còn nổi tiếng với hàng loạt chương trình đồ sộ khác như **đối xứng gương đồng điều** (*homological mirror symmetry*), tích phân motivic hay hiện tượng vượt tường (*wall-crossing*), người đọc ngày nay rất dễ nhầm lẫn. Bài học này bám sát đúng ba cột mốc lịch sử của lời trao giải năm 1998 — **giả thuyết Witten** trên $$\overline{\mathcal{M}}_{g,n}$$, **bất biến Vassiliev phổ dụng** (tích phân Kontsevich), và **lượng tử hóa biến dạng** các đa tạp Poisson — đồng thời đặt đối xứng gương đồng điều đúng vị trí của nó: một chương trình lớn từ ICM 1994, không phải kết quả thứ ba của Huy chương Fields 1998.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhớ lời trao giải năm 1998 gồm **ba** kết quả cụ thể, và không thay kết quả thứ ba bằng đối xứng gương đồng điều.
- Phát biểu ý chính của giả thuyết Witten: hàm sinh các số giao của lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ là một hàm tau của hệ KdV, và giải thích cách Kontsevich chứng minh bằng đồ thị ruy-băng và mô hình ma trận Airy.
- Mô tả tích phân Kontsevich như **bất biến kiểu hữu hạn (Vassiliev) phổ dụng**, đồng thời ghi công Vassiliev và Bar-Natan cho phần khung tổ hợp.
- Giải thích trực quan **lượng tử hóa biến dạng**: một tích sao không giao hoán làm biến dạng tích thông thường của hàm sao cho bậc nhất của giao hoán tử khôi phục móc Poisson, và cách định lý hình thức (formality) của Kontsevich dựng tích sao trên mọi đa tạp Poisson.
- Phân biệt đối xứng gương đồng điều (một chương trình lớn đề xuất từ năm 1994, nhiều trường hợp đã có định lý nhưng chưa khép lại toàn bộ) với ba kết quả chính thức của giải Fields 1998.
- Đặt các công trình này lên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) mà không đánh đồng trực giác vật lý với chứng minh toán học.

**Kiến thức nền.** Khái niệm không gian moduli của đường cong; móc Poisson trên $$\mathbb{R}^{2n}$$ hoặc trên đa tạp symplectic; đa thức Jones như một ví dụ về bất biến nút ngoài nhóm cơ bản. Biết giải tích phức và một giáo trình nhập môn hình học đại số sẽ có ích. Lý thuyết trường lượng tử thì không bắt buộc.

**Liên kết với các bài khác.** Bài [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) trình bày chương trình HMS, nên đọc *sau* và tách biệt với giải năm 1998. Bài [Pardon / symplectic]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) nói về phía phạm trù Fukaya, nơi HMS được sử dụng.

---

## Bản đồ kiến thức nền: Lượng tử hóa biến dạng, không gian moduli và nút thắt là gì?

Ba kết quả của Kontsevich thuộc ba nhánh toán học có tên gọi rất khác nhau, nhưng trực giác phía sau mỗi nhánh đều rất sáng rõ.

**1. Cơ học cổ điển vs. cơ học lượng tử và "lượng tử hóa biến dạng".**
Trong cơ học cổ điển, trạng thái của một hạt chuyển động được mô tả bằng điểm $$(q, p)$$ trong **không gian pha** (vị trí $$q$$ và động lượng $$p$$). Các đại lượng quan sát được (như năng lượng, động lượng góc) là các hàm trơn $$f(q,p), g(q,p)$$ nhân với nhau theo phép nhân thông thường có tính giao hoán: $$f \cdot g = g \cdot f$$. Để mô tả chuyển động theo thời gian, cơ học Hamilton trang bị thêm cho không gian pha một phép toán phản đối xứng gọi là **móc Poisson** $$\{f, g\}$$ — ở trường hợp chuẩn trên $$\mathbb{R}^2$$ là $$\{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}$$, đặc biệt $$\{q, p\} = 1$$. Một không gian có móc Poisson thỏa đồng nhất thức Jacobi và quy tắc Leibniz gọi là **đa tạp Poisson**.

Khi sang **cơ học lượng tử**, vị trí $$\hat{q}$$ và động lượng $$\hat{p}$$ không còn giao hoán nữa: $$\hat{q}\hat{p} - \hat{p}\hat{q} = i\hbar$$ (với $$\hbar$$ là hằng số Planck rút gọn). **Lượng tử hóa biến dạng** đặt một câu hỏi hoàn toàn đại số: thay vì xây không gian Hilbert, liệu ta có thể thay phép nhân giao hoán $$fg$$ trên tập các hàm trơn bằng một phép nhân mới gọi là **tích sao** $$f \star g$$ phụ thuộc theo tham số $$\hbar$$, sao cho khi $$\hbar \to 0$$ nó quay về tích cổ điển $$fg$$, còn sai khác bậc nhất của nó đúng bằng móc Poisson?

**2. Không gian moduli $$\overline{\mathcal{M}}_{g,n}$$ — "bản đồ của mọi mặt có $$g$$ lỗ".**
Một đường cong đại số phức trơn giống $$g$$ thực chất là một **mặt Riemann** (một mặt cầu có $$g$$ quai, như hình xuyến khi $$g=1$$ hay bánh vòng hai lỗ khi $$g=2$$). Tập tất cả các cấu trúc phức không đẳng cấu trên mặt có $$g$$ lỗ cùng $$n$$ điểm đánh dấu tạo thành **không gian moduli** $$\mathcal{M}_{g,n}$$. Để có thể tích phân và đếm số giao trên không gian này mà không bị "rơi ra mép", Deligne và Mumford bổ sung thêm các mặt suy biến (bị bóp thắt thành điểm nút) để thu được không gian compact $$\overline{\mathcal{M}}_{g,n}$$.

**3. Nút thắt và bất biến kiểu hữu hạn (Vassiliev).**
Một **nút** (*knot*) là một vòng dây khép kín nhúng trong không gian $$\mathbb{R}^3$$ không tự cắt. Bài toán kinh điển của tôpô là nhận diện hai nút có biến dạng liên tục về nhau được không, thông qua các **bất biến nút** (như đa thức Alexander hay đa thức Jones). **Vassiliev** tổ chức vô số bất biến nút thành một hệ phân cấp giống như "đạo hàm bậc cao": mỗi lần cho hai sợi dây xuyên qua nhau (đổi chỗ bắt chéo), ta lấy hiệu giá trị của bất biến; bất biến nào triệt tiêu sau $$m+1$$ lần đổi chỗ như vậy gọi là **bất biến kiểu hữu hạn bậc $$\le m$$**.

---

## 1. Từ bài toán cổ điển đến ý tưởng đột phá: vì sao nên bám theo danh sách năm 1998

Ảnh hưởng của một nhà toán học tầm cỡ thường lan xa hơn nhiều so với lời trao giải ban đầu. Sau năm 1998, tên tuổi Kontsevich gắn chặt với đối xứng gương đồng điều, tích phân motivic (phác thảo trong bài giảng Orsay 1995, sau đó Denef–Loeser phát triển hoàn chỉnh), và lý thuyết ánh xạ ổn định (Gromov–Witten). Nếu gộp tất cả vào "Fields 1998" sẽ làm sai lệch lịch sử.

Thực ra, chỉ riêng ba kết quả chính thức năm 1998 đã đủ tạo nên một kỳ tích thống nhất: chúng không phải ba sở thích rời rạc ở hình học đại số, tôpô và vật lý toán, mà là **ba biểu hiện của cùng một trực giác đột phá** — dùng **tổng có trọng số trên các đồ thị**, trong đó trọng số là những tích phân trên không gian cấu hình, để biến các cấu trúc hình học–tôpô phức tạp thành những phép tính đại số và giải tích rõ ràng.

---

## 2. Giả thuyết Witten: số giao trên $$\overline{\mathcal{M}}_{g,n}$$

Trên không gian moduli compact hóa $$\overline{\mathcal{M}}_{g,n}$$, tại mỗi điểm đánh dấu thứ $$i$$ ta gắn không gian đường đối tiếp xúc của đường cong tại điểm đó, tạo nên phân thớ đường $$\mathbb{L}_i$$. Lớp Chern thứ nhất của nó ký hiệu là $$\psi_i = c_1(\mathbb{L}_i)$$. Lấy tích phân tích của các lớp $$\psi_i$$ trên toàn không gian moduli, ta thu được các **số giao tautological**:

$$
\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g=\int_{\overline{\mathcal{M}}_{g,n}}\psi_1^{d_1}\cdots\psi_n^{d_n}
$$

(quy ước số giao bằng $$0$$ trừ khi tổng các bậc $$d_1 + \cdots + d_n$$ bằng đúng số chiều phức $$3g-3+n$$ của $$\overline{\mathcal{M}}_{g,n}$$). Ví dụ cơ bản nhất là ở giống $$g=0$$ với $$n=3$$ điểm đánh dấu: $$\overline{\mathcal{M}}_{0,3}$$ chỉ là một điểm duy nhất, nên $$\langle\tau_0^3\rangle_0 = 1$$; còn ở giống $$g=1, n=1$$, ta có con số nổi tiếng $$\langle\tau_1\rangle_1 = 1/24$$.

**Giả thuyết Witten (1990–1991).** Xuất phát từ hai cách tính độc lập cùng một lý thuyết vật lý (hấp dẫn lượng tử 2D: một cách dùng tích phân trên mặt Riemann, cách kia dùng giới hạn của các mô hình ma trận ngẫu nhiên), **Edward Witten** dự đoán rằng hàm sinh của toàn bộ vô hạn các số giao $$\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g$$ phải là một **hàm tau** của hệ phương trình sóng phi tuyến **Korteweg–de Vries (KdV)**! Nói cách khác, các số giao hình học tưởng chừng rời rạc này bị khóa chặt bởi một hệ phương trình vi phân đệ quy (tương đương các ràng buộc đại số Virasoro) đến mức chỉ từ giá trị ban đầu $$\langle\tau_0^3\rangle_0 = 1$$, ta có thể tính ra *tất cả* các số giao khác ở mọi giống $$g$$!

**Chứng minh đột phá của Kontsevich (1992).** Trong bài báo kinh điển *Intersection theory on the moduli space of curves and the matrix Airy function* (*Comm. Math. Phys.* 147), Kontsevich đã bắc một cây cầu táo bạo từ hình học liên tục sang tổ hợp đồ thị:
1. Nhờ định lý về **vi phân Strebel**, mỗi mặt Riemann có điểm đánh dấu và các tham số chu vi $$p_1, \ldots, p_n$$ được phân mảnh duy nhất thành một **đồ thị ruy-băng** (*ribbon graph* — đồ thị có thứ tự vòng quanh mỗi đỉnh, dày lên thành dải băng ghép lại đúng thành mặt Riemann đó).
2. Nhờ phép chia ô bằng đồ thị ruy-băng, tích phân hình học của các lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ biến đổi trực tiếp thành một **tổng trên tất cả các đồ thị ruy-băng bậc 3**, mà theo quy tắc Feynman, tổng này chính là khai triển tiệm cận của một **tích phân ma trận Airy** trên không gian ma trận Hermite $$N \times N$$!
3. Tích phân ma trận Airy lại là một đối tượng cổ điển của lý thuyết hệ khả tích, vốn đã thỏa mãn hệ KdV.

**Tóm tắt.** Witten tiên đoán các số giao trên không gian moduli đường cong bị chi phối bởi hệ phương trình KdV. Kontsevich dựng bộ từ điển **mặt Riemann $$\leftrightarrow$$ đồ thị ruy-băng $$\leftrightarrow$$ tích phân ma trận Airy**, biến lời tiên đoán vật lý thành một định lý hình học đại số chặt chẽ.

---

## 3. Bất biến Vassiliev phổ dụng và không gian cấu hình

Đầu thập niên 1990, **Victor Vassiliev** giới thiệu hệ thống **bất biến kiểu hữu hạn** của nút, còn **Dror Bar-Natan** chuyển hóa nó thành một ngôn ngữ tổ hợp tuyệt đẹp gồm **sơ đồ dây** (*chord diagrams* — những vòng tròn có các dây cung nối cặp điểm) và **hệ trọng số** (*weight systems*) gắn liền với các đại số Lie (như $$\mathfrak{sl}_2$$ sinh ra các hệ số khai triển của đa thức Jones). Câu hỏi định lý cơ bản của lý thuyết Vassiliev đặt ra là: liệu mọi hệ trọng số đại số có thực sự tích phân ngược lại được thành một bất biến nút tôpô hay không?

Chính tại đây **tích phân Kontsevich** (1993) xuất hiện như một công cụ giải tích **phổ dụng**. Hãy hình dung nút thắt $$K$$ nằm trong $$\mathbb{C} \times \mathbb{R}$$ (mặt phẳng phức ngang $$z$$ và trục cao độ thực $$t$$). Khi cắt ngang nút tại $$m$$ cao độ $$t_1 < t_2 < \cdots < t_m$$, mỗi cặp nhánh cắt tại cùng độ cao $$t_j$$ cho một dạng vi phân logarit $$\frac{dz_j - dz'_j}{z_j - z'_j}$$. Lấy tích phân lặp của các dạng vi phân này trên không gian cấu hình các điểm dọc theo nút (và tổng hóa theo các sơ đồ dây ghép cặp nhánh), Kontsevich thu được một đại lượng bất biến nút nhận giá trị thẳng trong đại số các sơ đồ dây!

Ví dụ đơn giản nhất (bậc $$m = 1$$) chính là công thức tích phân **số móc nối (linking number)** cổ điển của Gauss cho hai vòng dây trong $$\mathbb{R}^3$$; tích phân Kontsevich là sự tổng quát hóa bậc cao vô hạn của tích phân Gauss đó, hiện thực hóa chặt chẽ chuỗi nhiễu loạn Feynman của lý thuyết Chern–Simons mà Witten từng gợi ý. Vì **mọi** bất biến kiểu hữu hạn (kể cả mọi hệ số của đa thức Jones, HOMFLY-PT, Kauffman) đều thu được bằng cách ghép một hệ trọng số vào tích phân Kontsevich, nó xứng đáng với tên gọi **bất biến Vassiliev phổ dụng**.

**Ghi công.** Vassiliev phát hiện hệ phân cấp kiểu hữu hạn; Bar-Natan hệ thống hóa tổ hợp sơ đồ dây; Witten gợi ý nguồn gốc từ lý thuyết trường lượng tử Chern–Simons; còn Kontsevich xây dựng đối tượng giải tích phổ dụng biến mọi hệ trọng số thành bất biến nút thực sự.

---

## 4. Lượng tử hóa hình thức các đa tạp Poisson

Một **đa tạp Poisson** $$(M,\pi)$$ được trang bị một song vector (bivector) $$\pi$$ sao cho $$\{f,g\}=\langle\pi,df\wedge dg\rangle$$ là một móc Lie trên $$C^\infty(M)$$ thỏa quy tắc Leibniz. Đa tạp symplectic là trường hợp $$\pi$$ không suy biến ở mọi điểm (như không gian pha cổ điển $$\mathbb{R}^{2n}$$), còn cấu trúc Lie–Poisson trên không gian đối ngẫu $$\mathfrak{g}^*$$ của một đại số Lie là ví dụ kinh điển có điểm suy biến (tại gốc $$0$$, $$\pi = 0$$!).

Bài toán **lượng tử hóa biến dạng** (Bayen–Flato–Fronsdal–Lichnerowicz–Sternheimer, 1978) hỏi: với mọi đa tạp Poisson $$(M,\pi)$$, có tồn tại hay không một **tích sao** (*star product*) hình thức trên $$C^\infty(M)[\![\hbar]\!]$$,

$$
f\star g=fg+\hbar B_1(f,g)+\hbar^2 B_2(f,g)+\cdots,
$$

có tính **kết hợp** $$(f \star g) \star h = f \star (g \star h)$$, khôi phục tích thông thường khi $$\hbar=0$$, và thỏa

$$
f\star g-g\star f=i\hbar\{f,g\}+O(\hbar^2)?
$$

**Từ trường hợp cổ điển đến nút thắt Poisson:** Trên $$\mathbb{R}^{2n}$$ với móc Poisson hằng, ta đã biết **tích Moyal** từ giữa thế kỷ XX. Trên đa tạp **symplectic** tổng quát, vì mọi điểm đều có tọa độ địa phương Darboux đưa $$\pi$$ về dạng hằng, De Wilde–Lecomte (1983) và Fedosov (1994) đã ghép được các tích Moyal địa phương thành tích sao toàn cục. Nhưng trên đa tạp **Poisson tổng quát**, hạng của $$\pi$$ có thể nhảy bậc từ điểm này sang điểm khác — không hề có tọa độ Darboux! Bài toán tồn tại tích sao cho đa tạp Poisson tổng quát đứng vững suốt 20 năm.

**Ý tưởng đột phá: Định lý hình thức (Formality Theorem) của Kontsevich (1997).** Thay vì cố ghép các mảnh địa phương bằng tay, Kontsevich nhúng câu hỏi vào một bức tranh đại số đồng điều cao hơn: ông chứng minh rằng đại số Lie vi phân phân bậc (DGLA) của các đối xích Hochschild trên $$C^\infty(M)$$ (nơi sống các tích sao) là **hình thức** (*formal*), tức tựa đẳng cấu $$L_\infty$$ với đối đồng điều của chính nó là đại số Lie các trường đa vector với móc Schouten–Nijenhuis (nơi sống các cấu trúc Poisson $$\pi$$ thỏa $$[\pi, \pi] = 0$$). Hệ quả lập tức: mọi cấu trúc Poisson đều nâng được thành một tích sao kết hợp, và lớp tương đương của tích sao tương ứng 1–1 với lớp tương đương của các cấu trúc Poisson hình thức!

Hơn thế nữa, trên $$\mathbb{R}^d$$, Kontsevich viết ra một **công thức đồ thị tường minh** đẹp đến ngỡ ngàng: mỗi số hạng $$\hbar^n B_n(f,g)$$ là tổng trên các đồ thị có hướng "chấp nhận được" (*admissible graphs*) gồm $$n$$ đỉnh nội (đặt song vector $$\pi$$) và $$2$$ đỉnh biên (đặt hàm $$f$$ và $$g$$); trọng số $$w_\Gamma$$ của mỗi đồ thị là một tích phân hoàn toàn tường minh trên không gian cấu hình các điểm trong **nửa mặt phẳng trên Poincaré** $$\mathbb{H}$$ (cũng chính là khai triển nhiễu loạn của mô hình sigma Poisson hai chiều trong vật lý!).

Bài báo xuất hiện dưới dạng bản thảo năm 1997 (arXiv:q-alg/9709040) và công bố trên *Letters in Mathematical Physics* 66 (2003). Lưu ý chữ **"hình thức"**: kết quả làm việc trên vành chuỗi lũy thừa hình thức $$\mathbb{R}[\![\hbar]\!]$$, không khẳng định chuỗi hội tụ theo giá trị số thực của $$\hbar$$, và không đồng nghĩa với việc lượng tử hóa trên không gian Hilbert cho mọi đa tạp Poisson.

---

## 5. Các chương trình liên quan nhưng không phải kết quả thứ ba

**Đối xứng gương đồng điều (HMS).** Trong báo cáo chấn động tại ICM 1994 (Zürich; arXiv:alg-geom/9411018), Kontsevich đề xuất rằng hiện tượng đối xứng gương từ lý thuyết dây thực chất là một tương đương giữa hai phạm trù: phạm trù dẫn xuất các bó kết hợp trên đa tạp Calabi–Yau $$X$$ (hình học đại số, mô hình B) tương đương với phạm trù Fukaya của đa tạp gương $$Y$$ (hình học symplectic, mô hình A). Đề xuất này đã định hình cả một kỷ nguyên nghiên cứu, với hàng loạt trường hợp lớn đã được chứng minh bởi Seidel, Sheridan, Abouzaid và nhiều tác giả khác. Tuy nhiên, nó **không** phải kết quả thứ ba của lời trao giải năm 1998, và vẫn là một chương trình mở được trình bày riêng trong [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/).

**Tích phân motivic.** Kontsevich phác thảo ý tưởng năm 1995 tại Orsay; **Jan Denef và François Loeser** phát triển thành một lý thuyết hoàn chỉnh. Đây là nhánh công trình ra đời sau, không nằm trong danh sách năm 1998.

**Ánh xạ ổn định.** Cách compact hóa không gian các ánh xạ từ đường cong của Kontsevich đặt nền móng cho lý thuyết Gromov–Witten. Báo cáo của Taubes tại ICM 1998 có bàn đến nó như một đóng góp quan trọng khác, nhưng lời trao giải chính thức không tách nó thành một mục riêng.

---

## 6. Vì sao là Huy chương Fields

Huy chương năm 1998 tôn vinh những bộ **từ điển kỳ diệu** biến trực giác vật lý thành định lý toán học:
- **Đồ thị ruy-băng** $$\leftrightarrow$$ số giao tautological trên $$\overline{\mathcal{M}}_{g,n}$$ (giải giả thuyết Witten);
- **Đồ thị Feynman / sơ đồ dây** $$\leftrightarrow$$ bất biến nút kiểu hữu hạn (tích phân Kontsevich phổ dụng);
- **Đồ thị chấp nhận được trên nửa mặt phẳng trên** $$\leftrightarrow$$ tích sao lượng tử hóa mọi đa tạp Poisson (định lý hình thức).

Trong bức tranh Chương 2, Kontsevich là minh chứng sống động rằng vật lý toán hiện đại không chỉ gợi cảm hứng bằng những ẩn dụ mơ hồ, mà có thể **trực tiếp sản sinh ra cấu trúc đại số và chứng minh chặt chẽ**. Các chương trình sau năm 1998 như HMS hay tích phân motivic tiếp tục khẳng định tầm vóc đó, nhưng bản thân ba cột mốc trong lời trao giải năm 1998 đã là một kiệt tác trọn vẹn.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Kontsevich giải đối xứng gương." | Ông đề xuất HMS năm 1994; đó là một chương trình, với nhiều trường hợp đã được nhiều tác giả chứng minh. |
| "Fields 1998 = đối xứng gương đồng điều." | Kết quả thứ ba chính thức là lượng tử hóa hình thức các đa tạp Poisson. |
| "Giả thuyết Witten phân loại mọi đường cong." | Nó mô tả các số giao của lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ thông qua hệ KdV. |
| "Tích phân Kontsevich là đa thức Jones." | Nó là bất biến kiểu hữu hạn phổ dụng; đa thức Jones là một trong nhiều bất biến rút ra được từ nó. |
| "Lượng tử hóa hình thức là cơ học lượng tử trên không gian Hilbert." | Đó là một biến dạng kết hợp trên $$\mathbb{R}[\![\hbar]\!]$$; sự hội tụ là vấn đề riêng. |
| "Tích phân motivic là kết quả được Fields 1998." | Đó là công trình liên quan, đến sau (bài giảng của Kontsevich; Denef–Loeser). |

---

## Liên kết

- Trang IMU Fields Medal: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia — Maxim Kontsevich: [https://en.wikipedia.org/wiki/Maxim_Kontsevich](https://en.wikipedia.org/wiki/Maxim_Kontsevich)
- Kontsevich, lượng tử hóa biến dạng (arXiv:q-alg/9709040): [https://arxiv.org/abs/q-alg/9709040](https://arxiv.org/abs/q-alg/9709040)
- Kontsevich, đại số đồng điều của đối xứng gương (arXiv:alg-geom/9411018): [https://arxiv.org/abs/alg-geom/9411018](https://arxiv.org/abs/alg-geom/9411018)
- AMS Notices, “The Mathematical Work of the 1998 Fields Medalists”: [https://www.ams.org/notices/199901/fields.pdf](https://www.ams.org/notices/199901/fields.pdf)
- Tìm arXiv — Kontsevich Witten moduli: [https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all](https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 1998 — Maxim Kontsevich (khai mạc ICM Berlin; xem thêm Taubes, “The work of Maxim Kontsevich,” ICM 1998).
2. M. Kontsevich, “Intersection theory on the moduli space of curves and the matrix Airy function,” *Comm. Math. Phys.* 147 (1992).
3. E. Witten, hấp dẫn hai chiều và lý thuyết giao trên không gian moduli (giả thuyết).
4. M. Kontsevich, “Deformation quantization of Poisson manifolds,” *Lett. Math. Phys.* 66 (2003); bản thảo q-alg/9709040.
5. V. Vassiliev, bất biến nút kiểu hữu hạn; D. Bar-Natan, hệ trọng và phức sơ đồ.
6. M. Kontsevich, “Homological algebra of mirror symmetry,” *Proc. ICM Zürich 1994* — chương trình liên quan, không phải gạch thứ ba 1998.
7. J. Denef và F. Loeser, các bài về tích phân motivic (sau bài giảng Orsay của Kontsevich).
8. Khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/).

---

## Hướng đi tiếp

- Đọc một bài giảng hiện đại về các lớp tautological trên $$\overline{\mathcal{M}}_{g,n}$$ để thấy định lý Witten–Kontsevich *không* tính được những gì.
- Nếu học tiếp sang HMS, hãy ghi chép thành hai cột: "đề xuất năm 1994" và "định lý do các tác giả sau chứng minh".

## Video tham khảo

- **Xem trước**: [HLF Laureate Portraits: Maxim Kontsevich](https://www.youtube.com/watch?v=1CXvSRQVoZY) (Heidelberg Laureate Forum, tiếng Anh). Video chân dung ngắn, Kontsevich kể về con đường và cách làm toán của mình. Phù hợp để làm quen trước khi đọc bài.
- [Maxim Kontsevich | On the History of quantum cohomology and homological mirror symmetry](https://www.youtube.com/watch?v=Ml2x5NnEQ1I) (Harvard CMSA, tiếng Anh). Kontsevich kể lại lịch sử đối đồng điều lượng tử và đối xứng gương đồng điều. Nên xem sau khi đọc mục 5, để phân biệt rõ đề xuất HMS năm 1994 với ba kết quả của giải năm 1998.
