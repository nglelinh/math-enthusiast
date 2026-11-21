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

**Simon Donaldson** nhận **Huy chương Fields 1986**. Theo tường thuật chuẩn của IMU, ông được trao huy chương

> primarily for his work on the topology of four-manifolds, especially for showing that there is a differential structure on Euclidean four-space which is different from the usual structure.  
> — [IMU, Fields Medals 1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)

*Tạm dịch: chủ yếu vì công trình về tôpô của các đa tạp bốn chiều, đặc biệt là việc chỉ ra rằng có một cấu trúc vi phân trên không gian Euclid bốn chiều khác với cấu trúc thông thường.*

(Trang IMU về năm 1986 trích lại cuốn lịch sử các đại hội của Albers–Alexanderson–Reid.) Câu này đúng ở mức tiêu đề, nhưng chưa đủ để ghi công cho chứng minh. **Các cấu trúc trơn lạ (exotic) trên $$\mathbb{R}^4$$**, tức các đa tạp đồng phôi với không gian Euclid bốn chiều nhưng không vi phôi với nó, xuất hiện từ sự va chạm giữa hai định lý năm 1982–83: phân loại tôpô các đa tạp bốn chiều đơn liên của Michael Freedman, và các ràng buộc từ lý thuyết gauge của Donaldson đối với dạng giao của đa tạp **trơn**. Freedman cũng nhận Huy chương Fields tại cùng đại hội Berkeley, vì các phương pháp tôpô của ông, trong đó có chứng minh giả thuyết Poincaré bốn chiều trong phạm trù tôpô. Bài này xem hai kết quả đó như một sự kiện năm 1986 với hai động lực.

Động lực từ phía Donaldson là **lý thuyết gauge Yang–Mills**: các liên thông phản tự đối ngẫu (instanton) và tôpô của không gian moduli của chúng. Nền tảng giải tích giúp các không gian moduli này dùng được (tính compact, hiện tượng "sủi bọt" (bubbling), định lý kỳ dị khử được) phần lớn là công của Karen Uhlenbeck; xem [Uhlenbeck / lý thuyết gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/). **Lý thuyết Seiberg–Witten** (Witten, 1994) là một công cụ gauge khác, đến sau, đã làm đơn giản nhiều lập luận về đa tạp bốn chiều; đó là sự phát triển tiếp theo, không thuộc huy chương năm 1986. Khóa học chưa có bài riêng về Seiberg–Witten; bối cảnh vật lý toán xung quanh được phác họa trong [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/). Donaldson **không** phân loại mọi đa tạp bốn chiều.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao chiều bốn đặc biệt: mẹo Whitney và lý thuyết phẫu thuật cho chiều cao không dùng được, còn các phương pháp cắt dán của chiều thấp thì không đủ mạnh.
- Định nghĩa **dạng giao** của một đa tạp bốn chiều đóng, định hướng, như một dạng song tuyến trên $$H_2$$ (hoặc $$H^2$$), cho bởi số giao đại số (hoặc tích cup).
- Phát biểu **định lý Donaldson** (1983): dạng giao xác định của một đa tạp bốn chiều trơn, đóng, định hướng thì chéo hóa được trên $$\mathbb{Z}$$ (ban đầu với giả thiết đơn liên; về sau được mở rộng).
- So sánh với **Freedman**: mọi dạng song tuyến đối xứng unimodular đều là dạng giao của một đa tạp bốn chiều **tôpô** đơn liên, và các đa tạp này được phân loại bởi dạng giao cộng thêm một bất biến Kirby–Siebenmann (một bit) trong trường hợp dạng lẻ.
- Giải thích ngắn gọn vì sao sự va chạm này sinh ra (i) các đa tạp bốn chiều tôpô **không có cấu trúc trơn** và (ii) các **$$\mathbb{R}^4$$ lạ**.
- Mô tả không gian moduli instanton như nguồn hình học của các ràng buộc Donaldson, và gọi định lý compact của Uhlenbeck là nền tảng giải tích.
- Đặt lý thuyết Seiberg–Witten (1994) là sự phát triển về sau, không phải công trình năm 1986.
- Tránh câu "Donaldson đã phân loại mọi đa tạp bốn chiều".

