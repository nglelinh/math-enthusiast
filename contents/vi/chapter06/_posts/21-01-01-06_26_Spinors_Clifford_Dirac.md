---
layout: post
title: "Spinor, đại số Clifford và phương trình Dirac"
chapter: '06'
order: 26
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Hãy thử một trò ảo thuật ngay trên bàn tay của bạn (trò "chiếc cốc cà phê" hay *Dirac belt trick*): đặt lòng bàn tay ngửa lên như đang bưng một tách trà, rồi xoay bàn tay đúng **một vòng $$360^\circ$$** mà không làm đổ tách trà. Tay bạn lúc này bị xoắn vặn khó chịu — nó *chưa* trở về trạng thái ban đầu! Thế nhưng nếu bạn tiếp tục xoay thêm **một vòng $$360^\circ$$ nữa** (tổng cộng $$720^\circ$$) theo cùng một chiều, cánh tay bỗng tự tháo xoắn một cách kỳ diệu và trở về y hệt tư thế xuất phát! Đó không chỉ là trò vui về giải phẫu khớp vai: **electron, proton, neutron và mọi hạt vật chất (fermion) trong vũ trụ đều hành xử đúng như cánh tay ấy.** Quay một vectơ $$360^\circ$$ thì nó trở về chính nó, nhưng quay một **spinor** $$360^\circ$$ thì nó bị nhân với dấu $$-1$$; phải quay đủ $$720^\circ$$ nó mới trở lại trạng thái ban đầu.

Bí mật hình học của phép quay $$720^\circ$$ nằm ở **nhóm Spin**, **đại số Clifford**, và **toán tử Dirac** — toán tử mà Paul Dirac phát minh năm 1928 ở tuổi 25 khi tìm cách "lấy căn bậc hai" của phương trình sóng tương đối tính, và từ 8 ký hiệu ngắn ngủi ấy ông tiên đoán luôn sự tồn tại của phản vật chất! Bài tổng quan này nối lý thuyết biểu diễn, hình học và loại toán tử elliptic được giới toán học yêu thích nhất trong định lý chỉ số. Nên đọc kèm các bài [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/), [không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [định lý chỉ số Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/).

---

## Bản đồ kiến thức nền: Spinor, Đại số Clifford và Hình học spin đứng trên ba trụ cột nào?

Với hành trang đại số tuyến tính (ma trận quay $$3\times 3$$, số phức, ma trận Pauli) và phương trình vi phân bậc hai (phương trình sóng, toán tử Laplace), ta có thể nắm trọn ba trụ cột của bài này mà không cần phép màu nào:

### 1. Nhóm Spin và Phủ kép của nhóm quay
Không gian mọi phép quay 3 chiều $$SO(3)$$ có một đặc tính tô pô kỳ lạ: một đường cong khép kín ứng với phép quay $$360^\circ$$ quanh một trục *không thể* co liên tục về điểm đứng yên, nhưng đường cong ứng với phép quay $$720^\circ$$ thì *co được*! Vì thế nhóm cơ bản của $$SO(3)$$ là $$\mathbb{Z}/2\mathbb{Z}$$, và nó có một **không gian phủ kép đơn liên** là $$\mathrm{Spin}(3) \cong SU(2)$$ — trong đó hai phần tử đối nhau $$+U$$ và $$-U$$ cùng chiếu xuống đúng một phép quay vật lý. Trong cơ học lượng tử, trạng thái chỉ xác định sai khác một pha, nên tự nhiên được phép dùng biểu diễn của phủ kép $$SU(2)$$ — đó chính là **spinor** (hạt spin-$$1/2$$).

### 2. Đại số Clifford — "lấy căn bậc hai của dạng toàn phương"
Muốn viết tổng bình phương $$\partial_x^2 + \partial_y^2 + \partial_z^2$$ thành bình phương của một biểu thức tuyến tính $$\gamma_1 \partial_x + \gamma_2 \partial_y + \gamma_3 \partial_z$$, các hệ số $$\gamma_k$$ không thể là số thực hay số phức giao hoán mà buộc phải **phản giao hoán** ($$\gamma_j\gamma_k + \gamma_k\gamma_j = 0$$ với $$j \neq k$$). **Đại số Clifford** chính là hệ đại số sinh bởi quy tắc phản giao hoán đó — tổng quát hóa cả số phức $$\mathbb{C}$$, quaternion $$\mathbb{H}$$ (ứng dụng rộng rãi trong đồ họa 3D và định hướng robot/vệ tinh) lẫn các ma trận Pauli và Dirac.

### 3. Toán tử Dirac và Hình học spin
Khi mang phép "lấy căn bậc hai của toán tử Laplace" lên một đa tạp cong (như mặt cầu hay không–thời gian 4 chiều), ta thu được **toán tử Dirac** $$D$$. Nó là chiếc cầu nối vĩ đại nhất giữa hình học vi phân và tô pô: chỉ số của $$D$$ (đếm số nghiệm độc lập của $$D\psi = 0$$ theo tính chẵn lẻ) là một bất biến tô pô sâu sắc ($$\hat{A}$$-genus), đồng thời đặt ra những ràng buộc mạnh lên độ cong vô hướng của không gian.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao spin-$$1/2$$ cần đến **phủ kép** của nhóm quay ($$SU(2)\to SO(3)$$).
- Nêu định nghĩa cơ bản của **đại số Clifford**: các phần tử sinh $$\gamma_\mu$$ thỏa $$\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}$$.
- Viết **phương trình Dirac** tự do $$(i\gamma^\mu\partial_\mu-m)\psi=0$$ và nêu bài toán lịch sử mà nó giải quyết (electron tương đối tính, spin, và phản hạt theo cách diễn giải của Dirac).
- Giải thích vì sao toán tử Dirac giữ vai trò trung tâm trong **lý thuyết chỉ số** và hình học phổ.
- Tránh các cách hiểu sai: "spinor chỉ là một mũi tên nhỏ" hoặc "phương trình Dirac chỉ dùng cho hóa học của electron".

