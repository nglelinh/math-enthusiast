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

**Andrei Okounkov** nhận **Huy chương Fields 2006** tại ICM Madrid. Citation chính thức của IMU là một câu cầu nối, và khóa học này giữ nguyên tính chính thức:

> For his contributions bridging probability, representation theory and algebraic geometry.

Văn bản báo chí dài hơn của IMU (2006) thêm rằng công trình khó phân loại vì chạm nhiều vùng, với hai chủ đề lặp lại: **tính ngẫu nhiên** và **lý thuyết biểu diễn cổ điển**, được dùng chống các bài toán hình học đại số và cơ học thống kê. Bài này dành cho người đã gặp phân hoạch, nhóm đối xứng, và ý tưởng hàm sinh, muốn thấy vì sao một độ đo trên diagram Young có thể nói với bất biến Gromov–Witten hoặc với đếm instanton. Bài **không** khẳng định Okounkov đã phân loại mọi biểu diễn, phát minh lý thuyết gauge, hay thay hình học đại số bằng tổ hợp.

Lớp 2006 còn gồm **Terence Tao**, **Wendelin Werner**, và **Grigori Perelman** (người từ chối). Bốn huy chương, bốn phong cách “cầu.”

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lại citation IMU 2006 như một **cây cầu**, không phải định lý phân loại.
- Mô tả **độ đo Plancherel** trên các phân hoạch của $$n$$ và phong cảnh **hình dạng giới hạn** của Vershik–Kerov và Logan–Shepp.
- Giải thích, ở mức khẩu hiệu, lý thuyết biểu diễn nhóm đối xứng đánh chỉ mục phân hoạch như thế nào, và vì sao tính ngẫu nhiên trên các phân hoạch đó là câu hỏi xác suất.
- Đặt công trình Gromov–Witten **Okounkov–Pandharipande** (và các hàm sinh Hurwitz / completed cycle liên quan) như hình học đếm qua toán tử biểu diễn-lý thuyết.
- Xem đếm instanton **Nekrasov–Okounkov** như một **cầu nghiên cứu** tới hình học Seiberg–Witten, không phải “Okounkov phát minh lý thuyết gauge.”
- Gọi tên **độ đo Schur / quá trình Schur** (Okounkov; Borodin–Okounkov–Olshanski và cộng sự) và các bức tranh dimer / tinh thể chảy (gồm Kenyon–Okounkov) như xác suất tổ hợp láng giềng.
- Tránh tuyên bố ông đã phân loại mọi biểu diễn của mọi nhóm.

**Kiến thức nền.** Phân hoạch một số nguyên; nhóm đối xứng $$S_n$$ ở mức “các biểu diễn bất khả quy được gắn nhãn bởi diagram Young”; hàm sinh. Hình học đại số ở mức “đường cong trong một đa tạp có thể được đếm theo nghĩa ảo” là đủ cho khẩu hiệu Gromov–Witten. Không cần lý thuyết trường lượng tử.

**Liên kết seminar.** LO1 (chương trình cầu nối sâu) và LO6 (kỷ luật citation). Láng giềng cùng năm: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Hình học moduli: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (moduli khác, cùng tinh thần “không gian các hình dạng trở thành động lực hoặc xác suất”).

---

## 1. Phân hoạch như bảng chữ cái chung

Một **phân hoạch** của số nguyên dương $$n$$ là một dãy giảm yếu các số nguyên dương có tổng $$n$$. Người ta vẽ nó như **diagram Young** (một chồng hộp). Cùng những diagram đó đánh chỉ mục:

- lớp liên hợp và **biểu diễn bất khả quy** của nhóm đối xứng $$S_n$$;
- hàm Schur trong vành hàm đối xứng;
- nhiều cấu hình cơ học thống kê (lát lozenge, phân hoạch phẳng, phủ dimer sau đổi tranh).

**Độ đo Plancherel** trên các phân hoạch của $$n$$ là xác suất

$$
\mathbb{P}(\lambda)=\frac{\bigl(\dim\lambda\bigr)^2}{n!},
$$

