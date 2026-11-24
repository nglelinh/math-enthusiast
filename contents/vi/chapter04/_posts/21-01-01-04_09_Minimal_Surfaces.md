---
layout: post
title: "Mặt tối thiểu"
chapter: '04'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
---

Hãy uốn một đoạn dây thép thành một vòng cong uốn lượn tùy ý, nhúng vào chậu nước xà phòng rồi nhẹ nhàng nhấc lên. Trong chớp mắt, chẳng cần giải một phương trình vi phân nào, lớp màng xà phòng óng ánh tự co lại thành một mặt cong hình yên ngựa tuyệt đẹp — một "máy tính tương tự" của tự nhiên đang giải bài toán tối ưu hình học để cực tiểu hóa năng lượng sức căng bề mặt.

Trong toán học, những hình dạng như thế gọi là **mặt tối thiểu** (minimal surface): mặt có diện tích nhỏ nhất theo nghĩa địa phương. Về mặt giải tích, chúng là nghiệm của một điều kiện duy nhất nhưng cực kỳ sâu sắc: **độ cong trung bình bằng $$0$$**, dẫn tới một phương trình đạo hàm riêng phi tuyến. Hiếm có chủ đề nào nơi giải tích, hình học vi phân và vẻ đẹp thị giác gặp nhau trọn vẹn đến thế: catenoid, helicoid và mặt Costa vừa là định lý sâu sắc vừa như những tác phẩm điêu khắc.

**Lộ trình:** màng xà phòng và bài toán Plateau → độ cong trung bình bằng 0 → các ví dụ cổ điển → tính ổn định và tôpô → lý thuyết tồn tại hiện đại → ứng dụng → nhầm lẫn thường gặp, hướng đi tiếp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu **bài toán Plateau**: tìm mặt có diện tích nhỏ nhất với biên cho trước.
- Giải thích **độ cong trung bình** ở mức trực giác và điều kiện $$H=0$$ cho mặt tối thiểu.
- Nhận ra các ví dụ cổ điển: **mặt phẳng**, **catenoid**, **helicoid**, và ý tưởng của **mặt Costa**.
- Phân biệt cực tiểu địa phương (mặt tối thiểu) với cực tiểu diện tích toàn cục.
- Mô tả vì sao mặt tối thiểu xuất hiện trong khoa học vật liệu và giải tích hình học.
- Tránh nói "mặt tối thiểu là mặt nhỏ nhất trong vũ trụ" khi chưa nêu biên hoặc ràng buộc.

**Kiến thức cần có.** Trực giác về giải tích nhiều biến (đạo hàm riêng, đồ thị $$z=u(x,y)$$); hình dung được đường cong và mặt cong. Biết phương trình đạo hàm riêng thì tốt nhưng không bắt buộc.

---

## Bản đồ kiến thức nền: Phép tính biến phân và Giải tích hình học là gì và giữ vai trò gì?

Ở giải tích đại cương, để tìm điểm $$x$$ làm cực tiểu hàm số $$f(x)$$, ta giải phương trình đạo hàm $$f'(x) = 0$$. Nhưng nếu ẩn số không còn là một con số $$x$$, mà là **cả một đường cong** (như đường đi ngắn nhất giữa hai điểm) hay **cả một mặt cong $$S$$** (như màng xà phòng có diện tích nhỏ nhất căng trên khung dây), thì ta bước sang **Phép tính biến phân** (Calculus of Variations) và **Giải tích hình học**. Đây là ngôn ngữ lõi của cơ học cổ điển (nguyên lý tác dụng tối thiểu), thuyết tương đối rộng (chứng minh định lý khối lượng dương của Schoen–Yau), thiết kế kết cấu kiến trúc siêu nhẹ và xử lý lưới 3D trong đồ họa máy tính.

