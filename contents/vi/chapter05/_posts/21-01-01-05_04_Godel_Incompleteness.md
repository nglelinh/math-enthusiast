---
layout: post
title: "Định lý Bất toàn Gödel"
chapter: '05'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter05
---

Tháng 9 năm 1930, tại thành phố Königsberg — chính quê hương của bài toán bảy cây cầu — đại kiện tướng toán học **David Hilbert** khép lại bài diễn văn nghỉ hưu bằng lời tuyên ngôn vang vọng khắp thế kỷ: *"Wir müssen wissen, wir werden wissen"* — *"Chúng ta phải biết, chúng ta sẽ biết."* Giấc mơ cả đời ông (Chương trình Hilbert) là xây dựng một bộ tiên đề hoàn chỉnh, chặt chẽ tuyệt đối, không bao giờ tự mâu thuẫn, để từ đó có thể chứng minh hoặc bác bỏ **mọi** mệnh đề toán học.

Điều trớ trêu của lịch sử là: ngay ngày hôm trước, tại một bàn tròn nhỏ trong cùng hội nghị ấy, một nhà logic học 24 tuổi trầm lặng đến từ Vienna tên **Kurt Gödel** đã nhẹ nhàng công bố một kết quả làm sụp đổ vĩnh viễn giấc mơ đó.

**Các định lý bất toàn của Gödel** (1931) không nói rằng "toán học bị hỏng" hay "không gì chứng minh được". Điều chúng khẳng định sắc bén hơn nhiều: mọi hệ tiên đề hình thức đủ mạnh để làm số học sơ cấp, có tập tiên đề cho được một cách hiệu quả, và nhất quán thì **luôn bất toàn** (tồn tại những mệnh đề mà hệ không chứng minh cũng không bác bỏ được), và hệ đó cũng **không thể tự chứng minh tính nhất quán của chính mình** bằng các công cụ bên trong nó. Trở ngại này không đến từ sự thiếu kiên nhẫn của con người, mà nằm ngay trong mối quan hệ sâu thẳm giữa cú pháp, con số và tính tự quy chiếu.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Phát biểu định lý bất toàn thứ nhất và thứ hai ở dạng không hình thức nhưng chính xác.
- Giải thích số Gödel là cách biến cú pháp thành số học.
- Mô tả câu tự quy chiếu ở mức ý chính ("tôi không chứng minh được") và vì sao, nếu lý thuyết nhất quán, câu đó đúng nhưng không chứng minh được.
- Phân biệt bất toàn với không nhất quán, và với bất khả quyết định theo nghĩa tính toán (có liên quan nhưng không phải một).
- Tránh các cách diễn giải sai phổ biến (cho rằng mọi chân lý đều tương đối, hoặc cho rằng trí óc con người vượt máy móc mà không có thêm lập luận).
- Nối tinh thần đường chéo với Cantor và với các kết quả về tính toán được sau này.

**Kiến thức cần có.** Quen với ý tưởng chứng minh hình thức là một chuỗi ký hiệu hữu hạn theo quy tắc, và số học cơ bản. Không cần học logic trước; ta chỉ làm ở mức ý tưởng.

---

## Bản đồ kiến thức nền: Logic toán, chứng minh hình thức và Định lý bất toàn Gödel là gì?

Nhiều người tốt nghiệp đại học từng nghe về Định lý Gödel qua các bài báo triết học nhưng vẫn thấy mơ hồ vì thiếu ba khái niệm trụ cột của **Logic toán (Mathematical Logic)**:

