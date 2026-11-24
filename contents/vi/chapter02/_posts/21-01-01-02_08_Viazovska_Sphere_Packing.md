---
layout: post
title: "Viazovska và Bài toán Xếp cầu (Huy chương Fields 2022)"
chapter: '02'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Nếu bạn đi qua một sạp bán cam, bạn sẽ thấy người bán luôn xếp cam theo từng lớp lục giác chồng so le lên nhau. Năm 1611, Johannes Kepler phỏng đoán rằng đó là cách xếp quả cầu đặc nhất có thể trong không gian 3 chiều — nhưng phải mất gần bốn thế kỷ (tới năm 1998), Thomas Hales mới chứng minh được điều ấy nhờ hàng trăm trang lập luận kết hợp với hàng nghìn giờ tính toán trên máy tính. Thế nên khi các nhà toán học hỏi tiếp: *"Vậy trong không gian 4 chiều, 8 chiều, hay 24 chiều thì xếp cầu thế nào là khít nhất?"*, ai cũng nghĩ bài toán sẽ còn khó gấp bội.

Rồi vào một ngày tháng 3 năm 2016, **Maryna Viazovska** đăng lên arXiv một bài báo chỉ dài hơn 20 trang, tinh tế đến mức khiến cả cộng đồng toán học sững sờ: không cần siêu máy tính kiểm tra hàng nghìn trường hợp, bà chứng minh trọn vẹn rằng lưới đối xứng **$$E_8$$** cho mật độ xếp cầu tối ưu tuyệt đối trong **8 chiều**! Chỉ một tuần sau, cùng bốn cộng sự (Cohn, Kumar, Miller, Radchenko), bà áp dụng cùng ý tưởng đó để giải luôn bài toán trong **24 chiều** với **lưới Leech**. Thành tựu rực rỡ này mang về cho Viazovska **Huy chương Fields 2022**, đưa bà trở thành **người phụ nữ thứ hai** trong lịch sử đoạt giải (sau Maryam Mirzakhani năm 2014).

Điều kỳ diệu nhất của câu chuyện nằm ở cú chuyển ngôn ngữ: thay vì xếp thử vô số quả cầu trong không gian 8 chiều, Viazovska đã dùng **dạng modular** — một công cụ tưởng chỉ sống trong lý thuyết số — để thiết kế một **"hàm kỳ diệu"** trong giải tích Fourier, tự động loại bỏ mọi đối thủ xếp cầu khác chỉ bằng một bất đẳng thức!

Hành trình của bài học này đi qua tám chặng:

**Mật độ xếp → các chiều thấp → các lưới đặc biệt → chặn Cohn–Elkies → hàm "kỳ diệu" → dạng modular → $$E_8$$ và Leech → Fields 2022.**

Mục tiêu không phải là tự tay dựng dạng modular, mà là hiểu **tối ưu nghĩa là gì**, **vì sao chiều 8 và 24 đặc biệt**, và **giải tích Fourier đã biến bài toán xếp cầu thành bài toán thiết kế hàm như thế nào**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa cẩn thận mật độ của một cách xếp (tỉ lệ thể tích bị phủ).
- Nêu sơ lược lời giải cổ điển trong 2 và 3 chiều.
- Giải thích vì sao $$E_8$$ và lưới Leech là những ứng viên tự nhiên trong 8 và 24 chiều.
- Mô tả chặn Cohn–Elkies như một bài toán tối ưu trên các hàm xuyên tâm.
- Phân biệt định lý cho $$E_8$$ (Viazovska một mình) và định lý cho lưới Leech (công trình chung CKMRV).
- Không khẳng định rằng bài toán xếp cầu đã được giải cho mọi số chiều.
- Kể lại sơ lược chuỗi ý tưởng từ chồng đạn đại bác của Kepler → xếp rời rạc nhiều chiều → mã hóa tín hiệu vô tuyến trong cuộc trò chuyện của Tao với Big Think, mà không biến lý thuyết mã thành nội dung lời trích dẫn giải Fields của Viazovska.

**Kiến thức cần có.** Thể tích quả cầu, lưới như một nhóm con rời rạc của $$\mathbb{R}^n$$, và ý tưởng về biến đổi Fourier của hàm xuyên tâm (chi tiết không bắt buộc).

---

