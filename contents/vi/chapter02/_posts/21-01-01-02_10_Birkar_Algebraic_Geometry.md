---
layout: post
title: "Công trình của Birkar trong Hình học Đại số (Huy chương Fields 2018)"
chapter: '02'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử tưởng tượng một khu rừng vô tận chứa mọi hình dạng có thể tạo ra từ nghiệm của các phương trình đa thức nhiều biến: từ đường tròn, mặt cầu quen thuộc đến những đa tạp 3 chiều, 10 chiều hay 100 chiều kỳ lạ và xoắn xuýt. Làm sao các nhà toán học có thể đưa ra một **bảng tuần hoàn** — giống như bảng tuần hoàn các nguyên tố hóa học — để sắp xếp trật tự cho khu rừng vô tận ấy?

Ở chiều 1 (đường cong) và chiều 2 (mặt đại số), các nhà toán học thế kỷ XIX–XX đã vẽ xong bản đồ phân loại. Nhưng khi bước sang chiều 3 trở lên, mọi thứ bỗng trở nên hỗn loạn bởi những kỳ dị phức tạp và các phép "cắt dán" nhiều chiều. **Chương trình mô hình tối thiểu** (*Minimal Model Program*, viết tắt là MMP) ra đời để giải quyết đúng thách thức đó: rút gọn mọi đa tạp đại số về ba "viên gạch cơ bản" — giống như phân tích số tự nhiên ra thừa số nguyên tố — trong đó nhóm "cong dương" được gọi là **đa tạp Fano**.

Nhưng một nỗi lo lớn kéo dài hàng chục năm: nhỡ đâu ở một số chiều cố định, số kiểu đa tạp Fano lại nhiều vô hạn và ngày càng "hoang dã" đến mức không thể lập danh mục nổi? Năm 2016, **Caucher Birkar** — một nhà toán học gốc Kurd lớn lên giữa chiến tranh và đến Anh tị nạn — đã chứng minh **tính bị chặn của các đa tạp Fano**, khép lại một câu hỏi trung tâm (giả thuyết BAB) và mang về **Huy chương Fields 2018**.

Mục tiêu không phải là biến bạn thành chuyên gia về flip. Mục tiêu là hiểu **MMP hỏi gì**, **đa tạp Fano là gì** ở mức sơ lược, **tính bị chặn nghĩa là kiểm soát một họ đa tạp như thế nào**, và **vì sao** cộng đồng xem các định lý của Birkar (cùng một chuỗi dài các công trình hợp tác trước đó) như việc khép lại một chương lớn của hình học đại số chiều cao.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu mục tiêu của MMP trong một đoạn: đưa một đa tạp, bằng các phép biến đổi song hữu tỉ, về một mô hình "đơn giản" (mô hình tối thiểu hoặc không gian thớ Mori).
- Giải thích sơ lược thế nào là đa tạp **Fano**: lớp chính tắc âm, tức lớp phản chính tắc là ample; đó là các đa tạp "dương" theo nghĩa song hữu tỉ.
- Phân biệt hai loại kết quả: **sự tồn tại của flip** (một bước trong MMP) và **tính bị chặn của đa tạp Fano** (kiểm soát toàn cục cả họ).
- Nhìn hình học song hữu tỉ như **kiến trúc tổng thể** của hình học đại số chiều cao, chứ không chỉ là một danh sách ví dụ.
- Ghi nhận công lao cẩn thận: Huy chương Fields 2018 nằm trong mạng lưới công trình BCHM, Hacon–McKernan, Shokurov, Kawamata, Kollár–Mori…; đóng góp nổi bật riêng của Birkar là tính bị chặn của đa tạp Fano và một số trường hợp của MMP.
- Tránh nhầm "song hữu tỉ = đẳng cấu" và "mọi đa tạp đều là Fano".

