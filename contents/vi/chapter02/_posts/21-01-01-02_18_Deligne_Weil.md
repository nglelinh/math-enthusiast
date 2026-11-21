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

**Pierre Deligne** nhận **Huy chương Fields 1978**. Theo lời IMU tại đại hội năm đó, giải thưởng dành cho **lời giải các giả thuyết Weil** về tổng quát hóa giả thuyết Riemann cho đa tạp trên trường hữu hạn, một công trình "đã góp phần lớn vào việc thống nhất hình học đại số và lý thuyết số đại số." Huy chương không có nghĩa là một mình ông xây dựng đối đồng điều étale, cũng không có nghĩa là **các giả thuyết chuẩn** về chu trình đại số hay **giả thuyết Hodge** đã được giải. **André Weil** đặt ra các giả thuyết (1949). **Bernard Dwork** chứng minh tính hữu tỷ bằng phương pháp $$p$$-adic (1960). **Trường phái Grothendieck** xây dựng đối đồng điều étale và từ đó thu được phương trình hàm. Deligne chứng minh phần khó nhất còn lại, tức là phần tương tự giả thuyết Riemann, trong *La conjecture de Weil: I* (1974), và sau đó một dạng tổng quát hơn dùng lý thuyết bó trong *Weil II* (1980).

Bài này dành cho người đã biết hàm zeta Riemann và khái niệm đa tạp xạ ảnh, và muốn thấy một bài toán đếm điểm trên $$\mathbb{F}_q$$ trở thành một định lý về trị riêng của phép Frobenius. Một giải thưởng sau này, **Giải Abel 2013**, ghi nhận đóng góp cả sự nghiệp của ông. Giải đó khác với Huy chương Fields 1978 và không nên gộp chung.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của các giả thuyết Weil: hàm zeta của một đa tạp xạ ảnh trơn trên trường hữu hạn là **hữu tỷ**, thỏa **phương trình hàm**, và có các không điểm, cực điểm nằm trên những đường thẳng đứng xác định (**tương tự giả thuyết Riemann**).
- Ghi nhận đúng công lao: **Dwork** (tính hữu tỷ), **đối đồng điều étale của Grothendieck–Artin** (biểu diễn bằng đối đồng điều và phương trình hàm), **Deligne** (tính thuần khiết, tức phần tương tự giả thuyết Riemann; Weil I và Weil II).
- Viết hàm sinh zeta theo biến $$T=q^{-s}$$ và hiểu $$N_m$$ là số điểm trên $$\mathbb{F}_{q^m}$$.
- Giải thích vì sao đối đồng điều étale là *công cụ*, còn ước lượng của Deligne cho trị riêng Frobenius là *chặn còn thiếu*.
- Phát biểu cẩn thận rằng chặn Ramanujan–Petersson cho dạng modular chỉnh hình có trọng số ít nhất $$2$$ được suy ra từ các giả thuyết Weil áp dụng cho những đa tạp thích hợp (đa tạp Kuga–Sato), chứ không phải từ một lập luận ngắn trên một đường cong modular duy nhất.
- Bác bỏ hai khẳng định quá mức: Deligne **không** chứng minh các giả thuyết chuẩn, và **không** chứng minh giả thuyết Hodge.

**Kiến thức cần có.** Trường hữu hạn $$\mathbb{F}_q$$; ý tưởng về đa tạp xạ ảnh và việc đếm điểm hữu tỷ; tích Euler và giả thuyết Riemann cổ điển như *mô hình* cho một phát biểu về không điểm. Không bắt buộc biết lược đồ hay phạm trù dẫn xuất; chỉ cần nghĩ đến "một lý thuyết đối đồng điều có công thức vết Lefschetz".

