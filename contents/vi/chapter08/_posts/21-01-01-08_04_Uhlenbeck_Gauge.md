---
layout: post
title: "Karen Uhlenbeck: Phân tích Hình học và Gauge Theory (Abel 2019)"
chapter: '08'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

Nhúng một vòng dây đồng vào nước xà phòng rồi nhẹ nhàng nhấc lên: màng xà phòng lập tức căng ra thành một mặt cong mượt mà có diện tích nhỏ nhất có thể. Tự nhiên rất chuộng những trạng thái "cực tiểu hóa năng lượng" như thế. Nhưng điều gì xảy ra nếu ta thử kéo căng một màng năng lượng không phải trong không gian 3 chiều quen thuộc, mà là các **trường lực vật lý** sống trên một không gian cong 4 chiều? Năng lượng có thể không chịu trải đều êm ái, mà đột ngột dồn nén lại tại một điểm duy nhất—và từ điểm đó, một **"bong bóng" (bubble)** năng lượng tự tách ra như một giọt xà phòng nhỏ bứt khỏi màng lớn!

Người đầu tiên chế ngự được những bong bóng kỳ dị ấy bằng những ước lượng giải tích sắc bén, đặt nền móng vững chắc cho cả một nhánh mới của toán học và vật lý toán, là **Karen Keskulla Uhlenbeck**. Năm **2019**, bà trở thành **nữ nhà toán học đầu tiên** nhận **Giải Abel**:

> “for her pioneering achievements in geometric partial differential equations, gauge theory and integrable systems, and for the fundamental impact of her work on analysis, geometry and mathematical physics.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2019)

