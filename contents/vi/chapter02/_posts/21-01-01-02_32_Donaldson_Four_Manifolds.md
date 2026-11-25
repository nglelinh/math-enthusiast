---
layout: post
title: "Đa tạp bốn chiều và cấu trúc trơn ngoại lai của Donaldson (Huy chương Fields 1986)"
chapter: '02'
order: 32
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử hỏi một câu tưởng chừng đơn giản trong giải tích nhiều biến: có bao nhiêu cách để định nghĩa phép lấy đạo hàm trên không gian Euclid $$\mathbb{R}^n$$? Nếu $$n = 1, 2, 3$$, câu trả lời là **duy nhất một cách**. Nếu $$n = 5, 6, 7, \ldots, 100$$, câu trả lời vẫn là **duy nhất một cách**! Ấy vậy mà vào mùa xuân năm 1982, một nghiên cứu sinh 24 tuổi ở Oxford tên **Simon Donaldson** — dùng phương trình **Yang–Mills** từ vật lý hạt cơ bản — đã làm chấn động giới toán học bằng một cú va chạm lịch sử: **riêng không gian Euclid bốn chiều $$\mathbb{R}^4$$ lại có vô hạn (thậm chí không đếm được!) những "cấu trúc vi phân lạ" (exotic $$\mathbb{R}^4$$)** — những không gian hoàn toàn giống $$\mathbb{R}^4$$ về mặt tôpô liên tục nhưng *không thể nào* chuyển đổi trơn mượt sang $$\mathbb{R}^4$$ quen thuộc!

Tại ICM Berkeley năm 1986, **Simon Donaldson** nhận **Huy chương Fields**:

> primarily for his work on the topology of four-manifolds, especially for showing that there is a differential structure on Euclidean four-space which is different from the usual structure.  
> — [IMU, Fields Medals 1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)

*Tạm dịch: chủ yếu vì công trình về tôpô của các đa tạp bốn chiều, đặc biệt là việc chỉ ra rằng có một cấu trúc vi phân trên không gian Euclid bốn chiều khác với cấu trúc thông thường.*

Để hiểu đúng kỳ tích năm 1986, cần đặt **ba mảnh ghép** cạnh nhau: (1) định lý phân loại tôpô đa tạp 4 chiều đơn liên của **Michael Freedman** (1982, cùng nhận Huy chương Fields tại ICM Berkeley 1986); (2) nền tảng giải tích về tính compact và "sủi bọt" của **Karen Uhlenbeck** (xem [Uhlenbeck / lý thuyết gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)); và (3) định lý ràng buộc trơn chấn động của **Donaldson** (1983) từ không gian moduli instanton. Chính sự **va chạm trực diện** giữa sự tự do của thế giới tôpô (Freedman) và sự cứng rắn của thế giới trơn (Donaldson) đã đẻ ra những đa tạp 4 chiều không có cấu trúc trơn và các $$\mathbb{R}^4$$ lạ! Còn **lý thuyết Seiberg–Witten** (Witten, 1994) là cuộc cách mạng gauge đến sau 8 năm (xem bối cảnh [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/)), và bài toán phân loại mọi đa tạp 4 chiều trơn đến nay vẫn còn mở.

