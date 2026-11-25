---
layout: post
title: "Zelmanov và bài toán Burnside hạn chế (Huy chương Fields 1994)"
chapter: '02'
order: 31
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử tưởng tượng một khối Rubik kỳ lạ: bạn chỉ có đúng $$d = 2$$ thao tác xoay cơ bản là $$a$$ và $$b$$, và mọi chuỗi xoay bất kỳ $$x$$ mà bạn tổ hợp ra, chỉ cần lặp lại đúng $$n$$ lần là khối Rubik quay về nguyên trạng ban đầu ($$x^n = 1$$). Trực giác mách bảo rằng với luật siết chặt như thế, tổng số trạng thái khác nhau của khối Rubik chắc chắn phải là hữu hạn! Năm 1902, **William Burnside** đặt chính câu hỏi đó cho lý thuyết nhóm — và suốt gần một thế kỷ, nó đã tạo ra những cú ngoặt ngoạn mục bậc nhất lịch sử đại số.

Bất ngờ thứ nhất: trực giác đó **sai**! Ngay cả khi cố định số mũ $$n$$ chung cho mọi phần tử, vẫn tồn tại những **nhóm vô hạn** chỉ cần 2 phần tử sinh mà mọi phần tử đều thỏa $$x^n = 1$$ (do Golod–Shafarevich, rồi Novikov–Adian, Ol’shanskii, Ivanov, Lysënok xây dựng). Nhưng giữa rừng "quái vật vô hạn" ấy, từ thập niên 1930 các nhà đại số đặt ra một câu hỏi sắc bén hơn mang tên **bài toán Burnside hạn chế**: nếu ta chỉ xét các nhóm **hữu hạn** được sinh bởi $$d$$ phần tử và có số mũ $$n$$, liệu cấp của chúng có thể lớn tùy ý không, hay bị khóa chặt bởi một trần trên duy nhất chỉ phụ thuộc vào $$(d, n)$$?

Năm 1990–1991, bằng một cú chuyển ngôn ngữ ngoạn mục từ lý thuyết nhóm sang **đại số Lie** và **đại số Jordan**, **Efim Zelmanov** chứng minh câu trả lời là **CÓ** cho mọi $$d$$ và mọi $$n$$ — và nhận **Huy chương Fields 1994**:

> “For the solution of the restricted Burnside problem.”  
> — [IMU, Fields Medals 1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)

*Tạm dịch: vì lời giải bài toán Burnside hạn chế.*

Trọn vẹn ý nghĩa của bài học này nằm ở chữ **hạn chế** (*restricted*): phân biệt rạch ròi ba bài toán Burnside, thấy rõ vì sao định lý khẳng định của Zelmanov hoàn toàn không mâu thuẫn với các nhóm vô hạn của Novikov–Adian, và hiểu cách đại số Lie cùng đại số Jordan giải bài toán về nhóm hữu hạn.

**Mạch bài học:** Kiến thức cần nhớ (ba bài toán Burnside, tuyến tính hóa nhóm thành đại số Lie, đại số Jordan) → Ví dụ tính tay làm từng bước: chứng minh $$B(d, 2)$$ có cấp $$2^d$$ và khám phá nhóm $$B(2, 3)$$ cấp $$27$$ cùng đồng nhất thức Engel → Các phản ví dụ vô hạn (Golod–Shafarevich, Novikov–Adian, quái vật Tarski) → Giải thích: 4 bước từ Hall–Higman và Kostrikin đến định lý Zelmanov (1990–1991) → Ranh giới định lý.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt rành mạch **ba bài toán Burnside**: **tổng quát** (nhóm tuần hoàn), **bị chặn** (nhóm Burnside tự do $$B(d,n)$$ có số mũ $$n$$ cố định), và **hạn chế** (chỉ xét các nhóm *hữu hạn* $$d$$-sinh có số mũ $$n$$).
- Tự tay chứng minh $$B(d,2)$$ là nhóm abel cấp $$2^d$$ và giải thích trực giác vì sao điều kiện $$x^3 = 1$$ sinh ra đồng nhất thức móc Lie kiểu Engel.
- Giải thích vì sao $$B(d,n)$$ có thể **vô hạn** trong khi thương hữu hạn lớn nhất $$B_0(d,n)$$ của nó vẫn **hữu hạn**.
- Nêu đúng các cột mốc: **Golod–Shafarevich**, **Novikov–Adian**, **Ol’shanskii**, **Ivanov–Lysënok** (các phản ví dụ vô hạn); **Hall–Higman** (rút gọn về lũy thừa nguyên tố); **Kostrikin** (số mũ nguyên tố $$p$$); và **Zelmanov** (mọi số mũ $$n$$).
- Mô tả phương pháp chứng minh của Zelmanov: chuyển từ nhóm sang **vành Lie / đại số Lie**, rồi dùng lý thuyết **đại số Jordan** để chứng minh tính lũy linh.