Câu chuyện của Uhlenbeck là minh họa đẹp nhất cho "toán học hạ tầng": nếu thiếu những định lý về tính compact, bong bóng và kỳ dị khử được mà bà xây dựng, cả cuộc cách mạng tôpô 4 chiều của Simon Donaldson và mối lương duyên hiện đại giữa lý thuyết trường lượng tử với hình học đã không thể cất cánh. Tài liệu chính thức: [abelprize.no](https://abelprize.no/).

**Mạch bài học:** Bản đồ kiến thức nền (Phân thớ, liên thông, độ cong, giải tích hình học) → Lý thuyết gauge và năng lượng Yang–Mills → Vì sao giải tích là nút thắt → Khung giải thích chậm: tính tay tính bất biến bảo giác và hiện tượng bong bóng năng lượng → Các định lý đột phá của Uhlenbeck → Không gian moduli và cố định gauge.

---

## Mục tiêu học tập

Sau bài này, bạn có thể giải thích các đối tượng gauge (liên thông, độ cong, phân thớ) ở mức khẩu hiệu; mô tả vì sao **tính compact, bubbling và kỳ dị khử được** quan trọng với PDE hình học; đặt Uhlenbeck vào vị trí hạ tầng giải tích cho tôpô gauge (Donaldson và các thế hệ sau); nối văn hóa của giải tích hình học với mặt cực tiểu và các dòng hình học; và phân biệt “cảm hứng từ vật lý” với “định lý toán học về không gian moduli”.

**Kiến thức nền.** Giải tích nhiều biến; ý niệm về đa tạp và mặt. Đại số tuyến tính giúp hiểu “liên thông gần như là cách lấy đạo hàm trường vector”. Không cần đã học lý thuyết gauge. Liên kết: [mặt cực tiểu]({{ site.baseurl }}/contents/vi/chapter04/04_09_Minimal_Surfaces/), [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

---

## Bản đồ kiến thức nền: Giải tích hình học và lý thuyết trường chuẩn (Gauge Theory) là gì và nghiên cứu những gì?

Khi nghe hai cụm từ **giải tích hình học (geometric analysis)** và **lý thuyết trường chuẩn (gauge theory)**, nhiều sinh viên đại học dễ nghĩ ngay đến các phương trình phức tạp trong vật lý hạt cơ bản. Thật ra, ý tưởng cốt lõi của chúng đứng trên ba trụ cột hình học vô cùng gần gũi:

### 1. Phân thớ (Bundle) và Liên thông (Connection)
Hãy tưởng tượng bề mặt Trái Đất (một đa tạp $$M$$). Tại mỗi điểm trên mặt đất, ta gắn thêm một "không gian nội tại"—ví dụ một mặt đồng hồ hay một hệ trục tọa độ để đo pha lượng tử của hạt. Tập hợp tất cả các không gian nội tại gắn trên mọi điểm của $$M$$ gọi là một **phân thớ**. Vấn đề là: không gian nội tại ở Hà Nội và ở TP.HCM không có sẵn một "mốc 12 giờ" chung để so sánh trực tiếp. Một **liên thông** $$A$$ chính là *quy tắc vận chuyển song song*—cho biết cách mang một vector nội tại đi dọc theo một con đường từ điểm này sang điểm khác sao cho "không bị xoay oan".

### 2. Độ cong (Curvature) và Phép biến đổi Gauge
Cầm một mũi tên ở cực Bắc, giữ nó "thẳng" theo quy tắc liên thông, đi xuống xích đạo, rẽ trái 90 độ đi một phần tư vòng xích đạo, rồi đi ngược về cực Bắc. Khi về tới nơi, mũi tên đã bị xoay đi 90 độ so với ban đầu! Sự sai lệch sau khi đi hết một vòng kín chính là **độ cong** $$F_A$$. Trong vật lý điện từ, liên thông $$A$$ chính là *thế điện từ*, còn độ cong $$F_A$$ chính là *trường điện từ* ($$\mathbf{E}, \mathbf{B}$$). Ta có thể tự do xoay lại mốc 12 giờ ở từng điểm mà không làm thay đổi thực tại vật lý; phép đổi hệ quy chiếu cục bộ ấy gọi là **phép biến đổi chuẩn (gauge transformation)**. Lý thuyết trường chuẩn nghiên cứu những phương trình *bất biến* dưới sự thay đổi hệ quy chiếu đó—nổi tiếng nhất là phương trình **Yang–Mills**.

### 3. Giải tích hình học (Geometric Analysis)
Là ngành dùng các phương trình đạo hàm riêng (PDE) và ước lượng giải tích để nghiên cứu hình dạng toàn cục của không gian. Nếu màng xà phòng là nghiệm cực tiểu hóa diện tích, thì các liên thông Yang–Mills là nghiệm cực tiểu hóa năng lượng độ cong. Nhiệm vụ của giải tích hình học là trả lời: *nghiệm có tồn tại không? Nó có trơn không? Và khi một dãy nghiệm có năng lượng bị chặn, chúng hội tụ về đâu hay nổ thành bong bóng?*

---

## 1. Lý thuyết gauge như hình học

Trong vật lý, trường gauge mô tả các lực cơ bản của tự nhiên: điện từ là trường gauge giao hoán (nhóm đối xứng $$U(1)$$); còn tương tác yếu và tương tác mạnh liên quan đến trường **Yang–Mills** không giao hoán (như $$SU(2)$$ hay $$SU(3)$$). Dịch sang ngôn ngữ toán học, ta có một **phân thớ** chính hoặc phân thớ vector trên một đa tạp $$M$$. Một **liên thông** $$A$$ là quy tắc lấy đạo hàm hiệp biến các tiết diện, và **độ cong** $$F_A$$ đo mức độ không giao hoán giữa các đạo hàm riêng theo hai hướng khác nhau; dưới dạng địa phương bằng ngôn ngữ các dạng vi phân có giá trị trong đại số Lie:

$$
F_A = dA + A\wedge A.
$$

Số hạng $$A \wedge A$$ chính là nơi sự **phi tuyến** (và tính không giao hoán) bùng nổ: với điện từ cổ điển ($$U(1)$$), $$A \wedge A = 0$$ nên phương trình Maxwell là tuyến tính; còn với Yang–Mills ($$SU(2)$$), $$A \wedge A \neq 0$$ khiến trường lực tự tương tác với chính nó!

**Phiếm hàm Yang–Mills** đo tổng năng lượng của độ cong trên toàn đa tạp:

$$
\mathrm{YM}(A) = \int_M \lvert F_A\rvert^2\, d\mathrm{vol}.
$$

Các điểm tới hạn của phiếm hàm này là những **liên thông Yang–Mills**—tương tự như màng xà phòng là điểm tới hạn của phiếm hàm diện tích. Ở chiều 4 (không–thời gian Euclid 4 chiều), những nghiệm cực tiểu đặc biệt gọi là **instanton** (liên thông phản tự đối ngẫu) bất ngờ trở thành chìa khóa giải mã tôpô của các 4-đa tạp trơn.

Thế nhưng để chiết xuất thông tin tôpô từ **không gian moduli** của các nghiệm instanton (như Simon Donaldson đã làm để giành Huy chương Fields năm 1986), giới toán học buộc phải có những định lý giải tích chặt chẽ: sự tồn tại, tính compact, tính chính quy và khả năng kiểm soát kỳ dị. Nếu thiếu nền móng giải tích đó, mọi tính toán hình thức của vật lý hay tôpô đại số chỉ dừng lại ở mức trực giác chứ không thể trở thành định lý. Cụm *"fundamental impact"* trong lời trao giải Abel 2019 chính là sự ghi nhận cho tầng hạ tầng tối quan trọng ấy.

---

## 2. Vì sao giải tích là nút thắt

Không gian của tất cả các liên thông—ngay cả sau khi đã gom những liên thông tương đương nhau qua phép biến đổi gauge—vẫn là một không gian **vô hạn chiều** và **không compact** theo nghĩa ngây thơ. Nếu bạn lấy một dãy các liên thông $$A_1, A_2, A_3, \dots$$ có cùng mức năng lượng Yang–Mills bị chặn, điều gì có thể xảy ra khi $$k \to \infty$$?

- Chúng có thể hội tụ mượt mà trên gần như toàn bộ đa tạp $$M$$;  
- Hoặc một phần năng lượng đột ngột **tập trung** vào một vài điểm cô lập (hoặc tập có chiều thấp hơn), khiến độ cong tại đó tăng vọt lên vô cực;  
- Tại mỗi điểm tập trung ấy, nếu bạn dùng kính hiển vi phóng đại liên tục không gian xung quanh, một nghiệm Yang–Mills hoàn chỉnh trên mặt cầu $$S^4$$ (hay $$\mathbb{R}^4$$) sẽ hiện ra như một **"bong bóng" (bubble)** tách khỏi mặt nền.

### Khung giải thích: Vì sao ở chiều tới hạn lại xuất hiện "bong bóng" năng lượng? (nên đọc chậm)

Tại sao hiện tượng bong bóng năng lượng của Yang–Mills lại đặc biệt bùng nổ ở đúng **chiều $$n = 4$$** (và với ánh xạ điều hòa ở đúng **chiều $$n = 2$$**)? Bạn có thể tự tay kiểm tra bằng hai phép tính giải tích năm nhất dưới đây!

#### Bước 1: Kiểm tra phép co giãn thang đo cho năng lượng Yang–Mills
Giả sử ta có một liên thông $$A(x)$$ trên $$\mathbb{R}^n$$ và ta "bóp nhỏ" nó lại theo tỉ lệ $$\lambda > 0$$ bằng cách đặt $$A_\lambda(x) = \lambda^{-1} A(x/\lambda)$$ (hệ số $$\lambda^{-1}$$ xuất hiện vì $$A$$ là 1-dạng $$A_i\,dx^i$$). Khi đó độ cong $$F_{A_\lambda}(x) = \lambda^{-2} F_A(x/\lambda)$$. Đổi biến $$y = x/\lambda$$ (nên $$dx = \lambda^n\,dy$$), ta tính ngay năng lượng:

$$
\mathrm{YM}(A_\lambda) = \int_{\mathbb{R}^n} \lvert F_{A_\lambda}(x)\rvert^2\,dx = \int_{\mathbb{R}^n} \lambda^{-4} \lvert F_A(y)\rvert^2 \cdot \lambda^n\,dy = \lambda^{n-4}\,\mathrm{YM}(A).
$$

Nhìn vào số mũ $$n - 4$$: đúng tại **$$n = 4$$**, ta có $$\lambda^{4-4} = 1$$! Nghĩa là bạn có thể nén một trường lực Yang–Mills vào một chấm nhỏ cỡ $$10^{-100}$$ mà **tổng năng lượng không hề tăng lên chút nào**!

#### Bước 2: Tự tay tính tích phân một "bong bóng" 2 chiều đang thu nhỏ
Để thấy tận mắt năng lượng dồn vào một điểm ra sao, hãy xét họ ánh xạ điều hòa (mô hình Sacks–Uhlenbeck trong 2D) với mật độ năng lượng trên mặt phẳng cực $$(r, \theta)$$ cho bởi:

$$
e_\lambda(r) = \frac{4\lambda^2}{(r^2 + \lambda^2)^2}, \qquad \lambda > 0.
$$

Ta tính năng lượng chứa trong một đĩa tròn nhỏ bán kính $$R$$ quanh gốc tọa độ bằng phép đổi biến cơ bản $$u = r^2 + \lambda^2$$ ($$du = 2r\,dr$$):

$$
E_\lambda(B_R) = \int_0^{2\pi} \int_0^R \frac{4\lambda^2}{(r^2 + \lambda^2)^2}\,r\,dr\,d\theta = 4\pi\lambda^2 \left[ -\frac{1}{r^2 + \lambda^2} \right]_0^R = 4\pi\left(1 - \frac{\lambda^2}{R^2 + \lambda^2}\right) = 4\pi\,\frac{R^2}{R^2 + \lambda^2}.
$$

Hãy thay số cụ thể với đĩa siêu nhỏ $$R = 0.01$$:
- Khi $$\lambda = 1$$ (bong bóng còn rộng): $$E_1(B_{0.01}) \approx 4\pi \times 10^{-4}$$ (gần như bằng 0).
- Khi $$\lambda = 0.01$$: $$E_{0.01}(B_{0.01}) = 2\pi$$ (một nửa năng lượng đã chui vào đĩa $$R=0.01$$).
- Khi $$\lambda \to 0$$: $$E_\lambda(B_{0.01}) \to 4\pi$$ — **toàn bộ năng lượng $$4\pi$$ (diện tích mặt cầu đơn vị $$S^2$$!) đã tập trung gọn lỏn tại duy nhất gốc tọa độ**, trong khi ở mọi điểm $$r > 0$$ mật độ năng lượng $$e_\lambda(r) \to 0$$!

Nếu không kiểm soát được những bong bóng ấy, không gian moduli sẽ bị "thủng lỗ chỗ" ở biên: ta không thể compact hóa nó, không thể đếm nghiệm, và không thể suy ra bất biến tôpô. Giải tích hình học sống theo một phương châm nhất quán: **ước lượng trước, phân loại sau.**

---

## 3. Những đột phá giải tích gắn với Uhlenbeck

### Tính compact của Uhlenbeck

Định lý nổi tiếng nhất mang tên bà khẳng định: với một dãy liên thông Yang–Mills có năng lượng bị chặn trên một 4-đa tạp, sau khi chọn một hệ quy chiếu chuẩn phù hợp (cố định gauge), luôn tồn tại một dãy con hội tụ trơn ở mọi nơi **ngoại trừ hữu hạn điểm kỳ dị**—đúng những nơi năng lượng tập trung thành bong bóng. Biết chính xác số điểm kỳ dị là hữu hạn (bị chặn bởi tổng năng lượng chia cho năng lượng tối thiểu của một bong bóng) cho phép các nhà toán học "vá biên" không gian moduli bằng cách gắn thêm các "cây bong bóng".

### Kỳ dị khử được và tính chính quy epsilon

Hai trụ cột kỹ thuật đi kèm định lý compact là:

- **Tính chính quy epsilon ($$\varepsilon$$-regularity):** Tồn tại một ngưỡng năng lượng dương $$\varepsilon_0 > 0$$ sao cho hễ năng lượng độ cong trong một quả cầu nhỏ thấp hơn $$\varepsilon_0$$, thì liên thông trong quả cầu đó bắt buộc phải trơn tru và bị kiểm soát chặt (sau khi chọn gauge). Nói cách khác, **năng lượng nhỏ cấm mọi hành vi hoang dại**—muốn tạo ra kỳ dị hay bong bóng, thiên nhiên bắt buộc phải trả một "mức phí năng lượng" tối thiểu.
- **Định lý kỳ dị khử được (Removable singularities):** Nếu một liên thông Yang–Mills có một điểm kỳ dị cô lập (chẳng hạn tại gốc tọa độ $$0 \in \mathbb{R}^4$$) nhưng tổng năng lượng xung quanh nó là hữu hạn, thì điểm kỳ dị ấy thực chất chỉ là "ảo giác" do chọn hệ tọa độ xấu: luôn có một phép biến đổi gauge làm nó trơn tru trở lại hoàn toàn! Đây là kết quả kỳ diệu giúp "lấp lỗ hổng" khi compact hóa không gian moduli.

### Mẫu hình ngoài Yang–Mills

Triết lý của Sacks–Uhlenbeck và Uhlenbeck không dừng lại ở lý thuyết trường chuẩn. Nó lan rộng sang ánh xạ điều hòa (*harmonic maps*), đường cong giả chỉnh hình trong tôpô symplectic (Gromov), phương trình Yang–Mills–Higgs và vô số PDE hình học khác. Chu trình **tập trung năng lượng → phóng đại tại điểm kỳ dị → phân loại bong bóng** đã trở thành ngôn ngữ tiêu chuẩn trong mọi khóa cao học về giải tích hình học.

### Hệ khả tích và giải tích hình học rộng hơn

Lời tuyên dương Abel còn nhắc đến **các hệ khả tích** (*integrable systems*)—những phương trình phi tuyến đặc biệt có vô hạn đại lượng bảo toàn và lời giải có cấu trúc đại số tinh tế (như ánh xạ điều hòa vào nhóm Lie). Sự nghiệp của Uhlenbeck rộng hơn nhiều so với một định lý đơn lẻ: bà mở ra cả một tuyến xa lộ hai chiều nối giải tích thuần túy với hình học và vật lý lý thuyết.

---

## 4. Tập trung năng lượng: bản đồ sâu hơn

Nhiều bài toán đẹp nhất của hình học đều có dạng tìm điểm tới hạn của một phiếm hàm năng lượng (năng lượng Dirichlet cho ánh xạ, diện tích cho mặt cực tiểu, Yang–Mills cho liên thông). Ở **số chiều tới hạn**—chiều 2 cho ánh xạ điều hòa, chiều 4 cho Yang–Mills—năng lượng có tính **bất biến bảo giác** (phóng to hay thu nhỏ miền không làm thay đổi tổng năng lượng). Chính tính bất biến theo thang đo này là nguyên nhân khiến bong bóng có thể hình thành ở kích thước nhỏ tùy ý mà không làm năng lượng tăng vọt.

Các ước lượng kiểu Uhlenbeck đem lại một ngưỡng định lượng sắc như dao: dưới ngưỡng $$\varepsilon_0$$, không thể có bong bóng nào lẩn trốn; trên ngưỡng $$\varepsilon_0$$, mọi bong bóng đều phải lộ diện và được đếm rõ ràng. Nhờ đó, "phần biên ở vô cùng" của không gian moduli không còn là vùng tối hỗn loạn, mà mang cấu trúc hình học rõ nét.

Nếu so sánh thận trọng với bài toán kỳ dị của Navier–Stokes hay dòng Ricci (Perelman), phương trình tuy khác nhau nhưng tinh thần **phân tích đa thang (blow-up)**—đặt kính hiển vi vào đúng nơi mật độ năng lượng hoặc độ cong bùng nổ—là cùng một dòng máu của giải tích hình học hiện đại.

---

## 5. Vì sao đáng một giải Abel

Một phép tính khéo léo chỉ giải được một bài tập; còn Uhlenbeck đã làm cho các PDE hình học vô hạn chiều trở nên **sử dụng được** cho cả tôpô lẫn vật lý. Trên nền đất vững chắc mà bà đặt xuống, Simon Donaldson đã chứng minh sự tồn tại của các cấu trúc vi phân kỳ lạ trên $$\mathbb{R}^4$$ (một cú sốc lớn nhất của tôpô thế kỷ XX), rồi sau đó là lý thuyết Seiberg–Witten, Donaldson–Thomas và hàng loạt nhánh hình học hiện đại khác.

Giải Abel 2019 là một giải **tôn vinh hạ tầng** đúng nghĩa. Việc Karen Uhlenbeck là người phụ nữ đầu tiên nhận Giải Abel là một cột mốc lịch sử đáng trân trọng đối với văn hóa khoa học; đồng thời, giá trị toán học trong công trình của bà đứng sừng sững hoàn toàn độc lập với cột mốc đó. Hãy tránh cả hai lối nhìn giản lược: đừng rút gọn giải thưởng thành "chỉ là sự kiện lịch sử về giới", cũng đừng rút gọn lý thuyết gauge thành "chỉ là chuyện vật lý hạt".

---

## 6. Cố định gauge, moduli và “không gian nghiệm”

Một liên thông chỉ có ý nghĩa hình học sau khi chia bỏ **nhóm biến đổi gauge**: đổi hệ quy chiếu nội tại làm biểu thức tọa độ của $$A$$ thay đổi, nhưng thực thể hình học vẫn y nguyên. Đối tượng thật sự mà nhà hình học muốn khảo sát là **không gian moduli**:

$$
\mathcal{M} = \{\text{Yang–Mills connections}\}/\text{gauge}.
$$

Chia một không gian vô hạn chiều cho một nhóm vô hạn chiều là một cơn ác mộng giải tích: phương trình Yang–Mills ban đầu thậm chí không có tính elliptic vì bị "nhiễu" bởi vô hạn hướng biến đổi gauge. Bí quyết của Uhlenbeck là **cố định gauge** (chẳng hạn chọn **gauge Coulomb**, đặt điều kiện $$d^* A = 0$$): khi khóa chặt tự do chọn hệ quy chiếu, phương trình lập tức trở thành elliptic và cho phép áp dụng các ước lượng giải tích mạnh mẽ để kiểm soát nghiệm cục bộ.

Ở chiều 4, không gian moduli của các liên thông phản tự đối ngẫu (instanton) trở thành một đối tượng hữu hạn chiều mang dấu ấn của cấu trúc trơn trên 4-đa tạp nền. Nếu không có định lý cố định gauge, tính compact và kỳ dị khử được của Uhlenbeck, chương trình không gian moduli của Donaldson đã không thể khởi động.

---

## 7. Vị trí trong khóa học

- [Mặt cực tiểu]({{ site.baseurl }}/contents/vi/chapter04/04_09_Minimal_Surfaces/): năng lượng, tính chính quy, các kết luận hình học rút ra từ PDE.  
- [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/): nơi trường gauge quay lại với tư cách vật lý.  
- [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/): PDE hình học chinh phục tôpô bằng một con đường khác (dòng Ricci có phẫu thuật).  
- Lý thuyết gauge và tôpô của các 4-đa tạp là câu chuyện song song “PDE → tôpô”, đối với “PDE → hình học hóa” của dòng Ricci.

Một so sánh rất đáng nhớ: dòng Ricci biến dạng *metric* của không gian; còn Yang–Mills nghiên cứu *liên thông* tới hạn trên phân thớ. Cả hai đều là những chương trình PDE hình học dùng giải tích để đọc ra tôpô. Phương trình và mô hình kỳ dị khác nhau, nhưng triết lý thì đồng nhất: **ước lượng trước, phân loại sau**.

---

## 8. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Gauge chỉ là vật lý hạt.” | Trong toán thuần túy: hình học của liên thông và không gian moduli, với ứng dụng cho tôpô. |
| “Compact nghĩa là mọi dãy đều hội tụ.” | Hội tụ của một dãy con sau khi chọn gauge, thường ngoài một tập kỳ dị, có thể kèm bong bóng. |
| “Uhlenbeck chứng minh định lý Donaldson.” | Donaldson dùng không gian moduli gauge cho tôpô; phân tích kiểu Uhlenbeck là hạ tầng. |
| “Kỳ dị khử được nghĩa là không có gì xấu.” | Có thể gỡ kỳ dị *dưới giả thiết* (năng lượng bị chặn). |
| “Giải Abel 2019 chỉ là giải của sự đa dạng.” | Citation nói về toán học của PDE hình học và gauge; cột mốc lịch sử chỉ là sự kiện thêm vào. |

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2019: Uhlenbeck, PDE hình học, gauge, bubbling và kỳ dị.
- Nữ laureate đầu tiên; hạ tầng giải tích cho tôpô gauge.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: bài giảng Abel của Uhlenbeck về Phép tính biến phân: [https://www.youtube.com/watch?v=1WepO8tFGto](https://www.youtube.com/watch?v=1WepO8tFGto).  
2. **Cốt lõi**: Bryant, về bong bóng và kỳ dị (nói về công trình của Uhlenbeck): [https://www.youtube.com/watch?v=EZNpi8H6q1Q](https://www.youtube.com/watch?v=EZNpi8H6q1Q).  
3. **Định hướng**: phỏng vấn Uhlenbeck của giải Abel: [https://www.youtube.com/watch?v=0fOaetX4eHM](https://www.youtube.com/watch?v=0fOaetX4eHM).  
4. **Định hướng**: phỏng vấn trực tiếp Uhlenbeck: [https://www.youtube.com/watch?v=mmWdPPwSi64](https://www.youtube.com/watch?v=mmWdPPwSi64).  
5. **Lịch sử**: buổi công bố giải Abel 2019: [https://www.youtube.com/watch?v=arrl_nM0T4s](https://www.youtube.com/watch?v=arrl_nM0T4s).  

**Cổng chính thức và tài liệu**

- Abel 2019 Uhlenbeck: https://abelprize.no/abel-prize-laureates/2019  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/uhlenbeck-gauge_1WepO8tFGto_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2019 Uhlenbeck — https://abelprize.no/abel-prize-laureates/2019  
2. Uhlenbeck Abel lecture — Calculus of Variations — https://www.youtube.com/watch?v=1WepO8tFGto  
3. Bryant — Bubbles & singularities (on Uhlenbeck) — https://www.youtube.com/watch?v=EZNpi8H6q1Q  
4. Abel Prize Interview Uhlenbeck — https://www.youtube.com/watch?v=0fOaetX4eHM  
5. Live interview Uhlenbeck — https://www.youtube.com/watch?v=mmWdPPwSi64  
6. Abel announcement 2019 — https://www.youtube.com/watch?v=arrl_nM0T4s  
7. Quanta — Uhlenbeck Abel — https://www.quantamagazine.org/karen-uhlenbeck-uniter-of-geometry-and-analysis-wins-abel-prize-20190319/  
8. Celebratio Mathematica — Uhlenbeck — https://celebratio.org/Uhlenbeck_K/cover/472/  
9. AMS Notices survey (Donaldson on Uhlenbeck PDF) — https://www.ams.org/journals/notices/201903/rnoti-p303.pdf  
10. Wikipedia — Karen Uhlenbeck — https://en.wikipedia.org/wiki/Karen_Uhlenbeck  

1. [Abel 2019](https://abelprize.no/abel-prize-laureates/2019).  
2. Bài khảo sát về giải tích của Yang–Mills và tính compact của Uhlenbeck.  
3. Nhập môn tôpô gauge (Donaldson–Kronheimer, …) để lấy ngữ cảnh, không phải là điều kiện tiên quyết đầy đủ.  
4. Liên kết trong khóa: mặt cực tiểu; vật lý toán; Perelman.

---

## Hướng đi tiếp

- So sánh ngôn ngữ về bubbling với kỳ dị của Navier–Stokes (phương trình khác, triết lý thang đo tương tự).  
- Trong seminar: phê bình những bài phổ thông chỉ gán gauge cho vật lý hạt.  
- Ghi lại một thách thức giải tích còn mở trong PDE hình học mà bạn quan tâm (gauge ở chiều cao hơn, mô hình kỳ dị, …).  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

## Video tham khảo

- **Xem trước** — [Karen Uhlenbeck: Some Thoughts on the Calculus of Variations](https://www.youtube.com/watch?v=1WepO8tFGto) — The Abel Prize, tiếng Anh. Xem trước để nghe chính Uhlenbeck nói về phép tính biến phân, nền tảng cho phần còn lại của bài.
- [Robert Bryant: Limits, Bubbles, and Singularities: The fundamental ideas of Karen Uhlenbeck](https://www.youtube.com/watch?v=EZNpi8H6q1Q) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để thấy giới hạn, bong bóng và kỳ dị được giải thích có hệ thống.
- [Karen Uhlenbeck - The Abel Prize interview 2019](https://www.youtube.com/watch?v=0fOaetX4eHM) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua cuộc phỏng vấn về con đường làm toán của bà.
