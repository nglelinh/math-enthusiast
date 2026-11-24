---
layout: post
title: "Mirzakhani và Không gian Mô-đun (Huy chương Fields 2014)"
chapter: '02'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy hình dung một chiếc bàn bi-a hình đa giác kỳ lạ, và bạn đánh một viên bi lăn mãi không dừng. Quỹ đạo của viên bi sẽ lặp lại một vòng kín, hay dần dần tô kín toàn bộ mặt bàn? Nghe tưởng như một câu đố giải trí, nhưng bài toán bi-a trong đa giác lại dẫn thẳng vào một trong những vùng đất trừu tượng và đẹp đẽ nhất của toán học hiện đại: hình học của **các mặt cong** và **không gian chứa mọi hình dạng có thể có của chúng** — gọi là *không gian mô-đun*.

Năm 2014, **Maryam Mirzakhani** trở thành **người phụ nữ đầu tiên** trong lịch sử nhận **Huy chương Fields**, nhờ những đóng góp mang tính đột phá cho **động lực học và hình học** của **mặt Riemann** và **không gian mô-đun** của chúng. Thay vì coi không gian mô-đun như một khái niệm trừu tượng chỉ để định nghĩa, công trình của bà đã biến "vũ trụ của mọi hình dạng" thành một đối tượng vừa **tính toán được** (đo được thể tích, đếm được số đường cong khép kín) vừa **nghiên cứu được bằng hệ động lực** (theo dõi các dòng chuyển động và tính hỗn loạn đều khắp), bắc một cây cầu rực rỡ giữa hình học hyperbolic, lý thuyết Teichmüller và hệ động lực.

Hành trình của bài học này đi qua bảy chặng:

**Mặt hyperbolic → không gian Teichmüller và không gian mô-đun → thể tích Weil–Petersson → đếm đường trắc địa → dòng động đất → động lực trên các tầng (strata) → Fields 2014.**

Mục tiêu không phải là dựng lại toàn bộ luận án hay các bài báo trên *Annals*, mà là hiểu **không gian mô-đun là gì**, **các bài toán đếm và bài toán động lực hỏi gì**, và **vì sao chúng khó nhưng vẫn "tính được"**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa một cách không hình thức **mặt Riemann** giống $$g\ge 2$$, **metric hyperbolic**, **không gian Teichmüller** và **không gian mô-đun**.
- Giải thích vì sao không gian mô-đun là "không gian các hình dạng", chứ không phải một mặt được vẽ trong không gian.
- Phát biểu bài toán đếm **đường trắc địa đóng đơn** và tốc độ tăng tiệm cận mà Mirzakhani xác định được (bậc $$6g-6$$).
- Mô tả thể tích **Weil–Petersson** như một độ đo hình học trên không gian các hình dạng.
- Phác thảo ý tưởng **dòng động đất** (earthquake flow) và **tính ergodic** (cùng với Eskin).
- Liên hệ mặt phẳng dịch chuyển và bi-a trong đa giác với cùng một hệ ý tưởng.
- Ghi nhận chính xác rằng Mirzakhani là **người phụ nữ đầu tiên đoạt Huy chương Fields** (2014), và thấy được giải thưởng ghi nhận cả một sự nghiệp nghiên cứu rộng lớn, chứ không chỉ một công thức đơn lẻ.

**Kiến thức cần có.** Mặt giống $$g$$ (mặt cầu, mặt xuyến, …); metric Riemann và độ dài đường trắc địa; ký hiệu tiệm cận $$f(L)\sim c L^k$$. Không cần biết trước lý thuyết Teichmüller.

**Liên hệ trong khóa học.** Các bài liên quan: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/), [vô hạn / hình dạng]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

---

## Bản đồ kiến thức nền: Hình học hyperbolic, Không gian mô-đun và Lý thuyết ergodic

