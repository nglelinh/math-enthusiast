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

*Tạm dịch: vì những đóng góp cho hình học đại số, tôpô và vật lý toán, trong đó có chứng minh giả thuyết Witten về số giao trên không gian moduli các đường cong ổn định, xây dựng bất biến Vassiliev phổ dụng của nút, và lượng tử hóa hình thức các đa tạp Poisson.*

Lời trao giải nêu ba kết quả. Nhìn lại từ những năm 2020, người ta dễ thay danh sách này bằng những chủ đề nổi tiếng về sau như đối xứng gương đồng điều, tích phân motivic, hiện tượng vượt tường (wall-crossing). Các chương trình đó có thật, và một số là của Kontsevich. Nhưng chúng **không** nằm trong lời trao giải năm 1998. Bài này đi theo đúng ba kết quả chính thức: **giả thuyết Witten** trên $$\overline{\mathcal{M}}_{g,n}$$, **bất biến Vassiliev phổ dụng**, và **lượng tử hóa biến dạng** các đa tạp Poisson. Đối xứng gương đồng điều chỉ được nhắc như một đề xuất liên quan tại ICM 1994, không phải như một bài toán "đã được giải".

Kontsevich (sinh năm 1964) là giáo sư thường trực tại Institut des Hautes Études Scientifiques (IHÉS). Ông làm việc ở chỗ giao nhau của hình học đại số, tôpô và vật lý toán. Huy chương ghi nhận các công trình ở vùng giao đó trong thập niên 1990, chứ không phải toàn bộ sự nghiệp của ông.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhớ lời trao giải năm 1998 gồm **ba** kết quả, và không thay kết quả thứ ba bằng đối xứng gương đồng điều.
- Phát biểu ý chính của giả thuyết Witten: hàm sinh các số giao của lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ là một hàm tau của hệ KdV. Kontsevich chứng minh điều này bằng đồ thị ruy-băng và mô hình ma trận.
- Mô tả tích phân Kontsevich như **bất biến kiểu hữu hạn (Vassiliev) phổ dụng**, đồng thời ghi công Vassiliev và Bar-Natan cho phần lý thuyết xung quanh.
- Giải thích lượng tử hóa biến dạng: một tích sao làm biến dạng tích thông thường của hàm, sao cho số hạng bậc nhất của giao hoán tử cho lại móc Poisson. Định lý hình thức (formality) và công thức đồ thị của Kontsevich tạo ra tích này trên mọi đa tạp Poisson.
- Nhắc đến đối xứng gương đồng điều như một chương trình từ năm 1994, chưa hoàn thành, và không phải kết quả thứ ba của giải Fields.
- Đặt các công trình này lên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), nhưng không coi trực giác vật lý là chứng minh.

**Kiến thức nền.** Khái niệm không gian moduli của đường cong; móc Poisson trên $$\mathbb{R}^{2n}$$ hoặc trên đa tạp symplectic; đa thức Jones như một ví dụ về bất biến nút ngoài nhóm cơ bản. Biết giải tích phức và một giáo trình nhập môn hình học đại số sẽ có ích. Lý thuyết trường lượng tử thì không bắt buộc.

**Liên kết với các bài khác.** Bài [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) trình bày chương trình HMS, nên đọc *sau* và tách biệt với giải năm 1998. Bài [Pardon / symplectic]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) nói về phía phạm trù Fukaya, nơi HMS được sử dụng.

---

## 1. Vì sao nên bám theo danh sách năm 1998

Ảnh hưởng của một người đoạt giải thường kéo dài hơn lời trao giải. Ảnh hưởng về sau của Kontsevich rất lớn: đối xứng gương đồng điều thành một lĩnh vực riêng; tích phân motivic (bài giảng ở Orsay năm 1995, rồi Denef–Loeser phát triển) thành công cụ trong lý thuyết kỳ dị; ánh xạ ổn định và lý thuyết Gromov–Witten làm thay đổi hình học đếm. Nếu một khóa học gộp tất cả vào "Fields 1998" thì sẽ sai về lịch sử.

Lời trao giải chính thức đã đủ tham vọng. Nó ghi nhận ba việc: chứng minh một giả thuyết của Witten về lý thuyết giao trên không gian moduli các đường cong ổn định; xây dựng một bất biến nút kiểu hữu hạn phổ dụng; và lượng tử hóa mọi đa tạp Poisson ở mức hình thức. Hình học đại số, tôpô và vật lý toán ở đây không phải ba sở thích rời nhau. Cả ba kết quả đều đến từ cùng một kỹ thuật: tổng trên đồ thị, với trọng số là tích phân.

---

