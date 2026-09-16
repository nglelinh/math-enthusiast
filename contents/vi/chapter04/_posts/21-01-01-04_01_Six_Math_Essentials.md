---
layout: post
title: "Sáu Điều Cốt Yếu Của Toán Học (theo Terence Tao)"
chapter: '04'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
---

Toán học có thể trông như kho kỹ thuật không họ hàng: số nguyên tố ở dãy này, độ cong ở dãy kia, xúc xắc ở lối khác, phương trình chất lỏng trong phòng khóa. Terence Tao, trong [cuộc trò chuyện Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) giới thiệu cuốn sách sắp ra *Six Math Essentials*, đưa một bức tranh khác. Ông tổ chức một dải lớn của môn học quanh **sáu trụ cột quen thuộc**—số, đại số, hình học, xác suất, giải tích và động lực—mỗi trụ bắt đầu như thứ hầu như ai cũng đã gặp, rồi lớn dần qua nhiều thế kỷ thành ngôn ngữ chính xác để nghĩ cho rõ.

Bài này là **bản đồ khóa học**, không phải lời chứng thực cho một giáo trình, cũng không phải khẳng định rằng sáu chủ đề của Tao đã hết toán học. Các trụ cột không thay thế các bài toán Clay, chân dung Fields, hay các bài chứng minh ở chỗ khác trên site. Chúng cho những trang ấy một ngữ pháp chung. Khi bạn gọi được tên trụ cột mà một câu chuyện đang dùng, bạn có thể đi giữa các chương mà không mất mạch.

**Xem.** [One of the world's greatest mathematicians explains 6 essential concepts of math](https://www.youtube.com/watch?v=OOMx2BHHWtE) (Terence Tao, Big Think). Các đoạn diễn giải dưới đây bám cuộc trò chuyện đó; không phải câu trích được bịa.

**Ghi chú nghiên cứu.** Gói khóa học: `research/video-research/tao-six-essentials/`.

---

## Mục tiêu học tập

Sau bài này bạn cần làm được:

- Kể tên sáu trụ cột của Tao và đưa một ví dụ dễ gần cho mỗi trụ, mà không biến danh sách thành bản đồ đầy đủ của toán học.
- Giải thích, mỗi ý một câu, hệ thống số được mở rộng thế nào ($$\mathbb{N}\to\mathbb{Z}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}$$) và vì sao cú sốc $$\sqrt{2}$$ thuộc câu chuyện đó.
- Phân biệt **xảy ra hầu chắc chắn cuối cùng** với **thời gian chờ dùng được**, nhờ thí nghiệm tưởng tượng khỉ gõ máy.
- Nối một câu chuyện “tò mò trước” (tiên đề song song, xếp cầu, hoặc compressed sensing) với một lần dùng khoa học hay công nghệ sau đó—mà không khẳng định toán học luôn được trả công đúng hạn.
- Đi từ hub này sang các bài trên khóa học về [$$\sqrt{2}$$]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/), [vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/), [xếp cầu]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/), [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/), và [toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/).

**Tiên quyết.** Quen số phổ thông, một ít đại số, và ý rằng chứng minh là lập luận chứ không phải phép tính. Không cần giải tích sau đại học.

---

## 1. Một bản đồ, không phải atlas đầy đủ

Nhận xét mở đầu của Tao khiêm tốn và hữu ích. Sáu chủ đề thì cũ—có thứ tiền sử, có thứ mới vài thế kỷ—và vẫn là những từ nhà toán học với tới khi phải giải thích một môn mới cho người ngoài chuyên ngành. Lột hết trang phục kỹ thuật, còn lại những ý gần như quá trực giác: bao nhiêu, thao tác thế nào, đo không gian ra sao, sống với bất định thế nào, khống chế sai số và vô hạn ra sao, sự vật đổi theo thời gian thế nào. Sự tinh vi nằm ở **ngôn ngữ**, không ở một thành phần thứ bảy bí mật.