**Kiến thức nền.** Đa tạp trơn, đồng điều và tích cup ở mức giáo trình tôpô đại số nhập môn; khái niệm phân thớ vectơ và liên thông. Không cần học trước lý thuyết gauge: có thể hiểu liên thông là một cách lấy đạo hàm các nhát cắt, và độ cong đo mức độ các đạo hàm riêng hỗn hợp không giao hoán.

**Liên kết với các bài khác.** Bài này cho thấy phương trình đạo hàm riêng có nguồn gốc vật lý trở thành công cụ tôpô, và sự khác nhau giữa phạm trù tôpô với phạm trù trơn. Đọc cùng [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) (cách tiếp cận giải tích – hình học cho đa tạp ba chiều về sau), và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## 1. Vì sao chiều bốn không chỉ là "thêm một giá trị của $$n$$"

Với $$n\ge 5$$, các định lý phẫu thuật cho chiều cao và định lý $$h$$-cobordism (Smale, và công trình tôpô của Kirby–Siebenmann) cho ta một bộ máy phân loại: kiểu đồng luân, cộng thêm một ít $$K$$-lý thuyết đại số và vật cản phẫu thuật, gần như xác định đa tạp trong một phạm trù cho trước. Với $$n\le 3$$, giả thuyết hình học hóa và các phương pháp cắt dán cổ điển chiếm ưu thế. Chiều bốn là vùng còn lại. Mẹo Whitney cần đủ chỗ để triệt tiêu các điểm giao, và nó không dùng được trong phạm trù trơn ở chiều bốn; các "tay cầm Casson" (Casson handle) và các đĩa nhúng hoang dại xuất hiện; và phạm trù trơn với phạm trù tôpô **tách rời nhau**.

Bất biến đại số cơ bản của một đa tạp bốn chiều đóng, định hướng $$X$$ là **dạng giao**

$$
Q_X: H_2(X;\mathbb{Z})/\mathrm{torsion}\times H_2(X;\mathbb{Z})/\mathrm{torsion}\to\mathbb{Z},
$$

một dạng song tuyến đối xứng cho bởi số giao đại số của các mặt (tương đương: tích cup trên $$H^2$$ rồi lấy giá trị trên lớp cơ bản). Theo đối ngẫu Poincaré, dạng này unimodular. Trên $$\mathbb{R}$$, nó được phân loại bởi hạng và chỉ số (signature); trên $$\mathbb{Z}$$ thì có nhiều lớp đẳng cấu hơn (lưới $$E_8$$ là ví dụ tiêu biểu của một dạng chẵn, xác định, không chéo hóa được).

Định lý Rokhlin đã ràng buộc các đa tạp bốn chiều spin **trơn** (chỉ số chia hết cho $$16$$). Freedman và Donaldson, mỗi người theo một hướng, biến dạng giao nguyên thành gần như một phân loại tôpô đầy đủ, và thành một vật cản chặt chẽ cho cấu trúc trơn.

---

## 2. Freedman: đa tạp bốn chiều tôpô

Michael Freedman, trong bài "The topology of four-dimensional manifolds", *J. Differential Geom.* 17 (1982), chứng minh rằng mọi dạng song tuyến đối xứng unimodular đều là dạng giao của một đa tạp bốn chiều **tôpô** đóng, đơn liên. Trong trường hợp dạng chẵn, dạng giao xác định đa tạp sai khác đồng phôi; trong trường hợp dạng lẻ có đúng hai lớp đồng phôi, phân biệt bởi bất biến Kirby–Siebenmann trong $$\mathbb{Z}/2$$. Hệ quả là ông chứng minh **giả thuyết Poincaré bốn chiều trong phạm trù tôpô**: mọi đa tạp đồng luân với mặt cầu bốn chiều đều đồng phôi với $$S^4$$.

Các cách xây dựng dùng tay cầm Casson, những tháp vô hạn mà về tôpô là bình thường nhưng về trơn thì nói chung là lạ. Vì vậy thế giới tôpô của Freedman rộng hơn thế giới trơn: nhiều dạng giao xuất hiện được về mặt tôpô nhưng không thể xuất hiện trên đa tạp trơn.

---

## 3. Định lý Donaldson: dạng xác định trên đa tạp trơn

Kết quả gây chấn động đầu tiên của Donaldson, khi ông còn là nghiên cứu sinh ở Oxford (với Hitchin, rồi Atiyah), là định lý năm 1983:

> Nếu $$X$$ là đa tạp bốn chiều đóng, định hướng, trơn, đơn liên và có dạng giao xác định, thì dạng đó chéo hóa được trên các số nguyên, tức là tương đương với $$\langle\pm 1\rangle\oplus\cdots\oplus\langle\pm 1\rangle$$.

Bài báo là "An application of gauge theory to four-dimensional topology", *J. Differential Geom.* 18 (1983), 279–315; thông báo ngắn là "Self-dual connections and the topology of smooth 4-manifolds", *Bull. Amer. Math. Soc.* 8 (1983). Trong bài giới thiệu tại ICM, Atiyah có câu nổi tiếng rằng công trình này "stunned the mathematical world" (làm cả giới toán học sửng sốt). Các bài sau (trong đó có bài trên *J. Differential Geom.* 26 (1987) về tính định hướng của không gian moduli) bỏ được giả thiết đơn liên, cho dạng định lý dùng ngày nay.

Kết hợp với Freedman, định lý lập tức cho ta **các đa tạp bốn chiều tôpô không có cấu trúc trơn**: lấy đa tạp tôpô đơn liên có dạng giao $$E_8$$ (hoặc $$E_8\oplus E_8$$). Nó tồn tại về mặt tôpô, nhưng không thể có bất kỳ cấu trúc trơn nào, vì $$E_8$$ xác định mà không chéo hóa được.

Cũng sự va chạm đó, khi đặt ở các "đầu" của một đa tạp bốn chiều mở thay vì trên đa tạp đóng, sinh ra **các $$\mathbb{R}^4$$ lạ**. Các phép nhúng tôpô và định lý $$h$$-cobordism riêng (proper) của Freedman cho phép "vá" các mảnh trong phạm trù tôpô; còn các ràng buộc của Donaldson cấm đa tạp mở thu được vi phôi với $$\mathbb{R}^4$$ chuẩn (ví dụ, nó có thể chứa một tập compact không nằm trong bất kỳ mặt cầu $$S^3$$ nhúng trơn nào). Những ví dụ tường minh đầu tiên xuất hiện ngay trong cùng tập năm 1983 của *Journal of Differential Geometry* (Gompf, "Three exotic $$\mathbf{R}^4$$’s and other anomalies"). Các công trình sau của Gompf, Taubes và những người khác cho thấy có vô hạn, thực ra là không đếm được, cấu trúc trơn đôi một không vi phôi trên không gian bốn chiều tôpô. Câu tiêu đề của IMU, rằng Donaldson chỉ ra có một cấu trúc vi phân không chuẩn trên không gian Euclid bốn chiều, là cách gọi phổ biến của hiện tượng **Donaldson + Freedman** này. Nó không có nghĩa là bản thân một không gian moduli instanton là một $$\mathbb{R}^4$$ lạ.

---

## 4. Instanton như một công cụ tôpô

Cho $$P\to X$$ là một phân thớ chính với nhóm $$\mathrm{SU}(2)$$ (hoặc $$\mathrm{SO}(3)$$). Một liên thông $$A$$ có độ cong $$F_A$$. Ở chiều bốn, toán tử sao Hodge biến 2-dạng thành 2-dạng, nên có thể đặt phương trình **phản tự đối ngẫu** (ASD) $$F_A^+=0$$ (hoặc phương trình tự đối ngẫu). Các nghiệm có năng lượng Yang–Mills hữu hạn

$$
\mathrm{YM}(A)=\int_X \lvert F_A\rvert^2
$$

được gọi là **instanton**. Không gian các liên thông đó, sau khi lấy thương theo phép biến đổi gauge, là một **không gian moduli** $$\mathcal{M}$$. Với đa tạp bốn chiều có dạng giao xác định và phân thớ thích hợp, Donaldson chỉ ra rằng $$\mathcal{M}$$ có thể compact hóa thành một đa tạp có biên (hay một không gian phân tầng), trong đó biên có chứa một bản sao của $$X$$. Phần biên này ứng với các instanton có năng lượng tập trung ("sủi bọt") tại một điểm, giống như mô hình không gian moduli instanton trên $$S^4$$: một quả cầu đặc năm chiều với $$S^4$$ ở vô cùng. Ràng buộc tôpô đó trên $$\mathcal{M}$$ buộc dạng giao phải chéo hóa được: không thể có một dạng xác định không chuẩn.

