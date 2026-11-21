---
layout: post
title: "Đối ngẫu như một nguyên lý (Toán & Vật lý)"
chapter: '06'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Michael Atiyah từng viết:

> "Duality in mathematics is not a theorem, but a 'principle'."  
> *(Đối ngẫu trong toán học là một "nguyên lý", chứ không phải một định lý.)*

Từ "đối ngẫu" (duality) cũng xuất hiện trong vật lý với tầm quan trọng tương đương. Hai lý thuyết trông rất khác nhau có thể mô tả cùng một hiện tượng, và chế độ khó tính ở phía này có thể là chế độ dễ ở phía kia. Bài này là **bản đồ của nguyên lý đó**: từ không gian đối ngẫu và biến đổi Fourier, đến đối ngẫu Poincaré, nhóm đối ngẫu Langlands, đối xứng gương, đối ngẫu điện–từ và AdS/CFT. Mỗi mục được ghi rõ trạng thái: định lý, giả thuyết sâu, hay chỉ là một khẩu hiệu dùng trong seminar.

Nên đọc sau bài [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/). Bài có liên kết sang [chương trình Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/), và giải tích gauge ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)). Các bài đọc sâu (đối xứng gương, AdS/CFT, Langlands hình học) nằm ở sau; ở đây mục tiêu là **nhìn tất cả dưới một mái nhà** và biết đọc đúng từng loại.

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- Phát biểu cẩn thận, trong một câu, toán học thường hiểu **đối ngẫu** là gì (một phép ghép cặp, một phép đối hợp, hoặc một tương đương đảo chiều mũi tên / đổi sang chiều bù).
- Nêu ba ví dụ toán học ở các tầng khác nhau (ví dụ: không gian đối ngẫu, đối ngẫu Poincaré, đối ngẫu Gelfand / Spec giữa không gian và đại số).
- Nêu ba ví dụ vật lý (đối ngẫu điện–từ; đối ngẫu T hoặc S ở mức ý chính; AdS/CFT như nguyên lý toàn ảnh).
- Giải thích vì sao đối ngẫu **hữu ích**: đòn bẩy tính toán, phân loại, và gộp "hai lý thuyết" thành một.
- Tránh coi mọi phép đối ngẫu là định lý đã chứng minh, và tránh nhầm đối xứng thông thường của một Lagrangian với sự tương đương của hai lý thuyết.
- Chỉ ra ít nhất hai chỗ trong khóa học đã có đối ngẫu (nhóm đối ngẫu Langlands; định lý chỉ số / lớp đặc trưng).

**Kiến thức cần có.** Đại số tuyến tính (biết không gian đối ngẫu là có lợi); giải tích nhiều biến. Tôpô và lý thuyết trường lượng tử **không** bắt buộc; nắm ý chính và khái niệm ghép cặp là đủ. Nên đọc kèm bài vật lý toán để có bối cảnh về phương trình đạo hàm riêng và lý thuyết trường lượng tử.

---

## 1. Đối ngẫu là loại đối tượng gì?

Định nghĩa dùng trong khóa học này:

> **Đối ngẫu** là một tương ứng có hệ thống, biến các đối tượng, phát biểu, hoặc cả một lý thuyết thành các đối tượng "bù" với chúng (thường bằng cách đảo chiều mũi tên, đổi sang chiều bù, hoặc đổi chế độ "khó" thành "dễ"), sao cho cấu trúc ở phía này kiểm soát cấu trúc ở phía kia.

Các dạng thường gặp (có thể chồng lên nhau):

| Dạng | Ý chính | Ví dụ quen thuộc |
|-----|--------|-----------------|
| **Đối hợp** (involution) | Đối ngẫu của đối ngẫu ≈ ban đầu | Phần bù của tập hợp; đa diện đối ngẫu; nhiều đối ngẫu thứ tự |
| **Đảo mũi tên** | Ánh xạ đi theo chiều ngược lại | Không gian đối ngẫu $$V^*$$; phạm trù đối; lý thuyết Galois: trường ↔ nhóm con |
| **Ghép cặp hoàn hảo** | $$A\times B\to\text{scalars}$$ không suy biến | Đồng điều – đối đồng điều; hàm thử và hàm suy rộng (phân bố) |
| **Tương đương lý thuyết** | Hai cách mô tả, một vật lý | Đối ngẫu S, T; AdS/CFT; đối ngẫu Seiberg |