**Mạch bài học:** Kiến thức cần nhớ (tôpô vs. trơn ở chiều 4, dạng giao $$Q_X$$, phương trình tự đối ngẫu Yang–Mills) → Ví dụ ma trận làm từng bước: dạng giao của $$\mathbb{CP}^2$$, $$S^2 \times S^2$$ và ma trận $$8\times 8$$ của lưới $$E_8$$ → Cú va chạm Freedman (1982) + Donaldson (1983) → Giải thích: 4 bước dùng không gian moduli instanton 5 chiều để khóa chặt dạng giao $$Q_X$$ → Seiberg–Witten (1994) và những phát triển sau.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao **chiều bốn** là số chiều dị biệt nhất trong tôpô (mẹo Whitney thất bại trong phạm trù trơn vì $$2 + 2 = 4$$, nhưng vẫn vá được trong phạm trù tôpô bằng tay cầm Casson).
- Tự viết ma trận **dạng giao** $$Q_X$$ cho $$\mathbb{CP}^2$$, $$S^2 \times S^2$$ và lưới $$E_8$$, và hiểu vì sao $$E_8$$ là dạng xác định dương unimodular *không* chéo hóa được trên $$\mathbb{Z}$$.
- Phát biểu **định lý Donaldson (1983)** (dạng giao xác định của đa tạp 4 chiều trơn đóng phải chéo hóa được trên $$\mathbb{Z}$$) đối chiếu với **định lý Freedman (1982)** (mọi dạng unimodular đều thực hiện được bằng đa tạp tôpô đơn liên).
- Giải thích vì sao sự va chạm **Freedman + Donaldson** lập tức tạo ra (i) đa tạp 4 chiều tôpô không có cấu trúc trơn và (ii) các **$$\mathbb{R}^4$$ lạ**.
- Mô tả vai trò của không gian moduli **instanton** ($$F_A^+ = 0$$) cùng nền tảng giải tích của **Uhlenbeck** (sủi bọt tạo biên).
- Tách bạch **Seiberg–Witten (1994)** khỏi Huy chương Fields 1986 và tránh tuyên bố rằng Donaldson đã phân loại mọi đa tạp 4 chiều.

**Kiến thức nền.** Đa tạp trơn, đồng điều và tích cup ở mức giáo trình tôpô đại số nhập môn; khái niệm phân thớ vectơ và liên thông. Không cần học trước lý thuyết gauge: có thể hiểu liên thông là một cách lấy đạo hàm các nhát cắt, và độ cong đo mức độ các đạo hàm riêng hỗn hợp không giao hoán.

**Liên kết với các bài khác.** Bài này cho thấy phương trình đạo hàm riêng có nguồn gốc vật lý trở thành công cụ tôpô, và sự khác nhau giữa phạm trù tôpô với phạm trù trơn. Đọc cùng [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) (cách tiếp cận giải tích – hình học cho đa tạp ba chiều về sau), và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Kiến thức cần nhớ: Tôpô 4 chiều, Dạng giao và Lý thuyết trường chuẩn là gì?

### 1. Tôpô vs. Trơn — và tại sao chiều 4 lại dị biệt?
Một **đa tạp tôpô** chỉ cần các phép biến đổi liên tục (đồng phôi — nặn đất sét có góc nhọn); một **đa tạp trơn** đòi hỏi hệ tọa độ khả vi nhất quán ở mọi nơi (vi phôi).
- Ở chiều $$n \ge 5$$, **mẹo Whitney** có đủ chỗ trống để kéo trượt triệt tiêu các cặp điểm giao ngược dấu của hai đĩa, tạo ra lý thuyết phẫu thuật phân loại đa tạp.
- Ở chiều $$n \le 3$$, cắt dán và hình học hóa Thurston–Perelman kiểm soát hoàn toàn.
- Ở **chiều $$n = 4$$**, hai đĩa 2 chiều cắt nhau tại các điểm rời rạc ($$2 + 2 = 4$$), nên kéo trượt để xóa điểm giao cũ lại sinh ra điểm giao mới! Trong phạm trù tôpô, ta đẩy vô hạn các điểm giao mới thành **tay cầm Casson** (vẫn đồng phôi với tay cầm chuẩn); trong phạm trù trơn, tay cầm đó gãy gập hoàn toàn!

### 2. Dạng giao $$Q_X$$ — "ma trận vân tay" của đa tạp 4 chiều
Trong đa tạp 4 chiều đóng, định hướng $$X$$, hai mặt 2 chiều tổng quát cắt nhau tại hữu hạn điểm. Đếm tổng số giao có dấu giữa các lớp trong $$H_2(X; \mathbb{Z})/\mathrm{torsion}$$ cho ta một ma trận nguyên đối xứng có định thức $$\pm 1$$ (unimodular):

$$
Q_X: H_2(X;\mathbb{Z})/\mathrm{torsion}\times H_2(X;\mathbb{Z})/\mathrm{torsion}\to\mathbb{Z}.
$$

