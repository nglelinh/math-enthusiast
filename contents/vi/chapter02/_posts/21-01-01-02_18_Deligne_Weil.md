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

**Pierre Deligne** nhận **Huy chương Fields 1978** vì, theo lời IMU chuẩn của đại hội đó, đưa ra **lời giải các giả thuyết Weil** về các tổng quát hóa giả thuyết Riemann cho đa tạp trên trường hữu hạn, công trình “đã làm nhiều để thống nhất hình học đại số và lý thuyết số đại số.” Huy chương không phải tuyên bố một người xây đối đồng điều étale, cũng không phải **các giả thuyết chuẩn** về chu trình đại số, hay **giả thuyết Hodge**, đã được giải. **André Weil** đặt câu hỏi (1949). **Bernard Dwork** chứng minh tính hữu tỷ bằng phương pháp $$p$$-adic (1960). **Trường phái Grothendieck** xây đối đồng điều étale và thu được phương trình hàm. Deligne chứng minh phát biểu tinh khiết còn lại—tương tự giả thuyết Riemann—trong *La conjecture de Weil: I* (1974), rồi một nâng cấp lý thuyết bó sâu hơn trong *Weil II* (1980).

Bài này dành cho người đã gặp hàm zeta Riemann thông thường và một đa tạp xạ ảnh, và muốn thấy một bài toán đếm trên $$\mathbb{F}_q$$ trở thành định lý về trị riêng của Frobenius. Một vinh dự sau, **Giải Abel 2013**, ghi nhận ảnh hưởng cả đời; nó khác Fields 1978 và không nên gộp vào đó.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu các giả thuyết Weil mức khẩu hiệu: hàm zeta của một đa tạp xạ ảnh trơn trên trường hữu hạn là **hữu tỷ**, thỏa **phương trình hàm**, và có zero/cực trên những đường thẳng đứng quy định (**tương tự RH**).
- Gán công: **Dwork** (tính hữu tỷ), **đối đồng điều étale Grothendieck–Artin** (biểu thức đối đồng điều và phương trình hàm), **Deligne** (tính tinh khiết / tương tự RH, Weil I và Weil II).
- Viết hàm sinh zeta theo $$T=q^{-s}$$ và hiểu $$N_m$$ là số điểm trên $$\mathbb{F}_{q^m}$$.
- Giải thích vì sao đối đồng điều étale là *máy* và ước lượng của Deligne trên trị riêng Frobenius là *chặn còn thiếu*.
- Phát biểu, cẩn thận, rằng các chặn Ramanujan–Petersson cho dạng modular chỉnh hình trọng số ít nhất $$2$$ suy từ các giả thuyết Weil áp vào những đa tạp thích hợp (xây dựng Kuga–Sato / modular)—không phải từ một lập luận một dòng trên một đường cong modular đơn lẻ.
- Từ chối hai tuyên bố quá đà: Deligne **không** chứng minh các giả thuyết chuẩn; ông **không** chứng minh giả thuyết Hodge.

**Kiến thức nền.** Trường hữu hạn $$\mathbb{F}_q$$; ý tưởng đa tạp xạ ảnh và đếm điểm hữu tỷ; tích Euler và giả thuyết Riemann cổ điển như *mô hình* cho một phát biểu về zero. Scheme và phạm trù dẫn xuất không bắt buộc—nghĩ “một lý thuyết đối đồng điều hình học có công thức vết Lefschetz.”

