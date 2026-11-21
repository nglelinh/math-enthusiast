---
layout: post
title: "Bài toán đàn bò của Archimedes và phương trình Pell"
chapter: '04'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
---

Archimedes gửi cho Eratosthenes một bài thơ tiếng Hy Lạp dài 44 câu, hỏi đàn bò của thần Mặt Trời có bao nhiêu con. Nửa đầu bài thơ trông như một bài toán tỉ lệ ở trường phổ thông. Nửa sau biến nó thành một trong những **phương trình Pell** nổi tiếng nhất lịch sử. Đàn bò nhỏ nhất thỏa mọi điều kiện có **206.545 chữ số**; in ra sẽ tốn hàng chục trang giấy.

Bài này nói về cú sốc đó, và về bộ máy đứng sau nó: phương trình $$x^2-dy^2=1$$, luật nhóm sinh ra vô hạn nghiệm từ một nghiệm, và thuật toán phân số liên tục để tìm nghiệm đầu tiên.

**Lộ trình:** câu đố → phần tuyến tính và các ràng buộc số chính phương/số tam giác → phương trình Pell (và cái tên bị gán nhầm) → phép hợp thành Brahmagupta → phân số liên tục cho $$d=2$$ → vì sao số chữ số tăng vọt → Pell âm và định lý Stevenhagen → nhầm lẫn thường gặp, bài tập.

Nguồn phổ biến: [Toán Khó (7/8/2026)](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/). Nội dung dưới đây là phần toán học được trình bày lại, không phải bản dịch của trang đó.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tách bài toán đàn bò thành tầng **tuyến tính** và tầng **Pell**, và nói được mỗi tầng cho ra kết quả gì.
- Phát biểu **phương trình Pell** $$x^2-dy^2=1$$ ($$d>0$$ không chính phương) và nêu đúng những người đã phát triển nó (không phải John Pell).
- Nhân hai nghiệm bằng **phép hợp thành Brahmagupta** và hiểu tích đó như một phần tử khả nghịch (đơn vị) trong $$\mathbb{Z}[\sqrt{d}]$$.
- Tính nghiệm cơ bản của $$x^2-2y^2=1$$ từ các phân số xấp xỉ của $$\sqrt{2}$$, rồi sinh ra vài nghiệm tiếp theo.
- Giải thích vì sao chỉ thay đổi $$d$$ một chút cũng có thể làm số chữ số tăng vọt, với ví dụ $$d=61$$ và bài toán đàn bò.
- Phát biểu định lý Lagrange cho trường hợp $$+1$$ và kết quả mật độ **Stevenhagen** cho trường hợp $$-1$$, mà không nói sai thành "58% mọi $$d$$".

**Kiến thức nền.** Số nguyên, số chính phương, ý tưởng về phân số liên tục. Bài [tính vô tỉ của $$\sqrt{2}$$]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/) là bài đọc kèm phù hợp.

---

## 1. Bài thơ không phải câu đố dân gian

Gọi $$W,B,Y,D$$ là số **bò đực** màu trắng, đen, vàng, đốm, và $$w,b,y,d$$ là số **bò cái** cùng màu. Bảy điều kiện tỉ lệ của Archimedes đều là tuyến tính:

$$
\begin{aligned}
W &= Y + \tfrac{5}{6}B, &
B &= Y + \tfrac{9}{20}D, &
D &= Y + \tfrac{13}{42}W,\\
w &= \tfrac{7}{12}(B+b), &
b &= \tfrac{9}{20}(D+d), &
d &= \tfrac{11}{30}(Y+y), &
y &= \tfrac{13}{42}(W+w).
\end{aligned}
$$

Tám ẩn nguyên dương với bảy quan hệ độc lập cho ta một **họ nghiệm phụ thuộc một tham số**. Riêng nghiệm dương nhỏ nhất đã có tổng đàn là

$$
W+B+Y+D+w+b+y+d = 50{,}389{,}082
$$

(với $$W=10{,}366{,}482$$, $$B=7{,}460{,}514$$, $$Y=4{,}149{,}387$$, $$D=7{,}358{,}060$$). Con số này lớn so với một bài toán ở trường, nhưng vẫn viết ra được.

Bài thơ thêm hai ràng buộc **hình học**:

$$
W+B = m^2, \qquad D+Y = \frac{n(n+1)}{2}
$$

với $$m,n\ge 1$$ (bò đực trắng và đen xếp thành hình vuông; bò đực vàng và đốm xếp thành hình tam giác). Thay họ nghiệm tuyến tính vào hai điều kiện này, bài toán quy về một phương trình Pell. Dạng chưa rút gọn là

$$
x^2 - 410{,}286{,}423{,}278{,}424\, y^2 = 1;
$$

