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

**Curtis T. McMullen** nhận **Huy chương Fields 1998** tại ICM Berlin. Khác với các huy chương 1990 và 1994, năm 1998 có citation ngắn chính thức, và khóa học này dùng nguyên văn:

> For his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.

Bài này dành cho người đã gặp mặt Riemann và iteration phức ở mức tập Julia của đa thức bậc hai, muốn thấy **kiến trúc** nối những bức tranh đó với lý thuyết Teichmüller và với chương trình Thurston về đa tạp hyperbolic ba chiều. Bài **không** nói McMullen đã chứng minh hình học hóa đầy đủ hay giả thuyết Poincaré—đó là phần hoàn tất chương trình Hamilton–Thurston của [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Công trình 3-đa tạp của McMullen sống *trong* văn hóa Thurston: tái chuẩn hóa, cứng nhắc, và cấu trúc hyperbolic trên các đa tạp phân thớ trên đường tròn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu citation chính thức 1998 và gọi tên hai định lý được nêu tường minh (mật độ cusp của Bers; giả thuyết theta của Kra).
- Phác **động lực chỉnh hình** của một ánh xạ hữu tỷ: tập Julia đối với tập Fatou, và vì sao **tái chuẩn hóa** (Sullivan, Douady–Hubbard, rồi McMullen) là một máy chứ không phải một công thức.
- Giải thích, ở mức khẩu hiệu, **không gian Teichmüller** của một mặt và một **cusp** trên biên Bers đang cố trở thành gì.
- Phân biệt đóng góp của McMullen cho **văn hóa hình học hóa Thurston** với chứng minh hình học hóa đầy đủ của Perelman.
- Liên kết chéo [moduli của Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) như một chương moduli-và-động lực sau này (McMullen là người hướng dẫn luận án của Mirzakhani—một sự thật tiểu sử chính xác, không thay thế các định lý của bà).
- Luyện LO6: huy chương là một *khối công trình* với hai giả thuyết được nêu tên, không phải “McMullen đã phân loại mọi tập Julia.”

**Kiến thức nền.** Hàm chỉnh hình trên $$\mathbb{C}$$ và mặt cầu Riemann $$\widehat{\mathbb{C}}$$; ý tưởng mặt Riemann compact giống $$g\ge 2$$ với metric hyperbolic; thoải mái với “iteration” như lặp một ánh xạ. Không giả sử đã học nhóm Kleinian.

**Liên kết seminar.** LO1 (các chương trình tổ chức lại hình học và động lực cùng lúc). Họ hàng hình học: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Phong cảnh động lực phức: Fatou, Julia, Sullivan, Douady–Hubbard, Thurston, Yoccoz.

---

## 1. Động lực chỉnh hình: ánh xạ, Julia, Fatou, tái chuẩn hóa

Một **ánh xạ hữu tỷ** $$f:\widehat{\mathbb{C}}\to\widehat{\mathbb{C}}$$ là tự ánh chỉnh hình của mặt cầu Riemann, tương đương một thương đa thức. Iteration sinh một hệ động lực rời rạc $$z\mapsto f(z)\mapsto f^{\circ 2}(z)\mapsto\cdots$$. **Tập Fatou** là tập mở các điểm có quỹ đạo đẳng liên tục (họ chuẩn); **tập Julia** $$J(f)$$ là phần bù, thường là fractal nơi các quỹ đạo lân cận phân kỳ. Các đa thức bậc hai $$z\mapsto z^2+c$$ được tổ chức thành **tập Mandelbrot** trên mặt phẳng tham số: một từ điển, đặc biệt nhờ **Douady–Hubbard**, giữa dữ liệu tổ hợp và các thành phần hyperbolic.

**Tái chuẩn hóa** hỏi điều gì xảy ra khi một mảnh nhỏ của động lực trông như bản sao của một ánh xạ đơn giản hơn—cổ điển, khi một iterate hạn chế trên lân cận điểm tới hạn là **quadratic-like** theo nghĩa Douady–Hubbard. **Sullivan** viết lại nhiều phần lý thuyết bằng ngôn ngữ phân thớ mặt Riemann và động lực đo được. Cuốn *Complex Dynamics and Renormalization* của McMullen (Annals of Mathematics Studies **135**, 1994) phát triển các đa thức bậc hai tái chuẩn hóa vô hạn lần, tính cứng nhắc, và hình học các tháp ánh xạ quadratic-like. Bài giảng ICM 1998 của Steve Smale về công trình nhấn rằng, đối với mật độ đa thức hyperbolic bậc hai, trường hợp tái chuẩn hóa hữu hạn lần đã được **Yoccoz** xử lý; phân tích của McMullen nhắm các điểm tái chuẩn hóa vô hạn lần trong tập Mandelbrot.

**Khẩu hiệu.** Động lực chỉnh hình không chỉ là tranh tập Julia. Đó là lý thuyết cứng nhắc: khi hai ánh xạ giống nhau về tổ hợp, các giới hạn hình học và sự giãn thường buộc chúng trùng nhau, hoặc buộc tập Julia liên thông địa phương, hoặc buộc hyperbolic trù mật trong một lát tham số.

Luận án tiến sĩ của McMullen (Harvard, 1985, người hướng dẫn **Dennis Sullivan**) đã nằm trong phong cảnh này: họ ánh xạ hữu tỷ và thuật toán tìm nghiệm lặp. Citation Fields gọi lý thuyết rộng hơn, không một thuật toán đơn lẻ.

---

## 2. Không gian Teichmüller và biên Bers

Gọi $$S$$ là mặt định hướng đóng giống $$g\ge 2$$ (hoặc mặt hyperbolic kiểu hữu hạn). **Không gian Teichmüller** $$\mathcal{T}(S)$$ tham số hóa các cấu trúc hyperbolic được đánh dấu—hoặc tương đương các mặt Riemann được đánh dấu—trên mặt tôpô $$S$$. Nó là một tế bào hữu hạn chiều (chiều thực $$6g-6$$ cho mặt đóng giống $$g$$). **Nhóm lớp ánh xạ** tác động, và thương là không gian moduli; đó là bối cảnh của [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

**Bers** nhúng không gian Teichmüller như một miền bị chặn trong một không gian các vi phân toàn phương chỉnh hình (nhúng Bers). **Biên Bers** là biên của nhúng đó. Các điểm trên biên tương ứng với nhóm Kleinian (thường suy biến): giới hạn của biểu diễn quasifuchsian trong đó một số đường cong trên mặt đã bị pinch. Một **cusp cực đại** là giới hạn hữu hạn hình học trong đó một hệ cực đại các đường cong đóng đơn giản rời nhau đã bị pinch thành cusp hạng một.

**Giả thuyết Bers**, dạng McMullen chứng minh, là **các cusp trù mật** trên biên này: cusp cực đại trù mật trong biên Bers của không gian Teichmüller. Bài “Cusps are dense” của McMullen, *Ann. of Math.* **133** (1991), chứng minh mật độ. Lập luận dùng một ước lượng cho hiệu ứng đại số của một biến dạng quasiconformal đơn vị được chống trên phần mỏng của mặt—pinch không phải thao tác vô cùng tinh tế; nó có thể được xấp xỉ từ phía trong một cách trù mật.

**Khẩu hiệu.** “Cạnh” của không gian các mặt hyperbolic đẹp được phủ, một cách trù mật, bởi những mặt đã bị pinch dọc đường cong cho đến khi các đường đó trở thành cusp. Suy biến không hiếm; nó điển hình trên biên.

Đây là định lý về *biên của không gian Teichmüller*, không phải phân loại mọi 3-đa tạp.

---

## 3. Giả thuyết hàm theta của Kra

Một phủ các mặt Riemann hyperbolic $$Y\to X$$ cảm sinh một nhúng các không gian Teichmüller $$\mathcal{T}(X)\hookrightarrow\mathcal{T}(Y)$$. Việc nhúng đó là đẳng cự hay co đối với metric Teichmüller phụ thuộc vào phủ. McMullen chứng minh rằng nhúng là đẳng cự nếu phủ **amenable**, và co chặt nếu không (*Invent. Math.* **97**, 1989).

Một trường hợp cổ điển đặc biệt là toán tử chuỗi Poincaré $$\Theta$$ lấy trung bình một vi phân toàn phương chỉnh hình trên đĩa xuống một mặt kiểu hữu hạn. **Giả thuyết hàm theta của Kra** khẳng định toán tử này là co chặt: $$\|\Theta\|<1$$ đối với chuỗi Poincaré cổ điển. McMullen chứng minh giả thuyết như hệ quả của tiêu chuẩn amenable.

Citation nêu định lý này vì đó là một sự thật giải tích sắc, có hệ quả hình học: các ước lượng co nuôi công trình sau về iteration trên không gian Teichmüller và về tính cứng của cấu trúc hyperbolic. Bài giảng ICM của Smale ghi rằng, được trang bị công trình giả thuyết theta, McMullen có thể đóng góp đáng kể cho chương trình Thurston đặt metric hyperbolic lên một lớp lớn 3-đa tạp.

---

## 4. Văn hóa hình học hóa—không phải định lý của Perelman

**Giả thuyết hình học hóa của Thurston** đề xuất rằng mọi 3-đa tạp đóng phân rã thành các mảnh, mỗi mảnh mang một trong tám hình học thuần nhất; các mảnh hyperbolic là sâu nhất. Thurston chứng minh những phần lớn của chương trình (đặc biệt cho đa tạp Haken). **Perelman** chứng minh toàn bộ giả thuyết qua Ricci flow kèm phẫu thuật, kéo theo giả thuyết Poincaré; xem [bài Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

Đóng góp của McMullen thuộc loài khác. Cuốn 1996 *Renormalization and 3-Manifolds Which Fiber over the Circle* (Annals of Mathematics Studies **142**) trình bày thống nhất hai xây dựng: điểm bất động của tái chuẩn hóa trong động lực phức, và cấu trúc hyperbolic trên 3-đa tạp **phân thớ trên đường tròn**. Cả hai được nghiên cứu qua giới hạn hình học và cứng nhắc. Các đa tạp hyperbolic mở được chỉ ra là inflexible theo nghĩa định lượng bổ sung cho cứng Mostow. Đó là mệnh đề “geometrization of three-manifolds” trong citation: một tiếp cận tái chuẩn hóa-và-cứng trong chương trình Thurston, đặc biệt cho đa tạp phân thớ—không phải tuyên bố McMullen đã khép hình học hóa toàn bộ.

**Câu chính xác cho khóa học này.** McMullen làm việc *trong* chương trình hình học hóa; Perelman *hoàn tất* hình học hóa (và Poincaré). Hai câu đó tương thích.

---

## 5. Vì sao hai giả thuyết được nêu tên ngồi cùng nhau

Mật độ Bers và co của Kra trông như giải tích trên không gian Teichmüller. Động lực chỉnh hình trông như iteration trên mặt cầu. Sự thống nhất là **tính cứng của hệ động lực bảo giác**, dù hệ là ánh xạ hữu tỷ hay nhóm Kleinian (một phân nhóm rời rạc của $$\mathrm{PSL}(2,\mathbb{C})$$ tác động trên mặt cầu Riemann và trên không gian hyperbolic ba chiều). Từ điển của Sullivan giữa hai chủ đề là nền văn hóa; các định lý của McMullen là những phép co, mật độ, và giới hạn hình học cụ thể khiến từ điển sinh ra chứng minh.

Cùng cảm quan sau này xuất hiện trong công trình của học trò McMullen—gồm **Maryam Mirzakhani**—về moduli, động lực, và mặt hyperbolic. Trích điều đó như dòng dõi, rồi gửi người đọc tới [các định lý riêng của Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

---

## 6. Vì sao là Huy chương Fields

1. **Những điểm được nêu tên, mở lâu.** Mật độ cusp trên biên Bers và $$\|\Theta\|<1$$ của Kra là các mục tiêu được thừa nhận; chứng minh chúng đạt mức citation.
2. **Một từ điển biết tính.** Tái chuẩn hóa không chỉ là triết lý. Các cuốn sách của McMullen biến nó thành ước lượng chuyển thông tin giữa ánh xạ quadratic-like và 3-đa tạp hyperbolic.
3. **Tính trung tâm.** Động lực phức, lý thuyết Teichmüller, và hình học 3-đa tạp đã là những lĩnh vực lớn; công trình cho thấy chúng chia sẻ cơ chế compactness và cứng nhắc.

Các đồng giải 1998 gồm **Borcherds**, **Gowers**, và **Kontsevich**—nhắc rằng một ICM có thể cùng lúc tôn vinh moonshine, tổ hợp không gian Banach, và lượng tử hóa biến dạng cạnh động lực bảo giác.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “McMullen đã chứng minh hình học hóa / Poincaré.” | Hình học hóa đầy đủ là Perelman. McMullen đóng góp trong chương trình Thurston (hyperbolization phân thớ / tái chuẩn hóa). |
| “Cusp trù mật nghĩa là mọi mặt Riemann đều có cusp.” | Định lý nói về *biên Bers* của không gian Teichmüller, không về một mặt trơn điển hình ở phần trong. |
| “Không gian Teichmüller là không gian moduli.” | Teichmüller nhớ đánh dấu; moduli lấy thương theo nhóm lớp ánh xạ. |
| “Tập Julia = tập Mandelbrot.” | Julia sống trên mặt phẳng động lực của một ánh xạ; Mandelbrot sống trên mặt phẳng tham số của một họ. |
| “Tái chuẩn hóa chỉ là phóng to một bức tranh.” | Đó là xây dựng ánh xạ trở lại với ánh xạ quadratic-like và một lý thuyết cứng. |
| “Huy chương chỉ là Bers + Kra.” | Đó là các mục được nêu tên; citation còn gọi động lực chỉnh hình và văn hóa hình học hóa 3-đa tạp. |
| “McMullen đã phân loại mọi ánh xạ hữu tỷ.” | Không. Công trình là cứng, mật độ, và tái chuẩn hóa, không phải kiểm kê các lớp liên hợp. |

---

## Bài tập

1. Định nghĩa tập Fatou và Julia của một ánh xạ hữu tỷ trong hai câu. Vì sao $$J(f)$$ thường là tập “thú vị” đối với tính cứng?
2. Ánh xạ quadratic-like là gì (khẩu hiệu Douady–Hubbard)? Vì sao tái chuẩn hóa sinh ra một ánh xạ như thế?
3. Phát biểu giả thuyết mật độ cusp của Bers trong một câu cẩn thận có các từ **biên** và **Teichmüller**.
4. Giả thuyết Kra là bất đẳng thức chuẩn toán tử $$\|\Theta\|<1$$. Vì sao một phép *co chặt* trên không gian Teichmüller có thể hữu ích về hình học?
5. Viết bốn câu một bạn học có thể dùng: McMullen đối với Perelman về “hình học hóa.”
6. Đọc thành tiếng citation chính thức. Hai giả thuyết nào được nêu tên? Hai tiêu đề chủ đề nào bao quanh chúng?
7. **Seminar mở rộng.** So sánh không gian Teichmüller ở đây với không gian moduli trong [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/): cái gì được nhớ, cái gì bị quên, và vì sao động lực có thể sống trên cả hai.

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

- Đọc chân dung ICM ngắn của Smale trước các cuốn 1994/1996.
- So sánh biên Bers với biên tập Mandelbrot: cả hai được phỏng đoán tổ chức bởi phân thớ (Thurston; Douady–Hubbard); mật độ cusp của McMullen chống đỡ một phía của ẩn dụ đó.
- Seminar A3: một trang “từ điển” ba cặp từ song song (ánh xạ hữu tỷ / nhóm Kleinian; tập Julia / tập giới hạn; tái chuẩn hóa / hyperbolization phân thớ)—không tuyên bố từ điển là tương đương phạm trù.