**Kiến thức nền.** Ma trận, vectơ phức; nên đọc trước bài [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/).

---

## 1. Spin không có gì bí ẩn

Nhóm các phép quay 3 chiều $$SO(3)$$ không đơn liên: nhóm cơ bản của nó là $$\mathbb{Z}/2\mathbb{Z}$$. Phủ kép đơn liên của nó là $$SU(2)\cong\mathrm{Spin}(3)$$ — về mặt tô pô chính là mặt cầu 3 chiều $$S^3$$, nơi mỗi cặp điểm đối cực $$+u$$ và $$-u$$ tương ứng với cùng một phép quay trong $$SO(3)$$. Các biểu diễn của $$SU(2)$$ không hạ xuống được thành biểu diễn thông thường của $$SO(3)$$ chính là các biểu diễn xạ ảnh của nhóm quay, và chúng ứng đúng với **spin bán nguyên** ($$1/2, 3/2, \dots$$).

Một phép tính $$2\times 2$$ cho thấy điều đó ngay lập tức: phép quay góc $$\theta$$ quanh trục $$z$$ trong $$SU(2)$$ được biểu diễn bằng ma trận

$$
U_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}.
$$

Thay $$\theta = 2\pi$$ ($$360^\circ$$), ta thu được $$U_z(2\pi) = -I$$ — cả vectơ spinor đổi dấu! Phải thay $$\theta = 4\pi$$ ($$720^\circ$$), ta mới thu lại $$U_z(4\pi) = +I$$.

**Cơ chế chính.** Biên độ lượng tử của hạt spin-$$1/2$$ biến đổi theo $$SU(2)$$, chứ không chỉ theo các ma trận quay $$3\times 3$$. Dấu trừ sau vòng quay $$360^\circ$$ không phải trò ký hiệu trên giấy: nó đã được đo trực tiếp từ thập niên 1970 bằng thí nghiệm giao thoa kế neutron (tách chùm neutron thành hai nhánh, cho một nhánh đi qua từ trường xoay đúng $$360^\circ$$ rồi cho giao thoa lại — kết quả là vân giao thoa đảo ngược hoàn toàn từ sáng thành tối!).

---

## 2. Đại số Clifford

Cho một không gian vectơ với dạng toàn phương (Euclid hoặc Minkowski), **đại số Clifford** là đại số kết hợp sinh bởi các vectơ với quy tắc phản giao hoán cốt lõi:

$$
vw+wv=2\langle v,w\rangle.
$$

Trong ký hiệu vật lý cho không–thời gian Minkowski 4 chiều, các phần tử sinh theo bốn trục tọa độ là bốn ma trận Dirac $$4\times 4$$ thỏa mãn

$$
\{\gamma^\mu,\gamma^\nu\} = \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2\eta^{\mu\nu}.
$$