Lý thuyết phạm trù gói nhiều phép đối ngẫu dưới dạng **tương đương phản biến** hoặc cặp hàm tử liên hợp. Vật lý thường diễn đạt chúng như **tương đương giữa hai lý thuyết** sau một phép đổi tham số (hằng số tương tác, bán kính, điện tích). Bạn không cần toàn bộ lý thuyết phạm trù. Hãy để ý ba dấu hiệu: **mũi tên đảo chiều**, **chiều được thay bằng chiều bù**, và **cùng một câu trả lời từ hai ngôn ngữ khác nhau**.

---

## 2. Tầng A: Đại số tuyến tính và giải tích (các ví dụ mẫu)

### Không gian đối ngẫu

Với không gian vectơ $$V$$ trên trường $$K$$, **không gian đối ngẫu** là

$$
V^* = \mathrm{Hom}(V,K) = \{\text{ánh xạ tuyến tính }\varphi:V\to K\}.
$$

Mỗi ánh xạ tuyến tính $$f:V\to W$$ sinh ra $$f^*:W^*\to V^*$$ bằng phép kéo lùi (pullback): **mũi tên đảo chiều**. Không gian hữu hạn chiều thỏa $$V\cong V^{**}$$ một cách chính tắc (qua phép lấy giá trị). Với không gian vô hạn chiều, ta cần thêm tôpô (đối ngẫu liên tục, không gian Banach phản xạ, không gian Hilbert qua định lý Riesz).

**Vì sao quan trọng.** Phép đo là đối ngẫu của trạng thái. Trong cơ học lượng tử, bra và ket là hai ngôn ngữ đối ngẫu: đại lượng quan sát đóng vai đối ngẫu với vectơ trạng thái. Đối ngẫu trong tối ưu (bài toán gốc ↔ bài toán đối ngẫu của quy hoạch tuyến tính) là họ hàng gần: mỗi biến ở phía này ứng với một ràng buộc ở phía kia, và hai giá trị tối ưu bằng nhau dưới các giả thiết chuẩn.

### Biến đổi Fourier và đối ngẫu Pontryagin

Biến đổi Fourier đổi "vị trí" thành "tần số". Về mặt cấu trúc, **đối ngẫu Pontryagin** nói rằng một nhóm abel compact địa phương $$G$$ được khôi phục từ nhóm các đặc trưng

$$
\widehat G = \mathrm{Hom}(G,S^1)
$$

qua đẳng cấu tự nhiên $$G\cong\widehat{\widehat G}$$. Nhóm rời rạc đối ngẫu với nhóm compact và ngược lại. Đây là nền tảng cấu trúc của giải tích điều hòa cổ điển, và là khuôn mẫu cho ý "không gian ↔ hàm trên đối ngẫu".

---

## 3. Tầng B: Hình học và tôpô (đổi sang chiều bù)

### Đa diện đều đối ngẫu và hình học xạ ảnh

Lập phương ↔ bát diện, thập nhị diện ↔ nhị thập diện, tứ diện tự đối ngẫu: **mặt của hình này là đỉnh của hình kia**. Hình học xạ ảnh đổi điểm thành đường thẳng và vẫn giữ quan hệ liên thuộc; nhờ đó nhiều định lý đi theo cặp, chứng minh một là có ngay định lý đối ngẫu.

### Đối ngẫu Poincaré

Trên một đa tạp $$M$$ compact, định hướng, $$n$$ chiều (với các giả thiết chuẩn), đồng điều và đối đồng điều ở các bậc bù nhau thì đối ngẫu với nhau:

$$
H^k(M)\;\simeq\; H_{n-k}(M)
$$

(hoặc tương đương: có một ghép cặp hoàn hảo giữa đối đồng điều bậc $$k$$ và bậc $$n-k$$). Số giao, **toán tử sao Hodge** ($$k$$-dạng ↔ $$(n-k)$$-dạng), và đối ngẫu điện–từ cổ điển viết bằng dạng vi phân đều là những ý gần với nó.

