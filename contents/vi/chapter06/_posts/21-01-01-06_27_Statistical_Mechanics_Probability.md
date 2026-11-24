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

Trong một cốc nước bình thường trên bàn có khoảng $$10^{25}$$ phân tử $$\text{H}_2\text{O}$$ đang va chạm hỗn loạn hàng tỉ lần mỗi giây. Không một siêu máy tính nào trên Trái Đất có thể giải phương trình chuyển động cho từng phân tử ấy — nhưng kỳ lạ thay, ở thang mắt thường, cốc nước lại tuân theo những định luật cực kỳ gọn gàng và chắc chắn: ở $$0^\circ\text{C}$$ nó đột ngột đóng băng, ở $$100^\circ\text{C}$$ nó sôi bùng thành hơi, với áp suất và nhiệt dung đo được chính xác từng chữ số! Làm thế nào sự hỗn loạn vi mô khổng lồ lại tự kết tinh thành những bước nhảy sắc lẹm gọi là **chuyển pha**?

**Cơ học thống kê cân bằng** trả lời câu hỏi đó bằng ngôn ngữ của **lý thuyết xác suất**: thay vì theo dõi một quỹ đạo riêng lẻ, ta đặt lên không gian tất cả các cấu hình vi mô một phân bố xác suất gọi là **độ đo Gibbs** (trọng số $$e^{-\beta E(s)}$$), gom mọi thông tin vào một hàm sinh duy nhất gọi là **hàm phân hoạch** $$Z$$, rồi cho số hạt $$N \to \infty$$. Chính cấu trúc ấy vừa là nguồn gốc của nhiều nhánh xác suất hiện đại (lý thuyết độ lệch lớn, tập trung độ đo, quá trình điểm Gibbs), vừa — qua phép quay Wick sang thời gian ảo — trùng khớp về mặt toán học với lý thuyết trường lượng tử Euclid!

Bài tổng quan này đi sâu vào mục 4 của [bài trung tâm về vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), đồng thời liên hệ với bài [nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/) và bài [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/). Mục tiêu là nắm cơ chế chính và học cách nói chính xác.

---

## Bản đồ kiến thức nền: Cơ học thống kê toán học là gì và nghiên cứu những gì?

Nếu bạn đã học xác suất thống kê ở đại học (luật số lớn, phân phối hàm mũ/softmax trong học máy, kỳ vọng và phương sai), bạn sẽ nhận ra ngay một bí mật thú vị: **công thức softmax trong mạng nơ-ron thực chất chính là phân bố Boltzmann–Gibbs** $$p(s) = \frac{1}{Z} e^{-\beta E(s)}$$ của cơ học thống kê!

Điều làm nên sức sâu sắc của **cơ học thống kê toán học** là cuộc giằng co vĩnh cửu giữa **năng lượng** (muốn kéo hệ về trạng thái trật tự có năng lượng thấp nhất) và **entropy** (số lượng áp đảo của các cấu hình hỗn loạn), được điều tiết bởi tham số nhiệt độ nghịch đảo $$\beta = 1/(k_B T)$$:

- **Khi nhiệt độ cao ($$\beta \to 0$$):** Trọng số $$e^{-\beta E(s)} \approx 1$$ gần như đều nhau; entropy thắng thế, hệ rơi vào pha hỗn loạn (khí, chất thuận từ).
- **Khi nhiệt độ thấp ($$\beta \to \infty$$):** Cấu hình có năng lượng thấp nhất áp đảo tuyệt đối; năng lượng thắng thế, hệ khóa vào pha trật tự (tinh thể rắn, nam châm sắt từ).
- **Ngành này nghiên cứu gì?** Không giống xác suất cơ bản chỉ xét các biến ngẫu nhiên *độc lập* (nên luôn mượt mà), cơ học thống kê nghiên cứu các hệ gồm vô số biến ngẫu nhiên **tương tác mạnh với hàng xóm của chúng** trên một đồ thị hay mạng lưới $$\mathbb{Z}^d$$. Câu hỏi lớn nhất là: trong giới hạn thể tích vô hạn ($$N \to \infty$$), khi nào tồn tại *nhiều hơn một* độ đo Gibbs tương thích với cùng quy tắc tương tác (dấu hiệu toán học của **chuyển pha**), tương quan giữa hai điểm xa nhau suy giảm nhanh theo hàm mũ hay chậm theo hàm lũy thừa (điểm tới hạn), và hình dạng ngẫu nhiên ở thang vĩ mô hội tụ về đối tượng liên tục nào?

