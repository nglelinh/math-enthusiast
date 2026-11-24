---
layout: post
title: "Bài toán Navier–Stokes"
chapter: '01'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

Buổi sáng, khi bạn rót một dòng sữa vào tách cà phê đen, những vệt trắng mượt mà lập tức cuộn thành vòng xoáy lớn, rồi vỡ ra thành hàng chục xoáy nhỏ hơn, rồi nhỏ hơn nữa cho tới khi hòa tan hoàn toàn. Từ dòng nước chảy xiết qua ghềnh đá, luồng khí nâng cánh máy bay nặng hàng trăm tấn, cho đến những cơn bão đại dương — tất cả đều tuân theo một bộ phương trình duy nhất ra đời từ thế kỷ 19: **hệ phương trình Navier–Stokes**.

Về bản chất, đó chỉ là định luật II Newton $$F = ma$$ viết lại cho một chất lỏng nhớt không nén. Các kỹ sư tin dùng hệ phương trình này mỗi ngày để thiết kế tên lửa, dự báo thời tiết và mô phỏng dòng máu trong động mạch. Thế nhưng ẩn sau công cụ quen thuộc ấy lại là một trong những bài toán Thiên niên kỷ hóc búa nhất của Viện Clay: liệu mô hình toán học liên tục lý tưởng này có **luôn bảo đảm** giữ cho dòng chảy trơn tru mãi mãi khi xuất phát từ trạng thái êm đềm, hay có thể tự sinh ra một **điểm kỳ dị** — nơi vận tốc hoặc độ xoáy vọt lên vô hạn chỉ sau một khoảng thời gian hữu hạn?

Câu hỏi ở đây **không** phải là "ta có chạy mô phỏng máy tính được không?". Bài học này sẽ tách rạch ròi giữa **thực hành kỹ thuật**, **nghiệm yếu Leray** và **bài toán chính quy Thiên niên kỷ**, đồng thời kết nối với những đột phá gần đây về nguồn gốc động học của phương trình chất lưu.

**Mạch bài học:** Bản đồ kiến thức nền → hệ phương trình & kiểm chứng tay dòng Poiseuille → bài toán Clay → những gì đã biết (2D, Leray) → phép tính đổi tỉ lệ siêu tới hạn 2D vs 3D & khung giải thích chậm → tiêu chí chính quy & Deng → kỹ thuật vs bài toán Clay.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết hệ Navier–Stokes **không nén** (vận tốc và áp suất, ràng buộc $$\nabla\cdot u=0$$) và gọi tên các số hạng phi tuyến, nhớt, áp suất.
- Phân biệt **việc dùng hệ Navier–Stokes trong kỹ thuật** với **bài toán chính quy Thiên niên kỷ**.
- Giải thích sự khác nhau giữa nghiệm yếu **Leray** và nghiệm trơn cổ điển (có nghiệm yếu toàn cục không có nghĩa là có tính chính quy và tính duy nhất đầy đủ).
- Phát biểu bài toán mở: tồn tại và duy nhất nghiệm trơn toàn cục trong 3 chiều, hoặc nghiệm bùng nổ (blow-up) sau thời gian hữu hạn từ dữ liệu trơn.
- Kể một số kết quả từng phần: Beale–Kato–Majda; dữ liệu nhỏ và nghiệm mild; chính quy từng phần (Caffarelli–Kohn–Nirenberg); tính chính quy trong 2 chiều.
- Liên hệ với [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): suy ra mô hình liên tục từ lý thuyết động học là vấn đề **khác** với tính chính quy của hệ Navier–Stokes 3 chiều.
- Tránh các lỗi phổ biến như "máy bay bay được nên Navier–Stokes đã được giải" hay "mô phỏng thấy bùng nổ là chứng minh".

**Kiến thức cần có.** Giải tích nhiều biến; hiểu phương trình đạo hàm riêng như các định luật cân bằng địa phương. Không cần khóa học nâng cao về phương trình đạo hàm riêng; các định lý chỉ được nêu tên và ý chính.