Nếu bạn mới nghe tên những lĩnh vực phía sau công trình của Mirzakhani, hãy tưởng tượng chúng qua ba câu hỏi trực giác:

- **Hình học hyperbolic (Hyperbolic Geometry) nghiên cứu gì?** Trong hình học phẳng Euclid, tổng ba góc của một tam giác bằng $$180^\circ$$ và độ cong bằng $$0$$. Trên mặt cầu, tam giác phồng ra nên tổng ba góc lớn hơn $$180^\circ$$ (độ cong dương). **Hình học hyperbolic** là thế giới ngược lại: mọi điểm đều uốn cong như yên ngựa (độ cong âm hằng $$-1$$), tổng ba góc của tam giác nhỏ hơn $$180^\circ$$, và các đường "thẳng nhất" (**đường trắc địa**) tách xa nhau cực nhanh. Điều bất ngờ là hầu hết mọi bề mặt đóng có từ **hai lỗ trở lên** (bánh vòng 2 lỗ, 3 lỗ, ...) đều mang tự nhiên một hình học hyperbolic!
- **Không gian mô-đun (Moduli Space) là gì?** Hãy nghĩ đến một ví dụ siêu đơn giản: mọi hình chữ nhật có diện tích bằng $$1$$ chỉ khác nhau ở tỉ lệ dài/rộng $$r \ge 1$$. Vậy "không gian mọi hình dạng chữ nhật diện tích 1" chính là tia số $$[1, \infty)$$: mỗi *điểm* trên tia đó là một *hình chữ nhật*! Tương tự, **không gian mô-đun** $$\mathcal{M}_g$$ là không gian mà mỗi *điểm* của nó đại diện cho một *hình dạng hoàn chỉnh* của chiếc bánh vòng $$g$$ lỗ. Khi bạn đi dọc một đường cong trong $$\mathcal{M}_g$$, hình dạng của bề mặt đang biến đổi liên tục.
- **Lý thuyết ergodic & vì sao lại chuyển ngôn ngữ?** Thay vì đứng trên *một* bề mặt cố định để đếm từng đường cong (việc cực kỳ khó vì các đường cong ngoằn ngoèo đan chéo nhau), Mirzakhani bước lùi ra ngoài, nhìn lên **cả không gian mô-đun $$\mathcal{M}_g$$** chứa tất cả các hình dạng cùng lúc, rồi dùng các phép tính thể tích và các dòng chuyển động (như dòng động đất) trên đó. Một bài toán đếm trên *một* mặt nhờ vậy biến thành bài toán tích phân và hệ động lực trên *không gian mọi mặt*.

---

## 1. Mặt Riemann, metric hyperbolic và "hình dạng"

Một **mặt Riemann đóng** là một mặt compact, định hướng được, không có biên, mang cấu trúc phức (về mặt địa phương giống một miền mở trong $$\mathbb{C}$$, các phép chuyển tọa độ là chỉnh hình). Về tô pô: với mỗi $$g\ge 0$$ có đúng một mặt đóng định hướng được có giống (số lỗ) $$g$$: mặt cầu ($$g=0$$), mặt xuyến ($$g=1$$), mặt xuyến kép ($$g=2$$), … Đặc trưng Euler là:

$$
\chi=2-2g.
$$

Với $$g\ge 2$$ thì $$\chi<0$$. Theo **định lý đơn trị hóa** (*uniformization*), mỗi mặt như vậy có một **metric hyperbolic** với độ cong hằng $$-1$$, duy nhất trong lớp bảo giác của nó (sai khác một phép đẳng cự). Đường trắc địa là đường "thẳng nhất"; **đường trắc địa đóng** là đường cong đóng có độ dài cực tiểu địa phương — giống như một sợi dây chun căng ôm chặt quanh một cái eo của bề mặt.

Đường trắc địa đóng **đơn** là đường không tự cắt. Trên mặt hyperbolic, chúng rất "cứng": mỗi lớp đồng luân tự do của một đường cong đơn cốt yếu chứa đúng một đại diện là đường trắc địa; độ dài của nó là một bất biến hình học của mặt được đánh dấu.

