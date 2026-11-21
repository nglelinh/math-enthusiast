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

*Tạm dịch: vì những đóng góp xuất sắc cho lý thuyết phương trình đạo hàm riêng ngẫu nhiên, đặc biệt là việc xây dựng lý thuyết cấu trúc chính quy cho các phương trình này.*

Lời trao giải nói về một **ngôn ngữ** mới. Nó không nói rằng mọi phương trình đạo hàm riêng ngẫu nhiên nay đều có nghiệm tốt. Giải tích Itô cổ điển, ra đời từ những năm 1940, đã xử lý được phương trình vi phân ngẫu nhiên thường. Nhưng nó không xử lý được các **phương trình đạo hàm riêng ngẫu nhiên (SPDE) kỳ dị**. Đó là những phương trình có nghiệm thô đến mức số hạng phi tuyến trở thành tích của các phân phối. **Cấu trúc chính quy** (regularity structures) của Hairer cho ba công cụ: một kiểu khai triển giống khai triển Taylor cho các nghiệm đó, một định lý tái dựng để biến khai triển trừu tượng thành phân phối thật, và một quy trình "tái chuẩn hóa rồi tìm điểm bất động". Nhờ vậy, các phương trình mà nhà vật lý đã viết ra từ nhiều thập niên trước lần đầu có nghĩa toán học chặt chẽ.

Bài này giúp bạn đủ hiểu để theo dõi một buổi seminar. Ta sẽ xem vì sao phép nhân thất bại, hai ví dụ thử là KPZ và $$\Phi^4_3$$ động lực, cấu trúc chính quy làm gì, và **phân phối paracontrol** (Gubinelli–Imkeller–Perkowski), một bộ công cụ độc lập, liên quan thế nào với lý thuyết của Hairer. Bài **không** nói bài toán Navier–Stokes của Viện Clay đã được giải. Bài cũng **không** coi bằng tiến sĩ vật lý của Hairer là lý do được huy chương.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích trong một đoạn vì sao tích của hai phân phối nói chung không xác định, và vì sao trở ngại này xuất hiện trong SPDE phi tuyến có nhiễu trắng không-thời gian.
- Nêu hai phương trình kỳ dị (KPZ và $$\Phi^4_3$$ động lực) và giải thích "kỳ dị" nghĩa là gì trong từng trường hợp.
- Mô tả cấu trúc chính quy như một **ngôn ngữ khai triển phân bậc**: đa thức Taylor được mở rộng để chứa thêm các đơn thức xây từ nhiễu.
- Phát biểu ý chính của **định lý tái dựng**: một phân phối được mô hình hóa (trừu tượng) xác định duy nhất một phân phối thật, và phân phối thật này gần mỗi điểm trông giống mô hình.
- Ghi đúng công: **đường thô (rough path) của Lyons** là công trình đi trước, còn **phân phối paracontrol** là cách tiếp cận song song. Cả hai không phải phát minh của Hairer.
- Phát biểu chính xác: huy chương 2014 trao cho lý thuyết SPDE và cấu trúc chính quy; bằng tiến sĩ vật lý chỉ là tiểu sử; bài toán Navier–Stokes 3D tất định vẫn còn mở.

**Kiến thức nền.** Phương trình nhiệt và khái niệm phương trình đạo hàm riêng; chuyển động Brown là đường liên tục nhưng không khả vi tại bất kỳ điểm nào; phân phối là phiếm hàm tuyến tính liên tục trên các hàm thử. Về tích phân ngẫu nhiên, chỉ cần hiểu "nhiễu trắng là đạo hàm của chuyển động Brown". Không cần học trước lý thuyết đường thô.

