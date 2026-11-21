---
layout: post
title: "Nhóm renormalization: Tỉ lệ như một ý tưởng toán"
chapter: '06'
order: 22
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Một hệ vật lý trông khác nhau khi nhìn ở các độ phóng đại khác nhau. Chất lỏng là tập hợp phân tử ở thang nhỏ, nhưng là một trường vận tốc liên tục ở thang lớn. Nam châm là các spin nguyên tử khi nhìn gần, nhưng là một trường từ hóa trơn khi nhìn từ xa. **Nhóm tái chuẩn hóa (RG)** là tập hợp các ý tưởng giải thích **mô tả hiệu dụng thay đổi thế nào theo thang đo**, và vì sao nhiều chi tiết trở nên không quan trọng, trong khi chỉ vài hằng số tương tác quyết định hành vi ở khoảng cách lớn.

RG ra đời từ những khó khăn với các đại lượng vô hạn trong lý thuyết trường lượng tử, và trưởng thành trong lý thuyết hiện tượng tới hạn của Kenneth Wilson. Ngày nay nó là ngôn ngữ chung của lý thuyết trường lượng tử, cơ học thống kê, và cả một phần của xác suất và hình học. Bài trong nhánh Cầu nối này trình bày ý chính, bức tranh điểm bất động, và phân biệt phần nào là định lý, phần nào là phép tính của vật lý. Bài liên quan: [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), [bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích khái niệm **lý thuyết hiệu dụng**: một mô hình đúng ở dưới một mức cắt (cutoff) $$\Lambda$$, chỉ với hữu hạn hằng số quan trọng.
- Phát biểu ý chính của RG: lấy tích phân hết các bậc tự do ở khoảng cách ngắn → các hằng số $$g(\mu)$$ thay đổi ("chạy") theo thang đo $$\mu$$.
- Định nghĩa ở mức ý tưởng các toán tử **liên quan / không liên quan / biên** (relevant / irrelevant / marginal) gần một điểm bất động.
- Liên hệ hiện tượng tới hạn (độ dài tương quan $$\to\infty$$) với điểm bất động của RG và tính phổ quát.
- Liên hệ tính tự do tiệm cận của lý thuyết gauge không giao hoán với dòng RG của hằng số tương tác (ở mức tổng quan).
- Tránh các cách hiểu sai: "tái chuẩn hóa chỉ là giấu vô hạn xuống dưới thảm", "RG chứng minh được bài toán khe khối lượng của Clay".

**Kiến thức nền.** Quen với việc mô hình có tham số; bài [phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/) (không bắt buộc) giúp hiểu ngôn ngữ về mức cắt.

---

## 1. Vì sao thang đo đi vào toán học

Một lý thuyết trường liên tục có bậc tự do ở mọi độ dài. Nếu không tổ chức lại thì có vô hạn mode. Tự nhiên thường cho thấy **tính tách rời** (decoupling): người quan sát ở thang vĩ mô không cần biết toàn bộ Hamiltonian vi mô, mà chỉ cần một vài tham số hiệu dụng.

RG đặt câu hỏi một cách chính xác: **nếu thay đổi độ phân giải, cần điều chỉnh các tham số thế nào để các đại lượng quan sát ở khoảng cách lớn không thay đổi?**

---

## 2. Mức cắt và tham số trần

Ta chính quy hóa bằng một mức cắt $$\Lambda$$ (bước mạng lưới $$a\sim 1/\Lambda$$, mức cắt xung lượng, …). Hằng số trần (bare) $$g_0(\Lambda)$$ phụ thuộc vào mức cắt. Các đại lượng vật lý ở thang $$\mu\ll\Lambda$$ cần có giới hạn hữu hạn khi $$\Lambda\to\infty$$, sau khi điều chỉnh $$g_0$$ thích hợp. Đó là ý tưởng cổ điển về **tính tái chuẩn hóa được** (bao gồm Yang–Mills 4 chiều, theo nghĩa nhiễu loạn).

**Liên hệ với phân bố và giới hạn liên tục.** Bỏ mức cắt là lấy giới hạn trong một không gian hàm; vấn đề tích các phân bố không xác định xuất hiện trở lại, giống như trong bài về giới hạn liên tục.

---

## 3. Bức tranh của Wilson: gộp khối và điểm bất động

RG theo Wilson (cho hiện tượng tới hạn, thập niên 1970), nói đại khái, gồm các bước:

1. Bắt đầu với một lý thuyết trường thống kê hoặc mô hình spin trên mạng lưới ở khoảng cách ngắn.  
2. **Làm thô** (gộp các spin thành khối, hoặc lấy tích phân các xung lượng cao).  
3. Co giãn lại độ dài để đơn vị mạng lưới trở về như cũ.  
4. Đọc ra các hằng số hiệu dụng mới $$g'$$, xem như một ánh xạ $$g\mapsto R(g)$$.  

Lặp lại $$R$$ cho ta một **dòng chảy**. Một **điểm bất động** $$R(g_*)=g_*$$ mô tả một lý thuyết bất biến theo thang đo. Gần $$g_*$$, các trị riêng của RG tuyến tính hóa phân loại các nhiễu loạn:

| Loại | Hành vi khi thang đo tăng (vùng hồng ngoại) | Vai trò |
|------|--------------------------|---------|
| Liên quan (relevant) | Tăng lên | Phải tinh chỉnh; quyết định pha |
| Không liên quan (irrelevant) | Tắt dần | Chi tiết vi mô bị quên đi → **tính phổ quát** |
| Biên (marginal) | Thay đổi chậm (theo logarit) | Tinh tế; hằng số "chạy" |

**Cơ chế chính.** Các lớp phổ quát tồn tại vì nhiều mô hình vi mô khác nhau cùng chảy về **một** điểm bất động; chỉ các hướng liên quan mới phân biệt các pha vĩ mô.

---

## 4. Phương trình Callan–Symanzik và hằng số chạy (ý chính trong lý thuyết trường lượng tử)

Trong ngôn ngữ lý thuyết trường lượng tử liên tục, sự phụ thuộc của các hàm tương quan vào thang tái chuẩn hóa $$\mu$$ bị ràng buộc bởi một phương trình vi phân (phương trình Callan–Symanzik). **Hàm beta** $$\beta(g)=\mu\partial_\mu g$$ cho biết hằng số tương tác thay đổi thế nào.

**Tính tự do tiệm cận.** Với lý thuyết gauge không giao hoán (QCD), $$\beta(g)<0$$ khi tương tác yếu: tương tác càng yếu đi ở khoảng cách ngắn. Đây là nền tảng khái niệm để hiểu các thí nghiệm tán xạ không đàn hồi sâu. Cùng ý tưởng này giải thích vì sao có thể hy vọng tiếp cận giới hạn liên tục từ mạng lưới, nhưng nó không tự chứng minh được định lý khe khối lượng của Clay.

---

## 5. Cầu nối với cơ học thống kê và xác suất

Mô hình Ising, thấm (percolation), mô hình $$\phi^4$$ là những phòng thí nghiệm nơi các ý tưởng RG đã trở thành định lý, ở một số chiều đặc biệt hoặc bằng phương pháp kiến thiết. Lý thuyết trường bảo giác (CFT) tại điểm tới hạn (đặc biệt trong 2 chiều) nâng tính bất biến theo thang đo lên thành đối xứng bảo giác. Liên hệ với xác suất gồm các giới hạn tỉ lệ của hệ ngẫu nhiên (SLE trong 2 chiều), nơi đối tượng liên tục xuất hiện sau một quá trình lấy giới hạn kiểu tái chuẩn hóa.

---

## 6. Những gì RG *không* tự động cho ta

- Một định nghĩa kiến thiết đầy đủ cho QCD liên tục 4 chiều.  
- Chứng minh hiện tượng giam hãm hay khe khối lượng ([bài toán Clay về Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/)).  
- Quyền bỏ qua dị thường, tô pô, hay các lớp phi nhiễu loạn ([instanton]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/)).  