## 2. Giả thuyết Witten: số giao trên $$\overline{\mathcal{M}}_{g,n}$$

Gọi $$\overline{\mathcal{M}}_{g,n}$$ là compact hóa Deligne–Mumford của không gian moduli các đường cong giống $$g$$ với $$n$$ điểm đánh dấu. Trên không gian này có các phân thớ đường tautological $$\mathbb{L}_i$$, với thớ là đường đối tiếp xúc (cotangent line) tại điểm đánh dấu thứ $$i$$. Lớp Chern thứ nhất của chúng gọi là các **lớp $$\psi$$**. Các số giao

$$
\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g=\int_{\overline{\mathcal{M}}_{g,n}}\psi_1^{d_1}\cdots\psi_n^{d_n}
$$

là những bất biến số đơn giản nhất của vành tautological (quy ước: số giao bằng $$0$$ trừ khi tổng các bậc bằng số chiều $$3g-3+n$$).

**Giả thuyết Witten** (đầu thập niên 1990) khẳng định hàm sinh của các số này là một hàm tau của hệ **Korteweg–de Vries (KdV)**. Nói cách khác, các số giao thỏa một hệ phương trình đạo hàm riêng, liên quan đến các ràng buộc Virasoro. Giả thuyết xuất phát từ hấp dẫn lượng tử hai chiều: hai cách mô tả mặt ngẫu nhiên, một bằng mô hình ma trận (tổ hợp) và một bằng hình học, phải cho cùng kết quả.

**Chứng minh của Kontsevich** (*Intersection theory on the moduli space of curves and the matrix Airy function*, *Comm. Math. Phys.* 147, 1992) đồng nhất lý thuyết giao với một khai triển tổ hợp trên **đồ thị ruy-băng**. Công cụ là vi phân Strebel: một mêtric đặc biệt cắt đường cong thành một đồ thị "béo". Khi đó hàm sinh trở thành tích phân ma trận Airy, mà tích phân này đã được biết là thỏa KdV. Như vậy bài toán hình học được đưa về một mô hình ma trận có tính khả tích cổ điển.

**Tóm tắt.** Witten dự đoán các số giao tautological trên không gian moduli đường cong tuân theo hệ KdV. Kontsevich đưa ra một bộ từ điển bằng đồ thị ruy-băng, biến dự đoán đó thành một phép tính.

Đây là kết quả thuộc hình học đại số. Nó không phân loại mọi đường cong. Nó là định lý về một họ số cụ thể trên $$\overline{\mathcal{M}}_{g,n}$$.

---

## 3. Bất biến Vassiliev phổ dụng và không gian cấu hình

**Vassiliev** (đầu thập niên 1990) đưa ra các bất biến kiểu hữu hạn của nút. Đó là các bất biến bằng $$0$$ trên mọi nút kỳ dị có đủ nhiều điểm kép; tương đương, sự phụ thuộc của bất biến vào các lần đổi chỗ bắt chéo là đa thức có bậc bị chặn. **Bar-Natan** hệ thống hóa phần tổ hợp: hệ trọng số, sơ đồ dây (chord diagram), và mối liên hệ với đại số Lie cũng như với các hệ số của đa thức Jones.

Điều còn thiếu là một công cụ giải tích **phổ dụng**, tạo ra mọi bất biến kiểu hữu hạn từ một cách xây dựng duy nhất. Kontsevich đưa ra công cụ đó: **tích phân Kontsevich**, xây từ các tích phân lặp trên không gian cấu hình các điểm nằm trên nút (và, trong cách nhìn nhiễu loạn của lý thuyết Chern–Simons, cả các điểm trong $$\mathbb{R}^3$$ xung quanh). Biểu thức dưới dấu tích phân dùng đúng các đồ thị xuất hiện trong khai triển Feynman của lý thuyết Chern–Simons, nhưng giờ là những dạng vi phân hội tụ thật sự (sau khi chọn framing và chính quy hóa).

Kết quả là một bất biến nút nhận giá trị trong một đại số sơ đồ đầy đủ. Mọi bất biến kiểu hữu hạn đều đi qua nó; đó là nghĩa của chữ **phổ dụng**. Tích phân số móc nối (linking number) cổ điển của Gauss là ví dụ đơn giản nhất của kiểu công thức này.

**Ghi công.** Vassiliev đưa ra lọc kiểu hữu hạn; Bar-Natan và nhiều người khác phát triển phần tổ hợp để dùng được; Witten gợi ý rằng các bất biến có nguồn gốc từ tích phân đường Chern–Simons; Kontsevich cho một cách xây dựng toán học hiện thực hóa đối tượng phổ dụng. Huy chương ghi nhận cách xây dựng đó, không phải nói rằng lý thuyết nút bắt đầu từ năm 1993.