Điều này nằm cạnh mạch **định lý quả cầu lông → đặc trưng Euler → Poincaré–Hopf → Atiyah–Singer** trong [bài định lý chỉ số]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/): đối ngẫu ghép các bậc bù nhau là họ hàng tôpô của các ràng buộc chỉ số. Ở đây không cần chứng minh đối ngẫu Poincaré; chỉ cần nắm **hình dạng** của phát biểu.

---

## 4. Tầng C: Không gian ↔ đại số, và đối ngẫu thứ tự

### Gelfand và hình học đại số

**Đối ngẫu Gelfand** (ý chính): mỗi không gian Hausdorff compact tương ứng với C*-đại số giao hoán các hàm liên tục trên nó, và không gian được khôi phục như phổ các đặc trưng của đại số. **Hình học đại số** ghép vành giao hoán với lược đồ affine qua $$\mathrm{Spec}$$: đại số hàm ↔ không gian hình học. Hình học không giao hoán cố ý giữ lại phía đại số ngay cả khi không còn không gian cổ điển nào.

### Galois và thứ tự

Lý thuyết Galois: các trường trung gian ↔ các nhóm con đóng của nhóm Galois, với **thứ tự bị đảo ngược**. Lý thuyết thứ tự có các cặp đối ngẫu min/max, iđêan/lọc, mở/đóng (qua phần bù). Đó là những phép đối ngẫu "nhỏ", nhưng rèn cùng một phản xạ như các phép đối ngẫu lớn.

---

## 5. Tầng D: Các phép đối ngẫu lớn trong toán học

### Langlands và nhóm đối ngẫu

[Chương trình Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) nối biểu diễn tự đẳng cấu với dữ liệu Galois và số học, qua các $$L$$-hàm và **nhóm đối ngẫu Langlands** $$G^\vee$$. Langlands số học là một mạng lưới giả thuyết rộng lớn, trong đó có những "hòn đảo" đã thành định lý (tính modular; Bổ đề cơ bản do Ngô và nhiều người khác). **Langlands hình học** phát biểu một đối ngẫu tương tự trên đường cong, bằng ngôn ngữ bó và không gian moduli các phân thớ. Nó gần hình học hơn và (theo giả thuyết) gần vật lý hơn.

**Cách nói đúng.** Đừng nói "Langlands đã được chứng minh xong". Hãy nói: nhóm đối ngẫu và tính hàm tử (functoriality) tổ chức cả một chương trình; một số bổ đề then chốt đã mở đường cho các phép so sánh; phần lớn mạng lưới vẫn còn mở.

### Đối xứng gương

**Đối xứng gương** (xuất phát từ lý thuyết dây, nay là một ngành toán) ghép hình học symplectic của $$X$$ (mô hình A / phạm trù Fukaya) với hình học phức của đa tạp gương $$\check X$$ (mô hình B / bó chỉnh hình). **Đối xứng gương thuần nhất** (homological mirror symmetry) của Kontsevich phát biểu điều này như một tương đương phạm trù. Bức tranh **SYZ** cho rằng, trong nhiều trường hợp, cơ chế hình học là đối ngẫu T dọc theo các xuyến Lagrange đặc biệt.

Một số phát biểu đã là định lý cho các họ đặc biệt; chương trình tổng quát vẫn đang được nghiên cứu. Với bài này, chỉ cần nhớ: **hai hình học trông khác nhau lại tính ra cùng dữ liệu đếm / phạm trù**.

---

## 6. Tầng E: Đối ngẫu trong vật lý

### Đối ngẫu điện–từ

Lý thuyết Maxwell (trong chân không, với đơn vị thích hợp) đối xử đối xứng giữa điện và từ. Toán tử sao Hodge trên cường độ trường phát biểu điều này chính xác: $$F$$ và $$\star F$$. **Montonen–Olive** và các công trình sau mở rộng đối ngẫu điện–từ sang lý thuyết gauge không giao hoán: điện tích và đơn cực từ đổi vai cho nhau, thường kèm theo **mạnh ↔ yếu**. Đó là mầm mống của **đối ngẫu S**.

### Đối ngẫu S và đối ngẫu T (ý chính trong lý thuyết dây / lý thuyết trường lượng tử)

