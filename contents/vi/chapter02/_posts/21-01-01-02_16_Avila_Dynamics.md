---
layout: post
title: "Tái chuẩn hóa của Avila trong các hệ động lực (Huy chương Fields 2014)"
chapter: '02'
order: 16
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Artur Avila** nhận **Huy chương Fields 2014**. Theo lời IMU, giải thưởng dành cho "những đóng góp sâu sắc cho lý thuyết hệ động lực, đã làm thay đổi diện mạo của lĩnh vực, lấy ý tưởng mạnh mẽ của **tái chuẩn hóa** (renormalization) làm nguyên lý thống nhất." Lời trích dẫn nêu một *phương pháp*, chứ không nêu một giả thuyết riêng lẻ đã được giải. Avila không phát minh ra tái chuẩn hóa. Trước ông đã có công trình của Wilson trong vật lý, dãy nhân đôi chu kỳ của Feigenbaum, động lực chỉnh hình của Sullivan, và trường phái động lực một chiều ở Brazil và Pháp. Huy chương ghi nhận một loạt định lý trong đó việc nhìn hệ ở một thang mới, rồi lại một thang mới nữa, trở thành ngôn ngữ chung cho ánh xạ một chiều, toán tử Schrödinger tựa tuần hoàn và động lực Teichmüller.

Bài này dành cho người đã biết về phép lặp của một ánh xạ $$f:[0,1]\to[0,1]$$, hoặc về hệ tuyến tính có hệ số thay đổi, và muốn nắm **cấu trúc chung** của các công trình của Avila. Bài **không** nói rằng ông đã phân loại mọi hệ động lực, và cũng không coi định lý về phổ Ten Martini là của riêng ông. Những ý cần nắm đúng: ánh xạ đơn mốt (unimodal) chính quy và ngẫu nhiên; cocycle và tính gần khả quy; phổ Cantor của toán tử almost Mathieu; tính trộn yếu của ánh xạ trao đổi khoảng; và ghi nhận đúng công của các cộng sự như Jitomirskaya, Forni, Viana, de Melo, Lyubich.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lời trích dẫn của IMU năm 2014 trong một câu cẩn thận, trong đó **tái chuẩn hóa** là công cụ thống nhất chứ không phải phát minh của riêng ông.
- Giải thích ở mức ý tưởng **tái chuẩn hóa** một hệ động lực nghĩa là gì: chuyển sang ánh xạ quay về lần đầu (first-return map) hoặc ánh xạ đã đổi tỷ lệ, rồi coi đối tượng mới như một phần tử thuộc cùng lớp.
- Mô tả **toán tử almost Mathieu** và **bài toán Ten Martini** (phổ có phải là tập Cantor không), và ghi nhận lời giải là công trình **chung** của **Avila–Jitomirskaya**.
- Phân biệt cocycle Schrödinger tựa tuần hoàn một tần số với khẳng định sai "mọi phổ lượng tử đều là tập Cantor".
- Phác thảo ánh xạ trao đổi khoảng, động lực Teichmüller và vai trò của **số mũ Lyapunov**, kèm tên các cộng sự (Forni, Viana và những người khác).
- Luyện **LO6**: câu "Avila phân loại được hỗn loạn" là nói quá; các định lý của ông sắp xếp lại một số lớp hệ cụ thể và khó.

**Kiến thức cần có.** Phép lặp của ánh xạ trên đường thẳng thực; quỹ đạo và sự phụ thuộc nhạy vào điều kiện ban đầu; ma trận và trị riêng, đủ để hiểu "số mũ Lyapunov" là tốc độ tăng theo hàm mũ; tập Cantor là tập hoàn hảo, không đâu trù mật trên đường thẳng. Không cần biết trước về lý thuyết Teichmüller hay lý thuyết phổ của toán tử ergodic.

**Liên hệ với khóa học.** Bài gần nhất về động lực: [Mirzakhani, không gian moduli và Teichmüller]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (cùng được trao giải năm 2014; bà nghiên cứu mặt, không nghiên cứu phổ). Động lực trong số học theo một hướng khác: [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/). Về "ngôn ngữ thống nhất" ở chỗ khác trong chương, có thể so với [Scholze và phép tilting]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), nhưng đó là hạ tầng cho một lĩnh vực khác, không cùng bộ công cụ.

