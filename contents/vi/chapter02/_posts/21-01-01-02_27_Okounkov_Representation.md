---
layout: post
title: "Những cây cầu của Okounkov: xác suất, biểu diễn, và hình học (Huy chương Fields 2006)"
chapter: '02'
order: 27
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử một trò chơi tưởng chừng thuần túy giải trí: bạn lấy một bộ bài gồm $$n = 1{,}000{,}000$$ lá đánh số từ $$1$$ đến $$n$$, xáo trộn hoàn toàn ngẫu nhiên rồi tìm độ dài của **dãy con tăng dài nhất**. Ai có thể ngờ rằng dao động thống kê của con số ấy lại tuân theo **chính xác** cùng một định luật xác suất (luật Tracy–Widom) với trị riêng lớn nhất của một ma trận ngẫu nhiên khổng lồ? Và càng khó tin hơn nữa: cùng những bảng ô vuông (biểu đồ Young) điều khiển bộ bài xáo trộn ấy lại đang âm thầm điều khiển cả việc **đếm đường cong trong hình học đại số** lẫn việc **đếm instanton trong lý thuyết trường lượng tử bốn chiều**!

Người đã nhìn thấu và dựng nên những cây cầu nối liền ba lục địa tưởng chừng cách biệt ấy là **Andrei Okounkov**. Tại ICM Madrid năm 2006 — cùng đợt với **Terence Tao**, **Wendelin Werner** và **Grigori Perelman** — ông nhận **Huy chương Fields** với lời trao giải chỉ một câu đầy cô đọng:

> For his contributions bridging probability, representation theory and algebraic geometry.

*Tạm dịch: vì những đóng góp bắc cầu giữa xác suất, lý thuyết biểu diễn và hình học đại số.*

Thông cáo báo chí của IMU năm 2006 thẳng thắn nhận xét công trình của Okounkov khó xếp vào một ngăn tủ truyền thống nào, bởi hai chủ đề xuyên suốt của ông là **tính ngẫu nhiên** và **lý thuyết biểu diễn cổ điển** (nhóm đối xứng, biểu đồ Young), được dùng để giải các bài toán trung tâm của hình học đại số đếm và cơ học thống kê. Bài học này sẽ đi từ một ví dụ cầm tay cho $$n = 3$$ trên nhóm đối xứng $$S_3$$ tới tinh thể nóng chảy, lý thuyết Gromov–Witten của Okounkov–Pandharipande và hàm phân hoạch instanton của Nekrasov–Okounkov — đồng thời giữ ranh giới chính xác: ông không phân loại mọi biểu diễn nhóm và không phát minh lý thuyết gauge.

**Mạch bài học:** Bản đồ kiến thức nền (lý thuyết biểu diễn $$S_n$$, biểu đồ Young, không gian Fock) → Ví dụ cầm tay chỉ việc: tính trọn bộ độ đo Plancherel cho $$S_3$$ và chạy thuật toán Robinson–Schensted → Từ hình dạng giới hạn đến tinh thể nóng chảy và đường cong đại số → Khung giải thích chậm: 4 bước bắc cầu từ biểu đồ Young sang Gromov–Witten ($$\mathbb{P}^1$$) và instanton Seiberg–Witten → Quá trình Schur & những điều không khẳng định.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại lời trao giải của IMU năm 2006 như một **chương trình bắc cầu** giữa xác suất, lý thuyết biểu diễn và hình học đại số.
- Tự tay tính **độ đo Plancherel** trên tất cả các phân hoạch của $$n = 3$$ và hiểu ý nghĩa của **hình dạng giới hạn** tất định (Vershik–Kerov; Logan–Shepp).
- Giải thích mối liên hệ giữa dãy con tăng dài nhất của hoán vị ngẫu nhiên, luật Tracy–Widom của ma trận ngẫu nhiên, và cách chứng minh bằng **mặt ngẫu nhiên** của Okounkov.
- Trình bày cây cầu **Okounkov–Pandharipande**: biến hàm sinh của lý thuyết Gromov–Witten trên $$\mathbb{P}^1$$ thành kỳ vọng chân không trong không gian Fock gắn với hệ khả tích **2-Toda**.
- Hiểu công trình **Nekrasov–Okounkov** như bộ từ điển đồng nhất hàm phân hoạch instanton đã chính quy hóa với phân hoạch ngẫu nhiên và hình học Seiberg–Witten.
- Nhận diện **độ đo Schur / quá trình Schur** (Okounkov, Reshetikhin, Borodin, Olshanski) và mô hình **dimer / tinh thể nóng chảy** (Kenyon–Okounkov).

