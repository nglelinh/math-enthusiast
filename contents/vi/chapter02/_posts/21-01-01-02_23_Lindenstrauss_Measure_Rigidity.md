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

*Tạm dịch: vì các kết quả về độ cứng độ đo trong lý thuyết ergodic và những ứng dụng của chúng vào lý thuyết số.*

**Độ cứng độ đo** (measure rigidity) là hiện tượng sau: một tác động nhóm thoạt nhìn có vẻ hỗn loạn nhưng lại chỉ có **rất ít** độ đo xác suất bất biến, và những độ đo đó có bản chất đại số (độ đo Haar trên một quỹ đạo đóng, độ đo Lebesgue trên một xuyến con). Khi đã phân loại được các độ đo bất biến, ta suy ra được các định lý về phân bố đều và các kết quả về xấp xỉ Diophantine. Huy chương của Lindenstrauss ghi nhận một loạt kết quả phân loại như vậy cho **tác động chéo hóa được có hạng cao**, cùng hai ứng dụng nổi tiếng. Thứ nhất, các ngoại lệ của **giả thuyết Littlewood** tạo thành một tập có chiều Hausdorff bằng không (cùng Einsiedler và Katok). Thứ hai, **tính ergodic lượng tử duy nhất số học** trên các mặt hyperbolic số học compact (trong khuôn khổ dạng Hecke–Maass của Rudnick–Sarnak).

Bài này **không** nói giả thuyết Littlewood đã được chứng minh trọn vẹn. Bài cũng **không** coi tính ergodic lượng tử duy nhất là định lý cho mọi mặt hyperbolic. Lindenstrauss được đặt trong bối cảnh do Furstenberg, Margulis, Ratner, Katok, Einsiedler và Host–Kra xây dựng.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa độ cứng độ đo là hiện tượng "các độ đo bất biến rất ít, và thường có bản chất đại số", rồi so sánh với trường hợp một ánh xạ đơn lẻ trên xuyến, nơi có vô số độ đo bất biến.
- Phân biệt độ cứng cho dòng **lũy đơn (unipotent)** (các định lý Ratner) với độ cứng cho tác động **chéo, hạng cao** (các bài toán kiểu Furstenberg; Einsiedler–Katok–Lindenstrauss).
- Phát biểu giả thuyết Littlewood và định lý EKL: giả thuyết đúng, có thể trừ một tập có **chiều Hausdorff bằng không**.
- Phát biểu tính ergodic lượng tử duy nhất (QUE) số học cho mặt hyperbolic số học compact (dạng Hecke–Maass), ghi công Rudnick–Sarnak cho giả thuyết, và nêu vai trò của Soundararajan trên mặt modular không compact (chứng minh không có khối lượng thoát ra xa).
- Xem Furstenberg, Margulis, Ratner, Katok, Einsiedler và Host–Kra là bối cảnh chung, chứ không phải một trường phái với một định lý duy nhất.
- Nối câu chuyện này với các công trình động lực học được giải Abel trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/), nhưng không nhầm giải Abel với giải Fields.

**Kiến thức nền.** Tác động nhóm; khái niệm độ đo bất biến và tính ergodic; hình học hyperbolic trên nửa mặt phẳng trên ở mức hình dung ($$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$). Không gian thuần nhất $$\Gamma\backslash G$$ có thể hiểu đơn giản là "một lưới (lattice) tác động lên một nhóm Lie", chưa cần lý thuyết đầy đủ.

**Liên kết với các bài khác.** [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/) trình bày quan điểm được giải Abel 2020 ghi nhận: động lực học là công cụ cho lý thuyết số. [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) là một ví dụ khác về việc đưa phương pháp ergodic vào số học. [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/) cho thấy động lực học thuần nhất trong một chân dung Fields về sau.

---

## 1. Lý thuyết ergodic như một công cụ phân loại

Một tác động bảo toàn độ đo của nhóm $$H$$ trên không gian xác suất $$(X,\mu)$$ gọi là **ergodic** nếu mọi tập đo được bất biến đều tầm thường (độ đo bằng 0 hoặc 1). Lý thuyết ergodic nghiên cứu các trung bình dọc theo quỹ đạo. **Độ cứng độ đo** đặt câu hỏi đi trước: ngay từ đầu, *những* độ đo $$\mu$$ nào có thể bất biến?