Vì sao quan tâm? Phổ độ dài mã hóa hình dạng của mặt. Đếm các đường trắc địa có độ dài bị chặn là "họ hàng" hình học của bài toán đếm số nguyên tố có độ lớn bị chặn: cả hai đều hỏi một bất biến rời rạc phân bố ra sao khi một tham số liên tục tăng dần.

---

## 2. Không gian Teichmüller và không gian mô-đun: không gian các hình dạng

Cần phân biệt cẩn thận hai loại "không gian các mặt".

**Không gian Teichmüller** $$\mathcal{T}_g$$ tham số hóa các cấu trúc hyperbolic (hoặc cấu trúc phức) trên một mặt tô pô cố định có giống $$g$$, sai khác phép đồng luân đẳng vị (isotopy); tương đương với các mặt Riemann *được đánh dấu*. Việc đánh dấu ghi nhớ cách đồng nhất mặt với một mặt tham chiếu, nên trong bức tranh cổ điển $$\mathcal{T}_g$$ là đơn liên; nó là một đa tạp thực có số chiều

$$
\dim_{\mathbb{R}}\mathcal{T}_g=6g-6\qquad(g\ge 2).
$$

Từ đâu ra con số $$6g-6$$? Hãy thử ngay với chiếc bánh vòng **2 lỗ** ($$g = 2$$): bạn có thể cắt nó dọc theo **3 đường tròn rời nhau** để tách thành **2 "chiếc quần"** (*pair of pants* — hình cầu khoét 3 lỗ). Hình dạng hyperbolic của mỗi chiếc quần được xác định duy nhất bởi độ dài 3 đường biên của nó! Vậy 3 đường cắt cho ta 3 tham số *độ dài* $$(\ell_1, \ell_2, \ell_3)$$. Khi dán hai chiếc quần lại dọc theo 3 đường cắt ấy, tại mỗi đường dán ta còn được quyền *xoay lệch* một góc tùy ý — thêm 3 tham số *góc xoắn* $$(\theta_1, \theta_2, \theta_3)$$. Tổng cộng $$3 + 3 = 6 = 6(2) - 6$$ tham số thực! Đây chính là **tọa độ Fenchel–Nielsen**.

**Không gian mô-đun** $$\mathcal{M}_g$$ là không gian các lớp đẳng cấu không đánh dấu: các mặt sai khác một song chỉnh hình (hoặc một phép đẳng cự của metric hyperbolic). Viết hình thức:

$$
\mathcal{M}_g\simeq\mathcal{T}_g/\mathrm{Mod}_g,
$$

trong đó $$\mathrm{Mod}_g$$ là **nhóm lớp ánh xạ** (*mapping class group*), gồm các lớp đẳng vị của các phép đồng phôi bảo toàn định hướng. Mỗi điểm của $$\mathcal{M}_g$$ là một hình dạng thuần túy; mỗi điểm của $$\mathcal{T}_g$$ là một hình dạng kèm theo nhãn cho các đường cong và lịch sử biến dạng.

![Moduli như không gian hình dạng]({{ site.baseurl }}/img/chapter_img/mirzakhani_moduli_shapes.svg)

*Hình (minh họa ý tưởng). Mỗi điểm của không gian mô-đun là một lớp hình dạng của mặt; một đường cong trong không gian mô-đun là một quá trình biến dạng hình dạng.*

**Lưu ý quan trọng.** Các bài viết phổ thông đôi khi nói "không gian mô-đun là một mặt". Không phải vậy. Mỗi mặt chỉ là một điểm; không gian mô-đun là một không gian hình học nhiều chiều hơn gồm tất cả các điểm đó. Nhầm lẫn giữa hai khái niệm này là lỗi phổ biến nhất khi thảo luận.