### 3. Phương trình Yang–Mills phản tự đối ngẫu (ASD) & Instanton
Trên đa tạp 4 chiều trơn $$X$$ với phân thớ chính $$\mathrm{SU}(2)$$, toán tử sao Hodge $$\star$$ biến 2-dạng thành 2-dạng với $$\star^2 = 1$$ — một phép đối xứng **độc quyền của chiều 4**! Nhờ đó độ cong $$F_A$$ tách làm hai phần $$F_A = F_A^+ + F_A^-$$. Các liên thông cực tiểu hóa năng lượng Yang–Mills $$\mathrm{YM}(A) = \int_X \lvert F_A\rvert^2$$ thỏa phương trình đạo hàm riêng cấp một **$$F_A^+ = 0$$**, gọi là các **instanton**.

---

## 1. Ví dụ ma trận làm từng bước: $$\mathbb{CP}^2$$, $$S^2 \times S^2$$ và lưới $$E_8$$

Hãy viết tường minh ma trận dạng giao $$Q_X$$ của ba ví dụ kinh điển để thấy ngay bản chất của định lý Donaldson:

1. **Mặt phẳng xạ ảnh phức $$\mathbb{CP}^2$$ (chiều thực 4):** $$H_2(\mathbb{CP}^2; \mathbb{Z}) \cong \mathbb{Z}$$ sinh bởi một đường thẳng phức $$\mathbb{CP}^1$$. Hai đường thẳng phức khác nhau luôn cắt nhau tại đúng $$1$$ điểm có dấu dương, nên ma trận dạng giao là:
   $$
   Q_{\mathbb{CP}^2} = \begin{pmatrix} 1 \end{pmatrix}.
   $$
   Đây là dạng **xác định dương**, **lẻ** và **đã chéo hóa**!

2. **Tích hai mặt cầu $$S^2 \times S^2$$:** $$H_2(S^2 \times S^2; \mathbb{Z}) \cong \mathbb{Z}^2$$ sinh bởi hai mặt cầu $$A = S^2 \times \{p\}$$ và $$B = \{q\} \times S^2$$. Ta có $$A \cdot A = 0$$ (dịch song song không cắt nhau), $$B \cdot B = 0$$, còn $$A \cdot B = 1$$ (cắt tại đúng điểm $$(q,p)$$), nên ma trận dạng giao là:
   $$
   Q_{S^2 \times S^2} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
   $$
   Đây là dạng **chẵn** nhưng **không xác định dấu** (một trị riêng $$+1$$, một trị riêng $$-1$$).

3. **Ma trận $$E_8$$ (cỡ $$8\times 8$$):** Trong lý thuyết số, ma trận Cartan của hệ nghiệm $$E_8$$ là:
   $$
   E_8 = \begin{pmatrix}
   2 & -1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   -1 & 2 & -1 & 0 & 0 & 0 & 0 & 0 \\
   0 & -1 & 2 & -1 & 0 & 0 & 0 & 0 \\
   0 & 0 & -1 & 2 & -1 & 0 & 0 & 0 \\
   0 & 0 & 0 & -1 & 2 & -1 & 0 & -1 \\
   0 & 0 & 0 & 0 & -1 & 2 & -1 & 0 \\
   0 & 0 & 0 & 0 & 0 & -1 & 2 & 0 \\
   0 & 0 & 0 & 0 & -1 & 0 & 0 & 2
   \end{pmatrix}.
   $$
   Hãy kiểm tra bằng mắt ba tính chất cực kỳ đặc biệt của $$E_8$$:
   - Mọi phần tử trên đường chéo đều là **$$2$$** (chẵn), nên với *mọi* vector nguyên $$v \in \mathbb{Z}^8$$, giá trị $$v^T E_8 v$$ luôn là **số chẵn** — **không bao giờ bằng $$1$$**!
   - Định thức $$\det(E_8) = 1$$ (unimodular) và tất cả các định thức con chính đều dương (**xác định dương**)!
   - Vì không tồn tại vector nguyên nào có $$v^T E_8 v = 1$$, ma trận $$E_8$$ **không thể nào chéo hóa trên $$\mathbb{Z}$$** về ma trận đơn vị $$I_8$$!