Danh sách là xương sống, không phải kiểm kê. Lý thuyết phạm trù, logic và tổ hợp không bị đuổi; chúng thường xuất hiện như cách nói *xuyên* các trụ cột. Khóa học này đã có những xương sống khác: bài toán mở nổi tiếng, chân dung giải thưởng, ứng dụng đổi thế giới, chứng minh nổi tiếng. Dùng sáu điều cốt yếu khi bạn muốn hỏi: “Trang hiện đại này vẫn đang luyện thói quen tư duy cổ xưa nào?”

---

## 2. Số: độ chính xác, rồi sự mở rộng

Số, Tao lưu ý, thuộc những phát minh cũ nhất ta còn thấy khắc trên xương. Không có chúng, mô tả ở lại thơ và trôi khi kể lại. Có chúng, đại lượng trở nên mang đi được: bạn nói về thóc, khoảng cách, hay thuế mà không phải chỉ tay vào đống. Nông nghiệp, thương mại, và bộ máy ít lãng mạn của văn minh đều cần sự mang đi ấy. Không phải mọi quyết định người đều nên thu thành bảng lãi–lỗ—Tao nói thẳng rằng một buổi hẹn không phải chỗ cho bảng tính—nhưng tài chính và y học đầy lựa chọn mà tư duy định lượng tự trang trải.

Câu chuyện sâu hơn là số **tự sống cuộc đời riêng**. Đếm cừu gợi phép cộng và trừ. Phép trừ không luôn ở lại trong $$\{1,2,3,\ldots\}$$, nên người ta phát minh số không và số âm, rồi thấy các luật cũ vẫn chạy: $$(A-B)+B=A$$ ngay cả khi $$B>A$$. Phép chia phát minh phân số. Rồi đến cú sốc: có độ dài nằm giữa mọi phân số; $$\sqrt{2}$$ không viết được thành tỉ số hai số nguyên. Lời Latin *irrational* ghi lại cảm giác vô lý lúc ấy. Về sau, căn bậc hai không chịu ở lại số thực sinh số phức, rồi số phức trở thành ngôn ngữ tự nhiên cho điện từ và cơ học lượng tử.

**Chỗ đáp của khóa học.** Chứng minh $$\sqrt{2}$$ không phải tỉ số là bài cổ điển Chương 5: [Vô tỉ của $$\sqrt{2}$$]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/). Cùng một đạo lý mở rộng—số mới được bịa để phương trình khép lại, rồi bất ngờ hữu ích—là bài học hệ thống số của essay đó.

---

## 3. Đại số: luật của phép toán, không chỉ của số

Đại số, trong lớp xếp của Tao, là trừu tượng lần hai. Số đã thay cừu bằng ký hiệu cộng được. Đại số thay số cụ thể bằng $$x$$ và $$y$$, rồi nghiên cứu chính **các phép toán**. Phép cộng giao hoán: $$A+B=B+A$$. Xoay một vật $$30^\circ$$ rồi $$60^\circ$$ giao hoán theo cùng nghĩa đại số; đi tất rồi đi giày thì không. Khi phép toán mới tuân luật bạn đã hiểu, bạn chuyển được chứng minh. Ma trận không phải số, nhưng thừa hưởng đủ cấu trúc đại số để đôi tay từng thao tác vô hướng bắt đầu thao tác mảng—cùng loại mảng mà mô hình ngôn ngữ lớn nhân ở quy mô công nghiệp. Xem [đại số tuyến tính và AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

Mẩu sử của Tao là Kepler ở chợ rượu. Một người đo thùng bằng một cây thước xuyên lỗ bung tới góc xa và đọc ra thể tích. Độ dài ấy không xác định thể tích cho mọi hình khả dĩ, nhưng nếu thương nhân đang cực đại hóa thể tích theo một đường chéo cho trước, một ít proto-calculus gần như phục hồi đúng những thùng thực sự được bán. Đại số cộng giả định tối ưu biến quy tắc thương mại rút từ thực nghiệm thành lời giải thích—và, Tao gợi ý, nằm trong dòng dõi của phép tính Newton và Leibniz sau này hệ thống hóa. Người anh ứng dụng là [giải tích trong vật lý và kỹ thuật]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/).