Trực giác cho giống thấp: với mặt xuyến ($$g=1$$), ta tạo ra nó bằng cách dán các cạnh đối diện của một hình bình hành trên mặt phẳng phức $$\mathbb{C}$$ sinh bởi $$1$$ và $$\tau$$ (với $$\operatorname{Im}\tau > 0$$). Như vậy mọi hình dạng mặt xuyến tương ứng với một điểm $$\tau$$ trong nửa mặt phẳng trên chia cho tác động của $$\mathrm{SL}_2(\mathbb{Z})$$. Với $$g\ge 2$$, metric Weil–Petersson, các phép compact hóa và hệ động lực trở thành các chủ đề trung tâm.

---

## 3. Đếm các đường trắc địa đóng đơn

Cố định một mặt hyperbolic $$X$$ có giống $$g\ge 2$$. Gọi $$N_X(L)$$ là số đường trắc địa đóng đơn có độ dài $$\le L$$. (Nếu cho phép đường cong tự cắt nhau, số đường trắc địa đóng tăng theo hàm mũ $$e^L / L$$ — cực nhanh; điều kiện *đơn*, không tự cắt, khiến số lượng tăng chậm hơn nhiều theo hàm đa thức và mang tính cứng hình học hơn.)

Mirzakhani chứng minh một công thức tiệm cận dạng

$$
N_X(L)\sim c_X\, L^{6g-6}\qquad(L\to\infty),
$$

trong đó số mũ $$6g-6$$ đúng bằng số chiều thực của không gian Teichmüller / mô-đun (ví dụ bậc $$6$$ với mặt 2 lỗ, bậc $$12$$ với mặt 3 lỗ), và hằng số $$c_X$$ được biểu diễn tường minh qua dữ liệu hình học của $$X$$. Các phép đếm chi tiết hơn còn phân biệt được cả tỉ lệ giữa các kiểu tô pô khác nhau của đường cong — chẳng hạn trên mặt 2 lỗ, một đường trắc địa đóng đơn dài ngẫu nhiên có xác suất cắt mặt thành hai mảnh rời nhau thấp hơn rất nhiều so với đường không tách mặt (tỉ lệ chính xác tính được từ thể tích không gian mô-đun!).

Phương pháp không phải là "vẽ mặt rồi liệt kê các đường cong". Bà lấy tích phân của một độ đo hình học trên không gian mô-đun, dùng cấu trúc đệ quy khi cắt mặt dọc theo các đường cong đơn (phân tách thành các "quần", *pants decomposition*), và khai thác mối liên hệ giữa các hàm độ dài với hình học symplectic Weil–Petersson.

**Bài học.** Một bài toán đếm trên *một* mặt được giải bằng cách hiểu độ đo trên *không gian của mọi mặt*. Bước chuyển từ một đối tượng sang không gian mô-đun của nó là phong cách đặc trưng của Mirzakhani.

Tóm tắt:

$$
\text{đếm đường cong trên }X
\;\longleftrightarrow\;
\text{tích phân / thể tích trên moduli}.
$$

---

## 4. Thể tích Weil–Petersson của không gian mô-đun

Dạng symplectic **Weil–Petersson** (WP) cho không gian mô-đun (và không gian Teichmüller) một phần tử thể tích tự nhiên, xuất phát từ hình học hyperbolic và giải tích phức (trong tọa độ Fenchel–Nielsen, nó có dạng cực kỳ gọn đẹp: $$\omega_{\mathrm{WP}} = \sum d\ell_i \wedge d\theta_i$$ theo định lý Wolpert). Gọi $$V_{g,n}(L_1,\ldots,L_n)$$ là thể tích WP của không gian mô-đun các mặt có giống $$g$$ với $$n$$ thành phần biên là đường trắc địa có độ dài cho trước $$L_i$$.