**Kết nối trong khóa học.** Bạn nên đọc kèm bài [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (nền tảng động học của chất lưu) và phần ứng dụng phương trình vi phân trong khóa học.

---

## Bản đồ kiến thức nền: Phương trình đạo hàm riêng (PDE) và Cơ học chất lưu là gì?

Ở bậc đại học, bạn đã gặp **phương trình vi phân thường (ODE)** như $$y'(t) = -ky(t)$$, nơi đại lượng cần tìm chỉ phụ thuộc vào *một* biến (thời gian $$t$$). Thế nhưng thế giới vật lý tồn tại trong cả không gian lẫn thời gian: nhiệt độ, sóng âm, hay vận tốc nước đều là các **trường** phụ thuộc đồng thời vào vị trí $$(x,y,z)$$ và thời gian $$t$$. Ba trụ cột sau đây giúp bạn hiểu toàn bộ bài toán Navier–Stokes:

### 1. Phương trình đạo hàm riêng (PDE) và tính đặt chỉnh Hadamard
PDE là ngôn ngữ mô tả mối liên hệ giữa tốc độ đổi theo thời gian ($$\partial_t$$) và độ dốc/độ cong theo không gian ($$\nabla, \Delta$$) của một trường. Các định luật nền tảng nhất của vật lý đều là PDE: truyền nhiệt, truyền sóng, hệ Maxwell, phương trình Schrödinger và Navier–Stokes. Khi viết ra một PDE, nhà toán học đặt ba câu hỏi của Hadamard về **tính đặt chỉnh (well-posedness)**: (1) Nghiệm có *tồn tại* không? (2) Có *duy nhất* không? (3) Có *trơn và ổn định* không?

### 2. Giải tích hàm & Nghiệm yếu (Weak Solutions)
Với PDE phi tuyến, sóng xung kích hay xoáy cực sắc có thể khiến đạo hàm thông thường không tồn tại tại một số điểm. Thay vì bó tay, các nhà toán học nhân phương trình với một hàm thử trơn $$\varphi$$ rồi tích phân từng phần để "đẩy đạo hàm" từ $$u$$ sang $$\varphi$$. Khái niệm **nghiệm yếu** (trong các không gian hàm Sobolev $$L^2, H^1$$) giúp chứng minh *sự tồn tại* dễ hơn nhiều — nhưng mở ra bài toán khó mới: liệu nghiệm yếu đó có thực sự khả vi trơn mượt không?

### 3. Phép đổi tỉ lệ (Scaling) & Tính siêu tới hạn
Một PDE thường có một phép co giãn không–thời gian giữ nguyên dạng phương trình. So sánh xem đại lượng bảo toàn (như tổng động năng) thay đổi thế nào dưới phép co giãn đó sẽ tiết lộ ngay bài toán là *dưới tới hạn* (dễ kiểm soát ở thang đo nhỏ), *tới hạn* (như Navier–Stokes 2D), hay **siêu tới hạn** (như Navier–Stokes 3D — nơi năng lượng hữu hạn mất quyền kiểm soát khi xoáy thu nhỏ về một điểm!).

**Ứng dụng thực tiễn:** Dự báo thời tiết và khí hậu, thiết kế khí động lực học máy bay–ô tô, mô phỏng dòng máu tim mạch, tản nhiệt chip bán dẫn và đồ họa hiệu ứng khói–nước trong điện ảnh.

---

## 1. Hệ phương trình (dạng không nén)

Cho trường vận tốc $$u(x,t)\in\mathbb{R}^3$$ và áp suất $$p(x,t)$$,

$$
\begin{aligned}
\partial_t u + (u\cdot\nabla)u &= \nu \Delta u - \nabla p + f,\\
\nabla\cdot u &= 0,
\end{aligned}
$$

với độ nhớt động học $$\nu>0$$ và ngoại lực $$f$$ (có thể không có). Trên $$\mathbb{R}^3$$ hoặc trên xuyến $$\mathbb{T}^3$$, dữ liệu ban đầu thường được cho là trơn, có divergence bằng 0 và năng lượng hữu hạn.

**Đọc hệ phương trình như định luật Newton $$a = F/m$$:**
Nếu bạn từng học giải tích nhiều biến, hãy theo dõi một hạt nước nhỏ trôi theo quỹ đạo $$x(t)$$ với vận tốc $$u(x(t), t)$$. Theo quy tắc đạo hàm hàm hợp (chain rule), gia tốc thực sự mà hạt nước đó cảm nhận là:

$$
\frac{d}{dt}\,u(x(t), t) = \partial_t u + (u\cdot\nabla)u.
$$

Đó chính xác là vế trái của phương trình Navier–Stokes! Còn vế phải là tổng các lực tác dụng lên một đơn vị khối lượng chất lỏng:

- $$\partial_t u$$: tốc độ đổi vận tốc tại một điểm cố định trong không gian.  
- $$(u\cdot\nabla)u$$: **số hạng đối lưu phi tuyến**; chất lỏng tự mang động lượng của chính nó trôi đi theo các đường dòng. Vì vận tốc $$u$$ nhân với đạo hàm $$\nabla u$$, đây là nguồn gốc toán học của hầu hết mọi khó khăn.  
- $$\nu\Delta u$$: **khuếch tán nhớt**; toán tử Laplace $$\Delta u$$ đóng vai trò như "bàn ủi" làm phẳng những chỗ vận tốc thay đổi đột ngột. $$\nu$$ càng lớn thì chất lỏng càng đặc (mật ong có $$\nu$$ lớn gấp hàng nghìn lần nước).  
- $$-\nabla p$$: lực do chênh lệch áp suất (chất lỏng bị đẩy từ nơi áp suất cao sang nơi áp suất thấp).  
- $$\nabla\cdot u=0$$: **điều kiện không nén**; lượng nước chảy vào một thể tích nhỏ luôn bằng đúng lượng chảy ra (mật độ không đổi).  
- $$f$$: ngoại lực (trọng lực, lực khuấy trộn, …), thường đặt bằng 0 trong phát biểu thuần túy của Viện Clay.

### Ví dụ cầm tay chỉ việc 1: Tự kiểm chứng từng số hạng trên dòng chảy Poiseuille

Để hệ Navier–Stokes không còn là những ký hiệu xa lạ, hãy thử kiểm tra trực tiếp một nghiệm trơn nổi tiếng — dòng nước chảy êm giữa hai thành ống song song $$y = -1$$ và $$y = 1$$ (dòng **Poiseuille**), với vận tốc parabol $$u(x,y) = \bigl(U(1 - y^2),\, 0\bigr)$$ và áp suất giảm tuyến tính $$p(x,y) = -2\nu U x$$ (không đổi theo thời gian, ngoại lực $$f=0$$):

1. **Điều kiện không nén:** $$\nabla\cdot u = \frac{\partial}{\partial x}\bigl(U(1-y^2)\bigr) + \frac{\partial}{\partial y}(0) = 0 + 0 = 0$$ ✓.
2. **Số hạng gia tốc cục bộ:** $$\partial_t u = (0, 0)$$.
3. **Số hạng đối lưu phi tuyến:** $$(u\cdot\nabla)u = u_x \partial_x u + u_y \partial_y u = U(1-y^2)\cdot(0,0) + 0\cdot\partial_y u = (0, 0)$$. (Số hạng phi tuyến rắc rối tự triệt tiêu sạch!)
4. **Số hạng nhớt:** $$\nu \Delta u = \bigl(\nu \partial_{yy}(U - Uy^2),\, 0\bigr) = (-2\nu U,\, 0)$$.
5. **Gradient áp suất:** $$-\nabla p = -\bigl(\partial_x(-2\nu U x),\, \partial_y(-2\nu U x)\bigr) = (+2\nu U,\, 0)$$.

Cộng vế phải: $$\nu\Delta u - \nabla p = (-2\nu U + 2\nu U,\, 0) = (0, 0) =$$ vế trái! Lực đẩy từ chênh lệch áp suất cân bằng tuyệt đối với ma sát nhớt. Ta giải được gọn gàng như vậy chỉ vì dòng chảy chảy thẳng nên số hạng phi tuyến $$(u\cdot\nabla)u$$ bằng 0; ngay khi dòng chảy xoáy cuộn trong 3D và $$(u\cdot\nabla)u \neq 0$$, mọi công thức đóng đều biến mất!

Áp suất không phải một trường tự do độc lập như $$u$$: lấy divergence của phương trình động lượng, ta khôi phục được $$p$$ (sai khác một hằng số) qua một phương trình kiểu Poisson $$-\Delta p = \nabla\cdot((u\cdot\nabla)u)$$. Tính không nén là một ràng buộc; áp suất đóng vai trò nhân tử Lagrange tự điều chỉnh tức thời để giữ ràng buộc đó.

**Ý nghĩa vật lý qua số Reynolds.** Để biết số hạng phi tuyến hay độ nhớt đang "làm chủ cuộc chơi", các nhà vật lý dùng **số Reynolds**: $$\mathrm{Re} = \frac{UL}{\nu}$$.
- Khi mật ong nhỏ giọt chậm ($$\mathrm{Re} \ll 1$$), độ nhớt thắng tuyệt đối: dòng chảy êm ả, mượt mà (chảy tầng).
- Khi nước chảy từ vòi bếp ($$\mathrm{Re} \sim 10^3\text{–}10^4$$) hay không khí lướt qua cánh máy bay phản lực ($$\mathrm{Re} \sim 10^7$$), quán tính phi tuyến lấn át độ nhớt: dòng chảy vỡ thành vô số xoáy chồng chéo ở nhiều thang đo (chảy rối).

**Năng lượng.** Nhân phương trình động lượng với $$u$$ rồi lấy tích phân trên toàn không gian, số hạng đối lưu phi tuyến và áp suất triệt tiêu đẹp mắt nhờ $$\nabla\cdot u = 0$$, để lại **bất đẳng thức năng lượng**:

$$
\frac{1}{2}\int \vert u(x,t)\vert^2\,dx + \nu \int_0^t \int \vert \nabla u(x,s)\vert^2\,dx\,ds \le \frac{1}{2}\int \vert u_0(x)\vert^2\,dx
$$

(khi $$f=0$$). Động năng toàn phần luôn bị chặn và giảm dần do ma sát nhớt.

---

## 2. Bài toán Thiên niên kỷ hỏi gì

Đại ý (xem bài của Fefferman cho Viện Clay để có phát biểu và không gian hàm chính xác), trên $$\mathbb{R}^3$$ (hoặc trên xuyến):

Chứng minh một trong hai khẳng định:

- **Chính quy toàn cục:** với dữ liệu trơn, divergence bằng 0, năng lượng hữu hạn (và ngoại lực phù hợp), tồn tại nghiệm trơn duy nhất $$u,p$$ với mọi $$t>0$$, và các chuẩn tự nhiên không bùng nổ sau thời gian hữu hạn; hoặc  
- **Bùng nổ:** tồn tại dữ liệu trơn có năng lượng hữu hạn sao cho nghiệm trơn không kéo dài được qua một thời điểm hữu hạn $$T_*$$, tức là một chuẩn của vận tốc hoặc độ xoáy không bị chặn khi $$t\to T_*^-$$.

Các câu hỏi liên quan: **tính duy nhất** của nghiệm yếu Leray–Hopf; cấu trúc hình học của tập kỳ dị nếu có. Giải thưởng dành cho một định lý về phương trình đạo hàm riêng liên tục, không dành cho một thí nghiệm số "trông như kỳ dị" trên lưới.

**Tình trạng (2026):** **còn mở**. Đây là một trong sáu bài toán Thiên niên kỷ chưa được giải; giả thuyết Poincaré là bài duy nhất đã được giải (Perelman).

"Còn mở" nghĩa là chưa có **định lý về tồn tại và chính quy cho mô hình liên tục**, chứ không phải "chưa ai mô phỏng được nước".

---

## 3. Những gì *đã* biết: thời gian ngắn, 2 chiều, nghiệm yếu

**Tồn tại trong thời gian ngắn.** Với dữ liệu trơn có divergence bằng 0, tồn tại nghiệm trơn duy nhất trên $$[0,T)$$, với $$T$$ phụ thuộc vào độ lớn của dữ liệu (trong không gian Sobolev hoặc Hölder phù hợp). Câu hỏi là: có phải luôn có $$T=\infty$$, hay với một số dữ liệu thì $$T$$ hữu hạn?

**Hai chiều.** Tính chính quy toàn cục trong 2 chiều là kết quả cổ điển (Olga Ladyzhenskaya và cộng sự, thập niên 1950–1960). Lý do nằm ở cấu trúc hình học: hiện tượng **kéo giãn xoáy** (*vortex stretching*) không tồn tại trong mặt phẳng 2 chiều! Độ xoáy $$\omega=\nabla\times u$$ trong 2 chiều chỉ là một vô hướng thỏa phương trình vận chuyển–khuếch tán đơn giản, không có số hạng kéo giãn $$(\omega\cdot\nabla)u$$ như trong 3 chiều. Câu "Navier–Stokes 2 chiều chưa được giải" là sai; toàn bộ kịch tính của bài toán Thiên niên kỷ nằm ở **ba chiều**.

**Leray (1934).** Jean Leray xây dựng **nghiệm yếu** toàn cục trong 3 chiều: các trường thỏa phương trình theo nghĩa phân bố, thỏa bất đẳng thức năng lượng và khớp với dữ liệu ban đầu theo một tôpô phù hợp. Như vậy sự tồn tại không phải là câu hỏi bỏ ngỏ. Điều còn mở là: nghiệm yếu ấy có thực sự trơn khi dữ liệu ban đầu trơn không; nó có duy nhất không; mọi nghiệm yếu có trùng với nghiệm cổ điển hay không.

Tóm lại: "đã biết có nghiệm yếu toàn cục; chưa biết bài toán có đặt chỉnh với nghiệm trơn toàn cục hay không".

---

## 4. Vì sao tính chính quy trong 3 chiều khó

### Ví dụ cầm tay chỉ việc 2: Phép đổi tỉ lệ chỉ ra ranh giới sinh tử giữa 2D và 3D!

Hệ Navier–Stokes không có ngoại lực sở hữu một đối xứng co giãn tuyệt đẹp: nếu $$u(x,t)$$ là một nghiệm trên $$\mathbb{R}^d$$, thì với mọi hệ số $$\lambda > 0$$, hàm đổi tỉ lệ

$$
u_\lambda(x, t) = \lambda\, u(\lambda x, \lambda^2 t)
$$

cũng là một nghiệm chính xác! Bây giờ hãy tính xem **động năng toàn phần** $$E(u_\lambda) = \frac{1}{2}\int_{\mathbb{R}^d} \vert u_\lambda(x,t) \vert^2 \, dx$$ thay đổi ra sao bằng phép đổi biến tích phân năm nhất $$y = \lambda x \implies dx = \lambda^{-d}\,dy$$:

$$
E(u_\lambda) = \frac{1}{2} \int_{\mathbb{R}^d} \lambda^2 \vert u(\lambda x, \lambda^2 t)\vert^2 \, dx = \frac{1}{2}\,\lambda^{2-d} \int_{\mathbb{R}^d} \vert u(y, \tau)\vert^2 \, dy = \lambda^{2-d}\, E(u).
$$

Hãy nhìn chằm chằm vào số mũ **$$2 - d$$**:
- **Trong 2 chiều ($$d = 2$$):** $$\lambda^{2-2} = \lambda^0 = 1$$! Động năng **bất biến tỉ lệ** — dù một xoáy có co nhỏ lại gấp 1.000 lần (đặt $$\lambda = 1000$$), nó vẫn phải tốn *nguyên vẹn* một lượng năng lượng như cũ để duy trì cường độ. Kho năng lượng hữu hạn ban đầu đủ sức khóa chặt mọi điểm kỳ dị!
- **Trong 3 chiều ($$d = 3$$):** $$\lambda^{2-3} = \lambda^{-1}$$! Nếu bạn nén một xoáy vào vùng nhỏ hơn 1.000 lần ($$\lambda = 1000$$, vận tốc cực đại tăng gấp 1.000 lần!), động năng mà nó tiêu tốn lại **giảm đi 1.000 lần** ($$E(u_\lambda) = 10^{-3} E(u)$$)!!

Đó chính xác là ý nghĩa của từ **siêu tới hạn (supercritical)**: trong 3 chiều, một giọt nước có tổng năng lượng bé xíu vẫn có đủ "ngân sách năng lượng" để nuôi một xoáy nhỏ li ti có vận tốc vọt lên vô hạn!

### Khung giải thích: Vì sao có nghiệm yếu toàn cục (1934) mà bài toán Clay vẫn mở? (nên đọc chậm)

#### Bước 1: Cuộc kéo co giữa độ nhớt và kéo giãn xoáy
Trong 3 chiều, độ nhớt $$\nu \Delta u$$ cố gắng làm phẳng vận tốc, nhưng cơ chế **kéo giãn xoáy** $$(\omega\cdot\nabla)u$$ lại kéo dài và bóp mảnh các ống xoáy — hệt như vận động viên trượt băng thu hai tay sát người để xoay nhanh hơn. Xoáy càng mạnh lại càng tự kéo giãn mình mạnh hơn.

#### Bước 2: Bất đẳng thức năng lượng chỉ cho ta "nghiệm yếu"
Nhờ tổng năng lượng $$E(t)$$ bị chặn (và tích phân $$\int \vert \nabla u \vert^2$$ hữu hạn), Jean Leray (1934) chứng minh được luôn tồn tại một **nghiệm yếu** kéo dài mãi mãi tới $$t = \infty$$. Nhưng điều kiện tích phân bình phương hữu hạn vẫn cho phép hàm $$u$$ bị "nhọn vọt lên vô hạn" tại một vài điểm cô lập!

#### Bước 3: Bức tường siêu tới hạn cắt đứt lập luận nâng cấp độ trơn
Để chứng minh nghiệm yếu Leray thực sự trơn (không có điểm nổ), ta cần khống chế vận tốc cực đại $$\|u\|_{L^\infty}$$ hoặc độ xoáy cực đại $$\|\omega\|_{L^\infty}$$. Nhưng phép tính đổi tỉ lệ $$E(u_\lambda) = \lambda^{-1} E(u)$$ ở trên cho thấy: mọi ước lượng chỉ dựa vào định luật bảo toàn năng lượng đều mất tác dụng ở thang đo vi mô!

#### Bước 4: Ranh giới giữa mô phỏng số và định lý liên tục
Mô phỏng chảy rối trên siêu máy tính hoạt động trên lưới hữu hạn (nên không thể phóng to mãi về kích thước $$0$$). Vì vậy, dù mô phỏng có chạy êm hay bị "tràn số", nó đều không trả lời được câu hỏi giải tích của Viện Clay.

So sánh với [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/): kiểm tra hữu hạn trường hợp không chứng minh được một phát biểu về vô hạn trường hợp; ở đây, kiểm tra bằng số trên phương trình rời rạc không chứng minh được một phát biểu về mô hình liên tục. **Bằng chứng không phải là chứng minh.**

---

## 5. Tiêu chí chính quy, dữ liệu nhỏ, chính quy từng phần

**Chính quy có điều kiện.** Nếu một số chuẩn nhất định giữ hữu hạn trên $$[0,T]$$ thì nghiệm chắc chắn trơn đến thời điểm $$T$$. Ví dụ nổi tiếng là **Beale–Kato–Majda (1984)**: nếu tích phân theo thời gian của độ xoáy cực đại $$\int_0^T \|\omega(\cdot,t)\|_{L^\infty}\,dt < \infty$$ thì nghiệm không bùng nổ trước $$T$$. Có nhiều biến thể (Prodi–Serrin; trường hợp điểm mút của Escauriaza–Seregin–Šverák). Các kết quả này quy bài toán Thiên niên kỷ về: *chứng minh các chuẩn đó không bùng nổ*, hoặc *dựng dữ liệu làm chúng bùng nổ*.

**Dữ liệu nhỏ.** Nếu dữ liệu ban đầu đủ nhỏ (chẳng hạn vận tốc nhỏ hoặc độ nhớt $$\nu$$ rất lớn) trong một không gian tới hạn phù hợp thì có nghiệm trơn toàn cục. Dữ liệu lớn mới là vấn đề: về nguyên tắc, số hạng phi tuyến có thể dồn năng lượng vào các thang đo nhỏ.

**Chính quy từng phần.** Với các nghiệm yếu phù hợp, **Caffarelli–Kohn–Nirenberg (1982)** (dựa trên công trình của Scheffer) chứng minh một kết quả kinh điển: nếu có điểm kỳ dị trong không–thời gian 4 chiều $$(x,y,z,t)$$, thì tập hợp tất cả các điểm kỳ dị đó có **chiều Hausdorff parabolic $$\le 1$$** — nghĩa là chúng thậm chí không thể tạo thành một đường cong liên tục theo thời gian! Đây là một định lý chính quy sâu sắc, nhưng tập "nhỏ" vẫn **chưa** chứng minh được là tập rỗng.

**Các mốc khác** (chỉ cần biết tên): Ladyzhenskaya, Prodi, Serrin; nghiệm mild của Kato; kỹ thuật tích phân lồi (convex integration) và tính không duy nhất cho các nghiệm *yếu hơn* (liên hệ với giả thuyết Onsager về phương trình Euler). Đây là lĩnh vực phát triển nhanh; cần đọc các bài phổ thông một cách thận trọng.

---

## 6. Nền tảng động học, bài toán thứ sáu của Hilbert, và Deng

Có một câu hỏi thứ hai về chất lưu: không chỉ "phương trình liên tục có trơn không?" mà còn "phương trình liên tục có thực sự là giới hạn của hệ hàng tỷ phân tử va chạm nhau không?". Đây là tinh thần của **bài toán thứ sáu của Hilbert** (đi từ cơ học nguyên tử qua cơ học thống kê đến mô hình liên tục).

Chương trình nghiên cứu được Giải Fields ghi nhận của **Yu Deng** (cùng các cộng sự, trong đó có Zaher Hani và Xiao Ma) xây dựng cầu nối toán học chặt chẽ từ mô hình quả cầu cứng (hệ hạt Newton) đến phương trình Boltzmann và, trong chế độ phù hợp, đến các phương trình chất lưu. Kết quả này hỗ trợ việc *suy ra* mô hình liên tục với các giả thiết đã nêu, nhưng **không** tự chứng minh tính chính quy của Navier–Stokes 3 chiều theo phát biểu của bài toán Thiên niên kỷ.

Đọc bài [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) để hiểu **vì sao phương trình chất lưu xuất hiện như một giới hạn**. Đọc *bài này* để hiểu **phương trình liên tục đó có luôn trơn hay không**. Việc suy ra phương trình và tính chính quy là hai vấn đề liên quan nhưng không phải cùng một định lý.

Hướng nghiên cứu về tính chính quy của Luis Caffarelli (biên tự do, phương trình đạo hàm riêng phi tuyến), người nhận Giải Abel, là một cầu nối khác: tính chính quy từng phần của Navier–Stokes có cùng tinh thần với lý thuyết độ đo hình học, tức là phân tích để kiểm soát kích thước tập kỳ dị ngay cả khi chưa loại bỏ hoàn toàn được chúng.

---

## 7. Tính toán chất lưu trong kỹ thuật không phải bài toán Thiên niên kỷ

| Thực tiễn | Bài toán Clay |
|-----------|---------------|
| DNS / LES / RANS | Lý thuyết nghiệm trơn toàn cục cho hệ Navier–Stokes không nén lý tưởng |
| Lưới, bước thời gian, mô hình chảy rối | Định lý về tồn tại, duy nhất, chính quy |
| Chi phí tính toán theo số Reynolds khi giải đủ các xoáy | Ước lượng giải tích và khả năng bùng nổ |
| Kiểm chứng bằng thí nghiệm | Chứng minh trong không gian hàm |

Cả hai đều quan tâm đến sự truyền năng lượng qua nhiều thang đo, nhưng chỉ một bên là bài toán Clay. Câu "Navier–Stokes đã được giải vì phần mềm ANSYS chạy được" là sai về bản chất toán học; ngược lại, câu "máy bay không nên bay vì bài toán Clay còn mở" cũng sai nốt với thực tế kỹ thuật!

**Mô phỏng số trực tiếp (DNS)** cố gắng giải hệ Navier–Stokes đến tận thang đo nhớt nhỏ nhất; chi phí tính toán tăng rất nhanh theo số Reynolds (cỡ $$\mathrm{Re}^3$$). **LES và RANS** dùng mô hình gần đúng cho các thang đo nhỏ. Thành công rực rỡ về kỹ thuật không trả lời câu hỏi của Viện Clay.

---

## 8. Toán học quanh hệ Navier–Stokes

- **Tiêu chí chính quy:** các định lý có điều kiện dạng "nếu có điểm kỳ dị thì chuẩn này phải bùng nổ".  
- **Nghiệm yếu:** tồn tại toàn cục với ít tính chính quy, rồi tìm cách nâng tính chính quy.  
- **Dữ liệu nhỏ:** số hạng phi tuyến không phải lúc nào cũng thắng.  
- **Chính quy từng phần:** nếu có điểm kỳ dị thì chúng "hiếm" theo nghĩa độ đo hình học.

Đây là kiểu "toán học quanh một bài toán mở" giống như [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): câu hỏi gốc chưa giải được, nhưng xung quanh đã hình thành cả một rừng định lý sâu sắc.

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) về cuốn *Six Math Essentials*, Terence Tao đưa ra một ví dụ động lực học gần gũi hơn: bài toán **hai vật** của Newton giải được chính xác; sang bài toán **ba vật** đã gây đau đầu, vì quy tắc thì đơn giản nhưng dáng điệu dài hạn lại khó lường, và dự báo trung thực về lâu dài phải chuyển sang xác suất. Navier–Stokes không phải là "bài toán ba vật cho nước", nhưng đó là một nơi nữa mà cả động lực học lẫn giải tích vẫn còn nợ một định lý chính quy toàn cục. Xem thêm bài tổng hợp [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/) và bài [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/).

