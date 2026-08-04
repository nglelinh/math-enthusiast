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

$$
a\equiv b\pmod n
$$

khi $$n$$ chia hết $$a-b$$. Cộng nhân đồng dư nhất quán. Khi $$n=p$$ nguyên tố, $$\mathbb{Z}/p\mathbb{Z}$$ là trường—mọi phần tử khác 0 có nghịch đảo.

**Lũy thừa nhanh** $$a^e\bmod n$$ bằng bình phương lặp $$O(\log e)$$. Tìm căn hoặc log rời rạc được tin là khó trong thiết lập chọn kỹ—quặng thô của mật mã khóa công khai.

Fermat/Euler: nếu $$p\nmid a$$ thì $$a^{p-1}\equiv 1\pmod p$$. Tính đúng của RSA dựa trên triệt tiêu số mũ modulo—không dựa trên giấu thuật toán. **Euclid** tính $$\gcd$$ và nghịch đảo modulo: lý thuyết số thế kỷ XIX thành subroutine thế kỷ XXI.

---

## 2. Đối xứng vs khóa công khai

**Đối xứng** (AES, …): chung một bí mật; tuyệt cho dữ liệu khối; tệ cho “chưa từng gặp nhau mà muốn nói an toàn.”

**Khóa công khai** (DH 1976; RSA 1978; ECC sau đó): công khai một khóa, giữ bí mật một khóa. Bất kỳ ai mã hóa tới bạn; chỉ bạn giải. Chữ ký đảo trực giác: chỉ bạn ký; ai cũng kiểm.

**Hàm một chiều có cửa sập:** dễ tính, khó đảo không có cấu trúc bí mật, dễ đảo với cửa sập. **Kerckhoffs:** an ninh dựa trên bí mật khóa, không giấu thuật toán.

---

## 3. RSA: phân tích thừa số như cửa sập

1. Chọn nguyên tố bí mật $$p,q$$; công bố $$n=pq$$.  
2. $$\varphi(n)=(p-1)(q-1)$$ bí mật.  
3. Chọn $$e$$ nguyên tố cùng nhau với $$\varphi(n)$$.  
4. $$d$$ với $$ed\equiv 1\pmod{\varphi(n)}$$.  
5. Mã: $$c\equiv m^e\pmod n$$; giải: $$m\equiv c^d\pmod n$$.

**Cơ chế một câu.**  
*Mã hóa là lũy thừa modulo với số mũ công khai; giải mã cần số mũ nghịch đảo—dễ nếu biết $$\varphi(n)$$ (nên biết $$p,q$$), được tin là khó nếu chỉ biết $$n$$.*

**Giả định (không chính thức).** Phân tích semiprime lớn bất khả thi ở cỡ khuyến nghị. **Padding** (OAEP, PSS) bắt buộc—RSA textbook thô không triển khai được. Vệ sinh tham số, side channel, RNG xấu đã phá RSA “đúng toán” ngoài đời.

---

## 4. Diffie–Hellman và log rời rạc

- Alice bí mật $$a$$, gửi $$A=g^a$$.  
- Bob bí mật $$b$$, gửi $$B=g^b$$.  
- Bí mật chung $$g^{ab}$$.

**DLP:** từ $$g,g^a$$ khôi phục $$a$$. Nếu DLP khó, kẻ nghe lén không tính được $$g^{ab}$$ chỉ từ bản công khai (dưới giả định CDH/DDH được phát biểu cẩn thận).

**Cơ chế.** *Truyền công khai là lũy thừa nhóm; bí mật chung là tổ hợp song tuyến trong số mũ—chỉ bên biết ít nhất một số mũ thấy được.*

---

## 5. Mật mã đường cong elliptic (ECC)

Đường cong elliptic trên trường hữu hạn (dạng Weierstrass đơn giản $$y^2=x^3+Ax+B$$) mang cấu trúc **nhóm** điểm với phép dây–tiếp tuyến. Nhân vô hướng $$P\mapsto aP$$ dễ; đảo (ECDLP) được tin khó trên đường cong chọn tốt. Cùng mẫu DH, khóa nhỏ hơn cho an ninh cổ điển tương đương khuyến nghị. TLS điện thoại gần như chắc dùng ECDHE.

**Cơ chế.** *ECC chuyển DH từ nhóm nhân của trường hữu hạn sang nhóm điểm trên đường cong—cùng hình cửa sập, mật độ an ninh theo bit cao hơn.*

---

## 6. Chữ ký, chứng chỉ, mã hóa lai

Chữ ký (RSA-PSS, ECDSA, EdDSA, …); PKI gắn khóa với danh tính; **hybrid**: khóa công khai thiết lập khóa phiên đối xứng, rồi AES cho bulk; authenticated encryption chống sửa lặng. Lý thuyết số ở bắt tay; kỹ thuật–kinh tế–luật ở mô hình tin cậy. Cả hai có thể hỏng mà giả định độ khó vẫn “đúng.”

---

## 7. Văn hóa độ khó: mật mã gặp độ phức tạp

Cần bài toán: dễ sinh instance, dễ giải với cửa sập, khó cho đối thủ trên instance **điển hình** (trung bình, không chỉ worst-case). Họ hàng nhưng không trùng [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): NP-đầy đủ là worst-case; crypto muốn độ khó trung bình dùng được.

---

## 8. Bóng lượng tử và mật mã hậu lượng tử

**Shor** (lượng tử) phân tích thừa số và log rời rạc đa thức—đe dọa RSA/DH/ECC nếu máy lượng tử lớn tin cậy ra đời. **PQC** chuyển giả định sang bài không biết sụp vì Shor: **lưới** (LWE), **mã**, **chữ ký hash**, đa thức/isogeny (luôn bị cryptanalysis—một số isogeny đã đổ). Chuẩn hóa NIST (ML-KEM, ML-DSA, …) là mặt thể chế. Xem [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

**Cơ chế chuyển.** *Khóa công khai cổ điển khai thác one-way số học trên nhóm nhân và elliptic; PQC khai thác độ khó lưới cao chiều—vẫn toán thuần nuôi hạ tầng.*

---

## 9. Vì sao lý thuyết số “sẵn sàng”

Tính nguyên tố, nghịch đảo modulo, cấu trúc nhóm và ám ảnh số nguyên tố có trước thương mại điện tử. Khi cần cửa sập, hộp dụng cụ đã trên kệ. Di cư pure→applied không đòi đổi tên môn; đòi nhận ra **độ khó tính toán giả định** cũng quý như công thức đóng.

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
