---
layout: post
title: "Tối ưu → Vận hành & AI"
chapter: '03'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Mỗi sáng, một hãng hàng không lớn phải xếp lịch cho hàng trăm máy bay và hàng nghìn phi công sao cho không chuyến nào thiếu tổ bay, không ai bay quá giờ luật định, và lượng nhiên liệu tiêu thụ là thấp nhất. Cùng lúc đó, ở một trung tâm dữ liệu cách đó nửa vòng Trái Đất, hàng nghìn chip GPU đang miệt mài chỉnh sửa hàng chục tỷ trọng số của một mô hình ngôn ngữ để sai số dự đoán từ tiếp theo nhỏ đi thêm một chút.

Nhìn bề ngoài, xếp lịch bay, chia ca trực bệnh viện, điều phối xe giao hàng và huấn luyện trí tuệ nhân tạo có vẻ thuộc về những thế giới hoàn toàn khác nhau. Nhưng dưới con mắt toán học, tất cả chỉ là những chiếc áo khoác khác nhau của **một câu hỏi duy nhất**: *giữa vô vàn phương án hợp lệ thỏa mãn các ràng buộc thực tế, đâu là phương án tốt nhất?*

Bài học này nối tối ưu hóa toán học với vận trù học công nghiệp và việc huấn luyện AI. Chúng ta không đi hết từng thuật toán chi tiết, mà tập trung mở rõ bức tranh để bạn hiểu các bộ giải công nghiệp (LP/MIP solver) và các thuật toán như SGD, Adam thực sự đang làm gì bên trong.

**Lộ trình:** bản đồ ngành tối ưu hóa → khuôn mẫu chung → tính lồi → gradient và phương pháp bậc nhất → ràng buộc, nhân tử Lagrange và KKT → quy hoạch tuyến tính (LP) và quy hoạch nguyên (IP) → đối ngẫu → bề mặt không lồi trong học sâu → nhầm lẫn thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết bài toán dưới dạng $$\min_{x\in\mathcal{X}} f(x)$$ và nhận ra mục tiêu, biến, ràng buộc trong một bài toán có lời văn.
- Giải thích vì sao **tính lồi** làm cho mọi cực tiểu địa phương đều là cực tiểu toàn cục.
- Mô tả phương pháp gradient descent và vai trò của bước nhảy; nối nó với việc huấn luyện mô hình học máy.
- Nêu quy hoạch tuyến tính (LP) và quy hoạch nguyên (IP) mô hình hóa những gì trong vận hành.
- Giải thích ý tưởng **đối ngẫu** (giá bóng, chứng nhận tối ưu).
- Tránh hai nhầm lẫn: "gradient descent luôn tìm được cực tiểu toàn cục" và "bài toán lồi thì trong thực tế luôn dễ".

**Kiến thức nền.** Gradient. Sẽ có ích nếu biết [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/) và [xác suất, rủi ro]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).

---

## Bản đồ kiến thức nền: Tối ưu hóa toán học là gì và nghiên cứu những gì?

Ở phổ thông, muốn tìm cực tiểu của một hàm số $$f(x)$$, ta cứ lấy đạo hàm, giải $$f'(x)=0$$ rồi lập bảng biến thiên. Nhưng ngoài đời thực, hàm mục tiêu có thể có **hàng triệu biến** (không giải nổi $$f'(x)=0$$ bằng tay), bị gãy khúc không có đạo hàm, bị kẹp giữa hàng nghìn **ràng buộc bất đẳng thức**, hoặc buộc các biến phải là **số nguyên** (chẳng hạn không thể điều động 1,4 chiếc máy bay!).

**Tối ưu hóa toán học (mathematical optimization)** là ngành nghiên cứu cách thiết kế thuật toán tìm nghiệm tối ưu (hoặc đủ gần tối ưu) trong những điều kiện khắc nghiệt đó, đồng thời trả lời hai câu hỏi sống còn: *thuật toán có chạy nhanh không?* và *làm sao chứng minh được nghiệm tìm thấy thật sự là tốt nhất?*

