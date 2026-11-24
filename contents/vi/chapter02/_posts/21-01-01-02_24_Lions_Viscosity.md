---
layout: post
title: "Nghiệm nhớt của Lions và PDE phi tuyến (Huy chương Fields 1994)"
chapter: '02'
order: 24
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử một thí nghiệm hình học cực kỳ giản dị: xét phương trình khoảng cách (eikonal) trong một chiều $$\vert u'(x) \vert = 1$$ trên đoạn $$[-1, 1]$$ với điều kiện biên $$u(-1) = u(1) = 0$$. Mọi học sinh trung học đều nhận ra ngay ứng cử viên tự nhiên nhất là cái lều tam giác $$u(x) = 1 - \vert x \vert$$ — nhưng cái lều đó **có đỉnh nhọn tại $$x = 0$$ nên không khả vi**! Tệ hơn nữa, nếu cho phép hàm có góc nhọn, ta có thể vẽ ra *vô số* đường răng cưa nhấp nhô đều có độ dốc $$\pm 1$$ hầu khắp nơi và cùng bằng $$0$$ ở hai đầu mút. Vậy đâu là "nghiệm đúng" duy nhất?

Bài toán nhỏ xíu ấy chính là cánh cửa dẫn vào một cuộc cách mạng lớn của giải tích phi tuyến cuối thế kỷ XX. Năm 1994 tại ICM Zürich, **Pierre-Louis Lions** nhận **Huy chương Fields** — không phải cho một giả thuyết đơn lẻ nào, mà như S. R. S. Varadhan trình bày trong diễn văn ICM, cho cả một **chương trình nghiên cứu** trải rộng từ **xác suất** đến **phương trình đạo hàm riêng phi tuyến**, luôn bắt nguồn sâu sắc từ ứng dụng. Trụ cột nổi tiếng nhất của chương trình ấy là lý thuyết **nghiệm nhớt** (*viscosity solutions*) — do **Crandall và Lions** khởi xướng cho phương trình Hamilton–Jacobi, được **Evans**, **Ishii**, **Souganidis** mở rộng sang phương trình cấp hai phi tuyến hoàn toàn, và kết tinh trong bài *User's Guide* kinh điển của **Crandall–Ishii–Lions** (1992). Bên cạnh đó là hai trụ cột khác không kém phần vang dội: lý thuyết **DiPerna–Lions** cho phương trình Boltzmann và vận chuyển, cùng **nguyên lý tập trung–compact**. Bài học này cũng sẽ giữ hai ranh giới rõ ràng: Lions **không** giải bài toán Navier–Stokes không nén 3D của Viện Clay, và **trò chơi trường trung bình** (Lasry–Lions) là một nhánh ảnh hưởng rực rỡ *về sau* (giữa thập niên 2000), không thuộc lời trao giải năm 1994.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhìn nhận Huy chương Fields 1994 của Lions như một **chương trình nghiên cứu rộng lớn** (xác suất, PDE phi tuyến, ứng dụng), thay vì quy về một định lý đơn lẻ.
- Giải thích bằng ví dụ cụ thể vì sao phương trình Hamilton–Jacobi và PDE phi tuyến hoàn toàn thường không có nghiệm cổ điển $$C^1$$ hay $$C^2$$, và vì sao tích phân từng phần không dùng được.
- Trình bày trực giác định nghĩa **nghiệm nhớt** bằng hàm thử trơn chạm vào đồ thị từ phía trên và phía dưới, cùng vai trò quyết định của **nguyên lý so sánh** trong việc chọn ra nghiệm duy nhất.
- Ghi nhận đúng công lao tập thể của **Crandall**, **Ishii**, **Evans**, **Souganidis**, với bài hướng dẫn của **Crandall–Ishii–Lions** (1992) làm cột mốc cho phương trình cấp hai.
- Nêu vai trò của hai trụ cột song hành trong chương trình của Lions: lý thuyết **DiPerna–Lions** (phương trình Boltzmann và vận chuyển) và **nguyên lý tập trung–compact**.
- Tách bạch **trò chơi trường trung bình** (Lasry–Lions, 2006) khỏi lời trao giải 1994, và bác bỏ nhầm lẫn rằng Lions đã giải bài toán Clay về Navier–Stokes.