---

## 4. Hình học: đo điều bạn không chạm được

Hình học, đúng nghĩa gốc, là đo Trái Đất. Khoảng cách, góc, và **đồng dạng** cho phép suy khoảng cách núi từ góc nâng, hoặc—đã từ cổ đại—ước quy mô Mặt Trăng và Mặt Trời mà không phải đi tới đó. Hình học kéo dài giác quan.

Phần tiếp theo do tò mò dẫn dắt là **tiên đề song song**. Các tiên đề khác của Euclid nghe như tất yếu; khẳng định rằng qua một điểm ngoài đường thẳng có đúng một đường song song thì không. Bỏ nó đi, hai hình học nhất quán xuất hiện: hình học **cầu**, nơi các vòng lớn luôn cắt nhau (không có song song), và hình học **hyperbolic**, nơi có nhiều đường song song. Một khi “cái” hình học không còn duy nhất, không gian cong mọi kiểu trở nên nghĩ được. Hình học Riemann rồi cung cấp ngôn ngữ Einstein cần: khối–năng lượng bảo không-thời gian cong thế nào. Các phương trình thì tàn bạo khi giải—ngay hai lỗ đen va nhau cũng làm siêu máy tính căng—nhưng chúng *phát biểu* tự nhiên một khi vốn từ hình học đã có.

**Chỗ đáp của khóa học.** Cú sốc phi Euclid sống cùng [hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/). Phần xếp cầu trong cùng chương nói của Tao—đạn đại bác của Kepler, chứng minh 3D có máy tính hỗ trợ của Hales, rồi xếp rời rạc cao chiều như mã vô tuyến—đáp ở [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/) và [studio xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

---

## 5. Xác suất: sống với bất định

Bài toán lời ở trường thì đã khử trùng: Annie có ba mươi quả táo và không gì còn nghi. Thế giới thì không. Một đồng xu có một dải kết cục; ngay một lần tung “tất định” cũng quá đắt để dự từ nguyên lý đầu. Xác suất ghi **kết cục nào thường hơn**, không phải một sự chắc chắn giả.

Câu chuyện nguồn, như Tao kể, là thư từ đánh bạc: nếu tính được tỉ lệ, về dài hạn bạn tránh được vai người không tính được. Rồi môn học thoát sòng. Mọi hệ quá phức tạp cho mô hình cơ chế đủ—thị trường, thử thuốc, xổ số di truyền—mời một mô tả ngẫu nhiên. Xác suất chạy tốt nhất trên sự kiện lặp đủ để ước tần suất. Sự kiện **một lần trong thế kỷ** khớp kém hơn; toán cho thảm họa thực sự hiếm vẫn đang được xây. Đối lại sự tỉnh táo ấy là một điều kỳ: **tính phổ quát**. Những cơ chế khác nhau hoang dã thường sinh cùng hình dạng, đường cong chuông Gauss là ngôi sao.

**Chỗ đáp của khóa học.** [Xác suất và khoa học dữ liệu]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/). Trụ giải tích sẽ lập tức cảnh báo đừng nhầm “xác suất một” với “sắp xảy ra.”

---

## 6. Giải tích: thanh sai số, giới hạn, và vô hạn có dây an toàn

Giải tích, với Tao, là toán của **sự không chính xác** và của **vô hạn**. Một vật dài hai mét, cộng trừ mười centimet; thanh sai số là một phần của phát biểu. Bạn có thể đẩy sai số về không, nhưng chạm không có thể tốn một ngân sách vô hạn độ chính xác. Luật sắp xếp lại của đại số an toàn với năm số hạng và hiểm với vô hạn số hạng: một số chuỗi vô hạn đổi tổng khi bạn đổi thứ tự.

