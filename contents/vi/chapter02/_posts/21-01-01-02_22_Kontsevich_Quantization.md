---
layout: post
title: "Maxim Kontsevich: Witten, Vassiliev và Lượng tử hóa (Huy chương Fields 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Maxim Kontsevich** nhận **Huy chương Fields 1998** vì những đóng góp cho hình học đại số, tôpô và vật lý toán, gồm chứng minh giả thuyết Witten về các số giao trên không gian moduli các đường cong ổn định, xây dựng bất biến Vassiliev phổ dụng của nút, và lượng tử hóa hình thức các đa tạp Poisson. Huy chương **không** đặt tên một “định lý Kontsevich” duy nhất. Nó đặt tên ba xây dựng đã hoàn tất, ngồi ở những phòng khác nhau của hình học—moduli đường cong, bất biến nút hữu hạn kiểu, và lượng tử hóa biến dạng—và chia sẻ một khẩu vị biến hàm sinh của nhà vật lý thành một đối tượng đại số hoặc tổ hợp chặt chẽ.

Bài này dành cho người học đã gặp không gian moduli lần đầu hoặc ngoặc Poisson lần đầu và muốn nắm kiến trúc của ba mục trong trích dẫn ấy. Bài **không** coi đối xứng gương đồng điều là one-liner chính thức 1998 (đó đã là đề xuất ICM 1994), cũng không coi tích phân motivic là khẩu hiệu Fields (một ý tưởng Kontsevich sau hơn, được phát triển với Denef–Loeser). Những láng giềng ấy xuất hiện trong một mục riêng để công lao được giữ trung thực.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Thuộc **ba mục** của trích dẫn 1998 mà không gộp chúng thành một định lý.
- Phát biểu giả thuyết Witten ở mức khẩu hiệu: một hàm sinh các số giao trên $$\overline{\mathcal{M}}_{g,n}$$ thỏa hệ KdV (và phương trình dây).
- Mô tả **tích phân Kontsevich** như bất biến hữu hạn kiểu (Vassiliev) phổ dụng của nút, xây từ các tích phân lặp dọc theo một nút.
- Giải thích **lượng tử hóa biến dạng hình thức**: một tích sao trên các hàm làm biến dạng tích từng điểm, với giao hoán tử bậc nhất cho bởi ngoặc Poisson.
- Đặt đối xứng gương đồng điều và tích phân motivic như **các chương trình Kontsevich liên quan**, không phải danh sách Fields chính thức.

**Kiến thức nền.** Ý rằng không gian moduli tham số hóa các đối tượng hình học; ngoặc Poisson trên các hàm trên $$\mathbb{R}^{2n}$$ hoặc trên một đa tạp symplectic; sự phân biệt giữa một nút và sơ đồ của nó. Không cần khóa operad hay $$A_\infty$$ trước đó.

**Liên kết seminar.** LO1 / LO4 (chương trình khó; hàm sinh vật lý ↔ xây dựng đại số). Ghép với [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) cho một văn hóa moduli đường cong khác, và với [Pardon]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) nếu sau này bạn gặp phạm trù Fukaya như người tiêu thụ đối xứng gương.

---

## 1. Ba mục, không phải một định lý

Các tường thuật phổ thông đôi khi bịa một “định lý Kontsevich” ma giải thích lý thuyết dây, nút và lượng tử hóa trong một câu. Văn bản IMU kỷ luật hơn. Nó liệt kê ba thành tựu:

1. Chứng minh **giả thuyết Witten** về các số giao của lớp tautological trên không gian moduli các đường cong ổn định.
2. Xây dựng **bất biến Vassiliev phổ dụng** của nút.
3. **Lượng tử hóa hình thức** các đa tạp Poisson.

Mỗi mục có định nghĩa, tiền bối và dòng công trình tiếp theo riêng. Điều chúng chia sẻ là một phương pháp: viết một hàm sinh hoặc chuỗi hình thức mà hệ số là hình học, rồi sản xuất một máy tổ hợp hoặc đồng điều tính chúng và chứng minh các đồng nhất kỳ vọng.