trong đó $$\dim\lambda$$ là chiều biểu diễn bất khả quy của $$S_n$$ gắn nhãn bởi $$\lambda$$. Đó là độ đo mang tính biểu diễn nhất trong các độ đo tự nhiên trên diagram: nó là pushforward của độ đo Haar (đều) trên $$S_n$$ qua ánh xạ ghi hình dạng của một tableau Young ngẫu nhiên, tương đương phân rã Plancherel của biểu diễn chính quy.

**Vershik–Kerov** và độc lập **Logan–Shepp** (cuối thập niên 1970) chứng minh rằng một diagram Plancherel-ngẫu nhiên, sau khi scale bởi $$\sqrt{n}$$, hội tụ tới một **hình dạng giới hạn** tất định—một đường cong trên mặt phẳng trông như cầu thang xoay, được làm mượt. Phân hoạch điển hình không phải móc dài mỏng và không phải hình vuông; nó ôm một profile mang vẻ đại số. Thăng giáng quanh hình dạng đó, và thống kê các hàng dài nhất, trở thành một ngành thập niên 1990 nối với ma trận ngẫu nhiên.

**Khẩu hiệu.** Một khi biểu diễn cung cấp một độ đo ưu tiên trên diagram, lý thuyết biểu diễn tiệm cận *là* một chương của xác suất.

---

## 2. Các tinh chỉnh của Okounkov: từ BDJ tới mặt ngẫu nhiên

**Baik–Deift–Johansson** xác định thăng giáng của dãy con tăng dài nhất của một hoán vị ngẫu nhiên (tương đương hàng đầu của một phân hoạch Plancherel-ngẫu nhiên) và quan sát luật **Tracy–Widom** của trị riêng lớn nhất của ma trận Hermitian Gauss. Họ phỏng đoán sự khớp cho luật đồng thời của vài hàng đầu. Okounkov chứng minh giả thuyết đó bằng một đường riêng: cả hai bài toán khớp một bài toán thứ ba về **đếm mặt ngẫu nhiên** (sơ đồ Feynman đối với phủ phân nhánh). Một chứng minh khác do **Borodin–Okounkov–Olshanski** đưa ra; Johansson cũng có một chứng minh. Gán công lao cho phong cảnh, rồi cho phép so sánh hình học của Okounkov.

Bài IMU 2006 nêu kết quả sớm này như một hạt giống: một liên kết trực tiếp giữa ma trận ngẫu nhiên, hoán vị ngẫu nhiên, và hình học đại số. Công trình sau xử lý **phân hoạch phẳng ngẫu nhiên** và “tinh thể chảy”: nếu bớt hộp khỏi một góc một cách ngẫu nhiên với trọng số thích hợp, vùng lỏng vĩ mô bị chặn bởi một **đường cong đại số**. **Kenyon–Okounkov** (và công trình dimer liên quan với Sheffield và những người khác) làm chính xác kết luận đại số thực bất ngờ đó. Khẩu hiệu khóa học một lần nữa là cây cầu: một định lý hình dạng cơ học thống kê đáp xuống hình học đại số.

Okounkov không phát minh hình dạng giới hạn (Vershik–Kerov, Logan–Shepp) và không phát minh luật Tracy–Widom của ma trận ngẫu nhiên (Tracy–Widom; BDJ). Ông *nối* các đối tượng đó với mặt, phủ, và sau đó với các hàm sinh Gromov–Witten và lý thuyết gauge.

---

## 3. Lý thuyết Gromov–Witten như hàm sinh

**Lý thuyết Gromov–Witten** đếm (theo nghĩa ảo) các ánh xạ chỉnh hình từ đường cong tới một đa tạp đích, với điều kiện tới hạn—ngôn ngữ hiện đại của hình học đếm, được vật lý làm giàu. Các số được đóng gói thành hàm sinh. Okounkov, đặc biệt cùng **Rahul Pandharipande**, phát triển một hình thức toán tử trong đó các hàm sinh đó trở thành kỳ vọng chân không trong một không gian Fock (biểu diễn nêm vô hạn của đại số Heisenberg/fermion—cùng đại số tổ chức hàm Schur và phân hoạch).