Với bản đồ đó trong tay, mỗi công thức trong cơ học thống kê đều hiện ra như một bài toán xác suất rất giàu hình ảnh.

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

**Hàm phân hoạch** $$Z(\beta)$$ không chỉ là hằng số chuẩn hóa cho tổng xác suất bằng 1 — nó là "hàm sinh vạn năng" của cả hệ! Chỉ cần lấy đạo hàm của $$\log Z(\beta)$$ theo $$\beta$$, ta rút ngay ra mọi đại lượng vĩ mô: chẳng hạn $$-\frac{\partial}{\partial \beta}\log Z = \langle E\rangle$$ (năng lượng trung bình) và $$\frac{\partial^2}{\partial \beta^2}\log Z = \operatorname{Var}(E)$$ (phương sai năng lượng, tỉ lệ trực tiếp với nhiệt dung!). Năng lượng tự do $$F=-\beta^{-1}\log Z$$ gói gọn toàn bộ nhiệt động học cân bằng, còn xác suất $$p(s)\propto e^{-\beta E(s)}$$ gọi là trọng số **Boltzmann–Gibbs**.

Hãy thử nhanh với một **hệ 2 trạng thái** đơn giản (một hạt spin trong từ trường có hai mức năng lượng $$0$$ và $$\Delta > 0$$): khi đó $$Z(\beta) = 1 + e^{-\beta\Delta}$$ và năng lượng trung bình là $$\langle E\rangle = \frac{\Delta}{e^{\beta\Delta} + 1}$$. Khi nhiệt độ tiến về $$0$$ ($$\beta \to \infty$$), $$\langle E\rangle \to 0$$ (hệ đóng băng hoàn toàn ở trạng thái cơ bản); khi nhiệt độ rất cao ($$\beta \to 0$$), $$\langle E\rangle \to \Delta/2$$ (hai trạng thái xảy ra đồng đều $$50\%–50\%$$).

**Cơ chế chính.** Một đại lượng vĩ mô ở trạng thái cân bằng là **kỳ vọng theo một phân bố xác suất có trọng số theo năng lượng**, chứ không phải giá trị dọc theo một quỹ đạo cơ học riêng lẻ.

---

## 2. Giới hạn nhiệt động và các pha

Một điểm toán học cực kỳ tinh tế thường bị bỏ qua ở sách nhập môn: với bất kỳ hệ **hữu hạn** nào (dù $$N = 10^{23}$$), hàm phân hoạch $$Z_N(\beta)$$ là một tổng hữu hạn các hàm mũ dương $$e^{-\beta E(s)} > 0$$, nên mật độ năng lượng tự do $$f_N(\beta) = -\frac{1}{\beta N}\log Z_N(\beta)$$ luôn là một **hàm giải tích trơn vô hạn**, không bao giờ có góc nhọn hay bước nhảy! Chỉ khi lấy **giới hạn nhiệt động** $$N \to \infty$$ (với mật độ cố định), giới hạn $$f(\beta) = \lim_{N\to\infty} f_N(\beta)$$ mới có thể xuất hiện **điểm kỳ dị không giải tích** — đó mới là định nghĩa toán học chặt chẽ của **chuyển pha** (chuyển pha loại một ứng với đạo hàm bậc nhất nhảy vọt như nước hóa hơi; chuyển pha loại hai hay điểm tới hạn ứng với đạo hàm bậc hai phân kỳ như nam châm ở nhiệt độ Curie). Vì vậy, ở thể tích vô hạn, ta định nghĩa trạng thái cân bằng thông qua họ các điều kiện tương thích địa phương (phương trình DLR — Dobrushin–Lanford–Ruelle) cho **độ đo Gibbs**; khi phương trình DLR có nhiều hơn một nghiệm, hệ có sự cùng tồn tại của nhiều pha!