- **Cú pháp (Syntax) so với Ngữ nghĩa (Semantics):** Trong toán học, ta cần phân biệt rạch ròi hai thế giới. Thế giới *cú pháp* giống như một trò chơi đẩy ký hiệu theo luật: từ các tiên đề ban đầu, áp dụng quy tắc suy diễn cơ học để rút ra dòng kết luận (ký hiệu $$T \vdash \varphi$$, đọc là "hệ $$T$$ chứng minh được $$\varphi$$"). Thế giới *ngữ nghĩa* nói về việc mệnh đề ấy có **đúng** trong thế giới thực của các số tự nhiên $$\mathbb{N}$$ hay không (ký hiệu $$\mathbb{N} \models \varphi$$).
- **Hệ tiên đề hình thức (Formal System) là gì?** Đó là một "cỗ máy chứng minh" được đặc tả rõ ràng đến mức một máy tính có thể kiểm tra từng dòng xem chứng minh có hợp lệ không — chẳng hạn **Số học Peano (PA)** cho các số tự nhiên, hay **Lý thuyết tập hợp ZFC** cho gần như toàn bộ toán học hiện đại.
- **Ba phẩm chất mà Hilbert mơ ước:**
  1. **Nhất quán (Consistent):** Không bao giờ chứng minh được cả $$\varphi$$ lẫn $$\neg \varphi$$ (không sinh ra mâu thuẫn kiểu $$0 = 1$$).
  2. **Đầy đủ (Complete):** Với mọi câu $$\varphi$$, hệ phải chứng minh được ít nhất một trong hai: $$\varphi$$ hoặc $$\neg \varphi$$.
  3. **Tiên đề hóa hiệu quả (Effectively axiomatized):** Có một thuật toán hữu hạn kiểm tra được một dòng có phải tiên đề hay không.

Định lý bất toàn của Gödel vạch ra ranh giới vĩnh viễn giữa *chân lý* ($$\models$$) và *khả năng chứng minh* ($$\vdash$$): bạn không thể vừa có một cỗ máy nhất quán, hiệu quả, đủ mạnh để làm số học, vừa đòi nó bắt trọn mọi chân lý số học.

---

## 1. Một lý thuyết hình thức là gì

Một **hệ tiên đề hình thức** cho số học (theo nghĩa cần dùng ở đây) gồm:

- bảng ký hiệu và ngôn ngữ chính xác ($$0$$, hàm kế tiếp, phép cộng, phép nhân, lượng từ, các liên kết logic);
- một tập tiên đề quyết định được (hoặc một lược đồ tiên đề hiệu quả);
- các quy tắc suy diễn có thể thực hiện máy móc.

**Chứng minh** là một dãy hữu hạn các công thức, trong đó mỗi dòng là tiên đề hoặc suy ra được từ các dòng trước. "$$T$$ chứng minh $$\varphi$$" nghĩa là tồn tại một dãy như vậy kết thúc ở $$\varphi$$. Vì chứng minh là một đối tượng tổ hợp hữu hạn, nên sau khi mã hóa, câu hỏi "có chứng minh được hay không" trở thành một câu hỏi về số.

Hilbert hỏi đại ý: có thể chọn một lý thuyết nhất quán, đầy đủ, trình bày được một cách hiệu quả, nắm bắt đúng chân lý số học, và chứng minh được tính nhất quán của nó bằng phương tiện hữu hạn không? Ở đây "đầy đủ" nghĩa là với mọi câu $$\varphi$$, hoặc $$\varphi$$ hoặc $$\neg\varphi$$ chứng minh được.

---

## 2. Các định lý (phát biểu ở mức ý tưởng)

**Định lý bất toàn thứ nhất (không hình thức).**
Cho $$T$$ là lý thuyết nhất quán, có tiên đề cho được hiệu quả, và đủ mạnh để biểu đạt một phần số học sơ cấp (kiểu Peano hoặc tương đương). Khi đó tồn tại câu $$G$$ trong ngôn ngữ của $$T$$ sao cho $$T$$ không chứng minh $$G$$ và cũng không chứng minh $$\neg G$$. Nói riêng, $$T$$ bất toàn.