---

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Navier–Stokes chưa được giải nên máy bay không được bay." | Mô hình kỹ thuật cùng thực nghiệm vẫn hoạt động tốt; Viện Clay hỏi về một định lý thuần túy về tồn tại và chính quy. |
| "Ai đó mô phỏng được bùng nổ là bài toán đã xong." | Mô phỏng không phải chứng minh cho phương trình liên tục. |
| "Deng đã giải bài toán Navier–Stokes." | Deng có bước tiến trong việc suy ra phương trình từ lý thuyết động học; tính chính quy 3 chiều vẫn còn mở. |
| "2 chiều và 3 chiều cũng như nhau." | Tính chính quy trong 2 chiều đã biết; 3 chiều mới là trường hợp khó. |
| "Leray đã giải xong vì có nghiệm toàn cục." | Đó là nghiệm yếu; tính chính quy và tính duy nhất đầy đủ vẫn còn mở. |
| "Bài toán Clay là về cách chọn bước lưới tối ưu." | Không; đây là câu hỏi về lý thuyết giải tích của phương trình đạo hàm riêng. |

---

## Từ các bài giảng: hướng bùng nổ (Tao) và hướng chính quy (Caffarelli)

Video của Numberphile (Crawford), bài giảng của Caffarelli cho Viện Clay và bài giảng Einstein của Tao bổ sung các ý sau:

- **Hướng Caffarelli:** chính quy từng phần (CKN) giới hạn *mức độ xấu* của tập kỳ dị với nghiệm yếu phù hợp; tập "nhỏ" không có nghĩa là tập rỗng.  
- **Hướng Tao:** bùng nổ sau thời gian hữu hạn cho các mô hình *lấy trung bình* hay mô hình đơn giản hóa nhấn mạnh tính **siêu tới hạn**: ước lượng năng lượng không có thang đo phù hợp để khép kín lập luận bootstrap cho dữ liệu trơn lớn. Bùng nổ cho một phương trình đã sửa đổi **không** phải lời giải bài toán Clay cho hệ Navier–Stokes thật.  
- **Hai thế giới cùng tồn tại:** DNS/LES/RANS hoạt động trong thế giới rời rạc; Viện Clay hỏi về định lý cho mô hình liên tục.

**Tình trạng (2026):** câu hỏi chính quy toàn cục hay bùng nổ trong 3 chiều vẫn **còn mở** (bài toán Thiên niên kỷ).

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Đánh giá: `research/video-research/Navier_Stokes/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *Navier-Stokes Equations* (Crawford): [YouTube](https://www.youtube.com/watch?v=ERBVFcutl3M).  
2. **Trực giác** — vcubingx, *The million dollar equation*: [YouTube](https://www.youtube.com/watch?v=Ra7aQlenTb8).  
3. **Nền tảng** — Caffarelli, bài giảng của Viện Clay về Navier–Stokes: [YouTube](https://www.youtube.com/watch?v=ta6Q70y6YVU).  
4. **Nghiên cứu** — Tao, *Can NS Blow Up in Finite Time?*: [YouTube](https://www.youtube.com/watch?v=DgmuGqeRTto).  
5. **Văn bản gốc** — Fefferman, bản PDF: [navierstokes.pdf](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) · [Clay](https://www.claymath.org/millennium/navier-stokes-equation/).

**Sau khi xem:** thành công của tính toán chất lưu không phải định lý Clay. Nghiệm yếu không phải nghiệm trơn. Tình trạng năm 2026: **còn mở**.

---


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/Navier_Stokes/transcripts/` · trạng thái: `research/video-research/Navier_Stokes/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Navier_Stokes_ERBVFcutl3M_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

Danh sách URL: `research/video-research/Navier_Stokes/references.md`.

1. Clay — [NS](https://www.claymath.org/millennium/navier-stokes-equation/) · Fefferman PDF: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf  
2. Robinson — [survey](https://royalsocietypublishing.org/rsta/article/378/2174/20190526/111659/The-Navier-Stokes-regularity-problem).  
3. Wikipedia — [NS existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness).  
4. Numberphile: https://www.youtube.com/watch?v=ERBVFcutl3M  
5. vcubingx: https://www.youtube.com/watch?v=Ra7aQlenTb8  
6. Caffarelli: https://www.youtube.com/watch?v=ta6Q70y6YVU  
7. Tao: https://www.youtube.com/watch?v=DgmuGqeRTto  
7b. Tao trên Big Think (sáu trụ cột; bài toán hai vật và ba vật): https://www.youtube.com/watch?v=OOMx2BHHWtE  
8. [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/). Bộ tư liệu: `research/video-research/Navier_Stokes/`.

---

## Hướng đi tiếp

Có thể chọn làm đề tài cho bài **A3**. Bài thực hành: xem chuỗi truyền năng lượng của Kolmogorov như một *lập luận gần đúng*, không phải chứng minh. Đọc bài Deng để hiểu "từ hạt đến mô hình liên tục", rồi giữ rõ ranh giới giữa kỹ thuật và bài toán Clay.

## Video tham khảo

- **Xem trước:** [Navier-Stokes Equations - Numberphile](https://www.youtube.com/watch?v=ERBVFcutl3M) — Numberphile, tiếng Anh. Giới thiệu hệ phương trình và bài toán giải thưởng một triệu đô la; nên xem trước khi đọc bài.
- [The million dollar equation (Navier-Stokes equations)](https://www.youtube.com/watch?v=Ra7aQlenTb8) — vcubingx, tiếng Anh. Giải thích trực quan từng số hạng của phương trình; nên xem sau khi đã nắm ý chính của bài.
- [Luis Caffarelli, Navier-Stokes existence and smoothness](https://www.youtube.com/watch?v=ta6Q70y6YVU) — Clay Mathematics Institute, tiếng Anh. Xem thêm sau hai video trên, để nghe phát biểu bài toán từ góc nhìn của một chuyên gia về tính chính quy.
