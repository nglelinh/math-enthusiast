---
layout: post
title: "Hình học không giao hoán trong một giờ seminar"
chapter: '06'
order: 25
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Một không gian cổ điển có thể được dựng lại hoàn toàn từ đại số các hàm (giao hoán) trên nó; đó là nội dung định lý Gelfand. Trong khi đó, cơ học lượng tử gợi ý những "tọa độ" không giao hoán với nhau. **Hình học không giao hoán (NCG)**, đặc biệt theo cách trình bày của Alain Connes, coi một đại số không giao hoán như là đại diện cho một "không gian", và dựng lại hình học metric từ **dữ liệu phổ**: một không gian Hilbert, một đại số toán tử, và một toán tử kiểu Dirac.

Bài này là một bản đồ tổng quan, giúp bạn định vị NCG trong nhánh Cầu nối Vật lý–Toán mà không cần học hết cả một môn: bạn sẽ nắm cơ chế chính và học cách nói chính xác, tránh thổi phồng. Liên kết: [đại số toán tử]({{ site.baseurl }}/contents/vi/chapter06/06_24_Operator_Algebras_QM/), [spinor và toán tử Dirac]({{ site.baseurl }}/contents/vi/chapter06/06_26_Spinors_Clifford_Dirac/), [định lý chỉ số Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/), [nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của định lý Gelfand: C*-đại số giao hoán ↔ không gian (Hausdorff compact địa phương).
- Giải thích ý tưởng cốt lõi của NCG: **coi một đại số không giao hoán như một không gian suy rộng**.
- Kể tên các thành phần của một **bộ ba phổ** (spectral triple) $$(A,\mathcal{H},D)$$ ở mức ý tưởng.
- Nêu một động lực từ vật lý (tính không giao hoán trong cơ học lượng tử; tác dụng phổ cho Mô hình chuẩn, đây là một chương trình nghiên cứu, không phải định lý về tự nhiên).
- Phân biệt việc biết đọc công trình Connes–Kreimer về đại số Hopf trong tái chuẩn hóa với khẳng định sai "NCG đã giải quyết xong lý thuyết trường lượng tử".

**Kiến thức nền.** Phép nhân ma trận không giao hoán; bài [đại số toán tử]({{ site.baseurl }}/contents/vi/chapter06/06_24_Operator_Algebras_QM/) sẽ giúp ích.

---

## 1. Phép đối ngẫu mở đầu cho NCG

Định lý Gelfand–Naimark: mọi C*-đại số giao hoán đều đẳng cấu với đại số các hàm liên tục triệt tiêu tại vô cực trên phổ của nó. Như vậy, tô pô của không gian được mã hóa hoàn toàn trong đại số. Khi $$AB\neq BA$$, không còn một không gian điểm cổ điển nào có đại số hàm như vậy, nhưng ta vẫn có thể làm "hình học" bằng các bất biến đại số và phổ.

**Cơ chế chính.** Thay vì bắt đầu từ các điểm, ta bắt đầu từ đại số và phổ của nó.

---

## 2. Bộ ba phổ (ý tưởng về metric)

Một **bộ ba phổ** (trường hợp không bị chặn) gồm, nói đại khái:

- một *-đại số $$A$$ biểu diễn trên một không gian Hilbert $$\mathcal{H}$$,  
- một toán tử tự liên hợp $$D$$ (kiểu Dirac) có giải thức compact, dưới các giả thiết thích hợp,  
- các điều kiện tương thích (giao hoán tử $$[D,a]$$ bị chặn, v.v.).

Trong trường hợp giao hoán, có một công thức khoảng cách cho phép dựng lại metric từ $$D$$. Phép ghép cặp chỉ số cho lại thông tin về K-đồng điều, cùng tinh thần với định lý Atiyah–Singer.

---

## 3. Liên hệ với vật lý (có ghi trạng thái)

| Lĩnh vực | Ý chính | Trạng thái |
|-----------|--------|-----------------|
| Cơ học lượng tử | Vị trí và động lượng không giao hoán | Định luật vật lý, có khung toán học đầy đủ |
| Xuyến không giao hoán / mặt phẳng Moyal | Tọa độ bị biến dạng | Mô hình toán học; một số được dùng trong vật lý |
| Tác dụng phổ / hình học gần giao hoán | Các boson của Mô hình chuẩn xuất hiện từ dao động bên trong của $$D$$ | Chương trình nghiên cứu; không phải "lý thuyết của vạn vật" duy nhất |
| Connes–Kreimer | Đại số Hopf sắp xếp quá trình tái chuẩn hóa các giản đồ Feynman | Một từ điển quan trọng giữa toán và lý thuyết trường lượng tử |
| Hy vọng về hấp dẫn lượng tử | Không–thời gian xuất hiện từ dữ liệu phổ | Suy đoán, đang nghiên cứu |

---

## 4. Đọc tiếp trong khóa học

- Nền tảng đại số: [Đại số toán tử]({{ site.baseurl }}/contents/vi/chapter06/06_24_Operator_Algebras_QM/)  
- Nguồn gốc toán tử Dirac: [Spinor]({{ site.baseurl }}/contents/vi/chapter06/06_26_Spinors_Clifford_Dirac/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/)  
- Thang đo: [Nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/)  
- Hình học gauge cổ điển: [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)

---

## 5. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "NCG chứng minh Mô hình chuẩn." | Thổi phồng | Có một mô hình hình học; việc nó là duy nhất phù hợp với thực nghiệm không phải là định lý. |
| "Không giao hoán thì chỉ là lý thuyết dây." | Quá hẹp | NCG là một chương trình toán học độc lập, có nhiều điểm tiếp xúc với vật lý. |
| "Tọa độ không giao hoán nhưng các điểm vẫn như cũ." | Thường sai | Khái niệm điểm có thể mất đi; phổ và trạng thái thay thế vai trò của điểm. |

---

## Bài tập

1. **Định lý Gelfand.** C*-đại số giao hoán ↔ ?  
2. **Bộ ba phổ.** Nêu vai trò của $$A$$, $$\mathcal{H}$$, $$D$$, mỗi thứ một dòng.  
3. **Nói chính xác.** Viết lại câu: "Connes đã hình học hóa vật lý hạt nên mọi thứ ở LHC đều thuần túy là NCG."  
4. **Cầu nối.** Một liên thông gauge trên một phân thớ khác với việc dùng đại số không giao hoán thay cho không gian nền như thế nào? (Trả lời ở mức ý tưởng là được.)

---

## Tài liệu tham khảo

1. Connes, *Noncommutative Geometry* (Hình học không giao hoán).  
2. van Suijlekom, *Noncommutative Geometry and Particle Physics* (Hình học không giao hoán và vật lý hạt).  
3. Các liên kết trong khóa học ở trên.  
