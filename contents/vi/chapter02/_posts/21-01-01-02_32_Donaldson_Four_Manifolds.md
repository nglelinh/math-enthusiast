---
layout: post
title: "Đa tạp bốn chiều và cấu trúc trơn ngoại lai của Donaldson (Huy chương Fields 1986)"
chapter: '02'
order: 32
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử hỏi một câu tưởng chừng ngớ ngẩn trong giải tích nhiều biến: có bao nhiêu cách để định nghĩa phép lấy đạo hàm trên không gian Euclid $$\mathbb{R}^n$$? Nếu $$n = 1, 2, 3$$, câu trả lời là **duy nhất một cách**. Nếu $$n = 5, 6, 7, \ldots, 100$$, câu trả lời vẫn là **duy nhất một cách**! Ta dễ dàng tin rằng chẳng có lý do gì số $$4$$ lại khác biệt. Ấy vậy mà vào mùa xuân năm 1982, một nghiên cứu sinh 24 tuổi tại Oxford tên **Simon Donaldson** — dùng phương trình **Yang–Mills** từ vật lý hạt cơ bản — đã làm chấn động cả thế giới toán học bằng một cú va chạm lịch sử: **riêng không gian bốn chiều $$\mathbb{R}^4$$ lại sở hữu vô hạn (thậm chí không đếm được!) những "cấu trúc vi phân lạ" (exotic $$\mathbb{R}^4$$)** — những không gian hoàn toàn giống $$\mathbb{R}^4$$ về mặt tôpô liên tục nhưng *không thể nào* chuyển đổi trơn mượt sang $$\mathbb{R}^4$$ quen thuộc của chúng ta!

Tại ICM Berkeley năm 1986, **Simon Donaldson** nhận **Huy chương Fields**:

> primarily for his work on the topology of four-manifolds, especially for showing that there is a differential structure on Euclidean four-space which is different from the usual structure.  
> — [IMU, Fields Medals 1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)

*Tạm dịch: chủ yếu vì công trình về tôpô của các đa tạp bốn chiều, đặc biệt là việc chỉ ra rằng có một cấu trúc vi phân trên không gian Euclid bốn chiều khác với cấu trúc thông thường.*

Để hiểu trọn vẹn kỳ tích năm 1986, ta phải đặt đúng **ba mảnh ghép** cạnh nhau: (1) định lý phân loại tôpô đa tạp 4 chiều đơn liên của **Michael Freedman** (1982, cũng nhận Huy chương Fields ngay tại ICM Berkeley 1986); (2) nền tảng giải tích về tính compact và "sủi bọt" cho phương trình Yang–Mills của **Karen Uhlenbeck** (xem [Uhlenbeck / lý thuyết gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)); và (3) định lý ràng buộc trơn chấn động của **Simon Donaldson** (1983) từ không gian moduli instanton. Chính sự **va chạm trực diện** giữa sự linh hoạt kỳ lạ của thế giới tôpô (Freedman) và sự cứng rắn khắc nghiệt của thế giới trơn (Donaldson) mới đẻ ra những đa tạp 4 chiều không thể làm trơn và các $$\mathbb{R}^4$$ lạ! Còn **lý thuyết Seiberg–Witten** (Witten, 1994) là một cuộc cách mạng gauge thứ hai ra đời 8 năm sau đó (xem bối cảnh tại [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/)), và việc phân loại toàn bộ đa tạp 4 chiều trơn đến nay vẫn còn mở.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao **chiều bốn** là số chiều dị biệt nhất trong tôpô: quá nhỏ để mẹo Whitney của chiều cao ($$n \ge 5$$) hoạt động trong phạm trù trơn, nhưng lại quá lớn so với cắt dán của chiều thấp ($$n \le 3$$).
- Định nghĩa trực quan **dạng giao** $$Q_X$$ của một đa tạp 4 chiều đóng, định hướng (đếm số giao có dấu giữa hai mặt 2 chiều bên trong không gian 4 chiều) và hiểu vì sao nó là dạng song tuyến đối xứng unimodular trên $$\mathbb{Z}$$.
- Phát biểu **định lý Donaldson (1983)**: mọi dạng giao xác định của một đa tạp 4 chiều **trơn** đóng, định hướng đều phải chéo hóa được trên $$\mathbb{Z}$$.
- Đối chiếu với **định lý Freedman (1982)**: mọi dạng unimodular đều thực hiện được bởi một đa tạp 4 chiều **tôpô** đơn liên (kéo theo giả thuyết Poincaré 4 chiều tôpô).
- Giải thích vì sao sự va chạm **Freedman + Donaldson** lập tức sinh ra (i) đa tạp 4 chiều tôpô **không có bất kỳ cấu trúc trơn nào** (như đa tạp $$E_8$$) và (ii) các **$$\mathbb{R}^4$$ lạ**.
- Mô tả ý tưởng hình học của không gian moduli **instanton** (phương trình Yang–Mills phản tự đối ngẫu) cùng nền tảng giải tích của **Uhlenbeck** (hiện tượng sủi bọt tạo biên).
- Tách bạch **lý thuyết Seiberg–Witten (1994)** khỏi Huy chương Fields 1986, và không phóng đại rằng Donaldson đã phân loại mọi đa tạp 4 chiều.

