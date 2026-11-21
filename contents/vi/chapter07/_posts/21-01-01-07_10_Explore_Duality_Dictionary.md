---
layout: post
title: "Studio: Vẽ từ điển đối ngẫu"
chapter: '07'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Lộ trình: Nhánh đối ngẫu (bước thực hành)**  
> **1.** [Đối ngẫu như một nguyên lý]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)  
> **2.** Không bắt buộc, đọc sâu thêm: đối xứng gương, AdS/CFT, Langlands hình học  
> **3. Bạn đang ở đây:** bài thực hành chương 7, **lập một từ điển đối ngẫu**  
> *Thời lượng gợi ý:* khoảng 90–150 phút (đây không phải bài học chứng minh).

Đây là một **bài thực hành**, không phải danh sách định lý. Đối ngẫu xuất hiện dưới nhiều dạng khác nhau. Nhiệm vụ của bạn là: **chọn một cặp đối ngẫu**, lập một từ điển hai cột, ghi rõ dòng nào là **định lý** và dòng nào là **giả thuyết**, và giữ một nhật ký ngắn. Bạn không chứng minh AdS/CFT hay giả thuyết đối xứng gương đồng điều (HMS). Bạn tập trình bày các chương trình nghiên cứu đó sao cho người khác **đọc hiểu được**.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Chọn một cặp đối ngẫu trong khóa học và nêu rõ **cái gì được hoán đổi**.
- Lập một **từ điển hai cột** (ít nhất 6 dòng) gồm các đối tượng hoặc phát biểu tương ứng.
- Gắn nhãn cho mỗi khẳng định quan trọng: **định lý / chương trình nghiên cứu / giả thuyết / từ điển vật lý / phép so sánh**.
- Phân biệt **đối xứng của một lý thuyết** với **sự tương đương giữa hai lý thuyết**.
- Giữ một nhật ký có ít nhất một dòng từ điển bị sai hoặc phải sửa lại.

**Kiến thức cần có.** Bài [Đối ngẫu như một nguyên lý]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/). Các bài đọc sâu là không bắt buộc.

---

## 1. Kiến thức nền (một trang)

Một từ điển đối ngẫu là một bảng như sau:

| Phía A | Phía B | Nhãn trạng thái |
|--------|--------|-----------------|
| đối tượng / phát biểu | đối tượng tương ứng | định lý / … |

Các ví dụ đã gặp trong khóa học:

| Cặp | Cái được hoán đổi | Lưu ý về trạng thái |
|-----|--------------|----------------------|
| Không gian đối ngẫu $$V$$ / $$V^*$$ | vectơ ↔ phép đo tuyến tính | Định lý (đại số tuyến tính) |
| Fourier / Pontryagin | vị trí ↔ tần số / đặc trưng (character) | Định lý (nhóm abel compact địa phương) |
| Đối ngẫu Poincaré | bậc $$k$$ ↔ bậc $$n-k$$ | Định lý (với đa tạp thỏa điều kiện thích hợp) |
| Điện–từ | $$E\leftrightarrow B$$ | Đúng với phương trình Maxwell cổ điển; đối ngẫu S cho Yang–Mills: chương trình nghiên cứu |
| Đối xứng gương A / B | hình học symplectic ↔ hình học phức | HMS: chương trình nghiên cứu, một số trường hợp đã thành định lý |
| AdS / CFT | hấp dẫn trong khối ↔ lý thuyết trường lượng tử trên biên | Tương ứng đang nghiên cứu |
| Langlands $$G$$ / $$G^\vee$$ | tự đẳng cấu (automorphic) ↔ Galois / phổ | Chương trình rộng; nhiều kết quả bộ phận là định lý |

**Quy tắc của bài.** Nếu bạn chưa gắn được nhãn trạng thái cho một khẳng định, nghĩa là bạn chưa hiểu nó. Hãy đọc lại bài gốc, đừng tự gán mức độ chắc chắn.

---

## 2. Giả thuyết, chứng minh và từ điển

| Nhãn | Dùng khi |
|------|----------|
| **Định lý** | Đã được chứng minh dưới các giả thiết nêu rõ (trích bài trong khóa hoặc tên chuẩn của định lý) |
| **Chương trình / giả thuyết** | Còn mở, hoặc mới chứng minh được một phần |
| **Từ điển vật lý** | Được chấp nhận rộng rãi trong vật lý lý thuyết; trạng thái về mặt toán học có thể khác |
| **Phép so sánh** | Chỉ để dễ hình dung khi giảng dạy, không được coi là định lý |

Làm tốt bài này **không** có nghĩa là "chứng minh được kết quả Kapustin–Witten". Làm tốt nghĩa là sổ tay của bạn rõ ràng đến mức người khác kiểm tra lại được.

---

## 3. Nhiệm vụ

### A. Chọn cặp (15 phút)

Chọn **đúng một** cặp chính trong bảng ở mục 1 (có thể chọn một biến thể nếu bạn cẩn thận). Tránh nhầm loại: "RSA và bài toán phân tích thừa số" **không** phải là một cặp đối ngẫu.

Viết ba câu: (1) về phía A; (2) về phía B; (3) điều bạn **không** khẳng định.