Bây giờ hãy đặt hai định lý 1982–1983 cạnh ma trận $$E_8$$ này:
- **Freedman (1982):** *Mọi* ma trận unimodular đều là dạng giao của một đa tạp 4 chiều **tôpô** đóng, đơn liên $$\implies$$ **tồn tại đa tạp 4 chiều tôpô $$M_{E_8}$$ có dạng giao đúng bằng $$E_8$$!** (Và kéo theo giả thuyết Poincaré 4 chiều **tôpô** là đúng.)
- **Donaldson (1983):** Dạng giao xác định của mọi đa tạp 4 chiều **trơn** đóng, định hướng đều **chéo hóa được trên $$\mathbb{Z}$$** (về $$\pm I_n$$) $$\implies$$ **đa tạp tôpô $$M_{E_8}$$ hoàn toàn không thể có bất kỳ cấu trúc trơn nào!**

Và khi đặt chính sự va chạm đó vào phần "đầu mở" của mặt K3 trơn (vốn có dạng giao $$2(-E_8) \oplus 3H$$) bằng kỹ thuật vá tôpô của Freedman, ta sinh ra một đa tạp mở **đồng phôi với $$\mathbb{R}^4$$** nhưng chứa một tập compact không bao giờ nhốt được bên trong bất kỳ mặt cầu $$S^3$$ nhúng trơn nào — tức là một **$$\mathbb{R}^4$$ lạ (exotic $$\mathbb{R}^4$$)**! (Ngay năm 1983, Robert Gompf chỉ ra 3 $$\mathbb{R}^4$$ lạ tường minh; về sau Gompf và Taubes chứng minh có **không đếm được** các $$\mathbb{R}^4$$ lạ đôi một không vi phôi!)

---

## 2. Giải thích: Làm sao phương trình Yang–Mills ép dạng giao phải chéo hóa?

Tại sao một phương trình PDE vật lý hạt cơ bản ($$F_A^+ = 0$$) lại đọc được một ma trận nguyên trên $$H_2(X; \mathbb{Z})$$? Hãy theo dõi 4 bước kỳ diệu trong chứng minh năm 1983 của Donaldson:

#### Bước 1: Dựng không gian moduli instanton $$\mathcal{M}$$ — một đa tạp 5 chiều
Cho đa tạp 4 chiều trơn, đóng, đơn liên $$X$$ có dạng giao xác định dương. Trên phân thớ chính $$\mathrm{SU}(2)$$ có số instanton $$k = 1$$, xét không gian moduli $$\mathcal{M}$$ của tất cả các nghiệm phương trình $$F_A^+ = 0$$ chia cho nhóm biến đổi gauge. Theo định lý chỉ số Atiyah–Singer, $$\mathcal{M}$$ là một **đa tạp 5 chiều** trơn ở hầu khắp nơi!

#### Bước 2: Đếm các điểm kỳ dị bên trong $$\mathcal{M}$$ — dấu vết của dạng giao $$Q_X$$
Những chỗ duy nhất $$\mathcal{M}$$ bị mất tính trơn (kỳ dị) là các **liên thông khả quy** (nhóm đối xứng thu gọn từ $$\mathrm{SU}(2)$$ về $$\mathrm{U}(1)$$). Hóa ra số điểm kỳ dị đó tương ứng **1–1** với số cặp lớp $$\pm\alpha \in H_2(X;\mathbb{Z})$$ thỏa mãn $$\alpha \cdot \alpha = 1$$! Và lân cận của mỗi điểm kỳ dị trong không gian 5 chiều $$\mathcal{M}$$ có hình dáng chính xác là một **hình nón trên $$\mathbb{CP}^2$$**!

#### Bước 3: Hiện tượng "sủi bọt" (Uhlenbeck) tạo ra biên của $$\mathcal{M}$$ là chính $$X$$!
Không gian 5 chiều $$\mathcal{M}$$ không compact vì một instanton có thể co năng lượng dồn hết về **một điểm duy nhất** $$x \in X$$ với bán kính tiến về $$0$$ (hiện tượng **sủi bọt**, *bubbling* — giống hệt không gian moduli instanton trên $$S^4$$ là quả cầu đặc 5 chiều có biên là chính $$S^4$$). Nhờ **định lý compact của Karen Uhlenbeck** và **định lý kỳ dị khử được** (xem [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)), Donaldson chứng minh sủi bọt tại điểm là kiểu suy biến duy nhất có thể xảy ra: khi bổ sung các instanton sủi bọt đó vào, phần biên ở vô cực của $$\mathcal{M}$$ chính là một bản sao nguyên vẹn của đa tạp **$$X$$**!