bỏ đi thừa số chính phương, phương trình thường được giải là

$$
u^2 - 4{,}729{,}494\, v^2 = 1.
$$

**Tình trạng.** Bài toán đàn bò **đã được giải**, không phải giả thuyết mở. Điều đáng chú ý là *độ lớn* của nghiệm nhỏ nhất và *cấu trúc* sinh ra nó.

---

## 2. Phương trình Pell, một cái tên bị gán nhầm

Với số nguyên dương $$d$$ **không chính phương**, **phương trình Pell** là

$$
x^2 - d y^2 = 1, \qquad x,y\in\mathbb{Z}.
$$

Nghiệm tầm thường $$(\pm 1,0)$$ luôn có. Nội dung chính của lý thuyết là: tồn tại một **nghiệm cơ bản** $$(x_1,y_1)$$ nhỏ nhất với $$x_1>1$$, $$y_1>0$$, và mọi nghiệm dương khác đều sinh ra từ nó bằng một luật nhóm (xem mục sau).

**Tên gọi.** Euler gán nhầm tên phương trình cho John Pell, người gần như không đóng góp gì ở đây. Ở châu Âu thế kỷ 17, Fermat đưa ra thách đố và Brouncker giải được. Nhánh lâu đời hơn và sâu hơn là ở Ấn Độ: **Brahmagupta** (năm 628, sách *Brāhmasphuṭasiddhānta*) và **Bhāskara II** (thế kỷ 12, phương pháp *cakravāla*).

Lagrange (1768) chứng minh rằng với mọi $$d>0$$ không chính phương, phương trình luôn có nghiệm không tầm thường, và có vô hạn nghiệm. Đó là lý thuyết hoàn chỉnh cho trường hợp $$+1$$.

---

## 3. Phép hợp thành Brahmagupta: một đồng nhất thức

Nếu $$x_1^2-dy_1^2=k_1$$ và $$x_2^2-dy_2^2=k_2$$ thì

$$
(x_1x_2+d y_1y_2)^2 - d(x_1y_2+x_2y_1)^2 = k_1k_2.
$$

Đặc biệt, các nghiệm của $$x^2-dy^2=1$$ **nhân** được với nhau:

$$
(x_1,y_1)\ast(x_2,y_2) = (x_1x_2+d y_1y_2,\ x_1y_2+x_2y_1).
$$

Về mặt đại số, đây là tính nhân tính của chuẩn

$$
(x_1+y_1\sqrt{d})(x_2+y_2\sqrt{d}) = (x_1x_2+dy_1y_2)+(x_1y_2+x_2y_1)\sqrt{d}
$$

trong vành $$\mathbb{Z}[\sqrt{d}]$$. Nghiệm Pell chính là các đơn vị có **chuẩn $$+1$$**. Các lũy thừa của đơn vị cơ bản có chuẩn $$+1$$ cho ta mọi nghiệm dương.

Vì vậy "tìm được một nghiệm là có vô hạn nghiệm" không phải là khẩu hiệu suông: đó là nhóm đơn vị của một trường toàn phương thực, một trường hợp riêng của định lý đơn vị Dirichlet.

---

## 4. Tìm nghiệm đầu tiên: $$d=2$$

Phân số liên tục của căn bậc hai một số không chính phương luôn tuần hoàn từ một lúc nào đó. Với $$d=2$$,

$$
\sqrt{2} = [1;\overline{2}] = 1+\frac{1}{2+\frac{1}{2+\cdots}}.
$$

Các phân số xấp xỉ (tiệm cận):

| $$n$$ | $$p_n/q_n$$ | $$p_n^2-2q_n^2$$ |
|------:|:-----------:|-----------------:|
| 0 | $$1/1$$ | $$-1$$ |
| 1 | $$3/2$$ | $$+1$$ |

Vậy $$(x_1,y_1)=(3,2)$$ là nghiệm cơ bản của $$x^2-2y^2=1$$. Phân số xấp xỉ trước đó cho nghiệm của **Pell âm** $$x^2-2y^2=-1$$.

Hợp thành $$(3,2)$$ với chính nó:

$$
(3,2)\ast(3,2) = (9+8,\ 6+6) = (17,12),
$$

rồi $$(17,12)\ast(3,2)=(99,70)$$. Dãy nghiệm tiếp tục: $$(1,0),\ (3,2),\ (17,12),\ (99,70),\ (577,408),\ \ldots$$.

![Điểm nguyên trên hyperbola x² − 2y² = 1]({{ site.baseurl }}/img/chapter_img/pell_hyperbola_d2_toankho.png)