**Kiến thức nền.** Nhóm cho bởi phần tử sinh và hệ thức; sự khác nhau giữa "mọi phần tử có cấp hữu hạn" và "có một $$n$$ chung sao cho $$x^n=1$$"; khái niệm đại số Lie như một phép toán móc song tuyến tính thỏa đồng nhất thức Jacobi và $$[x,x]=0$$. Không cần học trước lý thuyết nhóm tổ hợp.

**Liên kết với các bài khác.** Bài này cho thấy một câu hỏi cổ điển tách thành nhiều định lý khác nhau, và các bài viết phóng đại về huy chương hay bỏ mất chữ "hạn chế". Đọc cùng các bài khác trong chương có kiểu "một tên bài toán, nhiều nghĩa", và với các chương trình cấu trúc dài hơi trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/).

---

## Kiến thức cần nhớ: Nhóm Burnside, Đại số Lie và Đại số Jordan nghiên cứu gì?

### 1. Ba bài toán Burnside — đừng bao giờ gộp chung
- **Tổng quát (1902):** Mọi nhóm hữu hạn sinh tuần hoàn (mỗi $$x$$ có một cấp hữu hạn $$n_x$$ riêng) có hữu hạn không? $$\Rightarrow$$ **KHÔNG** (Golod–Shafarevich, 1964).
- **Bị chặn (Bounded):** Nhóm Burnside tự do $$B(d,n)$$ (nhóm $$d$$-sinh lớn nhất thỏa $$x^n = 1$$ với mọi $$x$$) có hữu hạn không? $$\Rightarrow$$ **CÓ** với $$n = 2, 3, 4, 6$$; **KHÔNG** với nhiều $$n$$ lớn (Novikov–Adian 1968, Ivanov 1994, Lysënok 1996); vẫn **MỞ** ngay cả ở $$B(2, 5)$$!
- **Hạn chế (Restricted, thập niên 1930):** Chỉ xét các **nhóm hữu hạn** $$d$$-sinh có số mũ $$n$$, có tồn tại trần trên chung cho cấp của chúng không (tức thương hữu hạn lớn nhất $$B_0(d,n)$$ có hữu hạn không)? $$\Rightarrow$$ **CÓ, với mọi $$d, n$$** (Kostrikin cho $$n = p$$; **Zelmanov 1990–1991** cho mọi $$n$$)!

### 2. Tại sao $$B(d,n)$$ vô hạn không mâu thuẫn với $$B_0(d,n)$$ hữu hạn?
Một nhóm vô hạn vẫn có thể có rất ít (thậm chí không có) thương hữu hạn! Ví dụ một nhóm đơn vô hạn không có nhóm con chuẩn tắc có chỉ số hữu hạn nào ngoài chính nó, nên thương hữu hạn lớn nhất của nó chỉ có cấp $$1$$! Tương tự, trong $$B(d,n)$$ vô hạn, giao của tất cả các nhóm con chuẩn tắc có chỉ số hữu hạn là một nhóm con vô hạn, trong khi phần thương hữu hạn $$B_0(d,n)$$ lại hoàn toàn hữu hạn.

### 3. Tuyến tính hóa nhóm thành Đại số Lie và vai trò của Đại số Jordan
Bằng cách lấy dãy nhóm con giao hoán tử $$G = G_1 \supseteq G_2 \supseteq \cdots$$ ($$G_{k+1} = [G_k, G]$$), ta biến một nhóm phi giao hoán thành một **đại số Lie phân bậc** $$L(G) = \bigoplus_{k \ge 1} G_k/G_{k+1}$$ với móc Lie sinh từ giao hoán tử $$[g,h] = g^{-1}h^{-1}gh$$. Điều kiện $$x^n = 1$$ biến thành **đồng nhất thức Engel** $$(\mathrm{ad}\,x)^m = 0$$ trong $$L(G)$$. Và chính những phần tử đặc biệt (phần tử *sandwich* thỏa $$(\mathrm{ad}\,a)^2 = 0$$) bên trong đại số Lie lại tự nhiên mang cấu trúc của một **đại số Jordan** (đại số không kết hợp với phép nhân đối xứng $$A\circ B = \frac{1}{2}(AB+BA)$$)!