#### Bước 4: Cắt bỏ đỉnh nón $$\implies$$ cobordism 5 chiều khóa chặt dạng giao $$Q_X$$
Cắt bỏ một lân cận nhỏ quanh từng điểm kỳ dị nón (lộ ra $$m$$ bản sao biên là $$\pm\mathbb{CP}^2$$), không gian 5 chiều $$\overline{\mathcal{M}}$$ trở thành một **cobordism 5 chiều** nối liền đa tạp $$X$$ với tổng rời của $$m$$ bản sao $$\pm\mathbb{CP}^2$$!
Vì chỉ số (signature) là bất biến qua cobordism và $$Q_X$$ xác định dương (chỉ số bằng hạng $$b_2$$), ta lập tức có $$m \ge b_2$$ — nghĩa là tồn tại ít nhất $$b_2$$ lớp độc lập có tự giao $$\alpha_i \cdot \alpha_i = 1$$! Một bài toán đại số tuyến tính ngắn gọn lập tức ép dạng giao $$Q_X$$ phải **chéo hóa hoàn toàn về ma trận đơn vị $$I_{b_2}$$**!

Tóm tắt cầu nối chấn động của Donaldson:

$$
\text{Đa tạp trơn 4D } X
\;\xrightarrow{F_A^+ = 0}\;
\text{Moduli 5D } \mathcal{M}
\;\xrightarrow{\text{Sủi bọt (Uhlenbeck)}}\;
\text{Cobordism: } X \sim \bigsqcup \pm\mathbb{CP}^2
\;\Longrightarrow\;
Q_X \cong I_{b_2}.
$$

*(Về sau, năm 1990, Donaldson khai thác tiếp không gian moduli instanton bậc cao để tạo ra **đa thức Donaldson**, phân biệt được vô số cấu trúc trơn khác nhau trên cùng một đa tạp 4 chiều tôpô đóng.)*

---

## 3. Những phát triển về sau và vì sao là Huy chương Fields 1986

- **Lý thuyết Seiberg–Witten (1994):** Tám năm sau huy chương của Donaldson, **Edward Witten** giới thiệu phương trình monopole Seiberg–Witten (nhóm gauge giao hoán $$\mathrm{U}(1)$$ thay vì $$\mathrm{SU}(2)$$), có không gian moduli tự động compact (không cần sủi bọt!) và dễ tính toán hơn nhiều, tái chứng minh ngắn gọn định lý Donaldson và mở ra hàng loạt định lý mới. Đây là bước kế thừa năm 1994, không thuộc huy chương 1986.
- **Các chương sau của Donaldson:** Định lý Donaldson–Uhlenbeck–Yau về metric Hermite–Einstein, chùm Lefschetz symplectic, và định lý Chen–Donaldson–Sun về metric Kähler–Einstein trên đa tạp Fano.

**Vì sao là Huy chương Fields 1986:** Không ai từng ngờ phương trình Yang–Mills của vật lý hạt lại có thể đọc thấu tôpô trơn của không gian 4 chiều, đập vỡ hoàn toàn sự đồng nhất giữa tôpô và vi phân bằng sự ra đời của đa tạp không làm trơn được và các $$\mathbb{R}^4$$ lạ. Tại ICM Berkeley 1986, ba tấm Huy chương Fields thuộc về **Simon Donaldson**, **Michael Freedman** và **Gerd Faltings**.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Donaldson phân loại mọi đa tạp bốn chiều." | Ông chứng minh các ràng buộc nền tảng và đưa ra các bất biến về sau. Phân loại trong phạm trù trơn vẫn còn mở. |
| "Một mình Donaldson xây dựng $$\mathbb{R}^4$$ lạ." | Sự tồn tại dùng **ràng buộc trơn của Donaldson** cùng **lý thuyết tôpô của Freedman** (và các xây dựng sớm của Gompf và những người khác). |
| "Giả thuyết Poincaré của Freedman là phiên bản trơn." | Freedman chứng minh giả thuyết Poincaré bốn chiều **tôpô**. Giả thuyết Poincaré bốn chiều trơn vẫn còn mở. |
| "Seiberg–Witten thuộc huy chương 1986." | Các bất biến Seiberg–Witten xuất hiện năm **1994**. |
| "Định lý compact của Uhlenbeck là một định lý tôpô." | Đó là định lý **giải tích** về tính compact và kỳ dị khử được, rồi được dùng cho tôpô. |
| "$$\mathbb{R}^4$$ lạ mâu thuẫn với tính duy nhất của $$\mathbb{R}^n$$ khi $$n\neq 4$$." | Với $$n\neq 4$$, không gian Euclid có cấu trúc trơn duy nhất; chiều bốn là ngoại lệ. |

