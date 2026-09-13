---
layout: post
title: "Lượng tử hóa, đường cong và nút của Kontsevich (Huy chương Fields 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Maxim Kontsevich** nhận **Huy chương Fields 1998**

> “For his contributions to algebraic geometry, topology, and mathematical physics, including the proof of Witten's conjecture of intersection numbers in moduli spaces of stable curves, construction of the universal Vassiliev invariant of knots, and formal quantization of Poisson manifolds.”
> — Citation IMU, ICM 1998 (như được ghi trong hồ sơ [Fields Medal](https://www.mathunion.org/imu-awards/fields-medal) và các nguồn tiểu sử chuẩn)

Ba gạch, ba chủ đề. Cám dỗ, nhìn lại từ những năm 2020, là thay danh sách ấy bằng các slogan sau này—đối xứng gương đồng điều, tích phân motivic, wall-crossing. Những chương trình ấy có thật, và vài cái là của Kontsevich. Chúng **không** phải citation 1998. Bài này theo bộ ba chính thức: **giả thuyết Witten** trên $$\overline{\mathcal{M}}_{g,n}$$, **bất biến Vassiliev phổ dụng**, và **lượng tử hóa biến dạng** các đa tạp Poisson. Đối xứng gương đồng điều chỉ xuất hiện như đề xuất ICM 1994 liên quan, không như tuyên bố đối xứng gương đã “được giải.”

Kontsevich (sinh 1964) là giáo sư thường trực tại Institut des Hautes Études Scientifiques và làm việc xuyên hình học đại số, topology, và vật lý toán. Huy chương là chân dung chỗ giao ấy trong thập niên 1990, không phải đống sự nghiệp trọn đời.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Thuộc citation 1998 như **ba** kết quả, và từ chối thay gạch thứ ba bằng đối xứng gương đồng điều.
- Phát biểu giả thuyết Witten ở mức slogan: hàm sinh các giao của lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ là tau-function của hệ KdV; Kontsevich chứng minh bằng đồ thị ruy-băng / mô hình ma trận.
- Mô tả tích phân Kontsevich như **bất biến kiểu hữu hạn (Vassiliev) phổ dụng**, với công lao cho Vassiliev và Bar-Natan về lý thuyết xung quanh.
- Giải thích lượng tử hóa biến dạng: một tích sao biến dạng tích từng điểm sao cho giao hoán tử bậc nhất khôi phục móc Poisson; định lý formality / công thức đồ thị của Kontsevich sinh tích ấy trên mọi đa tạp Poisson.
- Nhắc đối xứng gương đồng điều như chương trình 1994, không như phân loại đã xong và không như gạch thứ ba của Fields.
- Đặt công trình trên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) mà không coi vật lý là thay thế chứng minh.

**Kiến thức nền.** Ý không gian moduli của đường cong; móc Poisson trên $$\mathbb{R}^{2n}$$ hoặc trên đa tạp symplectic; đa thức Jones như “một bất biến nút không chỉ là nhóm cơ bản.” Giải tích phức và một giáo trình hình học đại số đầu giúp ích; lý thuyết trường lượng tử là không khí tùy chọn.

**Liên kết seminar.** [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) cho chương trình HMS như *đọc sau*, tách khỏi 1998. [Pardon / symplectic]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) cho phía Fukaya tiêu thụ HMS.

---

## 1. Vì sao danh sách 1998 là dàn bài đúng

Các bài prize ICM thường sống lâu hơn citation. Ảnh hưởng sau này của Kontsevich rất lớn: đối xứng gương đồng điều thành một lĩnh vực; tích phân motivic (bài giảng Orsay 1995, rồi Denef–Loeser) thành công cụ trong lý thuyết kỳ dị; map ổn định và lý thuyết Gromov–Witten đổi hình học đếm. Một khóa học nhét hết vào “Fields 1998” sẽ sai lịch sử.

Câu chính thức đã tham vọng đủ. Nó nói: một người chứng minh một giả thuyết của Witten về lý thuyết giao tautological của moduli đường cong ổn định; xây một bất biến nút kiểu hữu hạn phổ dụng; và lượng tử hóa mọi đa tạp Poisson ở mức formal. Hình học đại số, topology, và vật lý toán không phải ba sở thích. Chúng là ba nơi cùng bản năng đồ thị-và-tích phân sinh ra định lý.

---

## 2. Giả thuyết Witten: giao trên $$\overline{\mathcal{M}}_{g,n}$$