**Liên hệ với khóa học.** Giả thuyết Riemann cổ điển, vẫn còn mở: [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Các bài liên quan về hình học số học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) (hàm $$L$$ của đường cong trên $$\mathbb{Q}$$), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Scholze và đối đồng điều $$p$$-adic]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/). Về giải thưởng cho cả sự nghiệp: [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

---

## 1. Lịch sử: đếm điểm và dự đoán một hàm zeta

Gauss đã đếm số điểm trên một số đường cong elliptic trên trường hữu hạn khi nghiên cứu về chu kỳ và lý thuyết chia đường tròn. **Hasse** chứng minh tương tự của giả thuyết Riemann cho đường cong elliptic: nếu $$E/\mathbb{F}_q$$ có $$N_1$$ điểm thì $$|N_1-(q+1)|\le 2\sqrt{q}$$. **Weil** chứng minh các giả thuyết này cho đường cong có giống bất kỳ và cho đa tạp abel, rồi năm 1949 đề xuất phát biểu tổng quát cho đa tạp xạ ảnh trơn ở mọi số chiều. Hàm sinh

$$
Z(X,T)=\exp\Bigl(\sum_{m\ge 1}N_m\frac{T^m}{m}\Bigr),\qquad T=q^{-s},
$$

phải là một hàm **hữu tỷ** theo $$T$$; phải thỏa một **phương trình hàm** liên hệ $$Z(X,T)$$ với $$Z(X,1/q^n T)$$ (với $$n=\dim X$$); và các nghịch đảo của nghiệm của nhân tử bậc $$i$$ phải có môđun bằng $$q^{i/2}$$. Điều kiện cuối là **tương tự giả thuyết Riemann**, còn gọi là **tính thuần khiết**. Mệnh đề thứ tư nói rằng bậc của các nhân tử bằng số Betti của một đa tạp phức tương ứng, khi đa tạp đó tồn tại.

Sự tương tự với tôpô vừa nổi tiếng vừa gợi mở. Trên $$\mathbb{C}$$, công thức vết Lefschetz đếm số điểm bất động của một ánh xạ qua các vết trên đối đồng điều. Trên $$\mathbb{F}_q$$, Frobenius là một ánh xạ, và $$N_m$$ chính là số điểm bất động của nó (lặp $$m$$ lần) trên $$X(\overline{\mathbb{F}}_q)$$. Nếu có một lý thuyết đối đồng điều với công thức vết *và* đối ngẫu Poincaré (để sinh ra phương trình hàm), thì phần tương tự giả thuyết Riemann sẽ trở thành một chặn cho các trị riêng.

**Dwork (1960)** chứng minh tính hữu tỷ bằng giải tích $$p$$-adic, không cần xây dựng lý thuyết đối đồng điều đó. **Grothendieck**, **Michael Artin** và cộng đồng **SGA** xây dựng **đối đồng điều étale** với hệ số $$\ell$$-adic, chứng minh công thức vết Lefschetz, và thu lại tính hữu tỷ cùng phương trình hàm. Grothendieck hy vọng suy ra tính thuần khiết từ **các giả thuyết chuẩn** của ông về chu trình đại số. Các giả thuyết đó vẫn còn mở (trừ một số phần như định lý Lefschetz mạnh, mà sau này Deligne chứng minh trong đặc số dương như một hệ quả của công trình về giả thuyết Weil). Vì vậy, phần tương tự giả thuyết Riemann cần một lập luận khác.

---

## 2. Ý chính: Frobenius tác động, và các trị riêng của nó là thuần khiết

Khi đã có đối đồng điều étale, ta có (với giả thiết đa tạp trơn và xạ ảnh) phân tích

$$
Z(X,T)=\frac{P_1(T)P_3(T)\cdots P_{2n-1}(T)}{P_0(T)P_2(T)\cdots P_{2n}(T)},
$$

với $$P_i(T)=\det\bigl(1-T\,\mathrm{Frob}\,;\,H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}},\mathbb{Q}_\ell)\bigr)$$, $$P_0(T)=1-T$$ và $$P_{2n}(T)=1-q^n T$$. Công thức vết Lefschetz biến đẳng thức này thành một đồng nhất thức giữa các hàm sinh, không còn là dự đoán.

**Định lý Deligne (Weil I, 1974).** Mọi nghịch đảo nghiệm $$\alpha$$ của $$P_i$$ đều thỏa $$|\alpha|=q^{i/2}$$. Nói cách khác, các trị riêng của Frobenius trên $$H^i$$ là **thuần khiết với trọng số $$i$$**.