---

## 1. Lịch sử của ý tưởng nhìn lại hệ ở thang nhỏ hơn

Lý thuyết hệ động lực hỏi điều gì xảy ra khi ta lặp đi lặp lại một quy tắc. Họ ánh xạ logistic $$x\mapsto rx(1-x)$$ gây bất ngờ lớn vào thập niên 1970: chỉ là một đa thức bậc hai, nhưng khi tham số $$r$$ thay đổi, hệ có thể đi từ chu kỳ hút qua dãy nhân đôi chu kỳ để vào hỗn loạn. **Mitchell Feigenbaum** tìm ra các hằng số tỷ lệ phổ quát trong dãy nhân đôi đó. Trong vật lý, **Kenneth Wilson** đã dùng tái chuẩn hóa như một cách chuyển thang trong cơ học thống kê. Trong động lực một chiều, **Dennis Sullivan** và những người khác viết lại bài toán sao cho ánh xạ quay về lần đầu, sau khi đổi tỷ lệ bằng một phép afin, lại trông như một ánh xạ cùng lớp. Như vậy tái chuẩn hóa là một toán tử trên không gian các ánh xạ, chứ không phải trên một quỹ đạo.

Sang thập niên 1990, trường phái Brazil quanh IMPA (de Melo, Palis, ảnh hưởng của Yoccoz trong động lực một chiều, công trình của Lyubich về họ ánh xạ bậc hai) đặt ra một mục tiêu cụ thể: với ánh xạ đơn mốt điển hình, hành vi dài hạn phải hoặc là **chính quy** (một chu kỳ hút quyết định tương lai), hoặc là **ngẫu nhiên** (có độ đo bất biến liên tục tuyệt đối, tức là hỗn loạn mô tả được bằng xác suất). Nhiều trường hợp đặc biệt đã được biết. Bài báo năm 2003 của **Avila, Welington de Melo và Mikhail Lyubich** giải quyết vấn đề cho các họ ánh xạ đơn mốt giải tích thực: một ánh xạ chọn ngẫu nhiên trong họ như vậy là chính quy hoặc ngẫu nhiên. Tái chuẩn hóa là công cụ so sánh ánh xạ quay về ở thang nhỏ với họ ban đầu, và nhờ đó biến câu "điển hình" thành định lý.

**Ý chính.** Tái chuẩn hóa không phải là một phương trình chuyển động mới. Đó là *phép đổi tọa độ trên không gian các hệ*: phóng to, đổi tỷ lệ, rồi hỏi hệ mới có đơn giản hơn không, có liên hợp với một mô hình đã biết không, hay có thể tái chuẩn hóa thêm lần nữa không.

Các công trình sau này của Avila cho thấy ý tưởng đó **dùng được ở nhiều nơi**. Cùng một cách làm (so sánh một cocycle trên phép quay với cocycle đã tái chuẩn hóa, hoặc so sánh ánh xạ quay về của một phép trao đổi khoảng với một phép trao đổi đơn giản hơn) xuất hiện lại trong lý thuyết phổ và trong động lực Teichmüller. Chính khả năng áp dụng rộng này là điều IMU gọi là nguyên lý thống nhất.

---

## 2. Các định lý tái chuẩn hóa sắp xếp lại điều gì

Một định lý khó điển hình trong lĩnh vực này không liệt kê mọi quỹ đạo. Nó **sắp xếp lại không gian tham số**. Trước định lý, ta có một tập hỗn tạp các trường hợp: tần số Diophantine và tần số Liouville; hành vi hyperbolic và parabolic; ánh xạ tái chuẩn hóa được vô hạn lần và ánh xạ không tái chuẩn hóa được. Sau định lý, những vùng lớn của tập đó được chứng minh là tương đương nhau, hoặc được đưa về một mô hình mà ta đã hiểu số mũ Lyapunov, phổ hay tính trộn.

