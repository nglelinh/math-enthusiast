---
layout: post
title: "Không gian Hilbert và ngôn ngữ phổ của cơ học lượng tử"
chapter: '06'
order: 18
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Giữa thập niên 1920, vật lý học rơi vào một tình huống lạ lùng: cùng một nguyên tử hydro mà có tới hai lý thuyết trông chẳng giống nhau chút nào. Werner Heisenberg mô tả electron bằng những bảng số vô hạn nhân với nhau không giao hoán (cơ học ma trận), còn Erwin Schrödinger lại viết ra một phương trình sóng liên tục trông như phương trình truyền sóng trên mặt nước (cơ học sóng). Cả hai đều cho ra đúng các vạch quang phổ đo được trong phòng thí nghiệm! Chính nhà toán học John von Neumann đã bước vào và chỉ ra bí mật đằng sau: hai lý thuyết ấy thực ra chỉ là **hai hệ tọa độ khác nhau của cùng một không gian hình học vô hạn chiều** — **không gian Hilbert**.

Nếu cơ học cổ điển theo dõi một điểm chuyển động trong không gian pha, thì cơ học lượng tử chuyển toàn bộ câu chuyện sang hình học tuyến tính: **trạng thái là một vectơ** (hoặc toán tử mật độ), **đại lượng đo được là một toán tử tuyến tính**, còn kết quả và xác suất đo được đọc ra từ **phổ** và các phép chiếu trực giao. Bài này nối trực tiếp từ thế giới hữu hạn chiều của [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) sang các hệ liên tục vô hạn chiều và [bài trung tâm về vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Bản đồ kiến thức nền: Giải tích hàm, không gian Hilbert và lý thuyết phổ nghiên cứu những gì?

Bạn đã quen với không gian Euclid $$\mathbb{R}^3$$ từ đại số tuyến tính: ở đó ta biết cộng vectơ, đo độ dài, tính góc vuông qua tích vô hướng, và chéo hóa một ma trận đối xứng để tìm các trục chính (trị riêng và vectơ riêng). Nhưng khi đối tượng không còn là mũi tên 3 tọa độ mà là **một hàm số** $$\psi(x)$$ xác định trên cả trục số thực — tức một vectơ có vô hạn thành phần — thì mọi chuyện tinh tế hơn rất nhiều.

**Giải tích hàm** (functional analysis) và **lý thuyết phổ** (spectral theory) ra đời để trả lời câu hỏi: *điều gì của đại số tuyến tính vẫn còn sống sót ở vô hạn chiều, và điều gì bị gãy đổ?*

- **Không gian Hilbert là gì?** Hãy hình dung nó là phiên bản vô hạn chiều "ngoan ngoãn" nhất của không gian Euclid phức $$\mathbb{C}^n$$: nó có **tích vô hướng** (nên ta vẫn đo được độ dài và trực giao, vẫn có định lý Pythagoras và chuỗi trực chuẩn như chuỗi Fourier) và có **tính đầy đủ** (mọi dãy Cauchy — những dãy tiến sát nhau mãi — đều hội tụ về một phần tử *nằm bên trong* không gian, không bị "rơi ra lỗ thủng").
- **Lý thuyết phổ nghiên cứu gì?** Với ma trận $$n\times n$$, ta tìm trị riêng $$\lambda$$ sao cho $$Av = \lambda v$$. Nhưng ở vô hạn chiều, một toán tử tự nhiên như toán tử vị trí $$(X\psi)(x) = x\psi(x)$$ trên $$L^2(\mathbb{R})$$ lại **không có một vectơ riêng nào nằm trong $$L^2$$**! Thay vì chỉ tìm trị riêng rời rạc, lý thuyết phổ nghiên cứu toàn bộ **phổ** $$\sigma(A)$$ — gồm cả phần rời rạc (như các mức năng lượng liên kết của nguyên tử hydro) lẫn phần liên tục (như năng lượng của hạt tự do bay tự do ngoài không gian).
- **Vì sao lại dùng số phức?** Trong cơ học lượng tử, không chỉ độ lớn mà cả **pha** $$e^{i\theta}$$ của biên độ cũng tạo ra giao thoa, và toán tử tiến hóa theo thời gian $$U(t) = e^{-itH/\hbar}$$ cần đơn vị ảo $$i$$ để biến một toán tử tự liên hợp $$H$$ (có phổ thực) thành phép quay bảo toàn độ dài $$U(t)$$.

Nắm được bộ ba **không gian Hilbert – toán tử tự liên hợp – định lý phổ**, bạn có trong tay khung xương toán học của toàn bộ cơ học lượng tử hiện đại.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa **không gian Hilbert** ở mức đại học (có tích vô hướng và đầy đủ), và cho ví dụ $$\mathbb{C}^n$$, $$L^2(\mathbb{R})$$.
- Giải thích ý chính của quy tắc Born: xác suất được tính bằng $$|\langle\phi|\psi\rangle|^2$$ với các vectơ đơn vị.
- Giải thích vì sao **đại lượng quan sát được** được mô hình bằng toán tử tự liên hợp (phổ thực, độ đo phổ gồm các phép chiếu trực giao).
- Phác thảo **định lý phổ** cho ma trận Hermite, và ý chính của phiên bản vô hạn chiều cho toán tử không bị chặn.
- Mô tả sự tiến hóa theo thời gian như một **nhóm unita** $$e^{-itH/\hbar}$$ sinh bởi Hamiltonian.
- Nêu các điểm cần thận trọng: cách nói về biến ẩn, "sụp đổ hàm sóng" so với tiên đề về phép đo, việc bỏ qua miền xác định của toán tử không bị chặn.

**Kiến thức nền.** Đại số tuyến tính (trị riêng, cơ sở trực chuẩn); số phức. Không cần lý thuyết độ đo.

---

## 1. Từ ma trận hữu hạn đến không gian Hilbert

Một qubit được mô tả trong $$\mathbb{C}^2$$: trạng thái thuần là một vectơ đơn vị, sai khác một pha tổng thể. Hai qubit được mô tả trong $$\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathbb{C}^4$$. Ở đây, cơ học lượng tử hữu hạn chiều thực chất là đại số tuyến tính quen thuộc với ma trận Hermite và phép quay unita.

Các hệ liên tục cần không gian vô hạn chiều. Một hạt chuyển động trên đường thẳng có hàm sóng $$\psi\in L^2(\mathbb{R})$$ — tập các hàm bình phương khả tích $$\int_{-\infty}^{\infty} |\psi(x)|^2\,dx < \infty$$ — với tích vô hướng

$$
\langle\phi|\psi\rangle = \int_{-\infty}^{\infty} \overline{\phi(x)}\,\psi(x)\,dx.
$$

Chính **tính đầy đủ** (mọi dãy Cauchy đều hội tụ trong $$L^2$$) làm cho không gian này là một **không gian Hilbert**, chứ không chỉ là không gian có tích vô hướng. Để thấy tính đầy đủ quan trọng thế nào, hãy nghĩ tới không gian các hàm liên tục trên $$[0,1]$$ với chuẩn $$L^2$$: ta có thể dựng một dãy hàm liên tục mịn tiến dần về hàm bậc thang nhảy vọt, nghĩa là giới hạn của dãy đã *rơi ra ngoài* không gian các hàm liên tục! Việc mở rộng sang $$L^2$$ lấp đầy mọi "lỗ thủng" đó, nhờ vậy các phép chiếu trực giao và khai triển theo cơ sở trực chuẩn luôn tồn tại. Trong tính toán vật lý nhanh, điều này thường bị ẩn đi; nhưng cơ học lượng tử ở dạng toán học chặt chẽ được xây dựng trên chính nền tảng ấy.

---

## 2. Trạng thái, tia và toán tử mật độ

**Trạng thái thuần** là một vectơ đơn vị $$\psi$$, hay nói chính xác hơn là một **tia** $$\{e^{i\theta}\psi\}$$ (vì nhân toàn bộ vectơ với một số phức có môđun 1 không làm thay đổi bất kỳ xác suất đo nào). Một **đại lượng quan sát** $$A$$ là một ma trận Hermite trên $$\mathbb{C}^n$$, có các trị riêng thực $$a_k$$ và các vectơ riêng trực chuẩn $$u_k$$. Đo $$A$$ ở trạng thái $$\psi$$ cho kết quả $$a_k$$ với xác suất $$|\langle u_k|\psi\rangle|^2$$ (trong trường hợp không suy biến).

Hãy thử một ví dụ cụ thể bằng tay trên $$\mathbb{C}^2$$: xét ma trận Pauli $$A = \sigma_z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$ có hai vectơ riêng là $$|0\rangle = (1,0)^T$$ (trị riêng $$+1$$) và $$|1\rangle = (0,1)^T$$ (trị riêng $$-1$$). Nếu hệ ở trạng thái chồng chập $$\psi = \frac{\sqrt{3}}{2}|0\rangle + \frac{i}{2}|1\rangle$$, ta thấy $$\|\psi\|^2 = \frac{3}{4} + \frac{1}{4} = 1$$. Khi đo $$A$$, xác suất thu được $$+1$$ là $$|\langle 0|\psi\rangle|^2 = 3/4$$, còn xác suất thu được $$-1$$ là $$|\langle 1|\psi\rangle|^2 = 1/4$$. Về mặt hình học, quy tắc Born đơn giản là **bình phương độ dài hình chiếu trực giao** của vectơ trạng thái lên từng trục riêng!

**Trạng thái hỗn hợp** xuất hiện khi ta không biết chắc hệ đang ở trạng thái thuần nào (ví dụ do tương tác với môi trường hoặc vướng víu với hệ khác mà ta bỏ qua). Khi đó ta dùng **toán tử mật độ** $$\rho\geq 0$$, $$\operatorname{tr}\rho=1$$, với giá trị kỳ vọng $$\operatorname{tr}(\rho A)$$. Thông tin lượng tử hữu hạn chiều gần như hoàn toàn dùng ngôn ngữ này.

---

## 3. Tính tự liên hợp và định lý phổ

**Vì sao cần tự liên hợp?** Trong thực nghiệm, kết quả đo một đại lượng vật lý (năng lượng, vị trí, spin) phải là số thực. Một ma trận Hermite ($$A = A^\dagger$$) trên $$\mathbb{C}^n$$ luôn có các trị riêng thực và một cơ sở trực chuẩn gồm các vectơ riêng:

$$
A = \sum_k a_k |u_k\rangle\langle u_k|.
$$

Đó là **định lý phổ** trong trường hợp hữu hạn chiều: mọi toán tử Hermite đều phân rã thành tổng có trọng số của các phép chiếu trực giao lên các trục riêng.

Nhưng khi bước sang vô hạn chiều, nhiều toán tử vật lý quan trọng nhất lại **không bị chặn** — chẳng hạn toán tử xung lượng $$P = -i\hbar \frac{d}{dx}$$ hay Hamiltonian $$H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$$. Không phải hàm $$L^2$$ nào cũng khả vi, nên $$P$$ hay $$H$$ chỉ xác định trên một **miền trù mật** $$D(A) \subset \mathcal{H}$$. Lúc này, điều kiện đối xứng hình thức $$\langle \phi, A\psi\rangle = \langle A\phi, \psi\rangle$$ là *chưa đủ* — ta cần điều kiện chặt hơn là **tính tự liên hợp** ($$D(A) = D(A^*)$$). Ví dụ kinh điển: xét toán tử xung lượng $$-i\frac{d}{dx}$$ trên đoạn hữu hạn $$[0,1]$$. Nếu chọn điều kiện biên $$\psi(0)=\psi(1)=0$$, toán tử đối xứng nhưng *không* tự liên hợp và không sinh ra tiến hóa unita; chỉ khi chọn điều kiện biên tuần hoàn $$\psi(1)=e^{i\theta}\psi(0)$$ thì nó mới trở thành tự liên hợp!

Tính tự liên hợp bảo đảm phổ là tập con của $$\mathbb{R}$$ và tồn tại duy nhất một **độ đo phổ** $$E$$ nhận giá trị là các phép chiếu trực giao, sao cho

$$
A = \int_{\sigma(A)} \lambda\,dE(\lambda)
$$

theo nghĩa thích hợp. Nhờ đó, xác suất để phép đo $$A$$ rơi vào khoảng $$[a,b]$$ được định nghĩa hoàn toàn chặt chẽ là $$\|E([a,b])\psi\|^2$$, kể cả khi phổ là liên tục. Song hành với nó là **định lý Stone**, nối một–một các nhóm unita liên tục mạnh $$U(t)$$ với phần tử sinh tự liên hợp $$H$$ của chúng. Nhờ vậy, động lực học và phép đo dùng chung một ngôn ngữ phổ.

**Sự chặt chẽ cho ta điều gì.** Với các hệ liên tục, những vấn đề như tính tự liên hợp cốt yếu (chọn điều kiện biên đúng tại kỳ dị thế năng Coulomb), sự ổn định của vật chất, lý thuyết tán xạ, hay phổ liên tục không phải là chú thích phụ có thể bỏ qua — chúng quyết định liệu mô hình vật lý có tiên đoán duy nhất hay không.

---

## 4. Động lực học và phương trình Schrödinger

Cho Hamiltonian tự liên hợp $$H$$,

$$
i\hbar \frac{d}{dt}\psi(t) = H\psi(t) \quad\Longleftrightarrow\quad \psi(t)= e^{-itH/\hbar}\psi(0)
$$

với $$\psi(0)$$ nằm trong miền thích hợp (hoặc mở rộng liên tục cho mọi vectơ trong $$\mathcal{H}$$ nhờ nhóm unita $$U(t)=e^{-itH/\hbar}$$). Bảo toàn tổng xác suất theo thời gian chính là tính unita: $$\|\psi(t)\|=\|\psi(0)\|$$. Về trực giác hình học, tiến hóa lượng tử của một hệ cô lập chỉ là một **phép quay đều trong không gian Hilbert phức** — độ dài vectơ trạng thái không bao giờ đổi, chỉ có hướng và pha tương đối giữa các thành phần riêng xoay với các tần số khác nhau $$e^{-iE_k t/\hbar}$$.

---

## 4b. Đại lượng quan sát không giao hoán (gợi ý đọc thêm)

Tính tự liên hợp bảo đảm từng đại lượng quan sát riêng lẻ hoạt động đúng. Nhưng một **cặp** đại lượng thì khác: nếu $$[A,B]\neq 0$$, hai toán tử không có chung một cơ sở gồm các vectơ riêng (chúng chỉ có thể có vectơ riêng chung trong hạch của giao hoán tử), và bất đẳng thức Robertson chặn dưới tích các độ lệch chuẩn bởi $$\tfrac12\bigl|\langle[A,B]\rangle\bigr|$$. Vị trí và xung lượng thỏa $$[X,P]=i\hbar$$, nên bất đẳng thức Fourier $$\sigma_x\sigma_p\ge\hbar/2$$ thực chất là một hệ quả trực tiếp của giao hoán tử. Bài đọc hiểu đầy đủ, gồm bất đẳng thức Kennard, dạng Weyl, ý chính của định lý Stone–von Neumann, và những thận trọng với hệ thức năng lượng–thời gian, là bài [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/).

---

## 5. Delta Dirac, phân bố và sự trung thực

Trong giáo trình vật lý, ta rất hay gặp ký hiệu $$|x\rangle$$ cho "trạng thái có vị trí chính xác tại $$x$$" với $$\langle x|x'\rangle = \delta(x-x')$$. Thực tế, hàm delta Dirac và sóng phẳng $$e^{ipx/\hbar}$$ **không nằm trong $$L^2(\mathbb{R})$$** (vì tích phân bình phương của chúng phân kỳ). Chúng là những lý tưởng hóa cực kỳ tiện dụng cho tính toán, nhưng không phải vectơ thật của không gian Hilbert.

