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

**Simon Donaldson** nhận **Huy chương Fields 1986**, theo tường thuật IMU chuẩn,

> primarily for his work on the topology of four-manifolds, especially for showing that there is a differential structure on Euclidean four-space which is different from the usual structure.  
> — [IMU, Fields Medals 1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)

(Trang IMU 1986 tái bản lịch sử đại hội Albers–Alexanderson–Reid.) Câu đúng như tiêu đề và chưa đủ như ghi công chứng minh. **Các cấu trúc trơn ngoại lai trên $$\mathbb{R}^4$$**—các đa tạp đồng phôi với không gian Euclid bốn chiều nhưng không vi phôi với nó—phát sinh từ xung đột giữa hai định lý 1982–83: phân loại tôpô các đa tạp bốn chiều đơn liên của Michael Freedman, và các ràng buộc lý thuyết gauge của Donaldson lên dạng giao **trơn**. Freedman nhận Huy chương Fields tại cùng đại hội Berkeley, vì các phương pháp tôpô gồm giả thuyết Poincaré bốn chiều trong phạm trù tôpô. Bài này coi cặp đó như một sự kiện 1986 với hai động cơ.

Động cơ phía Donaldson là **lý thuyết gauge Yang–Mills**: liên kết phản tự đối ngẫu (instanton) và tôpô các không gian moduli của chúng. Hạ tầng giải tích làm các không gian moduli dùng được—compact, bubbling, kỳ dị loại được—mang nợ trung tâm với Karen Uhlenbeck; xem [Uhlenbeck / lý thuyết gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/). **Lý thuyết Seiberg–Witten** (Witten, 1994) là động cơ gauge khác, sau đó, đã đơn giản hóa nhiều lập luận đa tạp bốn chiều; đó là hậu duệ, không phải phần huy chương 1986. Không có bài “Donaldson–Seiberg–Witten” riêng trong Chương 6 của khóa học này; văn hóa vật lý toán xung quanh được phác trong [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/). Donaldson **không** phân loại mọi đa tạp bốn chiều.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao chiều bốn đặc biệt: mánh Whitney và phẫu thuật chiều cao thất bại, trong khi cắt–dán chiều thấp không đủ.
- Định nghĩa **dạng giao** của đa tạp bốn chiều đóng, định hướng như cặp trên $$H_2$$ (hoặc $$H^2$$) cho bởi giao đại số (hoặc tích cup).
- Nêu **định lý Donaldson** (1983): dạng giao xác định của một đa tạp bốn chiều trơn, đóng, định hướng là chéo hóa được trên $$\mathbb{Z}$$ (ban đầu dưới giả thuyết đơn liên; sau được mở rộng).
- Đối chiếu với **Freedman**: mọi dạng song tuyến đối xứng unimodular được thực hiện bởi một đa tạp bốn chiều **tôpô** đơn liên, và các đa tạp đó được phân loại bởi dạng cộng một bit Kirby–Siebenmann trong trường hợp lẻ.
- Giải thích, ở mức khẩu hiệu, xung đột sinh ra (i) đa tạp bốn chiều tôpô **không có cấu trúc trơn** và (ii) **$$\mathbb{R}^4$$ ngoại lai**.
- Mô tả không gian moduli instanton như nguồn hình học của các ràng buộc Donaldson, và gọi compact Uhlenbeck là hạ tầng giải tích.
- Đặt Seiberg–Witten (1994) như hậu duệ sau, không phải công trình 1986.
- Tránh câu “Donaldson phân loại mọi đa tạp bốn chiều.”

**Kiến thức nền.** Đa tạp trơn, đồng điều và tích cup ở mức khóa tôpô đại số thứ nhất; ý tưởng bundle véctơ và liên kết. Không giả định khóa lý thuyết gauge: coi liên kết như cách lấy đạo hàm các lát, và độ cong như sự thất bại của đạo hàm riêng hỗn hợp giao hoán.

**Liên kết seminar.** LO1 / LO4 (PDE lấy cảm hứng vật lý như máy tôpô; phạm trù tôpô versus trơn). Ghép [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) cho tấn công giải tích–hình học sau này lên đa tạp ba chiều, và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## 1. Vì sao chiều bốn không phải “chỉ thêm một $$n$$”

