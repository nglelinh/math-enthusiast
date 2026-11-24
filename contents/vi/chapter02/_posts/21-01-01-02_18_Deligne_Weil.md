---
layout: post
title: "Chứng minh các giả thuyết Weil của Deligne (Huy chương Fields 1978)"
chapter: '02'
order: 18
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử tưởng tượng một bài toán tưởng chừng chỉ dành cho máy tính bỏ túi: cho một phương trình đa thức nhiều biến với hệ số nguyên, chẳng hạn $$y^2 = x^3 + x + 1$$, và ta đếm xem nó có bao nhiêu nghiệm trên các trường hữu hạn $$\mathbb{F}_p, \mathbb{F}_{p^2}, \mathbb{F}_{p^3}, \ldots$$. Thoạt nhìn, đây là một dãy số nguyên rời rạc, lộn xộn và chẳng hề có chút bóng dáng nào của hình học liên tục. Ấy vậy mà vào năm 1949, **André Weil** nhìn thấy bên dưới những con số đếm điểm ấy một cấu trúc đáng kinh ngạc: dãy số nghiệm đó hành xử hệt như thể đa tạp đại số trên trường hữu hạn đang sở hữu những "lỗ hổng tôpô" như mặt cầu hay hình xuyến trong không gian phức, và hàm sinh của nó tuân theo một phiên bản hoàn chỉnh của giả thuyết Riemann.

Phải mất đúng một phần tư thế kỷ, qua ba chặng tiếp sức lịch sử, giấc mơ đó mới trở thành định lý. **Bernard Dwork** (1960) chứng minh tính hữu tỷ của hàm zeta bằng giải tích $$p$$-adic. **Alexander Grothendieck**, **Michael Artin** và trường phái **SGA** dựng lên cả một lâu đài mới mang tên **đối đồng điều étale** để biến bài toán đếm điểm thành công thức vết và suy ra phương trình hàm. Nhưng phần sâu và cứng rắn nhất — **tương tự giả thuyết Riemann**, tức chặn chính xác cho môđun của các trị riêng phép Frobenius — vẫn đứng vững. Năm 1974, khi mới 29 tuổi, **Pierre Deligne** công bố *La conjecture de Weil: I*, đi vòng qua các giả thuyết chuẩn còn bỏ ngỏ của người thầy Grothendieck để hoàn tất mảnh ghép cuối cùng, rồi mở rộng thành bộ máy lý thuyết bó trong *Weil II* (1980).

Chính bước ngoặt đó đã mang lại cho ông **Huy chương Fields 1978**, với ghi nhận của IMU rằng lời giải các giả thuyết Weil "đã góp phần lớn vào việc thống nhất hình học đại số và lý thuyết số đại số." Cũng cần tách bạch ngay từ đầu: Huy chương Fields 1978 không có nghĩa là một mình Deligne xây dựng đối đồng điều étale, càng không có nghĩa là **các giả thuyết chuẩn** về chu trình đại số hay **giả thuyết Hodge** đã được giải. Và giải thưởng **Giải Abel 2013** sau này là sự tôn vinh dành cho cả sự nghiệp đồ sộ của ông, tách biệt hoàn toàn với huy chương năm 1978.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của các giả thuyết Weil: hàm zeta của một đa tạp xạ ảnh trơn trên trường hữu hạn là **hữu tỷ**, thỏa **phương trình hàm**, và có các không điểm, cực điểm nằm trên những đường thẳng đứng xác định (**tương tự giả thuyết Riemann**).
- Ghi nhận đúng công lao của từng chặng: **Dwork** (tính hữu tỷ), **đối đồng điều étale của Grothendieck–Artin** (biểu diễn bằng đối đồng điều và phương trình hàm), và **Deligne** (tính thuần khiết, tức phần tương tự giả thuyết Riemann; *Weil I* và *Weil II*).
- Viết hàm sinh zeta theo biến $$T=q^{-s}$$ và hiểu rõ $$N_m$$ là số điểm trên $$\mathbb{F}_{q^m}$$, đồng thời tự kiểm tra trên các ví dụ cơ sở như đường thẳng xạ ảnh $$\mathbb{P}^1$$ hay đường cong elliptic.
- Giải thích vì sao đối đồng điều étale là *công cụ biến phép đếm thành vết*, còn ước lượng của Deligne cho trị riêng Frobenius là *chặn còn thiếu*.
- Phát biểu cẩn thận rằng chặn Ramanujan–Petersson cho dạng modular chỉnh hình có trọng số ít nhất $$2$$ được suy ra từ các giả thuyết Weil áp dụng cho những đa tạp chiều cao thích hợp (đa tạp Kuga–Sato), chứ không phải từ một lập luận ngắn trên một đường cong modular duy nhất.
- Phân biệt rõ ranh giới của định lý: Deligne **không** chứng minh giả thuyết Riemann cổ điển, **không** chứng minh các giả thuyết chuẩn, và **không** chứng minh giả thuyết Hodge.

