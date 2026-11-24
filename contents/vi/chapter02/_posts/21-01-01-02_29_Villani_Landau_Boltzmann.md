---
layout: post
title: "Landau damping phi tuyến và phương trình Boltzmann của Villani (Huy chương Fields 2010)"
chapter: '02'
order: 29
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy đặt hai bức tranh vật lý tưởng chừng trái ngược nhau cạnh nhau. Bức tranh thứ nhất là một bình khí loãng: hàng tỷ tỷ phân tử bay hỗn loạn và va chạm chan chát vào nhau, sinh ra entropy và dần dàn phẳng nhiệt độ về trạng thái cân bằng Maxwell. Bức tranh thứ hai là một đám mây **plasma** nóng rực ngoài không gian (hoặc trong lò phản ứng nhiệt hạch): các hạt điện tích loãng đến mức **hầu như không bao giờ va chạm trực tiếp với nhau**, phương trình chuyển động hoàn toàn thuận nghịch theo thời gian và entropy *không hề tăng*. Ấy vậy mà vào năm 1946, nhà vật lý **Lev Landau** tiên đoán một hiện tượng nghịch lý: chỉ cần thả một dao động điện trường vào đám mây plasma không va chạm đó, điện trường vĩ mô vẫn tự động **tắt dần theo hàm mũ** như thể có ma sát!

Suốt hơn sáu thập kỷ, câu hỏi liệu "ma sát không va chạm" kỳ lạ đó có còn sống sót khi đưa số hạng **phi tuyến** thực sự vào phương trình hay không — và tốc độ hội tụ về cân bằng của một chất khí **không thuần nhất** theo phương trình Boltzmann nhanh đến mức nào — vẫn là hai thách thức lớn của lý thuyết động học. Năm 2010, **Cédric Villani** nhận **Huy chương Fields**:

> “For his proofs of nonlinear Landau damping and convergence to equilibrium for the Boltzmann equation.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

*Tạm dịch: vì các chứng minh về hiện tượng tắt dần Landau phi tuyến và sự hội tụ về trạng thái cân bằng của phương trình Boltzmann.*

Có một hiểu lầm rất phổ biến cần làm sáng tỏ ngay đầu bài: dù Villani nổi tiếng khắp thế giới nhờ hai bộ sách kinh điển về **vận chuyển tối ưu** (*Topics in Optimal Transportation* và *Optimal Transport: Old and New*), lời trao giải năm 2010 của IMU **không** nói về vận chuyển tối ưu (mảng đó được trình bày ở [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/)). Huy chương 2010 tôn vinh hai kiệt tác về **phương trình động học**: chứng minh **tắt dần Landau phi tuyến** (cùng **Clément Mouhot**) cho phương trình Vlasov–Poisson, và chứng minh **tốc độ hội tụ về cân bằng** cho phương trình Boltzmann không thuần nhất (cùng **Laurent Desvillettes**, cùng chương trình **hypocoercivity** của Villani). Đồng thời, cuốn sách bán chạy *Théorème vivant* (*Birth of a Theorem*) là một tác phẩm hồi ký hấp dẫn về quá trình nghiên cứu cùng Mouhot, không phải bài báo khoa học.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt rành mạch hai khung vật lý đối lập: phương trình **Vlasov** (không va chạm, thuận nghịch, trường tự hợp) của tắt dần Landau và phương trình **Boltzmann** (có va chạm, tăng entropy) của xu hướng về cân bằng.
- Giải thích trực quan cơ chế **trộn pha** (*phase mixing*) đằng sau phát hiện năm 1946 của Landau: vì sao điện trường vĩ mô có thể tắt dần mà không cần va chạm hay mất năng lượng.
- Ghi công đúng cho **Mouhot–Villani** trong định lý tắt dần Landau phi tuyến (với dữ kiện giải tích / Gevrey, vượt qua hiện tượng "tiếng vọng plasma").
- Mô tả định lý $$H$$ của Boltzmann và giải thích vì sao trường hợp **không thuần nhất theo không gian** lại khó hơn rất nhiều so với trường hợp thuần nhất.
- Giải thích trực quan ý tưởng **hypocoercivity**: khi sự tiêu tán chỉ tác động lên vận tốc $$v$$, quá trình vận chuyển theo không gian $$x$$ giúp "trộn" sự tiêu tán sang cả không gian pha.
- Nhận rõ rằng định lý hội tụ của **Desvillettes–Villani** là một định lý **có điều kiện** (giả thiết trước về độ trơn, suy giảm và tính dương), không phải lý thuyết chính quy toàn cục không điều kiện.
- Tách bạch lời trao giải năm 2010 khỏi các chuyên khảo về **vận chuyển tối ưu** và cuốn hồi ký *Birth of a Theorem*.

