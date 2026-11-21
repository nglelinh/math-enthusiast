---
layout: post
title: "Khi vật lý viết lại topology: Donaldson đến Seiberg–Witten"
chapter: '06'
order: 23
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Đầu thập niên 1980, Simon Donaldson dùng không gian moduli của các **liên thông Yang–Mills phản tự đối ngẫu**, vốn là đối tượng xuất phát từ vật lý hạt, để chứng minh những định lý về **đa tạp trơn 4 chiều** mà tô pô thuần túy trước đó chưa lường trước được. Khoảng mười năm sau, lý thuyết Seiberg–Witten, lấy cảm hứng từ lý thuyết trường lượng tử siêu đối xứng, cung cấp một công cụ đối ngẫu với phần giải tích dễ xử lý hơn, và làm thay đổi cách làm việc hằng ngày trong tô pô 4 chiều.

Đây là một trục trong nhánh Cầu nối Vật lý–Toán: **hình học lấy cảm hứng từ vật lý đóng góp cho toán học thuần túy**, chứ không chỉ theo chiều ngược lại. Nên đọc sau các bài [lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/) và [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/); đọc kèm bài [instanton]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu bước đi then chốt của Donaldson: **không gian moduli gauge → bất biến trơn của đa tạp 4 chiều**.
- Giải thích vì sao phần giải tích (tính compact, hiện tượng nổi bọt) là không thể thiếu, chứ không phải "gia vị vật lý" có cũng được không có cũng được.
- So sánh, ở mức ý tưởng, bài toán phân loại theo đồng phôi và theo **vi phôi** trong 4 chiều.
- Mô tả phương trình Seiberg–Witten như một công cụ gauge đối ngẫu ra đời sau, có lợi thế về mặt thực hành.
- Đặt cách diễn giải TQFT của Witten vào vai trò cầu nối giữa tích phân đường và bất biến.
- Tránh các nhầm lẫn kiểu "thí nghiệm QCD chứng minh định lý Donaldson", hoặc nhầm theo chiều ngược lại.

**Kiến thức nền.** Ý chính về độ cong gauge; chấp nhận "không gian moduli = không gian nghiệm chia cho đối xứng". Không cần giáo trình về đa tạp 4 chiều.

---

## 1. Bốn chiều rất đặc biệt

Ở số chiều $$\geq 5$$, lý thuyết phẫu thuật (surgery) giúp tổ chức phần lớn tô pô. Ở 3 chiều có định lý hình học hóa (Perelman). Còn 4 chiều nằm ở giữa và rất khó: có những **cấu trúc trơn kỳ lạ** (exotic) trên các đa tạp tô pô 4 chiều; các công cụ dùng được ở chiều khác lại không dùng được ở đây. Cũng khoảng cách giữa trơn và tô pô này làm cho câu hỏi **một nút có là nút lát (slice) hay không** trở nên tinh tế: một nút có thể bao được một đĩa tô pô trong $$B^4$$ nhưng không bao được đĩa trơn nào. Xem bài [Piccirillo và nút Conway]({{ site.baseurl }}/contents/vi/chapter06/06_28_Piccirillo_Conway_Knot/).

Ý tưởng của Donaldson không phải là tạo ra tô pô trơn từ hư không, mà là dùng **không gian moduli giải tích của các liên thông** làm một công cụ dò, nhạy với cấu trúc trơn.

---

## 2. Không gian moduli instanton như một chiếc kính hiển vi

Cố định một phân thớ chính trên đa tạp trơn định hướng 4 chiều $$X$$, và xét các liên thông phản tự đối ngẫu (ASD):

$$
F_A^+ = 0
$$

(các nghiệm, sau khi chia cho phép biến đổi gauge, tạo thành không gian moduli $$\mathcal{M}$$). Dưới các giả thiết thích hợp, $$\mathcal{M}$$ là một đa tạp hữu hạn chiều (có những điểm kỳ dị cần kiểm soát), với số chiều được dự đoán bằng phép tính chỉ số.

**Định lý compact của Uhlenbeck** bảo đảm một dãy liên thông ASD có giới hạn được kiểm soát: instanton có thể "nổi bọt" (bubble) tại một điểm ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)).

Từ các không gian moduli này, Donaldson trích ra các **bất biến đa thức**, giúp phân biệt những cấu trúc trơn mà tô pô đại số cổ điển (đồng điều, đồng luân) không thấy được.

**Cơ chế chính.** Cấu trúc trơn → phương trình đạo hàm riêng elliptic của lý thuyết gauge → hình học của không gian moduli → bất biến → định lý về vật cản hoặc về sự phân biệt.

