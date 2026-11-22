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

**Maryna Viazovska** nhận **Huy chương Fields 2022** nhờ chứng minh rằng lưới $$E_8$$ cho mật độ tối ưu trong bài toán xếp cầu 8 chiều, cùng các đóng góp liên quan, trong đó có việc chứng minh (cùng các cộng sự) tính tối ưu của lưới Leech trong 24 chiều. Bà là **người phụ nữ thứ hai** nhận giải Fields (sau Mirzakhani năm 2014). Thành tựu này giải quyết trọn vẹn hai số chiều "đặc biệt" của hình học rời rạc bằng cách **thiết kế một hàm Fourier**, chứ không phải bằng cách liệt kê các cấu hình.

Nội dung bài:

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

## 1. Bài toán xếp cầu

Cố định số chiều $$n$$, xếp các quả cầu đóng có bán kính bằng nhau, **không chồng lên nhau**, trong $$\mathbb{R}^n$$. **Mật độ** của một cách xếp là

$$
\delta=\limsup_{R\to\infty}\frac{\text{thể tích cầu nằm trong }B(0,R)}{\operatorname{Vol} B(0,R)}.
$$

Một cách tương đương (với cách xếp theo lưới), người ta so sánh thể tích của miền cơ bản với số quả cầu có tâm tại các điểm của lưới.

**Câu hỏi.** $$\delta_n$$, cận trên đúng của mật độ trên mọi cách xếp trong $$n$$ chiều, bằng bao nhiêu? Cấu hình nào đạt được giá trị đó?

![Xếp lục giác]({{ site.baseurl }}/img/chapter_img/viazovska_packing_2d.svg)

*Hình. Cách xếp lục giác trên mặt phẳng, cách xếp tối ưu cổ điển trong 2 chiều.*

Bài toán vừa trực quan vừa khó: khi số chiều tăng, "khoảng trống" hành xử ngược với trực giác; cách xếp tối ưu toàn cục có thể không phải là một lưới; và chứng minh chặn trên thường khó hơn nhiều so với việc tìm ra một ứng viên tốt.

---

## 2. Đã biết gì về các chiều thấp?

| Số chiều | Tình trạng |
|-------|------------|
| $$n=1$$ | Hiển nhiên (các đoạn thẳng trên đường thẳng) |
| $$n=2$$ | Lưới lục giác, kết quả cổ điển |
| $$n=3$$ | FCC / HCP: giả thuyết Kepler, Hales (cùng với kiểm chứng hình thức) |
| $$n=8$$ | $$E_8$$: **Viazovska (2016)** |
| $$n=24$$ | Leech: **Cohn–Kumar–Miller–Radchenko–Viazovska** |
| $$n$$ tổng quát | Phần lớn còn mở; đã có các chặn tiệm cận |

Với hầu hết các số chiều, chưa biết cách xếp tối ưu chính xác. Chiều 8 và 24 là những trường hợp đặc biệt nhờ tính đối xứng.

### Từ đạn đại bác đến chuỗi bit (theo lời kể của Tao)

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) cho loạt *Six Math Essentials* sắp ra mắt, Terence Tao kể về bài toán xếp cầu như một ví dụ cho chặng đường từ sự tò mò đến công nghệ. Một thủy thủ muốn chất được nhiều đạn đại bác nhất trong khoang tàu; khoảng trống quanh các quả cầu là phần bị lãng phí. Kepler đề xuất cách xếp lục giác như người bán cam vẫn xếp, phủ khoảng 74% thể tích trong ba chiều, nhưng không chứng minh được đó là cách tốt nhất. **Giả thuyết Kepler** trở thành một bài toán hình học kéo dài hàng thế kỷ. Trường hợp mặt phẳng (các đĩa tròn) được giải khoảng năm 1900; trường hợp ba chiều phải chờ đến chứng minh có máy tính hỗ trợ của Hales (công bố năm 1998), và sau đó là một phép kiểm chứng hình thức, xóa bỏ những nghi ngờ của các nhà phản biện mà Tao còn nhớ. Rồi các nhà toán học đặt ra những câu hỏi có vẻ "vô dụng": bốn chiều thì sao? một không gian *rời rạc* gồm các chuỗi bit thì sao?

Khi điện thoại gửi tín hiệu số, mỗi thông điệp là một chuỗi bit. Ta muốn các tín hiệu khác nhau nằm cách xa nhau trong khối lập phương nhiều chiều đó, để nhiễu không làm lẫn tín hiệu này với tín hiệu khác. Ý chính của Tao là đây vẫn là bài toán xếp cầu, chỉ là trong nhiều chiều và rời rạc, và toán học về xếp cầu cung cấp cả các cách xây dựng lẫn **giới hạn lý thuyết** cho số bit mỗi giây có thể truyền qua một dải tần (từ đó, về mặt kinh tế, người ta có thể định giá dải tần đó). Theo lời kể ấy, ngành viễn thông vô tuyến đang "xếp cam" trong những không gian có số chiều rất lớn.

