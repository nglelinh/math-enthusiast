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

Hãy thử một thí nghiệm tưởng tượng kỳ lạ: bạn có một bộ bài gồm $$n = 1{,}000{,}000$$ lá đánh số từ $$1$$ đến $$n$$, xáo trộn hoàn toàn ngẫu nhiên rồi tìm độ dài của **dãy con tăng dài nhất** trong bộ bài đó. Thoạt nhìn, đây chỉ là một bài toán giải trí về tổ hợp và xác suất. Thế nhưng vào cuối thập niên 1990, các nhà toán học bàng hoàng phát hiện rằng dao động của con số này tuân theo **chính xác** cùng một định luật xác suất (luật Tracy–Widom) với trị riêng lớn nhất của một ma trận ngẫu nhiên khổng lồ! Và càng khó tin hơn nữa: cùng những sơ đồ ô vuông (biểu đồ Young) điều khiển bộ bài xáo trộn ấy lại đang âm thầm điều khiển cả việc **đếm đường cong trong hình học đại số** lẫn việc **đếm instanton trong lý thuyết trường lượng tử bốn chiều**!

Người đã nhìn thấu và dựng nên những cây cầu vững chắc nối liền các lục địa tưởng chừng cách biệt ấy là **Andrei Okounkov**. Tại ICM Madrid năm 2006 — cùng năm với **Terence Tao**, **Wendelin Werner** và **Grigori Perelman** — ông nhận **Huy chương Fields** với lời trao giải ngắn gọn nhưng đầy sức nặng:

> For his contributions bridging probability, representation theory and algebraic geometry.

*Tạm dịch: vì những đóng góp bắc cầu giữa xác suất, lý thuyết biểu diễn và hình học đại số.*

Thông cáo của IMU năm 2006 thẳng thắn nhận xét rằng công trình của Okounkov rất khó xếp vào một ô phân loại duy nhất, bởi sợi chỉ xuyên suốt sự nghiệp ông là dùng **tính ngẫu nhiên** và **lý thuyết biểu diễn cổ điển** (của nhóm đối xứng và các biểu đồ Young) để giải quyết những bài toán trung tâm của hình học đại số đếm và cơ học thống kê. Bài học này sẽ giúp bạn đi dọc ba cây cầu lớn của ông — từ phân hoạch ngẫu nhiên và tinh thể nóng chảy, sang lý thuyết Gromov–Witten của Okounkov–Pandharipande, đến hàm phân hoạch instanton của Nekrasov–Okounkov — đồng thời giữ sự chính xác: ông không phân loại mọi biểu diễn nhóm, không phát minh lý thuyết gauge, và không thay thế hình học đại số bằng tổ hợp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại lời trao giải của IMU năm 2006 như một **chương trình bắc cầu** giữa ba lĩnh vực, thay vì một định lý phân loại đơn ngành.
- Mô tả **độ đo Plancherel** trên các phân hoạch của $$n$$ và kết quả về **hình dạng giới hạn** tất định của Vershik–Kerov và Logan–Shepp.
- Giải thích trực quan vì sao các biểu diễn bất khả quy của nhóm đối xứng $$S_n$$ được đánh nhãn bằng biểu đồ Young, và vì sao việc chọn ngẫu nhiên một biểu đồ lại trở thành bài toán xác suất giàu cấu trúc.
- Trình bày ý chính cây cầu **Okounkov–Pandharipande**: biến hàm sinh của lý thuyết Gromov–Witten (đặc biệt trên $$\mathbb{P}^1$$) thành các kỳ vọng toán tử trên không gian Fock gắn với hệ khả tích 2-Toda.
- Hiểu công trình **Nekrasov–Okounkov** như một cây cầu toán học đồng nhất hàm phân hoạch instanton với mô hình phân hoạch ngẫu nhiên và hình học Seiberg–Witten, không phóng đại thành "Okounkov phát minh lý thuyết gauge".
- Nhận diện các khái niệm song hành: **độ đo Schur / quá trình Schur** (Okounkov, Reshetikhin, Borodin, Olshanski) và mô hình **dimer / tinh thể nóng chảy** (Kenyon–Okounkov).

