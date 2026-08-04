---
layout: post
title: "Yao: Minimax, Độ phức tạp Giao tiếp (Turing 2000)"
chapter: '09'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Andrew Chi-Chih Yao** nhận **A.M. Turing Award 2000**

> “in recognition of his fundamental contributions to the theory of computation, including the complexity-based theory of pseudorandom number generation, cryptography, and communication complexity.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Bài này không liệt kê CV. Nó dựng **ba ý tưởng Yao** đã trở thành ngôn ngữ chung của theoretical computer science: (1) **nguyên lý minimax** nối thuật toán ngẫu nhiên với phân tích deterministic worst-case trên phân phối; (2) **độ phức tạp giao tiếp** như mô hình tài nguyên nơi bit trao đổi—không phải chu kỳ CPU—là “thời gian”; (3) cầu sang **pseudorandomness** và mật mã, nơi hardness tính toán biến thành bit “gần ngẫu nhiên”. Đọc vì cơ chế; năm giải chỉ là đèn spotlight. Liên kết nền: [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).

---

## Mục tiêu học tập

Sau bài, bạn có thể phát biểu **nguyên lý Yao** (minimax) ở mức khẩu hiệu chính xác: cost tối ưu randomized worst-case bằng cost tối ưu deterministic trung bình theo phân phối khó nhất; định nghĩa **độ phức tạp giao tiếp** hai bên cho hàm $$f:\{0,1\}^n\times\{0,1\}^n\to\{0,1\}$$ và giải thích vì sao nó khác thời gian máy Turing; nêu một chặn dưới giao tiếp kinh điển (ví dụ equality hoặc set disjointness) và ý nghĩa “thông tin phải đi qua kênh”; mô tả vì sao mô hình giao tiếp nuôi streaming, data structure, circuit depth và multiparty; nối Yao với [ngẫu nhiên–derandomization]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/) mà không tuyên bố mọi thuật toán ngẫu nhiên đã bị “giải mã” deterministic.

**Kiến thức nền.** Xác suất cơ bản (kỳ vọng, phân phối); runtime poly vs mũ; ý minimax trong lý thuyết trò chơi (giá trị maximin/minimax). Biết [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) giúp ví dụ, không bắt buộc.

---

## 1. Yao và không khí Turing 2000

Cuối thập niên 1970–80, complexity không chỉ hỏi “bài này thuộc P hay NP-đầy đủ?”. Người ta hỏi **tài nguyên tinh**: số bit ngẫu nhiên, số bit giao tiếp, độ sâu mạch, số truy vấn. Yao là một trong những người biến các câu hỏi đó thành **định lý và phương pháp**, không chỉ heuristic kỹ thuật.

Citation Turing 2000 nhấn ba cột: pseudorandomness dựa hardness, cryptography, communication complexity. Bài này tập trung **minimax + communication**, vì chúng là “toán thuần” rõ nhất cho khóa học Math Enthusiast: định lý cấu trúc, chặn dưới thông tin, và một chuyển đổi maxim–min đẹp như lý thuyết trò chơi. Phần PRG/crypto sẽ chạm nhẹ và trỏ sang [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) cùng bài Wigderson.

Hình ảnh hữu ích: nếu Knuth dạy ta *phân tích* thuật toán, Cook–Karp dạy ta *độ khó worst-case có điều kiện*, thì Yao dạy ta **tách mô hình tài nguyên** và **đổi thứ tự lượng tử hóa** (minimax) để chứng minh cái không thể.

---

## 2. Nguyên lý Yao: minimax cho thuật toán ngẫu nhiên

### Randomized worst-case vs distributional deterministic

Xét lớp thuật toán deterministic $$\mathcal{A}$$ cho bài toán, và lớp “tung xu” là phân phối trên $$\mathcal{A}$$ (mô hình Las Vegas/Monte Carlo tùy chuẩn lỗi). Với input $$x$$, cost $$C(A,x)$$ có thể là thời gian, số so sánh, số bit giao tiếp…

- **Chi phí randomized worst-case** của thuật toán ngẫu nhiên $$R$$ (phân phối trên $$A$$):  
  $$\displaystyle \max_x \mathbb{E}_{A\sim R}[C(A,x)].$$
- **Chi phí deterministic trung bình** trên phân phối input $$D$$:  
  $$\displaystyle \mathbb{E}_{x\sim D}[C(A,x)].$$

**Nguyên lý Yao** (dạng minimax cổ điển áp vào complexity): trong thiết lập zero-sum hữu hạn thích hợp,

$$
\min_R \max_x \mathbb{E}_{A\sim R} C(A,x)
\;=\;
\max_D \min_A \mathbb{E}_{x\sim D} C(A,x).
$$

