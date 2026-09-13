---
layout: post
title: "Cấu trúc chính quy của Hairer (Huy chương Fields 2014)"
chapter: '02'
order: 21
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Martin Hairer** nhận **Huy chương Fields 2014**

> “for his outstanding contributions to the theory of stochastic partial differential equations, and in particular for the creation of a theory of regularity structures for such equations.”
> — [IMU, Fields Medals 2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)

Citation nêu một **ngôn ngữ**, không phải tuyên bố mọi PDE ngẫu nhiên nay đều well-posed. Giải tích Itô cổ điển thuần hóa phương trình vi phân ngẫu nhiên thường trong những năm 1940. Các **phương trình đạo hàm riêng ngẫu nhiên (SPDE) kỳ dị**—phương trình có nghiệm thô đến mức số hạng phi tuyến là tích các phân phối—nằm ngoài giải tích ấy. **Cấu trúc chính quy** (regularity structures) của Hairer cung cấp khai triển kiểu Taylor cho các nghiệm đó, một định lý tái dựng biến jet trừu tượng thành phân phối thật, và một lược đồ tái chuẩn hóa-rồi-điểm bất động cho nghĩa chặt cho những phương trình nhà vật lý đã viết hàng thập niên.

Bài này nhằm sự thành thạo seminar: vì sao tích thất bại, KPZ và $$\Phi^4_3$$ động lực trông ra sao như case thử, cấu trúc chính quy đang cố là gì, và **phân phối paracontrol** (Gubinelli–Imkeller–Perkowski) ngồi cạnh lý thuyết Hairer như toolkit độc lập liên quan thế nào. Nó **không** tuyên bố bài Clay Navier–Stokes đã được giải, và **không** coi bằng tiến sĩ vật lý trước đó của Hairer là huy chương.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích, trong một đoạn, vì sao tích hai phân phối nói chung không xác định, và vì sao chướng ngại ấy xuất hiện trong SPDE phi tuyến với nhiễu trắng không-thời gian.
- Nêu hai phương trình kỳ dị (KPZ; $$\Phi^4_3$$ động lực) và nói “kỳ dị” nghĩa là gì với mỗi cái.
- Mô tả cấu trúc chính quy như **ngôn ngữ khai triển phân bậc**—đa thức Taylor được nâng cấp để gồm cả đơn thức xây từ nhiễu.
- Phát biểu slogan **định lý tái dựng**: một phân phối được mô hình trừu tượng xác định duy nhất một phân phối thật trông giống mô hình gần mọi điểm.
- Ghi công **rough path của Lyons** như tiền bối và **phân phối paracontrol** như cách tiếp cận song song, không phải phát minh của Hairer.
- Luyện độ chính xác: huy chương 2014 là lý thuyết SPDE / cấu trúc chính quy; tiến sĩ vật lý là tiểu sử; Navier–Stokes 3D tất định vẫn mở.

**Kiến thức nền.** Phương trình nhiệt và ý PDE; chuyển động Brown như đường liên tục nhưng không đâu khả vi; phân phối như phiếm hàm tuyến tính liên tục trên hàm thử. Tích phân ngẫu nhiên ở mức “nhiễu trắng là đạo hàm của Brown” là đủ. Không đòi giáo trình rough path trước.

