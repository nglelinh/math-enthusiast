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

Nếu bạn khai triển hàm $$f(g) = e^{-1/g^2}$$ thành chuỗi Taylor quanh $$g = 0$$, bạn sẽ nhận được một kết quả trêu ngươi: **mọi đạo hàm ở mọi bậc đều bằng 0**, nên chuỗi Taylor của nó chỉ là $$0 + 0g + 0g^2 + \dots$$ — hoàn toàn mù tịt trước sự tồn tại của chính hàm số đó! Trong lý thuyết trường lượng tử, các giản đồ Feynman đóng vai trò giống hệt chuỗi Taylor theo hằng số tương tác $$g$$: chúng cực kỳ sắc bén cho những dao động nhỏ quanh chân không, nhưng lại hoàn toàn "mù" trước một tầng sâu hơn của tự nhiên — những hiệu ứng phi nhiễu loạn mang cỡ $$e^{-c/g^2}$$ được **tô pô** khóa cứng.

Hai nhân vật chính của tầng sâu ấy là **instanton** (những cấu hình trường mang số nguyên tô pô không thể làm phẳng đi được, tạo ra hiệu ứng đường hầm giữa các chân không) và **dị thường lượng tử (anomaly)** — hiện tượng một đối xứng hoàn hảo của phương trình cổ điển bỗng bị phá vỡ khi ta lượng tử hóa, và kỳ diệu thay, độ lớn của sự phá vỡ ấy lại trùng khớp với **chỉ số tô pô của toán tử Dirac**. Bài trong nhánh Cầu nối này gom ba bài [hình học gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/), [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), và [định lý chỉ số Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) thành một bản đồ chung ở mức ý tưởng, không phải giáo trình lý thuyết trường lượng tử đầy đủ.

---

## Bản đồ kiến thức nền: Tô pô trường chuẩn, Instanton và Lý thuyết chỉ số nghiên cứu những gì?

Với nền tảng toán đại học (giải tích nhiều biến, đại số tuyến tính và phương trình vi phân), ba mảng toán học đứng sau bài này đều có trực giác rất rõ ràng:

### 1. Tô pô của ánh xạ và Lớp đặc trưng (Số vòng quấn & Số Chern)
Hãy hình dung một sợi dây thun buộc kín quanh một cái trụ (đường tròn $$S^1$$): bạn có thể quấn nó 0 vòng, 1 vòng, hay 2 vòng rồi nối hai đầu. Dù kéo giãn thế nào mà không cắt đứt dây, bạn không thể đổi số vòng quấn — đó là một **bất biến tô pô** nhận giá trị nguyên. Trong không–thời gian 4 chiều, các phân thớ trường chuẩn Yang–Mills cũng tự phân chia thành các "ngăn" rời nhau đánh số bằng một số nguyên $$k \in \mathbb{Z}$$ gọi là **số Chern thứ hai** (số instanton), tính qua tích phân độ cong $$\frac{1}{8\pi^2}\int \operatorname{tr}(F\wedge F)$$.

