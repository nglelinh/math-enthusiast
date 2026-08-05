---
layout: post
title: "Mật mã khóa công khai: Diffie–Hellman và RSA"
chapter: '09'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

Trước giữa thập niên 1970, mật mã thực dụng chủ yếu là **đối xứng**: hai bên chia sẻ sẵn một bí mật. Vấn đề phân phối khóa—làm sao hai người chưa từng gặp nhau thỏa thuận bí mật trên kênh bị nghe lén—trông như nghịch lý. **Whitfield Diffie** và **Martin Hellman** (ý tưởng công khai 1976; Turing Award **2015** cho công trình khóa công khai của họ) — song song lịch sử với công việc mật mã Anh tại GCHQ trước đó, không phải “đồng giải” Turing với GCHQ — cùng **Ron Rivest, Adi Shamir, Leonard Adleman** với **RSA** (1977/78; Turing Award **2002**), biến nghịch lý thành **giao thức toán**: công khai một phần thông tin, giữ cửa sập, dựa trên bài toán số học được tin là khó.

Bài này là chân dung **cơ chế** Diffie–Hellman và RSA trong khung chương Turing—bổ sung flagship [Lý thuyết số → mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) bằng góc giải thưởng và giả định độ khó. Liên kết: [Cook–Karp]({{ site.baseurl }}/contents/vi/chapter09/09_04_Cook_Karp_NP/), [Goldwasser–Micali]({{ site.baseurl }}/contents/vi/chapter09/09_07_Goldwasser_Micali/), [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích **vấn đề phân phối khóa** và vì sao đối xứng đơn thuần không đủ cho internet mở.  
- Mô tả **Diffie–Hellman**: từ $$g^a,g^b$$ công khai tới bí mật $$g^{ab}$$; nêu DLP/CDH.  
- Mô tả **RSA**: $$n=pq$$, số mũ $$e,d$$, mã $$c\equiv m^e\pmod n$$; cửa sập $$\varphi(n)$$.  
- Phân biệt giả định (factoring, DLP) với NP-đầy đủ worst-case.  
- Nêu vai trò **padding**, độ dài khóa, và bóng **Shor / hậu lượng tử** ở mức biết đọc.  
- Tránh nhầm: “RSA = nhân hai nguyên tố là đủ,” “công khai ⇒ ai cũng giải mã được,” “khóa công khai tuyệt đối an toàn.”

**Tiên quyết.** Đồng dư, nguyên tố, lũy thừa; ý nhóm nhân modulo $$p$$. Đã đọc ch.03 mật mã thì lặp cơ chế có chủ đích để gắn Turing Award. Euclid gcd và nghịch đảo modulo là bạn đồng hành.

---

## 1. Đối xứng, Kerckhoffs, và nghịch lý kênh công cộng

**Mã đối xứng** (AES, …): cùng khóa $$k$$ để mã và giải. Hiệu quả tuyệt vời cho luồng dữ liệu lớn. Yếu điểm kiến trúc: phải có $$k$$ chung **trước** khi nói chuyện an toàn. Trên mạng mở, gửi $$k$$ thô qua kênh bị nghe lén là tự sát mật mã.

**Nguyên lý Kerckhoffs:** an ninh dựa trên bí mật **khóa**, không dựa trên giấu thuật toán. Thuật toán công khai, peer-reviewed; chỉ key material là bí mật.

**Khóa công khai** tách cặp: khóa **công khai** $$pk$$ mọi người dùng để mã hóa (hoặc kiểm chữ ký); khóa **bí mật** $$sk$$ chỉ chủ sở hữu giữ để giải (hoặc ký). Cần **hàm một chiều có cửa sập**: dễ tính theo một chiều, khó đảo không có $$sk$$, dễ đảo với $$sk$$.

---

## 2. Diffie–Hellman: thỏa thuận khóa trên kênh nghe lén

Cố định nhóm cyclic (phiên bản cổ điển: nhân modulo nguyên tố lớn $$p$$) với phần tử sinh $$g$$. Alice chọn bí mật $$a$$, gửi $$A = g^a$$. Bob chọn bí mật $$b$$, gửi $$B = g^b$$. Cả hai tính

$$
K = B^a = (g^b)^a = g^{ab} = (g^a)^b = A^b.
$$

Kẻ nghe lén thấy $$g,g^a,g^b$$ (và $$p$$). **Bài toán log rời rạc (DLP):** cho $$g,g^a$$, tìm $$a$$. **Computational Diffie–Hellman (CDH):** cho $$g,g^a,g^b$$, tìm $$g^{ab}$$. Nếu CDH khó, kẻ nghe lén thụ động không tính được $$K$$ chỉ từ bản công khai (dưới mô hình chuẩn).

**Cơ chế một câu.** *Lũy thừa nhóm dễ; “trộn” hai số mũ thành bí mật chung mà không gửi số mũ—kẻ ngoài thiếu ít nhất một số mũ.*

**Lưu ý giao thức.** DH thuần dễ bị tấn công man-in-the-middle nếu không **xác thực**. Thực tế TLS dùng chữ ký/chứng chỉ (RSA hoặc ECDSA/EdDSA) neo danh tính, rồi ECDHE thỏa thuận khóa phiên. An ninh là **hệ** giao thức, không chỉ một công thức đẹp.

---

## 3. RSA: nhân nguyên tố làm cửa sập

1. Chọn nguyên tố bí mật $$p,q$$ đủ lớn; công bố modulus $$n=pq$$.  
2. Tính $$\varphi(n)=(p-1)(q-1)$$ (bí mật; tương đương biết thừa số trong bối cảnh này).  
3. Chọn $$e$$ với $$\gcd(e,\varphi(n))=1$$ (thường $$65537$$).  
4. Tìm $$d$$ sao cho $$ed\equiv 1\pmod{\varphi(n)}$$ (Euclid mở rộng).  
5. Công khai $$(n,e)$$; bí mật $$d$$ (và $$p,q$$).  
6. Mã (textbook): $$c \equiv m^e \pmod n$$. Giải: $$m \equiv c^d \pmod n$$.

Tính đúng dựa trên số học Euler/Carmichael: số mũ nhân modulo $$\lambda(n)$$ triệt tiêu. **Giả định an ninh thô:** từ $$n$$ khó khôi phục $$p,q$$ (factoring semiprime lớn); và các bài RSA đảo (tính căn $$e$$-th modulo $$n$$) khó khi không biết cửa sập.

**Cơ chế một câu.** *Lũy thừa công khai dễ; nghịch đảo số mũ dễ nếu biết $$\varphi(n)$$, được tin là khó nếu chỉ biết $$n$$.*

**Padding bắt buộc.** RSA textbook không an toàn triển khai: cần OAEP (mã hóa) / PSS (chữ ký) và RNG chất lượng. Side channel (timing, power), modulus dùng chung xấu, và tham số yếu đã phá hệ “đúng công thức” ngoài đời.

---

## 4. ECC: cùng hình, nhóm khác

**Mật mã đường cong elliptic** chuyển DH/DSA sang nhóm điểm trên đường cong over finite field. Nhân vô hướng $$P\mapsto aP$$ dễ; ECDLP được tin khó trên đường cong chọn tốt. Khóa ngắn hơn cho mức an ninh cổ điển tương đương khuyến nghị—lý do điện thoại ưu tiên ECDHE. Cơ chế cửa sập **cùng hình** Diffie–Hellman; chỉ thay “nhóm nào.”

---

## 5. Giả định độ khó: không phải NP-đầy đủ tự động

Factoring và DLP nằm trong **NP ∩ coNP** dưới các formal hóa tự nhiên; chúng **không** được biết là NP-đầy đủ, và cộng đồng **không kỳ vọng** chúng NP-đầy đủ (vì hệ quả sụp đổ cấu trúc lớp). Mật mã cần:

- độ khó **average-case** trên phân phối keygen;  
- **one-wayness** / hardcore bits;  
- đôi khi giả định mạnh hơn (DDH, RSA assumption, …).

Cook–Karp cho ngôn ngữ worst-case tổ hợp; Diffie–Hellman–RSA cho **mỏ số học cụ thể**. Rút gọn từ worst-case lattice sang average-case LWE là thành tựu hiếm và quý—nền PQC hiện đại—không phải chuyện RSA 1978 đã có.

---

## 6. Chữ ký, PKI, và internet

**Chữ ký số** đảo trực giác mã hóa: ký bằng $$sk$$, kiểm bằng $$pk$$. RSA và các scheme dựa trên DLP/ECDSA cung cấp xác thực phần mềm, chứng chỉ TLS, và neo tin cậy (PKI)—dù PKI mang thêm bài toán thể chế (CA, revoke, UX).

Mỗi lần trình duyệt hiển thị khóa: thường là bắt tay (EC)DHE + chữ ký chứng chỉ + mã đối xứng phiên (AES-GCM, …). Toán khóa công khai giải **bootstrap tin cậy và khóa**; đối xứng gánh **throughput**.

---

## 7. Lượng tử và hậu lượng tử

Thuật toán **Shor** đặt factoring và DLP (gồm ECDLP trên nhóm dùng phổ biến) vào **BQP**—máy lượng tử đủ lớn, đủ ít lỗi sẽ phá RSA/DH/ECC cổ điển. Do đó lộ trình **PQC**: Kyber/Dilithium và họ lattice, code-based, hash-based, … Xem [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/) và [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/).

Biết đọc: “RSA vỡ ngày mai trên laptop” là sai; “RSA không phải primitive vĩnh cửu trước mô hình lượng tử” là đúng. Turing Award vinh danh **paradigm khóa công khai**, không phải một modulus cụ thể vĩnh viễn.

---

## 8. Nhầm lẫn thường gặp

| Khẳng định | Chỉnh |
|------------|-------|
| “Khóa công khai ai cũng giải mã được.” | Ai cũng *mã* được tới bạn; chỉ bạn *giải*. |
| “RSA an toàn vì giấu thuật toán.” | Thuật toán công khai; an ninh ở khóa + giả định + triển khai. |
| “Factoring NP-đầy đủ.” | Không được biết; kỳ vọng không. |
| “DH đủ xác thực.” | DH thuần không chống MITM; cần chữ ký/kênh tin cậy. |
| “Số nguyên tố lớn ⇒ an toàn.” | Cần quy trình sinh đúng, modulus đủ bit, padding, side-channel hygiene. |
| “PQC chỉ là QKD.” | PQC chủ yếu là primitive tính toán cổ điển (lattice, …); QKD là kênh vật lý khác. |

---

## Bài tập

1. Viết protocol DH 5 bước (chọn nhóm, $$a$$, $$A$$, $$b$$, $$B$$, $$K$$) và khoanh chỗ kẻ nghe lén nhìn thấy gì.  
2. Với $$p=23$$, $$g=5$$, $$a=6$$, $$b=15$$ (ví dụ đồ chơi): tính $$A,B,K$$ modulo $$23$$.  
3. RSA đồ chơi: $$p=5$$, $$q=11$$, $$n=55$$, chọn $$e=3$$, tìm $$d$$, mã $$m=7$$. (Chỉ đồ chơi—không phải an ninh.)  
4. Giải thích ≤100 từ vì sao $$\gcd(e,\varphi(n))=1$$ cần cho sự tồn tại $$d$$.  
5. So sánh 1 đoạn: DLP vs factoring—mỗi cái đỡ primitive nào (DH vs RSA).  
6. **≤250 từ:** Vì sao NP-đầy đủ của SAT không tự cho bạn hệ RSA.  
7. Liệt kê ba tầng an ninh: toán primitive / giao thức / triển khai—mỗi tầng một rủi ro.  
8. Studio: đọc một citation Turing liên quan (RSA 2002 hoặc Diffie–Hellman 2015) và gạch chân danh từ toán.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/public-key-crypto/`.

**Khẩu hiệu từ gói nghiên cứu**

- Diffie–Hellman 2015; RSA 2002; khóa công khai.

**Thứ tự xem gợi ý**


**Cổng chính thức / tài liệu**

- Diffie Turing: https://amturing.acm.org/award_winners/diffie_8371646.cfm  
- Hellman Turing: https://amturing.acm.org/award_winners/hellman_4055781.cfm  
- Rivest Turing: https://amturing.acm.org/award_winners/rivest_1562803.cfm  
- Shamir Turing: https://amturing.acm.org/award_winners/shamir_2327856.cfm  
- Adleman Turing: https://amturing.acm.org/award_winners/adleman_7308544.cfm  

Danh mục URL đầy đủ: `research/video-research/public-key-crypto/references.md`.

## Tài liệu


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/public-key-crypto/references.md`.

1. Diffie Turing — https://amturing.acm.org/award_winners/diffie_8371646.cfm  
2. Hellman Turing — https://amturing.acm.org/award_winners/hellman_4055781.cfm  
3. Rivest Turing — https://amturing.acm.org/award_winners/rivest_1562803.cfm  
4. Shamir Turing — https://amturing.acm.org/award_winners/shamir_2327856.cfm  
5. Adleman Turing — https://amturing.acm.org/award_winners/adleman_7308544.cfm  
6. Wikipedia — Public-key cryptography — https://en.wikipedia.org/wiki/Public-key_cryptography  
7. Wikipedia — Diffie–Hellman key exchange — https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange  
8. Wikipedia — RSA (cryptosystem) — https://en.wikipedia.org/wiki/RSA_(cryptosystem)  
9. Original DH paper culture (IEEE) — https://ee.stanford.edu/~hellman/publications/24.pdf  
10. Thư mục gói: `research/video-research/public-key-crypto/`.

1. Diffie, W., & Hellman, M. (1976). New directions in cryptography. *IEEE Trans. Inf. Theory*.  
2. Rivest, R., Shamir, A., & Adleman, L. (1978). A method for obtaining digital signatures and public-key cryptosystems. *Comm. ACM*.  
3. ACM Turing citations: RSA (2002); Diffie & Hellman (2015).  
4. [Mật mã ch.03]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/); [PQC ch.06]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/); [Goldwasser–Micali]({{ site.baseurl }}/contents/vi/chapter09/09_07_Goldwasser_Micali/).

