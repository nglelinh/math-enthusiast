---
layout: post
title: "Luis Caffarelli: Free Boundary và PDE Phi tuyến (Abel 2023)"
chapter: '08'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

Thả một viên đá lạnh vào ly nước ấm và quan sát thật kỹ: ranh giới giữa phần đá rắn và phần nước lỏng không hề đứng yên—nó liên tục dịch chuyển, uốn cong và co rút theo chính dòng nhiệt đang truyền qua nó. Hay hãy tưởng tượng bạn kéo căng một tấm màng đàn hồi phủ lên một viên sỏi nhẵn: chỗ nào tấm màng ôm sát mặt sỏi, chỗ nào nó lơ lửng trên không? Đường ranh giới tách biệt hai vùng ấy không hề được vẽ sẵn trên đề bài—nó là một **ẩn số hình học** tự hình thành từ cân bằng lực. Liệu đường ranh giới ấy có luôn mượt mà, hay có thể đột ngột xuất hiện những góc nhọn sắc lẹm?

Suốt hơn bốn thập niên, **Luis A. Caffarelli** (Đại học Texas tại Austin) đã biến câu hỏi tưởng như đầy cảm tính ấy thành một trong những lý thuyết sâu sắc và sắc bén nhất của giải tích hiện đại. Năm **2023**, ông nhận **Giải Abel**:

> “for his seminal contributions to regularity theory for nonlinear partial differential equations including free-boundary problems and the Monge–Ampère equation.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2023)

Từ những bài toán biên tự do như băng tan và màng đàn hồi, phương trình hoàn toàn phi tuyến Monge–Ampère ở trái tim của vận chuyển tối ưu, cho đến định lý chính quy từng phần nổi tiếng **Caffarelli–Kohn–Nirenberg (CKN)** cho phương trình dòng chảy Navier–Stokes, sự nghiệp của Caffarelli đã dạy cho cả cộng đồng giải tích cách "đặt kính hiển vi" vào những nơi phương trình phi tuyến có nguy cơ gãy vỡ. Tài liệu chính thức: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể định nghĩa bài toán biên tự do và cho một ví dụ vật lý; giải thích mục tiêu của lý thuyết chính quy (khi nào nghiệm và mặt phân cách là trơn); đặt Monge–Ampère vào họ phương trình hoàn toàn phi tuyến; nêu tính chính quy từng phần CKN làm được gì và **không** làm được gì cho Navier–Stokes; và phân biệt việc suy ra phương trình chất lỏng (cầu nối động học) với tính chính quy của Navier–Stokes trong môi trường liên tục.

