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

Hãy thử hình dung một khối Rubik kỳ lạ: bạn chỉ có hữu hạn thao tác xoay cơ bản (chẳng hạn $$d = 2$$ thao tác $$a$$ và $$b$$), và mọi chuỗi xoay bất kỳ $$x$$ mà bạn tổ hợp ra, nếu lặp lại đúng $$n$$ lần, đều đưa khối Rubik về trạng thái ban đầu ($$x^n = 1$$). Trực giác thông thường mách bảo rằng với luật siết chặt như thế, tổng số trạng thái khác nhau của khối Rubik chắc chắn phải là hữu hạn! Năm 1902, **William Burnside** đặt chính câu hỏi đó cho lý thuyết nhóm — và suốt gần một thế kỷ, nó đã đẻ ra những cú bất ngờ ngoạn mục bậc nhất của đại số hiện đại.

Bất ngờ thứ nhất: trực giác đó **sai**! Ngay cả khi cố định một số mũ $$n$$ chung cho mọi phần tử, vẫn tồn tại những **nhóm vô hạn** được sinh bởi chỉ 2 phần tử mà mọi phần tử đều thỏa $$x^n = 1$$ (do Golod–Shafarevich, rồi Novikov–Adian, Ol’shanskii, Ivanov, Lysënok xây dựng). Nhưng giữa một rừng "quái vật vô hạn" đó, từ thập niên 1930 các nhà đại số đặt ra một câu hỏi sắc bén hơn mang tên **bài toán Burnside hạn chế**: nếu ta chỉ nhìn vào các nhóm **hữu hạn** được sinh bởi $$d$$ phần tử và có số mũ $$n$$, liệu kích thước của chúng có thể phình to vô hạn không, hay bị khóa chặt bởi một trần trên duy nhất chỉ phụ thuộc vào $$(d, n)$$?

Năm 1990–1991, bằng một màn chuyển đổi đại số đầy bất ngờ từ lý thuyết nhóm sang **đại số Lie** và **đại số Jordan**, **Efim Zelmanov** chứng minh câu trả lời là **CÓ** cho mọi $$d$$ và mọi $$n$$ — và nhận **Huy chương Fields 1994**:

> “For the solution of the restricted Burnside problem.”  
> — [IMU, Fields Medals 1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)

*Tạm dịch: vì lời giải bài toán Burnside hạn chế.*

Toàn bộ sức nặng của bài học này nằm ở chữ **hạn chế** (*restricted*): hiểu rõ sự khác biệt giữa ba phiên bản bài toán Burnside, vì sao định lý khẳng định của Zelmanov hoàn toàn không mâu thuẫn với các phản ví dụ vô hạn của Novikov–Adian, và vì sao một bài toán tưởng thuần túy về nhóm hữu hạn lại được giải bằng đại số không kết hợp (Lie và Jordan).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu câu hỏi gốc năm 1902 của Burnside và phân biệt rành mạch **ba bài toán Burnside**: bài toán **tổng quát** (nhóm tuần hoàn), bài toán **bị chặn** (số mũ $$n$$ cố định), và bài toán **hạn chế** (tính hữu hạn của tập các nhóm *hữu hạn* $$d$$-sinh có số mũ $$n$$).
- Giải thích vì sao một nhóm Burnside tự do $$B(d,n)$$ có thể **vô hạn** trong khi thương hữu hạn lớn nhất $$B_0(d,n)$$ của nó vẫn **hữu hạn** (không có mâu thuẫn giữa Novikov–Adian và Zelmanov).
- Nêu đúng các cột mốc phản ví dụ: **Golod–Shafarevich** (bác bỏ dạng tổng quát), **Novikov–Adian** ($$B(d,n)$$ vô hạn cho $$n$$ lẻ lớn), **Ivanov** và **Lysënok** (số mũ chẵn lớn), và "quái vật Tarski" của **Ol’shanskii**.
- Phát biểu định lý **Zelmanov** (1990 cho số mũ lẻ; 1991 cho $$2$$-nhóm, suy ra mọi $$n$$), đồng thời ghi công **A. I. Kostrikin** cho bước đột phá sớm ở trường hợp số mũ nguyên tố $$p$$.
- Mô tả trực quan chiến lược chứng minh: biến một nhóm hữu hạn có số mũ $$n$$ thành một **đại số Lie** thỏa đồng nhất thức Engel, rồi dùng kỹ thuật **đại số Jordan** để chứng minh tính lũy linh.
- Tránh các câu nói sai như "Zelmanov giải bài toán Burnside" hay "mọi nhóm Burnside đều hữu hạn".