**Định lý compact của Uhlenbeck** và **định lý kỳ dị khử được** giúp $$\mathcal{M}$$ dùng được: các dãy có năng lượng bị chặn hội tụ trơn bên ngoài hữu hạn điểm, và các kỳ dị cô lập có năng lượng nhỏ khử được. Xem [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/). Donaldson dùng không gian moduli đã compact hóa như một cobordism giữa $$X$$ và một mô hình đơn giản; Uhlenbeck bảo đảm cho việc compact hóa. Cuốn *Instantons and Four-Manifolds* (1984) của Freed–Uhlenbeck là giáo trình của thế hệ đầu tiên. Các đa thức Donaldson về sau (*Topology* 29 (1990)) phân biệt được các cấu trúc trơn khác nhau trên cùng một đa tạp bốn chiều tôpô; đó là phần tiếp nối, và vẫn chưa phải phân loại mọi đa tạp bốn chiều.

---

## 5. Những phát triển về sau, không thuộc huy chương

Năm 1994, Witten đưa ra các phương trình monopole **Seiberg–Witten**, xuất phát từ lý thuyết gauge siêu đối xứng $$N=2$$ ("Monopoles and four-manifolds", *Math. Res. Lett.* 1 (1994)). Chúng thường dễ tính toán hơn đa thức Donaldson. Hãy nhắc tới chúng như công cụ tiếp theo, không phải công trình năm 1986. Các công trình sau này của Donaldson về metric Hermite–Einstein (định lý DUY), về chùm Lefschetz trên đa tạp symplectic, và định lý Chen–Donaldson–Sun về metric Kähler–Einstein trên đa tạp Fano là những chương khác. Huy chương năm 1986 là về tôpô đa tạp bốn chiều thông qua phương trình Yang–Mills phản tự đối ngẫu.

Người ta đã dự đoán chiều bốn là khó. Nhưng không ai ngờ rằng giải tích Yang–Mills lại buộc "xác định thì chéo hóa được", và rằng sự linh hoạt tôpô của Freedman khi kết hợp với nó lại cho ra các đa tạp không có cấu trúc trơn và các $$\mathbb{R}^4$$ lạ. Những người nhận huy chương năm 1986 là Donaldson, Faltings (giả thuyết Mordell) và Freedman: hình học đại số số học; đa tạp bốn chiều tôpô; đa tạp bốn chiều trơn qua lý thuyết gauge.

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

## Bài tập

1. Một dạng song tuyến trên $$\mathbb{Z}$$ là **unimodular** nghĩa là gì? Vì sao đối ngẫu Poincaré cho ta tính chất đó với $$Q_X$$?
2. Phát biểu định lý về dạng xác định của Donaldson và định lý thực hiện của Freedman. Từ đó suy ra, trong ba câu, rằng đa tạp tôpô có dạng giao $$E_8$$ không có cấu trúc trơn.
3. Vì sao "đồng phôi nhưng không vi phôi với $$\mathbb{R}^4$$" chỉ chứng minh được khi có **cả** sự linh hoạt tôpô lẫn sự cứng nhắc của phạm trù trơn?
4. Mô tả không gian moduli instanton trong một đoạn: phương trình ASD, thương theo gauge, hiện tượng sủi bọt tại điểm, compact hóa chứa $$X$$. Ta rút ra kết luận tôpô nào cho $$X$$ có dạng giao xác định?
5. Luyện ghi công: viết một mệnh đề chính xác cho mỗi người: **Donaldson**, **Freedman**, **Uhlenbeck**, **Witten (1994)**.
6. Giả thuyết Poincaré bốn chiều trơn vẫn còn mở. Nó khác định lý của Freedman ở điểm nào?
7. **Luyện phát biểu chính xác.** Viết lại câu "Donaldson tìm ra một $$\mathbb{R}^4$$ trơn kỳ lạ bằng cách giải Yang–Mills" thành hai câu đúng, phù hợp với khóa học.
8. **Thảo luận.** So sánh câu chuyện lý thuyết gauge năm 1986 với [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/): dòng Ricci ở chiều ba và instanton ở chiều bốn. Trong mỗi câu chuyện, đối tượng nào được compact hóa hoặc bị suy biến?

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