**Liên kết seminar.** RH cổ điển, vẫn mở: [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Láng giềng hình học số: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) (hàm $$L$$ của đường cong trên $$\mathbb{Q}$$), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Scholze / đối đồng điều $$p$$-adic]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/). Song song giải trọn đời: [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

---

## 1. Lịch sử đếm điểm và đoán một hàm zeta

Gauss đã đếm điểm trên một số đường cong elliptic trên trường hữu hạn khi nghiên cứu chu kỳ và cyclotomy. **Hasse** chứng minh tương tự RH cho đường cong elliptic: nếu $$E/\mathbb{F}_q$$ có $$N_1$$ điểm thì $$|N_1-(q+1)|\le 2\sqrt{q}$$. **Weil** chứng minh các giả thuyết cho đường cong mọi giống và cho đa tạp Abel, rồi năm 1949 đề xuất mẫu cho đa tạp xạ ảnh trơn mọi chiều. Hàm sinh

$$
Z(X,T)=\exp\Bigl(\sum_{m\ge 1}N_m\frac{T^m}{m}\Bigr),\qquad T=q^{-s},
$$

phải là hàm **hữu tỷ** theo $$T$$; phải thỏa **phương trình hàm** liên hệ $$Z(X,T)$$ với $$Z(X,1/q^n T)$$ (ở đây $$n=\dim X$$); và các căn nghịch đảo của nhân tử bậc $$i$$ phải có modulus $$q^{i/2}$$—**tương tự giả thuyết Riemann**, hay **tính tinh khiết**. Một mệnh đề thứ tư đồng nhất các bậc đó với số Betti của một nâng phức, khi nâng đó tồn tại.

Ẩn dụ với tôpô vừa là tai tiếng vừa là lời mời. Trên $$\mathbb{C}$$, công thức vết Lefschetz đếm điểm cố định của một ánh xạ từ các vết trên đối đồng điều. Trên $$\mathbb{F}_q$$, Frobenius là một ánh xạ, và $$N_m$$ là phép đếm điểm cố định của nó trên $$X(\overline{\mathbb{F}}_q)$$. Nếu tồn tại một lý thuyết đối đồng điều có công thức vết *và* đối ngẫu Poincaré sinh ra phương trình hàm, thì tương tự RH sẽ trở thành một chặn trên trị riêng.

**Dwork (1960)** chứng minh tính hữu tỷ bằng giải tích $$p$$-adic, không xây đối đồng điều đó. **Grothendieck**, **Michael Artin**, và cộng đồng **SGA** xây **đối đồng điều étale** hệ số $$\ell$$-adic, chứng minh công thức vết Lefschetz, và thu được tính hữu tỷ lần nữa cùng phương trình hàm. Grothendieck hy vọng suy tính tinh khiết từ **các giả thuyết chuẩn** của ông về chu trình đại số. Các giả thuyết đó vẫn mở (trừ những mảnh như hard Lefschetz, mà Deligne sau này thiết lập bằng cách mở rộng công trình Weil). Tương tự RH vì thế đòi một lập luận khác.

---

## 2. Khẩu hiệu: Frobenius tác động, và trị riêng của nó tinh khiết

Một khi đối đồng điều étale được chấp nhận, ta có (dưới các giả thuyết trơn và xạ ảnh đang đứng) một phân tích

$$
Z(X,T)=\frac{P_1(T)P_3(T)\cdots P_{2n-1}(T)}{P_0(T)P_2(T)\cdots P_{2n}(T)},
$$

với $$P_i(T)=\det\bigl(1-T\,\mathrm{Frob}\,;\,H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}},\mathbb{Q}_\ell)\bigr)$$ và $$P_0(T)=1-T$$, $$P_{2n}(T)=1-q^n T$$. Công thức vết Lefschetz biến đây thành đồng nhất thức của hàm sinh, không phải một phỏng đoán.

**Định lý Deligne (Weil I, 1974).** Mỗi căn nghịch đảo $$\alpha$$ của $$P_i$$ thỏa $$|\alpha|=q^{i/2}$$. Tương đương, các trị riêng của Frobenius trên $$H^i$$ **tinh khiết trọng số $$i$$**.

**Khẩu hiệu.** Các giả thuyết Weil sắp xếp lại một bài toán đếm thành bài toán **phổ**: số điểm là vết; tương tự RH là hạn chế nơi các trị riêng thành phần của những vết đó được phép nằm. Deligne cung cấp hạn chế. Trường phái Grothendieck cung cấp các vết.