**Kiến thức nền.** Phân hoạch một số nguyên; nhóm đối xứng $$S_n$$ ở mức "các biểu diễn bất khả quy được gắn nhãn bằng biểu đồ Young"; hàm sinh. Về hình học đại số, chỉ cần biết "có thể đếm các đường cong trong một đa tạp theo một nghĩa ảo" là đủ để hiểu ý chính của lý thuyết Gromov–Witten. Không cần lý thuyết trường lượng tử.

**Liên kết với các bài khác.** Bài này minh họa một chương trình nghiên cứu bắc cầu sâu giữa các lĩnh vực, và việc trích dẫn đúng lời trao giải. Người cùng năm: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Về hình học không gian moduli: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (một không gian moduli khác, nhưng cùng ý tưởng "không gian các hình dạng trở thành đối tượng của động lực học hoặc xác suất").

---

## Bản đồ kiến thức nền: Lý thuyết biểu diễn, biểu đồ Young và hình học đếm là gì?

Để thấy ba lĩnh vực "xác suất – biểu diễn – hình học đại số" chạm nhau ở điểm nào, hãy xem ba viên gạch nền rất đơn giản.

**1. Lý thuyết biểu diễn — biến nhóm trừu tượng thành ma trận.**
**Lý thuyết biểu diễn** nghiên cứu các nhóm đối xứng bằng cách biểu diễn mỗi phần tử của nhóm thành một ma trận vuông khả nghịch (như phép quay trong mặt phẳng ứng với ma trận $$2 \times 2$$). Giống như mọi số tự nhiên đều phân tích thành tích các số nguyên tố, mọi biểu diễn của một nhóm hữu hạn đều tách thành tổng trực tiếp của các "viên gạch cơ bản" gọi là **biểu diễn bất khả quy**.
Với **nhóm đối xứng $$S_n$$** (nhóm tất cả $$n!$$ hoán vị của $$n$$ phần tử), một phép màu tổ hợp xảy ra: các biểu diễn bất khả quy của $$S_n$$ tương ứng **1–1** với các **phân hoạch** của số $$n$$ — tức các cách viết $$n = \lambda_1 + \lambda_2 + \cdots + \lambda_k$$ (với $$\lambda_1 \ge \lambda_2 \ge \cdots > 0$$), vẽ trực quan thành **biểu đồ Young** gồm các hàng ô vuông xếp chồng. Ví dụ với $$n = 4$$, phân hoạch $$4 = 2 + 1 + 1$$ là một hình chữ L gồm 4 ô vuông, ứng với một biểu diễn bất khả quy 3 chiều của $$S_4$$.

**2. Khi biểu đồ Young trở nên khổng lồ — xác suất xuất hiện.**
Khi $$n$$ rất lớn (ví dụ $$n = 10^6$$), số phân hoạch của $$n$$ bùng nổ theo hàm mũ. Nếu ta chọn ngẫu nhiên một biểu đồ Young $$\lambda$$ gồm $$n$$ ô theo một quy luật xác suất tự nhiên (như độ đo Plancherel), liệu đường viền của biểu đồ khổng lồ đó có hỗn loạn không? Không! Giống như định luật số lớn, khi co nhỏ cả hai trục đi $$\sqrt{n}$$ lần, đường viền của hầu hết mọi biểu đồ ngẫu nhiên đều tập trung sít sao quanh một **đường cong mượt tất định** gọi là **hình dạng giới hạn** (*limit shape*).

**3. Hình học đếm (Enumerative Geometry) và không gian Fock.**
Từ thời cổ đại, hình học đếm đặt những câu hỏi kiểu: "có bao nhiêu đường thẳng đi qua 2 điểm?" (1 đường), "có bao nhiêu đường conic đi qua 5 điểm?" (1 đường), "có bao nhiêu đường cong hữu tỷ bậc $$d$$ trên mặt phẳng đi qua $$3d-1$$ điểm tổng quát?". **Lý thuyết Gromov–Witten** hiện đại gói toàn bộ vô hạn các con số đếm đường cong (hoặc đếm phủ phân nhánh — số Hurwitz) vào một **hàm sinh**. Và phát hiện làm đổi thay cuộc chơi là: các biểu đồ Young đóng vai trò như một **hệ cơ sở trực chuẩn** của một không gian Hilbert gọi là **không gian Fock** (không gian của các hạt fermion 1 chiều trong vật lý lượng tử), khiến các phép đếm hình học phức tạp biến thành phép nhân ma trận và tính kỳ vọng trên không gian Fock!

---

## 1. Phân hoạch: bảng chữ cái chung của ba thế giới