| Tên | Đổi gì (gần đúng) | Lợi ích điển hình |
|-----|--------------|-------------------|
| **Đối ngẫu S** | Hằng số tương tác $$g\leftrightarrow 1/g$$ (mạnh ↔ yếu) | Tính chế độ tương tác mạnh qua lý thuyết đối ngẫu tương tác yếu |
| **Đối ngẫu T** | Bán kính compact $$R\leftrightarrow \alpha'/R$$; số lần cuốn ↔ xung lượng | Nối dây loại IIA với IIB (và hai loại dây heterotic) trên xuyến |
| **Đối ngẫu U** | Nhóm đối xứng rời rạc trộn S và T | Lý thuyết M / các cấu trúc ngoại lệ |

**Đối ngẫu Seiberg** và nhiều đối ngẫu 2 và 3 chiều (hạt–xoáy, boson hóa) cho thấy **các Lagrangian khác nhau có thể dẫn đến cùng một vật lý ở năng lượng thấp**. Đó là tương đương giữa các lý thuyết, không phải đối xứng liên tục của một hàm tác dụng.

### AdS/CFT (nguyên lý toàn ảnh)

**Tương ứng AdS/CFT** (do Maldacena đề xuất, sau đó được phát triển bởi rất nhiều người) nói rằng một lý thuyết hấp dẫn trong không gian phản de Sitter $$(d+1)$$ chiều tương đương với một lý thuyết trường bảo giác, không có hấp dẫn, sống trên biên $$d$$ chiều. Ví dụ kinh điển: dây loại IIB trên $$\mathrm{AdS}_5\times S^5$$ ↔ $$\mathcal N=4$$ super Yang–Mills bốn chiều (với $$N$$ lớn, trong giới hạn kiểm soát được).

**Cách nói đúng.** Các trường hợp kiểm soát tốt nhất đều có siêu đối xứng và/hoặc $$N$$ lớn; nhiều ứng dụng còn mang tính giả thuyết hoặc chỉ dựa trên từ điển. Hãy coi AdS/CFT là **một chương trình nghiên cứu và một công cụ tính toán**, chứ không phải một định lý đã giải quyết xong hấp dẫn lượng tử. Dù vậy, nó vẫn là ví dụ tiêu biểu cho đối ngẫu khối ↔ biên và cho từ điển mạnh ↔ yếu.

### Vật lý chất rắn và tôpô

Chất cách điện tôpô, anyon và việc khớp dị thường (anomaly matching) dùng lại các ý về đối ngẫu và chỉ số: tôpô bên trong khối ràng buộc các mode trên biên; một số phép đếm nghiệm phụ thuộc vào hình dạng hơn là vào chi tiết vi mô. Điều này gợi lại phần vật lý của bài [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/).

---

## 7. Vì sao đối ngẫu thay đổi cách làm việc

1. **Đòn bẩy tính toán.** Giải bài toán ở phía đối ngẫu dễ hơn, rồi chuyển kết quả về ($$T$$ cao ↔ $$T$$ thấp trong đối ngẫu Kramers–Wannier; yếu ↔ mạnh trong đối ngẫu S).  
2. **Phân loại.** Điểm tự đối ngẫu xác định giá trị tới hạn của hằng số tương tác; nhóm đối ngẫu sắp xếp các phép đối ngẫu có thể có.  
3. **Gộp lý thuyết.** "Hai lý thuyết" trở thành một lớp tương đương (mạng lưới đối ngẫu của lý thuyết dây; lược đồ là đối ngẫu của dữ liệu vành).  
4. **Khám phá.** Kỳ vọng về đối ngẫu dự đoán trước các đối tượng (đơn cực từ, D-brane, nhóm đối ngẫu Langlands) trước khi người ta dựng được chúng trực tiếp.

Cách nghĩ hiện đại: câu hỏi hay thường không chỉ là "giải phương trình này", mà là "**mô tả đối ngẫu là gì, và nó có dễ hơn không?**". Đây cũng là sự thay đổi cách nghĩ giống lý thuyết chỉ số: "tôpô buộc phải có bao nhiêu nghiệm?".

---

## 8. Bảng từ điển tóm tắt