Chứng minh không phải chép lại lập luận của Weil cho đường cong. Nó dùng lập luận lũy thừa thớ / correspondence, ước lượng tổng mũ, và một rút gọn cho phép suy tính tinh khiết chiều cao từ những tình huống hình học dễ kiểm soát hơn—né các giả thuyết chuẩn. Báo cáo ICM Helsinki của Katz (1980) vẫn là hướng dẫn chuẩn về kiến trúc vào thời điểm trao huy chương.

---

## 3. Weil II sắp xếp lại điều gì, và điều gì thì không

*La conjecture de Weil: II* (1980) là tổng quát hóa từ bó hằng trên đa tạp xạ ảnh trơn sang **các bó $$\ell$$-adic constructible hỗn hợp** trên những lược đồ tổng quát hơn trên trường hữu hạn. Nó chặn **trọng số** của ảnh trực tiếp, và trở thành ngôn ngữ hàng ngày của lý thuyết bó $$\ell$$-adic: một định lý về đa tạp thường là trường hợp riêng của một định lý về một bó.

**Điều được sắp xếp lại.** Tổng mũ, monodromy, và nhiều ước lượng trong lý thuyết số giải tích trở thành phát biểu trọng số hình học. Công trình sớm hơn của Deligne với **Serre** về biểu diễn $$\ell$$-adic của dạng modular, và suy ra **Ramanujan–Petersson**, nằm trong cùng vòng: một khi biết trọng số, ta biết chặn.

**Ramanujan–Petersson, nói cẩn thận.** Với hàm tau Ramanujan, giả thuyết $$|\tau(p)|\le 2p^{11/2}$$ là tương tự RH cho một motive trọng số $$11$$ gắn với dạng modular discriminant. Deligne rút Ramanujan–Petersson cho các dạng cusp chỉnh hình trọng số $$\ge 2$$ về các giả thuyết Weil cho những đa tạp chiều cao hơn (đa tạp Kuga–Sato, xây từ lũy thừa của đường cong elliptic phổ dụng trên các đường cong modular). Weil I vì thế kéo theo các chặn đó. Trọng số $$1$$ là câu chuyện khác, hoàn tất trong công trình **Deligne–Serre**. Các chặn tổng Kloosterman cổ điển liên quan nhưng dễ hơn ở chiều một: chúng suy từ định lý Weil cho đường cong, đã có trước 1974. Đừng nói “Deligne chặn tổng Kloosterman, vậy nên Ramanujan”; giả thuyết dạng modular cần tính tinh khiết chiều cao hơn.

**Điều không được chứng minh.** **Các giả thuyết chuẩn** (Grothendieck) vẫn mở như một gói. **Giả thuyết Hodge** vẫn mở. Deligne định nghĩa **chu trình Hodge tuyệt đối** như một vật thay thế dùng được trong một số lập luận, và ông tạo **cấu trúc Hodge hỗn hợp**, tổ chức trọng số trong hình học phức; đó là công cụ, không phải chứng minh Hodge. Motive, theo nghĩa mạnh Grothendieck muốn, vẫn là một chương trình.

---

## 4. Gán công lao trung thực

| Người đóng góp | Vai trò |
|----------------|---------|
| Weil (1949; đường cong sớm hơn) | Các giả thuyết; chứng minh cho đường cong và đa tạp Abel |
| Hasse | Đường cong elliptic trên trường hữu hạn |
| Dwork (1960) | Tính hữu tỷ, $$p$$-adic |
| Grothendieck, M. Artin, SGA | Đối đồng điều étale; công thức vết; phương trình hàm |
| Serre | Đầu vào đối đồng điều và modular sớm; sau này Deligne–Serre |
| Deligne, Weil I (1974) | Tương tự RH / tính tinh khiết trị riêng Frobenius |
| Deligne, Weil II (1980) | Trọng số cho bó; dạng làm việc của lý thuyết |
| Cộng đồng sau | Bó perverse (BBD, với Beilinson–Bernstein–Gabber), các ứng dụng |