Với $$n\ge 5$$, các định lý phẫu thuật chiều cao và $$h$$-cobordism (Smale, và công trình tôpô của Kirby–Siebenmann) cho một máy phân loại: kiểu đồng luân cộng một ít $$K$$-lý thuyết đại số và cản phẫu thuật phần lớn xác định đa tạp trong một phạm trù cho trước. Với $$n\le 3$$, geometrization và cắt–dán cổ điển thống trị. Chiều bốn là chiến trường còn lại. Mánh Whitney, cần chỗ để triệt giao, thất bại trong phạm trù trơn ở chiều bốn; Casson handle và đĩa nhúng hoang xuất hiện; và các phạm trù trơn và tôpô **tách nhau**.

Bất biến đại số cơ bản của một đa tạp bốn chiều đóng định hướng $$X$$ là **dạng giao**

$$
Q_X: H_2(X;\mathbb{Z})/\mathrm{torsion}\times H_2(X;\mathbb{Z})/\mathrm{torsion}\to\mathbb{Z},
$$

dạng song tuyến đối xứng unimodular cho bởi giao đại số các mặt (tương đương, tích cup trên $$H^2$$ tính trên lớp cơ bản). Theo đối ngẫu Poincaré dạng là unimodular. Trên $$\mathbb{R}$$ nó được phân loại bởi hạng và signature; trên $$\mathbb{Z}$$ có nhiều kiểu đẳng cấu hơn (lattice $$E_8$$ là ví dụ chẵn, xác định, không chéo hóa được mang tính biểu tượng).

Định lý Rohlin đã ràng buộc các đa tạp bốn chiều spin **trơn** (signature chia hết cho $$16$$). Freedman và Donaldson lần lượt biến dạng nguyên thành phân loại tôpô gần đầy đủ và một cản trơn nghiêm ngặt.

---

## 2. Freedman: đa tạp bốn chiều tôpô

Michael Freedman, “The topology of four-dimensional manifolds,” *J. Differential Geom.* 17 (1982), chứng minh mọi dạng song tuyến đối xứng unimodular được thực hiện như dạng giao của một đa tạp bốn chiều **tôpô** đóng đơn liên, và trong trường hợp chẵn dạng xác định kiểu đồng phôi; trong trường hợp lẻ có hai kiểu đồng phôi, phân biệt bởi bất biến Kirby–Siebenmann trong $$\mathbb{Z}/2$$. Hệ quả, ông chứng minh **giả thuyết Poincaré bốn chiều trong phạm trù tôpô**: một bốn-cầu đồng luân đồng phôi với $$S^4$$.

Các xây dựng dùng Casson handle—các tháp vô hạn chuẩn về tôpô nhưng ngoại lai về trơn nói chung. Thế giới của Freedman vì thế lớn hơn thế giới trơn: nhiều dạng xuất hiện về tôpô mà không thể xuất hiện về trơn.

---

## 3. Định lý Donaldson: dạng xác định, về trơn

Cú sốc đầu của Donaldson, đạt được khi ông còn là nghiên cứu sinh ở Oxford (Hitchin, rồi Atiyah), là định lý 1983:

> Nếu $$X$$ là đa tạp bốn chiều đóng, định hướng, trơn, đơn liên có dạng giao xác định, thì dạng đó chéo hóa được trên các số nguyên: tương đương $$\langle\pm 1\rangle\oplus\cdots\oplus\langle\pm 1\rangle$$.

Bài báo là “An application of gauge theory to four-dimensional topology,” *J. Differential Geom.* 18 (1983), 279–315; thông báo ngắn là “Self-dual connections and the topology of smooth 4-manifolds,” *Bull. Amer. Math. Soc.* 8 (1983). Tường thuật ICM của Atiyah nổi tiếng nói công trình “stunned the mathematical world.” Các bài sau (gồm *J. Differential Geom.* 26 (1987) về định hướng không gian moduli) bỏ giả thuyết đơn liên trong dạng dùng ngày nay.