Tư duy cốt lõi gồm ba bước cực kỳ tự nhiên:
1. **Định nghĩa phiếm hàm năng lượng:** Gán cho mỗi mặt cong $$S$$ một con số — diện tích $$\mathrm{Area}(S)$$.
2. **Đẩy nhẹ mặt cong và cho "đạo hàm" bằng $$0$$:** Nếu mặt đang ở trạng thái dừng, mọi biến dạng nhỏ giữ nguyên khung biên sẽ không làm thay đổi diện tích ở bậc nhất. Điều kiện "đạo hàm bằng $$0$$" trong thế giới mặt cong hóa ra lại chính là **độ cong trung bình $$H = 0$$** tại mọi điểm!
3. **Phân biệt điểm dừng, cực tiểu địa phương và cực tiểu toàn cục:** Giống như $$f'(x)=0$$ có thể là cực tiểu, cực đại hay điểm uốn, điều kiện $$H=0$$ chỉ đảm bảo *diện tích dừng* — còn muốn biết màng xà phòng có vỡ hay nhảy sang dạng khác hay không, ta phải xét tính ổn định (biến phân bậc hai) và so sánh diện tích toàn cục.

---

## 1. Màng xà phòng và bài toán Plateau

**Joseph Plateau** làm thí nghiệm với màng xà phòng vào thế kỷ XIX. Phiên bản toán học, **bài toán Plateau**, hỏi: cho một đường cong đóng $$\Gamma$$ trong $$\mathbb{R}^3$$ (khung dây), có tồn tại mặt $$S$$ có biên $$\Gamma$$ với diện tích nhỏ nhất không, và mặt đó trơn đến mức nào?

Màng xà phòng gợi ý rằng lời giải tồn tại và trơn, ngoại trừ có thể dọc những đường nơi các màng gặp nhau theo quy tắc hình học (luôn chụm ba màng tạo góc $$120^\circ$$ trong bọt xà phòng). Việc chứng minh sự tồn tại và độ trơn cần đến giải tích sâu của thế kỷ XX: Jesse Douglas (nhờ đó ông đoạt một trong hai Huy chương Fields đầu tiên năm 1936) và Tibor Radó giải được các trường hợp quan trọng; sau đó lý thuyết độ đo hình học mở rộng sang số chiều cao hơn và các tập có điểm kỳ dị.

Màng xà phòng thật chỉ là cực tiểu năng lượng **địa phương**; toán học phân biệt cực tiểu địa phương, cực tiểu toàn cục, và điểm tới hạn của phiếm hàm diện tích.

---

## 2. Độ cong trung bình và phương trình mặt tối thiểu

Với một mặt trơn có định hướng, tại mỗi điểm ta xét các lát cắt vuông góc với mặt: độ uốn lớn nhất và nhỏ nhất dọc hai phương trực giao gọi là hai **độ cong chính** $$\kappa_1,\kappa_2$$. **Độ cong trung bình** là

$$
H=\frac{\kappa_1+\kappa_2}{2}
$$

(tùy theo quy ước chuẩn hóa). Mặt là **tối thiểu** khi $$H\equiv 0$$ ở mọi điểm.

Hãy kiểm tra trực giác ngay bằng hai ví dụ quen thuộc:
- **Mặt cầu bán kính $$R$$:** uốn cong về cùng một phía theo mọi hướng, nên $$\kappa_1 = \kappa_2 = 1/R \implies H = 1/R \neq 0$$. Vậy mặt cầu *không* phải là mặt tối thiểu! (Bong bóng xà phòng có dạng hình cầu chỉ vì nó phải nhốt một thể tích không khí cố định bên trong, tạo chênh lệch áp suất — nên nó có độ cong trung bình là *hằng số khác $$0$$*, chứ không bằng $$0$$.)
- **Mặt yên ngựa (hoặc màng xà phòng mở):** hai bên màng đều tiếp xúc cùng áp suất khí quyển, nên để lực căng cân bằng, nếu mặt uốn lên theo hướng này ($$\kappa_1 > 0$$) thì nó buộc phải uốn xuống với đúng cường độ đó theo hướng vuông góc ($$\kappa_2 = -\kappa_1 < 0$$), khiến $$H = 0$$!

Nếu mặt là đồ thị $$z=u(x,y)$$, điều kiện $$H=0$$ trở thành **phương trình mặt tối thiểu**

$$
\mathrm{div}\!\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right)=0,
$$

