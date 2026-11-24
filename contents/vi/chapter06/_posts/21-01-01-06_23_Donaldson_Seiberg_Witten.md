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

Năm 1982, khi vẫn còn là nghiên cứu sinh năm hai ở Oxford, Simon Donaldson công bố một kết quả làm rung chuyển cả giới tô pô học: ông không dùng các công cụ cắt dán đa tạp truyền thống, mà mượn thẳng **phương trình Yang–Mills phản tự đối ngẫu** từ lý thuyết hạt cơ bản để chứng minh những định lý hoàn toàn mới về hình học của **đa tạp trơn 4 chiều**. Kết hợp với định lý phân loại tô pô của Michael Freedman vừa ra mắt cùng năm, kết quả của Donaldson lập tức kéo theo một cú sốc khó tin: ngay cả không gian Euclid quen thuộc $$\mathbb{R}^4$$ cũng tồn tại **vô số cấu trúc trơn "kỳ lạ" (exotic $$\mathbb{R}^4$$)** — cùng hình dáng tô pô liên tục, nhưng mãi mãi không thể biến đổi khả vi trơn thành $$\mathbb{R}^4$$ chuẩn! Mười hai năm sau, một cú xoay ngoạn mục thứ hai xuất hiện: lý thuyết **Seiberg–Witten**, lấy cảm hứng từ đối ngẫu siêu đối xứng trong vật lý trường lượng tử, đưa ra một hệ phương trình gọn nhẹ hơn hẳn nhưng mạnh mẽ tương đương, làm thay đổi hoàn toàn cách làm việc hằng ngày của tô pô 4 chiều.

Đây là một trục đẹp nhất trong nhánh Cầu nối Vật lý–Toán: **hình học lấy cảm hứng từ vật lý quay ngược lại giải quyết những câu hỏi cốt lõi của toán học thuần túy**, chứ không chỉ toán học phục vụ vật lý. Nên đọc sau các bài [lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/) và [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/); đọc kèm bài [instanton]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/).

---

## Bản đồ kiến thức nền: Tô pô vi phân 4 chiều và Lý thuyết Donaldson–Seiberg–Witten nghiên cứu những gì?

Với nền tảng đại số tuyến tính (dạng toàn phương, ma trận đối xứng) và giải tích nhiều biến (hàm khả vi trơn $$C^\infty$$), bạn có thể hiểu trọn vẹn ba trụ cột làm nên cuộc cách mạng tô pô 4 chiều:

### 1. Đồng phôi (tô pô liên tục) vs. Vi phôi (tô pô trơn)
Ở chiều 1, 2 và 3, nếu hai không gian có thể kéo giãn liên tục thành nhau (đồng phôi — *homeomorphic*), thì ta luôn có thể làm mượt phép biến đổi đó thành khả vi trơn (vi phôi — *diffeomorphic*). Chẳng hạn trên $$\mathbb{R}^3$$ chỉ có duy nhất một cách làm giải tích vi phân. Nhưng **chiều 4** là chiều duy nhất mà hai thế giới này tách rời nhau sâu sắc: có những đa tạp tô pô 4 chiều **không mang nổi dù chỉ một cấu trúc trơn**, và có những đa tạp (như chính $$\mathbb{R}^4$$!) mang **vô hạn không đếm được** cấu trúc trơn đôi một không vi phôi!

### 2. Dạng giao (Intersection Form) — "dấu vân tay ma trận" của đa tạp 4 chiều
Trong không gian 4 chiều, hai mặt cong 2 chiều tổng quát cắt nhau tại **các điểm rời rạc** (vì $$2 + 2 = 4$$). Đếm số điểm giao có dấu giữa các mặt 2 chiều cơ bản bên trong đa tạp 4 chiều $$X$$ cho ta một ma trận đối xứng với hệ số nguyên gọi là **dạng giao $$Q_X$$** (với $$\det Q_X = \pm 1$$ khi $$X$$ đóng, đơn liên). **Định lý Freedman (1982)** chứng minh rằng về mặt *tô pô liên tục*, dạng giao $$Q_X$$ gần như phân loại trọn vẹn mọi đa tạp 4 chiều đơn liên!