---

## 3. "Vật lý viết lại tô pô" nên hiểu cẩn thận thế nào

| Phía vật lý | Phía toán học |
|-------------|-----------|
| Yang–Mills, instanton | Phương trình ASD, năng lượng Chern–Weil |
| Quỹ đạo gauge | Thương theo nhóm gauge |
| Lập luận tích phân đường / TQFT (ra đời sau) | Lý thuyết giao trên không gian moduli, chặt chẽ (phần giải tích khó) |
| Đối ngẫu siêu đối xứng (thập niên 1990) | Phiên bản đơn giản hơn của Seiberg–Witten |

Các định lý là toán học. **Cảm hứng và việc chọn phương trình** đến từ lý thuyết gauge. Năm 1988, Witten diễn giải TQFT, giải thích về mặt hình thức các đa thức Donaldson qua tích phân đường. Cách diễn giải này gợi ý những phép đối ngẫu mới, nhưng không thay thế được phần giải tích, cho đến khi Seiberg–Witten đưa ra một hệ phương trình đạo hàm riêng cổ điển dễ xử lý hơn.

---

## 4. Seiberg–Witten (1994): công cụ đối ngẫu

Nghiên cứu của Seiberg và Witten về lý thuyết Yang–Mills $$N=2$$ gợi ý một mô tả đối ngẫu ở vùng tương tác yếu, liên quan đến các đơn cực từ (monopole). Witten dịch điều này thành **phương trình Seiberg–Witten** cho một liên thông spin$$^c$$ và một spinor trên đa tạp 4 chiều.

Lợi thế (ở mức tổng quan): tính compact tốt hơn (ít rắc rối với hiện tượng nổi bọt); bất biến thường dễ tính hơn; nhiều kết luận của Donaldson được chứng minh lại hoặc làm gọn hơn.

Đây là một khuôn mẫu tiêu biểu của nhánh Cầu nối: **đối ngẫu trong lý thuyết trường lượng tử → phương trình đạo hàm riêng cổ điển → tô pô**.

---

## 5. Liên hệ với phần còn lại của khóa học

- Hình học của liên thông: [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)  
- Tô pô phi nhiễu loạn trong lý thuyết trường lượng tử: [Instanton và dị thường]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/)  
- Nền tảng giải tích: [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)  
- Số chiều của không gian moduli: [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/)  
- Đối ngẫu: [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)  
- Sự tồn tại của lý thuyết lượng tử, vấn đề còn mở: [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/). Lưu ý: Donaldson dùng phương trình ASD **cổ điển**; công trình của ông **không** giải bài toán Clay về Yang–Mills lượng tử.  
- Tương đương lát (concordance) và tính lát trơn trong 4 chiều: [Piccirillo và nút Conway]({{ site.baseurl }}/contents/vi/chapter06/06_28_Piccirillo_Conway_Knot/)

---

## 6. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Máy gia tốc hạt đã chứng minh có đa tạp 4 chiều kỳ lạ." | Sai | Định lý là toán học; vật lý chỉ cung cấp phương trình và trực giác. |
| "Bất biến Donaldson là một quan sát thực nghiệm." | Nhầm loại | Đó là bất biến của tô pô trơn. |
| "TQFT giải thích được các bất biến nên không cần giải tích nữa." | Sai | Định nghĩa chặt chẽ vẫn cần phương trình đạo hàm riêng và không gian moduli (hoặc một cách tương đương). |

---

## Bài tập

1. **Bước then chốt.** Trong không quá 60 chữ: không gian các liên thông phát hiện cấu trúc trơn như thế nào?  
2. **ASD.** Điều kiện $$F_A^+=0$$ đòi hỏi gì ở độ cong?  
3. **Seiberg–Witten và Donaldson.** Nêu một lợi thế thực hành của Seiberg–Witten.  
4. **Nói chính xác.** Viết lại câu: "Vật lý đã phát hiện ra rằng tô pô bốn chiều bị sai."  
5. **Giải thích nguyên lý.** Phác thảo trong 5 câu: phương trình → không gian moduli → bất biến → định lý về đa tạp.

---

## Tài liệu tham khảo

1. Donaldson & Kronheimer, *The Geometry of Four-Manifolds* (Hình học của đa tạp bốn chiều).  
2. Witten, bài về TQFT (1988); bài "Monopoles and four-manifolds" (Đơn cực và đa tạp bốn chiều, 1994).  
3. Các liên kết trong khóa học ở trên.  