### 2. Giải tích phi nhiễu loạn và Instanton
Trong mỗi ngăn tô pô $$k \neq 0$$, tác dụng năng lượng Yang–Mills có một chặn dưới cứng (chặn Bogomol'nyi) tỉ lệ với $$|k|$$. Cấu hình đạt đúng cực tiểu năng lượng trong ngăn đó gọi là **instanton**. Trong tích phân đường Euclid, instanton đóng vai trò đường hầm lượng tử nối hai chân không khác nhau, sinh ra hiệu ứng cỡ $$e^{-c/g^2}$$ mà khai triển nhiễu loạn quanh một điểm không bao giờ chạm tới.

### 3. Lý thuyết chỉ số Atiyah–Singer và Dị thường lượng tử
Trong đại số tuyến tính hữu hạn chiều, mọi ma trận vuông $$n\times n$$ đều có $$\dim\ker M = \dim\ker M^\dagger$$ (hiệu số luôn bằng 0). Nhưng với **toán tử vi phân elliptic trên không gian vô hạn chiều** (như toán tử Dirac $$D_A$$ ghép với trường gauge $$A$$), hiệu số $$\operatorname{ind} D_A = \dim\ker D_A - \dim\ker D_A^\dagger$$ có thể **khác không** — và định lý Atiyah–Singer chứng minh hiệu số giải tích này bằng đúng một tích phân tô pô (chính là số instanton $$k$$!). Trong vật lý, sự chênh lệch giữa số mode không thuận tay trái và tay phải ấy phá vỡ đối xứng cổ điển ngay trong độ đo tích phân đường — đó chính là **dị thường lượng tử**.

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

(tùy cách chuẩn hóa). Một bất đẳng thức sơ cấp kiểu hằng đẳng thức bình phương (chặn Bogomol'nyi) cho thấy tác dụng Yang–Mills luôn thỏa mãn $$S_E[A] \ge \frac{8\pi^2}{g^2}|k|$$, và dấu bằng xảy ra đúng khi độ cong thỏa điều kiện tự đối ngẫu (hoặc phản tự đối ngẫu) $$F = \pm \star F$$. Những liên thông đạt đúng chặn dưới tô pô của tác dụng ấy được gọi là **instanton** (tên gọi do Gerard 't Hooft đặt vì chúng định xứ cả trong không gian lẫn trong thời gian Euclid — xuất hiện như một "khoảnh khắc" chuyển pha ngắn ngủi).

### Khung giải thích: tự tay tìm một instanton 1 chiều và một chỉ số khác 0 (nên đọc chậm)

Để nắm trọn hai ý tưởng "mẹo bình phương tạo chặn tô pô" và "chỉ số khác 0 ở vô hạn chiều" mà không cần hình học 4 chiều, hãy tự tính hai ví dụ bỏ túi sau:

1. **Instanton 1 chiều trong giếng thế đôi (mẹo Bogomol'nyi):** Xét một hạt trong giếng thế chữ W là $$V(q) = \frac{1}{2}(q^2 - 1)^2$$ (có hai đáy chân không tại $$q = -1$$ và $$q = +1$$). Với mọi đường đi $$q(\tau)$$ nối từ $$q(-\infty) = -1$$ sang $$q(+\infty) = +1$$, ta hoàn thiện bình phương tác dụng Euclid:
   $$
   S_E[q] = \frac{1}{2}\int_{-\infty}^{\infty} \bigl(\dot{q}^2 + (1 - q^2)^2\bigr)\,d\tau = \frac{1}{2}\int_{-\infty}^{\infty} \bigl(\dot{q} - (1 - q^2)\bigr)^2\,d\tau + \int_{-\infty}^{\infty} (1 - q^2)\dot{q}\,d\tau.
   $$
   Số hạng đầu luôn $$\ge 0$$; còn số hạng sau đổi biến $$dq = \dot{q}\,d\tau$$ lập tức cho một **hằng số tô pô** chỉ phụ thuộc hai đầu mút:
   $$
   \int_{-1}^{1} (1 - q^2)\,dq = \Bigl[q - \frac{q^3}{3}\Bigr]_{-1}^{1} = \frac{4}{3}.
   $$
   Vậy $$S_E[q] \ge \frac{4}{3}$$, và dấu bằng xảy ra khi $$\dot{q} = 1 - q^2$$, có nghiệm tường minh $$q(\tau) = \tanh(\tau)$$ — đó chính là **instanton 1 chiều** (kink) nối hai chân không với trọng số xuyên hầm $$e^{-4/(3\hbar)}$$! Trong Yang–Mills 4 chiều, mẹo viết $$\operatorname{tr}(F\wedge\star F) = \frac{1}{2}\operatorname{tr}\bigl((F \mp \star F)\wedge\star(F \mp \star F)\bigr) \pm \operatorname{tr}(F\wedge F)$$ hoạt động *y hệt như vậy*!
2. **Vì sao chỉ số $$\operatorname{ind}(T) = \dim\ker T - \dim\ker T^\dagger$$ có thể khác 0 ở vô hạn chiều?** Trên không gian Hilbert các dãy bình phương khả tổng $$\ell^2(\mathbb{N})$$, xét **toán tử dịch phải**:
   $$
   S(a_0, a_1, a_2, \dots) = (0, a_0, a_1, a_2, \dots).
   $$
   - Tìm $$\ker S$$: $$S(a) = 0 \implies a_0 = a_1 = \dots = 0$$, nên $$\dim\ker S = 0$$.
   - Toán tử liên hợp $$S^\dagger$$ là **toán tử dịch trái**: $$S^\dagger(a_0, a_1, a_2, \dots) = (a_1, a_2, \dots)$$.
   - Tìm $$\ker S^\dagger$$: $$S^\dagger(a) = 0 \iff a_1 = a_2 = \dots = 0$$, còn $$a_0$$ tùy ý! Vậy $$\ker S^\dagger = \operatorname{span}\{(1,0,0,\dots)\}$$ có $$\dim\ker S^\dagger = 1$$.
   - Suy ra $$\operatorname{ind}(S) = 0 - 1 = -1 \neq 0$$! Và nếu bạn thêm bất kỳ nhiễu compact nhỏ nào vào $$S$$, chỉ số $$-1$$ vẫn bất biến — đó chính là tinh thần ổn định tô pô của định lý Atiyah–Singer!

**Trong vật lý.** Trong tích phân đường Euclid, instanton là các điểm yên ngựa phi nhiễu loạn, đóng góp một thừa số dạng $$e^{-8\pi^2/g^2}$$. Chúng mô tả hiệu ứng đường hầm giữa các chân không cổ điển có số vòng quấn khác nhau và sinh ra cấu trúc chân không phụ thuộc vào góc tham số $$\theta$$ (gọi là chân không $$\theta$$).

**Trong toán học.** Không gian moduli các instanton là một đối tượng hình học tuyệt đẹp. Việc nghiên cứu biên và tính compact của nó đòi hỏi định lý nổi bọt của Karen Uhlenbeck ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)) và là nền tảng trực tiếp cho lý thuyết Donaldson phân biệt đa tạp 4 chiều ([Donaldson–Seiberg–Witten]({{ site.baseurl }}/contents/vi/chapter06/06_23_Donaldson_Seiberg_Witten/)).

