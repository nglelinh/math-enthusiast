---
layout: post
title: "Alessio Figalli: Vận chuyển Tối ưu và các Ứng dụng (Huy chương Fields 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Alessio Figalli** nhận **Huy chương Fields 2018** vì những đóng góp cho lý thuyết vận chuyển tối ưu và các ứng dụng của nó trong phương trình đạo hàm riêng, hình học metric và xác suất. Huy chương không đặt tên một định lý dạng đóng duy nhất. Nó đặt tên một từ điển: một khi biết cách chuyển một phân bố khối lượng lên một phân bố khác với chi phí tối thiểu, ta thừa hưởng một thế lồi, một phương trình Monge–Ampère, và một cách đo mức gần của một hình gần tối ưu với quả cầu hoặc tinh thể.

Bài này dành cho người học đã gặp bài toán biến phân lần đầu và muốn nắm kiến trúc của vận chuyển tối ưu (OT) hiện đại. Bài **không** khẳng định Figalli phát minh OT, cũng không khẳng định Huy chương Fields 2010 của Cédric Villani là “vì vận chuyển tối ưu.” Trích dẫn 2010 của Villani là tắt dần Landau và phương trình Boltzmann; sách của ông vẫn là tài liệu OT chuẩn, nhưng hai huy chương là hai câu chuyện khác nhau. Chương vận chuyển của khóa này xem [Vận chuyển Tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/); chân dung động học của Villani xem [Villani / Landau]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu bài toán **Monge** và **Kantorovich**: tìm một ánh xạ, hoặc một coupling, chuyển $$\mu$$ lên $$\nu$$ đồng thời cực tiểu hóa một chi phí.
- Giải thích vì sao, với chi phí toàn phương, ánh xạ tối ưu là gradient của một hàm lồi và do đó thỏa một phương trình **Monge–Ampère**.
- Phân biệt **chính quy đầy đủ** (ước lượng kiểu Caffarelli khi dữ liệu đẹp) với **chính quy từng phần** (kỳ dị trên một tập nhỏ khi tính lồi của đích thất bại).
- Mô tả **ổn định** của các hình đẳng chu và hình Wulff: các gần-cực tiểu của chu vi hoặc năng lượng mặt anisotropic gần quả cầu hoặc tinh thể Wulff.
- Gán công lao cẩn thận: Brenier, McCann, Caffarelli, Ambrosio, Villani, và De Philippis–Figalli chiếm những phòng khác nhau của cùng một ngôi nhà.

**Kiến thức nền.** Gradient của hàm lồi; ý về độ đo xác suất trên $$\mathbb{R}^n$$; bất đẳng thức đẳng chu cổ điển ở mức khẩu hiệu. Không cần lý thuyết Monge–Ampère trước đó.

**Liên kết seminar.** LO1 / LO4 (chương trình giải tích khó; hình học hình dạng ↔ chính quy PDE). Ghép với [Vận chuyển Tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) cho từ điển rộng hơn, và với [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau/) chỉ như *một* câu chuyện Fields *khác* tình cờ chia sẻ tác giả của những cuốn sách OT nổi tiếng.

---

## 1. Bài toán vận chuyển thực sự hỏi gì

Monge hỏi làm sao chuyển một đống đất $$\mu$$ vào một hố đào $$\nu$$ sao cho tổng công tối thiểu. Trong ký hiệu hiện đại người ta tìm ánh xạ đo được $$T$$ với $$T_\sharp\mu=\nu$$ cực tiểu hóa

$$
\int c\bigl(x,T(x)\bigr)\,d\mu(x).
$$

Kantorovich nới lỏng ánh xạ thành **coupling**: các độ đo khớp trên không gian tích với đúng các marginal. Bài toán đã nới lỏng là quy hoạch tuyến tính trên không gian vô hạn chiều; nó luôn có nghiệm dưới giả thuyết nhẹ về chi phí $$c$$. Khi $$c(x,y)=\lvert x-y\rvert^2$$ và nguồn tuyệt đối liên tục, định lý Brenier nói bộ tối ưu là duy nhất và có dạng $$T=\nabla\varphi$$ với thế lồi $$\varphi$$.

