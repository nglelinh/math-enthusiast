---
layout: post
title: "Wigderson: Ngẫu nhiên, Chứng minh và Độ phức tạp (Turing 2023)"
chapter: '09'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Avi Wigderson** nhận **A.M. Turing Award 2023** vì các đóng góp nền tảng cho lý thuyết tính toán—đặc biệt **ngẫu nhiên trong tính toán**, lý thuyết độ phức tạp, và việc định hình lại khoa học máy tính lý thuyết như một ngành toán học. Trước đó ông đã chia **Abel Prize 2021** với László Lovász: một cặp spotlight hiếm—vinh dự cao nhất của computing và giải trọn đời của toán thuần—trên lãnh thổ tri thức chồng lấn.

Bài này phát triển các chủ đề Wigderson ở mức seminar: ngẫu nhiên như tài nguyên; **derandomization** và paradigm hardness-versus-randomness; **chứng minh tương tác** và sức mạnh của tương tác + ngẫu nhiên trong verification; expander và pseudorandomness như cầu nối tới toán rời rạc; và cách đọc câu chuyện Turing *cùng với* [bài Abel về Lovász & Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/). Tài liệu chính thức: [amturing.acm.org](https://amturing.acm.org/), [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể giải thích vì sao ngẫu nhiên được coi là tài nguyên tính toán ngang thời gian và không gian; nêu khẩu hiệu derandomization rằng các giả thiết hardness phù hợp suy ra PRG hiệu quả và “sụp” các lớp ngẫu nhiên về phía lớp deterministic; mô tả interactive proofs như mô hình verification vượt quá witness NP tĩnh; gọi tên expander như đồ thị thưa nhưng trộn nhanh dùng làm đối tượng pseudorandom; và nối Turing 2023 với Abel 2021 mà không khẳng định giải nào đã giải [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/).

**Tiên quyết / liên kết seminar.** [Lý thuyết độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Yao / communication & minimax]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/), [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/), [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/). Hub chương: [Tổng quan Turing]({{ site.baseurl }}/contents/vi/chapter09/09_00_Tong_quan/).

---

## 1. Hai huy chương, một danh tính toán học

Abel 2021 vinh danh Lovász và Wigderson vì đã đưa toán rời rạc và khoa học máy tính lý thuyết trở thành **toán học hiện đại trung tâm**. Turing 2023 tập trung ống kính cộng đồng computing vào vai trò lãnh đạo độ phức tạp của Wigderson: ngẫu nhiên, liên hệ circuit complexity, hệ chứng minh, thuật toán, và hàng thập niên xây lĩnh vực (kể cả sách phổ biến *Mathematics and Computation*).

Với Math Enthusiast, giải đôi là vàng sư phạm. Sinh viên nghĩ “Turing = kỹ thuật” và “Abel = toán thuần” gặp phản ví dụ: cùng các định lý về expander, derandomization, và interactive proofs là **cả hai**.

---

## 2. Ngẫu nhiên như tài nguyên

Thuật toán ngẫu nhiên có thể dùng tung xu. Các lớp như **BPP** nắm các ngôn ngữ quyết định được trong thời gian đa thức với lỗi hai phía bị chặn. Lịch sử, ngẫu nhiên dường như mua sức mạnh thật: polynomial identity testing, một số thuật toán đồ thị, hashing, sampling, protocol giao tiếp ([Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/)).

Lý thuyết độ phức tạp hỏi sắc hơn:

- Ngẫu nhiên có *thiết yếu* không, hay mọi thuật toán ngẫu nhiên hiệu quả đều mô phỏng được hiệu quả không cần xu?  
- Số bit ngẫu nhiên tối thiểu là bao nhiêu?  
- Ngẫu nhiên tương tác thế nào với tương tác, nonuniformity (mạch), và pseudorandomness mật mã?

Thân công trình Wigderson coi các câu hỏi này là toán cấu trúc—không chỉ kỹ thuật thuật toán.

---

## 3. Hardness versus randomness

### Máy sinh giả ngẫu nhiên (PRG)

Một **PRG** kéo dài seed ngẫu nhiên ngắn thành chuỗi dài trông ngẫu nhiên với một lớp test hiệu quả (mạch kích thước bị chặn). Nếu tồn tại PRG mạnh, thuật toán cần nhiều bit ngẫu nhiên có thể liệt kê seed hoặc dùng chuỗi kéo dài và vẫn thành công với bảo đảm tương đương—**derandomization**.