Có ba kết quả có thể trình bày an toàn ở mức seminar.

**Ánh xạ đơn mốt (cùng de Melo và Lyubich).** Phân chia chính quy/ngẫu nhiên cho ánh xạ đơn mốt giải tích điển hình biến nhiều thập niên nghiên cứu từng trường hợp thành một bức tranh toàn cục: hỗn loạn không phải là ngoại lệ hiếm hoi, mà là một trong hai trạng thái điển hình, và tái chuẩn hóa mô tả ranh giới giữa hai trạng thái đó.

**Toán tử Schrödinger một tần số và cocycle.** Một thế tựa tuần hoàn, đơn giản nhất là hàm cosin lấy mẫu dọc theo một phép quay vô tỷ, sinh ra một toán tử Schrödinger rời rạc trên $$\ell^2(\mathbb{Z})$$. **Cocycle Schrödinger** tương ứng là ánh xạ cập nhật nghiệm bằng các ma trận $$2\times 2$$ phụ thuộc vào pha. **Lý thuyết toàn cục về cocycle một tần số** của Avila (phát triển trong những năm 2000, công bố trong thập niên sau đó) dùng tái chuẩn hóa và phép phức hóa năng lượng để chia trục năng lượng thành các chế độ. Ở một số chế độ, cocycle gần như hằng sau một phép đổi tọa độ (**tính gần khả quy**, almost reducibility). Ở các chế độ khác, số mũ Lyapunov dương và độ đo phổ kỳ dị hơn. Họ almost Mathieu là ví dụ tiêu biểu, nhưng không phải ví dụ duy nhất.

**Ánh xạ trao đổi khoảng và dòng Teichmüller (cùng cộng sự).** Cắt một khoảng thành các khoảng con rồi hoán vị chúng, ta được **ánh xạ trao đổi khoảng** (interval exchange transformation, IET). Đây là phiên bản một chiều của dòng tịnh tiến trên mặt phẳng. **Avila–Forni** chứng minh hầu hết mọi IET (không phải phép quay) đều trộn yếu. **Avila–Viana** chứng minh giả thuyết Zorich–Kontsevich rằng các số mũ Lyapunov không tầm thường của dòng trắc địa Teichmüller trên không gian moduli các vi phân Abel đều đơn (khác nhau từng đôi). Đây là các định lý về hệ *điển hình* theo nghĩa độ đo, không phải phân loại mọi mặt hay mọi hoán vị.

**Những gì chưa được sắp xếp lại.** Không có định lý nào, của Avila hay của ai khác, "phân loại mọi hệ động lực". Động lực trơn ở chiều cao, vi phôi bảo toàn thể tích và nhiều vấn đề về hyperbolic từng phần vẫn còn mở. Sau này chính Avila còn đóng góp (cùng Crovisier, Wilkinson và những người khác) vào các vấn đề về entropy và tính ergodic, khá xa ánh xạ đơn mốt. Lời trích dẫn Fields nói về một *cách tiếp cận*, không phải một bộ bách khoa toàn thư.

---

## 3. Toán tử almost Mathieu và bài toán Ten Martini

**Toán tử almost Mathieu** trên $$\ell^2(\mathbb{Z})$$ là

$$
(H_{\lambda,\alpha}\psi)_n=\psi_{n+1}+\psi_{n-1}+2\lambda\cos\bigl(2\pi n\alpha\bigr)\,\psi_n,
$$

với hằng số liên kết $$\lambda\in\mathbb{R}$$ và tần số $$\alpha$$. Khi $$\alpha$$ hữu tỷ, phổ là hợp của hữu hạn đoạn. Khi $$\alpha$$ vô tỷ, phổ không phụ thuộc vào tham số pha (ở đây ta bỏ qua tham số này). Từ công trình của Azbel và hình **con bướm Hofstadter**, người ta dự đoán phổ là một **tập Cantor**: đóng, không đâu trù mật, không có điểm cô lập. **Mark Kac** treo thưởng mười ly martini cho ai chứng minh được điều này, và **Barry Simon** đặt tên là **bài toán Ten Martini**.