Kết hợp với Freedman, định lý tức thì sinh **đa tạp bốn chiều tôpô không làm trơn được**: lấy đa tạp tôpô đơn liên có dạng giao $$E_8$$ (hoặc $$E_8\oplus E_8$$). Nó tồn tại về tôpô và không thể nhận bất kỳ cấu trúc trơn nào, vì $$E_8$$ xác định và không chéo hóa được.

Cùng xung đột, sắp xếp ở các đầu của đa tạp bốn chiều mở chứ không trên đa tạp đóng, sinh **$$\mathbb{R}^4$$ ngoại lai**. Các nhúng tôpô và $$h$$-cobordism proper của Freedman cho phép bịt các mảnh trong phạm trù tôpô; các ràng buộc của Donaldson cấm đa tạp bốn chiều mở thu được vi phôi với $$\mathbb{R}^4$$ chuẩn (ví dụ, nó có thể chứa một tập compact không bị bao bởi bất kỳ $$S^3$$ nhúng trơn nào). Các xây dựng sớm tường minh xuất hiện trong cùng tập 1983 của *Journal of Differential Geometry* (Gompf, “Three exotic $$\mathbf{R}^4$$’s and other anomalies”). Công trình sau của Gompf, Taubes, và những người khác sinh vô hạn—thực sự không đếm được—cấu trúc trơn không vi phôi trên không gian bốn chiều tôpô. Tiêu đề IMU rằng Donaldson chỉ ra có cấu trúc vi phân không chuẩn trên không gian Euclid bốn chiều là tên công cộng của hiện tượng **Donaldson + Freedman** này, không phải khẳng định một không gian moduli instanton tự nó là một $$\mathbb{R}^4$$ ngoại lai.

---

## 4. Instanton như công cụ tôpô

Cho $$P\to X$$ là bundle chính $$\mathrm{SU}(2)$$ (hoặc $$\mathrm{SO}(3)$$). Một liên kết $$A$$ có độ cong $$F_A$$. Ở chiều bốn, sao Hodge gửi 2-dạng tới 2-dạng, và người ta có thể đặt phương trình **phản tự đối ngẫu** (ASD) $$F_A^+=0$$ (hoặc phương trình tự đối ngẫu). Các nghiệm năng lượng Yang–Mills hữu hạn

$$
\mathrm{YM}(A)=\int_X \lvert F_A\rvert^2
$$

là **instanton**. Không gian các liên kết đó modulo biến đổi gauge là một **không gian moduli** $$\mathcal{M}$$. Với đa tạp bốn chiều xác định và bundle thích hợp, Donaldson chỉ ra $$\mathcal{M}$$ có thể compact hóa thành đa tạp-với-biên (hoặc không gian phân tầng) có biên chứa một bản sao của $$X$$—năng lượng sủi tại các điểm, theo mô hình không gian moduli instanton trên $$S^4$$, là một năm-cầu với $$S^4$$ ở vô hạn. Ràng buộc tôpô đó trên $$\mathcal{M}$$ buộc dạng giao chéo hóa được: một dạng xác định không chuẩn không thể xảy ra.

**Compact Uhlenbeck** và **kỳ dị loại được** làm $$\mathcal{M}$$ dùng được: các dãy năng lượng bị chặn hội tụ trơn ngoài hữu hạn điểm, và kỳ dị cô lập năng lượng nhỏ được lấp. Xem [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/). Donaldson dùng không gian moduli đã compact hóa như cobordism giữa $$X$$ và một mô hình; Uhlenbeck bảo đảm compact hóa. Freed–Uhlenbeck, *Instantons and Four-Manifolds* (1984), là giáo trình thế hệ đầu. Các đa thức Donaldson sau (*Topology* 29 (1990)) phân biệt cấu trúc trơn trên một đa tạp bốn chiều tôpô cố định; đó là sự tiếp nối, vẫn không phải phân loại mọi đa tạp bốn chiều.

---

## 5. Hậu duệ không thuộc huy chương

