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

*Tạm dịch: vì lời giải bài toán Burnside hạn chế.*

Bài giới thiệu tại ICM của Walter Feit cũng nói đúng như vậy: Zelmanov nhận huy chương vì đã giải bài toán Burnside hạn chế. Chữ **hạn chế** (restricted) là điểm mấu chốt của cả bài này. Năm 1902, William Burnside hỏi: một nhóm hữu hạn sinh mà mọi phần tử đều có cấp hữu hạn thì có nhất thiết là nhóm hữu hạn không? Ngay cả ở dạng mạnh nhất với "số mũ bị chặn", tức mọi phần tử thỏa $$x^n=1$$ với một $$n$$ cố định, câu trả lời nói chung là **không**: tồn tại những nhóm hữu hạn sinh, vô hạn, có số mũ hữu hạn (Golod–Shafarevich cho trường hợp cấp các phần tử không bị chặn đều; Novikov–Adian, Ol’shanskii, Ivanov và những người khác cho số mũ lớn). Zelmanov **không** lật ngược các định lý đó. Ông trả lời một câu hỏi khác, được đặt ra từ những năm 1930 và được Wilhelm Magnus đặt tên: nếu chỉ xét các nhóm **hữu hạn**, có một chặn trên chung cho cấp của mọi nhóm $$d$$-sinh có số mũ $$n$$ hay không? Nói cách khác: sai khác đẳng cấu, có phải chỉ có hữu hạn nhóm hữu hạn $$d$$-sinh với số mũ $$n$$? Câu trả lời là **có**, với mọi $$d$$ và mọi $$n$$. A. I. Kostrikin đã giải trường hợp số mũ nguyên tố; Zelmanov giải trường hợp số mũ lẻ (1990), rồi trường hợp $$2$$-nhóm (1991), từ đó suy ra mọi số mũ.

Bài này dành cho người đã biết cách cho nhóm bằng phần tử sinh và hệ thức, và muốn phân biệt rõ ba bài toán Burnside, không gộp chúng thành một câu chung chung.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu câu hỏi năm 1902 của Burnside: một nhóm tuần hoàn hữu hạn sinh có nhất thiết hữu hạn không?
- Phân biệt bài toán **tổng quát** (tuần hoàn, không có số mũ chung), bài toán **Burnside bị chặn** (số mũ $$n$$ cố định), và bài toán **Burnside hạn chế** (tính hữu hạn của tập các nhóm *hữu hạn* $$d$$-sinh có số mũ $$n$$).
- Nêu ngắn gọn các phản ví dụ: **Golod–Shafarevich** ($$p$$-nhóm hữu hạn sinh, vô hạn, cấp các phần tử không bị chặn đều); **Novikov–Adian** (nhóm Burnside tự do $$B(d,n)$$ vô hạn với $$n$$ lẻ đủ lớn); các kết quả về số mũ chẵn sau này của **Ivanov** và **Lysënok**; "quái vật Tarski" của **Ol’shanskii**.
- Phát biểu định lý Zelmanov: với mọi $$d,n$$, chỉ có hữu hạn nhóm hữu hạn $$d$$-sinh có số mũ $$n$$ (tương đương: nhóm Burnside hạn chế là hữu hạn).
- Ghi công **Kostrikin** cho trường hợp số mũ nguyên tố của bài toán hạn chế.
- Mô tả ngắn gọn phương pháp: chuyển từ nhóm sang **vành Lie / đại số Lie** liên kết, dùng các đồng nhất thức, với nền tảng là **đại số Jordan**.
- Tránh các câu sai "Zelmanov giải bài toán Burnside" và "mọi nhóm Burnside đều hữu hạn".

**Kiến thức nền.** Nhóm cho bởi phần tử sinh và hệ thức; sự khác nhau giữa "mọi phần tử có cấp hữu hạn" và "có một $$n$$ chung sao cho $$x^n=1$$"; khái niệm đại số Lie như một phép toán móc song tuyến tính thỏa đồng nhất thức Jacobi và $$[x,x]=0$$. Không cần học trước lý thuyết nhóm tổ hợp.

**Liên kết với các bài khác.** Bài này cho thấy một câu hỏi cổ điển tách thành nhiều định lý khác nhau, và các bài viết phóng đại về huy chương hay bỏ mất chữ "hạn chế". Đọc cùng các bài khác trong chương có kiểu "một tên bài toán, nhiều nghĩa", và với các chương trình cấu trúc dài hơi trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/).