Các kết quả một phần được tích lũy qua nhiều thập niên (Bellissard–Simon, Sinai, Helffer–Sjöstrand, Last, Puig và những người khác), thường cần điều kiện Diophantine cho $$\alpha$$ hoặc phải tránh hằng số liên kết **tới hạn** $$|\lambda|=1$$. Trong giai đoạn 2005–2009, **Artur Avila** và **Svetlana Jitomirskaya** chứng minh phát biểu đầy đủ: phổ là tập Cantor với **mọi tần số vô tỷ và mọi hằng số liên kết khác không**. Khi đọc lần đầu, trường hợp không tới hạn $$|\lambda|\neq 1$$ là dễ hình dung nhất. Cái khó của bài toán là kỹ thuật cho tần số Diophantine và kỹ thuật cho tần số Liouville không tự khớp với nhau, và có một vùng tham số hẹp ở giữa phải xử lý riêng. Cần ghi nhận đây là định lý **chung** của hai tác giả. Các công trình sau đó của Jitomirskaya và những người khác mở rộng hiện tượng phổ Cantor cho các thế khác ngoài hàm cosin; đó là phần tiếp theo, không thuộc lời trích dẫn năm 2014.

**Lưu ý về độ chính xác.** Bài toán Ten Martini nói về *hình dạng* của phổ như một tập con của $$\mathbb{R}$$. Có những giả thuyết riêng về *độ đo* của phổ (giả thuyết Aubry–André: độ đo Lebesgue bằng $$|4-4|\lambda||$$) và về tính định xứ của hàm riêng. Đừng gộp chúng thành một câu.

---

## 4. Ghi nhận công lao một cách trung thực

Bản tin của IMU về công trình của Avila nói rõ: gần như toàn bộ công trình được làm cùng cộng sự, khoảng ba mươi nhà toán học. Một bảng tóm tắt công bằng như sau.

| Kết quả (tóm tắt) | Tác giả |
|---------------------|----------|
| Chính quy hay ngẫu nhiên cho ánh xạ đơn mốt điển hình | Avila–de Melo–Lyubich (2003) |
| Tính trộn yếu của hầu hết IET và dòng tịnh tiến | Avila–Forni (2007) |
| Phổ Cantor của toán tử almost Mathieu (Ten Martini) | Avila–Jitomirskaya (*Annals*, 2009) |
| Tính đơn của các số mũ Lyapunov của dòng Teichmüller | Avila–Viana (giả thuyết Zorich–Kontsevich) |
| Lý thuyết toàn cục cho toán tử Schrödinger một tần số | Avila (dựa trên truyền thống lâu dài của lý thuyết phổ) |
| Tái chuẩn hóa như một ý tưởng | Wilson, Feigenbaum, Sullivan, Lyubich, Yoccoz, … |

Avila lớn lên ở Rio de Janeiro, bảo vệ tiến sĩ tại **IMPA** năm 2001 dưới sự hướng dẫn của **Welington de Melo**, sau đó làm việc tại CNRS (Pháp) rồi Đại học Zurich. Ông là **người Brazil đầu tiên** và cũng là người Mỹ Latinh đầu tiên nhận Huy chương Fields. Những chi tiết tiểu sử này giúp hiểu vì sao công chúng quan tâm, nhưng không thay thế được các định lý.

---

## 5. Vì sao ông nhận Huy chương Fields

Có ba lý do liên quan với nhau. Không lý do nào là "ông đã chế ngự được hỗn loạn nói chung".

