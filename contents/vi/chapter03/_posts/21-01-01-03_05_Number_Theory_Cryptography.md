---
layout: post
title: "Lý thuyết Số → Mật mã học"
chapter: '03'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Từng là “nữ hoàng toán học” thuần túy nhất, **lý thuyết số** nay bảo vệ giao tiếp an toàn trên internet. Mỗi bắt tay TLS, chữ ký phần mềm và biểu tượng khóa tin nhắn đều tiêu thụ số học modulo, sinh số nguyên tố và bài toán khó trên nhóm.

Bài **flagship Phần 3** theo một chuỗi cơ chế sạch:

**số học modulo → hàm cửa sập → mật mã khóa công khai (RSA, Diffie–Hellman, ECC) → giao thức internet thật → bóng lượng tử và lưới hậu lượng tử.**

Mục tiêu **LO4**: nối lĩnh vực cổ điển với công nghệ có tên, kèm cơ chế một bước đúng—không khẩu hiệu “lý thuyết số dùng trong mật mã.”

**Lộ trình:** đồng dư → đối xứng vs khóa công khai → RSA → DH → ECC → chữ ký/PKI/lai → văn hóa độ khó → PQC → nhầm lẫn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tính và diễn giải $$a\equiv b\pmod n$$; giải thích lũy thừa modulo nhanh.
- Giải thích **ý tưởng khóa công khai**: tách mã hóa khỏi giải mã nhờ cửa sập.
- Nêu **cơ chế RSA** ở mức $$n=pq$$, số mũ $$e,d$$, giả định phân tích thừa số.
- Mô tả **Diffie–Hellman** như thỏa thuận $$g^{ab}$$ từ $$g^a,g^b$$ công khai.
- Nêu vì sao **đường cong elliptic** thu nhỏ khóa và vì sao **hậu lượng tử** chuyển sang lưới/mã/hash.
- Tránh nhầm: RSA không phải “chỉ nhân hai nguyên tố”; an ninh = độ khó tính toán + kỹ thuật; PQC ≠ chỉ QKD.

**Kiến thức nền.** Số nguyên, nguyên tố, lũy thừa.

**Liên kết.** [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/).

---

## 1. Số học modulo: đại số phần dư

Cố định số nguyên dương $$n$$ (**modulo**). Ta viết

$$
a \equiv b \pmod{n}
$$

khi $$n$$ chia hết $$a-b$$—tương đương $$a$$ và $$b$$ cùng số dư khi chia cho $$n$$.

Làm việc **mod $$n$$** giống đồng hồ $$n$$ giờ: sau $$n-1$$ quay về $$0$$. Cộng và nhân đồng dư nhất quán:

$$
a\equiv a',\quad b\equiv b' \pmod{n} \implies a+b\equiv a'+b',\quad ab\equiv a'b' \pmod{n}.
$$

Vành $$\mathbb{Z}/n\mathbb{Z}$$ là ngôi nhà đại số của crypto textbook. Khi $$n=p$$ nguyên tố, mọi phần dư khác 0 có nghịch đảo nhân—$$\mathbb{Z}/p\mathbb{Z}$$ là **trường**—nên phép chia và đại số tuyến tính trên trường hữu hạn khả dụng (AES dùng số học trường hữu hạn; đường cong elliptic trên $$\mathbb{F}_p$$).

**Lũy thừa nhanh.** Tính $$a^e\bmod n$$ với $$e$$ khổng lồ khả thi bằng **bình phương lặp** trong $$O(\log e)$$ phép nhân. Tính *căn bậc $$e$$* hoặc *log rời rạc* được tin là khó trong thiết lập chọn kỹ. Bất đối xứng đó—lũy thừa dễ, đảo khó—là quặng thô của mật mã khóa công khai.

**Hương vị Fermat / Euler.** Nếu $$p$$ nguyên tố và $$p\nmid a$$ thì $$a^{p-1}\equiv 1\pmod p$$ (Fermat). Tổng quát hơn, định lý Euler dùng $$\varphi(n)$$—số phần dư nguyên tố cùng nhau với $$n$$. Tính đúng của RSA dựa trên triệt tiêu số mũ modulo kiểu đó—**không** dựa trên giấu thuật toán (thuật toán là công khai).

