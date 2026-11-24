---
layout: post
title: "Turing, Tính được và Bất khả quyết định"
chapter: '09'
order: 3
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

Năm 1928, nhà toán học vĩ đại David Hilbert đứng trước Đại hội Toán học Quốc tế với một giấc mơ lạc quan: liệu có tồn tại một **thủ tục máy móc** — thứ mà bất kỳ ai làm theo từng bước mù quáng cũng thực hiện được — để nhập vào một phát biểu toán học bất kỳ rồi nhận ra câu trả lời dứt khoát *Đúng* hay *Sai* không? Người Đức gọi đó là **Entscheidungsproblem** (Bài toán Quyết định). Tám năm sau, năm **1936**, khi chưa có chiếc máy tính điện tử hiện đại nào ra đời, chàng trai 23 tuổi **Alan Turing** đã khép lại giấc mơ ấy bằng bài báo kinh điển *On Computable Numbers, with an Application to the Entscheidungsproblem*.

Turing không ngồi chế tạo một chiếc máy tính xách tay. Ông làm một việc toán học táo bạo hơn nhiều: lần đầu tiên **định nghĩa chặt chẽ** thế nào là một "thủ tục tính toán hữu hạn bước" thông qua mô hình chiếc máy dùng băng giấy, xây dựng **máy phổ quát** (hạt nhân của khái niệm phần mềm ngày nay), rồi chứng minh bằng một cú lật đường chéo cực kỳ sắc bén rằng **Bài toán Dừng là không thể giải quyết được bằng bất kỳ thuật toán nào**. Cùng thời điểm đó, Alonzo Church (với phép tính lambda), Kleene và Post cũng đi tới đúng cùng một lớp hàm — hội tụ thành **Luận đề Church–Turing**. Bài học này đi theo dấu chân ý tưởng năm 1936 ấy, nối sang đường chéo Cantor, bất toàn Gödel và ranh giới với P vs NP. Liên kết: [Giải Turing là gì?]({{ site.baseurl }}/contents/vi/chapter09/09_02_What_Is_Turing_Award/), [Định lý bất toàn Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/), [Đường chéo Cantor]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô tả máy Turing ở mức thành phần (băng, đầu đọc–ghi, trạng thái hữu hạn, bảng chuyển) và giải thích vì sao mô hình cố ý thô.  
- Phát biểu ý **máy phổ quát** và liên hệ với “phần mềm chạy trên phần cứng.”  
- Phát biểu **bài toán dừng** và phác thảo ý tưởng chứng minh bất khả quyết định bằng đường chéo.  
- Phân biệt **không tính được / không quyết định được** với **khó tính (NP-khó)** và với **bất toàn logic**.  
- Nêu luận đề Church–Turing như tuyên bố mô hình, không như định lý trong ZFC theo nghĩa thông thường.  
- Tránh nhầm: “máy Turing chậm nên vô dụng,” “mọi thứ toán học đều quyết định được,” “bất khả quyết định = chưa tìm ra thuật toán.”

**Tiên quyết.** Quen ý thuật toán như quy trình hữu hạn bước; số nguyên và xâu bit; đọc được ký hiệu tập hợp cơ bản. Không cần đã học ôtômat hình thức; ta ở mức ý tưởng. Toán rời rạc ở mức quan hệ và hàm là đủ.

---

## Bản đồ kiến thức nền: Lý thuyết tính toán được (Computability Theory) là gì và nghiên cứu những gì?

Khi lập trình, bạn có bao giờ tự hỏi: *Tại sao không ai viết nổi một công cụ kiểm tra mã nguồn (linter) có thể đảm bảo 100% rằng bất kỳ chương trình Python nào đưa vào sẽ không bao giờ bị treo vào vòng lặp vô hạn?* Câu trả lời không phải vì lập trình viên chưa đủ giỏi hay máy tính chưa đủ nhanh — mà là một **định luật bất khả thi** của **Lý thuyết tính toán được (Computability Theory / Recursion Theory)**.

Ngành toán học này nghiên cứu một câu hỏi cực kỳ trong sáng: **nếu cho bạn thời gian và bộ nhớ lớn tùy ý (miễn là hữu hạn), bài toán nào có thuật toán giải và bài toán nào tuyệt đối không có?**
- Để trả lời *"Có"*, bạn chỉ cần viết ra một chương trình.
- Để trả lời *"Không"*, bạn bắt buộc phải có một **mô hình toán học** định nghĩa thế nào là "mọi chương trình có thể có" — và **máy Turing** chính là mô hình chuẩn mực đó.