**Kiến thức cần có.** Đa tạp đại số, đa tạp xạ ảnh ở mức trực giác; ước (divisor) và lớp chính tắc $$K_X$$ như một kiểu "độ cong đại số"; phân biệt đẳng cấu với các quan hệ thô hơn.

**Liên hệ với khóa học.** So sánh với phân loại mặt (Enriques–Kodaira), nơi trường hợp chiều 2 về cơ bản đã xong; MMP là nỗ lực đưa phân loại lên chiều cao hơn. Có thể đọc cùng [Scholze / perfectoid]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), nhưng chỉ như *một* mặt khác của hình học đại số hiện đại (hình học số học, p-adic), không đồng nhất với hình học song hữu tỉ phức.

---

## Bản đồ kiến thức nền: Hình học đại số song hữu tỉ là gì và nghiên cứu những gì?

Nếu cụm từ "hình học đại số song hữu tỉ" nghe quá trừu tượng, hãy hình dung nó qua hai ví dụ quen thuộc từ hình học giải tích:

- **Đa tạp đại số là gì?** Là tập nghiệm của một hệ phương trình đa thức (ví dụ đường tròn $$x^2 + y^2 = 1$$ hay mặt bậc ba $$x^3 + y^3 + z^3 = 1$$), thường được đặt trong **không gian xạ ảnh** $$\mathbb{P}^n$$ (nơi ta thêm các "điểm ở vô cực" để hai đường song song cũng cắt nhau và mọi hình trở nên khép kín).
- **Tương đương song hữu tỉ (Birational Equivalence) là gì?** Trong hình học thông thường, hai hình giống nhau khi có phép biến đổi tương ứng 1–1 tại *mọi* điểm (đẳng cấu). Nhưng trong hình học đại số, yêu cầu đó quá chặt! Hãy nhìn đường tròn $$x^2 + y^2 = 1$$ và đường thẳng trục số $$t$$: phép chiếu lập thể $$t \mapsto \left(\frac{1-t^2}{1+t^2}, \frac{2t}{1+t^2}\right)$$ thiết lập một tương ứng 1–1 bằng hàm hữu tỉ giữa **toàn bộ** đường thẳng và **gần như toàn bộ** đường tròn (chỉ trừ đúng 1 điểm $$(-1, 0)$$)! Nói cách khác, đường tròn và đường thẳng **tương đương song hữu tỉ** — chúng có chung "phần lõi" và chỉ khác nhau trên một tập nhỏ không đáng kể. Một thao tác cơ bản khác là **phép nổ** (*blow-up*): thay một điểm duy nhất trên mặt phẳng bằng một đường tròn các hướng đi qua điểm đó — giống như xoay cầu thang xoắn quanh một trục để tách rời các nhánh đường cong cắt nhau tại gốc.
- **Ba "viên gạch" theo dấu của độ cong đại số $$K_X$$:** Giống như các mặt 2 chiều chia thành 3 kiểu độ cong (mặt cầu cong dương, mặt xuyến phẳng, mặt nhiều lỗ cong âm), trong hình học đại số chiều cao, **lớp chính tắc $$K_X$$** đóng vai trò là thước đo ngược dấu với độ cong:
  1. **Đa tạp Fano** ($$-K_X > 0$$): tương ứng với "độ cong dương" (như mặt cầu, không gian xạ ảnh $$\mathbb{P}^n$$).
  2. **Đa tạp Calabi–Yau** ($$K_X \equiv 0$$): tương ứng với "độ cong bằng 0" (như đường cong elliptic / mặt xuyến).
  3. **Đa tạp kiểu tổng quát** ($$K_X > 0$$): tương ứng với "độ cong âm" (như mặt hyperbolic nhiều lỗ).

  Toàn bộ **Chương trình mô hình tối thiểu (MMP)** chính là nỗ lực chứng minh rằng mọi đa tạp đại số bất kỳ đều có thể cắt tỉa bằng các phép biến đổi song hữu tỉ để xây nên từ đúng ba viên gạch cơ bản này!