Ranh giới lớn nhất chia đôi thế giới tối ưu hóa không phải "tuyến tính hay phi tuyến", mà là **lồi hay không lồi** và **liên tục hay rời rạc**:
- **Tối ưu lồi (LP, QP, bình phương tối thiểu, SVM):** bề mặt giống như một chiếc bát trơn tru chỉ có một đáy duy nhất → có thuật toán mạnh và có chứng nhận tối ưu toàn cục.
- **Tối ưu rời rạc / Quy hoạch nguyên (IP/MIP):** quyết định Có/Không trong logistics, lịch bay → NP-khó về lý thuyết nhưng giải cực hiệu quả nhờ kỹ thuật nhánh cận và nới lỏng lồi.
- **Tối ưu không lồi quy mô lớn (Học sâu):** bề mặt gồ ghề hàng tỷ chiều → dùng phương pháp bậc nhất ngẫu nhiên (SGD, Adam) để tìm những thung lũng phẳng giúp mô hình tổng quát hóa tốt.

---

## 1. Khuôn mẫu chung

Mọi bài toán tối ưu đều gói gọn trong một dòng ký hiệu:

$$
\min_x f(x)\quad\text{s.t.}\quad x\in\mathcal{X}.
$$

Trong đó $$x$$ là **biến quyết định** (số lượng hàng sản xuất, trọng số mạng nơ-ron), $$f(x)$$ là **hàm mục tiêu** (chi phí, thời gian trễ, sai số dự đoán), và $$\mathcal{X}$$ là **miền ràng buộc** (ngân sách, công suất nhà máy, luật lao động). Kỹ năng **mô hình hóa** — chuyển một bài toán kinh doanh lộn xộn thành đúng biến, mục tiêu và ràng buộc — chiếm một nửa thành công của cả ngành.

**Ý chính.** *Một hệ thống trở nên "tối ưu" khi quyết định được phát biểu thành mục tiêu kèm ràng buộc, rồi giải bằng thuật toán có bảo đảm toán học hoặc hiệu quả thực nghiệm rõ ràng.*

---

## 2. Tính lồi: bề mặt đáng tin cậy

Một tập $$\mathcal{X}$$ là **lồi** nếu đoạn thẳng nối hai điểm bất kỳ trong $$\mathcal{X}$$ không bao giờ thò ra ngoài (hình tròn, hình đa giác lồi thì lồi; hình lưỡi liềm thì không). Một hàm $$f$$ là **lồi** nếu dây cung nối hai điểm bất kỳ trên đồ thị luôn nằm phía trên đồ thị:

$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y),\qquad \forall t\in[0,1].
$$

Với hàm khả vi, điều này tương đương với việc mọi mặt phẳng tiếp tuyến đều nằm dưới đồ thị: $$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle$$.

**Vì sao tính lồi lại là "siêu năng lực" trong tối ưu?** Hãy tưởng tượng bạn bị bịt mắt thả xuống một vùng núi và chỉ được phép sờ độ dốc dưới chân để bước xuống. Nếu đó là một **chiếc bát lồi**, cứ đi xuống dốc thì *chắc chắn* bạn sẽ tới đúng đáy thấp nhất của cả chiếc bát — **mọi cực tiểu địa phương đều là cực tiểu toàn cục**. Ngược lại, trên một dãy núi không lồi đầy hố nhỏ, bạn rất dễ mắc kẹt ở một thung lũng lưng chừng núi mà tưởng mình đã xuống tới chân núi! Quy hoạch tuyến tính, bình phương tối thiểu, hồi quy logistic và SVM đều là bài toán lồi — đó là lý do chúng chạy cực kỳ ổn định và đáng tin cậy.

---

## 3. Gradient và các phương pháp bậc nhất

Khi bài toán có hàng triệu hay hàng tỷ biến (như mạng nơ-ron), ta không đủ bộ nhớ để tính ma trận đạo hàm bậc hai (Hessian $$n\times n$$). Công cụ chủ lực là **phương pháp bậc nhất** chỉ dùng đạo hàm bậc nhất (gradient):

$$
x_{k+1}=x_k-\eta_k\nabla f(x_k).
$$

Hướng ngược với gradient là hướng giảm nhanh nhất tại chỗ.