**Thuật toán Euclid** tính $$\gcd$$ và nghịch đảo modulo trong thời gian log—lý thuyết số thế kỷ XIX thành subroutine thế kỷ XXI.

---

## 2. Đối xứng vs khóa công khai

**Mật mã đối xứng:** Alice và Bob chia sẻ trước một khóa bí mật; mã hóa và giải mã dùng cùng bí mật (AES-GCM, ChaCha20-Poly1305, …). Tuyệt cho dữ liệu khối tốc độ đường truyền; tệ với câu hỏi khởi động: *làm sao bắt đầu nói chuyện an toàn nếu chưa từng gặp nhau và mạng đầy kẻ nghe lén?*

**Mật mã khóa công khai** (Diffie–Hellman 1976; RSA 1978; biến thể elliptic sau đó): mỗi bên công bố khóa **công khai** và giữ khóa **bí mật**. Ai cũng mã hóa tới bạn bằng khóa công khai; chỉ bạn giải được. Chữ ký số đảo trực giác: chỉ bạn ký; ai cũng kiểm bằng khóa công khai của bạn.

Phép màu toán học là **hàm một chiều có cửa sập**: dễ tính, khó đảo khi không có cấu trúc bí mật, dễ đảo khi có cửa sập.

**Nguyên lý Kerckhoffs.** An ninh dựa trên bí mật khóa, không dựa trên giấu thuật toán. Crypto hiện đại giả định thuật toán công khai và bị chuyên gia tấn công.

---

## 3. RSA: phân tích thừa số như cửa sập

**Thiết lập (RSA textbook đơn giản hóa).**

1. Chọn nguyên tố bí mật lớn $$p,q$$; công bố $$n=pq$$ (không công bố $$p,q$$).  
2. Tính $$\varphi(n)=(p-1)(q-1)$$ (bí mật).  
3. Chọn số mũ công khai $$e$$ nguyên tố cùng nhau với $$\varphi(n)$$ (thực tế hay $$e=65537$$).  
4. Tính $$d$$ bí mật với $$ed\equiv 1\pmod{\varphi(n)}$$ (nghịch đảo modulo).  
5. Mã hóa đại diện tin $$m$$: $$c\equiv m^e\pmod n$$.  
6. Giải: $$m\equiv c^d\pmod n$$.

**Cơ chế một câu.**  
*Mã hóa là lũy thừa modulo với số mũ công khai; giải mã cần số mũ nghịch đảo—dễ nếu biết $$\varphi(n)$$ (nên biết $$p,q$$), được tin là khó nếu chỉ biết $$n$$.*

**Giả định độ khó (không chính thức).** Phân tích semiprime lớn bất khả thi ở cỡ khuyến nghị (hàng nghìn bit). Nếu phân tích thừa số dễ, cửa sập RSA sụp. Sắc thái: các reduction an ninh chỉ liên hệ đảo RSA với factoring từng phần; **padding** (OAEP, PSS) bắt buộc—RSA textbook thô dễ bị malleable, không triển khai được.

**Lý thuyết số thuần đóng góp gì.** Euclid, nghịch đảo modulo, $$\varphi$$ Euler, sinh nguyên tố (kể cả kiểm tra nguyên tố xác suất), và độ phức tạp tính toán của factoring—lịch sử Gauss-to-Gentry nén vào bắt tay khóa.

**Vệ sinh tham số.** $$e$$ nhỏ + padding xấu, chia sẻ nguyên tố giữa các moduli, RNG thiên vị, side channel—đều đã phá RSA “đúng toán” ngoài đời. Lý thuyết số cho cửa sập; kỹ thuật cho phần còn lại của bề mặt tấn công.

---

## 4. Diffie–Hellman và log rời rạc

Tham số công khai: một nhóm (cổ điển: nhóm nhân modulo nguyên tố, hoặc nhóm đường cong elliptic) và generator $$g$$ của một nhóm con lớn cấp nguyên tố.

- Alice chọn bí mật $$a$$, gửi $$A=g^a$$.  
- Bob chọn bí mật $$b$$, gửi $$B=g^b$$.  
- Bí mật chung: $$A^b=B^a=g^{ab}$$.

