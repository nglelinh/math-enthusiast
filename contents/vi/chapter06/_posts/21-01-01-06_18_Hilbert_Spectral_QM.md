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

Cơ học cổ điển theo dõi một điểm trong không gian pha. Cơ học lượng tử thì mô tả **trạng thái bằng vectơ** (hoặc toán tử mật độ) và **đại lượng quan sát bằng toán tử**; các xác suất đo được đọc ra từ phổ và các phép chiếu. Ngôn ngữ toán học cho điều này là **không gian Hilbert**, tức không gian có tích vô hướng và đầy đủ, cùng với **định lý phổ** cho các toán tử tự liên hợp.

Bài này giúp bạn đọc hiểu các ý chính: vì sao lại dùng không gian Hilbert phức, tính tự liên hợp cho ta điều gì, tiến hóa unita hoạt động thế nào, và ở chỗ nào cách làm chặt chẽ khác với "cơ học lượng tử bằng ma trận hữu hạn". Bài nối từ [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) (hữu hạn chiều) sang các hệ liên tục và [bài trung tâm về vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

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

Một qubit được mô tả trong $$\mathbb{C}^2$$: trạng thái thuần là một vectơ đơn vị, sai khác một pha tổng thể. Hai qubit được mô tả trong $$\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathbb{C}^4$$. Cơ học lượng tử hữu hạn chiều chính là đại số tuyến tính với ma trận Hermite và tiến hóa unita.

Các hệ liên tục cần không gian vô hạn chiều. Một hạt trên đường thẳng có hàm sóng $$\psi\in L^2(\mathbb{R})$$, với tích vô hướng

$$
\langle\phi|\psi\rangle = \int_{-\infty}^{\infty} \overline{\phi(x)}\,\psi(x)\,dx.
$$

Tính đầy đủ (mọi dãy Cauchy đều hội tụ trong $$L^2$$) làm cho không gian này là một **không gian Hilbert**, chứ không chỉ là không gian có tích vô hướng. Trong tính toán vật lý, điều này thường bị bỏ qua; nhưng cơ học lượng tử ở dạng toán học chặt chẽ được xây dựng trên chính nền tảng đó.

---

## 2. Trạng thái, tia và toán tử mật độ

**Trạng thái thuần** là một vectơ đơn vị $$\psi$$, hay nói chính xác hơn là một **tia** $$\{e^{i\theta}\psi\}$$. Một **đại lượng quan sát** $$A$$ là một ma trận Hermite trên $$\mathbb{C}^n$$, có các trị riêng thực $$a_k$$ và các vectơ riêng trực chuẩn $$u_k$$. Đo $$A$$ ở trạng thái $$\psi$$ cho kết quả $$a_k$$ với xác suất $$|\langle u_k|\psi\rangle|^2$$ (trong trường hợp không suy biến).

**Trạng thái hỗn hợp** dùng toán tử mật độ $$\rho\geq 0$$, $$\operatorname{tr}\rho=1$$, với giá trị kỳ vọng $$\operatorname{tr}(\rho A)$$. Thông tin lượng tử hữu hạn chiều gần như hoàn toàn dùng ngôn ngữ này.

---

## 3. Tính tự liên hợp và định lý phổ

**Vì sao cần tự liên hợp?** Trong sách giáo khoa, kết quả đo là số thực. Một ma trận Hermite trên $$\mathbb{C}^n$$ có các trị riêng thực và một cơ sở trực chuẩn gồm các vectơ riêng:

$$
A = \sum_k a_k |u_k\rangle\langle u_k|.
$$

Đó là định lý phổ trong trường hợp hữu hạn chiều.

Ở vô hạn chiều, nhiều toán tử vật lý **không bị chặn** (xung lượng, Hamiltonian). Chúng chỉ được định nghĩa trên một miền trù mật. **Tính tự liên hợp** (một điều kiện chính xác về miền xác định, mạnh hơn tính Hermite hình thức) bảo đảm phổ là thực và có một độ đo phổ $$E$$ nhận giá trị là các phép chiếu, sao cho

$$
A = \int_{\sigma(A)} \lambda\,dE(\lambda)
$$

theo nghĩa thích hợp. **Định lý Stone** nối các nhóm unita liên tục mạnh với phần tử sinh tự liên hợp của chúng. Nhờ vậy, động lực học và đại lượng quan sát dùng chung một ngôn ngữ phổ.

**Sự chặt chẽ cho ta điều gì.** Với các hệ liên tục, những vấn đề như tính tự liên hợp cốt yếu, sự ổn định của vật chất, lý thuyết tán xạ, phổ liên tục không phải là chú thích phụ có thể bỏ qua.

---

## 4. Động lực học và phương trình Schrödinger

Cho Hamiltonian tự liên hợp $$H$$,

$$
i\hbar \frac{d}{dt}\psi(t) = H\psi(t) \quad\Longleftrightarrow\quad \psi(t)= e^{-itH/\hbar}\psi(0)
$$

với $$\psi(0)$$ nằm trong miền thích hợp (hoặc mở rộng liên tục cho mọi vectơ nhờ nhóm unita). Bảo toàn xác suất chính là tính unita: $$\|\psi(t)\|=\|\psi(0)\|$$.

---

## 4b. Đại lượng quan sát không giao hoán (gợi ý đọc thêm)

Tính tự liên hợp bảo đảm từng đại lượng quan sát riêng lẻ hoạt động đúng. Nhưng một **cặp** đại lượng thì khác: nếu $$[A,B]\neq 0$$, hai toán tử không có chung một cơ sở gồm các vectơ riêng (chúng chỉ có thể có vectơ riêng chung trong hạch của giao hoán tử), và bất đẳng thức Robertson chặn dưới tích các độ lệch chuẩn bởi $$\tfrac12\bigl|\langle[A,B]\rangle\bigr|$$. Vị trí và xung lượng thỏa $$[X,P]=i\hbar$$, nên bất đẳng thức Fourier $$\sigma_x\sigma_p\ge\hbar/2$$ thực chất là một hệ quả của giao hoán tử. Bài đọc hiểu đầy đủ, gồm bất đẳng thức Kennard, dạng Weyl, ý chính của định lý Stone–von Neumann, và những thận trọng với hệ thức năng lượng–thời gian, là bài [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/).

---

## 5. Delta Dirac, phân bố và sự trung thực

Trạng thái riêng của vị trí $$|x\rangle$$ và hàm delta Dirac là những lý tưởng hóa nằm ngoài $$L^2$$. **Lý thuyết phân bố** của Schwartz và **không gian Hilbert trang bị** (rigged Hilbert space) làm cho nhiều thao tác của Dirac trở nên chặt chẽ. Bài học ở đây là:

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

Hệ tiên đề của von Neumann đã biến cơ học ma trận và cơ học sóng, vốn còn mang tính trực quan, thành một khung giải tích có thể kiểm tra chặt chẽ.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Cơ học lượng tử chỉ là xác suất với số phức." | Thiếu | Đại lượng quan sát không giao hoán và hiện tượng vướng víu vượt ra ngoài xác suất cổ điển. |
| "Hàm sóng là một đám mây điện tích nhỏ." | Chỉ là hình ảnh | $$|\psi|^2$$ là mật độ xác suất (quy tắc Born). |
| "Cơ học lượng tử vô hạn chiều chỉ là ma trận rất lớn." | Dễ sai | Miền xác định, phổ liên tục, tính không bị chặn tạo ra những hiện tượng mới thật sự. |
| "Định lý phổ đã giải quyết bài toán đo lường." | Sai | Định lý phổ sắp xếp các kết quả đo; còn cách diễn giải và nền tảng vẫn đang được tranh luận. |

---

## Bài tập

1. **Tích vô hướng.** Kiểm tra rằng $$\langle\phi|\psi\rangle=\sum_i\overline{\phi_i}\psi_i$$ trên $$\mathbb{C}^n$$ tuyến tính theo $$\psi$$ và phản tuyến tính (liên hợp tuyến tính) theo $$\phi$$.  
2. **Quy tắc Born.** Với $$\psi=(1/\sqrt{2},1/\sqrt{2})$$ và $$A=\operatorname{diag}(1,-1)$$, tính xác suất của từng kết quả đo.  
3. **Tự liên hợp.** Vì sao một ma trận không Hermite là mô hình không phù hợp cho một đại lượng quan sát có kết quả đo là số thực?  
4. **$$L^2$$.** Vì sao hàm hằng $$1$$ không thuộc $$L^2(\mathbb{R})$$?  
5. **Tiến hóa unita.** Chứng minh rằng nếu $$U(t)=e^{-itH/\hbar}$$ với $$H$$ là ma trận Hermite trên $$\mathbb{C}^n$$ thì $$\|U(t)\psi\|=\|\psi\|$$.  
6. **Cầu nối.** Viết một đoạn nối bài này với qubit trong bài thông tin lượng tử.  
7. **Giao hoán tử.** Vì sao dùng ma trận không Hermite là sai *loại* công cụ khi bàn về nguyên lý bất định, và bạn sẽ gặp $$[X,P]=i\hbar$$ ở bài nào tiếp theo?

---

## Tài liệu tham khảo

1. Hall, *Quantum Theory for Mathematicians* (Lý thuyết lượng tử cho nhà toán học).  
2. Reed & Simon, *Methods of Modern Mathematical Physics* (Các phương pháp của vật lý toán hiện đại), tập I.  
3. Trong khóa học: [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).  
