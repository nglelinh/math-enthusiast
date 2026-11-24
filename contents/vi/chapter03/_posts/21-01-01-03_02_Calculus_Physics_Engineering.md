---
layout: post
title: "Giải tích → Vật lý & Kỹ thuật"
chapter: '03'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Hãy hình dung bạn đang lái xe qua một cây cầu dây văng dài hàng cây số giữa cơn gió giật mạnh. Hàng trăm nghìn tấn bê tông và thép đang rung nhẹ dưới bánh xe bạn, từng sợi cáp kéo căng lên rồi chùng xuống theo từng nhịp gió. Vì sao cây cầu không cộng hưởng rồi sụp đổ như cầu Tacoma Narrows năm 1940? Không phải vì kỹ sư chỉ "áp vài công thức có sẵn". Nó đứng vững vì tại **mỗi milimét thép và từng phần nghìn giây**, tốc độ biến thiên cục bộ của ứng suất và chuyển vị phải tuân theo các định luật cân bằng — và các kỹ sư đã tích phân những phương trình vi phân đó để biết trước cây cầu sẽ uốn cong bao nhiêu trước khi đổ viên bê tông đầu tiên.

Theo nghĩa đó, giải tích không nằm trên trang giấy thi đại học; giải tích chính là phần khung xương vô hình nâng đỡ mọi cây cầu, máy bay, mạch điện và nhà máy điện quanh ta.

Bài học này không dạy lại bảng công thức đạo hàm phổ thông. Thay vào đó, chúng ta sẽ đi theo mạch tư duy sâu hơn: **vì sao giải tích trở thành ngôn ngữ mẹ đẻ của vật lý cổ điển và kỹ thuật hiện đại**, và bằng cách nào những phương trình viết trên không gian liên tục lại biến thành các phần mềm mô phỏng công nghiệp đang chạy mỗi ngày.

**Lộ trình:** bản đồ ngành giải tích → tốc độ và tích lũy → định lý cơ bản → định luật Newton và ODE → thêm biến không gian (PDE) → định luật bảo toàn → giải tích vectơ (gradient, divergence, curl) → tư duy biến phân → phương pháp phần tử hữu hạn (FEM) → các ngành kỹ thuật và những nhầm lẫn thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích đạo hàm và tích phân là hai phép toán ngược nhau, được nối với nhau bởi định lý cơ bản của giải tích.
- Viết định luật hai Newton dưới dạng phương trình vi phân, và hiểu lực, khối lượng, gia tốc trong cách viết đó.
- Phân biệt phương trình vi phân thường (ODE) và phương trình đạo hàm riêng (PDE); nêu các ví dụ chuẩn (phương trình nhiệt, phương trình sóng, phương trình Laplace).
- Mô tả ngắn gọn cách **phương pháp phần tử hữu hạn (FEM)** biến một định luật cân bằng liên tục thành một bài toán đại số tuyến tính cỡ lớn.
- Kể tên ba ngành kỹ thuật dùng giải tích thường xuyên và nói rõ trong mỗi ngành, *đại lượng nào* được lấy đạo hàm hay tích phân.
- Tránh hai nhầm lẫn: "giải tích chỉ là công thức ở phổ thông" và "phần mềm đã thay thế toán học".

**Kiến thức nền.** Trực giác giải tích ở phổ thông (độ dốc, diện tích). Biết về hàm nhiều biến sẽ có ích cho phần PDE.

**Liên kết.** [Phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes (Ch.1)]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), và bài Fourier trong chương này.

---

## Bản đồ kiến thức nền: Giải tích và giải tích vectơ là gì, nghiên cứu những gì?

Khi rời khỏi phổ thông, nhiều người nhớ giải tích như một loạt bài tập tìm cực trị hàm bậc ba hay tính diện tích hình phẳng. Nhưng ở tầm đại học và trong khoa học tự nhiên, **giải tích (calculus / mathematical analysis)** là ngành toán học nghiên cứu **sự thay đổi liên tục** và **cách cộng dồn vô hạn những mảnh vô cùng nhỏ**.

Cấu trúc của ngành này mở rộng theo ba tầng tự nhiên:

1. **Giải tích một biến:** nghiên cứu một đại lượng thay đổi theo một biến duy nhất (như vị trí theo thời gian). Hai trụ cột là *đạo hàm* (phóng đại cục bộ đến mức đường cong trông như đường thẳng) và *tích phân* (cắt nhỏ rồi cộng dồn).
2. **Giải tích nhiều biến & Giải tích vectơ:** thế giới thật có ba chiều không gian cộng thêm thời gian. Nhiệt độ, áp suất, điện trường hay vận tốc gió không phải một con số mà là các **trường** biến thiên khắp không gian. Giải tích vectơ phát minh ra các toán tử gradient, divergence, curl và các định lý tích phân (Gauss, Stokes) để liên kết những gì xảy ra *bên trong* một khối thể tích với dòng chảy đi qua *bề mặt biên* của nó.
3. **Phương trình vi phân & Phép tính biến phân:** thay vì tìm một con số $$x$$, ta đi tìm cả một *hàm số* $$u(x,t)$$ — chẳng hạn hình dạng võng xuống của cả một cây cầu hay phân bố nhiệt độ trên cả một cánh tua-bin — sao cho nó thỏa mãn quy luật cân bằng vật lý hoặc làm cực tiểu năng lượng.