**Ví dụ số về chiếc thung lũng hẹp (tại sao cần Momentum và Adam).** Xét hàm lồi rất đơn giản $$f(x,y) = x^2 + 10y^2$$ (một thung lũng dốc gấp 10 lần theo phương $$y$$ so với phương $$x$$), bắt đầu từ $$(1,1)$$ với $$\nabla f = (2x, 20y) = (2, 20)$$:
- Nếu chọn bước nhảy hơi lớn $$\eta = 0{,}11$$: tọa độ $$y$$ nhảy từ $$1 \to 1 - 0{,}11(20) = -1{,}2$$ — văng qua bờ bên kia và nổ tung ra vô cực!
- Nếu chọn bước nhảy nhỏ $$\eta = 0{,}05$$ để $$y$$ không nổ: $$y$$ nhảy về $$0$$ ngay lập tức, nhưng $$x$$ chỉ nhích chậm chạp từ $$1 \to 0{,}9 \to 0{,}81 \dots$$

Các biến thể như **Momentum** (tích lũy quán tính như hòn bi lăn để giảm dao động zíc-zắc) và **Adam** (tự động điều chỉnh bước nhảy riêng cho từng tọa độ dựa trên độ lớn gradient quá khứ) ra đời chính để trị những thung lũng méo mó như vậy.

**SGD (Gradient Descent ngẫu nhiên):** khi hàm mất mát là trung bình trên $$n = 10^8$$ mẫu dữ liệu, tính đúng $$\nabla f$$ cho 1 bước cập nhật quá chậm. SGD bốc ngẫu nhiên một lô nhỏ (mini-batch, ví dụ 256 mẫu) để ước lượng gradient. Nhiễu ngẫu nhiên này không những giảm chi phí tính toán hàng nghìn lần mà còn giúp mô hình thoát khỏi các đáy hẹp, tìm được các thung lũng rộng giúp tổng quát hóa tốt hơn.

**Trong AI.**  
*Huấn luyện mạng nơ-ron là tối ưu phi tuyến quy mô lớn cho rủi ro thực nghiệm; lan truyền ngược cung cấp gradient; các thuật toán họ SGD/Adam cập nhật tham số.*

Liên hệ với [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/): hàm mất mát trên tập huấn luyện chỉ là rủi ro thực nghiệm, còn cái ta thực sự muốn nhỏ là rủi ro kỳ vọng ngoài đời thật.

---

## 4. Ràng buộc: phép chiếu, hàm chắn, nhân tử Lagrange

Khi biến quyết định không được chạy tự do mà phải nằm trong miền ràng buộc $$x\in\mathcal{X}$$, ta có bốn chiến lược chính:

- **Phép chiếu (projected gradient):** cứ bước một bước xuống dốc, nếu văng ra ngoài hàng rào $$\mathcal{X}$$ thì kéo về điểm gần nhất trên hàng rào.  
- **Hàm phạt & Lagrange tăng cường:** cộng thêm tiền phạt nặng vào hàm mục tiêu mỗi khi vi phạm ràng buộc.  
- **Điểm trong & hàm chắn (interior-point, barrier):** dựng một "bức tường năng lượng" tăng lên vô cực sát biên miền $$\mathcal{X}$$ để thuật toán luôn đi mượt mà bên trong miền (lõi của các bộ giải LP/QP hiện đại).  
- **Tập hoạt động (active-set):** đoán xem những ràng buộc nào đang bị ép sát dấu bằng.

Với ràng buộc đẳng thức $$g(x)=0$$, **nhân tử Lagrange** $$\lambda$$ ghép mục tiêu và ràng buộc thành $$L(x,\lambda)=f(x)+\langle\lambda,g(x)\rangle$$. Khi có thêm ràng buộc bất đẳng thức, điều kiện cần cho tối ưu trở thành **điều kiện KKT** (điều kiện dừng, chấp nhận được, và điều kiện bù: ràng buộc nào còn dư dả thì nhân tử của nó bằng 0).

**Trực giác kinh tế cực kỳ hữu ích: Giá bóng (Shadow Price).** Giả sử một tiệm bánh tối đa hóa lợi nhuận dưới ràng buộc chỉ có $$100\text{ kg}$$ bột mì mỗi ngày, và bộ giải trả về nhân tử Lagrange $$\lambda_{\text{bột}} = 50{.}000\text{ đ/kg}$$. Con số $$\lambda$$ này nói cho chủ tiệm biết ngay một bí mật kinh doanh: *mỗi kg bột mì mua thêm sẽ làm lợi nhuận tối đa tăng thêm đúng 50.000 đ!* Vì thế nếu nhà cung cấp chào bán thêm bột giá 35.000 đ/kg, hãy mua ngay; còn nếu giá 60.000 đ/kg thì từ chối.

