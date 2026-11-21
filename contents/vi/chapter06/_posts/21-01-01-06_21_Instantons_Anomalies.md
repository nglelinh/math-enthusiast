---
layout: post
title: "Instanton, topology và anomaly"
chapter: '06'
order: 21
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Có những hiệu ứng lượng tử không xuất hiện ở bất kỳ bậc hữu hạn nào của khai triển giản đồ Feynman, nhưng lại được **tô pô** kiểm soát: số instanton, số vòng quấn (winding number) của một ánh xạ, chỉ số của toán tử Dirac. Một số hiệu ứng khác là **dị thường** (anomaly): một đối xứng cổ điển không còn được bảo toàn khi lượng tử hóa, và thường được tính bằng chính phép đếm chỉ số mà toán học thuần túy rất coi trọng.

Bài trong nhánh Cầu nối này gom ba bài [hình học gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/), [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), và [định lý chỉ số Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) thành một bản đồ chung, ở mức ý tưởng, không phải giáo trình lý thuyết trường lượng tử đầy đủ.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa **instanton** ở mức ý tưởng: một trường gauge cổ điển có tác dụng hữu hạn và có số tô pô khác không.
- Giải thích vì sao số tô pô $$k\propto\int\operatorname{tr}(F\wedge F)$$ không đổi khi biến dạng liên tục (trong cùng một lớp).
- Nêu **dị thường lượng tử** là gì: một đối xứng cổ điển bị phá vỡ ở mức lượng tử.
- Liên hệ **dị thường chiral** và việc đếm mode không với **chỉ số** của toán tử Dirac.
- Đọc hiểu được các thảo luận về bài toán $$U(1)$$ và chân không $$\theta$$ (không cần học đầy đủ QCD).
- Phân biệt các sự kiện hình học đã chặt chẽ (chỉ số, số Chern) với các kết luận vật lý dựa trên khung lý thuyết trường lượng tử.

**Kiến thức nền.** Bài [lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/); khái niệm "số chiều của hạt nhân" trong đại số tuyến tính. Nên đọc thêm bài Atiyah–Singer.

---

## 1. Instanton: điểm yên ngựa mang tính tô pô

Trên không gian Euclid bốn chiều (hoặc trên đa tạp 4 chiều đóng), mỗi liên thông Yang–Mills có tác dụng hữu hạn thuộc về một lớp tô pô, đặc trưng bởi một số nguyên

$$
k = \frac{1}{8\pi^2}\int \operatorname{tr}(F\wedge F)
$$

(tùy cách chuẩn hóa). Các liên thông tự đối ngẫu, tức là đạt đúng chặn dưới tô pô của tác dụng, được gọi là **instanton**.

**Trong vật lý.** Trong tích phân đường Euclid, instanton là các điểm yên ngựa phi nhiễu loạn, đóng góp một thừa số dạng $$e^{-8\pi^2/g^2}$$. Chúng mô tả hiệu ứng đường hầm giữa các chân không cổ điển và sinh ra các hiện tượng vật lý phụ thuộc vào tham số $$\theta$$.

**Trong toán học.** Không gian moduli các instanton là một đối tượng hình học. Việc nghiên cứu nó cần các kết quả compact kiểu Uhlenbeck ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)) và là nền tảng cho lý thuyết Donaldson ([Donaldson–Seiberg–Witten]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/)).

---

## 2. Vì sao tô pô không thấy được ở từng bậc

Lý thuyết nhiễu loạn khai triển quanh một chân không theo lũy thừa của hằng số tương tác. Việc chuyển giữa các lớp tô pô và nhiều hiệu ứng toàn cục khác là **phi nhiễu loạn**: chúng nằm trong các thừa số dạng $$e^{-c/g^2}$$.

**Cơ chế chính.** Tô pô chia không gian các cấu hình trường thành các thành phần liên thông (các lớp). Biên độ lượng tử có thể là tổng trên các lớp này, với những trọng số mà chuỗi lũy thừa quanh một điểm không thể thấy được.

---

## 3. Dị thường: khi đối xứng cổ điển bị phá vỡ ở mức lượng tử

**Một đối xứng của tác dụng cổ điển** không nhất thiết còn tồn tại sau khi lượng tử hóa. Dị thường gauge làm lý thuyết mất tính nhất quán; còn dị thường toàn cục và dị thường chiral có thể là hiện tượng vật lý thật và đo được.

