---
layout: post
title: "Percolation và mô hình Ising phẳng của Smirnov (Huy chương Fields 2010)"
chapter: '02'
order: 28
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Stanislav Smirnov** nhận **Huy chương Fields 2010**

> “For the proof of conformal invariance of percolation and the planar Ising model in statistical physics.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

*Tạm dịch: vì chứng minh tính bất biến bảo giác của mô hình thấm (percolation) và mô hình Ising phẳng trong vật lý thống kê.*

Lời trao giải nêu tên **hai mô hình trên lưới** của vật lý thống kê. Nó không nói rằng "mọi mô hình hai chiều ở điểm tới hạn đều đã thành định lý". Từ lâu, các nhà vật lý đã dự đoán rằng ở điểm tới hạn, nhiều mô hình phẳng "quên" mất cấu trúc lưới vi mô và chỉ còn giữ lại một hình học bảo giác. Cụ thể, trong giới hạn thang đo (scaling limit), các sự kiện có đường nối xuyên qua miền, các đường biên phân cách và các hàm tương quan đều biến đổi một cách hiệp biến dưới ánh xạ bảo giác của miền. Muốn biến dự đoán này thành toán học, cần tìm những đại lượng quan sát được (observable) vẫn kiểm soát được khi bước lưới tiến về không. Smirnov tìm ra những đại lượng như vậy cho **mô hình thấm đỉnh tới hạn trên lưới tam giác** (2001) và, cùng các cộng sự, cho **mô hình Ising phẳng**. Ngôn ngữ liên tục để mô tả các đường biên là **tiến hóa Schramm–Loewner (SLE)**, do Oded Schramm đưa ra và được Gregory Lawler, Schramm và Wendelin Werner phát triển; xem [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Các định lý về chuyển pha của Hugo Duminil-Copin về sau thuộc cùng lĩnh vực: [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

Bài này dành cho người đã học giải tích phức và xác suất cơ bản, và muốn nắm **cấu trúc** của huy chương năm 2010: công thức Cardy nói gì, vì sao lưới tam giác là thiết yếu, tính bất biến bảo giác của mô hình Ising nghĩa là gì khi nói qua các "fermion", và những bài toán gần đó nào vẫn còn mở.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nói ngắn gọn **mô hình thấm Bernoulli** là gì, và phân biệt thấm **đỉnh** (site) với thấm **cạnh** (bond).
- Giải thích vì sao giá trị **tới hạn** $$p_c$$ là nơi nên tìm một giới hạn thang đo không tầm thường.
- Mô tả **công thức Cardy** như một dự đoán về xác suất để một cụm tới hạn nối xuyên qua một "hình chữ nhật bảo giác", và biết rằng định lý của Smirnov năm 2001 chứng minh dự đoán đó cho **mô hình thấm đỉnh tới hạn trên lưới tam giác**.
- Giải thích vì sao **không** được khẳng định cùng kết quả cho mọi lưới, đặc biệt là cho **mô hình thấm cạnh trên lưới vuông**.
- Đặt **SLE** làm ngôn ngữ cho giới hạn thang đo của các đường biên, ghi công Schramm cho định nghĩa và Lawler–Schramm–Werner cho lý thuyết giải tích.
- Phân biệt định lý về mô hình thấm với kết quả về tính bất biến bảo giác của **mô hình Ising phẳng** đến sau (Smirnov; Chelkak–Smirnov và các cộng sự).
- Ghi công cẩn thận và tránh những câu phóng đại như "Smirnov đã giải xong vật lý thống kê hai chiều".

**Kiến thức nền.** Hàm chỉnh hình và ánh xạ bảo giác giữa các miền phẳng ở mức giáo trình giải tích phức nhập môn; biến ngẫu nhiên Bernoulli và ý tưởng giới hạn thang đo (bước lưới $$\delta\to 0$$); sự khác nhau giữa mô hình rời rạc và quá trình liên tục. Không cần học trước về SLE.

**Liên kết với các bài khác.** Bài này cho thấy một dự đoán vật lý trở thành định lý gắn với một lưới cụ thể, và mối nối giữa mô hình rời rạc với hình học bảo giác liên tục. Đọc cùng [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) để hiểu ngôn ngữ đường cong, và [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) cho các kết quả sắc nét về chuyển pha.

---

## 1. Vì sao vật lý thống kê quan tâm tới tính bất biến bảo giác

Một cấu hình **thấm** trên một đồ thị là cách tô màu ngẫu nhiên các đỉnh (site) hoặc các cạnh (bond) thành "mở" hoặc "đóng", độc lập với nhau, mỗi phần tử mở với xác suất $$p$$. Câu hỏi hình học đơn giản nhất: các đỉnh mở có tạo thành một đường nối hai cung trên biên hay không. Khi $$p$$ rất nhỏ hoặc rất lớn, câu trả lời không có gì thú vị. Nhiều lưới hai chiều có một **giá trị tới hạn** $$p_c$$, tại đó xác suất có đường nối xuyên qua một hình chữ nhật lớn vẫn bị chặn xa khỏi cả $$0$$ lẫn $$1$$.

Khi co bước lưới $$\delta\to 0$$, người ta dự đoán hình học của các cụm sẽ hội tụ về một đối tượng ngẫu nhiên liên tục. Lý thuyết trường bảo giác (CFT) hai chiều gợi ý một điều mạnh hơn: giới hạn đó phải **bất biến bảo giác**. John Cardy, dùng các phương pháp CFT chưa chặt chẽ, đưa ra công thức tường minh cho xác suất nối xuyên trong giới hạn, cho một "hình chữ nhật bảo giác" (*J. Phys. A*, 1992). Lennart Carleson nhận thấy công thức trở nên rất đơn giản nếu dùng tam giác đều. Cái khó không phải là viết ra công thức. Cái khó là chứng minh rằng một mô hình lưới cụ thể thực sự hội tụ, và giới hạn biến đổi đúng như Cardy dự đoán.

---

## 2. Mô hình thấm đỉnh trên lưới tam giác

Định lý năm 2001 của Smirnov nói về **mô hình thấm đỉnh tới hạn trên lưới tam giác** $$\mathbb{T}$$, với $$p=1/2$$. Bài báo ngắn trên *Comptes Rendus* (Smirnov, *C. R. Acad. Sci. Paris* 333 (2001); bản dài hơn là arXiv:0909.4499) đưa ra các hàm rời rạc xây từ xác suất nối xuyên, cùng một lập luận đổi màu. Các hàm này gần như điều hòa và thỏa một hệ Cauchy–Riemann rời rạc, nhờ một **đẳng thức đổi màu** chỉ có trên $$\mathbb{T}$$. Chúng hội tụ về các hàm chỉnh hình tường minh, là nghiệm của một bài toán biên hỗn hợp Dirichlet–Neumann. Từ đó suy ra tính bất biến bảo giác của xác suất nối xuyên và **công thức Cardy**. Dạng của Carleson: trên tam giác đều cạnh bằng một, xác suất (trong giới hạn) để có đường mở nối một cạnh với một đoạn trên cạnh khác tỉ lệ tuyến tính với độ dài đoạn đó.

**Không được nói mơ hồ ở chỗ này.** Lập luận dùng đối xứng bậc ba của $$\mathbb{T}$$ một cách thiết yếu. Đây là định lý về **mô hình trên lưới này**, không phải định lý về "mô hình thấm trên mặt phẳng" nói chung. Đặc biệt, **mô hình thấm cạnh tới hạn trên lưới vuông**, mô hình thấm phẳng nổi tiếng còn lại, vẫn là một bài toán mở nổi tiếng về tính bất biến bảo giác. Người ta tin vào tính phổ quát, và đã có nhiều tiến bộ từng phần, nhưng khóa học không giả vờ rằng kết quả năm 2001 của Smirnov đã giải quyết mọi lưới.

---

## 3. Từ xác suất nối xuyên tới đường cong: SLE là ngôn ngữ của giới hạn

Xác suất nối xuyên là một đại lượng vô hướng bất biến bảo giác. Đối tượng phong phú hơn là các **đường biên**: đường phân cách vùng mở với vùng đóng, hay đường "thám hiểm" chạy dọc biên các cụm. Khi đã kiểm soát được xác suất nối xuyên, người ta hỏi tiếp: các đường ngẫu nhiên này có hội tụ theo phân phối về một quá trình liên tục hay không.

**Tiến hóa Schramm–Loewner** $$\mathrm{SLE}_\kappa$$, do Oded Schramm đưa ra năm 2000 (*Israel J. Math.* 118, "Scaling limits of loop-erased random walks and uniform spanning trees"), là một họ một tham số các tập (hull) ngẫu nhiên lớn dần trong một miền phẳng. Chúng được sinh ra bằng cách cho phương trình Loewner được điều khiển bởi một chuyển động Brown có phương sai $$\kappa$$. Schramm chứng minh: nếu một giới hạn thang đo dạng dây cung (chordal) tồn tại và bất biến bảo giác (cùng với một tính chất Markov miền), thì nó phải là $$\mathrm{SLE}_\kappa$$ với một giá trị $$\kappa$$ nào đó. Với mô hình thấm, giá trị dự đoán là $$\kappa=6$$.

Lawler, Schramm và Werner phát triển lý thuyết giải tích của SLE: tính chất hạn chế (restriction), các số mũ giao và số mũ tách rời, và hình học của chuyển động Brown hai chiều. Đó là nội dung Huy chương Fields 2006 của Werner, **không** phải nội dung lời trao giải cho Smirnov; nó là ngôn ngữ để đọc các định lý trên lưới của Smirnov. Các công trình sau (đáng chú ý là Camia–Newman, và các bài về đường biên) dùng định lý nối xuyên của Smirnov làm điểm xuất phát để chứng minh đường thám hiểm của mô hình thấm hội tụ về $$\mathrm{SLE}_6$$. Khi trình bày, cần phân công rõ:

| Đóng góp | Của ai, nói ngắn gọn |
|----------|---------------------|
| Đưa ra SLE | Schramm (2000) |
| Lý thuyết giải tích của SLE; biên ngoài của chuyển động Brown; các số mũ | Lawler–Schramm–Werner |
| Công thức Cardy và tính bất biến bảo giác cho mô hình thấm đỉnh trên lưới tam giác | Smirnov (2001) |
| Đại lượng quan sát được / đường biên của mô hình Ising phẳng | Smirnov; về sau Chelkak–Smirnov và các cộng sự |

---

## 4. Mô hình Ising phẳng

**Mô hình Ising** gán spin $$\pm 1$$ cho các đỉnh của một đồ thị phẳng, với trọng số Boltzmann ưu tiên các đỉnh kề nhau cùng hướng. Ở nhiệt độ tới hạn, người ta dự đoán mô hình có giới hạn thang đo bất biến bảo giác; đây là một trong những thành công sớm nhất của CFT về mặt vật lý. (Lời giải chính xác của Onsager cho năng lượng tự do hai chiều; còn tính bất biến bảo giác của toàn bộ hình học là một khẳng định khác, khó hơn.)

Smirnov đưa ra các **fermion chỉnh hình rời rạc** cho mô hình Ising tới hạn (xem "Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model", *Ann. of Math.* 172 (2010)). Cùng Dmitry Chelkak, ông chứng minh rằng các đại lượng fermion này có giới hạn thang đo phổ quát và bất biến bảo giác trên một họ lớn các đồ thị phẳng, không chỉ trên một lưới: Chelkak–Smirnov, "Universality in the 2D Ising model and conformal invariance of fermionic observables", *Invent. Math.* 189 (2012), arXiv:0910.2045. Các công trình sau cùng Chelkak, Duminil-Copin, Hongler, Kemppainen và những người khác chứng minh đường biên của mô hình Ising hội tụ về đường SLE (cụ thể là $$\mathrm{SLE}_3$$ cho đường biên spin, trong bối cảnh thích hợp).

Có hai điểm cần lưu ý. Thứ nhất, cụm "tính bất biến bảo giác của mô hình Ising" trong lời trao giải nói về chương trình đại lượng quan sát được và giới hạn này, không phải lời giải năm 1944 của Onsager cho hàm phân hoạch. Thứ hai, theo một nghĩa nào đó, lý thuyết cho mô hình Ising **phổ quát hơn** định lý về mô hình thấm năm 2001: khung Chelkak–Smirnov áp dụng cho một lớp rộng các đồ thị đẳng bán kính (isoradial), còn định lý Cardy cho mô hình thấm vẫn gắn với lưới tam giác.

---

## 5. Cách xây dựng chứng minh, và vì sao được Fields

Cả hai câu chuyện đều bắt đầu bằng việc nghĩ ra một đại lượng rời rạc $$F_\delta$$ mã hóa sự kiện cần nghiên cứu (nối xuyên, spin, đường biên), thỏa một hệ gần như chỉnh hình, và có điều kiện biên chuyển thành một bài toán Dirichlet hoặc Riemann–Hilbert liên tục. Tính tiền compact cho ta các giới hạn theo dãy con; tính duy nhất nghiệm của bài toán liên tục xác định được giới hạn; và tính hiệp biến bảo giác được thừa hưởng từ đó. Với mô hình thấm trên lưới tam giác, đẳng thức đổi màu đồng nhất hai sự kiện "ba nhánh" và cho ta hệ Cauchy–Riemann rời rạc. Với mô hình Ising, đại lượng quan sát được là một fermion, và tính chỉnh hình rời rạc đến từ tính khả tích của mô hình. Hai phương pháp có họ hàng nhưng không giống hệt nhau: lưới phải cung cấp một đẳng thức đủ mạnh để khép kín hệ phương trình. Vì vậy có lưới giải được, có lưới vẫn còn mở.

Huy chương không phải vì "ông đoán đúng công thức Cardy". Một dự đoán vật lý đã thành định lý với công thức nối xuyên tường minh; các đại lượng chỉnh hình rời rạc đã tổ chức lại cơ học thống kê hai chiều; và khi chúng bất biến bảo giác, lý thuyết đường cong của Schramm–Lawler–Werner có thể gắn $$\mathrm{SLE}_6$$ hoặc $$\mathrm{SLE}_3$$ với một mô hình lưới cụ thể. Những người cùng nhận huy chương năm 2010 là Lindenstrauss, Ngô Bảo Châu và Villani; xem [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/) cho lời trao giải về phương trình động học tại cùng đại hội.

---

## 6. Những gì vẫn còn mở

Mô hình thấm cạnh tới hạn trên lưới vuông, và tính bất biến bảo giác của mô hình thấm trên các lưới phẳng tổng quát, vẫn chưa thành định lý theo nghĩa của Smirnov 2001. Với mô hình thấm đỉnh trên lưới tam giác, khi đã có tính bất biến bảo giác thì nhiều số mũ và xác suất "nhánh" (arm events) đã được tính; nhưng các phát biểu tương ứng trên các lưới khác thường vẫn là giả thuyết hoặc chỉ chuyển sang được một phần. Bước đi tự tránh (self-avoiding walk), với giới hạn thang đo được dự đoán là $$\mathrm{SLE}_{8/3}$$, là một bài toán gần gũi nổi tiếng nhưng **không** phải định lý của Smirnov. Bài về Duminil-Copin nói về tính sắc nét của chuyển pha và các kết quả trên lưới khác; các kết quả đó bổ sung, chứ không lặp lại, định lý bất biến bảo giác năm 2001.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Smirnov chứng minh tính bất biến bảo giác của mô hình thấm trên mọi lưới." | Định lý năm 2001 dành cho **mô hình thấm đỉnh tới hạn trên lưới tam giác**. Mô hình thấm cạnh trên lưới vuông là trường hợp còn lại nổi tiếng. |
| "Cardy đã chứng minh công thức nối xuyên." | Cardy suy ra công thức bằng CFT, chưa chặt chẽ; Smirnov chứng minh nó cho mô hình thấm đỉnh trên lưới tam giác. |
| "SLE do Werner (hoặc Smirnov) phát minh." | SLE do **Schramm** đưa ra (2000). Huy chương của Werner là cho việc phát triển SLE và hình học Brown hai chiều, chủ yếu cùng Lawler và Schramm. |
| "Huy chương 2010 chỉ nói về mô hình thấm." | Lời trao giải của IMU nêu mô hình thấm **và** mô hình Ising phẳng. |
| "Lời giải Onsager chính là tính bất biến bảo giác của mô hình Ising." | Onsager tính năng lượng tự do hai chiều (1944). Tính bất biến bảo giác của đại lượng quan sát được và đường biên là một phát biểu hình học đến sau. |
| "Có SLE thì mọi mô hình hai chiều đã xong." | SLE chỉ là ứng viên cho phân phối giới hạn. Chứng minh một mô hình lưới hội tụ về SLE với một $$\kappa$$ cụ thể là một định lý riêng, thường vẫn còn mở. |

---

## Bài tập

1. Trong hai câu, phân biệt mô hình thấm **đỉnh** và thấm **cạnh**. Vì sao một chứng minh dùng đẳng thức đổi màu trên lưới tam giác có thể không chuyển được sang lưới vuông?
2. **Xác suất nối xuyên** của một hình chữ nhật bảo giác là gì? Vì sao chỉ tại $$p_c$$ người ta mới kỳ vọng có một giới hạn không tầm thường, không phụ thuộc bước lưới, nằm trong $$(0,1)$$?
3. Nêu ý chính của công thức Cardy, và viết một câu về dạng tam giác đều của Carleson.
4. Luyện ghi công: viết cho **Schramm**, **Lawler–Schramm–Werner** và **Smirnov** mỗi người một câu, đủ chính xác để dùng trong một báo cáo phản biện.
5. Đọc lướt tóm tắt bài Chelkak–Smirnov (arXiv:0910.2045). Đại lượng quan sát được là gì, và theo nghĩa nào kết quả này "phổ quát" hơn Smirnov 2001?
6. Vì sao "đường biên hội tụ về $$\mathrm{SLE}_6$$" mạnh hơn "xác suất nối xuyên hội tụ về công thức Cardy"? Nói ngắn gọn: cần thêm những bước nào về tính compact hoặc nhận dạng giới hạn?
7. **Luyện phát biểu chính xác.** Viết lại câu phổ biến "Smirnov chỉ ra chuyển pha hai chiều là bảo giác" thành hai câu chính xác cho khóa học này.
8. **Thảo luận.** So sánh huy chương này với [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/): ai cung cấp quá trình đường cong, ai cung cấp mô hình lưới hội tụ về nó?

---

## Liên kết

- IMU Fields Medals 2010 (chỉ mục được yêu cầu): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- Trang Smirnov IMU / ICM 2010 (bản lưu hoạt động): [Fields Medal – Stanislav Smirnov](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-stanislav-smirnov.html)
- Chỉ mục Fields Medal IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia: [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov)
- arXiv: [0909.4499](https://arxiv.org/abs/0909.4499) (Smirnov, percolation tới hạn); [0910.2045](https://arxiv.org/abs/0910.2045) (Chelkak–Smirnov, Ising); tìm [Smirnov percolation Cardy](https://arxiv.org/search/?query=Smirnov+percolation+Cardy&searchtype=all)
- Khóa học: [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/), [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/)

---

## Tài liệu tham khảo

1. International Mathematical Union, citation Fields Medals 2010 cho Stanislav Smirnov (tài liệu IMU / ICM Hyderabad 2010).
2. **S. Smirnov**, “Critical percolation in the plane: conformal invariance, Cardy’s formula, scaling limits,” *C. R. Acad. Sci. Paris Sér. I Math.* 333 (2001), 239–244; bản dài arXiv:0909.4499.
3. **J. L. Cardy**, “Critical percolation in finite geometries,” *J. Phys. A* 25 (1992), L201–L206.
4. **O. Schramm**, “Scaling limits of loop-erased random walks and uniform spanning trees,” *Israel J. Math.* 118 (2000), 221–288.
5. **D. Chelkak and S. Smirnov**, “Universality in the 2D Ising model and conformal invariance of fermionic observables,” *Invent. Math.* 189 (2012), 515–580, arXiv:0910.2045.
6. **S. Smirnov**, “Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model,” *Ann. of Math.* 172 (2010), 1441–1473.
7. Wikipedia, [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov); chân dung khóa học [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) và [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

---

## Hướng đi tiếp

- Đọc một bài tổng quan về lập luận đổi màu trước khi đọc bài trên *Comptes Rendus*. Sau khi đọc [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), viết nửa trang về trình tự: tiên đề của SLE → công thức Cardy → chứng minh hội tụ về $$\mathrm{SLE}_6$$.
- Bài tập thêm: viết một trang "những gì còn mở về mô hình thấm hai chiều", **không** khẳng định tính phổ quát là định lý.

## Video tham khảo

- **Xem trước**: [Stanislav Smirnov - 2d Percolation Revisited](https://www.youtube.com/watch?v=6QOnfvWqVoo) (MIT Department of Mathematics, tiếng Anh). Smirnov nhìn lại mô hình thấm hai chiều. Nên xem trước để làm quen với mô hình thấm đỉnh, thấm cạnh và câu hỏi nối xuyên.
- [Stanislav Smirnov, Percolation crossings and complex analysis](https://www.youtube.com/watch?v=6hCSSCV7lvQ) (Clay Mathematics Institute, tiếng Anh). Bài giảng về xác suất nối xuyên và vai trò của giải tích phức, đúng nội dung mục 1 và 2.
- [Stanislav Smirnov - Percolation revisited](https://www.youtube.com/watch?v=ZNpbvrhfWPA) (Department of Mathematics - Northwestern University, tiếng Anh). Một bài giảng khác cùng chủ đề. Dùng để ôn lại sau khi đọc xong bài.