Gọi $$\overline{\mathcal{M}}_{g,n}$$ là compact hóa Deligne–Mumford của không gian moduli các đường cong giống $$g$$ với $$n$$ điểm đánh dấu. Trên không gian này sống các bundle đường tautological $$\mathbb{L}_i$$ có thớ là đường tiếp xúc tại các điểm đánh dấu; lớp Chern thứ nhất của chúng là các **lớp $$\psi$$**. Các số giao

$$
\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g=\int_{\overline{\mathcal{M}}_{g,n}}\psi_1^{d_1}\cdots\psi_n^{d_n}
$$

là các bất biến số đơn giản nhất của vành tautological (với quy ước triệt tiêu trừ khi các bậc cộng thành chiều $$3g-3+n$$).

**Giả thuyết Witten** (đầu thập niên 1990) khẳng định hàm sinh các số này là một tau-function của hệ **Korteweg–de Vries (KdV)**—tương đương, các số thỏa một hệ PDE mà thành viên đầu liên quan ràng buộc Virasoro / KdV. Giả thuyết đến từ hấp dẫn lượng tử hai chiều: hai mô tả mô hình ma trận của mặt ngẫu nhiên phải trùng, một tổ hợp và một hình học.

**Chứng minh của Kontsevich** (*Intersection theory on the moduli space of curves and the matrix Airy function*, *Comm. Math. Phys.* 147, 1992) đồng nhất lý thuyết giao với khai triển tổ hợp trên **đồ thị ruy-băng** (qua vi phân Strebel: một metric phân rã đường cong thành đồ thị béo). Hàm sinh trở thành tích phân Airy ma trận, vốn đã biết thỏa KdV. Hình học nhờ đó rút về một mô hình ma trận có hệ khả tích cổ điển.

**Slogan.** Witten đoán các số giao tautological của moduli đường cong biết KdV; Kontsevich trưng một từ điển đồ thị ruy-băng biến đoán thành tính toán.

Đây là gạch hình học đại số. Nó không phải phân loại mọi đường cong; nó là định lý về một họ số cụ thể trên $$\overline{\mathcal{M}}_{g,n}$$.

---

## 3. Bất biến Vassiliev phổ dụng và không gian cấu hình

**Vassiliev** (đầu thập niên 1990) đưa vào các bất biến kiểu hữu hạn của nút: bất biến triệt tiêu trên nút kỳ dị có đủ điểm kép, tương đương, bất biến có phụ thuộc vào đổi crossing là đa thức bậc bị chặn. **Bar-Natan** tổ chức phía tổ hợp: hệ trọng, sơ đồ dây, và quan hệ với đại số Lie cùng hệ số của đa thức Jones.

Thiếu một cỗ máy giải tích **phổ dụng** sinh mọi bất biến kiểu hữu hạn từ một xây dựng duy nhất. Kontsevich cung cấp một cái: **tích phân Kontsevich**, xây từ các tích phân lặp trên không gian cấu hình các điểm trên nút (và, trong bức tranh Chern–Simons nhiễu loạn, các điểm trong $$\mathbb{R}^3$$ nền). Các integrands là cùng phức đồ thị xuất hiện trong khai triển Feynman của lý thuyết Chern–Simons—nay như dạng vi phân hội tụ (sau framing và regularize).

Đầu ra là một bất biến nút nhận giá trị trong một đại số sơ đồ đầy đủ. Mọi bất biến kiểu hữu hạn phân tố qua nó; đó là nghĩa của **phổ dụng**. Tích phân linking cổ điển của Gauss là tổ tiên đơn giản nhất.

**Công lao.** Vassiliev đặt filtration kiểu hữu hạn; Bar-Natan và những người khác làm tổ hợp dùng được; Witten gợi một nguồn path-integral Chern–Simons cho bất biến; Kontsevich cho một xây dựng toán học hiện thực hóa đối tượng phổ dụng. Gạch Fields là xây dựng ấy, không phải tuyên bố lý thuyết nút bắt đầu năm 1993.

---

## 4. Lượng tử hóa formal các đa tạp Poisson

Một **đa tạp Poisson** $$(M,\pi)$$ mang một bivector $$\pi$$ sao cho $$\{f,g\}=\langle\pi,df\wedge dg\rangle$$ là móc Lie trên $$C^\infty(M)$$ thỏa quy tắc Leibniz. Đa tạp symplectic là trường hợp không thoái hóa; cấu trúc Lie–Poisson trên đối ngẫu đại số Lie là trường hợp tuyến tính.