**Kiến thức nền.** Phương trình vi phân thường và phương trình đạo hàm riêng ở mức một giáo trình giải tích nghiêm túc đầu tiên; hàm mật độ xác suất $$f(t,x,v)$$ trên không gian vị trí–vận tốc; entropy như một hàm Lyapunov. Biết cơ học Hamilton và biến đổi Fourier sẽ giúp hiểu tắt dần Landau, nhưng không bắt buộc.

**Liên kết với các bài khác.** Bài này minh họa một chương trình biến cơ chế vật lý thành các đánh giá toán học. Đọc cùng [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/) cho mảng còn lại của Villani, và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) cho bối cảnh rộng hơn. Người cùng năm: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/).

---

## Bản đồ kiến thức nền: Lý thuyết động học, trộn pha và hypocoercivity là gì?

Trước khi đi vào các phương trình, hãy nắm ba hình ảnh trực quan cực kỳ gần gũi cho thấy điều gì thực sự xảy ra bên trong chất khí và plasma.

**1. Không gian pha $$(x, v)$$ — tấm bản đồ của chất khí.**
Thay vì theo dõi từng phân tử trong $$10^{23}$$ hạt (điều bất khả thi), **lý thuyết động học** mô tả cả đám mây hạt bằng một hàm mật độ $$f(t, x, v) \ge 0$$: tại thời điểm $$t$$, có bao nhiêu hạt đang ở quanh vị trí $$x$$ và bay với vận tốc $$v$$. Khi lấy tích phân theo mọi vận tốc, $$\rho(t,x) = \int f(t,x,v)\,dv$$ cho ta mật độ vật chất quan sát được ở vị trí $$x$$.

**2. Trộn pha (Phase mixing) — hình ảnh đoàn vận động viên chạy quanh sân vận động.**
Hãy tưởng tượng 10.000 vận động viên xuất phát cùng lúc tại vạch xuất phát trên một đường chạy vòng tròn, nhưng mỗi người chạy với một vận tốc không đổi $$v$$ khác nhau (phân bố mượt quanh một vận tốc trung bình). Họ **không hề va chạm** vào nhau và **không ai chạy chậm lại** cả! Thế nhưng chỉ sau vài vòng, người nhanh vượt xa người chậm, đám đông bị kéo giãn thành những dải xoắn ốc ngày càng mảnh trong không gian $$(x,v)$$. Nếu bạn đứng ở khán đài chỉ đếm **tổng số người ở mỗi đoạn đường chạy** (tức lấy trung bình theo vận tốc $$v$$), bạn sẽ thấy mật độ vận động viên dọc theo vòng chạy phẳng lỳ đều tăm tắp — mọi dao động đám đông ban đầu đã **tắt hẳn**! Đó chính xác là cơ chế của **tắt dần Landau**: thông tin không biến mất mà bị đẩy dần sang các tần số vận tốc cực cao!

**3. Hypocoercivity — khuấy một tách cà phê sữa chỉ chạm thìa ở một chiều.**
Trong phương trình Boltzmann, va chạm giữa các phân tử chỉ làm mượt và đưa phân bố **vận tốc $$v$$** về hình chuông Maxwell, chứ không trực tiếp di chuyển các hạt từ đầu phòng này sang đầu phòng kia (biến **vị trí $$x$$**). Vậy tại sao một căn phòng có góc nóng, góc lạnh cuối cùng vẫn đạt nhiệt độ đều khắp nơi? Vì các hạt bay tự do theo số hạng vận chuyển $$v \cdot \nabla_x$$, liên tục trộn lẫn các vị trí với nhau rồi lại bị va chạm hãm vận tốc! Trong giải tích, một hệ có thành phần tiêu tán bị "khuyết chiều" (chỉ hãm theo $$v$$) nhưng nhờ kết hợp với thành phần bảo toàn không giao hoán (vận chuyển theo $$x$$) mà vẫn suy giảm toàn cục về cân bằng được Villani đặt tên là **hypocoercivity**.

---

## 1. Hai thế giới của lý thuyết động học

Huy chương Fields 2010 kết nối hai phương trình nền tảng nằm ở hai thái cực của lý thuyết động học:

**Thế giới không va chạm — Phương trình Vlasov–Poisson:** Mô tả các hạt tích điện trong plasma (hoặc các ngôi sao trong thiên hà tương tác bằng lực hấp dẫn). Các hạt không đụng nhau trực tiếp mà cùng chuyển động trong trường lực tự hợp $$E[f]$$ sinh ra bởi mật độ tổng $$\rho(t,x) = \int f\,dv - 1$$:

$$
\partial_t f + v\cdot\nabla_x f + E[f]\cdot\nabla_v f = 0.
$$

Phương trình này hoàn toàn **thuận nghịch theo thời gian** và bảo toàn mọi chuẩn $$L^p$$ cũng như entropy $$\int f \log f$$! Không có định lý $$H$$ nào kéo $$f$$ về cân bằng theo nghĩa mạnh; sự tắt dần duy nhất có thể xảy ra là hội tụ yếu do **trộn pha** (điện trường $$E[f]$$ tắt về $$0$$ khi $$f$$ bị kéo thành sợi mảnh).

**Thế giới có va chạm — Phương trình Boltzmann:** Mô tả chất khí trung hòa nơi các phân tử va chạm từng đôi một theo toán tử va chạm song tuyến tính $$Q(f,f)$$:

$$
\partial_t f + v\cdot\nabla_x f = Q(f,f).
$$

Tại đây, **định lý $$H$$ của Boltzmann** khẳng định phiếm hàm $$H(f) = \int f \log f\,dx\,dv$$ luôn giảm (tức entropy vật lý luôn tăng), và $$H(f)$$ chỉ ngừng giảm khi $$f$$ là một **phân bố cân bằng Maxwell** (hình chuông Gauss theo vận tốc). Câu hỏi toán học lớn là: nghiệm tiến về cân bằng Maxwell *nhanh đến mức nào* khi chất khí ban đầu không đồng nhất trong không gian?

---

## 2. Tắt dần Landau: từ bài toán tuyến tính 1946 đến đột phá phi tuyến

Năm 1946, **Lev Landau** tuyến tính hóa phương trình Vlasov–Poisson quanh một trạng thái cân bằng thuần nhất $$f^0(v)$$ (như phân bố Maxwell). Bằng biến đổi Fourier theo không gian và giải tích phức trên mặt phẳng vận tốc (đường tích phân Landau), ông chứng minh rằng nếu $$f^0$$ thỏa điều kiện ổn định Penrose, thì điện trường $$E(t,x)$$ tắt nhanh theo hàm mũ $$e^{-\lambda t}$$ — mặc dù không có chút va chạm nào!

**Vì sao bài toán phi tuyến lại đứng vững suốt 65 năm?** Khi giữ lại số hạng phi tuyến $$E[f] \cdot \nabla_v f$$, các sợi mảnh trong không gian pha có thể tự tương tác ngược lại với nhau và tạo ra hiện tượng vật lý nổi tiếng gọi là **tiếng vọng plasma** (*plasma echoes*): một dao động tưởng đã tắt lịm bỗng "sống dậy" mạnh mẽ sau một khoảng thời gian nhờ cộng hưởng tần số! Nếu chuỗi tiếng vọng này khuếch đại nối tiếp nhau, chúng sẽ phá tan hoàn toàn sự tắt dần tuyến tính.