Nói ngắn gọn: **tự nhiên hiếm khi viết ra đáp án cuối cùng; tự nhiên chỉ viết ra quy luật thay đổi cục bộ.** Giải tích là chiếc cầu nối từ quy luật cục bộ ấy đến hành vi toàn cục mà kỹ sư có thể đo đạc và thiết kế.

---

## 1. Hai ý tưởng, một bộ máy

**Đạo hàm** trả lời câu hỏi: tại *đúng khoảnh khắc này*, một đại lượng đang thay đổi nhanh đến mức nào? Vận tốc là đạo hàm của vị trí; cường độ dòng điện là tốc độ thay đổi của điện tích; chi phí biên trong kinh tế là đạo hàm của tổng chi phí.

**Tích phân** trả lời câu hỏi ngược lại: nếu biết tốc độ thay đổi ở từng khoảnh khắc nhỏ, thì sau cả một khoảng thời gian, tổng cộng đại lượng đó đã tích lũy được bao nhiêu? Quãng đường là tích phân của vận tốc; công cơ học là tích phân của lực dọc theo đường đi; tổng nhiệt lượng là tích phân của mật độ nhiệt trên toàn bộ vật thể.

**Ví dụ trực quan bằng số.** Giả sử một chiếc ô tô tăng tốc đều từ trạng thái đứng yên với vận tốc $$v(t) = 2t\text{ (m/s)}$$. Sau $$t=5$$ giây, vận tốc tức thời là $$10\text{ m/s}$$, nhưng quãng đường đi được không phải $$10 \times 5 = 50\text{ m}$$, mà là diện tích tam giác dưới đường thẳng $$v(t)$$: $$\int_0^5 2t\,dt = \left. t^2 \right|_0^5 = 25\text{ m}$$. Nhờ biết nguyên hàm $$F(t)=t^2$$ có đạo hàm đúng bằng $$2t$$, ta không cần cộng hàng triệu đoạn đường siêu nhỏ bằng tay.

**Định lý cơ bản của giải tích** nối hai ý tưởng này thành một bộ máy duy nhất: với các giả thiết phù hợp, lấy đạo hàm và lấy tích phân là hai phép toán ngược nhau:

$$
\int_a^b f(x)\,dx = F(b)-F(a)\quad\text{khi }F'=f.
$$

**Vì sao định lý này lại hữu ích đến thế?** Vì trước Newton và Leibniz, muốn tính diện tích một hình cong hay thể tích một thùng rượu, người ta phải nghĩ ra một mẹo hình học riêng cho từng hình. Định lý cơ bản biến bài toán cộng dồn vô hạn cực khó thành bài toán tìm ngược đạo hàm — và đặt nền móng cho toàn bộ vật lý hiện đại.

Tóm lại: **giải tích là ngôn ngữ toán học của sự thay đổi liên tục.**

---

## 2. Từ hình học đến động lực học

Về lịch sử, giải tích ra đời từ các bài toán hình học (vẽ tiếp tuyến, đo diện tích) rồi nhanh chóng trở thành động cơ của **động lực học**. Newton và Leibniz không chỉ nghĩ ra vài mẹo tính toán; họ tạo ra một ngôn ngữ để biến các định luật tự nhiên thành phương trình có thể giải được.

**Định luật hai Newton** trong một chiều,

$$
m \frac{d^2 x}{dt^2} = F\bigl(x,\tfrac{dx}{dt},t\bigr),
$$

đã là một phương trình vi phân: ẩn số không còn là một con số mà là cả một *hàm số* $$x(t)$$.

**Ví dụ cụ thể: hệ giảm xóc ô tô.** Khi bánh xe đi qua một gờ giảm tốc, lò xo kéo bánh xe về vị trí cân bằng với lực $$-kx$$, còn ống giảm chấn cản chuyển động với lực $$-c\frac{dx}{dt}$$. Định luật Newton lập tức cho ra phương trình:

$$
m\frac{d^2 x}{dt^2} + c\frac{dx}{dt} + kx = 0.
$$

Chỉ cần nhìn vào tỉ lệ giữa hệ số cản $$c$$ và độ cứng lò xo $$k$$ (thông qua nghiệm phương trình đặc trưng), kỹ sư biết ngay xe sẽ nảy lên xuống nhiều lần gây say xe (thiếu cản), trở về êm ái nhanh nhất (cản tới hạn), hay cứng nhắc (quá cản) — **trước khi chế tạo bất kỳ chiếc lò xo nào**.