**Kiến thức cần có.** Trường hữu hạn $$\mathbb{F}_q$$; ý tưởng về đa tạp xạ ảnh và việc đếm điểm hữu tỷ; tích Euler và giả thuyết Riemann cổ điển như *mô hình* cho một phát biểu về không điểm. Không bắt buộc biết lược đồ hay phạm trù dẫn xuất; chỉ cần nghĩ đến "một lý thuyết đối đồng điều có công thức vết Lefschetz".

**Liên hệ với khóa học.** Giả thuyết Riemann cổ điển, vẫn còn mở: [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Các bài liên quan về hình học số học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) (hàm $$L$$ của đường cong trên $$\mathbb{Q}$$), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Scholze và đối đồng điều $$p$$-adic]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/). Về giải thưởng cho cả sự nghiệp: [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

---

## Bản đồ kiến thức nền: Hình học đại số và đối đồng điều étale là gì?

Nếu bạn tốt nghiệp đại học ngành khoa học hay kỹ thuật nhưng chưa từng học qua hình học đại số hiện đại, cụm từ "đối đồng điều étale với hệ số $$\ell$$-adic" nghe rất dễ gây choáng ngợp. Thực ra, bản chất của nó bắt nguồn từ một câu hỏi rất gần gũi.

**1. Hình học đại số nghiên cứu gì?**
Trong giải tích, ta nghiên cứu các hình cong bằng đạo hàm, giới hạn và khoảng cách (như mặt cầu $$x^2 + y^2 + z^2 = 1$$ trong $$\mathbb{R}^3$$). **Hình học đại số** cũng nghiên cứu tập nghiệm của các hệ phương trình đa thức — gọi là **đa tạp đại số** — nhưng nó không bó buộc mình vào số thực $$\mathbb{R}$$ hay số phức $$\mathbb{C}$$. Ta có thể lấy cùng một hệ phương trình đa thức đó và xét tập nghiệm của nó trên số hữu tỷ $$\mathbb{Q}$$, hoặc trên một **trường hữu hạn** $$\mathbb{F}_q$$ (chẳng hạn tập các số dư theo modulo một số nguyên tố $$p$$). Khi làm việc trên $$\mathbb{F}_q$$, không gian chỉ gồm hữu hạn điểm rời rạc: không có khái niệm "lân cận nhỏ tùy ý", không có đường cong liên tục, và mọi trực giác từ giải tích cổ điển tưởng như sụp đổ.

**2. Đối đồng điều (cohomology) là gì trong hình học thông thường?**
Trên các không gian quen thuộc như mặt cầu hay hình xuyến (torus), tôpô đại số gắn cho mỗi không gian $$X$$ một dãy các không gian vector hữu hạn chiều $$H^0(X), H^1(X), H^2(X), \ldots$$ gọi là các **nhóm đối đồng điều**. Chiều của $$H^i(X)$$ (gọi là **số Betti** $$b_i$$) đếm số "lỗ hổng $$i$$ chiều":
- Mặt cầu $$S^2$$ có $$b_0 = 1$$ (1 mảnh liên thông), $$b_1 = 0$$ (không có vòng tròn nào không co được về một điểm), $$b_2 = 1$$ (1 khoảng rỗng bên trong).
- Hình xuyến $$T^2$$ (cũng là dáng hình của một đường cong elliptic trên $$\mathbb{C}$$) có $$b_0 = 1$$, $$b_1 = 2$$ (hai vòng độc lập: một vòng quanh lỗ, một vòng quanh thân), $$b_2 = 1$$.

Sức mạnh kỳ diệu của đối đồng điều là **tính hàm tử**: mọi ánh xạ liên tục $$f: X \to X$$ tự động cảm sinh một toán tử tuyến tính $$f^*$$ trên từng không gian vector $$H^i(X)$$. Và **công thức vết Lefschetz** nói rằng số điểm bất động của $$f$$ (những điểm thỏa $$f(x) = x$$) bằng tổng đan dấu các vết (trace) của $$f^*$$ trên các $$H^i(X)$$:

$$
\#\{x \in X : f(x) = x\} = \sum_{i=0}^{2n} (-1)^i\,\mathrm{Tr}\bigl(f^* \mid H^i(X)\bigr).
$$

**3. Đối đồng điều étale là gì và vì sao cần nó?**
Trên trường hữu hạn $$\mathbb{F}_q$$, ta có một ánh xạ cực kỳ tự nhiên là **phép Frobenius** $$\mathrm{Frob}: (x_1, \ldots, x_k) \mapsto (x_1^q, \ldots, x_k^q)$$. Nhờ định lý nhỏ Fermat tổng quát ($$a^q = a \iff a \in \mathbb{F}_q$$), một điểm có tọa độ trong bao đóng đại số $$\overline{\mathbb{F}}_q$$ nằm trong $$\mathbb{F}_q$$ **khi và chỉ khi** nó là điểm bất động của $$\mathrm{Frob}$$! Tương tự, số điểm $$N_m$$ trên $$\mathbb{F}_{q^m}$$ chính là số điểm bất động của $$\mathrm{Frob}^m$$.

Nhưng tôpô Zariski cổ điển của hình học đại số lại quá "thô" (mọi tập mở khác rỗng đều khổng lồ và giao nhau), nên nó không tạo ra được các nhóm đối đồng điều có số Betti đúng như trên $$\mathbb{C}$$. Ý tưởng thiên tài của Grothendieck và Artin là định nghĩa lại khái niệm "tập mở" thành các **phủ étale** — phiên bản đại số của phép vi phôi địa phương trong giải tích. Thay vì cắt không gian thành những mảnh con nhỏ, ta "soi" không gian bằng các không gian phủ không rẽ nhánh phía trên nó. Lý thuyết đối đồng điều xây dựng trên tôpô mới này gọi là **đối đồng điều étale** $$H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}}, \mathbb{Q}_\ell)$$ (với $$\ell \neq p$$ là một số nguyên tố phụ trợ để các không gian vector có đặc số $$0$$). Nó khôi phục đúng các số Betti cổ điển, có công thức vết Lefschetz, và biến bài toán đếm điểm số học thành bài toán đại số tuyến tính về trị riêng của ma trận Frobenius!