---

## 1. Phân loại song hữu tỉ: bỏ qua gì, giữ lại gì?

Hai đa tạp xạ ảnh (hoặc tựa xạ ảnh) $$X$$ và $$Y$$ được gọi là **tương đương song hữu tỉ** nếu tồn tại các tập mở trù mật $$U\subset X$$, $$V\subset Y$$ và một đẳng cấu $$U\simeq V$$. Nói nôm na, chúng trùng nhau "ở hầu hết mọi nơi", chỉ khác nhau trên một tập đóng nhỏ hơn, giống như hai cách compact hóa khác nhau của cùng một phần lõi affine, hoặc hai mô hình nhận được bằng các phép nổ (*blow-up*) khác nhau.

**Phép tương đương song hữu tỉ bỏ qua** chi tiết về kỳ dị nhỏ và cách chọn compact hóa.  
**Nó giữ lại** nhiều bất biến sâu: trường hàm hữu tỉ, chiều Kodaira, và (sau khi chạy MMP) các mô hình chuẩn được sắp xếp theo dấu của $$K_X$$.

So với **đẳng cấu** (toàn cục, tại mọi điểm), tương đương song hữu tỉ thô hơn. So với "có cùng trường hàm", nó chính là cách diễn đạt hình học của quan hệ đó. Phân loại song hữu tỉ là một chiến lược: thay vì liệt kê mọi đa tạp sai khác đẳng cấu (quá nhiều), ta gom chúng thành các lớp song hữu tỉ và tìm một **đại diện đẹp** trong mỗi lớp.

**Ví dụ ở chiều thấp (sơ lược).**

- Đường cong xạ ảnh trơn: mỗi lớp song hữu tỉ chỉ có đúng một đại diện trơn duy nhất, được phân loại bằng giống $$g$$ ($$g=0$$ là $$\mathbb{P}^1$$ kiểu Fano; $$g=1$$ là đường cong elliptic; $$g\ge 2$$ là kiểu tổng quát).  
- Mặt (chiều 2): phân loại Enriques–Kodaira thu gọn mọi mặt bằng cách liên tục **co** các đường cong ngoại lệ (đường cong $$(-1)$$, giống như đảo ngược phép nổ) cho tới khi không còn gì để co nữa.  
- Chiều $$\ge 3$$: kỳ dị, flop/flip, và việc "chỉ co các đường cong" không còn đủ, buộc người ta xây dựng một cơ chế trừu tượng hơn, đó là MMP.

---

## 2. Chương trình mô hình tối thiểu (MMP) là gì?

Xuất phát từ một đa tạp xạ ảnh $$X$$ (thường giả sử $$\mathbb{Q}$$-giai thừa và có kỳ dị klt sau khi đã "dọn dẹp"), MMP tìm cách cải thiện $$X$$ bằng một chuỗi phép biến đổi song hữu tỉ, hướng tới một trong hai đích:

1. **Mô hình tối thiểu.** Một đa tạp $$X_{\min}$$ tương đương song hữu tỉ với $$X$$ sao cho lớp chính tắc $$K_{X_{\min}}$$ là **nef** (có giao không âm với mọi đường cong). Khi đó không còn hướng nào để "co" theo tính âm của $$K$$.
2. **Không gian thớ Mori.** Nếu không thể làm $$K$$ thành không âm ở mọi hướng, quá trình dừng ở một phân thớ $$X\to Z$$ mà mỗi thớ là một **đa tạp Fano** (lớp chính tắc âm trên thớ tổng quát). Khi đó đa tạp được hiểu như một họ các đa tạp Fano xếp trên một cơ sở $$Z$$ có chiều thấp hơn.

### 2.1. Hai thao tác: phép co và flip