*Hình. Hyperbola $$x^2-2y^2=1$$ và các điểm nguyên. Bảng nghiệm trong hình là đúng. Nhưng công thức đóng khung $$x+y\sqrt{2}=(1+\sqrt{2})^n$$ thì **sai**: $$1+\sqrt{2}$$ có chuẩn $$-1$$, nên các lũy thừa lẻ cho nghiệm của $$x^2-2y^2=-1$$. Nghiệm của phương trình $$+1$$ ứng với lũy thừa chẵn, tức $$(x+y\sqrt{2})=(3+2\sqrt{2})^n=(1+\sqrt{2})^{2n}$$. (Hình nguồn: [Toán Khó](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/); sinh bằng AI.)*

Ý tưởng chứng minh sự tồn tại: có một phân số xấp xỉ $$p/q$$ của $$\sqrt{d}$$ thỏa $$p^2-dq^2=\pm 1$$; nếu là $$-1$$ thì hợp thành nghiệm đó với chính nó sẽ được một nghiệm $$+1$$.

---

## 5. Vì sao các con số tăng vọt

Nhìn hình dạng của $$x^2-dy^2=1$$, không có gì báo trước $$x_1$$ sẽ lớn đến đâu. Độ lớn được quyết định bởi **regulator** $$\log(x_1+y_1\sqrt{d})$$, và đại lượng này có thể nhảy nhiều bậc độ lớn khi $$d$$ chỉ thay đổi 1 đơn vị.

Thách đố của Fermat năm 1657, $$x^2-61y^2=1$$, có nghiệm cơ bản

$$
x_1 = 1{,}766{,}319{,}049, \qquad y_1 = 226{,}153{,}980.
$$

Mười chữ số và chín chữ số, trong khi hệ số $$d$$ chỉ đếm trên hai bàn tay là đủ.

Bài toán đàn bò là cùng hiện tượng đó ở quy mô lớn hơn nhiều. A. Amthor (1880) xác định được tổng đàn nhỏ nhất xấp xỉ

$$
\approx 7.760271\times 10^{206544},
$$

một số nguyên có **206.545 chữ số**, lớn hơn rất nhiều so với số nguyên tử trong vũ trụ quan sát được ($$\sim 10^{80}$$). Các tính toán bằng máy sau này (Williams–German–Zarnke 1965; Nelson 1981) cho ra toàn bộ các chữ số. Đó là việc **viết ra** nghiệm; nó không thay thế định lý tồn tại của Lagrange, vốn đã áp dụng được cho $$d=4{,}729{,}494$$.

![Poster phổ thông về đàn bò / Pell]({{ site.baseurl }}/img/chapter_img/pell_digit_explosion_toankho.png)

*Hình. Poster từ bài nguồn. Con số **206.545** là số chữ số của đàn bò đầy đủ nhỏ nhất. Poster gán con số đó cho $$d=226$$ là **sai**: hệ số Pell đã rút gọn của bài toán đàn bò là $$4{,}729{,}494$$. Hãy dùng hình này làm bài tập đọc phê phán tài liệu toán phổ thông, không dùng làm nguồn số liệu. (Minh họa AI, Toán Khó.)*

---

## 6. Điều gì đã được chứng minh, điều gì tinh tế hơn

