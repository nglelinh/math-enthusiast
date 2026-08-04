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

Năm **1936**, trước khi máy tính điện tử phổ biến, **Alan Turing** công bố *On Computable Numbers, with an Application to the Entscheidungsproblem*. Bài báo không “phát minh laptop.” Nó làm một việc toán học sắc hơn: đưa ra mô hình chính xác cho **thủ tục hữu hạn, máy móc, từng bước** mà ta gọi là tính toán, rồi chứng minh rằng **không phải mọi bài toán đều giải được** bởi bất kỳ thủ tục nào thuộc lớp đó. Cùng thời kỳ, Church, Kleene, Post và những người khác xây dựng các hình thức tương đương; luận đề **Church–Turing** tóm tắt sự hội tụ: mọi khái niệm hợp lý về “tính được bằng thuật toán” đều trùng với lớp hàm máy Turing tính được.

Bài này là chân dung **ý tưởng**, không phải tiểu sử đầy đủ. Ta đi từ máy Turing, qua tính phổ quát và bài toán dừng, tới họ hàng với đường chéo Cantor và bất toàn Gödel, rồi ranh giới với **độ phức tạp hiệu quả** (P vs NP) ở các bài sau. Liên kết: [Giải Turing là gì?]({{ site.baseurl }}/contents/vi/chapter09/09_02_What_Is_Turing_Award/), [Định lý bất toàn Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/), [Đường chéo Cantor]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô tả máy Turing ở mức thành phần (băng, đầu đọc–ghi, trạng thái hữu hạn, bảng chuyển) và giải thích vì sao mô hình cố ý thô.  
- Phát biểu ý **máy phổ quát** và liên hệ với “phần mềm chạy trên phần cứng.”  
- Phát biểu **bài toán dừng** và phác thảo ý tưởng chứng minh bất khả quyết định bằng đường chéo.  
- Phân biệt **không tính được / không quyết định được** với **khó tính (NP-khó)** và với **bất toàn logic**.  
- Nêu luận đề Church–Turing như tuyên bố mô hình, không như định lý trong ZFC theo nghĩa thông thường.  
- Tránh nhầm: “máy Turing chậm nên vô dụng,” “mọi thứ toán học đều quyết định được,” “bất khả quyết định = chưa tìm ra thuật toán.”

**Tiên quyết.** Quen ý thuật toán như quy trình hữu hạn bước; số nguyên và xâu bit; đọc được ký hiệu tập hợp cơ bản. Không cần đã học ôtômat hình thức; ta ở mức ý tưởng seminar. Toán rời rạc ở mức quan hệ và hàm là đủ.

---

## 1. Entscheidungsproblem và nhu cầu một mô hình

Hilbert và các đồng nghiệp hỏi, đại khái, liệu có **thủ tục tổng quát** quyết định tính đúng/chứng minh được của mọi công thức trong một hệ logic đủ mạnh không. Để trả lời “không,” trước hết phải định nghĩa “thủ tục” đủ chặt: nếu “thủ tục” mơ hồ, câu trả lời phủ định cũng mơ hồ.

Turing chọn hình ảnh máy với:

- **băng** chia ô, mỗi ô chứa một ký hiệu từ bảng chữ cái hữu hạn (có thể coi là $$0,1$$ và khoảng trống);  
- **đầu** đọc/ghi một ô tại một thời điểm, có thể dịch trái/phải;  
- **trạng thái hữu hạn** kiểm soát hành vi;  
- **bảng chuyển** hữu hạn: từ (trạng thái, ký hiệu đang đọc) sang (ký hiệu viết, hướng dịch, trạng thái mới).

Máy bắt đầu trên input hữu hạn, chạy theo bảng chuyển. Nó có thể **dừng** với output, hoặc **chạy mãi**. Một ngôn ngữ $$L\subseteq\{0,1\}^*$$ **quyết định được** nếu có máy luôn dừng và chấp nhận đúng các xâu thuộc $$L$$. Một hàm **tính được** nếu có máy, trên mọi input hợp lệ, dừng và in giá trị đúng.

Mô hình cố ý nghèo nàn về kỹ thuật—không cache, không GPU—nhưng giàu về nguyên lý: mọi “thuật toán” ta viết bằng tay hoặc bằng ngôn ngữ lập trình hiện đại đều mô phỏng được bằng máy Turing (với chi phí thời gian–không gian có thể lớn). Đó là điểm mạnh sư phạm: độ khó **không quyết định được** không phụ thuộc vào việc ta chọn C++ hay Python.

---

## 2. Máy phổ quát và ý tưởng phần mềm

Turing chỉ ra tồn tại **máy phổ quát** $$U$$: khi được cung cấp mô tả mã hóa $$\langle M\rangle$$ của một máy $$M$$ cùng input $$x$$, $$U$$ mô phỏng hành vi của $$M$$ trên $$x$$. Nói không hình thức:

$$
U\big(\langle M\rangle, x\big) \;\text{mô phỏng}\; M(x).
$$

Đây là hạt nhân khái niệm của **chương trình như dữ liệu**. Phần cứng cố định; phần mềm là mô tả; máy phổ quát diễn giải mô tả. Lịch sử kỹ thuật sau này—von Neumann, hệ điều hành, máy ảo, container—là hiện thực hóa kỹ nghệ của ý tưởng đã có trong lý thuyết 1936.

Hệ quả triết học–toán: lớp hàm tính được **không** phụ thuộc việc ta “mua thêm opcode.” Thêm cú pháp ngôn ngữ lập trình không vượt ra ngoài lớp đệ quy (recursive functions) nếu vẫn trong khuôn khổ thuật toán chuẩn. Muốn vượt, phải đổi mô hình theo hướng khác (oracle, không tất định với tài nguyên, lượng tử với chi phí khác, v.v.)—và ngay cả khi đó, câu chuyện **bất khả quyết định** vẫn còn nhiều biến thể.

---

## 3. Bài toán dừng

**Bài toán dừng (halting problem).** Cho mô tả máy $$\langle M\rangle$$ và input $$x$$, hỏi: $$M$$ có dừng trên $$x$$ không?

**Định lý (Turing).** Không tồn tại máy Turing $$H$$ quyết định đúng bài toán dừng cho mọi cặp $$(\langle M\rangle, x)$$.

**Ý tưởng chứng minh (đường chéo).** Giả sử, phản chứng, có $$H$$ sao cho $$H(\langle M\rangle, x)=1$$ nếu $$M(x)$$ dừng, và $$=0$$ nếu không. Xây máy $$D$$ hành xử như sau trên input $$\langle M\rangle$$: chạy $$H(\langle M\rangle, \langle M\rangle)$$; nếu $$H$$ báo “dừng,” thì $$D$$ **lặp vô hạn**; nếu $$H$$ báo “không dừng,” thì $$D$$ **dừng**. Xét $$D$$ trên input $$\langle D\rangle$$:

- Nếu $$D(\langle D\rangle)$$ dừng, thì theo xây dựng $$H$$ đã báo không dừng—mâu thuẫn.  
- Nếu $$D(\langle D\rangle)$$ không dừng, thì $$H$$ đã báo dừng—mâu thuẫn.

Do đó $$H$$ không thể tồn tại. Đây là anh em của đường chéo Cantor (xây đối tượng thoát mọi liệt kê) và của câu Gödel (tự tham chiếu có kiểm soát). Cùng một **động tác thoát**: với mọi ứng viên “tổng quát,” dựng hành vi lật trên đường chéo.

---

## 4. Họ hàng bất khả quyết định

Một khi bài toán dừng không quyết định được, hàng loạt bài toán khác **quy về** nó (reduction theo nghĩa tính được): nếu ta quyết định được bài $$A$$ thì ta quyết định được bài dừng—do đó $$A$$ cũng không quyết định được.

Ví dụ cổ điển (mức khẩu hiệu seminar):

- **Bài toán trống (emptiness)** cho một số lớp máy/chương trình đủ mạnh: “chương trình có bao giờ chấp nhận input nào không?”  
- **Bài toán tương đương** chương trình: “hai chương trình có cùng hành vi trên mọi input không?”  
- **Bài toán dừng với input rỗng.**  
- Trong logic: tính thỏa mãn của một số lớp công thức đủ biểu đạt (liên hệ Entscheidungsproblem).  
- Trong hình học rời rạc: **lát Wang** toàn phẳng—Berger chứng minh bất khả quyết định bằng cách nhúng mô phỏng tính toán vào quy tắc màu cạnh; xem hương vị ở [Lát gạch]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/).

Reduction ở tầng tính được khác reduction poly-time ở tầng NP-đầy đủ, nhưng **tinh thần** giống nhau: chuyển độ khó từ bài đã biết sang bài mới, bảo toàn câu trả lời có/không.

---

## 5. Số tính được và Church–Turing

**Số thực tính được** có thủ tục in chữ số/xấp xỉ theo yêu cầu. Chỉ đếm được nhiều chương trình, trong khi $$\mathbb{R}$$ không đếm được—hầu hết số thực không tính được ([vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/), [Cantor]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/)). Tồn tại cổ điển ≠ tồn tại **có thuật toán**.

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

Gödel và Turing họ hàng đường chéo nhưng **không đồng nhất**. Gödel nói về chứng minh trong hệ tiên đề; Turing nói về dừng của máy. Có cầu kỹ thuật sâu (số hóa cú pháp, biểu diễn quan hệ tính được), nhưng khẩu hiệu seminar cần giữ tách: “không chứng minh được” ≠ “không tính được” ≠ “NP-khó.”

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