Năm 1994 Witten đưa vào các phương trình monopole **Seiberg–Witten** từ lý thuyết gauge siêu đối xứng $$N=2$$ (“Monopoles and four-manifolds,” *Math. Res. Lett.* 1 (1994)), thường dễ tính hơn đa thức Donaldson. Nhắc chúng như động cơ tiếp theo, không phải công trình 1986, và đừng bịa đường dẫn Chương 6 `Donaldson_Seiberg_Witten`. Công trình Hermitian–Einstein / DUY sau này của Donaldson, pencil Lefschetz symplectic, và định lý Kähler–Einstein Chen–Donaldson–Sun cho Fano là chương khác. Huy chương 1986 là tôpô đa tạp bốn chiều qua Yang–Mills ASD.

Chiều bốn được kỳ vọng khó; rằng giải tích Yang–Mills sẽ buộc “xác định kéo theo chéo hóa được,” và rằng sự dư dả tôpô của Freedman rồi sẽ cho đa tạp không làm trơn được và $$\mathbb{R}^4$$ ngoại lai, thì không. Lớp 1986 là Donaldson, Faltings (Mordell), và Freedman: hình học đại số số học; đa tạp bốn chiều tôpô; đa tạp bốn chiều trơn qua lý thuyết gauge.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Donaldson phân loại mọi đa tạp bốn chiều.” | Ông chứng minh các ràng buộc nền và các bất biến sau. Phân loại vẫn mở trong phạm trù trơn. |
| “Donaldson một mình xây $$\mathbb{R}^4$$ ngoại lai.” | Tồn tại dùng **ràng buộc trơn của Donaldson** cùng **lý thuyết tôpô của Freedman** (và các xây dựng sớm của Gompf và những người khác). |
| “Giả thuyết Poincaré của Freedman là giả thuyết trơn.” | Freedman chứng minh giả thuyết Poincaré 4D **tôpô**. Giả thuyết Poincaré 4D trơn vẫn mở. |
| “Seiberg–Witten là huy chương 1986.” | Các bất biến Seiberg–Witten xuất hiện năm **1994**. |
| “Compact Uhlenbeck là định lý tôpô.” | Đó là định lý compact / kỳ dị loại được **giải tích** mà tôpô rồi dùng. |
| “$$\mathbb{R}^4$$ ngoại lai mâu thuẫn tính duy nhất của $$\mathbb{R}^n$$ với $$n\neq 4$$.” | Với $$n\neq 4$$, không gian Euclid có cấu trúc trơn duy nhất; chiều bốn là ngoại lệ. |

---

## Bài tập

1. Dạng song tuyến trên $$\mathbb{Z}$$ **unimodular** nghĩa là gì? Vì sao đối ngẫu Poincaré cho điều đó với $$Q_X$$?
2. Nêu định lý dạng xác định của Donaldson và định lý thực hiện của Freedman. Suy ra, trong ba câu, rằng một đa tạp $$E_8$$ tôpô không làm trơn được.
3. Vì sao “đồng phôi nhưng không vi phôi với $$\mathbb{R}^4$$” chỉ có thể sau khi có **cả** sự linh hoạt tôpô lẫn sự cứng trơn?
4. Moduli instanton trong một đoạn: phương trình ASD, thương gauge, bubbling tại điểm, compact hóa chứa $$X$$. Kết luận tôpô nào được rút cho $$X$$ xác định?
5. Luyện gán công: một mệnh đề chính xác mỗi người cho **Donaldson**, **Freedman**, **Uhlenbeck**, **Witten (1994)**.
6. Giả thuyết Poincaré bốn chiều trơn vẫn mở. Điều đó khác định lý Freedman thế nào?
7. **Luyện độ chính xác.** Viết lại “Donaldson tìm một $$\mathbb{R}^4$$ trơn kỳ lạ bằng cách giải Yang–Mills” thành hai câu khóa học này chấp nhận.
8. **Seminar.** So câu chuyện lý thuyết gauge 1986 này với [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/): Ricci flow ở chiều ba versus instanton ở chiều bốn. Cái gì đang được compact hóa hoặc suy biến trong mỗi câu chuyện?

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

- Đọc laudation ICM 1986 của Atiyah, rồi Chương 1 Donaldson–Kronheimer; sau bài Uhlenbeck, ghi chú vì sao bubbling là đặc trưng (nó sinh $$\partial\mathcal{M}$$).
- Gợi ý seminar: một phân loại các đa tạp bốn chiều trơn đơn liên còn cần gì ngoài dạng giao?
