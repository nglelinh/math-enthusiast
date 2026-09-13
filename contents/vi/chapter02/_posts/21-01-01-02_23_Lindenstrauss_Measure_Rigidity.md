---
layout: post
title: "Độ cứng độ đo của Lindenstrauss (Huy chương Fields 2010)"
chapter: '02'
order: 23
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Elon Lindenstrauss** nhận **Huy chương Fields 2010**

> “for his results on measure rigidity in ergodic theory, and their applications to number theory.”
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

**Độ cứng độ đo** (measure rigidity) là slogan rằng một hành động nhóm trông a priori hỗn độn thường chỉ nhận **rất ít** độ đo xác suất bất biến—và những độ đo ít ỏi ấy là đại số (độ đo Haar trên quỹ đạo đóng, Lebesgue trên một dưới-torus). Một khi các độ đo được phân loại, các định lý phân bố đều và các phát biểu Diophantine trở thành hệ quả. Huy chương của Lindenstrauss ghi nhận một thân các phân loại ấy cho **hành động chéo hóa được hạng cao**, và hai món xuất khẩu nổi tiếng: một định lý chiều Hausdorff zero cho ngoại lệ của **giả thuyết Littlewood** (cùng Einsiedler và Katok), và **ergodic lượng tử duy nhất số học** cho mặt hyperbolic số học compact (trong khung Hecke–Maass của Rudnick–Sarnak).

Bài này **không** nói giả thuyết Littlewood đã được chứng minh đầy đủ. Nó **không** coi ergodic lượng tử duy nhất như định lý về mọi mặt hyperbolic. Nó đặt Lindenstrauss trong một cảnh quan đã được Furstenberg, Margulis, Ratner, Katok, Einsiedler và Host–Kra định hình.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa độ cứng độ đo như “các độ đo bất biến khan hiếm, thường là đại số,” và đối chiếu với sự phong phú của độ đo cho một tự đẳng cấu torus hyperbolic đơn.
- Phân biệt độ cứng **unipotent** (các định lý Ratner) với độ cứng **chéo / hạng cao** (các bài toán kiểu Furstenberg; Einsiedler–Katok–Lindenstrauss).
- Phát biểu giả thuyết Littlewood và định lý EKL: nó đúng trừ có thể trên một tập **chiều Hausdorff zero**.
- Phát biểu QUE số học cho mặt hyperbolic số học compact (Hecke–Maass), ghi công Rudnick–Sarnak về giả thuyết, và mô tả vai trò Soundararajan trên mặt modular không compact (không thoát khối lượng).
- Nêu Furstenberg, Margulis, Ratner, Katok, Einsiedler và Host–Kra như cảnh quan, không như một trường phái với một định lý.
- Nối câu chuyện với văn hóa động lực cấp Abel trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/) mà không tuyên bố giải Abel là giải Fields.

**Kiến thức nền.** Hành động nhóm; ý độ đo bất biến và ergodicity; hình học hyperbolic của nửa mặt phẳng trên ở mức slogan ($$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$). Không gian thuần nhất $$\Gamma\backslash G$$ như “lattice hành động trên nhóm Lie” có thể lấy như bức tranh chứ không như lý thuyết.

**Liên kết seminar.** [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/) cho worldview Abel 2020 (động lực như công cụ cho lý thuyết số). [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) cho một xuất khẩu ergodic-sang-số học khác. [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/) cho động lực thuần nhất trong một chân dung Fields sau.

---

## 1. Lý thuyết ergodic như cỗ máy phân loại

Một hành động bảo toàn độ đo của nhóm $$H$$ trên không gian xác suất $$(X,\mu)$$ là **ergodic** nếu mọi tập đo được bất biến đều tầm thường. Lý thuyết ergodic nghiên cứu trung bình theo quỹ đạo. **Độ cứng độ đo** nghiên cứu câu hỏi trước: *những* độ đo $$\mu$$ nào có thể bất biến ngay từ đầu?