---

## 1. Từ bài toán cổ điển đến ý tưởng đột phá: đếm điểm và dự đoán một hàm zeta

Câu chuyện bắt đầu từ đầu thế kỷ XIX, khi Gauss đếm số nghiệm của các phương trình như $$x^3 - y^3 = 1$$ hay $$y^2 = x^4 + 1$$ trên trường hữu hạn $$\mathbb{F}_p$$ để nghiên cứu luật tương hỗ bậc cao. Đến năm 1933, **Helmut Hasse** chứng minh một định lý làm kinh ngạc giới số học cho đường cong elliptic $$E/\mathbb{F}_q$$: số điểm hữu tỷ $$N_1 = \#E(\mathbb{F}_q)$$ luôn dao động rất sát quanh $$q + 1$$ (số điểm của đường thẳng xạ ảnh $$\mathbb{P}^1(\mathbb{F}_q)$$), với sai số không vượt quá $$2\sqrt{q}$$:

$$
|N_1 - (q+1)| \le 2\sqrt{q}.
$$

Hãy dừng lại một giây để thấy con số $$2\sqrt{q}$$ kỳ diệu thế nào. Nếu ta tung $$q$$ đồng xu ngẫu nhiên để chọn tọa độ, độ lệch chuẩn thống kê cũng cỡ $$\sqrt{q}$$. Chặn Hasse nói rằng số điểm trên đường cong elliptic không hề hỗn loạn: sai số tuyệt đối bị khóa chặt bởi $$2\sqrt{q}$$, mà số $$2$$ ở đây chính là số Betti $$b_1 = 2$$ của hình xuyến!

**André Weil** đã chứng minh định lý tương tự cho đường cong có giống $$g$$ bất kỳ (với sai số bị chặn bởi $$2g\sqrt{q}$$) và cho đa tạp abel. Rồi năm 1949, ông gói gọn toàn bộ dãy số đếm điểm $$N_m = \#X(\mathbb{F}_{q^m})$$ của một đa tạp xạ ảnh trơn $$X$$ chiều $$n$$ trên $$\mathbb{F}_q$$ vào một hàm sinh duy nhất gọi là **hàm zeta địa phương**:

$$
Z(X,T)=\exp\Bigl(\sum_{m\ge 1}N_m\frac{T^m}{m}\Bigr),\qquad T=q^{-s}.
$$

