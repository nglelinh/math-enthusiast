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

**Efim Zelmanov** nhận **Huy chương Fields 1994**

> “For the solution of the restricted Burnside problem.”  
> — [IMU, Fields Medals 1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)

Laudation ICM của Walter Feit nêu cùng một câu: Zelmanov nhận huy chương vì lời giải bài toán Burnside hạn chế. Tính từ **hạn chế** (restricted) là toàn bộ điểm sư phạm của bài này. William Burnside hỏi năm 1902 liệu một nhóm hữu hạn sinh trong đó mọi phần tử có cấp hữu hạn có nhất thiết hữu hạn. Ở dạng “số mũ bị chặn” mạnh nhất—mọi phần tử thỏa $$x^n=1$$ với $$n$$ cố định—câu trả lời tổng quát là **không**: tồn tại nhóm hữu hạn sinh vô hạn có số mũ hữu hạn (Golod–Shafarevich cho torsion không bị chặn đều; Novikov–Adian, Ol’shanskii, Ivanov, và những người khác cho số mũ lớn). Zelmanov **không** đảo các định lý đó. Ông trả lời một câu hỏi khác, được phát biểu những năm 1930 và được Wilhelm Magnus đặt tên: trong vũ trụ các nhóm **hữu hạn**, có chặn đều nào cho cấp của một nhóm $$d$$-sinh số mũ $$n$$ không? Tương đương: có chỉ hữu hạn nhóm hữu hạn $$d$$-sinh số mũ $$n$$, sai khác đẳng cấu, không? Câu trả lời là **có**, với mọi $$d$$ và mọi $$n$$. A. I. Kostrikin đã xử lý số mũ nguyên tố; Zelmanov xử lý số mũ lẻ (1990) rồi các $$2$$-nhóm (1991), do đó mọi số mũ.

Bài này dành cho người đã gặp biểu diễn nhóm bằng sinh và hệ thức, muốn giữ ba bài toán Burnside khỏi sụp thành một khẩu hiệu.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu câu hỏi 1902 của Burnside: một nhóm tuần hoàn hữu hạn sinh có nhất thiết hữu hạn?
- Phân biệt bài toán **tổng quát** (tuần hoàn, không số mũ đều), bài toán **Burnside bị chặn** (số mũ $$n$$ cố định), và bài toán **Burnside hạn chế** (tính hữu hạn của các nhóm $$d$$-sinh *hữu hạn* số mũ $$n$$).
- Nêu phản ví dụ ở mức khẩu hiệu: **Golod–Shafarevich** ($$p$$-nhóm hữu hạn sinh vô hạn, cấp phần tử không bị chặn đều); **Novikov–Adian** (nhóm Burnside tự do $$B(d,n)$$ vô hạn với $$n$$ lẻ lớn); công trình số mũ chẵn sau của **Ivanov** và **Lysënok**; quái vật Tarski của **Ol’shanskii**.
- Nêu định lý Zelmanov: với mọi $$d,n$$ chỉ có hữu hạn nhóm hữu hạn $$d$$-sinh số mũ $$n$$ (tương đương, nhóm Burnside hạn chế hữu hạn).
- Ghi công **Kostrikin** cho trường hợp số mũ nguyên tố của bài toán hạn chế.
- Mô tả phương pháp ở mức khẩu hiệu: chuyển từ nhóm sang **vành Lie / đại số Lie** liên kết, dùng đẳng thức và, ở nền, **đại số Jordan**.
- Tránh các câu sai “Zelmanov giải bài toán Burnside” và “mọi nhóm Burnside đều hữu hạn.”

**Kiến thức nền.** Nhóm cho bởi sinh và hệ thức; khác biệt giữa “mọi phần tử có cấp hữu hạn” và “có $$n$$ đều sao cho $$x^n=1$$”; ý tưởng đại số Lie như móc song tuyến với Jacobi và $$[x,x]=0$$. Không giả định lý thuyết nhóm tổ hợp trước đó.

**Liên kết seminar.** LO1 / LO6 (câu hỏi cổ điển tách thành nhiều định lý; hype huy chương bỏ chữ “hạn chế”). Ghép các chân dung “một tên bài toán, nhiều nghĩa” khác trong chương này, và văn hóa chương trình cấu trúc dài ở [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/).

---

## 1. Ba bài toán chung một tên

