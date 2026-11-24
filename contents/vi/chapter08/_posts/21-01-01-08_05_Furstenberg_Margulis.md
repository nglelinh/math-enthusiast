---
layout: post
title: "Furstenberg & Margulis: Động lực, Ergodic, Rigidity (Abel 2020)"
chapter: '08'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

Hãy thử tưởng tượng một trò chơi tưởng chừng chẳng liên quan gì đến vật lý hay chuyển động: bạn chọn tùy ý một tập hợp các số nguyên dương chiếm ít nhất 1% mật độ của trục số—dù bạn cố tình chọn chúng lộn xộn đến đâu, liệu trong tập đó có luôn ẩn chứa một cấp số cộng dài 100 số hạng cách đều nhau không? Hoặc một câu hỏi khác: nếu bạn lấy ba số nguyên $$x, y, z$$ bất kỳ và tính $$x^2 + y^2 - \sqrt{2}\,z^2$$, tập các giá trị thu được có thể tiến sát *mọi* số thực tùy ý hay không?

Suốt nhiều thập niên, những câu hỏi thuần túy về số nguyên và tổ hợp ấy đã làm nản lòng bao thế hệ dùng công cụ đếm cổ điển. Thế rồi hai nhà toán học xuất hiện với một ý tưởng táo bạo đến mức làm thay đổi bản đồ của toán học thuần túy: **hãy biến các con số tĩnh lặng ấy thành chuyển động!** Thay vì đếm từng phần tử, hãy nhìn chúng như quỹ đạo của một điểm đang chạy trong một không gian có đối xứng, dưới sự dẫn dắt của xác suất và hệ động lực.

Năm **2020**, **Giải Abel** được trao chung cho **Hillel Furstenberg** (Đại học Hebrew Jerusalem) và **Gregory Margulis** (Đại học Yale):

> “for pioneering the use of methods from probability and dynamics in group theory, number theory and combinatorics.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2020)

Việc trao chung giải thưởng cho hai sự nghiệp mang phong cách rất khác nhau gửi đi một thông điệp rõ ràng: xác suất và hệ động lực không còn đứng bên lề toán học ứng dụng, mà đã trở thành động cơ giải mã những bí mật sâu nhất của số học, tổ hợp và lý thuyết nhóm. Tài liệu chính thức: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Định nghĩa lý thuyết ergodic như việc lấy trung bình theo quỹ đạo với một độ đo bất biến; nêu một chủ đề của Furstenberg (tái hồi nhiều lần / cấu trúc của các tập số nguyên có mật độ dương); nêu một chủ đề của Margulis (siêu cứng / tính số học / động lực thuần nhất); giải thích động lực học như một **công cụ** cho số học và tổ hợp, chứ không chỉ là chuyện hỗn độn; và nối cách nhìn này với [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) mà không khẳng định hai phương pháp giống hệt nhau.

**Kiến thức nền.** Nhóm tác động lên không gian; xác suất cơ bản (trung bình, độ đo); tập con của các số nguyên.

---

## Bản đồ kiến thức nền: Lý thuyết Ergodic, hệ động lực và nhóm Lie là gì và nghiên cứu những gì?

Nếu bạn tốt nghiệp đại học và từng học xác suất hay phương trình vi phân, ba khái niệm dưới đây sẽ giúp bạn mở khóa toàn bộ thế giới của Furstenberg và Margulis mà không cần giáo trình cao học:

- **Hệ động lực (Dynamical System):** Là bất kỳ quy tắc nào mô tả trạng thái của một hệ thay đổi theo thời gian. Ở dạng rời rạc, ta có một không gian $$X$$ và một ánh xạ $$T: X \to X$$; bắt đầu từ một điểm $$x$$, ta đi theo quỹ đạo $$x, Tx, T^2x, T^3x, \dots$$. Ví dụ đơn giản nhất là **phép quay trên đường tròn**: mỗi bước nhảy ta quay góc vô tỉ $$\alpha$$ (chẳng hạn $$\alpha = \sqrt{2}$$ vòng). Quỹ đạo của một điểm sẽ không bao giờ lặp lại đúng chỗ cũ, mà dần dần phủ kín và trải đều khắp đường tròn.
- **Lý thuyết Ergodic (Ergodic Theory):** Bắt nguồn từ vật lý thống kê của Boltzmann (nghiên cứu các phân tử khí chuyển động trong bình), lý thuyết ergodic hỏi: *nếu ta theo dõi một hạt duy nhất trong thời gian rất dài (trung bình theo thời gian), kết quả có trùng với việc chụp ảnh toàn bộ các trạng thái có thể của bình khí tại một thời điểm (trung bình theo không gian) hay không?* Một hệ có tính chất "không thể tách đôi thành hai vùng độc lập mà quỹ đạo không bao giờ đi qua nhau" gọi là hệ **ergodic**. Khi hệ là ergodic, định lý ergodic bảo đảm rằng hầu hết mọi quỹ đạo đều ghé thăm mọi vùng với tần suất đúng bằng kích thước (độ đo) của vùng đó.
- **Nhóm Lie, Lattice và Không gian thuần nhất (Homogeneous Space):** Một **nhóm Lie** $$G$$ là một nhóm đối xứng vừa có cấu trúc đại số, vừa là một không gian cong trơn tru—ví dụ nhóm các phép quay 3D $$\mathrm{SO}(3)$$ hay nhóm ma trận $$\mathrm{SL}_3(\mathbb{R})$$ có định thức bằng 1. Bên trong $$G$$ có thể chứa một nhóm con rời rạc đều đặn $$\Gamma$$ gọi là **lattice** (giống như lưới số nguyên $$\mathbb{Z}^n$$ nằm gọn trong không gian thực $$\mathbb{R}^n$$, hoặc $$\mathrm{SL}_3(\mathbb{Z})$$ nằm trong $$\mathrm{SL}_3(\mathbb{R})$$). Khi ta "gấp" không gian $$G$$ theo lưới đối xứng $$\Gamma$$, ta thu được **không gian thuần nhất** $$G/\Gamma$$ (giống như gấp mặt phẳng $$\mathbb{R}^2$$ theo lưới $$\mathbb{Z}^2$$ để ra mặt bánh donut $$\mathbb{T}^2$$). **Động lực thuần nhất** nghiên cứu các dòng chuyển động tự nhiên trên không gian $$G/\Gamma$$—và kỳ diệu thay, quỹ đạo của chúng lại chứa lời giải cho các bài toán số học cổ điển!

---

## 1. Một cuộc cách mạng chung

Lý thuyết số cổ điển vốn quen với việc đếm và ước lượng từng bước: đếm điểm nguyên trong một hình cầu, tìm số nguyên tố nằm trong một cấp số cộng, hay khảo sát tập giá trị của một dạng toàn phương. Furstenberg và Margulis đã mở ra một cánh cửa bất ngờ: nhiều bài toán số học và tổ hợp hóc búa bỗng trở nên trong suốt khi ta dịch chúng sang **bài toán về quỹ đạo** của một nhóm tác động lên một không gian, nơi một **độ đo bất biến** kiểm soát hành vi dài hạn.

Thông điệp chung của hai ông vừa mang chiều sâu kỹ thuật, vừa tạo ra một cuộc dịch chuyển văn hóa trong toán học:

> Xác suất và động lực học là **toán thuần túy cốt lõi**, không chỉ là phụ lục ứng dụng.

Ngày nay, ngôn ngữ ergodic và động lực thuần nhất đã thấm sâu vào lý thuyết số giải tích, lý thuyết nhóm hình học và tổ hợp cộng tính. Giải Abel 2020 ghi nhận hai người mở đường cho cuộc hội tụ lịch sử ấy.

---

## 2. Lý thuyết ergodic trong một trang

Một **hệ động lực bảo toàn độ đo** gồm bộ ba $$(X, \mu, T)$$: một không gian trạng thái $$X$$, một độ đo xác suất $$\mu$$ (với $$\mu(X) = 1$$), và một phép biến đổi $$T: X \to X$$ bảo toàn độ đo (tức $$\mu(T^{-1}A) = \mu(A)$$ với mọi tập đo được $$A$$). **Quỹ đạo** của một điểm $$x \in X$$ là dãy:

$$
\{ x,\, Tx,\, T^2x,\, T^3x,\, \dots \}.
$$

**Định lý ergodic Birkhoff** kết nối trung bình theo thời gian dọc quỹ đạo với trung bình theo không gian: nếu hệ là ergodic (không thể phân rã thành hai tập bất biến nhỏ hơn có độ đo dương), thì với mọi hàm khả tích $$f$$ và với hầu hết mọi điểm khởi đầu $$x$$,

