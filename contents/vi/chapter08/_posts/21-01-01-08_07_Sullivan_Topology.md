---
layout: post
title: "Dennis Sullivan: Tôpô, Động lực và Hình học (Abel 2022)"
chapter: '08'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

Nếu một nhà toán học dành cả đời để cắt dán những không gian cong năm, sáu chiều trong tôpô hình học, bạn có ngờ rằng một ngày nọ ông sẽ bước sang thế giới của các bức hình fractal hỗn độn—tập Julia và tập Mandelbrot—và giải quyết gọn gàng một bài toán đã treo lơ lửng hơn nửa thế kỷ kể từ thời Pierre Fatou? Với hầu hết mọi người, phân loại hình dạng đa tạp nhiều chiều và nghiên cứu sự hỗn độn khi lặp một hàm số phức là hai chuyên ngành xa nhau nghìn trùng. Nhưng với **Dennis Parnell Sullivan**, cả hai chỉ là những phương ngữ khác nhau của cùng một ngôn ngữ về **hình dạng và sự biến đổi**.

Năm **2022**, **Dennis Parnell Sullivan** (Đại học Stony Brook; CUNY Graduate Center) nhận **Giải Abel**:

> “for his groundbreaking contributions to topology in its broadest sense, and in particular its algebraic, geometric and dynamical aspects.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2022)