**Kiến thức nền.** Nhóm cho bởi phần tử sinh và hệ thức; sự khác nhau giữa "mọi phần tử có cấp hữu hạn" và "có một $$n$$ chung sao cho $$x^n=1$$"; khái niệm đại số Lie như một phép toán móc song tuyến tính thỏa đồng nhất thức Jacobi và $$[x,x]=0$$. Không cần học trước lý thuyết nhóm tổ hợp.

**Liên kết với các bài khác.** Bài này cho thấy một câu hỏi cổ điển tách thành nhiều định lý khác nhau, và các bài viết phóng đại về huy chương hay bỏ mất chữ "hạn chế". Đọc cùng các bài khác trong chương có kiểu "một tên bài toán, nhiều nghĩa", và với các chương trình cấu trúc dài hơi trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/).

---

## Bản đồ kiến thức nền: Nhóm tự do, đại số Lie và đại số Jordan liên quan gì với nhau?

Tại sao một bài toán về **nhóm hữu hạn** (đối tượng kết hợp) lại dẫn thẳng đến **đại số Lie** và **đại số Jordan** (những cấu trúc *không kết hợp*)? Hãy hình dung qua ba bước dịch ngôn ngữ.

**1. Nhóm cho bởi phần tử sinh và hệ thức — và "độ lớn" của thương hữu hạn.**
Nếu bạn có $$d$$ chữ cái $$x_1, \ldots, x_d$$ và không áp đặt quy tắc nào (trừ $$x_i x_i^{-1} = 1$$), bạn thu được **nhóm tự do** $$F_d$$ (vô hạn). Nếu áp đặt thêm quy tắc $$w^n = 1$$ cho mọi từ $$w$$, bạn thu được **nhóm Burnside tự do** $$B(d,n)$$.
- Một điều rất dễ nhầm: một nhóm vô hạn vẫn có thể có **rất ít** thương hữu hạn! Ví dụ đơn giản nhất: nhóm số nguyên $$\mathbb{Z}$$ là vô hạn nhưng có vô số thương hữu hạn $$\mathbb{Z}/m\mathbb{Z}$$; ngược lại, một nhóm đơn vô hạn không có thương hữu hạn không tầm thường nào cả (thương hữu hạn lớn nhất của nó chỉ là nhóm tầm thường có 1 phần tử!). Vì vậy, việc $$B(d,n)$$ vô hạn hoàn toàn **không** ngăn cản thương hữu hạn lớn nhất $$B_0(d,n)$$ của nó là hữu hạn!

**2. Biến nhóm thành Đại số Lie (tuyến tính hóa nhóm).**
Nhóm phi giao hoán rất khó tính vì phép nhân không phân phối qua phép cộng. Từ thập niên 1930 (Magnus, Witt, Jennings, Zassenhaus), các nhà đại số nghĩ ra một chiếc kính lúp tuyệt vời: lấy dãy nhóm con giao hoán tử $$G = G_1 \supseteq G_2 \supseteq G_3 \supseteq \cdots$$ (với $$G_{k+1} = [G_k, G]$$), rồi xếp các thương giao hoán $$G_k / G_{k+1}$$ lại thành tổng trực tiếp

$$
L(G) = \bigoplus_{k \ge 1} G_k / G_{k+1}.
$$

Phép lấy giao hoán tử $$[g, h] = g^{-1}h^{-1}gh$$ trong nhóm $$G$$ biến thành **móc Lie** $$[\bar{g}, \bar{h}]$$ trên không gian vector $$L(G)$$! Phép nhân phức tạp của nhóm nay đã được "tuyến tính hóa" thành một **đại số Lie**! Nếu ta chứng minh được đại số Lie $$L(G)$$ là **lũy linh** (tức mọi móc lồng nhau đủ sâu $$[\cdots[a_1, a_2], \ldots, a_c]$$ đều bằng $$0$$) với bậc $$c$$ chỉ phụ thuộc $$(d, n)$$, thì cấp của nhóm $$G$$ lập tức bị chặn!