### 3. Phương trình gauge như chiếc "kính hiển vi trơn"
Vì các công cụ tô pô đại số cổ điển chỉ nhìn thấy phần liên tục, chúng mù tịt trước cấu trúc trơn. Ý tưởng thiên tài của **Donaldson** (1983) và **Seiberg–Witten** (1994) là đặt lên $$X$$ một **phương trình đạo hàm riêng phi tuyến** vốn đòi hỏi phép lấy đạo hàm trơn, rồi trích ra những con số bất biến từ **không gian nghiệm (moduli)** của nó — giống như gõ vào hai chiếc chuông giống hệt hình dáng bên ngoài để nghe ra cấu trúc kim loại khác nhau bên trong!

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

Ở số chiều $$\geq 5$$, không gian đủ rộng để tách các mặt 2 chiều giao nhau ra khỏi nhau (bổ đề Whitney), nên lý thuyết phẫu thuật (surgery) giúp tổ chức phần lớn tô pô một cách có hệ thống. Ở chiều 3, cấu trúc hình học rất chặt chẽ và được định lý hình học hóa (Perelman) phân loại trọn vẹn. Còn **4 chiều** kẹt đúng ở giữa: hai mặt 2 chiều cắt nhau tại các điểm cô lập và không đủ chiều dư để gỡ chúng ra một cách trơn tru! Hệ quả là có vô số **cấu trúc trơn kỳ lạ** (exotic) xuất hiện trên các đa tạp tô pô 4 chiều — riêng $$\mathbb{R}^4$$ là không gian Euclid duy nhất trong mọi số chiều $$\mathbb{R}^n$$ sở hữu cấu trúc trơn kỳ lạ (thực tế là không đếm được!).

Cũng chính khoảng cách giữa *trơn* và *tô pô* này làm cho câu hỏi **một nút có là nút lát (slice) hay không** trở nên cực kỳ tinh tế: một nút trong $$S^3$$ có thể là biên của một đĩa tô pô phẳng cục bộ trong quả cầu 4 chiều $$B^4$$, nhưng lại không bao giờ là biên của bất kỳ đĩa *trơn* nào. Xem câu chuyện nổi tiếng này trong bài [Piccirillo và nút Conway]({{ site.baseurl }}/contents/vi/chapter06/06_28_Piccirillo_Conway_Knot/).

### Khung giải thích: tự tay kiểm tra cú sốc giữa Freedman và Donaldson qua dạng giao $$E_8$$ (nên đọc chậm)

Để thấy sức mạnh của định lý Donaldson chỉ bằng đại số tuyến tính năm nhất, hãy xem ví dụ kinh điển nhất lịch sử tô pô 4 chiều:

1. **Dạng giao của hai đa tạp quen thuộc:**
   - Trên mặt phẳng xạ ảnh phức $$\mathbb{CP}^2$$ (là đa tạp thực 4 chiều), hai đường thẳng phức bất kỳ cắt nhau tại đúng $$1$$ điểm, nên dạng giao là ma trận $$1\times 1$$: $$Q_{\mathbb{CP}^2} = (1)$$.
   - Trên tích hai mặt cầu $$S^2 \times S^2$$, hai mặt cầu cơ bản $$S^2 \times \{p\}$$ và $$\{q\} \times S^2$$ cắt nhau tại đúng $$1$$ điểm, còn mỗi mặt cầu tự trượt nhẹ ra khỏi chính nó nên tự giao bằng $$0$$; dạng giao là ma trận $$2\times 2$$:
     $$
     Q_{S^2\times S^2} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
     $$