RG là **một nguyên lý tổ chức và một khung tính toán**. Đôi khi nó được nâng lên thành định lý, nhưng thường được dùng như một phép tính vật lý có kiểm soát.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Tái chuẩn hóa nghĩa là lý thuyết sai và ta che giấu lỗi." | Gây hiểu nhầm | Đó là mô tả hiệu dụng phụ thuộc thang đo, cùng với việc lấy giới hạn liên tục. |
| "Wilson đã giải quyết xong lý thuyết trường lượng tử." | Nói quá | Ông thay đổi cả khung lý thuyết; nhưng nhiều bài toán dựng lý thuyết vẫn còn mở. |
| "Tự do tiệm cận nghĩa là đã chứng minh khe khối lượng." | Sai | Hai trực giác có liên quan, nhưng là hai mệnh đề toán học khác nhau. |

---

## Bài tập

1. **Lý thuyết hiệu dụng.** Nêu một ví dụ ngoài vật lý về một mô tả thô chỉ cần ít tham số (không quá 80 chữ).  
2. **Hàm beta.** Nếu $$\beta(g)<0$$ với $$g>0$$ nhỏ, hằng số tương tác tăng hay giảm khi $$\mu$$ tăng?  
3. **Tính phổ quát.** Vì sao nước (tại điểm tới hạn lỏng–khí) và nam châm có thể có cùng số mũ tới hạn?  
4. **Nói chính xác.** Viết lại câu: "Vì phải tái chuẩn hóa nên lý thuyết trường lượng tử không phải toán học thật."  
5. **Cầu nối.** Viết một đoạn nối dòng RG với mục tiêu đi từ mạng lưới đến giới hạn liên tục cho Yang–Mills.

---

## Tài liệu tham khảo

1. Wilson & Kogut, về RG và khai triển $$\epsilon$$.  
2. Cardy, *Scaling and Renormalization in Statistical Physics* (Tỉ lệ và tái chuẩn hóa trong vật lý thống kê).  
3. Trong khóa học: [Tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).  