Đẩy $$\mu=f\,dx$$ tới $$\nu=g\,dy$$ bằng $$\nabla\varphi$$ sinh ra, ở mức mật độ, phương trình Monge–Ampère

$$
\det D^2\varphi(x)=\frac{f(x)}{g\bigl(\nabla\varphi(x)\bigr)}
$$

trên nguồn, với $$\nabla\varphi$$ đưa giá của $$f$$ lên giá của $$g$$. Chính quy của $$T$$ trở thành chính quy của một phương trình elliptic phi tuyến đầy đủ mà vế phải và hình học miền có thể không thân thiện.

**Khẩu hiệu.** Vận chuyển tối ưu không phải khẩu hiệu về “chuyển đồ hiệu quả.” Nó là một cỗ máy sản xuất thế lồi và dữ liệu Monge–Ampère.

---

## 2. Lịch sử ý tưởng

Monge (1781) đặt bài toán ánh xạ; Kantorovich (thập niên 1940) đưa vào coupling và đối ngẫu. Trong những năm 1980–1990, Brenier, Rüschendorf và McCann đồng nhất ánh xạ tối ưu với gradient của hàm lồi và mở rộng lý thuyết sang đa tạp Riemann. Caffarelli phát triển lý thuyết chính quy trong cho nghiệm Alexandrov lồi chặt của Monge–Ampère khi mật độ trơn và đích lồi: thế trơn, do đó ánh xạ cũng vậy.

Các chuyên luận của Villani tổ chức lĩnh vực cho một thế hệ và nối OT với độ cong Ricci và lý thuyết động học. Thế hệ Figalli thừa hưởng một lý thuyết có thể phát biểu tồn tại sạch sẽ và chứng minh trơn trong các tình huống lồi, trơn—và vỡ ngay khi đích không còn lồi, hoặc chi phí không còn toàn phương, hoặc người ta hỏi **mức gần** của một gần-cực tiểu với bộ tối ưu đúng.

Trích dẫn 2018 ghi nhận công trình biến những chế độ “vỡ” ấy thành định lý: chính quy Sobolev và chính quy từng phần cho Monge–Ampère và ánh xạ vận chuyển, ổn định định lượng của các bất đẳng thức hình học, và các ứng dụng trong đó vận chuyển là công cụ chứ không phải đối tượng nghiên cứu.

---

## 3. Chính quy: từ Caffarelli đến De Philippis–Figalli

Khi giá đích không lồi, tính trơn toàn cục của Caffarelli có thể thất bại: ánh xạ tối ưu có thể sinh kỳ dị. Định lý thực tế khi ấy là **chính quy từng phần**. Cùng Guido De Philippis, Figalli chứng minh rằng các ánh xạ tối ưu (với một lớp chi phí rộng) trơn bên ngoài một tập đóng độ đo không, và rằng nghiệm Alexandrov của Monge–Ampère hưởng chính quy $$W^{2,1}$$ của thế—đạo hàm cấp hai thuộc $$L^1_{\mathrm{loc}}$$—đó là tính khả tích tự nhiên một khi rời thế giới lồi đều, trơn.

Các kết quả ấy sắp xếp lại địa lý cảm xúc của chủ đề. Trước chúng, kỳ dị của ánh xạ vận chuyển nghe như bệnh lý người ta hy vọng không gặp. Sau đó, kỳ dị được định vị: ánh xạ chính quy đến mức phương trình cho phép trên một tập độ đo đầy, và đạo hàm cấp hai khả tích đủ để biện minh nhiều lập luận PDE trước đó còn mang tính hình thức.

**Độ chính xác.** Lý thuyết của Caffarelli vẫn là động cơ trơn khi giả thuyết đúng. De Philippis–Figalli cung cấp lý thuyết về điều xảy ra khi chúng không đúng. Không bài nào “giải Monge–Ampère” theo nghĩa nghiệm dạng đóng.