$$
\lim_{N\to\infty}\frac{1}{N}\sum_{k=0}^{N-1} f(T^k x) = \int_X f\, d\mu.
$$

**Ví dụ trực quan:** Xét phép quay vô tỉ $$Tx = (x + \sqrt{2}) \bmod 1$$ trên đường tròn $$[0, 1)$$. Lấy $$f$$ là hàm chỉ thị của một cung nhỏ $$I$$ dài $$0{,}1$$. Định lý ergodic nói rằng tỷ lệ số bước nhảy rơi vào cung $$I$$ sẽ hội tụ đúng về $$0{,}1$$. Vì sao lý thuyết số lại say mê điều này? Bởi nhiều cấu hình số học (như việc một tập số nguyên chứa cấp số cộng) có thể mã hóa thành sự kiện **quỹ đạo đồng thời quay lại cùng một vùng $$A$$** tại những thời điểm cách đều nhau!

---

## 3. Furstenberg: tái hồi, cấu trúc và biên

### Tái hồi nhiều lần và cấu trúc kiểu Szemerédi

Năm 1975, Endre Szemerédi chứng minh một định lý tổ hợp lừng danh: *mọi tập con $$E \subset \mathbb{N}$$ có mật độ trên dương (ví dụ chứa ít nhất 0,001% các số tự nhiên) đều chứa những cấp số cộng dài $$k$$ tùy ý.* Chứng minh gốc của Szemerédi là một kiệt tác tổ hợp nhưng vô cùng dài và phức tạp.

Chỉ hai năm sau (1977), **Hillel Furstenberg** gây chấn động khi tìm ra một chứng minh hoàn toàn mới bằng **lý thuyết ergodic**. Qua **nguyên lý tương ứng Furstenberg**, ông dịch tập số nguyên $$E$$ thành một hệ động lực $$(X, \mu, T)$$ cùng một tập $$A \subset X$$ có độ đo dương $$\mu(A) > 0$$ (đóng vai trò mật độ của $$E$$). Khi đó, việc $$E$$ chứa một cấp số cộng $$k$$ số hạng $$a, a+n, a+2n, \dots, a+(k-1)n$$ tương đương với **Định lý tái hồi nhiều lần Furstenberg**: tồn tại bước thời gian $$n \ge 1$$ sao cho

$$
\mu\big(A \cap T^{-n}A \cap T^{-2n}A \cap \cdots \cap T^{-(k-1)n}A\big) > 0.
$$

Nếu định lý tái hồi Poincaré cổ điển (thế kỷ XIX) chỉ bảo đảm một điểm sẽ quay lại vùng $$A$$ một lần (ứng với $$k=2$$), thì Furstenberg chứng minh nó sẽ quay lại **liên tiếp $$k$$ lần theo những nhịp thời gian đều đặn**!

Ý tưởng sâu xa phía sau rất đẹp: **sự tái hồi của quỹ đạo mã hóa các mẫu hình tổ hợp.** Để chứng minh định lý tái hồi, Furstenberg xây dựng một định lý cấu trúc phân tách mọi hệ động lực thành phần "có trật tự" (compact / gần tuần hoàn) và phần "trộn mạnh" (weakly mixing)—và chính tư tưởng phân tách cấu trúc–ngẫu nhiên này về sau trở thành linh hồn của chứng minh Định lý Green–Tao về cấp số cộng trong các số nguyên tố!

### Ứng dụng số học và biên

Ngoài tái hồi nhiều lần, Furstenberg còn đặt nền móng cho **lý thuyết biên (Furstenberg boundary)** của các bước đi ngẫu nhiên trên nhóm Lie và nhóm rời rạc—biến việc nghiên cứu xác suất của bước đi ngẫu nhiên thành công cụ khám phá cấu trúc hình học ở vô cùng của nhóm. Phong cách của ông mang dấu ấn không thể lẫn: dịch một câu hỏi rời rạc khô cứng thành bài toán động lực có độ đo, rồi thu hoạch tính tái hồi và cấu trúc.

---

## 4. Margulis: tính cứng, tính số học, động lực thuần nhất

Nếu Furstenberg là bậc thầy của những hệ động lực trừu tượng, thì **Gregory Margulis** là kiến trúc sư của thế giới đối xứng hình học: nhóm Lie, lattice và không gian thuần nhất.

### Siêu cứng (Superrigidity)