**Khẩu hiệu.** Huy chương 1998 là **trích dẫn bộ ba**, không phải định lý thống nhất.

---

## 2. Giả thuyết Witten và moduli đường cong

Gọi $$\overline{\mathcal{M}}_{g,n}$$ là compact hóa Deligne–Mumford của không gian moduli các đường cong giống $$g$$ với $$n$$ điểm đánh dấu. Trên orbifold này sống các bundle đường tautological $$\mathbb{L}_i$$ mà lớp Chern thứ nhất $$\psi_i=c_1(\mathbb{L}_i)$$ đo đường cotangent tại dấu thứ $$i$$. Các số giao

$$
\langle\tau_{k_1}\cdots\tau_{k_n}\rangle_g=\int_{\overline{\mathcal{M}}_{g,n}}\psi_1^{k_1}\cdots\psi_n^{k_n}
$$

đóng gói hình học đếm của những lớp ấy. Witten giả thuyết rằng hàm sinh lắp từ các số này là một tau-function của hệ KdV—tương đương, rằng các giao thỏa một hệ PDE đệ quy do hấp dẫn hai chiều dự đoán.

Kontsevich chứng minh giả thuyết (Comm. Math. Phys., 1992) bằng cách, cho mục đích các giao này, thay không gian moduli bằng một mô hình tổ hợp: đồ thị ruy-băng (hoặc, tương đương, vi phân Strebel) mà các ô tính các tích phân $$\psi$$, cùng một tích phân Airy ma trận mà khai triển tiệm cận tái tạo hàm sinh. Chứng minh là cây cầu giữa hình học đại số và mô hình ma trận, không phải “phân loại mọi đường cong.”

**Độ chính xác.** Witten phát biểu giả thuyết; Kontsevich chứng minh nó. Các chứng minh sau (Okounkov–Pandharipande, Mirzakhani, và những người khác) viết lại cùng các đồng nhất bằng ngôn ngữ khác. Thể tích Weil–Petersson của Mirzakhani là câu chuyện moduli láng giềng, không phải sự thay thế bài 1992.

---

## 3. Tích phân Kontsevich và bất biến Vassiliev

Các bất biến hữu hạn kiểu của Vassiliev đối với nút triệt tiêu trên các sơ đồ có đủ điểm kép; chúng tạo thành một đại số đã lọc mà mảnh phân bậc liên kết được mô tả bởi các hệ trọng trên sơ đồ dây. Một bất biến Vassiliev **phổ dụng** là bất biến nút nhận giá trị trong một đại số sơ đồ đầy đủ, chuyên biệt hóa thành mọi bất biến hữu hạn kiểu một khi chọn một hệ trọng.

Kontsevich xây một bất biến như vậy bằng công thức tích phân lặp (**tích phân Kontsevich**): người ta nhúng nút vào không gian, viết một chuỗi tích phân không gian cấu hình dọc các cặp điểm trên nút, và nhận giá trị trong một đại số sơ đồ dây. Sau chuẩn hóa thích hợp (và, trong câu chuyện đầy đủ, một associator Drinfeld để xử lý phiên bản có framing hoặc ngoặc), tích phân phổ dụng trên $$\mathbb{C}$$.

**Đừng viết** rằng Kontsevich “đã phân loại mọi nút.” Các bất biến hữu hạn kiểu không tách mọi nút; tích phân phổ dụng cho lớp đã lọc ấy, không phải bảng nút đầy đủ.

---

## 4. Lượng tử hóa hình thức các đa tạp Poisson

Một đa tạp Poisson $$(M,\pi)$$ mang một ngoặc song tuyến $$\{\,,\,\}$$ trên các hàm thỏa Jacobi và Leibniz. Lượng tử hóa biến dạng hỏi một tích sao

$$
f\star g=fg+\sum_{k\ge 1}h^k B_k(f,g)
$$