Với một tự đẳng cấu torus hyperbolic đơn—chẳng hạn $$x\mapsto 2x$$ trên $$\mathbb{R}/\mathbb{Z}$$—các độ đo bất biến rất nhiều: Lebesgue, Dirac tại $$0$$, và một vườn thú độ đo fractal tựa trên tập Cantor. Không có hy vọng liệt kê hết. Độ cứng xuất hiện khi hành động giàu hơn: vài ánh xạ giao hoán, hoặc một dòng unipotent, hoặc một nhóm chéo hạng cao của một nhóm Lie. Bất biến thêm có thể buộc $$\mu$$ đại số.

Bài toán $$\times 2,\times 3$$ của Furstenberg là giả thuyết mẫu kiểu này: độ đo xác suất không nguyên tử duy nhất trên đường tròn bất biến dưới cả $$x\mapsto 2x$$ lẫn $$x\mapsto 3x$$ phải là Lebesgue. Bài toán vẫn mở đầy đủ; các kết quả từng phần (Rudolph, Johnson, Host, …) đã cho thấy entropy dương cộng bất biến thêm là ràng buộc mạnh. Host–Kra về sau phân loại các nhân tố cấu trúc của trung bình ergodic bội, lộ các hệ nil như chướng ngại đặc trưng—một định lý độ cứng khác trong cùng văn hóa, không phải bổ đề trong các bài của Lindenstrauss.

Đóng góp của Lindenstrauss là đẩy văn hóa này lên **không gian thuần nhất** $$\Gamma\backslash G$$, nơi $$G$$ là nhóm Lie hoặc nhóm adelic, và rút ra lý thuyết số.

---

## 2. Unipotent đối chéo

**Các định lý Ratner** (thập niên 1990) phân loại bao đóng quỹ đạo và độ đo bất biến cho các dòng **unipotent** trên không gian thuần nhất. Phần tử unipotent (nghĩ ma trận tam giác trên chặt) có quỹ đạo đa thức; phân loại đầy đủ và đại số. Công trình của Margulis về dòng unipotent và giả thuyết Oppenheim là tổ tiên số học nổi tiếng: một khi bao đóng quỹ đạo được hiểu, giá trị các dạng toàn phương không xác định tại số nguyên trở nên trù mật.

Hành động **chéo** khác. Một torus tách—các ma trận chéo dương nhân trái trên, chẳng hạn, $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$—có **hạng cao** khi torus có chiều ít nhất hai. Quỹ đạo mũ, không đa thức. Không có định lý Ratner cùng mức tổng quát. Furstenberg và Margulis đặt giả thuyết rằng độ đo bất biến cho hành động ấy vẫn phải khan hiếm. Giá kỹ thuật là giả thuyết thêm: entropy dương, hồi quy theo hướng thêm, tương thích với tương ứng Hecke.

**Einsiedler–Katok–Lindenstrauss** (Annals of Mathematics, 2006) chứng minh một định lý phân loại độ đo cho hành động chéo hạng cao dưới giả thuyết **entropy dương**: một độ đo bất biến ergodic có entropy dương (đối với một phần tử của torus) thì đại số. Lời tán dương IMU 2010 nói điều này thiết lập một giả thuyết kiểu Furstenberg–Margulis dưới giả thuyết thêm ấy. Entropy dương không phải trang trí; nó loại các độ đo fractal thoái hóa nhất.

Đối chiếu sư phạm:

| Văn hóa | Tác nhân điển hình | Phân loại | Xuất khẩu số học |
|---------|-------------------|-----------|------------------|
| Ratner / Margulis unipotent | Nhóm một tham số unipotent | Đầy đủ, đại số | Oppenheim, nhiều cái khác |
| Chéo hạng cao | Torus tách, $$\times 2\times 3$$ | Từng phần; giả thuyết entropy | Diophantine kiểu Littlewood |

Lindenstrauss làm việc trên hàng thứ hai, dùng entropy, hồi quy, và đôi khi đối xứng adelic thêm.