**Ví dụ trực quan: đường thẳng xạ ảnh $$\mathbb{P}^1$$.** Trên $$\mathbb{F}_{q^m}$$, đường thẳng xạ ảnh gồm $$q^m$$ điểm hữu hạn cộng thêm $$1$$ điểm ở vô cực, nên $$N_m = q^m + 1$$. Thay vào hàm sinh, ta tính trực tiếp được bằng khai triển $$-\ln(1 - u) = \sum_{m \ge 1} u^m/m$$:

$$
\sum_{m\ge 1}(q^m + 1)\frac{T^m}{m} = -\ln(1 - qT) - \ln(1 - T) \implies Z(\mathbb{P}^1, T) = \frac{1}{(1 - T)(1 - qT)}.
$$

Một chuỗi lũy thừa vô hạn lại thu gọn thành một phân thức hữu tỷ đơn giản, với hai cực điểm ứng với hai trị riêng $$1 = q^{0/2}$$ (từ $$H^0$$) và $$q = q^{2/2}$$ (từ $$H^2$$)!

Weil dự đoán rằng điều kỳ diệu tương tự phải đúng cho **mọi** đa tạp xạ ảnh trơn $$X$$ chiều $$n$$ trên $$\mathbb{F}_q$$:
1. **Tính hữu tỷ:** $$Z(X,T)$$ là một hàm hữu tỷ theo $$T$$.
2. **Phương trình hàm:** $$Z(X,T)$$ liên hệ đối xứng với $$Z(X, 1/(q^n T))$$.
3. **Tương tự giả thuyết Riemann (tính thuần khiết):** Khi viết $$Z(X,T)$$ dưới dạng tích đan dấu các đa thức $$P_i(T)$$, mọi nghịch đảo nghiệm $$\alpha$$ của $$P_i(T)$$ đều là số nguyên đại số có môđun đúng bằng $$q^{i/2}$$. Đặt $$T = q^{-s}$$, điều này có nghĩa là mọi không điểm và cực điểm của $$Z(X, q^{-s})$$ đều nằm gọn trên các đường thẳng đứng $$\mathrm{Re}(s) = i/2$$.
4. **Số Betti:** Nếu $$X$$ là phép rút gọn theo modulo $$p$$ của một đa tạp xạ ảnh trơn trên $$\mathbb{C}$$, thì bậc của $$P_i(T)$$ đúng bằng số Betti $$b_i$$ của đa tạp phức đó.

Sự tương tự với tôpô vừa nổi tiếng vừa gợi mở: trên $$\mathbb{F}_q$$, $$N_m$$ là số điểm bất động của $$\mathrm{Frob}^m$$ trên $$X(\overline{\mathbb{F}}_q)$$. Nếu có một lý thuyết đối đồng điều thỏa công thức vết Lefschetz *và* đối ngẫu Poincaré (để sinh ra phương trình hàm), thì phần tương tự giả thuyết Riemann sẽ lập tức quy về một chặn cho các trị riêng của Frobenius.

**Ba chặng giải quyết:**
- **Bernard Dwork (1960)** bất ngờ chứng minh **tính hữu tỷ** trước tiên bằng giải tích $$p$$-adic, hoàn toàn không cần xây dựng lý thuyết đối đồng điều nào.
- **Grothendieck**, **Michael Artin** và cộng đồng **SGA** xây dựng **đối đồng điều étale** với hệ số $$\ell$$-adic, chứng minh công thức vết Lefschetz và đối ngẫu Poincaré, qua đó thu lại tính hữu tỷ, phương trình hàm và liên hệ với số Betti.
- Grothendieck hy vọng suy ra mảnh ghép cuối cùng — tính thuần khiết — từ **các giả thuyết chuẩn** (*standard conjectures*) về chu trình đại số. Thế nhưng các giả thuyết chuẩn lại quá khó và đến tận ngày nay vẫn còn mở (trừ một số phần như định lý Lefschetz mạnh trong đặc số dương, mà sau này chính Deligne suy ra ngược lại như một hệ quả của giả thuyết Weil). Vì vậy, phần tương tự giả thuyết Riemann cần một con đường đột phá hoàn toàn khác.

---

## 2. Ý chính: Frobenius tác động, và các trị riêng của nó là thuần khiết

Khi đã có đối đồng điều étale, công thức vết Lefschetz cho phép viết trực tiếp hàm zeta của một đa tạp xạ ảnh trơn chiều $$n$$ dưới dạng một phân thức rõ ràng:

$$
Z(X,T)=\frac{P_1(T)P_3(T)\cdots P_{2n-1}(T)}{P_0(T)P_2(T)\cdots P_{2n}(T)},
$$

