---
layout: post
title: "Luật hợp thành của Bhargava và hạng trung bình (Huy chương Fields 2014)"
chapter: '02'
order: 17
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Năm 1801, trong kiệt tác *Disquisitiones Arithmeticae*, Carl Friedrich Gauss viết ra hàng chục trang công thức dày đặc để mô tả một phép "nhân" bí ẩn giữa hai biểu thức bậc hai dạng $$ax^2 + bxy + cy^2$$ — gọi là **luật hợp thành Gauss**. Suốt đúng hai trăm năm sau đó, các nhà toán học ngỡ rằng quy luật kỳ diệu ấy chỉ là một phép màu độc nhất vô nhị ở bậc 2.

Rồi vào mùa hè năm 1998, một nghiên cứu sinh trẻ tuổi tại Princeton (đồng thời là tay trống tabla cừ khôi) tên là **Manjul Bhargava** ngồi xoay khối lập phương Rubik mini trong phòng ký túc xá và chợt nảy ra một ý tưởng làm rúng động giới lý thuyết số: nếu viết 8 số nguyên lên 8 đỉnh của một **khối lập phương $$2\times 2\times 2$$**, rồi cắt khối lập phương ấy theo 3 hướng (trên–dưới, trước–sau, trái–phải), bạn lập tức thu được đúng 3 dạng toàn phương nhị phân thỏa mãn luật hợp thành Gauss! Từ chiếc chìa khóa trực quan đó, Bhargava không chỉ viết lại Gauss trong vài dòng, mà còn khám phá ra **13 luật hợp thành bậc cao** mới, dùng chúng để đếm các trường số bậc $$2, 3, 4, 5$$, và cùng **Arul Shankar** chứng minh những định lý mang tính bước ngoặt về **hạng trung bình của đường cong elliptic** — thành tựu mang về cho ông **Huy chương Fields 2014**.

Theo lời trích dẫn của IMU, giải thưởng dành cho việc *"phát triển những phương pháp mới mạnh mẽ trong hình học các số, và áp dụng chúng để đếm các vành hạng nhỏ và để chặn hạng trung bình của đường cong elliptic."* Cần nói rõ ngay từ đầu: Bhargava **không** chứng minh [giả thuyết Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), nhưng các kết quả của ông về **nhóm Selmer** và hạng trung bình đã lần đầu tiên cho thấy hành vi thống kê của đa số đường cong elliptic khớp ngoạn mục với những gì BSD dự đoán.

**Mạch bài học:** Kiến thức cần nhớ (tính tay hoàn chỉnh **khối lập phương $$2\times 2\times 2$$ Bhargava** cho biệt thức $$-23$$, hình học các số và ví dụ hạng $$0/1$$ của đường cong elliptic) → Đếm vành hạng $$2, 3, 4, 5$$ → Giải thích 4 bước: từ dạng bậc 4 nhị phân đến kích thước 2-Selmer $$= 3$$ và hạng trung bình bị chặn → Ghi nhận công lao & phân biệt với BSD.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tự tay kiểm tra phép cắt 3 chiều trên một **khối lập phương $$2\times 2\times 2$$ cụ thể** của Bhargava và tính ra ngay 3 dạng toàn phương cùng biệt thức $$D = -23$$.
- Giải thích **hình học các số** (đếm điểm lưới nguyên qua thể tích miền cơ bản) và vai trò của nó trong việc đếm vành hạng $$2, 3, 4, 5$$.
- Hiểu mạch 4 bước của **Bhargava–Shankar**: tham số hóa nhóm **2-Selmer** bằng dạng bậc 4 nhị phân → đếm quỹ đạo cho kích thước trung bình $$\#\mathrm{Sel}_2(E) = 3$$ → suy ra hạng trung bình $$\le 1{,}5$$ (rồi $$< 0{,}885$$).
- Phân biệt rõ **định lý đã chứng minh** (hạng trung bình bị chặn; tỷ lệ dương có hạng $$0$$ và hạng $$1$$) với **giả thuyết chưa chứng minh** (hạng trung bình bằng $$1/2$$; giả thuyết BSD).

**Kiến thức cần có.** Ma trận $$2\times 2$$, định thức, biệt thức $$b^2 - 4ac$$ và khái niệm nhóm hữu hạn sinh $$E(\mathbb{Q}) \simeq \mathbb{Z}^r \oplus E(\mathbb{Q})_{\mathrm{tors}}$$. Không cần biết trước lý thuyết trường lớp.