## Bản đồ kiến thức nền: Hình học rời rạc, Giải tích Fourier và Dạng modular

Để thấy rõ vì sao một bài toán "xếp cam trong 8 chiều" lại gặp gỡ lý thuyết số, hãy xem ba ngành toán học giao nhau ở đây:

- **Hình học rời rạc và Lưới (Discrete Geometry & Lattices):** Nghiên cứu các cấu hình điểm, đa diện và cách sắp xếp tối ưu trong không gian $$\mathbb{R}^n$$. Trong mặt phẳng 2 chiều, nếu xếp đồng xu theo lưới ô vuông, diện tích bị phủ là $$\pi / 4 \approx 78{,}5\%$$; nếu xếp lệch thành lưới tổ ong lục giác, mật độ tăng vọt lên $$\pi / \sqrt{12} \approx 90{,}7\%$$. Càng lên số chiều cao, thể tích quả cầu co lại rất nhanh so với hình lập phương bao quanh, nên phần "khoảng trống" phình to ra một cách phản trực giác — trừ những số chiều có lưới đối xứng ngoại lệ như $$8$$ và $$24$$.
- **Giải tích Fourier và Công thức tổng Poisson:** Biến đổi Fourier $$\hat f$$ phân tích một hàm $$f(x)$$ theo các tần số sóng. **Công thức tổng Poisson** nối trực tiếp tổng giá trị của $$f$$ trên một lưới $$\Lambda$$ với tổng giá trị của $$\hat f$$ trên lưới đối ngẫu $$\Lambda^*$$: $$\sum_{x \in \Lambda} f(x) = \frac{1}{\operatorname{Vol}(\Lambda)} \sum_{\xi \in \Lambda^*} \hat f(\xi)$$. Chính đẳng thức này biến một bài toán hình học (tìm cấu hình xếp cầu) thành bài toán giải tích (tìm một hàm $$f$$ có dấu phù hợp!).
- **Dạng modular (Modular Forms) và lý do chuyển ngôn ngữ:** Dạng modular là những hàm giải tích sống trên nửa mặt phẳng phức trên, sở hữu một lượng **đối xứng khổng lồ** dưới nhóm $$\mathrm{SL}_2(\mathbb{Z})$$ (kiểu như $$F(-1/z) = z^k F(z)$$). Vì bị ràng buộc bởi quá nhiều đối xứng, không gian các dạng modular cực kỳ nhỏ và cứng — gần như chỉ cần biết vài hệ số đầu là biết toàn bộ hàm! Viazovska nhận ra rằng các điều kiện cực ngặt của "hàm kỳ diệu" (phải triệt tiêu đúng tại mọi bán kính $$\sqrt{2}, \sqrt{4}, \sqrt{6}, \dots$$ của lưới $$E_8$$) có thể được mã hóa chính xác bằng biến đổi Laplace của các dạng modular.

---

## 1. Bài toán xếp cầu

Cố định số chiều $$n$$, xếp các quả cầu đóng có bán kính bằng nhau, **không chồng lên nhau**, trong $$\mathbb{R}^n$$. **Mật độ** của một cách xếp là

$$
\delta=\limsup_{R\to\infty}\frac{\text{thể tích cầu nằm trong }B(0,R)}{\operatorname{Vol} B(0,R)}.
$$

Một cách tương đương (với cách xếp theo lưới), người ta so sánh thể tích của một quả cầu với thể tích của miền cơ bản (ô lưới) chứa tâm của nó.

**Câu hỏi.** $$\delta_n$$, cận trên đúng của mật độ trên mọi cách xếp trong $$n$$ chiều, bằng bao nhiêu? Cấu hình nào đạt được giá trị đó?

![Xếp lục giác]({{ site.baseurl }}/img/chapter_img/viazovska_packing_2d.svg)

*Hình. Cách xếp lục giác trên mặt phẳng, cách xếp tối ưu cổ điển trong 2 chiều.*

Bài toán vừa trực quan vừa khó: khi số chiều tăng, "khoảng trống" hành xử ngược với trực giác; cách xếp tối ưu toàn cục có thể không phải là một lưới; và chứng minh chặn trên thường khó hơn nhiều so với việc tìm ra một ứng viên tốt.

---

## 2. Đã biết gì về các chiều thấp?