Định lý **siêu cứng** của Margulis là một trong những kết quả gây kinh ngạc nhất của thế kỷ XX: nếu $$\Gamma$$ là một lattice trong một nhóm Lie nửa đơn "hạng cao" (như $$\mathrm{SL}_3(\mathbb{Z}) \subset \mathrm{SL}_3(\mathbb{R})$$), thì hầu như mọi đồng cấu nhóm từ $$\Gamma$$ vào một nhóm ma trận đại số khác đều không thể hành xử tùy tiện—nó buộc phải mở rộng thành một ánh xạ đại số trơn trên toàn bộ nhóm Lie $$G$$! Trực giác: khi số chiều đối xứng đủ cao, cấu trúc hình học trở nên "cứng như kim cương", khóa chặt mọi phép biến dạng hoang dại.

### Tính số học (Arithmeticity)

Từ định lý siêu cứng, Margulis suy ra **Định lý tính số học** nổi tiếng (đã mang về cho ông Huy chương Fields năm 1978): mọi lattice bất khả quy trong nhóm Lie nửa đơn hạng cao đều bắt buộc có nguồn gốc **số học** (tức xây dựng từ các ma trận có phần tử nguyên hoặc nguyên đại số, giống như $$\mathrm{SL}_n(\mathbb{Z})$$). Một đối tượng hoàn toàn hình học–rời rạc lại bị ép phải mang bản chất lý thuyết số!

### Động lực thuần nhất và Giả thuyết Oppenheim

Đỉnh cao minh họa cho sức mạnh của động lực thuần nhất là chứng minh của Margulis năm 1986 cho **Giả thuyết Oppenheim** (tồn tại gần 60 năm). Xét dạng toàn phương ba biến không xác định:

$$
Q(x, y, z) = x^2 + y^2 - \sqrt{2}\, z^2.
$$

Vì hệ số $$\sqrt{2}$$ là số vô tỉ, ta có thể làm cho $$\lvert Q(x, y, z)\rvert$$ nhỏ tùy ý (chẳng hạn nhỏ hơn $$10^{-100}$$) bằng cách chọn các số nguyên $$(x, y, z) \neq (0,0,0)$$ không? Phương pháp lý thuyết số giải tích truyền thống chỉ làm được khi số biến từ 5 trở lên, và hoàn toàn bó tay ở 3 biến.

Margulis đã xoay chuyển cục diện chỉ bằng vài trang lập luận tuyệt đẹp: ông xét không gian thuần nhất $$X = \mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$ (chính là không gian của tất cả các mạng lưới 3 chiều có thể tích đơn vị) và cho nhóm đối xứng $$H = \mathrm{SO}(2,1)$$ bảo toàn dạng $$Q$$ tác động lên đó. Câu hỏi về giá trị của $$Q$$ tại điểm nguyên hóa ra tương đương với việc hỏi **quỹ đạo của nhóm $$H$$ trong $$X$$ có bị chặn hay lan ra trù mật**. Bằng cách khai thác tính cứng của các dòng unipotent (mà Marina Ratner sau này hoàn thiện thành bộ định lý tổng quát), Margulis chứng minh quỹ đạo ấy không thể thu gọn lại một cách bệnh lý—và Giả thuyết Oppenheim lập tức sụp đổ!

### Expander và giao diện giữa toán thuần túy và khoa học máy tính

Năm 1973, Margulis còn tạo ra một bước ngoặt khác: ông dùng tính chất (T) của Kazhdan trong lý thuyết nhóm để xây dựng họ **đồ thị expander tường minh đầu tiên** trong lịch sử. Đồ thị expander là những mạng lưới rất thưa (mỗi đỉnh chỉ nối với vài đỉnh lân cận) nhưng kết nối cực kỳ chắc chắn và trộn thông tin nhanh chóng. Ngày nay expander là viên gạch nền của lý thuyết mã sửa lỗi, mật mã học, mạng truyền thông và khoa học máy tính lý thuyết—nối trực tiếp Giải Abel 2020 sang Giải Abel 2021 của Lovász và Wigderson.

---

## 5. Khẩu hiệu của động lực thuần nhất (bản đồ sâu hơn)