**Mô hình Ising.** Trên mỗi đỉnh $$i$$ của một mạng lưới (như lưới vuông $$\mathbb{Z}^d$$), ta đặt một spin $$\sigma_i \in \{+1, -1\}$$ với năng lượng $$E(\sigma) = -J\sum_{i\sim j}\sigma_i\sigma_j$$ (các spin hàng xóm thích chỉ cùng chiều để giảm năng lượng).
- Ở **1 chiều** ($$\mathbb{Z}$$): Ernst Ising chứng minh năm 1925 rằng *không có chuyển pha* ở mọi nhiệt độ dương (chỉ cần một vết đứt gãy cũng đủ phá trật tự toàn dây).
- Ở **2 chiều** ($$\mathbb{Z}^2$$): Lars Onsager (1944) giải chính xác năng lượng tự do và chỉ ra một chuyển pha sắc nét tại $$\beta_c J = \frac{1}{2}\ln(1+\sqrt{2})$$ — một trong những cột mốc vĩ đại nhất nơi vật lý gặp toán học chặt chẽ!
- Ở **3 chiều** trở lên: chuyển pha tồn tại (lập luận đường biên Peierls), nhưng không có công thức giải tích đóng kiểu Onsager; việc hiểu chính xác các số mũ tới hạn của Ising 3 chiều vẫn là một lĩnh vực nghiên cứu sôi động (từ bootstrap bảo giác đến xác suất hình học).

---

## 3. Cấu trúc xác suất

| Ý tưởng | Vai trò |
|---------|---------|
| Độ lệch lớn | Xác suất của sự kiện hiếm giảm theo hàm mũ, với "chi phí" (hàm tốc độ) tính được, liên hệ trực tiếp với entropy và năng lượng tự do |
| Tương quan suy giảm / tính trộn | Liên quan đến tính duy nhất của độ đo Gibbs và tốc độ hội tụ của thuật toán lấy mẫu MCMC |
| Giới hạn tỉ lệ | Trường liên tục xuất hiện từ mô hình mạng lưới (liên hệ với nhóm tái chuẩn hóa, SLE trong 2 chiều — mang về các Huy chương Fields cho Werner, Smirnov, Duminil-Copin) |
| Hiện tượng tập trung | Cấu hình điển hình nằm sát giá trị kỳ vọng (theo tinh thần các kết quả của Michel Talagrand cho thủy tinh spin) |

Cơ học thống kê là **nguồn sinh ra hàng loạt định lý xác suất hiện đại**, chứ không chỉ là nơi áp dụng bài toán đếm tổ hợp ở trình độ đại học.

---

## 4. Cầu nối với lý thuyết trường lượng tử và nhóm tái chuẩn hóa

Về mặt hình thức, lý thuyết trường lượng tử Euclid trông giống hệt một lý thuyết trường thống kê liên tục, trong đó tác dụng Euclid $$S_E[\phi]$$ đóng vai trò năng lượng $$E(s)$$ và $$\hbar$$ đóng vai trò nhiệt độ $$k_B T$$ ([tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/)). Hiện tượng tới hạn (nơi độ dài tương quan tiến ra vô cùng) và quá trình lấy giới hạn liên tục từ mạng lưới được tổ chức bằng nhóm tái chuẩn hóa ([nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/)). Lý thuyết trường kiến thiết thường kiểm soát các xấp xỉ trên mạng lưới hữu hạn rồi lấy giới hạn nhiệt động và giới hạn bước lưới về $$0$$ — cùng một tinh thần giải tích với cơ học thống kê trên thể tích vô hạn.

---

## 5. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Chuyển pha là khi đồ thị trông gián đoạn." | Thiếu chặt chẽ | Về mặt toán học, chuyển pha gắn với giới hạn nhiệt động và điểm kỳ dị của năng lượng tự do. |
| "Cơ học thống kê chỉ dùng cho hóa học." | Sai | Nó liên hệ trực tiếp với toán thuần túy qua xác suất, phương trình đạo hàm riêng, lý thuyết trường lượng tử. |
| "Onsager giải được Ising 2 chiều nên mọi hiện tượng tới hạn đã được hiểu." | Sai | Ising 2 chiều là một kết quả đẹp; lý thuyết tổng quát (đặc biệt ở chiều 3 và các hệ không cân bằng, chảy rối) vẫn còn rất nhiều vấn đề mở. |

---

## Tài liệu tham khảo

1. Baxter, *Exactly Solved Models in Statistical Mechanics* (Các mô hình giải được chính xác trong cơ học thống kê).  
2. Georgii, *Gibbs Measures and Phase Transitions* (Độ đo Gibbs và chuyển pha).  
3. Trong khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).  
