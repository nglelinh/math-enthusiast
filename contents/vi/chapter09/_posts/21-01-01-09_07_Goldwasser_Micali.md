---
layout: post
title: "Goldwasser, Micali và Nền tảng Mật mã Hiện đại (Turing 2012)"
chapter: '09'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Shafi Goldwasser** và **Silvio Micali** nhận Giải Turing **2012** cho các đóng góp cách mạng tạo nên **nền tảng lý thuyết độ phức tạp** của mật mã hiện đại—gồm định nghĩa an ninh có thể chứng minh, mã hóa xác suất, và đặc biệt văn hóa **zero-knowledge proof**. Nếu Diffie–Hellman và RSA mang **paradigm khóa công khai** vào thế giới, Goldwasser–Micali (và trường phái đồng hành) mang **ngôn ngữ chứng minh**: an ninh không còn là khẩu hiệu engineering mà là định lý dạng “mọi adversary poly-time thành công với xác suất không đáng kể dưới giả định X.”

Bài này đọc citation 2012 như bản đồ khái niệm: semantic security, scheme Goldwasser–Micali dựa trên quadratic residuosity, zero-knowledge, và cầu sang interactive proof / randomness. Liên kết: [Khóa công khai]({{ site.baseurl }}/contents/vi/chapter09/09_06_Public_Key_Crypto/), [mật mã ch.03]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao **mã hóa tất định** kiểu textbook RSA không đạt an ninh ngữ nghĩa mạnh.  
- Phát biểu ý **semantic security / IND-CPA** ở mức: ciphertext không tiết lộ thông tin tính toán được về plaintext.  
- Mô tả scheme **Goldwasser–Micali**: bit plaintext → quadratic residue / non-residue với ký hiệu Jacobi điều khiển; homomorphic XOR.  
- Nêu ba tính chất **zero-knowledge**: completeness, soundness, zero-knowledge (simulator).  
- Phân biệt “chứng minh tương tác” với “đưa nguyên witness.”  
- Tránh nhầm: “zero-knowledge = mã hóa,” “có ZK ⇒ P = NP,” “an ninh có chứng minh = không thể bị phá trên implementation.”

**Tiên quyết.** RSA/DH ở mức cơ chế; xác suất sơ cấp; ý poly-time adversary. Đồng dư và ký hiệu Jacobi/quadratic residue hữu ích; ta giải thích lại ngắn.

---

## 1. Từ “trông khó” tới định nghĩa trò chơi

Mật mã tiền hiện đại thường lập luận: “muốn phá phải factoring, mà factoring khó.” Lỗ hổng logic: adversary có thể khôi phục **một bit** plaintext, hoặc phân biệt hai thông điệp, mà không factoring hoàn toàn. Cần định nghĩa **mục tiêu an ninh** và **mô hình tấn công**.

Trường phái Goldwasser–Micali–Rackoff và cộng đồng 1980s đưa mật mã vào khung:

- **Adversary** là thuật toán (thường prob. poly-time).  
- **Experiment/game**: challenger sinh khóa, adversary chọn thách thức, nhận ciphertext, cố thắng (đoán bit, khôi phục message, …).  
- **Lợi thế (advantage)** phải **negligible** theo tham số an ninh $$\lambda$$ nếu scheme an toàn.

**Semantic security** (ý): mọi thông tin về plaintext mà adversary tính được từ ciphertext, nó cũng tính được *không* cần ciphertext—tức ciphertext “vô dụng” về mặt tính toán. Tương đương thực dụng với **IND-CPA**: adversary chọn hai plaintext $$m_0,m_1$$; nhận mã của $$m_b$$ ngẫu nhiên; không đoán $$b$$ tốt hơn $$1/2 + \mathrm{negl}$$.

Hệ quả quan trọng: scheme **tất định** (cùng $$m$$ luôn ra cùng $$c$$) không thể IND-CPA nếu adversary được mã hóa thử—vì nó tự mã $$m_0,m_1$$ và so khớp. Do đó **mã hóa xác suất** là bắt buộc cho an ninh hiện đại: cùng plaintext, nhiều ciphertext.

---

## 2. Quadratic residuosity và scheme Goldwasser–Micali