```text
Không gian dual V*      đo lường  ↔  bị đo
Fourier / Pontryagin    vị trí    ↔  tần số / character
Poincaré / Hodge        bậc k     ↔  bậc n−k ; E ↔ B
Gelfand / Spec          không gian ↔  đại số hàm
Langlands G ↔ G∨       automorphic ↔  Galois / spectral
Mirror A ↔ B            symplectic ↔  phức
S-duality               điện      ↔  từ ; mạnh ↔ yếu
T-duality               bán kính R ↔  α′/R ; winding ↔ momentum
AdS/CFT                 hấp dẫn bulk ↔ QFT biên
```

**Một cầu nối đáng nhớ.** Langlands hình học thường được xem là hình bóng toán học của **đối ngẫu S** trong lý thuyết gauge siêu đối xứng bốn chiều (Kapustin–Witten và các công trình liên quan). Hệ Hitchin của $$G$$ và của $$G^\vee$$ là gương của nhau theo ngôn ngữ SYZ. Chỉ một câu đó đã giải thích vì sao số học, hình học và vật lý năng lượng cao cùng xuất hiện trong một seminar.

---

## 9. Bản đồ khóa học

| Bài | Liên hệ với đối ngẫu |
|-----|-----------------|
| [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) | Trường gauge, lý thuyết trường lượng tử, phương trình Maxwell viết bằng dạng vi phân |
| [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) | Nhóm đối ngẫu, tính hàm tử |
| [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) | Chỉ số; Euler; lớp đặc trưng; cầu nối với vật lý |
| [Uhlenbeck / gauge]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/) | Kiểm soát giải tích không gian moduli gauge |
| [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) | Đối ngẫu trong không gian Hilbert; kênh đối ngẫu (sẽ học sau) |
| [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) | Công thức đối ngẫu Kantorovich |

---

## 10. Những nhầm lẫn thường gặp

| Khẳng định | Chỉnh lại |
|------------|-----------|
| "Đối ngẫu = đối xứng của một Lagrangian." | Thường là **tương đương giữa hai lý thuyết**, không phải đối xứng thông thường của một hàm tác dụng. |
| "Mọi đối ngẫu đều là phép đối hợp $$D^2=\mathrm{id}$$." | Đó là trường hợp lý tưởng; đôi khi chỉ dựng được một chiều, hoặc lấy đối ngẫu hai lần cho ra đối tượng lớn hơn. |
| "Đối xứng gương luôn là đối ngẫu T." | SYZ gợi ý đối ngẫu T trên xuyến; đối xứng gương thuần nhất rộng hơn và mang tính phạm trù. |
| "Langlands / AdS–CFT là định lý đã xong." | Đó là các chương trình với một số phần đã chứng minh; đừng phóng đại. |
| "Đối ngẫu Poincaré = định lý chỉ số." | Hai ý tôpô có họ hàng; định lý chỉ số là đẳng thức giữa hai bất biến của một toán tử elliptic. |
| "Đối ngẫu trong vật lý chỉ có ở lý thuyết dây." | Lý thuyết Maxwell, mô hình Ising, vật lý chất rắn, lý thuyết trường siêu đối xứng đều có đối ngẫu. |

---

## Bài tập

1. **Không gian đối ngẫu.** Với $$V=\mathbb{R}^2$$, mô tả $$V^*$$ và giải thích vì sao $$f:V\to W$$ sinh ra một ánh xạ **theo chiều ngược lại** giữa các không gian đối ngẫu.  
2. **Ghép cặp.** Không quá 80 chữ: một "ghép cặp hoàn hảo" $$A\times B\to K$$ cho ta điều gì về mặt khái niệm?  
3. **Đối ngẫu Poincaré.** Với một mặt đóng, định hướng ($$n=2$$), đối ngẫu Poincaré nói gì về $$H^1$$ và $$H_1$$ (ở mức ý chính)?  
4. **Đối ngẫu điện–từ.** Viết phương trình Maxwell trong chân không dưới dạng làm lộ rõ $$E\leftrightarrow B$$ (lập luận gần đúng cũng được), hoặc giải thích toán tử sao Hodge của $$F$$ trong một đoạn.  
5. **S và T.** Lập bảng hai hàng so sánh đối ngẫu S và đối ngẫu T (đổi gì; mỗi loại một lợi ích).  
6. **Nói đúng về Langlands.** Nhóm đối ngẫu Langlands dùng để làm gì (ý chính), và bạn **không** được khẳng định điều gì về trạng thái của chương trình?  
7. **Không quá 200 chữ:** vì sao "hai lý thuyết, một vật lý" khác với "một lý thuyết có nhóm đối xứng lớn"?  
8. **Không bắt buộc.** Đọc lướt một bài phổ biến khoa học về AdS/CFT; liệt kê ba mục trong từ điển (đối tượng trong khối ↔ trên biên), kèm lưu ý về trạng thái.