**Kiến thức nền.** Giải tích nhiều biến; phương trình đạo hàm riêng cấp một như phương trình Hamilton–Jacobi $$u_t + H(x,\nabla u)=0$$; nguyên lý cực đại cổ điển cho hàm điều hòa hoặc cho phương trình elliptic tuyến tính đều. Điều khiển tối ưu và lý thuyết động học giúp hiểu động cơ, nhưng không bắt buộc phải học trước.

**Liên kết với các bài khác.** Bài này minh họa hai ý của chương: một chương trình nghiên cứu có thể thay đổi cả ngôn ngữ của một lĩnh vực, và cần trích dẫn đúng lời trao giải. Các bài giải tích liên quan: [Yu Deng / PDE động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (phương trình Boltzmann ở giai đoạn sau), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (tính chính quy cho phương trình phi tuyến hoàn toàn, có *dùng* nghiệm nhớt), và [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) (để tách riêng bài toán Thiên niên kỷ).

---

## Bản đồ kiến thức nền: PDE phi tuyến hoàn toàn và "nghiệm yếu" là gì?

Để cảm nhận sự táo bạo của nghiệm nhớt, hãy so sánh hai cách làm "nghiệm yếu" hoàn toàn khác nhau trong giải tích hiện đại.

**1. Cách cổ điển: tích phân từng phần (nghiệm phân phối / Sobolev).**
Với một PDE tuyến tính như phương trình Laplace $$-\Delta u = f$$, nếu $$u$$ không khả vi cấp hai, ta nhân hai vế với một hàm thử trơn $$\varphi$$ rồi tích phân từng phần để "đá" đạo hàm từ $$u$$ sang $$\varphi$$: $$\int \nabla u \cdot \nabla \varphi = \int f\varphi$$. Cách này hoạt động cực tốt cho mọi PDE tuyến tính và các phương trình ở **dạng divergence** (như phương trình nhiệt, phương trình sóng, luật bảo toàn).

**2. Khi tích phân từng phần bó tay: PDE phi tuyến hoàn toàn.**
Hãy nhìn phương trình eikonal $$\vert \nabla u \vert = 1$$, phương trình Hamilton–Jacobi $$u_t + H(x, \nabla u) = 0$$ (trong điều khiển tối ưu và quang hình học), hoặc phương trình cấp hai phi tuyến hoàn toàn $$F(x, u, \nabla u, D^2 u) = 0$$ — ví dụ phương trình **Hamilton–Jacobi–Bellman** trong điều khiển ngẫu nhiên hay phương trình **Monge–Ampère** $$\det D^2 u = f$$. Ở đây các đạo hàm của $$u$$ bị nhốt bên trong các hàm phi tuyến (giá trị tuyệt đối, cực đại theo tham số điều khiển, định thức ma trận Hessian): **ta không thể tích phân từng phần để đẩy đạo hàm sang hàm thử $$\varphi$$ được!**

**3. Ý tưởng thiên tài: thay "tích phân từng phần" bằng "nguyên lý cực đại".**
Giả sử $$u$$ là một hàm trơn $$C^2$$ và hàm thử trơn $$\varphi$$ chạm vào đồ thị của $$u$$ từ phía trên tại điểm $$x_0$$ (tức $$u - \varphi$$ đạt **cực đại địa phương** tại $$x_0$$). Theo giải tích năm nhất, tại điểm cực đại ta lập tức biết:
- Đạo hàm bậc nhất trùng nhau: $$\nabla u(x_0) = \nabla \varphi(x_0)$$;
- Đạo hàm bậc hai bị chặn: $$D^2 u(x_0) \le D^2 \varphi(x_0)$$ (theo nghĩa ma trận bán xác định).

Nếu phương trình $$F$$ có tính elliptic (đơn điệu theo $$D^2 u$$), thì thay $$D^2 u(x_0)$$ bằng $$D^2 \varphi(x_0)$$ chỉ làm đổi chiều thành một bất đẳng thức! Điểm kỳ diệu là: **bất đẳng thức viết theo $$\nabla\varphi(x_0)$$ và $$D^2\varphi(x_0)$$ vẫn hoàn toàn có nghĩa ngay cả khi bản thân $$u$$ chỉ liên tục và có đầy góc nhọn!**

---

## 1. Từ bài toán cổ điển đến ý tưởng đột phá: vì sao cần một lý thuyết nghiệm yếu mới

Xét phương trình Hamilton–Jacobi tiến hóa, trông hết sức gọn gàng:

$$
u_t + H\bigl(x,\nabla u\bigr) = 0.
$$

Trong điều khiển tối ưu, $$u(t,x)$$ là chi phí tối thiểu để đưa hệ từ trạng thái $$x$$ đến đích trong thời gian $$t$$; trong quang hình học, $$u$$ là mặt sóng ánh sáng lan truyền. Phương pháp đường đặc trưng cho nghiệm trơn trong thời gian ngắn, nhưng rất nhanh sau đó hai tia sáng (hay hai quỹ đạo tối ưu) giao cắt nhau: tại nơi giao cắt, gradient $$\nabla u$$ nhảy đột ngột, đồ thị xuất hiện nếp gấp, và nghiệm cổ điển $$C^1$$ **chấm dứt tồn tại**.

Với phương trình cấp hai phi tuyến hoàn toàn

$$
F\bigl(x,u,\nabla u,D^2 u\bigr) = 0,
$$

tình hình còn gay go hơn vì ẩn hàm đi vào phi tuyến ngay trong ma trận Hessian $$D^2 u$$. Trong nhiều thập niên, giới giải tích khao khát một khái niệm **nghiệm yếu** thỏa đồng thời ba đòi hỏi: đủ rộng để luôn tồn tại toàn cục (kể cả khi xuất hiện góc nhọn), đủ chặt để **duy nhất** (loại bỏ hàng loạt nghiệm răng cưa giả tạo), và bền vững khi lấy giới hạn. Nghiệm nhớt của Crandall và Lions đã đáp ứng trọn vẹn cả ba đòi hỏi đó.

---

## 2. Nghiệm nhớt: dùng hàm thử chạm vào đồ thị thay cho đạo hàm

Ý tưởng cốt lõi được **Michael Crandall và Pierre-Louis Lions** công bố đầu thập niên 1980 (bài nền tảng về phương trình Hamilton–Jacobi trên *Trans. Amer. Math. Soc.*, 1983): ta "đo" một hàm liên tục $$u$$ không khả vi bằng tất cả các hàm trơn $$\varphi$$ có thể chạm vào đồ thị của nó.

Với phương trình dừng $$F(x,u,\nabla u,D^2 u)=0$$ (theo quy ước elliptic suy biến: $$F$$ giảm theo biến ma trận $$D^2 u$$):
- $$u$$ là **nghiệm dưới nhớt** (*viscosity subsolution*) nếu mỗi khi một hàm thử trơn $$\varphi$$ chạm $$u$$ từ **phía trên** tại $$x_0$$ ($$u - \varphi$$ đạt cực đại địa phương tại $$x_0$$), ta có

$$
F\bigl(x_0,u(x_0),\nabla\varphi(x_0),D^2\varphi(x_0)\bigr) \le 0.
$$

- $$u$$ là **nghiệm trên nhớt** (*viscosity supersolution*) nếu mỗi khi hàm thử trơn $$\varphi$$ chạm $$u$$ từ **phía dưới** tại $$x_0$$ ($$u - \varphi$$ đạt cực tiểu địa phương tại $$x_0$$), ta có bất đẳng thức ngược lại $$\ge 0$$.
- $$u$$ là **nghiệm nhớt** nếu nó vừa là nghiệm dưới nhớt vừa là nghiệm trên nhớt.

**Hãy kiểm tra ngay trên ví dụ cái lều $$\vert u'(x) \vert - 1 = 0$$ trên $$[-1, 1]$$!**
- Với cái lều ngửa lên $$u_1(x) = 1 - \vert x \vert$$: tại đỉnh nhọn $$x = 0$$, **không có** hàm trơn nào chạm được từ phía dưới (nên điều kiện nghiệm trên tự động đúng một cách trống rỗng!). Còn mọi hàm trơn $$\varphi$$ chạm từ phía trên tại $$x = 0$$ đều phải có độ dốc nằm trong $$[-1, 1]$$, tức $$\vert \varphi'(0) \vert - 1 \le 0$$ — **thỏa đúng điều kiện nghiệm dưới!** Vậy $$u_1(x) = 1 - \vert x \vert$$ là một nghiệm nhớt.
- Ngược lại, thử xét cái lều lộn ngược $$u_2(x) = \vert x \vert - 1$$ (cũng có $$\vert u_2' \vert = 1$$ hầu khắp nơi và bằng $$0$$ ở biên): tại đáy nhọn $$x = 0$$, hàm hằng $$\varphi \equiv -1$$ chạm $$u_2$$ từ phía dưới với $$\varphi'(0) = 0$$, khiến $$\vert \varphi'(0) \vert - 1 = -1 < 0$$ — **vi phạm ngay điều kiện nghiệm trên ($$\ge 0$$)!**

Chỉ bằng một phép thử chạm cực kỳ thanh lịch, định nghĩa nghiệm nhớt lập tức giữ lại cái lều vật lý đúng $$1 - \vert x \vert$$ và gạch bỏ toàn bộ vô số nghiệm răng cưa phi vật lý!

**Vì sao gọi là "nhớt" (viscosity)?** Tên gọi xuất phát từ phương pháp vật lý cổ điển: muốn chọn đúng nghiệm vật lý của $$u_t + H(\nabla u) = 0$$, người ta thêm một số hạng khuếch tán nhỏ $$-\varepsilon \Delta u$$ (giống độ nhớt nhân tạo làm mờ góc nhọn) để có nghiệm trơn $$u^\varepsilon$$, rồi cho $$\varepsilon \to 0$$. Các bất đẳng thức hàm thử sống sót sau giới hạn $$\varepsilon \to 0$$ chính là định nghĩa ở trên! Tên gọi lưu lại dấu tích lịch sử đó, còn bản thân định nghĩa hoàn toàn nội tại và chẳng dính dáng gì đến độ nhớt của chất lưu.

Sự trưởng thành của lý thuyết là công sức của cả một cộng đồng: **Lawrence C. Evans** (cùng Crandall và Lions) làm sắc nét các tính chất cơ bản; **Hitoshi Ishii** tạo bước nhảy vọt quyết định sang phương trình cấp hai phi tuyến hoàn toàn (với bổ đề Ishii / định lý tổng nổi tiếng); và **Panagiotis Souganidis** phát triển lý thuyết xấp xỉ, tính ổn định và lan truyền mặt sóng. Hai cột mốc lịch sử là bài báo 1983 (cấp một) và bài hướng dẫn kinh điển *User's Guide* của **Crandall–Ishii–Lions** (1992, cấp hai).

---

## 3. Nguyên lý so sánh là cốt lõi

Một khái niệm nghiệm yếu chỉ thực sự có sức sống khi nó đi kèm định lý **tồn tại** và **duy nhất**. Trong lý thuyết nghiệm nhớt, trái tim đảm bảo cả hai điều đó là **nguyên lý so sánh** (*comparison principle*): nếu $$u$$ là nghiệm dưới nhớt và $$v$$ là nghiệm trên nhớt của một phương trình elliptic (hoặc parabolic) với $$u \le v$$ trên biên, thì $$u \le v$$ trong toàn bộ miền. Hệ quả tức thì: hai nghiệm nhớt có cùng điều kiện biên bắt buộc phải **trùng nhau**! (Và kết hợp với phương pháp Perron, nguyên lý so sánh thậm chí cho luôn cả sự tồn tại nghiệm.)

Chứng minh nguyên lý so sánh cho hàm không khả vi là một tuyệt kỹ giải tích mang tên **nhân đôi biến** (*doubling of variables*): thay vì tìm cực đại của $$u(x) - v(x)$$, ta tối đa hóa $$u(x) - v(y) - \frac{1}{2\varepsilon}\vert x - y \vert^2$$ để ép $$x$$ và $$y$$ tiến sát nhau, áp dụng định nghĩa hàm thử (và bổ đề Ishii cho bậc hai) tại cặp điểm cực đại $$(x_\varepsilon, y_\varepsilon)$$, rồi dùng tính elliptic của $$F$$ để dẫn tới mâu thuẫn. **Bài hướng dẫn của Crandall–Ishii–Lions** (*Bull. Amer. Math. Soc.* 1992; [arXiv:math/9207212](https://arxiv.org/abs/math/9207212)) đã hệ thống hóa trọn vẹn phép tính jet cấp hai này thành cẩm nang gối đầu giường của mọi nhà giải tích PDE.

Ưu điểm song hành thứ hai là **tính ổn định kỳ diệu**: giới hạn hội tụ đều (thậm chí giới hạn nửa liên tục kiểu Barles–Perthame) của một dãy nghiệm nhớt vẫn tự động là nghiệm nhớt — hoàn toàn không cần kiểm soát đạo hàm của dãy! Nhờ cặp bài trùng "ổn định + so sánh", ta chứng minh ngay được rằng nghiệm của phương pháp xấp xỉ độ nhớt tiến về 0, nghiệm của lược đồ sai phân hữu hạn đơn điệu, hay hàm giá trị trong điều khiển tối ưu đều hội tụ về đúng nghiệm nhớt duy nhất.

**Tóm tắt.** Nghiệm nhớt là lý thuyết nghiệm yếu xây trên **nguyên lý cực đại** chứ không phải trên **tích phân từng phần**.

---

## 4. Các trụ cột khác: DiPerna–Lions và nguyên lý tập trung–compact

Chương trình được tôn vinh tại ICM 1994 còn đứng trên hai trụ cột đồ sộ khác ngoài nghiệm nhớt:

**1. Lý thuyết DiPerna–Lions (phương trình Boltzmann và vận chuyển).** Cùng **Ronald J. DiPerna**, Lions đưa ra khái niệm **nghiệm tái chuẩn hóa** (*renormalized solutions*) cho **phương trình Boltzmann** trong lý thuyết động học chất khí, chứng minh sự tồn tại toàn cục và ổn định yếu cho dữ kiện ban đầu lớn tùy ý (*Annals of Mathematics*, 1989). Vì toán tử va chạm có dạng bình phương nên không khả tích nổi khi mật độ chỉ thuộc $$L^1$$, DiPerna và Lions chia phương trình cho $$1 + f$$ (tức tác động bằng hàm phi tuyến $$\beta(f) = \ln(1+f)$$) kết hợp với bổ đề compact trung bình vận tốc để làm phương trình có nghĩa trở lại. Cùng tinh thần đó, bài báo *DiPerna–Lions (1989)* về **phương trình vận chuyển** chứng minh rằng ngay cả khi trường vận tốc chỉ thuộc lớp Sobolev $$W^{1,1}$$ (không đủ Lipschitz để phương trình vi phân thường có quỹ đạo duy nhất theo định lý Cauchy–Lipschitz), phương trình vận chuyển vẫn có nghiệm yếu duy nhất và dòng Lagrange tổng quát vẫn xác định hầu khắp nơi (sau này Luigi Ambrosio mở rộng sang lớp BV). So với [bài về Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): DiPerna–Lions giải bài toán đặt đúng của *chính* phương trình Boltzmann, còn Deng–Hani–Ma suy dẫn phương trình Boltzmann từ chuyển động va chạm của hệ hạt cầu cứng.

**2. Nguyên lý tập trung–compact (Concentration-Compactness, 1984–1985).** Khi cực tiểu hóa một phiếm hàm năng lượng trên toàn không gian $$\mathbb{R}^n$$ (như tìm hàm cực trị của bất đẳng thức Sobolev hay phương trình Schrödinger phi tuyến), không gian không compact nên một dãy cực tiểu hóa có thể "trốn thoát" theo đúng ba kịch bản:
- **Tan biến (vanishing):** khối lượng trải loãng đều ra khắp không gian về $$0$$;
- **Tách đôi (dichotomy):** khối lượng bị xé thành hai hay nhiều cục trôi dạt ra xa vô tận;
- **Tập trung / Compact (compactness):** toàn bộ khối lượng giữ gọn lại trong một vùng (xê dịch bởi phép tịnh tiến hoặc co giãn) và hội tụ mạnh!

Nguyên lý tập trung–compact của Lions phân loại triệt để các kiểu mất compact này và cho ra tiêu chuẩn năng lượng chặt (bất đẳng thức dưới cộng tính nghiêm ngặt) để loại trừ kịch bản tách đôi, từ đó chứng minh sự tồn tại cực tiểu.

Cả ba trụ cột — nghiệm nhớt, DiPerna–Lions, và tập trung–compact — đều chia sẻ một chữ ký phong cách độc đáo của Lions: **chẩn đoán chính xác vì sao công cụ cổ điển gãy đổ (mất khả vi, mất khả tích, hay mất compact), rồi thiết kế ngay khái niệm cấu trúc mới xoay quanh đúng vết gãy đó.**

---

## 5. Những điều huy chương 1994 không khẳng định

**Không phải bài toán Clay về Navier–Stokes.** Lions đã viết hai chuyên khảo đồ sộ về cơ học chất lưu và đạt những kết quả tồn tại yếu xuất sắc cho hệ Navier–Stokes **nén được** (*compressible*). Tuy nhiên, đó không phải lời giải cho [bài toán Thiên niên kỷ của Viện Clay]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) về tính chính quy toàn cục của phương trình Navier–Stokes **không nén ba chiều**.

**Không phải trò chơi trường trung bình (Mean Field Games).** Cùng **Jean-Michel Lasry**, Lions đồng sáng lập lý thuyết **trò chơi trường trung bình** (công bố năm 2006): mô tả giới hạn liên tục của cân bằng Nash khi hàng triệu tác nhân hợp lý tương tác với nhau, dẫn đến hệ ghép giữa một phương trình Hamilton–Jacobi–Bellman (chạy ngược thời gian) và một phương trình Fokker–Planck (chạy xuôi thời gian). Đây là một đóng góp cực kỳ có ảnh hưởng đến kinh tế học, tài chính và mô hình đám đông, nhưng nó ra đời **hơn một thập kỷ sau năm 1994** — tuyệt đối không đưa vào lời trao giải Fields.

**Không phải phát minh của một người đơn lẻ.** Nghiệm nhớt là kết tinh từ Crandall–Lions, được Evans, Ishii, Souganidis và cả một trường phái lớn đồng kiến tạo. Huy chương Fields 1994 ghi nhận vai trò dẫn dắt của Lions trong mạng lưới đó và trong toàn bộ chương trình PDE phi tuyến của ông.

---

## 6. Vì sao là Huy chương Fields

Ba điểm sáng mà Varadhan nêu bật trong diễn văn ICM 1994 vẫn còn nguyên sức nặng sau hơn ba thập kỷ:

1. **Tạo ra một ngôn ngữ phổ quát mới.** Nghiệm nhớt đã biến cả một lục địa rộng lớn gồm điều khiển tối ưu, trò chơi vi phân, lan truyền mặt sóng và hình học phi tuyến hoàn toàn từ vùng đất thiếu định lý duy nhất thành một lý thuyết chặt chẽ và hiệu quả.
2. **Bề rộng phi thường của các công cụ.** Mỗi công trình — nghiệm nhớt, DiPerna–Lions, nguyên lý tập trung–compact — đều đủ sức mở ra cả một hướng nghiên cứu độc lập với hàng nghìn bài báo tiếp nối.
3. **Ứng dụng là cội nguồn sinh ra lý thuyết sâu.** Lions chứng minh rằng những câu hỏi thực tế nhất (va chạm phân tử khí, điều khiển dưới nhiễu ngẫu nhiên, ổn định sao và plasma) chính là mảnh đất màu mỡ nhất để phát hiện những cấu trúc toán học thuần túy sâu sắc nhất.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Nghiệm nhớt là nghiệm cổ điển $$C^2$$ có thêm độ nhớt." | Đó là nghiệm *yếu*, định nghĩa bằng bất đẳng thức với hàm thử; nghiệm $$C^2$$ chỉ là trường hợp đặc biệt. |
| "'Nhớt' là độ nhớt vật lý của chất lưu." | Tên gọi nhắc tới các *xấp xỉ* có độ nhớt tiến về 0; định nghĩa không liên quan tới chất lưu nào. |
| "Lions đã giải Navier–Stokes." | Không. Kết quả tồn tại cho trường hợp nén được không phải bài toán chính quy không nén của Viện Clay. |
| "Huy chương 1994 là nhờ trò chơi trường trung bình." | Trò chơi trường trung bình của Lasry–Lions xuất hiện giữa thập niên 2000; chỉ là ảnh hưởng về sau. |
| "Nghiệm phân phối là đủ cho phương trình phi tuyến hoàn toàn." | Khi $$F$$ phi tuyến theo $$D^2 u$$, tích phân từng phần không dùng được; nguyên lý so sánh mới là công cụ đúng. |
| "Một mình Lions phát minh nghiệm nhớt." | Crandall–Lions; sau đó Evans, Ishii, Souganidis và nhiều người khác. |
| "DiPerna–Lions suy ra phương trình Boltzmann từ hệ hạt." | Họ cho một lý thuyết đặt đúng cho phương trình động học; suy dẫn từ hệ hạt là câu chuyện khác (về sau). |

---

## Liên kết

- Trang Huy chương Fields của IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Huy chương Fields 1994: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)
- Wikipedia, Pierre-Louis Lions: [https://en.wikipedia.org/wiki/Pierre-Louis_Lions](https://en.wikipedia.org/wiki/Pierre-Louis_Lions)
- Wikipedia, viscosity solution: [https://en.wikipedia.org/wiki/Viscosity_solution](https://en.wikipedia.org/wiki/Viscosity_solution)
- User’s guide Crandall–Ishii–Lions trên arXiv: [https://arxiv.org/abs/math/9207212](https://arxiv.org/abs/math/9207212)
- Tiểu sử ghế Collège de France: [https://www.college-de-france.fr/en/chair/pierre-louis-lions-partial-differential-equations-and-applications-statutory-chair/biography](https://www.college-de-france.fr/en/chair/pierre-louis-lions-partial-differential-equations-and-applications-statutory-chair/biography)
- Tìm arXiv, Lions viscosity: [https://arxiv.org/search/?query=Lions+viscosity+solutions&searchtype=all](https://arxiv.org/search/?query=Lions+viscosity+solutions&searchtype=all)

---

## Tài liệu tham khảo

1. S. R. S. Varadhan, bài giảng về công trình P.-L. Lions, *Proceedings of the ICM*, Zürich, 1994 (tài liệu ICM chuẩn được IMU 1994 trích).
2. **M. G. Crandall và P.-L. Lions**, “Viscosity solutions of Hamilton–Jacobi equations,” *Trans. Amer. Math. Soc.* **277** (1983).
3. **M. G. Crandall, L. C. Evans và P.-L. Lions**, “Some properties of viscosity solutions of Hamilton–Jacobi equations,” *Trans. Amer. Math. Soc.* **282** (1984).
4. **M. G. Crandall, H. Ishii và P.-L. Lions**, “User’s guide to viscosity solutions of second order partial differential equations,” *Bull. Amer. Math. Soc.* **27** (1992); [arXiv:math/9207212](https://arxiv.org/abs/math/9207212).
5. **R. J. DiPerna và P.-L. Lions**, “On the Cauchy problem for Boltzmann equations: global existence and weak stability,” *Ann. of Math.* **130** (1989).
6. **P.-L. Lions**, các bài concentration-compactness, *Ann. Inst. H. Poincaré Anal. Non Linéaire* (1984) và *Rev. Mat. Iberoamericana* (1985).
7. **J.-M. Lasry và P.-L. Lions**, ghi chú / *C. R. Math.* về mean field games (2006)—ảnh hưởng sau, không phải citation 1994.
8. Ngữ cảnh khóa học: [Deng / phương trình động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).

---

## Hướng đi tiếp

- Đọc bài hướng dẫn của Crandall–Ishii–Lions như một giáo trình: học nguyên lý so sánh trước, ví dụ sau.
- So sánh giới hạn độ nhớt tiến về 0 với nghiệm entropy của luật bảo toàn vô hướng (một lý thuyết nghiệm yếu gần gũi, nhưng định nghĩa khác).
- Nếu quan tâm tới ứng dụng, hãy xem trò chơi trường trung bình như một lĩnh vực *sử dụng* nghiệm nhớt, ra đời sau huy chương.
- Bài tập thêm: viết một trang "nghiệm nhớt không phải là gì" (không phải lời giải Navier–Stokes, không phải nội dung lời trao giải về trò chơi trường trung bình, không phải độ nhớt của chất lưu).

## Video tham khảo

- **Xem trước**: [The Essentials of Viscosity Solutions in R^n II](https://www.youtube.com/watch?v=I_fsCAW3xrM) (USF GradMath, tiếng Anh). Bài giảng nhập môn về nghiệm nhớt trong R^n, đúng đối tượng giải tích của bài này. Nên xem trước khi nghe các bài giảng của chính Lions.
- [Pierre-Louis Lions: Complete" Analysis of the Master Equation: an Example](https://www.youtube.com/watch?v=k0G_fwTVqHA) (Centre de recherches mathématiques - CRM, tiếng Anh). Bài giảng của Lions về "phương trình chủ" (master equation) trong trò chơi trường trung bình. Đây là chủ đề về sau, giúp thấy nghiệm nhớt được dùng tiếp ra sao, nhưng không thuộc lời trao giải 1994.
- [Charlemagne Distingushed Lecture Series 2012 with Prof. Dr. Pierre-Louis Lions](https://www.youtube.com/watch?v=spkaGZPTt9Q) (IRTG 2379 MIP, tiếng Anh). Bài giảng đại chúng của Lions trong chuỗi Charlemagne năm 2012. Xem để có thêm góc nhìn về cách ông chọn bài toán từ ứng dụng.
