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

Năm 1781, kỹ sư quân sự Pháp **Gaspard Monge** đứng trước một bài toán hết sức trần tục: làm thế nào để xúc một đống đất lớn và đổ đầy một công sự gần đó sao cho tổng công vận chuyển là nhỏ nhất? Hơn hai thế kỷ sau, bài toán xúc đất tưởng chừng tầm thường ấy đã lớn lên thành một trong những ngôn ngữ thống nhất mạnh mẽ nhất của toán học hiện đại — **lý thuyết vận chuyển tối ưu** (*optimal transport*, OT) — kết nối từ hình dạng tinh thể, chuyển động của các front khí quyển, đến hình học của không gian cong và học máy.

Nhưng giữa việc biết "tồn tại một cách vận chuyển tối ưu" và việc thực sự *dùng* được ánh xạ vận chuyển đó trong phương trình đạo hàm riêng hay hình học lại có một vực thẳm: liệu ánh xạ vận chuyển có **trơn** không, hay nó xé rách đống đất thành từng mảng gãy khúc? Năm 2018, **Alessio Figalli** nhận **Huy chương Fields**

> “for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability.”
> — [IMU, Fields Medals 2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)

*Tạm dịch:* Cho các đóng góp vào lý thuyết vận chuyển tối ưu và các ứng dụng của nó trong phương trình đạo hàm riêng, hình học metric và xác suất.

Hãy đặt ngay một cột mốc trung thực: **Figalli không phát minh ra vận chuyển tối ưu.** Monge đặt bài toán, Kantorovich nới lỏng nó bằng quy hoạch tuyến tính, Brenier nối nó với hàm lồi, Caffarelli đặt nền móng đầu tiên cho lý thuyết chính quy, còn Ambrosio và Villani biến nó thành ngôn ngữ chung. Đóng góp mang tầm Fields của Figalli nằm ở phần lõi khó nhất bên trong ngôn ngữ đó: ông cùng các cộng sự (đặc biệt là Guido De Philippis) đã bóc tách **tính chính quy từng phần**, **tính ổn định định lượng** và cấu trúc **tập kỳ dị** của ánh xạ vận chuyển tối ưu khi các giả thiết hình học đẹp đẽ bị gỡ bỏ — biến lý thuyết chính quy thành cây cầu vững chắc sang bất đẳng thức hình học, khí tượng học và xác suất. Bài học này tiếp nối phần giới thiệu Monge–Kantorovich trong [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), đồng thời tách bạch Huy chương Fields 2018 của Figalli với huy chương năm 2010 của người thầy Villani về phương trình động học trong [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đặt lời trích dẫn năm 2018 cho Figalli vào lịch sử dài của vận chuyển tối ưu (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) mà không quy cả lĩnh vực về một cá nhân.
- Phát biểu định lý Brenier: với chi phí bình phương khoảng cách, ánh xạ tối ưu là gradient của một hàm thế lồi, và hàm thế đó thỏa phương trình **Monge–Ampère**.
- Giải thích vì sao **tính chính quy của ánh xạ** là một bài toán PDE phi tuyến hoàn toàn, và vì sao lý thuyết của Caffarelli là nền tảng trực tiếp chứ không phải chi tiết phụ.
- Mô tả trực quan ba trụ cột của Figalli và các cộng sự (đặc biệt là De Philippis): tính chính quy Sobolev $$W^{2,1}$$, tính chính quy từng phần (kiểm soát tập kỳ dị có độ đo không), và tính ổn định định lượng.
- Nêu hai lĩnh vực ứng dụng lớn (bất đẳng thức đẳng chu không đẳng hướng định lượng; phương trình bán địa chuyển trong khí tượng học) và giải thích vì sao tính chính quy của ánh xạ là chìa khóa.
- Phân biệt rõ **Figalli 2018 (vận chuyển tối ưu và ứng dụng)** với **Villani 2010 (tắt dần Landau và phương trình Boltzmann)**.

**Kiến thức cần có.** Bài toán Monge và Kantorovich cùng khái niệm đẩy tiến độ đo (push-forward) $$T_\#\mu=\nu$$, như trong bài OT ở Chương 6; hàm lồi và ma trận Hessian; biết rằng một PDE elliptic phi tuyến hoàn toàn (fully nonlinear) có thể có lý thuyết chính quy. Không cần học trước về phương trình Monge–Ampère.

**Liên hệ với khóa học.** Đọc cùng bài [Caffarelli: biên tự do và Monge–Ampère]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) để thấy truyền thống nghiên cứu tính chính quy (được trao Giải Abel) mà Figalli kế thừa. Bài [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) chỉ là *một* câu chuyện Fields khác về PDE (giới hạn động học, không phải ánh xạ vận chuyển).

