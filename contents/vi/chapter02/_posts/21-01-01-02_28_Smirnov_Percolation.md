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

Citation nêu **hai mô hình lattice** của vật lý thống kê, không phải khẩu hiệu “mọi mô hình 2D tới hạn đều đã thành định lý.” Từ lâu các nhà vật lý tiên đoán rằng, ở tới hạn, nhiều mô hình phẳng quên lưới vi mô và chỉ nhớ một hình học conformal: sự kiện xuyên, giao diện, và hàm tương quan, trong giới hạn scaling, biến đổi hiệp biến dưới ánh xạ conformal của miền. Biến tiên đoán đó thành toán học đòi hỏi các quan sát được (observable) vẫn kiểm soát được khi bước lưới tiến về không. Smirnov cung cấp các quan sát được đó cho **percolation đỉnh tới hạn trên lưới tam giác** (2001) và, cùng cộng sự, cho **mô hình Ising phẳng**. Ngôn ngữ liên tục của các giao diện là **Schramm–Loewner evolution (SLE)**, do Oded Schramm khởi tạo và do Gregory Lawler, Schramm, và Wendelin Werner phát triển—xem [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Các định lý chuyển pha sau này của Hugo Duminil-Copin nằm cùng cảnh quan: [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

Bài này dành cho người đã gặp giải tích phức và xác suất sơ cấp, muốn nắm **kiến trúc** huy chương 2010: công thức Cardy nói gì, vì sao lưới tam giác là thiết yếu, bất biến conformal của Ising nghĩa là gì ở mức fermion, và những phát biểu láng giềng nào vẫn mở.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu, ở mức khẩu hiệu, **Bernoulli percolation** là gì, và phân biệt percolation **đỉnh** (site) với percolation **cạnh** (bond).
- Giải thích vì sao tham số **tới hạn** $$p_c$$ là nơi đáng tìm giới hạn scaling không tầm thường.
- Mô tả **công thức xuyên Cardy** như tiên đoán xác suất một cluster tới hạn xuyên một hình chữ nhật conformal, và gọi định lý Smirnov 2001 là chứng minh tiên đoán đó cho **percolation đỉnh tới hạn trên lưới tam giác**.
- Giải thích vì sao **không** khẳng định cùng kết quả cho mọi lưới, và đặc biệt không cho **percolation cạnh trên lưới vuông**.
- Đặt **SLE** làm ngôn ngữ giới hạn scaling của giao diện, ghi công Schramm về định nghĩa và Lawler–Schramm–Werner về lý thuyết giải tích.
- Phân biệt định lý percolation với bất biến conformal **Ising phẳng** sau đó (Smirnov; Chelkak–Smirnov và cộng sự).
- Gán công lao cẩn thận; tránh câu hype “Smirnov đã giải xong vật lý thống kê 2D.”

**Kiến thức nền.** Hàm holomorph và ánh xạ conformal của miền phẳng ở mức khóa giải tích phức thứ nhất; biến ngẫu nhiên Bernoulli và ý tưởng giới hạn scaling (bước lưới $$\delta\to 0$$); khác biệt giữa mô hình rời rạc và quá trình liên tục. Không cần khóa SLE trước.

**Liên kết seminar.** LO1 / LO4 (tiên đoán vật lý thành định lý gắn một lưới; mô hình rời rạc ↔ hình học conformal liên tục). Ghép [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) cho ngôn ngữ đường cong, và [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) cho các kết quả sắc về chuyển pha.

---

## 1. Vì sao vật lý thống kê muốn bất biến conformal

Một cấu hình **percolation** trên đồ thị là tô màu ngẫu nhiên các đỉnh (site) hoặc cạnh (bond) thành mở hoặc đóng, độc lập, với xác suất $$p$$ là mở. Câu hỏi hình học đơn giản nhất: các đỉnh mở có tạo đường nối hai cung biên không. Với $$p$$ cực trị câu trả lời nhàm chán; nhiều lưới hai chiều có **giá trị tới hạn** $$p_c$$ tại đó xác suất xuyên của một hình chữ nhật lớn nằm cách đều cả $$0$$ lẫn $$1$$.

Nếu đổi tỉ lệ về bước $$\delta\to 0$$, hình học cluster được kỳ vọng hội tụ tới một đối tượng liên tục ngẫu nhiên. Lý thuyết trường conformal hai chiều gợi ý điều mạnh hơn: giới hạn phải **bất biến conformal**. John Cardy, bằng phương pháp CFT không chặt, đưa ra công thức tường minh cho xác suất xuyên giới hạn của một hình chữ nhật conformal (*J. Phys. A*, 1992). Lennart Carleson nhận thấy công thức trở nên đơn giản trên tam giác đều. Khó không phải viết công thức; khó là chứng minh một mô hình lattice cụ thể hội tụ và giới hạn biến đổi như Cardy tiên đoán.

---

## 2. Percolation đỉnh trên lưới tam giác

Định lý Smirnov 2001 nói về **percolation đỉnh tới hạn trên lưới tam giác** $$\mathbb{T}$$, với $$p=1/2$$. Note *Comptes Rendus* (Smirnov, *C. R. Acad. Sci. Paris* 333 (2001); bản dài hơn arXiv:0909.4499) đưa vào các bất biến conformal điều hòa rời rạc xây từ xác suất xuyên và đổi màu. Các hàm đó xấp xỉ điều hòa và thỏa hệ Cauchy–Riemann rời rạc nhờ **đẳng thức đổi màu** đặc thù của $$\mathbb{T}$$. Chúng hội tụ tới các hàm holomorph tường minh của một bài toán Dirichlet–Neumann, cho bất biến conformal của xuyên và **công thức Cardy**. Dạng Carleson: trên tam giác đều cạnh một, xác suất xuyên giới hạn từ một cạnh tới một điểm đối diện là hàm tuyến tính theo vị trí.

**Độ chính xác không được làm mờ.** Lập luận dùng đối xứng bậc ba của $$\mathbb{T}$$ một cách thiết yếu. Đây là định lý về **mô hình lưới này**, không phải định lý về “percolation trên mặt phẳng” theo nghĩa đầy đủ. Đặc biệt, **percolation cạnh tới hạn trên lưới vuông**—mô hình percolation phẳng nổi tiếng còn lại—vẫn là bài toán mở nổi tiếng ở cùng mức bất biến conformal. Tính phổ quát được tin tưởng, và có nhiều tiến bộ từng phần, nhưng khóa học này không giả vờ Smirnov 2001 đã khép mọi lưới.

---

## 3. Từ xuyên tới đường cong: SLE như ngôn ngữ giới hạn

Xác suất xuyên là bất biến conformal vô hướng. Đối tượng giàu hơn là **giao diện**: đường tách mở khỏi đóng, hoặc đường thám sát theo biên cluster. Khi xuyên đã được kiểm soát, người ta hỏi các đường ngẫu nhiên này có hội tụ theo luật tới một quá trình liên tục không.

**Schramm–Loewner evolution** $$\mathrm{SLE}_\kappa$$, do Oded Schramm đưa vào năm 2000 (*Israel J. Math.* 118, “Scaling limits of loop-erased random walks and uniform spanning trees”), là họ một tham số các bao (hull) ngẫu nhiên tăng dần trong một miền phẳng, sinh bằng cách lái phương trình Loewner bằng chuyển động Brown phương sai $$\kappa$$. Schramm chứng minh: nếu một giới hạn scaling chordal tồn tại và bất biến conformal (cùng tính Markov hạn chế), thì nó phải là $$\mathrm{SLE}_\kappa$$ với một $$\kappa$$ nào đó. Với percolation, giá trị tiên đoán là $$\kappa=6$$.

Lawler, Schramm, và Werner phát triển lý thuyết giải tích của SLE: tính chất hạn chế (restriction), số mũ giao và disconnect, và hình học chuyển động Brown hai chiều. Sự phát triển đó là nội dung Huy chương Fields 2006 của Werner và **không** phải citation của Smirnov; đó là ngôn ngữ để đọc các định lý lattice của Smirnov. Các công trình sau (đáng chú ý Camia–Newman, và các bài về giao diện) dùng định lý xuyên của Smirnov làm cửa để đồng nhất đường thám sát percolation với $$\mathrm{SLE}_6$$. Trong seminar, giữ phân công:

| Đóng góp | Ai, ở mức khẩu hiệu |
|----------|---------------------|
| Khởi tạo SLE | Schramm (2000) |
| Lý thuyết giải tích SLE; frontier Brownian; số mũ | Lawler–Schramm–Werner |
| Cardy + bất biến conformal cho percolation đỉnh tam giác | Smirnov (2001) |
| Quan sát được / giao diện Ising phẳng | Smirnov; Chelkak–Smirnov và cộng sự sau đó |

---

## 4. Mô hình Ising phẳng

**Mô hình Ising** gán spin $$\pm 1$$ cho các đỉnh của một đồ thị phẳng, với trọng Boltzmann ưu tiên láng giềng cùng hướng. Ở nhiệt độ tới hạn, mô hình được kỳ vọng có giới hạn scaling bất biến conformal—một trong những thành công CFT sớm nhất về mặt vật lý (nghiệm đúng Onsager đã cho năng lượng tự do 2D; bất biến conformal của toàn bộ hình học là khẳng định khác, khó hơn).

Smirnov đưa vào **fermion holomorph rời rạc** cho Ising tới hạn (xem “Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model,” *Ann. of Math.* 172 (2010)). Cùng Dmitry Chelkak, ông chứng minh các quan sát được fermion này có giới hạn scaling phổ quát, bất biến conformal trên một họ lớn các đồ thị phẳng, không chỉ một lưới: Chelkak–Smirnov, “Universality in the 2D Ising model and conformal invariance of fermionic observables,” *Invent. Math.* 189 (2012), arXiv:0910.2045. Công trình sau với Chelkak, Duminil-Copin, Hongler, Kemppainen, và những người khác đồng nhất giao diện Ising với đường SLE (đặc biệt $$\mathrm{SLE}_3$$ cho giao diện spin, trong thiết lập thích hợp).

Hai điểm sư phạm. Thứ nhất, “bất biến conformal của mô hình Ising” trong citation huy chương chỉ chương trình quan sát được và giới hạn này, không phải nghiệm 1944 của Onsager cho hàm phân hoạch. Thứ hai, lý thuyết Ising theo một số nghĩa **phổ quát hơn** định lý percolation 2001: khung Chelkak–Smirnov phủ một lớp rộng đồ thị isoradial, trong khi định lý Cardy percolation vẫn gắn lưới tam giác.

---

## 5. Thiết kế chứng minh, và vì sao có Fields

Cả hai câu chuyện đều invent một quan sát được rời rạc $$F_\delta$$ mã hóa sự kiện (xuyên, spin, giao diện), thỏa hệ gần-holomorph, và có điều kiện biên chuyển thành bài toán Dirichlet hoặc Riemann–Hilbert liên tục. Tính tiền compact cho giới hạn theo dãy con; tính duy nhất của bài toán liên tục nhận diện giới hạn; hiệp biến conformal được thừa hưởng. Với percolation tam giác, đẳng thức đổi màu đồng nhất hai sự kiện ba nhánh và cung cấp Cauchy–Riemann rời rạc. Với Ising, quan sát được là fermion và holomorph rời rạc đến từ tính integrability. Hai phương pháp là họ hàng, không phải bản sao: lưới phải cho một đẳng thức đủ mạnh để khép hệ—vì thế một lưới có thể rơi, lưới khác vẫn mở.

Huy chương không phải “ông đoán đúng công thức Cardy.” Một tiên đoán vật lý thành định lý với luật xuyên tường minh; các quan sát được holomorph rời rạc tổ chức lại cơ học thống kê 2D; và khi chúng bất biến conformal, lý thuyết đường cong Schramm–Lawler–Werner có thể gắn $$\mathrm{SLE}_6$$ hoặc $$\mathrm{SLE}_3$$ với một mô hình lattice có tên. Lớp 2010 còn có Lindenstrauss, Ngô, và Villani—xem [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/) cho citation động học từ cùng đại hội.

---

## 6. Điều vẫn mở, nói thật

Percolation cạnh tới hạn trên lưới vuông, và bất biến conformal của percolation trên các lưới phẳng tổng quát, vẫn chưa là định lý theo nghĩa Smirnov 2001. Nhiều số mũ và sự kiện arm đã biết cho mô hình đỉnh tam giác một khi có bất biến conformal; các phát biểu tương ứng trên lưới khác thường còn là giả thuyết hoặc chỉ chuyển được một phần. Đường tự tránh (self-avoiding walk), với giới hạn scaling tiên đoán $$\mathrm{SLE}_{8/3}$$, là láng giềng nổi tiếng **không** phải định lý của Smirnov. Chân dung Duminil-Copin xử lý độ sắc của chuyển pha và các kết quả lattice bổ sung—không lặp lại—định lý bất biến conformal 2001.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Smirnov chứng minh bất biến conformal của percolation trên mọi lưới.” | Định lý 2001 là cho **percolation đỉnh tới hạn trên lưới tam giác**. Percolation cạnh lưới vuông là trường hợp còn lại nổi tiếng. |
| “Cardy đã chứng minh công thức xuyên.” | Cardy suy ra bằng CFT không chặt; Smirnov chứng minh cho percolation đỉnh tam giác. |
| “SLE do Werner (hoặc Smirnov) invent.” | SLE do **Schramm** đưa vào (2000). Fields của Werner là phát triển SLE và hình học Brownian 2D, chủ yếu với Lawler và Schramm. |
| “Huy chương 2010 chỉ về percolation.” | Citation IMU nêu percolation **và** mô hình Ising phẳng. |
| “Nghiệm Onsager trùng bất biến conformal của Ising.” | Onsager tính năng lượng tự do 2D (1944). Bất biến conformal của quan sát được và giao diện là phát biểu hình học sau đó. |
| “Có SLE thì mọi mô hình 2D đã xong.” | SLE là luật giới hạn ứng viên. Đồng nhất một mô hình lattice với một $$\kappa$$ là định lý riêng, thường vẫn mở. |

---

## Bài tập

1. Trong hai câu, phân biệt percolation **đỉnh** và percolation **cạnh**. Vì sao một chứng minh dùng đẳng thức đổi màu trên tam giác có thể không chép được sang lưới vuông?
2. **Xác suất xuyên** của một hình chữ nhật conformal là gì? Vì sao $$p_c$$ là nơi duy nhất người ta kỳ vọng giới hạn không tầm thường, độc lập bước lưới, nằm trong $$(0,1)$$?
3. Nêu công thức Cardy ở mức khẩu hiệu, và viết một câu về dạng tam giác đều của Carleson.
4. Luyện gán công: viết cho **Schramm**, **Lawler–Schramm–Werner**, và **Smirnov** mỗi người một câu có thể xuất hiện trong báo cáo phản biện.
5. Lướt abstract Chelkak–Smirnov (arXiv:0910.2045). Quan sát được là gì, và theo nghĩa nào kết quả “phổ quát” hơn Smirnov 2001?
6. Vì sao “giao diện hội tụ tới $$\mathrm{SLE}_6$$” mạnh hơn “xác suất xuyên hội tụ tới công thức Cardy”? Ở mức khẩu hiệu, cần thêm công việc compact hoặc nhận diện nào?
7. **Luyện độ chính xác.** Viết lại câu phổ thông “Smirnov chỉ ra chuyển pha 2D là conformal” thành hai câu chính xác cho khóa học này.
8. **Seminar.** So huy chương này với [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/): ai cung cấp quá trình đường cong, ai cung cấp mô hình lattice hội tụ tới nó?

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

- Đọc một survey về lập luận đổi màu trước note *Comptes Rendus*; sau [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), viết nửa trang về thứ tự tiên đề SLE → Cardy → đồng nhất với $$\mathrm{SLE}_6$$.
- Tùy chọn seminar: một trang “điều vẫn mở trong percolation 2D” **không** khẳng định tính phổ quát là định lý.