Một **phân hoạch** $$\lambda$$ của số nguyên dương $$n$$ (vẽ thành **biểu đồ Young**) chính là viên đá Rosetta nối ba ngành toán học:
- Trong **lý thuyết biểu diễn**: đánh chỉ số các biểu diễn bất khả quy của $$S_n$$ và các hàm đối xứng **Schur** $$s_\lambda$$.
- Trong **cơ học thống kê**: nếu chồng thêm ô vuông theo chiều thứ ba trong một góc tường 3D (gọi là **phân hoạch phẳng**, *plane partition*), nhìn từ xa nó chính là hình ảnh một góc tinh thể lập phương hay một phép lát mặt phẳng bằng hình thoi (mô hình **dimer**).
- Trong **xác suất**: từ đẳng thức cổ điển $$\sum_{\lambda \vdash n} (\dim \lambda)^2 = n!$$ của nhóm $$S_n$$, ta nhận được ngay một phân bố xác suất cực kỳ tự nhiên gọi là **độ đo Plancherel**:

$$
\mathbb{P}(\lambda)=\frac{\bigl(\dim\lambda\bigr)^2}{n!},
$$

trong đó $$\dim\lambda$$ là số chiều của biểu diễn bất khả quy ứng với $$\lambda$$ (tính bằng công thức độ dài móc nổi tiếng). Thuật toán **Robinson–Schensted** biến mỗi hoán vị ngẫu nhiên đều trong $$S_n$$ thành một biểu đồ Young có phân phối đúng là độ đo Plancherel — và chiều dài hàng đầu tiên $$\lambda_1$$ của biểu đồ đó **chính bằng độ dài dãy con tăng dài nhất** của hoán vị!

Cuối thập niên 1970, **Vershik–Kerov** và độc lập **Logan–Shepp** chứng minh một định lý tuyệt đẹp: khi $$n \to \infty$$, nếu xoay biểu đồ Young ngẫu nhiên đi $$45^\circ$$ và co nhỏ theo tỷ lệ $$\sqrt{n}$$, đường biên trên của nó hội tụ về một **đường cong giới hạn trơn tất định** (có công thức lượng giác ngược tường minh), qua đó suy ra độ dài dãy con tăng dài nhất của một hoán vị ngẫu nhiên cỡ $$n$$ xấp xỉ $$2\sqrt{n}$$.

**Tóm tắt.** Khi lý thuyết biểu diễn cung cấp độ đo tự nhiên trên biểu đồ Young, lý thuyết biểu diễn tiệm cận lập tức hóa thân thành một chương sống động của lý thuyết xác suất.

---

## 2. Từ bài toán bộ bài ngẫu nhiên đến tinh thể nóng chảy và đường cong đại số

Năm 1999, **Baik–Deift–Johansson (BDJ)** chứng minh rằng độ lệch của dãy con tăng dài nhất quanh giá trị $$2\sqrt{n}$$ (sau khi chia cho $$n^{1/6}$$) hội tụ về phân phối **Tracy–Widom** — đúng phân phối của trị riêng lớn nhất trong một ma trận ngẫu nhiên Hermite Gauss! Họ dự đoán sự trùng khớp kỳ bí đó còn đúng cho phân phối đồng thời của nhiều hàng dài nhất $$\lambda_1, \lambda_2, \ldots, \lambda_k$$.

**Ý tưởng đột phá của Okounkov (2000):** Thay vì tính toán giải tích trực tiếp bằng đa thức trực giao như BDJ, Okounkov chứng minh sự trùng khớp bằng một **cây cầu hình học**: ông chỉ ra rằng cả mô-men của ma trận ngẫu nhiên lẫn mô-men của biểu đồ Plancherel đều đếm *cùng một đối tượng hình học* — các **mặt ngẫu nhiên** (phủ phân nhánh của mặt cầu, tương ứng với các đồ thị ruy-băng)! (Độc lập với đó, **Borodin–Okounkov–Olshanski** và **Johansson** cũng đưa ra những chứng minh khác theo hướng quá trình điểm định thức.)

