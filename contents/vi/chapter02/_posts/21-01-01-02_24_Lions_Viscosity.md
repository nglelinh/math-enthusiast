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

**Pierre-Louis Lions** nhận **Huy chương Fields 1994** tại ICM Zürich. Tài liệu chuẩn của ICM, tức bài giảng của S. R. S. Varadhan về công trình của ông, không nêu riêng một giả thuyết nào. Nó mô tả cả một *chương trình nghiên cứu*: các đóng góp trải từ **xác suất** đến **phương trình đạo hàm riêng**, có nhiều kết quả đẹp về **phương trình phi tuyến**, và việc chọn bài toán luôn **xuất phát từ ứng dụng**. Từ chương trình đó, khóa học này chọn ra một ý chính là **nghiệm nhớt** (viscosity solutions) cho phương trình đạo hàm riêng elliptic và parabolic phi tuyến. Khái niệm này được **Crandall–Lions** đưa ra cho phương trình Hamilton–Jacobi, được phát triển cùng **Evans** và nhiều người khác, rồi được hệ thống hóa cho phương trình cấp hai trong bài **hướng dẫn sử dụng** (user's guide) của **Crandall–Ishii–Lions**.

Bài này dành cho người đã biết phương trình đạo hàm riêng cấp một và nguyên lý cực đại cổ điển, và muốn hiểu vì sao một khái niệm nghiệm *yếu*, định nghĩa bằng các hàm thử chạm vào đồ thị thay vì bằng đạo hàm cấp hai tại từng điểm, lại trở thành ngôn ngữ chung của giải tích phi tuyến hiện đại. Bài **không** nói Lions đã giải bài toán Thiên niên kỷ của Viện Clay về tính chính quy của phương trình Navier–Stokes không nén ba chiều. Trò chơi trường trung bình (mean field games, Lasry–Lions) chỉ được nhắc như một ảnh hưởng **về sau**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại tài liệu ICM 1994 như một **chương trình nghiên cứu** (xác suất, phương trình phi tuyến, ứng dụng), chứ không phải một định lý đơn lẻ.
- Giải thích vì sao phương trình Hamilton–Jacobi và phương trình phi tuyến hoàn toàn (fully nonlinear) có thể không có nghiệm cổ điển $$C^2$$, và nghiệm **nhớt** được đặt ra để giải quyết điều gì.
- Mô tả vai trò trung tâm của **nguyên lý so sánh** (một dạng nguyên lý cực đại): nếu một nghiệm dưới nhớt nằm dưới một nghiệm trên nhớt trên biên thì nó cũng nằm dưới trong toàn miền.
- Ghi công đúng mức cho **Crandall**, **Ishii**, **Evans**, **Souganidis**, và biết rằng bài hướng dẫn của **Crandall–Ishii–Lions** là tài liệu chuẩn cho phương trình cấp hai.
- Xem lý thuyết **DiPerna–Lions** (phương trình Boltzmann, phương trình vận chuyển) và **nguyên lý tập trung–compact** là những trụ cột khác trong cùng chương trình về phương trình phi tuyến.
- Không đưa **trò chơi trường trung bình** (Lasry–Lions, giữa thập niên 2000) vào lời trao giải 1994, và bác bỏ câu "Lions đã giải Navier–Stokes".

**Kiến thức nền.** Giải tích nhiều biến; phương trình đạo hàm riêng cấp một như phương trình Hamilton–Jacobi $$u_t + H(x,\nabla u)=0$$; nguyên lý cực đại cổ điển cho hàm điều hòa hoặc cho phương trình elliptic tuyến tính đều. Điều khiển tối ưu và lý thuyết động học giúp hiểu động cơ, nhưng không bắt buộc phải học trước.

**Liên kết với các bài khác.** Bài này minh họa hai ý của chương: một chương trình nghiên cứu có thể thay đổi cả ngôn ngữ của một lĩnh vực, và cần trích dẫn đúng lời trao giải. Các bài giải tích liên quan: [Yu Deng / PDE động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (phương trình Boltzmann ở giai đoạn sau), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (tính chính quy cho phương trình phi tuyến hoàn toàn, có *dùng* nghiệm nhớt), và [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) (để tách riêng bài toán Thiên niên kỷ).

---

## 1. Vì sao cần một lý thuyết nghiệm yếu

Xét phương trình Hamilton–Jacobi dạng tiến hóa, trông có vẻ đơn giản,

$$
u_t + H\bigl(x,\nabla u\bigr) = 0,
$$

Trong điều khiển tối ưu hay quang hình học, ẩn $$u$$ là hàm giá trị hoặc hàm pha (eikonal). Phương pháp đặc trưng cho nghiệm trơn trong thời gian ngắn. Sau đó các đường đặc trưng cắt nhau, gradient bị nhảy, và không còn nghiệm $$C^1$$ (càng không có nghiệm $$C^2$$) để đi tiếp. Phương trình cấp hai phi tuyến hoàn toàn

$$
F\bigl(x,u,\nabla u,D^2 u\bigr) = 0
$$

còn khó hơn. Ẩn hàm xuất hiện phi tuyến qua ma trận Hessian (ví dụ phương trình Hamilton–Jacobi–Bellman trong điều khiển ngẫu nhiên, hay một số phương trình độ cong). Lý thuyết chính quy elliptic cổ điển không áp dụng trực tiếp được. Ta cũng không thể chỉ "lấy tích phân từng phần" để có nghiệm yếu Sobolev như với phương trình tuyến tính dạng divergence.

Vậy bài toán đặt ra mang tính khái niệm: cần một lớp **nghiệm yếu** đủ rộng để luôn có nghiệm toàn cục, đủ hẹp để nghiệm là duy nhất, và tương thích với **nguyên lý cực đại**, công cụ cốt lõi của lý thuyết elliptic và parabolic. Nghiệm theo nghĩa phân phối không dùng được khi $$F$$ không tuyến tính theo $$D^2 u$$. Nghiệm nhớt là lời giải cho bài toán này.

---

## 2. Nghiệm nhớt: dùng hàm thử chạm vào đồ thị thay cho đạo hàm

Ý tưởng của Crandall–Lions (công bố và phát triển đầu thập niên 1980; bài nền tảng về Hamilton–Jacobi là **Crandall–Lions, Trans. Amer. Math. Soc. 1983**) là kiểm tra một hàm $$u$$ chỉ liên tục bằng cách dùng các hàm trơn chạm vào đồ thị của nó từ phía trên hoặc phía dưới. Với phương trình dừng $$F(x,u,\nabla u,D^2 u)=0$$: $$u$$ là **nghiệm dưới** nhớt nếu mỗi khi một hàm thử trơn $$\varphi$$ chạm $$u$$ từ phía trên tại $$x_0$$, ta có

$$
F\bigl(x_0,u(x_0),\nabla\varphi(x_0),D^2\varphi(x_0)\bigr) \le 0
$$

(chiều của bất đẳng thức phụ thuộc vào quy ước dấu của $$F$$; bài hướng dẫn cố định quy ước này cẩn thận). **Nghiệm trên** nhớt là điều kiện ngược lại, với hàm thử chạm từ phía dưới. **Nghiệm nhớt** là hàm vừa là nghiệm dưới vừa là nghiệm trên.

Định nghĩa không đòi $$u$$ khả vi. Các đạo hàm đưa vào $$F$$ được lấy từ hàm thử tại điểm tiếp xúc. Nếu $$u$$ tình cờ thuộc lớp $$C^2$$ thì định nghĩa trở về phương trình cổ điển tại từng điểm. Đây là một kiểm tra tính nhất quán.

**Vì sao gọi là "nhớt"?** Về lịch sử, người ta xấp xỉ phương trình cấp một bằng cách thêm một số hạng cấp hai nhỏ $$\varepsilon\Delta u$$ (độ nhớt nhân tạo) rồi cho $$\varepsilon\to 0$$. Các bất đẳng thức còn giữ lại sau giới hạn chính là điều kiện chạm ở trên. Tên gọi nhắc lại phép lấy giới hạn độ nhớt tiến về 0, nhưng định nghĩa hiện đại không cần dựng phép xấp xỉ đó mỗi lần.

**Evans** (cùng Crandall và Lions) làm rõ các phát biểu tương đương và các tính chất cơ bản. **Ishii** đóng vai trò trung tâm khi mở rộng lý thuyết sang phương trình cấp hai phi tuyến hoàn toàn. **Souganidis** (thường cùng Lions và những người khác) phát triển tính ổn định, các phép xấp xỉ và bài toán lan truyền mặt sóng, giúp lý thuyết dùng được trong hình học và ứng dụng. Đây là công sức của cả một cộng đồng. Hai mốc cần nhớ tên là định nghĩa năm 1983 và bài hướng dẫn năm 1992.

---

## 3. Nguyên lý so sánh là cốt lõi

Có tồn tại mà không duy nhất thì chưa có giá trị nhiều; có duy nhất mà không tồn tại thì chỉ là lời nói. Lý thuyết nghiệm nhớt có được cả hai nhờ **nguyên lý so sánh**. Trong một bài toán Dirichlet điển hình: nếu $$u$$ là nghiệm dưới nhớt và $$v$$ là nghiệm trên nhớt của một phương trình elliptic đều (hoặc elliptic suy biến, với các giả thiết cấu trúc phù hợp), và $$u\le v$$ trên biên, thì $$u\le v$$ trong miền. Do đó hai nghiệm nhớt có cùng dữ kiện biên phải trùng nhau.

Chứng minh là một phiên bản nâng cấp của lập luận nguyên lý cực đại cho hàm không khả vi. Người ta xét giá trị lớn nhất của $$u(x)-v(y)$$ trừ đi một số hạng phạt buộc $$x$$ và $$y$$ ở gần nhau, áp dụng định nghĩa nghiệm nhớt tại các điểm gần trùng nhau, rồi dùng tính elliptic của $$F$$ để suy ra mâu thuẫn, trừ khi giá trị lớn nhất đó không dương. **Bài hướng dẫn của Crandall–Ishii–Lions** (*Bull. Amer. Math. Soc.* 1992; cũng có tại [arXiv:math/9207212](https://arxiv.org/abs/math/9207212)) là tài liệu chuẩn cho phép tính cấp hai này: jet, định lý tổng (theorem of sums), nguyên lý so sánh, và tính ổn định khi lấy giới hạn đều.

**Tính ổn định** là ưu điểm thứ hai. Giới hạn đều của các nghiệm nhớt vẫn là nghiệm nhớt. Vì vậy, khi đã có nguyên lý so sánh, ta có thể khẳng định rằng giới hạn của các xấp xỉ có độ nhớt tiến về 0, của các lược đồ số, hay hàm giá trị trong bài toán điều khiển, đều trùng với nghiệm nhớt duy nhất.

**Tóm tắt.** Nghiệm nhớt là một khái niệm nghiệm yếu dựa trên nguyên lý cực đại, chứ không dựa trên đồng nhất thức tích phân từng phần.

---

## 4. Các trụ cột khác: DiPerna–Lions và nguyên lý tập trung–compact

Tài liệu năm 1994 không chỉ nói về phương trình Hamilton–Jacobi.

**Lý thuyết DiPerna–Lions.** Cùng **Ronald J. DiPerna**, Lions phát triển khái niệm **nghiệm tái chuẩn hóa** (renormalized solutions) cho phương trình Boltzmann: tồn tại toàn cục và ổn định yếu cho bài toán Cauchy với dữ kiện lớn (*Ann. of Math.* **1989**). Toán tử va chạm khó định nghĩa khi mật độ chỉ khả tích. Phép tái chuẩn hóa và tính compact của trung bình theo vận tốc giúp phương trình có nghĩa trở lại. Cùng nhóm ý tưởng đó dẫn tới lý thuyết **phương trình vận chuyển** với trường vectơ thuộc lớp Sobolev: đường đặc trưng không nhất thiết duy nhất theo nghĩa Lipschitz, nhưng phương trình liên tục vẫn đặt đúng (sau này Ambrosio và những người khác mở rộng). Đặt cạnh [bài về Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): DiPerna–Lions nói về tính đặt đúng của chính phương trình động học; Deng–Hani–Ma nói về việc suy ra phương trình Boltzmann từ hệ hạt. Đó là hai tầng khác nhau của bài toán thứ sáu của Hilbert.

**Nguyên lý tập trung–compact (concentration-compactness).** Trên $$\mathbb{R}^n$$, một dãy cực tiểu hóa có thể mất tính compact do bị tịnh tiến ra xa hoặc bị co giãn (vị tự). Nguyên lý tập trung–compact của Lions (trường hợp compact địa phương năm **1984**; trường hợp giới hạn có vị tự năm **1985**) phân loại các kiểu thất bại này và khôi phục tính compact khi một bất đẳng thức năng lượng chặt loại trừ khả năng dãy bị tách đôi (dichotomy). Bài học rút ra: nếu bài toán biến phân bất biến dưới một nhóm không compact, hãy đo xem tính compact bị mất *theo cách nào*. Ứng dụng gồm các hàm cực trị cho bất đẳng thức Sobolev và một số bài toán hình học kiểu Yamabe.

Điểm chung với nghiệm nhớt nằm ở cách xây dựng: tạo ra đúng loại đối tượng yếu, rồi chứng minh một tính chất chặt chẽ khiến đối tượng đó duy nhất hoặc đạt được.

---

## 5. Những điều huy chương 1994 không khẳng định

**Không phải tính chính quy của Navier–Stokes.** Lions có các kết quả tồn tại cho hệ Navier–Stokes **nén được** trong một số khuôn khổ (thuộc cùng chương trình về chất lưu và phương trình động học với DiPerna–Lions). Đó không phải lời giải bài toán Clay về tính chính quy toàn cục của Navier–Stokes **không nén ba chiều**. Hãy giữ [phát biểu bài toán Thiên niên kỷ]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) tách riêng.

**Không phải trò chơi trường trung bình.** Cùng **Jean-Michel Lasry**, Lions về sau đưa ra **trò chơi trường trung bình** (các ghi chú và bài trên *Comptes Rendus* năm **2006**): giới hạn liên tục của cân bằng Nash khi có rất nhiều tác nhân hợp lý. Mô hình thường là một hệ ghép giữa phương trình Hamilton–Jacobi–Bellman và phương trình Fokker–Planck. Lý thuyết này dùng nghiệm nhớt và có ảnh hưởng lớn về sau tới giải tích, kinh tế học và mô hình đám đông. Nhưng nó ra đời **sau năm 1994**. Đừng đưa nó vào lời trao giải Fields.

**Không phải phát minh của một người.** Nghiệm nhớt ra đời từ Crandall–Lions, được Evans, Ishii, Souganidis mở rộng, và sau đó cả một cộng đồng phát triển. Huy chương ghi nhận vai trò của Lions trong mạng lưới đó và trong một chương trình rộng hơn về phương trình phi tuyến.

---

## 6. Vì sao là Huy chương Fields

Có ba lý do, khớp với những điểm Varadhan nhấn mạnh tại ICM.

1. **Một ngôn ngữ mới.** Nghiệm nhớt biến các phương trình không có nghiệm cổ điển thành bài toán đặt đúng. Cả những lĩnh vực như điều khiển tối ưu, lan truyền mặt sóng, và một phần hình học phi tuyến hoàn toàn nay có thể phát biểu các định lý duy nhất nghiệm mà trước đó không phát biểu chặt chẽ được.
2. **Nhiều công cụ sâu, không chỉ một bổ đề.** Nguyên lý tập trung–compact và lý thuyết DiPerna–Lions là những công trình độc lập. Cùng nhau, chúng cho thấy một phong cách: xác định chính xác vì sao tính compact hay tính khả vi cổ điển bị mất, rồi xây dựng phép tính xoay quanh chỗ mất đó.
3. **Ứng dụng là nguồn sinh định lý.** Văn bản ICM nhấn mạnh rằng việc chọn bài toán xuất phát từ ứng dụng. Đó không phải lời khen phụ. Đó là phương pháp nghiên cứu: toán tử va chạm Boltzmann, hàm giá trị trong điều khiển, và hàm cực trị Sobolev trên $$\mathbb{R}^n$$ đều đòi hỏi một khái niệm nghiệm hoặc một kiểu compact mới.

Giai đoạn sau, với trò chơi trường trung bình và các bài giảng ở Collège de France, tiếp tục phương pháp đó. Nhưng chỉ riêng công trình đến năm 1994 đã đủ cho huy chương.

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

## Bài tập

1. Bằng lời của bạn: vì sao các đường đặc trưng của $$u_t+H(\nabla u)=0$$ có thể làm gradient bị nhảy sau một thời gian hữu hạn? Vì sao điều đó buộc ta cần một lý thuyết nghiệm yếu?
2. Viết định nghĩa nghiệm dưới nhớt cho $$u_t+H(\nabla u)=0$$ bằng hàm thử chạm từ trên, rồi kiểm tra tính nhất quán: nếu $$u$$ thuộc $$C^1$$ thì định nghĩa trở về bất đẳng thức cổ điển.
3. Vì sao **nguyên lý so sánh** quý hơn một cách xây dựng nghiệm chỉ mang tính hình thức? Trả lời trong tối đa sáu câu.
4. Đọc lướt vài trang đầu bài của Crandall–Ishii–Lions (BAMS 1992 hoặc arXiv:math/9207212). Chọn ba thuật ngữ (ví dụ jet, hàm thử, elliptic suy biến) và giải thích mỗi thuật ngữ trong một dòng.
5. Lập một bảng so sánh **nghiệm nhớt**, **nghiệm tái chuẩn hóa DiPerna–Lions** và **nguyên lý tập trung–compact**. Mỗi công cụ xử lý chỗ thất bại nào của lý thuyết cổ điển?
6. **Luyện phát biểu chính xác.** Tìm một câu nói huy chương 1994 được trao "vì trò chơi trường trung bình". Viết lại thành hai câu chính xác.
7. **Mở rộng.** So sánh nguyên lý so sánh cho nghiệm nhớt với nguyên lý cực đại cho hàm điều hòa: điều gì được giữ lại, và điều gì phải xây dựng lại khi $$u$$ không khả vi?

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