**Lượng tử hóa biến dạng** hỏi một tích sao formal—một tích song tuyến trên $$C^\infty(M)[\![\hbar]\!]$$—

$$
f\star g=fg+\hbar B_1(f,g)+\hbar^2 B_2(f,g)+\cdots,
$$

kết hợp, rút về tích từng điểm tại $$\hbar=0$$, và thỏa

$$
f\star g-g\star f=i\hbar\{f,g\}+O(\hbar^2).
$$

Tồn tại trên đa tạp symplectic đã biết (De Wilde–Lecomte, Fedosov). Trường hợp Poisson còn mở: không có bản đồ Darboux trong đó $$\pi$$ hằng, nên một công thức địa phương không đủ trừ khi nó **tự nhiên** theo $$\pi$$.

**Định lý formality** của Kontsevich nói rằng đại số Lie vi phân phân bậc các Hochschild cochain của $$C^\infty(M)$$ là formal: nó quasi-đẳng cấu với đối đồng điều của nó, đại số Lie các đa vector trường với móc Schouten–Nijenhuis. Formality kéo theo mọi cấu trúc Poisson (một phần tử Maurer–Cartan trong đa vector trường) nâng lên thành tích sao. Chứng minh cung cấp một **công thức đồ thị tường minh**: tổng trên một số đồ thị admissible, mỗi cái được trọng bằng một tích phân không gian cấu hình trên nửa mặt phẳng trên, của các toán tử hai vi phân xây từ $$\pi$$.

Bài lưu hành như bản thảo 1997 (arXiv:q-alg/9709040) và in trong *Letters in Mathematical Physics* 66 (2003). “Formal” nghĩa theo tham số chuỗi lũy thừa hình thức $$\hbar$$; không phải tuyên bố về hội tụ giải tích của chuỗi, cũng không về lượng tử hóa không gian Hilbert của mọi đa tạp Poisson.

**Slogan.** Mọi móc Poisson là bóng bậc nhất của một tích sao; Kontsevich viết tích như khai triển Feynman có biên độ là số từ không gian cấu hình.

---

## 5. Các chương trình liên quan không phải gạch thứ ba

**Đối xứng gương đồng điều (HMS).** Trong bài ICM 1994 (Zürich; arXiv:alg-geom/9411018), Kontsevich đề xuất rằng đối xứng gương nên là một tương đương phạm trù: phạm trù derived các sheaf chỉnh hình trên Calabi–Yau $$X$$ tương đương phạm trù Fukaya của một gương $$Y$$ (đổi A-model / B-model). Đề xuất ấy tổ chức một thế hệ hình học symplectic và đại số; nhiều trường hợp nay là định lý (của nhiều người). Nó **không** phải mục thứ ba của citation 1998, và nói Kontsevich “giải đối xứng gương” là sai. Khóa học đã coi HMS như chương trình còn mở trong [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/).

**Tích phân motivic.** Kontsevich phác thảo trong bài giảng Orsay 1995; **Denef–Loeser** phát triển lý thuyết đã xuất bản. Láng giềng và sau—không phải gạch Fields.

**Map ổn định.** Compact hóa map từ đường cong của Kontsevich trung tâm với lý thuyết Gromov–Witten. Báo cáo ICM 1998 của Taubes thảo luận nó; citation chính thức không biến nó thành mục giải thưởng thứ ba.

---

## 6. Vì sao Huy chương Fields

Huy chương 1998 nằm trong những giải thưởng **từ điển**: đồ thị ruy-băng $$\leftrightarrow$$ giao tautological; đồ thị Feynman $$\leftrightarrow$$ bất biến nút; đồ thị admissible $$\leftrightarrow$$ tích sao. Mỗi từ điển biến một hàm sinh gợi từ vật lý thành một chứng minh.