trong đó mỗi đa thức $$P_i(T) = \det\bigl(1 - T\,\mathrm{Frob} \mid H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}},\mathbb{Q}_\ell)\bigr)$$ là đa thức đặc trưng ngược của tác động Frobenius trên nhóm đối đồng điều bậc $$i$$, với $$P_0(T)=1-T$$ và $$P_{2n}(T)=1-q^n T$$. Khai triển logarit hai vế chính là công thức vết:

$$
N_m = \sum_{i=0}^{2n} (-1)^i \sum_{j=1}^{b_i} \alpha_{i,j}^m,
$$

với $$\alpha_{i,j}$$ là các trị riêng của Frobenius trên $$H^i_{\mathrm{\acute{e}t}}$$. Nhìn vào công thức này, ta thấy ngay vì sao trường hợp đường cong elliptic $$E$$ cho ra chặn Hasse: khi $$n = 1$$, ta có $$b_0 = 1$$ ($$\alpha_{0,1} = 1$$), $$b_2 = 1$$ ($$\alpha_{2,1} = q$$), và $$b_1 = 2$$ (hai trị riêng $$\alpha_1, \alpha_2$$). Do đó $$N_1 = 1 - (\alpha_1 + \alpha_2) + q$$. Nếu $$|\alpha_1| = |\alpha_2| = q^{1/2}$$, bất đẳng thức tam giác lập tức cho $$|N_1 - (q+1)| = |\alpha_1 + \alpha_2| \le 2\sqrt{q}$$!

**Định lý Deligne (Weil I, 1974).** Mọi trị riêng $$\alpha$$ của Frobenius trên $$H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}},\mathbb{Q}_\ell)$$ đều là số đại số và có môđun phức (dưới mọi phép nhúng vào $$\mathbb{C}$$) thỏa $$|\alpha| = q^{i/2}$$. Nói cách khác, các trị riêng của Frobenius trên $$H^i$$ là **thuần khiết với trọng số $$i$$**.

**Ý tưởng đột phá của Deligne để đi vòng qua giả thuyết chuẩn:**
Thay vì cố gắng chứng minh tính xác định dương của các chu trình đại số như Grothendieck mong đợi, Deligne kết hợp một chuỗi kỹ thuật hết sức khéo léo:
1. **Cắt lát bằng chùm Lefschetz (Lefschetz pencil):** Ông cắt một đa tạp chiều $$n$$ thành một họ 1-tham số các siêu mặt chiều $$n-1$$, biến bài toán quy nạp theo số chiều thành việc nghiên cứu sự biến thiên của đối đồng điều dọc theo một đường cong cơ sở (tạo ra một nhóm **đơn đạo** — monodromy).
2. **Thủ thuật Rankin (lũy thừa tenxơ bậc chẵn):** Thay vì ước lượng trực tiếp môđun của một trị riêng $$\alpha$$, Deligne xét lũy thừa tenxơ bậc $$2k$$ của hệ địa phương để mọi số hạng đều trở thành số thực không âm. Nếu có một trị riêng "vượt rào" với $$|\alpha| > q^{i/2}$$, thì khi lấy lũy thừa $$2k$$ rất lớn, sự đóng góp của nó sẽ phình to vượt quá giới hạn hình học của nhóm đơn đạo — một mâu thuẫn giống hệt cách chứng minh bất đẳng thức cổ điển bằng cách nâng lên lũy thừa cao rồi lấy căn bậc $$2k$$!
3. **Kết hợp với đối ngẫu Poincaré:** Chặn trên $$|\alpha| \le q^{i/2}$$ kết hợp với đối ngẫu giữa $$H^i$$ và $$H^{2n-i}$$ (ghép cặp $$\alpha$$ với $$q^n/\alpha$$) lập tức khóa chặt đẳng thức $$|\alpha| = q^{i/2}$$.

**Tóm lại.** Các giả thuyết Weil biến một bài toán đếm điểm số học thành một bài toán về **phổ**: số điểm là vết, còn phần tương tự giả thuyết Riemann giới hạn chính xác đường tròn mà các trị riêng phải nằm trên đó. Trường phái Grothendieck cung cấp các vết; Deligne cung cấp chiếc khóa phổ còn thiếu. Báo cáo của Katz tại ICM Helsinki (1978) vẫn là tài liệu chuẩn về cấu trúc chứng minh vào thời điểm trao huy chương.

---

## 3. Weil II đã làm được gì và chưa làm được gì