trên các chuỗi lũy thừa hình thức theo một tham số $$h$$ (thường viết $$\hbar$$), kết hợp, với

$$
f\star g-g\star f=h\{f,g\}+O(h^2).
$$

Với đa tạp symplectic, Fedosov và những người khác đã có xây dựng. Kontsevich chứng minh rằng **mọi** đa tạp Poisson đều nhận một tích sao hình thức chính tắc, cho bởi một tổng tường minh trên các đồ thị admissible: mỗi đồ thị đóng góp một toán tử hai vi phân mà hệ số là các co của $$\pi$$ và đạo hàm của nó. Động cơ sâu hơn là định lý **formality**: một tựa đẳng cấu $$L_\infty$$ giữa đại số Lie vi phân đã phân bậc của các đa vector và các đối chuỗi Hochschild của đại số hàm. Cấu trúc Poisson là phần tử Maurer–Cartan ở một phía; tích sao là phần tử Maurer–Cartan ở phía kia.

**Độ chính xác.** Định lý nói về chuỗi **hình thức** theo $$h$$. Tự nó không sinh một $$C^*$$-đại số của một đa tạp Poisson, cũng không “lượng tử hóa hấp dẫn.”

---

## 5. Công trình liên quan không phải one-liner 1998

Hai chương trình láng giềng dễ bị xếp nhầm hồ sơ.

**Đối xứng gương đồng điều.** Bài giảng ICM 1994 của Kontsevich đề xuất rằng đối xứng gương là một tương đương phạm trù: phạm trù Fukaya dẫn xuất của một đa tạp symplectic và phạm trù dẫn xuất các bó chỉnh hình trên một đa tạp phức gương. Đến 1998 đây đã là giả thuyết có ảnh hưởng và một chương trình nghiên cứu. Nó **không** phải một trong ba mục được nêu trong trích dẫn Fields. Hãy coi nó là công trình liên quan sau này trở thành một lĩnh vực riêng (xem chương đối xứng gương của khóa học).

**Tích phân motivic.** Trong một bài giảng năm 1995 Kontsevich gợi một lý thuyết tích phân nhận giá trị trong vành Grothendieck của các đa tạp, được thiết kế một phần để chứng minh rằng các đa tạp Calabi–Yau birational có cùng số Hodge. Denef và Loeser phát triển lý thuyết một cách có hệ thống. Đó là một ý tưởng lớn của Kontsevich; nó **không** phải one-liner 1998.

Khi viết một đoạn seminar, hãy nêu phòng thí nghiệm bạn muốn nói. Đừng để HMS hay motive đóng giả trích dẫn.

---

## 6. Vì sao là Huy chương Fields

Ba lý do đan vào nhau:

1. **Độ khó.** Mỗi mục giải hoặc xây điều cộng đồng đã đặt tên mà chưa hoàn tất: khẳng định KdV của Witten, một bất biến hữu hạn kiểu phổ dụng, một tích sao cho cấu trúc Poisson tùy ý.
2. **Tính trung tâm.** Moduli đường cong, tôpô lượng tử, và lý thuyết biến dạng là ba xa lộ của hình học cuối thế kỷ hai mươi; trích dẫn đặt Kontsevich trên cả ba.
3. **Khẩu hiệu trong sáng với phương pháp sâu.** “Chứng minh Witten; viết bất biến Vassiliev phổ dụng; lượng tử hóa mọi đa tạp Poisson” là danh sách một sinh viên nhớ được; mỗi chứng minh phát minh một máy (đồ thị ruy-băng, tích phân cấu hình, đồ thị formality).

Trong khóa này, Kontsevich ngồi cạnh các chân dung Fields khác hoàn tất **các chương trình đã đặt tên** chứ không phải một giả thuyết số duy nhất—và cạnh các chân dung sau tiêu thụ HMS mà không viết lại trích dẫn 1998.

---

## Nhầm lẫn thường gặp