Hãy hình dung một ví dụ siêu nhỏ về máy Turing để thấy nó giản dị đến mức nào: muốn kiểm tra xem một chuỗi nhị phân (như `10110`) có chứa số lẻ bit `1` hay không, máy chỉ cần **2 trạng thái** (`Chẵn` và `Lẻ`). Đầu đọc trượt từ trái sang phải từng ô một: cứ gặp `1` thì đổi trạng thái `Chẵn ↔ Lẻ`, gặp `0` thì giữ nguyên; đến ô trống cuối chuỗi, nếu đang ở trạng thái `Lẻ` thì báo *Chấp nhận*, ngược lại báo *Từ chối*. Kỳ diệu ở chỗ, chỉ cần thêm nhiều trạng thái hơn và cho phép đầu đọc quay lại ghi đè lên băng, cỗ máy thô sơ ấy có thể mô phỏng **mọi siêu máy tính trên hành tinh**!

---

## 1. Entscheidungsproblem và nhu cầu một mô hình

Hilbert và các đồng nghiệp hỏi, đại khái, liệu có **thủ tục tổng quát** quyết định tính đúng/chứng minh được của mọi công thức trong một hệ logic đủ mạnh không. Để trả lời “không,” trước hết phải định nghĩa “thủ tục” đủ chặt: nếu “thủ tục” mơ hồ, câu trả lời phủ định cũng mơ hồ.

Turing chọn hình ảnh máy với:

- **băng** chia ô, mỗi ô chứa một ký hiệu từ bảng chữ cái hữu hạn (có thể coi là $$0,1$$ và khoảng trống);  
- **đầu** đọc/ghi một ô tại một thời điểm, có thể dịch trái/phải;  
- **trạng thái hữu hạn** kiểm soát hành vi;  
- **bảng chuyển** hữu hạn: từ (trạng thái, ký hiệu đang đọc) sang (ký hiệu viết, hướng dịch, trạng thái mới).

Máy bắt đầu trên input hữu hạn, chạy theo bảng chuyển. Nó có thể **dừng** với output, hoặc **chạy mãi**. Một ngôn ngữ $$L\subseteq\{0,1\}^*$$ **quyết định được** nếu có máy luôn dừng và chấp nhận đúng các xâu thuộc $$L$$. Một hàm **tính được** nếu có máy, trên mọi input hợp lệ, dừng và in giá trị đúng.

### Ví dụ cầm tay chỉ việc 1: Tự chạy một Máy Turing cộng 1 vào số nhị phân `1011` ($$11 \to 12$$)

Ta thiết kế một máy Turing chỉ có **3 trạng thái** (`TìmCuối`, `CộngNhớ`, `Dừng`) để cộng 1 vào bất kỳ số nhị phân nào:
- Ở trạng thái `TìmCuối`: gặp `0` hoặc `1` thì giữ nguyên, dịch **Phải**; gặp ô trống `_` thì dịch **Trái** và đổi sang `CộngNhớ`.
- Ở trạng thái `CộngNhớ`: gặp `1` thì ghi `0` (nhớ 1), dịch **Trái**; gặp `0` hoặc `_` thì ghi `1` (hết nhớ) và chuyển sang `Dừng`.

Hãy theo dõi từng nhịp đồng hồ trên dải băng chứa `1011_` (đầu đọc gạch chân):
1. `TìmCuối` trượt qua hết 4 bit đến ô trống `_`, lùi về bit cuối: `101[1]` (trạng thái `CộngNhớ`).
2. Đọc `1` → ghi `0`, lùi trái: `10[1]0` (vẫn `CộngNhớ`).
3. Đọc `1` → ghi `0`, lùi trái: `1[0]00` (vẫn `CộngNhớ`).
4. Đọc `0` → ghi `1`, dừng: `1100` ($$12_{10}$$) — **chính xác 100%!**

Mô hình cố ý nghèo nàn về kỹ thuật — không cache, không GPU — nhưng giàu về nguyên lý: mọi thuật toán viết bằng Python hay C++ đều mô phỏng được bằng máy Turing. Đó là điểm mạnh toán học: tính **không quyết định được** là giới hạn bản chất, không phụ thuộc ngôn ngữ lập trình.

---

## 2. Máy phổ quát và ý tưởng phần mềm

Turing chỉ ra tồn tại **máy phổ quát** $$U$$: khi được cung cấp mô tả mã hóa $$\langle M\rangle$$ của một máy $$M$$ cùng input $$x$$, $$U$$ mô phỏng hành vi của $$M$$ trên $$x$$. Nói không hình thức:

$$
U\big(\langle M\rangle, x\big) \;\text{mô phỏng}\; M(x).
$$