Sáu năm sau, trong *La conjecture de Weil: II* (1980), Deligne tiến thêm một bước còn rộng lớn hơn nữa: ông giải phóng định lý khỏi giả thiết đa tạp phải trơn, xạ ảnh và hệ số phải là bó hằng. *Weil II* mở rộng khái niệm trọng số sang **các bó $$\ell$$-adic kiến thiết hỗn hợp** (*mixed constructible sheaves*) trên những lược đồ tùy ý trên trường hữu hạn. Định lý chính của *Weil II* cho thấy phép lấy ảnh trực tiếp có giá compact $$Rf_!$$ bảo toàn bất đẳng thức trọng số (nếu bó đầu vào có trọng số $$\le w$$, thì $$R^i f_!$$ có trọng số $$\le w + i$$). Nhờ một phép biến đổi Fourier $$\ell$$-adic và định lý *Weil II*, lý thuyết bó trở thành ngôn ngữ làm việc hằng ngày của hình học số học hiện đại: một định lý về đa tạp giờ chỉ là trường hợp riêng của một định lý về bó.

**Những gì được làm rõ.** Các tổng mũ phức tạp (như tổng Gauss, tổng Kloosterman nhiều biến), nhóm đơn đạo, và vô số ước lượng vốn thuộc lý thuyết số giải tích nay trở thành những phát biểu hình học về trọng số. Công trình trước đó của Deligne (1969, theo gợi ý của Serre) gắn cho mỗi dạng modular một biểu diễn Galois $$\ell$$-adic, và việc suy ra **giả thuyết Ramanujan–Petersson** cũng nằm trọn trong mạch tư duy này: khi biết trọng số hình học, ta lập tức thu được chặn giải tích sắc bén.

**Ramanujan–Petersson, nói cho cẩn thận.** Xét hàm $$\tau(n)$$ nổi tiếng của Ramanujan — hệ số khai triển của dạng modular biệt thức $$\Delta(q) = q \prod_{m \ge 1}(1 - q^m)^{24} = \sum_{n \ge 1} \tau(n) q^n$$ (trọng số $$k = 12$$). Giả thuyết Ramanujan phát biểu rằng với mọi số nguyên tố $$p$$,

$$
|\tau(p)| \le 2p^{11/2}.
$$

Đây chính là tương tự giả thuyết Riemann cho một đối tượng hình học (motive) trọng số $$11$$ gắn với $$\Delta$$. Deligne đã quy bài toán Ramanujan–Petersson cho mọi dạng cusp chỉnh hình trọng số $$k \ge 2$$ về các giả thuyết Weil cho những đa tạp có số chiều cao hơn — cụ thể là **đa tạp Kuga–Sato** (xây dựng bằng cách lấy tích thớ $$(k-2)$$ lần của đường cong elliptic phổ dụng trên một đường cong modular). Vì vậy, *Weil I* (1974) kéo theo ngay chặn $$|\tau(p)| \le 2p^{11/2}$$! Còn trường hợp trọng số $$k = 1$$ là một câu chuyện khác, được hoàn thành trong công trình chung **Deligne–Serre**. Lưu ý một điểm hay bị nhầm: các chặn cổ điển cho tổng Kloosterman một biến cũng dùng ý tưởng Weil nhưng chỉ ở chiều một, nên chúng đã suy ra từ định lý Weil cho đường cong từ trước năm 1974. Đừng nói "Deligne chặn được tổng Kloosterman nên suy ra Ramanujan"; chặn cho dạng modular trọng số cao đòi hỏi tính thuần khiết ở số chiều cao hơn.

**Những gì chưa được chứng minh.** **Các giả thuyết chuẩn** của Grothendieck vẫn còn mở. **Giả thuyết Hodge** vẫn còn mở. Deligne định nghĩa **chu trình Hodge tuyệt đối** như một khái niệm thay thế hữu hiệu trong nhiều lập luận số học, và ông xây dựng lý thuyết **cấu trúc Hodge hỗn hợp** để tổ chức trọng số trong hình học phức — mở rộng trực giác trọng số của *Weil II* sang thế giới số phức. Đó là những công cụ nền tảng cực mạnh, nhưng không phải lời giải cho giả thuyết Hodge. Lý thuyết motive theo nghĩa mạnh mà Grothendieck mơ ước vẫn là một chương trình nghiên cứu đang mở rộng.

---

## 4. Ghi nhận công lao một cách trung thực