Deligne sinh năm 1944 tại Bỉ, viết luận án dưới Grothendieck, và trải những năm Fields tại IHÉS trước khi chuyển sang Institute for Advanced Study. Huy chương 1978 ghi nhận công trình Weil và sự thống nhất nó làm lộ rõ. **Giải Abel 2013**—“vì những đóng góp nền cho hình học đại số và ảnh hưởng biến đổi của chúng lên lý thuyết số, lý thuyết biểu diễn, và các lĩnh vực liên quan”—là giải *trọn đời* bao phủ lý thuyết Hodge hỗn hợp, biểu diễn Deligne–Lusztig, moduli đường cong với Mumford, và nhiều điều khác. Giữ hai vinh dự trên hai dòng riêng.

---

## 5. Vì sao Huy chương Fields, và vì sao câu chuyện vẫn quan trọng

Các giả thuyết Weil là bài toán định hình một thế hệ: chúng buộc phải phát minh một lý thuyết đối đồng điều rồi đòi một ước lượng mà lý thuyết không cho không. Hoàn tất chúng thống nhất hai mô tả cùng các số nguyên $$N_m$$—một từ đếm, một từ tôpô trên trường hữu hạn—và xuất khẩu các chặn vào dạng tự đẳng cấu và tổng mũ. Trong khóa học này, Deligne là chân dung một **chương trình hoàn tất bởi nhiều tay**, với một ước lượng quyết định.

[Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) cổ điển vẫn mở. Đó không phải sự ngượng của câu chuyện Weil; đó là lời nhắc rằng “tương tự RH” nghĩa là một hạn chế trọng số *đã chứng minh* ở đặc số hữu hạn, không phải chứng minh phát biểu gốc của Riemann. Sinh viên đôi khi nghe “Deligne chứng minh RH.” Ông chứng minh RH *cho hàm zeta của đa tạp trên trường hữu hạn*.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Deligne phát minh đối đồng điều étale.” | Grothendieck, Artin, và SGA xây máy. |
| “Dwork chứng minh các giả thuyết Weil.” | Dwork chứng minh **tính hữu tỷ**. Tính tinh khiết là Deligne. |
| “Deligne chứng minh các giả thuyết chuẩn / giả thuyết Hodge.” | Cả hai vẫn mở (như phát biểu tổng quát). |
| “Deligne chứng minh giả thuyết Riemann cổ điển.” | Ông chứng minh **tương tự** cho đa tạp trên $$\mathbb{F}_q$$. |
| “Ramanujan suy từ Weil cho một đường cong modular đơn.” | Trọng số $$\ge 2$$ dùng hình học chiều cao hơn (Kuga–Sato); trọng số 1 là Deligne–Serre. |
| “Abel 2013 cùng vinh dự với Fields 1978.” | Abel là giải trọn đời sau này; Fields trích công trình Weil năm 1978. |

---

## Bài tập

1. Viết $$Z(X,T)$$ và nói bằng lời $$N_m$$ đếm gì. Kiểm tra công thức cho $$\mathbb{P}^1$$: $$N_m=q^m+1$$.
2. Trong trường hợp đường cong elliptic, chặn Hasse $$|N_1-(q+1)|\le 2\sqrt{q}$$ là tương tự RH cho $$n=1$$. Vì sao hai số phức modulus $$\sqrt{q}$$ sinh ra bất đẳng thức đó?
3. Ai chứng minh mảnh nào: tính hữu tỷ, phương trình hàm, tính tinh khiết? Điền bảng ba hàng không nhìn lại.
4. Vì sao các giả thuyết chuẩn của Grothendieck *trông như* một đường tới tính tinh khiết, và vì sao việc Deligne tránh cần chúng lại quan trọng?
5. **Ramanujan, cẩn thận.** Phát biểu $$|\tau(p)|\le 2p^{11/2}$$ và viết hai câu về vì sao đây là chặn kiểu Weil chứ không phải ước lượng sơ cấp trên một mình đường cong modular $$X_0(1)$$.
6. **LO6.** Tìm một câu phổ thông nói “Deligne chứng minh giả thuyết Riemann.” Viết lại cho khóa học này.
7. Lướt vài trang đầu Weil I hoặc một survey (Katz, ICM 1978) và liệt kê năm từ cần học tiếp (ví dụ Lefschetz pencil, vanishing cycle, trọng số, $$\ell$$-adic, đối ngẫu Poincaré).
8. **Seminar mở rộng.** So “tính tinh khiết của trọng số” ở đây với các ngôn ngữ đối đồng điều $$p$$-adic sau này của [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/): cả hai đều nói về chuyển thông tin giữa các lý thuyết đối đồng điều. Bài toán nào là trường hữu hạn, bài toán nào là mixed-characteristic?