**Kiến thức nền.** Phân hoạch một số nguyên; nhóm đối xứng $$S_n$$ ở mức "các biểu diễn bất khả quy được gắn nhãn bằng biểu đồ Young"; hàm sinh. Về hình học đại số, chỉ cần biết "có thể đếm các đường cong trong một đa tạp theo một nghĩa ảo" là đủ để hiểu ý chính của lý thuyết Gromov–Witten. Không cần lý thuyết trường lượng tử.

**Liên kết với các bài khác.** Bài này minh họa một chương trình nghiên cứu bắc cầu sâu giữa các lĩnh vực, và việc trích dẫn đúng lời trao giải. Người cùng năm: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Về hình học không gian moduli: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (một không gian moduli khác, nhưng cùng ý tưởng "không gian các hình dạng trở thành đối tượng của động lực học hoặc xác suất").

---

## Bản đồ kiến thức nền: Lý thuyết biểu diễn $$S_n$$, Biểu đồ Young và Không gian Fock là gì?

### 1. Lý thuyết biểu diễn nhóm đối xứng $$S_n$$ nghiên cứu gì?
**Lý thuyết biểu diễn** biến các nhóm đối xứng trừu tượng thành các ma trận vuông khả nghịch, rồi phân tích chúng thành những "nguyên tử" gọi là **biểu diễn bất khả quy**. Với nhóm đối xứng $$S_n$$ (gồm $$n!$$ hoán vị của $$n$$ phần tử), các biểu diễn bất khả quy tương ứng **1–1** với các **phân hoạch** $$\lambda = (\lambda_1 \ge \lambda_2 \ge \cdots)$$ của số $$n$$, vẽ trực quan thành **biểu đồ Young** gồm các hàng ô vuông xếp chồng.

### 2. Xác suất trên các biểu đồ Young và hình dạng giới hạn
Từ đẳng thức cơ bản của lý thuyết biểu diễn $$\sum_{\lambda \vdash n} (\dim\lambda)^2 = n!$$, ta có ngay một phân bố xác suất tự nhiên gọi là **độ đo Plancherel**:

$$
\mathbb{P}(\lambda) = \frac{(\dim\lambda)^2}{n!}.
$$

Khi $$n \to \infty$$, **Vershik–Kerov** và **Logan–Shepp** (cuối thập niên 1970) chứng minh rằng nếu co nhỏ biểu đồ Young ngẫu nhiên đi $$\sqrt{n}$$ lần, đường viền của nó tập trung chặt quanh một **hình dạng giới hạn** trơn tất định!

### 3. Không gian Fock — cầu nối từ biểu đồ Young sang hình học đếm
Nếu coi mỗi biểu đồ Young $$\lambda$$ (ở mọi kích thước $$n \ge 0$$) là một vector cơ sở trực chuẩn $$\vert\lambda\rangle$$ của một không gian Hilbert vô hạn chiều, ta thu được **không gian Fock** (không gian trạng thái của các hạt fermion 1 chiều). Phép thêm/bớt một ô vuông trên biểu đồ trở thành các toán tử sinh/hủy quen thuộc của vật lý lượng tử — và kỳ diệu thay, các hàm sinh của **hình học đếm (Gromov–Witten)** lại có thể viết gọn thành giá trị kỳ vọng $$\langle 0 \vert \cdots \vert 0 \rangle$$ của đúng các toán tử ấy!

---

## 1. Ví dụ cầm tay chỉ việc: tính trọn bộ độ đo Plancherel cho $$S_3$$ và thuật toán Robinson–Schensted

Hãy thử với $$n = 3$$ (nhóm $$S_3$$ có $$3! = 6$$ hoán vị). Số $$3$$ có đúng **3 phân hoạch**:

| Phân hoạch $$\lambda$$ | Biểu đồ Young | Số bảng chuẩn ($$\dim\lambda$$) | Xác suất Plancherel $$\frac{(\dim\lambda)^2}{3!}$$ |
|---|---|---|---|
| $$(3)$$ | 1 hàng 3 ô | $$1$$ (biểu diễn tầm thường) | $$1^2 / 6 = 1/6$$ |
| $$(2, 1)$$ | Hàng 2 ô + hàng 1 ô | $$2$$ (biểu diễn chuẩn 2D) | $$2^2 / 6 = 4/6 = 2/3$$ |
| $$(1, 1, 1)$$ | 1 cột 3 ô | $$1$$ (biểu diễn dấu) | $$1^2 / 6 = 1/6$$ |