---

## Hướng đi tiếp

- Làm lại cơ chế RSA/DH bằng lời của bạn **không nhìn** công thức—rồi đối chiếu.  
- Tiếp: [Goldwasser, Micali và nền tảng mật mã hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_07_Goldwasser_Micali/)—semantic security, quadratic residuosity, zero-knowledge.  
- Đọc một đoạn TLS 1.3 overview (mức sơ đồ) để thấy DH+chữ ký+đối xứng ghép thế nào.

---

## Paradigm hơn là modulus

Di sản Turing Award ở đây là **paradigm**: công khai hóa khả năng mã hóa/thỏa thuận mà không công khai cửa sập; biến giả định số học thành primitive mạng. Modulus 2048-bit cụ thể sẽ lỗi thời; ý tưởng cặp khóa và trao đổi khóa trên kênh công cộng thì đã viết lại kiến trúc tin cậy toàn cầu.

Trong essay seminar, ưu tiên câu *cơ chế một bước đúng* hơn khẩu hiệu “lý thuyết số dùng trong mật mã.” Hỏi: gì dễ? gì khó? cửa sập là gì? giả định tên gì? tấn công bị loại là thụ động hay chủ động? Bốn câu đó tách người học cơ chế khỏi người thuộc tên giải thưởng.

## Lũy thừa nhanh: chi tiết Knuth gặp mật mã

Tính $$g^a\bmod p$$ bằng bình phương lặp: $$O(\log a)$$ nhân modulo. Đây là chỗ [phân tích thuật toán]({{ site.baseurl }}/contents/vi/chapter09/09_05_Knuth_Algorithms/) gặp mật mã: primitive chỉ khả thi vì lũy thừa **poly-time** trong khi đảo (DLP) được tin không. Hiệu quả và độ khó **đi cặp**—một chiều phải chạy trên điện thoại; chiều kia phải đứng trước adversary poly-time (cổ điển).