Trong bài báo đồ sộ dài gần 200 trang *"On Landau damping"* (*Acta Mathematica* 207, 2011; [arXiv:0904.2760](https://arxiv.org/abs/0904.2760)), **Clément Mouhot và Cédric Villani** đã chinh phục hoàn toàn bài toán phi tuyến cho plasma tuần hoàn (trên hình xuyến $$\mathbb{T}^d$$): với mọi nhiễu ban đầu đủ nhỏ có độ chính quy **giải tích** (hoặc trong lớp **Gevrey** đủ cao — mở rộng về sau của Bedrossian–Masmoudi–Mouhot còn sắc nét hơn), và với thế tương tác không kỳ dị hơn thế Coulomb/Newton, điện trường $$E(t)$$ vẫn **tắt theo hàm mũ** về $$0$$, mật độ không gian hội tụ về hằng số, còn hàm phân bố $$f(t)$$ hội tụ yếu về một trạng thái cân bằng thuần nhất gần đó!

**Ý tưởng đột phá của Mouhot–Villani:**
1. **Đánh đổi tính chính quy lấy sự suy giảm:** Họ theo dõi chuẩn giải tích *giảm dần bán kính hội tụ theo thời gian* đo dọc theo chuyển động vận chuyển tự do — biến "trộn pha" thành sự chuyển dịch năng lượng sang tần số cao.
2. **Thuần hóa tiếng vọng plasma:** Họ thiết lập các đánh giá tinh vi chứng minh chuỗi tiếng vọng phi tuyến tuy có xuất hiện nhưng bị kìm hãm bởi lớp chính quy giải tích/Gevrey, không kịp bùng nổ trước khi trộn pha dập tắt điện trường.
3. **Sơ đồ lặp kiểu Newton–KAM:** Họ giải phương trình phi tuyến bằng phép lặp giống lý thuyết KAM (Kolmogorov–Arnold–Moser) trong cơ học thiên thể.

(Lưu ý quan trọng: định lý yêu cầu độ chính quy cao — với dữ kiện chỉ thuộc không gian Sobolev bậc thấp, tiếng vọng thực sự *có thể* phá hủy tắt dần Landau! Và cần luôn ghi công song song **Mouhot–Villani**, không chỉ một mình Villani.)

---

## 3. Phương trình Boltzmann: entropy, tính không thuần nhất và các điều kiện

Với phương trình Boltzmann **thuần nhất theo không gian** ($$f$$ chỉ phụ thuộc $$t, v$$, không phụ thuộc $$x$$), lý thuyết định lượng về định lý $$H$$ đã phát triển mạnh từ lâu (trong đó chính Villani chứng minh bài báo nổi tiếng *"Cercignani's conjecture is sometimes true and always almost true"*, 2003, lượng hóa tốc độ sinh entropy $$D(f) \ge c (H(f) - H(M))^{1+\varepsilon}$$).

Nhưng với chất khí **không thuần nhất theo không gian** ($$f(t,x,v)$$ trong một hộp kín hoặc trên hình xuyến), một bẫy lớn xuất hiện: có thể tồn tại những trạng thái **cân bằng địa phương** — tại mỗi điểm $$x$$, phân bố vận tốc đã là hình chuông Maxwell nên toán tử va chạm $$Q(f,f) = 0$$ (sự sinh entropy bằng $$0$$!), nhưng nhiệt độ hay mật độ giữa các điểm $$x$$ khác nhau vẫn chưa đều nhau! Một phân bố như vậy không nằm ở cân bằng toàn cục, nhưng tại đúng thời điểm đó entropy lại tạm thời ngừng tăng!

Trong bài báo bước ngoặt năm 2005 (*Inventiones Mathematicae* 159), **Laurent Desvillettes và Cédric Villani** giải bài toán này và chứng minh rằng nghiệm hội tụ về cân bằng Maxwell toàn cục với tốc độ **nhanh hơn mọi lũy thừa của thời gian** ($$O(t^{-\infty})$$). Chiến lược của họ cực kỳ sắc sảo:
- Kết hợp định lý $$H$$ định lượng (nếu $$f$$ xa cân bằng địa phương thì entropy tăng nhanh);
- Với một định lý về **tính không ổn định của chế độ thủy động lực** (nếu $$f$$ tiến sát một cân bằng địa phương *không đồng nhất*, số hạng vận chuyển $$v \cdot \nabla_x$$ lập tức kéo nó *rời khỏi* lớp cân bằng địa phương, buộc sự sinh entropy phải bật sáng trở lại!);
- Cùng các bất đẳng thức hình học (kiểu bất đẳng thức Korn) để biến sự bật-tắt liên hồi đó thành tốc độ suy giảm toàn cục $$O(t^{-\infty})$$.

Cần lưu ý tính trung thực của định lý: kết quả Desvillettes–Villani là **có điều kiện** — họ giả thiết trước rằng nghiệm đang xét có độ trơn đều, suy giảm tốt theo vận tốc và có chặn dưới dương (những tính chất vốn cực khó chứng minh không điều kiện cho dữ kiện ban đầu lớn). Đó là định lý về **cơ chế và tốc độ hội tụ**, không phải lời giải cho bài toán mở về tính chính quy toàn cục của phương trình Boltzmann với dữ kiện lớn bất kỳ.

---

## 4. Hypocoercivity, vận chuyển tối ưu và vì sao được Fields

Từ kinh nghiệm với phương trình Boltzmann và Fokker–Planck động học, Villani khái quát hóa cơ chế "tiêu tán suy biến + trộn vận chuyển $$\Rightarrow$$ suy giảm về cân bằng" thành một lý thuyết hệ thống mang tên **Hypocoercivity** (*Memoirs of the AMS*, 2009), lấy cảm hứng từ định lý hypoellipticity của Hörmander (dùng giao hoán tử $$[A, B]$$ để sinh ra hướng tiêu tán còn thiếu). Hypocoercivity không chỉ cho thấy hệ tiến về cân bằng, mà còn cho **tốc độ tường minh** (như hàm mũ hoặc $$O(t^{-\infty})$$) thay vì lập luận compact định tính không rõ nhanh chậm.

Còn về **vận chuyển tối ưu** (khoảng cách Wasserstein $$W_p$$, hai cuốn sách kinh điển, và lý thuyết độ cong Ricci tổng hợp **Lott–Villani** / Sturm): đó là một trụ cột song song cực kỳ đồ sộ trong sự nghiệp Villani, ảnh hưởng sâu sắc tới cả hình học lẫn giải tích (và nối trực tiếp tới học trò của ông là [Alessio Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), Fields 2018). Hãy luôn tách rõ hai ngăn: **Fields 2010 = tắt dần Landau phi tuyến (Mouhot–Villani) + hội tụ về cân bằng của phương trình Boltzmann (Desvillettes–Villani, hypocoercivity)**; còn **vận chuyển tối ưu** là mảng đóng góp lớn song hành ngoài lời trao giải năm 2010.

Lý do Villani nhận Huy chương Fields 2010 rất rõ ràng: suốt hơn nửa thế kỷ, lý thuyết động học có hai trụ cột vật lý nổi tiếng (tắt dần Landau 1946 và định lý $$H$$ của Boltzmann) nhưng lại thiếu những định lý phi tuyến định lượng tương xứng. Mouhot–Villani đã biến phép tính tuyến tính của Landau thành một định lý phi tuyến chặt chẽ bằng kỹ thuật giải tích KAM; còn Desvillettes–Villani đã biến câu nói định tính "entropy tăng" thành một định lý tốc độ hội tụ tường minh cho chất khí không thuần nhất.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Huy chương 2010 là về vận chuyển tối ưu." | Lời trao giải của IMU nói về tắt dần Landau và cân bằng của phương trình Boltzmann. Vận chuyển tối ưu là một mảng lớn riêng trong sự nghiệp của ông. |
| "Một mình Villani chứng minh tắt dần Landau phi tuyến." | Định lý là của **Mouhot–Villani**. |
| "Landau đã chứng minh kết quả phi tuyến năm 1946." | Phân tích của Landau là **tuyến tính**. Bài toán phi tuyến còn mở trong nhiều thập niên. |
| "Desvillettes–Villani cho nghiệm trơn toàn cục không điều kiện của phương trình Boltzmann." | Tốc độ của họ **có điều kiện** về độ chính quy, độ suy giảm và tính dương, như nêu trong bài báo. |
| "*Birth of a Theorem* là một bài báo." | Đó là hồi ký (bản tiếng Pháp 2012, tiếng Anh 2015), không phải bài nghiên cứu. |
| "Tắt dần Landau là nhờ va chạm." | Đó là hiện tượng **không va chạm** (phương trình Vlasov); phương trình Boltzmann là vế có va chạm trong lời trao giải. |

---

## Bài tập

1. Viết bốn câu mà một nhà vật lý có thể chấp nhận: tắt dần Landau tuyến tính là gì, và vì sao tính thuận nghịch của phương trình Vlasov không mâu thuẫn ngay với nó?
2. Vì sao số hạng phi tuyến đe dọa sự suy giảm tuyến tính? Trả lời ngắn gọn (tiếng vọng / cộng hưởng), không cần dựng lại bài báo trên *Acta*.
3. Nêu sự khác nhau giữa một định lý **có điều kiện** về xu hướng tiến tới cân bằng và một định lý về **tính chính quy toàn cục**. Kết quả Desvillettes–Villani năm 2005 thuộc loại nào?
4. Giải thích hypocoercivity trong một đoạn: tiêu tán suy biến + trộn $$\Rightarrow$$ suy giảm. Vẽ một hình minh họa (vận chuyển theo $$x$$, va chạm theo $$v$$).
5. Mở cuốn *Topics in Optimal Transportation* hoặc bài [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), viết ba câu so sánh bài toán Monge với bài toán Kantorovich, rồi thêm một câu giải thích vì sao nội dung đó **không** thuộc lời trao giải năm 2010.
6. Luyện ghi công: viết cho **Landau (1946)**, **Mouhot**, **Desvillettes** và **Villani** mỗi người một mệnh đề chính xác.
7. **Luyện phát biểu chính xác.** Viết lại câu "Villani chứng minh entropy luôn dập tắt hỗn loạn ngay lập tức" thành hai câu đúng, phù hợp với khóa học.
8. **Thảo luận.** So sánh huy chương này với [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/): cả hai đều thuộc "vật lý thống kê", nhưng một bên là mô hình lưới / hình học bảo giác, bên kia là phương trình động học / phương trình đạo hàm riêng. Trong mỗi câu chuyện, "giới hạn thang đo" nghĩa là gì?

---

## Liên kết

- IMU Fields Medals 2010 (chỉ mục được yêu cầu): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- Trang Villani IMU / ICM 2010: [Fields Medal – Cédric Villani](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-cedric-villani.html)
- Wikipedia: [Cédric Villani](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani)
- arXiv: [0904.2760](https://arxiv.org/abs/0904.2760) (Mouhot–Villani); tìm [Desvillettes Villani Boltzmann](https://arxiv.org/search/?query=Desvillettes+Villani+Boltzmann&searchtype=all)
- Khóa học: [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/)

---

## Tài liệu tham khảo

1. International Mathematical Union, citation Fields Medals 2010 cho Cédric Villani (tài liệu IMU / ICM Hyderabad 2010).
2. **C. Mouhot and C. Villani**, “On Landau damping,” *Acta Math.* 207 (2011), 29–201, arXiv:0904.2760.
3. **L. Desvillettes and C. Villani**, “On the trend to global equilibrium for spatially inhomogeneous kinetic systems: The Boltzmann equation,” *Invent. Math.* 159 (2005), 245–316.
4. **C. Villani**, *Hypocoercivity*, Mem. Amer. Math. Soc. 202 (2009), no. 950.
5. **C. Villani**, *Topics in Optimal Transportation*, Grad. Stud. Math. 58, AMS, 2003; *Optimal Transport: Old and New*, Grundlehren 338, Springer, 2009. (Bối cảnh; không phải citation Fields.)
6. **C. Villani**, *Théorème vivant*, Grasset, 2012; bản Anh *Birth of a Theorem*, Farrar, Straus and Giroux, 2015. (Hồi ký, không phải bài nghiên cứu.)
7. Wikipedia, [Cédric Villani](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani); các chương khóa học đã dẫn.

---

## Hướng đi tiếp

- Đọc phần mở đầu bài Mouhot–Villani (trộn pha khác với mất năng lượng thế nào) trước khi đọc phần về các chuẩn giải tích. So sánh định lý $$H$$ cho trường hợp thuần nhất với sơ đồ chứng minh của Desvillettes–Villani cho trường hợp không thuần nhất.
- Câu hỏi thảo luận: bạn đoán tắt dần Landau phi tuyến có thể không còn đúng với lớp chính quy nào, và vì sao điều đó không mâu thuẫn với định lý trên *Acta*?

## Video tham khảo

- **Xem trước**: [Conferências Magnas: Cédric Villani - Large particle systems and Landau damping (2012)](https://www.youtube.com/watch?v=3Aa1Fyd1pW0) (Instituto de Matemática Pura e Aplicada, tiếng Anh). Bài giảng lớn của Villani tại IMPA về hệ nhiều hạt và tắt dần Landau. Nên xem trước để nắm sự khác nhau giữa mô hình không va chạm và mô hình có va chạm.
- [Cédric Villani - From KAM Theory to Landau Damping, IHP 30/09/2013 - Part 1](https://www.youtube.com/watch?v=pHJV-E1EOA8) (Institut Henri Poincaré, tiếng Anh). Phần đầu bài giảng nối lý thuyết KAM với tắt dần Landau, đúng với mạch chứng minh ở mục 2.
- [Landau damping: Gevrey regularity and paraproducts - Clément Mouhot](https://www.youtube.com/watch?v=eja7NTV7Igs) (Institute for Advanced Study, tiếng Anh). Bài giảng của đồng tác giả Mouhot về lớp chính quy Gevrey và kỹ thuật paraproduct. Dành cho người muốn đi sâu vào kỹ thuật sau khi đọc xong bài.
