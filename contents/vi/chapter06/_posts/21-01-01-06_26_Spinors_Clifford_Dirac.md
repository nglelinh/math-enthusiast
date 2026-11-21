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

Quay một vectơ $$360^\circ$$ thì nó trở về đúng như cũ. Nhưng quay một **spinor** (đối tượng toán học mô tả hạt có spin-$$1/2$$) $$360^\circ$$ thì nó bị nhân với $$-1$$; phải quay $$720^\circ$$ mới trở về trạng thái ban đầu. Hiện tượng phủ kép này được mô tả bằng **nhóm Spin**, **đại số Clifford** và **toán tử Dirac**. Dirac đưa ra toán tử này năm 1928 để có một phương trình sóng tương đối tính bậc nhất mà khi bình phương lên thì cho lại phương trình Klein–Gordon.

Bài tổng quan này nối lý thuyết biểu diễn, hình học, và loại toán tử elliptic được ưa chuộng nhất trong định lý chỉ số. Mục tiêu là hiểu cơ chế chính và thấy được cầu nối giữa vật lý và toán. Nên đọc kèm các bài [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/), [không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [định lý chỉ số Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/).

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

Nhóm $$SO(3)$$ có nhóm cơ bản là $$\mathbb{Z}/2\mathbb{Z}$$. Phủ kép đơn liên của nó là $$SU(2)\cong\mathrm{Spin}(3)$$. Các biểu diễn của $$SU(2)$$ không đi qua được $$SO(3)$$ chính là các biểu diễn xạ ảnh của nhóm quay, và chúng ứng đúng với spin bán nguyên.

**Cơ chế chính.** Biên độ lượng tử của hạt spin-$$1/2$$ biến đổi theo $$SU(2)$$, chứ không chỉ theo các ma trận quay $$3\times 3$$. Vì vậy một vòng quay $$360^\circ$$ có thể cho dấu trừ. Dấu trừ này quan sát được trong các thí nghiệm giao thoa, chẳng hạn thí nghiệm với neutron.

---

## 2. Đại số Clifford

Cho một dạng toàn phương (Euclid hoặc Minkowski), **đại số Clifford** là đại số sinh bởi các vectơ với quan hệ

$$
vw+wv=2\langle v,w\rangle.
$$

Trong ký hiệu vật lý, các ma trận Dirac thỏa

$$
\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}.
$$

Không gian spinor là một module trên đại số Clifford. Toán tử Dirac được dựng bằng cách kết hợp phép nhân Clifford với đạo hàm (và thêm liên thông khi làm việc trên đa tạp hoặc khi có trường gauge).

---

## 3. Phương trình Dirac (tổng quan)

Phương trình Dirac tự do trên không–thời gian Minkowski:

$$
(i\gamma^\mu\partial_\mu-m)\psi=0.
$$

Bình phương toán tử này (làm cẩn thận) cho phương trình bậc hai kiểu Klein–Gordon cho từng thành phần, tức là đúng hệ thức năng lượng–xung lượng tương đối tính, trong khi vẫn giữ được cấu trúc Hamilton bậc nhất phù hợp với cách diễn giải lượng tử. Thành quả lịch sử gồm việc giải thích spin-$$1/2$$ và dự đoán phản vật chất (positron).

Để đưa tương tác điện từ vào, ta thay $$\partial_\mu$$ bằng $$D_\mu=\partial_\mu+iqA_\mu$$; đây chính là đạo hàm hiệp biến gauge ([hình học gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)).

---

## 4. Hình học và lý thuyết chỉ số

Trên một đa tạp spin, **toán tử Dirac** $$D$$ là toán tử elliptic (dưới các điều kiện chuẩn). Chỉ số giải tích của nó bằng một biểu thức tô pô gọi là Â-genus (định lý Atiyah–Singer). Đây là lý do sâu xa khiến số các mode không (zero mode) được đếm bằng tô pô ([instanton và dị thường]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/)).

Trong hình học không giao hoán, $$D$$ được nâng lên thành dữ liệu hình học cơ bản trong một bộ ba phổ ([hình học không giao hoán]({{ site.baseurl }}/contents/vi/chapter06/06_25_Noncommutative_Geometry_Map/)).

---

## 5. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Spinor chứng tỏ electron có phép màu." | Thổi phồng | Spinor là lý thuyết biểu diễn cộng với module trên đại số Clifford. |
| "Phương trình Dirac chính là Mô hình chuẩn." | Thiếu | Các fermion được mô tả bằng spinor Dirac (hoặc Weyl, Majorana); Mô hình chuẩn đầy đủ còn cần nhóm gauge, các thế hệ hạt và trường Higgs. |
| "Định lý chỉ số chỉ là toán thuần túy." | Thiếu | Nó giữ vai trò trung tâm trong việc hiểu dị thường và các mode không trong vật lý. |

---

## Bài tập

1. **Phủ kép.** Vì sao phép quay $$360^\circ$$ không phải lúc nào cũng là phép đồng nhất trên spinor?  
2. **Đại số Clifford.** Viết quan hệ phản giao hoán của các $$\gamma^\mu$$.  
3. **Gauge.** Phép ghép tối thiểu (minimal coupling) xuất hiện trong phương trình Dirac như thế nào?  
4. **Cầu nối.** Viết một đoạn: phương trình Dirac như cầu nối từ spin của hạt đến định lý Atiyah–Singer.  
5. **Nói chính xác.** Viết lại câu: "Spin chứng minh cơ học lượng tử tự mâu thuẫn."

---



<!-- THELANMATH_BATCH_EXTRACTS -->
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