Một hoạt họa đánh bạc làm nguy hiểm thành cụ thể. Nếu bạn luôn gấp đôi cược hòa vốn đang thua, một lần thắng sau dường như gỡ đồng đô-la—**nếu** bạn có vốn vô hạn. Chiến lược ấy chỉ nén phá sản vào một biến cố tí hon, lúc số tiền đã thành thiên văn. Giải tích là thứ cho bạn thấy “vô hạn gian lận” rồi trở lại, cẩn thận, với tiền hữu hạn.

Định lý **khỉ vô hạn** là cùng một lời cảnh báo ở bộ đồ khác. Nếu một con khỉ gõ mãi, hoặc vô hạn con khỉ gõ, thì mọi văn bản hữu hạn cố định—kể cả *Hamlet*—xảy ra **hầu chắc chắn**. Ý chứng minh sơ cấp: mỗi khối có xác suất dương, lặp độc lập, đẩy xác suất thất bại vĩnh viễn về không. Thời gian chờ, ngược lại, lớn theo hàm mũ theo độ dài văn bản. Một từ bốn chữ cái có thể xuất hiện một buổi chiều; một trang *Hamlet* không phải thí nghiệm lớp học. “Hầu chắc chắn cuối cùng” không phải lịch trình.

Mã gian lận sư phạm của Tao mượn từ trò chơi điện tử thời trẻ: trước hết cho mình máu vô hạn, học bản đồ, rồi chơi bản tài nguyên hữu hạn. Lý tưởng hóa (ma sát không, năng lượng vô hạn), giải, rồi dùng giải tích để xem đặc trưng nào sống sót chuyến về. Đó cũng là bức tranh của ông về quy trình toán học: thất bại rẻ, nên bạn được phép thám **không gian âm** của những phương pháp không chạy cho đến khi đường còn lại trông hiển nhiên—và cảm giác ít “eureka” hơn là “sao mình bỏ sót sớm thế?” Tiêu chuẩn cao thuộc về **kết quả**; **quy trình** được phép là chuỗi dài những sai lầm thông minh.

**Chỗ đáp của khóa học.** Vô hạn cardinal và ordinal: [Vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/) (flagship seminar của chương này) và [đường chéo Cantor]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/). Studio: [Mô tả vô hạn]({{ site.baseurl }}/contents/vi/chapter07/07_08_Explore_Describe_Infinity/).

---

## 7. Động lực: quy tắc đơn, thời gian dài, bất ngờ

Động lực là đổi theo thời gian: một quy tắc đưa trạng thái sang trạng thái kế, lặp đến khi cấu trúc không ngờ xuất hiện. Các quy tắc địa phương của tiến hóa thì đơn và sinh quyển thì không. Mỗi xe trên cao tốc chỉ bám xe phía trước; mạng lưới sinh **sóng giao thông** còn đó nhiều giờ sau khi tai nạn gốc đã hết. Cân bằng có thể **ổn định** (con lắc treo) hoặc **không ổn định** (cùng con lắc dựng trên mũi). Nhận xét khí hậu của Tao là cảnh báo ổn định, không phải chương trình chính trị: một gần-cân-bằng sống lâu có thể bị rời, và động lực mới có thể ít khoan dung hơn.

Newton giải được bài toán **hai vật** dưới hấp dẫn bình phương nghịch và lấy lại ellipse của Kepler. Bài toán **ba vật**, theo Tao thuật lại lời Newton, cho ông nhức đầu: không có nghiệm đóng gọn, và số trị hiện đại cho thấy những đoạn dài gần tuần hoàn bị những lần sắp xếp lại đột ngột cắt. Ngay hệ Mặt Trời, êm trên thang thời gian người, cũng có thể giấu bất ổn dài hạn. Sau một ngưỡng, mô hình trung thực của một hệ hỗn độn tất định thường là mô hình **xác suất**: dự báo nhoè.

**Chỗ đáp của khóa học.** [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/), [hiện tượng nảy sinh]({{ site.baseurl }}/contents/vi/chapter04/04_12_Emergence/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Studio lặp]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/).

---

## 8. Các trụ cột nói với khoa học (và với khóa học này) thế nào