2. **Ma trận kỳ lạ $$E_8$$:** Trong đại số Lie có một ma trận đối xứng nguyên $$8 \times 8$$ nổi tiếng là ma trận Cartan $$E_8$$: mọi phần tử trên đường chéo chính đều bằng $$2$$, các phần tử ngoài đường chéo là $$0$$ hoặc $$-1$$ (nên mọi số chéo là chẵn), xác định dương ($$v^T E_8 v > 0$$ với mọi $$v \neq 0$$) và có $$\det(E_8) = 1$$.
3. **Kiểm tra bằng tay tính chẵn lẻ:** Với bất kỳ vectơ nguyên $$v = (v_1, \dots, v_8)^T \in \mathbb{Z}^8$$ nào, khai triển dạng toàn phương:
   $$
   v^T E_8 v = \sum_{i=1}^8 2 v_i^2 + 2\sum_{i < j} (E_8)_{ij}\,v_i v_j \in 2\mathbb{Z} \quad (\text{luôn là số CHẴN!}).
   $$
   Vì vậy **không bao giờ tồn tại vectơ nguyên $$v$$ nào sao cho $$v^T E_8 v = 1$$**. Ngược lại, với ma trận đơn vị $$I_8$$, chỉ cần chọn $$e_1 = (1,0,\dots,0)^T$$ ta có ngay $$e_1^T I_8 e_1 = 1$$! Suy ra $$E_8$$ **không thể đổi cơ sở nguyên** thành $$I_8$$.
4. **Va chạm giữa hai định lý Fields:**
   - **Freedman (1982):** Tồn tại một **đa tạp tô pô 4 chiều** đóng, đơn liên $$M_{E_8}$$ có dạng giao đúng bằng $$E_8$$.
   - **Donaldson (1983):** Nếu một đa tạp 4 chiều đóng, đơn liên mang **cấu trúc trơn** và có dạng giao xác định dương, thì dạng giao của nó *bắt buộc* phải chéo hóa được về ma trận đơn vị $$I_n$$ trên $$\mathbb{Z}$$!
   - **Hệ quả tức thì:** Đa tạp tô pô $$M_{E_8}$$ có thật, nhưng nó **không thể mang bất kỳ cấu trúc khả vi trơn nào**! (Và từ đây chỉ vài bước nữa suy ra sự tồn tại của $$\mathbb{R}^4$$ kỳ lạ!)

---

## 2. Không gian moduli instanton như một chiếc kính hiển vi

Cố định một phân thớ chính $$SU(2)$$ trên đa tạp trơn định hướng đóng 4 chiều $$X$$, và xét các liên thông phản tự đối ngẫu (ASD — tức các instanton):

$$
F_A^+ = 0
$$

(trong đó $$F_A^+$$ là phần tự đối ngẫu của 2-dạng độ cong $$F_A$$ dưới toán tử sao Hodge $$\star$$ — một phép tách đặc thù chỉ tồn tại ở đúng chiều 4 vì $$\star^2 = +1$$ trên 2-dạng!). Tập các nghiệm, sau khi đồng nhất những nghiệm chỉ khác nhau bởi phép biến đổi gauge, tạo thành **không gian moduli $$\mathcal{M}$$**. Dưới các giả thiết tổng quát về metric trên $$X$$, $$\mathcal{M}$$ là một đa tạp hữu hạn chiều (có một số điểm kỳ dị ứng với liên thông khả quy cần kiểm soát), với số chiều được tính chính xác bằng định lý chỉ số Atiyah–Singer.

Điểm mấu chốt để trích ra bất biến là **biên của $$\mathcal{M}$$**: trong không gian vô hạn chiều các liên thông, một dãy nghiệm ASD có thể không hội tụ trơn. **Định lý compact của Uhlenbeck** bảo đảm sự mất hội tụ đó diễn ra theo cách hoàn toàn kiểm soát được: năng lượng độ cong chỉ có thể tập trung tại hữu hạn điểm như những "bọt khí" (instanton) tách ra ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)). Trong trường hợp kinh điển đầu tiên (định lý chéo hóa Donaldson 1983), chính đa tạp 4 chiều $$X$$ hiện ra như một phần biên của không gian moduli 5 chiều $$\mathcal{M}$$, từ đó buộc dạng giao của $$X$$ (nếu xác định dương) phải chéo hóa được trên $$\mathbb{Z}$$!