| Người đóng góp | Vai trò |
|----------------|---------|
| Weil (1949; trước đó cho đường cong) | Đặt giả thuyết; chứng minh cho đường cong và đa tạp abel |
| Hasse | Đường cong elliptic trên trường hữu hạn |
| Dwork (1960) | Tính hữu tỷ, bằng phương pháp $$p$$-adic |
| Grothendieck, M. Artin, SGA | Đối đồng điều étale; công thức vết; phương trình hàm |
| Serre | Các ý tưởng sớm về đối đồng điều và dạng modular; sau này Deligne–Serre |
| Deligne, Weil I (1974) | Tương tự giả thuyết Riemann / tính thuần khiết của trị riêng Frobenius |
| Deligne, Weil II (1980) | Trọng số cho bó; dạng làm việc của lý thuyết |
| Các nhà toán học sau đó | Bó perverse (BBD: Beilinson–Bernstein–Deligne, cùng Gabber) và các ứng dụng |

Deligne sinh năm 1944 tại Bỉ, làm luận án dưới sự hướng dẫn của Grothendieck, và làm việc tại IHÉS trong những năm nhận Huy chương Fields, trước khi chuyển sang Institute for Advanced Study (Princeton). Huy chương năm 1978 ghi nhận công trình về giả thuyết Weil và sự thống nhất mà nó mở ra. **Giải Abel 2013**, trao "vì những đóng góp nền tảng cho hình học đại số và ảnh hưởng sâu rộng của chúng đến lý thuyết số, lý thuyết biểu diễn và các lĩnh vực liên quan", là giải cho *cả sự nghiệp*, bao gồm lý thuyết Hodge hỗn hợp, biểu diễn Deligne–Lusztig, không gian moduli của đường cong (cùng Mumford) và nhiều công trình khác. Hãy luôn tách riêng hai giải thưởng này.

---

## 5. Vì sao ông nhận Huy chương Fields, và vì sao câu chuyện này vẫn quan trọng

Các giả thuyết Weil đã định hướng cả một thế hệ toán học thế kỷ XX: chúng buộc giới hình học đại số phải xây dựng lại từ gốc một lý thuyết đối đồng điều mới, rồi lại đòi hỏi một ước lượng phổ sâu sắc mà bản thân lý thuyết đó không tự động nhả ra. Việc hoàn thành các giả thuyết đã nối liền hai cách nhìn tưởng như ở hai vũ trụ khác nhau về cùng một dãy số nguyên $$N_m$$ — một bên là phép đếm nghiệm số học, một bên là tôpô và phổ trị riêng trên trường hữu hạn — đồng thời đưa sức mạnh của hình học đại số vào lý thuyết dạng tự đẳng cấu và tổng mũ. Trong khóa học, câu chuyện Deligne là hình mẫu kinh điển về một **chương trình vĩ đại được nhiều người cùng dựng khung**, rồi được chốt lại bằng một ước lượng mang tính quyết định.

[Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) cổ điển cho hàm $$\zeta(s)$$ trên trường số hữu tỷ vẫn còn mở. Điều đó không hề làm giảm tầm vóc của câu chuyện Weil; ngược lại, nó cho thấy vì sao các nhà toán học ngày nay vẫn tìm cách bắt chước chiến lược của Grothendieck và Deligne (tìm một "đối đồng điều" và một "phép Frobenius" cho $$\mathrm{Spec}(\mathbb{Z})$$). Đôi khi trên báo phổ thông ta bắt gặp câu "Deligne đã chứng minh giả thuyết Riemann". Cách nói chính xác phải là: ông đã chứng minh **tương tự giả thuyết Riemann cho hàm zeta của đa tạp đại số trên trường hữu hạn**.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Deligne phát minh ra đối đồng điều étale." | Grothendieck, Artin và SGA xây dựng lý thuyết đó. |
| "Dwork chứng minh các giả thuyết Weil." | Dwork chứng minh **tính hữu tỷ**. Tính thuần khiết là của Deligne. |
| "Deligne chứng minh các giả thuyết chuẩn / giả thuyết Hodge." | Cả hai vẫn còn mở (ở dạng tổng quát). |
| "Deligne chứng minh giả thuyết Riemann cổ điển." | Ông chứng minh **phiên bản tương tự** cho đa tạp trên $$\mathbb{F}_q$$. |
| "Ramanujan suy ra từ giả thuyết Weil cho một đường cong modular." | Trọng số $$\ge 2$$ cần hình học chiều cao hơn (Kuga–Sato); trọng số 1 là kết quả của Deligne–Serre. |
| "Giải Abel 2013 và Huy chương Fields 1978 là cùng một sự ghi nhận." | Giải Abel là giải cho cả sự nghiệp, trao sau này; Huy chương Fields năm 1978 ghi nhận công trình về giả thuyết Weil. |