Mirzakhani thiết lập **công thức đệ quy** cho các thể tích này, liên hệ $$V_{g,n}$$ với thể tích của các mặt đơn giản hơn sau khi cắt dọc một đường cong đơn. Công thức đủ tường minh để tính nhiều trường hợp nhỏ — chẳng hạn với mặt xuyến khoét một lỗ ($$g=1, n=1$$) có biên dài $$L$$, thể tích là một đa thức bậc hai cực gọn $$V_{1,1}(L) = \frac{1}{24}(L^2 + 4\pi^2)$$ — và để chứng minh tổng quát rằng mọi thể tích $$V_{g,n}$$ đều là đa thức theo $$L_1^2, \dots, L_n^2$$. Thể tích xuất hiện trong định lý đếm vì việc lấy tích phân "có bao nhiêu đường cong độ dài $$\le L$$" theo độ đo trên không gian mô-đun tương ứng (theo kiểu đối ngẫu) với câu hỏi "tập các mặt có một đường cong ngắn thuộc kiểu cho trước lớn đến mức nào".

Sơ đồ ý tưởng (không phải định lý đầy đủ):

$$
\text{đếm đường cong trên }X\text{ điển hình}
\quad\longleftrightarrow\quad
\text{hình học thể tích WP trên }\mathcal{M}_g.
$$

Liên hệ với vật lý và mặt ngẫu nhiên: thể tích WP xuất hiện trong lý thuyết hấp dẫn lượng tử 2 chiều (giả thuyết Witten–Kontsevich) và các mô hình ma trận; công thức đệ quy của Mirzakhani không chỉ làm rõ phía toán học của sự tương ứng đó mà còn cho một chứng minh hình học mới, ngắn gọn cho giả thuyết Witten. Điều cần nhớ: thể tích không phải chi tiết phụ, mà là **công cụ tích phân** cho các bài toán đếm.

---

## 5. Dòng động đất và tính ergodic

Một **phép động đất** (Thurston) là cách biến dạng mặt hyperbolic bằng việc "trượt" dọc các lá của một lá phân đo được (*measured lamination*). Hãy tưởng tượng cắt mặt dọc theo một họ đường cong (giống như một đường đứt gãy địa chất), trượt hai mép lệch nhau rồi dán lại; đây là dạng tổng quát của phép xoắn Fenchel–Nielsen.

**Dòng động đất** biến phép biến dạng đó thành một hệ động lực trên phân thớ đối tiếp xúc / một không gian đo thích hợp gắn với không gian mô-đun. Cùng với **Alex Eskin** (và trong công trình riêng về dòng động đất), Mirzakhani chứng minh **tính ergodic** của dòng động đất: các quỹ đạo "điển hình" lấp đầy không gian theo nghĩa độ đo, không bị kẹt trong các vùng bất biến không tầm thường.

Nói gọn về tính ergodic: trung bình theo thời gian dọc một quỹ đạo bằng trung bình theo không gian đối với độ đo bất biến (giống như việc theo dõi một phân tử khí bay lâu vô hạn trong bình sẽ ghé qua mọi vùng với tỉ lệ thời gian đúng bằng tỉ lệ thể tích vùng đó). Hệ quả: nhiều đại lượng hình học có hành vi thống kê rõ ràng; không có "hòn đảo bất biến" nào với độ đo dương che giấu những hành vi bất thường.

### Mặt phẳng dịch chuyển, bi-a và các tầng