---

## 4. Ổn định của quả cầu và hình Wulff

Bất đẳng thức đẳng chu cổ điển nói rằng trong các tập thể tích cho trước, quả cầu cực tiểu hóa chu vi. Bài toán **Wulff** thay chu vi Euclid bằng năng lượng mặt anisotropic (năng lượng mặt tinh thể phụ thuộc hướng); bộ cực tiểu là hình Wulff gắn với năng lượng ấy.

**Ổn định** hỏi một câu định lượng: nếu một tập gần đạt năng lượng cực tiểu, nó gần quả cầu hoặc tinh thể Wulff đến mức nào? Cùng Maggi và Pratelli, Figalli chứng minh các phiên bản định lượng sắc của bất đẳng thức đẳng chu anisotropic bằng lập luận vận chuyển khối lượng, xây trên chứng minh vận chuyển của Gromov cho bất đẳng thức đẳng chu và trên ánh xạ Brenier–McCann. Công trình sau (kể cả chuẩn tinh thể với Zhang) đẩy ổn định mạnh vào những bối cảnh hình Wulff có mặt phẳng và hình học kém trơn hơn.

Chân dung Quanta nổi tiếng khung Figalli như “bậc thầy bọt xà phòng và vận chuyển.” Khẩu hiệu bọt xà phòng công bằng như thơ—các bài toán đẳng chu là bài toán bọt—nhưng các định lý là ước lượng ổn định, không phải phân loại mọi mặt mao dẫn.

---

## 5. Vận chuyển như công cụ trong PDE, hình học và xác suất

Nửa sau của trích dẫn—“ứng dụng trong phương trình đạo hàm riêng, hình học metric và xác suất”—không phải trang trí. Figalli đã dùng ánh xạ vận chuyển và chính quy của chúng để nghiên cứu phương trình semigeostrophic, ổn định của các bất đẳng thức hàm (Sobolev, Brunn–Minkowski, Prékopa–Leindler), và các bài toán trong đó một coupling xấp xỉ phải được nâng thành ánh xạ gần tối ưu. Mẫu hình có thể mang đi: một bất đẳng thức với trường hợp đẳng thức đã biết trở thành định lý ổn định một khi kiểm soát được ánh xạ vận chuyển xuất hiện trong một chứng minh sắc.

Đó là lý do huy chương không phải “Figalli hoàn tất OT.” Tồn tại và đối ngẫu đã trưởng thành. Sự sắp xếp lại là **chính quy và ổn định** trở nên vững đủ để đi vào các lĩnh vực láng giềng.

---

## 6. Vì sao là Huy chương Fields

Ba lý do đan vào nhau:

1. **Độ khó.** Chính quy từng phần cho ánh xạ sinh bởi thế lồi, và ổn định sắc cho đẳng chu anisotropic, đòi hỏi sự kết hợp lý thuyết độ đo hình học và PDE phi tuyến đầy đủ không suy ra từ việc trích dẫn định lý Brenier.
2. **Tính trung tâm.** OT đã trở thành lingua franca. Cải thiện lý thuyết chính quy và ổn định của nó cải thiện lập luận xuyên giải tích.
3. **Khẩu hiệu trong sáng với phương pháp sâu.** “Gần-cực tiểu gần hình Wulff; ánh xạ kỳ dị thì kỳ dị trên tập nhỏ” dễ nhớ; chứng minh thì không.

Trong khóa này, Figalli ngồi cạnh [chương OT]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) như một tinh chỉnh mức Fields của một từ điển sinh viên gặp như công cụ, và cạnh [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau/) như lời nhắc rằng hai huy chương có thể chung giá sách mà không chung trích dẫn.

---

## Nhầm lẫn thường gặp