một phương trình đạo hàm riêng elliptic tựa tuyến tính (quasilinear). Nghiệm của nó là đồ thị có diện tích nhỏ nhất so với các đồ thị lân cận có cùng giá trị trên biên (với điều kiện phù hợp). Tính phi tuyến đến từ việc phần tử diện tích là $$\sqrt{1+u_x^2+u_y^2}\,dx\,dy$$.

### Ví dụ tính toán cầm tay chỉ việc: tự tay kiểm tra $$H = 0$$ trên mặt Catenoid!

Xét mặt tròn xoay **catenoid** sinh bởi đường dây xích $$r(z) = a\cosh(z/a)$$ (với $$a > 0$$ là bán kính thắt eo tại $$z = 0$$). Ta có:
- Đạo hàm bậc nhất: $$r'(z) = \sinh(z/a)$$, suy ra $$\sqrt{1 + (r')^2} = \sqrt{1 + \sinh^2(z/a)} = \cosh(z/a)$$.
- Đạo hàm bậc hai: $$r''(z) = \frac{1}{a}\cosh(z/a)$$.

Tính trực tiếp hai độ cong chính của mặt tròn xoay tại độ cao $$z$$ bất kỳ:
1. **Độ cong dọc đường kinh tuyến** (uốn ra ngoài):
   $$\kappa_1 = \frac{r''}{(1 + r'^2)^{3/2}} = \frac{\frac{1}{a}\cosh(z/a)}{\cosh^3(z/a)} = \frac{1}{a\cosh^2(z/a)}.$$
2. **Độ cong dọc vòng tròn vĩ tuyến** (uốn ngược vào trục $$z$$):
   $$\kappa_2 = -\frac{1}{r\sqrt{1 + r'^2}} = -\frac{1}{a\cosh(z/a)\cdot \cosh(z/a)} = -\frac{1}{a\cosh^2(z/a)}.$$

Cộng hai kết quả lại: $$H = \frac{\kappa_1 + \kappa_2}{2} = 0$$ **triệt tiêu tuyệt đối tại mọi điểm $$z$$!** Hai độ uốn ngược chiều nhau vừa khít từng milimét ở khắp mặt catenoid.

### Khung giải thích: từ màng xà phòng đến phương trình đạo hàm riêng $$H = 0$$ (nên đọc chậm)

Tại sao một câu hỏi hình học cực kỳ đơn giản ("diện tích nhỏ nhất") lại biến thành phương trình độ cong trung bình $$H = 0$$? Hãy đi chậm qua 4 bước:

1. **Viết diện tích như một phiếm hàm năng lượng:** Sức căng bề mặt tỉ lệ trực tiếp với diện tích $$A[S] = \iint \sqrt{1 + u_x^2 + u_y^2}\,dx\,dy$$. Màng xà phòng tự co lại để giảm $$A[S]$$.
2. **Đẩy nhẹ mặt cong theo phương pháp tuyến:** Tạo họ mặt lân cận $$S_t$$ bằng cách dịch chuyển mỗi điểm trên $$S$$ đi một đoạn nhỏ $$t\cdot f$$ theo hướng pháp tuyến (giữ cố định khung dây biên).
3. **Tính tốc độ thay đổi diện tích ở bậc nhất (Công thức biến phân bậc nhất):** Tích phân từng phần cho thấy $$\left.\frac{d}{dt}\mathrm{Area}(S_t)\right\vert_{t=0} = -2\iint_S H f\,dA$$. Để diện tích dừng với *mọi* cách đẩy $$f$$, bắt buộc $$H \equiv 0$$ khắp mặt!
4. **Kiểm tra độ bền bằng biến phân bậc hai và cực tiểu toàn cục:** $$H=0$$ mới là điều kiện cần (điểm dừng). Như trong video catenoid bên dưới, khi kéo hai vòng vượt quá $$d \approx 1{,}06$$ bán kính, catenoid vẫn thỏa $$H=0$$ nhưng hai đĩa rời đã có diện tích nhỏ hơn; vượt quá $$d \approx 1{,}325$$, nghiệm catenoid biến mất và màng vỡ tức thì.

**Kiểm tra nhanh.** Một quả bóng bay hay bong bóng xà phòng tròn vo có phải là mặt tối thiểu không? Không — vì nó nhốt không khí bên trong nên áp suất trong lớn hơn ngoài, dẫn đến $$H = 1/R > 0$$ (độ cong trung bình hằng khác 0).

---

### Video ngắn: Màng xà phòng giữa hai vòng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/soap-film-catenoid_vi.mp4"></video>
</div>

Giữa hai vòng bán kính 1, màng là một catenoid. Khi hai vòng tách ra, diện tích màng tăng: từ khoảng 1,06 bán kính hai đĩa phẳng (diện tích $$2\pi \approx 6.28$$) đã có diện tích nhỏ hơn, và quá khoảng 1,33 bán kính thì không còn catenoid nào nên màng vỡ thành hai đĩa.


### Tự tay thử: Kéo hai vòng ra xa

<div class="mex-explainer" data-mex="catenoid" data-lang="vi"></div>


## 3. Các ví dụ cổ điển

**Mặt phẳng.** Cả hai độ cong chính đều bằng 0; mặt phẳng là mặt tối thiểu.

**Catenoid.** Mặt tròn xoay sinh ra khi quay đường dây xích $$r(z) = a\cosh(z/a)$$ quanh trục $$z$$. Hai vòng tròn đồng trục bán kính $$1$$ nhúng vào nước xà phòng sẽ giữ một màng hình catenoid thắt eo ở giữa. Khi kéo hai vòng tách dần ra, diện tích catenoid tăng lên: vượt quá khoảng cách $$d \approx 1{,}06$$, hai đĩa tròn phẳng rời nhau (tổng diện tích $$2\pi \approx 6{,}28$$) đã có diện tích nhỏ hơn (catenoid trở thành cực tiểu *địa phương* giả bền); và khi vượt quá ngưỡng tới hạn $$d \approx 1{,}325$$, phương trình không còn nghiệm catenoid nào nữa nên màng vỡ đột ngột thành hai đĩa phẳng — một bước nhảy tôpô ngoạn mục ngay trước mắt ta!

**Helicoid.** Mặt tối thiểu kẻ (ruled) có dạng cầu thang xoắn ốc; có thể hình dung nó như vết quét của một đường thẳng vừa tịnh tiến vừa quay như con vít. Helicoid và catenoid là cặp đôi cổ điển: có một họ biến dạng đẳng cự (không hề kéo giãn hay nhăn nheo khoảng cách trên mặt!) gồm toàn mặt tối thiểu nối liền mạch giữa chúng (họ liên kết, associate family; Bonnet).

**Mặt Scherk, mặt Enneper** và nhiều ví dụ khác. Biểu diễn Weierstrass–Enneper tạo ra mặt tối thiểu từ dữ liệu chỉnh hình: giải tích phức khoác áo hình học.

**Mặt Costa (1982).** Suốt hai trăm năm, người ta tin rằng chỉ có đúng ba mặt tối thiểu đầy đủ, không tự cắt, có tôpô hữu hạn trong $$\mathbb{R}^3$$: mặt phẳng, catenoid và helicoid. Năm 1982, Celso Costa tìm ra một công thức mới cho một mặt tối thiểu đầy đủ giống như mặt phẳng đâm xuyên qua catenoid với một "tay cầm" xuyến ở giữa; sau đó David Hoffman và William Meeks (nhờ trực quan hóa bằng đồ họa máy tính) đã chứng minh mặt này thực sự nhúng không tự cắt. Kết quả này lật đổ niềm tin tồn tại hai thế kỷ và mở ra kỷ nguyên hiện đại của việc xây dựng và phân loại mặt tối thiểu.

---

## 4. Tôpô, tính đầy đủ và phép nhúng

Những câu hỏi định hướng nghiên cứu:

- Những tôpô nào cho phép có mặt tối thiểu đầy đủ nhúng chìm (immersed) trong $$\mathbb{R}^3$$?
- Khi nào mặt tối thiểu là **nhúng** (không tự cắt), chứ không chỉ nhúng chìm?
- Các **đầu mút** (ends) của một mặt tối thiểu đầy đủ có thể có dạng nào?
- Mặt tối thiểu có **ổn định** dưới các biến phân có giá compact không?

Các định lý của Fischer-Colbrie, do Carmo, Schoen và những người khác ràng buộc chặt các mặt tối thiểu đầy đủ ổn định. Lý thuyết Colding–Minicozzi phân tích cấu trúc của các đĩa tối thiểu nhúng và các phân lá (lamination): giải tích sâu dẫn đến kết luận hình học. Ý chung: **điều kiện về độ cong cộng với tôpô dẫn đến tính cứng nhắc**.

---

## 5. Ngoài màng xà phòng: ứng dụng và các khái niệm liên quan

- **Khoa học vật liệu:** mặt phân cách có năng lượng cực tiểu; biên hạt; mặt mao dẫn (độ cong trung bình được ấn định, không nhất thiết bằng 0).
- **Kiến trúc:** kết cấu căng và phương pháp tìm hình (form-finding) lấy cảm hứng từ màng xà phòng (như mái vòm Sân vận động Olympic Munich của Frei Otto).
- **Thuyết tương đối rộng:** chân trời biểu kiến và các kỹ thuật mặt tối thiểu trong toán học của thuyết tương đối (như chứng minh định lý khối lượng dương của Schoen–Yau).
- **Giải tích hình học:** siêu mặt tối thiểu là công cụ để nghiên cứu đa tạp chứa nó (phương pháp min-max; sự tồn tại của nhiều siêu mặt tối thiểu).
- **Hình học calibrated:** phiên bản nhiều chiều, liên quan đến hình học lấy cảm hứng từ lý thuyết dây.

Mặt tối thiểu là cầu nối giữa **thị giác** và **giải tích**: thứ ta gần như nhìn thấy trong thí nghiệm khung dây trở thành phương trình đạo hàm riêng và cả một chương trình nghiên cứu.

---

## 6. Vì sao đẹp

Cùng một điều kiện $$H=0$$ sinh ra những hình dạng đa dạng đến bất ngờ, từ catenoid giản dị đến những mê cung hiện đại, nhưng tất cả đều xuất phát từ một ý hình học: **diện tích dừng** (đạo hàm diện tích bằng 0). Vẻ đẹp nằm ở sự thống nhất giữa nguyên lý biến phân, phương trình vi phân và lớp màng ta có thể chạm vào.

---

## 7. Nhầm lẫn thường gặp

1. "Tối thiểu nghĩa là diện tích nhỏ nhất toàn cục." Mặt tối thiểu là điểm tới hạn của diện tích; cực tiểu toàn cục chỉ là một lớp con.
2. "Màng xà phòng luôn tìm được cực tiểu tuyệt đối." Màng có thể ở trạng thái giả bền (metastable), và có những bước nhảy tôpô.
3. "$$H=0$$ nghĩa là phẳng." Catenoid và helicoid đều cong nhưng vẫn là mặt tối thiểu.
4. "Bài toán Plateau chỉ dành cho một vòng dây." Có các biến thể với biên gồm nhiều thành phần và có chướng ngại vật.
5. "Mọi mặt tối thiểu đều là đồ thị." Đồ thị chỉ là một lớp tiện lợi; mặt đầy đủ thường không phải là đồ thị trên toàn bộ.
6. "Mặt Costa khép lại chủ đề." Ngược lại, nó mở lại câu hỏi phân loại.

---

### Những ý chính về mặt tối thiểu (từ phần tìm hiểu video)

- Màng xà phòng gợi ra **bài toán Plateau**; toán học cần chứng minh sự tồn tại, độ trơn, và xét khả năng có điểm kỳ dị.
- **Độ cong trung bình bằng 0** là định nghĩa giải tích thường dùng.
- Catenoid và helicoid là những ví dụ mặt tối thiểu đầy đủ đầu tiên.

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/minimal-surfaces/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — Mathemaniac — Physics/math soap films & Plateau-style problems / minimal surfaces culture: [https://www.youtube.com/watch?v=Cvs8iRqG6lg](https://www.youtube.com/watch?v=Cvs8iRqG6lg).
2. **ORIENTATION** — Stand-up Maths / Parker soap film optimization demos: [https://www.youtube.com/watch?v=Cvs8iRqG6lg](https://www.youtube.com/watch?v=Cvs8iRqG6lg).
3. **CORE** — Camillo De Lellis — Plateau's problem lecture math videos: [https://www.youtube.com/watch?v=aTS69X-DBiA](https://www.youtube.com/watch?v=aTS69X-DBiA).
4. **FOUNDATION** — Mean curvature flow / minimal surface university lectures: [https://www.youtube.com/watch?v=aTS69X-DBiA](https://www.youtube.com/watch?v=aTS69X-DBiA).
5. **INTUITION** — Helicoid and catenoid classic visualizations: [https://www.youtube.com/watch?v=Cvs8iRqG6lg](https://www.youtube.com/watch?v=Cvs8iRqG6lg).
6. **FRONTIER** — CMSA / IAS geometry seminar samples (advanced): [https://www.youtube.com/watch?v=aTS69X-DBiA](https://www.youtube.com/watch?v=aTS69X-DBiA).

Danh mục URL đầy đủ: `research/video-research/minimal-surfaces/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/minimal-surfaces/transcripts/` · trạng thái: `research/video-research/minimal-surfaces/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/minimal-surfaces_Cvs8iRqG6lg_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/minimal-surfaces/references.md`.

### Video (lộ trình chính)

1. Mathemaniac — Physics/math soap films & Plateau-style problems / minimal surfaces culture — https://www.youtube.com/watch?v=Cvs8iRqG6lg
2. Stand-up Maths / Parker soap film optimization demos — https://www.youtube.com/watch?v=Cvs8iRqG6lg
3. Camillo De Lellis — Plateau's problem lecture math videos — https://www.youtube.com/watch?v=aTS69X-DBiA
4. Mean curvature flow / minimal surface university lectures — https://www.youtube.com/watch?v=aTS69X-DBiA
5. Helicoid and catenoid classic visualizations — https://www.youtube.com/watch?v=Cvs8iRqG6lg
6. CMSA / IAS geometry seminar samples (advanced) — https://www.youtube.com/watch?v=aTS69X-DBiA
7. Calculus of variations soap film intros — https://www.youtube.com/watch?v=Cvs8iRqG6lg
8. Course calculus essay variational section (internal) (FOUNDATION).

### Video (tìm thêm / phụ)

9. Architecture freeform / tensile structure math talks — https://en.wikipedia.org/wiki/Minimal_surface

### Bài báo, sách, OCW và web

10. Colding & Minicozzi — A Course in Minimal Surfaces (AMS): https://bookstore.ams.org/gsm-121
11. Wikipedia — Minimal surface: https://en.wikipedia.org/wiki/Minimal_surface
12. Wikipedia — Plateau's problem: https://en.wikipedia.org/wiki/Plateau%27s_problem
13. Wikipedia — Mean curvature: https://en.wikipedia.org/wiki/Mean_curvature
14. Wikipedia — Catenoid: https://en.wikipedia.org/wiki/Catenoid
15. Wikipedia — Helicoid: https://en.wikipedia.org/wiki/Helicoid

### Trong khóa

16. Liên kết: [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/), [Hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/), [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/). Gói: `research/video-research/minimal-surfaces/`.

## Hướng đi tiếp

Cùng tư duy biến phân: [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/). Những điều lạ trong hình học: [Hình học lạ]({{ site.baseurl }}/contents/vi/chapter04/04_06_Strange_Geometry/). Ràng buộc đối xứng: [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/). Mô hình môi trường liên tục: [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).

## Video tham khảo

- **Xem trước**: [How physics solves a math problem (and a 3D graphics problem)](https://www.youtube.com/watch?v=Cvs8iRqG6lg) (Mathemaniac, tiếng Anh). Màng xà phòng và cách vật lý giúp giải bài toán mặt tối thiểu. Nên xem trước khi đọc §1 và §2.
- [Camillo De Lellis (UZH) Pieces of soap films: boundaries and Plateau's problem](https://www.youtube.com/watch?v=aTS69X-DBiA) (Math UniPD, tiếng Anh). Bài giảng của Camillo De Lellis về màng xà phòng, biên và bài toán Plateau. Ở mức chuyên sâu hơn; xem sau khi đã nắm ý chính của bài.