| Số chiều | Tình trạng |
|-------|------------|
| $$n=1$$ | Hiển nhiên (các đoạn thẳng nối khít trên đường thẳng, mật độ $$100\%$$) |
| $$n=2$$ | Lưới lục giác ($$\pi/\sqrt{12} \approx 90{,}7\%$$), kết quả cổ điển (Thue, Fejes Tóth) |
| $$n=3$$ | FCC / HCP ($$\pi/\sqrt{18} \approx 74{,}05\%$$): giả thuyết Kepler, Hales (cùng kiểm chứng hình thức) |
| $$n=8$$ | $$E_8$$ ($$\pi^4/384 \approx 25{,}37\%$$): **Viazovska (2016)** |
| $$n=24$$ | Leech ($$\pi^{12}/12! \approx 0{,}193\%$$): **Cohn–Kumar–Miller–Radchenko–Viazovska** |
| $$n$$ tổng quát | Phần lớn còn mở; đã có các chặn tiệm cận |

Với hầu hết các số chiều (kể cả chiều 4, 5, 6, 7!), ta vẫn chưa biết chứng minh chặt chẽ cho cách xếp tối ưu. Chiều 8 và 24 tỏa sáng như hai "ốc đảo đối xứng" hiếm hoi.

### Từ đạn đại bác đến chuỗi bit (theo lời kể của Tao)

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) cho loạt *Six Math Essentials*, Terence Tao kể về bài toán xếp cầu như một ví dụ tiêu biểu cho chặng đường từ sự tò mò thuần túy đến công nghệ hiện đại. Một thủy thủ muốn chất được nhiều đạn đại bác nhất trong khoang tàu; khoảng trống quanh các quả cầu là phần bị lãng phí. Kepler đề xuất cách xếp lục giác như người bán cam vẫn xếp, phủ khoảng 74% thể tích trong ba chiều, nhưng không chứng minh được đó là cách tốt nhất. **Giả thuyết Kepler** trở thành một bài toán hình học kéo dài gần bốn thế kỷ. Trường hợp mặt phẳng (các đĩa tròn) được giải khoảng năm 1900; trường hợp ba chiều phải chờ đến chứng minh có máy tính hỗ trợ của Hales (công bố năm 1998), và sau đó là một phép kiểm chứng hình thức hoàn toàn bằng máy tính, xóa bỏ những nghi ngờ của các nhà phản biện. Rồi các nhà toán học đặt ra những câu hỏi tưởng như "vô dụng": bốn chiều thì sao? tám chiều thì sao? một không gian *rời rạc* gồm các chuỗi bit thì sao?

Khi điện thoại gửi tín hiệu số, mỗi thông điệp là một chuỗi bit. Ta muốn các tín hiệu hợp lệ khác nhau nằm cách đủ xa nhau trong khối lập phương nhiều chiều đó, để nhiễu không làm lẫn tín hiệu này với tín hiệu khác. Ý chính của Tao là đây vẫn là bài toán xếp cầu, chỉ là trong không gian nhiều chiều và rời rạc — và toán học về xếp cầu cung cấp cả các **mã sửa lỗi** lẫn **giới hạn lý thuyết** cho số bit mỗi giây có thể truyền qua một dải tần (từ đó, về mặt kinh tế, người ta định giá được dải tần vô tuyến). Theo lời kể ấy, ngành viễn thông vô tuyến thực chất đang "xếp cam" trong những không gian có số chiều rất lớn.