**Liên hệ với khóa học.** Câu chuyện về hạng gắn chặt với [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/). Các bài liên quan: [Tsimerman]({{ site.baseurl }}/contents/vi/chapter02/02_14_Tsimerman_Arithmetic/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/), [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/). Cùng năm 2014: [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

---

## Kiến thức cần nhớ: Hình học các số, Khối lập phương Bhargava và Đường cong elliptic

### 1. Tự tính tay Khối lập phương $$2\times 2\times 2$$ của Bhargava (Biệt thức $$D = -23$$!)
Đặt 8 số nguyên lên 8 đỉnh của một khối lập phương $$2\times 2\times 2$$, viết dưới dạng cặp hai mặt trước–sau $$M_1$$ và $$M_2$$:

$$
M_1 = \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad M_2 = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}.
$$

Bây giờ lập tổ hợp tuyến tính $$M_1 x + M_2 y$$ rồi lấy **âm định thức**:

$$
Q_1(x, y) \;=\; -\det\begin{pmatrix} -x + y & x + y \\ x + y & x - 2y \end{pmatrix}
\;=\; -\Bigl[(-x + y)(x - 2y) - (x + y)^2\Bigr]
\;=\; \mathbf{2x^2 - xy + 3y^2}.
$$

Hãy kiểm tra biệt thức của $$Q_1$$: $$D = (-1)^2 - 4(2)(3) = 1 - 24 = \mathbf{-23}$$!
Bây giờ bạn hãy cắt cùng khối lập phương đó theo hai chiều còn lại (trên–dưới và trái–phải): vì 8 số trên được chọn đối xứng hoàn toàn, cả ba lát cắt đều cho ra đúng ba dạng toàn phương $$Q_1 = Q_2 = Q_3 = 2x^2 - xy + 3y^2$$ có cùng biệt thức $$-23$$! Và trong nhóm lớp các dạng bậc hai biệt thức $$-23$$ (nhóm cyclic cấp 3 gồm $$x^2 + xy + 6y^2$$ và $$2x^2 \pm xy + 3y^2$$), tích của chúng đúng bằng phần tử đơn vị:

$$
Q_1 \cdot Q_2 \cdot Q_3 \;=\; Q_1^3 \;=\; 1!
$$

Tổng quát, với **mọi** khối lập phương 8 số nguyên bất kỳ, 3 lát cắt theo 3 chiều luôn sinh ra 3 dạng toàn phương nhị phân cùng biệt thức $$D$$ thỏa mãn $$Q_1 \cdot Q_2 \cdot Q_3 = 1$$ — rút gọn hàng chục trang công thức của Gauss thành đúng 3 dòng định thức $$2\times 2$$!

### 2. Hình học các số (Geometry of Numbers) là gì?
Bắt nguồn từ Hermann Minkowski cuối thế kỷ XIX, **hình học các số** biến bài toán đếm số nguyên thành bài toán **đo thể tích**: số điểm lưới nguyên $$\mathbb{Z}^n$$ nằm bên trong một miền hình học lớn gần bằng chính *thể tích* của miền đó (sai khác một phần sai số ở biên). Khi tham số hóa được các vành hoặc phần tử nhóm Selmer bằng các điểm nguyên trong một không gian vector (với tác động của nhóm $$\mathrm{SL}_n(\mathbb{Z})$$), ta chỉ cần tính thể tích miền cơ bản và khống chế các "đỉnh nhọn" (*cusp*) chạy ra vô tận!

### 3. Hạng của đường cong elliptic — Ví dụ cầm tay hạng $$0$$ và hạng $$1$$
Xét đường cong elliptic $$E: y^2 = x^3 + Ax + B$$ trên $$\mathbb{Q}$$. Theo Định lý Mordell–Weil, tập nghiệm hữu tỷ tạo thành nhóm giao hoán hữu hạn sinh $$E(\mathbb{Q}) \simeq \mathbb{Z}^{r_E} \oplus E(\mathbb{Q})_{\mathrm{tors}}$$, trong đó $$r_E \ge 0$$ là **hạng đại số**:
- **Hạng $$r = 0$$:** Đường cong $$y^2 = x^3 - x$$ chỉ có đúng 4 điểm hữu tỷ là $$(0, 0), (1, 0), (-1, 0)$$ và điểm ở vô cực (toàn bộ là phần xoắn!).
- **Hạng $$r = 1$$:** Đường cong $$y^2 = x^3 - 2$$ có điểm hữu tỷ $$P = (3, 5)$$ (kiểm tra: $$5^2 = 25 = 3^3 - 2$$!). Kẻ tiếp tuyến tại $$P$$ cắt đường cong tại điểm mới $$2P = \left(\frac{129}{100}, -\frac{383}{1000}\right)$$, cứ lặp mãi sinh ra **vô hạn** nghiệm hữu tỷ!