---

## 3. Giả thuyết Littlewood, gần như

**Giả thuyết Littlewood** (thập niên 1930) hỏi liệu mọi cặp số thực $$(\alpha,\beta)$$ có thỏa

$$
\liminf_{n\to\infty}\, n\,\|n\alpha\|\,\|n\beta\|=0,
$$

nơi $$\|\cdot\|$$ là khoảng cách tới số nguyên gần nhất. Tương đương: có luôn tìm được số nguyên $$n$$ làm $$n\alpha$$ và $$n\beta$$ *đồng thời* gần số nguyên khác thường, với bound tích cải thiện Dirichlet? Giả thuyết vẫn **mở**.

Bản dịch động lực thuần nhất (Cassels, Swinnerton-Dyer, rồi trường phái hiện đại) hiện thực hóa các $$(\alpha,\beta)$$ ngoại lệ như các điểm có quỹ đạo chéo trên một không gian lattice tránh cusp theo cách có kiểm soát. Nếu mọi độ đo bất biến của hành động torus liên quan là Haar trên quỹ đạo đóng, ngoại lệ không thể tích tụ.

**Einsiedler–Katok–Lindenstrauss** suy ra tập ngoại lệ có **chiều Hausdorff zero**. Hầu hết mọi cặp (theo nghĩa fractal rất mạnh) thỏa Littlewood; mọi tập phản ví dụ mỏng hơn mọi tập con chiều dương của mặt phẳng. Đó là định lý. Đó không phải chứng minh giả thuyết Littlewood. Các tóm tắt phổ thông nói “Littlewood đã giải” là sai.

---

## 4. Ergodic lượng tử duy nhất số học

Một dạng Maass trên mặt hyperbolic $$M=\Gamma\backslash\mathbb{H}$$ là hàm riêng $$L^2$$ của toán tử Laplace–Beltrami. Các độ đo

$$
\mu_\phi=\lvert\phi\rvert^2\,d\mathrm{vol}
$$

mô tả khối lượng của hàm riêng năng lượng cao ngồi trên $$M$$ thế nào. **Ergodic lượng tử** (Šnirel’man, Zelditch, Colin de Verdière) nói rằng *hầu hết* các độ đo ấy phân bố đều về thể tích, trên đa tạp compact độ cong âm. **Ergodic lượng tử duy nhất (QUE)**, do **Rudnick–Sarnak** giả thuyết (1994), hỏi liệu *mọi* dãy hàm riêng có phân bố đều—không có sẹo ngoại lệ.

Trên mặt số học người ta có thêm toán tử Hecke. Thu hẹp về hàm riêng chung (dạng Hecke–Maass) là **QUE số học**. Người ta kỳ vọng phổ Laplace đơn, nên điều kiện Hecke sẽ tự động; tính đơn ấy không được biết.

**Lindenstrauss** (*Invariant measures and arithmetic quantum unique ergodicity*, Annals of Mathematics, 163, 2006) chứng minh QUE số học cho mặt hyperbolic số học **compact**: giới hạn lượng tử số học duy nhất là thể tích chuẩn hóa. Chứng minh phân loại các độ đo trên không gian mở rộng $$\Gamma\backslash\mathrm{SL}(2,\mathbb{R})\times L$$ bất biến dưới dòng chéo, có entropy dương, và hồi quy theo các hướng (Hecke / adelic) thêm; các nâng microlocal của độ đo khối lượng Hecke–Maass sinh ra các đối tượng ấy.

Với mặt congruence **không compact**, kể cả mặt modular $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$, cùng phương pháp chỉ ra mọi giới hạn lượng tử số học là $$c$$ lần thể tích với $$c\in[0,1]$$. Khối lượng có thể thoát vào cusp. **Kannan Soundararajan** (*Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$*, Annals, 2010) loại thoát khối lượng cho dạng Hecke–Maass trên mặt modular; kết hợp với Lindenstrauss, điều này chứng minh QUE số học ở đó. Công trình chung trước đó của Bourgain–Lindenstrauss cung cấp các bound entropy dùng trong chương trình.