Từ hạt giống đó, Okounkov cùng **Richard Kenyon** (và Scott Sheffield) tiến sang mô hình **tinh thể nóng chảy** (*melting crystal*) và **mô hình dimer** (phủ lưới tổ ong bằng hình thoi). Hãy hình dung một góc phòng 3D lấp đầy vô hạn các khối lập phương băng, rồi bạn bắt đầu làm tan chảy ngẫu nhiên từng khối từ góc phòng ra ngoài. Bạn sẽ thấy một hiện tượng gây sững sờ:
- Xa góc phòng, tinh thể vẫn "đóng băng" cứng nhắc thành các mặt phẳng phẳng lì;
- Gần góc phòng, tinh thể "tan chảy" thành vùng lỏng hỗn loạn;
- Và **đường biên phân cách giữa vùng đóng băng và vùng lỏng** (được gọi là *đường cong băng giá* — arctic curve) không phải một đường cong ngẫu nhiên bất kỳ, mà **Kenyon–Okounkov** chứng minh nó luôn là một **đường cong đại số thực** (loại đường cong Harnack)! Từ một bài toán xác suất cơ học thống kê thuần túy, hình học đại số bất ngờ hiện hình ngay trước mắt!

---

## 3. Lý thuyết Gromov–Witten như những hàm sinh trong không gian Fock

Trong hình học đại số hiện đại, **lý thuyết Gromov–Witten** đếm (theo nghĩa tích phân ảo trên không gian moduli ánh xạ ổn định) số đường cong đại số giống $$g$$ nằm trong một đa tạp đích $$X$$ và đi qua các chu trình cho trước. Những con số này cực kỳ khó tính bằng hình học thuần túy.