**Kiến thức nền.** Đa tạp trơn, đồng điều và tích cup ở mức giáo trình tôpô đại số nhập môn; khái niệm phân thớ vectơ và liên thông. Không cần học trước lý thuyết gauge: có thể hiểu liên thông là một cách lấy đạo hàm các nhát cắt, và độ cong đo mức độ các đạo hàm riêng hỗn hợp không giao hoán.

**Liên kết với các bài khác.** Bài này cho thấy phương trình đạo hàm riêng có nguồn gốc vật lý trở thành công cụ tôpô, và sự khác nhau giữa phạm trù tôpô với phạm trù trơn. Đọc cùng [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) (cách tiếp cận giải tích – hình học cho đa tạp ba chiều về sau), và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Bản đồ kiến thức nền: Tôpô 4 chiều, dạng giao và lý thuyết trường chuẩn là gì?

Để cảm nhận cú sốc mà Donaldson tạo ra, chỉ cần nắm vững ba khái niệm trực quan sau.

**1. Đa tạp "tôpô" khác gì đa tạp "trơn"?**
- Một **đa tạp tôpô** là không gian mà cục bộ trông giống $$\mathbb{R}^n$$ qua các phép biến đổi **liên tục** (như nặn đất sét dẻo: bạn có thể tạo góc nhọn, nếp gấp miễn không xé rách). Hai đa tạp tôpô giống nhau gọi là **đồng phôi** (*homeomorphic*).
- Một **đa tạp trơn** (khả vi) được trang bị thêm một hệ tọa độ cho phép **lấy đạo hàm** nhất quán ở mọi nơi (không góc nhọn). Hai đa tạp trơn giống nhau gọi là **vi phôi** (*diffeomorphic*).
Câu hỏi lớn của tôpô: một đa tạp tôpô có thể có *bao nhiêu* cấu trúc trơn khác nhau (không vi phôi với nhau)? (Ví dụ Milnor năm 1956 từng gây sốc khi tìm thấy 28 cấu trúc trơn khác nhau trên mặt cầu 7 chiều $$S^7$$ — nhưng trên không gian phẳng $$\mathbb{R}^n$$ với mọi $$n \neq 4$$, cấu trúc trơn luôn là duy nhất!)

**2. Dạng giao (Intersection form) — "dấu vân tay" của đa tạp 4 chiều.**
Trong không gian 3 chiều, hai đường thẳng tổng quát né nhau; trong mặt phẳng 2 chiều, hai đường cong cắt nhau tại hữu hạn điểm. Tương tự, trong một **đa tạp 4 chiều** đóng, định hướng $$X$$, hai mặt 2 chiều tổng quát (như hai mặt cầu hay hai hình xuyến nằm bên trong $$X$$) cắt nhau tại **hữu hạn điểm** (vì $$2 + 2 = 4$$!). Đếm tổng số giao có dấu ($$+1$$ hoặc $$-1$$ tùy định hướng) giữa các lớp mặt 2 chiều trong $$H_2(X; \mathbb{Z})$$ cho ta một ma trận nguyên đối xứng có định thức $$\pm 1$$ (unimodular) gọi là **dạng giao** $$Q_X$$:

$$
Q_X: H_2(X;\mathbb{Z})/\mathrm{torsion}\times H_2(X;\mathbb{Z})/\mathrm{torsion}\to\mathbb{Z}.
$$