Đây là hạt nhân khái niệm của **chương trình như dữ liệu**. Trước Turing, muốn giải một bài toán mới, người ta thường phải lắp ráp hoặc đấu dây lại một cỗ máy mới (giống máy cộng cơ khí chỉ biết cộng). Máy phổ quát đảo ngược tư duy đó: **phần cứng cố định; phần mềm chỉ là một chuỗi bit mô tả bảng chuyển; máy phổ quát đọc chuỗi bit đó và biến thân thành bất kỳ cỗ máy nào**. Lịch sử kỹ thuật sau này—kiến trúc von Neumann, hệ điều hành, trình thông dịch Python, máy ảo, container—đều là hiện thực hóa kỹ nghệ của ý tưởng đã có trong bài báo năm 1936.

Hệ quả triết học–toán: lớp hàm tính được **không** phụ thuộc việc ta “mua thêm opcode.” Thêm cú pháp ngôn ngữ lập trình không vượt ra ngoài lớp đệ quy (recursive functions) nếu vẫn trong khuôn khổ thuật toán chuẩn. Muốn vượt, phải đổi mô hình theo hướng khác (oracle, không tất định với tài nguyên, lượng tử với chi phí khác, v.v.)—và ngay cả khi đó, câu chuyện **bất khả quyết định** vẫn còn nhiều biến thể.

---

## 3. Bài toán dừng

**Bài toán dừng (halting problem).** Cho mô tả máy $$\langle M\rangle$$ và input $$x$$, hỏi: $$M$$ có dừng trên $$x$$ không?

<div class="textbook-theorem" markdown="1">
**Định lý (Turing).** Không tồn tại máy Turing $$H$$ quyết định đúng bài toán dừng cho mọi cặp $$(\langle M\rangle, x)$$.
</div>

### Ví dụ cầm tay chỉ việc 2 & Khung giải thích: Mạch 4 bước chứng minh Bài toán Dừng bằng bảng đường chéo (nên đọc chậm)

Hãy tưởng tượng ta liệt kê tất cả các chương trình hợp lệ trên đời thành từng hàng $$M_1, M_2, M_3, \dots$$ và cho mỗi chương trình chạy thử với đầu vào là chính mã nguồn của các chương trình khác:

| Máy \ Đầu vào | $$\langle M_1 \rangle$$ | $$\langle M_2 \rangle$$ | $$\langle M_3 \rangle$$ | $$\langle M_4 \rangle$$ | $$\cdots$$ |
|---|:-:|:-:|:-:|:-:|:-:|
| $$M_1$$ | **Dừng** | Lặp | Dừng | Dừng | $$\cdots$$ |
| $$M_2$$ | Lặp | **Lặp** | Dừng | Lặp | $$\cdots$$ |
| $$M_3$$ | Dừng | Dừng | **Dừng** | Lặp | $$\cdots$$ |
| $$M_4$$ | Lặp | Dừng | Lặp | **Lặp** | $$\cdots$$ |
| **Máy nghịch đảo $$D$$** | **Lặp** | **Dừng** | **Lặp** | **Dừng** | $$\cdots$$ |

Dưới đây là mạch lập luận 4 bước khiến cỗ máy tiên tri $$H$$ không bao giờ có thể tồn tại:

1. **Giả sử phản chứng có tiên tri $$H$$:** giả sử tồn tại chương trình $$H(\langle M\rangle, x)$$ luôn dừng và in `1` nếu $$M(x)$$ dừng, in `0` nếu $$M(x)$$ lặp vô hạn (tức là $$H$$ điền được chính xác toàn bộ bảng trên).
2. **Dựng máy nghịch đảo $$D$$ lật ngược đường chéo:** nhận đầu vào là mã nguồn $$\langle M\rangle$$, máy $$D$$ gọi $$H(\langle M\rangle, \langle M\rangle)$$ để xem ô trên đường chéo chính, rồi làm **ngược lại hoàn toàn**: nếu $$H$$ báo `Dừng` thì $$D$$ cố tình chạy vòng lặp vô hạn; nếu $$H$$ báo `Lặp` thì $$D$$ lập tức `Dừng`!
3. **Đặt chính $$D$$ vào làm đầu vào cho $$D$$ (ô đường chéo $$D(\langle D\rangle)$$):** vì $$D$$ cũng là một chương trình hợp lệ, nó phải xuất hiện đâu đó ở một hàng trong bảng. Nhưng tại ô $$(D, \langle D\rangle)$$:
   - Nếu $$D(\langle D\rangle)$$ **dừng**, thì theo định nghĩa, $$H$$ phải báo `Dừng` → buộc $$D$$ phải **lặp vô hạn** (mâu thuẫn!).
   - Nếu $$D(\langle D\rangle)$$ **lặp vô hạn**, thì $$H$$ phải báo `Lặp` → buộc $$D$$ phải **dừng** (mâu thuẫn!).
