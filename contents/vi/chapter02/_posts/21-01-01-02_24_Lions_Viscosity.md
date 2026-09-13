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

**Pierre-Louis Lions** nhận **Huy chương Fields 1994** tại ICM Zürich. Tài liệu ICM chuẩn, trong bài giảng của S. R. S. Varadhan về công trình, không cô lập một giả thuyết mang tên. Nó ghi một *danh mục*: đóng góp trải từ **xác suất** đến **phương trình đạo hàm riêng**, với những kết quả đẹp trên **phương trình phi tuyến**, và với việc chọn bài toán luôn **được thúc đẩy bởi ứng dụng**. Khẩu hiệu toán học mà khóa học này lấy từ danh mục đó là **nghiệm nhớt** (viscosity solutions) cho PDE elliptic và parabolic phi tuyến—được đưa vào cho phương trình Hamilton–Jacobi bởi **Crandall–Lions**, được phát triển cùng **Evans** và những người khác, rồi được tổ chức cho phương trình cấp hai trong **hướng dẫn sử dụng** của **Crandall–Ishii–Lions**.

Bài này dành cho người đã gặp PDE cấp một và nguyên lý cực đại cổ điển, muốn hiểu vì sao một khái niệm nghiệm *yếu*—định nghĩa bằng cách chạm bằng hàm thử chứ không bằng đạo hàm cấp hai từng điểm—trở thành ngôn ngữ của giải tích phi tuyến hiện đại. Bài **không** khẳng định Lions đã giải bài toán Clay Millennium về chính quy Navier–Stokes không nén ba chiều. Trò chơi trường trung bình (mean field games, Lasry–Lions) chỉ xuất hiện như ảnh hưởng **sau này**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lại tài liệu ICM 1994 như một **danh mục** (xác suất, PDE phi tuyến, ứng dụng) chứ không phải một định lý đơn lẻ.
- Giải thích vì sao nghiệm cổ điển $$C^2$$ của Hamilton–Jacobi và phương trình fully nonlinear có thể thất bại, và nghiệm **nhớt** được thiết kế để cho phép điều gì.
- Mô tả động cơ **so sánh / nguyên lý cực đại**: nếu dưới-nghiệm nhớt nằm dưới trên-nghiệm trên biên thì nó vẫn nằm dưới ở trong miền.
- Gán công lao **Crandall**, **Ishii**, **Evans**, **Souganidis** đúng mức, và gọi **Crandall–Ishii–Lions** user’s guide là tài liệu chuẩn cấp hai.
- Đặt lý thuyết **DiPerna–Lions** (Boltzmann / phương trình vận chuyển) và **concentration-compactness** như những trụ khác của cùng danh mục PDE phi tuyến.
- Giữ **mean field games** (Lasry–Lions, giữa thập niên 2000) ra ngoài citation 1994, và từ chối khẩu hiệu “Lions đã giải Navier–Stokes.”

**Kiến thức nền.** Giải tích nhiều biến; ý tưởng PDE cấp một như Hamilton–Jacobi $$u_t + H(x,\nabla u)=0$$; nguyên lý cực đại cổ điển cho phương trình điều hòa hoặc elliptic tuyến tính đều. Điều khiển tối ưu và lý thuyết động học hữu ích như động lực, không bắt buộc như giáo trình formal.