Trong hệ động lực hỗn độn thông thường (như ánh xạ logistic hay thời tiết), quỹ đạo có thể tạo ra những tập fractal rối rắm không sao phân loại nổi. Ngược lại, các **dòng unipotent** trên không gian thuần nhất $$G/\Gamma$$ lại có bao đóng quỹ đạo cực kỳ **cứng**: bao đóng của mỗi quỹ đạo luôn là một không gian con thuần nhất mượt mà, không bao giờ biến thành fractal kỳ dị.

Tính cứng ấy là món quà vô giá cho lý thuyết số. Thay vì phải vật lộn ước lượng từng sai số nhỏ bằng tay, nhà toán học chỉ cần tìm ra đúng không gian thuần nhất mã hóa bài toán: sự cứng rắn của quỹ đạo sẽ tự động phân loại mọi khả năng số học có thể xảy ra.

Dù Furstenberg (nghiêng về hệ bảo toàn độ đo trừu tượng và tổ hợp) và Margulis (nghiêng về nhóm Lie, lattice và không gian thuần nhất) vận hành hai cỗ máy khác nhau, Giải Abel 2020 đặt họ đứng cạnh nhau vì cả hai đều chứng minh rằng **động lực học là một ngôn ngữ bản địa của toán thuần túy**.

---

## 6. Vì sao Abel ghép hai người

Hai phong cách khác biệt, một cuộc cách mạng chung. Sau Furstenberg và Margulis, các nhà lý thuyết số xem độ đo bất biến như công cụ hằng ngày; các nhà tổ hợp trích dẫn định lý tái hồi ergodic; và các nhà hình học nhóm rời rạc sống trong động lực thuần nhất. Xác suất không còn bị gán mác "chỉ để thống kê", còn động lực học không còn bị đóng khung là "chỉ vẽ hình hỗn độn".

Đặt cạnh [Định lý Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) (trong câu chuyện Huy chương Fields ở Chương 02): việc tìm cấp số cộng dài tùy ý trong tập số nguyên tố sử dụng tư duy tổ hợp cộng tính kết hợp chặt chẽ với tinh thần cấu trúc–ngẫu nhiên xuất phát từ chứng minh ergodic của Furstenberg. Giải Abel 2020 vinh danh hai người mở đường đã khởi phát toàn bộ làn sóng ấy.

---

## 7. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Ergodic chỉ là vật lý hay thống kê.” | Đó là lý thuyết toán thuần túy về hệ bảo toàn độ đo, có ứng dụng số học. |
| “Furstenberg chứng minh Szemerédi trước.” | Chứng minh tổ hợp của Szemerédi có trước; Furstenberg đưa ra chứng minh ergodic mang tính nền tảng. |
| “Tính cứng nghĩa là không có gì chuyển động.” | Các ánh xạ và quỹ đạo bị ràng buộc mạnh, thường là theo kiểu đại số, chứ không tùy ý. |
| “Expander chỉ dành cho khoa học máy tính.” | Chúng cũng là trung tâm của toán thuần túy (nhóm, hình học, phổ của đồ thị). |
| “Động lực học giải quyết xong lý thuyết số.” | Là bộ công cụ mạnh cho *một số* bài toán; nhiều bài còn nằm ngoài tầm với. |

---

## Bài tập