**Lý thuyết phân bố** của Laurent Schwartz và **không gian Hilbert trang bị** (rigged Hilbert space — bộ ba $$\Phi \subset \mathcal{H} \subset \Phi'$$, với $$\Phi$$ là không gian các hàm thử rất mịn và $$\Phi'$$ là không gian các phiếm hàm tuyến tính trên đó) làm cho nhiều thao tác của Dirac trở nên chặt chẽ. Bài học ở đây là:

> Ký hiệu hình thức của vật lý là chỉ dẫn; các định lý về không gian Hilbert mới là cam kết.

Tích phân đường (Feynman) là một cách trình bày khác, tương đương trong nhiều bối cảnh, nhưng địa vị của độ đo trong đó rất tinh tế. Xem bài trung tâm về vật lý toán.

---

## 6. Toán học nảy sinh từ đây

| Cấu trúc | Nguồn gốc / ứng dụng trong vật lý |
|----------|---------------------|
| Không gian Hilbert, toán tử | Trạng thái và đại lượng quan sát trong cơ học lượng tử |
| Định lý phổ | Phép đo và động lực học |
| Đại số toán tử (von Neumann, C*) | Hệ vô hạn, lý thuyết trường lượng tử đại số |
| Không gian Hilbert trang bị | Vectơ riêng suy rộng |
| Lý thuyết nửa nhóm | Hệ mở, động lực học tiêu tán |