**Liên kết seminar.** LO1 (chương trình khó viết lại ngôn ngữ của một lĩnh vực) và LO6 (kỷ luật citation). Láng giềng giải tích: [Yu Deng / PDE động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (Boltzmann như chương kinetic sau), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (chính quy fully nonlinear *dùng* nghiệm nhớt), và [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) (để tách bài Millennium).

---

## 1. Vì sao cần một lý thuyết yếu

Một phương trình Hamilton–Jacobi kiểu tiến hóa trông vô hại,

$$
u_t + H\bigl(x,\nabla u\bigr) = 0,
$$

và trong điều khiển tối ưu hay quang hình học, ẩn $$u$$ là hàm giá trị hoặc pha eikonal. Phương pháp đặc trưng cho nghiệm trơn trong thời gian ngắn. Rồi các đặc trưng cắt nhau: gradient nhảy, và không còn nghiệm $$C^1$$ (huống chi $$C^2$$) để tiếp tục. Phương trình cấp hai fully nonlinear

$$
F\bigl(x,u,\nabla u,D^2 u\bigr) = 0
$$

còn khó hơn. Ẩn đi vào qua Hessian một cách phi tuyến (ví dụ Hamilton–Jacobi–Bellman từ điều khiển ngẫu nhiên, và một số phương trình độ cong). Chính quy elliptic cổ điển không áp sẵn, và không thể chỉ “lấy tích phân từng phần” như lý thuyết dạng phân kỳ tuyến tính sinh ra nghiệm yếu Sobolev.

Bài toán thiết kế vì thế mang tính khái niệm: tạo một lớp **nghiệm yếu** đủ lớn để tồn tại toàn cục, đủ nhỏ để duy nhất, và tương thích với **nguyên lý cực đại** mà lý thuyết elliptic và parabolic sống nhờ. Nghiệm phân bố là ngôn ngữ sai khi $$F$$ không tuyến tính theo $$D^2 u$$. Nghiệm nhớt trả lời bài toán thiết kế đó.

---

## 2. Nghiệm nhớt: chạm thay vì lấy đạo hàm

Ý tưởng Crandall–Lions (công bố rồi phát triển đầu thập niên 1980; bài Hamilton–Jacobi nền tảng là **Crandall–Lions, Trans. Amer. Math. Soc. 1983**) là kiểm tra một hàm $$u$$ chỉ liên tục bằng các hàm trơn chạm đồ thị từ trên hoặc từ dưới. Khẩu hiệu cho phương trình dừng $$F(x,u,\nabla u,D^2 u)=0$$: $$u$$ là **dưới-nghiệm** nhớt nếu, mỗi khi hàm thử trơn $$\varphi$$ chạm $$u$$ từ trên tại $$x_0$$, ta có

$$
F\bigl(x_0,u(x_0),\nabla\varphi(x_0),D^2\varphi(x_0)\bigr) \le 0
$$

(chiều bất đẳng thức tùy quy ước của $$F$$; user’s guide cố định quy ước cẩn thận). **Trên-nghiệm** là điều kiện chạm ngược lại. **Nghiệm nhớt** là cả hai.

Không gì trong định nghĩa đòi $$u$$ khả vi. Các đạo hàm đi vào $$F$$ được mượn từ hàm thử tại điểm tiếp xúc. Nếu $$u$$ tình cờ là $$C^2$$, định nghĩa thu về phương trình cổ điển từng điểm: đó là kiểm tra nhất quán.

**Vì sao gọi “nhớt” (viscosity)?** Một đường lịch sử xấp xỉ phương trình cấp một bằng cách thêm một số hạng cấp hai nhỏ $$\varepsilon\Delta u$$ (nhớt nhân tạo) rồi lấy giới hạn $$\varepsilon\to 0$$. Các bất đẳng thức sống sót chính là điều kiện chạm. Tên nhớ giới hạn nhớt triệt tiêu; định nghĩa hiện đại không đòi xây xấp xỉ mỗi lần.

**Evans** (cùng Crandall và Lions) làm rõ các phát biểu tương đương và tính chất cơ bản. **Ishii** đóng vai trò trung tâm khi mở rộng lý thuyết sang phương trình cấp hai fully nonlinear. **Souganidis** (thường cùng Lions và những người khác) phát triển ổn định, xấp xỉ, và lan truyền mặt trước, khiến lý thuyết dùng được trong hình học và ứng dụng. Công lao là cộng đồng; định nghĩa 1983 và hướng dẫn 1992 là hai mốc seminar cần gọi tên.

---

## 3. So sánh là động cơ

Tồn tại mà không duy nhất thì rẻ; duy nhất mà không tồn tại thì chỉ là khẩu hiệu. Lý thuyết nhớt kiếm được cả hai nhờ **so sánh**. Trong một bài Dirichlet điển hình: nếu $$u$$ là dưới-nghiệm nhớt và $$v$$ là trên-nghiệm nhớt của một phương trình elliptic đều (hoặc elliptic suy biến, dưới giả thuyết cấu trúc), và nếu $$u\le v$$ trên biên, thì $$u\le v$$ trong miền. Hai nghiệm nhớt cùng dữ liệu biên vì thế trùng nhau.

Động cơ là một lập luận nguyên lý cực đại được nâng cấp cho hàm không khả vi. Người ta xét cực đại của $$u(x)-v(y)$$ sau một phạt buộc $$x$$ và $$y$$ lại gần, áp định nghĩa chạm tại các điểm gần trùng, rồi dùng tính elliptic của $$F$$ để được mâu thuẫn trừ khi cực đại không dương. **User’s guide Crandall–Ishii–Lions** (*Bull. Amer. Math. Soc.* 1992; cũng [arXiv:math/9207212](https://arxiv.org/abs/math/9207212)) là trình bày chuẩn của phép tính cấp hai này: jet, định lý tổng, so sánh, và ổn định dưới giới hạn đều.

**Ổn định** là món quà kia. Giới hạn đều của nghiệm nhớt vẫn là nghiệm nhớt. Đó là lý do các xấp xỉ nhớt triệt tiêu, lược đồ số, và hàm giá trị điều khiển có thể được đồng nhất với nghiệm nhớt duy nhất một khi đã có nguyên lý so sánh.

**Khẩu hiệu.** Nghiệm nhớt là nghiệm yếu lấy nguyên lý cực đại làm luật, chứ không lấy đồng nhất thức tích phân từng phần.

---

## 4. Các trụ khác: DiPerna–Lions và concentration-compactness

Tài liệu 1994 rộng hơn Hamilton–Jacobi.

**Lý thuyết DiPerna–Lions.** Cùng **Ronald J. DiPerna**, Lions phát triển **nghiệm renormalized** cho phương trình Boltzmann: tồn tại toàn cục và ổn định yếu cho bài Cauchy dữ liệu lớn (*Ann. of Math.* **1989**). Toán tử va chạm khó định nghĩa trên mật độ chỉ khả tích; renormalization và compactness trung bình vận tốc khôi phục một phương trình có nghĩa. Cùng vòng ý tưởng sinh ra **phương trình vận chuyển** với trường vectơ Sobolev: đặc trưng không cần duy nhất theo nghĩa Lipschitz, nhưng lý thuyết phương trình liên tục vẫn đặt đúng (sau này Ambrosio và những người khác mở rộng). Ghép với [chương kinetic của Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): DiPerna–Lions là tính đặt đúng của chính phương trình động học; Deng–Hani–Ma là suy dẫn Boltzmann từ hạt. Các bậc khác nhau của bài toán thứ sáu Hilbert.

**Concentration-compactness.** Dãy cực tiểu hóa trên $$\mathbb{R}^n$$ có thể thoát bằng tịnh tiến hoặc vị tự. **Nguyên lý tập trung–compact** của Lions (trường hợp compact địa phương **1984**; trường hợp vị tự/giới hạn **1985**) phân loại những thất bại đó và khôi phục compactness khi một bất đẳng thức năng lượng chặt ngăn dichotomy. Đạo lý: nếu bài toán biến phân bất biến dưới một nhóm không compact, hãy đo *cách* compactness thất bại. Ứng dụng gồm cực trị Sobolev và một số bài hình học kiểu Yamabe.

Nét họ hàng với nghiệm nhớt là kiến trúc: tạo đúng đối tượng yếu, rồi chứng minh một cứng nhắc khiến nó duy nhất hoặc đạt được.

---

## 5. Huy chương 1994 không phải là gì

**Không phải chính quy Navier–Stokes.** Lions đóng góp lý thuyết tồn tại cho hệ Navier–Stokes **nén được** trong một số khung (cùng danh mục kinetic/fluid DiPerna–Lions). Đó không phải lời giải bài Clay về chính quy toàn cục của Navier–Stokes **không nén ba chiều**. Giữ [phát biểu Millennium]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) tách riêng.

**Không phải mean field games như citation.** Cùng **Jean-Michel Lasry**, Lions sau đó đưa vào **trò chơi trường trung bình** (ghi chú và *Comptes Rendus* **2006**): giới hạn continuum của cân bằng Nash cho nhiều tác nhân hữu tỷ, thường là hệ Hamilton–Jacobi–Bellman / Fokker–Planck liên kết. Lý thuyết dùng nghiệm nhớt và là ảnh hưởng lớn sau này đối với giải tích, kinh tế, và mô hình đám đông. Nó **sau 1994**. Đừng viết nó vào citation Fields.

**Không phải phát minh một mình.** Nghiệm nhớt là Crandall–Lions lúc sinh, Evans–Ishii–Souganidis khi mở rộng, và một cộng đồng về sau. Huy chương ghi nhận vai trò của Lions trong mạng đó và trong một danh mục PDE phi tuyến rộng hơn.

---

## 6. Vì sao là Huy chương Fields

Ba lý do khớp nhấn mạnh của Varadhan tại ICM.

1. **Một ngôn ngữ mới.** Nghiệm nhớt biến những phương trình không có nghiệm cổ điển thành bài toán đặt đúng. Cả lĩnh vực—điều khiển tối ưu, lan truyền mặt trước, một phần hình học fully nonlinear—có thể phát biểu định lý duy nhất mà trước đó nằm ngoài tầm formal.
2. **Nhiều máy sâu, không một bổ đề.** Concentration-compactness và lý thuyết DiPerna–Lions là kiến trúc độc lập; cùng nhau chúng cho thấy một phong cách: chẩn đoán thất bại của compactness hoặc khả vi cổ điển, rồi xây phép tính quanh thất bại đó.
3. **Ứng dụng như nguồn định lý.** Văn bản ICM nhấn rằng việc chọn bài toán được thúc đẩy bởi ứng dụng. Đó không phải giải an ủi. Đó là phương pháp nghiên cứu: toán tử va chạm Boltzmann, hàm giá trị của bài điều khiển, và cực trị Sobolev trên $$\mathbb{R}^n$$ đều buộc một khái niệm nghiệm hoặc compactness mới.

Một chương sau—mean field games, bài giảng Collège de France—tiếp tục phương pháp. Huy chương 1994 đã đủ.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Nghiệm nhớt là nghiệm cổ điển $$C^2$$ với thêm nhớt.” | Chúng là nghiệm *yếu* định nghĩa bằng bất đẳng thức hàm thử; nghiệm $$C^2$$ là trường hợp đặc biệt. |
| “Viscosity nghĩa là độ nhớt vật lý của chất lưu.” | Tên nhớ các *xấp xỉ* nhớt triệt tiêu; định nghĩa không đòi một chất lưu. |
| “Lions đã giải Navier–Stokes.” | Không. Kết quả tồn tại nén được không phải bài chính quy không nén của Clay. |
| “Mean field games mang lại huy chương 1994.” | Mean field games Lasry–Lions thuộc giữa thập niên 2000; chỉ là ảnh hưởng sau. |
| “Nghiệm phân bố đã đủ cho phương trình fully nonlinear.” | Khi $$F$$ phi tuyến theo $$D^2 u$$, tích phân từng phần là động cơ sai; so sánh mới đúng. |
| “Lions một mình phát minh nghiệm nhớt.” | Crandall–Lions; rồi Evans, Ishii, Souganidis, và nhiều người khác. |
| “DiPerna–Lions suy dẫn Boltzmann từ hạt.” | Nó cho một lý thuyết động học đặt đúng; suy dẫn từ hạt là câu chuyện khác (sau này). |

---

## Bài tập

1. Bằng lời của bạn: vì sao đặc trưng của $$u_t+H(\nabla u)=0$$ có thể sinh nhảy gradient trong thời gian hữu hạn? Vì sao điều đó buộc một lý thuyết yếu?
2. Viết định nghĩa chạm của dưới-nghiệm nhớt cho $$u_t+H(\nabla u)=0$$, rồi kiểm tra nhất quán: nếu $$u$$ là $$C^1$$, định nghĩa thu về bất đẳng thức cổ điển.
3. Vì sao **so sánh** quý hơn một xây dựng tồn tại formal? Trả lời tối đa sáu câu.
4. Lướt những trang đầu Crandall–Ishii–Lions (BAMS 1992 hoặc arXiv:math/9207212). Liệt kê ba từ jargon (jet, hàm thử, elliptic suy biến) và chú thích một dòng cho mỗi từ.
5. Phân biệt, trong một bảng của bạn, **nghiệm nhớt**, **nghiệm renormalized DiPerna–Lions**, và **concentration-compactness**. Mỗi cái xử lý thất bại nào của lý thuyết cổ điển?
6. **Luyện độ chính xác.** Tìm một câu nói huy chương 1994 là “vì mean field games.” Viết lại bằng hai câu chính xác.
7. **Seminar mở rộng.** So sánh so sánh nhớt với nguyên lý cực đại cho hàm điều hòa: cái gì được thừa kế, và cái gì phải xây lại cho $$u$$ không khả vi?

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

- Đọc user’s guide như giáo trình seminar: so sánh trước, ví dụ sau.
- So sánh giới hạn nhớt triệt tiêu với nghiệm entropy của luật bảo toàn vô hướng (một lý thuyết yếu họ hàng, không cùng định nghĩa).
- Nếu đi tiếp về ứng dụng, hãy xem mean field games như *người tiêu thụ* nghiệm nhớt, định niên đại sau huy chương.
- Tùy chọn seminar A3: một trang “nghiệm nhớt không phải là gì” (không phải NS, không phải MFG-như-citation, không phải độ nhớt chất lưu).