1. **Vượt qua ranh giới giữa các chế độ.** Lý thuyết phổ tựa tuần hoàn bị chia thành hai thế giới Diophantine và Liouville, trông như hai môn khác nhau. Giải bài toán Ten Martini và xây dựng lý thuyết toàn cục cho cocycle đòi hỏi phải làm việc được ở cả hai thế giới, thay vì chọn thế giới nào thuận tiện.
2. **Một phương pháp dùng được ở nhiều nơi.** Tái chuẩn hóa đã có từ trước. Avila biến nó thành *công cụ mặc định* cho nhiều bài toán hàng đầu, và nhờ đó thay đổi những gì một bài báo về hệ động lực có thể thử làm.
3. **Các định lý về tính điển hình.** Tính trộn yếu của IET và phân chia chính quy/ngẫu nhiên cho ánh xạ đơn mốt là các phát biểu về hầu hết mọi hệ theo một độ đo tự nhiên. Trong nhiều nhánh của hệ động lực, đây là cách hiện đại thay cho việc phân loại từng hệ một, điều vốn không thể làm được.

Trong khóa học, Avila được đặt cạnh [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) như một câu chuyện năm 2014 về không gian moduli của mặt và các dòng trên đó: hình học gần nhau nhưng câu hỏi khác nhau. Ông cũng thuộc nhóm các huy chương cho "một chương trình nghiên cứu" hơn là cho một giả thuyết số học riêng lẻ.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Avila phát minh ra tái chuẩn hóa." | Ý tưởng này có từ trước (Wilson, Feigenbaum, Sullivan, …). Ông dùng nó như một công cụ thống nhất. |
| "Ông đã phân loại mọi hệ động lực." | Ông chứng minh các định lý sâu cho một số lớp hệ cụ thể và quan trọng. |
| "Bài toán Ten Martini do một mình Avila giải." | Đó là công trình chung của **Avila–Jitomirskaya**. |
| "Mọi toán tử Schrödinger đều có phổ là tập Cantor." | Định lý dành cho họ almost Mathieu (và các mở rộng sau này). Toán tử một tần số tổng quát có nhiều chế độ hơn. |
| "Trộn yếu cũng là trộn." | IET không bao giờ trộn (theo nghĩa mạnh). Avila–Forni chứng minh tính trộn yếu cho phép trao đổi điển hình. |
| "Kết quả về số mũ Lyapunov của dòng Teichmüller là của riêng Avila." | Tính đơn là kết quả của Avila–Viana, hoàn thành giả thuyết Zorich–Kontsevich; Forni và những người khác cũng có đóng góp trong câu chuyện này. |

---

## Bài tập

1. Diễn đạt bằng lời của bạn: khi đi từ một ánh xạ đơn mốt sang ánh xạ quay về lần đầu đã đổi tỷ lệ, một **bước tái chuẩn hóa** bỏ đi thông tin gì và giữ lại thông tin gì?
2. Vì sao cả nhà vật lý lẫn nhà toán học đều quan tâm phổ có phải là tập Cantor hay không? Tách riêng "hình vẽ đẹp (con bướm Hofstadter)" và "định lý (tập đóng, phần trong rỗng, không có điểm cô lập)".
3. Viết toán tử almost Mathieu, đánh dấu **hằng số liên kết** và **tần số**. Điều gì xảy ra (ở mức ý tưởng) khi tần số hữu tỷ?
4. Bài toán Ten Martini: phát biểu định lý trong một câu và nêu tên **cả hai** tác giả. Sau đó viết một câu mà bạn *không chấp nhận* in ra (ví dụ "Avila chứng minh mọi phổ lượng tử đều là fractal").
5. Ánh xạ trao đổi khoảng: dùng một hình vẽ để giải thích vì sao việc cắt và xếp lại không nhất thiết trộn đều như khi xào bài, và khái niệm "trộn yếu" nhằm nắm bắt điều gì.
6. **Luyện ghi nhận công lao.** Lấy một câu trên báo phổ thông nói rằng Avila "giải được bài toán hỗn loạn". Viết lại thành hai câu chính xác cho khóa học này.
7. Đọc lướt văn bản của IMU năm 2014 về Avila (hoặc bản tin PDF) và liệt kê **ba** kết quả *không phải* bài toán Ten Martini.
8. **Seminar mở rộng.** So sánh các định lý của Avila về "ánh xạ đơn mốt điển hình" với các định lý của [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) về đường trắc địa điển hình trên không gian moduli. Cả hai đều nói về *một không gian các hệ*. Trong mỗi trường hợp, không gian đó là gì?