---

## Nguồn video và đọc thêm

Bài này không có bộ tài liệu video riêng của khóa học.

1. Huy chương Fields 1978 của IMU (lời trích dẫn cho Deligne): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1978).
2. Bách khoa: [Pierre Deligne](https://en.wikipedia.org/wiki/Pierre_Deligne); [Weil conjectures](https://en.wikipedia.org/wiki/Weil_conjectures).
3. Giải Abel 2013 (giải cho cả sự nghiệp, khác Huy chương Fields): [abelprize.no/abel-prize-laureates/2013](https://abelprize.no/abel-prize-laureates/2013).
4. Thông cáo của IAS (Abel 2013): [Pierre Deligne Awarded 2013 Abel Prize](https://www.ias.edu/press-releases/pierre-deligne-awarded-2013-abel-prize).
5. Tìm trên arXiv: [Deligne Weil](https://arxiv.org/search/?query=Deligne+Weil&searchtype=all).
6. Trong khóa học: [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/); [Tổng quan về Giải Abel]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

**Ghi nhớ:** Đây là tương tự giả thuyết Riemann của Weil trên trường hữu hạn, **không** phải giả thuyết Riemann cổ điển, **không** phải giả thuyết Hodge, **không** phải các giả thuyết chuẩn.

---

## Tài liệu tham khảo

1. International Mathematical Union, Huy chương Fields 1978: Pierre Deligne (văn bản in lại từ sách lịch sử các đại hội của Albers–Alexanderson–Reid năm 1986, đăng trên trang IMU).
2. **A. Weil**, *Numbers of solutions of equations in finite fields*, *Bull. Amer. Math. Soc.* (1949).
3. **B. Dwork**, *On the rationality of the zeta function of an algebraic variety*, *Amer. J. Math.* (1960).
4. **P. Deligne**, *La conjecture de Weil: I*, *Publ. Math. IHÉS* 43 (1974); *La conjecture de Weil: II*, *Publ. Math. IHÉS* 52 (1980).
5. **N. Katz**, *The work of Pierre Deligne*, kỷ yếu ICM Helsinki 1978 (bài tổng quan vào thời điểm trao huy chương).
6. Nền tảng SGA và đối đồng điều étale: Grothendieck–Artin; một giáo trình hiện đại (ví dụ bài giảng của Milne) để tham khảo, không bắt buộc đọc.
7. Lời trích dẫn Giải Abel 2013 cho Pierre Deligne (abelprize.no).
8. Trong khóa học: [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/).

---

## Hướng đi tiếp

- Tự tính $$Z(\mathbb{P}^n,T)$$. Đây là các giả thuyết Weil trong trường hợp không cần đối đồng điều, và giúp bạn quen với ký hiệu.
- Đọc một bài giảng (một buổi) về công thức vết Lefschetz trong đối đồng điều étale trước khi đọc Weil I.
- Bài seminar A3 (tùy chọn): viết một trang về "những gì còn mở sau Deligne" (các giả thuyết chuẩn, giả thuyết Hodge, motive, giả thuyết Riemann cổ điển), tách rõ Huy chương Fields 1978 với Giải Abel 2013.
- Nếu bạn quan tâm đến dạng modular, hãy theo Ramanujan–Petersson đến các bài báo của Deligne, rồi đến Deligne–Serre cho trọng số một, và luôn ghi rõ số chiều của đa tạp được dùng.

## Video tham khảo

- **Xem trước** — [Timothy Gowers: The Weil conjectures explained](https://www.youtube.com/watch?v=PHkYqPX3Je4) — The Abel Prize, tiếng Anh. Timothy Gowers giải thích các giả thuyết Weil cho khán giả rộng, nhân dịp Giải Abel 2013. Nên xem trước khi đọc bài.
- [The Weil Conjectures, from Abel to Deligne - Sophie Morel](https://www.youtube.com/watch?v=iDgtP6ZpR70) — Institute for Advanced Study, tiếng Anh. Sophie Morel kể lại lịch sử các giả thuyết Weil từ Abel đến Deligne, tương ứng với mục 1–2. Nên xem sau khi đọc bài.
- [The Weil conjectures - Lothar Goettsche - 2016](https://www.youtube.com/watch?v=kiQwnXT7j7g) — ICTP Mathematics, tiếng Anh. Bài giảng có tính kỹ thuật hơn về các giả thuyết Weil. Dành cho người muốn đi sâu.