4. **Kết luận:** mâu thuẫn chỉ có thể đến từ giả định ban đầu — chương trình tiên tri $$H$$ **tuyệt đối không tồn tại**.

**Kiểm tra nhanh.** Chú ý sự giống nhau kỳ diệu với **đường chéo Cantor** (chứng minh số thực không đếm được) và **định lý bất toàn Gödel** (câu tự tham chiếu "tôi không chứng minh được"): cả ba đều dùng chung một động tác lật ngược trên đường chéo để thoát khỏi mọi danh sách bao trùm!

---

### Video ngắn: Alan Turing (1936): Máy phổ quát & Bài toán Dừng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/turing-halting_vi.mp4"></video>
</div>

Video dài khoảng 2 phút 31 giây (có thuyết minh tiếng Việt giọng Algenib): mô hình máy Turing, máy phổ quát U, dựng máy nghịch đảo D(⟨M⟩) và mâu thuẫn tự tham chiếu D(⟨D⟩).

## 4. Họ hàng bất khả quyết định

Một khi bài toán dừng không quyết định được, hàng loạt bài toán khác **quy về** nó (reduction theo nghĩa tính được): nếu ta quyết định được bài $$A$$ thì ta quyết định được bài dừng—do đó $$A$$ cũng không quyết định được. (Định lý Rice thậm chí còn khái quát hóa mạnh mẽ: *mọi* tính chất không tầm thường về hành vi vào–ra của chương trình đều không quyết định được!)

Một số ví dụ cổ điển (nêu ở mức ý tưởng):

- **Bài toán trống (emptiness)** cho một số lớp máy/chương trình đủ mạnh: “chương trình có bao giờ chấp nhận input nào không?”  
- **Bài toán tương đương** chương trình: “hai chương trình có cùng hành vi trên mọi input không?” (đây là lý do không thể có trình tối ưu hóa mã nguồn hoàn hảo tuyệt đối!).  
- **Bài toán dừng với input rỗng.**  
- Trong logic: tính thỏa mãn của một số lớp công thức đủ biểu đạt (liên hệ Entscheidungsproblem).  
- Trong hình học rời rạc: **lát Wang** toàn phẳng—Berger chứng minh bất khả quyết định bằng cách nhúng mô phỏng tính toán vào quy tắc màu cạnh; xem hương vị ở [Lát gạch]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/).

Reduction ở tầng tính được khác reduction poly-time ở tầng NP-đầy đủ, nhưng **tinh thần** giống nhau: chuyển độ khó từ bài đã biết sang bài mới, bảo toàn câu trả lời có/không.

---

## 5. Số tính được và Church–Turing

**Số thực tính được** có thủ tục in chữ số/xấp xỉ theo yêu cầu (như $$\pi, e, \sqrt{2}$$). Chỉ đếm được nhiều chương trình (vì mỗi chương trình là một chuỗi ký tự hữu hạn), trong khi $$\mathbb{R}$$ không đếm được—hầu hết số thực trên trục số là **không tính được** ([vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/), [Cantor]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/)). Tồn tại cổ điển ≠ tồn tại **có thuật toán**.

**Luận đề Church–Turing:** “thuật toán” trực giác trùng máy Turing / lambda / đệ quy mu—tuyên bố mô hình đã kiểm chứng bằng tương đương nhiều hình thức, không phải định lý ZFC thông thường. Máy lượng tử **không** phá luận đề về lớp hàm tính được; chúng nhắm tăng tốc (BQP), không tính hàm không đệ quy. Xem [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/).

---

## 6. Ranh giới với độ phức tạp và với Gödel

Ba tầng hay bị trộn:

| Tầng | Câu hỏi điển hình | Ví dụ |
|------|-------------------|--------|
| **Logic / bất toàn** | Lý thuyết có chứng minh mọi chân lý không? | Gödel: hệ đủ mạnh nhất quán thì bất toàn |
| **Tính được** | Có thuật toán nào (không giới hạn thời gian) không? | Bài toán dừng: không |
| **Độ phức tạp** | Có thuật toán **hiệu quả** (poly-time, …) không? | P vs NP: mở |

Bài toán có thể **quyết định được** nhưng **không biết** có nằm trong P hay không; hoặc nằm ngoài P dưới giả thuyết chuẩn; hoặc quyết định được trong lý thuyết nhưng thời gian khổng lồ. Ngược lại, bất khả quyết định là chặn tuyệt đối trong mô hình: không phải “chờ máy nhanh hơn.”