---

## Tài liệu tham khảo

1. Wikipedia — [Duality (mathematics)](https://en.wikipedia.org/wiki/Duality_(mathematics)).  
2. nLab — [duality](https://ncatlab.org/nlab/show/duality), [duality in string theory](https://ncatlab.org/nlab/show/duality+in+string+theory).  
3. Atiyah — nhận xét dualty như nguyên lý (thường được trích trong survey).  
4. Giáo trình đối ngẫu Pontryagin / Fourier (giải tích điều hòa chuẩn).  
5. Hatcher hoặc Bott–Tu — tôpô đại số cho Poincaré duality.  
6. Frenkel — survey Langlands và geometric Langlands (phổ biến).  
7. Polchinski / Becker–Becker–Schwarz — dualty string (phía vật lý).  
8. Maldacena; Aharony–Gubser–Maldacena–Ooguri–Oz — review AdS/CFT.  
9. De Haro et al. — *Dualities in Physics*.  
10. Khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/).

---

## Hướng tiếp

- **Bài đọc sâu:**  
  - [Mirror Symmetry]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/): mô hình A/B, SYZ, đối xứng gương thuần nhất  
  - [AdS/CFT & holography]({{ site.baseurl }}/contents/vi/chapter06/06_14_AdS_CFT/): từ điển khối ↔ biên  
  - [Geometric Langlands & S-duality]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/): cầu nối Kapustin–Witten  
- **Bài liên quan:** [Pontryagin & Fourier]({{ site.baseurl }}/contents/vi/chapter06/06_16_Pontryagin_Fourier_Duality/), [bài ngắn về Witten]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/)  
- **Bài thực hành:** [Vẽ từ điển đối ngẫu]({{ site.baseurl }}/contents/vi/chapter07/07_10_Explore_Duality_Dictionary/)  
- **Gói nghiên cứu:** `research/video-research/mirror-symmetry/`, `ads-cft/`, `geometric-langlands-sduality/`.  
- **Thói quen nên có:** ghi ba cột: *cặp đối ngẫu / đổi gì / định lý hay giả thuyết*.  
- **Câu hỏi thảo luận:** Lý thuyết chỉ số có phải là một phép đối ngẫu không? (Chỉ số giải tích = chỉ số tôpô là một *đẳng thức giữa hai bất biến*; gần với đối ngẫu, nhưng không phải là tương đương giữa hai lý thuyết.)

## Video tham khảo

- **Xem trước:** [Edward Witten: Mirror Symmetry & Geometric Langlands (2012)](https://www.youtube.com/watch?v=S02ghGCdNDo) (Graduate Mathematics, tiếng Anh). Witten nói về hai phép đối ngẫu lớn, đối xứng gương và Langlands hình học, và mối liên hệ giữa chúng. Nên xem trước khi đọc mục 5 và 6.
- [HMS for local CY manifolds via SYZ | Kwokwai Chan](https://www.youtube.com/watch?v=Kz6Dj8KSFjM) (Harvard CMSA, tiếng Anh). Bài giảng chuyên sâu về đối xứng gương thuần nhất cho đa tạp Calabi–Yau địa phương qua bức tranh SYZ. Nên xem sau, khi đã đọc bài đối xứng gương.
- [Lagrangian fillings what does the sheaf say? | Eric Zaslow](https://www.youtube.com/watch?v=Y3-sw3tjZiU) (Harvard CMSA, tiếng Anh). Bài giảng nghiên cứu về mặt lấp Lagrange nhìn qua lý thuyết bó; dành cho người muốn đi sâu vào hình học symplectic.