**Định lý bất toàn thứ hai (không hình thức).**
Dưới các giả thiết tương tự, nếu $$T$$ nhất quán thì $$T$$ không chứng minh được $$\mathrm{Con}(T)$$, tức câu số học biểu đạt tính nhất quán của $$T$$. Nói gọn: một lý thuyết đủ mạnh không thể tự bảo đảm tính nhất quán của mình từ bên trong.

Cũng có những phát biểu hiện đại chính xác hơn (về tính biểu diễn được, vị từ chứng minh được, v.v.). Các phát biểu ở trên là mức bạn nên nắm.

---

## 3. Số Gödel: biến cú pháp thành số

Ý tưởng lớn thứ nhất là **số hóa cú pháp** (Gödel numbering). Mỗi ký hiệu có một mã số tự nhiên; mỗi chuỗi hữu hạn ký hiệu có một mã duy nhất; mỗi dãy các chuỗi (tức một bản chứng minh hoàn chỉnh) cũng có một mã duy nhất.

**Ví dụ cụ thể về mã hóa Gödel.** Giả sử ta gán mã nhỏ cho vài ký hiệu: ký hiệu `0` có mã $$1$$, ký hiệu `=` có mã $$3$$, ký hiệu `S` (số kế tiếp) có mã $$2$$. Để mã hóa công thức `0=0` (chuỗi ba ký hiệu có mã lần lượt là $$1, 3, 1$$), ta dùng lũy thừa của các số nguyên tố liên tiếp $$2, 3, 5$$:

$$
\ulcorner 0=0 \urcorner \;=\; 2^1 \cdot 3^3 \cdot 5^1 \;=\; 2 \cdot 27 \cdot 5 \;=\; 270.
$$

Nhờ Định lý Cơ bản của Số học (phân tích thừa số nguyên tố là duy nhất), từ con số $$270$$ ta giải mã ngược ra chính xác chuỗi `0=0` mà không bao giờ nhầm lẫn với bất kỳ chuỗi nào khác! Tương tự, một bản chứng minh gồm $$k$$ dòng công thức có mã $$g_1, g_2, \ldots, g_k$$ được gói gọn thành một số nguyên duy nhất $$2^{g_1} \cdot 3^{g_2} \cdots p_k^{g_k}$$.

Khi đó có một quan hệ số học thuần túy, ký hiệu $$\mathrm{Proof}_T(m,n)$$, đúng khi $$m$$ mã hóa một chứng minh hợp lệ trong $$T$$ của công thức có mã là $$n$$. Vì tiên đề cho được hiệu quả và quy tắc suy diễn là máy móc, quan hệ "$$m$$ là chứng minh của $$n$$" quyết định được (và biểu diễn được bằng cộng, nhân trong số học). Khi đó "chứng minh được" trở thành

$$
\mathrm{Prov}_T(n) \;:\iff\; \exists m\, \mathrm{Proof}_T(m,n).
$$

Điều đáng kinh ngạc là $$T$$ vốn chỉ nói về số tự nhiên, nay bỗng nhiên nói được về **chứng minh các mệnh đề về số**, vì chính các bản chứng minh cũng đã hóa thân thành số. Phép gán từng đối tượng ngôn ngữ với một số nguyên chính là chiếc cầu nối.

---

### Video ngắn: Kurt Gödel (1931): Định lý Bất toàn

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/godel-incompleteness_vi.mp4"></video>
</div>

Video dài khoảng 2 phút 23 giây (có thuyết minh tiếng Việt giọng Algenib): chương trình Hilbert, mã hóa Gödel biến công thức thành số nguyên tố (ví dụ 270 = 2¹·3³·5¹), bổ đề điểm bất động tạo câu tự quy chiếu G ⇔ (T ⊬ G), và vì sao đúng chưa chắc chứng minh được.

## 4. Từ Nghịch lý Kẻ Nói Dối đến câu tự quy chiếu Gödel