Ví dụ quen thuộc: với mặt phẳng xạ ảnh phức $$\mathbb{CP}^2$$ (chiều thực 4), hai đường thẳng phức luôn cắt nhau tại đúng $$1$$ điểm, nên dạng giao là ma trận $$1 \times 1$$: $$\langle +1 \rangle$$. Ngược lại, trong lý thuyết số có những ma trận unimodular xác định dương **không thể chéo hóa trên $$\mathbb{Z}$$** — nổi tiếng nhất là ma trận $$8 \times 8$$ của **lưới $$E_8$$** (mọi phần tử đường chéo đều là $$2$$, định thức bằng $$1$$, xác định dương, nhưng không có vector nguyên nào có bình phương độ dài bằng $$1$$!).

**3. Lý thuyết trường chuẩn (Gauge Theory) & Instanton — khi vật lý hạt soi chiếu tôpô.**
Trong vật lý lý thuyết, **phương trình Yang–Mills** mô tả lực tương tác mạnh và yếu thông qua một **liên thông** $$A$$ (thế trường chuẩn) và **độ cong** $$F_A$$ (cường độ trường). Trên đa tạp 4 chiều, nhờ một phép đối xứng kỳ diệu riêng có ở chiều 4 (toán tử sao Hodge $$\star$$ biến 2-dạng thành 2-dạng với $$\star^2 = 1$$), độ cong tách đôi thành phần tự đối ngẫu $$F_A^+$$ và phản tự đối ngẫu $$F_A^-$$. Những liên thông làm cực tiểu hóa năng lượng Yang–Mills thỏa phương trình cấp một **$$F_A^+ = 0$$** gọi là các **instanton**. Trước Donaldson, các nhà toán học tìm cách giải phương trình Yang–Mills *trên một đa tạp cố định*. Ý tưởng đảo ngược thiên tài của Donaldson là: **dùng không gian tất cả các nghiệm instanton như một chiếc máy chụp X-quang để nhìn thấu cấu trúc trơn của chính đa tạp 4 chiều $$X$$!**

---

## 1. Vì sao chiều bốn không chỉ là "thêm một giá trị của $$n$$"

Ở chiều cao ($$n \ge 5$$), **mẹo Whitney** (kéo trượt hai đĩa con để triệt tiêu từng cặp điểm giao ngược dấu) có đủ "khoảng trống" để thực hiện mà không tự cắt, dẫn đến định lý $$h$$-cobordism của Smale và lý thuyết phẫu thuật phân loại đa tạp. Ở chiều thấp ($$n \le 3$$), các mặt cắt đơn giản và hình học hóa Thurston–Perelman kiểm soát toàn bộ không gian.

**Chiều bốn** rơi đúng vào ranh giới định mệnh: hai đĩa 2 chiều trong không gian 4 chiều ($$2 + 2 = 4$$) cắt nhau tại những điểm cô lập, nên khi cố thực hiện mẹo Whitney để xóa điểm giao cũ, ta lại vô tình đẻ ra **điểm giao mới**! Trong phạm trù tôpô, ta có thể đẩy các điểm giao mới ra vô tận thành một tháp vô hạn gọi là **tay cầm Casson** (*Casson handle*) — vốn vẫn đồng phôi với tay cầm chuẩn. Nhưng trong phạm trù trơn, tháp vô hạn đó gãy gập hoàn toàn! Chính vì vậy, chiều bốn là nơi phạm trù tôpô và phạm trù trơn **xé tách nhau sâu sắc nhất** trong toàn bộ toán học.

---

## 2. Michael Freedman (1982): sự tự do tuyệt đối của thế giới tôpô 4 chiều

Trong kiệt tác *"The topology of four-dimensional manifolds"* (*J. Differential Geom.* 17, 1982), **Michael Freedman** chứng minh rằng tay cầm Casson thực sự đồng phôi với tay cầm 2 chiều chuẩn $$D^2 \times \mathbb{R}^2$$. Từ đó ông thu được bảng phân loại chấn động cho **mọi đa tạp 4 chiều tôpô đóng, đơn liên**:
- **Mọi** dạng song tuyến đối xứng unimodular trên $$\mathbb{Z}$$ (kể cả những dạng kỳ lạ như $$E_8$$!) đều là dạng giao của một đa tạp 4 chiều **tôpô** đóng, đơn liên;
- Nếu dạng giao là **chẵn**, đa tạp tôpô đó là **duy nhất** sai khác đồng phôi; nếu dạng giao là **lẻ**, có đúng **hai** lớp đồng phôi (phân biệt bởi bất biến Kirby–Siebenmann $$\in \mathbb{Z}/2$$).
- Hệ quả lừng danh: **Giả thuyết Poincaré 4 chiều trong phạm trù tôpô là đúng** — mọi đa tạp 4 chiều tôpô tương đương đồng luân với $$S^4$$ đều đồng phôi với $$S^4$$! (Lưu ý: giả thuyết Poincaré 4 chiều **trơn** đến tận ngày nay vẫn là bài toán mở nổi tiếng nhất của tôpô!)