Tao coi STEM như một đường ống: khoa học cơ bản do tò mò dẫn, rồi khoa học ứng dụng, rồi kỹ thuật, rồi công nghiệp. Bỏ một cộng đồng là đường ống gãy. “Hiệu lực khó hiểu” của Eugene Wigner là điều bí: khái niệm bịa để chơi—số phức, không gian cong—sau đó khớp phòng thí nghiệm. Lý thuyết làm việc của chính Tao, đưa ra như một lý thuyết chứ không phải định lý, là lời giải thích ngắn thì hiếm, nên một ngôn ngữ toán cô đọng và một ngôn ngữ vật lý cô đọng đôi khi trùng nhau sau khi cả hai phía đã **bỏ học** một giả định xấu (thời gian tuyệt đối là ví dụ tương đối tính).

Ba câu chuyện từ cùng cuộc trò chuyện xuất hiện lại thành các essay khóa học:

| Câu chuyện (diễn giải từ Big Think) | Trang khóa học |
|-------------------------------------|----------------|
| $$\sqrt{2}$$ và mở rộng hệ thống số | [Vô tỉ của $$\sqrt{2}$$]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/) |
| Tiên đề song song → hình học Riemann → hấp dẫn | [Hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/) |
| Đạn đại bác → Kepler → xếp rời rạc cao chiều → mã vô tuyến | [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/) |
| MRI, bình phương tối thiểu, total variation, các “mẹo” được thống nhất | [Green–Tao / chân dung Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) (mẩu compressed sensing) |
| Khỉ vô hạn; cược gấp đôi | [Vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/) |
| Hai vật vs ba vật; hỗn độn như dự báo nhoè | [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) |
| Trực thăng tới thác so với đi bộ theo bản đồ | [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) |

Mẩu compressed sensing là câu Tao kể ở ngôi thứ nhất: một tái tạo MRI trông quá đẹp, một đêm cố chứng minh điều đó không thể, một bước thất bại đảo thành lời giải thích, rồi nhận ra nhà địa chấn và nhà thiên văn đã dùng mẹo họ hàng mà không có định lý chung. Chân dung Fields của Tao trên site này là định lý Green–Tao; mẩu chuyện nằm đó để “Tao 2006” không bị thu thành một tít cấp số cộng nguyên tố.

Về **AI**, Tao liệt các mode khoa học kế tiếp—lý thuyết, thí nghiệm, mô phỏng, dữ liệu lớn, và nay hỗ trợ tự động—và lo rằng trực thăng tới thác bỏ qua những hẻm bên chỉ thấy khi đi bộ. Mô hình ngôn ngữ lớn, trong bức tranh của ông, là động cơ đoán từ kế cực kỳ được huấn luyện: rộng, nhanh, và bổ sung cho **độ sâu** của người. Chứng minh có thể được sinh và kiểm nhanh hơn cộng đồng **tiêu hóa** chúng vào giáo trình. “Khó tiêu chứng minh” ấy là chủ đề Chương 6, không phải lý do bỏ nghiên cứu do tò mò dẫn dắt.

---

## 9. Nhầm lẫn thường gặp

1. **“Sáu chủ đề này là toàn bộ toán học.”** — Chúng là xương sống dạy học. Logic, tổ hợp, và nhiều lĩnh vực khác vẫn hạng nhất.
2. **“Hầu chắc chắn nghĩa là sắp xảy ra.”** — Con khỉ gõ *Hamlet* với xác suất một trong thời gian vô hạn; kỳ vọng chờ không phải kỹ năng sống.
3. **“Chiến lược gấp đôi thắng nhà cái.”** — Chỉ khi vốn vô hạn; giải tích là dây an toàn.
4. **“Hình học phi Euclid được bịa cho Einstein.”** — Hình học đến từ tò mò; vật lý đến sau.
5. **“Trang này chứng thực một cuốn sách hay một video như giáo trình chính thức.”** — Đây là bản đồ theo khung công khai của một nhà toán học, gắn với Big Think và một cuốn sách sắp ra, ngồi cạnh các bản đồ khác của khóa học.