Một chương cụ thể: lý thuyết Gromov–Witten của **đường cong** đích, gồm **lý thuyết Gromov–Witten đẳng biến của $$\mathbb{P}^1$$**. Okounkov–Pandharipande đồng nhất sector dừng với **lý thuyết Hurwitz** có chèn **completed cycle**, và chỉ ra rằng lý thuyết đẳng biến của $$\mathbb{P}^1$$ chịu sự chi phối của **phân tầng 2-Toda**. Các bài (gồm *Ann. of Math.* **163**, 2006, và chuỗi arXiv bắt đầu từ [math/0207233](https://arxiv.org/abs/math/0207233)) là các mốc mức seminar.

Cùng **Maulik, Nekrasov, và Pandharipande**, Okounkov cũng nêu những giả thuyết nổi tiếng liên hệ bất biến **Gromov–Witten** và **Donaldson–Thomas** của threefold—một cây cầu khác, lần này giữa hai lý thuyết đếm, không phải tuyên bố rằng một trong hai lý thuyết được phát minh năm 2006.

**Khẩu hiệu.** Hình học đếm trở nên tính được khi hàm sinh của nó được nhận ra như một tau-function hoặc phần tử ma trận chân không đã được nghiên cứu trong lý thuyết biểu diễn.

---

## 4. Hàm phân hoạch Nekrasov: một cầu nghiên cứu

**Nekrasov** (2002) đưa ra một định nghĩa chính quy toán học, đã được regularize, của hàm phân hoạch một số lý thuyết gauge siêu đối xứng $$\mathcal{N}=2$$ bốn chiều, như một tích phân đẳng biến trên moduli instanton (một thay thế localization cho cutoff khoảng cách dài). **Nekrasov–Okounkov** chỉ ra rằng tích phân localization này có thể viết lại như một độ đo trên phân hoạch với thế tuần hoàn, và đồng nhất prepotential Seiberg–Witten với **sức căng mặt của một hình dạng giới hạn**. Bài khảo sát gần ICM của Okounkov “Random partitions and instanton counting” ([arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)) là bản đồ dễ đọc.

**Độ chính xác.** Hình học Seiberg–Witten và định nghĩa của Nekrasov đứng trước hoặc cạnh công trình chung. Okounkov không phát minh lý thuyết gauge. Đóng góp là một từ điển: tổng instanton *là* phân hoạch ngẫu nhiên; nhiệt động lực học của chúng *là* đường cong Seiberg–Witten. Đó đúng là loại cầu mà citation IMU gọi tên.

---

## 5. Quá trình Schur, dimer, và điều không được tuyên bố

**Độ đo Schur** (Okounkov) tổng quát hóa Plancherel bằng cách gắn trọng diagram bằng hàm Schur. **Quá trình Schur** (Okounkov–Reshetikhin và vòng **Borodin, Okounkov, Olshanski**) là các độ đo trên *dãy* phân hoạch với hàm tương quan định thức. Chúng mô hình phân hoạch phẳng, một số quá trình tăng trưởng, và, sau phiên dịch, mô hình dimer và lát. Khóa học nên gọi tên cộng sự: đây không phải kiểm kê một mình mọi quá trình định thức.

**Điều Okounkov không làm.**

- Ông không phân loại mọi biểu diễn bất khả quy của mọi nhóm. Nhóm đối xứng, nhóm đối xứng vô hạn, và lý thuyết biểu diễn tổ hợp liên quan là lãnh thổ nhà; “phân loại biểu diễn” là một chương trình dài thế kỷ khác (nhóm hữu hạn, nhóm Lie, nhóm p-adic, …).
- Ông không thay thế hình học đại số. Bất biến Gromov–Witten vẫn mang tính hình học; sự thật mới là hàm sinh của chúng có dạng đóng biểu diễn-lý thuyết trong những trường hợp quan trọng.
- Ông không khép lý thuyết Seiberg–Witten như vật lý. Ông cung cấp một đồng nhất toán học trong một mô hình instanton đã regularize.

---

## 6. Vì sao là Huy chương Fields

Bài IMU 2006 thành thật khác thường về thể loại: công trình khó phân loại. Đó chính là điểm. Một Huy chương Fields có thể thưởng một **từ điển** khiến ba lĩnh vực tính được câu trả lời của nhau.

1. **Một độ đo ưu tiên trở thành công cụ hình học.** Plancherel và các biến dạng Schur của nó chuyển từ lý thuyết nhóm tiệm cận sang mặt ngẫu nhiên và hình học đếm.
2. **Hàm sinh như định lý.** Phân tầng Toda và kỳ vọng chân không không phải trang trí; chúng *là* lý thuyết GW của $$\mathbb{P}^1$$ trong hình thức Okounkov–Pandharipande.
3. **Vật lý như nguồn toán đặt đúng.** Đếm instanton, một khi được regularize, trở thành bài toán hình dạng giới hạn. Cây cầu ở mức nghiên cứu và hai chiều.

Bài trình bày kiểu Bourbaki / ICM của Giovanni Felder “The work of Andrei Okounkov” ([arXiv:math/0609847](https://arxiv.org/abs/math/0609847)) là bài đọc tiếp theo được khuyến nghị sau bài này.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Okounkov đã phân loại mọi biểu diễn.” | Ông dùng lý thuyết biểu diễn nhóm đối xứng (và họ hàng) như một cây cầu; phân loại biểu diễn là dự án khác. |
| “Okounkov phát minh hình dạng giới hạn Plancherel.” | Vershik–Kerov và Logan–Shepp thiết lập hình dạng; Okounkov tinh chỉnh các liên kết và ứng dụng. |
| “Okounkov phát minh lý thuyết gauge / Seiberg–Witten.” | Nekrasov định nghĩa hàm phân hoạch đã regularize; Nekrasov–Okounkov đồng nhất nó với phân hoạch ngẫu nhiên. |
| “Lý thuyết Gromov–Witten chỉ là tổ hợp.” | Các bất biến mang tính hình học; một số hàm sinh nhận công thức tổ hợp/biểu diễn. |
| “Độ đo Plancherel đều trên các phân hoạch.” | Nó gắn trọng một diagram bằng $$(\dim\lambda)^2/n!$$, không phải $$1/p(n)$$. |
| “Huy chương 2006 chỉ là ma trận ngẫu nhiên.” | Liên kết ma trận ngẫu nhiên là một chương sớm; các cầu GW và instanton cũng trung tâm trong các tài liệu công chúng. |
| “Quá trình Schur là của một mình Okounkov.” | Okounkov, Reshetikhin, Borodin, Olshanski, và những người khác. |

---

## Bài tập

1. Viết trọng Plancherel $$\mathbb{P}(\lambda)$$ và giải thích trong một câu vì sao nó mang tính biểu diễn chứ không đều.
2. Một **hình dạng giới hạn** quên gì, và giữ gì, về một diagram Young ngẫu nhiên cỡ $$n$$?
3. Baik–Deift–Johansson đối với Okounkov đối với Borodin–Okounkov–Olshanski: trong ba dòng, ai làm gì với bài toán dãy con tăng dài nhất / hàng đầu?
4. Phát biểu một khẩu hiệu một câu cho Okounkov–Pandharipande trên $$\mathbb{P}^1$$: hàm sinh, toán tử, phân tầng khả tích.
5. Vì sao “Nekrasov–Okounkov = Okounkov phát minh instanton” sai? Viết một sửa hai câu.
6. **Luyện độ chính xác.** Viết lại “Okounkov phân loại biểu diễn và giải lý thuyết dây” thành hai câu chính xác phù hợp khóa học này.
7. **Seminar mở rộng.** So sánh cây cầu này (xác suất $$\leftrightarrow$$ biểu diễn $$\leftrightarrow$$ hình học đếm) với cây cầu của [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (hình học hyperbolic $$\leftrightarrow$$ moduli $$\leftrightarrow$$ động lực). “Hình dạng ngẫu nhiên” là gì trong mỗi câu chuyện?

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

- Đọc chân dung ngắn của Felder, rồi một lời mở Okounkov–Pandharipande, rồi khảo sát instanton—đừng bắt đầu bằng Seiberg–Witten như vật lý.
- So sánh Plancherel với độ đo đều trên phân hoạch: cùng diagram, hình dạng điển hình khác.
- Seminar A3: một trang “sơ đồ cầu” với ba nút (xác suất, biểu diễn, hình học đếm) và hai cạnh bạn thực sự gọi tên được (Plancherel; toán tử GW/Hurwitz).