**3. Vai trò bất ngờ của Đại số Jordan.**
Nếu đại số Lie mô tả giao hoán tử $$[A, B] = AB - BA$$ của ma trận, thì **đại số Jordan** mô tả phép nhân đối xứng $$A \circ B = \frac{1}{2}(AB + BA)$$ (xuất hiện ban đầu trong cơ học lượng tử). Trong đại số Lie $$L(G)$$ gắn với một nhóm số mũ $$n$$, điều kiện $$x^n = 1$$ chuyển thành **đồng nhất thức Engel** $$(\mathrm{ad}\,x)^m = 0$$ (móc liên tiếp với cùng một phần tử $$x$$ đủ $$m$$ lần sẽ bằng $$0$$). Những phần tử đặc biệt gọi là "phần tử sandwich" (thỏa $$(\mathrm{ad}\,a)^2 = 0$$) lại tự nhiên mang cấu trúc của một **đại số Jordan** (hay cặp Jordan)! Chính nhờ bề dày bậc thầy về đại số Jordan vô hạn chiều, Zelmanov đã bẻ gãy được bài toán Engel–Lie làm bó tay giới đại số suốt 30 năm!

---

## 1. Ba bài toán chung một tên: hãy tách rõ từng câu hỏi

Một nhóm $$G$$ gọi là **tuần hoàn** (*periodic* / *torsion*) nếu mọi phần tử $$g \in G$$ đều có cấp hữu hạn (tồn tại $$n_g \ge 1$$ sao cho $$g^{n_g} = 1$$). Năm 1902, Burnside hỏi:

> Nếu $$G$$ hữu hạn sinh và tuần hoàn, thì $$G$$ có nhất thiết hữu hạn không?

Từ câu hỏi gốc đó, lịch sử tách ra đúng **ba bài toán riêng biệt**:

1. **Bài toán Burnside tổng quát:** Mọi nhóm $$d$$-sinh tuần hoàn (cấp các phần tử có thể khác nhau và không bị chặn chung) có hữu hạn không?
2. **Bài toán Burnside bị chặn (Bounded):** Nếu cố định số mũ $$n$$ chung ($$g^n = 1$$ với mọi $$g \in G$$), thì **nhóm Burnside tự do** $$B(d,n)$$ có hữu hạn không?
   - Với các số mũ rất nhỏ, câu trả lời là **có**: $$B(d,2)$$ là nhóm abel sơ cấp cấp $$2^d$$ (vì $$x^2=1$$ kéo theo $$ab = (ab)^{-1} = b^{-1}a^{-1} = ba$$!); Burnside (1902) chứng minh $$B(d,3)$$ hữu hạn; Sanov (1940) chứng minh $$B(d,4)$$ hữu hạn; Marshall Hall (1958) chứng minh $$B(d,6)$$ hữu hạn.
   - Đáng kinh ngạc là với ngay cả trường hợp nhỏ xíu **$$B(2, 5)$$** (2 phần tử sinh, mọi phần tử thỏa $$x^5 = 1$$), đến tận ngày nay vẫn **chưa ai biết** nó hữu hạn hay vô hạn!
3. **Bài toán Burnside hạn chế (Restricted, đặt ra thập niên 1930):** Không hỏi $$B(d,n)$$ có hữu hạn không, mà chỉ hỏi trong tất cả các **nhóm hữu hạn** $$d$$-sinh có số mũ $$n$$, có tồn tại một **trần trên chung** cho cấp của chúng không? Tương đương, nhóm thương hữu hạn lớn nhất $$B_0(d,n)$$ (lấy thương của $$B(d,n)$$ theo giao mọi nhóm con chuẩn tắc có chỉ số hữu hạn) có hữu hạn không?

Định lý của Zelmanov khẳng định: **$$B_0(d,n)$$ luôn hữu hạn với mọi $$d \ge 1$$ và mọi $$n \ge 1$$!**

---

## 2. Các bài toán không hạn chế: một vườn "quái vật vô hạn"

Trước khi Zelmanov đạt tới lời giải khẳng định cho bài toán hạn chế, các phiên bản không hạn chế đã chứng kiến những phản ví dụ chấn động nhất lịch sử lý thuyết nhóm:

- **Golod–Shafarevich (1964):** Xây dựng các $$p$$-nhóm hữu hạn sinh **vô hạn** mà mọi phần tử đều có cấp là lũy thừa của $$p$$ (nhưng cấp tăng không bị chặn), bác bỏ dứt điểm **bài toán Burnside tổng quát**.
- **Novikov–Adian (1968):** Bằng một chứng minh quy nạp tổ hợp dài hàng trăm trang cực kỳ phức tạp, họ chứng minh $$B(d,n)$$ là **vô hạn** với mọi $$d \ge 2$$ và mọi số mũ lẻ $$n \ge 4381$$ (sau đó Adian hạ ngưỡng xuống $$n \ge 665$$ lẻ), bác bỏ **bài toán Burnside bị chặn**!
- **Alexander Ol’shanskii (cuối thập niên 1970–1980):** Dùng hình học đồ thị van Kampen để xây dựng **"quái vật Tarski"** (*Tarski monsters*): những nhóm vô hạn sinh bởi 2 phần tử, có số mũ là số nguyên tố lớn $$p$$, mà *mọi nhóm con thực sự không tầm thường đều là nhóm cyclic cấp $$p$$*!
- **S. V. Ivanov (1994) và I. G. Lysënok (1996):** Chinh phục trường hợp **số mũ chẵn** còn khó hơn nhiều, chứng minh $$B(d,n)$$ vô hạn với mọi $$n \ge 8000$$ chia hết cho $$16$$ (Lysënok).

**Điểm chốt không được nhầm:** Nhiều nhóm $$B(d,n)$$ là vô hạn, nhưng phần "lõi vô hạn" của chúng (giao của mọi nhóm con chuẩn tắc có chỉ số hữu hạn) không thể phân tách được bằng bất kỳ đồng cấu nào vào nhóm hữu hạn; phần thương hữu hạn $$B_0(d,n)$$ vẫn gọn gàng và hữu hạn theo định lý Zelmanov!

---

## 3. Bài toán hạn chế: từ Hall–Higman và Kostrikin đến đột phá của Zelmanov

Con đường chinh phục bài toán Burnside hạn chế trải qua ba chặng lịch sử:

**Chặng 1 — Rút gọn về lũy thừa số nguyên tố (Hall–Higman, 1956).** Philip Hall và Graham Higman chứng minh một định lý rút gọn tuyệt đẹp (mà sau khi **Định lý Phân loại Nhóm Đơn Hữu hạn** hoàn tất vào đầu thập niên 1980, trở thành kết quả không điều kiện): bài toán Burnside hạn chế đúng cho *mọi* số mũ $$n$$ **khi và chỉ khi** nó đúng cho mọi **lũy thừa số nguyên tố** $$n = p^k$$!

**Chặng 2 — Số mũ nguyên tố $$n = p$$ (Kostrikin, 1959).** Nhà toán học Nga **Alexei Kostrikin** chứng minh bài toán Burnside hạn chế đúng cho mọi số mũ nguyên tố $$p$$ bằng cách chuyển sang đại số Lie đặc số $$p$$ thỏa đồng nhất thức Engel bậc $$p-1$$ và phát minh ra kỹ thuật *phần tử sandwich*. Nhưng suốt 30 năm tiếp theo, ngay cả số mũ $$n = p^2$$ (như $$n = 4, 9, 25$$) cũng làm bó tay phương pháp của Kostrikin vì đại số Lie không còn thỏa đồng nhất thức Engel thuần nhất đơn giản nữa.

**Chặng 3 — Mọi lũy thừa số nguyên tố (Zelmanov, 1990–1991).** Bằng hai bài báo liên tiếp mang tính bước ngoặt:
- *"Solution of the restricted Burnside problem for groups of odd exponent"* (*Izv. Akad. Nauk SSSR*, 1990) — giải trọn trường hợp $$p$$ lẻ, $$n = p^k$$;
- *"Solution of the restricted Burnside problem for $$2$$-groups"* (*Mat. Sb.*, 1991) — giải trường hợp $$n = 2^k$$ khó nhất (vì đặc số $$2$$ làm sụp đổ nhiều đồng nhất thức tuyến tính hóa!),

**Efim Zelmanov** hoàn tất toàn bộ bài toán Burnside hạn chế cho **mọi số mũ $$n$$**!

---

## 4. Phương pháp, nói ngắn gọn: nhóm $$\to$$ vành Lie $$\to$$ đại số Jordan