Một nhóm $$G$$ gọi là **tuần hoàn** (hoặc torsion) nếu mọi phần tử có cấp hữu hạn. Nhóm hữu hạn là tuần hoàn; $$p$$-nhóm Prüfer tuần hoàn và vô hạn, nhưng không hữu hạn sinh. Burnside hỏi:

> Nếu $$G$$ hữu hạn sinh và tuần hoàn, thì $$G$$ có nhất thiết hữu hạn?

Đó là **bài toán Burnside tổng quát**. Một phiên bản sắc hơn cố định số mũ: tồn tại $$n$$ sao cho $$g^n=1$$ với mọi $$g\in G$$. **Nhóm Burnside tự do** $$B(d,n)$$ là nhóm $$d$$-sinh lớn nhất số mũ $$n$$ (thương của nhóm tự do $$F_d$$ bởi nhóm con đầy đủ bất biến sinh bởi mọi lũy thừa $$n$$). **Bài toán Burnside bị chặn** hỏi: với những $$d,n$$ nào thì $$B(d,n)$$ hữu hạn?

Các trường hợp dương dễ biết sớm. $$B(1,n)$$ là cyclic cấp $$n$$. $$B(d,2)$$ là sơ cấp abelian hạng $$d$$. Burnside, Sanov, và Marshall Hall thiết lập tính hữu hạn của $$B(d,3)$$, $$B(d,4)$$, và $$B(d,6)$$. Với hầu hết số mũ nhỏ khác—nổi tiếng $$B(2,5)$$—câu hỏi vẫn mở. Với số mũ lớn câu trả lời là phủ định, như mục sau nhắc lại.

**Bài toán Burnside hạn chế** đổi vũ trụ diễn ngôn. Nó không hỏi $$B(d,n)$$ có hữu hạn không. Nó hỏi các thương **hữu hạn** của $$B(d,n)$$ có cấp bị chặn không—tương đương, có nhóm hữu hạn $$d$$-sinh số mũ $$n$$ tối đại duy nhất không, thường ký hiệu $$\widehat{B}(d,n)$$ hoặc $$B_0(d,n)$$, thu được bằng cách thương theo giao của mọi kernel residual chỉ số hữu hạn (tương đương, trong khung tuần hoàn này, mọi kernel hữu hạn). Nếu thương hữu hạn tối đại đó tồn tại và hữu hạn, thì mọi nhóm hữu hạn $$d$$-sinh số mũ $$n$$ là thương của một nhóm hữu hạn duy nhất, nên chỉ có hữu hạn kiểu đẳng cấu.

Zelmanov chứng minh thương hữu hạn tối đại này **hữu hạn** với mọi $$d$$ và mọi $$n$$.

---

## 2. Các bài toán không hạn chế: câu trả lời là không

Năm 1964, Evgeny Golod và Igor Shafarevich xây các $$p$$-nhóm hữu hạn sinh vô hạn (qua một định lý về biểu diễn đại số). Các nhóm đó tuần hoàn, nên chúng giết bài toán Burnside tổng quát, nhưng cấp phần tử không bị chặn bởi một $$n$$ cố định trước.

Bài toán số mũ bị chặn đòi công nghệ khác. Năm 1968, Pyotr Novikov và Sergei Adian chứng minh $$B(d,n)$$ vô hạn với $$d\ge 2$$ và $$n$$ lẻ lớn hơn $$4381$$ (Adian sau đó hạ chặn lẻ xuống $$665$$). Alexander Ol’shanskii cho các xây dựng hình học của nhóm hữu hạn sinh vô hạn số mũ nguyên tố lẻ lớn trong đó mọi nhóm con thực sự là cyclic (quái vật Tarski)—dạng “vô hạn nhưng địa phương cyclic” đặc biệt ấn tượng. Trường hợp số mũ chẵn khó hơn: S. V. Ivanov (1994) chứng minh vô hạn với số mũ chẵn lớn chia hết cho một lũy thừa cao của $$2$$; I. G. Lysënok (1996) cải thiện chặn chẵn. Kết luận cho khóa học này:

**Nhiều nhóm Burnside tự do $$B(d,n)$$ là vô hạn.** Định lý Zelmanov tương thích với sự thật đó. Một nhóm vô hạn vẫn có thể chỉ có hữu hạn thương hữu hạn kiểu cho trước; chính xác hơn, phần residual hữu hạn của $$B(d,n)$$ có thể rất lớn trong khi thương hữu hạn $$B_0(d,n)$$ vẫn hữu hạn.

Đừng nói “các nhóm Burnside hữu hạn.” Đừng nói “Zelmanov chỉ ra chúng hữu hạn.”