## Bài tập

1. Liệt kê năm thành phần của máy Turing và giải thích trong một câu vì sao bảng chuyển phải hữu hạn.  
2. Viết ≤120 từ giải thích máy phổ quát cho người chưa học tin học, dùng ẩn dụ “công thức nấu ăn + đầu bếp.”  
3. Phác thảo (không cần formal) bước đường chéo trong chứng minh bài dừng: chỉ rõ chỗ nào $$D$$ “lật” câu trả lời của $$H$$.  
4. Cho ví dụ reduction khẩu hiệu: nếu quyết định được bài toán X thì quyết định được bài dừng—do đó X không quyết định được. Tự chọn X ở mức ý tưởng (ví dụ tương đương chương trình).  
5. Phân biệt bằng bảng 2×2: quyết định được / không; hiệu quả (poly-time) / không hiệu quả—đặt P vs NP và bài dừng vào đúng ô.  
6. Đọc lại [Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/): viết ba câu về họ hàng đường chéo **và** một câu về khác biệt.  
7. **≤250 từ:** Vì sao “thêm RAM, thêm core” không giải quyết bài toán dừng?  
8. Studio: mô phỏng bằng tay một máy Turing 2–3 trạng thái cộng hai số unary nhỏ; ghi cấu hình từng bước.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/turing-computability/`.

**Khẩu hiệu từ gói nghiên cứu**

- Máy Turing; bài toán dừng không quyết định được; Entscheidungsproblem.
- Không quyết định được ≠ “chưa tìm ra thuật toán.”

**Thứ tự xem gợi ý**

1. **ORIENTATION** — Computerphile / Numberphile culture: search Turing halting: [https://www.youtube.com/watch?v=macM_MtS_w4](https://www.youtube.com/watch?v=macM_MtS_w4).  

**Cổng chính thức / tài liệu**

- amturing.acm.org (award named for Turing): https://amturing.acm.org/  

Danh mục URL đầy đủ: `research/video-research/turing-computability/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/turing-computability/transcripts/` · trạng thái: `research/video-research/turing-computability/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/turing-computability_macM_MtS_w4_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/turing-computability/references.md`.

1. Wikipedia — Turing machine — https://en.wikipedia.org/wiki/Turing_machine  
2. Wikipedia — Halting problem — https://en.wikipedia.org/wiki/Halting_problem  
3. Wikipedia — Church–Turing thesis — https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis  
4. Wikipedia — Entscheidungsproblem — https://en.wikipedia.org/wiki/Entscheidungsproblem  
5. SEP — Turing machines — https://plato.stanford.edu/entries/turing-machine/  
6. SEP — Computability and complexity — https://plato.stanford.edu/entries/computability/  
7. Turing's 1936 paper (archive culture) — https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf  
8. amturing.acm.org (award named for Turing) — https://amturing.acm.org/  
9. Computerphile / Numberphile culture: search Turing halting — https://www.youtube.com/watch?v=macM_MtS_w4  
10. Thư mục gói: `research/video-research/turing-computability/`.

1. Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proc. London Math. Soc.*  
2. Sipser, M. *Introduction to the Theory of Computation* — chương máy Turing và undecidability.  
3. [Cantor đường chéo]({{ site.baseurl }}/contents/vi/chapter05/05_03_Cantor_Diagonal/); [Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/); [Lát gạch]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/).  
4. Soare, R. *Turing Computability* — góc nhìn hiện đại về lý thuyết đệ quy (đọc thêm).

---

## Hướng đi tiếp

- Viết một đoạn nối 1936 với câu hỏi hiệu quả ở [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): cùng “thuật toán,” khác tầng tài nguyên.  
- Tiếp: [Cook, Karp và NP-đầy đủ]({{ site.baseurl }}/contents/vi/chapter09/09_04_Cook_Karp_NP/).  
- Ôn [Giải Turing là gì?]({{ site.baseurl }}/contents/vi/chapter09/09_02_What_Is_Turing_Award/) để nhớ vì sao citation nhấn “nền tảng” hơn “gadget.”

---

## Tính được như đường chân trời

**Tính được** là chân trời nguyên lý; **độ phức tạp** là bản đồ độ cao bên trong. Turing đặt chân trời; Cook–Karp–Knuth–mật mã làm việc chủ yếu bên trong. Đọc tin AI “giải toán”: bài **quyết định được**? Máy **dừng**? Chi phí theo $$n$$? Ba tầng tách bạch. Seminar chỉ cần nắm ba khối chứng minh dừng: **giả sử có $$H$$** → **dựng $$D$$** → **mâu thuẫn đường chéo**.