Như Walter Feit nhấn mạnh trong diễn văn ICM 1994, bài toán Burnside hạn chế "về bản chất là một bài toán về đại số Lie". Chuỗi biến đổi gồm bốn bước:

1. Xuất phát từ một $$p$$-nhóm hữu hạn $$d$$-sinh $$G$$ có số mũ $$n = p^k$$. Ta cần một chặn trên cho $$\lvert G \rvert$$ chỉ phụ thuộc vào $$(d, p^k)$$.
2. Chuyển sang **đại số Lie phân bậc** $$L(G)$$ trên trường $$\mathbb{F}_p$$ xây từ $$p$$-dãy tâm dưới Jennings–Zassenhaus. Điều kiện $$x^{p^k} = 1$$ biến thành một cặp điều kiện đại số trong $$L(G)$$: (i) $$L(G)$$ thỏa một đồng nhất thức đa thức (kiểu Engel đã tuyến tính hóa) và (ii) mọi phần tử thuần nhất đều là phần tử Engel địa phương.
3. **Định lý lõi của Zelmanov:** Mọi đại số Lie trên trường đặc số $$p$$ thỏa hai điều kiện đó và hữu hạn sinh đều **lũy linh** (nên hữu hạn chiều với số chiều chỉ phụ thuộc $$(d, p^k)$$)! Để chứng minh điều này mà không cần giả thiết hữu hạn chiều, Zelmanov đã phát triển một lý thuyết cấu trúc sắc bén về **đại số Jordan** vô hạn chiều (từ các bài báo trước đó của chính ông về đồng nhất thức Glennie và đại số Jordan đặc biệt) nhằm chế ngự tác động phụ hợp $$\mathrm{ad}$$ và triệt tiêu các phần tử sandwich.
4. Dịch chặn chiều của đại số Lie $$L(G)$$ ngược trở lại thành chặn trên cho cấp $$\lvert G \rvert$$ của nhóm $$G$$!

**Tóm tắt.** Một trong những bài toán kinh điển nhất của lý thuyết nhóm hữu hạn lại được chốt hạ bằng một định lý lũy linh cho đại số Lie, sử dụng vũ khí bí mật là đại số Jordan không kết hợp.

---

## 5. Định lý cho biết gì và không cho biết gì

Định lý Zelmanov khẳng định sự **tồn tại** một chặn trên chung cho cấp của mọi nhóm hữu hạn $$d$$-sinh số mũ $$n$$. Nó không lập danh sách các nhóm đó (trên thực tế, các chặn tường minh rút từ chứng minh lớn đến mức khổng lồ), và không trả lời liệu bản thân $$B(d,n)$$ có hữu hạn hay không.

| Câu hỏi | Trả lời |
|---------|---------|
| Mọi nhóm tuần hoàn hữu hạn sinh có hữu hạn không? | **Không** (Golod–Shafarevich). |
| Mọi $$B(d,n)$$ có hữu hạn không? | **Không** với nhiều $$n$$ lớn; **có** với một số $$n$$ nhỏ; một số trường hợp nhỏ vẫn **mở**. |
| Có phải chỉ có hữu hạn nhóm *hữu hạn* $$d$$-sinh số mũ $$n$$? | **Có**, với mọi $$d,n$$ (Kostrikin cho $$n=p$$; Zelmanov cho trường hợp tổng quát). |

Huy chương Fields 1994 của Zelmanov nằm gọn ở **hàng thứ ba**.

---

## 6. Vì sao là Huy chương Fields

Giữa một lĩnh vực vốn lừng danh vì những phản ví dụ vô hạn kỳ quái (Golod–Shafarevich, Novikov–Adian, quái vật Tarski), bài toán Burnside hạn chế là pháo đài cuối cùng của tính hữu hạn — tồn tại suốt hơn 50 năm và kháng cự mọi phương pháp lý thuyết nhóm thuần túy. Zelmanov đã phá vỡ pháo đài đó bằng sức mạnh thuần túy của đại số cấu trúc (Lie và Jordan), mở ra cả một nhánh nghiên cứu mới về nhóm pro-$$p$$ và đại số không kết hợp. Tại ICM Zürich 1994, Zelmanov đại diện xuất sắc cho mảng đại số bên cạnh ba người cùng nhận huy chương là Jean Bourgain, Pierre-Louis Lions và Jean-Christophe Yoccoz.

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
