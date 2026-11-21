---
layout: post
title: "Vận chuyển tối ưu và tính chính quy của Figalli (Huy chương Fields 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Alessio Figalli** nhận **Huy chương Fields 2018**

> “for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability.”
> — [IMU, Fields Medals 2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)

*Tạm dịch:* Cho các đóng góp vào lý thuyết vận chuyển tối ưu và các ứng dụng của nó trong phương trình đạo hàm riêng, hình học metric và xác suất.

Lời trích dẫn này ghi nhận đóng góp trong một **chương trình nghiên cứu**, không nói rằng một người đã tạo ra cả một lĩnh vực. **Vận chuyển tối ưu (optimal transport, OT)** có từ trước Figalli rất lâu. Monge đặt bài toán tìm ánh xạ vận chuyển năm 1781. Kantorovich phát biểu lại nó thành một bài toán quy hoạch tuyến tính trên các phép ghép (coupling). Brenier chứng minh rằng với chi phí bình phương, ánh xạ tối ưu là gradient của một hàm thế lồi. Caffarelli xây dựng lý thuyết chính quy sâu sắc đầu tiên cho các hàm thế đó. Ambrosio, Villani và nhiều người khác biến OT thành một ngôn ngữ chung cho PDE, hình học metric và xác suất. Huy chương của Figalli ghi nhận những gì ông làm *bên trong* ngôn ngữ đó: ông phát triển lý thuyết về tính chính quy, tính ổn định và biên tự do (free boundary) của các ánh xạ vận chuyển đủ mạnh để áp dụng vào các bất đẳng thức hình học, mô hình khí quyển và giải tích định lượng.