| Khẳng định | Chữa lại |
|------------|----------|
| “Huy chương Fields của Villani là vì vận chuyển tối ưu.” | Villani 2010 là tắt dần Landau / Boltzmann; ông viết sách OT, nhưng đó không phải trích dẫn. |
| “Figalli phát minh vận chuyển tối ưu.” | Monge, Kantorovich, Brenier, Caffarelli và nhiều người khác xây lý thuyết; Figalli định hình lại chính quy và ổn định. |
| “Monge–Ampère luôn có nghiệm trơn.” | Tính trơn cần giả thuyết; nếu không thì có chính quy từng phần và ước lượng Sobolev. |
| “Ổn định nghĩa là quả cầu là cực tiểu duy nhất.” | Tính duy nhất của cực tiểu đã cũ hơn; ổn định là phát biểu gần định lượng. |
| “Hình Wulff luôn tròn.” | Chúng là tinh thể của một năng lượng anisotropic; chúng có thể có mặt phẳng. |

---

## Bài tập

1. Bằng lời của bạn: nới Kantorovich **quên gì** và **giữ gì** so với bài toán ánh xạ của Monge?
2. Vì sao $$T=\nabla\varphi$$ với $$\varphi$$ lồi biến bài toán vận chuyển toàn phương thành Monge–Ampère? Viết đồng nhất mật độ trong một dòng.
3. Phân biệt tính trơn trong của Caffarelli với chính quy từng phần De Philippis–Figalli trong bốn câu.
4. Phát biểu bất đẳng thức đẳng chu và bản nâng ổn định của nó bằng hai khẩu hiệu song song (“cực tiểu là quả cầu” đối lập “gần-cực tiểu gần quả cầu”).
5. **Luyện độ chính xác.** Tìm một câu phổ thông nói Villani “đoạt Huy chương Fields vì vận chuyển tối ưu.” Viết lại thành hai câu chính xác.
6. **Kéo giãn seminar.** Lướt [Vận chuyển Tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và liệt kê ba cách dùng OT **không** cần chính quy từng phần mức Figalli. Khi nào bạn vẫn cần lý thuyết chính quy?

---

## Nguồn video và đọc thêm

1. **Trích dẫn IMU** — Fields Medals 2018: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018).
2. **Định hướng** — chân dung Quanta: [Alessio Figalli, a Master of Soap Bubbles and Transport](https://www.quantamagazine.org/alessio-figalli-a-master-of-soap-bubbles-and-transport-20180801/).
3. **Nền** — Villani, *Topics in Optimal Transportation* và *Optimal Transport: Old and New* (các cuốn sách, không phải huy chương 2010).

**Nhắc trạng thái:** Chính quy và ổn định của vận chuyển—**không** phải khẳng định OT bắt đầu năm 2018, và **không** phải trích dẫn Fields của Villani.

---

## Tài liệu tham khảo

1. Trích dẫn Huy chương Fields 2018 của IMU — Alessio Figalli (mathunion.org).
2. **G. De Philippis và A. Figalli** — chính quy $$W^{2,1}$$ cho Monge–Ampère (Invent. Math., 2013); chính quy từng phần cho ánh xạ vận chuyển tối ưu (Publ. Math. IHÉS, 2015).
3. **A. Figalli, F. Maggi, A. Pratelli** — Tiếp cận vận chuyển khối lượng đối với các bất đẳng thức đẳng chu định lượng (Invent. Math., 2010).
4. **L. Caffarelli** — lý thuyết chính quy cho Monge–Ampère và ánh xạ tối ưu (thập niên 1990).
5. Láng giềng khóa học: [Vận chuyển Tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau/).

---

## Hướng đi tiếp

- So sánh định lý tồn tại của Brenier với định lý trơn của Caffarelli: giả thuyết nào vào chỗ nào?
- Đọc một tổng quan về hình Wulff và hỏi “tinh thể” thay đổi gì trong một chứng minh ổn định.
- Tùy chọn seminar A3: một trang về OT trên không gian metric-độ đo (Lott–Villani, Sturm)—mà không gán lý thuyết ấy vào one-liner 2018 của Figalli.
