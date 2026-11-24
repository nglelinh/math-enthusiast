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

Hãy quan sát ranh giới cháy lan trên một tờ giấy, hay mặt trên gồ ghề của một đám tuyết rơi dày. Các nhà vật lý rất thích viết xuống những phương trình đạo hàm riêng có thêm một số hạng "nhiễu trắng" đại diện cho vô số va chạm ngẫu nhiên li ti. Trên bảng phấn của nhà vật lý, những phương trình ấy trông gọn gàng và đầy sức gợi; nhưng trong mắt nhà toán học giải tích, chúng lại là một **cơn ác mộng lôgic**: nghiệm của phương trình gồ ghề đến mức ngay cả việc bình phương đạo hàm hay lấy lập phương của nghiệm cũng trở thành "nhân hai đại lượng vô hạn với nhau" — một phép toán hoàn toàn vô nghĩa!

Trong suốt nhiều thập niên, những phương trình nổi tiếng như **phương trình KPZ** (mô tả bề mặt phát triển ngẫu nhiên) hay **phương trình $$\Phi^4_3$$ động lực** (trong lý thuyết trường lượng tử) nằm trong tình trạng lơ lửng: ai cũng tin chúng mô tả đúng tự nhiên, nhưng không ai biết cách *định nghĩa* thế nào là một nghiệm của chúng. Năm 2014, **Martin Hairer** nhận **Huy chương Fields**

> “for his outstanding contributions to the theory of stochastic partial differential equations, and in particular for the creation of a theory of regularity structures for such equations.”
> — [IMU, Fields Medals 2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)

*Tạm dịch: vì những đóng góp xuất sắc cho lý thuyết phương trình đạo hàm riêng ngẫu nhiên, đặc biệt là việc xây dựng lý thuyết cấu trúc chính quy cho các phương trình này.*

Điểm đặc biệt của giải thưởng này là nó trao cho một **ngôn ngữ mới**. Bằng cách mở rộng khai triển Taylor cổ điển — bổ sung vào danh sách đa thức $$1, x, x^2, \ldots$$ các "đơn thức trừu tượng" dựng từ chính nhiễu trắng — lý thuyết **cấu trúc chính quy** (*regularity structures*) của Hairer lần đầu tiên cho phép ta nhân các phân phối gồ ghề trong một không gian đại số, thực hiện **tái chuẩn hóa** một cách chặt chẽ, rồi "tái dựng" lại thành nghiệm thật. Song song đó, ta cũng sẽ đặt công trình của Hairer cạnh lý thuyết **đường thô** (*rough paths*) của Lyons và **phân phối paracontrol** của Gubinelli–Imkeller–Perkowski, đồng thời khẳng định rõ: đây không phải lời giải cho bài toán Navier–Stokes 3D của Viện Clay, và bằng tiến sĩ vật lý của Hairer chỉ là chi tiết tiểu sử chứ không phải lý do trao giải.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích rõ vì sao tích của hai phân phối nói chung không xác định, và vì sao trở ngại này xuất hiện ngay khi đưa nhiễu trắng không-thời gian vào một PDE phi tuyến.
- Nêu hai phương trình kỳ dị kinh điển (KPZ và $$\Phi^4_3$$ động lực) và chỉ rõ số hạng nào làm phương trình "vỡ nghĩa" trong từng trường hợp.
- Mô tả cấu trúc chính quy như một **ngôn ngữ khai triển Taylor mở rộng**: thêm vào đa thức cổ điển những đơn thức trừu tượng dựng từ nhiễu để phép nhân trở nên hợp lệ.
- Phát biểu ý chính của **định lý tái dựng**: một phân phối được mô hình hóa (trừu tượng) xác định duy nhất một phân phối thật khớp với mô hình gần mọi điểm.
- Ghi nhận đúng công lao của các hướng liên quan: **đường thô của Terry Lyons** là tiền đề trực tiếp, còn **phân phối paracontrol** (Gubinelli–Imkeller–Perkowski) là một bộ công cụ song song độc lập.
- Phân biệt rõ phạm vi định lý: lý thuyết áp dụng cho lớp **SPDE parabolic dưới tới hạn**, không giải bài toán Navier–Stokes 3D tất định của Viện Clay.