Trong loạt bài báo kinh điển (*Annals of Mathematics* 163, 2006; bắt đầu từ [arXiv:math/0207233](https://arxiv.org/abs/math/0207233)), **Andrei Okounkov và Rahul Pandharipande** đã giải mã hoàn chỉnh lý thuyết Gromov–Witten khi đa tạp đích là một đường cong — đặc biệt là đường thẳng xạ ảnh $$\mathbb{P}^1$$. Họ xây dựng một **hình thức toán tử trên không gian Fock** (không gian "nêm vô hạn" với cơ sở là các biểu đồ Young):
- Họ đồng nhất phần dừng của lý thuyết Gromov–Witten trên $$\mathbb{P}^1$$ với **lý thuyết Hurwitz** (đếm phủ phân nhánh của mặt cầu — vốn hoàn toàn biểu diễn được qua tích trong tâm đại số nhóm $$S_n$$!) có chèn thêm các toán tử **chu trình hoàn chỉnh** (*completed cycles*).
- Từ đó, họ chứng minh toàn bộ hàm sinh Gromov–Witten đẳng biến của $$\mathbb{P}^1$$ là một hàm tau của **hệ phương trình khả tích 2-Toda** (người anh em tổng quát của hệ KdV trong định lý Witten–Kontsevich)!

Tiếp nối mạch tư duy bắc cầu này, **Maulik–Nekrasov–Okounkov–Pandharipande (MNOP)** còn đề xuất bộ giả thuyết nổi tiếng nối liền hai lý thuyết đếm tưởng chừng xa lạ của đa tạp ba chiều: **lý thuyết Gromov–Witten** (đếm đường cong) và **lý thuyết Donaldson–Thomas** (đếm bó lý tưởng — mà ở trường hợp xuyến lại quay về đúng bài toán đếm **phân hoạch phẳng 3D**!).

**Tóm tắt.** Hình học đếm trở nên tính được tường minh khi ta nhận ra hàm sinh của nó chính là một kỳ vọng chân không của các toán tử trên không gian Fock trong lý thuyết biểu diễn.

---

## 4. Hàm phân hoạch Nekrasov: cây cầu sang lý thuyết gauge bốn chiều

Năm 2002, nhà vật lý toán **Nikita Nekrasov** đưa ra một định nghĩa toán học chặt chẽ (đã chính quy hóa bằng tác động xuyến) cho **hàm phân hoạch instanton** của lý thuyết trường gauge siêu đối xứng $$\mathcal{N}=2$$ bốn chiều, dưới dạng tích phân định vị đẳng biến trên không gian moduli instanton. Nhờ định lý định vị Atiyah–Bott, các điểm bất động của tác động xuyến trên không gian moduli instanton lại được đánh chỉ số bởi... **các bộ biểu đồ Young**!

Trong công trình chung đột phá **Nekrasov–Okounkov** (xem bài tổng quan dễ đọc của Okounkov [arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)), hai tác giả viết lại toàn bộ hàm phân hoạch instanton của Nekrasov thành một **độ đo xác suất trên các phân hoạch ngẫu nhiên** (một biến dạng của độ đo Plancherel), rồi áp dụng chính kỹ thuật **hình dạng giới hạn** kiểu Vershik–Kerov để tính hành vi tiệm cận! Kết quả làm chấn động cả hai giới toán và vật lý: năng lượng tự do (sức căng bề mặt) của hình dạng giới hạn đó **trùng khớp hoàn toàn với hàm thế trước (prepotential) của lý thuyết Seiberg–Witten**, cung cấp chứng minh toán học đầu tiên cho dự đoán nổi tiếng của Nekrasov!

**Nói cho chính xác:** Okounkov không phát minh ra lý thuyết gauge hay phương trình Seiberg–Witten. Đóng góp mang tầm Fields ở đây là một bộ từ điển phi thường: **tổng theo instanton 4D $$\leftrightarrow$$ phân hoạch ngẫu nhiên $$\leftrightarrow$$ hình dạng giới hạn $$\leftrightarrow$$ đường cong Seiberg–Witten**.

---

## 5. Quá trình Schur, dimer, và những điều không nên khẳng định

Bên cạnh các cây cầu hình học, Okounkov còn tặng cho lý thuyết xác suất hiện đại một công cụ cực mạnh: **độ đo Schur** (Okounkov, 2001) tổng quát hóa độ đo Plancherel bằng cách thay $$(\dim\lambda)^2$$ bằng tích hai hàm Schur $$s_\lambda(x) s_\lambda(y)$$, và **quá trình Schur** (*Schur processes*, **Okounkov–Reshetikhin**, cùng các phát triển của **Borodin–Okounkov–Olshanski**) — một họ các độ đo trên *dãy* phân hoạch có cấu trúc **quá trình điểm định thức** (*determinantal point process*). Chính cấu trúc định thức này giúp ta tính chính xác mọi hàm tương quan của phân hoạch phẳng, mô hình tăng trưởng ngẫu nhiên và mô hình lát dimer.

**Những điều Okounkov không làm:**
- Ông **không** phân loại mọi biểu diễn bất khả quy của mọi nhóm (một chương trình thế kỷ trải khắp nhóm hữu hạn, nhóm Lie, nhóm $$p$$-adic). Công cụ sở trường của ông là nhóm đối xứng, biểu đồ Young và các đại số vô hạn chiều gắn với chúng.
- Ông **không** thay thế hình học đại số bằng tổ hợp; bất biến Gromov–Witten vẫn có bản chất hình học sâu sắc, chỉ là hàm sinh của chúng nhận công thức toán tử từ lý thuyết biểu diễn.
- Ông **không** giải quyết toàn bộ lý thuyết trường lượng tử Seiberg–Witten về mặt vật lý, mà chứng minh đẳng thức toán học cho hàm phân hoạch instanton đã chính quy hóa của Nekrasov.

---

## 6. Vì sao là Huy chương Fields

Văn bản của IMU năm 2006 thẳng thắn ghi nhận một sự thật hiếm có: công trình của Okounkov không chịu nằm gọn trong một ngăn tủ truyền thống nào. Huy chương Fields 2006 tôn vinh sức mạnh của **những cây cầu**:

1. **Một độ đo xác suất tự nhiên hóa thành công cụ hình học.** Độ đo Plancherel và độ đo Schur đi từ bài toán xáo bài ngẫu nhiên sang mặt ngẫu nhiên, đường cong Harnack và không gian moduli.
2. **Hàm sinh trở thành định lý cấu trúc.** Hệ phân cấp 2-Toda và không gian Fock biến hình học đếm Gromov–Witten của $$\mathbb{P}^1$$ thành một lý thuyết hoàn toàn tính được.
3. **Vật lý toán sinh ra toán học tinh khiết hai chiều.** Việc đếm instanton 4D biến thành bài toán hình dạng giới hạn của phân hoạch ngẫu nhiên, vừa xác nhận dự đoán vật lý Seiberg–Witten vừa mở ra cả một nhánh xác suất tích phân mới.

Bài giới thiệu của Giovanni Felder tại ICM 2006, *"The work of Andrei Okounkov"* ([arXiv:math/0609847](https://arxiv.org/abs/math/0609847)), là tài liệu tuyệt vời để đọc nối tiếp sau bài này.

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