Với một ánh xạ đơn lẻ có tính hyperbolic, chẳng hạn $$x\mapsto 2x$$ trên $$\mathbb{R}/\mathbb{Z}$$, có rất nhiều độ đo bất biến: độ đo Lebesgue, độ đo Dirac tại $$0$$, và vô số độ đo fractal tập trung trên các tập kiểu Cantor. Không có hy vọng liệt kê hết. Độ cứng xuất hiện khi tác động phong phú hơn: nhiều ánh xạ giao hoán với nhau, một dòng lũy đơn, hoặc một nhóm chéo có hạng cao trong một nhóm Lie. Việc phải bất biến dưới nhiều phép biến đổi hơn có thể buộc $$\mu$$ phải có bản chất đại số.

Bài toán $$\times 2,\times 3$$ của Furstenberg là giả thuyết tiêu biểu cho kiểu này: độ đo xác suất ergodic không có nguyên tử duy nhất trên đường tròn, bất biến dưới cả $$x\mapsto 2x$$ lẫn $$x\mapsto 3x$$, phải là độ đo Lebesgue. Bài toán vẫn chưa được giải trọn vẹn. Các kết quả từng phần (Rudolph, Johnson, Host, …) cho thấy entropy dương cộng với bất biến thêm là một ràng buộc rất mạnh. Về sau, Host–Kra phân loại các nhân tử cấu trúc của trung bình ergodic bội, và chỉ ra các hệ nil là vật cản đặc trưng. Đó là một định lý độ cứng khác cùng tinh thần, không phải một bổ đề trong các bài báo của Lindenstrauss.

Đóng góp của Lindenstrauss là đưa cách tiếp cận này lên **không gian thuần nhất** $$\Gamma\backslash G$$, trong đó $$G$$ là nhóm Lie hoặc nhóm adelic, và từ đó rút ra các kết quả lý thuyết số.

---

## 2. Lũy đơn và chéo

**Các định lý Ratner** (đầu thập niên 1990) phân loại bao đóng quỹ đạo và độ đo bất biến cho các dòng **lũy đơn** trên không gian thuần nhất. Phần tử lũy đơn (hãy nghĩ tới ma trận tam giác trên có đường chéo bằng 1) có quỹ đạo tăng kiểu đa thức, và phân loại ở đây là đầy đủ và mang tính đại số. Công trình của Margulis về dòng lũy đơn và giả thuyết Oppenheim là ứng dụng số học nổi tiếng đi trước: khi hiểu được bao đóng quỹ đạo, ta suy ra tập giá trị tại các điểm nguyên của một dạng toàn phương không xác định dấu (với điều kiện thích hợp) là trù mật.

Tác động **chéo** thì khác. Một xuyến tách (split torus), chẳng hạn nhóm các ma trận chéo dương nhân bên trái trên $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$, gọi là có **hạng cao** khi xuyến có chiều từ hai trở lên. Quỹ đạo ở đây tăng theo hàm mũ chứ không theo đa thức. Không có định lý nào tổng quát như định lý Ratner cho trường hợp này. Furstenberg và Margulis đặt giả thuyết rằng độ đo bất biến cho các tác động như vậy vẫn rất ít. Cái giá phải trả về kỹ thuật là các giả thiết bổ sung: entropy dương, tính hồi quy theo các hướng phụ, tương thích với các tương ứng Hecke.

**Einsiedler–Katok–Lindenstrauss** (Annals of Mathematics, 2006) chứng minh một định lý phân loại độ đo cho tác động chéo hạng cao dưới giả thiết **entropy dương**: một độ đo bất biến ergodic có entropy dương (đối với một phần tử của xuyến) thì có bản chất đại số. Lời tán dương của IMU năm 2010 nói kết quả này chứng minh một giả thuyết kiểu Furstenberg–Margulis dưới giả thiết bổ sung đó. Entropy dương không phải điều kiện cho đẹp. Nó loại bỏ những độ đo fractal suy biến nhất.

So sánh để dễ nhớ:

| Hướng nghiên cứu | Tác động điển hình | Phân loại | Ứng dụng số học |
|---------|-------------------|-----------|------------------|
| Ratner / Margulis, lũy đơn | Nhóm một tham số lũy đơn | Đầy đủ, đại số | Oppenheim và nhiều kết quả khác |
| Chéo, hạng cao | Xuyến tách, $$\times 2\times 3$$ | Từng phần; cần giả thiết entropy | Xấp xỉ Diophantine kiểu Littlewood |

Lindenstrauss làm việc ở hàng thứ hai, dùng entropy, tính hồi quy và đôi khi cả các đối xứng adelic bổ sung.

---

## 3. Giả thuyết Littlewood: gần như đã chứng minh

**Giả thuyết Littlewood** (thập niên 1930) hỏi liệu mọi cặp số thực $$(\alpha,\beta)$$ có thỏa

$$
\liminf_{n\to\infty}\, n\,\|n\alpha\|\,\|n\beta\|=0,
$$

trong đó $$\|\cdot\|$$ là khoảng cách tới số nguyên gần nhất. Nói cách khác: có phải luôn tìm được số nguyên $$n$$ sao cho $$n\alpha$$ và $$n\beta$$ *đồng thời* gần số nguyên một cách bất thường, với tích các khoảng cách tốt hơn đánh giá Dirichlet? Giả thuyết vẫn còn **mở**.

Khi dịch sang ngôn ngữ động lực học thuần nhất (Cassels, Swinnerton-Dyer, rồi các tác giả hiện đại), mỗi cặp $$(\alpha,\beta)$$ ngoại lệ ứng với một điểm mà quỹ đạo chéo của nó trên không gian các lưới luôn tránh xa vùng "đỉnh" (cusp) một cách có kiểm soát. Nếu mọi độ đo bất biến của tác động xuyến tương ứng đều là độ đo Haar trên quỹ đạo đóng, thì các ngoại lệ không thể tích tụ nhiều.

**Einsiedler–Katok–Lindenstrauss** suy ra rằng tập các ngoại lệ có **chiều Hausdorff bằng không**. Như vậy, theo một nghĩa fractal rất mạnh, hầu hết các cặp đều thỏa Littlewood: tập phản ví dụ (nếu có) còn mỏng hơn mọi tập con có chiều dương của mặt phẳng. Đó là một định lý. Nhưng đó không phải là chứng minh giả thuyết Littlewood. Các bài phổ biến nói "Littlewood đã được giải" là sai.

---

## 4. Tính ergodic lượng tử duy nhất số học

Một dạng Maass trên mặt hyperbolic $$M=\Gamma\backslash\mathbb{H}$$ là một hàm riêng thuộc $$L^2$$ của toán tử Laplace–Beltrami. Các độ đo

$$
\mu_\phi=\lvert\phi\rvert^2\,d\mathrm{vol}
$$

mô tả khối lượng của các hàm riêng ứng với năng lượng cao phân bố trên $$M$$ như thế nào. **Định lý ergodic lượng tử** (Šnirel’man, Zelditch, Colin de Verdière) nói rằng trên đa tạp compact có độ cong âm, *hầu hết* các độ đo này phân bố đều theo thể tích. **Tính ergodic lượng tử duy nhất (QUE)**, do **Rudnick–Sarnak** đặt giả thuyết năm 1994, hỏi liệu *mọi* dãy hàm riêng có phân bố đều hay không, tức là không có ngoại lệ nào tập trung khối lượng (không có "vết sẹo").

Trên mặt số học, ta có thêm các toán tử Hecke. Chỉ xét các hàm riêng chung (dạng Hecke–Maass) thì được bài toán **QUE số học**. Người ta dự đoán phổ của toán tử Laplace là đơn, khi đó điều kiện Hecke sẽ tự động thỏa; nhưng tính đơn này chưa được chứng minh.

**Lindenstrauss** (*Invariant measures and arithmetic quantum unique ergodicity*, Annals of Mathematics, 163, 2006) chứng minh QUE số học cho các mặt hyperbolic số học **compact**: giới hạn lượng tử số học duy nhất là độ đo thể tích đã chuẩn hóa. Chứng minh phân loại các độ đo trên không gian mở rộng $$\Gamma\backslash\mathrm{SL}(2,\mathbb{R})\times L$$ bất biến dưới dòng chéo, có entropy dương và có tính hồi quy theo các hướng phụ (Hecke / adelic). Những đối tượng này xuất hiện khi nâng (theo nghĩa vi địa phương, microlocal lift) các độ đo khối lượng của dạng Hecke–Maass.