---

## 3. Định lý Donaldson (1983): cú sốc trong thế giới trơn và sự ra đời của $$\mathbb{R}^4$$ lạ

Chỉ một năm sau bài báo của Freedman, khi mới là nghiên cứu sinh năm hai ở Oxford (dưới sự hướng dẫn của Nigel Hitchin và Michael Atiyah), **Simon Donaldson** công bố bài báo *"An application of gauge theory to four-dimensional topology"* (*J. Differential Geom.* 18, 1983) với một định lý làm Michael Atiyah phải thốt lên rằng nó *"làm sững sờ cả thế giới toán học"*:

> **Định lý Donaldson (1983).** Nếu $$X$$ là một đa tạp bốn chiều đóng, định hướng, **trơn**, đơn liên và có dạng giao **xác định** (dương hoặc âm), thì dạng giao $$Q_X$$ bắt buộc phải **chéo hóa được trên $$\mathbb{Z}$$**, tức tương đương với $$\langle \pm 1 \rangle \oplus \cdots \oplus \langle \pm 1 \rangle$$.

(Sau đó, năm 1987, Donaldson còn gỡ bỏ luôn cả giả thiết đơn liên!)

Hãy xem **hai hệ quả chấn động** lập tức nổ ra khi định lý Donaldson va chạm trực diện với định lý Freedman:

**Hệ quả 1: Đa tạp 4 chiều tôpô hoàn toàn không thể làm trơn.** Theo Freedman, tồn tại một đa tạp 4 chiều tôpô đóng, đơn liên có dạng giao đúng bằng lưới $$E_8$$ (một dạng xác định dương nhưng *không* chéo hóa được trên $$\mathbb{Z}$$). Theo Donaldson, đa tạp $$E_8$$ đó **không thể mang bất kỳ cấu trúc trơn nào**! (Thậm chí đa tạp $$E_8 \oplus E_8$$ thỏa luôn cả định lý Rokhlin về chỉ số chia hết cho 16, nhưng vẫn bị định lý Donaldson cấm tuyệt đối!)

**Hệ quả 2: Các cấu trúc trơn ngoại lai trên $$\mathbb{R}^4$$ (Exotic $$\mathbb{R}^4$$).** Nếu đặt sự va chạm Freedman–Donaldson vào một đa tạp mở thay vì đa tạp đóng (bằng cách dùng mặt K3 trơn vốn có dạng giao $$2(-E_8) \oplus 3H$$ và khéo léo cắt bỏ một phần bằng kỹ thuật tôpô của Freedman), ta thu được một đa tạp 4 chiều mở **đồng phôi với $$\mathbb{R}^4$$**, nhưng **chứa một tập compact $$K$$ không thể bao trọn bởi bất kỳ mặt cầu 3 chiều $$S^3$$ nhúng trơn nào** (nếu bao được, ta có thể đóng nó lại thành một đa tạp trơn có dạng giao $$-E_8 \oplus (-E_8)$$, trái với định lý Donaldson!). Do đó nó **không thể vi phôi với $$\mathbb{R}^4$$ chuẩn**! Ngay trong cùng tập tạp chí năm 1983, Robert Gompf công bố ba $$\mathbb{R}^4$$ lạ tường minh; về sau Gompf, Taubes và nhiều người khác chứng minh tồn tại **không đếm được** các cấu trúc trơn đôi một không vi phôi ngay trên không gian Euclid 4 chiều thân quen!

---

## 4. Instanton như một công cụ tôpô và nền tảng giải tích của Uhlenbeck

Làm thế nào mà một phương trình vật lý ($$F_A^+ = 0$$) lại ép được một ma trận nguyên phải chéo hóa? Chứng minh của Donaldson đẹp như một kiệt tác điêu khắc hình học:

Cho phân thớ chính $$\mathrm{SU}(2)$$ trên đa tạp trơn 4 chiều $$X$$ có dạng giao xác định dương (và số instanton $$k = 1$$). Xét **không gian moduli** $$\mathcal{M}$$ tất cả các nghiệm instanton (liên thông thỏa $$F_A^+ = 0$$, cực tiểu hóa năng lượng Yang–Mills $$\mathrm{YM}(A) = \int_X \lvert F_A \rvert^2$$) lấy thương theo nhóm biến đổi gauge.
1. **Chiều của không gian moduli:** Theo định lý chỉ số Atiyah–Singer, $$\mathcal{M}$$ là một đa tạp **5 chiều** trơn (trừ một số hữu hạn điểm kỳ dị dạng nón trên $$\mathbb{CP}^2$$, tương ứng chính xác với số cặp vector $$\pm \alpha$$ trong $$H_2(X;\mathbb{Z})$$ có tự giao $$\alpha \cdot \alpha = 1$$!).
2. **Biên sủi bọt (Bubbling) tái hiện chính $$X$$:** Khi năng lượng của một instanton tập trung dồn vào đúng một điểm $$x \in X$$ với bán kính thu về $$0$$ (hiện tượng **sủi bọt** — giống hệt không gian moduli instanton trên $$S^4$$ là một quả cầu đặc 5 chiều có biên là chính $$S^4$$!), phần biên ở vô cực của $$\mathcal{M}$$ chính là một bản sao nguyên vẹn của đa tạp **$$X$$**!
3. **Nền tảng giải tích của Karen Uhlenbeck:** Nhờ **định lý compact của Uhlenbeck** và **định lý kỳ dị khử được** (xem [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)), ta đảm bảo được rằng sủi bọt tại một điểm là kiểu suy biến duy nhất có thể xảy ra, giúp compact hóa $$\mathcal{M}$$ thành một **cobordism 5 chiều** nối liền $$X$$ với tổng rời của các $$\mathbb{CP}^2$$ (từ các điểm kỳ dị nón)!
4. **Cú chốt tôpô:** Vì hai đa tạp cobordant có cùng chỉ số (signature), nên số điểm kỳ dị nón (số lớp có tự giao $$+1$$) phải đủ lớn để sinh ra toàn bộ hạng của $$Q_X$$ — buộc dạng giao $$Q_X$$ phải là ma trận đơn vị chéo hóa!

Sau đó, Donaldson tiếp tục khai thác không gian moduli instanton bậc cao để định nghĩa các **đa thức Donaldson** (*Topology* 29, 1990) — phân biệt được vô số cấu trúc trơn khác nhau trên cùng một đa tạp 4 chiều tôpô đóng (như các mặt Dolgachev).

---

## 5. Những phát triển về sau, không thuộc huy chương 1986

Năm 1994, **Edward Witten** (dựa trên công trình vật lý của Nathan Seiberg và Witten về lý thuyết gauge siêu đối xứng $$\mathcal{N}=2$$) giới thiệu **phương trình monopole Seiberg–Witten**. Vì nhóm gauge là nhóm giao hoán $$\mathrm{U}(1)$$ thay vì $$\mathrm{SU}(2)$$, không gian moduli Seiberg–Witten tự động compact (không còn hiện tượng sủi bọt!) và dễ tính toán hơn đa thức Donaldson gấp nhiều lần — lập tức cho chứng minh ngắn gọn lại định lý Donaldson cùng vô số kết quả mới (như giả thuyết Thom của Kronheimer–Mrowka). Cần nhớ rõ: Seiberg–Witten là cuộc cách mạng tiếp nối năm **1994**, không thuộc Huy chương Fields **1986**.

Các công trình lừng danh khác sau này của Donaldson (định lý Donaldson–Uhlenbeck–Yau về metric Hermite–Einstein, chùm Lefschetz symplectic, hay định lý Chen–Donaldson–Sun về metric Kähler–Einstein trên đa tạp Fano) cũng là những chương kế tiếp của sự nghiệp đồ sộ của ông. Tại ICM Berkeley 1986, ba tấm Huy chương Fields thuộc về **Simon Donaldson** (đa tạp 4 chiều trơn qua lý thuyết gauge), **Michael Freedman** (đa tạp 4 chiều tôpô) và **Gerd Faltings** (giả thuyết Mordell trong hình học số học) — một trong những kỳ đại hội rực rỡ nhất lịch sử toán học.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Donaldson phân loại mọi đa tạp bốn chiều." | Ông chứng minh các ràng buộc nền tảng và đưa ra các bất biến về sau. Phân loại trong phạm trù trơn vẫn còn mở. |
| "Một mình Donaldson xây dựng $$\mathbb{R}^4$$ lạ." | Sự tồn tại dùng **ràng buộc trơn của Donaldson** cùng **lý thuyết tôpô của Freedman** (và các xây dựng sớm của Gompf và những người khác). |
| "Giả thuyết Poincaré của Freedman là phiên bản trơn." | Freedman chứng minh giả thuyết Poincaré bốn chiều **tôpô**. Giả thuyết Poincaré bốn chiều trơn vẫn còn mở. |
| "Seiberg–Witten thuộc huy chương 1986." | Các bất biến Seiberg–Witten xuất hiện năm **1994**. |
| "Định lý compact của Uhlenbeck là một định lý tôpô." | Đó là định lý **giải tích** về tính compact và kỳ dị khử được, rồi được dùng cho tôpô. |
| "$$\mathbb{R}^4$$ lạ mâu thuẫn với tính duy nhất của $$\mathbb{R}^n$$ khi $$n\neq 4$$." | Với $$n\neq 4$$, không gian Euclid có cấu trúc trơn duy nhất; chiều bốn là ngoại lệ. |

