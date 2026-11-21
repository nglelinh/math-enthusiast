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

**Andrei Okounkov** nhận **Huy chương Fields 2006** tại ICM Madrid. Lời trao giải chính thức của IMU chỉ có một câu, nói về việc bắc cầu giữa các lĩnh vực, và khóa học giữ nguyên câu đó:

> For his contributions bridging probability, representation theory and algebraic geometry.

*Tạm dịch: vì những đóng góp bắc cầu giữa xác suất, lý thuyết biểu diễn và hình học đại số.*

Thông cáo báo chí dài hơn của IMU (2006) nói thêm rằng công trình của ông khó xếp vào một lĩnh vực, vì nó chạm tới nhiều vùng, với hai chủ đề lặp lại: **tính ngẫu nhiên** và **lý thuyết biểu diễn cổ điển**, được dùng để giải các bài toán của hình học đại số và cơ học thống kê. Bài này dành cho người đã biết phân hoạch, nhóm đối xứng và hàm sinh, và muốn thấy vì sao một độ đo trên các biểu đồ Young lại liên quan tới bất biến Gromov–Witten hay việc đếm instanton. Bài **không** nói Okounkov đã phân loại mọi biểu diễn, đã phát minh lý thuyết gauge, hay đã thay hình học đại số bằng tổ hợp.

Những người cùng nhận huy chương năm 2006 là **Terence Tao**, **Wendelin Werner** và **Grigori Perelman** (người từ chối nhận). Bốn huy chương, bốn kiểu kết nối các lĩnh vực khác nhau.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại lời trao giải của IMU năm 2006 như một **cây cầu** giữa các lĩnh vực, không phải một định lý phân loại.
- Mô tả **độ đo Plancherel** trên các phân hoạch của $$n$$ và kết quả về **hình dạng giới hạn** của Vershik–Kerov và Logan–Shepp.
- Giải thích ngắn gọn vì sao các biểu diễn của nhóm đối xứng được đánh chỉ số bằng phân hoạch, và vì sao tính ngẫu nhiên trên các phân hoạch đó là một câu hỏi xác suất.
- Đặt công trình về lý thuyết Gromov–Witten của **Okounkov–Pandharipande** (cùng các hàm sinh Hurwitz và "chu trình hoàn chỉnh" liên quan) vào vị trí của nó: hình học đếm được tính bằng các toán tử của lý thuyết biểu diễn.
- Xem việc đếm instanton của **Nekrasov–Okounkov** như một **cây cầu nghiên cứu** tới hình học Seiberg–Witten, chứ không phải "Okounkov phát minh lý thuyết gauge".
- Nêu tên **độ đo Schur / quá trình Schur** (Okounkov; Borodin–Okounkov–Olshanski và các cộng sự) và các mô hình dimer / tinh thể nóng chảy (trong đó có Kenyon–Okounkov) như những chủ đề xác suất tổ hợp liên quan.
- Tránh nói rằng ông đã phân loại mọi biểu diễn của mọi nhóm.

**Kiến thức nền.** Phân hoạch một số nguyên; nhóm đối xứng $$S_n$$ ở mức "các biểu diễn bất khả quy được gắn nhãn bằng biểu đồ Young"; hàm sinh. Về hình học đại số, chỉ cần biết "có thể đếm các đường cong trong một đa tạp theo một nghĩa ảo" là đủ để hiểu ý chính của lý thuyết Gromov–Witten. Không cần lý thuyết trường lượng tử.

**Liên kết với các bài khác.** Bài này minh họa một chương trình nghiên cứu bắc cầu sâu giữa các lĩnh vực, và việc trích dẫn đúng lời trao giải. Người cùng năm: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Về hình học không gian moduli: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (một không gian moduli khác, nhưng cùng ý tưởng "không gian các hình dạng trở thành đối tượng của động lực học hoặc xác suất").

---

## 1. Phân hoạch: bảng chữ cái chung

Một **phân hoạch** của số nguyên dương $$n$$ là một dãy không tăng các số nguyên dương có tổng bằng $$n$$. Người ta vẽ nó thành một **biểu đồ Young** (các hàng ô vuông xếp chồng). Cùng các biểu đồ đó được dùng để đánh chỉ số:

- các lớp liên hợp và các **biểu diễn bất khả quy** của nhóm đối xứng $$S_n$$;
- các hàm Schur trong vành các hàm đối xứng;
- nhiều cấu hình trong cơ học thống kê (lát bằng hình thoi, phân hoạch phẳng, phủ dimer sau khi đổi cách nhìn).

**Độ đo Plancherel** trên các phân hoạch của $$n$$ là phân phối xác suất

$$
\mathbb{P}(\lambda)=\frac{\bigl(\dim\lambda\bigr)^2}{n!},
$$

trong đó $$\dim\lambda$$ là số chiều của biểu diễn bất khả quy của $$S_n$$ ứng với $$\lambda$$. Trong các độ đo tự nhiên trên biểu đồ, đây là độ đo gắn chặt nhất với lý thuyết biểu diễn. Có thể hiểu nó theo hai cách tương đương: đó là phân phối của hình dạng thu được khi áp dụng phép tương ứng Robinson–Schensted cho một hoán vị ngẫu nhiên đều trong $$S_n$$; và đó là cách biểu diễn chính quy tách thành các biểu diễn bất khả quy (phân tích Plancherel).

**Vershik–Kerov**, và độc lập là **Logan–Shepp** (cuối thập niên 1970), chứng minh rằng một biểu đồ ngẫu nhiên theo độ đo Plancherel, sau khi co theo hệ số $$\sqrt{n}$$, hội tụ tới một **hình dạng giới hạn** tất định. Hình dạng đó là một đường cong trơn trên mặt phẳng, trông như một bậc thang bị xoay rồi làm mượt. Phân hoạch điển hình không phải một cái móc dài và mảnh, cũng không phải một hình vuông; nó bám theo một đường cong có công thức tường minh. Thăng giáng quanh hình dạng đó, và thống kê của các hàng dài nhất, trở thành một hướng nghiên cứu trong thập niên 1990, gắn với lý thuyết ma trận ngẫu nhiên.

**Tóm tắt.** Khi lý thuyết biểu diễn cho ta một độ đo tự nhiên trên các biểu đồ, thì lý thuyết biểu diễn tiệm cận *chính là* một chương của xác suất.

---

## 2. Các kết quả của Okounkov: từ BDJ tới mặt ngẫu nhiên

**Baik–Deift–Johansson** chứng minh rằng thăng giáng của dãy con tăng dài nhất trong một hoán vị ngẫu nhiên (tương đương: hàng đầu tiên của một phân hoạch ngẫu nhiên theo Plancherel) tuân theo luật **Tracy–Widom**, chính là luật của trị riêng lớn nhất của ma trận Hermite Gauss. Họ dự đoán rằng sự trùng khớp này còn đúng cho phân phối đồng thời của vài hàng đầu tiên. Okounkov chứng minh dự đoán đó theo một con đường riêng: cả hai bài toán đều trùng với một bài toán thứ ba về **đếm mặt ngẫu nhiên** (các sơ đồ Feynman ứng với phủ phân nhánh). **Borodin–Okounkov–Olshanski** đưa ra một chứng minh khác, và Johansson cũng có một chứng minh. Hãy ghi công cho cả nhóm kết quả này, rồi mới nói tới cách so sánh hình học riêng của Okounkov.

Văn bản IMU năm 2006 nêu kết quả sớm này như một hạt giống: một liên hệ trực tiếp giữa ma trận ngẫu nhiên, hoán vị ngẫu nhiên và hình học đại số. Các công trình sau xử lý **phân hoạch phẳng ngẫu nhiên** và mô hình "tinh thể nóng chảy" (melting crystal): nếu lấy bớt ngẫu nhiên các khối lập phương khỏi một góc, với trọng số thích hợp, thì ở thang vĩ mô vùng "lỏng" được giới hạn bởi một **đường cong đại số**. **Kenyon–Okounkov** (và các công trình về dimer liên quan, cùng Sheffield và những người khác) chứng minh chính xác kết luận bất ngờ đó, rằng biên là một đường cong đại số thực. Một lần nữa, đây là một cây cầu: một định lý về hình dạng trong cơ học thống kê dẫn tới hình học đại số.