---

## 1. Đếm các vành hạng $$2, 3, 4, 5$$ bằng Luật hợp thành bậc cao

Một **vành hạng $$n$$** trên $$\mathbb{Z}$$ (như vành số nguyên của trường số bậc $$n$$) có biệt thức $$\mathrm{disc}$$. Bài toán đếm hỏi: có bao nhiêu lớp đẳng cấu với $$\vert\mathrm{disc}\vert < X$$ khi $$X \to \infty$$?

Trong luận án tiến sĩ (hướng dẫn bởi Andrew Wiles) và loạt 4 bài báo *Higher composition laws I–IV* trên *Annals of Mathematics* (2004–2008), Bhargava khám phá ra các **tham số hóa bằng quỹ đạo nguyên** cho mọi hạng nhỏ:
- **Hạng 2:** Khối lập phương $$2\times 2\times 2$$ (thu lại luật Gauss).
- **Hạng 3:** Dạng bậc ba nhị phân $$ax^3 + bx^2y + cxy^2 + dy^3$$ (mở rộng kết quả cổ điển Davenport–Heilbronn).
- **Hạng 4:** Cặp dạng toàn phương ba biến (cặp ma trận đối xứng $$3\times 3$$) — lần đầu tiên đếm chính xác tiệm cận mật độ trường bậc 4!
- **Hạng 5:** Bộ tứ dạng đối xứng lệch $$5\times 5$$ — lần đầu tiên đếm chính xác mật độ trường bậc 5!

Từ bậc $$6$$ trở đi hiện vẫn là bài toán mở lớn vì không còn không gian vector tiền thuần nhất tương ứng.

---

## 2. Giải thích: Bhargava và Shankar chặn "Hạng trung bình của đường cong elliptic" như thế nào?

Làm sao từ các phép tham số hóa đa thức, **Manjul Bhargava và Arul Shankar** lại chặn được hạng trung bình của *tất cả* các đường cong elliptic trên $$\mathbb{Q}$$ (một kết quả mà ngay cả Giả thuyết Riemann mở rộng trước đó cũng chưa chứng minh được)? Hãy theo dõi mạch 4 bước:

#### Bước 1: Thay nhóm Mordell–Weil khó tính bằng nhóm 2-Selmer hữu hạn
Tính trực tiếp hạng $$r_E$$ của đường cong elliptic cực kỳ khó. Thay vào đó, ta xét **nhóm 2-Selmer** $$\mathrm{Sel}_2(E)$$ — một nhóm hữu hạn luôn tính được bằng điều kiện địa phương tại từng số nguyên tố $$p$$, nằm trong dãy khớp cơ bản:

$$
0 \longrightarrow E(\mathbb{Q})/2E(\mathbb{Q}) \longrightarrow \mathrm{Sel}_2(E) \longrightarrow \Sha(E)[2] \longrightarrow 0.
$$

Vì kích thước của $$E(\mathbb{Q})/2E(\mathbb{Q})$$ ít nhất bằng $$2^{r_E}$$, ta luôn có bất đẳng thức vàng:

$$
2^{r_E} \;\le\; \#\mathrm{Sel}_2(E).
$$

#### Bước 2: Tham số hóa nhóm 2-Selmer bằng dạng bậc 4 nhị phân!
Birch và Swinnerton-Dyer đã biết từ lâu rằng mỗi phần tử của nhóm 2-Selmer $$\mathrm{Sel}_2(E)$$ ứng với một quỹ đạo của **dạng bậc 4 nhị phân** $$f(x, y) = ax^4 + bx^3y + cx^2y^2 + dxy^3 + ey^4$$ có hai bất biến $$(I, J)$$ đúng bằng hệ số $$(A, B)$$ của đường cong elliptic $$y^2 = x^3 + Ax + B$$! Đếm kích thước trung bình của $$\mathrm{Sel}_2(E)$$ bỗng biến thành bài toán **hình học các số**: đếm số quỹ đạo dạng bậc 4 nhị phân có bất biến bị chặn!