Khẩu hiệu đúng: **chi phí tối ưu của thuật toán ngẫu nhiên trong worst-case bằng chi phí deterministic tốt nhất khi input được chọn từ phân phối khó nhất**. Hệ quả phương pháp cực mạnh: để chặn dưới randomized complexity, chỉ cần dựng **một** phân phối $$D$$ khó cho *mọi* thuật toán deterministic, rồi lấy min–average. Không cần “đuổi” mọi protocol ngẫu nhiên.

### Vì sao đây là toán, không chỉ mẹo chứng minh

Minimax của von Neumann (và dạng Yao–Yao cho complexity) nói rằng trong trò chơi zero-sum, thứ tự “ai đi trước” có thể đổi khi cho phép mixed strategy. Yao biến **algorithm designer vs adversary** thành trò chơi đó. Adversary chọn input (hoặc phân phối); designer chọn thuật toán (hoặc phân phối trên thuật toán). Giá trị trò chơi là complexity. Đây là cầu giữa [lý thuyết trò chơi]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) (minimax, cân bằng) và chặn dưới thuật toán.

**Cảnh báo đọc.** Nguyên lý Yao *không* nói “randomness vô dụng”. Nó nói: sức mạnh randomness, nếu có, phải thể hiện như lợi thế **trung bình trên phân phối**, và adversary có thể “biết” mixed strategy của bạn theo nghĩa worst-case expectation. Randomness vẫn có thể giảm cost kỳ vọng trên input cố định; minimax so sánh *các đại lượng tối ưu* hai phía.

### Ứng dụng tư duy nhanh

Muốn chứng minh không có thuật toán so sánh ngẫu nhiên tìm phần tử lớn thứ $$k$$ với ít hơn $$c\,n$$ so sánh trong worst-case expectation? Đủ dựng phân phối input làm mọi cây quyết định deterministic trả giá trung bình $$\ge c\,n$$. Nhiều chặn dưới cổ điển (sorting, selection, một phần communication) đi theo khuôn này.

---

## 3. Độ phức tạp giao tiếp: bit là tài nguyên

### Mô hình Yao

Hai bên **Alice** và **Bob** nhận lần lượt $$x,y\in\{0,1\}^n$$. Họ muốn tính $$f(x,y)$$ bằng cách gửi tin nhắn qua kênh; mỗi bên thấy input riêng, không thấy input kia. **Độ phức tạp giao tiếp** $$D(f)$$ (deterministic) là số bit tối thiểu trong protocol đúng mọi $$(x,y)$$. Phiên bản ngẫu nhiên $$R(f)$$ cho phép xu nội bộ và lỗi nhỏ. Multiparty, quantum, nondeterministic là biến thể.

Điểm khái niệm: đây **không** phải “mạng máy tính chậm”. Đây là **mô hình thông tin tối thiểu** cần để tính $$f$$ khi dữ liệu bị phân mảnh. Chặn dưới giao tiếp là định lý về *cấu trúc* $$f$$—thường qua ma trận truyền thông $$M_f[x,y]=f(x,y)$$, phân hoạch hình chữ nhật, rank, mutual information.

### Equality: ví dụ mở đầu

$$
\mathrm{EQ}(x,y)=\begin{cases}1 & x=y,\\ 0 & x\neq y.\end{cases}
$$

Deterministic: cần $$\Theta(n)$$ bit trong mô hình chuẩn (Alice không thể nén $$x$$ thành ít bit mà vẫn phân biệt mọi khả năng Bob). Randomized (public/private coins tùy chuẩn): fingerprinting cho phép $$O(\log n)$$ bit với lỗi nhỏ—hash ngẫu nhiên so khớp. Bài học kép: (1) randomness *đổi* complexity giao tiếp; (2) minimax/Yao vẫn áp để chặn dưới randomized protocols qua phân phối hard.

### Set disjointness: chặn dưới “cứng”

$$
\mathrm{DISJ}(x,y)=1 \iff \forall i,\; x_i y_i=0
$$

(hai tập con $$[n]$$ rời nhau). Đây là hàm “nặng” thông tin: randomized communication complexity $$\Theta(n)$$ (kết quả sâu, nhiều proof qua information complexity). Hệ quả lan: nhiều bài streaming và data structure kế thừa chặn dưới gần tuyến tính—bạn không thể tóm tắt stream bằng bộ nhớ quá nhỏ mà vẫn trả lời giao cắt/thống kê liên quan.

### Hình chữ nhật và rank