Hai điều cần lưu ý khi đọc. Thứ nhất, công trình được giải Fields của Viazovska là về xếp cầu trong không gian Euclid **liên tục** 8 và 24 chiều, không phải định lý nói rằng bà thiết kế mạng 5G. Thứ hai, những chi tiết lịch sử được kể gọn trong một buổi nói chuyện phổ thông (năm tháng, "thủy thủ người Anh", con số hiệu suất chính xác) nên được đối chiếu với tài liệu chuyên ngành khi cần trích dẫn. Trang chính của khóa học: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/); bài thực hành: [Khám phá xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

### Từ đạn đại bác tới chuỗi bit (theo Tao)

Terence Tao, trong [cuộc trò chuyện Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) cho *Six Math Essentials* sắp ra, kể lại xếp cầu như đường ống tò mò-đến-công nghệ. Một thủy thủ muốn nhiều đạn đại bác nhất trong hầm tàu; khoảng trống quanh quả cầu là cái giá. Kepler đề xuất xếp lục giác kiểu người bán cam—khoảng 74% ở ba chiều—và không chứng minh được đó là tốt nhất. **Giả thuyết Kepler** ấy thành bài hình học dài thế kỷ. Mặt phẳng (đĩa) xong khoảng 1900; ba chiều chờ chứng minh có máy tính hỗ trợ của Hales (công bố 1998) và, sau đó, kiểm chứng hình thức gỡ nghi ngờ trọng tài mà Tao nhớ. Nhà toán học rồi hỏi những câu “vô dụng”: bốn chiều? một không gian *rời rạc* các chuỗi bit?

Khi điện thoại gửi tín hiệu số, mỗi thông điệp là một chuỗi bit. Bạn muốn các tín hiệu khác nhau nằm xa nhau trong khối lập phương cao chiều ấy để nhiễu không nhầm cái này với cái kia. Khẩu hiệu của Tao là đây vẫn là xếp cầu—cao chiều và rời rạc—và toán xếp cung cấp cả xây dựng lẫn **giới hạn lý thuyết** về số bit mỗi giây qua một lát phổ (nên, ở lớp kinh tế, người ta có thể định giá lát phổ ấy thế nào). Ngành viễn thông vô tuyến, trong lời kể ấy, đang xếp cam ở chiều rất cao.

Hai hàng rào biết đọc. Thứ nhất, công trình Fields của Viazovska là xếp Euclid **liên tục** ở chiều 8 và 24, không phải định lý rằng bà thiết kế 5G. Thứ hai, sự nén sử trong buổi nói chuyện phổ thông (năm tháng, “thủy thủ Anh,” hiệu suất đúng) nên đối chiếu tài liệu xếp chuyên khi bạn cần trích dẫn. Hub khóa học: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/); studio: [Khám phá xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

---

### Video ngắn: Xếp đĩa tròn trong mặt phẳng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/disc-packing-2d_vi.mp4"></video>
</div>

Trong mặt phẳng, lưới ô vuông phủ khoảng 78,5 phần trăm còn cách xếp tổ ong phủ khoảng 90,7 phần trăm, là mật độ tối ưu trong hai chiều.


## 3. Lưới, $$E_8$$ và lưới Leech

Một **lưới** $$\Lambda\subset\mathbb{R}^n$$ là một nhóm con rời rạc sinh ra $$\mathbb{R}^n$$ (có thể hình dung là $$\mathbb{Z}^n$$ sau một phép đổi biến tuyến tính). **Cách xếp theo lưới** đặt tâm các quả cầu tại các điểm của lưới, với bán kính bằng một nửa độ dài của vectơ khác không ngắn nhất.

### Lưới nghiệm $$E_8$$

$$E_8\subset\mathbb{R}^8$$ là lưới **unimodular chẵn** duy nhất (sai khác một phép đẳng cự) trong 8 chiều. Lưới này có:

- các vectơ ngắn nhất có chuẩn 2, tạo thành hệ nghiệm $$E_8$$ (**240 nghiệm**);  
- một nhóm đối xứng cực lớn (nhóm Weyl / nhóm tự đẳng cấu);  
- từ lâu đã được dự đoán là cho mật độ xếp tối ưu **toàn cục**, không chỉ trong lớp các lưới.

### Lưới Leech $$\Lambda_{24}$$

Trong 24 chiều, **lưới Leech** là lưới unimodular chẵn **không có nghiệm** (không có vectơ chuẩn 2). Nó có vai trò trung tâm trong lý thuyết các nhóm đơn rời rạc (sporadic), và cũng được dự đoán là cách xếp dày nhất.

![E8 và Leech]({{ site.baseurl }}/img/chapter_img/viazovska_e8_leech.svg)

*Hình. Hai lưới đặc biệt mà Viazovska và các cộng sự đã chứng minh là tối ưu.*

**Lưu ý.** Tối ưu trong lớp các lưới **không** tự động là tối ưu toàn cục: một cấu hình không tuần hoàn có thể tốt hơn. Định lý của Viazovska / CKMRV loại trừ khả năng đó trong 8 và 24 chiều.

---

## 4. Cohn–Elkies: bài toán xếp cầu gặp giải tích Fourier

**Cohn–Elkies** đưa việc chặn trên mật độ về sự tồn tại của một hàm xuyên tâm đặc biệt, với các ràng buộc về dấu trên $$f$$ và trên biến đổi Fourier $$\hat f$$ của nó; ý tưởng xuất phát từ quy hoạch tuyến tính và công thức tổng Poisson.

**Các giả thiết** (dạng sơ đồ, bỏ qua hằng số chuẩn hóa):

- $$f$$ xuyên tâm, thuộc lớp Schwartz (hoặc đủ tốt);  
- $$f(x)\le 0$$ khi $$\|x\|\ge r$$ (ngoài một bán kính);  
- $$\hat f(\xi)\ge 0$$ với mọi tần số;  
- $$f(0),\hat f(0)>0$$.

Khi đó, mật độ của mọi cách xếp bị chặn trên bởi một biểu thức đơn giản theo $$f(0),\hat f(0)$$ và bán kính.

![Ý tưởng Cohn–Elkies]({{ site.baseurl }}/img/chapter_img/viazovska_cohn_elkies.svg)

*Hình. Các điều kiện về dấu trên $$f$$ và $$\hat f$$ cho ta một chặn trên cho bài toán xếp cầu.*

**Bài toán dấu bằng.** Để chứng minh một lưới là tối ưu, cần tìm $$f$$ sao cho chặn Cohn–Elkies **bằng đúng** mật độ của lưới đó; đó là **hàm kỳ diệu** (*magic function*). Các ràng buộc cực kỳ chặt: vừa điều kiện dấu trong không gian, vừa tính dương của biến đổi Fourier, vừa dấu bằng tại dữ liệu của lưới.

Nếu $$\hat f$$ có "hố âm", chặn có thể sai hoặc không chặt; tính dương của biến đổi Fourier là cơ chế kiểm soát cấu hình ở mức **toàn cục**, không chỉ ở lân cận.

---

## 5. Hàm kỳ diệu trong 8 chiều

Viazovska xây dựng một hàm Fourier đặc biệt bằng **dạng modular** và biến đổi Laplace của một số dạng gần chỉnh hình (weakly holomorphic) được chọn lọc, bảo đảm:

- các điều kiện về dấu của Cohn–Elkies;  
- dấu bằng tại dữ liệu xếp của $$E_8$$.

Đây là một chứng minh giải tích chính xác, không phải tối ưu bằng số cho "gần khớp" rồi làm tròn.

<div class="textbook-theorem" markdown="1">
**Định lý (Viazovska, 2016/2017).**  
Cách xếp theo lưới $$E_8$$ đạt mật độ lớn nhất trong **mọi** cách xếp cầu trong $$\mathbb{R}^8$$.
</div>

Điểm đẹp: dạng modular, vốn là công cụ của số học và lý thuyết hàm tự đẳng cấu, trở thành **công cụ tối ưu trong hình học rời rạc**. Giải tích Fourier cùng tính modular loại trừ mọi đối thủ.

---

## 6. Hai mươi bốn chiều: công trình hợp tác

**Cohn, Kumar, Miller, Radchenko, Viazovska** xây dựng hàm kỳ diệu trong 24 chiều và chứng minh lưới Leech là tối ưu trong mọi cách xếp trong $$\mathbb{R}^{24}$$.

Ghi nhận công lao cần nhớ:

- **Chiều 8:** Viazovska (một mình; cột mốc trung tâm).  
- **Chiều 24:** công trình hợp tác CKMRV.

Huy chương Fields 2022 ghi nhận cả nhóm đóng góp liên quan, không chỉ một con số mật độ.

---

## 7. Không chỉ là một con số mật độ

Các ý tưởng của Cohn–Elkies / Viazovska được tiếp nối trong:

- **tính tối ưu phổ quát** (universal optimality) và bài toán cực tiểu năng lượng của hệ điểm;  
- các công thức nội suy Fourier (liên quan đến Radchenko–Viazovska);  
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

**Số hôn** (kissing number, số quả cầu đơn vị có thể cùng chạm một quả cầu cho trước) có liên quan nhưng **khác** với mật độ xếp trong toàn không gian: giải được bài toán số hôn không tự động giải được bài toán xếp cầu, và ngược lại.

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