Các dạng riêng Hecke **chỉnh hình** là bài QUE song song. **Holowinsky–Soundararajan** (Annals, 2010) chứng minh QUE cho dạng cusp Hecke chỉnh hình trên mặt modular bằng lý thuyết số giải tích, không bằng độ cứng độ đo. Đừng gán định lý ấy cho Lindenstrauss.

QUE cho mặt hyperbolic compact tổng quát (không số học) vẫn mở.

---

## 5. Một cảnh quan tên tuổi

| Tên | Vai trò trong câu chuyện này |
|-----|------------------------------|
| Furstenberg | $$\times 2,\times 3$$ và ý rằng các map giao hoán thêm làm cứng độ đo; hồi quy bội |
| Margulis | Superrigidity, arithmeticity, dòng unipotent, Oppenheim; độ cứng chéo giả thuyết |
| Ratner | Phân loại dòng unipotent—anh em đã hoàn tất của bài chéo |
| Katok | Entropy, độ cứng, và hợp tác EKL |
| Einsiedler | EKL và động lực thuần nhất sau này với Lindenstrauss và những người khác |
| Host–Kra | Cấu trúc trung bình bội / nhân tử nil—văn hóa độ cứng ergodic rộng hơn |
| Rudnick–Sarnak | Giả thuyết QUE |
| Soundararajan | Không thoát khối lượng trên $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$; QUE chỉnh hình với Holowinsky |
| Bourgain | Entropy của giới hạn lượng tử (với Lindenstrauss) |

Lindenstrauss (sinh 1970) viết luận án 1999 tại Hebrew University với Benjamin Weiss. Ông là fellow giải thưởng dài hạn Clay (2003–2005), dạy tại Princeton, trở về Jerusalem, và năm 2024 gia nhập faculty thường trực của Institute for Advanced Study. Ông là người Israel đầu tiên nhận Fields. Tiểu sử không phải định lý; định lý là sự khan hiếm của độ đo.

---

## 6. Vì sao Huy chương Fields

Văn bản IMU 2010 nhấn hai món xuất khẩu—xấp xỉ Diophantine kiểu Littlewood và QUE số học—cùng độ sâu của phân loại nền. Huy chương không phải “một giả thuyết bị khép.” Littlewood chưa khép. QUE khép trong trường hợp compact số học và, với Soundararajan, trên mặt modular cho dạng Hecke–Maass. Điều bị khép là một **phương pháp**: entropy cộng bất biến thêm cộng động lực thuần nhất như cỗ máy sản xuất định lý số học.

Với khóa học này, Lindenstrauss là đối tác scale Fields của câu chuyện Abel trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/): động lực như đại số ẩn của lý thuyết số. Các giải khác nhau; văn hóa thì chung.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Giả thuyết Littlewood đã được chứng minh.” | EKL: ngoại lệ có chiều Hausdorff zero. Phát biểu đầy đủ vẫn mở. |
| “QUE được chứng minh cho mọi mặt hyperbolic.” | Hecke–Maass số học, trường hợp compact (Lindenstrauss); mặt modular với Soundararajan; QUE tổng quát vẫn mở. |
| “Lindenstrauss chứng minh QUE chỉnh hình.” | Holowinsky–Soundararajan, bằng phương pháp khác. |
| “Độ cứng độ đo là định lý Ratner.” | Ratner là chương unipotent; chéo hạng cao là chương khác, từng phần. |
| “Entropy dương là giả thuyết thêm nhỏ.” | Đó là giả thuyết giết các độ đo bất biến bệnh lý nhất. |
| “Fields 2010 giống Abel 2020.” | Abel 2020 vinh danh Furstenberg và Margulis dùng động lực cả đời; Lindenstrauss là triển khai scale Fields sau. |

---

## Bài tập