**Tóm tắt trong một câu.**  
*Các định luật vật lý thường cho biết tốc độ thay đổi của trạng thái phụ thuộc vào chính trạng thái đó; giải phương trình vi phân cho phép dự đoán tương lai từ điều kiện ban đầu.*

---

## 3. ODE và PDE: khi có thêm biến không gian

**ODE (phương trình vi phân thường)** chỉ có đạo hàm theo một biến độc lập (thường là thời gian $$t$$). Hệ khối lượng – lò xo – giảm chấn hay mạch điện RLC là ODE vì ta chỉ cần theo dõi vài con số (vị trí, dòng điện) theo thời gian.

**PDE (phương trình đạo hàm riêng)** xuất hiện khi đại lượng thay đổi đồng thời theo cả *không gian* lẫn *thời gian*. Hãy tưởng tượng một thanh sắt dài được nung nóng ở giữa. Nhiệt độ $$u(x,t)$$ phụ thuộc vào cả vị trí $$x$$ dọc theo thanh lẫn thời điểm $$t$$. Phương trình nhiệt mô tả quá trình đó:

$$
\partial_t u = \kappa \Delta u.
$$

**Trực giác của toán tử Laplace $$\Delta u$$.** Trong một chiều, $$\Delta u = \frac{\partial^2 u}{\partial x^2}$$ đo *độ cong* của đồ thị nhiệt độ — nói cách khác, nó đo xem điểm $$x$$ đang nóng hơn hay lạnh hơn trung bình hai điểm lân cận. Nếu điểm $$x$$ là một "đỉnh nóng" (nóng hơn xung quanh), độ cong âm ($$\Delta u < 0$$), nên $$\partial_t u < 0$$: nhiệt độ tại đó lập tức giảm xuống! Ngược lại, ở "thung lũng lạnh", độ cong dương nên nhiệt độ tăng lên. Phương trình nhiệt nói một điều cực kỳ tự nhiên: **nhiệt luôn tự san phẳng các đỉnh và lấp đầy các hõm**.

Tương tự, phương trình sóng $$\partial_{tt}u=c^2\Delta u$$ truyền nhiễu động (âm thanh, rung động dây đàn, sóng điện từ) đi với tốc độ hữu hạn $$c$$. Còn phương trình Laplace $$\Delta u=0$$ mô tả trạng thái cân bằng tĩnh, khi mọi thứ đã ngừng thay đổi theo thời gian.

**Vì sao ngành công nghệ quan tâm.** ODE là mô hình chính cho mạch điện phần tử tập trung, cơ học vật rắn và nhiều vòng điều khiển. PDE là mô hình chính cho các trường liên tục: nhiệt, ứng suất, điện từ (phương trình Maxwell), chất lỏng (Navier–Stokes). "Mô phỏng" trong công nghiệp thực chất gồm ba bước: rời rạc hóa PDE, giải một hệ phương trình đại số lớn, rồi hiển thị kết quả. Tất cả vẫn là giải tích kết hợp với giải tích số.

---

## 4. Định luật bảo toàn, thông lượng và mô hình môi trường liên tục

Làm sao các nhà vật lý biết viết ra đúng phương trình nhiệt hay phương trình Navier–Stokes? Hầu hết các mô hình môi trường liên tục đều được xây dựng theo cùng một khuôn bốn bước cực kỳ nhất quán:

1. **Chọn một đại lượng bảo toàn** (khối lượng, năng lượng, động lượng, điện tích).  
2. **Viết định luật cân bằng dạng tích phân:** tốc độ tăng của đại lượng bên trong một hộp tưởng tượng $$\Omega$$ phải bằng lượng chảy vào qua vỏ hộp (thông lượng qua biên $$\partial\Omega$$) cộng với nguồn sinh ra bên trong.  
3. **Chuyển từ tích phân sang PDE nhờ định lý phân kỳ** (định lý Green, Stokes, Gauss cùng một họ; xem [Vật lý toán / Stokes→Maxwell]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/)). Định lý này biến tích phân trên mặt biên thành tích phân trên thể tích; cho hộp thu nhỏ lại về một điểm, ta thu được một phương trình vi phân đúng tại *mọi điểm*.  
4. **Đóng hệ phương trình bằng một định luật cấu thành** mang tính thực nghiệm của vật liệu (định luật Fourier: dòng nhiệt chảy từ nóng sang lạnh $$\mathbf{q} = -k\nabla u$$; định luật Hooke: ứng suất tỉ lệ với biến dạng; định luật Ohm; …).

Với truyền nhiệt: ghép cân bằng năng lượng ($$\partial_t u + \nabla\cdot \mathbf{q} = 0$$) với định luật Fourier ($$\mathbf{q} = -k\nabla u$$), ta thu ngay phương trình nhiệt $$\partial_t u = \kappa \Delta u$$. Toán học ở đây không phải để trang trí: định lý phân kỳ chính là cầu nối biến phép "cân đối sổ sách vào – ra" thành một PDE.