| Khẳng định | Chữa lại |
|------------|----------|
| “Huy chương Fields là vì đối xứng gương đồng điều.” | HMS là đề xuất ICM 1994; trích dẫn 1998 liệt kê Witten, Vassiliev và lượng tử hóa. |
| “Có một định lý Kontsevich.” | Có một trích dẫn bộ ba cộng một kho sau lớn. |
| “Tích phân motivic là one-liner 1998.” | Đó là ý tưởng sau/liên quan, phát triển đặc biệt với Denef–Loeser. |
| “Tích phân Kontsevich phân loại nút.” | Nó phổ dụng đối với bất biến Vassiliev, không phải bộ phân loại đầy đủ. |
| “Lượng tử hóa biến dạng là biểu diễn không gian Hilbert.” | Mục 1998 là tích sao hình thức, không phải lý thuyết biểu diễn giải tích. |

---

## Bài tập

1. Viết ba mục trích dẫn 1998 từ trí nhớ. Tự kiểm với đoạn mở đầu.
2. Một số giao $$\langle\tau_{k_1}\cdots\tau_{k_n}\rangle_g$$ quên gì và giữ gì về một không gian moduli đường cong?
3. Trong một đoạn: vì sao “bất biến Vassiliev phổ dụng” không nghĩa là “bất biến nút đầy đủ”?
4. Viết hai hạng tử đầu của một tích sao và điều kiện giao hoán tử khớp ngoặc Poisson.
5. **Luyện độ chính xác.** Tìm một câu phổ thông nói Kontsevich “đoạt Huy chương Fields vì đối xứng gương.” Viết lại thành hai câu chính xác.
6. **Kéo giãn seminar.** So sánh trích dẫn bộ ba này với [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) về moduli đường cong: một bên chứng minh khẳng định hàm sinh Witten; bên kia đo thể tích Weil–Petersson. Điều gì được chia sẻ, điều gì thì không?

---

## Nguồn video và đọc thêm

1. **Trích dẫn IMU** — Fields Medals 1998 (ICM Berlin): one-liner chính thức như trích ở trên; xem các trang Huy chương Fields của IMU và kỷ yếu ICM 1998.
2. **Bài gốc** — Kontsevich, *Intersection theory on the moduli space of curves and the matrix Airy function* (1992); *Deformation quantization of Poisson manifolds* (bản thảo 1997; Lett. Math. Phys., 2003).
3. **Liên quan, không phải trích dẫn** — Kontsevich, *Homological algebra of mirror symmetry* (ICM 1994); Denef–Loeser về tích phân motivic.

**Nhắc trạng thái:** Ba xây dựng đã đặt tên—**không** phải một định lý duy nhất, và **không** phải “Fields vì HMS.”

---

## Tài liệu tham khảo

1. Trích dẫn Huy chương Fields 1998 của IMU — Maxim Kontsevich (hình học đại số, tôpô, vật lý toán; Witten, Vassiliev, lượng tử hóa Poisson).
2. **M. Kontsevich** — Intersection theory on the moduli space of curves and the matrix Airy function (Comm. Math. Phys., 1992).
3. **M. Kontsevich** — Các bất biến nút của Vassiliev / tích phân Kontsevich (đầu thập niên 1990).
4. **M. Kontsevich** — Deformation quantization of Poisson manifolds (1997/2003).
5. Láng giềng khóa học: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/); đối xứng gương như người tiêu thụ sau của bài ICM 1994, không phải danh sách 1998.

---

## Hướng đi tiếp

- Đọc một trình bày hiện đại về giả thuyết Witten (ví dụ một tổng quan so sánh Kontsevich, Okounkov–Pandharipande và Mirzakhani) và liệt kê đối tượng nào mỗi chứng minh coi là cơ bản.
- Phác, ở mức khẩu hiệu, vì sao formality của phức Hochschild sinh tích sao từ các song vector Poisson.
- Tùy chọn seminar A3: một trang xếp HMS, tích phân motivic và trích dẫn 1998 vào ba ngăn—mà không bịa “định lý chính” thứ tư.