Hai điều cần lưu ý khi đọc. Thứ nhất, công trình được giải Fields của Viazovska là về xếp cầu trong không gian Euclid **liên tục** 8 và 24 chiều, không phải định lý nói rằng bà thiết kế mạng 5G. Thứ hai, những chi tiết lịch sử được kể gọn trong một buổi nói chuyện phổ thông (năm tháng, "thủy thủ người Anh", con số hiệu suất chính xác) nên được đối chiếu với tài liệu chuyên ngành khi cần trích dẫn. Trang chính của khóa học: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/); bài thực hành: [Khám phá xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

---

### Video ngắn: Xếp đĩa tròn trong mặt phẳng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/disc-packing-2d_vi.mp4"></video>
</div>

Trong mặt phẳng, lưới ô vuông phủ khoảng 78,5 phần trăm còn cách xếp tổ ong phủ khoảng 90,7 phần trăm, là mật độ tối ưu trong hai chiều.


## 3. Lưới, $$E_8$$ và lưới Leech

Một **lưới** $$\Lambda\subset\mathbb{R}^n$$ là một nhóm con rời rạc sinh ra $$\mathbb{R}^n$$ (có thể hình dung là $$\mathbb{Z}^n$$ sau một phép đổi biến tuyến tính). **Cách xếp theo lưới** đặt tâm các quả cầu tại các điểm của lưới, với bán kính bằng một nửa độ dài của vectơ khác không ngắn nhất.

### Lưới nghiệm $$E_8$$

$$E_8\subset\mathbb{R}^8$$ là lưới **unimodular chẵn** duy nhất (sai khác một phép đẳng cự) trong 8 chiều. Ta có thể mô tả nó cực kỳ gọn: đó là tập tất cả các vectơ trong $$\mathbb{R}^8$$ có tọa độ hoặc đều nguyên hoặc đều bán nguyên (dạng $$k + \frac{1}{2}$$), sao cho tổng 8 tọa độ là một số chẵn! Lưới này có:

- các vectơ ngắn nhất có bình phương độ dài bằng $$2$$ (tức độ dài $$\sqrt{2}$$), tạo thành hệ nghiệm $$E_8$$ gồm đúng **240 vectơ** — nghĩa là mỗi quả cầu trong $$E_8$$ chạm khít đồng thời **240** quả cầu hàng xóm xung quanh nó!  
- một nhóm đối xứng cực lớn (nhóm Weyl có gần 700 triệu phép đối xứng);  
- từ lâu đã được dự đoán là cho mật độ xếp tối ưu **toàn cục**, không chỉ trong lớp các lưới.

### Lưới Leech $$\Lambda_{24}$$

Trong 24 chiều, **lưới Leech** là lưới unimodular chẵn duy nhất **không có nghiệm** (không có vectơ nào có bình phương độ dài bằng 2; các vectơ ngắn nhất có bình phương độ dài bằng 4, và có tới **196.560** vectơ như thế!). Nó có vai trò trung tâm trong lý thuyết các nhóm đơn rời rạc (*sporadic groups*) và mã sửa lỗi Golay, và cũng được dự đoán là cách xếp dày nhất trong 24 chiều.

![E8 và Leech]({{ site.baseurl }}/img/chapter_img/viazovska_e8_leech.svg)

*Hình. Hai lưới đặc biệt mà Viazovska và các cộng sự đã chứng minh là tối ưu.*

**Lưu ý.** Tối ưu trong lớp các lưới **không** tự động là tối ưu toàn cục: ở nhiều số chiều, một cấu hình không tuần hoàn có thể xếp khít hơn mọi lưới. Định lý của Viazovska / CKMRV loại trừ khả năng đó trong 8 và 24 chiều.

---

## 4. Cohn–Elkies: bài toán xếp cầu gặp giải tích Fourier

Năm 2003, **Henry Cohn và Noam Elkies** đã mở ra một cánh cửa hoàn toàn mới: đưa việc chặn trên mật độ xếp cầu về sự tồn tại của một **hàm xuyên tâm** đặc biệt (chỉ phụ thuộc vào khoảng cách $$\|x\|$$), với các ràng buộc về dấu trên $$f$$ và trên biến đổi Fourier $$\hat f$$ của nó; ý tưởng xuất phát từ quy hoạch tuyến tính và công thức tổng Poisson.

**Các giả thiết** (dạng sơ đồ, bỏ qua hằng số chuẩn hóa):

- $$f$$ xuyên tâm, thuộc lớp Schwartz (giảm rất nhanh ra vô tận);  
- $$f(x)\le 0$$ khi $$\|x\|\ge r$$ (ngoài bán kính tối thiểu giữa hai tâm cầu);  
- $$\hat f(\xi)\ge 0$$ với mọi tần số $$\xi$$;  
- $$f(0),\hat f(0)>0$$.

Khi đó, mật độ của *mọi* cách xếp (dù tuần hoàn hay hỗn loạn) đều bị chặn trên bởi một biểu thức đơn giản theo $$f(0)/\hat f(0)$$ và $$r$$! Trực giác từ công thức tổng Poisson: nếu ta áp dụng công thức tổng Poisson cho lưới $$\Lambda$$, vế trái là $$f(0) + \sum_{x \neq 0} f(x) \le f(0)$$ (vì mọi điểm khác gốc đều nằm ngoài bán kính $$r$$ nên $$f(x) \le 0$$), còn vế phải là $$\frac{1}{\operatorname{Vol}(\Lambda)}\left(\hat f(0) + \sum_{\xi \neq 0} \hat f(\xi)\right) \ge \frac{\hat f(0)}{\operatorname{Vol}(\Lambda)}$$ (vì $$\hat f \ge 0$$). Ghép hai bất đẳng thức đó lại, ta lập tức có cận dưới cho $$\operatorname{Vol}(\Lambda)$$, tức cận trên cho mật độ!

![Ý tưởng Cohn–Elkies]({{ site.baseurl }}/img/chapter_img/viazovska_cohn_elkies.svg)

*Hình. Các điều kiện về dấu trên $$f$$ và $$\hat f$$ cho ta một chặn trên cho bài toán xếp cầu.*

**Bài toán dấu bằng.** Để chứng minh một lưới là tối ưu tuyệt đối, cả hai bất đẳng thức trên phải đồng thời xảy ra **dấu bằng**: nghĩa là $$f(x)$$ phải bằng $$0$$ (và đổi dấu/tiếp xúc với trục hoành thành **không điểm kép**) tại đúng độ dài của mọi vectơ trong lưới ($$\sqrt{2}, \sqrt{4}, \sqrt{6}, \dots$$ với $$E_8$$), đồng thời $$\hat f(\xi)$$ cũng phải có không điểm kép tại mọi vectơ của lưới đối ngẫu! Hàm thỏa mãn điều kiện gắt gao ấy gọi là **hàm kỳ diệu** (*magic function*). Trong hơn 10 năm, các thí nghiệm bằng máy tính của Cohn và Elkies cho thấy chặn trên khớp với mật độ của $$E_8$$ và Leech tới hơn 30 chữ số thập phân — nhưng không ai viết ra được công thức chính xác cho hàm kỳ diệu!

---

## 5. Hàm kỳ diệu trong 8 chiều

Viazovska đã tìm ra công thức chính xác cho hàm kỳ diệu bằng một cú ngoặt bất ngờ: tách hàm $$f$$ thành tổng của hai phần — một hàm riêng của biến đổi Fourier với trị riêng $$+1$$ và một hàm với trị riêng $$-1$$ — rồi xây dựng chúng qua **biến đổi Laplace** của các **dạng gần modular** (*quasimodular / weakly holomorphic modular forms*) được chọn lọc tinh xảo, bảo đảm đồng thời:

- các điều kiện về dấu của Cohn–Elkies;  
- không điểm kép chính xác tại $$\sqrt{2k}$$ ($$k \ge 1$$) — đúng bằng độ dài các vectơ của $$E_8$$!

Đây là một chứng minh giải tích chính xác tuyệt đối, không phải tối ưu bằng số cho "gần khớp" rồi làm tròn.

<div class="textbook-theorem" markdown="1">
**Định lý (Viazovska, 2016/2017).**  
Cách xếp theo lưới $$E_8$$ đạt mật độ lớn nhất trong **mọi** cách xếp cầu trong $$\mathbb{R}^8$$.
</div>

Điểm đẹp: dạng modular, vốn là công cụ của số học và lý thuyết hàm tự đẳng cấu, bất ngờ trở thành **công cụ tối ưu trong hình học rời rạc**. Giải tích Fourier cùng tính modular loại trừ mọi đối thủ.

---

## 6. Hai mươi bốn chiều: công trình hợp tác

Chỉ một tuần sau bài báo về $$E_8$$, **Cohn, Kumar, Miller, Radchenko và Viazovska** cùng nhau xây dựng hàm kỳ diệu trong 24 chiều và chứng minh lưới Leech là tối ưu trong mọi cách xếp trong $$\mathbb{R}^{24}$$.

Ghi nhận công lao cần nhớ:

- **Chiều 8:** Viazovska (một mình; cột mốc trung tâm).  
- **Chiều 24:** công trình hợp tác CKMRV.

Huy chương Fields 2022 ghi nhận cả nhóm đóng góp liên quan, không chỉ một con số mật độ.

---

## 7. Không chỉ là một con số mật độ

Các ý tưởng của Cohn–Elkies / Viazovska được tiếp nối trong:

- **tính tối ưu phổ quát** (*universal optimality*): lưới $$E_8$$ và lưới Leech không chỉ xếp cầu đặc nhất, mà còn cực tiểu hóa năng lượng của hệ điểm dưới **mọi** thế năng tương tác hoàn toàn đơn điệu (giống như cấu trúc tinh thể bền vững nhất mọi lúc);  
- các **công thức nội suy Fourier** (liên quan đến Radchenko–Viazovska), cho phép tái tạo chính xác một hàm xuyên tâm chỉ từ giá trị của nó và biến đổi Fourier của nó tại các bán kính $$\sqrt{n}$$;  
- chương trình tìm lời giải chính xác trong hình học rời rạc bằng giải tích điều hòa.

Bài toán xếp cầu trở thành cửa ngõ vào cả một "xưởng" thiết kế các hàm cực trị.

---

## 8. Vì sao kết quả này quan trọng

- Giải quyết hai bài toán xếp cầu chính xác nổi tiếng nhất ngoài các chiều thấp.  
- Dùng dạng modular như một công cụ **tối ưu hình học**.  
- Bổ sung cho chứng minh có máy tính hỗ trợ trong 3 chiều (Hales) một thành tựu **thuần giải tích** ở các chiều đặc biệt.  
- Là cây cầu trong Chương 2: **giải tích ↔ hình học rời rạc**.

So với [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/): cả hai đều kết hợp giải tích mạnh với cấu trúc đặc biệt; một bên là cấp số cộng các số nguyên tố, một bên là cách xếp theo lưới.

---

## 9. Nhìn lại điều nghịch lý

Với hầu hết các số chiều, ta không chỉ ra được cách xếp dày nhất. Trong 8 và 24 chiều, các lưới đặc biệt không chỉ tồn tại mà còn **được chứng minh là tốt nhất**, nhờ một hàm được thiết kế bằng giải tích Fourier loại trừ mọi đối thủ. Quy luật "chiều càng cao càng khó" có ngoại lệ khi đối xứng đủ lớn để các dạng modular "biết" được hàm kỳ diệu.

**Số hôn** (*kissing number*, số quả cầu đơn vị có thể cùng chạm một quả cầu cho trước — bằng $$6$$ trong 2 chiều, $$12$$ trong 3 chiều, $$240$$ trong 8 chiều, $$196.560$$ trong 24 chiều) có liên quan nhưng **khác** với mật độ xếp trong toàn không gian: giải được bài toán số hôn không tự động giải được bài toán xếp cầu, và ngược lại.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Bài toán xếp cầu đã giải xong cho mọi số chiều." | **Sai** | Chỉ một số chiều có lời giải tối ưu chính xác. |
| "Tính tối ưu của $$E_8$$ chỉ là một con số gần đúng." | **Sai** | Đó là một định lý chính xác. |
| "Một mình Viazovska chứng minh cho lưới Leech." | **Sai** | Trường hợp 24 chiều là công trình hợp tác CKMRV. |
| "Tối ưu trong lớp lưới thì tự động tối ưu toàn cục." | **Sai** | Nói chung, một cấu hình không phải lưới có thể tốt hơn; định lý loại trừ điều đó trong 8 và 24 chiều. |
| "Chỉ là chuyện hệ nghiệm, không có giải tích." | **Sai** | Các điều kiện Fourier là công cụ chính để có chặn trên. |

---

## Bài tập

1. Thảo luận về mật độ của cách xếp theo lưới nguyên trong $$\mathbb{R}^2$$ (sau khi đổi tỉ lệ thích hợp).  
2. Định nghĩa mật độ của cách xếp theo lưới qua thể tích miền cơ bản.  
3. Vì sao con số 240 nghiệm gợi ý rằng $$E_8$$ rất "chật" ở mức số hôn / lân cận?  
4. Viết một đoạn: tính dương của biến đổi Fourier kiểm soát cấu hình toàn cục như thế nào?  
5. Viết hai câu phân biệt tác giả của định lý cho $$E_8$$ và cho lưới Leech.  
6. Đọc phần mở đầu bài báo của Viazovska / một bài tổng quan; liệt kê các thành phần giải tích xuất hiện trước khi dạng modular được đưa vào.  
7. **Liên hệ trong chương.** Viết một đoạn so sánh "thiết kế hàm để chứng minh tính tối ưu" (Viazovska) với "kiểm soát nhiều thang đo" trong giải tích điều hòa (Wang).  
8. Nêu một khác biệt giữa cách chứng minh của Hales (Kepler, 3 chiều) và của Viazovska ($$E_8$$).

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Viazovska_Sphere_Packing/`.

**Thứ tự xem gợi ý**

1. Bài viết năm 2016 của Quanta về xếp cầu: [link](https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/).  
2. Bài giảng Einstein của Viazovska: [YouTube](https://www.youtube.com/watch?v=fH6KNlUJux0).  
3. Hội thảo Breakthrough: [YouTube](https://www.youtube.com/watch?v=VCZeVsTb7DU).  
4. arXiv:1603.04246.

**Nhắc lại:** lời giải tối ưu đã biết cho các chiều 1, 2, 3, 8, 24, không phải mọi số chiều.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Viazovska_Sphere_Packing/transcripts/` · trạng thái: `research/video-research/Viazovska_Sphere_Packing/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Viazovska_Sphere_Packing_fH6KNlUJux0_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Viazovska_Sphere_Packing/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=fH6KNlUJux0  
2. https://www.youtube.com/watch?v=VCZeVsTb7DU  
3. https://www.youtube.com/watch?v=qr6ZbYancMY  
4. https://arxiv.org/abs/1603.04246  
5. https://arxiv.org/pdf/1603.04246  
6. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-mv.pdf  
7. https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/  
8. https://en.wikipedia.org/wiki/Sphere_packing  
9. https://en.wikipedia.org/wiki/Maryna_Viazovska  
10. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
11. https://www.math.inc/sphere-packing  
12. https://en.wikipedia.org/wiki/E8_lattice  
13. https://en.wikipedia.org/wiki/Leech_lattice  
14. https://www.youtube.com/watch?v=OOMx2BHHWtE  

### Bộ tư liệu nghiên cứu

14. Bộ tư liệu của khóa học: `research/video-research/Viazovska_Sphere_Packing/`.

1. **M. Viazovska** (2017), *Annals of Mathematics* — 8 chiều.  
2. **Cohn–Kumar–Miller–Radchenko–Viazovska**, *Annals* — 24 chiều.  
3. **Cohn & Elkies** — chặn bằng quy hoạch tuyến tính.  
4. Các bài tổng quan / Quanta — trực giác phổ thông.  
5. IMU, Huy chương Fields 2022 — Viazovska.  
6. Conway–Sloane — kiến thức cổ điển về lưới.

---

## Hướng đi tiếp

- Tìm hiểu tính tối ưu phổ quát và bài toán cực tiểu năng lượng.  
- Học nhập môn về dạng modular dành cho người làm giải tích.  
- So sánh với Maynard và Green–Tao: cấu trúc đặc biệt kết hợp giải tích mạnh.  
- Ghi lại một câu hỏi cụ thể bạn vẫn còn thắc mắc, ví dụ "vì sao dạng modular tạo ra đúng các không điểm của $$f$$?"  
- Đọc song song bài [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/) về một nữ chủ nhân khác của giải Fields, và bài [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/) về cấu trúc trong không gian thưa / rời rạc.

## Video tham khảo

- **Xem trước:** [Einstein Lectures: Maryna Viazovska - The sphere packing problem](https://www.youtube.com/watch?v=fH6KNlUJux0) — Universität Bern, tiếng Anh. Viazovska giới thiệu bài toán xếp cầu cho khán giả rộng; nên xem trước khi đọc bài.
- [Maryna Viazovska: 2018 Breakthrough Prize Symposium](https://www.youtube.com/watch?v=VCZeVsTb7DU) — Breakthrough, tiếng Anh. Bài nói của Viazovska tại hội thảo Breakthrough; nên xem sau khi đã nắm ý chính của bài.
- [What is...sphere packing?](https://www.youtube.com/watch?v=qr6ZbYancMY) — VisualMath, tiếng Anh. Xem thêm sau hai video trên; giới thiệu ngắn về khái niệm xếp cầu.