---

## Bài tập

1. Với mỗi trụ trong sáu trụ, viết một câu mà bạn cùng lớp chưa xem video vẫn dùng được.
2. Phác thảo mở rộng $$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$$ và đánh dấu chỗ $$\sqrt{2}$$ và $$i$$ vào. Rồi đọc essay chứng minh [$$\sqrt{2}$$]({{ site.baseurl }}/contents/vi/chapter05/05_06_Irrationality_Sqrt2/) và thêm một câu về *vì sao* cú sốc Hy Lạp là sự kiện hệ thống số, không chỉ sự kiện thập phân.
3. Giải thích, không dùng công thức, khác biệt giữa “con khỉ hầu chắc chắn gõ câu này” và “ta nên chờ nó chiều nay.”
4. Trong ≤250 từ, kể lại chuyện tiên đề song song hoặc chuyện xếp-cầu-sang-mã như đường ống tò mò-đến-ứng-dụng. Gắn nhãn cái gì là định lý, cái gì là sử, cái gì là ẩn dụ.
5. Chọn một essay khóa học từ bảng Mục 8 và viết “thẻ trụ cột” bốn dòng: trụ nào nó dùng, trụ nào nó chỉ mượn.
6. (Nâng cao) Sau [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), đối chiếu hiệu năng trực thăng với hiểu biết khi đi bộ trong một đoạn. Thiện ích khoa học nào gặp rủi ro nếu chỉ tấm ảnh thác được tính?
7. (Nâng cao) Xem video Big Think và thêm một ghi chú có mốc thời gian (chủ đề + phút) mà bài này *không* phủ; mang tới seminar như câu hỏi, không như trụ cột chính thức mới.

---

## Nguồn video

Dùng cuộc trò chuyện cho **định hướng và câu chuyện**, không thay thế định lý được chứng ở chỗ khác trong khóa học.

1. **ORIENTATION / CORE** — Terence Tao, *One of the world's greatest mathematicians explains 6 essential concepts of math* (Big Think): [https://www.youtube.com/watch?v=OOMx2BHHWtE](https://www.youtube.com/watch?v=OOMx2BHHWtE).
2. Các chân dung và chứng minh đi cùng trên site này (Green–Tao, Viazovska, vô hạn, $$\sqrt{2}$$, Navier–Stokes, toán học của AI) có gói video-research riêng.

**Nhắc trạng thái.** *Six Math Essentials* là sách **sắp xuất bản** tính theo cuộc trò chuyện năm 2026. Trang này diễn giải một buổi nói chuyện công khai; không phải cuốn sách.

---

## Tài liệu

1. Terence Tao — cuộc trò chuyện Big Think, YouTube OOMx2BHHWtE: https://www.youtube.com/watch?v=OOMx2BHHWtE
2. Gói khóa học: `research/video-research/tao-six-essentials/`
3. Eugene Wigner, “The Unreasonable Effectiveness of Mathematics in the Natural Sciences” (tiểu luận sử mà Tao ám chỉ).
4. Các chỗ đáp khóa học liệt kê ở Mục 8; [Tổng quan Chương 4]({{ site.baseurl }}/contents/vi/chapter04/).
5. Green–Tao và compressed sensing: xem mẩu trong [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) và gói `research/video-research/Green_Tao/`.

*Ghi chú biết đọc.* Phỏng vấn phổ thông nén sử (Kepler, Euclid, Newton, Einstein, Hales). Ưu tiên các essay chuyên khi năm tháng, phát biểu định lý, hoặc dòng ghi công là chỗ chịu tải.

---

## Hướng đi tiếp

Đọc [Vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/) tiếp nếu muốn trụ giải tích ở tốc độ chậm; [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/) nếu muốn động lực. Để thấy cùng thói quen tư duy trả công ở quy mô giải thưởng, nhảy tới [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) và [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/). Cho chương AI của cùng cuộc trò chuyện, tới [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/). Điểm của một hub không phải là xong sáu trụ. Điểm là biết mình đang mở cửa nào.