---

## 1. Ba bài toán chung một tên

Một nhóm $$G$$ gọi là **tuần hoàn** (hay nhóm xoắn, torsion) nếu mọi phần tử đều có cấp hữu hạn. Nhóm hữu hạn thì tuần hoàn; $$p$$-nhóm Prüfer là tuần hoàn và vô hạn, nhưng không hữu hạn sinh. Burnside hỏi:

> Nếu $$G$$ hữu hạn sinh và tuần hoàn, thì $$G$$ có nhất thiết hữu hạn không?

Đó là **bài toán Burnside tổng quát**. Một phiên bản chặt hơn cố định số mũ: tồn tại $$n$$ sao cho $$g^n=1$$ với mọi $$g\in G$$. **Nhóm Burnside tự do** $$B(d,n)$$ là nhóm $$d$$-sinh lớn nhất có số mũ $$n$$ (thương của nhóm tự do $$F_d$$ theo nhóm con chuẩn tắc đầy đủ (fully invariant) sinh bởi mọi lũy thừa bậc $$n$$). **Bài toán Burnside bị chặn** hỏi: với những $$d,n$$ nào thì $$B(d,n)$$ hữu hạn?

Một số trường hợp có câu trả lời khẳng định được biết từ sớm. $$B(1,n)$$ là nhóm cyclic cấp $$n$$. $$B(d,2)$$ là nhóm abel sơ cấp hạng $$d$$. Burnside, Sanov và Marshall Hall chứng minh tính hữu hạn của $$B(d,3)$$, $$B(d,4)$$ và $$B(d,6)$$. Với hầu hết các số mũ nhỏ khác, nổi tiếng nhất là $$B(2,5)$$, câu hỏi vẫn còn mở. Với số mũ lớn, câu trả lời là phủ định, như mục sau nhắc lại.

**Bài toán Burnside hạn chế** đổi đối tượng xét. Nó không hỏi $$B(d,n)$$ có hữu hạn không. Nó hỏi các thương **hữu hạn** của $$B(d,n)$$ có cấp bị chặn hay không. Tương đương: có một nhóm hữu hạn $$d$$-sinh số mũ $$n$$ lớn nhất hay không, thường ký hiệu là $$\widehat{B}(d,n)$$ hoặc $$B_0(d,n)$$, thu được bằng cách lấy thương của $$B(d,n)$$ theo giao của mọi nhóm con chuẩn tắc có chỉ số hữu hạn. Nếu thương hữu hạn lớn nhất đó tồn tại và hữu hạn, thì mọi nhóm hữu hạn $$d$$-sinh số mũ $$n$$ đều là thương của một nhóm hữu hạn duy nhất, nên chỉ có hữu hạn lớp đẳng cấu.

Zelmanov chứng minh thương hữu hạn lớn nhất này là **hữu hạn** với mọi $$d$$ và mọi $$n$$.

---

## 2. Các bài toán không hạn chế: câu trả lời là không

Năm 1964, Evgeny Golod và Igor Shafarevich xây dựng các $$p$$-nhóm hữu hạn sinh vô hạn (dựa trên một định lý về cách cho đại số bằng phần tử sinh và hệ thức). Các nhóm này tuần hoàn, nên chúng bác bỏ bài toán Burnside tổng quát; nhưng cấp của các phần tử không bị chặn bởi một $$n$$ cố định cho trước.

Bài toán số mũ bị chặn đòi hỏi kỹ thuật khác. Năm 1968, Pyotr Novikov và Sergei Adian chứng minh $$B(d,n)$$ vô hạn với $$d\ge 2$$ và $$n$$ lẻ lớn hơn $$4381$$ (sau đó Adian hạ ngưỡng lẻ xuống $$665$$). Alexander Ol’shanskii đưa ra các cách xây dựng hình học cho những nhóm hữu hạn sinh vô hạn, có số mũ là một số nguyên tố lẻ lớn, trong đó mọi nhóm con thực sự đều là nhóm cyclic (quái vật Tarski). Đây là một ví dụ đặc biệt ấn tượng về một nhóm vô hạn mà mọi nhóm con thực sự đều rất nhỏ. Trường hợp số mũ chẵn khó hơn: S. V. Ivanov (1994) chứng minh tính vô hạn với số mũ chẵn lớn chia hết cho một lũy thừa cao của $$2$$; I. G. Lysënok (1996) cải thiện ngưỡng cho số mũ chẵn. Kết luận cho khóa học:

**Nhiều nhóm Burnside tự do $$B(d,n)$$ là vô hạn.** Định lý Zelmanov không mâu thuẫn với điều đó. Một nhóm vô hạn vẫn có thể chỉ có hữu hạn thương hữu hạn; cụ thể, giao của mọi nhóm con chuẩn tắc có chỉ số hữu hạn trong $$B(d,n)$$ có thể là một nhóm con vô hạn, trong khi thương hữu hạn $$B_0(d,n)$$ vẫn hữu hạn.

Đừng nói "các nhóm Burnside là hữu hạn". Đừng nói "Zelmanov chỉ ra chúng hữu hạn".

---

## 3. Bài toán hạn chế: Kostrikin rồi Zelmanov

Cuối những năm 1950, Kostrikin công bố rằng bài toán Burnside hạn chế có câu trả lời khẳng định cho số mũ **nguyên tố** $$p$$: tồn tại một nhóm hữu hạn $$d$$-sinh số mũ $$p$$ lớn nhất. Lập luận là một định lý về đại số Lie đặc số $$p$$ (một đồng nhất thức kiểu Engel kéo theo tính lũy linh trong vành Lie liên kết). Những chỗ chưa chặt trong cách trình bày ban đầu được sửa về sau; cuốn *Around Burnside* của Kostrikin là tài liệu chuẩn cho trường hợp này, và đã nhắc tới công trình sau đó của Zelmanov.

Các bài báo của Zelmanov là:

- "Solution of the restricted Burnside problem for groups of odd exponent", *Izv. Akad. Nauk SSSR Ser. Mat.* 54 (1990); bản tiếng Anh *Math. USSR-Izv.* 36 (1991), 41–60.
- "Solution of the restricted Burnside problem for $$2$$-groups", *Mat. Sb.* 182 (1991); bản tiếng Anh *Math. USSR-Sb.* 72 (1992), 543–565.

Kết hợp với các bổ đề đưa số mũ tổng quát về số mũ là lũy thừa của số nguyên tố (dựa trên lý thuyết Sylow và các lập luận về nhóm hữu hạn liên quan), hai bài này cho định lý hạn chế với **mọi** $$n$$. Bài giảng năm 1994 của Feit nhấn mạnh rằng Zelmanov trước hết làm đơn giản và mở rộng bộ máy đại số Lie ra ngoài trường hợp nguyên tố của Kostrikin, rồi xử lý trường hợp $$2$$-nhóm khó hơn nhiều.

---

## 4. Phương pháp, nói ngắn gọn: nhóm, vành Lie, đại số Jordan

Theo cách nói của Feit, bài toán hạn chế "phần lớn là một bài toán về đại số Lie". Phương pháp cổ điển của trường phái Nga (Kostrikin, Magnus, Sanov, Zelmanov) như sau:

1. Bắt đầu với một nhóm hữu hạn $$d$$-sinh $$G$$ có số mũ $$n$$. Ta muốn chặn $$\lvert G\rvert$$ bằng một số chỉ phụ thuộc $$d$$ và $$n$$.
2. Chuyển sang **vành Lie** liên kết (hoặc đại số Lie phân bậc trên trường hữu hạn), xây từ dãy tâm dưới, hoặc từ $$p$$-dãy Jennings–Zassenhaus khi $$n$$ là lũy thừa của một số nguyên tố. Điều kiện số mũ $$n$$ trở thành một **đồng nhất thức** trong vành Lie này: điều kiện kiểu Engel, ràng buộc trên toán tử ad, hoặc đồng nhất thức "sandwich".
3. Chứng minh rằng một đại số Lie trên trường đặc số hữu hạn, thỏa các đồng nhất thức đó và sinh bởi $$d$$ phần tử, phải **lũy linh** với lớp bị chặn, hoặc ít nhất hữu hạn chiều với số chiều bị chặn.
4. Chuyển chặn trên đại số Lie ngược lại thành chặn cho cấp của $$G$$.

Bước khó là bước (3). Công trình trước đó của Zelmanov về **đại số Jordan** (cấu trúc của đại số Jordan vô hạn chiều; các đồng nhất thức như của Glennie) cho ông công cụ xử lý các đồng nhất thức không kết hợp xuất hiện trong tác động phụ hợp (ad), và ông chứng minh đồng nhất thức Engel kéo theo tính lũy linh mà không cần giả thiết hữu hạn chiều. Khóa học sẽ không dựng lại các đồng nhất thức đó. Tóm tắt: bài toán Burnside hạn chế là **một định lý hữu hạn cho đại số Lie thỏa đồng nhất thức**, được chuyển sang nhóm qua vành Lie liên kết. Vì thế một huy chương về lý thuyết nhóm lại dựa trên nền tảng là các nghiên cứu về đại số Jordan.

