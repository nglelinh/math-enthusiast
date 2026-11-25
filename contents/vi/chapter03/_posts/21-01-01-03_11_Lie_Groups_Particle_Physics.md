---
layout: post
title: "Đối xứng, nhóm Lie và vật lý hạt"
chapter: '03'
order: 11
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Vào đầu thập niên 1960, các máy gia tốc hạt khiến giới vật lý bối rối khi liên tục bắn ra hàng chục loại hạt hạ nguyên tử mới trông lộn xộn chẳng khác gì một "sở thú hạt" không có quy luật. Thế rồi năm 1962, nhà vật lý Murray Gell-Mann thử xếp các hạt này theo **lý thuyết biểu diễn của một nhóm đối xứng toán học liên tục có tên $$SU(3)$$**. Khi vẽ xong hình tam giác phân loại gồm 10 vị trí, ông thấy 9 vị trí đã có hạt lấp đầy — còn đúng **một ô trống duy nhất ở đỉnh dưới cùng**. Chỉ dựa vào tính đối xứng của nhóm $$SU(3)$$, Gell-Mann mạnh dạn tiên đoán khối lượng, điện tích và độ lạ của hạt còn thiếu (hạt $$\Omega^-$$). Hai năm sau, phòng thí nghiệm Brookhaven tìm thấy hạt $$\Omega^-$$ đúng y hệt các con số toán học đã chỉ ra!

Nếu hình học là ngôn ngữ của không–thời gian và hấp dẫn, thì **đối xứng liên tục** chính là bản thiết kế kiến trúc của các định luật bảo toàn và bảng tuần hoàn của thế giới hạ nguyên tử. Toàn bộ **Mô hình Chuẩn (Standard Model)** của vật lý hạt hiện đại được dựng trên một biểu thức nhóm Lie cực kỳ cô đọng:

$$
G_{\mathrm{SM}} = U(1)_Y \times SU(2)_L \times SU(3)_c.
$$