**Bài toán log rời rạc (DLP):** cho $$g$$ và $$g^a$$, khôi phục $$a$$. Nếu DLP khó, kẻ nghe lén không nên tính được $$g^{ab}$$ chỉ từ các giá trị công khai (dưới giả định kiểu CDH/DDH, phát biểu cẩn thận).

**Cơ chế.**  
*Truyền công khai là lũy thừa nhóm; bí mật chung là tổ hợp song tuyến các bí mật trong số mũ—chỉ bên biết ít nhất một số mũ thấy được.*

**DH trường hữu hạn** cần nguyên tố lớn và tham số an toàn chống index-calculus. Áp lực đó góp phần thúc đẩy elliptic curves.

---

## 5. Mật mã đường cong elliptic (ECC)

Một **đường cong elliptic** trên trường (ở đây trường hữu hạn $$\mathbb{F}_q$$) có thể viết, dạng Weierstrass đơn giản, là

$$
y^2 = x^3 + Ax + B
$$

với discriminant khác 0. Tập điểm cộng điểm vô cực tạo thành **nhóm** abelian dưới luật dây–tiếp tuyến hình học. Nhân vô hướng $$P\mapsto aP$$ (cộng $$P$$ với chính nó $$a$$ lần) dễ; đảo lại (log rời rạc elliptic) được tin khó trên đường cong chọn tốt.

**Cùng mẫu giao thức DH**, khóa nhỏ hơn cho an ninh cổ điển tương đương khuyến nghị (ví dụ đường cong 256 bit so với modulus RSA 3072 bit—số cụ thể thay đổi theo hướng dẫn). Stack TLS điện thoại gần như chắc đàm phán ECDHE.

**Cơ chế.**  
*ECC chuyển Diffie–Hellman từ nhóm nhân của trường hữu hạn sang nhóm điểm trên đường cong chọn kỹ—cùng hình cửa sập, mật độ an ninh theo bit cao hơn.*

Hình học số học sâu lặng lẽ bước vào an ninh hàng hóa—một chiến thắng chủ đề chương cho toán “thuần.”

---

## 6. Chữ ký, chứng chỉ, và mã hóa lai

Mã hóa khóa công khai một mình không dựng được web. Còn cần:

- **Chữ ký** (RSA-PSS, ECDSA, EdDSA, …) để cập nhật phần mềm và tài liệu chứng minh nguồn gốc và toàn vẹn.  
- **Chứng chỉ** (PKI / X.509) gắn khóa với danh tính qua cơ quan tin cậy hoặc mô hình tin cậy khác.  
- **Mã hóa lai (hybrid):** dùng khóa công khai (hoặc KEM) thiết lập khóa phiên đối xứng, rồi AES (hoặc tương tự) cho bulk.  
- **Authenticated encryption** để ciphertext không bị sửa lặng.

Lý thuyết số ngồi ở bắt tay; kỹ thuật, kinh tế và luật ngồi ở mô hình tin cậy. Cả hai có thể hỏng—RNG xấu (thảm họa Debian OpenSSL), CA bị xâm nhập, tấn công hạ cấp giao thức—mà giả định độ khó nền vẫn chưa “sai.”

---

## 7. Văn hóa độ khó: mật mã gặp độ phức tạp

Mật mã cần bài toán:

1. Dễ sinh instance,  
2. Dễ giải với cửa sập / bí mật,  
3. Khó cho đối thủ trên instance **điển hình** (trung bình, không chỉ worst-case).

Họ hàng nhưng không trùng **P vs NP**. NP-đầy đủ là về độ khó worst-case của bài quyết định; crypto muốn độ khó trung bình *dùng được* có cấu trúc (xem [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/)). Dù vậy cả hai cùng nằm trong văn hóa **bất khả thi tính toán như tài nguyên**.

Hàm một chiều, bộ tạo giả ngẫu nhiên, và zero-knowledge tinh chỉnh văn hóa này xa hơn RSA—nhưng câu chuyện undergrad vẫn bắt đầu từ số học modulo.

---