Với các mặt đồng dư (congruence) **không compact**, kể cả mặt modular $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$, cùng phương pháp đó chỉ cho thấy mọi giới hạn lượng tử số học có dạng $$c$$ nhân với độ đo thể tích, với $$c\in[0,1]$$. Một phần khối lượng có thể thoát ra vùng đỉnh. **Kannan Soundararajan** (*Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$*, Annals, 2010) chứng minh không có khối lượng thoát ra cho dạng Hecke–Maass trên mặt modular. Kết hợp với kết quả của Lindenstrauss, điều này chứng minh QUE số học trên mặt modular. Công trình chung trước đó của Bourgain–Lindenstrauss cung cấp các đánh giá entropy được dùng trong chương trình này.

Bài toán QUE song song cho các dạng riêng Hecke **chỉnh hình** được **Holowinsky–Soundararajan** (Annals, 2010) giải cho dạng cusp Hecke chỉnh hình trên mặt modular, bằng lý thuyết số giải tích, không dùng độ cứng độ đo. Đừng gán định lý này cho Lindenstrauss.

QUE cho mặt hyperbolic compact tổng quát (không số học) vẫn còn mở.

---

## 5. Những người liên quan

| Tên | Vai trò trong câu chuyện |
|-----|------------------------------|
| Furstenberg | Bài toán $$\times 2,\times 3$$ và ý tưởng rằng các ánh xạ giao hoán bổ sung làm độ đo trở nên cứng; hồi quy bội |
| Margulis | Siêu cứng (superrigidity), tính số học (arithmeticity), dòng lũy đơn, giả thuyết Oppenheim; giả thuyết về độ cứng cho tác động chéo |
| Ratner | Phân loại cho dòng lũy đơn, trường hợp đã hoàn tất, đối xứng với bài toán chéo |
| Katok | Entropy, độ cứng, và cộng tác trong EKL |
| Einsiedler | EKL và các công trình động lực học thuần nhất sau này với Lindenstrauss và những người khác |
| Host–Kra | Cấu trúc của trung bình bội / nhân tử nil, thuộc hướng độ cứng ergodic rộng hơn |
| Rudnick–Sarnak | Giả thuyết QUE |
| Soundararajan | Không thoát khối lượng trên $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$; QUE chỉnh hình cùng Holowinsky |
| Bourgain | Entropy của giới hạn lượng tử (cùng Lindenstrauss) |

Lindenstrauss (sinh năm 1970) bảo vệ luận án năm 1999 tại Đại học Hebrew dưới sự hướng dẫn của Benjamin Weiss. Ông là nghiên cứu viên dài hạn của Viện Clay (2003–2005), giảng dạy tại Princeton, rồi trở về Jerusalem, và năm 2024 trở thành giáo sư thường trực của Institute for Advanced Study. Ông là người Israel đầu tiên nhận Huy chương Fields. Nhưng tiểu sử không phải là định lý; định lý ở đây là các độ đo bất biến rất hiếm.

---

## 6. Vì sao là Huy chương Fields

Văn bản của IMU năm 2010 nhấn mạnh hai ứng dụng (xấp xỉ Diophantine kiểu Littlewood và QUE số học) cùng chiều sâu của các kết quả phân loại phía sau. Huy chương không phải là phần thưởng cho "một giả thuyết đã được giải xong". Giả thuyết Littlewood chưa được giải. QUE đã được giải cho trường hợp compact số học, và (cùng với Soundararajan) cho dạng Hecke–Maass trên mặt modular. Điều được hoàn thiện là một **phương pháp**: kết hợp entropy, bất biến bổ sung và động lực học thuần nhất để sinh ra các định lý lý thuyết số.

