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

Hãy thử một thí nghiệm tưởng tượng quen thuộc: đặt một cốc nước sôi và một thanh nam châm sắt cạnh nhau, rồi đun cả hai tới đúng điểm tới hạn chuyển pha của chúng (điểm tới hạn lỏng–khí của nước ở $$374^\circ\text{C}$$, và nhiệt độ Curie của sắt ở $$770^\circ\text{C}$$). Ở cấp độ vi mô, nước và sắt chẳng có gì giống nhau — một bên là các phân tử $$\text{H}_2\text{O}$$ va chạm hỗn loạn, bên kia là mạng tinh thể nguyên tử sắt với các spin lượng tử. Thế nhưng khi đo cách các đại lượng vật lý biến đổi gần điểm tới hạn, ta lại thu được **chính xác cùng những con số mũ tới hạn giống hệt nhau**! Tại sao tự nhiên lại "quên sạch" toàn bộ chi tiết vi mô để chỉ giữ lại vài con số phổ quát như vậy?

Câu trả lời nằm ở một trong những ý tưởng sâu sắc nhất của vật lý toán thế kỷ XX: **nhóm tái chuẩn hóa (renormalization group — RG)**. Thay vì cố mô tả thế giới ở một độ phóng đại duy nhất, RG biến **tỉ lệ (scale)** thành một phép biến đổi động lực: khi ta lùi ra xa dần và "làm mờ" các chi tiết nhỏ, mô tả hiệu dụng của hệ chảy đi trong không gian các lý thuyết như thế nào? Ra đời từ cuộc vật lộn với các tích phân vô hạn trong lý thuyết trường lượng tử và trưởng thành qua lý thuyết hiện tượng tới hạn của Kenneth Wilson (giải Nobel 1982), RG ngày nay là ngôn ngữ chung của lý thuyết trường lượng tử, cơ học thống kê, xác suất và hình học. Bài liên quan: [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), [bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Kiến thức cần nhớ: Lý thuyết Nhóm tái chuẩn hóa (RG) đứng trên ba trụ cột nào?

Nếu bạn đã học giải tích hệ động lực và xác suất ở đại học, bạn thực ra đã gặp tinh thần của RG từ trước:

### 1. Xác suất và Định lý giới hạn trung tâm tổng quát
Hãy nhớ lại **định lý giới hạn trung tâm (CLT)**: lấy hàng nghìn biến ngẫu nhiên độc lập $$X_1, X_2, \dots$$ có phân phối bất kỳ (miễn phương sai hữu hạn), gộp thành từng khối rồi chia cho $$\sqrt{N}$$ để giữ nguyên độ rộng. Lặp lại phép "gộp khối + co giãn" đó, mọi phân phối ban đầu đều chảy về **một điểm bất động duy nhất** là phân phối chuẩn Gauss — mọi chi tiết hình dạng ban đầu (mômen bậc 3, 4, 5...) đều tắt dần. **RG** là sự mở rộng vĩ đại của CLT sang các hệ có **tương tác mạnh**, nơi điểm bất động không còn là Gauss mà là các lý thuyết tới hạn phi tầm thường!

### 2. Hệ động lực trên không gian các lý thuyết
Trong RG, "không gian trạng thái" là **không gian các bộ tham số/hằng số tương tác** $$g = (g_1, g_2, \dots)$$. Phép biến đổi RG $$g \mapsto R(g)$$ gồm hai nhịp: *làm thô* (tích phân/gộp các bậc tự do ở khoảng cách nhỏ) rồi *co giãn lại thước đo*. (Gọi là "nhóm" vì lý do lịch sử, nhưng vì làm thô làm mất thông tin chi tiết nên thực chất là một *nửa nhóm*.) Quanh mỗi **điểm bất động** $$R(g_*) = g_*$$, ta tuyến tính hóa $$R$$ (như ma trận Jacobian trong phương trình vi phân) để phân loại hướng nào phình to (liên quan — quyết định pha) và hướng nào co tắt (không liên quan — sinh ra **tính phổ quát**).

### 3. Lý thuyết trường hiệu dụng và Hàm beta
Ở vật lý năng lượng cao, RG giải thích vì sao ta không cần biết vật lý ở thang Planck $$10^{-35}\text{ m}$$ mới tính được quỹ đạo electron hay phản ứng hóa học: các chi tiết siêu nhỏ tự gộp vào một vài hằng số hiệu dụng "chạy" theo thang năng lượng $$\mu$$ dưới sự điều khiển của **hàm beta** $$\beta(g) = \mu \frac{\partial g}{\partial \mu}$$.

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

Một lý thuyết trường liên tục có bậc tự do ở mọi độ dài — từ quy mô thiên hà xuống tới $$10^{-35}$$ mét. Nếu muốn dự đoán dòng chảy nước trong ống dẫn mà buộc phải giải phương trình Schrödinger cho từng hạt quark trong mỗi nguyên tử oxy, khoa học sẽ tê liệt hoàn toàn. May mắn thay, tự nhiên thường có **tính tách rời thang đo** (decoupling): người quan sát ở thang vĩ mô không cần biết toàn bộ Hamiltonian vi mô, mà chỉ cần một vài tham số hiệu dụng (như mật độ và độ nhớt của chất lỏng).

RG đặt câu hỏi một cách chính xác: **nếu thay đổi độ phân giải (thang năng lượng $$\mu$$ hay bước lưới $$a$$), cần điều chỉnh các tham số thế nào để các đại lượng quan sát ở khoảng cách lớn không thay đổi?**

---

## 2. Mức cắt và tham số trần

Để tránh các tích phân phân kỳ ở khoảng cách bằng $$0$$ (xung lượng vô hạn), ta chính quy hóa lý thuyết bằng một **mức cắt $$\Lambda$$** (chẳng hạn đặt trường lên mạng lưới có bước $$a \sim 1/\Lambda$$, hoặc chỉ giữ các sóng có xung lượng nhỏ hơn $$\Lambda$$). Hằng số "trần" (bare) $$g_0(\Lambda)$$ xuất hiện trong Lagrangian ở thang cắt sẽ phụ thuộc vào $$\Lambda$$. Các đại lượng vật lý đo được ở thang thí nghiệm $$\mu \ll \Lambda$$ cần có giới hạn hữu hạn khi $$\Lambda \to \infty$$, sau khi ta điều chỉnh $$g_0(\Lambda)$$ thích hợp. Đó là ý tưởng cổ điển về **tính tái chuẩn hóa được** (bao gồm điện động lực học lượng tử QED và Yang–Mills 4 chiều, theo nghĩa nhiễu loạn).

**Liên hệ với phân bố và giới hạn liên tục.** Dưới góc nhìn giải tích, bỏ mức cắt ($$\Lambda \to \infty$$) là lấy giới hạn trong một không gian hàm suy rộng; vấn đề "nhân hai phân bố tại cùng một điểm không xác định" xuất hiện trở lại chính dưới dạng các vòng phân kỳ tử ngoại cần phản số hạng (counterterm) để điều chỉnh.

---

## 3. Bức tranh của Wilson: gộp khối và điểm bất động

RG theo Kenneth Wilson (cho hiện tượng tới hạn, thập niên 1970) biến quá trình "lùi ra xa nhìn ảnh" thành một phép lặp rõ ràng:

1. Bắt đầu với một lý thuyết trường thống kê hoặc mô hình spin trên mạng lưới ở khoảng cách ngắn.  
2. **Làm thô** (gộp các spin thành khối, hoặc lấy tích phân loại bỏ các mode xung lượng cao giữa $$\Lambda/b$$ và $$\Lambda$$).  
3. Co giãn lại độ dài để đơn vị mạng lưới trở về như cũ.  
4. Đọc ra các hằng số hiệu dụng mới $$g'$$, xem như một ánh xạ $$g\mapsto R(g)$$.  

### Giải thích: tự tay chạy một bước RG chính xác trên mô hình Ising 1 chiều

Thay vì chỉ nghe nói về "gộp khối spin", hãy tự tay tính **chính xác** ánh xạ RG $$K \mapsto K'$$ cho chuỗi nam châm Ising 1 chiều (các spin $$\sigma_i \in \{+1, -1\}$$ xếp thành hàng ngang, tương tác láng giềng với hằng số $$K = \beta J > 0$$):

1. **Làm thô bằng cách lấy tổng bỏ hết các spin ở vị trí chẵn:** Xét ba spin liên tiếp $$\sigma_1, \sigma_2, \sigma_3$$. Trọng số Boltzmann nối chúng là $$e^{K\sigma_1\sigma_2 + K\sigma_2\sigma_3}$$. Cộng trên hai trạng thái $$\sigma_2 = +1$$ và $$\sigma_2 = -1$$:
   $$
   \sum_{\sigma_2 = \pm 1} e^{K\sigma_2(\sigma_1 + \sigma_3)} = e^{K(\sigma_1 + \sigma_3)} + e^{-K(\sigma_1 + \sigma_3)} = 2\cosh\bigl(K(\sigma_1 + \sigma_3)\bigr).
   $$
2. **Tìm hằng số tương tác hiệu dụng mới $$K'$$ giữa $$\sigma_1$$ và $$\sigma_3$$:** Ta muốn viết biểu thức trên thành $$C\,e^{K'\sigma_1\sigma_3}$$ (một mô hình Ising giống hệt ban đầu nhưng khoảng cách lưới đã gấp đôi!). Kiểm tra hai trường hợp:
   - Nếu $$\sigma_1 = \sigma_3$$ (cùng dấu): $$C\,e^{K'} = 2\cosh(2K)$$.
   - Nếu $$\sigma_1 = -\sigma_3$$ (ngược dấu): $$C\,e^{-K'} = 2\cosh(0) = 2$$.
   Chia hai phương trình cho nhau ta được $$e^{2K'} = \cosh(2K)$$, và dùng đồng nhất thức hyperbolic $$\tanh(K') = \frac{e^{2K'}-1}{e^{2K'}+1} = \frac{\cosh(2K)-1}{\cosh(2K)+1}$$, ta thu được **quy tắc RG tuyệt đẹp**:
   $$
   \tanh(K') = \tanh^2(K)!
   $$
3. **Chạy dòng chảy bằng số cụ thể:** Đặt $$x = \tanh(K) \in [0, 1]$$. Khi đó ánh xạ RG chỉ là $$x \mapsto x^2$$!
   - Hai điểm bất động giải từ $$x = x^2$$ là $$x_* = 0$$ (nhiệt độ $$T = \infty$$, hỗn loạn hoàn toàn) và $$x_* = 1$$ (nhiệt độ $$T = 0$$, trật tự tuyệt đối).
   - Bắt đầu ở nhiệt độ rất lạnh với $$x_0 = 0.9$$: sau 1 bước $$x_1 = 0.81$$, bước 2 là $$x_2 = 0.6561$$, bước 3 là $$x_3 = 0.4305$$, bước 4 là $$x_4 = 0.1853$$, rồi nhanh chóng rơi tọt về $$x_* = 0$$!
4. **Kết luận toán học rút ra ngay lập tức:** Mọi nhiệt độ dương ($$x_0 < 1$$) khi lùi ra xa đều chảy về pha hỗn loạn $$x_* = 0$$! Chỉ bằng 4 dòng đại số, RG vừa **chứng minh chặt chẽ** rằng mô hình Ising 1 chiều không có chuyển pha ở bất kỳ nhiệt độ dương nào — còn ở 2 chiều và 3 chiều, tồn tại thêm một điểm bất động *không tầm thường* $$0 < x_* < 1$$ nằm giữa $$0$$ và $$1$$, và đó chính là điểm tới hạn!

Gần một điểm bất động $$g_*$$ tổng quát, tuyến tính hóa ánh xạ $$R$$ cho ta các trị riêng phân loại mọi nhiễu loạn thành ba nhóm:

| Loại | Hành vi khi thang đo tăng (vùng hồng ngoại) | Vai trò |
|------|--------------------------|---------|
| Liên quan (relevant) | Tăng lên | Phải tinh chỉnh; quyết định pha |
| Không liên quan (irrelevant) | Tắt dần | Chi tiết vi mô bị quên đi → **tính phổ quát** |
| Biên (marginal) | Thay đổi chậm (theo logarit) | Tinh tế; hằng số "chạy" |

**Cơ chế chính.** Các lớp phổ quát tồn tại vì vô số mô hình vi mô khác nhau (nước, $$\text{CO}_2$$, hợp kim từ tính một trục...) chỉ khác nhau ở các thành phần *không liên quan*, nên khi lùi ra xa chúng cùng bị hút về **cùng một** điểm bất động; chỉ một vài hướng *liên quan* (như nhiệt độ và áp suất/từ trường) mới cần tinh chỉnh để đặt hệ đúng vào điểm tới hạn.

---

## 4. Phương trình Callan–Symanzik và hằng số chạy (ý chính trong lý thuyết trường lượng tử)

Trong ngôn ngữ lý thuyết trường lượng tử liên tục, việc các dự đoán vật lý không được phụ thuộc vào thang đo tái chuẩn hóa nhân tạo $$\mu$$ dẫn tới một phương trình vi phân gọi là **phương trình Callan–Symanzik**. Nhân vật trung tâm của nó là **hàm beta**:

$$
\beta(g) = \mu \frac{\partial g}{\partial \mu},
$$

cho biết hằng số tương tác hiệu dụng $$g(\mu)$$ tăng hay giảm khi ta dò ở năng lượng $$\mu$$ cao hơn (tức khoảng cách ngắn hơn).

Hãy so sánh hai lực cơ bản nổi tiếng nhất để thấy sức mạnh của dấu hàm beta:
- Trong **QED (điện từ học)**, $$\beta(e) > 0$$: các cặp electron–positron ảo trong chân không che chắn điện tích gốc, nên nhìn càng xa thì điện tích hiệu dụng càng nhỏ, còn càng lại gần ($$\mu$$ lớn) thì lực điện càng mạnh.
- Trong **QCD (lý thuyết gauge không giao hoán $$SU(3)$$)**, David Gross, Frank Wilczek và David Politzer (giải Nobel 2004) phát hiện $$\beta(g) < 0$$ khi $$g$$ nhỏ: gluon tự tương tác gây hiệu ứng *phản che chắn*, khiến tương tác mạnh lại **càng yếu đi ở khoảng cách cực ngắn**! Hiện tượng **tính tự do tiệm cận (asymptotic freedom)** này giải thích vì sao các thí nghiệm bắn phá proton ở năng lượng cao lại thấy các quark bên trong gần như bay tự do. Cùng ý tưởng đó giải thích vì sao ta có cơ sở hy vọng xây dựng giới hạn liên tục từ mạng lưới cho Yang–Mills, nhưng nó không tự chứng minh được định lý khe khối lượng của Clay.

---

## 5. Cầu nối với cơ học thống kê và xác suất

Mô hình Ising, lý thuyết thấm (percolation), và mô hình trường vô hướng $$\phi^4$$ là những phòng thí nghiệm nơi các ý tưởng RG đã được chứng minh thành định lý chặt chẽ ở nhiều số chiều (bằng phương pháp nhóm tái chuẩn hóa kiến thiết của Glimm–Jaffe, Gawędzki–Kupiainen, Brydges, Bauerschmidt...). Tại điểm tới hạn (đặc biệt trong 2 chiều), tính bất biến thang đo được nâng cấp thành đối xứng bảo giác toàn cục, mở ra **lý thuyết trường bảo giác (CFT)**. Ở nhánh xác suất hiện đại, giới hạn tỉ lệ của các giao diện ngẫu nhiên trên mạng lưới 2 chiều hội tụ về **quá trình tiến hóa Schramm–Loewner (SLE)** — một thắng lợi toán học trực tiếp mang tinh thần tái chuẩn hóa.

---

## 6. Những gì RG *không* tự động cho ta

- Một định nghĩa kiến thiết đầy đủ cho QCD liên tục 4 chiều.  
- Chứng minh hiện tượng giam hãm màu hay khe khối lượng ([bài toán Clay về Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/)).  
- Quyền bỏ qua dị thường, tô pô, hay các lớp phi nhiễu loạn ([instanton]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/)).  

RG là **một nguyên lý tổ chức và một khung tính toán**. Đôi khi nó được nâng lên thành định lý chặt chẽ (như với mô hình $$\phi^4$$ ở chiều thấp hoặc quanh điểm bất động Gauss), nhưng trong nhiều bài toán biên giới, nó được dùng như một phép tính vật lý có kiểm soát.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Tái chuẩn hóa nghĩa là lý thuyết sai và ta che giấu lỗi." | Gây hiểu nhầm | Đó là mô tả hiệu dụng phụ thuộc thang đo, cùng với việc lấy giới hạn liên tục. |
| "Wilson đã giải quyết xong lý thuyết trường lượng tử." | Nói quá | Ông thay đổi cả khung lý thuyết; nhưng nhiều bài toán dựng lý thuyết vẫn còn mở. |
| "Tự do tiệm cận nghĩa là đã chứng minh khe khối lượng." | Sai | Hai trực giác có liên quan, nhưng là hai mệnh đề toán học khác nhau. |

---

## Tài liệu tham khảo

1. Wilson & Kogut, về RG và khai triển $$\epsilon$$.  
2. Cardy, *Scaling and Renormalization in Statistical Physics* (Tỉ lệ và tái chuẩn hóa trong vật lý thống kê).  
3. Trong khóa học: [Tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).  