Song song với đó, hãy quay lại chiếc bàn bi-a đa giác ở đầu bài: mỗi khi viên bi đập vào một cạnh, thay vì cho viên bi bật lại, ta có thể *phản chiếu* cả chiếc bàn qua cạnh đó và để viên bi đi thẳng! Khi dán các bản sao đối xứng của bàn bi-a lại với nhau, ta thu được một **mặt phẳng dịch chuyển** (*translation surface*). Các tầng (*strata*) của các vi phân chỉnh hình mang một tác động tự nhiên của nhóm ma trận $$\mathrm{SL}_2(\mathbb{R})$$ (kéo giãn theo một chiều, nén theo chiều kia). Trong bài báo nổi tiếng mệnh danh là **"định lý cây đũa thần"** (*Magic Wand Theorem*), **Eskin và Mirzakhani** (cùng Mohammadi) đã phân loại hoàn toàn các độ đo bất biến và bao đóng quỹ đạo của tác động này — một cuộc cách mạng của thập niên 2010. Chỉ cần nhớ: **cùng một hệ ý tưởng (hình học của mặt + động lực của tác động nhóm) được áp dụng cho không gian mô-đun hyperbolic và cho các tầng của mặt phẳng dịch chuyển**.

---

## 6. Vì sao công trình này quan trọng

- Làm cho không gian mô-đun **vừa tính toán được vừa nghiên cứu được bằng hệ động lực**, chứ không chỉ tồn tại một cách trừu tượng.  
- Nối hình học thuần túy với hệ động lực ở tầm giải Fields.  
- Tạo ra ngôn ngữ chung cho bài toán đếm đường cong, thể tích và lý thuyết ergodic trên không gian các hình dạng.  
- Truyền cảm hứng cho cả một thế hệ nghiên cứu về mặt, các tầng, và tác động hình học của nhóm.

Trong Chương 2, Mirzakhani là cây cầu **hệ động lực ↔ không gian mô-đun**, tương ứng với Green–Tao (tổ hợp ↔ số nguyên tố) và Ngô (hình học ↔ dạng tự đẳng cấu).

---

## 7. Lưu ý cho chính xác và bối cảnh con người

- Bà là **người phụ nữ đầu tiên** nhận Huy chương Fields (2014). Maryna Viazovska là người thứ hai (2022); xem bài [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/).  
- Nhiều định lý có đồng tác giả; **luôn kiểm tra** đồng tác giả cho từng phát biểu cụ thể (Eskin là cái tên thường xuyên xuất hiện trong các kết quả về động lực).  
- Mirzakhani mất năm 2017; ảnh hưởng của bà vẫn tiếp tục qua các học trò và các bài toán bà đã định hình.  
- Lời trích dẫn giải Fields nhấn mạnh **dynamics and geometry of Riemann surfaces and their moduli spaces** (động lực học và hình học của mặt Riemann và các không gian mô-đun của chúng); đừng thu hẹp thành "chỉ đếm đường trắc địa".

---

## 8. Điều nghịch lý

Với người học, không gian mô-đun có vẻ "vô cùng phức tạp" (không gian của các metric / cấu trúc phức), vậy mà:

- thể tích của nó có công thức đệ quy;  
- số đường cong ngắn có tiệm cận dạng đa thức;  
- một dòng tự nhiên trên nó có thể ergodic.