Okounkov không phát minh ra hình dạng giới hạn (Vershik–Kerov, Logan–Shepp) và cũng không phát minh luật Tracy–Widom của ma trận ngẫu nhiên (Tracy–Widom; BDJ). Ông *nối* các đối tượng đó với mặt, với phủ, và sau đó với hàm sinh Gromov–Witten và lý thuyết gauge.

---

## 3. Lý thuyết Gromov–Witten như những hàm sinh

**Lý thuyết Gromov–Witten** đếm (theo nghĩa ảo) các ánh xạ chỉnh hình từ một đường cong vào một đa tạp đích, thỏa các điều kiện cho trước. Đây là ngôn ngữ hiện đại của hình học đếm, được vật lý bổ sung nhiều ý tưởng. Các con số được gói lại thành hàm sinh. Okounkov, đặc biệt là cùng **Rahul Pandharipande**, xây dựng một hình thức toán tử, trong đó các hàm sinh này trở thành giá trị kỳ vọng chân không trong một không gian Fock (biểu diễn "nêm vô hạn" của đại số Heisenberg / đại số fermion, cũng chính là đại số tổ chức hàm Schur và phân hoạch).

Một ví dụ cụ thể là lý thuyết Gromov–Witten khi đa tạp đích là một **đường cong**, trong đó có **lý thuyết Gromov–Witten đẳng biến của $$\mathbb{P}^1$$**. Okounkov–Pandharipande đồng nhất phần dừng (stationary sector) với **lý thuyết Hurwitz** có chèn thêm các **chu trình hoàn chỉnh** (completed cycles), và chỉ ra rằng lý thuyết đẳng biến của $$\mathbb{P}^1$$ được điều khiển bởi **hệ phân cấp 2-Toda**. Các bài báo (trong đó có *Ann. of Math.* **163**, 2006, và loạt bài trên arXiv bắt đầu từ [math/0207233](https://arxiv.org/abs/math/0207233)) là những mốc chính.

Cùng **Maulik, Nekrasov và Pandharipande**, Okounkov cũng đưa ra các giả thuyết nổi tiếng nối bất biến **Gromov–Witten** với bất biến **Donaldson–Thomas** của đa tạp ba chiều. Đây là một cây cầu khác, lần này giữa hai lý thuyết đếm. Nó không có nghĩa là một trong hai lý thuyết được phát minh năm 2006.

**Tóm tắt.** Hình học đếm trở nên tính được khi ta nhận ra hàm sinh của nó là một hàm tau, hay một phần tử ma trận chân không, vốn đã được nghiên cứu trong lý thuyết biểu diễn.

---

## 4. Hàm phân hoạch Nekrasov: một cây cầu nghiên cứu

**Nekrasov** (2002) đưa ra một định nghĩa toán học chặt chẽ, đã được chính quy hóa, cho hàm phân hoạch của một số lý thuyết gauge siêu đối xứng $$\mathcal{N}=2$$ bốn chiều, dưới dạng một tích phân đẳng biến trên không gian moduli instanton, tính bằng phương pháp định vị (localization). **Nekrasov–Okounkov** chỉ ra rằng tích phân định vị này có thể viết lại thành một độ đo trên các phân hoạch, với một thế năng tuần hoàn, và đồng nhất hàm thế trước (prepotential) Seiberg–Witten với **sức căng bề mặt của một hình dạng giới hạn**. Bài tổng quan của Okounkov viết gần thời điểm ICM, "Random partitions and instanton counting" ([arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)), là một bản đồ dễ đọc.

**Nói cho chính xác.** Hình học Seiberg–Witten và định nghĩa của Nekrasov có trước hoặc song song với công trình chung này. Okounkov không phát minh lý thuyết gauge. Đóng góp ở đây là một bộ từ điển: tổng theo instanton *chính là* một mô hình phân hoạch ngẫu nhiên; nhiệt động học của mô hình đó *chính là* đường cong Seiberg–Witten. Đó đúng là kiểu cây cầu mà lời trao giải của IMU nhắc tới.

---

## 5. Quá trình Schur, dimer, và những điều không nên khẳng định

**Độ đo Schur** (Okounkov) tổng quát hóa độ đo Plancherel bằng cách gán trọng số cho các biểu đồ bằng hàm Schur. **Quá trình Schur** (Okounkov–Reshetikhin, và nhóm **Borodin, Okounkov, Olshanski**) là các độ đo trên *dãy* phân hoạch có hàm tương quan dạng định thức. Chúng mô hình hóa phân hoạch phẳng, một số quá trình tăng trưởng, và sau khi chuyển đổi, cả mô hình dimer và bài toán lát. Khóa học nên nêu tên các cộng sự: đây không phải công trình của một người về mọi quá trình định thức.

**Những điều Okounkov không làm.**

- Ông không phân loại mọi biểu diễn bất khả quy của mọi nhóm. Nhóm đối xứng, nhóm đối xứng vô hạn và lý thuyết biểu diễn tổ hợp liên quan là lĩnh vực chính của ông. "Phân loại biểu diễn" là một chương trình khác, kéo dài cả thế kỷ (nhóm hữu hạn, nhóm Lie, nhóm p-adic, …).
- Ông không thay thế hình học đại số. Bất biến Gromov–Witten vẫn mang bản chất hình học; điều mới là trong những trường hợp quan trọng, hàm sinh của chúng có công thức đóng từ lý thuyết biểu diễn.
- Ông không giải quyết xong lý thuyết Seiberg–Witten về mặt vật lý. Ông đưa ra một sự đồng nhất toán học trong một mô hình instanton đã được chính quy hóa.

---

## 6. Vì sao là Huy chương Fields

Văn bản của IMU năm 2006 thẳng thắn một cách hiếm thấy: công trình khó xếp loại. Và đó chính là điểm đáng chú ý. Một Huy chương Fields có thể ghi nhận một **bộ từ điển** giúp ba lĩnh vực tính được câu trả lời cho câu hỏi của nhau.

1. **Một độ đo tự nhiên trở thành công cụ hình học.** Độ đo Plancherel và các biến dạng Schur của nó đi từ lý thuyết nhóm tiệm cận sang mặt ngẫu nhiên và hình học đếm.
2. **Hàm sinh trở thành định lý.** Hệ phân cấp Toda và các kỳ vọng chân không không chỉ để trang trí; trong hình thức Okounkov–Pandharipande, chúng *chính là* lý thuyết Gromov–Witten của $$\mathbb{P}^1$$.
3. **Vật lý là nguồn của các bài toán toán học đặt đúng.** Việc đếm instanton, sau khi chính quy hóa, trở thành một bài toán hình dạng giới hạn. Cây cầu này ở mức nghiên cứu và đi theo cả hai chiều.

Bài giới thiệu của Giovanni Felder tại ICM, "The work of Andrei Okounkov" ([arXiv:math/0609847](https://arxiv.org/abs/math/0609847)), là bài nên đọc tiếp sau bài này.

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

## Bài tập

1. Viết trọng số Plancherel $$\mathbb{P}(\lambda)$$ và giải thích trong một câu vì sao nó đến từ lý thuyết biểu diễn chứ không phải phân phối đều.
2. Một **hình dạng giới hạn** bỏ qua điều gì, và giữ lại điều gì, về một biểu đồ Young ngẫu nhiên cỡ $$n$$?
3. Baik–Deift–Johansson, Okounkov, Borodin–Okounkov–Olshanski: trong ba dòng, cho biết ai làm gì với bài toán dãy con tăng dài nhất / hàng đầu tiên.
4. Tóm tắt trong một câu kết quả của Okounkov–Pandharipande về $$\mathbb{P}^1$$, dùng các từ: hàm sinh, toán tử, hệ phân cấp khả tích.
5. Vì sao câu "Nekrasov–Okounkov nghĩa là Okounkov phát minh instanton" là sai? Viết lại thành hai câu đúng.
6. **Luyện phát biểu chính xác.** Viết lại câu "Okounkov phân loại các biểu diễn và giải lý thuyết dây" thành hai câu chính xác, phù hợp với khóa học.
7. **Mở rộng.** So sánh cây cầu này (xác suất $$\leftrightarrow$$ lý thuyết biểu diễn $$\leftrightarrow$$ hình học đếm) với cây cầu của [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (hình học hyperbolic $$\leftrightarrow$$ không gian moduli $$\leftrightarrow$$ động lực học). Trong mỗi câu chuyện, "hình dạng ngẫu nhiên" là gì?

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