Số $$a$$ là **quadratic residue** modulo $$n$$ nếu $$\gcd(a,n)=1$$ và tồn tại $$x$$ với $$x^2\equiv a\pmod n$$. Với $$n=pq$$, bài toán **quadratic residuosity (QRP)**—phân biệt residue và non-residue khi ký hiệu Jacobi bằng $$+1$$—được tin khó nếu factoring khó (liên hệ cổ điển).

**Scheme GM (ý tưởng):**

- Khóa công khai gồm $$n=pq$$ và một non-residue $$z$$ với Jacobi symbol $$(z/n)=1$$.  
- Để mã **một bit** $$b\in\{0,1\}$$: chọn ngẫu nhiên $$r$$, gửi  
  $$
  c \equiv r^2 \cdot z^b \pmod n.
  $$  
  Nếu $$b=0$$, $$c$$ là residue; nếu $$b=1$$, $$c$$ là non-residue (loại Jacobi $$+1$$).  
- Giải bằng cửa sập $$p,q$$: kiểm tra residuality modulo $$p$$ và $$q$$ (hoặc tương đương).

**An ninh:** dưới giả định QRP, ciphertext không tiết lộ $$b$$ cho adversary poly-time—đúng tinh thần semantic security cho bit. **Chi phí:** mỗi bit plaintext phình thành một phần tử modulo $$n$$—không thực dụng throughput, nhưng là **mẫu chuẩn**: định nghĩa + giả định số học + chứng minh reduction.

**Homomorphic:** nhân ciphertext (mod $$n$$) tương ứng XOR bit plaintext (khi cẩn thận). Đây là gợi ý sớm cho **mã hóa đồng cấu**—họ hàng xa của FHE hiện đại.

---

## 3. Zero-knowledge: chứng minh mà không tiết lộ

**Bài toán trực giác.** Peggy (prover) muốn thuyết phục Victor (verifier) rằng bà biết một bí mật—ví dụ “đồ thị này 3-tô màu được” hoặc “tôi biết square root” hoặc “ciphertext mã bit 0”—**mà không** tiết lộ witness.

**Zero-knowledge proof (ZKP)** tương tác (phiên bản cổ điển) thỏa:

1. **Completeness:** nếu statement đúng và prover trung thực, verifier chấp nhận với xác suất cao.  
2. **Soundness:** nếu statement sai, mọi prover gian (dù mạnh) bị từ chối với xác suất cao (hoặc knowledge soundness: có thể trích witness).  
3. **Zero-knowledge:** verifier không học gì *ngoài* tính đúng của statement—formal qua **simulator**: mọi thứ verifier thấy có thể mô phỏng mà không cần witness.

Điểm triết học–toán: “không học gì” không phải cảm giác; đó là **tồn tại simulator poly-time** sinh transcript không phân biệt được (computationally) với tương tác thật.

### Ví dụ khẩu hiệu: 3-tô màu (Goldreich–Micali–Wigderson)

Prover biết tô màu $$\chi$$. Mỗi vòng: random permute màu, cam kết (commitment) màu đỉnh; verifier chọn một cạnh; prover mở màu hai đầu cạnh; verifier kiểm tra khác màu. Lặp nhiều vòng. Gian dối trên cạnh xấu bị bắt với xác suất dương mỗi vòng; honest verifier gần như không học tô màu toàn cục nhờ permute + commitment. Chi tiết commitment và mô hình cần sách chuyên khảo; seminar cần **hình dạng**: thách thức ngẫu nhiên + mở cục bộ + lặp để khuếch đại soundness.

### Ví dụ số học: residuality / square root

Prover chứng minh biết căn bậc hai hoặc chứng minh ciphertext GM mã bit nào đó—các protocol sigma cổ điển. Random challenge từ verifier buộc prover “cam kết trước,” không adapt gian.

---

## 4. Interactive proof, IP, và bạn hàng độ phức tạp

Zero-knowledge sống trong hệ sinh thái **interactive proof**: prover mạnh (đôi khi không giới hạn) và verifier poly-time trao đổi tin nhắn. Định lý nổi tiếng $$\mathbf{IP}=\mathbf{PSPACE}$$ (Shamir et al.) cho thấy tương tác + randomness tăng sức mạnh kiểm chứng vượt NP. ZK gắn thêm ràng buộc “không rò rỉ.”

Cầu sang [Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/): randomness là tài nguyên; commitment và PRG dựa trên hardness; expander và derandomization chạm cùng văn hóa pseudorandomness. Goldwasser–Micali đặt **mật mã** vào đúng thành phố độ phức tạp, không phải ngoại ô ad hoc.