---

## 4. Lượng tử hóa hình thức các đa tạp Poisson

Một **đa tạp Poisson** $$(M,\pi)$$ có một song vectơ (bivector) $$\pi$$ sao cho $$\{f,g\}=\langle\pi,df\wedge dg\rangle$$ là một móc Lie trên $$C^\infty(M)$$ thỏa quy tắc Leibniz. Đa tạp symplectic là trường hợp không suy biến. Cấu trúc Lie–Poisson trên không gian đối ngẫu của một đại số Lie là trường hợp tuyến tính.

**Lượng tử hóa biến dạng** đi tìm một tích sao hình thức, tức là một tích song tuyến tính trên $$C^\infty(M)[\![\hbar]\!]$$,

$$
f\star g=fg+\hbar B_1(f,g)+\hbar^2 B_2(f,g)+\cdots,
$$

có tính kết hợp, trở về tích thông thường khi $$\hbar=0$$, và thỏa

$$
f\star g-g\star f=i\hbar\{f,g\}+O(\hbar^2).
$$

Trên đa tạp symplectic, sự tồn tại đã được biết (De Wilde–Lecomte, Fedosov). Trường hợp Poisson thì còn mở. Lý do: không có tọa độ Darboux trong đó $$\pi$$ là hằng, nên một công thức địa phương là chưa đủ, trừ khi công thức đó **tự nhiên** theo $$\pi$$.

**Định lý hình thức (formality)** của Kontsevich nói rằng đại số Lie vi phân phân bậc của các đối xích Hochschild của $$C^\infty(M)$$ là hình thức: nó tựa đẳng cấu (quasi-isomorphic) với đối đồng điều của chính nó, tức là đại số Lie các trường đa vectơ với móc Schouten–Nijenhuis. Từ đó suy ra mọi cấu trúc Poisson (một phần tử Maurer–Cartan trong các trường đa vectơ) đều nâng được thành một tích sao. Chứng minh còn cho một **công thức đồ thị tường minh**: tổng trên các đồ thị "chấp nhận được" (admissible), mỗi đồ thị có trọng số là một tích phân trên không gian cấu hình ở nửa mặt phẳng trên, nhân với một toán tử song vi phân xây từ $$\pi$$.

Bài báo được lưu hành dưới dạng bản thảo năm 1997 (arXiv:q-alg/9709040) và in trên *Letters in Mathematical Physics* 66 (2003). "Hình thức" ở đây nghĩa là làm việc với chuỗi lũy thừa hình thức theo $$\hbar$$. Kết quả không nói gì về sự hội tụ của chuỗi, cũng không nói về lượng tử hóa trên không gian Hilbert cho mọi đa tạp Poisson.

**Tóm tắt.** Mọi móc Poisson là phần bậc nhất của một tích sao. Kontsevich viết tích này như một khai triển Feynman, với các hệ số là những con số lấy từ tích phân trên không gian cấu hình.

---

## 5. Các chương trình liên quan nhưng không phải kết quả thứ ba

**Đối xứng gương đồng điều (HMS).** Trong báo cáo tại ICM 1994 (Zürich; arXiv:alg-geom/9411018), Kontsevich đề xuất rằng đối xứng gương nên được hiểu là một tương đương phạm trù: phạm trù dẫn xuất các bó chỉnh hình trên một đa tạp Calabi–Yau $$X$$ tương đương với phạm trù Fukaya của một đa tạp gương $$Y$$ (đổi vai mô hình A và mô hình B). Đề xuất này định hướng cho cả một thế hệ nghiên cứu hình học symplectic và đại số. Nhiều trường hợp nay đã thành định lý, do nhiều tác giả chứng minh. Nhưng nó **không** phải mục thứ ba của lời trao giải năm 1998, và nói Kontsevich "đã giải đối xứng gương" là sai. Khóa học xem HMS là một chương trình còn mở trong bài [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/).

**Tích phân motivic.** Kontsevich phác thảo ý tưởng trong bài giảng ở Orsay năm 1995; **Denef–Loeser** phát triển và công bố lý thuyết hoàn chỉnh. Đây là công trình liên quan và đến sau, không thuộc giải Fields.

**Ánh xạ ổn định.** Cách compact hóa không gian các ánh xạ từ đường cong của Kontsevich là trung tâm của lý thuyết Gromov–Witten. Báo cáo của Taubes tại ICM 1998 có bàn về nó, nhưng lời trao giải chính thức không đưa nó thành một mục riêng.

---

## 6. Vì sao là Huy chương Fields