---

## 1. Ví dụ làm từng bước: chứng minh $$B(d, 2)$$ cấp $$2^d$$ và khám phá $$B(2, 3)$$ cấp $$27$$

### Ví dụ 1: Số mũ $$n = 2$$ — hai dòng chứng minh $$B(d, 2)$$ hữu hạn!
Giả sử mọi phần tử $$x$$ của nhóm $$G$$ đều thỏa $$x^2 = 1$$ (tức $$x = x^{-1}$$). Lấy hai phần tử bất kỳ $$a, b \in G$$:

$$
(ab)^2 = 1 \;\Longrightarrow\; ab = (ab)^{-1} = b^{-1}a^{-1} = ba!
$$

Nhóm $$G$$ tự động là **nhóm giao hoán (abel)**! Vì có $$d$$ phần tử sinh $$x_1, \ldots, x_d$$ giao hoán với nhau và mỗi phần tử chỉ có số mũ $$0$$ hoặc $$1$$, mọi phần tử của $$B(d, 2)$$ đều viết duy nhất dưới dạng $$x_1^{\varepsilon_1}\cdots x_d^{\varepsilon_d}$$ ($$\varepsilon_i \in \{0, 1\}$$), nên:

$$
\vert B(d, 2) \vert = 2^d.
$$

### Ví dụ 2: Số mũ $$n = 3$$ — khi giao hoán bị phá vỡ và móc Lie xuất hiện!
Xét nhóm $$B(2, 3)$$ sinh bởi 2 phần tử $$a, b$$ với quy tắc $$x^3 = 1$$ cho mọi $$x$$. Thử kiểm tra: $$B(2, 3)$$ **không** giao hoán! Cụ thể, nhóm Heisenberg trên trường $$\mathbb{F}_3$$ gồm các ma trận tam giác trên $$3\times 3$$:

$$
M(u, v, w) = \begin{pmatrix} 1 & u & w \\ 0 & 1 & v \\ 0 & 0 & 1 \end{pmatrix}, \qquad u, v, w \in \mathbb{F}_3,
$$

có đúng $$3^3 = 27$$ ma trận, được sinh bởi hai ma trận $$a = M(1,0,0)$$ và $$b = M(0,1,0)$$, và bạn có thể tự tính ngay lập phương của bất kỳ ma trận nào:

$$
M(u, v, w)^3 = \begin{pmatrix} 1 & 3u & 3w + 3uv \\ 0 & 1 & 3v \\ 0 & 0 & 1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \pmod 3!
$$

Giao hoán tử $$c = [a, b] = M(0, 0, 1) \neq I$$, nhưng giao hoán tử bậc ba $$[c, a] = [[a, b], a] = I$$ và $$[c, b] = [[a, b], b] = I$$!
Burnside (1902) và Levi–van der Waerden chứng minh rằng chính nhóm cấp $$27$$ này là toàn bộ $$B(2, 3)$$! Nhìn vào phương trình $$[[a, b], a] = 1$$, khi dịch sang đại số Lie $$L(G)$$ trên $$\mathbb{F}_3$$, nó chính là **đồng nhất thức Engel bậc 2**:

$$
(\mathrm{ad}\,x)^2(y) = [[y, x], x] = 0 \quad \forall x, y \in L(G)!
$$

Ví dụ nhỏ $$27$$ phần tử này hé lộ trọn vẹn chiến lược của trường phái Nga: thay vì đánh vật với các từ dài trong nhóm, hãy dịch $$x^{p^k} = 1$$ thành đồng nhất thức Engel trên đại số Lie $$L(G)$$ và chứng minh $$L(G)$$ phải lũy linh!

---

## 2. Giải thích: Con đường 4 bước từ Hall–Higman và Kostrikin đến định lý Zelmanov

Như Walter Feit nhấn mạnh tại ICM 1994, bài toán Burnside hạn chế *"về bản chất là một bài toán về đại số Lie"*. Hãy theo dõi 4 bước chinh phục pháo đài 60 năm tuổi này:

#### Bước 1: Định lý rút gọn Hall–Higman (1956) — đưa mọi số mũ $$n$$ về lũy thừa nguyên tố $$p^k$$
Phân tích $$n = p_1^{k_1} \cdots p_r^{k_r}$$. **Philip Hall và Graham Higman (1956)** chứng minh một định lý cấu trúc sâu sắc (trở thành vô điều kiện sau khi **Định lý Phân loại Nhóm Đơn Hữu hạn** hoàn tất đầu thập niên 1980): bài toán Burnside hạn chế đúng cho số mũ $$n$$ **khi và chỉ khi** nó đúng cho từng **lũy thừa số nguyên tố** $$p_i^{k_i}$$!