1. Tìm một ẩn dụ đời thường cho trung bình theo quỹ đạo.  
2. Vì sao mật độ dương của một tập số nguyên có thể liên quan đến tái hồi? Không quá 120 từ.  
3. So với [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/): một điểm giống và một điểm khác.  
4. **Không quá 200 từ:** “tính cứng” gợi lên điều gì trong thế giới của Margulis?  
5. Nêu một tác động của Margulis ở gần khoa học máy tính (expander) và một tác động số học.  
6. Đọc tài liệu về Abel 2020 trên [abelprize.no](https://abelprize.no/); trích ra ba danh từ chỉ đối tượng toán học.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2020: động lực và xác suất → số học và tổ hợp.
- Tái hồi của Furstenberg; siêu cứng, expander và giả thuyết Oppenheim của Margulis.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: các bài giảng Abel 2020 của Furstenberg và Margulis: [https://www.youtube.com/watch?v=2i5UJwKN7os](https://www.youtube.com/watch?v=2i5UJwKN7os).  
2. **Lịch sử**: phỏng vấn Furstenberg của giải Abel: [https://www.youtube.com/watch?v=01IdfSRYawE](https://www.youtube.com/watch?v=01IdfSRYawE).  
3. **Lịch sử**: phỏng vấn Margulis của giải Abel: [https://www.youtube.com/watch?v=FInTu9-MHHU](https://www.youtube.com/watch?v=FInTu9-MHHU).  
4. **Định hướng**: phần trình bày phổ thông về công trình 2020 (đoạn của Bellos): [https://www.youtube.com/watch?v=Fqdl_jyw8OE](https://www.youtube.com/watch?v=Fqdl_jyw8OE).  
5. **Liên quan**: Margulis nói về entropy Kolmogorov–Sinai (tuần Abel trước đó): [https://www.youtube.com/watch?v=cuYO5NQieRA](https://www.youtube.com/watch?v=cuYO5NQieRA).  

**Cổng chính thức và tài liệu**

- Abel 2020 Furstenberg & Margulis: https://abelprize.no/abel-prize-laureates/2020  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/furstenberg-margulis_2i5UJwKN7os_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2020 Furstenberg & Margulis — https://abelprize.no/abel-prize-laureates/2020  
2. Abel lectures 2020 Furstenberg & Margulis — https://www.youtube.com/watch?v=2i5UJwKN7os  
3. Abel interview Furstenberg — https://www.youtube.com/watch?v=01IdfSRYawE  
4. Abel interview Margulis — https://www.youtube.com/watch?v=FInTu9-MHHU  
5. Popular presentation of 2020 work (Bellos clip) — https://www.youtube.com/watch?v=Fqdl_jyw8OE  
6. Margulis on Kolmogorov–Sinai entropy (earlier Abel week) — https://www.youtube.com/watch?v=cuYO5NQieRA  
7. NYT Abel 2020 — https://www.nytimes.com/2020/03/18/science/abel-prize-mathematics.html  
8. Nature Abel 2020 — https://www.nature.com/articles/d41586-020-00799-7  
9. Wikipedia — Hillel Furstenberg — https://en.wikipedia.org/wiki/Hillel_Furstenberg  
10. Wikipedia — Grigory Margulis — https://en.wikipedia.org/wiki/Grigory_Margulis  

1. [Abel 2020](https://abelprize.no/abel-prize-laureates/2020).  
2. Bài trình bày về động lực thuần nhất; bài khảo sát về tái hồi nhiều lần của Furstenberg.  
3. Szemerédi: văn liệu tổ hợp và văn liệu ergodic chạy song song.  
4. Trong khóa: Green–Tao; sau đó là Lovász–Wigderson.

---

## Hướng đi tiếp

- Cây cầu tổ hợp cộng tính không cần toàn bộ ergodic: “động lực học phát hiện các mẫu hình”.  
- Đọc một bài phổ thông về Oppenheim qua động lực học.  
- So tính cứng ở đây với tính cứng của Sullivan (không có miền lang thang).  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Lovász & Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

## Xác suất và đối xứng trên không gian thuần nhất

Furstenberg–Margulis (Abel 2020) tôn vinh sự giao thoa giữa **lý thuyết ergodic, nhóm Lie và các ứng dụng số học và hình học**. Khẩu hiệu cho seminar: biến một câu hỏi số học hay hình học thành động lực học của một tác động nhóm, rồi khai thác các bất biến và độ đo.

## Đừng đồng nhất “ngẫu nhiên” với “không có cấu trúc”

Lý thuyết ergodic nói về trung bình theo thời gian hoặc theo không gian của các hệ động lực, thường là những cấu trúc rất cứng. Đó không phải là chuyện “toán học trở nên mơ hồ”.

## Studio

Viết 200 từ phân biệt: (a) dãy ngẫu nhiên theo nghĩa thuật toán, (b) quỹ đạo ergodic, (c) định lý mật độ kiểu Szemerédi (nếu đã học Green–Tao). Nêu một chỗ dễ nhầm thuật ngữ giữa ba thế giới đó.

## Video tham khảo

- **Xem trước** — [The Abel lectures: Hillel Furstenberg and Gregory Margulis](https://www.youtube.com/watch?v=2i5UJwKN7os) — The Abel Prize, tiếng Anh. Xem trước để nghe chính hai laureate trình bày công trình của mình.
- [Hillel Furstenberg - The Abel Prize interview 2020](https://www.youtube.com/watch?v=01IdfSRYawE) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe Furstenberg kể về con đường làm toán.
- [Gregory Margulis - The Abel Prize interview 2020](https://www.youtube.com/watch?v=FInTu9-MHHU) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua cuộc phỏng vấn Margulis.