- **Phép co ước / phép co cực trị.** Khi có một tia cực trị mà trên đó $$K$$ âm, ta co tập tương ứng (đường cong, ước…) xuống một điểm hoặc một tập nhỏ hơn để giảm "độ phức tạp".  
- **Flip.** Ở chiều $$\ge 3$$, đôi khi tập bị co có chiều quá nhỏ (đối chiều $$\ge 2$$) khiến đa tạp sau khi co mang kỳ dị quá xấu, không thể tính được giao với $$K$$ nữa! Khi đó cần một **flip**: nhổ bỏ một đường cong (hoặc tập nhỏ) có $$K < 0$$ và thay vào đúng chỗ đó một đường cong mới có $$K > 0$$, vẫn giữ tương đương song hữu tỉ nhưng làm đẹp lại kỳ dị. Sự tồn tại của flip từng là thách thức trung tâm trong nhiều thập niên.

Trực giác thô: phép co giống như "bóp" bớt phần thừa; flip giống như một "ca phẫu thuật" định hướng lại phần kỳ dị để $$K$$ dễ kiểm soát hơn. Kết quả không đẳng cấu với ban đầu, nhưng vẫn thuộc cùng một lớp song hữu tỉ.

### 2.2. Vành chính tắc và kỳ dị

MMP hiện đại làm việc với các **kỳ dị được phép** (klt, lc…) và với **vành chính tắc**

$$
R(X,K_X)=\bigoplus_{m\ge 0} H^0(X,mK_X).
$$

Tính hữu hạn sinh của vành chính tắc (các định lý lớn của BCHM và những người đi trước) là xương sống của lý thuyết: nó bảo đảm các bước "lấy $$\operatorname{Proj}$$ của vành" có ý nghĩa hình học. Không cần thuộc định nghĩa klt để hiểu ý chính: *MMP không thể mãi chỉ làm việc với đa tạp trơn; cho phép những kỳ dị nhẹ được kiểm soát là cái giá bắt buộc để cỗ máy phân loại hoạt động ở chiều cao*.

---

## 3. Đa tạp Fano: "dương" theo nghĩa song hữu tỉ

Một đa tạp xạ ảnh $$X$$ (với kỳ dị thích hợp) được gọi là **Fano** khi lớp phản chính tắc $$-K_X$$ là **ample** (hoặc, trong một số biến thể, big/nef tùy ngữ cảnh kỹ thuật). Nói gọn:

> Đa tạp Fano là đa tạp có "độ cong dương" theo thước đo chính tắc, tức là $$K_X$$ âm.

Ví dụ quen thuộc: không gian xạ ảnh $$\mathbb{P}^n$$; mọi siêu mặt trơn bậc $$d \le n$$ trong $$\mathbb{P}^n$$ (ví dụ mặt bậc hai hoặc mặt bậc ba trong $$\mathbb{P}^3$$); các thớ Fano trong không gian thớ Mori.

**Vì sao đa tạp Fano giữ vai trò trung tâm.** Trong phân loại, đa tạp Fano xuất hiện như:

- thớ của các không gian thớ Mori;
- "nguồn gốc" của nhiều hiện tượng song hữu tỉ (câu hỏi về tính hữu tỉ, tính K-ổn định, không gian moduli…);
- một lớp được kỳ vọng có **tính bị chặn**: khi cố định số chiều (và mức độ kỳ dị cho phép), không có vô hạn họ độc lập "hoang dã".

Câu hỏi về tính bị chặn (giả thuyết **Borisov–Alexeev–Borisov**, viết tắt BAB): *Các đa tạp Fano chiều $$n$$ có tạo thành một họ bị chặn không?* "Bị chặn" ở đây có nghĩa kỹ thuật: chúng đều xuất hiện như thớ của một họ phẳng trên một lược đồ kiểu hữu hạn — nói một cách gần gũi, chỉ cần **hữu hạn** tham số và hữu hạn gia đình đa thức là mô tả được *tất cả* các đa tạp Fano chiều $$n$$, chứ không có một dãy đa tạp có bậc phương trình ngày càng phình to ra vô tận!

---