#### Bước 2: Chặng Kostrikin (1959) — chinh phục số mũ nguyên tố $$n = p$$
Với một $$p$$-nhóm hữu hạn $$G$$ có số mũ nguyên tố $$p$$, **Alexei Kostrikin** chứng minh đại số Lie liên kết $$L(G)$$ trên $$\mathbb{F}_p$$ thỏa đồng nhất thức Engel bậc $$p-1$$: $$(\mathrm{ad}\,x)^{p-1} = 0$$. Bằng kỹ thuật **phần tử sandwich** (tìm các phần tử $$a \neq 0$$ thỏa $$(\mathrm{ad}\,a)^2 = 0$$), ông chứng minh mọi đại số Lie $$d$$-sinh thỏa điều kiện Engel bậc $$p-1$$ đều **lũy linh** với lớp bị chặn — giải xong bài toán Burnside hạn chế cho số mũ nguyên tố $$p$$!

#### Bước 3: Bức tường $$n = p^k$$ ($$k \ge 2$$) và đột phá đại số Jordan của Zelmanov (1990–1991)
Suốt 30 năm sau Kostrikin, ngay cả số mũ $$p^2$$ cũng chặn đứng mọi nỗ lực vì đại số Lie $$L(G)$$ (xây từ $$p$$-dãy Jennings–Zassenhaus) chỉ còn thỏa đồng nhất thức Engel cho các phần tử **thuần nhất** chứ không cho mọi tổ hợp tuyến tính, cộng thêm một đồng nhất thức đa thức yếu hơn!
Trong hai bài báo lịch sử — năm **1990** cho số mũ **lẻ** ($$p$$ lẻ) và năm **1991** cho **$$2$$-nhóm** ($$n = 2^k$$, trường hợp khó nhất vì đặc số $$2$$ phá hủy nhiều phép tuyến tính hóa) — **Efim Zelmanov** vận dụng toàn bộ kho vũ khí ông đã rèn từ lý thuyết cấu trúc **đại số Jordan vô hạn chiều** (đồng nhất thức Glennie, đại số Jordan đặc biệt) để kiểm soát các phần tử sandwich và chứng minh định lý lõi: *mọi đại số Lie $$d$$-sinh trên $$\mathbb{F}_p$$ thỏa đồng nhất thức đa thức và điều kiện Engel trên các phần tử thuần nhất đều **lũy linh**!*

#### Bước 4: Dịch ngược từ đại số Lie về trần trên cho cấp nhóm hữu hạn
Vì đại số Lie $$L(G)$$ lũy linh với lớp $$c(d, p^k)$$ chỉ phụ thuộc $$d$$ và $$p^k$$, số chiều của $$L(G)$$ trên $$\mathbb{F}_p$$ bị chặn bởi một hằng số $$N(d, p^k)$$, kéo theo cấp của $$p$$-nhóm hữu hạn $$G$$ bị chặn bởi $$p^{N(d, p^k)}$$! Kết hợp với Bước 1, bài toán Burnside hạn chế được giải quyết trọn vẹn cho **mọi $$d$$ và mọi $$n$$**!

Tóm tắt chuỗi chuyển hóa đại số của Zelmanov:

$$
\text{Nhóm hữu hạn } G\ (x^n=1)
\;\xrightarrow{\text{Hall–Higman}}\;
p\text{-nhóm } (x^{p^k}=1)
\;\xrightarrow{\text{Jennings–Zassenhaus}}\;
\text{Đại số Lie } L(G)
\;\xrightarrow{\text{Đại số Jordan (Zelmanov)}}\;
L(G) \text{ lũy linh} \implies \vert G\vert \le C(d,n).
$$

---

## 3. Bảng tổng hợp ba bài toán Burnside và vì sao là Huy chương Fields

| Câu hỏi | Trả lời |
|---------|---------|
| Mọi nhóm tuần hoàn hữu hạn sinh có hữu hạn không? | **Không** (Golod–Shafarevich, 1964). |
| Mọi $$B(d,n)$$ có hữu hạn không? | **Không** với nhiều $$n$$ lớn (Novikov–Adian, Ol’shanskii, Ivanov, Lysënok); **có** với $$n=2,3,4,6$$; một số trường hợp nhỏ như $$B(2,5)$$ vẫn **mở**. |
| Có phải chỉ có hữu hạn nhóm *hữu hạn* $$d$$-sinh số mũ $$n$$? | **Có**, với mọi $$d,n$$ (Kostrikin cho $$n=p$$; **Zelmanov** cho trường hợp tổng quát). |

