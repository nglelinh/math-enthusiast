---
layout: post
title: "Cơ học thống kê và xác suất"
chapter: '06'
order: 27
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Các định luật vĩ mô như áp suất, độ từ hóa, giản đồ pha đều xuất hiện từ một số lượng khổng lồ các bậc tự do vi mô. **Cơ học thống kê cân bằng** diễn đạt quá trình này bằng xác suất: độ đo Gibbs, hàm phân hoạch, giới hạn nhiệt động. Cũng chính cấu trúc này là nền tảng cho nhiều phần của lý thuyết xác suất (độ lệch lớn, quá trình điểm Gibbs) và, thông qua tích phân đường Euclid, cho cả lý thuyết trường lượng tử.

Bài tổng quan này đi sâu vào mục 4 của [bài trung tâm về vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), đồng thời liên hệ với bài [nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/) và bài [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/). Mục tiêu là nắm cơ chế chính và học cách nói chính xác.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết hàm phân hoạch $$Z=\sum_s e^{-\beta E(s)}$$ và giải thích ý nghĩa của $$\beta=1/(kT)$$.
- Giải thích khái niệm **giới hạn nhiệt động**: cho $$N\to\infty$$ với mật độ cố định; chuyển pha thể hiện thành điểm kỳ dị của năng lượng tự do.
- Liên hệ các mô hình kiểu Ising với **chuyển pha**, tính phổ quát và điểm bất động của nhóm tái chuẩn hóa.
- Nêu **độ đo Gibbs** mô tả điều gì (một phân bố xác suất trên các cấu hình, có trọng số theo năng lượng).
- Phân biệt cơ học thống kê cân bằng với các vấn đề còn mở về hệ không cân bằng và chảy rối.
- Tránh cách hiểu sai: "chuyển pha là khi đồ thị mô phỏng trông có bước nhảy".

**Kiến thức nền.** Xác suất cơ bản (kỳ vọng, tính độc lập); hàm mũ. Bài [Xác suất và khoa học dữ liệu]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) sẽ giúp ích.

---

## 1. Từ vi mô đến vĩ mô trong một công thức

Xét một hệ có hữu hạn cấu hình $$s$$, mỗi cấu hình có năng lượng $$E(s)$$:

$$
Z(\beta)=\sum_s e^{-\beta E(s)},\qquad
\langle O\rangle=\frac{1}{Z}\sum_s O(s)\,e^{-\beta E(s)}.
$$

Năng lượng tự do $$F=-\beta^{-1}\log Z$$ cho ta toàn bộ nhiệt động học. Xác suất $$p(s)\propto e^{-\beta E(s)}$$ được gọi là trọng số **Boltzmann–Gibbs**.

**Cơ chế chính.** Một đại lượng vĩ mô ở trạng thái cân bằng là **kỳ vọng theo một phân bố xác suất có trọng số theo năng lượng**, chứ không phải giá trị dọc theo một quỹ đạo riêng lẻ.

---

## 2. Giới hạn nhiệt động và các pha

Những điểm kỳ dị thú vị (bước nhảy ở chuyển pha loại một, điểm tới hạn) thường chỉ xuất hiện sau khi cho $$N\to\infty$$. Với hệ hữu hạn, $$Z$$ là hàm trơn; việc mật độ năng lượng tự do không giải tích là một hiện tượng của giới hạn. Vì vậy cần cẩn thận khi nói về sự tồn tại của độ đo Gibbs trên thể tích vô hạn.

**Mô hình Ising.** Các spin nhận giá trị $$\pm 1$$ trên một mạng lưới, tương tác với các spin láng giềng. Onsager đã giải chính xác trường hợp 2 chiều, một cột mốc nơi vật lý gặp toán học chặt chẽ. Ở số chiều cao hơn, đây vẫn là một lĩnh vực nghiên cứu sôi động.

---

## 3. Cấu trúc xác suất

| Ý tưởng | Vai trò |
|---------|---------|
| Độ lệch lớn | Xác suất của sự kiện hiếm giảm theo hàm mũ, với "chi phí" tính được |
| Tương quan suy giảm / tính trộn | Liên quan đến tính duy nhất của độ đo Gibbs |
| Giới hạn tỉ lệ | Trường liên tục xuất hiện từ mô hình mạng lưới (liên hệ với nhóm tái chuẩn hóa, SLE trong 2 chiều) |
| Hiện tượng tập trung | Cấu hình điển hình nằm sát giá trị kỳ vọng (theo tinh thần các kết quả của Talagrand) |

Cơ học thống kê là **nguồn sinh ra các định lý xác suất**, chứ không chỉ là nơi áp dụng tổ hợp ở trình độ đại học.

---

## 4. Cầu nối với lý thuyết trường lượng tử và nhóm tái chuẩn hóa

Về mặt hình thức, lý thuyết trường lượng tử Euclid trông giống một lý thuyết trường thống kê liên tục, trong đó tác dụng đóng vai trò năng lượng ([tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/)). Hiện tượng tới hạn và giới hạn liên tục được tổ chức bằng nhóm tái chuẩn hóa ([nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/)). Lý thuyết trường kiến thiết thường kiểm soát các xấp xỉ trên mạng lưới rồi lấy giới hạn, cùng tinh thần với cơ học thống kê trên thể tích vô hạn.

---

## 5. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Chuyển pha là khi đồ thị trông gián đoạn." | Thiếu chặt chẽ | Về mặt toán học, chuyển pha gắn với giới hạn nhiệt động và điểm kỳ dị của năng lượng tự do. |
| "Cơ học thống kê chỉ dùng cho hóa học." | Sai | Nó liên hệ trực tiếp với toán thuần túy qua xác suất, phương trình đạo hàm riêng, lý thuyết trường lượng tử. |
| "Onsager giải được Ising 2 chiều nên mọi hiện tượng tới hạn đã được hiểu." | Sai | Ising 2 chiều là một kết quả đẹp; lý thuyết tổng quát vẫn còn rất nhiều vấn đề mở. |

---

## Bài tập

1. **Hệ hai trạng thái.** Với năng lượng $$0$$ và $$E$$, viết $$Z$$ và năng lượng trung bình theo $$\beta$$.  
2. **Giới hạn nhiệt động.** Vì sao $$F$$ có thể trơn khi $$N$$ hữu hạn nhưng không còn trơn trong giới hạn?  
3. **Phân bố Gibbs.** Trong không quá 40 chữ: công thức $$p(s)\propto e^{-\beta E(s)}$$ mô tả điều gì?  
4. **Cầu nối.** Viết một đoạn: lý thuyết trường lượng tử Euclid như là "cơ học thống kê của trường".  
5. **Nói chính xác.** Viết lại câu: "Mô phỏng thấy có bước nhảy, vậy là ta đã chứng minh định lý về chuyển pha."

---

## Tài liệu tham khảo

1. Baxter, *Exactly Solved Models in Statistical Mechanics* (Các mô hình giải được chính xác trong cơ học thống kê).  
2. Georgii, *Gibbs Measures and Phase Transitions* (Độ đo Gibbs và chuyển pha).  
3. Trong khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).  