Bài này dành cho người đã đọc phần giới thiệu Monge–Kantorovich trong bài [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và muốn tìm hiểu phần **tính chính quy** mà bài đó chỉ nhắc qua. Bài **không** coi Figalli là người sáng lập OT, và **không** nhầm Huy chương Fields 2018 của ông với huy chương năm 2010 của Villani. Công trình về phương trình động học của Villani được trình bày ở bài [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đặt lời trích dẫn năm 2018 cho Figalli vào lịch sử dài của OT (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) mà không quy cả lịch sử đó về một người.
- Phát biểu định lý Brenier: với chi phí bình phương, ánh xạ tối ưu là gradient của một hàm thế lồi, và hàm thế đó thỏa phương trình **Monge–Ampère**.
- Giải thích vì sao **tính chính quy của ánh xạ** là một câu hỏi về PDE, và vì sao lý thuyết của Caffarelli là nền tảng chứ không phải chi tiết phụ.
- Mô tả ở mức ý tưởng tính chính quy bên trong, tính ổn định, và tính chính quy từng phần (kiểm soát tập kỳ dị) của ánh xạ OT, có ghi nhận đóng góp của De Philippis và các cộng sự khác.
- Nêu hai lĩnh vực ứng dụng (bất đẳng thức đẳng chu định lượng; phương trình bán địa chuyển (semigeostrophic)) và giải thích vì sao tính chính quy của ánh xạ là cầu nối.
- Phân biệt **Figalli 2018 (OT và ứng dụng)** với **Villani 2010 (tắt dần Landau / phương trình Boltzmann)**.

**Kiến thức cần có.** Bài toán Monge và Kantorovich cùng khái niệm đẩy tiến độ đo (push-forward) $$T_\#\mu=\nu$$, như trong bài OT ở Chương 6; hàm lồi và ma trận Hessian; biết rằng một PDE elliptic phi tuyến hoàn toàn (fully nonlinear) có thể có lý thuyết chính quy. Không cần học trước về phương trình Monge–Ampère.

**Liên hệ với khóa học.** Đọc cùng bài [Caffarelli: biên tự do và Monge–Ampère]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) để thấy truyền thống nghiên cứu tính chính quy (được trao Giải Abel) mà Figalli kế thừa. Bài [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) chỉ là *một* câu chuyện Fields khác về PDE (giới hạn động học, không phải ánh xạ vận chuyển).

---

## 1. Figalli không phát minh ra lĩnh vực này

Phần mở đầu có một nhiệm vụ đơn giản: nếu chỉ nhớ một câu từ các bài báo phổ thông, hãy nhớ câu này: **Figalli không phát minh ra vận chuyển tối ưu.**

Monge hỏi làm thế nào để chuyển một đống đất đến một vị trí cho trước với chi phí nhỏ nhất, và tìm một **ánh xạ** $$T$$. Kantorovich cho phép khối lượng được tách ra, thay ánh xạ bằng một **phép ghép** $$\pi$$ có các phân bố biên cố định, và từ đó có bài toán đối ngẫu lồi. Trong những năm 1980–1990, Brenier chứng minh rằng với chi phí $$c(x,y)=\|x-y\|^2$$ (dưới các giả thiết thông thường về mô-men), tồn tại ánh xạ tối ưu dạng

$$
T=\nabla\phi,
$$

với $$\phi$$ là hàm lồi. McCann, Gangbo và những người khác mở rộng kết quả này sang hình học Riemann và các hàm chi phí tổng quát hơn. Sau đó Caffarelli đặt câu hỏi của nhà giải tích: nếu các mật độ đủ tốt, thì $$\phi$$ tốt đến mức nào? Ambrosio phát triển OT như một công cụ cho dòng gradient và lý thuyết hàm biến phân bị chặn (BV). Villani viết các cuốn sách biến chủ đề thành ngôn ngữ chung, và dùng nó cho các bất đẳng thức hình học và độ cong Ricci. Tuy vậy, **Huy chương Fields 2010** của Villani là về phương trình động học, không phải vì đã sáng lập OT.

Figalli học với **Luigi Ambrosio** (Pisa) và **Cédric Villani** (ENS Lyon), bảo vệ tiến sĩ năm 2007, và làm việc tại ETH Zürich từ năm 2016. Huy chương của ông ghi nhận các kết quả về tính chính quy và ứng dụng bên trong một lĩnh vực đã phát triển.

---

## 2. Từ ánh xạ Brenier đến phương trình Monge–Ampère

Giả sử $$\mu=f\,dx$$ và $$\nu=g\,dy$$ là các độ đo xác suất liên tục tuyệt đối trên (một miền của) $$\mathbb{R}^n$$, và $$T=\nabla\phi$$ đẩy $$\mu$$ thành $$\nu$$. Phép đổi biến (một cách hình thức) cho đẳng thức Jacobian

$$
f(x)=g\bigl(\nabla\phi(x)\bigr)\,\det D^2\phi(x).
$$

Đây là phương trình **Monge–Ampère** cho hàm thế lồi $$\phi$$. Phương trình này phi tuyến hoàn toàn: ẩn hàm xuất hiện trong định thức của các đạo hàm cấp hai. Các khái niệm nghiệm yếu (nghiệm Alexandrov, nghiệm nhớt) đã có từ rất lâu trước khi người ta biết $$\phi$$ có thuộc $$C^2$$ hay không.

Vì sao tính chính quy quan trọng? Nếu $$\phi$$ chỉ là hàm lồi, thì $$T=\nabla\phi$$ xác định hầu khắp nơi nhưng có thể có bước nhảy, có nếp gấp, hoặc không khả vi trên một tập lớn. Các ứng dụng hình học cần nhiều hơn thế: chúng cần ánh xạ là vi phôi trên những tập mở lớn, hoặc cần kiểm soát định lượng xem ánh xạ lệch bao xa so với một ánh xạ mẫu (phép tịnh tiến, phép đẳng cự tuyến tính, ánh xạ đồng nhất). Trong mô hình khí quyển, chính ánh xạ đó là một phép đổi tọa độ; nếu nó quá thô, PDE trong không gian vật lý thậm chí không có nghĩa theo nghĩa phân bố.

Vì vậy, nghiên cứu tính chính quy trong OT không chỉ để làm đẹp kết quả. Nó lấp khoảng cách giữa "có ánh xạ xác định hầu khắp nơi" và "ánh xạ dùng được như một phép đổi biến".

---

## 3. Lý thuyết chính quy của Caffarelli: nền tảng đi trước

Lý thuyết chính quy sâu sắc đầu tiên cho ánh xạ OT với chi phí bình phương là của **Caffarelli**. Đầu thập niên 1990, ông chứng minh rằng nghiệm Alexandrov của phương trình Monge–Ampère thuộc $$C^{1,\alpha}$$ bên trong miền, và với điều kiện miền đích lồi cùng mật độ trơn, nghiệm còn chính quy hơn nữa, cho đến $$C^\infty$$ bên trong khi dữ liệu trơn và miền thỏa điều kiện thích hợp. Tính chính quy tại biên đòi hỏi thêm nhiều điều kiện hình học.

Lời trích dẫn Giải Abel 2023 cho Caffarelli nói đúng về truyền thống này: tính chính quy của PDE phi tuyến, biên tự do, và phương trình Monge–Ampère. Figalli tiếp nối truyền thống đó. Có thể tóm tắt công bằng như sau:

> Caffarelli chứng minh rằng trong trường hợp Euclid, miền lồi và chi phí bình phương, ánh xạ tối ưu chính quy như các mật độ cho phép; Figalli và các cộng sự hỏi điều gì còn đúng khi tính lồi, hàm chi phí hay hình học nền không còn thuộc loại đó.

Về sau, điều kiện Ma–Trudinger–Wang (MTW) đưa ra một giả thiết cấu trúc cho hàm chi phí tổng quát, đủ để khôi phục tính trơn hoàn toàn. Khi điều kiện này không thỏa, hoặc khi giá không lồi, người ta không còn kỳ vọng ánh xạ trơn trên toàn miền. Câu hỏi hiện đại trở thành **tính chính quy từng phần**: tập các điểm kỳ dị có nhỏ không?

---

## 4. Tính chính quy bên trong, tính ổn định và tập kỳ dị của ánh xạ

Các kết quả về OT của Figalli, thường cùng **Guido De Philippis**, và trong các bài khác cùng Kim, Loeper và những người khác, xoay quanh ba ý chính.

**Tính khả tích bậc cao và tính chính quy Sobolev.** Với nghiệm Alexandrov lồi, ban đầu ta chỉ biết $$D^2\phi$$ thuộc $$L^1_{\mathrm{loc}}$$. De Philippis–Figalli chứng minh tính chính quy $$W^{2,1}$$ cho phương trình Monge–Ampère (Inventiones, 2013). Kết quả này nghe có vẻ kỹ thuật, nhưng $$W^{2,1}$$ cho phép lấy đạo hàm ánh xạ theo nghĩa $$L^1$$ và chuyển qua giới hạn trong các biểu thức phi tuyến. Các công trình tiếp theo cho tính ổn định cấp hai: nếu các mật độ hội tụ, thì các ánh xạ hội tụ mạnh theo chuẩn Sobolev, không chỉ hội tụ yếu.

**Tính chính quy từng phần.** Trong bài *Partial regularity for optimal transport maps* (Publ. Math. IHÉS, 2015), De Philippis–Figalli chứng minh rằng với hàm chi phí tổng quát trên $$\mathbb{R}^n$$, hoặc với $$c=d^2/2$$ trên đa tạp Riemann, ánh xạ tối ưu giữa các mật độ trơn là trơn **bên ngoài một tập kỳ dị đóng có độ đo bằng không**. Kết quả này không cần điều kiện MTW và không cần giá lồi. Về bản chất, đây là một định lý về tập kỳ dị: ánh xạ là vi phôi trên một tập mở lớn, còn tập điểm xấu là tập đóng và có độ đo không. Các kết quả $$C^1$$ trong hai chiều trước đó (Figalli–Loeper) và tính chính quy từng phần cho nghiệm Brenier (Figalli–Kim) thuộc cùng nhóm kết quả này.

**Tính ổn định của bất đẳng thức.** Tính chính quy và tính ổn định đi cùng nhau. Nếu ánh xạ gần ánh xạ mẫu, thì các phiếm hàm hình học (chu vi, hằng số Sobolev, sự sinh entropy) phải gần giá trị tối ưu, với độ lệch (deficit) được ước lượng cụ thể. Đó là cầu nối từ ước lượng PDE sang hình học định lượng.

Các công trình sau này về bài toán vật cản và bài toán Stefan (Figalli–Serra, Figalli–Ros-Oton–Serra) là giải tích về biên tự do ở lĩnh vực lân cận, không phải là phần thứ ba của lời trích dẫn năm 2018. Lời trích dẫn chỉ nói về OT và các ứng dụng của nó.

---

## 5. Ứng dụng: bất đẳng thức, khí quyển, xác suất

**Bất đẳng thức đẳng chu định lượng.** Figalli–Maggi–Pratelli (Inventiones, 2010) dùng phép vận chuyển khối lượng để chứng minh dạng định lượng sắc của bất đẳng thức đẳng chu **không đẳng hướng** (anisotropic): nếu một tập gần như cực tiểu hóa chu vi không đẳng hướng, thì nó gần (theo một khoảng cách được định nghĩa chính xác) một phép tịnh tiến của hình Wulff. Phương pháp này thuộc về OT: một ánh xạ vận chuyển từ tập đã cho tới một hình mẫu biến độ lệch về chu vi thành độ lệch của ánh xạ, rồi tính chính quy và tính ổn định biến điều đó thành độ gần về hình học. Đây là phần "hình học metric" trong lời trích dẫn của IMU, được làm cụ thể.

**Phương trình bán địa chuyển.** Hệ phương trình bán địa chuyển (semigeostrophic, SG) là mô hình cho sự hình thành front thời tiết trong khoa học khí quyển. Sau khi đổi sang tọa độ địa chuyển, hàm thế áp suất là hàm lồi và gradient của nó là ánh xạ vận chuyển tối ưu giữa mật độ chất lưu và một độ đo tham chiếu. Benamou–Brenier và Cullen làm cho cách phát biểu này trở thành chuẩn. Sau đó Ambrosio–Colombo–De Philippis–Figalli dùng các ước lượng Sobolev mới cho phương trình Monge–Ampère để chứng minh sự tồn tại nghiệm Euler yếu toàn cục trên xuyến hai chiều và, với giả thiết lồi, trên miền lồi ba chiều. Ở đây tính chính quy của OT không phải hệ quả phụ, mà là lý do khiến vận tốc trong không gian vật lý là một phân bố được xác định đúng.

**Bất đẳng thức hàm và xác suất.** Cùng Carlen, Figalli chứng minh tính ổn định cho bất đẳng thức Gagliardo–Nirenberg và bất đẳng thức log-HLS (có ứng dụng cho mô hình Keller–Segel). Cùng Guionnet, ông dùng các ánh xạ vận chuyển xấp xỉ để chứng minh tính phổ quát trong các mô hình nhiều ma trận. Đó là phần "xác suất" của lời trích dẫn: vận chuyển như một công cụ so sánh các độ đo, không chỉ là ánh xạ giữa các đống cát.

---

## 6. Hai Huy chương Fields, hai trọng tâm khác nhau

Vì Figalli là học trò của Villani, người ta dễ nhầm hai huy chương làm một. Đây là hai giải thưởng khác nhau.

| Huy chương | Trọng tâm của lời trích dẫn | Ngôn ngữ chung | Kết quả riêng |
|------------|-------------------|---------------|------------------|
| Villani, 2010 | Tắt dần Landau phi tuyến; hội tụ về cân bằng cho phương trình Boltzmann | Entropy, bất đẳng thức, OT như bộ công cụ mà Villani cũng phát triển | Các định lý về hồi phục trong phương trình động học |
| Figalli, 2018 | Lý thuyết OT và ứng dụng vào PDE, hình học metric, xác suất | Monge–Ampère, ánh xạ, tính ổn định | Tính chính quy và tính ổn định của phép vận chuyển, cùng các hệ quả hình học |

Văn bản của IMU năm 2010 về Villani có nhắc đến việc ông đi đầu trong ứng dụng OT vào các bất đẳng thức và viết sách về vận chuyển khối lượng; đó là bối cảnh, không phải nội dung chính của huy chương. Còn lời trích dẫn năm 2018 cho Figalli *chính là* về OT. Bài [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/) trình bày riêng các định lý về phương trình động học.

---

## 7. Vì sao ông nhận Huy chương Fields

Có ba lý do, và không lý do nào cần gọi OT là "lý thuyết của Figalli".

1. **Độ khó.** Tính chính quy từng phần và ngưỡng Sobolev cho phương trình phi tuyến hoàn toàn nằm ở giới hạn của những gì giải tích lồi và lý thuyết Calderón–Zygmund làm được. Các chứng minh kết hợp nguyên lý cực đại Alexandrov, tính bất biến afin và lý thuyết độ đo hình học.
2. **Được dùng ở nơi khác.** Khi đã biết ánh xạ thuộc $$W^{2,1}$$ hoặc trơn ngoài một tập có độ đo không, các lĩnh vực khác có thể dùng kết quả đó: hình Wulff, front trong mô hình SG, mô hình ma trận, mô hình Keller–Segel.
3. **Làm rõ những gì còn lại.** Sau Caffarelli, người ta hiểu trường hợp Euclid với miền lồi. Sau Figalli–De Philippis và các nhà nghiên cứu xung quanh, người ta biết một định lý trông như thế nào khi hàm chi phí tổng quát, miền là đa tạp, hoặc ứng dụng chỉ cần ánh xạ thuộc không gian Sobolev.

Trong khóa học, Figalli là ví dụ về **tính chính quy như hạ tầng**: không phải giải một giả thuyết có tên, mà là xây dựng một bộ công cụ đủ mạnh để các định lý khác trở nên chặt chẽ.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Figalli phát minh ra vận chuyển tối ưu." | Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani và những người khác xây dựng lĩnh vực này; huy chương của Figalli là cho tính chính quy và các ứng dụng. |
| "Fields 2018 giống Fields 2010 của Villani." | Villani 2010 là về tắt dần Landau và phương trình Boltzmann; Figalli 2018 là về OT và các ứng dụng của nó. |
| "Ánh xạ Brenier luôn trơn." | Hàm thế lồi cho ánh xạ xác định hầu khắp nơi; tính trơn phụ thuộc vào mật độ, tính lồi, hàm chi phí, và thường chỉ đúng bên ngoài một tập kỳ dị. |
| "Lý thuyết của Caffarelli đã lỗi thời." | Đó là nền tảng; các công trình sau hỏi điều gì còn đúng khi bỏ các giả thiết hình học của ông. |
| "Chính quy từng phần nghĩa là ánh xạ thuộc $$C^\infty$$ ở mọi nơi." | Nghĩa là trơn bên ngoài một tập đóng có độ đo không; tập kỳ dị có thể khác rỗng. |
| "Tính chính quy trong OT chỉ có giá trị thẩm mỹ." | Tính đặt đúng của mô hình SG và bất đẳng thức đẳng chu định lượng đều dùng các ước lượng này làm giả thiết. |

---

## Bài tập

1. Trong hai câu, định lý Brenier bổ sung điều gì cho lý thuyết tồn tại của Kantorovich khi chi phí là bình phương khoảng cách?
2. Viết phương trình Monge–Ampère (dạng hình thức) liên hệ các mật độ $$f,g$$ với hàm thế lồi $$\phi$$. Số hạng nào là phi tuyến, và vì sao điều đó ngăn ta áp dụng trực tiếp lý thuyết chính quy elliptic thông thường?
3. Vì sao **tính lồi của miền đích** xuất hiện trong các định lý chính quy đầy đủ của Caffarelli? Trả lời ở mức ý tưởng, không cần chứng minh.
4. Phát biểu kết quả chính quy từng phần của De Philippis–Figalli (trơn bên ngoài một tập đóng có độ đo không). So với khung cổ điển của Caffarelli, kết quả này *bỏ* được những giả thiết nào?
5. Giải thích, trong không quá tám câu, ánh xạ tối ưu xuất hiện thế nào trong cách phát biểu mô hình bán địa chuyển. Vì sao tính chính quy $$W^{2,1}$$ của hàm thế quan trọng cho nghiệm Euler yếu?
6. **Luyện độ chính xác.** Tìm một câu nói Figalli "tạo ra vận chuyển tối ưu". Viết lại bằng hai câu chính xác, phù hợp với khóa học này.
7. So sánh Figalli 2018 với Villani 2010 bằng một bảng bốn hàng do bạn tự lập: lời trích dẫn, phương trình, vai trò của OT, điều không được khẳng định.
8. **Seminar mở rộng.** Đọc lướt phần mở đầu bài của De Philippis–Figalli, *The Monge–Ampère equation and its link to optimal transportation* (Bull. AMS, 2014), và liệt kê năm thuật ngữ cần học tiếp (ví dụ nghiệm Alexandrov, điều kiện MTW, tính c-lồi, hình Wulff, tọa độ Cullen–Purser).

---

## Liên kết

- IMU Fields Medals 2018: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)
- Wikipedia, Alessio Figalli: [https://en.wikipedia.org/wiki/Alessio_Figalli](https://en.wikipedia.org/wiki/Alessio_Figalli)
- Trang ETH (về tính chính quy của ánh xạ tối ưu): [https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps](https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps)
- Bài giới thiệu của Quanta (2018): [https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/](https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/)
- Tìm trên arXiv, Figalli Monge–Ampère: [https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all](https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all)
- De Philippis–Figalli, tính chính quy $$W^{2,1}$$ (arXiv:1111.7207): [https://arxiv.org/abs/1111.7207](https://arxiv.org/abs/1111.7207)
- De Philippis–Figalli, tính chính quy từng phần (arXiv:1209.5640): [https://arxiv.org/abs/1209.5640](https://arxiv.org/abs/1209.5640)

---

## Tài liệu tham khảo

1. Lời trích dẫn Huy chương Fields 2018 của IMU cho Alessio Figalli.
2. Y. Brenier, “Polar factorization and monotone rearrangement of vector-valued functions,” *Comm. Pure Appl. Math.* 44 (1991).
3. L. A. Caffarelli, các bài báo về tính chính quy của phương trình Monge–Ampère và ánh xạ OT (đầu thập niên 1990); lời trích dẫn Giải Abel 2023.
4. G. De Philippis và A. Figalli, “$$W^{2,1}$$ regularity for solutions of the Monge–Ampère equation,” *Invent. Math.* 192 (2013); “Partial regularity for optimal transport maps,” *Publ. Math. IHÉS* 121 (2015); survey trong *Bull. Amer. Math. Soc.* 51 (2014).
5. A. Figalli, F. Maggi và A. Pratelli, “A mass transportation approach to quantitative isoperimetric inequalities,” *Invent. Math.* 182 (2010).
6. L. Ambrosio, M. Colombo, G. De Philippis và A. Figalli, các kết quả về tính đặt đúng của nghiệm Euler cho phương trình bán địa chuyển (trường hợp hai chiều tuần hoàn và ba chiều lồi).
7. A. Figalli, *The Monge–Ampère Equation and Its Applications*, EMS (2017).
8. C. Villani, *Topics in Optimal Transportation*; *Optimal Transport: Old and New*. Đây là tài liệu nền, không phải nội dung của huy chương năm 2010.
9. Trong khóa học: [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/), [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Hướng đi tiếp

- Đọc ước lượng bên trong của Caffarelli song song với kết quả chính quy từng phần của De Philippis–Figalli: những giả thiết hình học nào chuyển từ "phải giả sử" sang "không cần cho tính trơn hầu khắp nơi"?
- So sánh OT tính toán (thuật toán Sinkhorn, Chương 6) với lý thuyết giải tích: tính toán số dùng phép chính quy hóa, còn lý thuyết chính quy giải thích khi nào ánh xạ chưa chính quy hóa đã gần như trơn.

## Video tham khảo

- **Xem trước** — [Alessio Figalli (2018 Fields Medal) explains Optimal Transport](https://www.youtube.com/watch?v=jyL6ZECM7oM) — Tom Rocks Maths, tiếng Anh. Figalli tự giải thích vận chuyển tối ưu cho khán giả rộng. Nên xem trước khi đọc bài.
- [Alessio Figalli at GYSS 2022 – Recent Developments in Optimal Transport Theory](https://www.youtube.com/watch?v=pu_WHpRDmKE) — National Research Foundation Singapore, tiếng Anh. Bài giảng về các phát triển gần đây của lý thuyết vận chuyển tối ưu, liên quan đến mục 4–5. Nên xem sau khi đọc bài.