## 4. Đột phá của Birkar: tính bị chặn của đa tạp Fano và MMP chiều cao

**Caucher Birkar** (trong dòng công trình chung với Cascini, Hacon, McKernan, cùng hai bài báo đột phá riêng năm 2016) đã đóng góp vào:

1. **Sự tồn tại của flip và MMP** trong những trường hợp lớn, cùng với nhóm **BCHM** (Birkar–Cascini–Hacon–McKernan, 2010), chứng minh tính hữu hạn sinh của vành chính tắc và MMP cho đa tạp kiểu tổng quát.
2. **Tính bị chặn của đa tạp Fano** (chứng minh trọn vẹn giả thuyết BAB): khi cố định số chiều $$n$$ và ngưỡng kỳ dị $$\varepsilon > 0$$ ($$\varepsilon$$-lc), họ tất cả các đa tạp Fano chiều $$n$$ tạo thành một **họ bị chặn**.

<div class="textbook-theorem" markdown="1">
**Định lý (sơ lược, Birkar).** Họ các đa tạp Fano chiều $$n$$ (với điều kiện kỳ dị $$\varepsilon$$-lc và các giả thiết chuẩn trong tài liệu) là **bị chặn**: chúng không "tản mát vô hạn" theo nghĩa moduli thô.
</div>

Hệ quả về mặt tư duy: phân loại ở chiều cao không còn là một danh sách lộn xộn. Sau khi MMP đưa về đa tạp Fano hoặc mô hình tối thiểu, **phía Fano** được kiểm soát toàn cục. Đó là lý do giải Fields nhấn mạnh tính bị chặn: đây không chỉ là một bổ đề kỹ thuật, mà là một **định lý cấu trúc**, làm thay đổi cách ta nghĩ về câu hỏi "có bao nhiêu đa tạp Fano".

### 4.1. Ghi nhận công lao cẩn thận

| Mốc / nhóm | Vai trò (tóm tắt) |
|------------|---------------------|
| Mori, Kawamata, Shokurov, Kollár… | Nền tảng của MMP, định lý nón, lý thuyết kỳ dị |
| Hacon–McKernan và cộng sự | Bước đột phá ở chiều cao, sự tồn tại của flip trong nhiều trường hợp |
| BCHM | Tính hữu hạn sinh / MMP cho đa tạp kiểu tổng quát và khung tổng quát hơn |
| Birkar | Tính bị chặn của đa tạp Fano (giả thuyết BAB); các định lý bổ sung về MMP; Fields 2018 |

Tránh viết "một mình Birkar hoàn tất MMP". Cũng tránh viết "tính bị chặn của đa tạp Fano là toàn bộ MMP".

---

## 5. Vì sao quan trọng, kể cả ngoài hình học song hữu tỉ?

**Trong hình học đại số.** Tính bị chặn và MMP tạo ra một **kiến trúc**: mọi đa tạp "đủ tốt" đều có thể đưa về một đại diện chuẩn, và các họ đa tạp Fano không hoang dã. Nhiều hướng hiện đại (tính K-ổn định, moduli của đa tạp Fano, lý thuyết kỳ dị, tính cứng song hữu tỉ) dựa vào việc biết đa tạp Fano bị chặn, hoặc biết MMP chạy được.

**Trong bức tranh chung của Chương 2.** Huy chương Fields không chỉ dành cho "một bất đẳng thức" hay "một phương trình đạo hàm riêng". Birkar là ví dụ cho kiểu **toán học mang tính kiến trúc**: những định lý sắp xếp không gian các đối tượng (các đa tạp) thành những ngăn được kiểm soát. So với Maynard (cấu trúc của số nguyên tố) hay Viazovska (bài toán xếp tối ưu), ở đây là cấu trúc **của chính các không gian hình học**.

**Giới hạn, nói thẳng.**