Kiểm tra tổng xác suất: $$\frac{1}{6} + \frac{4}{6} + \frac{1}{6} = 1$$! Hãy chú ý điều thú vị ngay ở $$n=3$$: phân hoạch "cân đối ở giữa" $$(2,1)$$ chiếm tới **$$2/3$$ xác suất**, trong khi hai dạng cực đoan dài dẹt $$(3)$$ và $$(1,1,1)$$ chỉ chiếm $$1/6$$ mỗi dạng! (Khi $$n$$ rất lớn, hiện tượng "tập trung vào dáng giữa" này chính là hình dạng giới hạn Vershik–Kerov–Logan–Shepp!)

**Thử chạy thuật toán Robinson–Schensted trên hoán vị $$(2, 1, 3) \in S_3$$:**
- Chèn $$2$$ vào bảng rỗng $$\to$$ hàng 1: `[2]`.
- Chèn $$1$$: vì $$1 < 2$$, số $$1$$ đẩy $$2$$ xuống hàng 2 $$\to$$ hàng 1: `[1]`, hàng 2: `[2]`.
- Chèn $$3$$: vì $$3 > 1$$, gắn $$3$$ vào cuối hàng 1 $$\to$$ hàng 1: `[1, 3]`, hàng 2: `[2]`.

Hình dạng bảng thu được là phân hoạch **$$(2, 1)$$**, với chiều dài hàng đầu tiên $$\lambda_1 = 2$$ — **bằng đúng độ dài dãy con tăng dài nhất** `(2, 3)` hoặc `(1, 3)` của hoán vị `(2, 1, 3)`! Nếu bạn làm tương tự với cả 6 hoán vị của $$S_3$$, sẽ có đúng 1 hoán vị ra $$(3)$$, 4 hoán vị ra $$(2,1)$$, và 1 hoán vị ra $$(1,1,1)$$ — khớp **100%** với phân phối Plancherel!

---

## 2. Từ BDJ đến tinh thể nóng chảy và đường cong đại số

Năm 1999, **Baik–Deift–Johansson (BDJ)** chứng minh rằng độ lệch của hàng đầu tiên $$\lambda_1$$ quanh $$2\sqrt{n}$$ (chia cho $$n^{1/6}$$) tuân theo phân phối **Tracy–Widom** của trị riêng lớn nhất trong ma trận ngẫu nhiên Hermite Gauss, và dự đoán điều này đúng đồng thời cho $$k$$ hàng đầu tiên. **Okounkov (2000)** chứng minh dự đoán đó bằng một cây cầu hình học hoàn toàn mới: cả mô-men của ma trận ngẫu nhiên lẫn mô-men của phân hoạch Plancherel đều đếm cùng một đối tượng — **các mặt ngẫu nhiên** (phủ phân nhánh của mặt cầu)! (Song song đó, **Borodin–Okounkov–Olshanski** và **Johansson** đưa ra các chứng minh khác qua quá trình điểm định thức.)

Tiếp đó, **Kenyon–Okounkov** (và Sheffield) nghiên cứu **phân hoạch phẳng 3D** (mô hình **tinh thể nóng chảy** và phủ **dimer** bằng hình thoi): khi ta làm tan chảy ngẫu nhiên các khối lập phương từ một góc tường 3D, ranh giới vĩ mô giữa vùng đóng băng phẳng lì và vùng lỏng hỗn loạn (*đường cong băng giá*) luôn là một **đường cong đại số thực** (đường cong Harnack)! Một lần nữa, xác suất cơ học thống kê lại dẫn thẳng về hình học đại số.

---

## 3. Khung giải thích: Ba cây cầu lớn của Okounkov vận hành như thế nào? (nên đọc chậm)

Làm sao cùng một bộ công cụ "biểu đồ Young + độ đo ngẫu nhiên" lại giải được bài toán ở cả hình học đếm lẫn vật lý lý thuyết 4 chiều? Hãy xem chuỗi 4 bước:

#### Bước 1: Lý thuyết Gromov–Witten của đường cong qua không gian Fock (Okounkov–Pandharipande)
**Lý thuyết Gromov–Witten** đếm (theo nghĩa ảo) số ánh xạ chỉnh hình từ đường cong giống $$g$$ vào đa tạp đích $$X$$. Khi đa tạp đích là **$$\mathbb{P}^1$$**, **Okounkov và Pandharipande** (*Ann. of Math.* 163, 2006; [arXiv:math/0207233](https://arxiv.org/abs/math/0207233)) đồng nhất phần dừng với **số Hurwitz** (đếm phủ phân nhánh — vốn là phép nhân trong tâm đại số nhóm $$S_n$$) có chèn các toán tử **chu trình hoàn chỉnh** (*completed cycles*). Khi chuyển sang cơ sở biểu đồ Young trong không gian Fock, toàn bộ hàm sinh Gromov–Witten đẳng biến của $$\mathbb{P}^1$$ hóa thành một hàm tau của **hệ phương trình khả tích 2-Toda**!

#### Bước 2: Giả thuyết cầu nối Gromov–Witten $$\leftrightarrow$$ Donaldson–Thomas (MNOP)
Cùng **Maulik, Nekrasov và Pandharipande**, Okounkov đề xuất bộ giả thuyết nối lý thuyết **Gromov–Witten** (đếm đường cong trong đa tạp 3 chiều) với lý thuyết **Donaldson–Thomas** (đếm bó lý tưởng — mà trên không gian xuyến chính là đếm **phân hoạch phẳng 3D**!).

#### Bước 3: Hàm phân hoạch instanton Nekrasov biến thành độ đo trên phân hoạch (Nekrasov–Okounkov)
Năm 2002, **Nikita Nekrasov** định nghĩa chặt chẽ hàm phân hoạch instanton của lý thuyết gauge siêu đối xứng $$\mathcal{N}=2$$ bốn chiều bằng tích phân định vị đẳng biến trên không gian moduli instanton. Nhờ định vị Atiyah–Bott, các điểm bất động được đánh chỉ số bởi các bộ biểu đồ Young! **Nekrasov và Okounkov** ([arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)) viết lại hàm phân hoạch đó thành một **độ đo xác suất trên phân hoạch ngẫu nhiên** (một biến dạng của độ đo Plancherel), rồi dùng phương pháp **hình dạng giới hạn** chứng minh năng lượng tự do (sức căng bề mặt) của hình dạng giới hạn khớp chính xác với **hàm thế trước Seiberg–Witten**!

#### Bước 4: Quá trình Schur — khung xác suất định thức chung
Để thống nhất tất cả các mô hình tăng trưởng, phân hoạch phẳng và dimer, **Okounkov** giới thiệu **độ đo Schur** (trọng số $$s_\lambda(x)s_\lambda(y)$$), rồi cùng **Reshetikhin** (và nhóm **Borodin–Okounkov–Olshanski**) xây dựng **quá trình Schur** — các độ đo trên dãy phân hoạch có hàm tương quan dạng định thức tính được tường minh.

Tóm tắt tam giác cầu nối của Okounkov:

$$
\text{Xác suất (Plancherel / Schur)}
\;\longleftrightarrow\;
\text{Biểu diễn (} S_n\text{, Không gian Fock)}
\;\longleftrightarrow\;
\text{Hình học (Gromov–Witten, Seiberg–Witten)}.
$$

---

## 4. Những điều Okounkov không làm và vì sao là Huy chương Fields

- Ông **không** phân loại mọi biểu diễn bất khả quy của mọi nhóm (công trình thế kỷ trải rộng trên nhóm hữu hạn, nhóm Lie, nhóm $$p$$-adic); sở trường của ông là nhóm đối xứng và lý thuyết biểu diễn tổ hợp làm cầu nối.
- Ông **không** thay thế hình học đại số bằng tổ hợp, và **không** phát minh lý thuyết gauge hay Seiberg–Witten (Nekrasov định nghĩa hàm phân hoạch; Nekrasov–Okounkov dựng từ điển nối với phân hoạch ngẫu nhiên).

**Vì sao là Huy chương Fields 2006:** Như Giovanni Felder tổng kết trong bài giới thiệu tại ICM (*"The work of Andrei Okounkov"*, [arXiv:math/0609847](https://arxiv.org/abs/math/0609847)), huy chương tôn vinh một **bộ từ điển phi thường** cho phép ba ngành lớn — xác suất, lý thuyết biểu diễn và hình học đại số — mượn công cụ của nhau để giải những bài toán tưởng chừng bất khả xâm phạm.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Okounkov đã phân loại mọi biểu diễn." | Ông dùng lý thuyết biểu diễn của nhóm đối xứng (và các nhóm gần gũi) như một cây cầu; phân loại biểu diễn là một dự án khác. |
| "Okounkov phát minh hình dạng giới hạn Plancherel." | Vershik–Kerov và Logan–Shepp tìm ra hình dạng đó; Okounkov phát triển các liên hệ và ứng dụng. |
| "Okounkov phát minh lý thuyết gauge / Seiberg–Witten." | Nekrasov định nghĩa hàm phân hoạch đã chính quy hóa; Nekrasov–Okounkov đồng nhất nó với một mô hình phân hoạch ngẫu nhiên. |
| "Lý thuyết Gromov–Witten chỉ là tổ hợp." | Các bất biến mang bản chất hình học; chỉ một số hàm sinh có công thức tổ hợp / lý thuyết biểu diễn. |
| "Độ đo Plancherel là độ đo đều trên các phân hoạch." | Nó gán cho mỗi biểu đồ trọng số $$(\dim\lambda)^2/n!$$, không phải $$1/p(n)$$. |
| "Huy chương 2006 chỉ là về ma trận ngẫu nhiên." | Liên hệ với ma trận ngẫu nhiên là một chương sớm; các cây cầu tới Gromov–Witten và instanton cũng là trung tâm trong các tài liệu chính thức. |
| "Quá trình Schur là của riêng Okounkov." | Okounkov, Reshetikhin, Borodin, Olshanski và nhiều người khác. |

---

## Liên kết

- Huy chương Fields 2006 của IMU: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2006](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2006)
- PDF citation Okounkov của IMU: [https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2006/OkounkovengDEF.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2006/OkounkovengDEF.pdf)
- Wikipedia, Andrei Okounkov: [https://en.wikipedia.org/wiki/Andrei_Okounkov](https://en.wikipedia.org/wiki/Andrei_Okounkov)
- Felder, “The work of Andrei Okounkov”: [https://arxiv.org/abs/math/0609847](https://arxiv.org/abs/math/0609847)
- Okounkov, “Random partitions and instanton counting”: [https://arxiv.org/abs/math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)
- Okounkov–Pandharipande, GW đẳng biến của $$\mathbb{P}^1$$: [https://arxiv.org/abs/math/0207233](https://arxiv.org/abs/math/0207233)
- Tìm arXiv theo tác giả: [https://arxiv.org/search/math?searchtype=author&query=Okounkov%2C+A](https://arxiv.org/search/math?searchtype=author&query=Okounkov%2C+A)
- Khóa học: [Perelman, cùng ICM]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)

---

## Tài liệu tham khảo

1. IMU, citation Huy chương Fields 2006 và bài báo chí cho Andrei Okounkov (PDF trên mathunion.org).
2. **G. Felder**, “The work of Andrei Okounkov,” [arXiv:math/0609847](https://arxiv.org/abs/math/0609847).
3. Hình dạng giới hạn: Vershik–Kerov; Logan–Shepp. Thăng giáng: Baik–Deift–Johansson; chứng minh của Okounkov; Borodin–Okounkov–Olshanski.
4. **A. Okounkov và R. Pandharipande**, chuỗi Gromov–Witten / Hurwitz / completed cycles, gồm *Ann. of Math.* **163** (2006) và [arXiv:math/0207233](https://arxiv.org/abs/math/0207233).
5. **N. Nekrasov và A. Okounkov**, lý thuyết Seiberg–Witten và phân hoạch ngẫu nhiên (khảo sát trong [arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)).
6. Độ đo Schur và quá trình Schur: Okounkov; Okounkov–Reshetikhin; Borodin–Okounkov–Olshanski và các khảo sát sau.
7. Dimer / hình dạng giới hạn đại số: Kenyon–Okounkov (và công trình liên quan).
8. Khóa học: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

---

## Hướng đi tiếp

- Đọc bài giới thiệu ngắn của Felder, rồi phần mở đầu một bài của Okounkov–Pandharipande, rồi bài tổng quan về instanton. Đừng bắt đầu từ lý thuyết Seiberg–Witten theo góc nhìn vật lý.
- So sánh độ đo Plancherel với độ đo đều trên các phân hoạch: cùng tập biểu đồ, nhưng hình dạng điển hình khác nhau.
- Bài tập thêm: vẽ một trang "sơ đồ cây cầu" với ba nút (xác suất, lý thuyết biểu diễn, hình học đếm) và hai cạnh mà bạn thực sự nêu tên được (độ đo Plancherel; toán tử Gromov–Witten / Hurwitz).

## Video tham khảo

- **Xem trước**: [On the crossroads of enumerative geometry and representation theory – Andrei Okounkov – ICM2018](https://www.youtube.com/watch?v=zlQ23vRAOCQ) (Rio ICM2018, tiếng Anh). Bài giảng toàn thể của Okounkov tại ICM 2018 về chỗ giao nhau của hình học đếm và lý thuyết biểu diễn, đúng tinh thần "cây cầu" của lời trao giải.
- [Andrei Okounkov | Classical and quantum integrable systems in enumerative geometry](https://www.youtube.com/watch?v=xZNGyBFR0ao) (Harvard CMSA, tiếng Anh). Bài giảng về các hệ khả tích cổ điển và lượng tử trong hình học đếm. Nên xem sau khi đọc mục 3, để thấy hướng phát triển về sau của các ý tưởng đó.