### Paradigm

Một chủ đề sâu của độ phức tạp hiện đại:

> **Hardness tính toán** có thể chuyển thành **pseudorandomness**. Nếu có hàm đủ cứng với mạch, ta dựng được PRG đánh lừa mạch nhỏ hơn, suy ra hệ quả derandomization như $$\mathbf{BPP}$$ nằm trong thời gian deterministic subexponential hoặc thậm chí đa thức dưới giả thiết đủ mạnh.

Ngược lại, derandomization phi tầm thường thường suy ra chặn dưới mạch. Hardness và randomness là hai mặt của một lý thuyết.

**Cảnh báo literacy.** Đây là định lý **có điều kiện** và chương trình nghiên cứu. Bản thân chúng **không** giải P vs NP. Chúng cho thấy thế giới chặn dưới sẽ trả cổ tức thuật toán—và tham vọng derandomization thuật toán lại đè lên nghiên cứu chặn dưới.

---

## 4. Chứng minh tương tác

### Vượt certificate NP

Trong **NP**, prover mạnh gửi witness ngắn; verifier poly-time kiểm tĩnh. **Hệ chứng minh tương tác** cho phép nhiều vòng giao tiếp, thường với ngẫu nhiên ở verifier. Lớp **IP** bằng **PSPACE** (Shamir; dòng Lund–Fortnow–Karloff–Nisan)—một cột mốc: tương tác + ngẫu nhiên có thể verify ngôn ngữ được tin xa hơn NP.

### Zero knowledge và văn hóa chứng minh

**Chứng minh zero-knowledge** thuyết phục verifier mệnh đề đúng mà không tiết lộ gì khác khả thi để tính. Chúng trung tâm trong mật mã và worldview hiện đại “chứng minh như protocol”. Đóng góp và cộng tác của Wigderson giúp định hình nền tảng độ phức tạp của hệ chứng minh và verification tiết kiệm ngẫu nhiên.

### Đạo đức seminar

“Chứng minh” trong TCS không chỉ là PDF tĩnh các suy ra. Nó có thể là **protocol** với soundness error và completeness error, phân tích như thuật toán. Dịch chuyển khái niệm đó là quy mô Turing.

---

## 5. Expander và đối tượng pseudorandom

Một họ vô hạn đồ thị $$d$$-chính quy là **họ expander** nếu tập nhỏ giãn nở theo một hệ số xác định (tương đương, spectral gap bị chặn dưới độc lập kích thước). Expander trộn random walk nhanh dù thưa—chúng là đối tượng deterministic **hành xử ngẫu nhiên**.

Dùng gồm:

- derandomization và khuếch đại deterministic;  
- mã sửa lỗi;  
- độ bền thiết kế mạng;  
- cầu nối toán thuần (nhóm, hình học phổ)—cũng thấy trong narrative Abel với dựng kiểu Margulis ([Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/) kề cận).