Gödel và Turing họ hàng đường chéo nhưng **không đồng nhất**. Gödel nói về chứng minh trong hệ tiên đề; Turing nói về dừng của máy. Có cầu kỹ thuật sâu (số hóa cú pháp, biểu diễn quan hệ tính được), nhưng cần giữ tách bạch các khái niệm: “không chứng minh được” ≠ “không tính được” ≠ “NP-khó.”

---

## 7. Nhầm lẫn thường gặp

| Khẳng định | Chỉnh |
|------------|-------|
| “Máy Turing quá chậm nên chỉ là đồ chơi.” | Mô hình nguyên lý; độ phức tạp so sánh tiệm cận sau khi chọn mô hình hợp lý. |
| “Bất khả quyết định = chưa ai tìm ra thuật toán.” | Nghĩa là **chứng minh** không tồn tại thuật toán trong mô hình. |
| “Máy lượng tử giải bài toán dừng.” | Không: bài dừng vẫn không quyết định được theo nghĩa chuẩn. |
| “Mọi bài toán toán học đều quyết định được.” | Nhiều bài toán tự nhiên không quyết định được. |
| “P vs NP là phiên bản bài dừng.” | Không: P vs NP nằm trong thế giới **đã tính được**, hỏi hiệu quả. |
| “Turing test là định lý.” | Gợi ý triết học/hành vi; không phải định lý tính được. |

---

## Video và tài liệu

Video gợi ý: [https://www.youtube.com/watch?v=macM_MtS_w4](https://www.youtube.com/watch?v=macM_MtS_w4) (Computerphile, về Turing và bài toán dừng). Hãy dùng video để làm quen với bối cảnh, không dùng thay cho chứng minh.


![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/turing-computability_macM_MtS_w4_thumb.jpg)

*Hình. Khung hình mẫu từ video trên.*

## Tài liệu tham khảo trực tuyến

1. Wikipedia — Turing machine — https://en.wikipedia.org/wiki/Turing_machine  
2. Wikipedia — Halting problem — https://en.wikipedia.org/wiki/Halting_problem  
3. Wikipedia — Định đề Church–Turing thesis — https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis  
4. Wikipedia — Entscheidungsproblem — https://en.wikipedia.org/wiki/Entscheidungsproblem  
5. Stanford Encyclopedia — Turing machines — https://plato.stanford.edu/entries/turing-machine/  
6. Stanford Encyclopedia — Computability and complexity — https://plato.stanford.edu/entries/computability/  
7. Bài báo năm 1936 của Turing — https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf  
8. amturing.acm.org (giải thưởng mang tên Turing) — https://amturing.acm.org/  
9. Video Computerphile về Turing và bài toán dừng — https://www.youtube.com/watch?v=macM_MtS_w4  

1. Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proc. London Math. Soc.*  
2. Sipser, M. *Introduction to the Theory of Computation*: chương về máy Turing và tính không quyết định được.  
3. [Cantor đường chéo]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/); [Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/); [Lát gạch]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/).  
4. Soare, R. *Turing Computability*: góc nhìn hiện đại về lý thuyết đệ quy (đọc thêm).

---

## Hướng đi tiếp

- Viết một đoạn nối 1936 với câu hỏi hiệu quả ở [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): cùng “thuật toán,” khác tầng tài nguyên.  
- Tiếp: [Cook, Karp và NP-đầy đủ]({{ site.baseurl }}/contents/vi/chapter09/09_04_Cook_Karp_NP/).  
- Ôn [Giải Turing là gì?]({{ site.baseurl }}/contents/vi/chapter09/09_02_What_Is_Turing_Award/) để nhớ vì sao citation nhấn “nền tảng” hơn “gadget.”

---

## Tính được như đường chân trời

**Tính được** là chân trời nguyên lý; **độ phức tạp** là bản đồ độ cao bên trong. Turing đặt chân trời; Cook–Karp–Knuth–mật mã làm việc chủ yếu bên trong. Khi đọc tin về AI “giải toán”, hãy hỏi: bài **quyết định được**? Máy **dừng**? Chi phí theo $$n$$? Ba tầng tách bạch. Chỉ cần nắm ba bước của chứng minh bài toán dừng: **giả sử có $$H$$** → **dựng $$D$$** → **mâu thuẫn đường chéo**.

## Video tham khảo

- **Xem trước** — [Turing & The Halting Problem - Computerphile](https://www.youtube.com/watch?v=macM_MtS_w4) — Computerphile, tiếng Anh. Giới thiệu bài toán dừng và ý tưởng của Turing.