---

## Bản đồ kiến thức nền: Vận chuyển tối ưu Monge–Kantorovich và tính chính quy là gì?

Trước khi bước vào phương trình Monge–Ampère, hãy hình dung bài toán bằng một ví dụ cực kỳ trực quan.

**1. Từ đống cát của Monge đến kế hoạch vận chuyển của Kantorovich.**
Giả sử bạn có một phân bố khối lượng ban đầu $$\mu$$ (ví dụ các tiệm bánh nằm rải rác trong thành phố) và một phân bố đích $$\nu$$ (các quán cà phê cần nhận bánh). Chi phí chuyển một đơn vị khối lượng từ điểm $$x$$ đến điểm $$y$$ là $$c(x,y)$$ (thường lấy $$c(x,y) = \|x - y\|^2$$).
- **Bài toán Monge** tìm một **ánh xạ** $$T$$ sao cho toàn bộ khối lượng ở điểm $$x$$ được chở gọn sang đúng một điểm $$y = T(x)$$, bảo toàn khối lượng (ký hiệu $$T_\# \mu = \nu$$), với tổng chi phí $$\int c(x, T(x))\,d\mu(x)$$ nhỏ nhất. Bài toán này rất khó về mặt giải tích vì điều kiện "không được tách khối lượng" làm không gian nghiệm không lồi.
- **Bài toán Kantorovich (1942)** nới lỏng yêu cầu: cho phép chia nhỏ khối lượng ở $$x$$ gửi đến nhiều điểm $$y$$ khác nhau, biểu diễn bằng một **kế hoạch vận chuyển** (hay **phép ghép**, *coupling*) $$\pi(x,y)$$ có biên là $$\mu$$ và $$\nu$$. Nhờ sự nới lỏng này, bài toán trở thành một bài toán tối ưu tuyến tính trên tập lồi compact, nên nghiệm tối ưu luôn tồn tại!

**2. Khi nào ánh xạ vận chuyển bị "xé rách"?**
Hãy thử một thí nghiệm tưởng tượng trong mặt phẳng $$\mathbb{R}^2$$: phân bố ban đầu $$\mu$$ là một **đĩa tròn** đồng nhất, còn phân bố đích $$\nu$$ là **hai nửa đĩa tròn tách rời nhau** (ví dụ nửa bên trái dịch sang trái một đoạn, nửa bên phải dịch sang phải một đoạn — một miền *không lồi*).
Để tốn ít công nhất, ánh xạ tối ưu $$T$$ buộc phải cắt đôi đĩa tròn ban đầu dọc theo đường kính ở giữa: nửa bên trái bay sang trái, nửa bên phải bay sang phải! Ngay dọc theo đường kính đó, ánh xạ $$T$$ **nhảy cóc (gián đoạn)** — hai hạt cát ban đầu nằm sát rạt nhau hai bên đường kính bỗng bị tách xa nhau hàng mét sau khi vận chuyển.

Đó chính là trực giác cốt lõi của **tính chính quy** (*regularity*) trong vận chuyển tối ưu:
- Khi miền đích lồi và các mật độ trơn, liệu ánh xạ $$T$$ có mượt mà không bị xé rách ở đâu không? (Câu trả lời: có — đó là định lý Caffarelli.)
- Khi miền đích **không lồi** (như hai nửa đĩa trên), hoặc khi chi phí không còn là bình phương khoảng cách, chắc chắn sẽ xuất hiện "đường xé" (gọi là **tập kỳ dị** $$\Sigma$$). Nhưng tập kỳ dị đó có nhỏ bé (chỉ như một đường cắt mỏng có diện tích bằng $$0$$) để bên ngoài nó ánh xạ vẫn hoàn toàn trơn tru không? Đó chính là câu hỏi **tính chính quy từng phần** mà Figalli và De Philippis đã chinh phục!

---

## 1. Figalli không phát minh ra lĩnh vực này

Nếu chỉ nhớ một điều để tránh sai lầm phổ biến trên báo chí đại chúng, hãy nhớ: **Figalli không phát minh ra vận chuyển tối ưu.** Ông đứng trên vai một truyền thống dài hơn 230 năm:

- **Monge (1781)** đặt bài toán tìm ánh xạ vận chuyển $$T$$ tối ưu.
- **Kantorovich (1942)** thay ánh xạ bằng phép ghép $$\pi$$, mở ra lý thuyết đối ngẫu lồi (và sau này nhận giải Nobel Kinh tế 1975).
- **Yann Brenier (1987–1991)** tạo ra bước ngoặt giải tích: với chi phí bình phương $$c(x,y)=\|x-y\|^2$$ (và $$\mu$$ không gán khối lượng cho các tập nhỏ), nghiệm tối ưu của Kantorovich thực ra tập trung trên đồ thị của một ánh xạ Monge duy nhất có dạng cực kỳ thanh lịch:

$$
T=\nabla\phi,
$$

trong đó $$\phi$$ là một **hàm lồi**. McCann, Gangbo và nhiều nhà toán học khác mở rộng kết quả này sang đa tạp Riemann và các hàm chi phí tổng quát.
- **Luis Caffarelli** đặt câu hỏi trung tâm của nhà giải tích PDE: nếu mật độ nguồn và đích đều trơn, thì hàm thế lồi $$\phi$$ trơn đến mức nào?
- **Luigi Ambrosio** biến vận chuyển tối ưu thành công cụ cho dòng gradient và hàm biến phân bị chặn (BV). **Cédric Villani** hệ thống hóa toàn bộ lĩnh vực trong hai chuyên khảo kinh điển và nối nó với độ cong Ricci cùng các bất đẳng thức hàm. Tuy vậy, **Huy chương Fields 2010** của Villani được trao cho phương trình động học (tắt dần Landau và Boltzmann), không phải vì sáng lập vận chuyển tối ưu.

Figalli học tiến sĩ dưới sự hướng dẫn đồng thời của **Luigi Ambrosio** (Scuola Normale Superiore di Pisa) và **Cédric Villani** (ENS Lyon), bảo vệ luận án năm 2007 chỉ sau một năm nghiên cứu, và giữ vị trí giáo sư tại ETH Zürich từ năm 2016. Huy chương năm 2018 ghi nhận những đột phá sắc bén về tính chính quy, tính ổn định và ứng dụng bên trong một lĩnh vực đã trưởng thành.

---

## 2. Từ ánh xạ Brenier đến phương trình Monge–Ampère

Giả sử $$\mu=f\,dx$$ và $$\nu=g\,dy$$ là hai độ đo xác suất liên tục tuyệt đối trên $$\mathbb{R}^n$$, và ánh xạ Brenier $$T=\nabla\phi$$ đẩy $$\mu$$ thành $$\nu$$. Theo công thức đổi biến trong tích phân bội, tỷ số thể tích địa phương do phép biến đổi $$y = \nabla\phi(x)$$ gây ra chính là định thức ma trận Jacobian của $$\nabla\phi$$ — tức định thức của **ma trận Hessian** $$D^2\phi(x)$$. Vì $$\phi$$ lồi nên $$D^2\phi \ge 0$$, và ta thu được một phương trình đạo hàm riêng nổi tiếng:

$$
f(x)=g\bigl(\nabla\phi(x)\bigr)\,\det D^2\phi(x).
$$

Đây là **phương trình Monge–Ampère** cho hàm thế lồi $$\phi$$. Hãy để ý cấu trúc đáng gờm của nó: ẩn hàm $$\phi$$ không xuất hiện tuyến tính như trong phương trình Laplace $$\Delta \phi = \mathrm{Tr}(D^2\phi) = f$$, mà nằm bên trong **định thức** của ma trận đạo hàm cấp hai (tích của tất cả các trị riêng của $$D^2\phi$$). Đó là một phương trình elliptic **phi tuyến hoàn toàn** (*fully nonlinear*). Ở chiều $$n = 2$$, phương trình viết ra là $$\phi_{xx}\phi_{yy} - \phi_{xy}^2 = f / g(\nabla\phi)$$. Chỉ cần một trị riêng tiến sát $$0$$ và trị riêng kia phình ra vô cực, tích của chúng vẫn có thể bằng hằng số — chính sự suy biến đó làm các kỹ thuật PDE cổ điển dễ dàng mất tác dụng!

Các khái niệm nghiệm yếu (nghiệm Alexandrov, nghiệm nhớt) đã có từ lâu trước khi người ta biết liệu $$\phi$$ có thuộc lớp $$C^2$$ hay không. Nhưng vì sao tính chính quy lại sống còn đến thế? Nếu $$\phi$$ chỉ là hàm lồi, thì $$T=\nabla\phi$$ xác định hầu khắp nơi nhưng có thể có nếp gấp, vết đứt, hoặc không khả vi trên một tập phức tạp. Trong khi đó:
- Các ứng dụng hình học cần $$T$$ là vi phôi trên những tập mở lớn, hoặc cần ước lượng định lượng xem $$T$$ lệch bao xa so với phép tịnh tiến hay phép đẳng cự.
- Trong khí tượng học, chính ánh xạ $$T$$ đóng vai trò là phép đổi tọa độ từ không gian "địa chuyển" về không gian vật lý; nếu $$T$$ quá thô, trường vận tốc trong không gian vật lý thậm chí không đủ chính quy để viết phương trình theo nghĩa phân bố.

Vì vậy, nghiên cứu tính chính quy trong vận chuyển tối ưu không phải chuyện đánh bóng kỹ thuật: nó là cầu nối quyết định giữa "có một ánh xạ trừu tượng hầu khắp nơi" và "có một phép đổi biến thực sự dùng được".

---

## 3. Lý thuyết chính quy của Caffarelli: nền tảng đi trước

Lý thuyết chính quy sâu sắc đầu tiên cho ánh xạ vận chuyển tối ưu với chi phí bình phương là kiệt tác của **Luis Caffarelli** đầu thập niên 1990. Ông chứng minh rằng nếu miền đích **lồi** và các mật độ $$f, g$$ bị chặn dương hai phía, thì nghiệm Alexandrov của phương trình Monge–Ampère tự động đạt tính chính quy $$C^{1,\alpha}$$ bên trong miền (tức ánh xạ $$T = \nabla\phi$$ liên tục Hölder, không hề có vết xé); và khi $$f, g$$ trơn $$C^\infty$$, $$\phi$$ cũng trơn $$C^\infty$$ bên trong miền. (Ví dụ hai nửa đĩa rời ở mục Bản đồ kiến thức nền chính là minh chứng sống động vì sao giả thiết *miền đích lồi* của Caffarelli là không thể thiếu cho tính trơn toàn cục!)

Lời trích dẫn Giải Abel 2023 cho Caffarelli tôn vinh đúng truyền thống nghiên cứu tính chính quy của PDE phi tuyến, biên tự do và phương trình Monge–Ampère này. Mối quan hệ kế thừa giữa Caffarelli và Figalli có thể tóm gọn trong một câu:

> Caffarelli chứng minh rằng trong trường hợp Euclid, miền đích lồi và chi phí bình phương, ánh xạ tối ưu chính quy tối đa như các mật độ cho phép; Figalli và các cộng sự hỏi điều gì còn đúng khi tính lồi, hàm chi phí hay hình học nền không còn thuộc trường hợp lý tưởng đó.

Về sau, điều kiện **Ma–Trudinger–Wang (MTW)** đưa ra một giả thiết cấu trúc (kiểu độ cong) cho hàm chi phí tổng quát $$c(x,y)$$ đủ để khôi phục tính trơn toàn cục. Nhưng trong thực tế hình học — chẳng hạn trên đa tạp Riemann có độ cong âm, hay khi miền đích không lồi — điều kiện MTW bị vi phạm và ánh xạ chắc chắn có điểm kỳ dị. Câu hỏi trung tâm của thế kỷ XXI chuyển sang **tính chính quy từng phần** (*partial regularity*): tập các điểm kỳ dị đó có đủ nhỏ để ánh xạ vẫn trơn hầu khắp nơi không?

---

## 4. Tính chính quy bên trong, tính ổn định và tập kỳ dị của ánh xạ

Các đột phá của Figalli trong vận chuyển tối ưu — thường hợp tác chặt chẽ với **Guido De Philippis**, cùng Kim, Loeper và nhiều cộng sự khác — xoay quanh ba trụ cột lớn:

**1. Tính khả tích bậc cao và tính chính quy Sobolev $$W^{2,1}$$.** Với nghiệm Alexandrov lồi của phương trình Monge–Ampère, ma trận Hessian $$D^2\phi$$ ban đầu chỉ là một độ đo Radon (có thể chứa phần kỳ dị kiểu hàm delta). Câu hỏi mở lâu năm là: khi vế phải bị chặn dương hai phía, liệu $$D^2\phi$$ có thực sự là một hàm khả tích địa phương $$L^1_{\mathrm{loc}}$$ (tức $$\phi \in W^{2,1}_{\mathrm{loc}}$$) không? Năm 2013 (*Inventiones Mathematicae*), **De Philippis và Figalli** chứng minh câu trả lời là **có** — thậm chí $$D^2\phi \in L \log^k L$$! Thoạt nghe có vẻ rất kỹ thuật, nhưng việc đẩy $$D^2\phi$$ từ độ đo lên hàm $$L^1$$ là ranh giới sống còn: nó cho phép lấy đạo hàm của ánh xạ $$T = \nabla\phi$$ theo nghĩa hàm thông thường và chuyển qua giới hạn trong các phương trình phi tuyến. Các công trình tiếp nối còn thiết lập tính ổn định cấp hai: nếu các mật độ hội tụ, các ánh xạ tối ưu hội tụ mạnh theo chuẩn Sobolev chứ không chỉ hội tụ yếu.

**2. Tính chính quy từng phần (kiểm soát tập kỳ dị).** Trong bài báo bước ngoặt *Partial regularity for optimal transport maps* (*Publ. Math. IHÉS*, 2015), **De Philippis và Figalli** chứng minh rằng với hàm chi phí tổng quát thỏa điều kiện xoắn trên $$\mathbb{R}^n$$, hoặc với chi phí $$c = d^2/2$$ trên một đa tạp Riemann bất kỳ, ánh xạ tối ưu giữa hai mật độ trơn luôn trơn $$C^\infty$$ **bên ngoài một tập kỳ dị đóng $$\Sigma$$ có độ đo bằng không**. Định lý này không cần điều kiện MTW và không cần miền đích lồi! Nói cách khác, dù thế giới không lý tưởng, ánh xạ vận chuyển tối ưu vẫn là một phép vi phôi trơn trên một tập mở chiếm 100% thể tích, chỉ trừ một tập "vết xé" đóng có thể tích bằng không. Các kết quả $$C^1$$ hai chiều trước đó (Figalli–Loeper) và tính chính quy từng phần cho nghiệm Brenier (Figalli–Kim) nằm trong cùng mạch đột phá này.

**3. Tính ổn định định lượng của bất đẳng thức.** Tính chính quy và tính ổn định luôn đi cặp với nhau. Nếu một hình gần đạt cực tiểu cho một đại lượng hình học (như chu vi), ta có thể dùng ánh xạ vận chuyển tối ưu đẩy nó sang hình chuẩn tối ưu: độ lệch của phiếm hàm hình học biến thành độ lệch của ánh xạ $$T$$ khỏi phép đồng nhất, và các ước lượng chính quy–ổn định sẽ dịch độ lệch đó thành khoảng cách hình học thực sự.

Lưu ý thêm: các công trình rất nổi tiếng sau này của Figalli về bài toán vật cản (*obstacle problem*) và bài toán Stefan (cùng Serra, Ros-Oton) thuộc giải tích biên tự do ở lĩnh vực lân cận, bổ sung cho sự nghiệp của ông chứ không phải nội dung chính của lời trích dẫn Huy chương Fields 2018 (vốn tập trung vào vận chuyển tối ưu và ứng dụng).

---

## 5. Ứng dụng: bất đẳng thức, khí quyển, xác suất

**1. Bất đẳng thức đẳng chu định lượng và hình dạng tinh thể.** Bất đẳng thức đẳng chu cổ điển nói rằng trong mọi hình có cùng thể tích, hình cầu có diện tích bề mặt nhỏ nhất. Trong vật lý chất rắn, năng lượng bề mặt của một tinh thể phụ thuộc vào hướng của mặt phẳng (không đẳng hướng), nên hình cân bằng cực tiểu hóa chu vi không đẳng hướng không phải hình cầu mà là một đa diện/hình lồi đặc trưng gọi là **hình Wulff** (*Wulff shape*). Năm 2010 (*Inventiones*), **Figalli–Maggi–Pratelli** dùng ánh xạ vận chuyển Brenier để chứng minh phiên bản **định lượng sắc** của bất đẳng thức đẳng chu không đẳng hướng: nếu một tập $$E$$ có chu vi không đẳng hướng chỉ lớn hơn chu vi hình Wulff một lượng nhỏ $$\delta$$, thì thể tích phần sai khác giữa $$E$$ và một phép tịnh tiến của hình Wulff bị chặn bởi $$C\sqrt{\delta}$$ (số mũ $$1/2$$ là tối ưu). Đây là minh họa rực rỡ nhất cho phần "hình học metric" trong lời trích dẫn của IMU.

**2. Phương trình bán địa chuyển (Semigeostrophic) trong khí tượng học.** Hệ phương trình bán địa chuyển mô tả chuyển động quy mô lớn của khí quyển và sự hình thành các **front thời tiết** (nơi hai khối khí nóng–lạnh ép sát nhau tạo ra sự thay đổi đột ngột về gió và nhiệt độ). Khi đổi sang "tọa độ địa chuyển" do Cullen và Purser đề xuất (và được Benamou–Brenier kết nối với OT), hàm thế áp suất trở thành một hàm lồi mà gradient của nó chính là ánh xạ vận chuyển tối ưu từ phân bố mật độ trong không gian vật lý sang không gian địa chuyển. Nhờ định lý chính quy $$W^{2,1}$$ mới cho phương trình Monge–Ampère, **Ambrosio–Colombo–De Philippis–Figalli** đã chứng minh sự tồn tại nghiệm yếu Euler toàn cục của hệ bán địa chuyển trên xuyến hai chiều và trên miền lồi ba chiều. Ở đây, ước lượng $$W^{2,1}$$ chính là mảnh ghép cho phép chuyển ngược từ tọa độ địa chuyển về trường vận tốc thực trong không gian vật lý!

**3. Bất đẳng thức hàm và xác suất.** Cùng **Eric Carlen**, Figalli chứng minh tính ổn định định lượng cho bất đẳng thức Gagliardo–Nirenberg và bất đẳng thức log-HLS (gắn chặt với mô hình Keller–Segel về sự tụ tập của vi sinh vật). Cùng **Alice Guionnet**, ông xây dựng các ánh xạ vận chuyển xấp xỉ để chứng minh tính phổ quát của phổ trị riêng trong các mô hình nhiều ma trận ngẫu nhiên. Đó là phần "xác suất" trong lời trích dẫn: vận chuyển tối ưu hoạt động như một thước đo hình học để so sánh hai phân bố xác suất phức tạp.

---

## 6. Hai Huy chương Fields, hai trọng tâm khác nhau

Vì Figalli là học trò tiến sĩ của Villani và cả hai đều là những tên tuổi lớn của vận chuyển tối ưu, người ngoài rất dễ gộp hai huy chương làm một. Thực tế, đây là hai ghi nhận có trọng tâm khác hẳn nhau:

| Huy chương | Trọng tâm của lời trích dẫn | Ngôn ngữ chung | Kết quả riêng |
|------------|-------------------|---------------|------------------|
| Villani, 2010 | Tắt dần Landau phi tuyến; hội tụ về cân bằng cho phương trình Boltzmann | Entropy, bất đẳng thức, OT như bộ công cụ mà Villani cũng phát triển | Các định lý về hồi phục trong phương trình động học |
| Figalli, 2018 | Lý thuyết OT và ứng dụng vào PDE, hình học metric, xác suất | Monge–Ampère, ánh xạ, tính ổn định | Tính chính quy và tính ổn định của phép vận chuyển, cùng các hệ quả hình học |

Văn bản của IMU năm 2010 về Villani có nhắc đến việc ông tiên phong ứng dụng vận chuyển tối ưu vào các bất đẳng thức và viết hai bộ sách kinh điển; đó là bối cảnh bổ trợ, không phải trụ cột chính của huy chương năm 2010. Ngược lại, lời trích dẫn năm 2018 cho Figalli đặt **chính vận chuyển tối ưu** vào trung tâm. Bài [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/) sẽ đi sâu riêng vào các định lý động học của Villani.

---

## 7. Vì sao ông nhận Huy chương Fields

Có ba lý do thuyết phục, và không lý do nào cần phóng đại rằng OT là "lý thuyết của riêng Figalli":

1. **Độ khó giải tích ở biên giới.** Tính chính quy từng phần và ngưỡng Sobolev $$W^{2,1}$$ cho phương trình phi tuyến hoàn toàn Monge–Ampère nằm ngay sát giới hạn của giải tích lồi và lý thuyết Calderón–Zygmund. Các chứng minh kết hợp tinh tế nguyên lý cực đại Alexandrov, tính bất biến afin và lý thuyết độ đo hình học.
2. **Sức lan tỏa sang các ngành khác.** Ngay khi biết ánh xạ tối ưu thuộc $$W^{2,1}$$ hoặc trơn ngoài một tập đóng có độ đo không, hàng loạt bài toán ở lĩnh vực lân cận lập tức được khai thông: độ ổn định của tinh thể Wulff, nghiệm Euler của front khí quyển bán địa chuyển, tính phổ quát của ma trận ngẫu nhiên, và bất đẳng thức trong mô hình Keller–Segel.
3. **Định hình bức tranh tổng quát sau Caffarelli.** Sau Caffarelli, giới toán học hiểu rõ thế giới lý tưởng (không gian Euclid, miền lồi, chi phí bình phương). Sau Figalli–De Philippis và các cộng sự, ta biết chính xác một định lý chính quy trông như thế nào khi rời khỏi thế giới lý tưởng đó.

Trong bức tranh toàn khóa học, Figalli là hình mẫu kinh điển về **tính chính quy như hạ tầng của toán học hiện đại**: không chỉ giải một bài toán đơn lẻ có tên gọi, mà xây dựng một bộ công cụ giải tích đủ sắc bén để hàng loạt định lý hình học và vật lý trở nên chặt chẽ.

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