---

## 5. Định lý cho biết gì và không cho biết gì

Định lý cho một **chặn trên chung**. Nó không liệt kê các nhóm hữu hạn có số mũ $$n$$, và các chặn tường minh thường cực kỳ lớn. Nó cũng không cho biết $$B(d,n)$$ nào là hữu hạn: bài toán hạn chế có lời giải khẳng định trong khi bản thân $$B(d,n)$$ vẫn có thể vô hạn.

Bảng so sánh:

| Câu hỏi | Trả lời |
|---------|---------|
| Mọi nhóm tuần hoàn hữu hạn sinh có hữu hạn không? | **Không** (Golod–Shafarevich). |
| Mọi $$B(d,n)$$ có hữu hạn không? | **Không** với nhiều $$n$$ lớn; **có** với một số $$n$$ nhỏ; một số trường hợp nhỏ vẫn **mở**. |
| Có phải chỉ có hữu hạn nhóm *hữu hạn* $$d$$-sinh số mũ $$n$$? | **Có**, với mọi $$d,n$$ (Kostrikin cho $$n=p$$; Zelmanov cho trường hợp tổng quát). |

Lời trao giải Fields ứng với hàng thứ ba.

---

## 6. Vì sao là Huy chương Fields

Câu hỏi của Burnside là một trong những câu hỏi lâu đời nhất của lý thuyết nhóm tổ hợp. Đến năm 1994, các bài toán không hạn chế đã cho ra một số nhóm "kỳ quặc" nhất từng được xây dựng, nên người chỉ nghe qua có thể nghĩ "bài toán Burnside đã xong". Bài toán hạn chế là câu hỏi về tính hữu hạn mà người ta vẫn hy vọng có câu trả lời **khẳng định**, và nó đã chống lại mọi nỗ lực với các số mũ không phải số nguyên tố, ngoài trường hợp $$p$$ của Kostrikin. Zelmanov giải xong nó bằng cách đào sâu bộ công cụ Lie và Jordan, chứ không bằng các xây dựng hình học kiểu "triệt tiêu nhỏ" (small cancellation) mới. Huy chương ghi nhận một định lý hữu hạn hoàn chỉnh trong một lĩnh vực vốn nổi tiếng vì các phản ví dụ.

Những người cùng nhận huy chương năm 1994 là Bourgain, Lions và Yoccoz. Zelmanov là đại diện cho mảng đại số tại đại hội Zürich năm đó.

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

## Bài tập

1. Viết ba câu, mỗi câu cho một bài toán Burnside (tổng quát, bị chặn, hạn chế), rõ đến mức bạn cùng lớp không thể nhầm lẫn.
2. Vì sao tính vô hạn của $$B(d,n)$$ **không** mâu thuẫn với tính hữu hạn của nhóm Burnside hạn chế $$B_0(d,n)$$?
3. Golod–Shafarevich xây dựng được gì, và nó trả lời câu hỏi Burnside nào?
4. Kostrikin và Zelmanov: viết cho mỗi người một câu, có dùng các cụm "số mũ nguyên tố" và "mọi số mũ".
5. Nói ngắn gọn: một đồng nhất thức trong đại số Lie mã hóa điều kiện $$x^n=1$$ như thế nào? (Không cần công thức chính xác; chỉ cần ý "đại số phân bậc liên kết + đồng nhất thức Engel / sandwich".)
6. Đọc lướt bài giảng ICM 1994 của Feit hoặc trang Wikipedia về bài toán Burnside, và liệt kê **ba** tên người, ngoài Zelmanov, phải có mặt trong mọi bài lịch sử trung thực.
7. **Luyện phát biểu chính xác.** Viết lại câu "Zelmanov chỉ ra các nhóm Burnside là hữu hạn" thành hai câu đúng, phù hợp với khóa học.
8. **Thảo luận.** So sánh hai kiểu kết quả: kiểu "phản ví dụ" (các nhóm vô hạn kỳ quặc) và kiểu "hữu hạn" (bài toán Burnside hạn chế). Vì sao cùng một họ câu hỏi lại sinh ra cả hai?

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