**Kiến thức nền.** Giải tích nhiều biến; ý niệm về PDE như phương trình Laplace $$\Delta u=0$$. Liên kết: [Navier–Stokes (Millennium)]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Deng và PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/), [ứng dụng của phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

---

## Bản đồ kiến thức nền: Phương trình đạo hàm riêng (PDE) phi tuyến và bài toán biên tự do là gì và nghiên cứu những gì?

Hầu hết sinh viên đại học đều từng gặp **phương trình đạo hàm riêng (PDE) tuyến tính** như phương trình nhiệt, phương trình sóng hay phương trình Laplace $$\Delta u = u_{xx} + u_{yy} = 0$$. Trong thế giới tuyến tính, mọi thứ rất "dễ bảo": tổng của hai nghiệm vẫn là nghiệm, và nếu dữ liệu ban đầu trơn tru thì nghiệm thường cũng trơn tru mượt mà. Thế nhưng thế giới thực lại hiếm khi tuyến tính:

- **PDE phi tuyến (Nonlinear PDE):** Là phương trình trong đó hàm ẩn $$u$$ hoặc các đạo hàm của nó nhân với nhau hay nằm trong một hàm phi tuyến (như $$u \cdot \nabla u$$ trong dòng chảy chất lỏng Navier–Stokes, hay định thức ma trận đạo hàm bậc hai $$\det D^2 u = f$$ trong phương trình Monge–Ampère). Trong thế giới phi tuyến, ta không thể cộng hai nghiệm lại, và nguy hiểm hơn: ngay cả khi dữ liệu ban đầu hoàn toàn trơn tru, nghiệm vẫn có thể đột ngột hình thành **kỳ dị** (vết gãy, sóng xung kích, độ cong bùng nổ lên vô cực).
- **Lý thuyết chính quy (Regularity Theory):** Trong nhiều bài toán, nhờ phép tính biến phân, người ta dễ chứng minh rằng có tồn tại một **"nghiệm yếu"** (một hàm có thể gồ ghề, thậm chí không có đạo hàm theo nghĩa cổ điển). Nhiệm vụ của lý thuyết chính quy là trả lời: *nghiệm yếu đó thực ra có trơn tru ($$C^1, C^2, C^\infty$$) không? Nếu nó có điểm kỳ dị, tập hợp các điểm xấu đó lớn cỡ nào và hình dáng ra sao?*
- **Bài toán biên tự do (Free-Boundary Problem):** Trong bài toán cổ điển (biên cố định), miền $$\Omega$$ được cho trước—ví dụ tìm phân bố nhiệt trên một tấm kim loại hình tròn cố định. Trong **bài toán biên tự do**, chính đường biên ngăn cách hai trạng thái (như mặt phân cách băng–nước khi băng tan, hay đường viền vùng tiếp xúc của màng đàn hồi đè lên vật cản) lại là **một phần của ẩn số** phải tìm đồng thời với nghiệm $$u$$!

---

## 1. Lý thuyết chính quy

Với PDE elliptic tuyến tính có hệ số trơn, một chiến thắng cổ điển của thế kỷ XX khẳng định nghiệm luôn trơn $$C^\infty$$. Thế nhưng khi bước sang **PDE phi tuyến**, dữ liệu trơn không còn bảo đảm nghiệm trơn. Nghiệm yếu có thể tồn tại trong không gian Sobolev nhưng chưa chắc khả vi cổ điển; mặt phân cách tự do có thể mọc ra những đỉnh nhọn hay góc gãy.

**Lý thuyết chính quy** xây dựng các ước lượng định lượng và định lý cấu trúc để trả lời những câu hỏi sống còn: khi nào nghiệm là $$C^{1,\alpha}$$ hay $$C^\infty$$? Khi nào biên tự do là một siêu mặt trơn? Nếu kỳ dị thực sự xuất hiện, tập kỳ dị có kích thước (chiều Hausdorff) nhỏ đến đâu và giới hạn khi phóng đại tại đó rơi vào những hình mẫu nào?

Sự nghiệp của Caffarelli là một chuẩn mực mẫu về nghệ thuật này trên cả ba mặt trận: bài toán biên tự do, PDE hoàn toàn phi tuyến và phương trình chất lỏng. Giải Abel 2023 tôn vinh cả một **chương trình phương pháp**: không phải một ước lượng may mắn, mà là một bộ công cụ hình học–giải tích dạy cả ngành cách phân biệt nơi nào biên tự do trơn tru và nơi nào nó buộc phải có kỳ dị.

---

## 2. Biên tự do

### Cái gì “tự do”?

Với bài toán biên cố định, miền $$\Omega$$ được chốt sẵn (ví dụ giải $$\Delta u = 0$$ trên đĩa đơn vị khi biết nhiệt độ ở viền đĩa). Với **bài toán biên tự do**, chính miền mà PDE được thỏa mãn lại **chưa biết trước**.

Ba ví dụ kinh điển từ đời thực đến tài chính:

- **Bài toán chướng ngại (Obstacle problem):** Phủ một tấm màng đàn hồi lên một vật cản cứng $$\varphi$$ và cố định mép màng ở bên ngoài. Vùng màng chạm sát vật cản là $$\{u = \varphi\}$$, vùng màng căng lơ lửng trên không là $$\{u > \varphi\}$$, còn ranh giới giữa hai vùng đó—**biên tự do** $$\partial\{u > \varphi\}$$—do tự nhiên tự chọn để cực tiểu hóa thế năng đàn hồi.
- **Bài toán Stefan:** Mô hình hóa một tảng băng đang tan trong nước. Nhiệt độ thỏa phương trình nhiệt trong phần nước và bằng $$0$$ trong phần đá; mặt phân cách rắn–lỏng dịch chuyển liên tục theo thời gian và là ẩn số của bài toán.
- **Định giá quyền chọn kiểu Mỹ (American options):** Trong toán tài chính, quyền chọn kiểu Mỹ cho phép thực hiện bất cứ lúc nào trước hạn. Ranh giới giữa "vùng nên giữ tiếp" và "vùng nên thực hiện ngay" chính là một biên tự do!

### Caffarelli làm thay đổi lĩnh vực

Trước Caffarelli (thập niên 1970), người ta biết bài toán chướng ngại có nghiệm yếu, nhưng gần như mù mờ về hình dạng của biên tự do ở chiều $$n \ge 3$$—liệu nó có thể là một tập fractal lởm chởm không? Năm 1977, Caffarelli tạo ra bước ngoặt lịch sử bằng kỹ thuật **phóng đại (blow-up)**, kết hợp các ước lượng hình học và **công thức đơn điệu**. Ông chứng minh rằng tại mọi điểm "chính quy", biên tự do của bài toán chướng ngại thực chất là một siêu mặt **trơn mượt** (thậm chí giải tích thực), còn tại các điểm kỳ dị hiếm hoi, tập kỳ dị bị giam gọn trong một siêu mặt trơn có chiều thấp hơn. Câu hỏi của ngành lập tức nâng tầm: từ *"nghiệm có tồn tại không?"* sang *"biên tự do trơn đến mức nào và phân loại kỳ dị ra sao?"*.

---

## 3. Bài toán chướng ngại như một mô hình

Hãy nhìn trực giác bài toán chướng ngại ở 1 chiều trước cho dễ hình dung: bạn căng một sợi dây đàn hồi qua một cái gờ cong nhẵn $$\varphi(x)$$. Ở nơi sợi dây không chạm gờ, nó căng thẳng thành đoạn thẳng ($$u'' = 0$$); ở nơi nó ôm theo gờ, $$u = \varphi$$. Tại đúng hai điểm tiếp xúc đầu và cuối (biên tự do trong 1D), sợi dây rời khỏi gờ một cách **tiếp tuyến mượt mà** ($$u' = \varphi'$$), nhưng đạo hàm bậc hai $$u''$$ bị nhảy bước đột ngột từ $$\varphi''$$ về $$0$$!

Ở nhiều chiều ($$n \ge 2$$), sợi dây trở thành tấm màng cực tiểu hóa năng lượng Dirichlet $$\int \lvert\nabla v\rvert^2 dx$$ dưới ràng buộc $$v \ge \varphi$$. Khi đó độ trơn tối ưu của nghiệm $$u$$ chỉ đạt tối đa $$C^{1,1}$$ (đạo hàm bậc hai bị chặn nhưng nhảy bước qua biên tự do), còn hình dạng của biên tự do $$\partial\{u > \varphi\}$$ phức tạp hơn gấp bội.

Mô thức của Caffarelli trở thành sách giáo khoa cho cả ngành: đặt tâm tại một điểm $$x_0$$ trên biên tự do, **phóng to liên tục** (đổi tỉ lệ), phân loại các nghiệm giới hạn thuần nhất cực kỳ đơn giản (chẳng hạn nửa không gian hoặc paraboloid), rồi dùng định lý cải thiện độ phẳng (*improvement of flatness*) để kéo tính trơn trở lại thang ban đầu.

---

## 4. Hoàn toàn phi tuyến và Monge–Ampère

### Phương trình elliptic hoàn toàn phi tuyến

Một PDE bậc hai được gọi là **hoàn toàn phi tuyến** (*fully nonlinear*) khi nó phụ thuộc phi tuyến vào chính ma trận đạo hàm bậc hai (ma trận Hessian $$D^2 u$$), chứ không chỉ vào $$u$$ và $$\nabla u$$. Lúc này các công cụ tích phân từng phần cổ điển không còn dùng trực tiếp được; thay vào đó, lý thuyết hiện đại dùng khái niệm **nghiệm nhớt (viscosity solutions)** và các ước lượng Harnack phi tuyến kiểu Krylov–Safonov–Caffarelli.

### Phương trình Monge–Ampère

Ngôi sao sáng nhất trong họ phương trình hoàn toàn phi tuyến là phương trình **Monge–Ampère**:

$$
\det D^2 u = f(x,u,\nabla u).
$$

Vì sao định thức của ma trận Hessian lại xuất hiện khắp nơi?
1. **Hình học vi phân:** Với một mặt cong $$z = u(x,y)$$, độ cong Gauss tại mỗi điểm tỷ lệ trực tiếp với $$\det D^2 u$$. Vì vậy bài toán tìm một mặt lồi có độ cong Gauss cho trước chính là phương trình Monge–Ampère.
2. **Vận chuyển tối ưu (Optimal Transport):** Giả sử bạn cần di chuyển một đống cát có phân bố mật độ $$\mu$$ sang lấp một cái hố có hình dạng mật độ $$\nu$$ sao cho tổng chi phí vận chuyển (bình phương khoảng cách) là nhỏ nhất. Theo định lý Brenier, ánh xạ vận chuyển tối ưu có dạng $$T(x) = \nabla u(x)$$ với $$u$$ là một hàm lồi, và điều kiện bảo toàn khối lượng cát viết đúng thành phương trình Monge–Ampère: $$\det D^2 u(x) = \frac{\mu(x)}{\nu(\nabla u(x))}$$!

Nếu hàm $$u$$ trơn, ta có thể di chuyển từng hạt cát một cách liên tục không bị xé rách; nếu $$u$$ có vết gãy, đống cát phải bị "chẻ đôi" ở ranh giới. Lý thuyết chính quy của Caffarelli cho phương trình Monge–Ampère (thập niên 1990) đã xác định chính xác khi nào nghiệm $$u$$ trơn $$C^{1,\alpha}$$ hay $$C^{2,\alpha}$$, trở thành trụ cột của cả giải tích hình học lẫn lý thuyết vận chuyển tối ưu hiện đại (và ứng dụng sâu vào học máy, thị giác máy tính ngày nay).

---

## 5. Tính chính quy từng phần của Navier–Stokes (CKN)

Năm 1982, cùng với **Robert Kohn** và **Louis Nirenberg**, Caffarelli chứng minh một trong những định lý sâu sắc nhất từng đạt được cho **phương trình Navier–Stokes 3 chiều**—phương trình mô tả chuyển động của chất lỏng nhớt không nén được.

Cho đến tận hôm nay, chưa ai biết liệu một dòng chất lỏng 3D xuất phát từ trạng thái hoàn toàn êm ả có thể đột ngột tạo ra điểm kỳ dị (vận tốc bùng nổ lên vô cực trong thời gian hữu hạn) hay không—đó chính là [bài toán Clay Millennium về Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/). Tuy chưa chứng minh được rằng tập kỳ dị là **rỗng**, định lý **Caffarelli–Kohn–Nirenberg (CKN)** chứng minh rằng tập kỳ dị trong không–thời gian 4 chiều (nếu có tồn tại) phải **vô cùng nhỏ bé**: độ đo Hausdorff parabolic 1 chiều của nó bằng $$0$$! Nói một cách trực quan, trong không–thời gian 4 chiều, các điểm kỳ dị (nếu có) thậm chí không đủ "dày" để tạo thành một đường cong liên tục kéo dài theo thời gian.

### Ba trục cần phân biệt (rất quan trọng cho seminar)

| Trục | Câu hỏi | Trạng thái |
|------|---------|------------|
| Suy ra phương trình / cầu nối động học | Mô hình liên tục liên hệ thế nào với mô hình hạt | Nghiên cứu sôi nổi ([Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/)) |
| Tính chính quy từng phần CKN | Tập kỳ dị của nghiệm yếu lớn đến mức nào? | Định lý lớn; tập kỳ dị được kiểm soát |
| Bài toán Millennium còn mở | Nghiệm trơn 3D có luôn trơn toàn cục không? | Còn mở |

Đừng gộp ba trục này thành một khẩu hiệu. Điểm cốt lõi cần nhớ: **tính chính quy từng phần CKN là đỉnh cao giải tích, nhưng không có nghĩa là bài toán Millennium Navier–Stokes đã được giải.**

---

## 6. Vì sao đáng giải Abel 2023

Tính chính quy của PDE phi tuyến là tầng hạ tầng âm thầm chống đỡ cho hình học, vật lý và khoa học ứng dụng. Biên tự do hiện diện trong vật liệu chuyển pha, dòng chảy ngầm và tài chính; Monge–Ampère nằm ở lõi của vận chuyển tối ưu và thiết kế gương phản xạ quang học; còn Navier–Stokes là trái tim của cơ học chất lỏng. Các ước lượng và kỹ thuật hình học của Caffarelli đã trở thành **ngôn ngữ chung** của hàng thế hệ nhà giải tích.

Giải Abel 2023 vinh danh một chương trình nghiên cứu trọn đời: dạy toán học cách chứng minh một biên tự do là trơn, hoặc phân loại chính xác hình dáng của nó khi nó không thể trơn.

### Phóng đại như một phương pháp (một đoạn dùng lại được)

Xuyên suốt lý thuyết biên tự do, động tác chuẩn là: tại một điểm $$x_0$$ trên biên tự do, ta đặt "kính hiển vi" đổi tỉ lệ

$$
u_r(x) = \frac{u(x_0 + r x)}{\text{normalization}(r)}
$$

rồi cho $$r \to 0$$. Giới hạn thu được thường là một nghiệm thuần nhất rất gọn (như mặt phẳng hay hình nón); việc phân loại các hình mẫu giới hạn đó cho ta thông tin chính quy ngược lại về biên tự do ban đầu. Công thức đơn điệu đóng vai trò chiếc khóa ổn định, ngăn nghiệm dao động hỗn loạn khi phóng to. Nắm được triết lý này còn giá trị hơn việc thuộc lòng từng hằng số kỹ thuật—và chính trường phái Caffarelli đã biến nó thành nghệ thuật chuẩn mực.

---

## 7. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “CKN giải xong bài toán Millennium về Navier–Stokes.” | Chính quy từng phần khác với chính quy hoàn toàn cho mọi dữ liệu trơn. |
| “Biên tự do là biên của miền ta chọn cho tiện.” | Mặt phân cách là **ẩn số**, do chính bài toán quyết định. |
| “PDE phi tuyến không thể có nghiệm trơn.” | Nhiều phương trình có; lý thuyết chính quy nói khi nào và như thế nào. |
| “Monge–Ampère chỉ dành cho vận chuyển tối ưu.” | Vận chuyển tối ưu là một mái nhà lớn; PDE hình học và hình học affine là những mái nhà khác. |
| “Giải Abel 2023 chỉ nói về chất lỏng.” | Biên tự do và Monge–Ampère có vị trí ngang nhau trong citation. |

---

## Điều rút ra ở mức đại học

1. **Biên tự do** là mặt phân cách chưa biết trước, gắn với một PDE.  
2. **Phóng đại** là phóng to cho đến khi bài toán thuần nhất xuất hiện.  
3. **Chính quy từng phần** nghĩa là trơn hầu như khắp nơi, với một chặn về chiều của tập “xấu”.  
4. **Giải tích tầm cỡ giải thưởng** thường cải thiện *bản đồ các kỳ dị có thể có*, chứ không chỉ chứng minh sự tồn tại nghiệm cổ điển.

### Bảng cho seminar (điền trong lớp)

| Chủ đề | Mô hình đơn giản | Người anh em khó | “Chính quy” nghĩa là gì |
|--------|------------------|------------------|--------------------------|
| Bài toán chướng ngại | Sợi dây 1D đặt trên gờ | Biên tự do chiều cao | Mặt phân cách trơn |
| Navier–Stokes | Tuyến tính hóa thành phương trình Stokes | Bài toán Millennium về Navier–Stokes | Không nổ; tập kỳ dị được kiểm soát |
| Monge–Ampère | Thế lồi 2D | Ánh xạ vận chuyển tối ưu | Ước lượng $$C^{1,\alpha}$$ hoặc cao hơn |

### Cảnh báo về CFD

Các chương trình CFD “giải Navier–Stokes” hằng ngày bằng rời rạc hóa và mô hình hóa. Bài toán mở của toán học nói về *phương trình liên tục chính xác* trong một lớp không gian hàm được phát biểu chặt chẽ. Hãy để thành công kỹ thuật và trạng thái Millennium ở **hai cột khác nhau** trong bài luận của bạn.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2023: tính chính quy của PDE phi tuyến, biên tự do, Monge–Ampère.
- Chính quy từng phần CKN cho Navier–Stokes không phải là lời giải của bài toán Clay.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: bài giảng Abel của Caffarelli, về cấu trúc mặt phi tuyến: [https://www.youtube.com/watch?v=dVGX6QhO8rU](https://www.youtube.com/watch?v=dVGX6QhO8rU).  
2. **Lịch sử**: phỏng vấn Caffarelli của giải Abel 2023: [https://www.youtube.com/watch?v=rz3uPOIL9AA](https://www.youtube.com/watch?v=rz3uPOIL9AA).  
3. **Định hướng**: phim ngắn về Caffarelli: [https://www.youtube.com/watch?v=tdUBLu4fHbw](https://www.youtube.com/watch?v=tdUBLu4fHbw).  
4. **Định hướng**: phản ứng khi nhận cuộc gọi về giải Abel: [https://www.youtube.com/watch?v=ze4SKx5yBFw](https://www.youtube.com/watch?v=ze4SKx5yBFw).  

**Cổng chính thức và tài liệu**

- Abel 2023 Caffarelli: https://abelprize.no/abel-prize-laureates/2023  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/caffarelli-pde_dVGX6QhO8rU_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2023 Caffarelli — https://abelprize.no/abel-prize-laureates/2023  
2. Caffarelli Abel lecture — non-linear surface structure — https://www.youtube.com/watch?v=dVGX6QhO8rU  
3. Abel interview Caffarelli 2023 — https://www.youtube.com/watch?v=rz3uPOIL9AA  
4. Caffarelli short film — https://www.youtube.com/watch?v=tdUBLu4fHbw  
5. Reaction to Abel Prize call — https://www.youtube.com/watch?v=ze4SKx5yBFw  
6. Wikipedia — Luis Caffarelli — https://en.wikipedia.org/wiki/Luis_Caffarelli  
7. Wikipedia — Free boundary problem — https://en.wikipedia.org/wiki/Free_boundary_problem  
8. Wikipedia — Obstacle problem — https://en.wikipedia.org/wiki/Obstacle_problem  
9. Clay — Navier–Stokes (contrast partial regularity) — https://www.claymath.org/millennium/navier-stokes-equation/  
10. Abel popular PDFs (pde/obstacle/freeBoundary) — https://abelprize.no/abel-prize-laureates/2023  

1. [Abel 2023](https://abelprize.no/abel-prize-laureates/2023).  
2. Bài khảo sát về biên tự do; văn liệu về Monge–Ampère.  
3. Caffarelli–Kohn–Nirenberg (chính quy từng phần của Navier–Stokes).  
4. Bài mô tả bài toán Navier–Stokes của Fefferman cho Clay; bài về Navier–Stokes và Deng trong khóa học.

---

## Hướng đi tiếp

- Một ẩn dụ kỹ thuật: mô phỏng sự đổi pha so với định lý.  
- Bảng cho seminar: Millennium Navier–Stokes / CKN / chính quy của biên tự do.  
- Ghi lại rằng bài toán Millennium về Navier–Stokes là người láng giềng gần nhất của CKN.  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Talagrand]({{ site.baseurl }}/contents/vi/chapter08/08_09_Talagrand_Probability/).

## Video tham khảo

- **Xem trước** — [Luis Caffarelli: Non-linear and non-local surface structure problems and some of its applications](https://www.youtube.com/watch?v=dVGX6QhO8rU) — The Abel Prize, tiếng Anh. Xem trước để nghe chính Caffarelli giới thiệu các bài toán cấu trúc mặt phi tuyến và các ứng dụng.
- [Luis A. Caffarelli - The Abel Prize Interview 2023](https://www.youtube.com/watch?v=rz3uPOIL9AA) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe ông kể về con đường làm toán.
- [Luis A. Caffarelli - the 2023 Abel Prize Laureate](https://www.youtube.com/watch?v=tdUBLu4fHbw) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua một đoạn phim ngắn giới thiệu laureate.