Hệ tiên đề của von Neumann đã biến cơ học ma trận và cơ học sóng, vốn ban đầu còn mang tính trực quan rời rạc, thành một khung giải tích thống nhất có thể kiểm tra chặt chẽ.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Cơ học lượng tử chỉ là xác suất với số phức." | Thiếu | Đại lượng quan sát không giao hoán và hiện tượng vướng víu vượt ra ngoài xác suất cổ điển. |
| "Hàm sóng là một đám mây điện tích nhỏ." | Chỉ là hình ảnh | $$\vert\psi\vert^2$$ là mật độ xác suất (quy tắc Born). |
| "Cơ học lượng tử vô hạn chiều chỉ là ma trận rất lớn." | Dễ sai | Miền xác định, phổ liên tục, tính không bị chặn tạo ra những hiện tượng mới thật sự. |
| "Định lý phổ đã giải quyết bài toán đo lường." | Sai | Định lý phổ sắp xếp các kết quả đo; còn cách diễn giải và nền tảng vẫn đang được tranh luận. |

---

## Tài liệu tham khảo

1. Hall, *Quantum Theory for Mathematicians* (Lý thuyết lượng tử cho nhà toán học).  
2. Reed & Simon, *Methods of Modern Mathematical Physics* (Các phương pháp của vật lý toán hiện đại), tập I.  
3. Trong khóa học: [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).  