---

## 3. Bài toán hạn chế: Kostrikin rồi Zelmanov

Kostrikin thông báo cuối những năm 1950 rằng bài toán Burnside hạn chế có câu trả lời dương cho số mũ **nguyên tố** $$p$$: có nhóm hữu hạn $$d$$-sinh số mũ $$p$$ lớn nhất. Lập luận là định lý về đại số Lie đặc trưng $$p$$ (đẳng thức kiểu Engel kéo theo lũy linh trong vành Lie liên kết). Các khó khăn trong xử lý ban đầu được sửa sau; sách *Around Burnside* của Kostrikin là tường thuật chuẩn của trường hợp đó, và đã chỉ về công trình sau của Zelmanov.

Các bài của Zelmanov là:

- “Solution of the restricted Burnside problem for groups of odd exponent,” *Izv. Akad. Nauk SSSR Ser. Mat.* 54 (1990); bản Anh *Math. USSR-Izv.* 36 (1991), 41–60.
- “Solution of the restricted Burnside problem for $$2$$-groups,” *Mat. Sb.* 182 (1991); bản Anh *Math. USSR-Sb.* 72 (1992), 543–565.

Cùng các bổ đề rút gọn số mũ tổng quát về số mũ nguyên tố-lũy thừa (qua Sylow và các lập luận nhóm hữu hạn liên quan), chúng cho định lý hạn chế với **mọi** $$n$$. Bài giảng 1994 của Feit nhấn mạnh rằng Zelmanov trước hết đơn giản hóa và mở rộng máy đại số Lie vượt trường hợp nguyên tố của Kostrikin, rồi xử lý tình huống $$2$$-sơ cấp khó hơn nhiều.

---

## 4. Phương pháp ở mức khẩu hiệu: nhóm, vành Lie, đại số Jordan

Bài toán hạn chế “phần lớn là bài toán đại số Lie,” theo câu của Feit. Từ điển cổ điển trong trường phái Nga của Kostrikin, Magnus, Sanov, và Zelmanov:

1. Bắt đầu với nhóm hữu hạn $$d$$-sinh $$G$$ số mũ $$n$$. Người ta muốn chặn $$\lvert G\rvert$$ chỉ phụ thuộc $$d$$ và $$n$$.
2. Chuyển sang **vành Lie** liên kết (hoặc đại số Lie phân bậc trên trường hữu hạn) xây từ dãy tâm dưới, hoặc từ $$p$$-dãy Jennings–Zassenhaus khi $$n$$ là lũy thừa nguyên tố. Số mũ $$n$$ trở thành một **đẳng thức** trong vành Lie này: điều kiện kiểu Engel, hạn chế toán tử ad, hoặc đẳng thức sandwich.
3. Chứng minh một đại số Lie trên trường đặc trưng hữu hạn thỏa các đẳng thức đó và sinh bởi $$d$$ phần tử phải **lũy linh** lớp bị chặn, hoặc ít nhất hữu hạn chiều với chiều bị chặn.
4. Dịch chặn đại số Lie ngược thành chặn cấp của $$G$$.

Bước khó là (3). Công trình trước của Zelmanov về **đại số Jordan** (cấu trúc vô hạn chiều; các đẳng thức như của Glennie) cung cấp công cụ cho đẳng thức không kết hợp trong tác động phụ hợp, và ông chỉ ra đẳng thức Engel kéo theo lũy linh ngay cả ở vô hạn chiều. Khóa học này sẽ không tái tạo các đẳng thức đó. Khẩu hiệu: Burnside hạn chế là **định lý hữu hạn cho đại số Lie có đẳng thức**, chuyển sang nhóm bằng máy vành Lie liên kết—do đó một huy chương lý thuyết nhóm dựa trên sự nghiệp đại số Jordan.

---

## 5. Định lý phân loại gì và không phân loại gì

Định lý là một **chặn đều**. Nó không liệt kê các nhóm hữu hạn số mũ $$n$$, và các chặn hiệu quả thường cực lớn. Nó cũng không quyết định $$B(d,n)$$ nào hữu hạn: lời giải hạn chế có thể đúng trong khi bản thân $$B(d,n)$$ vô hạn.

Bảng so sánh hữu ích:

| Câu hỏi | Trả lời |
|---------|---------|
| Mọi nhóm tuần hoàn hữu hạn sinh có hữu hạn? | **Không** (Golod–Shafarevich). |
| Mọi $$B(d,n)$$ có hữu hạn? | **Không** với nhiều $$n$$ lớn; **có** với một số $$n$$ nhỏ; một số trường hợp nhỏ **mở**. |
| Có chỉ hữu hạn nhóm *hữu hạn* $$d$$-sinh số mũ $$n$$? | **Có**, mọi $$d,n$$ (Kostrikin với $$n=p$$; Zelmanov tổng quát). |

Citation Fields là hàng thứ ba.

---

## 6. Vì sao có Fields

Câu hỏi của Burnside thuộc những câu cũ nhất trong lý thuyết nhóm tổ hợp. Tới 1994 các bài toán không hạn chế đã trưng một số nhóm hoang nhất từng được xây, nên người nghe qua loa có thể nghĩ “Burnside đã xong.” Bài toán hạn chế vẫn là câu hỏi hữu hạn người ta còn hy vọng trả lời **dương**, và đã kháng cự với lũy thừa nguyên tố ngoài $$p$$ của Kostrikin. Zelmanov khép nó bằng cách đào sâu bộ công cụ Lie và Jordan chứ không bằng xây dựng small-cancellation hình học mới. Huy chương ghi nhận một định lý hữu hạn kiểu phân loại đã hoàn tất trong một lĩnh vực nổi tiếng vì phản ví dụ.

Lớp 1994 còn có Bourgain, Lions, và Yoccoz. Chân dung Zelmanov là mặt đại số của đại hội Zürich đó.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Zelmanov giải bài toán Burnside.” | Ông giải bài toán Burnside **hạn chế**. Các bài toán không hạn chế/bị chặn có câu trả lời phủ định nói chung. |
| “Mọi nhóm số mũ hữu hạn đều hữu hạn.” | Sai: $$B(d,n)$$ vô hạn với nhiều $$n$$. |
| “Golod–Shafarevich đã xong tất cả.” | Họ giết bài toán *tổng quát* (không bị chặn đều). Burnside hạn chế nói về nhóm hữu hạn số mũ cố định. |
| “Kostrikin làm cả bài toán hạn chế.” | Kostrikin: số mũ **nguyên tố**. Zelmanov: số mũ lẻ và $$2$$-nhóm, do đó mọi $$n$$. |
| “Hạn chế nghĩa là ‘dễ hơn, nên nhóm hữu hạn.’” | Hạn chế nghĩa là “chỉ hỏi về nhóm **hữu hạn**.” Nhóm Burnside tự do vẫn có thể vô hạn. |
| “Chứng minh thuần tổ hợp lý thuyết nhóm.” | Máy là **vành Lie / đại số Lie**, với nền đại số Jordan. |

---

## Bài tập

1. Viết ba câu, mỗi câu một bài toán Burnside (tổng quát, bị chặn, hạn chế), sao cho bạn cùng lớp không thể trộn.
2. Vì sao tính vô hạn của $$B(d,n)$$ **không** mâu thuẫn tính hữu hạn của nhóm Burnside hạn chế $$B_0(d,n)$$?
3. Golod–Shafarevich xây gì, và câu hỏi Burnside nào được trả lời?
4. Kostrikin versus Zelmanov: mỗi người một câu, gồm các từ “số mũ nguyên tố” và “mọi số mũ.”
5. Ở mức khẩu hiệu, một đẳng thức đại số Lie mã hóa $$x^n=1$$ thế nào? (Không cần công thức đúng; cần ý “phân bậc liên kết + Engel/sandwich.”)
6. Lướt bài giảng ICM 1994 của Feit hoặc trang Wikipedia về bài toán Burnside và liệt kê **ba** tên ngoài Zelmanov phải xuất hiện trong mọi lịch sử trung thực.
7. **Luyện độ chính xác.** Viết lại “Zelmanov chỉ ra các nhóm Burnside hữu hạn” thành hai câu khóa học này chấp nhận.
8. **Seminar.** So huy chương này với câu chuyện “huy chương phản ví dụ” (quái vật vô hạn) versus câu chuyện “huy chương hữu hạn” (Burnside hạn chế). Vì sao cùng một họ câu hỏi sinh cả hai?

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

- Đọc một trang survey về vì sao số mũ lẻ lớn làm $$B(d,n)$$ vô hạn (small cancellation), rồi trở lại máy vành Lie; lưu ý $$B(2,5)$$ vẫn là trường hợp bị chặn mở nổi tiếng.
- Gợi ý seminar: nếu các chặn hiệu quả cực lớn, định lý *để làm gì*?