**Tóm tắt.** *Định luật bảo toàn cộng với định luật cấu thành cho ra PDE; hình dạng miền và điều kiện biên chọn ra nghiệm có ý nghĩa vật lý.*

---

## 5. Gradient, divergence và curl (công cụ của giải tích vectơ)

Các mô hình môi trường liên tục được viết bằng ngôn ngữ **trường**. **Trường vô hướng** gán một số cho mỗi điểm (nhiệt độ, độ cao). **Trường vectơ** gán một vectơ cho mỗi điểm (gió, vận tốc dòng chảy). Có ba toán tử xây dựng từ ký hiệu nabla $$\nabla$$ xuất hiện ở khắp nơi trong vật lý và kỹ thuật.

### Trường vô hướng và trường vectơ

| Đối tượng | Ý nghĩa | Ví dụ |
|-----------|---------|--------|
| Vô hướng | Chỉ có độ lớn | Nhiệt độ $$30^\circ\mathrm{C}$$ |
| Vectơ | Có độ lớn và hướng | Gió 10 đơn vị về hướng đông |
| Trường vô hướng | Một số tại mỗi điểm | Bản đồ nhiệt độ $$T(x,y)$$ |
| Trường vectơ | Một vectơ tại mỗi điểm | Bản đồ gió $$\mathbf{v}(x,y)$$ |

![Trường vector]({{ site.baseurl }}/img/chapter_img/veccalc_vector_field_example_bs.jpg)

*Hình. Trường vectơ $$\mathbf{v}(x,y)=(2x,y)$$ (nguồn: Brain Station Advanced).*

### Gradient: hướng dốc lên nhanh nhất

$$
\nabla f = \Bigl(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\ldots\Bigr).
$$

**Trực giác.** Hãy tưởng tượng bạn đang đứng trên một sườn núi có bản đồ độ cao $$f(x,y)$$. Vectơ $$\nabla f$$ chỉ theo hướng bạn phải bước để **leo lên dốc nhanh nhất**, và độ dài của nó cho biết con dốc đứng đến mức nào. Quả bóng thả tay sẽ tự lăn theo hướng ngược lại $$-\nabla f$$ (xuống dốc nhanh nhất — đây cũng chính là ý tưởng của thuật toán gradient descent trong AI).  
**Ví dụ.** Với mặt paraboloid $$f(x,y)=x^2+y^2$$, tại điểm $$(1,2)$$ ta có $$\nabla f=(2,4)$$. Nghĩa là đi theo hướng $$(2,4)$$ sẽ làm độ cao tăng nhanh nhất, với độ dốc bằng $$\sqrt{2^2+4^2}=\sqrt{20}\approx 4{,}47$$.

![Gradient lên dốc]({{ site.baseurl }}/img/chapter_img/veccalc_gradient_uphill_bs.jpg)

*Hình. Gradient của $$f=x^2+y^2$$ (cùng nguồn).*

### Divergence: nguồn, điểm hút và dòng không nén

$$
\nabla\cdot\mathbf{v} = \frac{\partial v_1}{\partial x}+\frac{\partial v_2}{\partial y}+\frac{\partial v_3}{\partial z}
$$

là một **số vô hướng**. Hãy hình dung một ô vuông nhỏ đặt trong dòng chảy:

| Dấu của $$\nabla\cdot\mathbf{v}$$ | Ý nghĩa |
|------------------------------|---------|
| $$>0$$ | Chảy ra nhiều hơn chảy vào → mật độ giảm (nguồn) |
| $$<0$$ | Chảy vào nhiều hơn chảy ra → mật độ tăng (điểm hút) |
| $$=0$$ | Vào bằng ra (dòng quay, hoặc dòng đều) |

**Ví dụ.** $$\mathbf{v}=(x,y)$$ có divergence $$=1+1=2$$ (tỏa ra mọi phía như vòi phun nước); $$\mathbf{v}=(-x,-y)$$ có divergence $$=-2$$ (hút vào tâm như lỗ thoát nước); trường quay $$\mathbf{v}=(-y,x)$$ hoặc trường hằng có divergence $$=0$$ (chất lỏng chảy nhưng không bị nén hay giãn).

![Nguồn]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_source_bs.jpg)

*Hình. Trường hướng ra ngoài: divergence dương (cùng nguồn video).*

![Sink]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_sink_bs.jpg)

*Hình. Trường hướng vào trong: divergence âm (cùng nguồn).*

![Dòng đều]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_uniform_bs.jpg)

*Hình. Dòng đều: $$\nabla\cdot\mathbf{v}=0$$ (cùng nguồn).*

Trong điện từ học, điện tích dương đóng vai trò **nguồn** của điện trường $$\mathbf{E}$$ (định luật Gauss: $$\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$$). Cùng với định lý phân kỳ, đây là bước biến định luật cân bằng dạng tích phân thành PDE (§4).

### Curl: độ xoáy cục bộ (thử bằng bánh xe cánh quạt)