Nghịch lý biến mất khi ta nhớ rằng đối xứng của nhóm lớp ánh xạ, cùng cấu trúc symplectic / hyperbolic trên không gian Teichmüller–mô-đun, cung cấp các hệ tọa độ và độ đo đủ cứng để giải tích và hệ động lực có chỗ bám.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Không gian mô-đun chính là bản thân mặt." | **Sai** | Đó là không gian của các mặt (các hình dạng). |
| "Bà chỉ đếm đường trắc địa." | **Sai** | Hệ động lực, thể tích và mối liên hệ với các tầng cũng là trung tâm. |
| "Không gian Teichmüller chính là không gian mô-đun." | **Sai** | Không gian Teichmüller có đánh dấu; không gian mô-đun là thương của nó (nói gần đúng). |
| "Tính ergodic nghĩa là mọi quỹ đạo đều tuần hoàn." | **Sai** | Đó là một phát biểu về độ đo, liên quan đến trung bình theo thời gian và theo không gian. |
| "Mọi kết quả đều do một mình bà làm." | **Sai** | Nhiều định lý là công trình hợp tác; hãy kiểm tra tác giả. |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Mirzakhani_Moduli/`.

**Thứ tự xem gợi ý**

1. Video về Mirzakhani của Quanta/Simons: [YouTube](https://www.youtube.com/watch?v=qNuh4uta8oQ).  
2. Bài viết của Quanta: [link](https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/).  
3. Trang bài giảng Morse tại IAS: [link](https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i).  
4. Bài "cây đũa thần" (magic wand): [arXiv:1302.3320](https://arxiv.org/abs/1302.3320).

**Nhắc lại:** phần toán về không gian mô-đun và hệ động lực là lý do bài này có trong chương trình; tiểu sử của bà quan trọng về mặt văn hóa.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Mirzakhani_Moduli/transcripts/` · trạng thái: `research/video-research/Mirzakhani_Moduli/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Mirzakhani_Moduli_qNuh4uta8oQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Mirzakhani_Moduli/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=qNuh4uta8oQ  
2. https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i  
3. https://arxiv.org/abs/1302.3320  
4. https://arxiv.org/abs/1305.3015  
5. https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/  
6. https://en.wikipedia.org/wiki/Maryam_Mirzakhani  
7. https://celebratio.org/Mirzakhani_M/article/1087/  
8. https://terrytao.wordpress.com/tag/maryam-mirzakhani/  
9. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014  
10. https://arxiv.org/search/?query=Mirzakhani+Weil-Petersson&searchtype=all  
11. https://news.stanford.edu/stories/2014/08/surfaces-mirzakhani-081214  

### Bộ tư liệu nghiên cứu

12. Bộ tư liệu của khóa học: `research/video-research/Mirzakhani_Moduli/`.

1. IMU, Huy chương Fields 2014 — Maryam Mirzakhani (lời trích dẫn và bài ca ngợi).  
2. Luận án và các bài báo về thể tích Weil–Petersson / đếm đường trắc địa.  
3. Eskin–Mirzakhani — dòng động đất và các hệ động lực liên quan.  
4. Các bài tổng quan về động lực Teichmüller / không gian mô-đun của đường cong (nhiều tác giả).  
5. Nhập môn: hình học hyperbolic của mặt; tọa độ Fenchel–Nielsen; nhóm lớp ánh xạ (mức sơ lược).

---

## Hướng đi tiếp

- Tìm hiểu mặt phẳng dịch chuyển và bi-a trong đa giác như một chủ đề anh em.  
- So sánh với các câu chuyện khác trong khóa học về "hệ động lực gặp hình học".  
- Đọc một bản trình bày về thể tích Weil–Petersson trước khi đọc bài báo gốc.  
- Ghi lại một câu hỏi cụ thể, ví dụ "độ đo nào khiến dòng động đất là ergodic?"  
- Đọc song song bài [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/) để so sánh hai truyền thống nghiên cứu hệ động lực.

## Video tham khảo

- **Xem trước:** [Maryam Mirzakhani: A Tenacious Explorer of Abstract Surfaces](https://www.youtube.com/watch?v=qNuh4uta8oQ) — Quanta Magazine, tiếng Anh. Chân dung Mirzakhani và các mặt trừu tượng bà nghiên cứu; nên xem trước khi đọc bài.
- [Dynamics on the Moduli Spaces of Curves, I - Maryam Mirzakhani](https://www.youtube.com/watch?v=8Az_W2wv4Zo) — Institute for Advanced Study, tiếng Anh. Bài giảng của chính Mirzakhani về động lực trên không gian mô-đun của đường cong; nên xem sau khi đã nắm ý chính của bài.
- [Maryam Mirzakhani, Dynamics Moduli Spaces of Curves I](https://www.youtube.com/watch?v=tprlQMClSYQ) — Harvard Mathematics Department, tiếng Anh. Xem thêm sau hai video trên; một bài giảng khác của bà về cùng chủ đề.