**Kiến thức nền.** Phương trình nhiệt và khái niệm phương trình đạo hàm riêng; chuyển động Brown là đường liên tục nhưng không khả vi tại bất kỳ điểm nào; phân phối là phiếm hàm tuyến tính liên tục trên các hàm thử. Về tích phân ngẫu nhiên, chỉ cần hiểu "nhiễu trắng là đạo hàm của chuyển động Brown". Không cần học trước lý thuyết đường thô.

**Liên kết với các bài khác.** Đặt câu chuyện này lên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/). Bài đó đã nêu SPDE của Hairer như một bài toán về tính đặt đúng (well-posedness). So sánh với [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (giới hạn động học tất định) và với [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (tính chính quy của PDE phi tuyến *không* có nhiễu trắng không-thời gian).

---

## Bản đồ kiến thức nền: Phương trình đạo hàm riêng ngẫu nhiên (SPDE) và phân phối là gì?

Để hiểu vì sao một dấu bình phương hay lập phương lại có thể làm khó cả thế giới giải tích suốt nửa thế kỷ, hãy lùi lại ba bước rất căn bản.

**1. Từ hàm trơn đến phân phối (hàm suy rộng).**
Trong giải tích năm nhất, đạo hàm của hàm bậc thang (nhảy từ $$0$$ lên $$1$$ tại $$x = 0$$) không tồn tại theo nghĩa thông thường. **Lý thuyết phân phối** của Laurent Schwartz giải quyết bằng cách không hỏi "giá trị của $$u$$ tại một điểm $$x$$ bằng bao nhiêu", mà chỉ đo tác động trung bình $$\langle u, \varphi \rangle = \int u(x)\varphi(x)\,dx$$ khi nhân $$u$$ với các hàm thử trơn $$\varphi$$. Nhờ phép tích phân từng phần, **mọi phân phối đều có đạo hàm cấp bất kỳ** — đạo hàm của hàm bậc thang chính là hàm delta Dirac $$\delta_0$$.
Nhưng cái giá phải trả là ta mất đi **phép nhân**: bạn có thể lấy đạo hàm của $$\delta_0$$ thoải mái, nhưng $$\delta_0(x)^2$$ thì hoàn toàn vô nghĩa (nếu xấp xỉ $$\delta_0$$ bằng một đỉnh cao $$1/\varepsilon$$ rộng $$\varepsilon$$, thì bình phương của nó có diện tích $$\varepsilon \cdot (1/\varepsilon)^2 = 1/\varepsilon \to \infty$$!).

**2. Chuyển động Brown và nhiễu trắng.**
**Chuyển động Brown** $$B_t$$ mô tả quỹ đạo zíc-zắc của hạt phấn hoa trong nước: đường cong $$t \mapsto B_t$$ liên tục ở mọi nơi, nhưng gồ ghề đến mức **không khả vi ở bất kỳ điểm nào** (về mặt định lượng, độ lệch $$\vert B_{t+h} - B_t \vert \sim \vert h \vert^{1/2}$$, nên nó chỉ đạt độ chính quy Hölder bậc $$1/2-$$). Đạo hàm theo nghĩa phân phối của chuyển động Brown gọi là **nhiễu trắng** $$\xi$$ — một phân phối có độ chính quy *âm* (nhỏ hơn $$-1/2$$). Trong không-thời gian, nhiễu trắng $$\xi(t,x)$$ còn thô hơn nữa: ở $$d$$ chiều không gian cộng $$1$$ chiều thời gian (với trọng số parabolic là $$d+2$$), độ chính quy của $$\xi$$ rơi xuống tận $$-\frac{d+2}{2}-$$!

**3. Giải tích Itô và điểm gãy của SPDE kỳ dị.**
Với phương trình vi phân ngẫu nhiên thường (SDE, chỉ có 1 biến thời gian $$t$$), **giải tích Itô** (thập niên 1940) xử lý gọn gàng bằng cách tận dụng chiều mũi tên thời gian (quá khứ độc lập với tương lai). Nhưng khi chuyển sang **SPDE** (có cả không gian $$x$$ lẫn thời gian $$t$$), không gian không có "quá khứ–tương lai". Nếu phương trình có số hạng phi tuyến tác động lên một nghiệm quá gồ ghề, ta đụng thẳng vào bài toán "nhân hai phân phối" — tương tự như tính $$\delta_0^2$$. Đó chính là thế giới của **SPDE kỳ dị** (*singular SPDEs*).

---

## 1. Khi tích không tồn tại: từ bài toán cổ điển đến hai "con quái vật" kỳ dị

Một phân phối Schwartz $$u\in\mathcal{S}'(\mathbb{R}^d)$$ lấy đạo hàm bao nhiêu lần cũng được, nhưng không phải lúc nào cũng nhân được với một phân phối khác. Quy tắc vàng của giải tích điều hòa (do Young và Bony phát hiện) nói rằng tích $$u \cdot v$$ chỉ xác định một cách tự nhiên khi **tổng độ chính quy của hai nhân tử dương**: $$\alpha + \beta > 0$$. Nếu cả hai đều thô đến mức tổng độ chính quy $$\le 0$$, nói chung **không tồn tại phép nhân chính tắc**.

Với SPDE tuyến tính như **phương trình nhiệt ngẫu nhiên**:

$$
\partial_t u=\Delta u+\xi,
$$

ta chưa gặp rắc rối: toán tử nhiệt $$(\partial_t - \Delta)^{-1}$$ có tác dụng "làm mượt" lên đúng $$+2$$ bậc. Trong một chiều không gian ($$d=1$$), nhiễu trắng $$\xi$$ có độ chính quy $$-3/2-$$, nên nghiệm $$u$$ được làm mượt thành hàm liên tục Hölder bậc $$-3/2 + 2 = 1/2-$$. Nhưng ngay khi thêm số hạng phi tuyến, mọi thứ sụp đổ:

**Ví dụ 1: Phương trình Kardar–Parisi–Zhang (KPZ).** Đây là mô hình kinh điển mô tả độ cao $$h(t,x)$$ của một bề mặt phát triển ngẫu nhiên trong một chiều không gian (như mép lửa cháy trên giấy):

$$
\partial_t h=\partial_x^2 h+(\partial_x h)^2+\xi.
$$

Nghiệm $$h$$ có độ chính quy giống nghiệm phương trình nhiệt ngẫu nhiên: bậc $$1/2-$$ theo không gian. Lấy đạo hàm một lần theo $$x$$, độ chính quy của $$\partial_x h$$ tụt xuống $$-1/2-$$ (chỉ còn là một phân phối). Khi bình phương nó thành $$(\partial_x h)^2$$, tổng độ chính quy là $$(-1/2-) + (-1/2-) = -1- < 0$$: **phép nhân hoàn toàn bất hợp pháp!** (Thực ra trong trường hợp rất đặc biệt của KPZ, phép biến đổi Cole–Hopf $$w = e^h$$ tình cờ tuyến tính hóa phương trình, nhưng đó là một mẹo "ăn may" chỉ dùng được cho KPZ chứ không mở rộng được cho các phương trình khác.)

**Ví dụ 2: Phương trình $$\Phi^4_3$$ động lực.** Đây là phiên bản động lực học (lượng tử hóa ngẫu nhiên) của trường lượng tử $$\Phi^4$$ trong **ba chiều không gian** ($$d=3$$):

$$
\partial_t\Phi=\Delta\Phi-\Phi^3+\xi.
$$

Ở $$d = 3$$, nhiễu trắng $$\xi$$ có độ chính quy $$-5/2-$$. Toán tử nhiệt kéo $$\Phi$$ lên bậc $$-5/2 + 2 = -1/2-$$. Tức là ngay bản thân $$\Phi$$ đã không phải là hàm mà là một phân phối thực sự! Khi đó, số hạng phi tuyến $$\Phi^3$$ là tích của ba phân phối có độ chính quy âm — hoàn toàn vô nghĩa theo cách hiểu cổ điển.

Trong ngữ cảnh này, gọi phương trình là "kỳ dị" không có nghĩa là "chưa ai đủ giỏi để giải", mà là biểu thức viết ra ban đầu **chưa định nghĩa một bài toán toán học hoàn chỉnh**. Muốn cho nó nghĩa chặt chẽ, ta phải làm trơn nhiễu thành $$\xi^\varepsilon$$, tìm cách trừ đi các hằng số phân kỳ (ví dụ $$C_\varepsilon \to \infty$$ khi $$\varepsilon \to 0$$) sao cho dãy nghiệm hội tụ về một giới hạn duy nhất không phụ thuộc vào cách làm trơn.

---

## 2. Con đường của Hairer: từ KPZ đến một ngôn ngữ tổng quát

Martin Hairer sinh năm 1975 tại Geneva, học toán và vật lý tại Đại học Geneva, và bảo vệ luận án tiến sĩ **vật lý** năm 2001 dưới sự hướng dẫn của Jean-Pierre Eckmann. Nền tảng vật lý lý thuyết giúp ông cảm nhận tự nhiên về tái chuẩn hóa và biểu đồ Feynman, nhưng Huy chương Fields 2014 được trao hoàn toàn cho bước ngoặt **toán học** trong lý thuyết SPDE.

Trước cấu trúc chính quy, có hai tiền đề quan trọng định hình tư duy của Hairer:
- Cùng **Jonathan Mattingly**, ông chứng minh tính ergodic (tính duy nhất của phân bố dừng) cho **phương trình Navier–Stokes ngẫu nhiên hai chiều** ngay cả khi nhiễu chỉ tác động vào rất ít tần số (*Annals of Mathematics*, 2006). Đây là một định lý xuất sắc về chất lỏng ngẫu nhiên 2D, tách biệt hoàn toàn với bài toán Thiên niên kỷ Clay về Navier–Stokes 3D tất định.
- Độc lập với đó, lý thuyết **đường thô (rough paths)** của **Terry Lyons** đã chứng minh một tư tưởng giải phóng: một phương trình vi phân thường bị lái bởi tín hiệu gồ ghề vẫn giải được *theo từng đường mẫu* (không cần tính xác suất kiểu Itô), miễn là ta cấp thêm cho tín hiệu đó một danh sách hữu hạn các **tích phân lặp** của nó. Hairer đã mang chính tinh thần đó từ 1 chiều thời gian lên không-thời gian nhiều chiều!

Năm 2013 (*Annals of Mathematics*), trong bài *Solving the KPZ equation*, Hairer lần đầu tiên cho phương trình KPZ một lời giải nội tại theo từng đường mẫu mà không cần nương nhờ phép biến đổi Cole–Hopf. Chỉ một năm sau, trong chuyên khảo dài gần 200 trang *A theory of regularity structures* (*Inventiones Mathematicae*, 2014; arXiv:1303.5113), ông trình bày bộ máy tổng quát xử lý đồng loạt KPZ, $$\Phi^4_3$$, mô hình Anderson parabolic và toàn bộ một lớp lớn **SPDE kỳ dị parabolic dưới tới hạn** theo cùng một kiến trúc đại số–giải tích thống nhất.

**Thế nào là "dưới tới hạn" (subcritical)?** Hãy tưởng tượng ta phóng to nghiệm ở thang rất nhỏ $$\lambda \ll 1$$. Nếu ở thang nhỏ, số hạng phi tuyến yếu dần so với phần tuyến tính $$\partial_t - \Delta$$ (dù cả hai đều kỳ dị), phương trình được gọi là **dưới tới hạn**. Điều kiện này đảm bảo chỉ cần bổ sung một số *hữu hạn* các đơn thức nhiễu và trừ đi một số *hữu hạn* các hằng số tái chuẩn hóa là đủ. Cấu trúc chính quy không phải chiếc đũa thần giải mọi SPDE tùy ý: các phương trình tới hạn (như $$\Phi^4_4$$) hay trên tới hạn vẫn nằm ngoài tầm với của bộ máy này.

---

## 3. Cấu trúc chính quy: đa thức Taylor cộng thêm các đơn thức nhiễu

Trong giải tích cổ điển, nói một hàm $$f$$ thuộc lớp $$C^\gamma$$ trên $$\mathbb{R}^d$$ nghĩa là gần mỗi điểm $$x$$, ta có thể xấp xỉ $$f(y)$$ rất sát bằng một tổ hợp tuyến tính của các đơn thức đa thức:

$$
f(y) \approx f(x)\cdot 1 + f'(x)\cdot (y-x) + \frac{1}{2}f''(x)\cdot (y-x)^2 + \cdots
$$

Nghiệm của SPDE kỳ dị *không* trông giống đa thức ở thang nhỏ — nó trông giống chính các đối tượng xây từ nhiễu trắng (ví dụ nghiệm của phương trình nhiệt ngẫu nhiên, hay bình phương của nó)! Ý tưởng thiên tài của Hairer là: **nếu đa thức thông thường không đủ để xấp xỉ nghiệm, hãy mở rộng bảng đơn thức Taylor bằng cách ném thêm các "đơn thức nhiễu" vào trong đó!**

Một **cấu trúc chính quy** là bộ ba đại số $$(\mathcal{A},T,G)$$ gồm:
- Một tập chỉ số $$\mathcal{A}\subset\mathbb{R}$$ (bị chặn dưới và rời rạc cục bộ), ghi lại "bậc thuần nhất" (độ chính quy) của từng đơn thức — bây giờ cho phép cả **bậc âm**!
- Một không gian vector phân bậc $$T=\bigoplus_{\alpha\in\mathcal{A}}T_\alpha$$, có cơ sở đóng vai trò các đơn thức trừu tượng (gồm đa thức thông thường $$1, X_i, X_i X_j, \ldots$$ *cộng thêm* các ký hiệu hình cây biểu diễn các tích phân lặp của nhiễu trắng).
- Một **nhóm cấu trúc** $$G$$ tác động trên $$T$$, đóng vai trò y hệt công thức nhị thức Newton khi ta đổi tâm khai triển Taylor từ điểm $$y$$ sang điểm $$x$$ (như viết $$(z-y)^2 = (z-x)^2 + 2(x-y)(z-x) + (x-y)^2$$).

Từ bộ khung trừu tượng đó, ta nối nó với thế giới thật bằng hai khái niệm:
- Một **mô hình** $$(\Pi,\Gamma)$$ gán cho mỗi ký hiệu trừu tượng $$\tau \in T$$ tại tâm $$x$$ một phân phối thật $$\Pi_x\tau$$, cùng phép chuyển tâm $$\Gamma_{xy} \in G$$. Điều kiện giải tích yêu cầu khi soi $$\Pi_x\tau$$ qua một hàm thử có bề rộng $$\lambda$$ quanh $$x$$, độ lớn của nó tỷ lệ đúng cỡ $$\lambda^{\vert \tau \vert}$$.
- Một **phân phối được mô hình hóa** (*modelled distribution*) là ánh xạ $$x \mapsto f(x) \in T$$ ghi lại các "hệ số Taylor tổng quát" tại mỗi điểm $$x$$, biến thiên mượt theo kiểu Hölder qua phép chuyển tâm $$\Gamma_{xy}$$.

**Tóm tắt bằng một hình ảnh.** Khai triển Taylor cổ điển giống như mô tả mọi đường cong trơn bằng bộ thước vẽ gồm đường thẳng và parabol. Cấu trúc chính quy bổ sung thêm vào hộp dụng cụ những "mẫu đường răng cưa" đúc sẵn từ nhiễu trắng. Trong không gian trừu tượng $$T$$, việc nhân hai biểu thức chỉ đơn giản là ghép các ký hiệu hình cây lại với nhau — hoàn toàn hợp lệ về mặt đại số, ngay cả khi phép nhân tương ứng trong không gian phân phối $$\mathcal{S}'$$ không tồn tại!

---

## 4. Tái dựng, tái chuẩn hóa, điểm bất động

Bộ máy của Hairer khép kín vòng tròn từ đại số trở về giải tích qua đúng ba bước nhịp nhàng:

**Bước 1 — Định lý tái dựng (Reconstruction Theorem).** Cho một mô hình $$(\Pi,\Gamma)$$ và một phân phối được mô hình hóa $$f$$ có độ chính quy dương $$\gamma > 0$$. Khi đó tồn tại **duy nhất** một phân phối thật $$\mathcal{R}f \in \mathcal{S}'$$ sao cho gần mọi điểm $$x$$, phân phối $$\mathcal{R}f$$ khớp với mô hình địa phương $$\Pi_x f(x)$$ với sai số cỡ $$\lambda^\gamma$$. Định lý này là cây cầu kỳ diệu biến các khai triển ký hiệu trên giấy thành một đối tượng giải tích thực thụ.

**Bước 2 — Tái chuẩn hóa (Renormalization).** Làm thế nào để xây dựng mô hình $$(\Pi, \Gamma)$$ cho nhiễu trắng $$\xi$$? Ta làm trơn nhiễu thành $$\xi^\varepsilon$$ (trơn ở thang $$\varepsilon > 0$$), lúc đó mọi tích đều xác định bình thường, cho ra mô hình tự nhiên $$(\Pi^\varepsilon, \Gamma^\varepsilon)$$. Nhưng khi cho $$\varepsilon \to 0$$, một số thành phần phi tuyến trong $$\Pi^\varepsilon$$ sẽ bùng nổ ra vô cực. Bằng một tác động nhóm đại số (nhóm tái chuẩn hóa, gắn với đại số Hopf của các cây có gốc), ta trừ đi đúng một danh sách hữu hạn các hằng số phân kỳ địa phương để thu được mô hình đã tái chuẩn hóa $$(\hat{\Pi}^\varepsilon, \hat{\Gamma}^\varepsilon)$$, rồi chứng minh bằng xác suất rằng chúng hội tụ về một mô hình giới hạn $$(\hat{\Pi}, \hat{\Gamma})$$ khi $$\varepsilon \to 0$$! Điều đáng kinh ngạc là bước xác suất nặng nhất chỉ phải làm *một lần duy nhất* cho hữu hạn ký hiệu cơ sở của mô hình, không cần làm lại khi giải phương trình.

**Bước 3 — Điểm bất động (Fixed Point).** Một khi đã có mô hình giới hạn $$(\hat{\Pi}, \hat{\Gamma})$$, toàn bộ phần còn lại trở nên hoàn toàn **tất định**: trên không gian Banach các phân phối được mô hình hóa, SPDE kỳ dị biến thành một ánh xạ co trên khoảng thời gian ngắn, giải được bằng định lý điểm bất động Banach (hệt như phép lặp Picard cho phương trình vi phân thường). Cuối cùng, áp dụng toán tử tái dựng $$\mathcal{R}$$ lên điểm bất động $$f$$, ta thu được phân phối $$\mathcal{R}f$$ — và *định nghĩa* nó là nghiệm của SPDE kỳ dị.

Nhờ quy trình ba bước này, lý thuyết của Hairer làm trọn ba việc cùng lúc: **định nghĩa** phương trình kỳ dị, **chứng minh tồn tại và duy nhất** nghiệm, và **khẳng định** rằng nghiệm đó là giới hạn phổ quát của các phương trình làm trơn sau khi tái chuẩn hóa.

---

## 5. Phân phối paracontrol: một bộ công cụ độc lập, có liên quan

Cùng thời điểm Hairer công bố cấu trúc chính quy, **Massimiliano Gubinelli**, **Peter Imkeller** và **Nicolas Perkowski** phát triển một lý thuyết song song độc lập mang tên **phân phối paracontrol** (*paracontrolled distributions*, *Forum of Mathematics, Pi*, 2015; bản thảo arXiv:1210.2684). Nếu cấu trúc chính quy mang tinh thần không gian thực và khai triển Taylor địa phương, thì phân phối paracontrol lại đi theo hướng **giải tích Fourier** và phép phân tách tần số (Littlewood–Paley): họ dùng tích *paraproduct* của Bony để tách tích hai phân phối thành phần "dễ nhân" và phần "cộng hưởng" nguy hiểm, rồi biểu diễn nghiệm $$u$$ như một đối tượng bị điều khiển theo tần số cao bởi các số hạng tuyến tính dựng từ nhiễu.

Cần ghi nhận công bằng: phân phối paracontrol **không** phải phát minh của Hairer và cũng **không** phải hệ quả của cấu trúc chính quy. Đây là một phương pháp độc lập, gọn nhẹ hơn ở bậc thấp và xử lý nhiều bài toán trùng khớp (kể cả KPZ và $$\Phi^4_3$$). Các công trình về sau đã xây dựng cầu nối chuyển đổi qua lại giữa hai ngôn ngữ này.

Bên cạnh đó, lý thuyết **đường thô** (*rough paths*) của **Terry Lyons** cùng mở rộng **đường thô phân nhánh** (*branched rough paths*, Gubinelli) là nền móng lịch sử trực tiếp: cấu trúc chính quy có thể được nhìn như sự tổng quát hóa đầy tham vọng của đường thô lên không gian đa chiều của PDE.

---

## 6. Những điều huy chương không khẳng định

Để giữ sự chính xác khoa học trong khóa học này, cần tách bạch bốn giới hạn:

- **Không phải mọi SPDE.** Cấu trúc chính quy nhắm vào lớp **SPDE parabolic dưới tới hạn**. Các mô hình tới hạn và trên tới hạn (như $$\Phi^4_4$$), nhiều bài toán hyperbolic và các phương trình chất lỏng phức tạp vẫn nằm ngoài, hoặc chỉ một phần nằm trong, phạm vi của bộ máy này.
- **Không phải bài toán Clay về Navier–Stokes.** Kết quả ergodic nổi tiếng của Hairer–Mattingly áp dụng cho Navier–Stokes *ngẫu nhiên* 2D. Bài toán chính quy toàn cục cho Navier–Stokes 3D tất định vẫn còn mở và không liên quan đến lời trao giải năm 2014.
- **Không phải "có bằng tiến sĩ vật lý nên được Fields".** Nền tảng vật lý giải thích phong cách tư duy và sự nhạy bén với tái chuẩn hóa của ông; huy chương được trao cho một lý thuyết toán học chặt chẽ về SPDE.
- **Không phải con đường duy nhất.** Phân phối paracontrol, phương pháp năng lượng hay phép biến đổi Cole–Hopf (cho KPZ) là những cách tiếp cận khác, bổ trợ cho nhau trong hệ sinh thái SPDE hiện đại.

Các vị trí giáo sư sau này của Hairer (Warwick, Imperial College London, EPFL) và Giải Breakthrough Toán học 2021 đều ghi nhận tiếp nối thành công đó, nhưng không làm thay đổi nội dung cụ thể của Huy chương Fields 2014.

---

## 7. Vì sao lý thuyết này quan trọng

SPDE kỳ dị nằm đúng ngã tư giữa xác suất, phương trình đạo hàm riêng và lý thuyết trường lượng tử: các nhà vật lý viết chúng ra rất dễ, nhưng cho chúng nghĩa toán học lại cực khó. Với một lớp lớn phương trình dưới tới hạn, cấu trúc chính quy đã thay thế những phép tính hình thức đầy bất trắc bằng một cỗ máy minh bạch: tách biệt rõ phần xác suất (tái chuẩn hóa hữu hạn mô hình cơ sở) khỏi phần giải tích tất định (định lý tái dựng và điểm bất động).

Trong bức tranh Chương 2, Martin Hairer là hình mẫu tiêu biểu cho một đóng góp mang tính **kiến tạo ngôn ngữ**: khi ngôn ngữ cũ (khai triển Taylor và giải tích cổ điển) không còn mô tả nổi sự gồ ghề của tự nhiên ngẫu nhiên, ông đã sáng tạo ra một thứ ngữ pháp mới khiến những phép toán tưởng chừng bất khả thi trở nên rõ ràng và chính xác.

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