Với khóa học này, Kontsevich là chân dung vật lý toán như **nguồn cung định lý**, không như ẩn dụ. Cùng bản năng đồ thị-tích phân xuất hiện ba lần, trong ba mệnh đề IMU. Các chương trình sau (HMS, motive) cho thấy bản năng không dừng năm 1998; chúng không viết lại citation.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Kontsevich giải đối xứng gương.” | Ông đề xuất HMS năm 1994; đó là chương trình, với định lý ở nhiều trường hợp của nhiều tác giả. |
| “Fields 1998 = đối xứng gương đồng điều.” | Gạch thứ ba chính thức là lượng tử hóa formal các đa tạp Poisson. |
| “Giả thuyết Witten phân loại mọi đường cong.” | Nó ràng buộc các số giao $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ qua KdV. |
| “Tích phân Kontsevich là đa thức Jones.” | Nó là bất biến kiểu hữu hạn phổ dụng; Jones là một trong nhiều chuyên biệt / trích xuất. |
| “Lượng tử hóa formal là cơ học lượng tử không gian Hilbert.” | Đó là biến dạng kết hợp trên $$\mathbb{R}[\![\hbar]\!]$$; giải tích hội tụ là chuyện riêng. |
| “Tích phân motivic là kết quả Fields 1998.” | Công trình láng giềng sau (bài giảng Kontsevich; Denef–Loeser). |

---

## Bài tập

1. Viết citation 1998 từ trí nhớ thành ba gạch. Mỗi gạch thuộc lĩnh vực nào?
2. Lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ là gì, ở mức slogan? Vì sao một số giao cần compact hóa?
3. Trong chứng minh đồ thị ruy-băng, cái gì được đồng nhất với cái gì? (Hình học metric / Strebel vs tích phân ma trận.)
4. **Phổ dụng** nghĩa là gì đối với một bất biến Vassiliev? Ghi công Vassiliev và Bar-Natan trong câu trả lời.
5. Viết hai tiên đề đầu của một tích sao (giới hạn $$\hbar=0$$; giao hoán tử vs Poisson). Vì sao trường hợp Poisson khó hơn trường hợp symplectic?
6. **Luyện độ chính xác.** Lấy một câu nói Kontsevich “chứng minh đối xứng gương.” Thay bằng hai câu: một về HMS 1994, một về gạch thứ ba 1998.
7. Lướt hai trang đầu arXiv:q-alg/9709040 hoặc arXiv:alg-geom/9411018 (chọn một) và liệt kê năm từ khóa.
8. **Seminar mở rộng.** “Phức đồ thị với tích phân không gian cấu hình” xuất hiện trong *cả* bất biến nút *và* tích sao thế nào? Một đoạn cẩn thận; đừng bịa một định lý đồng nhất chúng.

---

## Liên kết

- Trang IMU Fields Medal: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia — Maxim Kontsevich: [https://en.wikipedia.org/wiki/Maxim_Kontsevich](https://en.wikipedia.org/wiki/Maxim_Kontsevich)
- Kontsevich, lượng tử hóa biến dạng (arXiv:q-alg/9709040): [https://arxiv.org/abs/q-alg/9709040](https://arxiv.org/abs/q-alg/9709040)
- Kontsevich, đại số đồng điều của đối xứng gương (arXiv:alg-geom/9411018): [https://arxiv.org/abs/alg-geom/9411018](https://arxiv.org/abs/alg-geom/9411018)
- AMS Notices, “The Mathematical Work of the 1998 Fields Medalists”: [https://www.ams.org/notices/199901/fields.pdf](https://www.ams.org/notices/199901/fields.pdf)
- Tìm arXiv — Kontsevich Witten moduli: [https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all](https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 1998 — Maxim Kontsevich (khai mạc ICM Berlin; xem thêm Taubes, “The work of Maxim Kontsevich,” ICM 1998).
2. M. Kontsevich, “Intersection theory on the moduli space of curves and the matrix Airy function,” *Comm. Math. Phys.* 147 (1992).
3. E. Witten, hấp dẫn hai chiều và lý thuyết giao trên không gian moduli (giả thuyết).
4. M. Kontsevich, “Deformation quantization of Poisson manifolds,” *Lett. Math. Phys.* 66 (2003); bản thảo q-alg/9709040.
5. V. Vassiliev, bất biến nút kiểu hữu hạn; D. Bar-Natan, hệ trọng và phức sơ đồ.
6. M. Kontsevich, “Homological algebra of mirror symmetry,” *Proc. ICM Zürich 1994* — chương trình liên quan, không phải gạch thứ ba 1998.
7. J. Denef và F. Loeser, các bài về tích phân motivic (sau bài giảng Orsay của Kontsevich).
8. Khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/).

---

## Hướng đi tiếp

- Đọc một bài giảng hiện đại về lớp tautological trên $$\overline{\mathcal{M}}_{g,n}$$ để thấy Witten–Kontsevich *không* tính gì.
- Nếu tiếp tục sang HMS, giữ sổ hai cột: “đề xuất 1994” vs “định lý do các tác giả sau chứng minh.”