Curl là **tích có hướng** $$\nabla\times\mathbf{v}$$, kết quả là một vectơ. Đặt một bánh xe cánh quạt tí hon cố định tâm vào dòng chảy: nếu dòng chảy hai bên không đều làm bánh xe quay tít thì curl khác 0 (và hướng của vectơ curl là trục quay theo quy tắc bàn tay phải); nếu dòng chỉ đẩy bánh xe trôi đi mà không làm nó xoay quanh trục thì curl bằng 0.

![Curl]({{ site.baseurl }}/img/chapter_img/veccalc_curl_paddle_bs.jpg)

*Hình. Trường quay và trực giác bánh xe cánh quạt (cùng nguồn).*

### Bảng tóm tắt

| Toán tử | Kết quả | Ý nghĩa vật lý |
|---------|--------|------------------|
| $$\nabla f$$ | vectơ | Hướng tăng nhanh nhất của trường vô hướng (lực sinh từ thế năng; định luật Fourier dùng $$-\nabla T$$) |
| $$\nabla\cdot\mathbf{v}$$ | vô hướng | Cường độ nguồn hoặc điểm hút (phương trình liên tục, định luật Gauss) |
| $$\nabla\times\mathbf{v}$$ | vectơ | Độ xoáy cục bộ (xoáy trong chất lỏng; cấu trúc của phương trình Maxwell) |

---

## 6. Nguyên lý biến phân

Thay vì viết cân bằng lực tại từng điểm, tự nhiên còn có một góc nhìn thanh lịch đến kinh ngạc: **nguyên lý biến phân**. Cấu hình vật lý thực tế chính là cấu hình làm cực tiểu (hoặc làm dừng) một đại lượng tổng thể gọi là *năng lượng* hay *tác dụng (action)*.

Hãy tưởng tượng bạn nhúng một khung dây uốn lượn vào nước xà phòng. Màng xà phòng tự căng ra thành một bề mặt mượt mà sao cho diện tích (năng lượng bề mặt) nhỏ nhất có thể. Theo nguyên lý Dirichlet, trong số tất cả các hàm $$u$$ khớp với độ cao của khung dây ở biên, hàm làm cực tiểu năng lượng đàn hồi

$$
E[u]=\frac12\int_\Omega\lvert\nabla u\rvert^2\,dx
$$

chính là nghiệm của phương trình Laplace $$\Delta u = 0$$ (với giả thiết phù hợp). Đó là bề mặt "êm phẳng nhất" có thể nối các điểm trên biên lại với nhau.

**Vì sao góc nhìn biến phân lại quý giá đến thế?** Vì với một khung cầu hay vỏ động cơ có hình dạng cực kỳ méo mó, ta gần như không bao giờ tìm được công thức giải tích cho PDE. Nhưng nếu bài toán là *tìm cực tiểu của năng lượng* $$E[u]$$, ta có thể xấp xỉ bề mặt $$u$$ bằng hàng nghìn mảnh tam giác phẳng rồi tìm giá trị độ cao tại các đỉnh để tổng năng lượng nhỏ nhất. Chuỗi bước công nghiệp là: **phép tính biến phân → ma trận thưa → bộ giải đại số tuyến tính**.

**Tóm tắt.** *Trạng thái cân bằng là điểm dừng của năng lượng; FEM xấp xỉ không gian hàm rồi tìm cực tiểu (hoặc giải dạng yếu tương đương).*

---

## 7. Phần tử hữu hạn: giải tích ở quy mô công nghiệp

Các phần mềm mô phỏng cơ khí như ANSYS, Abaqus hay COMSOL hoạt động thế nào khi tính xem một cánh máy bay có bị gãy không? Câu trả lời là **Phương pháp phần tử hữu hạn (FEM)**.

### Ví dụ cầm tay chỉ việc: Tự tay giải bài toán thanh đàn hồi 1D bằng FEM

Xét một thanh thép dài $$L = 2\text{ m}$$, độ cứng kéo $$EA = 10$$, gắn chặt tường ở đầu trái $$x=0$$ (tức $$u(0)=0$$) và chịu lực kéo $$F = 20\text{ N}$$ ở đầu phải $$x=2$$. Ta muốn tìm độ giãn $$u(x)$$ dọc theo thanh mà **chỉ dùng phép tính ma trận**:

1. **Chia lưới:** cắt thanh thành 2 phần tử bằng nhau dài $$h = 1\text{ m}$$, có 3 nút $$x_0=0,\ x_1=1,\ x_2=2$$ với chuyển vị $$u_0, u_1, u_2$$.
2. **Ma trận độ cứng từng phần tử:** mỗi đoạn dài $$h=1$$ hành xử như một lò xo có độ cứng $$k = \frac{EA}{h} = \frac{10}{1} = 10$$, ứng với ma trận phần tử $$2\times 2$$:
$$
K^{(e)} = \begin{pmatrix} 10 & -10 \\ -10 & 10 \end{pmatrix}.
$$
3. **Lắp ráp ma trận toàn cục $$3\times 3$$:** cộng đóng góp của phần tử 1 (nối nút 0–1) và phần tử 2 (nối nút 1–2); tại nút giữa $$x_1$$ cả hai phần tử cùng kéo nên hệ số là $$10+10=20$$:
$$
\begin{pmatrix} 10 & -10 & 0 \\ -10 & 20 & -10 \\ 0 & -10 & 10 \end{pmatrix}
\begin{pmatrix} u_0 \\ u_1 \\ u_2 \end{pmatrix}
=
\begin{pmatrix} R_0 \\ 0 \\ 20 \end{pmatrix}.
$$
4. **Áp điều kiện biên và giải hệ:** vì đầu trái ngàm cứng nên $$u_0 = 0$$. Bỏ hàng 1 và cột 1, ta còn hệ $$2\times 2$$ cho hai ẩn tự do:
$$
\begin{pmatrix} 20 & -10 \\ -10 & 10 \end{pmatrix}
\begin{pmatrix} u_1 \\ u_2 \end{pmatrix}
=
\begin{pmatrix} 0 \\ 20 \end{pmatrix}.
$$
Từ hàng 1: $$20u_1 - 10u_2 = 0 \implies u_2 = 2u_1$$. Thay vào hàng 2: $$-10u_1 + 10(2u_1) = 10u_1 = 20 \implies u_1 = 2,\ u_2 = 4$$! Thay ngược lại hàng 1 của hệ $$3\times 3$$ ta còn biết luôn phản lực tường $$R_0 = -10u_1 = -20\text{ N}$$ (cân bằng đúng với lực kéo $$+20\text{ N}$$). Kiểm chứng bằng giải tích: $$u(x) = \frac{F}{EA}x = 2x$$ cho đúng $$u(1)=2,\ u(2)=4$$!

Trong công nghiệp, thay vì 3 nút, phần mềm dùng 3 triệu nút tứ diện 3D — nhưng quy trình lắp ráp ma trận thưa $$KU=F$$ thì giống hệt ví dụ 4 bước trên!

### Khung giải thích: Từ định luật vật lý liên tục đến phần mềm mô phỏng FEM (nên đọc chậm)

1. **Từ cân bằng lực đến PDE:** viết định luật bảo toàn trên một khối nhỏ rồi dùng định lý phân kỳ để thu được phương trình vi phân (như $$-EA u'' = f$$).
2. **Chuyển sang dạng yếu (tích phân từng phần):** nhân PDE với một hàm thử $$v$$ rồi tích phân từng phần để hạ bậc đạo hàm từ bậc 2 xuống bậc 1 ($$\int EA u'v'\,dx = \int fv\,dx$$). Nhờ hạ bậc đạo hàm, các hàm đa thức gấp khúc từng mảnh trên lưới tam giác trở nên hoàn toàn hợp lệ!
3. **Chiếu xuống không gian hữu hạn chiều:** viết nghiệm xấp xỉ thành tổ hợp tuyến tính của các "hàm lều" đặt tại $$N$$ nút lưới. Phép tính vi phân vô hạn chiều lập tức biến thành hệ đại số tuyến tính $$KU=F$$ với ma trận $$K$$ đối xứng, thưa và xác định dương.
4. **Giải số và kiểm chứng vật lý:** máy tính giải $$KU=F$$ bằng phương pháp lặp (như Gradient Liên hợp), rồi kỹ sư kiểm tra xem tổng phản lực có cân bằng ngoại lực không và lưới mịn hơn có làm nghiệm hội tụ không.

**Kiểm tra nhanh.** FEM *không* vứt bỏ giải tích để thay bằng máy tính: dạng yếu và phép tích phân từng phần chính là giải tích, còn việc giải $$KU=F$$ là đại số tuyến tính số.

Các phương pháp cùng họ: sai phân hữu hạn (lưới đều, dễ hình dung), thể tích hữu hạn (bảo toàn thông lượng ở mức rời rạc, rất phổ biến trong mô phỏng dòng chảy CFD), phương pháp phổ (dùng chuỗi Fourier hoặc đa thức trực giao).

---

## 8. Các ngành kỹ thuật dùng giải tích

| Ngành | Giải tích dùng để làm gì |
|----------|------------------|
| Cơ khí | Ứng suất, dao động, đàn hồi, tiếp xúc |
| Điện | ODE cho mạch điện; PDE Maxwell, tĩnh điện |
| Xây dựng | Dầm, đường truyền tải trọng, FEM cho công trình |
| Hàng không | Động lực học bay; CFD (liên hệ [NS]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/)) |
| Nhiệt – hóa | Truyền nhiệt và truyền khối; phản ứng – khuếch tán |
| Điều khiển | Tuyến tính hóa; tính ổn định; biến đổi Laplace |