---

## Nguồn video và đọc thêm

Bài này không có bộ tài liệu video riêng của khóa học. Nên ưu tiên các nguồn chính thức và bách khoa.

1. Lời trích dẫn Huy chương Fields 2014 của IMU: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. Bản tin của IMU, *The Work of Artur Avila*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_avila.pdf).
3. Tra cứu bách khoa: [Artur Avila](https://en.wikipedia.org/wiki/Artur_Avila); [almost Mathieu operator](https://en.wikipedia.org/wiki/Almost_Mathieu_operator).
4. Bài giới thiệu của Quanta (2014): [A Brazilian Wunderkind Who Calms Chaos](https://www.quantamagazine.org/artur-avila-is-first-brazilian-mathematician-to-win-fields-medal-20140812/).
5. Tìm trên arXiv (renormalization + Avila): [query](https://arxiv.org/search/?query=Avila+renormalization&searchtype=all).
6. Avila–Jitomirskaya, *The Ten Martini Problem*, *Annals of Mathematics* (2009): [trang Annals](https://annals.math.princeton.edu/2009/170-1/p08).

**Ghi nhớ:** Tái chuẩn hóa là phương pháp thống nhất; bài toán Ten Martini là công trình chung; không có phân loại cho mọi hệ động lực.

---

## Tài liệu tham khảo


1. International Mathematical Union, Fields Medals 2014 — citation và news release Artur Avila (mathunion.org).
2. **A. Avila, S. Jitomirskaya**, *The Ten Martini Problem*, *Ann. of Math.* 170 (2009).
3. **A. Avila, G. Forni**, *Weak mixing for interval exchange transformations and translation flows*, *Ann. of Math.* (2007).
4. **A. Avila, W. de Melo, M. Lyubich**, *Regular or stochastic dynamics in real analytic families of unimodal maps*, *Invent. Math.* (2003).
5. **A. Avila, M. Viana**, công trình về tính đơn số mũ Lyapunov của dòng Teichmüller (giả thuyết Zorich–Kontsevich).
6. Tài liệu nền (không phải định lý của Avila): dãy nhân đôi chu kỳ của Feigenbaum; tái chuẩn hóa của Sullivan; các bài tổng quan về toán tử Schrödinger tựa tuần hoàn.
7. Trong khóa học: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Đọc một bài tổng quan ngắn về cocycle một tần số, đến khi bạn giải thích được "tính gần khả quy" mà không cần trích từ blog.
- So sánh tính trộn yếu của IET với dòng tịnh tiến trên mặt phẳng. Đây là cầu nối sang không gian moduli của Mirzakhani và sang bài toán bi-a.
- Bài seminar A3 (tùy chọn): viết một trang về "các bài toán mở sau Avila" (toán tử Schrödinger nhiều tần số; hằng số hiệu quả; vi phôi bảo toàn thể tích), không khẳng định rằng huy chương đã khép lại lý thuyết hệ động lực.
- Khi gặp hình con bướm Hofstadter, hãy viết *định lý* Ten Martini bên cạnh để hình vẽ không thay thế cho phát biểu toán học.

## Video tham khảo

- **Xem trước** — [Dynamical Systems and Renormalisation by Prof. Artur Avila](https://www.youtube.com/watch?v=F3e5g5BwDu8) — swissQuant, tiếng Anh. Bài nói của chính Avila về hệ động lực và tái chuẩn hóa, dành cho khán giả rộng. Nên xem trước khi đọc bài.
- [Artur Avila - Poincaré series and renormalization MCA 2013](https://www.youtube.com/watch?v=Hff4sJm0xBA) — MCA2013, tiếng Anh. Bài giảng chuyên môn về chuỗi Poincaré và tái chuẩn hóa. Nên xem sau khi đã nắm mục 1–2.
- [Fields Medal Winner 2014 Artur Avila](https://www.youtube.com/watch?v=405_UtglyoQ) — International Mathematical Union, tiếng Anh. Video giới thiệu của IMU về Avila và giải Fields 2014, bổ sung phần tiểu sử ở mục 4.