- MMP và tính bị chặn phụ thuộc vào giả thiết về kỳ dị và về đặc số (các định lý kinh điển được trích ở đây thường ở đặc số 0).  
- Câu hỏi về tính hữu tỉ của đa tạp Fano, moduli chi tiết, và trường hợp đặc số dương vẫn là những hướng nghiên cứu sôi động.  
- "Đã phân loại xong" không có nghĩa là mọi đa tạp đều có một danh sách tường minh như với đường cong.

---

## 6. So sánh nhanh với phân loại mặt

| | Mặt (Enriques–Kodaira) | Chiều cao (MMP + Birkar) |
|--|------------------------|---------------------------|
| Bất biến chính | Chiều Kodaira, phân thớ | $$K$$ nef hay không gian thớ Mori; thớ Fano |
| Thao tác | Phép nổ, phân thớ cổ điển | Phép co, flip, tính hữu hạn sinh |
| Kiểm soát đa tạp Fano / thớ dương | Khá tường minh ở chiều 2 | Tính bị chặn của đa tạp Fano ở chiều cao |
| Hiện trạng | Cổ điển, khá hoàn chỉnh | Chương trình dài; nhiều phần lớn đã khép lại |

Bài học khi lên chiều cao: *cùng một triết lý phân loại theo tính dương của $$K$$*, nhưng công cụ và kỳ dị phức tạp hơn rất nhiều.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Mọi đa tạp đều là Fano." | Sai | Fano là một điều kiện về tính dương của $$-K$$; nhiều đa tạp có $$K$$ nef, hoặc dương theo những nghĩa khác. |
| "Song hữu tỉ = đẳng cấu." | Sai | Tương đương song hữu tỉ yếu hơn; có thể xuất hiện kỳ dị và tập ngoại lệ. |
| "Flip chỉ là một phép nổ." | Sai | Flip thay một tập theo tia cực trị; không phải một phép nổ cổ điển đơn giản. |
| "Fields 2018 chỉ nhờ một bài báo về đa tạp Fano." | Sai | Nó dựa trên nền MMP lâu dài; tính bị chặn là điểm nhấn trong nhiều công trình. |
| "MMP chạy trên mọi đa tạp trơn, không cần đến kỳ dị." | Sai | Kỳ dị klt/lc và tính Q-giai thừa là một phần của khung lý thuyết hiện đại. |
| "Bị chặn = chỉ có hữu hạn đa tạp Fano sai khác đẳng cấu." | Gần đúng nhưng thô | Nghĩa kỹ thuật là họ bị chặn trong một cách tham số hóa (moduli); tinh tế hơn "hữu hạn điểm". |

---

## Bài tập