**Tóm lại.** Các giả thuyết Weil biến một bài toán đếm thành một bài toán về **phổ**: số điểm là vết, còn phần tương tự giả thuyết Riemann giới hạn vị trí của các trị riêng tạo nên những vết đó. Trường phái Grothendieck cung cấp các vết, Deligne cung cấp giới hạn về trị riêng.

Chứng minh của Deligne không phải là chép lại lập luận của Weil cho đường cong. Nó dùng lập luận với lũy thừa tenxơ và các tương ứng, ước lượng tổng mũ, và một phép quy giúp suy ra tính thuần khiết ở chiều cao từ những tình huống hình học dễ kiểm soát hơn. Nhờ đó chứng minh tránh được các giả thuyết chuẩn. Báo cáo của Katz tại ICM Helsinki (1978) vẫn là tài liệu chuẩn về cấu trúc chứng minh vào thời điểm trao huy chương.

---

## 3. Weil II đã làm được gì và chưa làm được gì

*La conjecture de Weil: II* (1980) tổng quát hóa kết quả từ bó hằng trên đa tạp xạ ảnh trơn sang **các bó $$\ell$$-adic kiến thiết hỗn hợp** (mixed constructible) trên những lược đồ tổng quát hơn trên trường hữu hạn. Nó chặn **trọng số** của các ảnh trực tiếp, và trở thành ngôn ngữ làm việc hằng ngày của lý thuyết bó $$\ell$$-adic: một định lý về đa tạp thường là trường hợp riêng của một định lý về bó.

**Những gì được làm rõ.** Các tổng mũ, đơn đạo và nhiều ước lượng trong lý thuyết số giải tích trở thành các phát biểu về trọng số trong hình học. Công trình trước đó của Deligne (1969, theo gợi ý của Serre) xây dựng biểu diễn $$\ell$$-adic gắn với dạng modular, và việc suy ra **Ramanujan–Petersson** cũng thuộc cùng mạch này: khi biết trọng số, ta có chặn.

**Ramanujan–Petersson, nói cho cẩn thận.** Với hàm tau của Ramanujan, giả thuyết $$|\tau(p)|\le 2p^{11/2}$$ là tương tự giả thuyết Riemann cho một motive trọng số $$11$$ gắn với dạng modular biệt thức. Deligne quy Ramanujan–Petersson cho dạng cusp chỉnh hình trọng số $$\ge 2$$ về các giả thuyết Weil cho những đa tạp có số chiều cao hơn (đa tạp Kuga–Sato, xây dựng từ lũy thừa của đường cong elliptic phổ dụng trên đường cong modular). Vì vậy Weil I kéo theo các chặn đó. Trường hợp trọng số $$1$$ là một câu chuyện khác, được hoàn thành trong công trình của **Deligne–Serre**. Các chặn cổ điển cho tổng Kloosterman có liên quan nhưng dễ hơn vì chỉ ở chiều một: chúng suy ra từ định lý Weil cho đường cong, đã có trước 1974. Đừng nói "Deligne chặn được tổng Kloosterman, nên suy ra Ramanujan"; giả thuyết cho dạng modular cần tính thuần khiết ở chiều cao hơn.

**Những gì chưa được chứng minh.** **Các giả thuyết chuẩn** của Grothendieck vẫn còn mở. **Giả thuyết Hodge** vẫn còn mở. Deligne định nghĩa **chu trình Hodge tuyệt đối** như một khái niệm thay thế dùng được trong một số lập luận, và ông xây dựng lý thuyết **cấu trúc Hodge hỗn hợp** để tổ chức trọng số trong hình học phức. Đó là công cụ, không phải chứng minh giả thuyết Hodge. Lý thuyết motive theo nghĩa mạnh mà Grothendieck mong muốn vẫn là một chương trình nghiên cứu.

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