**Liên kết với các bài khác.** Đặt câu chuyện này lên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/). Bài đó đã nêu SPDE của Hairer như một bài toán về tính đặt đúng (well-posedness). So sánh với [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (giới hạn động học tất định) và với [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (tính chính quy của PDE phi tuyến *không* có nhiễu trắng không-thời gian).

---

## 1. Khi tích không tồn tại

Một phân phối Schwartz $$u\in\mathcal{S}'(\mathbb{R}^d)$$ lấy đạo hàm bao nhiêu lần cũng được, nhưng không phải lúc nào cũng nhân được với một phân phối khác. Muốn nhân từng điểm thì các nhân tử phải đủ chính quy. Nếu $$u$$ là một độ đo và $$v$$ là hàm liên tục thì tích vẫn xác định. Nếu cả hai đều thô như đạo hàm của chuyển động Brown thì nói chung **không có cách nhân chính tắc**.

Nhiễu trắng không-thời gian $$\xi$$, nói nôm na, là một phân phối Gauss có hiệp phương sai là hàm delta. Nó thô hơn mọi hàm thông thường rất nhiều. SPDE tuyến tính, như phương trình nhiệt ngẫu nhiên

$$
\partial_t u=\Delta u+\xi
$$

vẫn có nghĩa: ta tích chập $$\xi$$ với nhân nhiệt và được một nghiệm liên tục Hölder (trong một chiều không gian, nghiệm gần như Hölder bậc $$1/2-$$ theo biến không gian). Khó khăn bắt đầu khi phương trình **phi tuyến** theo nghiệm. Hai ví dụ tiêu biểu:

**Phương trình Kardar–Parisi–Zhang (KPZ).** Đây là mô hình cho một bề mặt đang lớn dần,

$$
\partial_t h=\partial_x^2 h+(\partial_x h)^2+\xi.
$$

Nghiệm $$h$$ được dự đoán là thô giống nghiệm phương trình nhiệt ngẫu nhiên. Khi đó $$\partial_x h$$ chỉ là một phân phối, và $$(\partial_x h)^2$$ là một tích không được phép.

**Phương trình $$\Phi^4_3$$ động lực.** Đây là lượng tử hóa ngẫu nhiên của trường $$\Phi^4$$ trong ba chiều không gian,

$$
\partial_t\Phi=\Delta\Phi-\Phi^3+\xi.
$$

Ở đây chính $$\Phi$$ đã là một phân phối, nên lũy thừa ba $$\Phi^3$$ không xác định được như một tích từng điểm.

Trong các tài liệu này, "kỳ dị" không có nghĩa là "chưa ai cố gắng đủ". Nó có nghĩa là phương trình viết ra một cách ngây thơ **chưa phải là một PDE xác định rõ**. Muốn nó có nghĩa, người ta phải chỉ ra một quy trình lấy giới hạn (làm trơn nhiễu, trừ đi các phần phân kỳ, rồi cho qua giới hạn) và chứng minh giới hạn đó tồn tại.

---

## 2. Con đường của Hairer: từ KPZ đến một ngôn ngữ tổng quát

Hairer sinh năm 1975 tại Geneva, học toán và vật lý ở Đại học Geneva, và bảo vệ luận án tiến sĩ **vật lý** năm 2001 dưới sự hướng dẫn của Jean-Pierre Eckmann. Nền tảng này giải thích vì sao ông quen với các tính toán hình thức về trường. Còn Huy chương Fields thì trao cho lý thuyết SPDE **toán học**.

Có hai hướng nghiên cứu trước đó đáng chú ý. Cùng với **Jonathan Mattingly**, ông chứng minh tính ergodic của **phương trình Navier–Stokes ngẫu nhiên hai chiều** với nhiễu suy biến (Annals, 2006). Đây là một định lý về chất lỏng ngẫu nhiên, không liên quan đến bài toán Clay về Navier–Stokes 3D tất định. Độc lập với ông, lý thuyết **đường thô (rough path) của Terry Lyons** đã cho thấy: phương trình vi phân thường được điều khiển bởi một tín hiệu rất gồ ghề vẫn giải được, nếu ta bổ sung cho tín hiệu các tích phân lặp của nó. Ghi chú của IMU năm 2014 nói rằng Hairer đã xây dựng tiếp trên ý tưởng này.

Trong bài *Solving the KPZ equation* (Annals of Mathematics, 2013), Hairer cho phương trình KPZ một nghĩa theo từng đường mẫu, bằng một cấu trúc chính quy riêng cho phương trình này (sau các kết quả dùng phép biến đổi Cole–Hopf và các kết quả về tính duy nhất trong cộng đồng xác suất). Bộ máy tổng quát xuất hiện trong *A theory of regularity structures* (Inventiones Mathematicae, 2014; arXiv:1303.5113). Đó là một khung chung xử lý KPZ, $$\Phi^4_3$$, mô hình Anderson parabolic và một lớp lớn SPDE kỳ dị **parabolic dưới tới hạn**, tất cả theo cùng một khuôn mẫu gồm phần đại số và phần giải tích.

**Dưới tới hạn** là một điều kiện về thang đo: sau khi so bậc của nhiễu và của số hạng phi tuyến, phương trình ở thang nhỏ trở nên ít kỳ dị hơn so với trường hợp tới hạn. Cấu trúc chính quy không cho phép ta viết ra một SPDE tùy ý rồi tuyên bố là đã giải được.

---

## 3. Cấu trúc chính quy: đa thức Taylor cộng thêm các đơn thức nhiễu

Một hàm cổ điển $$f$$ thuộc lớp $$C^\gamma$$ trên $$\mathbb{R}^d$$ là hàm mà gần mỗi điểm $$x$$ trông giống đa thức Taylor bậc $$\lfloor\gamma\rfloor$$, với phần dư kiểu Hölder. Ý tưởng của Hairer là giữ nguyên tinh thần "gần $$x$$ trông giống một khai triển", nhưng mở rộng danh sách các đơn thức được dùng.

Một **cấu trúc chính quy** là bộ ba $$(\mathcal{A},T,G)$$ gồm:
- một tập chỉ số $$\mathcal{A}\subset\mathbb{R}$$, là các bậc thuần nhất;
- một không gian vectơ phân bậc $$T=\bigoplus_{\alpha\in\mathcal{A}}T_\alpha$$, có cơ sở đóng vai trò các đơn thức trừu tượng (gồm đa thức thông thường *và* các ký hiệu xây từ nhiễu);
- một nhóm cấu trúc $$G$$, dùng để chuyển tâm khai triển từ điểm này sang điểm khác, giống như cách đa thức Taylor biến đổi khi đổi tâm $$x\mapsto y$$.

Một **mô hình** $$(\Pi,\Gamma)$$ biến các ký hiệu đó thành phân phối thật. $$\Pi_x\tau$$ là "hiện thực cụ thể của ký hiệu $$\tau$$ đặt tại tâm $$x$$", còn $$\Gamma_{xy}$$ chuyển một khai triển có tâm tại $$y$$ thành khai triển có tâm tại $$x$$. Các đánh giá giải tích yêu cầu $$\Pi_x\tau$$ có cỡ $$\lambda^{|\tau|}$$ khi thử với một hàm bướu (bump function) có bề rộng $$\lambda$$.

Một **phân phối được mô hình hóa** (modelled distribution) là một ánh xạ $$x\mapsto f(x)\in T$$, liên tục kiểu Hölder đối với $$\Gamma$$. Nói cách khác, đó là một khai triển Taylor trừu tượng với các hệ số thay đổi có kiểm soát. Cho đến bước tái dựng, toàn bộ lý thuyết chỉ mang tính địa phương và đại số.

**Tóm tắt.** Khai triển Taylor thông thường dùng các đơn thức $$1,\,(y-x),\,(y-x)^2,\ldots$$. Cấu trúc chính quy dùng các đơn thức đó *cộng thêm* một danh sách hữu hạn "đa thức làm từ nhiễu đã được làm trơn". Danh sách này được chọn sao cho số hạng phi tuyến của phương trình nhân được trong không gian trừu tượng, dù không nhân được trong $$\mathcal{S}'$$.

---

## 4. Tái dựng, tái chuẩn hóa, điểm bất động

**Định lý tái dựng.** Cho một mô hình và một phân phối được mô hình hóa $$f$$ có độ chính quy dương. Khi đó tồn tại duy nhất một phân phối $$\mathcal{R}f$$ sao cho gần mỗi điểm $$x$$, $$\mathcal{R}f$$ trông giống $$\Pi_x f(x)$$ với sai số Hölder như mong đợi. Định lý này là cây cầu từ đại số trở về giải tích. Nhờ nó, các khai triển trừu tượng không chỉ là ký hiệu trên giấy.

**Tái chuẩn hóa.** Nếu làm trơn nhiễu thành $$\xi^\varepsilon$$ rồi xây mô hình tương ứng, nhiều tích phân sẽ phân kỳ khi $$\varepsilon\to 0$$. Người ta trừ đi một danh sách hữu hạn các hằng số hoặc số hạng bù địa phương (hoặc, theo cách bất biến hơn, chuyển tâm lại). Đây cũng là ý tưởng tái chuẩn hóa trong lý thuyết trường lượng tử, nhưng giờ thành một định lý: các mô hình đã tái chuẩn hóa hội tụ. Khi đó các nghiệm tái dựng hội tụ về một giới hạn, và ta *định nghĩa* giới hạn đó là nghiệm của SPDE kỳ dị.

**Điểm bất động.** Trong không gian các phân phối được mô hình hóa, phương trình trở thành một ánh xạ co trên khoảng thời gian ngắn (hoặc trên toàn thời gian trong các trường hợp tiêu tán), giống hệt phép lặp Picard cho phương trình vi phân thường trên không gian Banach. Sự tồn tại và tính duy nhất ở đây không có gì bí ẩn. Chúng là định lý điểm bất động trên một không gian được thiết kế để các tích "không được phép" trở nên hợp lệ.

Như vậy lý thuyết của Hairer làm ba việc cùng lúc: nó **định nghĩa** phương trình, **xây dựng** nghiệm, và **chỉ ra** giới hạn của các phương trình đã làm trơn theo cách tự nhiên. Đó là lý do văn bản của IMU nói ông lần đầu tiên cho nhiều SPDE xuất phát từ vật lý một nghĩa chặt chẽ và nội tại.

---

## 5. Phân phối paracontrol: một bộ công cụ độc lập, có liên quan

Cùng thời gian đó, **Massimiliano Gubinelli**, **Peter Imkeller** và **Nicolas Perkowski** phát triển **phân phối paracontrol** (Forum of Mathematics, *Pi*, 2015; bản thảo arXiv:1210.2684). Ý tưởng này gần với giải tích Fourier hơn là với khai triển Taylor. Người ta dùng tích paraproduct của Bony để nói rằng nghiệm $$u$$ bị "điều khiển" bởi các đối tượng ngẫu nhiên tuyến tính xây từ nhiễu, rồi thực hiện phép nhân bằng phép tính paraproduct.

Cách tiếp cận này **không** phải phát minh của Hairer, cũng không phải hệ quả của cấu trúc chính quy. Đây là một bộ công cụ song song, xử lý các họ SPDE kỳ dị có phần trùng nhau (kể cả KPZ và $$\Phi^4_3$$). Các công trình sau này đã so sánh, chuyển đổi qua lại và đôi khi kết hợp hai ngôn ngữ. Khi trình bày, cần nêu đủ cả hai.

Một hướng gần gũi thứ ba, chỉ để định hướng, là lý thuyết **đường thô** (Lyons) và các mở rộng dạng đường thô phân nhánh (branched rough paths). Có thể xem cấu trúc chính quy là sự mở rộng của tư tưởng này lên mức phương trình đạo hàm riêng.

---

## 6. Những điều huy chương không khẳng định

Để nói cho chính xác trong khóa học này:

- **Không phải mọi SPDE.** Lý thuyết nhắm tới một lớp phương trình parabolic dưới tới hạn. Các mô hình tới hạn và trên tới hạn, các bài toán hyperbolic và nhiều phương trình chất lỏng vẫn nằm ngoài, hoặc chỉ một phần nằm trong, phạm vi của bộ máy này.
- **Không phải bài toán Clay về Navier–Stokes.** Kết quả ergodic của Hairer–Mattingly là cho Navier–Stokes *ngẫu nhiên* 2D. Bài toán chính quy 3D tất định không được giải bằng cấu trúc chính quy, và lời trao giải của IMU không nói như vậy.
- **Không phải "có bằng tiến sĩ vật lý nên được Fields".** Luận án giải thích sở thích và kỹ thuật của ông; giải thưởng là cho lý thuyết SPDE.
- **Không phải phương pháp duy nhất.** Phép tính paracontrol, phương pháp năng lượng và phép biến đổi Cole–Hopf giải được một số phương trình cùng loại bằng con đường khác.

Các vị trí giáo sư sau này (Warwick, Imperial, EPFL) và Giải Breakthrough 2021 không làm thay đổi nội dung lời trao giải năm 2014.

---

## 7. Vì sao lý thuyết này quan trọng

SPDE kỳ dị nằm ở chỗ giao nhau của xác suất, phương trình đạo hàm riêng và lý thuyết trường lượng tử: dễ viết ra, nhưng khó cho nghĩa. Với một lớp lớn phương trình được mô tả rõ ràng, cấu trúc chính quy thay cách làm "tính toán hình thức" bằng "điểm bất động sau khi tái chuẩn hóa".

Trong chương này, Hairer là ví dụ về một đóng góp mang tính **nền tảng**: một kiểu khai triển mới khiến các tính toán hình thức cũ trở nên hợp lệ. Có những Huy chương Fields được trao cho việc tạo ra một ngôn ngữ.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Mọi SPDE nay đều đặt đúng (well-posed)." | Chỉ một lớp lớn SPDE kỳ dị *parabolic dưới tới hạn*; đây không phải lý thuyết tồn tại cho mọi phương trình. |
| "Hairer giải Navier–Stokes." | Ông không giải bài toán Clay 3D tất định. Tính ergodic cho trường hợp 2D ngẫu nhiên là một định lý khác. |
| "Phân phối paracontrol là một phần của cấu trúc chính quy." | Gubinelli–Imkeller–Perkowski xây dựng một bộ công cụ độc lập, có liên quan. |
| "Nhiễu trắng là hàm, cứ nhân bình thường." | Nhiễu trắng là phân phối; muốn nhân phải có lý thuyết. |
| "Tái dựng chỉ là định lý Taylor." | Nó *mở rộng* Taylor: khai triển chứa các ký hiệu nhiễu, và kết quả là một phân phối. |
| "Fields được trao vì bằng tiến sĩ vật lý." | Đó là tiểu sử; lời trao giải nói về lý thuyết SPDE và cấu trúc chính quy. |

---

## Bài tập

1. Vì sao $$(\partial_x h)^2$$ không xác định nếu $$h$$ chỉ chính quy như nghiệm phương trình nhiệt ngẫu nhiên một chiều? Trả lời bằng ngôn ngữ tích các phân phối.
2. Viết phương trình $$\Phi^4_3$$ động lực và đánh dấu số hạng không xác định. Chỉ số dưới "3" nói về điều gì?
3. Trong một đoạn, hãy cho biết **mô hình** bổ sung dữ liệu gì vào cấu trúc chính quy trừu tượng $$(A,T,G)$$.
4. Phát biểu ý chính của định lý tái dựng mà không dùng chữ "ma thuật". Vì sao tính duy nhất của $$\mathcal{R}f$$ quan trọng khi định nghĩa nghiệm của PDE?
5. Trong câu chuyện này, **tái chuẩn hóa** làm gì: triệt tiêu một lực vật lý, hay chỉ ra giới hạn của các phương trình đã làm trơn?
6. Nêu một điểm **chung** của cấu trúc chính quy và phân phối paracontrol, và một điểm **khác nhau** (chỉ cần so khai triển Taylor trừu tượng với paraproduct).
7. **Luyện phát biểu chính xác.** Viết lại câu "Hairer giải mọi phương trình có nhiễu, kể cả rối loạn (turbulence)" thành hai câu đúng, có thể dùng trong khóa học này.
8. **Mở rộng.** Đọc lướt vài trang đầu bài của Hairer, arXiv:1303.5113, và liệt kê năm thuật ngữ cần học tiếp (ví dụ: phân phối được mô hình hóa, nhóm cấu trúc, dưới tới hạn, đại số Hopf của cây, nhóm tái chuẩn hóa).

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

## Hướng đi tiếp

- So sánh phép biến đổi Cole–Hopf cho KPZ với cách xây dựng bằng cấu trúc chính quy. Cách thứ nhất dựa vào một phép đổi biến đặc biệt; cách thứ hai áp dụng được cho cả những phương trình không có mẹo đó.
- Câu hỏi thảo luận: tái chuẩn hóa ở đây giống và khác tái chuẩn hóa trong lý thuyết trường lượng tử kiến thiết ở những điểm nào?

## Video tham khảo

- **Xem trước**: [Martin Hairer Colloquium Talk: Taming Infinities](https://www.youtube.com/watch?v=nBbx0wEgUXY) (Sydney Mathematical Research Institute - SMRI, tiếng Anh). Bài nói đại chúng của chính Hairer về việc "thuần hóa các đại lượng vô hạn". Nên xem trước để nắm vì sao tích các phân phối gây khó và tái chuẩn hóa làm gì.
- [Martin Hairer Mini-course 1: Introduction to Regularity Structures](https://www.youtube.com/watch?v=c0HlcVA1SoI) (Sydney Mathematical Research Institute - SMRI, tiếng Anh). Buổi đầu của một khóa ngắn giới thiệu cấu trúc chính quy. Nên xem sau khi đã đọc xong mục 3 và 4.
- [Martin Hairer: Fine properties of random fields: from fluids to QTF](https://www.youtube.com/watch?v=VnmfSICGDo4) (Centre International de Rencontres Mathématiques, tiếng Anh). Bài giảng về tính chất tinh tế của trường ngẫu nhiên, từ chất lỏng đến lý thuyết trường lượng tử. Dùng làm góc nhìn bổ sung sau hai video đầu.