Hãy bắt đầu từ một nghịch lý đời thường có từ thời Hy Lạp cổ đại — **Nghịch lý Kẻ Nói Dối (Liar Paradox)**:

> *"Câu này là sai."*

Nếu câu này đúng thì nội dung của nó buộc nó phải sai. Nếu nó sai thì điều nó nói lại hóa ra đúng! Trong ngôn ngữ tự nhiên, tự quy chiếu với khái niệm "sai" lập tức nổ tung thành mâu thuẫn.

Cú thiên tài của Gödel là nhận ra: trong số học hình thức, ta **không thể** viết vị từ "sai" (Định lý không định nghĩa được chân lý của Tarski), nhưng ta **có thể** viết vị từ *"không chứng minh được trong $$T$$"* nhờ số hóa Gödel! Khi thay từ "sai" bằng cụm *"không chứng minh được trong $$T$$"*, nghịch lý không còn nổ tung thành mâu thuẫn nữa — nó biến hình thành một định lý chấn động.

Ý tưởng lớn thứ hai là tạo ra tự quy chiếu hoàn toàn chặt chẽ thông qua phép dựng đường chéo (**Bổ đề điểm bất động**). Với công thức $$\psi(x)$$ phù hợp, tồn tại câu $$\varphi$$ sao cho $$T$$ chứng minh

$$
\varphi \;\leftrightarrow\; \psi(\ulcorner\varphi\urcorner),
$$

trong đó $$\ulcorner\varphi\urcorner$$ là số Gödel của $$\varphi$$. Áp dụng cho tính chất "không chứng minh được", ta được câu $$G$$ sao cho $$T$$ chứng minh được

$$
G \;\leftrightarrow\; \neg\mathrm{Prov}_T(\ulcorner G\urcorner).
$$

Nói bằng lời: $$G$$ nói rằng "$$G$$ không chứng minh được trong $$T$$". Đây là **câu Gödel** của $$T$$.

### Vì sao nhất quán kéo theo $$G$$ không chứng minh được

- **Trường hợp 1:** Giả sử $$T$$ chứng minh được $$G$$. Khi đó tồn tại một mã chứng minh $$m$$ cho $$G$$, nên $$\mathrm{Prov}_T(\ulcorner G\urcorner)$$ đúng và chứng minh được trong $$T$$. Nhưng vì $$T \vdash G \leftrightarrow \neg\mathrm{Prov}_T(\ulcorner G\urcorner)$$, điều này kéo theo $$T$$ chứng minh được cả $$G$$ lẫn $$\neg G$$ — làm $$T$$ **không nhất quán**!
- **Trường hợp 2:** Vậy nếu $$T$$ nhất quán, thì $$T$$ **không thể** chứng minh $$G$$. Nhưng khoan đã: chính câu $$G$$ lại phát biểu rằng *"$$G$$ không chứng minh được trong $$T$$"*. Vậy điều $$G$$ nói là **hoàn toàn đúng** trong mô hình chuẩn $$\mathbb{N}$$!

Kết luận: $$G$$ **đúng nhưng không chứng minh được** trong $$T$$. Do đó $$T$$ không nắm hết chân lý số học và chắc chắn bất toàn. (Gödel ban đầu dùng giả thiết mạnh hơn gọi là $$\omega$$-nhất quán để loại trừ khả năng $$T \vdash \neg G$$; năm 1936, J. Barkley Rosser cải tiến câu tự quy chiếu để chỉ cần đúng giả thiết nhất quán.)

Cấu trúc của chứng minh có thể tóm lại thành một mạch bốn bước:

**mã hóa → vị từ "chứng minh được" nằm trong hệ → tự quy chiếu bằng phép đường chéo → câu đúng nhưng không chứng minh được.**

---

## 5. Định lý thứ hai: tính nhất quán không có sẵn