**Điều khiển tự động (ví dụ về tên lửa giữ thăng bằng):** một hệ phi tuyến $$\dot{x}=f(x,u)$$ (như tên lửa SpaceX hạ cánh thẳng đứng) được tuyến tính hóa quanh điểm cân bằng để thu được $$\dot{\xi}=A\xi+B\mu$$. Phần thực của các giá trị riêng của ma trận $$A$$ quyết định hệ tự ổn định (phần thực âm → sai lệch tắt dần theo hàm mũ $$e^{\lambda t}$$) hay lật nhào (phần thực dương → sai lệch phình to). Bộ điều khiển phản hồi dùng luật $$u=-K\xi$$ để dịch toàn bộ giá trị riêng sang nửa trái mặt phẳng phức. Đó là đại số tuyến tính cộng với ODE — và vẫn là giải tích.

---

## 9. Mô hình liên tục và "bản sao số" (digital twin)

Kỹ thuật hiện đại kết hợp cảm biến, mô hình giải tích và tối ưu hóa thành một vòng lặp khép kín: mô hình ODE/PDE → ước lượng trạng thái thực từ số liệu cảm biến (như bộ lọc Kalman) → tối ưu đầu vào hoặc cảnh báo bảo trì trước khi hỏng hóc. **Bản sao số (digital twin)** của một tua-bin gió hay một cây cầu lớn thực chất là một mô hình giải tích (hoặc mô hình thay thế rút gọn) được liên tục hiệu chỉnh bằng dữ liệu thật. Nó không phải phép màu tách rời khỏi PDE.

Giới hạn thực tế: dòng rối (turbulence), tiếp xúc cơ học, sự lan truyền vết nứt, dòng nhiều pha và các hiện tượng nhiều thang đo vẫn là thách thức hàng đầu cho cả lý thuyết lẫn siêu máy tính. **Tính đặt chỉnh (well-posedness)** — nghiệm có tồn tại, duy nhất và thay đổi liên tục khi dữ liệu nhiễu nhẹ hay không — là một khái niệm giải tích có hậu quả kỹ thuật sống còn: với một bài toán không đặt chỉnh (như bài toán ngược tìm nguồn nhiệt từ đo đạc mờ nhiễu), chia lưới mịn hơn không những không giúp ích mà còn làm nhiễu nổ tung.

---

## 10. Vì sao vẫn cần hiểu, khi phần mềm "tự giải"

1. Sai số do **chọn sai mô hình vật lý** thường lớn hơn rất nhiều so với sai số do rời rạc hóa.  
2. **Điều kiện biên** (ngàm cứng hay gối trượt? cách nhiệt hay đối lưu?) thể hiện giả định vật lý của bạn; phần mềm không thể đoán thay bạn.  
3. **Đưa về dạng không thứ nguyên** giúp lộ ra các con số quyết định bản chất dòng chảy hay truyền nhiệt (số Reynolds, số Fourier, số Mach…).  
4. Tính ổn định và tính "cứng" (stiff) khi tích phân theo thời gian là các khái niệm giải tích (chọn bước thời gian, dùng phương pháp ẩn hay hiện để nghiệm không bị nổ số học).  
5. Muốn kiểm chứng và thẩm định kết quả, kỹ sư phải ước lượng được bài toán liên tục *đáng lẽ* cho đáp án cỡ nào trước khi tin vào những bức ảnh màu rực rỡ trên màn hình.

Chuỗi tổng quát: **cân bằng vật lý → phương trình vi phân → phân tích lý thuyết và tính toán số → quyết định thiết kế.**

---

### Tóm tắt giải tích vectơ (từ phần tìm hiểu video)