Trong khóa học này, Lindenstrauss là phiên bản ở tầm Fields của câu chuyện giải Abel trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/): động lực học là cấu trúc ẩn phía sau nhiều bài toán lý thuyết số. Hai giải thưởng khác nhau, nhưng tư tưởng là chung.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Giả thuyết Littlewood đã được chứng minh." | EKL: tập ngoại lệ có chiều Hausdorff bằng không. Phát biểu đầy đủ vẫn còn mở. |
| "QUE đã được chứng minh cho mọi mặt hyperbolic." | Chỉ cho dạng Hecke–Maass số học, trường hợp compact (Lindenstrauss); mặt modular thì cần thêm Soundararajan; QUE tổng quát vẫn mở. |
| "Lindenstrauss chứng minh QUE chỉnh hình." | Đó là Holowinsky–Soundararajan, bằng phương pháp khác. |
| "Độ cứng độ đo chính là định lý Ratner." | Ratner là phần lũy đơn; tác động chéo hạng cao là phần khác, mới giải được từng phần. |
| "Entropy dương chỉ là giả thiết phụ nhỏ." | Chính giả thiết này loại bỏ các độ đo bất biến kỳ quặc nhất. |
| "Fields 2010 giống Abel 2020." | Abel 2020 vinh danh cả sự nghiệp dùng động lực học của Furstenberg và Margulis; Lindenstrauss là một bước phát triển sau, ở tầm Fields. |

---

## Bài tập

1. Viết một đoạn giải thích độ đo bất biến là gì, và vì sao *phân loại* chúng có thể khó hơn chứng minh một định lý ergodic riêng lẻ.
2. So sánh dòng lũy đơn với tác động xuyến chéo theo ba tiêu chí: hình dạng quỹ đạo, tình trạng phân loại, ứng dụng số học điển hình.
3. Viết giả thuyết Littlewood. Viết kết luận của EKL. Khoanh tròn những cụm từ không được bỏ ("có thể trừ", "chiều Hausdorff bằng không").
4. Cấu trúc bổ sung nào làm QUE trở thành bài toán *số học*? Vì sao tính compact loại bỏ được vấn đề thoát khối lượng mà Soundararajan phải xử lý sau đó?
5. Vì sao giả thuyết QUE của Rudnick–Sarnak không suy ra được từ định lý ergodic lượng tử (Šnirel’man–Zelditch–Colin de Verdière)?
6. **Luyện phát biểu chính xác.** Viết lại câu "một nhà toán học Israel giải được Littlewood và hỗn loạn lượng tử" thành ba câu chính xác.
7. Đọc lướt tóm tắt bài của Lindenstrauss, Annals 163 (2006), hoặc của EKL, Annals 164 (2006), và liệt kê các giả thiết bạn cần tra cứu thêm (entropy, hồi quy, lưới đồng dư, nâng vi địa phương).
8. **Mở rộng.** So sánh bài toán $$\times 2,\times 3$$ của Furstenberg với EKL: cùng tư tưởng độ cứng, nhưng khác nhóm. Trong trường hợp đường tròn, điều gì vẫn còn mở?

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

- Đọc một bài giảng ngắn về định lý Ratner trước khi đọc EKL, để thấy rõ phân loại cho trường hợp chéo còn thiếu những gì, thay vì coi hai bên như nhau.
- Bài tập thêm: viết một trang tóm tắt "Littlewood sau EKL", liệt kê những gì một chứng minh đầy đủ còn cần, nhưng không tự bịa ra chứng minh.

## Video tham khảo

- **Xem trước**: [Conferências Magnas: Elon Lindenstrauss - Homogeneous dynamics and diagonalizable actions (2013)](https://www.youtube.com/watch?v=e9Gj1yohLCw) (Instituto de Matemática Pura e Aplicada, tiếng Anh). Bài giảng lớn tại IMPA của chính Lindenstrauss về động lực học thuần nhất và tác động chéo hóa được, đúng chủ đề của mục 1 và 2.
- [Elon Lindenstrauss - An effective proof of the Oppenheim Conjecture](https://www.youtube.com/watch?v=_hOglF2XvQ8) (International Centre for Theoretical Sciences, tiếng Anh). Bài giảng về một chứng minh có đánh giá định lượng cho giả thuyết Oppenheim, thuộc phía lũy đơn của câu chuyện. Nên xem sau khi đã đọc mục 2.
