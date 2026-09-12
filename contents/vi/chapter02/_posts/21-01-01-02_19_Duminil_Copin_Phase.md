---
layout: post
title: "Hugo Duminil-Copin: Chuyển pha trong Vật lý Thống kê (Huy chương Fields 2022)"
chapter: '02'
order: 19
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Hugo Duminil-Copin** nhận **Huy chương Fields 2022** vì đã giải quyết những bài toán tồn tại lâu trong lý thuyết xác suất của các chuyển pha trong vật lý thống kê, đặc biệt ở chiều ba và chiều bốn. Huy chương không đặt tên một định lý dạng đóng duy nhất. Nó đặt tên một phòng thí nghiệm: các mô hình trên lưới mà hành vi vĩ mô đổi đột ngột khi một tham số vượt giá trị tới hạn, cùng một tập chứng minh làm cho những thay đổi ấy sắc nét về mặt toán học ở những chiều mà tính giải được tường minh thất bại.

Bài này dành cho người học đã gặp percolation hoặc mô hình Ising lần đầu và muốn nắm kiến trúc của cơ học thống kê chặt chẽ hiện đại. Bài **không** khẳng định rằng “bất biến conformal của mọi mô hình hai chiều đã xong,” cũng không khẳng định Duminil-Copin làm việc một mình. Nó giải thích khẩu hiệu cẩn thận: liên tục đối lập gián đoạn của một chuyển pha, tính sắc nét, triviality kiểu trường trung bình ở chiều bốn, và cách percolation Fortuin–Kasteleyn ngồi cạnh các câu chuyện conformal của [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu **chuyển pha** như sự thay đổi của luật thể tích vô hạn của một mô hình trên lưới khi một tham số (nhiệt độ, trọng số cạnh, trọng số cluster) vượt giá trị tới hạn.
- Phân biệt **tính liên tục** của từ hóa hoặc mật độ percolation tại điểm tới hạn với **tính sắc nét** (suy giảm mũ ở phía dưới tới hạn, không có pha trung gian).
- Giải thích vì sao chiều bốn là **trường hợp biên** (marginal) đối với Ising và $$\varphi^4$$: hành vi Gaussian kiểu trường trung bình kèm hiệu chỉnh logarit, sau triviality Aizenman–Fröhlich ở các chiều $$d\ge 5$$.
- Mô tả percolation Fortuin–Kasteleyn (FK) như biểu diễn hình học của các mô hình Potts/Ising, và nói tính liên tục đối lập gián đoạn của chuyển pha FK trên $$\mathbb{Z}^2$$ nghĩa là gì.
- Gán công lao cẩn thận: dòng ngẫu nhiên, sắc nét kiểu OSSS, và bất biến quay là cộng tác; bất biến conformal đầy đủ của mọi mô hình FK phẳng **không** phải trích dẫn 2022.

**Kiến thức nền.** Percolation liên kết độc lập trên $$\mathbb{Z}^d$$ ở mức khẩu hiệu; Hamiltonian Ising như tổng tích spin láng giềng; ý rằng giới hạn thể tích vô hạn có thể phụ thuộc điều kiện biên. Không cần lý thuyết trường conformal trước đó.

**Liên kết seminar.** LO1 / LO4 (chương trình khó; xác suất trên lưới ↔ giới hạn scale continuum). Ghép với [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) cho bất biến conformal của percolation đỉnh tới hạn trên lưới tam giác, và với [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) cho SLE như ngôn ngữ continuum mà các giới hạn ấy nói khi chúng tồn tại.

---

## 1. Vì sao mô hình trên lưới cần định lý, không chỉ hình vẽ

Một khóa học mở đầu viết năng lượng Ising trên hộp hữu hạn $$\Lambda\subset\mathbb{Z}^d$$ là

$$
H_\Lambda(\sigma)=-\sum_{\{x,y\}\subset\Lambda}J_{xy}\sigma_x\sigma_y-h\sum_{x\in\Lambda}\sigma_x,\qquad \sigma_x=\pm 1,
$$

và trọng số Gibbs $$e^{-\beta H}$$. Khi $$\beta$$ tăng, các spin láng giềng thích thẳng hàng. Ở thể tích vô hạn người ta hỏi từ hóa

$$
m(\beta)=\lim_{h\downarrow 0}\langle\sigma_0\rangle_{\beta,h}
$$

bằng không hay dương. Cùng câu hỏi ấy, với percolation Bernoulli, hỏi liệu gốc có thuộc một cluster mở vô hạn với xác suất dương hay không.

Hình ảnh pha “trật tự” và “vô trật tự” thì dễ. Định lý thì không. Tồn tại nhiệt độ nghịch đảo tới hạn $$\beta_c\in(0,\infty)$$ ở các chiều $$d\ge 2$$ là cổ điển; điều xảy ra **tại** $$\beta_c$$, và tốc độ suy giảm tương quan **ngay dưới** nó, đã kháng cự hàng thập niên ở chiều ba. Ising hai chiều được Onsager giải; nghiệm tường minh ấy không xuất khẩu sang $$d=3$$ hay sang các mô hình percolation phụ thuộc mà trọng số không phải tung đồng xu độc lập.

**Khẩu hiệu.** Chuyển pha là định lý về độ đo thể tích vô hạn, không phải đồ thị từ hóa trên hộp hữu hạn.

---

## 2. Lịch sử ý tưởng

Nghiệm 1944 của Onsager cho Ising hai chiều biến tính liên tục của từ hóa tại $$\beta_c$$ thành một phép tính. Lý thuyết percolation, từ Broadbent–Hammersley trở đi, cung cấp ngôn ngữ hình học: cluster mở, xác suất tới hạn, và ước lượng cắt ngang Russo–Seymour–Welsh. Fortuin và Kasteleyn viết lại các mô hình Potts như độ đo **random-cluster** (FK), để tương quan spin trở thành xác suất liên thông. Biểu diễn **dòng ngẫu nhiên** của Aizenman biến tương quan Ising thành tính chất giao của các dòng nhận giá trị nguyên.

Vào những năm 1980–2000, bất biến conformal hai chiều trở thành một chương trình: Smirnov về percolation tam giác, SLE của Schramm, Werner về giao diện continuum. Chương trình ấy ngoạn mục và **gắn với chiều**. Chiều ba và bốn đòi hỏi dòng, thuật toán ngẫu nhiên (OSSS), chặn hồng ngoại, và ước lượng giao đa thang. Trích dẫn 2022 nhấn mạnh việc khép các bài toán chiều cao hơn và mô hình phụ thuộc ấy, chứ không thay thế câu chuyện conformal hai chiều.

---

## 3. Liên tục và sắc nét, đặc biệt ở chiều ba

**Tính liên tục** tại điểm tới hạn đối với các mô hình Ising sắt từ hỏi liệu từ hóa tự phát có triệt tiêu tại $$\beta_c$$ hay không. Với mô hình Ising láng giềng gần trên $$\mathbb{Z}^3$$ đây là câu hỏi tồn tại lâu. Cùng Aizenman và Sidoravicius, Duminil-Copin chứng minh tính liên tục bằng cách nghiên cứu các dòng ngẫu nhiên thể tích vô hạn và dùng tính duy nhất của cluster vô hạn trong biểu diễn ấy. Cùng vòng ý tưởng cho tính liên tục với một lớp hệ Ising sắt từ gồm cả lưới ba chiều chuẩn.

**Tính sắc nét** là phát biểu khác. Dưới tới hạn, người ta muốn suy giảm mũ của liên thông hoặc của tương quan spin, và tính hữu hạn của susceptibility; trên tới hạn, người ta muốn mật độ đều dương của cluster vô hạn hoặc từ hóa thực sự dương. Không nên có khoảng tham số “mờ” nơi tương quan suy giảm chậm nhưng không tồn tại cluster vô hạn. Duminil-Copin và Tassion đưa ra chứng minh mới cho tính sắc nét của percolation Bernoulli và Ising trên các đồ thị transitive tổng quát. Công trình sau với Raoufi và Tassion dùng bất đẳng thức OSSS để xử lý FK và các mô hình phụ thuộc liên quan một cách thống nhất.

**Độ chính xác.** Liên tục và sắc nét là anh em, không phải đồng nghĩa. Một chuyển pha có thể liên tục nhưng vẫn cần lập luận riêng để sắc nét; các mô hình Potts với $$q$$ lớn có thể gián đoạn.

---

## 4. Chiều bốn: trường trung bình và triviality

Lý thuyết trường lượng tử kiến tạo hỏi liệu một trường vô hướng Euclid không tầm thường với tương tác $$\varphi^4$$ có tồn tại ở chiều bốn hay không. Aizenman và Fröhlich, độc lập vào đầu những năm 1980, chỉ ra rằng ở các chiều $$d\ge 5$$, giới hạn scale của Ising tới hạn và các mô hình $$\varphi^4$$ trên lưới là Gaussian: luật Wick đúng, và lý thuyết continuum là “tầm thường” như một trường tương tác.

Chiều bốn là **trường hợp biên**. Các chặn hồng ngoại vẫn ràng buộc hàm hai điểm, nhưng ước lượng sơ đồ cây cho độ lệch khỏi luật Wick chưa đủ mạnh. Cùng Aizenman, Duminil-Copin chứng minh **triviality tại chiều biên** (marginal triviality): các giới hạn scale của Ising và $$\varphi^4_4$$ bốn chiều tới hạn và gần tới hạn là Gaussian. Chứng minh cải thiện chặn cây bằng một thừa số logarit, qua phân tích đa thang các xác suất giao của dòng ngẫu nhiên. Theo ngôn ngữ của trích dẫn, đây là hành vi tới hạn trường trung bình của Ising bốn chiều và triviality của lý thuyết trường vô hướng Euclid bốn chiều.

**Khẩu hiệu.** “Tầm thường” ở đây nghĩa là Gaussian như một trường Euclid, không phải “dễ chứng minh.”

---

## 5. Percolation FK: liên tục, gián đoạn, và một bước tới bất biến conformal

Độ đo random-cluster với trọng số cluster $$q\ge 1$$ nội suy percolation Bernoulli ($$q=1$$) và biểu diễn hình học của các mô hình Potts $$q$$ trạng thái. Trên lưới vuông điểm tới hạn đã biết (Beffara–Duminil-Copin). Cùng Sidoravicius và Tassion, Duminil-Copin chứng minh rằng chuyển pha FK trên $$\mathbb{Z}^2$$ là **liên tục** khi $$q\in[1,4]$$ và **gián đoạn** khi $$q>4$$, khớp dự đoán rằng $$q=4$$ là ngưỡng.

Tính liên tục của chuyển pha FK phẳng không phải **bất biến conformal** của một giới hạn scale. Một cộng tác sau (Kozlowski, Krachun, Manolescu, Oulamara) thiết lập **bất biến quay** của FK hai chiều tới hạn trên một khoảng $$q$$—một bước thực sự tới bất biến conformal, **không** phải chứng minh rằng mọi mô hình FK phẳng đều có giới hạn scale SLE hoặc CFT. Percolation tam giác của Smirnov và SLE Schramm–Werner vẫn là mẫu mực của một đồng nhất continuum đầy đủ. Bất biến conformal FK là chương trình láng giềng, vẫn mở ở dạng tổng quát đầy đủ.

---

## 6. Vì sao là Huy chương Fields

Ba lý do đan vào nhau:

1. **Độ khó.** Tính liên tục của Ising ba chiều và triviality ở chiều bốn là các bài toán mở cổ điển; chứng minh dùng những biểu diễn dễ gọi tên và khó khép.
2. **Tính trung tâm.** Chuyển pha tổ chức cơ học thống kê. Một khi liên tục, sắc nét, và các ngưỡng trường trung bình là định lý, bản đồ mô hình nào có thể có giới hạn continuum không tầm thường trở nên sắc hơn.
3. **Khẩu hiệu trong sáng với phương pháp sâu.** “Chuyển pha Ising 3D liên tục; Ising 4D là Gaussian ở thang lớn” là câu một học viên cao học nhớ được; các lập luận giao dòng và OSSS là những công trình lớn của xác suất đương đại.

Trong khóa này, Duminil-Copin ngồi giữa các câu chuyện Fields conformal hai chiều và câu hỏi lý thuyết trường kiến tạo về việc liệu một trường vô hướng tương tác có thể tồn tại ở chiều bốn.

---

## Nhầm lẫn thường gặp

| Khẳng định | Chữa lại |
|------------|----------|
| “Ông chứng minh bất biến conformal của mọi mô hình FK.” | Ông chứng minh các định lý liên tục/gián đoạn và các bước bất biến quay; bất biến conformal đầy đủ vẫn mở nói chung. |
| “Liên tục bằng sắc nét.” | Liên tục nói về tham số thứ tự tại $$\beta_c$$; sắc nét nói về việc không có pha trung gian và suy giảm mũ dưới $$\beta_c$$. |
| “Triviality nghĩa là mô hình Ising không thú vị.” | Nó nghĩa là giới hạn scale là Gaussian như một trường Euclid. |
| “Onsager đã làm xong chiều ba.” | Onsager giải Ising hai chiều; $$d=3$$ không có dạng đóng như vậy. |
| “Huy chương chỉ là percolation 2D.” | Trích dẫn nhấn mạnh chiều ba và bốn, cộng một lý thuyết xác suất rộng hơn về chuyển pha. |

---

## Bài tập

1. Bằng lời của bạn: độ đo Gibbs **thể tích vô hạn** quên gì và giữ gì so với hàm phân hoạch trên hộp hữu hạn?
2. Vì sao phát biểu rằng từ hóa **triệt tiêu tại** $$\beta_c$$ nghe khác phát biểu rằng tương quan **suy giảm mũ** với mọi $$\beta<\beta_c$$?
3. Viết sơ đồ trọng số random-cluster (trọng số cạnh $$p$$, trọng số cluster $$q$$) và nói cặp $$(p,q)$$ nào khôi phục percolation Bernoulli, cặp nào khôi phục Ising.
4. Aizenman–Fröhlich xử lý $$d\ge 5$$; Aizenman–Duminil-Copin xử lý $$d=4$$. “Biên” nghĩa là gì trong một đoạn?
5. **Luyện độ chính xác.** Tìm một câu phổ thông nói Duminil-Copin “chứng minh bất biến conformal ở 3D.” Viết lại thành hai câu chính xác.
6. **Kéo giãn seminar.** So sánh chân dung này với [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/): một phòng thí nghiệm đồng nhất một đối tượng continuum; phòng kia chứng minh định lý trên lưới khiến giới hạn continuum trở nên khả dĩ. Khi nào bạn muốn mỗi bên?

---

## Nguồn video và đọc thêm

1. **Trích dẫn IMU** — trang Fields Medals 2022 và PDF trích dẫn chính thức: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022) · [trích dẫn](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/IMU_Fields22_Duminil-Copin_citation.pdf).
2. **Định hướng** — chân dung Quanta: [Hugo Duminil-Copin Wins the Fields Medal](https://www.quantamagazine.org/hugo-duminil-copin-wins-the-fields-medal-20220705/).
3. **Tổng quan** — M. Biskup, *The work of Hugo Duminil-Copin* (arXiv:2207.02022), viết cho giải 2022.

**Nhắc trạng thái:** Liên tục, sắc nét, và triviality 4D—**không** phải khẳng định mọi mô hình FK phẳng đều bất biến conformal.

---

## Tài liệu tham khảo

1. Trích dẫn Huy chương Fields 2022 của IMU — Hugo Duminil-Copin (mathunion.org).
2. **M. Aizenman, H. Duminil-Copin, V. Sidoravicius** — Dòng ngẫu nhiên và tính liên tục của từ hóa Ising (2015).
3. **H. Duminil-Copin và V. Tassion** — Tính sắc nét của chuyển pha cho percolation và Ising (2016); công trình OSSS sau với A. Raoufi.
4. **M. Aizenman và H. Duminil-Copin** — Triviality biên của Ising 4D tới hạn và $$\varphi^4_4$$ (Ann. of Math., 2021).
5. Láng giềng khóa học: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/).

---

## Hướng đi tiếp

- Đọc một tổng quan về dòng ngẫu nhiên và liệt kê ba đồng nhất biến tương quan spin thành sự kiện hình học.
- So sánh nghiệm tường minh hai chiều của Onsager với định lý liên tục ba chiều: “đã giải” nghĩa là gì trong mỗi văn hóa?
- Tùy chọn seminar A3: một trang về những gì vẫn mở đối với bất biến conformal của các mô hình FK phẳng—mà không khẳng định huy chương 2022 đã khép chương trình ấy.