---

## 2. Vì sao tô pô không thấy được ở từng bậc

Lý thuyết nhiễu loạn khai triển quanh một chân không duy nhất theo chuỗi lũy thừa của hằng số tương tác $$g$$. Hãy hình dung bạn đang đứng trong một thung lũng của dãy núi và chỉ đo độ cong mặt đất ngay dưới chân mình bằng khai triển Taylor: dù bạn tính đạo hàm tới bậc thứ một trăm, bạn vẫn không thể biết bên kia dãy núi còn có một thung lũng giống hệt và một đường hầm nối sang đó! Việc chuyển giữa các lớp tô pô và nhiều hiệu ứng toàn cục khác là **phi nhiễu loạn**: chúng nằm trong các thừa số dạng $$e^{-c/g^2}$$, nhỏ hơn bất kỳ lũy thừa dương nào $$g^n$$ khi $$g \to 0^+$$.

**Cơ chế chính.** Tô pô chia không gian các cấu hình trường thành các thành phần liên thông rời nhau (các lớp đánh số bởi $$k \in \mathbb{Z}$$). Biên độ lượng tử là tổng trên tất cả các lớp này, với những trọng số dạng $$e^{ik\theta} e^{-8\pi^2|k|/g^2}$$ mà chuỗi lũy thừa quanh một điểm không bao giờ nhìn thấy được.

---

## 3. Dị thường: khi đối xứng cổ điển bị phá vỡ ở mức lượng tử

**Một đối xứng của tác dụng cổ điển** $$S[\phi]$$ không nhất thiết còn tồn tại sau khi lượng tử hóa: trong tích phân đường $$\int \mathcal{D}\phi\, e^{iS[\phi]/\hbar}$$, ngay cả khi $$S[\phi]$$ bất biến dưới một phép biến đổi, thì chính "độ đo" $$\mathcal{D}\phi$$ (hay quy trình chính quy hóa các vòng lượng tử) vẫn có thể biến đổi! Cần phân biệt hai hệ quả rất khác nhau: **dị thường gauge** (phá vỡ đối xứng địa phương vốn dùng để loại bỏ các trạng thái phi vật lý) làm lý thuyết mất tính nhất quán và buộc phải triệt tiêu hoàn toàn — thực tế, yêu cầu triệt tiêu dị thường gauge trong Mô hình chuẩn khớp một cách kỳ diệu giữa điện tích của quark và lepton! Ngược lại, **dị thường toàn cục** và **dị thường chiral** hoàn toàn hợp lệ và là hiện tượng vật lý thật, đo được.