Ủy ban Abel gọi ông là "một nghệ sĩ bậc thầy thực thụ" (*true virtuoso*), người liên tục đi qua ranh giới giữa đại số, hình học, giải tích và động lực học để thay đổi diện mạo của tôpô. Hãy cùng theo dấu hành trình của bậc thầy ấy—từ lý thuyết phẫu thuật đa tạp đến định lý **không có miền lang thang** lừng danh—và so sánh sự nghiệp đa tài trọn đời này với những bản anh hùng ca về một định lý đơn lẻ như Perelman và Giả thuyết Poincaré. Tài liệu chính thức: [abelprize.no](https://abelprize.no/).

**Mạch bài học:** Bản đồ kiến thức nền (Tôpô đại số, tôpô hình học và động lực phức) → Bốn cột mốc của Sullivan → Khung giải thích chậm: tự tay tính quỹ đạo $$f(z)=z^2-1$$ và cơ chế "đếm số chiều" chứng minh không có miền lang thang → Tập Julia và phân loại Fatou → So sánh với Perelman.

---

## Mục tiêu học tập

Sau bài này, bạn có thể đặt Sullivan vào ba mảng: tôpô đại số, tôpô hình học và động lực phức; nêu được định lý không có miền lang thang và thành phần Fatou lang thang là gì; giải thích “cấu trúc hình học trên không gian” như chủ đề thống nhất; so sánh tôpô của cả một đời với bản hùng ca một định lý ([Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)); và tránh việc rút gọn giải Abel 2022 thành một kết quả duy nhất.

**Kiến thức nền.** Ánh xạ liên tục; từ vựng cơ bản của tôpô; ý niệm lặp hàm $$f$$, $$f\circ f$$, $$f^{\circ n}$$. Giải tích phức, ngoài việc biết “có hàm biến phức”, không bắt buộc ở lần đọc đầu.

---

## Bản đồ kiến thức nền: Tôpô đại số, tôpô hình học và động lực phức là gì và nghiên cứu những gì?

Ba cụm từ trong lời trao giải của Sullivan nghe có vẻ rất chuyên sâu, nhưng trực giác cốt lõi của chúng đứng trên ba trụ cột rất gần gũi với người học toán đại học:

### 1. Tôpô đại số (Algebraic Topology) và Đồng luân hữu tỉ
Làm sao biết chắc chắn một quả cầu và một chiếc bánh donut (hình xuyến) không thể bóp méo liên tục thành nhau mà không cắt xé? Ta gắn cho mỗi không gian một **"chữ ký đại số"** (như nhóm cơ bản, nhóm đồng điều hay nhóm đồng luân) không thay đổi khi kéo giãn. **Đồng luân hữu tỉ** (nơi Sullivan phát minh ra *mô hình tối tiểu*) là cách "lọc nhiễu" thiên tài: bỏ qua các chi tiết xoắn hữu hạn phức tạp để biến toàn bộ hình dạng tôpô thành đại số đa thức gọn gàng trên $$\mathbb{Q}$$.

### 2. Tôpô hình học (Geometric Topology) và Phẫu thuật đa tạp (Surgery)
Tập trung trực tiếp vào hình dạng của các **đa tạp** (những không gian nhìn gần thì phẳng như $$\mathbb{R}^n$$, ví dụ bề mặt Trái Đất là 2-đa tạp). **Lý thuyết phẫu thuật** đúng như tên gọi: muốn chuyển một quả cầu thành chiếc bánh donut, ta khoét đi hai đĩa tròn trên quả cầu rồi khâu một ống trụ nối hai miệng lỗ đó lại! Các nhà tôpô chiều cao dùng đúng thao tác cắt–dán chuẩn hóa ấy để phân loại mọi đa tạp có thể tồn tại.

### 3. Động lực phức (Complex Dynamics) và Ánh xạ tựa bảo giác
Lấy một hàm biến phức đơn giản, ví dụ $$f(z) = z^2 + c$$, chọn điểm khởi đầu $$z_0 \in \mathbb{C}$$ rồi lặp mãi: $$z_1 = f(z_0), z_2 = f(z_1), \dots$$. Mặt cầu phức lập tức chia thành hai vùng: **tập Fatou** (vùng hiền lành—hai điểm gần nhau có số phận dài hạn giống nhau) và **tập Julia** (ranh giới fractal hỗn độn). Còn **ánh xạ tựa bảo giác** là phép biến dạng cho phép biến hình tròn siêu nhỏ thành hình elip có tỉ số trục bị chặn—đủ mềm để uốn nắn, nhưng đủ cứng để giữ thông tin giải tích.

---

## 1. Tôpô theo nghĩa rộng

Sự nghiệp hơn nửa thế kỷ của Sullivan giống như một chuyến du hành qua nhiều châu lục khác nhau: lý thuyết phẫu thuật đa tạp, đồng luân hữu tỉ, tôpô dây (*string topology*), hình học tựa bảo giác và động lực phức. Sợi chỉ đỏ kết nối tất cả là một tầm nhìn nhất quán: **cấu trúc hình học ẩn sâu trên mọi không gian**, dù đó là một đa tạp trơn nhiều chiều hay một tập Julia mong manh dạng fractal.

Cụm *"topology in its broadest sense"* trong lời tuyên dương không phải lời xã giao:

- Công cụ **đại số** (đồng luân hữu tỉ, đại số vi phân phân bậc DGA, toán tử đồng điều);  
- Công cụ **hình học** (phẫu thuật đa tạp, cấu trúc Lipschitz và ánh xạ tựa bảo giác);  
- Công cụ **động lực** (phép lặp ánh xạ phức, tính cứng và từ điển Sullivan giữa nhóm Kleinian và động lực hữu tỉ).

Hiếm có nhà toán học nào đi lại thành thạo và tạo ra đột phá nền tảng trên cả ba địa hạt ấy. Giải Abel 2022 cũng là lời nhắc nhở rằng động lực học không đứng ngoài toán thuần túy, mà là một nhánh máu thịt của tôpô hiện đại.

---

## 2. Các chủ đề cột mốc (chọn lọc)

Không một bài báo đơn lẻ nào gói trọn được sự nghiệp của Sullivan. Dưới đây là bốn cột mốc chính trên tấm bản đồ của ông:

### Phẫu thuật và đa tạp

Lý thuyết phẫu thuật đặt câu hỏi: nếu hai đa tạp có cùng "chữ ký đồng luân" (giống nhau về mặt tôpô đại số), khi nào ta có thể cắt và dán các mảnh chuẩn để biến cái này thành cái kia? Từ luận án tiến sĩ xuất sắc của mình, Sullivan đã giúp định hình ngôn ngữ chuẩn mực của tôpô đa tạp chiều cao hiện đại.

### Đồng luân hữu tỉ và mô hình đại số

Việc tính chính xác các nhóm đồng luân của một không gian (ngay cả của mặt cầu $$S^n$$!) là bài toán khó bậc nhất của tôpô. Sullivan đưa ra ý tưởng **mô hình tối tiểu** (*Sullivan minimal models*) bằng các dạng vi phân đa thức: nếu chấp nhận bỏ qua phần "xoắn hữu hạn" (làm việc trên $$\mathbb{Q}$$), toàn bộ kiểu đồng luân của một không gian tôpô có thể dịch sang một đối tượng đại số thuần túy, giúp việc tính toán trở nên tường minh và thực dụng đến bất ngờ.

### Ánh xạ tựa bảo giác và cấu trúc hình học

Một ánh xạ **bảo giác** (*conformal*) biến hình tròn cực nhỏ thành hình tròn cực nhỏ (giữ nguyên mọi góc), nên nó rất "cứng". Một ánh xạ **tựa bảo giác** (*quasiconformal*) nới lỏng một chút: nó biến hình tròn cực nhỏ thành hình elip có tỷ lệ trục dài/trục ngắn bị chặn. Sự nới lỏng có kiểm soát ấy tạo ra phép màu: đủ mềm dẻo để ta tha hồ uốn nắn và biến dạng, nhưng vẫn đủ cứng để giữ lại các thông tin hình học và giải tích cốt lõi.

### Động lực học: không có miền lang thang

Trong động lực phức, việc lặp một ánh xạ hữu tỉ trên mặt cầu Riemann chia mặt cầu thành tập Fatou (trật tự) và tập Julia (hỗn độn). Năm 1985, Sullivan dùng chính công cụ ánh xạ tựa bảo giác để chứng minh rằng **ánh xạ hữu tỉ không bao giờ có miền lang thang**, hoàn tất mảnh ghép cuối cùng trong bức tranh phân loại Fatou–Julia sau hơn 65 năm chờ đợi.

---

## 3. Động lực gặp tôpô: không có miền lang thang

Hãy bắt đầu bằng một ví dụ cực kỳ đơn giản để thấy tập Fatou và tập Julia hoạt động ra sao: xét $$f(z) = z^2$$ trên mặt cầu Riemann $$\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$$.
- Nếu $$\lvert z\rvert < 1$$ (bên trong đĩa đơn vị), bình phương liên tiếp kéo $$z$$ về $$0$$.
- Nếu $$\lvert z\rvert > 1$$ (bên ngoài đĩa đơn vị), bình phương liên tiếp đẩy $$z$$ ra $$\infty$$.
- Còn ngay trên đường tròn đơn vị $$\lvert z\rvert = 1$$, mọi điểm ở lại trên đường tròn và bị khuếch đại góc gấp đôi sau mỗi bước—hỗn độn hoàn toàn!

Ở đây, tập Julia là đường tròn $$\lvert z\rvert = 1$$, còn **tập Fatou** gồm hai miền mở rời nhau: bên trong đĩa (hút về $$0$$) và bên ngoài đĩa (hút về $$\infty$$). Cả hai miền này đều *bất biến* ($$f(U) = U$$). Với các đa thức hay ánh xạ hữu tỉ phức tạp hơn, tập Fatou có thể vỡ thành vô số mảnh mở nhỏ (gọi là **thành phần Fatou**), và phép lặp $$f$$ nhảy từ mảnh này sang mảnh khác.

Một câu hỏi tự nhiên suốt từ năm 1920 của Fatou: liệu có thể tồn tại một **miền lang thang (wandering domain)**—tức một thành phần Fatou $$U$$ sao cho các ảnh tiếp theo của nó

$$
U,\; f(U),\; f^{\circ 2}(U),\; f^{\circ 3}(U),\; \dots
$$

đều hoàn toàn phân biệt, cứ trôi dạt mãi trên mặt cầu mà không bao giờ quay lại thăm một miền nào cũ?

**Định lý Sullivan (1985):** Với mọi ánh xạ hữu tỉ $$f:\widehat{\mathbb{C}}\to\widehat{\mathbb{C}}$$ bậc $$d \ge 2$$, **không tồn tại miền lang thang**. Mọi thành phần Fatou sau hữu hạn bước đều phải rơi vào một chu kỳ tuần hoàn!

### Khung giải thích: Tự tay tính quỹ đạo $$f(z)=z^2-1$$ và cơ chế "đếm số chiều" của Sullivan (nên đọc chậm)

#### Phần 1: Tự tay tính quỹ đạo của đa thức bậc 2 $$f(z) = z^2 - 1$$ (tập Julia "Vương cung thánh đường")
Hãy thử vài điểm khởi đầu $$z_0$$ ngay bằng tay:
- **Điểm $$z_0 = 0$$:** $$0 \mapsto -1 \mapsto 0 \mapsto -1 \mapsto \cdots$$ — rơi vào **chu kỳ tuần hoàn độ dài 2**! Hơn nữa, vì đạo hàm $$(f^{\circ 2})'(0) = f'(-1)\cdot f'(0) = (-2)\cdot 0 = 0$$, chu kỳ $$\{0, -1\}$$ là chu kỳ *siêu hút*.
- **Điểm $$z_0 = 0.2$$ (nằm gần $$0$$):**
  $$
  0.2 \mapsto -0.96 \mapsto -0.0784 \mapsto -0.9939 \mapsto -0.0122 \mapsto -0.99985 \dots
  $$
  Quỹ đạo nhảy qua lại giữa thành phần Fatou quanh $$0$$ và thành phần Fatou quanh $$-1$$ rồi dính chặt vào chu kỳ $$\{0, -1\}$$!
- **Điểm $$z_0 = 2$$:** $$2 \mapsto 3 \mapsto 8 \mapsto 63 \mapsto 3968 \to \infty$$ (thuộc lưu vực hút của $$\infty$$).
- **Điểm cố định đẩy:** Giải $$z^2 - 1 = z \implies z = \frac{1 \pm \sqrt{5}}{2}$$ ($$\approx 1.618$$ và $$-0.618$$). Tại đây $$\lvert f'(z)\rvert = \lvert 2z\rvert > 1$$ nên chúng nằm ngay trên **tập Julia**!

#### Phần 2: Chứng minh phản chứng bằng "phép đếm số chiều" của Sullivan
Làm sao Sullivan chứng minh được rằng không bao giờ có một miền $$U$$ cứ nhảy sang những mảnh mới mãi mãi mà không quay lại?
1. **Giả sử phản chứng** tồn tại một miền lang thang $$U$$ sao cho $$U, f(U), f^{\circ 2}(U), \dots$$ đôi một rời nhau. Vì chúng hoàn toàn không đụng nhau, ta có thể tùy ý bóp méo góc (biến dạng tựa bảo giác) trên $$U$$ bằng **vô hạn tham số độc lập** rồi chép đồng bộ dọc theo quỹ đạo của nó mà không bao giờ gây mâu thuẫn tự va chạm!
2. **Định lý ánh xạ Riemann đo được:** Mỗi phép biến dạng tựa bảo giác như vậy sinh ra một ánh xạ hữu tỉ mới cùng bậc $$d$$. Vậy ta thu được một họ biến dạng **vô hạn chiều** các ánh xạ hữu tỉ bậc $$d$$.
3. **Đếm số chiều không gian ánh xạ hữu tỉ bậc $$d$$:** Mọi ánh xạ hữu tỉ bậc $$d$$ có dạng
   $$
   f(z) = \frac{a_d z^d + \cdots + a_1 z + a_0}{b_d z^d + \cdots + b_1 z + b_0}.
   $$
   Tử số có $$d+1$$ hệ số, mẫu số có $$d+1$$ hệ số; chia cả tử và mẫu cho một hằng số khác 0 ta mất đi $$1$$ bậc tự do, còn lại đúng **$$2d + 1$$ tham số phức** (ví dụ với $$d = 2$$ chỉ có đúng $$5$$ chiều phức!).
4. **Mâu thuẫn tuyệt đối:** Không thể nhét một họ biến dạng **vô hạn chiều** vào trong một không gian chỉ có **$$2d + 1$$ chiều** hữu hạn được! Vậy miền lang thang không thể tồn tại.

Chứng minh ấy vừa thanh thoát vừa sâu sắc, và nó còn mở ra **Từ điển Sullivan**, nối liền hai thế giới tưởng chừng tách biệt: động lực học của ánh xạ hữu tỉ và hình học hyperbol của các nhóm Kleinian trong 3 chiều.

### Đối chiếu với hàm nguyên

Cần nói thật chính xác về phạm vi định lý: nếu ta rời khỏi lớp ánh xạ hữu tỉ để xét **hàm nguyên siêu việt** (như $$f(z) = z + \sin(2\pi z) + 1$$), thì miền lang thang **có thể tồn tại** (vì không gian các hàm nguyên có số chiều vô hạn, nên lập luận phản chứng đếm số chiều ở Bước 3–4 không còn mâu thuẫn nữa). Ghi rõ điều kiện "ánh xạ hữu tỉ" là thói quen chính xác của người làm toán.

---

## 4. Tập Julia và “toán học đẹp”

Phép lặp hàm phức trên mặt cầu sinh ra những bức ảnh tập Julia và tập Mandelbrot rực rỡ, thường xuất hiện trên bìa sách hay áp phích toán học đại chúng. Vẻ đẹp thị giác ấy là có thật, nhưng giá trị toán học của định lý Sullivan sâu sắc hơn nhiều: kết quả của ông không phải là một bức họa đẹp, mà là một **định lý phân loại sắc bén** trên vùng trật tự (tập Fatou), giúp dọn sạch hành vi bệnh lý để toàn bộ động lực học hữu tỉ có thể được hiểu trọn vẹn.

Trong khóa học này, ta nối hình ảnh tập Julia với [toán học đẹp]({{ site.baseurl }}/contents/vi/chapter04/), nhưng luôn nhớ tách bạch: bức ảnh fractal là cánh cửa mời gọi sự tò mò, còn lời tuyên dương Giải Abel 2022 vinh danh cả tòa kiến trúc **tôpô và động lực học** phía sau nó.

---

## 5. Vì sao đáng giải Abel: sự nghiệp của một bậc thầy

Nếu câu chuyện Huy chương Fields thường tỏa sáng quanh một đột phá tập trung (như Perelman với Giả thuyết Poincaré), thì Giải Abel của Sullivan tôn vinh **một cung đường dài đầy sáng tạo**: ở mỗi lĩnh vực ông đi qua, ông đều mang theo một "máy dịch" giúp bài toán ở ngôn ngữ này được giải bằng công cụ của ngôn ngữ khác—mô hình đại số cho đồng luân, ánh xạ tựa bảo giác cho động lực phức, tôpô dây cho không gian vòng lặp.

Danh hiệu "nghệ sĩ bậc thầy" (*virtuoso*) ở đây mang nghĩa toán học rất cụ thể: không phải chỉ chơi thuần thục một nhạc cụ, mà là biết **chuyển điệu giữa nhiều thể loại** để tạo ra hòa âm mới.

### Chu kỳ của thành phần Fatou (định lý cho ta điều gì)

Một khi miền lang thang bị loại trừ, mọi thành phần Fatou $$U$$ của ánh xạ hữu tỉ đều trở nên **tiền tuần hoàn**: sau hữu hạn bước, ảnh $$f^{\circ m}(U)$$ rơi vào một chu kỳ tuần hoàn. Mà theo phân loại cổ điển của Fatou–Julia–Siegel–Herman, một thành phần Fatou tuần hoàn chỉ có thể thuộc đúng bốn kiểu: lưu vực hút (*attracting basin*), lưu vực parabolic, đĩa Siegel hoặc vành Herman.

Nhìn rộng ra toàn Chương 8, đây là một mô-típ kinh điển tầm cỡ Giải Abel: **tính cứng dọn sạch cảnh quan** để công việc phân loại trở nên khả thi—giống hệt cách tính siêu cứng của Margulis loại bỏ các đồng cấu hoang dại, hay tính modular của Wiles khóa chặt những đường cong elliptic được phép tồn tại.

---

## 6. So với Perelman (cẩn thận)

| | Sullivan (Abel 2022) | Perelman (Fields 2006) |
|--|----------------------|-------------------------|
| Điểm nhấn | Tôpô cả một sự nghiệp và động lực học | Dòng Ricci hoàn tất việc hình học hóa |
| Phong cách | Nhiều cảnh quan, nhiều ngôn ngữ | Hoàn tất chương trình của Hamilton một cách tập trung |
| Khẩu hiệu tiêu biểu | Không có miền lang thang (trong nhiều kết quả) | Hình học hóa ⇒ Poincaré |
| Loại giải thưởng | Abel, cả sự nghiệp | Fields (từ chối) và Clay (từ chối) |

Cả hai đều nối hình học và giải tích với tôpô. Đừng ép người này thành người kia.

---

## 7. Tôpô và hỗn độn như một nghề

Sự nghiệp của Sullivan lập luận rằng phân loại các không gian và phân loại các chuyển động dài hạn không đối lập nhau. Ánh xạ tựa bảo giác, phẫu thuật và tính cứng động lực cùng chia sẻ một thói quen: kiểm soát độ méo hình học cho đến khi kết luận tôpô tự theo sau. “Broadest sense” trong citation là lời mời bỏ những bức tường nhân tạo giữa động lực học và tôpô thuần túy.

**Gợi ý cho seminar.** Chọn một ảnh tập Julia và viết 150 từ nối sự hỗn độn nhìn thấy được với định nghĩa động lực học chính xác (quỹ đạo, tập Julia, tập Fatou), mà không tuyên bố đã chứng minh định lý không có miền lang thang.

---

## 8. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Giải Abel 2022 chỉ nói về tập Julia.” | Tập Julia là hình ảnh phổ thông; citation nói về tôpô theo nghĩa rộng. |
| “Không có miền lang thang cho mọi ánh xạ phức.” | Định lý nói về ánh xạ **hữu tỉ**; một số hàm nguyên thì khác. |
| “Sullivan chỉ là người làm động lực học.” | Động lực học là một nhánh; phẫu thuật, đồng luân hữu tỉ, tôpô hình học là những nhánh khác. |
| “Bậc thầy nghĩa là không sâu.” | Ở đây nghĩa là sâu trên nhiều “phương ngữ” của tôpô. |
| “Giải cho cả sự nghiệp thì không có định lý tiêu biểu.” | Thường có, và thường còn nhiều hơn một. |

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2022: tôpô theo nghĩa rộng, gồm đại số, hình học, động lực.
- Không có miền lang thang; mô hình của Sullivan; sự nghiệp của một bậc thầy.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: bài giảng Abel của Sullivan, Gathering chestnuts… fluid motion: [https://www.youtube.com/watch?v=RRMBRiyNcjI](https://www.youtube.com/watch?v=RRMBRiyNcjI).  
2. **Định hướng**: danh sách phát của giải Abel về Sullivan 2022: [https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw](https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw).  

**Cổng chính thức và tài liệu**

- Abel 2022 Sullivan: https://abelprize.no/abel-prize-laureates/2022  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/sullivan-topology_RRMBRiyNcjI_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2022 Sullivan — https://abelprize.no/abel-prize-laureates/2022  
2. Sullivan Abel lecture — Gathering chestnuts… fluid motion — https://www.youtube.com/watch?v=RRMBRiyNcjI  
3. Abel Prize playlist Sullivan 2022 — https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw  
4. Wikipedia — Dennis Sullivan — https://en.wikipedia.org/wiki/Dennis_Sullivan  
5. Wikipedia — No wandering domain theorem — https://en.wikipedia.org/wiki/No_wandering_domain_theorem  
6. Wikipedia — Rational homotopy theory — https://en.wikipedia.org/wiki/Rational_homotopy_theory  
7. Stony Brook / CUNY culture pages (search Sullivan Abel) — https://www.stonybrook.edu/  
8. Abel popular PDF topology (from laureate page materials) — https://abelprize.no/sites/default/files/2022-03/topolgy_eng.pdf  
9. Abel popular PDF no-wandering — https://abelprize.no/sites/default/files/2022-03/wanderingset_eng.pdf  

1. [Abel 2022](https://abelprize.no/abel-prize-laureates/2022).  
2. Sullivan, *Quasiconformal homeomorphisms and dynamics I…*, Ann. of Math. 1985 (miền lang thang).  
3. Các bài giới thiệu phổ thông (Quanta, PDF của giải Abel); luôn quay lại phát biểu của định lý.  
4. Trong khóa: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/); chương toán học đẹp (về tập Julia, cần cẩn thận).

---

## Hướng đi tiếp

- Seminar về hình ảnh: tập Julia và định lý đi kèm.  
- So tính cứng của Sullivan và của Margulis.  
- Ghi lại một hướng mở trong động lực phức hoặc tôpô hình học vẫn cuốn hút bạn.  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/).

## Video tham khảo

- **Xem trước** — [Dennis Sullivan: Gathering chestnuts of math related to fluid motion](https://www.youtube.com/watch?v=RRMBRiyNcjI) — The Abel Prize, tiếng Anh. Xem trước để nghe chính Sullivan nói về những ý tưởng toán học gắn với chuyển động của chất lỏng.