Bài học này giải mã biểu thức tưởng chừng bí hiểm ấy ở mức trực giác đại học: nhóm Lie là gì, vì sao vật lý cần lý thuyết biểu diễn, định lý Noether nối đối xứng với bảo toàn ra sao, và sự khác biệt then chốt giữa đối xứng toàn cục với đối xứng gauge. Nên đọc kèm bài [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/) và [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa không chính thức một **nhóm Lie** (vừa là nhóm vừa là đa tạp trơn, và các phép toán nhóm là trơn).
- Giải thích vì sao vật lý quan tâm đến **biểu diễn**: các hạt nằm trong không gian biểu diễn, chứ không chỉ trong nhóm trừu tượng.
- Phát biểu ý chính của **định lý Noether**: mỗi đối xứng liên tục ứng với một dòng, một đại lượng được bảo toàn.
- Kể tên các thành phần $$U(1)$$, $$SU(2)$$, $$SU(3)$$ của Mô hình Chuẩn và lực, tích tương ứng (siêu tích, rồi điện từ sau khi trộn; spin đồng vị yếu; màu).
- Phân biệt **đối xứng toàn cục** và **đối xứng gauge** ở mức "đối xứng vật lý hay phần dư thừa trong cách mô tả", không cần đến hình thức BRST.
- Tránh các cách nói sai: "$$SU(3)$$ chỉ có nghĩa là có ba quark", "đối xứng là phương trình trông đẹp", "gauge chỉ là một pha toàn cục".

**Kiến thức nền.** Phép nhân ma trận; giá trị riêng của ma trận Hermite; số phức. [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

---

## Kiến thức cần nhớ: Lý thuyết nhóm Lie và lý thuyết biểu diễn là gì, nghiên cứu những gì?

Khi nhắc đến "đối xứng", ta thường nghĩ đến một bông tuyết hay hình vuông: xoay $$90^\circ$$ nó trùng khít chính nó — đó là **nhóm hữu hạn (đối xứng rời rạc)**. Nhưng một hình tròn hay quả cầu có thể xoay đi một góc **bất kỳ** $$\theta \in [0, 2\pi)$$ một cách mượt mà, liên tục không đứt quãng!

Cuối thế kỷ XIX, nhà toán học Na Uy Sophus Lie đã kết hợp hai ngành tưởng chừng tách biệt — **đại số** (cấu trúc nhóm) và **giải tích/hình học** (đa tạp trơn để lấy đạo hàm) — để tạo ra **nhóm Lie (Lie group)**:

1. **Nhóm Lie:** một họ các phép biến đổi đối xứng thay đổi trơn tru theo tham số liên tục (như tập mọi phép quay 3D $$SO(3)$$, hay tập các ma trận unita $$SU(n)$$).
2. **Đại số Lie:** thay vì phải xử lý cả nhóm Lie cong phức tạp, ta chỉ cần phóng to sát quanh phép biến đổi đơn vị (xoay một góc vô cùng bé $$\varepsilon$$). Tập các "vận tốc xoay tức thời" đó lập thành một không gian vectơ phẳng gọi là **đại số Lie**, nơi mọi thứ trở lại tuyến tính gọn gàng — kèm theo phép giao hoán tử $$[X,Y] = XY - YX$$ ghi nhớ việc thứ tự xoay có quan trọng hay không!
3. **Lý thuyết biểu diễn (Representation Theory):** nghiên cứu mọi cách có thể để hiện thực hóa một nhóm trừu tượng thành các **ma trận** tác động lên không gian vectơ $$V$$. Nhờ đó ta phân rã được không gian phức tạp thành những "khối nguyên tử" bất khả quy — và trong cơ học lượng tử, mỗi khối bất khả quy đó chính là một **họ hạt cơ bản**!

---

## 1. Nhóm, họ liên tục và đại số Lie

**Nhóm** là một tập hợp có phép nhân kết hợp, có phần tử đơn vị và phần tử nghịch đảo; đó là ngôn ngữ đại số của mọi phép đối xứng có thể ghép nối tiếp nhau. **Nhóm Lie** là nhóm đồng thời là một đa tạp trơn, tiêu biểu là:
- $$U(1)$$: các số phức có mô-đun bằng 1 ($$e^{i\theta}$$, hình học là một đường tròn).
- $$SO(3)$$: các ma trận quay $$3\times 3$$ trong không gian 3D.
- $$SU(n)$$: các ma trận phức unita $$n\times n$$ ($$U^\dagger U = I$$) có định thức bằng 1.

### Ví dụ làm từng bước: Tự tính ma trận quay $$SO(2)$$, $$SO(3)$$ và kiểm chứng móc Lie $$[L_x, L_y] = L_z$$

1. **Từ Đại số Lie lên Nhóm Lie với phép quay 2D $$SO(2)$$:** xét ma trận sinh $$J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$. Ta tính các lũy thừa của $$J$$: $$J^2 = -I$$, $$J^3 = -J$$, $$J^4 = I$$ (giống hệt số phức $$i$$!). Thay vào chuỗi mũ ma trận $$\exp(\theta J) = \sum_{k=0}^\infty \frac{\theta^k}{k!}J^k$$:
$$
\exp(\theta J) = \left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right)I + \left(\theta - \frac{\theta^3}{3!} + \cdots\right)J = (\cos\theta)I + (\sin\theta)J = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = R(\theta)!
$$
Chỉ một ma trận phẳng $$J$$ đã sinh ra toàn bộ nhóm quay cong $$SO(2)$$!
2. **Vì sao phép quay 3D $$SO(3)$$ không giao hoán:** ba phép quay vô cùng bé quanh trục $$x, y, z$$ ứng với ba ma trận sinh $$3\times 3$$:
$$
L_x = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad
L_y = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ -1 & 0 & 0 \end{pmatrix}, \qquad
L_z = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.
$$
Nhân trực tiếp hai ma trận đầu:
$$
L_x L_y = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad
L_y L_x = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\implies
[L_x, L_y] = L_x L_y - L_y L_x = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = L_z!
$$
Hiệu giữa "xoay quanh $$x$$ rồi $$y$$" với "xoay quanh $$y$$ rồi $$x$$" không bằng 0 mà tạo ra đúng **một phép quay quanh trục $$z$$**! Chính cấu trúc giao hoán tử không bằng 0 đó là trái tim đại số của mômen động lượng lượng tử và các lực Yang–Mills ($$SU(2), SU(3)$$).

**Ví dụ $$SU(2)$$ và bí ẩn spin-$$1/2$$.** Nhóm $$SU(2)$$ gồm các ma trận phức unita $$2\times 2$$ định thức 1. Đại số Lie của nó có 3 chiều (sinh bởi 3 ma trận Pauli), và có cấu trúc móc Lie **đẳng cấu hoàn toàn** với đại số của phép quay 3D $$SO(3)$$. Tuy nhiên, $$SU(2)$$ phủ $$SO(3)$$ tới **2 lần** (hai ma trận $$+I$$ và $$-I$$ trong $$SU(2)$$ ứng với cùng một phép quay $$0^\circ$$ trong 3D). Đó là lý do toán học sâu xa khiến một hạt electron (spin-$$1/2$$) khi quay đủ $$360^\circ$$ vẫn bị đổi dấu hàm sóng ($$\psi \to -\psi$$), phải quay đủ **$$720^\circ$$** mới trở lại đúng trạng thái ban đầu!

---

## 2. Biểu diễn: nơi các hạt "sống"

Một nhóm trừu tượng tự nó chưa nói lên vật lý; nó chỉ trở thành vật lý khi **tác động lên không gian trạng thái lượng tử**. Một **biểu diễn tuyến tính** là một đồng cấu

$$
\rho: G \to GL(V)
$$

gán cho mỗi phép đối xứng $$g\in G$$ một ma trận khả nghịch tác động lên không gian vectơ $$V$$.

- **Biểu diễn bất khả quy (irreducible representation):** những khối không gian con không thể tách nhỏ hơn nữa dưới tác động của $$G$$ — trong vật lý hạt, đây chính là các **họ hạt cơ bản (multiplet)**.
- **Tích tensor:** mô tả cách ghép nhiều hạt lại với nhau (chẳng hạn ghép 3 quark trong biểu diễn 3 chiều của $$SU(3)$$ cho ra phân rã $$\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$$ — con số **10** đó chính là tam giác 10 hạt mà Gell-Mann dùng để tiên đoán hạt $$\Omega^-$$!).

### Giải thích: Từ một phép đối xứng trừu tượng đến hạt cơ bản và lực tương tác

1. **Nhận diện nhóm đối xứng liên tục $$G$$:** tự nhiên bất biến dưới các phép quay không gian, tịnh tiến thời gian và các phép xoay pha nội tại ($$U(1), SU(2), SU(3)$$).
2. **Nếu đối xứng là toàn cục → Định lý Noether sinh ra định luật bảo toàn:** mỗi chiều của đại số Lie cho ra một đại lượng bảo toàn (năng lượng, động lượng, điện tích), còn các **biểu diễn bất khả quy** phân loại các hạt thành những họ (multiplet) rõ ràng.
3. **Nâng lên đối xứng địa phương (gauge) → Xuất hiện trường lực:** cho phép tham số đối xứng $$g(x)$$ thay đổi tự do tại từng điểm không–thời gian buộc ta phải thêm một **trường liên thông** $$A_\mu$$ vào đạo hàm hiệp biến — mỗi phần tử sinh của đại số Lie trở thành một **hạt truyền lực** ($$1 + 3 + 8 = 12$$ boson gauge!).
4. **Cơ chế phá vỡ đối xứng tự phát (Higgs) hoàn thiện bức tranh khối lượng:** phương trình vẫn đối xứng nhưng chân không chọn một trạng thái cụ thể, trao khối lượng cho $$W^\pm, Z^0$$ và giữ photon không khối lượng.

**Kiểm tra nhanh.** Một nhóm Lie không phải là "hình dạng của hạt"; nó là **quy tắc biến đổi**, còn các hạt cơ bản sống trong **các không gian biểu diễn** chịu tác động của nhóm đó.

---

## 3. Định lý Noether (phát biểu ý chính)

Năm 1918, Emmy Noether chứng minh một trong những định lý sâu sắc nhất toàn bộ vật lý toán: **mỗi đối xứng liên tục của định luật tự nhiên (tác dụng) luôn tương ứng 1-1 với một định luật bảo toàn.**

| Đối xứng liên tục | Ý nghĩa trực quan | Đại lượng bảo toàn tương ứng |
|---|---|---|
| Tịnh tiến theo thời gian | Thí nghiệm hôm nay giống hệt hôm qua | **Năng lượng** |
| Tịnh tiến trong không gian | Thí nghiệm ở Hà Nội giống hệt ở Paris | **Động lượng** |
| Phép quay trong không gian ($$SO(3)$$) | Vũ trụ không có hướng ưu tiên | **Mômen động lượng** |
| Xoay pha phức toàn cục ($$U(1)$$) | Đổi pha hàm sóng $$\psi \mapsto e^{i\alpha}\psi$$ | **Điện tích** |

Trong lý thuyết trường, bảo toàn mang dạng phương trình liên tục địa phương $$\partial_\mu j^\mu=0$$ (điện tích hay năng lượng không thể biến mất ở đây rồi đột ngột hiện ra ở thiên hà khác mà phải chảy liên tục qua biên). Định lý Noether là cây cầu vàng nối **hình học đối xứng** với **bảng kiểm kê bảo toàn**.

---

## 4. Đối xứng gauge và đối xứng toàn cục

| | Đối xứng toàn cục | Đối xứng gauge (địa phương) |
|--|-------------------|-----------------|
| Phép biến đổi | Cùng một phần tử nhóm $$g$$ cố định cho toàn bộ vũ trụ | $$g(x)$$ thay đổi tự do theo từng điểm không–thời gian |
| Ý nghĩa | Đối xứng vật lý thật sự của hệ | **Sự dư thừa trong cách chọn tọa độ/quy ước** (cả một quỹ đạo gauge mô tả đúng một trạng thái vật lý) |
| Hệ quả | Đại lượng bảo toàn (Noether); phân nhóm hạt | Đòi hỏi xuất hiện **trường liên thông (trường lực)** để so sánh pha giữa các điểm |

**Trực giác cực đẹp: vì sao đối xứng gauge lại gắn liền với các lực?** Giả sử bạn có thể tự do xoay pha $$e^{i\lambda(x)}$$ của trường electron độc lập tại *mỗi điểm* $$x$$ khác nhau trong không–thời gian. Khi lấy đạo hàm $$\partial_\mu \psi$$ (so sánh $$\psi$$ ở hai điểm sát nhau), đạo hàm thường sẽ hỏng vì hai điểm đang dùng hai quy ước pha khác nhau! Muốn phép đạo hàm có ý nghĩa hình học, bạn *bắt buộc* phải đưa thêm một trường bù $$A_\mu$$ biến đổi theo $$A_\mu \mapsto A_\mu + \partial_\mu \lambda$$ vào đạo hàm hiệp biến $$D_\mu = \partial_\mu - ieA_\mu$$. Trường bù $$A_\mu$$ ấy hóa ra chính là **trường điện từ (hạt photon)**! Lý thuyết Yang–Mills tổng quát hóa chính ý tưởng này từ nhóm giao hoán $$U(1)$$ sang các nhóm không giao hoán $$SU(2), SU(3)$$.

**Cơ chế Higgs (trong một câu).** Các phương trình của lực điện yếu hoàn toàn đối xứng, nhưng trạng thái chân không năng lượng thấp nhất lại tự chọn một hướng cụ thể (phá vỡ đối xứng tự phát), trao khối lượng cho các hạt truyền lực yếu $$W^\pm, Z^0$$ trong khi vẫn giữ cho hạt photon không khối lượng.

---

## 5. Nhóm của Mô hình Chuẩn

Toàn bộ ba lực phi hấp dẫn đã biết trong vũ trụ được tổ chức bởi tích trực tiếp của ba nhóm Lie compact:

$$
\begin{aligned}
SU(3)_c &\quad \text{lực mạnh / màu (QCD — giữ các quark dính chặt trong proton, neutron)}\\
SU(2)_L &\quad \text{isospin yếu (tác động lên các fermion tay trái)}\\
U(1)_Y &\quad \text{siêu tích (trộn với thành phần trung hòa của }SU(2)_L\text{ tạo thành điện từ)}
\end{aligned}
$$

**Một phép đếm đẹp đến kinh ngạc từ số chiều đại số Lie!** Với mỗi nhóm gauge $$G$$, số loại hạt boson truyền lực bằng đúng **số chiều của đại số Lie** ($$\dim U(1) = 1$$ và $$\dim SU(n) = n^2 - 1$$):
- $$U(1)_Y$$ có $$1$$ phần tử sinh, $$SU(2)_L$$ có $$2^2 - 1 = 3$$ phần tử sinh → sau cơ chế Higgs trộn lại thành đúng **4 hạt truyền lực điện yếu**: photon ($$\gamma$$), $$W^+$$, $$W^-$$ và $$Z^0$$.
- $$SU(3)_c$$ có $$3^2 - 1 = 8$$ phần tử sinh → tương ứng đúng **8 loại hạt gluon** truyền lực hạt nhân mạnh!
Tổng cộng đúng **12 hạt truyền lực cơ bản** của tự nhiên, đọc ra trực tiếp từ công thức $$1 + 3 + 8 = 12$$ của lý thuyết nhóm Lie!

Quark sống trong biểu diễn tam tuyến màu (3 chiều) của $$SU(3)_c$$, còn lepton (như electron, neutrino) là đơn tuyến màu (1 chiều, nên không cảm nhận lực mạnh). Đây không phải chi tiết trang trí mà là **lý thuyết biểu diễn chạy ở quy mô toàn vũ trụ**.

---

## 6. Những lĩnh vực toán học được nuôi dưỡng bởi cùng ý tưởng

- Lý thuyết cấu trúc và phân loại hoàn chỉnh các đại số Lie nửa đơn (Cartan, Killing, sơ đồ Dynkin — một trong những thành tựu đẹp nhất thế kỷ XX).  
- Vành biểu diễn và phạm trù tensor (nay dùng cho hạt giả anyon và điện toán lượng tử tôpô).  
- Các nhóm và đại số vô hạn chiều (đại số Virasoro, Kac–Moody) trong lý thuyết trường bảo giác (CFT).  
- Đối ngẫu giữa nhóm $$G$$ và nhóm đối ngẫu Langlands $$G^\vee$$ kết nối vật lý đối ngẫu điện–từ với lý thuyết số ([Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)).

Vật lý hạt không phát minh ra lý thuyết Lie, nhưng suốt một thế kỷ nó đã biến lý thuyết biểu diễn thành kính hiển vi sắc bén nhất để đọc mã nguồn tự nhiên, đồng thời tặng lại cho toán học vô số bài toán sâu sắc mới.

---

## 7. Phân biệt chính xác và cường điệu

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Vũ trụ là $$SU(3)$$." | Đơn giản hóa quá mức | $$SU(3)$$ chỉ là một thành phần của nhóm gauge mô tả các lực đã biết; không phải "lý thuyết của mọi thứ". |
| "Đối xứng gauge sinh ra lực." | Thô | Bất biến gauge cộng với tính địa phương dẫn đến liên thông; động lực học còn cần một tác dụng (Yang–Mills, …). |
| "Mọi đối xứng đều là nhóm Lie." | Sai | Các đối xứng rời rạc cũng quan trọng. |
| "Biểu diễn là hình vẽ đẹp về hạt." | Thiếu | Đó là tác động tuyến tính trên không gian trạng thái, cho ra các số lượng tử đo được. |

---

## Tài liệu tham khảo

1. Hall — *Lie Groups, Lie Algebras, and Representations*.  
2. Georgi — *Lie Algebras in Particle Physics*.  
3. Khóa học: [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/), [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/), [Yang–Mills mass gap]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/).  