---

## Liên kết

- IMU Fields Medals 1986: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)
- Wikipedia: [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson); [Exotic $$\mathbb{R}^4$$](https://en.wikipedia.org/wiki/Exotic_R4); [Donaldson’s theorem](https://en.wikipedia.org/wiki/Donaldson%27s_theorem)
- Khóa học: [Uhlenbeck / gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)
- Tìm arXiv (công trình Donaldson sau; các bài 1983 trước arXiv): [Donaldson four-manifold](https://arxiv.org/search/?query=Donaldson+four-manifold+instanton&searchtype=all)

---

## Tài liệu tham khảo

1. International Mathematical Union, tường thuật Fields Medals 1986 về Simon K. Donaldson (trang Albers–Alexanderson–Reid / IMU).
2. **S. K. Donaldson**, “An application of gauge theory to four-dimensional topology,” *J. Differential Geom.* 18 (1983), 279–315.
3. **M. H. Freedman**, “The topology of four-dimensional manifolds,” *J. Differential Geom.* 17 (1982), 357–453.
4. **R. Gompf**, “Three exotic $$\mathbf{R}^4$$’s and other anomalies,” *J. Differential Geom.* 18 (1983), 317–328.
5. **S. K. Donaldson and P. B. Kronheimer**, *The Geometry of Four-Manifolds*, Oxford, 1990.
6. **D. S. Freed and K. K. Uhlenbeck**, *Instantons and Four-Manifolds*, Springer, 1984; bài khóa học [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/).
7. **E. Witten**, “Monopoles and four-manifolds,” *Math. Res. Lett.* 1 (1994), 769–796. (Hậu duệ, không phải huy chương 1986.)
8. Wikipedia, [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson), [Exotic R4](https://en.wikipedia.org/wiki/Exotic_R4).

---

## Hướng đi tiếp

- Đọc bài giới thiệu của Atiyah tại ICM 1986, rồi Chương 1 sách Donaldson–Kronheimer. Sau khi đọc bài Uhlenbeck, ghi lại vì sao hiện tượng sủi bọt là một tính năng chứ không phải lỗi (nó sinh ra $$\partial\mathcal{M}$$).
- Câu hỏi thảo luận: để phân loại các đa tạp bốn chiều trơn đơn liên, ngoài dạng giao ta còn cần gì?

## Video tham khảo

- **Xem trước**: [Simon Donaldson, Invariants of manifolds and the classification problem](https://www.youtube.com/watch?v=IO0HNEs8oxQ) (Clay Mathematics Institute, tiếng Anh). Donaldson nói về các bất biến của đa tạp và bài toán phân loại. Nên xem trước để hiểu vì sao chiều bốn đặc biệt.
- [The Shaw Prize Lecture in Mathematical Sciences 2009 - by Professor Simon K Donaldson](https://www.youtube.com/watch?v=5yhxUCtNRQE) (The Shaw Prize, tiếng Anh). Bài giảng của Donaldson khi nhận Giải Shaw 2009. Xem sau khi đọc xong mục 3 và 4.
- [Overview of gauge theory and submanifold geometry on G_2 manifolds - Simon Donaldson (2014)](https://www.youtube.com/watch?v=xIqLhsrgcBI) (Graduate Mathematics, tiếng Anh). Bài giảng tổng quan về lý thuyết gauge và đa tạp con trên đa tạp G_2, một hướng nghiên cứu về sau của Donaldson. Dùng làm góc nhìn bổ sung, không thuộc huy chương 1986.