**NIZK, zk-SNARK, blockchain.** Sau này: non-interactive ZK (Fiat–Shamir), SNARK/STARK với proof ngắn và verify nhanh—ứng dụng blockchain, private rollup, authentication. Di sản 2012 là **định nghĩa và khả năng tồn tại**; engineering 2020s là nén và concrete cost.

---

## 5. Reduction an ninh: nghề chứng minh

Một lemma kiểu GM: nếu adversary phá IND-CPA của scheme X với advantage không negligible, thì tồn tại algorithm dùng adversary đó để phá giả định Y (QRP, DDH, RSA, LWE, …) với advantage liên quan. Chứng minh an ninh là **reduction**—anh em tinh thần Karp, khác mục tiêu: không chứng minh NP-đầy đủ, mà chứng minh “phá crypto ⇒ phá mỏ số học.”

**Giới hạn.** Reduction asymptotic không tự động là concrete security tốt. Constant lớn, mô hình idealized (ROM), và gap giữa proof và implementation (side channel, bug) vẫn tồn tại. “Provable security” là tầng toán; sản phẩm cần thêm engineering và audit.

---

## 6. Phụ nữ, mentor, và xây lĩnh vực

Citation Turing 2012 vinh danh **nền tảng**. Goldwasser và Micali (cùng học trò và cộng tác) định hình chương trình học mật mã lý thuyết toàn cầu: định nghĩa game-based, zero-knowledge, pseudorandomness, encryption an toàn. Đây là kiểu đóng góp Abel/Turing cùng họ: **đổi khí hậu**, không chỉ một gadget.

Trong khóa *Math Enthusiast*, đây là dịp nhắc: toán–tin hiện đại không chỉ “nam giới huyền thoại 1936–1978.” Đọc citation và paper; tránh xóa lịch sử cộng đồng.

---

## 7. Nhầm lẫn thường gặp

| Khẳng định | Chỉnh |
|------------|-------|
| “Zero-knowledge giấu mọi thứ kể cả statement.” | Verifier học rằng statement **đúng**; không học witness. |
| “ZK chứng minh P = NP.” | Không: verifier không nhận witness dạng ngắn để tự kiểm trong mô hình NP cổ điển theo cùng cách; interactive/randomness đổi mô hình. |
| “GM scheme thay AES trong TLS.” | GM là mẫu lý thuyết bit-wise; thực tế dùng AEAD đối xứng + KEM/signature hiện đại. |
| “Semantic security = information-theoretic secrecy.” | Semantic security là **tính toán** (poly-time adversary); one-time pad là thông tin lý thuyết. |
| “Provable security ⇒ không bị hack.” | Proof trong mô hình; bug, side channel, phishing nằm ngoài game. |
| “Mã hóa tất định đủ nếu modulus lớn.” | Tất định xung đột IND-CPA khi adversary mã hóa thử được. |

---

## Bài tập

1. Giải thích ≤80 từ vì sao RSA textbook tất định không IND-CPA nếu adversary có $$pk$$ và chọn được $$m_0,m_1$$.  
2. Viết công thức mã bit GM và chỉ ra vai trò của $$r$$ ngẫu nhiên.  
3. Định nghĩa completeness / soundness / zero-knowledge mỗi cái một câu.  
4. Mô tả simulator *ý*: vì sao tồn tại simulator khiến “verifier không học witness” thành toán?  
5. So 1 đoạn: reduction Karp (NP-đầy đủ) vs reduction an ninh mật mã—giống và khác.  
6. **≤250 từ:** Quadratic residuosity đóng vai trò “mỏ” thế nào trong GM, song song factoring trong RSA.  
7. Đọc thêm một nguồn phổ biến về zk-SNARK (mức sơ đồ) và viết 5 câu nối về di sản ZK 1980s.  
8. Studio: chơi protocol 3-tô màu trên đồ thị 4 đỉnh (giấy): một người prover, một verifier, 3 vòng challenge cạnh.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/goldwasser-micali/`.

**Khẩu hiệu từ gói nghiên cứu**

- Turing 2012 Goldwasser–Micali: mã hóa xác suất, zero-knowledge.

**Thứ tự xem gợi ý**


**Cổng chính thức / tài liệu**

- Goldwasser Turing: https://amturing.acm.org/award_winners/goldwasser_8627889.cfm  
- Micali Turing: https://amturing.acm.org/award_winners/micali_9954407.cfm  
- Wigderson Turing 2023 (proof systems culture): https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Danh mục URL đầy đủ: `research/video-research/goldwasser-micali/references.md`.

## Tài liệu


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/goldwasser-micali/references.md`.