#### Bước 3: Kỹ thuật "lấy trung bình trên nhóm Lie" để diệt đỉnh nhọn (*cusp*)
Đếm điểm lưới trên miền cơ bản của dạng bậc 4 nhị phân khó hơn nhiều so với dạng bậc 2 vì miền có các "mũi nhọn" (*cusp*) cực mảnh kéo dài ra vô tận. Bhargava và Shankar sáng tạo ra kỹ thuật **lấy trung bình miền cơ bản dọc theo một tập compact của nhóm Lie** kết hợp với phương pháp sàng hình học để chứng minh phần sai số ở đỉnh nhọn triệt tiêu — và tính ra con số tuyệt đẹp:

$$
\text{Trung bình của } \#\mathrm{Sel}_2(E) \;=\; \mathbf{3}!
$$

#### Bước 4: Suy ra hạng trung bình bị chặn và tỷ lệ dương có hạng 0 và 1
Từ $$\mathbb{E}[2^{r_E}] \le \mathbb{E}[\#\mathrm{Sel}_2(E)] = 3$$ và bất đẳng thức sơ cấp $$2r \le 2^r$$ (đúng với mọi số nguyên $$r \ge 0$$: thử $$r=0: 0\le 1$$; $$r=1: 2\le 2$$; $$r=2: 4\le 4$$; $$r=3: 6\le 8$$!), ta lấy kỳ vọng hai vế và thu ngay:

$$
2\,\mathbb{E}[r_E] \;\le\; \mathbb{E}[2^{r_E}] \;\le\; 3 \;\Longrightarrow\; \mathbb{E}[r_E] \;\le\; \mathbf{1{,}5}!
$$

Lần đầu tiên trong lịch sử, hạng trung bình của đường cong elliptic được chứng minh là **hữu hạn** vô điều kiện! Sau đó, bằng cách lặp lại chiến lược này cho nhóm 3-Selmer (trung bình $$= 4$$), 4-Selmer ($$= 7$$), 5-Selmer ($$= 6$$), Bhargava–Shankar kéo chặn trên hạng trung bình xuống **dưới $$0{,}885$$**, chứng minh phần lớn đường cong có hạng $$0$$ hoặc $$1$$, và một tỷ lệ dương có hạng $$0$$ (cùng Bhargava–Skinner chứng minh một tỷ lệ dương có hạng $$1$$ và thỏa mãn BSD!).

Tóm tắt mạch chứng minh:

$$
\text{Đường cong } E(\mathbb{Q})
\;\xrightarrow{\text{2-Selmer}}\;
\text{Quỹ đạo dạng bậc 4 nhị phân}
\;\xrightarrow{\text{Hình học các số}}\;
\mathbb{E}[\#\mathrm{Sel}_2] = 3
\;\xrightarrow{2r \le 2^r}\;
\mathbb{E}[r_E] \le 1{,}5.
$$

---

## 3. Ghi nhận công lao và phân biệt với Giả thuyết BSD

| Thành phần | Vai trò |
|------------|---------|
| Luật hợp thành Gauss | Tiền thân của trường hợp hạng 2 |
| Sato–Shintani, Wright, Yukie, Datskovsky–Wright | Phép đếm trên không gian tiền thuần nhất; mật độ bậc ba |
| Bhargava, *Higher composition laws* I–IV | Khối lập phương & tham số hóa vành hạng $$2$$–$$5$$ |
| Bhargava–Shankar | Kích thước 2-Selmer trung bình bằng $$3$$; 3/4/5-Selmer; tỷ lệ dương có hạng $$0$$; hạng trung bình $$< 0{,}885$$ |
| Bhargava–Skinner và cộng sự | Tỷ lệ dương đường cong có hạng $$1$$ và thỏa mãn BSD |
| BSD (Birch, Swinnerton-Dyer; bài toán Clay) | **Vẫn còn mở:** sự bằng nhau giữa hạng đại số và hạng giải tích nói chung |

Bhargava sinh năm 1974 tại Hamilton (Canada), làm việc tại Đại học Princeton, và là **người gốc Ấn đầu tiên** nhận Huy chương Fields (2014).

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Bhargava giải được BSD." | Ông chặn hạng *đại số* trung bình thông qua nhóm Selmer và chứng minh BSD cho một tỷ lệ dương đường cong; BSD tổng quát vẫn còn mở. |
| "Hạng trung bình bằng $$1/2$$." | Đó là dự đoán heuristic. Định lý chứng minh hạng trung bình hữu hạn ($$\le 1{,}5$$ từ 2-Selmer, $$< 0{,}885$$ từ 5-Selmer). |
| "Ông phát minh ra hình học các số." | Minkowski, Davenport–Heilbronn và trường phái tiền thuần nhất đã đặt nền móng trước. |
| "Hợp thành bậc cao áp dụng cho mọi đa thức ở mọi bậc." | Đó là một họ các phép tham số hóa bằng quỹ đạo trên những biểu diễn cụ thể (bậc $$\le 5$$). |
| "Đếm vành nghĩa là liệt kê hết chúng." | Nghĩa là tìm công thức tiệm cận cho số lớp đẳng cấu có biệt thức bị chặn bởi $$X$$. |

---

## Nguồn video và đọc thêm

Bài này không có bộ tài liệu video riêng của khóa học.

1. Lời trích dẫn Huy chương Fields 2014 của IMU: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. Bản tin của IMU, *The Work of Manjul Bhargava*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_bhargava.pdf).
3. Bách khoa: [Manjul Bhargava](https://en.wikipedia.org/wiki/Manjul_Bhargava).
4. Bài giới thiệu của Quanta (2014): [The Musical, Magical Number Theorist](https://www.quantamagazine.org/number-theorist-manjul-bhargava-is-awarded-fields-medal-20140812/).
5. Tìm trên arXiv: [Bhargava composition](https://arxiv.org/search/?query=Bhargava+composition&searchtype=all); [Bhargava Shankar elliptic](https://arxiv.org/search/?query=Bhargava+Shankar+elliptic&searchtype=all).
6. Bài đọc sâu trong khóa học về hạng và hàm $$L$$: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/).

**Ghi nhớ:** Đây là các định lý về kích thước Selmer trung bình và hạng trung bình, **không** phải lời giải của BSD.

---

## Tài liệu tham khảo

1. International Mathematical Union, Huy chương Fields 2014: lời trích dẫn và bản tin về Manjul Bhargava.
2. **M. Bhargava**, *Higher composition laws* I–IV, *Ann. of Math.* (2004–2008).
3. **M. Bhargava, A. Shankar**, *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, *Ann. of Math.* 181 (2015).
4. **M. Bhargava, A. Shankar**, *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0*, *Ann. of Math.* 181 (2015).
5. Truyền thống đếm trước đó: Davenport–Heilbronn; Datskovsky–Wright; các bài tổng quan về không gian vector tiền thuần nhất (Wright, Yukie).
6. Trong khóa học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), [Tsimerman]({{ site.baseurl }}/contents/vi/chapter02/02_14_Tsimerman_Arithmetic/), [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/).

---

## Hướng đi tiếp

- Tự tính một ví dụ về luật Gauss (biệt thức $$-23$$ hoặc $$-31$$) trước khi đọc *Higher composition laws I*.
- Đọc một tài liệu giải thích về nhóm 2-Selmer (ví dụ một chương đầu trong sách của Silverman, kèm một bài tổng quan về thống kê số học) cho đến khi dãy khớp ở trên trở nên tự nhiên với bạn.
- Bài seminar A3 (tùy chọn): viết một trang về *những gì vẫn còn mở* (giá trị đúng của hạng trung bình, BSD, đếm trường bậc $$\ge 6$$), không thổi phồng công trình năm 2014 thành việc khép lại lý thuyết số.
- Nếu bạn thích khối lập phương hơn hạng, hãy tiếp tục với các phép tham số hóa. Nếu thích hạng hơn, hãy chuyển sang bài [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) và luôn phân biệt rõ nhóm Selmer với hàm $$L$$.

## Video tham khảo

- **Xem trước** — [Manjul Bhargava, The average rank of elliptic curves](https://www.youtube.com/watch?v=t5S8PO2PQgU) — Clay Mathematics Institute, tiếng Anh. Bài giảng của Bhargava về hạng trung bình của đường cong elliptic, nội dung chính của mục 3. Nên xem trước khi đọc bài.
- [Manjul Bhargava - The average rank of elliptic curves: data, conjectures, and theorems](https://www.youtube.com/watch?v=zm1v_FaTglw) — princetonmathematics, tiếng Anh. Trình bày dữ liệu, các dự đoán và các định lý về hạng trung bình, giúp phân biệt rõ phần đã chứng minh và phần còn là giả thuyết. Nên xem sau khi đọc mục 3.
- [Manjul Bhargava - Rational points on elliptic and hyperelliptic curves MCA 2013](https://www.youtube.com/watch?v=6NHO-0FKAjM) — MCA2013, tiếng Anh. Bài giảng về điểm hữu tỷ trên đường cong elliptic và siêu elliptic, mở rộng phương pháp sang các đường cong khác. Dành cho người muốn tìm hiểu thêm.