---

## 5. Quy hoạch tuyến tính: công cụ chủ lực của vận trù học

$$
\min_x\, c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\ge 0.
$$

**Ví dụ trực quan 2 biến.** Một xưởng mộc đóng bàn ($$x_1$$) và ghế ($$x_2$$), lãi 400 nghìn/bàn và 300 nghìn/ghế, bị giới hạn bởi tổng lượng gỗ ($$2x_1 + x_2 \le 100$$) và tổng giờ công ($$x_1 + 2x_2 \le 80$$). Vẽ hai bất đẳng thức này lên mặt phẳng ta được một đa giác lồi. Vì hàm mục tiêu tuyến tính (các đường đồng mức là những đường thẳng song song), điểm cho lợi nhuận lớn nhất **luôn nằm tại một đỉnh góc của đa giác** (ở đây là giao điểm $$x_1=40, x_2=20$$ cho lãi 22 triệu)!

Trong không gian hàng chục nghìn biến, **phương pháp đơn hình (Simplex)** đi nhảy cóc từ đỉnh này sang đỉnh tốt hơn dọc theo các cạnh đa diện; còn **phương pháp điểm trong (Interior-Point)** đi xuyên thẳng qua ruột đa diện với bảo đảm thời gian đa thức.

**Ứng dụng.** Pha trộn nhiên liệu, lập kế hoạch sản xuất, vận tải, và đặc biệt là bài toán **luồng mạng** trong bài [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/): ma trận ràng buộc của luồng mạng có tính chất *unimodular hoàn toàn*, khiến mọi đỉnh của đa diện đều tự động có tọa độ nguyên — một món quà cấu trúc tuyệt đẹp!

---

## 6. Quy hoạch nguyên: các quyết định rời rạc

Rất nhiều quyết định vận hành không thể chia lẻ: bạn không thể xây $$0{,}6$$ nhà kho hay phân công $$1{,}3$$ tổ bay. Khi biến bị ép là số nguyên hoặc nhị phân $$0/1$$, ta có **quy hoạch nguyên (IP)** hay **quy hoạch nguyên hỗn hợp (MIP)**:

$$
\min c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\in\mathbb{Z}^n.
$$

**Vì sao không thể cứ giải LP rồi làm tròn?** Giả sử LP cho nghiệm tối ưu mua $$1{,}6$$ chiếc máy bay. Làm tròn xuống $$1$$ có thể không đủ tải chở khách; làm tròn lên $$2$$ lại vượt ngân sách! Trong không gian hàng nghìn biến, điểm nguyên gần nhất với nghiệm LP thậm chí có thể hoàn toàn không hợp lệ.

Dù MIP tổng quát là NP-khó, các bộ giải công nghiệp hiện đại (như Gurobi, CPLEX, HiGHS) giải trơn tru những bài toán hàng trăm nghìn biến mỗi ngày nhờ **nhánh cận (branch-and-bound)** và **mặt phẳng cắt (cutting planes)**: dùng nghiệm **nới lỏng LP** làm cận dưới để cắt tỉa hàng tỷ nhánh vô vọng mà không cần duyệt qua chúng.

**Ý chính.** *Vận trù học thành công nhờ nghệ thuật mô hình hóa chặt chẽ để bộ giải MIP thu hẹp nhanh khoảng cách giữa cận trên và cận dưới; độ khó trong trường hợp xấu nhất không ngăn cản ta tối ưu hóa nền kinh tế thực.*

---

## 7. Đối ngẫu: chứng nhận và giá cả

Một trong những ý tưởng đẹp nhất của toán học ứng dụng là **đối ngẫu (duality)**: mọi bài toán tối ưu gốc (ví dụ *tìm cách vận chuyển chi phí thấp nhất*) đều có một "chiếc bóng phản chiếu" gọi là **bài toán đối ngẫu** (*tìm bảng giá cước cao nhất mà đối thủ không thể ép giá thấp hơn*).