Định lý thứ hai nói rằng câu $$\mathrm{Con}(T)$$ (biểu đạt "$$T$$ không chứng minh ra mâu thuẫn", chẳng hạn $$\neg\mathrm{Prov}_T(\ulcorner 0=1\urcorner)$$) không chứng minh được trong $$T$$, nếu $$T$$ nhất quán và đủ mạnh. Trực giác rất gọn: toàn bộ lập luận "nếu $$T$$ nhất quán thì $$T$$ không chứng minh được $$G$$" ở định lý thứ nhất có thể hình thức hóa ngay bên trong $$T$$ thành

$$
T \vdash \mathrm{Con}(T) \rightarrow G.
$$

Nếu $$T$$ chứng minh được $$\mathrm{Con}(T)$$, thì theo luật suy diễn *modus ponens*, $$T$$ lập tức chứng minh được $$G$$ — mâu thuẫn với định lý thứ nhất! Vì vậy, để chứng minh một hệ mạnh là nhất quán, ta buộc phải dùng những nguyên lý **không có sẵn trong hệ đó**, hoặc bước lên một siêu lý thuyết mạnh hơn (ví dụ: ta có thể chứng minh Số học Peano nhất quán bằng cách đứng bên trong ZFC, nhưng ZFC lại không thể tự bảo lãnh cho chính mình).

Đây là lý do hy vọng của Hilbert — chứng minh tính nhất quán của toàn bộ toán học bằng các phương tiện hữu hạn nằm gọn trong một hệ yếu — không thể thực hiện đối với các hệ đã chứa một lượng số học đáng kể.

---

## 6. Bất toàn *không* có nghĩa là gì

| Cách hiểu sai | Cách hiểu đúng |
|---------------|-----|
| "Không gì chứng minh được." | Phần lớn toán học vẫn được chứng minh như cũ; bất toàn chỉ giới hạn việc *một* hệ hiệu quả nắm trọn chân lý số học. |
| "Mọi hệ đều không nhất quán." | Định lý giả định hệ nhất quán để kết luận nó bất toàn. |
| "Con người thấy được chân lý mà máy không thấy." | Riêng các định lý này không chứng tỏ trí óc người vượt trội về bản chất. |
| "Bất toàn là bất khả quyết định của bài toán dừng." | Hai kết quả cùng họ đường chéo nhưng không phải một định lý. |
| "Gödel chứng minh toán học là chủ quan." | Ông chỉ ra giới hạn của một bộ tiên đề; thực hành toán học vẫn tiếp tục với chứng minh, mô hình và nhất quán tương đối. |

---

## 7. Họ hàng của phương pháp đường chéo: Cantor, Turing, Gödel

Cantor dựng một số thực không có trong danh sách nào. Turing dựng một hành vi mà không máy nào có. Gödel dựng một câu mà chứng minh nào trong $$T$$ cũng không chứng minh được, bằng cách cho câu đó nói về tính không chứng minh được của chính nó. Điểm chung thực sự là:

- giả sử có một danh sách (lời giải) tổng thể;
- dựng một đối tượng khác danh sách ở ngay vị trí đường chéo;
- kết luận rằng trong khung đã cho không có lời giải hiệu quả đầy đủ.

Hiểu Cantor rồi thì chiến lược của Gödel bớt giống ảo thuật, và giống một người anh em họ chính xác hơn.

---

## 8. Vì sao quan trọng

- **Nền tảng.** Với số học đủ mạnh, "đầy đủ" và "nhất quán" không thể có cùng lúc như Hilbert từng hy vọng.
- **Thực hành.** Hiếm khi ta gặp câu Gödel trong công việc hằng ngày, nhưng thói quen phân biệt chân lý trong một mô hình với tính chứng minh được trong một lý thuyết vẫn rất quan trọng.
- **Khoa học máy tính.** Ranh giới giữa chứng minh hình thức và chân lý ảnh hưởng đến chứng minh tự động và kiểm chứng phần mềm, và nhắc rằng một hệ không tự chứng minh được tính nhất quán của mình.
- **Triết học.** Các tranh luận về chủ nghĩa Platon, chủ nghĩa hình thức và bản chất của chân lý toán học đã được định hình lại.