Ví dụ nổi tiếng nhất là **dị thường chiral (Adler–Bell–Jackiw, ABJ)**: Lagrangian cổ điển của fermion không khối lượng có đối xứng quay pha riêng biệt cho hạt thuận tay trái và tay phải, nhưng ở mức lượng tử dòng axial không còn bảo toàn. Chính dị thường này giải thích tốc độ phân rã thực nghiệm của hạt pion trung hòa thành hai photon ($$\pi^0 \to \gamma\gamma$$) — một chiến thắng lừng lẫy của lý thuyết trường lượng tử. Giản đồ tam giác trong lý thuyết nhiễu loạn phát hiện ra hiện tượng này bằng phép tính trực tiếp; còn hình học hiện đại hiểu cùng một vật cản đó qua các lớp đặc trưng tô pô.

**Liên hệ với chỉ số.** Với toán tử Dirac $$D_A$$ ghép với trường gauge nền $$A$$, chỉ số giải tích

$$
\operatorname{ind} D_A = \dim\ker D_A - \dim\ker D_A^\dagger
$$

bằng đúng chỉ số tô pô (định lý Atiyah–Singer). Trong ngôn ngữ vật lý: $$\ker D_A$$ đếm số mode không (zero mode) thuận tay trái, $$\ker D_A^\dagger$$ đếm số mode không thuận tay phải; sự chênh lệch $$n_L - n_R$$ bị khóa cứng bằng số instanton $$k$$. Điều đó giải thích trực tiếp hệ số của dị thường chiral và sinh ra các quy tắc chọn bất ngờ cho hàm tương quan trong nền instanton (đỉnh tương tác 't Hooft).

Bài học rút ra:

> **Đếm mode không không phải là chuyện tình cờ, mà là lý thuyết chỉ số gặp lý thuyết trường lượng tử.**

---

## 4. Bài toán $$U(1)$$ và instanton (mức đọc hiểu)

Trong sắc động lực học lượng tử (QCD), vì khối lượng các quark nhẹ ($$u, d, s$$) rất nhỏ, nếu áp dụng định lý Goldstone cho đối xứng chiral một cách ngây thơ, lý thuyết sẽ dự đoán phải có chín hạt meson nhẹ (gồm pion, kaon, $$\eta$$ và một hạt thứ chín nhẹ cỡ pion). Nhưng thực nghiệm chỉ thấy tám hạt nhẹ, còn hạt thứ chín ($$\eta'$$) lại nặng hơn nhiều! Lời giải (gắn với tên tuổi 't Hooft, Witten và Veneziano) liên quan mật thiết đến bản chất dị thường của đối xứng $$U(1)$$ axial đơn tuyến và cấu trúc tô pô của chân không gauge có instanton. Bài giảng *"The uses of instantons"* (Các ứng dụng của instanton) của Sidney Coleman là tài liệu vật lý kinh điển về chủ đề này; còn nền tảng toán học của việc đếm mode không chính là lý thuyết chỉ số.

**Cần thận trọng.** Những câu như "instanton giải thích toàn bộ khối lượng proton" là nói quá; câu chuyện khối lượng hadron có nhiều tầng phối hợp (giam hãm màu, phá vỡ đối xứng chiral tự phát, tính toán QCD trên mạng lưới, và lý thuyết trường hiệu dụng).

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

## Tài liệu tham khảo

1. Coleman, "The uses of instantons" (Các ứng dụng của instanton).  
2. Nakahara, sách tô pô cho nhà vật lý (*Geometry, Topology and Physics*).  
3. Các liên kết trong khóa học ở trên.  