1. Trong một đoạn, độ đo bất biến là gì, và vì sao *phân loại* chúng có thể khó hơn chứng minh một định lý ergodic đơn?
2. Đối chiếu dòng unipotent với hành động torus chéo bằng ba slogan: hình quỹ đạo, trạng thái phân loại, hệ quả số học điển hình.
3. Viết giả thuyết Littlewood. Viết kết luận EKL. Khoanh những chữ không được xóa (“trừ có thể,” “chiều Hausdorff zero”).
4. Cấu trúc thêm nào làm QUE thành *số học*? Vì sao tính compact loại vấn đề thoát khối lượng mà Soundararajan sau đó xử lý?
5. Vì sao QUE Rudnick–Sarnak không theo từ ergodic lượng tử (Šnirel’man–Zelditch–Colin de Verdière)?
6. **Luyện độ chính xác.** Viết lại “một nhà toán học Israel giải Littlewood và hỗn độn lượng tử” thành ba câu chính xác.
7. Lướt abstract của Lindenstrauss, Annals 163 (2006), hoặc của EKL, Annals 164 (2006), và liệt kê các giả thuyết bạn cần tra tiếp (entropy, hồi quy, lattice congruence, nâng microlocal).
8. **Seminar mở rộng.** So bài $$\times 2,\times 3$$ của Furstenberg với EKL: cùng bản năng độ cứng, nhóm khác. Điều gì vẫn mở trong trường hợp đường tròn?

---

## Liên kết

- IMU Fields Medals 2010: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- Lời tán dương IMU ICM 2010 (Lindenstrauss): [https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html)
- Wikipedia — Elon Lindenstrauss: [https://en.wikipedia.org/wiki/Elon_Lindenstrauss](https://en.wikipedia.org/wiki/Elon_Lindenstrauss)
- Thông báo IAS (faculty 2024): [https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty](https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty)
- Soundararajan, QUE cho mặt modular (arXiv:0901.4060): [https://arxiv.org/abs/0901.4060](https://arxiv.org/abs/0901.4060)
- Tìm arXiv — Einsiedler Katok Lindenstrauss Littlewood: [https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all](https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all)
- Survey AMS Notices các Fields 2010: [https://www.ams.org/notices/201103/rtx110300453p.pdf](https://www.ams.org/notices/201103/rtx110300453p.pdf)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 2010 — Elon Lindenstrauss.
2. M. Einsiedler, A. Katok và E. Lindenstrauss, “Invariant measures and the set of exceptions to Littlewood’s conjecture,” *Ann. of Math.* 164 (2006).
3. E. Lindenstrauss, “Invariant measures and arithmetic quantum unique ergodicity,” *Ann. of Math.* 163 (2006).
4. Z. Rudnick và P. Sarnak, “The behaviour of eigenstates of arithmetic hyperbolic manifolds,” *Comm. Math. Phys.* 161 (1994) — giả thuyết QUE.
5. K. Soundararajan, “Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$,” *Ann. of Math.* 172 (2010).
6. R. Holowinsky và K. Soundararajan, “Mass equidistribution for Hecke eigenforms,” *Ann. of Math.* 172 (2010) — QUE chỉnh hình, phương pháp khác.
7. M. Ratner, phân loại độ đo và quỹ đạo cho dòng unipotent; H. Furstenberg, $$\times 2,\times 3$$ và disjointness; G. Margulis, dòng unipotent và Oppenheim.
8. B. Host và B. Kra, định lý cấu trúc cho trung bình ergodic bội (nhân tử nil).
9. Khóa học: [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/), [Tổng quan Chương 8]({{ site.baseurl }}/contents/vi/chapter08/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/).

---

## Hướng đi tiếp

- Đọc một bài giảng ngắn về định lý Ratner trước EKL, để phân loại chéo còn thiếu được cảm như một khoảng trống chứ không như từ đồng nghĩa.
- Tùy chọn seminar: một trang trạng thái “Littlewood sau EKL” liệt kê điều một chứng minh đầy đủ vẫn cần—mà không bịa chứng minh.