Deligne sinh năm 1944 tại Bỉ, làm luận án dưới sự hướng dẫn của Grothendieck, và làm việc tại IHÉS trong những năm nhận Huy chương Fields, trước khi chuyển sang Institute for Advanced Study. Huy chương năm 1978 ghi nhận công trình về giả thuyết Weil và sự thống nhất mà nó cho thấy. **Giải Abel 2013**, trao "vì những đóng góp nền tảng cho hình học đại số và ảnh hưởng sâu rộng của chúng đến lý thuyết số, lý thuyết biểu diễn và các lĩnh vực liên quan", là giải cho *cả sự nghiệp*, bao gồm lý thuyết Hodge hỗn hợp, biểu diễn Deligne–Lusztig, không gian moduli của đường cong (cùng Mumford) và nhiều công trình khác. Hãy tách riêng hai giải thưởng này.

---

## 5. Vì sao ông nhận Huy chương Fields, và vì sao câu chuyện này vẫn quan trọng

Các giả thuyết Weil định hướng cả một thế hệ: chúng buộc người ta phải xây dựng một lý thuyết đối đồng điều mới, rồi còn đòi một ước lượng mà lý thuyết đó không tự cho ra. Việc hoàn thành các giả thuyết đã thống nhất hai cách mô tả cùng các số nguyên $$N_m$$ (một từ phép đếm, một từ tôpô trên trường hữu hạn), và đưa các chặn này vào lý thuyết dạng tự đẳng cấu và tổng mũ. Trong khóa học, Deligne là ví dụ về một **chương trình được nhiều người cùng hoàn thành**, với một ước lượng mang tính quyết định.

[Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) cổ điển vẫn còn mở. Điều này không làm giảm giá trị của câu chuyện Weil. Nó nhắc ta rằng "tương tự giả thuyết Riemann" là một giới hạn về trọng số *đã được chứng minh* trong đặc số hữu hạn, không phải chứng minh phát biểu gốc của Riemann. Sinh viên đôi khi nghe nói "Deligne chứng minh giả thuyết Riemann". Thực ra ông chứng minh giả thuyết Riemann *cho hàm zeta của đa tạp trên trường hữu hạn*.

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

## Bài tập

1. Viết $$Z(X,T)$$ và nói bằng lời $$N_m$$ đếm gì. Kiểm tra công thức cho $$\mathbb{P}^1$$: $$N_m=q^m+1$$.
2. Với đường cong elliptic, chặn Hasse $$|N_1-(q+1)|\le 2\sqrt{q}$$ là tương tự giả thuyết Riemann cho $$n=1$$. Vì sao hai số phức có môđun $$\sqrt{q}$$ cho ra bất đẳng thức đó?
3. Ai chứng minh phần nào: tính hữu tỷ, phương trình hàm, tính thuần khiết? Điền bảng ba hàng mà không nhìn lại bài.
4. Vì sao các giả thuyết chuẩn của Grothendieck *trông như* một con đường dẫn đến tính thuần khiết, và vì sao việc Deligne không cần đến chúng lại quan trọng?
5. **Ramanujan, nói cho cẩn thận.** Phát biểu $$|\tau(p)|\le 2p^{11/2}$$ và viết hai câu giải thích vì sao đây là chặn kiểu Weil, chứ không phải một ước lượng sơ cấp chỉ dùng đường cong modular $$X_0(1)$$.
6. **LO6.** Tìm một câu trên báo phổ thông nói "Deligne chứng minh giả thuyết Riemann". Viết lại cho đúng trong khóa học này.
7. Đọc lướt vài trang đầu của Weil I hoặc một bài tổng quan (Katz, ICM 1978) và liệt kê năm thuật ngữ cần học tiếp (ví dụ chùm Lefschetz, chu trình triệt tiêu, trọng số, $$\ell$$-adic, đối ngẫu Poincaré).
8. **Seminar mở rộng.** So sánh "tính thuần khiết của trọng số" ở đây với các lý thuyết đối đồng điều $$p$$-adic sau này của [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/): cả hai đều nói về việc chuyển thông tin giữa các lý thuyết đối đồng điều. Bài toán nào thuộc trường hữu hạn, bài toán nào thuộc đặc số hỗn hợp?

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