1. Tương đương song hữu tỉ **bỏ qua** và **giữ lại** điều gì? Viết hai câu, rồi nêu sơ lược một ví dụ phép nổ để minh họa sự khác biệt với đẳng cấu.
2. Theo trực giác, vì sao flip khó hơn phép co? Không cần chứng minh, chỉ cần lập luận: "khi phép co không cho một cấu xạ đẹp thì cần gì?".
3. Định nghĩa sơ lược của đa tạp Fano là gì? Viết bằng ngôn ngữ "$$-K_X$$ ample", rồi bằng một câu không có ký hiệu.
4. Vì sao **tính bị chặn** của một lớp đa tạp quan trọng cho phân loại? Liên hệ với ý "không có dãy ngày càng hoang dã".
5. Đọc lướt một bài tổng quan ICM hoặc một bài giới thiệu về MMP; liệt kê **ba mốc** trước Birkar 2018 (tên và một dòng mô tả).
6. **So sánh.** Nêu một điểm giống và một điểm khác giữa "mô hình tối thiểu" và "không gian thớ Mori".
7. **Thảo luận (không quá 200 từ).** Giải thích cho một bạn học giải tích câu: "MMP là thuật toán rút gọn hình học theo dấu của $$K$$". Nêu giới hạn của cách so sánh với thuật toán.

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Birkar_Algebraic_Geometry/`.

**Thứ tự xem gợi ý**

1. Video của Quanta: [YouTube](https://www.youtube.com/watch?v=1EpMF16ShY0) · [bài viết](https://www.quantamagazine.org/caucher-birkar-who-fled-war-and-found-asylum-wins-fields-medal-20180801/).  
2. Phỏng vấn tại Cambridge: [YouTube](https://www.youtube.com/watch?v=CwMvjWL-gos).

**Nhắc lại:** tính bị chặn của đa tạp Fano và MMP không có nghĩa là đã phân loại hết mọi đa tạp.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Birkar_Algebraic_Geometry/transcripts/` · trạng thái: `research/video-research/Birkar_Algebraic_Geometry/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Birkar_Algebraic_Geometry_1EpMF16ShY0_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Birkar_Algebraic_Geometry/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=1EpMF16ShY0  
2. https://www.youtube.com/watch?v=CwMvjWL-gos  
3. https://www.simonsfoundation.org/2018/08/01/field-medals-video-caucher-birkar/  
4. https://arxiv.org/search/?query=Birkar+Fano+boundedness&searchtype=all  
5. https://www.quantamagazine.org/caucher-birkar-who-fled-war-and-found-asylum-wins-fields-medal-20180801/  
6. https://www.maths.cam.ac.uk/features/professor-caucher-birkar-wins-2018-fields-medal  
7. https://en.wikipedia.org/wiki/Caucher_Birkar  
8. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018  
9. https://arxiv.org/search/math?query=Birkar+boundedness+Fano&searchtype=all&source=header  
10. https://en.wikipedia.org/wiki/Minimal_model_program  
11. https://en.wikipedia.org/wiki/Fano_variety  
12. https://arxiv.org/search/?query=Birkar+Fano&searchtype=all  

### Bộ tư liệu nghiên cứu

13. Bộ tư liệu của khóa học: `research/video-research/Birkar_Algebraic_Geometry/`.

1. IMU, Huy chương Fields 2018 — Caucher Birkar.
2. C. Birkar — các bài báo về tính bị chặn của đa tạp Fano.
3. Birkar–Cascini–Hacon–McKernan (BCHM) — tính hữu hạn sinh / MMP.
4. J. Kollár, S. Mori — *Birational Geometry of Algebraic Varieties* (tài liệu nền).
5. Các bài tổng quan, báo cáo ICM về MMP và tính bị chặn của đa tạp Fano (nên chọn bản viết dễ đọc).
6. Trong khóa học: [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/), [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/) (một mặt khác của hình học đại số hiện đại).

---

## Hướng đi tiếp

- So sánh phân loại mặt (Enriques–Kodaira) với MMP ở chiều cao: cùng triết lý về tính dương, khác công cụ.
- Tìm hiểu **các loại kỳ dị trong MMP** (klt, lc) và **vành chính tắc** trước khi đọc bài báo nghiên cứu.
- Nếu quan tâm đến moduli của đa tạp Fano hay tính K-ổn định, đó là bước tiếp theo sau tính bị chặn; đừng nhầm với chính định lý của Birkar.
- Đọc một bài giới thiệu ngắn về tia cực trị và định lý nón để "thấy" tia cực trị trước khi học flip.

## Video tham khảo

- **Xem trước:** [Caucher Birkar: An Innovator Who Brings Order to an Infinitude of Equations](https://www.youtube.com/watch?v=1EpMF16ShY0) — Quanta Magazine, tiếng Anh. Giới thiệu Birkar và ý tưởng sắp xếp trật tự cho vô số phương trình; nên xem trước khi đọc bài.
- [2018 Fields Medal Recipient Caucher Birkar - Professor, University of Cambridge](https://www.youtube.com/watch?v=CwMvjWL-gos) — WebsEdgeScience, tiếng Anh. Phỏng vấn ngắn với Birkar về công trình của ông; nên xem sau khi đã nắm ý chính của bài.