### Khung giải thích: tự tay "lấy căn bậc hai" của toán tử Laplace 3 chiều (nên đọc chậm)

Làm sao một toán tử vi phân bậc nhất khi bình phương lên lại triệt tiêu sạch các đạo hàm hỗn hợp $$\partial_x\partial_y$$? Hãy tự tay kiểm tra trên $$\mathbb{R}^3$$ bằng ba **ma trận Pauli** $$2\times 2$$:

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

1. **Kiểm tra quy tắc Clifford $$\{\sigma_j, \sigma_k\} = 2\delta_{jk} I$$:**
   - Bình phương: $$\sigma_1^2 = \sigma_2^2 = \sigma_3^2 = I_2$$.
   - Phản giao hoán (thử cặp $$\sigma_1, \sigma_2$$):
     $$
     \sigma_1\sigma_2 + \sigma_2\sigma_1 = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} + \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}!
     $$
2. **Viết toán tử Dirac Euclid 3 chiều dưới dạng ma trận $$2\times 2$$:**
   $$
   D = \sigma_1\partial_x + \sigma_2\partial_y + \sigma_3\partial_z = \begin{pmatrix} \partial_z & \partial_x - i\partial_y \\ \partial_x + i\partial_y & -\partial_z \end{pmatrix}.
   $$
3. **Bình phương trực tiếp ma trận $$D$$:**
   $$
   D^2 = \begin{pmatrix} \partial_z & \partial_x - i\partial_y \\ \partial_x + i\partial_y & -\partial_z \end{pmatrix} \begin{pmatrix} \partial_z & \partial_x - i\partial_y \\ \partial_x + i\partial_y & -\partial_z \end{pmatrix} = \begin{pmatrix} \partial_z^2 + (\partial_x - i\partial_y)(\partial_x + i\partial_y) & \partial_z(\partial_x - i\partial_y) - (\partial_x - i\partial_y)\partial_z \\ (\partial_x + i\partial_y)\partial_z - \partial_z(\partial_x + i\partial_y) & (\partial_x + i\partial_y)(\partial_x - i\partial_y) + \partial_z^2 \end{pmatrix}.
   $$
4. **Rút gọn từng ô:** Hai ô ngoài đường chéo triệt tiêu bằng $$0$$ (vì đạo hàm riêng giao hoán), còn trên đường chéo chính $$(\partial_x - i\partial_y)(\partial_x + i\partial_y) = \partial_x^2 + \partial_y^2$$, nên:
   $$
   D^2 = \begin{pmatrix} \partial_x^2 + \partial_y^2 + \partial_z^2 & 0 \\ 0 & \partial_x^2 + \partial_y^2 + \partial_z^2 \end{pmatrix} = \Delta \cdot I_2!
   $$

Chỉ cần mở rộng từ 3 ma trận Pauli $$2\times 2$$ lên 4 ma trận Dirac $$4\times 4$$ (để thêm đạo hàm thời gian $$\partial_t$$ với dấu trừ của metric Minkowski), ta thu ngay phương trình Dirac 4 chiều!

Không gian **spinor** là một biểu diễn (module) tối tiểu trên đại số Clifford (trong không–thời gian 4 chiều, đó là $$\mathbb{C}^4$$ — spinor 4 thành phần, tự tách thành cặp 2 thành phần cho hạt và phản hạt, hoặc cho spin thuận tay trái và tay phải). Toán tử Dirac được dựng bằng cách kết hợp phép nhân Clifford với phép lấy đạo hàm (và thêm liên thông spin khi làm việc trên đa tạp cong hoặc khi có trường gauge).

---

## 3. Phương trình Dirac (tổng quan)

Phương trình Dirac tự do trên không–thời gian Minkowski có dạng gọn gàng đáng kinh ngạc:

$$
(i\gamma^\mu\partial_\mu-m)\psi=0.
$$

Bình phương toán tử bậc nhất này — bằng cách nhân thêm $$(-i\gamma^\nu\partial_\nu - m)$$ và dùng quy tắc đại số Clifford $$\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$$ — ta thu lại đúng phương trình bậc hai **Klein–Gordon** $$(\Box + m^2)\psi = 0$$ cho từng thành phần của $$\psi$$. Nói cách khác, phương trình Dirac vừa tôn trọng đúng hệ thức năng lượng–xung lượng tương đối tính $$E^2 = p^2 c^2 + m^2 c^4$$, vừa giữ được đạo hàm bậc nhất theo thời gian phù hợp với cấu trúc tiến hóa xác suất của cơ học lượng tử.