**Vì sao là Huy chương Fields 1994:** Giữa một lĩnh vực vốn nổi danh vì những phản ví dụ vô hạn kỳ quái (như quái vật Tarski của Ol’shanskii), bài toán Burnside hạn chế là pháo đài lớn cuối cùng của tính hữu hạn. Zelmanov đã giải quyết dứt điểm pháo đài đó bằng sức mạnh thuần túy của đại số cấu trúc (Lie và Jordan), đại diện xuất sắc cho mảng đại số tại ICM Zürich 1994 bên cạnh Bourgain, Lions và Yoccoz.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Zelmanov giải bài toán Burnside." | Ông giải bài toán Burnside **hạn chế**. Các bài toán không hạn chế / bị chặn nói chung có câu trả lời phủ định. |
| "Mọi nhóm có số mũ hữu hạn đều hữu hạn." | Sai: $$B(d,n)$$ vô hạn với nhiều giá trị $$n$$. |
| "Golod–Shafarevich đã giải quyết tất cả." | Họ bác bỏ bài toán *tổng quát* (không có chặn chung). Bài toán Burnside hạn chế nói về các nhóm hữu hạn có số mũ cố định. |
| "Kostrikin đã giải cả bài toán hạn chế." | Kostrikin: số mũ **nguyên tố**. Zelmanov: số mũ lẻ và $$2$$-nhóm, từ đó mọi $$n$$. |
| "'Hạn chế' nghĩa là 'dễ hơn, nên nhóm hữu hạn'." | "Hạn chế" nghĩa là "chỉ hỏi về các nhóm **hữu hạn**". Nhóm Burnside tự do vẫn có thể vô hạn. |
| "Chứng minh thuần túy là tổ hợp nhóm." | Công cụ chính là **vành Lie / đại số Lie**, với nền tảng từ đại số Jordan. |

---

## Liên kết

- IMU Fields Medals 1994: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)
- Wikipedia: [Efim Zelmanov](https://en.wikipedia.org/wiki/Efim_Zelmanov); [Burnside problem](https://en.wikipedia.org/wiki/Burnside_problem)
- Tìm arXiv: [Zelmanov restricted Burnside](https://arxiv.org/search/?query=Zelmanov+restricted+Burnside&searchtype=all)
- Trang lịch sử MacTutor về bài toán Burnside (liên kết từ bài Wikipedia)

---

## Tài liệu tham khảo

1. International Mathematical Union, citation Fields Medals 1994 cho Efim Zelmanov (laudation Feit, ICM Zürich 1994).
2. **E. I. Zelmanov**, “Solution of the restricted Burnside problem for groups of odd exponent,” *Math. USSR-Izv.* 36 (1991), 41–60.
3. **E. I. Zelmanov**, “A solution of the restricted Burnside problem for $$2$$-groups,” *Math. USSR-Sb.* 72 (1992), 543–565.
4. **A. I. Kostrikin**, *Around Burnside*, Springer, 1990 (trường hợp số mũ nguyên tố).
5. **W. Burnside**, “On an unsettled question in the theory of discontinuous groups,” *Quart. J. Pure Appl. Math.* 33 (1902), 230–238.
6. Wikipedia, [Efim Zelmanov](https://en.wikipedia.org/wiki/Efim_Zelmanov) và [Burnside problem](https://en.wikipedia.org/wiki/Burnside_problem) (Novikov–Adian, Golod–Shafarevich, Ol’shanskii, Ivanov, Lysënok).

---

## Hướng đi tiếp

- Đọc một bài tổng quan ngắn về lý do số mũ lẻ lớn làm $$B(d,n)$$ vô hạn (kỹ thuật triệt tiêu nhỏ), rồi quay lại phương pháp vành Lie; lưu ý $$B(2,5)$$ vẫn là trường hợp bị chặn còn mở nổi tiếng.
- Câu hỏi thảo luận: nếu các chặn tường minh lớn khủng khiếp như vậy, định lý *dùng để làm gì*?

## Video tham khảo

- **Xem trước**: [Why Do People Hate Mathematics? Efim Zelmanov (Fields Medal 1994)](https://www.youtube.com/watch?v=Nz3_RzZzuO8) (Tom Rocks Maths, tiếng Anh). Cuộc phỏng vấn trong đó Zelmanov nói về cách nhìn toán học của mình. Đây là phỏng vấn, không trình bày chứng minh bài toán Burnside hạn chế.