**Liên kết seminar.** Đặt câu chuyện trên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) (bài đó đã gắn cờ SPDE của Hairer như bài toán well-posedness). Đối chiếu với [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (giới hạn kinetic tất định) và với [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (chính quy PDE phi tuyến *không* có nhiễu trắng không-thời gian).

---

## 1. Khi tích không tồn tại

Một phân phối Schwartz $$u\in\mathcal{S}'(\mathbb{R}^d)$$ có thể lấy đạo hàm bao nhiêu lần cũng được, nhưng không phải lúc nào cũng nhân được với phân phối khác. Tích từng điểm đòi đủ chính quy: nếu $$u$$ là độ đo và $$v$$ là hàm liên tục thì tích ổn; nếu cả hai thô như đạo hàm của Brown, nói chung **không có tích chính tắc**.

Nhiễu trắng không-thời gian $$\xi$$, nói không chính thức, là phân phối Gauss có hiệp phương sai là hàm delta. Nó thô hơn hàm rất nhiều. SPDE tuyến tính như phương trình nhiệt ngẫu nhiên

$$
\partial_t u=\Delta u+\xi
$$

vẫn có nghĩa: ta chập $$\xi$$ với nhân nhiệt và được một phân phối Hölder (ở một chiều không gian, roughly Hölder-$$1/2-$$ theo không gian). Rắc rối bắt đầu khi phương trình **phi tuyến** theo nghiệm ấy. Hai ví dụ chuẩn:

**Kardar–Parisi–Zhang (KPZ).** Mô hình giao diện tăng trưởng,

$$
\partial_t h=\partial_x^2 h+(\partial_x h)^2+\xi.
$$

Nghiệm $$h$$ được kỳ vọng thô như phương trình nhiệt ngẫu nhiên, nên $$\partial_x h$$ là phân phối, và $$(\partial_x h)^2$$ là tích bất hợp pháp.

**$$\Phi^4_3$$ động lực.** Lượng tử hóa ngẫu nhiên của trường $$\Phi^4$$ trong ba chiều không gian,

$$
\partial_t\Phi=\Delta\Phi-\Phi^3+\xi.
$$

Ở đây chính $$\Phi$$ nhận giá trị phân phối, và lập phương $$\Phi^3$$ lại không xác định như tích từng điểm.

“Kỳ dị” trong văn liệu này không nghĩa “ta chưa cố đủ.” Nó nghĩa phương trình ngây thơ **không phải PDE xác định tốt** cho đến khi người ta chỉ rõ một thủ tục giới hạn (làm trơn nhiễu, trừ các phân kỳ, chuyển sang giới hạn) và chứng minh giới hạn tồn tại.

---

## 2. Lộ trình của Hairer: từ KPZ đến một ngôn ngữ tổng quát

Hairer sinh tại Geneva năm 1975, học toán và vật lý tại Đại học Geneva, và viết luận án tiến sĩ **vật lý** (2001) dưới sự hướng dẫn của Jean-Pierre Eckmann. Bối cảnh ấy giải thích sự thoải mái của ông với các tính toán trường hình thức. Huy chương Fields là cho lý thuyết SPDE **toán học**.

Hai mạch trước đó quan trọng. Cùng **Jonathan Mattingly**, ông chứng minh ergodicity cho **Navier–Stokes ngẫu nhiên hai chiều** với nhiễu thoái hóa (Annals, 2006)—một định lý chất lỏng ngẫu nhiên, không phải bài Clay cho Navier–Stokes 3D tất định. Tách biệt, **rough path của Terry Lyons** đã chỉ ra rằng SDE thường bị dẫn bởi tín hiệu bất quy tắc có thể giải được nếu ta làm giàu tín hiệu bằng các tích phân lặp. Ghi chú IMU 2014 nói Hairer xây trên ý ấy.

Trong *Solving the KPZ equation* (Annals of Mathematics, 2013), Hairer cho KPZ một nghĩa theo đường đi bằng một cấu trúc chính quy thích nghi với phương trình ấy (sau các công trình Cole–Hopf và uniqueness liên quan trong cộng đồng xác suất). Cỗ máy tổng quát xuất hiện như *A theory of regularity structures* (Inventiones Mathematicae, 2014; arXiv:1303.5113): một khung xử lý KPZ, $$\Phi^4_3$$, mô hình Anderson parabolic, và một lớp lớn SPDE kỳ dị **parabolic dưới-tới hạn** theo cùng mẫu đại số-cộng-giải tích.

**Dưới-tới hạn** là slogan scale: sau khi đếm mũ nhiễu và phi tuyến, phương trình trở nên ít kỳ dị hơn ở scale nhỏ so với mô hình tới hạn. Cấu trúc chính quy không phải giấy phép viết một SPDE tùy ý rồi tuyên bố đã giải.

---

## 3. Cấu trúc chính quy: đa thức Taylor với đơn thức nhiễu

Một hàm $$C^\gamma$$ cổ điển $$f$$ trên $$\mathbb{R}^d$$ là hàm trông, gần mọi điểm $$x$$, giống đa thức Taylor bậc $$\lfloor\gamma\rfloor$$, với phần dư Hölder. Ý của Hairer là giữ “trông giống khai triển gần $$x$$” nhưng mở rộng danh sách đơn thức được phép.

Một **cấu trúc chính quy** là bộ ba $$(\mathcal{A},T,G)$$: một tập chỉ số $$\mathcal{A}\subset\mathbb{R}$$ các bậc thuần nhất, một không gian vector phân bậc $$T=\bigoplus_{\alpha\in\mathcal{A}}T_\alpha$$ có cơ sở hành xử như đơn thức trừu tượng (đa thức thường *và* các ký hiệu xây từ nhiễu), và một nhóm cấu trúc $$G$$ tái tâm khai triển từ điểm gốc này sang điểm gốc khác, theo cách đa thức Taylor biến đổi dưới $$x\mapsto y$$.

Một **mô hình** $$(\Pi,\Gamma)$$ hiện thực hóa các ký hiệu ấy thành phân phối thật: $$\Pi_x\tau$$ là “jet cụ thể của ký hiệu $$\tau$$ đặt tại $$x$$,” và $$\Gamma_{xy}$$ chuyển khai triển đặt tại $$y$$ thành khai triển đặt tại $$x$$. Các bound giải tích nói rằng $$\Pi_x\tau$$ scale như $$\lambda^{|\tau|}$$ khi thử trên bump bề rộng $$\lambda$$.

Một **phân phối được mô hình** rồi là một ánh xạ $$x\mapsto f(x)\in T$$ Hölder đối với $$\Gamma$$—một jet Taylor trừu tượng có hệ số biến thiên có kiểm soát. Cả lý thuyết mang tính địa phương và đại số cho đến khi tái dựng.

**Slogan.** Lý thuyết Taylor thường khai triển theo $$1,\,(y-x),\,(y-x)^2,\ldots$$. Một cấu trúc chính quy khai triển theo những cái ấy *và* theo một danh sách hữu hạn “đa thức làm từ nhiễu đã regularize,” được chọn sao cho phi tuyến của PDE nhân được trong không gian trừu tượng ngay cả khi không nhân được trong $$\mathcal{S}'$$.

---

## 4. Tái dựng, tái chuẩn hóa, điểm bất động

**Định lý tái dựng.** Cho một mô hình và một phân phối được mô hình $$f$$ có chính quy dương, tồn tại duy nhất một phân phối $$\mathcal{R}f$$ sao cho, gần mỗi $$x$$, $$\mathcal{R}f$$ trông giống $$\Pi_x f(x)$$ sai số Hölder kỳ vọng. Tái dựng là cầu từ đại số về giải tích: đó là lý do jet trừu tượng không chỉ là sổ sách.

**Tái chuẩn hóa.** Nếu ta làm trơn nhiễu thành $$\xi^\varepsilon$$ và xây mô hình tương ứng, nhiều tích phân kỳ khi $$\varepsilon\to 0$$. Người ta trừ (hoặc, bất biến hơn, tái tâm) một danh sách hữu hạn hằng số hoặc số hạng đối kháng địa phương—cùng bản năng tái chuẩn hóa trong lý thuyết trường lượng tử, nay như định lý rằng các mô hình đã tái chuẩn hóa hội tụ. Các nghiệm tái dựng rồi hội tụ tới một giới hạn mà ta *định nghĩa* là nghiệm của SPDE kỳ dị.

**Điểm bất động.** Trong không gian các phân phối được mô hình, PDE trở thành ánh xạ co trên thời gian ngắn (hoặc toàn cục trong các trường hợp tiêu tán), đúng như Picard iteration cho ODE trên không gian Banach. Tồn tại và uniqueness không siêu hình; chúng là định lý điểm bất động trên một không gian được thiết kế để tích bất hợp pháp trở nên hợp pháp.

Lý thuyết Hairer vì thế làm ba việc cùng lúc: nó **định nghĩa** phương trình, **xây** nghiệm, và **nhận diện** giới hạn của các regularize tự nhiên. Đó là vì sao văn bản IMU nói ông cho, lần đầu, một nghĩa nội tại chặt cho nhiều SPDE phát sinh từ vật lý.

---

## 5. Phân phối paracontrol: toolkit độc lập liên quan

Cùng những năm ấy, **Massimiliano Gubinelli**, **Peter Imkeller** và **Nicolas Perkowski** phát triển **phân phối paracontrol** (Forum of Mathematics, *Pi*, 2015; bản thảo arXiv:1210.2684). Ý tưởng thuộc giải tích Fourier hơn là lý thuyết jet: người ta dùng paraproduct Bony để nói rằng nghiệm $$u$$ bị “kiểm soát” bởi các đối tượng ngẫu nhiên tuyến tính xây từ nhiễu, và nhân trong calculus paraproduct.

Đây **không** phải phát minh của Hairer, và không phải hệ quả của cấu trúc chính quy. Đó là toolkit song song xử lý các họ SPDE kỳ dị chồng lấn (kể cả KPZ và $$\Phi^4_3$$). Công trình sau đã so, dịch, và đôi khi kết hợp hai ngôn ngữ; sự trung thực seminar đòi nêu cả hai.

Một láng giềng thứ ba, chỉ để định hướng, là lý thuyết **rough path** (Lyons) và các mở rộng rough path phân nhánh: cấu trúc chính quy có thể đọc như sự làm giàu triết lý ấy ở scale PDE.

---

## 6. Huy chương không phải là gì

Các ràng buộc độ chính xác cho khóa học này:

- **Không phải mọi SPDE.** Lý thuyết nhắm một lớp phương trình parabolic dưới-tới hạn. Các mô hình tới hạn và trên-tới hạn, bài hyperbolic, và nhiều phương trình chất lỏng vẫn nằm ngoài, hoặc chỉ một phần nằm trong, cỗ máy.
- **Không phải Clay Navier–Stokes.** Ergodicity Hairer–Mattingly là cho Navier–Stokes *ngẫu nhiên* 2D. Bài chính quy 3D tất định không bị cấu trúc chính quy giải quyết, và citation IMU không claim ngược lại.
- **Không phải “tiến sĩ vật lý nên Fields.”** Luận án giải thích khẩu vị và kỹ thuật; giải thưởng là lý thuyết SPDE.
- **Không phải tính duy nhất của phương pháp.** Calculus paracontrol, phương pháp năng lượng, và biến đổi Cole–Hopf giải một số phương trình cùng loại bằng đường khác.

Các ghế sau này (Warwick, Imperial, EPFL) và Breakthrough Prize 2021 không đổi câu 2014.

---

## 7. Vì sao quan trọng trên bản đồ hiện đại

SPDE kỳ dị ngồi nơi xác suất, PDE và lý thuyết trường lượng tử chung một bức tường: dễ viết, khó diễn giải. Cấu trúc chính quy đổi mặc định từ “hình thức” sang “điểm bất động đã tái chuẩn hóa” cho một lớp lớn được mô tả tường minh.

Với chương này, Hairer là chân dung **hạ tầng**: một phạm trù khai triển mới làm các đối tượng hình thức cũ trở nên hợp lệ. Một số huy chương Fields thưởng một ngôn ngữ.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Mọi SPDE nay đều well-posed.” | Một lớp lớn SPDE kỳ dị *parabolic dưới-tới hạn*; không phải lý thuyết tồn tại phổ quát. |
| “Hairer giải Navier–Stokes.” | Ông không giải bài Clay 3D tất định. Ergodicity 2D ngẫu nhiên là định lý khác. |
| “Phân phối paracontrol là một phần của cấu trúc chính quy.” | Gubinelli–Imkeller–Perkowski xây toolkit độc lập, liên quan. |
| “Nhiễu trắng là hàm, cứ nhân.” | Nhiễu trắng là phân phối; tích cần một lý thuyết. |
| “Tái dựng giống định lý Taylor.” | Nó *mở rộng* Taylor: jet gồm ký hiệu nhiễu, và đầu ra là phân phối. |
| “Fields là cho bằng tiến sĩ vật lý.” | Tiểu sử; citation là lý thuyết SPDE và cấu trúc chính quy. |

---

## Bài tập

1. Vì sao $$(\partial_x h)^2$$ không xác định nếu $$h$$ chỉ chính quy bằng phương trình nhiệt ngẫu nhiên một chiều? Trả lời bằng ngôn ngữ tích phân phối.
2. Viết phương trình $$\Phi^4_3$$ động lực và đánh dấu số hạng bất hợp pháp. “3” ở chỉ số dưới nói tới gì?
3. Trong một đoạn, **mô hình** thêm data gì vào cấu trúc chính quy trừu tượng $$(A,T,G)$$?
4. Phát biểu slogan tái dựng mà không dùng chữ “ma thuật.” Vì sao uniqueness của $$\mathcal{R}f$$ quan trọng khi định nghĩa PDE?
5. **Tái chuẩn hóa** đang làm gì trong câu chuyện này—hủy một lực vật lý, hay chỉ rõ giới hạn của các phương trình đã regularize?
6. Nêu một điều cấu trúc chính quy và phân phối paracontrol **chia sẻ**, và một cách chúng **khác** (jet vs paraproduct là đủ).
7. **Luyện độ chính xác.** Viết lại “Hairer giải mọi phương trình nhiễu, kể cả turbulence” thành hai câu có thể xuất hiện trong khóa học này.
8. **Seminar mở rộng.** Lướt những trang đầu Hairer, arXiv:1303.5113, và liệt kê năm từ cần học tiếp (ví dụ phân phối được mô hình, nhóm cấu trúc, dưới-tới hạn, đại số Hopf của cây, nhóm tái chuẩn hóa).

---

## Liên kết

- IMU Fields Medals 2014: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)
- Citation ngắn IMU (Hairer): [https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations)
- Ghi chú IMU, “The Work of Martin Hairer” (PDF): [https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_hairer.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_hairer.pdf)
- Wikipedia — Martin Hairer: [https://en.wikipedia.org/wiki/Martin_Hairer](https://en.wikipedia.org/wiki/Martin_Hairer)
- Wikipedia — Regularity structure: [https://en.wikipedia.org/wiki/Regularity_structure](https://en.wikipedia.org/wiki/Regularity_structure)
- Hồ sơ Quanta (2014): [https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/](https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/)
- Hairer, cấu trúc chính quy (arXiv:1303.5113): [https://arxiv.org/abs/1303.5113](https://arxiv.org/abs/1303.5113)
- Gubinelli–Imkeller–Perkowski (arXiv:1210.2684): [https://arxiv.org/abs/1210.2684](https://arxiv.org/abs/1210.2684)
- Tìm arXiv — Hairer KPZ: [https://arxiv.org/search/?query=Hairer+KPZ&searchtype=all](https://arxiv.org/search/?query=Hairer+KPZ&searchtype=all)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 2014 — Martin Hairer.
2. M. Hairer, “Solving the KPZ equation,” *Ann. of Math.* 178 (2013).
3. M. Hairer, “A theory of regularity structures,” *Invent. Math.* 198 (2014).
4. M. Gubinelli, P. Imkeller và N. Perkowski, “Paracontrolled distributions and singular PDEs,” *Forum Math. Pi* 3 (2015).
5. T. Lyons, lý thuyết rough path (tiền bối cho SDE theo đường đi).
6. M. Hairer và J. Mattingly, “Ergodicity of the 2D Navier–Stokes equations with degenerate stochastic forcing,” *Ann. of Math.* 164 (2006) — 2D ngẫu nhiên, không phải Clay 3D.
7. Khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

---

## Hướng đi tiếp

- So biến đổi Cole–Hopf cho KPZ với xây dựng cấu trúc chính quy: một cái khai thác một phép đổi ẩn đặc biệt; cái kia scale sang phương trình không có mẹo ấy.
- Câu seminar: tái chuẩn hóa ở đây giống và khác tái chuẩn hóa trong lý thuyết trường lượng tử xây dựng ở những điểm nào?