Thành quả lịch sử của 8 ký hiệu này thật khó tin: từ thuần túy yêu cầu đối xứng Lorentz và đại số Clifford, spin-$$1/2$$ và tỉ số từ hồi chuyển $$g=2$$ của electron *tự động rơi ra* mà không cần lắp ghép bằng tay; đồng thời nghiệm mang năng lượng âm dẫn Dirac tới dự đoán chấn động về **phản vật chất (positron)** — được Carl Anderson phát hiện trong tia vũ trụ chỉ bốn năm sau đó (1932)!

Để đưa tương tác điện từ vào, ta thay $$\partial_\mu$$ bằng đạo hàm hiệp biến $$D_\mu=\partial_\mu+iqA_\mu$$; đây chính là phép ghép tối thiểu của hình học gauge ([hình học gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)).

---

## 4. Hình học và lý thuyết chỉ số

Trên một đa tạp Riemann cong có cấu trúc spin, **toán tử Dirac** $$D$$ là toán tử vi phân elliptic bậc nhất điển hình nhất. Chỉ số giải tích của nó ($$\dim\ker D^+ - \dim\ker D^-$$) bằng đúng một tích phân tô pô gọi là **$$\hat{A}$$-genus** (định lý Atiyah–Singer). Chính nhờ điều này mà việc đếm số mode không (zero mode) của fermion trong nền trường cong hay nền instanton lại bị khóa cứng bởi tô pô ([instanton và dị thường]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/)). Thậm chí Lichnerowicz còn dùng công thức $$D^2 = \nabla^*\nabla + \frac{1}{4}R$$ để chứng minh một định lý hình học nổi tiếng: nếu một đa tạp spin đóng có $$\hat{A}\text{-genus} \neq 0$$, nó **không bao giờ** có thể mang một metric với độ cong vô hướng dương khắp nơi!

Trong hình học không giao hoán, $$D$$ được nâng lên thành thước đo khoảng cách cơ bản trong một bộ ba phổ ([hình học không giao hoán]({{ site.baseurl }}/contents/vi/chapter06/06_25_Noncommutative_Geometry_Map/)).

---

## 5. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Spinor chứng tỏ electron có phép màu." | Thổi phồng | Spinor là lý thuyết biểu diễn cộng với module trên đại số Clifford. |
| "Phương trình Dirac chính là Mô hình chuẩn." | Thiếu | Các fermion được mô tả bằng spinor Dirac (hoặc Weyl, Majorana); Mô hình chuẩn đầy đủ còn cần nhóm gauge, các thế hệ hạt và trường Higgs. |
| "Định lý chỉ số chỉ là toán thuần túy." | Thiếu | Nó giữ vai trò trung tâm trong việc hiểu dị thường và các mode không trong vật lý. |

---



## Trích từ danh sách video Thelanmath (toán cao cấp)


### Video Thelanmath: Phương Trình Dirac — 8 Ký Hiệu Đoán Trước Nửa Vũ Trụ (giải thích bằng toán lớp 9)

*Nguồn:* [Phương Trình Dirac — 8 Ký Hiệu Đoán Trước Nửa Vũ Trụ (giải thích bằng ](https://www.youtube.com/watch?v=eu90bfsM-0E) (khoảng 635 giây, tiếng Việt). Phần dưới đây được **viết lại** từ phụ đề, không chép nguyên văn. Với các khẳng định kỹ thuật, hãy đối chiếu với nguồn gốc.

**Ý chính.** Video mở đầu bằng việc phương trình Dirac được khắc lên sàn một nơi tưởng niệm. Tác giả của nó khi mới 25 tuổi, chỉ với giấy và bút, đã dự đoán sự tồn tại của phản vật chất, "một nửa vũ trụ" mà lúc đó chưa ai từng quan sát. Video cũng nhắc lại bối cảnh năm 1926: vật lý khi đó có hai lý thuyết lớn (cơ học lượng tử và thuyết tương đối hẹp), mỗi lý thuyết đúng trong phạm vi riêng của nó.

*Gói nghiên cứu:* `research/video-research/thelanmath/eu90bfsM-0E/`

<!-- THELANMATH_BATCH_EXTRACTS_END -->

## Tài liệu tham khảo

1. Lawson & Michelsohn, *Spin Geometry* (Hình học spin).  
2. Peskin & Schroeder, chương về phương trình Dirac.  
3. Các liên kết trong khóa học ở trên.  