Từ các không gian moduli này, Donaldson trích ra các **bất biến đa thức**, giúp phân biệt những cấu trúc trơn mà tô pô đại số cổ điển (đồng điều, đồng luân) hoàn toàn không phân biệt nổi.

**Cơ chế chính.** Cấu trúc trơn → phương trình đạo hàm riêng elliptic của lý thuyết gauge → hình học của không gian moduli → bất biến → định lý về vật cản hoặc về sự phân biệt.

---

## 3. "Vật lý viết lại tô pô" nên hiểu cẩn thận thế nào

| Phía vật lý | Phía toán học |
|-------------|-----------|
| Yang–Mills, instanton | Phương trình ASD, năng lượng Chern–Weil |
| Quỹ đạo gauge | Thương theo nhóm gauge |
| Lập luận tích phân đường / TQFT (ra đời sau) | Lý thuyết giao trên không gian moduli, chặt chẽ (phần giải tích khó) |
| Đối ngẫu siêu đối xứng (thập niên 1990) | Phiên bản đơn giản hơn của Seiberg–Witten |

Các định lý là toán học thuần túy. **Cảm hứng và việc chọn đúng phương trình** đến từ lý thuyết gauge. Năm 1988, Edward Witten đưa ra cách diễn giải TQFT (lý thuyết trường lượng tử tô pô), giải thích về mặt hình thức các đa thức Donaldson như các hàm tương quan của một tích phân đường siêu đối xứng đã xoắn. Cách diễn giải này gợi ý những phép đối ngẫu mạnh mẽ, nhưng tự nó không thay thế được phần giải tích chặt chẽ, cho đến khi Seiberg–Witten tìm ra một hệ phương trình đạo hàm riêng cổ điển dễ xử lý hơn hẳn.

---

## 4. Seiberg–Witten (1994): công cụ đối ngẫu

Tháng 10 năm 1994, làn sóng phấn khích tràn khắp các khoa toán toàn cầu chỉ trong vài tuần. Nghiên cứu của Nathan Seiberg và Edward Witten về lý thuyết Yang–Mills siêu đối xứng $$\mathcal{N}=2$$ chỉ ra rằng ở vùng năng lượng thấp, lý thuyết $$SU(2)$$ phức tạp (với instanton không giao hoán) có một mô tả **đối ngẫu** bằng một lý thuyết **giao hoán $$U(1)$$** ghép với các đơn cực từ (monopole)! Witten lập tức dịch điều này thành **phương trình Seiberg–Witten** cho một cặp $$(A, \psi)$$ gồm một liên thông $$U(1)$$ (trên cấu trúc $$\operatorname{spin}^c$$) và một trường spinor $$\psi$$ trên đa tạp 4 chiều $$X$$:

$$
D_A \psi = 0, \qquad F_A^+ = q(\psi).
$$

Vì sao giới tô pô lại vỡ òa? Với phương trình Donaldson, nhóm gauge là $$SU(2)$$ không giao hoán và không gian moduli không compact nên phải xử lý hiện tượng nổi bọt cực kỳ công phu. Với phương trình Seiberg–Witten, nhóm gauge chỉ là $$U(1)$$ giao hoán, và một bất đẳng thức cực đại đơn giản (công thức Weitzenböck) lập tức suy ra **không gian moduli $$\mathcal{M}_{\mathrm{SW}}$$ tự động compact — không hề có hiện tượng nổi bọt!** Nhờ đó, nhiều định lý trước đây mất hàng trăm trang chứng minh bằng lý thuyết Donaldson (như giả thuyết Thom về giống cực tiểu của mặt cong trong $$\mathbb{CP}^2$$) bỗng được chứng minh lại chỉ trong vài trang giấy.

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

## Tài liệu tham khảo

1. Donaldson & Kronheimer, *The Geometry of Four-Manifolds* (Hình học của đa tạp bốn chiều).  
2. Witten, bài về TQFT (1988); bài "Monopoles and four-manifolds" (Đơn cực và đa tạp bốn chiều, 1994).  
3. Các liên kết trong khóa học ở trên.  