Protocol deterministic đúng cảm ứng **phân hoạch** không gian $$\{0,1\}^n\times\{0,1\}^n$$ thành hình chữ nhật đơn sắc (cùng giá trị $$f$$). Số hình chữ nhật liên quan số lá/protocol tree và do đó số bit. **Log-rank conjecture** (còn mở ở dạng đầy đủ) nối $$D(f)$$ với $$\log\operatorname{rank}(M_f)$$: rank tuyến tính của ma trận Boolean như proxy độ phức tạp. Đây là toán tổ hợp–đại số tuyến tính thuần túy sinh từ CS.

---

## 4. Từ giao tiếp sang streaming, mạch, cấu trúc dữ liệu

### Streaming

Một pass trên stream độ dài $$m$$ với bộ nhớ $$s$$ bits có thể mô phỏng như giao tiếp giữa “quá khứ” và “tương lai” của stream. Chặn dưới communication ⇒ chặn dưới memory. Vì thế disjointness và index xuất hiện khắp lý thuyết streaming hiện đại (ước lượng $$F_k$$, heavy hitters có điều kiện hardness…).

### Data structures

Cell-probe và static data structure lower bounds thường **giảm** về multiparty communication hoặc pointer chasing. Câu hỏi “cấu trúc bao nhiêu bit, truy vấn bao nhiêu probe?” trở thành câu hỏi thông tin giữa người dựng và người hỏi.

### Circuit depth và parallel time

Kohn–Kushilevitz–Nisan và dòng công trình nối communication complexity với độ sâu mạch và branching program. Intuition: wire giữa hai nửa mạch “giao tiếp” giá trị trung gian. Chặn dưới giao tiếp đa bên nuôi chặn dưới song song.

### Multiparty number-on-forehead

Mỗi bên thấy mọi input *trừ* input trán mình—mô hình lạ nhưng mạnh cho chặn dưới mạch AC$$^0$$ và tách lớp. Yao không “sở hữu” mọi định lý sau này; ông **mở sân** để các định lý đó có ngôn ngữ chung.

---

## 5. Pseudorandomness và mật mã (cột citation còn lại)

Yao còn gắn với quan điểm **computational indistinguishability**: hai phân phối “giống nhau” nếu mọi test hiệu quả không phân biệt được với lợi thế không đáng kể. Từ đó: định nghĩa modern của bit generator an toàn, và cầu “hardness ⇒ pseudorandomness” mà chương trình derandomization (Impagliazzo, Wigderson, …) khai thác.

Khẩu hiệu khóa học: **hardness không chỉ là rào cản; hardness là nguyên liệu**. Hàm đủ khó có thể ép bit trông ngẫu nhiên với mọi observer poly-time. Xem [mật mã số học]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) và [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/). Turing 2000 vinh danh đúng sự thống nhất đó—không chỉ một paper communication.

### Yao’s millionaires và secure computation (bối cảnh)

Giao thức “hai triệu phú” so sánh tài sản mà không lộ số—mầm của secure multiparty computation. Ở đây complexity giao tiếp gặp mật mã: bao nhiêu bit, dưới giả thiết số học nào, leakage nào chấp nhận được. Bài học Math Enthusiast: cùng một người có thể vừa chứng minh *chặn dưới thông tin thuần*, vừa thiết kế *giao thức dương* dưới giả thiết crypto.

---

## 6. Minimax trong learning và online algorithms (cầu ngang)

Nguyên lý dạng Yao xuất hiện lại khi phân tích **online learning** và statistical decision: regret minimax, distributional hardness cho estimation. Không phải mọi minimax đều “định lý Yao 1977”, nhưng thói quen tư duy giống nhau: worst-case randomized = best response trên prior khó. [Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) dùng ngôn ngữ đó cho rates; bài này cho bạn gốc complexity.

Studio seminar gợi ý: lấy một chặn dưới sorting bằng adversary argument cổ điển; viết lại bằng ngôn ngữ “phân phối $$D$$ làm mọi cây quyết định trả giá trung bình $$\ge \log_2(n!)-o(\cdot)$$”. Đó là tập gym cho nguyên lý Yao.

---

## 7. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “Độ phức tạp giao tiếp = latency mạng.” | Mô hình tài nguyên *thông tin*; không phải kỹ thuật TCP. |
| “Nguyên lý Yao ⇒ randomness vô dụng.” | Nói về *giá trị tối ưu* worst-case vs distributional; EQ randomized vẫn rẻ hơn deterministic. |
| “Communication complexity chỉ cho lý thuyết thuần.” | Nuôi streaming, data structure, circuit, crypto protocols. |
| “Chặn dưới $$n$$ bit ⇒ bài NP-đầy đủ.” | Sai phạm trù; đây là mô hình khác P vs NP. |
| “Rank ma trận = thời gian CPU.” | Rank là invariant đại số; conjecture nối với $$D(f)$$, không phải runtime Turing. |
| “Yao chỉ communication.” | Citation còn PRG/crypto; communication là một trụ. |