Huy chương năm 1998 ghi nhận những bộ **từ điển**: đồ thị ruy-băng $$\leftrightarrow$$ số giao tautological; đồ thị Feynman $$\leftrightarrow$$ bất biến nút; đồ thị chấp nhận được $$\leftrightarrow$$ tích sao. Mỗi từ điển biến một hàm sinh do vật lý gợi ý thành một chứng minh.

Trong khóa học này, Kontsevich là ví dụ cho thấy vật lý toán có thể **sinh ra định lý**, chứ không chỉ cho phép so sánh hình ảnh. Cùng một kỹ thuật đồ thị và tích phân xuất hiện ba lần, trong ba mệnh đề của IMU. Các chương trình về sau (HMS, motive) cho thấy hướng suy nghĩ đó còn tiếp tục sau năm 1998, nhưng chúng không thay đổi lời trao giải.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Kontsevich giải đối xứng gương." | Ông đề xuất HMS năm 1994; đó là một chương trình, với nhiều trường hợp đã được nhiều tác giả chứng minh. |
| "Fields 1998 = đối xứng gương đồng điều." | Kết quả thứ ba chính thức là lượng tử hóa hình thức các đa tạp Poisson. |
| "Giả thuyết Witten phân loại mọi đường cong." | Nó mô tả các số giao của lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ thông qua hệ KdV. |
| "Tích phân Kontsevich là đa thức Jones." | Nó là bất biến kiểu hữu hạn phổ dụng; đa thức Jones là một trong nhiều bất biến rút ra được từ nó. |
| "Lượng tử hóa hình thức là cơ học lượng tử trên không gian Hilbert." | Đó là một biến dạng kết hợp trên $$\mathbb{R}[\![\hbar]\!]$$; sự hội tụ là vấn đề riêng. |
| "Tích phân motivic là kết quả được Fields 1998." | Đó là công trình liên quan, đến sau (bài giảng của Kontsevich; Denef–Loeser). |

---

## Bài tập

1. Viết lại lời trao giải năm 1998 thành ba ý. Mỗi ý thuộc lĩnh vực nào?
2. Nói ngắn gọn: lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ là gì? Vì sao muốn có số giao thì cần compact hóa?
3. Trong chứng minh bằng đồ thị ruy-băng, đối tượng nào được đồng nhất với đối tượng nào? (Hình học mêtric / vi phân Strebel so với tích phân ma trận.)
4. Với bất biến Vassiliev, **phổ dụng** nghĩa là gì? Trong câu trả lời, ghi công Vassiliev và Bar-Natan.
5. Viết hai tiên đề đầu tiên của tích sao (giới hạn khi $$\hbar=0$$; giao hoán tử so với móc Poisson). Vì sao trường hợp Poisson khó hơn trường hợp symplectic?
6. **Luyện phát biểu chính xác.** Lấy câu "Kontsevich chứng minh đối xứng gương". Thay bằng hai câu: một câu về HMS năm 1994, một câu về kết quả thứ ba năm 1998.
7. Đọc lướt hai trang đầu của arXiv:q-alg/9709040 hoặc arXiv:alg-geom/9411018 (chọn một) và liệt kê năm từ khóa.
8. **Mở rộng.** Ý tưởng "tổng trên đồ thị với tích phân trên không gian cấu hình" xuất hiện trong *cả* bất biến nút *lẫn* tích sao như thế nào? Viết một đoạn cẩn thận; đừng bịa ra một định lý đồng nhất hai thứ này.

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

- Đọc một bài giảng hiện đại về các lớp tautological trên $$\overline{\mathcal{M}}_{g,n}$$ để thấy định lý Witten–Kontsevich *không* tính được những gì.
- Nếu học tiếp sang HMS, hãy ghi chép thành hai cột: "đề xuất năm 1994" và "định lý do các tác giả sau chứng minh".

## Video tham khảo

- **Xem trước**: [HLF Laureate Portraits: Maxim Kontsevich](https://www.youtube.com/watch?v=1CXvSRQVoZY) (Heidelberg Laureate Forum, tiếng Anh). Video chân dung ngắn, Kontsevich kể về con đường và cách làm toán của mình. Phù hợp để làm quen trước khi đọc bài.
- [Maxim Kontsevich | On the History of quantum cohomology and homological mirror symmetry](https://www.youtube.com/watch?v=Ml2x5NnEQ1I) (Harvard CMSA, tiếng Anh). Kontsevich kể lại lịch sử đối đồng điều lượng tử và đối xứng gương đồng điều. Nên xem sau khi đọc mục 5, để phân biệt rõ đề xuất HMS năm 1994 với ba kết quả của giải năm 1998.