1. Goldwasser Turing — https://amturing.acm.org/award_winners/goldwasser_8627889.cfm  
2. Micali Turing — https://amturing.acm.org/award_winners/micali_9954407.cfm  
3. Wikipedia — Shafi Goldwasser — https://en.wikipedia.org/wiki/Shafi_Goldwasser  
4. Wikipedia — Silvio Micali — https://en.wikipedia.org/wiki/Silvio_Micali  
5. Wikipedia — Zero-knowledge proof — https://en.wikipedia.org/wiki/Zero-knowledge_proof  
6. Wikipedia — Semantic security — https://en.wikipedia.org/wiki/Semantic_security  
7. Wikipedia — Goldwasser–Micali cryptosystem — https://en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem  
8. Wigderson Turing 2023 (proof systems culture) — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
9. ACM announcement culture 2012 — https://awards.acm.org/about/2012-turing  
10. Thư mục gói: `research/video-research/goldwasser-micali/`.

1. Goldwasser, S., & Micali, S. (1984). Probabilistic encryption. *J. Comput. Syst. Sci.*  
2. Goldwasser, S., Micali, S., & Rackoff, C. (1989). The knowledge complexity of interactive proof systems. *SIAM J. Comput.*  
3. ACM Turing Award 2012 citation: Goldwasser & Micali.  
4. Goldreich, O. *Foundations of Cryptography* — chuẩn mực định nghĩa.  
5. [Khóa công khai]({{ site.baseurl }}/contents/vi/chapter09/09_06_Public_Key_Crypto/); [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

---

## Hướng đi tiếp

- Viết một trang: “an ninh là trò chơi” với IND-CPA tự mô tả.  
- Quay lại [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) và giải thích vì sao average-case one-way functions không suy ra từ NP-đầy đủ worst-case.  
- Các bài sau chương 09 (Yao, Valiant, Pearl, deep learning, …) mở rộng spotlight Turing sang communication complexity, learning, causality—giữ thói quen: citation → đối tượng → cơ chế → liên kết khóa.

---

## Chứng minh như sản phẩm mật mã

Di sản sâu nhất có lẽ không phải một modulus hay một protocol cụ thể, mà là **chuẩn nghề**: đề xuất scheme kèm định nghĩa an ninh, mô hình adversary, và chứng minh reduction. Cộng đồng có thể bác giả định, siết định nghĩa (CCA thay CPA), hoặc chỉ ra gap—nhưng cuộc chơi là toán học, không phải khẩu hiệu brochure.

Trong seminar, khi ai đó nói “hệ này an toàn,” hãy hỏi: *an toàn theo game nào? adversary được làm gì? giả định tên gì? reduction có concrete không?* Bốn câu Goldwasser–Micali-style đó nâng thảo luận từ tin đồn sang khoa học.

## Homomorphic XOR và gợi ý đồng cấu

Nhân hai ciphertext GM (mod $$n$$) cho ciphertext của XOR hai bit—ví dụ sớm cho tính toán trên dữ liệu mã hóa. FHE hiện đại (Gentry và hậu duệ, lattice) mạnh hơn nhiều, nhưng **câu hỏi** đã được đặt: mật mã không chỉ giấu dữ liệu; nó có thể cho phép **xử lý có kiểm soát**. Chương Turing nối câu hỏi đó với độ phức tạp và giả định đại số.

## Tóm tắt sợi chỉ chương 09 đến đây

| Bài | Sợi chỉ |
|-----|---------|
| Turing Award là gì? | Spotlight thể chế |
| Turing 1936 | Chân trời tính được |
| Cook–Karp | Bản đồ độ khó hiệu quả |
| Knuth | Đo chi phí thuật toán |
| DH / RSA | Cửa sập số học trên kênh công cộng |
| Goldwasser–Micali | Định nghĩa an ninh + zero-knowledge |

Đọc xuôi: từ “cái gì tính được” tới “cái gì tính được *hiệu quả*,” tới “cái gì *chứng minh được là khó đủ* để tin cậy.” Đó là xương sống toán học tính toán trong khóa *Math Enthusiast*.