## 8. Bóng lượng tử và mật mã hậu lượng tử

**Thuật toán Shor** (lượng tử) phân tích thừa số và tính log rời rạc đa thức—đe dọa RSA và DH/ECC cổ điển nếu máy lượng tử lớn, tin cậy ra đời. Grover cho tăng tốc bình phương tìm kiếm không cấu trúc, thúc kích cỡ khóa đối xứng nhưng không “phá” AES ở độ dài nhân đôi theo cách Shor phá RSA.

**Mật mã hậu lượng tử (PQC)** chuyển giả định độ khó sang các bài chưa biết sụp vì Shor, đặc biệt:

- **Lưới** (Learning With Errors và họ hàng)—hình học số như crypto,  
- **Mã** (kiểu McEliece),  
- **Chữ ký dựa hash** (thận trọng, stateful hoặc SPHINCS-like stateless),  
- Ý tưởng đa thức và isogeny—luôn dưới cryptanalysis (một số hệ isogeny đã đổ).

Quá trình chuẩn hóa NIST PQC (Kyber/ML-KEM, Dilithium/ML-DSA, … với tên và tham số tiến hóa) là mặt thể chế của chuyển đổi này. Xem [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

**Cơ chế chuyển.**  
*Khóa công khai cổ điển khai thác one-way số học trên nhóm nhân và elliptic; PQC khai thác độ khó lưới cao chiều và cấu trúc liên quan—vẫn toán thuần nuôi hạ tầng.*

---

## 9. Vì sao lý thuyết số “sẵn sàng”

Tính nguyên tố, nghịch đảo modulo, cấu trúc nhóm, và ám ảnh số nguyên tố có trước thương mại điện tử. Khi Diffie, Hellman, Rivest, Shamir và Adleman cần cửa sập, hộp dụng cụ đã trên kệ. Di cư pure→applied không đòi đổi tên môn; đòi nhận ra **độ khó tính toán giả định** cũng quý như công thức đóng.

Giả thuyết Riemann ([Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/)) vẫn là ngọn hải đăng thuần về nguyên tố; mật mã là cách dùng số học khác—nhưng cả hai chứng tỏ cấu trúc số nguyên không cạn.

---

### Vệ sinh video mật mã (từ nghiên cứu)

Lộ trình phổ biến: [Numberphile RSA](https://www.youtube.com/watch?v=M7kEpw1tn50) → [RSA-129](https://www.youtube.com/watch?v=YQw124CtvO0) → [Computerphile public key](https://www.youtube.com/watch?v=GSIDS_lvRv4) → [Diffie–Hellman](https://www.youtube.com/watch?v=NmM9HA2MQGI).

- Video giải thích *trapdoor* tốt; thường bỏ padding, side channel, và vệ sinh tham số.
- Tính đúng RSA dùng Euler/Fermat; an ninh là tính toán, không phải lý thuyết thông tin.
- Hậu lượng tử: xem [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography).

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “RSA an toàn vì nhân khó.” | Nhân dễ; *phân tích thừa số* mới là hướng khó. |
| “Giấu thuật toán = an toàn.” | Kerckhoffs: thuật toán công khai; bí mật là khóa. |
| “$$n$$ to hơn luôn cứu.” | Cỡ quan trọng, nhưng padding, side channel, RNG, giao thức cũng vậy. |
| “ECC an toàn vì cong phức tạp.” | Dựa trên ECDLP của nhóm được chọn + triển khai đúng. |
| “Hậu lượng tử = chỉ crypto lượng tử.” | PQC thường là thuật toán cổ điển chống tấn công lượng tử. |
| “P≠NP ⇒ RSA an toàn mãi.” | Cần độ khó trung bình của bài cụ thể. |

---

## Bài tập

1. $$17\bmod 5$$, $$2^8\bmod 7$$, tìm $$x$$ với $$3x\equiv 1\pmod 7$$.  
2. Giải thích khóa công khai vs bí mật hai câu cho người không học toán.  
3. Vì sao công bố $$n=pq$$ không tức thì công bố $$p,q$$ với nguyên tố lớn?  
4. DH: kẻ nghe lén thấy $$g^a,g^b$$—log rời rạc cho phép làm gì?  
5. **LO4 (≤300 từ).** Cơ chế một bước nối lũy thừa modulo với mã hóa khóa công khai.  
6. Phê một bài báo “crypto không thể phá” vì một câu overclaim.  
7. Nâng cao: vì sao web dùng hybrid thay vì RSA cho mọi bulk traffic?

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/number-theory-cryptography/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — Numberphile — Encryption and HUGE numbers (RSA): [https://www.youtube.com/watch?v=M7kEpw1tn50](https://www.youtube.com/watch?v=M7kEpw1tn50).
2. **INTUITION / history** — Numberphile — RSA-129: [https://www.youtube.com/watch?v=YQw124CtvO0](https://www.youtube.com/watch?v=YQw124CtvO0).
3. **FOUNDATION** — Computerphile — Public Key Cryptography: [https://www.youtube.com/watch?v=GSIDS_lvRv4](https://www.youtube.com/watch?v=GSIDS_lvRv4).
4. **CORE** — Computerphile — Diffie-Hellman Key Exchange: [https://www.youtube.com/watch?v=NmM9HA2MQGI](https://www.youtube.com/watch?v=NmM9HA2MQGI).
5. **SURVEY** — Numberphile/Computerphile crypto playlist: [https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj](https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj).
6. **FOUNDATION** — Khan Academy — Journey into cryptography (hub): [https://www.khanacademy.org/computing/computer-science/cryptography](https://www.khanacademy.org/computing/computer-science/cryptography).

Danh mục URL đầy đủ: `research/video-research/number-theory-cryptography/references.md`.



### Transcript & frames (extract flagship)

Transcript caption và unit theo thời gian: `research/video-research/number-theory-cryptography/transcripts/` · trạng thái: `research/video-research/number-theory-cryptography/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Caption tải tự động (yt-dlp)—dùng để điều hướng, **không** thay nội dung bài.


![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/crypto_rsa_frame01.jpg)

*Hình. Frame mẫu từ video flagship chính (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/number-theory-cryptography/references.md`.

### Video (lộ trình chính)

1. Numberphile — Encryption and HUGE numbers (RSA) — https://www.youtube.com/watch?v=M7kEpw1tn50
2. Numberphile — RSA-129 — https://www.youtube.com/watch?v=YQw124CtvO0
3. Computerphile — Public Key Cryptography — https://www.youtube.com/watch?v=GSIDS_lvRv4
4. Computerphile — Diffie-Hellman Key Exchange — https://www.youtube.com/watch?v=NmM9HA2MQGI
5. Numberphile/Computerphile crypto playlist — https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj
6. Khan Academy — Journey into cryptography (hub) — https://www.khanacademy.org/computing/computer-science/cryptography
7. Stanford / Dan Boneh crypto course culture (Coursera/YouTube search) — https://crypto.stanford.edu/~dabo/courses/
8. NIST Post-Quantum Cryptography project — https://csrc.nist.gov/projects/post-quantum-cryptography

### Video (tìm thêm / phụ)

9. Numberphile — primes and primality culture videos — https://www.youtube.com/@numberphile

### Bài báo, sách, OCW và web

10. Rivest, Shamir, Adleman — A Method for Obtaining Digital Signatures… (1978): https://people.csail.mit.edu/rivest/Rsapaper.pdf
11. Diffie & Hellman — New Directions in Cryptography (1976): https://ee.stanford.edu/~hellman/publications/24.pdf
12. NIST PQC standards overview: https://csrc.nist.gov/projects/post-quantum-cryptography
13. Wikipedia — RSA (cryptosystem): https://en.wikipedia.org/wiki/RSA_(cryptosystem)
14. Wikipedia — Diffie–Hellman key exchange: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
15. Wikipedia — Post-quantum cryptography: https://en.wikipedia.org/wiki/Post-quantum_cryptography

### Trong khóa

16. Khóa: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Gói: `research/video-research/number-theory-cryptography/`.

## Hướng đi tiếp

- Flagship seminar LO4. Toy RSA số nguyên tố nhỏ (không an toàn); thảo luận padding.  
- [Đồ thị → Mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) hoặc [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).  
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