---

## Nhầm lẫn thường gặp

1. "Bất toàn nghĩa là tiên đề sai." Thực ra là không có tập tiên đề hiệu quả đủ mạnh nào vừa nhất quán vừa đầy đủ cho số học.
2. "Thêm $$G$$ làm tiên đề là sửa xong mãi mãi." Hệ $$T+G$$ lại có một câu Gödel *riêng* của nó; bất toàn xuất hiện lại.
3. "Số Gödel là thứ huyền bí tùy tiện." Đó là một lược đồ mã hóa, có sức mạnh vì số học biểu đạt được các quan hệ về mã.
4. "Định lý thứ hai nói ta không bao giờ tin được toán học." Nó chỉ nói một lý thuyết không thể là trọng tài duy nhất cho tính nhất quán của chính nó.
5. "Ý tưởng chứng minh chỉ là tự quy chiếu mơ hồ." Tự quy chiếu ở đây hoàn toàn chặt chẽ, nhờ bổ đề điểm bất động và tính biểu diễn được.

---

## Kiến thức rút ra từ phần tìm hiểu video

Tóm tắt dùng khi thảo luận (đối chiếu với nguồn viết; **không bịa nội dung transcript**). Gói: `research/video-research/godel-incompleteness/analysis.md`.

### Tình trạng

**Đã được chứng minh** (Gödel, 1931). Hai định lý bất toàn là định lý của logic toán; các bài phổ biến hay nói quá rằng "toán học bị hỏng".

### Phát biểu cốt lõi

Mọi lý thuyết nhất quán, có tiên đề hiệu quả và đủ mạnh để làm số học đều bất toàn: có những câu đúng (trong $$\mathbb{N}$$) mà lý thuyết không chứng minh được. Định lý thứ hai: một lý thuyết như vậy không thể chứng minh tính nhất quán của chính nó (với các hình thức hóa chuẩn).

### Các định nghĩa cần nắm chắc

- **Lý thuyết hình thức.** Ngôn ngữ, các tiên đề hiệu quả và các quy tắc suy diễn; định lý là các câu suy ra được.
- **Câu Gödel (ý tưởng).** Câu số học tự quy chiếu, khẳng định chính nó không chứng minh được trong $$T$$.

### Những hiểu lầm cần tránh

- Hiểu bất toàn là "không gì chứng minh được" hoặc "mọi hệ đều không nhất quán".
- Lẫn bất toàn với bất khả quyết định của những câu hỏi tùy ý trong ngôn ngữ tự nhiên.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và làm quen với cách nghiên cứu**, không thay cho chứng minh hay bài báo gốc khi cần khẳng định quan trọng. Chi tiết xếp hạng: `research/video-research/godel-incompleteness/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile — Gödel's Incompleteness Theorem (Marcus du Sautoy): [https://www.youtube.com/watch?v=O4ndIDcDSGc](https://www.youtube.com/watch?v=O4ndIDcDSGc).  
2. **Định hướng** — TED-Ed — Paradox at the heart of mathematics (du Sautoy): [https://www.youtube.com/watch?v=I4pQbo5MQOs](https://www.youtube.com/watch?v=I4pQbo5MQOs).  
3. **Cốt lõi** — Veritasium — Math's Fundamental Flaw (Gödel và mạch bất khả quyết định): [https://www.youtube.com/watch?v=HeQX2HjkcNo](https://www.youtube.com/watch?v=HeQX2HjkcNo).  
4. **Nền tảng** — Computerphile — Gödel's Incompleteness (Altenkirch / Lean): [https://www.youtube.com/watch?v=IuX8QMgy4qE](https://www.youtube.com/watch?v=IuX8QMgy4qE).  
5. **Trang giới thiệu** — Trang Numberphile: [https://www.numberphile.com/videos/godels-incompleteness-theorem](https://www.numberphile.com/videos/godels-incompleteness-theorem).  

**Nhắc tình trạng:** **Đã được chứng minh** (Gödel, 1931). Hai định lý bất toàn là định lý của logic toán; các bài phổ biến hay nói quá rằng "toán học bị hỏng".

---


### Transcript và khung hình (trích theo lô)

Transcript caption và unit theo thời gian: `research/video-research/godel-incompleteness/transcripts/` · trạng thái: `research/video-research/godel-incompleteness/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/godel-incompleteness_O4ndIDcDSGc_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói nghiên cứu để biết mốc thời gian).*