Ví dụ nổi tiếng: **dị thường chiral (ABJ)**. Dòng axial không còn bảo toàn ở mức lượng tử, dù Lagrangian cổ điển trông có đối xứng axial. Giản đồ tam giác trong lý thuyết nhiễu loạn phát hiện ra hiện tượng này; hình học hiện đại hiểu cùng một vật cản đó qua các lớp đặc trưng.

**Liên hệ với chỉ số.** Với toán tử Dirac $$D_A$$ ghép với trường gauge nền $$A$$, chỉ số giải tích

$$
\operatorname{ind} D_A = \dim\ker D_A - \dim\ker D_A^\dagger
$$

bằng chỉ số tô pô (định lý Atiyah–Singer). Trong ngôn ngữ vật lý: sự chênh lệch giữa số mode không thuận tay trái và tay phải gắn với hệ số dị thường và với các quy tắc chọn cho hàm tương quan trong nền instanton (đỉnh 't Hooft).

Bài học rút ra:

> **Đếm mode không không phải là chuyện tình cờ, mà là lý thuyết chỉ số gặp lý thuyết trường lượng tử.**

---

## 4. Bài toán $$U(1)$$ và instanton (mức đọc hiểu)

Nếu chỉ dựa vào đối xứng chiral một cách ngây thơ, QCD sẽ dự đoán một hạt nhẹ thứ chín giống boson Goldstone, nhưng thực tế không quan sát thấy. Một phần lời giải liên quan đến bản chất dị thường của đối xứng $$U(1)$$ axial đơn tuyến và cấu trúc tô pô của chân không gauge. Bài giảng "The uses of instantons" (Các ứng dụng của instanton) của Coleman là tài liệu vật lý kinh điển về chủ đề này; còn nền tảng toán học của việc đếm mode không là lý thuyết chỉ số.

**Cần thận trọng.** Những câu như "instanton giải thích khối lượng proton" là nói quá; câu chuyện có nhiều tầng (giam hãm, phá vỡ đối xứng chiral, tính toán trên mạng lưới, lý thuyết trường hiệu dụng).

---

## 5. Định lý và khung lý thuyết

| Loại | Ví dụ | Trạng thái |
|------|-------|------------|
| Tô pô của phân thớ | Số Chern là số nguyên | Định lý (hình học) |
| Định lý chỉ số | $$\operatorname{ind} D=$$ tích phân của một mật độ tô pô | Định lý |
| Công thức số chiều của moduli instanton | Phép dựng ADHM, tính chỉ số | Định lý của lý thuyết gauge cổ điển |
| Trọng số $$e^{-S_E}$$ trong tích phân đường | Phép tính phi nhiễu loạn trong vật lý | Chuẩn mực vật lý; độ đo đầy đủ có thể còn mở |
| Kết luận hiện tượng luận về QCD | Khối lượng, phân rã | Chương trình vật lý kết hợp mạng lưới và lý thuyết hiệu dụng |

---

## 6. Liên kết trong khóa học

- Hình học của $$F$$ và $$k$$: [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)  
- Điểm yên ngựa của tích phân đường: [Tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/)  
- Chỉ số: [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/)  
- Giải tích trên không gian moduli: [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)  
- Tô pô được viết lại: [Donaldson–Seiberg–Witten]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/)  
- Sự tồn tại của lý thuyết lượng tử, vấn đề mở: [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/)

---

## Bài tập

1. **Instanton.** Trong không quá 50 chữ: tác dụng hữu hạn và số tô pô.  
2. **Dị thường.** Phân biệt đối xứng của phương trình chuyển động với đối xứng của lý thuyết lượng tử.  
3. **Chỉ số.** Nếu $$\dim\ker D=2$$ và $$\dim\ker D^\dagger=0$$ thì $$\operatorname{ind} D$$ bằng bao nhiêu?  
4. **Nói chính xác.** Viết lại một câu thổi phồng, gán toàn bộ QCD cho "phép màu instanton".  
5. **Giải thích nguyên lý.** Trong không quá 150 chữ: trình bày *ý tưởng* vì sao chỉ số giải tích bằng chỉ số tô pô (không cần chứng minh).

---

## Tài liệu tham khảo

1. Coleman, "The uses of instantons" (Các ứng dụng của instanton).  
2. Nakahara, sách tô pô cho nhà vật lý (*Geometry, Topology and Physics*).  
3. Các liên kết trong khóa học ở trên.  