| Khẳng định | Tình trạng |
|------------|------------|
| $$x^2-dy^2=1$$ có vô hạn nghiệm với mọi $$d>0$$ không chính phương | **Định lý** (Lagrange 1768) |
| Nghiệm cơ bản đọc được từ phân số liên tục của $$\sqrt{d}$$ | **Định lý** |
| Bài đàn bò có nghiệm dương (khổng lồ) | **Đã giải** (tồn tại thế kỷ 19; đủ chữ số thế kỷ 20) |
| $$x^2-dy^2=-1$$ giải được với mọi $$d$$ như vậy | **Sai** (cản trở địa phương và toàn cục) |
| Trong họ $$d$$ không chính phương đủ điều kiện của Stevenhagen, mật độ những $$d$$ mà $$-1$$ giải được | **Định lý** (giả thuyết Stevenhagen 1993; Koymans–Pagano 2022, [arXiv:2201.13424](https://arxiv.org/abs/2201.13424)). Hằng số $$\approx 58{,}06\%$$, **không** phải “58% mọi $$d$$.” |

Pell âm $$x^2-dy^2=-1$$ hỏi đơn vị cơ bản của $$\mathbb{Q}(\sqrt{d})$$ có chuẩn $$-1$$ hay không. Đây là câu hỏi về 2-phần của nhóm lớp và ký hiệu Rédei, không phải một bản sao của định lý Lagrange.

**Đừng phóng đại ứng dụng.** Đơn vị của trường toàn phương thực (Pell) và **nhóm lớp** của trường toàn phương ảo (bối cảnh của CSIDH và một số hàm trì hoãn kiểm chứng được, VDF, dựa trên nhóm lớp) cùng nằm trong lý thuyết số đại số. Nhưng chúng không phải là một đối tượng. Phương trình Pell không phải là một hệ mật mã hậu lượng tử.

---

## Nhầm lẫn thường gặp

| Khẳng định | Kết luận | Sửa |
|------------|----------|-----|
| “Pell phát minh phương trình Pell.” | **Sai** | Euler gán nhầm; xem Brouncker / Brahmagupta / Bhāskara. |
| “Bài thơ đàn bò chỉ vài nghìn con.” | **Sai** | Phần tuyến tính: $$\sim 5\times 10^7$$. Bài đủ: $$206{,}545$$ chữ số. |
| “$$1+\sqrt{2}$$ sinh nghiệm $$+1$$ cho $$d=2$$.” | **Sai** | Nó sinh nghiệm **chuẩn $$-1$$**; hãy bình phương. |
| “Stevenhagen nói 58% mọi $$d$$ giải được $$-1$$.” | **Sai** | Mật độ trong một họ đủ điều kiện, không phải mọi $$d$$ không chính phương. |
| “206.545 chữ số là nghiệm cho $$d=226$$.” | **Sai** | Đó là đàn bò; $$d$$ đã rút là $$4{,}729{,}494$$. |
| “Pell = CSIDH.” | **Sai** | Số học láng giềng, nhóm khác nhau. |

---

## Bài tập

1. **Tầng tuyến tính.** Với bảy phương trình tỉ lệ, kiểm tra rằng bộ số bắt đầu bằng $$W=10{,}366{,}482$$, $$B=7{,}460{,}514$$, $$Y=4{,}149{,}387$$, $$D=7{,}358{,}060$$ có thể bổ sung số bò cái để cả bảy phương trình đều đúng. (Được phép tra số bò cái; mục tiêu là thấy cách tính toán.)
2. **Hợp thành.** Từ $$(3,2)$$ với $$d=2$$, tự tính hai nghiệm dương tiếp theo và kiểm tra lại phương trình Pell.
3. **Chuẩn $$-1$$.** Chỉ ra rằng $$1^2-2\cdot 1^2=-1$$, và hợp thành $$(1,1)$$ với chính nó thì được $$(3,2)$$.
4. **Không phải mọi $$d$$.** Giải thích trong hai câu vì sao $$x^2-3y^2=-1$$ không có nghiệm nguyên. (Gợi ý: xét modulo 3, hoặc dùng chuẩn.)
5. **Đọc độ lớn.** Nghiệm của Fermat cho $$d=61$$ có $$x$$ gồm 10 chữ số. Vì sao điều đó *không* mâu thuẫn với định lý tồn tại của Lagrange?
6. **Đọc phê phán tài liệu phổ thông.** Liệt kê hai lỗi hoặc chỗ phóng đại trên trang nguồn hoặc poster (tên gọi, $$d=226$$, CSIDH, Lean). Viết lại một câu sao cho bạn cùng lớp có thể tin được.
7. **Nối bài.** Trong tối đa tám câu, liên hệ bài này với nhận xét về phân số liên tục ở cuối bài [chứng minh $$\sqrt{2}$$ vô tỉ]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/).

---

## Tài liệu tham khảo

- Trang nguồn: [Bài toán đàn bò của Archimedes và phương trình Pell](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/) (Toán Khó, truy cập 2026-08-13). Hình sinh bằng AI; đừng tin số viết trên poster.
- Quanta: [Ancient Equations Offer New Look at Number Groups](https://www.quantamagazine.org/ancient-equations-offer-new-look-at-number-groups-20220810/) (10/8/2022).
- P. Koymans & C. Pagano, *On Stevenhagen’s conjecture*, [arXiv:2201.13424](https://arxiv.org/abs/2201.13424).
- H. W. Lenstra Jr., *Solving the Pell equation*, Notices AMS **49** (2002) — survey hiện đại chuẩn.
- E. J. Barbeau, *Pell’s Equation* (Springer) — ví dụ tính toán, gồm $$d=61$$.
- Trong khóa: [Vô tỉ của $$\sqrt{2}$$]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/); [Lý thuyết số → mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) (đừng trộn đơn vị Pell với RSA/CSIDH).

---

## Hướng đi tiếp

- Chạy thuật toán phân số liên tục cho vài giá trị $$d$$ nhỏ (2, 3, 7, 13, 61) và quan sát độ dài chu kỳ.
- Đọc bài tổng quan của Lenstra cho đến khi bạn tự định nghĩa được *regulator* và *infrastructure*.
- Ghi lại một câu hỏi còn bỏ ngỏ, ví dụ: "Phân số xấp xỉ nào của $$\sqrt{d}$$ có thể không cho đơn vị Pell, và vì sao?"