---

## Nguồn video và đọc thêm

Bài này không kèm gói nghiên cứu video của khóa học.

1. IMU Fields Medals 1978 (citation Deligne): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1978).
2. Bách khoa: [Pierre Deligne](https://en.wikipedia.org/wiki/Pierre_Deligne); [Weil conjectures](https://en.wikipedia.org/wiki/Weil_conjectures).
3. Giải Abel 2013 (vinh dự trọn đời, khác Fields): [abelprize.no/abel-prize-laureates/2013](https://abelprize.no/abel-prize-laureates/2013).
4. Thông cáo IAS (Abel 2013): [Pierre Deligne Awarded 2013 Abel Prize](https://www.ias.edu/press-releases/pierre-deligne-awarded-2013-abel-prize).
5. Tìm arXiv: [Deligne Weil](https://arxiv.org/search/?query=Deligne+Weil&searchtype=all).
6. Khóa học: [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/); [Tổng quan Abel]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

**Nhắc:** Tương tự RH Weil trên trường hữu hạn—**không** phải RH cổ điển, **không** phải Hodge, **không** phải các giả thuyết chuẩn.

---

## Tài liệu tham khảo

1. International Mathematical Union, Fields Medals 1978 — Pierre Deligne (lời văn tái bản từ lịch sử đại hội Albers–Alexanderson–Reid 1986 trên trang IMU).
2. **A. Weil**, *Numbers of solutions of equations in finite fields*, *Bull. Amer. Math. Soc.* (1949).
3. **B. Dwork**, *On the rationality of the zeta function of an algebraic variety*, *Amer. J. Math.* (1960).
4. **P. Deligne**, *La conjecture de Weil: I*, *Publ. Math. IHÉS* 43 (1974); *La conjecture de Weil: II*, *Publ. Math. IHÉS* 52 (1980).
5. **N. Katz**, *The work of Pierre Deligne*, kỷ yếu ICM Helsinki 1978 (survey thời điểm trao huy chương).
6. Nền SGA và đối đồng điều étale: Grothendieck–Artin; một giáo trình hiện đại (ví dụ notes của Milne) như con trỏ, không bắt buộc đọc.
7. Citation Giải Abel 2013 — Pierre Deligne (abelprize.no).
8. Khóa học: [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/).

---

## Hướng đi tiếp

- Tính $$Z(\mathbb{P}^n,T)$$ bằng tay; đó là các giả thuyết Weil không cần đối đồng điều, và nó chỉnh ký hiệu.
- Đọc một bài một buổi về công thức vết Lefschetz trong đối đồng điều étale trước khi thử Weil I.
- Tùy chọn seminar A3: bản một trang “mở sau Deligne”—các giả thuyết chuẩn, Hodge, motive, RH cổ điển—tách rõ Fields 1978 khỏi Abel 2013.
- Nếu dạng modular là móc của bạn, theo Ramanujan–Petersson vào các bài của Deligne rồi vào Deligne–Serre cho trọng số một; giữ phân biệt chiều trên trang.