### B. Lập từ điển (45–75 phút)

Bảng có **ít nhất 6 dòng**. Ít nhất hai dòng là **đối tượng**, ít nhất hai dòng là **câu hỏi hoặc phép tính** trở nên dễ hơn khi chuyển sang phía đối ngẫu.

Có thể vẽ tay. Nếu đề cương yêu cầu, chụp ảnh và đưa vào nhật ký.

### C. Kiểm tra trạng thái (20 phút)

Dòng nào cũng phải có nhãn. Đánh dấu dòng **kém chắc chắn nhất** và viết ra bằng chứng nào sẽ giúp nâng trạng thái của nó lên.

### D. Thí nghiệm nhỏ (nên làm, 20–40 phút)

Chọn **một** trong các việc sau:

1. **Đối ngẫu tuyến tính.** Với $$V=\mathbb{R}^2$$, tìm ánh xạ đối ngẫu của $$f(x,y)=(x+y,x)$$.  
2. **Fourier đơn giản.** DFT trên $$\mathbb{Z}/n\mathbb{Z}$$: tích chập ↔ tích từng điểm (phát biểu, không cần chứng minh đầy đủ).  
3. **Mô hình điện từ.** Phương trình Maxwell trong chân không và phép đối xứng $$E\leftrightarrow B$$ (lập luận trực quan).  
4. **Phân biệt hai loại Langlands.** Lập hai cột: Langlands số học và Langlands hình học (chỉ liệt kê đối tượng), trích từ chương 2 và bài đọc sâu về Langlands hình học.

### E. Nhật ký (ít nhất 5 mục có ghi ngày)

Mỗi mục gồm: dự định → việc đã làm → kết quả → nhãn → bước tiếp theo. Phải có ít nhất một lần **sửa** (xóa hoặc viết lại một dòng).

---

## 4. Danh sách cần nộp

| Hạng mục | Bắt buộc |
|----------|----------|
| Cặp đối ngẫu và ba câu nêu phạm vi | Có |
| Từ điển ít nhất 6 dòng, có nhãn | Có |
| Nhật ký ít nhất 5 mục, có một lần sai hoặc sửa | Có |
| Một đoạn giải thích: "đối xứng khác với tương đương giữa hai lý thuyết" | Có |
| Thí nghiệm ở nhiệm vụ D | Rất nên làm |
| Một câu "tôi **không** chứng minh …" | Có |

**Không phải mục tiêu:** chứng minh một phép đối ngẫu lớn cỡ giả thuyết Riemann, "giải" AdS/CFT, hay khẳng định "vật lý đã chứng minh Langlands".

---

## 5. Liên kết trong khóa học

| Tài liệu | Vai trò |
|------------|---------|
| [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/) | Bài tổng quan |
| [Đối ngẫu Pontryagin / Fourier]({{ site.baseurl }}/contents/vi/chapter06/06_16_Pontryagin_Fourier_Duality/) | Cầu nối ở trình độ đại học |
| [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) | Đọc sâu |
| [AdS/CFT]({{ site.baseurl }}/contents/vi/chapter06/06_14_AdS_CFT/) | Đọc sâu |
| [Langlands hình học]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) | Đọc sâu |
| [Witten: từ vật lý đến toán]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/) | Cách vật lý gợi ý cho toán |

---

## Bài tập cuối buổi

1. Viết một câu: cặp đối ngẫu của bạn **hoán đổi** cái gì?  
2. Chỉ ra một dòng là **định lý** và một dòng chỉ là **chương trình nghiên cứu**.  
3. Tìm một khẳng định phổ biến nhầm lẫn giữa đối xứng và đối ngẫu.  
4. **Không quá 100 chữ:** vì sao việc gắn nhãn trạng thái giúp tránh nói quá?

---

## Tài liệu

1. Nhánh đối ngẫu, chương 6, các bài 12–17.  
2. nLab, mục duality (để định hướng).  
3. Nhật ký của bạn là sản phẩm chính.

## Video tham khảo

- **Xem trước:** [Prof. Edward Witten | Duality, the Langlands Correspondence, and the Influence of Michael Atiyah](https://www.youtube.com/watch?v=fqHGe3acpC0) (INI Seminar Room 1, tiếng Anh). Witten nói về đối ngẫu và tương ứng Langlands, cùng ảnh hưởng của Atiyah. Xem trước khi chọn cặp đối ngẫu để có cái nhìn tổng quan.
- [AdS/CFT Correspondence, Part 1 - Juan Maldacena](https://www.youtube.com/watch?v=sYqtGXN59uE) (Institute for Advanced Study, tiếng Anh). Bài giảng của người đề xuất tương ứng AdS/CFT. Nên xem sau khi đã nắm ý chính, nhất là nếu bạn chọn cặp AdS/CFT.
- [Lecture 1: Geometric Langlands and S-duality in N = 4 SYM by Sergei Gukov](https://www.youtube.com/watch?v=bCpVL6flCxo) (International Centre for Theoretical Sciences, tiếng Anh). Bài giảng về mối liên hệ giữa Langlands hình học và đối ngẫu S. Xem thêm sau hai video trên nếu bạn chọn cặp Langlands.