Video trực quan chính: [Brain Station — Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (khoảng 15 phút).

- **Gradient:** $$\nabla f$$ là vectơ gồm các đạo hàm riêng; nó chỉ hướng **lên dốc** (tăng nhanh nhất). Muốn xuống dốc thì dùng $$-\nabla f$$.
- **Divergence:** $$\nabla\cdot\mathbf{v}$$ là một *số vô hướng*. Dương nghĩa là có nguồn, âm nghĩa là có điểm hút, bằng không nghĩa là thể tích được bảo toàn (chất lỏng vẫn có thể chuyển động).
- **Curl:** $$\nabla\times\mathbf{v}$$ đo độ xoáy cục bộ (thử bằng một bánh xe cánh quạt nhỏ).
- Xem thêm [Essence of calculus — 3Blue1Brown](https://www.youtube.com/watch?v=WUvTyaaNkzM) để nắm định lý cơ bản trước khi học các toán tử vectơ.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Giải tích chỉ để đi thi." | Giải tích là ngôn ngữ mô tả sự thay đổi liên tục trong vật lý và kỹ thuật. |
| "Phần mềm hội tụ thì mô hình đúng." | Hội tụ là chuyện tính toán số; sai mô hình hay sai điều kiện biên vẫn còn nguyên. |
| "ODE và PDE khó như nhau." | PDE là bài toán vô hạn chiều theo không gian; cả lý thuyết lẫn phương pháp số đều khác hẳn. |
| "FEM thay thế giải tích." | FEM *chính là* phép tính biến phân được rời rạc hóa, cộng với đại số tuyến tính. |
| "Lưới càng mịn càng giải quyết được mọi thứ." | Lưới mịn chỉ giảm sai số rời rạc; nó không sửa được một mô hình vật lý sai. |
| "Gradient chỉ hướng xuống dốc." | $$\nabla f$$ chỉ hướng **lên dốc**; $$-\nabla f$$ mới là hướng xuống dốc. |
| "Divergence bằng 0 nghĩa là chất lỏng đứng yên." | Divergence bằng 0 nghĩa là không có nguồn hay điểm hút ròng; chất lỏng vẫn có thể chảy (quay, hoặc chảy đều). |

---

## Video phổ thông

- **Nguồn:** [Best Explanation of Gradient, Divergence and Curl — Brain Station Advanced](https://www.youtube.com/watch?v=m_Psx7CdvDk) (khoảng 15 phút; 2026-08-03).  
  Trình tự: trường vô hướng và trường vectơ → gradient chỉ hướng lên dốc → divergence với nguồn và điểm hút → curl với bánh xe cánh quạt.

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/calculus-physics-engineering/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — 3Blue1Brown — Essence of calculus (series / ch.1 derivative): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).
2. **ORIENTATION** — 3Blue1Brown — Essence of calculus playlist hub: [https://www.3blue1brown.com/topics/calculus](https://www.3blue1brown.com/topics/calculus).
3. **CORE** — Brain Station Advanced — Gradient, Divergence and Curl: [https://www.youtube.com/watch?v=m_Psx7CdvDk](https://www.youtube.com/watch?v=m_Psx7CdvDk).
4. **FOUNDATION** — Khan Academy / 3B1B style multivariable (divergence theorem culture): [https://www.youtube.com/watch?v=rB83DpBJQsE](https://www.youtube.com/watch?v=rB83DpBJQsE).
5. **FOUNDATION** — MIT OCW 18.02 Multivariable Calculus (course page): [https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/](https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/).
6. **FOUNDATION** — MIT OCW 18.03 Differential Equations (video lectures): [https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/).

Danh mục URL đầy đủ: `research/video-research/calculus-physics-engineering/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/calculus-physics-engineering/transcripts/` · trạng thái: `research/video-research/calculus-physics-engineering/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/calculus-physics-engineering_WUvTyaaNkzM_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/calculus-physics-engineering/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — Essence of calculus (series / ch.1 derivative) — https://www.youtube.com/watch?v=WUvTyaaNkzM
2. 3Blue1Brown — Essence of calculus playlist hub — https://www.3blue1brown.com/topics/calculus
3. Brain Station Advanced — Gradient, Divergence and Curl — https://www.youtube.com/watch?v=m_Psx7CdvDk
4. Khan Academy / 3B1B style multivariable (divergence theorem culture) — https://www.youtube.com/watch?v=rB83DpBJQsE
5. MIT OCW 18.02 Multivariable Calculus (course page) — https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
6. MIT OCW 18.03 Differential Equations (video lectures) — https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/
7. Gilbert Strang & Cleve Moler — Learn Differential Equations (overview) — https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/
8. 3Blue1Brown — Divergence and curl playlist (multivariable) — https://www.3blue1brown.com/topics/multivariable-calculus

### Video (tìm thêm / phụ)

9. Numberphile / related continuum modeling culture (optional) — https://www.youtube.com/user/numberphile

### Bài báo, sách, OCW và web

10. Evans — Partial Differential Equations (AMS Graduate Studies): https://bookstore.ams.org/gsm-19-r
11. Wikipedia — Fundamental theorem of calculus: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
12. Wikipedia — Finite element method: https://en.wikipedia.org/wiki/Finite_element_method
13. MIT OCW 18.02: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
14. MIT OCW 18.03: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/

### Trong khóa

15. Khóa học: [Tổng quan]({{ site.baseurl }}/contents/vi/chapter03/03_00_Tong_quan/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/). Gói: `research/video-research/calculus-physics-engineering/`.

## Hướng đi tiếp

- Bài tiếp theo: [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).  
- Bài toán thuần túy liên quan: [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).  
- Tùy chọn: xem [video về gradient, divergence, curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) rồi đọc lại §5.  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [Best Explanation of Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (Brain Station Advanced, tiếng Anh). Giải thích trực quan ba toán tử gradient, divergence và curl bằng hình ảnh trường vectơ. Nên xem trước khi đọc §5.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) (3Blue1Brown, tiếng Anh). Tập mở đầu của loạt bài về bản chất của giải tích: đạo hàm, tích phân và định lý cơ bản. Hợp với §1 và §2.
- [Divergence and curl: The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) (3Blue1Brown, tiếng Anh). Giải thích divergence và curl qua dòng chất lỏng và phương trình Maxwell. Xem sau khi đã nắm §4 và §5.