---

## Liên kết

- IMU Fields Medals 1986: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)
- Wikipedia: [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson); [Exotic $$\mathbb{R}^4$$](https://en.wikipedia.org/wiki/Exotic_R4); [Donaldson’s theorem](https://en.wikipedia.org/wiki/Donaldson%27s_theorem)
- Khóa học: [Uhlenbeck / gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)
- Tìm arXiv (công trình Donaldson sau; các bài 1983 trước arXiv): [Donaldson four-manifold](https://arxiv.org/search/?query=Donaldson+four-manifold+instanton&searchtype=all)

---

## Tài liệu tham khảo

1. International Mathematical Union, tường thuật Fields Medals 1986 về Simon K. Donaldson (trang Albers–Alexanderson–Reid / IMU).
2. **S. K. Donaldson**, “An application of gauge theory to four-dimensional topology,” *J. Differential Geom.* 18 (1983), 279–315.
3. **M. H. Freedman**, “The topology of four-dimensional manifolds,” *J. Differential Geom.* 17 (1982), 357–453.
4. **R. Gompf**, “Three exotic $$\mathbf{R}^4$$’s and other anomalies,” *J. Differential Geom.* 18 (1983), 317–328.
5. **S. K. Donaldson and P. B. Kronheimer**, *The Geometry of Four-Manifolds*, Oxford, 1990.
6. **D. S. Freed and K. K. Uhlenbeck**, *Instantons and Four-Manifolds*, Springer, 1984; bài khóa học [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/).
7. **E. Witten**, “Monopoles and four-manifolds,” *Math. Res. Lett.* 1 (1994), 769–796. (Hậu duệ, không phải huy chương 1986.)
8. Wikipedia, [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson), [Exotic R4](https://en.wikipedia.org/wiki/Exotic_R4).

---

## Hướng đi tiếp

- Đọc bài giới thiệu của Atiyah tại ICM 1986, rồi Chương 1 sách Donaldson–Kronheimer. Sau khi đọc bài Uhlenbeck, ghi lại vì sao hiện tượng sủi bọt là một tính năng chứ không phải lỗi (nó sinh ra $$\partial\mathcal{M}$$).
- Câu hỏi thảo luận: để phân loại các đa tạp bốn chiều trơn đơn liên, ngoài dạng giao ta còn cần gì?

## Video tham khảo

- **Xem trước**: [Simon Donaldson, Invariants of manifolds and the classification problem](https://www.youtube.com/watch?v=IO0HNEs8oxQ) (Clay Mathematics Institute, tiếng Anh). Donaldson nói về các bất biến của đa tạp và bài toán phân loại. Nên xem trước để hiểu vì sao chiều bốn đặc biệt.
- [The Shaw Prize Lecture in Mathematical Sciences 2009 - by Professor Simon K Donaldson](https://www.youtube.com/watch?v=5yhxUCtNRQE) (The Shaw Prize, tiếng Anh). Bài giảng của Donaldson khi nhận Giải Shaw 2009. Xem sau khi đọc xong mục 3 và 4.
- [Overview of gauge theory and submanifold geometry on G_2 manifolds - Simon Donaldson (2014)](https://www.youtube.com/watch?v=xIqLhsrgcBI) (Graduate Mathematics, tiếng Anh). Bài giảng tổng quan về lý thuyết gauge và đa tạp con trên đa tạp G_2, một hướng nghiên cứu về sau của Donaldson. Dùng làm góc nhìn bổ sung, không thuộc huy chương 1986.
