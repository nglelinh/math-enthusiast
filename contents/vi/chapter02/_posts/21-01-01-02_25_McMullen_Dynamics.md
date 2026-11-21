---
layout: post
title: "Động lực chỉnh hình và hình học Teichmüller của McMullen (Huy chương Fields 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Curtis T. McMullen** nhận **Huy chương Fields 1998** tại ICM Berlin. Khác với các năm 1990 và 1994, năm 1998 có lời trao giải ngắn chính thức, và khóa học dùng nguyên văn:

> For his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.

*Tạm dịch: vì những đóng góp cho lý thuyết động lực học chỉnh hình và hình học hóa đa tạp ba chiều, trong đó có chứng minh giả thuyết Bers về tính trù mật của các điểm cusp trên biên không gian Teichmüller, và giả thuyết hàm theta của Kra.*

Bài này dành cho người đã biết mặt Riemann và phép lặp hàm phức ở mức tập Julia của đa thức bậc hai, và muốn thấy **mối liên hệ** giữa các hình ảnh đó với lý thuyết Teichmüller và chương trình Thurston về đa tạp hyperbolic ba chiều. Bài **không** nói McMullen đã chứng minh trọn vẹn giả thuyết hình học hóa hay giả thuyết Poincaré. Việc hoàn tất chương trình Hamilton–Thurston là công của [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Công trình về đa tạp ba chiều của McMullen nằm *bên trong* hướng nghiên cứu của Thurston: tái chuẩn hóa, tính cứng, và cấu trúc hyperbolic trên các đa tạp phân thớ trên đường tròn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại lời trao giải chính thức năm 1998 và nêu tên hai định lý được ghi rõ (tính trù mật của cusp theo Bers; giả thuyết theta của Kra).
- Phác họa **động lực học chỉnh hình** của một ánh xạ hữu tỷ: tập Julia và tập Fatou, và vì sao **tái chuẩn hóa** (Sullivan, Douady–Hubbard, rồi McMullen) là cả một bộ công cụ chứ không phải một công thức.
- Giải thích ngắn gọn **không gian Teichmüller** của một mặt là gì, và một **cusp** trên biên Bers là gì.
- Phân biệt đóng góp của McMullen cho **chương trình hình học hóa của Thurston** với chứng minh đầy đủ giả thuyết hình học hóa của Perelman.
- Liên hệ với [không gian moduli của Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), một hướng về moduli và động lực học ra đời sau. McMullen là người hướng dẫn luận án của Mirzakhani; đây là sự thật tiểu sử, không thay thế cho các định lý của bà.
- Phát biểu chính xác: huy chương ghi nhận một *khối công trình* có hai giả thuyết được nêu tên, chứ không phải "McMullen đã phân loại mọi tập Julia".

**Kiến thức nền.** Hàm chỉnh hình trên $$\mathbb{C}$$ và mặt cầu Riemann $$\widehat{\mathbb{C}}$$; khái niệm mặt Riemann compact giống $$g\ge 2$$ với mêtric hyperbolic; quen với việc lặp một ánh xạ nhiều lần. Không cần học trước nhóm Klein (Kleinian groups).

**Liên kết với các bài khác.** Bài này minh họa một chương trình nghiên cứu tổ chức lại cả hình học lẫn động lực học. Các bài hình học liên quan: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Những tên tuổi chính của động lực học phức: Fatou, Julia, Sullivan, Douady–Hubbard, Thurston, Yoccoz.

---

## 1. Động lực học chỉnh hình: ánh xạ, tập Julia, tập Fatou, tái chuẩn hóa

Một **ánh xạ hữu tỷ** $$f:\widehat{\mathbb{C}}\to\widehat{\mathbb{C}}$$ là một ánh xạ chỉnh hình từ mặt cầu Riemann vào chính nó, tức là thương của hai đa thức. Lặp ánh xạ cho ta một hệ động lực rời rạc $$z\mapsto f(z)\mapsto f^{\circ 2}(z)\mapsto\cdots$$. **Tập Fatou** là tập mở gồm các điểm mà quanh đó họ các lặp là đồng liên tục (họ chuẩn tắc). **Tập Julia** $$J(f)$$ là phần bù, thường là một fractal, nơi các quỹ đạo xuất phát gần nhau tách xa nhau. Các đa thức bậc hai $$z\mapsto z^2+c$$ được sắp xếp thành **tập Mandelbrot** trên mặt phẳng tham số. Nhờ **Douady–Hubbard**, ta có một bộ từ điển giữa dữ liệu tổ hợp và các thành phần hyperbolic của tập này.

**Tái chuẩn hóa** hỏi điều gì xảy ra khi một mảnh nhỏ của hệ động lực trông giống bản sao của một ánh xạ đơn giản hơn. Trường hợp cổ điển: một lặp của ánh xạ, thu hẹp vào một lân cận của điểm tới hạn, là ánh xạ **dạng bậc hai** (quadratic-like) theo nghĩa Douady–Hubbard. **Sullivan** viết lại nhiều phần của lý thuyết bằng ngôn ngữ phân lá mặt Riemann (Riemann surface laminations) và động lực học đo được. Cuốn *Complex Dynamics and Renormalization* của McMullen (Annals of Mathematics Studies **135**, 1994) nghiên cứu các đa thức bậc hai tái chuẩn hóa được vô hạn lần, tính cứng, và hình học của các tháp ánh xạ dạng bậc hai. Bài giảng tại ICM 1998 của Steve Smale về công trình của McMullen nhấn mạnh rằng, với bài toán trù mật của đa thức hyperbolic bậc hai, trường hợp tái chuẩn hóa hữu hạn lần đã được **Yoccoz** giải quyết; phân tích của McMullen nhắm vào các điểm tái chuẩn hóa vô hạn lần trong tập Mandelbrot.

**Tóm tắt.** Động lực học chỉnh hình không chỉ là những bức tranh tập Julia. Đó là một lý thuyết về tính cứng: khi hai ánh xạ giống nhau về tổ hợp, các giới hạn hình học và tính giãn thường buộc chúng phải trùng nhau, hoặc buộc tập Julia liên thông địa phương, hoặc buộc các ánh xạ hyperbolic trù mật trong một họ tham số.

Luận án tiến sĩ của McMullen (Harvard, 1985, người hướng dẫn **Dennis Sullivan**) đã thuộc lĩnh vực này: họ các ánh xạ hữu tỷ và các thuật toán lặp để tìm nghiệm đa thức. Lời trao giải Fields nói về lý thuyết rộng hơn, không phải một thuật toán cụ thể.

---

## 2. Không gian Teichmüller và biên Bers

Gọi $$S$$ là một mặt đóng định hướng giống $$g\ge 2$$ (hoặc một mặt hyperbolic kiểu hữu hạn). **Không gian Teichmüller** $$\mathcal{T}(S)$$ tham số hóa các cấu trúc hyperbolic có đánh dấu, hay tương đương, các mặt Riemann có đánh dấu, trên mặt tôpô $$S$$. Đó là một ô (cell) hữu hạn chiều (chiều thực $$6g-6$$ với mặt đóng giống $$g$$). **Nhóm lớp ánh xạ** (mapping class group) tác động lên nó, và không gian thương là không gian moduli; đó là bối cảnh của [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

**Bers** nhúng không gian Teichmüller thành một miền bị chặn trong không gian các vi phân bậc hai chỉnh hình (phép nhúng Bers). **Biên Bers** là biên của ảnh phép nhúng đó. Các điểm trên biên ứng với các nhóm Klein (thường là suy biến): giới hạn của các biểu diễn tựa Fuchs (quasifuchsian) khi một số đường cong trên mặt bị thắt lại (pinch). Một **cusp cực đại** là một giới hạn hữu hạn hình học, trong đó một hệ cực đại các đường cong đóng đơn rời nhau đã bị thắt lại thành các cusp hạng một.

**Giả thuyết Bers**, ở dạng McMullen chứng minh, nói rằng **các cusp trù mật** trên biên này: các cusp cực đại trù mật trong biên Bers của không gian Teichmüller. Bài "Cusps are dense" của McMullen, *Ann. of Math.* **133** (1991), chứng minh điều đó. Lập luận dùng một đánh giá về tác động đại số của một biến dạng tựa bảo giác có chuẩn đơn vị, đặt trên phần mỏng của mặt. Nói cách khác, việc thắt một đường cong không phải là thao tác quá tinh tế; có thể xấp xỉ nó một cách trù mật từ bên trong.

**Tóm tắt.** "Mép" của không gian các mặt hyperbolic được phủ trù mật bởi những mặt đã bị thắt dọc theo các đường cong cho tới khi các đường cong đó trở thành cusp. Trên biên, sự suy biến không hiếm mà là điển hình.

Đây là một định lý về *biên của không gian Teichmüller*, không phải sự phân loại mọi đa tạp ba chiều.

---

## 3. Giả thuyết hàm theta của Kra

Một phủ các mặt Riemann hyperbolic $$Y\to X$$ cảm sinh một phép nhúng giữa các không gian Teichmüller $$\mathcal{T}(X)\hookrightarrow\mathcal{T}(Y)$$. Phép nhúng đó là đẳng cự hay là co đối với mêtric Teichmüller tùy thuộc vào phủ. McMullen chứng minh rằng phép nhúng là đẳng cự nếu phủ **khả trung bình** (amenable), và co chặt nếu ngược lại (*Invent. Math.* **97**, 1989).

Một trường hợp cổ điển đặc biệt là toán tử chuỗi Poincaré $$\Theta$$, lấy trung bình một vi phân bậc hai chỉnh hình trên đĩa để được một vi phân trên một mặt kiểu hữu hạn. **Giả thuyết hàm theta của Kra** khẳng định toán tử này co chặt: $$\|\Theta\|<1$$ đối với chuỗi Poincaré cổ điển. McMullen chứng minh giả thuyết này như một hệ quả của tiêu chuẩn khả trung bình.

Lời trao giải nêu định lý này vì đây là một kết quả giải tích sắc nét có hệ quả hình học: các đánh giá co được dùng trong các công trình sau về phép lặp trên không gian Teichmüller và về tính cứng của cấu trúc hyperbolic. Bài giảng ICM của Smale ghi rằng, với công cụ từ giả thuyết theta, McMullen đã đóng góp đáng kể cho chương trình của Thurston nhằm đặt mêtric hyperbolic lên một lớp lớn các đa tạp ba chiều.

---

## 4. Chương trình hình học hóa, không phải định lý của Perelman

**Giả thuyết hình học hóa của Thurston** đề xuất rằng mọi đa tạp ba chiều đóng đều cắt được thành các mảnh, mỗi mảnh mang một trong tám hình học thuần nhất; các mảnh hyperbolic là phức tạp nhất. Thurston chứng minh những phần lớn của chương trình (đặc biệt cho đa tạp Haken). **Perelman** chứng minh toàn bộ giả thuyết bằng dòng Ricci có phẫu thuật, và từ đó suy ra giả thuyết Poincaré; xem [bài Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

Đóng góp của McMullen thuộc loại khác. Cuốn sách năm 1996 *Renormalization and 3-Manifolds Which Fiber over the Circle* (Annals of Mathematics Studies **142**) trình bày song song hai cách xây dựng: điểm bất động của phép tái chuẩn hóa trong động lực học phức, và cấu trúc hyperbolic trên các đa tạp ba chiều **phân thớ trên đường tròn**. Cả hai được nghiên cứu bằng giới hạn hình học và tính cứng. Ông chỉ ra rằng các đa tạp hyperbolic mở có tính "không uốn được" (inflexible) theo một nghĩa định lượng, bổ sung cho định lý cứng Mostow. Đó là nội dung cụm "geometrization of three-manifolds" trong lời trao giải: một cách tiếp cận bằng tái chuẩn hóa và tính cứng trong chương trình Thurston, đặc biệt cho các đa tạp phân thớ. Nó không có nghĩa McMullen đã hoàn tất toàn bộ giả thuyết hình học hóa.

**Câu phát biểu chính xác cho khóa học.** McMullen làm việc *trong* chương trình hình học hóa; Perelman *hoàn tất* giả thuyết hình học hóa (và giả thuyết Poincaré). Hai câu này không mâu thuẫn nhau.

---

## 5. Vì sao hai giả thuyết được nêu tên lại đi cùng nhau

Tính trù mật của Bers và tính co của Kra trông như giải tích trên không gian Teichmüller. Động lực học chỉnh hình trông như phép lặp trên mặt cầu. Điểm chung là **tính cứng của các hệ động lực bảo giác**, dù hệ đó là một ánh xạ hữu tỷ hay một nhóm Klein (một nhóm con rời rạc của $$\mathrm{PSL}(2,\mathbb{C})$$, tác động lên mặt cầu Riemann và lên không gian hyperbolic ba chiều). Bộ từ điển của Sullivan giữa hai chủ đề là nền tảng chung. Các định lý của McMullen là những đánh giá co, kết quả trù mật và giới hạn hình học cụ thể, giúp bộ từ điển đó thực sự sinh ra chứng minh.

Cùng cách nhìn này về sau xuất hiện trong công trình của các học trò McMullen, trong đó có **Maryam Mirzakhani**, về không gian moduli, động lực học và mặt hyperbolic. Có thể nhắc điều đó như một dòng truyền thừa, rồi giới thiệu người đọc tới [các định lý riêng của Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

---

## 6. Vì sao là Huy chương Fields

1. **Những bài toán có tên, tồn tại lâu.** Tính trù mật của cusp trên biên Bers và bất đẳng thức $$\|\Theta\|<1$$ của Kra là những mục tiêu được công nhận rộng rãi; chứng minh chúng xứng đáng được ghi vào lời trao giải.
2. **Một bộ từ điển tính toán được.** Tái chuẩn hóa không chỉ là triết lý. Các cuốn sách của McMullen biến nó thành những đánh giá chuyển thông tin qua lại giữa ánh xạ dạng bậc hai và đa tạp hyperbolic ba chiều.
3. **Tính trung tâm.** Động lực học phức, lý thuyết Teichmüller và hình học đa tạp ba chiều đều là những lĩnh vực lớn; công trình cho thấy chúng dùng chung cơ chế compact và tính cứng.

Những người cùng nhận Huy chương Fields năm 1998 là **Borcherds**, **Gowers** và **Kontsevich**. Cùng một kỳ ICM đã vinh danh moonshine, tổ hợp trong không gian Banach, lượng tử hóa biến dạng, và động lực học bảo giác.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "McMullen đã chứng minh hình học hóa / Poincaré." | Hình học hóa đầy đủ là của Perelman. McMullen đóng góp trong chương trình Thurston (hyperbolic hóa đa tạp phân thớ / tái chuẩn hóa). |
| "Cusp trù mật nghĩa là mọi mặt Riemann đều có cusp." | Định lý nói về *biên Bers* của không gian Teichmüller, không nói về một mặt trơn điển hình ở bên trong. |
| "Không gian Teichmüller là không gian moduli." | Không gian Teichmüller giữ thông tin đánh dấu; không gian moduli là thương theo nhóm lớp ánh xạ. |
| "Tập Julia = tập Mandelbrot." | Tập Julia nằm trên mặt phẳng động lực của một ánh xạ; tập Mandelbrot nằm trên mặt phẳng tham số của cả một họ. |
| "Tái chuẩn hóa chỉ là phóng to một bức tranh." | Đó là phép dựng một ánh xạ mới từ ánh xạ dạng bậc hai, kèm một lý thuyết về tính cứng. |
| "Huy chương chỉ vì Bers + Kra." | Đó là hai mục được nêu tên; lời trao giải còn nhắc tới động lực học chỉnh hình và hình học hóa đa tạp ba chiều. |
| "McMullen đã phân loại mọi ánh xạ hữu tỷ." | Không. Công trình nói về tính cứng, tính trù mật và tái chuẩn hóa, không phải liệt kê các lớp liên hợp. |

---

## Bài tập

1. Định nghĩa tập Fatou và tập Julia của một ánh xạ hữu tỷ trong hai câu. Vì sao $$J(f)$$ thường là nơi "đáng chú ý" khi nghiên cứu tính cứng?
2. Ánh xạ dạng bậc hai (quadratic-like) là gì, theo cách nói của Douady–Hubbard? Vì sao phép tái chuẩn hóa tạo ra một ánh xạ như vậy?
3. Phát biểu giả thuyết trù mật cusp của Bers trong một câu cẩn thận, có các từ **biên** và **Teichmüller**.
4. Giả thuyết Kra là bất đẳng thức về chuẩn toán tử $$\|\Theta\|<1$$. Vì sao một phép *co chặt* trên không gian Teichmüller có thể hữu ích về mặt hình học?
5. Viết bốn câu mà một bạn học có thể dùng để phân biệt McMullen với Perelman về chuyện "hình học hóa".
6. Đọc lại lời trao giải chính thức. Hai giả thuyết nào được nêu tên? Hai chủ đề lớn nào bao quanh chúng?
7. **Mở rộng.** So sánh không gian Teichmüller ở đây với không gian moduli trong [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/): thông tin nào được giữ, thông tin nào bị bỏ, và vì sao có thể nghiên cứu động lực học trên cả hai?

---

## Liên kết

- Trang Huy chương Fields của IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Huy chương Fields 1998: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998)
- Wikipedia, Curtis T. McMullen: [https://en.wikipedia.org/wiki/Curtis_T._McMullen](https://en.wikipedia.org/wiki/Curtis_T._McMullen)
- Trang Harvard của McMullen: [https://people.math.harvard.edu/~ctm/](https://people.math.harvard.edu/~ctm/)
- Khóa học: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)
- Tìm arXiv, McMullen dynamics: [https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all](https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all)

---

## Tài liệu tham khảo

1. Citation chính thức Fields Medal 1998 cho C. T. McMullen (IMU / ICM Berlin); xem thêm diễn từ của Yuri Manin với tư cách chủ tịch ủy ban.
2. **S. Smale**, “The work of Curtis T. McMullen,” *Doc. Math.*, Extra Vol. ICM 1998.
3. **C. T. McMullen**, “Cusps are dense,” *Ann. of Math.* **133** (1991).
4. **C. T. McMullen**, “Amenability, Poincaré series and quasiconformal maps,” *Invent. Math.* **97** (1989) (giả thuyết theta của Kra).
5. **C. T. McMullen**, *Complex Dynamics and Renormalization*, Ann. of Math. Studies **135**, Princeton, 1994.
6. **C. T. McMullen**, *Renormalization and 3-Manifolds Which Fiber over the Circle*, Ann. of Math. Studies **142**, Princeton, 1996.
7. Nền: Douady–Hubbard về ánh xạ quadratic-like và tập Mandelbrot; Sullivan về phân thớ mặt Riemann và từ điển với nhóm Kleinian; Thurston về hình học hóa (các trường hợp Haken / phân thớ).
8. Khóa học: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

---

## Hướng đi tiếp

- Đọc bài giới thiệu ngắn của Smale tại ICM trước khi đọc hai cuốn sách năm 1994 và 1996.
- So sánh biên Bers với biên của tập Mandelbrot: cả hai được dự đoán là có cấu trúc phân lá (Thurston; Douady–Hubbard). Kết quả trù mật cusp của McMullen ủng hộ một phía của sự tương tự này.
- Bài tập thêm: lập một "từ điển" một trang gồm ba cặp khái niệm song song (ánh xạ hữu tỷ / nhóm Klein; tập Julia / tập giới hạn; tái chuẩn hóa / hyperbolic hóa đa tạp phân thớ), nhưng không khẳng định rằng từ điển này là một tương đương chặt chẽ.

## Video tham khảo

- **Xem trước**: [Curtis McMullen: Manifolds, topology and dynamics](https://www.youtube.com/watch?v=g0fQDrV-UuE) (The Abel Prize, tiếng Anh). McMullen nói về đa tạp, tôpô và động lực học ở mức đại chúng. Phù hợp để làm quen với các chủ đề trước khi đọc bài.
- [Planes in number theory, geometry and dynamics: C. McMullen](https://www.youtube.com/watch?v=hlDDHnk5aRU) (Fields Institute, tiếng Anh). Bài giảng về vai trò của các mặt phẳng trong lý thuyết số, hình học và động lực học. Thuộc giai đoạn sau giải Fields, nên xem sau khi đã đọc xong bài.
- [Dynamics on K3 Surfaces - Curtis McMullen](https://www.youtube.com/watch?v=gWTi1xvGMb8) (Stony Brook Mathematics, tiếng Anh). Bài giảng về động lực học trên mặt K3, một hướng nghiên cứu khác của McMullen. Dùng làm góc nhìn bổ sung, không thuộc lời trao giải 1998.