- **Đối ngẫu yếu:** mọi nghiệm hợp lệ của bài đối ngẫu đều tạo ra một **cận dưới** cứng rắn cho bài toán cực tiểu gốc. Nếu bài gốc tìm được phương án tốn 10 tỷ, còn bài đối ngẫu chứng minh không phương án nào tốn dưới 9,8 tỷ, bạn biết ngay mình đã sát tối ưu tối đa 2%!
- **Đối ngẫu mạnh** (đúng với LP chấp nhận được và bị chặn, cũng như bài toán lồi thỏa điều kiện Slater): hai giá trị tối ưu **bằng nhau tuyệt đối**. Nghiệm đối ngẫu chính là **tờ giấy chứng nhận toán học** khẳng định không ai trên đời tìm được phương án rẻ hơn nữa.

Với bài toán luồng mạng, định lý luồng cực đại – lát cắt cực tiểu chính là đối ngẫu mạnh dưới lớp áo tổ hợp.

---

## 8. Bài toán không lồi và học sâu

Hàm mất mát của mạng nơ-ron sâu là một địa hình **không lồi** cực kỳ phức tạp trong không gian hàng tỷ chiều: đầy điểm yên ngựa (saddle points) và vô số cực tiểu tương đương nhau do hoán vị nơ-ron. Lý thuyết không còn hứa hẹn SGD sẽ tìm ra cực tiểu toàn cục.

Thế nhưng thực nghiệm lại cho thấy một bất ngờ thú vị: trong không gian cực nhiều chiều của các mạng dư thừa tham số (overparameterized), hầu hết điểm dừng cục bộ đều là điểm yên ngựa (có hướng đi xuống để SGD dễ thoát ra) chứ không phải đáy cạn bị kẹt, và những thung lũng phẳng mà SGD tìm được thường tổng quát hóa rất tốt ([Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/)). Các kỹ thuật kiến trúc hiện đại như kết nối tắt (**residual connections**) hay chuẩn hóa lớp (**LayerNorm**) thực chất đóng vai trò "làm phẳng bề mặt tối ưu" giúp gradient chảy thông suốt.

**Nói thật.** "Huấn luyện bằng Adam" không phải một chứng minh tối ưu. Đó là một quy trình kỹ thuật mạnh mẽ để hạ rủi ro thực nghiệm, luôn cần đi kèm kiểm tra trên tập validation độc lập.

---

## 9. Tối ưu hóa trong các công nghệ của chương 3

| Lĩnh vực | Bài toán điển hình |
|----------|---------------------|
| Thiết kế kỹ thuật | Tối ưu có ràng buộc là PDE; tối ưu hình dạng và tôpô |
| Điều khiển | LQR, điều khiển dự báo (MPC) như các bài QP giải lặp |
| Vận hành | LP/MIP cho lập lịch và định tuyến |
| Thống kê | MLE, ERM, hồi quy có chính quy hóa |
| Học máy | ERM không lồi giải bằng SGD |
| Xử lý tín hiệu | Basis pursuit, cảm biến nén (thay bài toán khó bằng bài toán lồi) |
| Vận chuyển | [Vận chuyển tối ưu Ch.6]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) |

Điểm chung về cả tư duy lẫn thực hành: **viết rõ mục tiêu, tôn trọng ràng buộc, nhận diện đúng địa hình bài toán (lồi hay không lồi, liên tục hay rời rạc), và chọn thuật toán một cách có hiểu biết.**

---

### Tóm tắt về tối ưu (từ phần tìm hiểu video)

Xem [3B1B gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) cùng với cuốn sách miễn phí của Boyd [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).