## Tài liệu

1. Gödel (1931). *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I* (bản tiếng Anh: *On formally undecidable propositions…*).
2. Sách logic chuẩn: Enderton; Mendelson; hoặc Smullyan về các định lý của Gödel.
3. Nagel & Newman — *Gödel's Proof*.
4. Trong khóa học: [Cantor]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/), [Vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/).

---


Danh mục URL đầy đủ: `research/video-research/godel-incompleteness/references.md`.

### Video (lộ trình gợi ý)

- Numberphile — Gödel's Incompleteness Theorem (Marcus du Sautoy) (ORIENTATION): https://www.youtube.com/watch?v=O4ndIDcDSGc
- TED-Ed — Paradox at the heart of mathematics (du Sautoy) (ORIENTATION): https://www.youtube.com/watch?v=I4pQbo5MQOs
- Veritasium — Math's Fundamental Flaw (Gödel + undecidability arc) (CORE): https://www.youtube.com/watch?v=HeQX2HjkcNo
- Computerphile — Gödel's Incompleteness (Altenkirch / Lean) (FOUNDATION): https://www.youtube.com/watch?v=IuX8QMgy4qE
- Numberphile page (META): https://www.numberphile.com/videos/godels-incompleteness-theorem

### Bài báo và web (từ gói nghiên cứu)

- Wikipedia — Gödel's incompleteness theorems: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
- Stanford Encyclopedia of Philosophy — Gödel's incompleteness: https://plato.stanford.edu/entries/goedel-incompleteness/
- Stanford Encyclopedia of Philosophy, mục của Raatikainen (cùng trang trên): https://plato.stanford.edu/entries/goedel-incompleteness/
- TED-Ed lesson page: https://ed.ted.com/lessons/the-paradox-at-the-heart-of-mathematics-godel-s-incompleteness-theorem-marcus-du-sautoy
- Wikipedia — Hilbert's program (context): https://en.wikipedia.org/wiki/Hilbert%27s_program

### Khóa học

- Gói: `research/video-research/godel-incompleteness/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- So sánh với cải tiến của Rosser cho định lý thứ nhất.
- Nối bất toàn với bài toán thứ mười của Hilbert (định lý khác, cùng chủ đề tính toán).
- Trong các trình hỗ trợ chứng minh: lõi (kernel) đáng tin cậy liên quan thế nào đến việc "tính nhất quán nằm ở siêu lý thuyết"?
- Ghi lại một câu hỏi chính xác mà bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước** — [Gödel's Incompleteness Theorem - Numberphile](https://www.youtube.com/watch?v=O4ndIDcDSGc) — Numberphile, tiếng Anh. Video định hướng cho mục tiêu của bài: phát biểu định lý bất toàn thứ nhất và thứ hai ở dạng không hình thức nhưng chính xác.
- [The paradox at the heart of mathematics: Gödel's Incompleteness Theorem - Marcus du Sautoy](https://www.youtube.com/watch?v=I4pQbo5MQOs) — TED-Ed, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ.
- [Math's Fundamental Flaw](https://www.youtube.com/watch?v=HeQX2HjkcNo) — Veritasium, tiếng Anh. Góc nhìn bổ sung sau hai video đầu.