**Không nên tuyên bố.** “Đã derandomize mọi thứ vì có minimax.” Minimax là công cụ *chứng minh và so sánh*, không phải thuật toán biến Monte Carlo thành deterministic zero-error miễn phí.

---

## 8. Đọc định lý chặn dưới giao tiếp như thế nào

Khi paper nói “$$R_{1/3}(\mathrm{DISJ})=\Omega(n)$$”, checklist:

1. **Mô hình:** private vs public coins? error một phía hay hai phía?  
2. **Hàm promise:** full disjointness hay gap version?  
3. **Loại chặn:** information complexity, corruption bound, discrepancy?  
4. **Giảm bài:** streaming/data structure reduce *về* DISJ thế nào (ai là Alice/Bob)?  
5. **Hằng số và asymptotically:** $$\Omega(n)$$ hay $$\Omega(n/\log n)$$?  

Biết đọc biên giới (LO6) ở communication complexity chính là checklist này cộng sự khiêm tốn về hằng số concrete.

---

## Bài tập

1. Phát biểu nguyên lý Yao ≤80 từ; nêu một hệ quả phương pháp (“để chặn dưới randomized, đủ…”).  
2. Vì sao deterministic EQ cần $$\Omega(n)$$ bit trong mô hình chuẩn? Lập luận thông tin / pigeonhole một đoạn.  
3. Mô tả fingerprinting randomized cho EQ: Alice gửi hash $$h(x)$$; Bob so $$h(y)$$. Lỗi từ đâu?  
4. Viết định nghĩa DISJ; giải thích một câu vì sao chặn dưới gần tuyến tính “đau” cho streaming giao cắt.  
5. **≤200 từ:** So minimax Yao với minimax lý thuyết trò chơi zero-sum: giống ở đâu, đối tượng $$C(A,x)$$ khác gì payoff cổ điển.  
6. Nối [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/): communication complexity có “giải” P vs NP không? Vì sao không.  
7. **Seminar:** Chọn một lower bound data structure (cell-probe) trên survey; chỉ ra bước reduce về communication (ai nói với ai).

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/yao-complexity/`.

**Khẩu hiệu từ gói nghiên cứu**

- Yao Turing 2000: communication complexity, minimax, PRG/quantum culture.

**Thứ tự xem gợi ý**


**Cổng chính thức / tài liệu**

- Yao Turing page: https://amturing.acm.org/award_winners/yao_1611524.cfm  
- Wigderson randomness (related resource theory): https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Danh mục URL đầy đủ: `research/video-research/yao-complexity/references.md`.

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/yao-complexity/references.md`.

1. Yao Turing page — https://amturing.acm.org/award_winners/yao_1611524.cfm  
2. Wikipedia — Andrew Yao — https://en.wikipedia.org/wiki/Andrew_Yao  
3. Wikipedia — Communication complexity — https://en.wikipedia.org/wiki/Communication_complexity  
4. Wikipedia — Yao's principle — https://en.wikipedia.org/wiki/Yao%27s_principle  
5. Wikipedia — Pseudorandom generator — https://en.wikipedia.org/wiki/Pseudorandom_generator  
6. Yao class / IIIS Tsinghua culture — https://iiis.tsinghua.edu.cn/en/  
7. Wigderson randomness (related resource theory) — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
8. Survey entry: Kushilevitz–Nisan book culture — https://en.wikipedia.org/wiki/Communication_complexity  
9. Thư mục gói: `research/video-research/yao-complexity/`.

1. ACM A.M. Turing Award — Andrew C. Yao (2000), citation và lecture.  
2. Kushilevitz & Nisan — *Communication Complexity* (sách nền).  
3. Rao & Yehudayoff — *Communication Complexity* (Cambridge; hiện đại, information).  
4. Yao — papers nền về minimax principle và communication protocols (thập niên 1970–80).  
5. Khóa: [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/); [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/); [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/).

---

## Hướng đi tiếp

- Ngẫu nhiên như tài nguyên toàn cục: [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).  
- Hardness nuôi crypto: [mật mã số học]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) và [mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).  
- Learning rates minimax: [lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).  
- Thực hành: cài fingerprinting EQ; đo số bit vs xác suất lỗi trên $$n$$ tăng.  
- Đọc: một chapter Kushilevitz–Nisan về rectangle → một survey information complexity → một paper streaming lower bound.  
- Tiếp chương: [Valiant và học tính toán]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/).