- **Tính lồi:** cực tiểu địa phương cũng là cực tiểu toàn cục; đó là lý do bộ giải có thể chứng nhận kết quả.
- **Phương pháp bậc nhất:** chỉ dùng gradient; chạy được với số chiều rất lớn, đổi lại phụ thuộc nhiều vào tính điều kiện của bài toán.
- **Đối ngẫu:** biến đối ngẫu cho biết "giá" của các ràng buộc; đối ngẫu mạnh cần thêm điều kiện về ràng buộc.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Gradient descent luôn tìm được cực tiểu toàn cục." | Chỉ đúng với điều kiện nhất định (ví dụ bài toán lồi). |
| "Bài toán lồi lúc nào cũng tầm thường." | Nhiều chiều, không trơn, nhiều ràng buộc vẫn là thách thức. |
| "LP và tối ưu trong học máy không liên quan gì nhau." | Cùng là cực tiểu hóa một mục tiêu; khác nhau ở thuật toán và bảo đảm. |
| "Biến đối ngẫu chỉ là thứ thừa của bộ giải." | Đó là giá bóng và chứng nhận tối ưu. |
| "Quy hoạch nguyên không giải được vì NP-khó." | Các bài toán công nghiệp có cấu trúc được giải hằng ngày. |
| "Mất mát huấn luyện nhỏ hơn thì mô hình tốt hơn." | Khả năng tổng quát hóa phụ thuộc vào rủi ro, không chỉ vào mất mát thực nghiệm. |

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/optimization-operations-ai/`.

**Thứ tự xem gợi ý**

1. **CORE** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).
2. **FOUNDATION** — Stanford / Boyd — Convex Optimization lectures (EE364): [https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h).
3. **FOUNDATION** — Boyd & Vandenberghe — Convex Optimization book (free PDF): [https://web.stanford.edu/~boyd/cvxbook/](https://web.stanford.edu/~boyd/cvxbook/).
4. **FOUNDATION** — MIT 6.255J / optimization OCW culture: [https://ocw.mit.edu/search/?q=optimization](https://ocw.mit.edu/search/?q=optimization).
5. **ORIENTATION** — StatQuest — Gradient Descent: [https://www.youtube.com/watch?v=sDv4f4s2SB8](https://www.youtube.com/watch?v=sDv4f4s2SB8).
6. **ORIENTATION** — 3Blue1Brown — Essence of calculus (derivatives for optimization): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).

Danh mục URL đầy đủ: `research/video-research/optimization-operations-ai/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/optimization-operations-ai/transcripts/` · trạng thái: `research/video-research/optimization-operations-ai/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/optimization-operations-ai_IHZwWFHWa-w_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/optimization-operations-ai/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — Gradient descent, how neural networks learn — https://www.youtube.com/watch?v=IHZwWFHWa-w
2. Stanford / Boyd — Convex Optimization lectures (EE364) — https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h
3. Boyd & Vandenberghe — Convex Optimization book (free PDF) — https://web.stanford.edu/~boyd/cvxbook/
4. MIT 6.255J / optimization OCW culture — https://ocw.mit.edu/search/?q=optimization
5. StatQuest — Gradient Descent — https://www.youtube.com/watch?v=sDv4f4s2SB8
6. 3Blue1Brown — Essence of calculus (derivatives for optimization) — https://www.youtube.com/watch?v=WUvTyaaNkzM
7. Linear programming simplex culture (popular explainers) — https://en.wikipedia.org/wiki/Simplex_algorithm
8. Duality / Lagrange multipliers visual lectures — https://en.wikipedia.org/wiki/Lagrange_multiplier

### Video (tìm thêm / phụ)

9. Nocedal & Wright numerical optimization culture talks — https://web.stanford.edu/~boyd/cvxbook/

### Bài báo, sách, OCW và web

10. Boyd & Vandenberghe — Convex Optimization (PDF): https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
11. Nesterov — Introductory Lectures on Convex Optimization: https://link.springer.com/book/10.1007/978-1-4419-8853-9
12. Wikipedia — Convex optimization: https://en.wikipedia.org/wiki/Convex_optimization
13. Wikipedia — Linear programming: https://en.wikipedia.org/wiki/Linear_programming
14. Wikipedia — Lagrange multiplier: https://en.wikipedia.org/wiki/Lagrange_multiplier
15. Wikipedia — Stochastic gradient descent: https://en.wikipedia.org/wiki/Stochastic_gradient_descent

### Trong khóa

16. Khóa: [Đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/), [Đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [Optimal Transport]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/). Gói: `research/video-research/optimization-operations-ai/`.

## Hướng đi tiếp

- [Fourier → Xử lý tín hiệu]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/).  
- [Toán của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/).  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) (3Blue1Brown, tiếng Anh). Hàm mất mát và cách mạng nơ-ron học bằng gradient descent, minh họa bằng hình ảnh. Nên xem trước khi đọc §3.
- [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) (StatQuest with Josh Starmer, tiếng Anh). Tính từng bước gradient descent trên một ví dụ hồi quy đơn giản. Hợp để luyện bài tập 3 và 4.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) (3Blue1Brown, tiếng Anh). Ôn lại đạo hàm, nền tảng của gradient. Dành cho ai muốn củng cố kiến thức giải tích.