Thế giới Wigderson coi expander là dụng cụ chuẩn, như nhà giải tích coi cơ Fourier. Xem thêm mục expander trong [bài Abel Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

---

## 6. Độ phức tạp như hình học của tính toán hiệu quả

Chương trình phổ biến của Wigderson trình bày các chủ đề TCS—mạch, reduction, ngẫu nhiên, tối ưu, mật mã—như toán học với định nghĩa, định lý, và bài toán mở độ khó kiểu Hilbert. [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn mở; quanh nó là các nhà thờ đã xây: IP = PSPACE, định lý PCP và độ cứng xấp xỉ, dựng expander, định lý derandomization có điều kiện, chặn dưới communication complexity.

Với LO6: khi viết phổ thông nói “lý thuyết độ phức tạp thất bại vì P vs NP còn mở,” hãy trả lời bằng danh sách định lý **không** cần kết quả đó. Giải trọn đời vinh danh **kiến trúc của một lĩnh vực**.

### Giảm lỗi tiết kiệm ngẫu nhiên

Một mini-chủ đề cụ thể: giả sử thuật toán BPP dùng nhiều bit ngẫu nhiên và lỗi với xác suất $$1/3$$. Lặp độc lập giảm lỗi theo hàm mũ nhưng nhân chi phí bit. **Walk trên expander** và các đối tượng pseudorandom liên quan có thể giảm lỗi trong khi tái chế ngẫu nhiên tiết kiệm hơn—cấu trúc đồ thị deterministic thay cho xu tươi. Đây là bản thu nhỏ của cả chương trình: dựng tổ hợp mua tiết kiệm tài nguyên mà xác suất ngây thơ phải trả bằng mẫu độc lập.

### Mạch, nonuniformity, và advice

Độ phức tạp phân biệt thuật toán uniform (một máy cho mọi độ dài) với **họ mạch** (có thể mạch khác cho mỗi độ dài đầu vào). Định lý derandomization thường nói ngôn ngữ mạch vì “test” mà PRG phải đánh lừa là nonuniform. Lý thuyết kiểu Wigderson thoải mái di chuyển giữa lớp uniform (P, BPP) và nonuniform (P/poly)—literacy thiết yếu để đọc paper hiện đại dù seminar này không dựng PRG từ hàm cứng từng bước.

### Zero knowledge như định nghĩa của “biết”

Ngoài IP = PSPACE, **zero knowledge** hình thức hóa việc thuyết phục mà không dạy. Định nghĩa đó định hình lại mật mã (protocol nhận dạng, hệ chứng minh hiện đại) và các câu hỏi gần triết học về tri thức. Đó là ví dụ flagship của TCS xuất khẩu một *định nghĩa* mạnh như một định lý: một khi “zero knowledge” chính xác, ta chứng minh protocol đạt nó dưới giả thiết, ghép chúng, và kiểm lời tuyên bố phổ thông rằng hệ “không tiết lộ gì.”

### Đọc Wigderson cạnh Yao

[Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/) nhấn chặn dưới giao tiếp và chuyển minimax giữa độ phức tạp ngẫu nhiên và phân bố. Wigderson nhấn khi nào ngẫu nhiên có thể **gỡ bỏ** và khi nào tương tác mở rộng sức mạnh chứng minh. Cùng nhau họ kẹp ngẫu nhiên: đôi khi xu là cần thiết theo thông tin hoặc theo độ phức tạp trong một mô hình; đôi khi hardness sản xuất xu đủ tốt cho thuật toán hiệu quả. Prompt tổng hợp seminar: chọn một bài toán và biện luận bạn đang ở mood “ngẫu nhiên giúp / chặn dưới” hay “derandomize dưới hardness.”

---

## 7. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “Turing 2023 / Abel 2021 đã giải P vs NP.” | Không. Cả hai vinh danh đóng góp nền tảng; P vs NP vẫn mở. |
| “BPP thực tế chỉ là P, nên ngẫu nhiên vô vị.” | Derandomization thực hành khác chứng minh; lý thuyết cấu trúc sâu và phần lớn có điều kiện. |
| “Interactive proof giống hệt certificate NP.” | Tương tác và ngẫu nhiên đổi mô hình verifier; IP = PSPACE là định lý lớn. |
| “Expander chỉ là đồ thị ngẫu nhiên.” | Đồ thị ngẫu nhiên thường expand; điểm còn gồm dựng **tường minh** và dùng deterministic. |
| “Derandomization nghĩa là xóa xác suất khỏi khoa học.” | Nghĩa là gỡ phụ thuộc thuật toán vào bit ngẫu nhiên dưới ràng buộc tài nguyên—không phủ nhận mô hình xác suất của dữ liệu. |
| “Wigderson chỉ làm chặn dưới.” | Chương trình khóa thuật toán, pseudorandomness, chứng minh, và giáo dục. |

---

## Bài tập

1. Nêu một bài toán ở mức khẩu hiệu nơi thuật toán ngẫu nhiên đơn giản hơn hoặc nhanh hơn.  
2. PRG đang cố đánh lừa cái gì, và vì sao điều đó derandomize thuật toán?  
3. Hardness vs randomness: giải thích con đường hai chiều trong ≤150 từ.  
4. Interactive proof khác kiểm witness NP cổ điển thế nào?  
5. Định nghĩa họ expander một câu (giãn nở hoặc spectral gap).  
6. **≤250 từ:** Vì sao cùng một người có thể thắng cả Abel và Turing cho công trình liên quan? Dùng chủ đề citation.  
7. Liệt kê ba định lý TCS vẫn thú vị ngay cả nếu P = NP (tái dùng kỷ luật bài Abel).  
8. Lướt trang Turing của Wigderson tại [amturing.acm.org](https://amturing.acm.org/) và tài liệu Abel 2021; viết bốn từ khóa xuất hiện ở cả hai narrative.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Xếp hạng và ghi chú đầy đủ: `research/video-research/wigderson-complexity/`.

**Khẩu hiệu từ gói nghiên cứu (phải nhớ)**

- **Năm Turing Award là 2023** (không phải 2021). Abel chung Lovász là **2021**.
- Ngẫu nhiên như tài nguyên; hardness↔randomness; expander; văn hóa interactive proofs.
- Sách *Mathematics and Computation*; sư phạm đôi Abel+Turing.

**Thứ tự xem gợi ý**

1. **Core** — Wigderson Turing Award Lecture (ACM): [https://www.youtube.com/watch?v=f2NiGO8zC1c](https://www.youtube.com/watch?v=f2NiGO8zC1c).  
2. **Orientation** — IAS Q&A Wigderson Turing: [https://www.youtube.com/watch?v=TK_vD-VnsFw](https://www.youtube.com/watch?v=TK_vD-VnsFw).  
3. **Orientation** — CACM June 2024 Wigderson feature: [https://www.youtube.com/watch?v=Ur9XNF6TeYw](https://www.youtube.com/watch?v=Ur9XNF6TeYw).  
4. **Related** — Wigderson — Reading Alan Turing (Berkeley): [https://www.youtube.com/watch?v=BiFSUniv70c](https://www.youtube.com/watch?v=BiFSUniv70c).  
5. **Cross** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  

**Cổng chính thức / tài liệu viết**

- Wigderson Turing 2023 page: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
- Wigderson Turing lecture page: https://amturing.acm.org/vp/wigderson_3844537.cfm  
- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  

Danh mục URL đầy đủ: `research/video-research/wigderson-complexity/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/wigderson-complexity/transcripts/` · trạng thái: `research/video-research/wigderson-complexity/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/wigderson-complexity_f2NiGO8zC1c_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/wigderson-complexity/references.md`.

1. Wigderson Turing 2023 page — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
2. Wigderson Turing lecture page — https://amturing.acm.org/vp/wigderson_3844537.cfm  
3. Wigderson Turing Award Lecture (ACM) — https://www.youtube.com/watch?v=f2NiGO8zC1c  
4. IAS Q&A Wigderson Turing — https://www.youtube.com/watch?v=TK_vD-VnsFw  
5. CACM June 2024 Wigderson feature — https://www.youtube.com/watch?v=Ur9XNF6TeYw  
6. Wigderson — Reading Alan Turing (Berkeley) — https://www.youtube.com/watch?v=BiFSUniv70c  
7. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
8. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
9. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
10. byyear listing (confirm 2023) — https://amturing.acm.org/byyear.cfm  
11. Mathematics and Computation (book info) — https://www.math.ias.edu/avi/book  
12. Thư mục gói: `research/video-research/wigderson-complexity/`.

1. ACM Turing Award 2023 — Avi Wigderson — [amturing.acm.org](https://amturing.acm.org/).  
2. Abel Prize 2021 — Lovász & Wigderson — [abelprize.no](https://abelprize.no/).  
3. A. Wigderson, *Mathematics and Computation* (Princeton); Arora–Barak, *Computational Complexity*; survey Vadhan về pseudorandomness.  
4. Khóa: [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/); [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/); [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/).

---

## Hướng đi tiếp

- Đọc một chương *Mathematics and Computation* như bài viết cho khán giả toán thuần.  
- So phương pháp chặn dưới minimax của Yao với tham vọng upper-bound derandomization dựa PRG.  
- Học phác dựng expander cụ thể (dù chỉ lịch sử tồn tại/tường minh kiểu Margulis).  
- Sau nhận thức IP = PSPACE: hé nhìn vai trò định lý PCP trong độ cứng xấp xỉ.  
- Tiếp: [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/)—privacy, tối ưu/ML theory, coding, thuật toán lượng tử, verification.
