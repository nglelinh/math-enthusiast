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

Suốt hàng nghìn năm — từ mật mã Caesar của La Mã cổ đại cho tới cỗ máy Enigma thời Thế chiến II — mật mã học luôn vướng phải một nghịch lý tưởng chừng không thể tháo gỡ: muốn gửi thư mật cho nhau, hai người phải **gặp nhau trước** (hoặc cử giao liên xách va-li khóa) để thống nhất một chìa khóa chung. Thế nhưng trong kỷ nguyên Internet, làm sao trình duyệt của bạn có thể gửi số thẻ tín dụng an toàn tới một cửa hàng ở nửa bên kia Trái Đất mà hai bên **chưa từng gặp mặt**, trong khi mọi gói tin truyền đi đều chạy qua đường dây công cộng có kẻ nghe lén?

Giữa thập niên 1970, hai bước ngoặt toán học đã đập tan nghịch lý ấy. Năm 1976, **Whitfield Diffie** và **Martin Hellman** (Giải Turing **2015**) công bố giao thức trao đổi khóa công khai — cho phép hai người hét to các con số qua một căn phòng đầy tai mắt mà cuối cùng vẫn tính ra được một bí mật chỉ riêng hai người biết! Một năm sau, **Ron Rivest, Adi Shamir và Leonard Adleman** (Giải Turing **2002**) dựng nên hệ mật **RSA** biến phép nhân hai số nguyên tố lớn thành một chiếc ổ khóa mở công khai cho cả thế giới khóa lại, nhưng chỉ chủ nhân mới có chìa mở ra. (Lịch sử sau này mới tiết lộ các nhà mật mã ở GCHQ của Anh từng tìm ra ý tưởng tương tự trước đó vài năm nhưng phải giữ bí mật tuyệt đối; Giải Turing tôn vinh những công trình công khai đã thay đổi cả nhân loại.) Bài này bổ sung cho [Lý thuyết số và mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) góc nhìn về cơ chế cửa sập và giả định độ khó. Liên kết: [Cook–Karp]({{ site.baseurl }}/contents/vi/chapter09/09_04_Cook_Karp_NP/), [Goldwasser–Micali]({{ site.baseurl }}/contents/vi/chapter09/09_07_Goldwasser_Micali/), [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích **vấn đề phân phối khóa** và vì sao đối xứng đơn thuần không đủ cho internet mở.  
- Mô tả **Diffie–Hellman**: từ $$g^a,g^b$$ công khai tới bí mật $$g^{ab}$$; nêu DLP/CDH.  
- Mô tả **RSA**: $$n=pq$$, số mũ $$e,d$$, mã $$c\equiv m^e\pmod n$$; cửa sập $$\varphi(n)$$.  
- Phân biệt giả định (factoring, DLP) với NP-đầy đủ worst-case.  
- Nêu vai trò **padding**, độ dài khóa, và bóng **Shor / hậu lượng tử** ở mức đủ để đọc hiểu.  
- Tránh nhầm: “RSA = nhân hai nguyên tố là đủ,” “công khai ⇒ ai cũng giải mã được,” “khóa công khai tuyệt đối an toàn.”

**Tiên quyết.** Đồng dư, nguyên tố, lũy thừa; ý nhóm nhân modulo $$p$$. Nếu đã đọc phần mật mã ở ch.03 thì bài này nhắc lại cơ chế có chủ ý để gắn với giải Turing. Euclid gcd và nghịch đảo modulo là bạn đồng hành.

---

## Bản đồ kiến thức nền: Mật mã học khóa công khai và Lý thuyết số tính toán là gì, nghiên cứu những gì?

Đằng sau biểu tượng ổ khóa màu xanh trên thanh địa chỉ trình duyệt là một sự đảo ngược tư duy ngoạn mục của **Lý thuyết số tính toán (Computational Number Theory)** và **Mật mã học khóa công khai (Public-Key Cryptography)**. Thông thường trong khoa học máy tính, bài toán *khó* là kẻ thù cần tiêu diệt. Nhưng trong mật mã học, **sự bất đối xứng về độ phức tạp** — dễ làm theo chiều xuôi, cực khó làm theo chiều ngược — lại là nguồn tài nguyên quý giá nhất!

Toàn bộ kiến trúc khóa công khai xoay quanh khái niệm **hàm một chiều có cửa sập (trapdoor one-way function)** — giống như việc pha trộn hai thùng sơn hay đập vỡ một chiếc bình gốm: làm xuôi mất một giây, làm ngược gần như bất khả thi *trừ khi* bạn nắm trong tay một "cửa sập bí mật". Có hai mỏ toán học kinh điển tạo nên kỷ nguyên đầu tiên:
1. **Nhóm nhân modulo số nguyên tố $$p$$ (Diffie–Hellman):** tính lũy thừa $$g^a \bmod p$$ cực nhanh (chỉ tốn $$O(\log a)$$ phép nhân nhờ bình phương lặp), nhưng cho trước $$g^a \bmod p$$ mà tìm ngược lại số mũ $$a$$ (**bài toán logarit rời rạc — DLP**) lại cực kỳ khó khi $$p$$ có vài nghìn bit.
2. **Phân tích thừa số nguyên tố (RSA):** nhân hai số nguyên tố 1024-bit $$p \times q = n$$ chỉ mất vài micro-giây, nhưng từ $$n$$ tách ngược ra $$p, q$$ đòi hỏi những thuật toán sàng trường số khổng lồ vượt quá khả năng máy tính cổ điển hiện nay.

Hãy xem một **ví dụ đồ chơi bằng số thật** cho Diffie–Hellman để cảm nhận phép màu trong 10 giây: chọn công khai $$p = 23$$, $$g = 5$$. Alice bí mật chọn $$a = 6$$, gửi công khai $$A = 5^6 \bmod 23 = 8$$. Bob bí mật chọn $$b = 15$$, gửi công khai $$B = 5^{15} \bmod 23 = 19$$. Alice tính $$19^6 \bmod 23 = 2$$; Bob tính $$8^{15} \bmod 23 = 2$$. Cả hai cùng thu được bí mật chung $$K = 2$$ mà chưa từng gửi $$a, b$$ hay $$2$$ qua mạng!

---

## 1. Đối xứng, Kerckhoffs và nghịch lý kênh công cộng

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

Ví dụ đồ chơi: chọn $$p=5, q=11 \implies n=55$$ và $$\varphi(55) = 4\cdot 10 = 40$$. Chọn $$e=3$$, ta tìm được $$d=27$$ (vì $$3\cdot 27 = 81 \equiv 1 \pmod{40}$$). Để mã hóa thông điệp $$m=7$$, người gửi tính $$c = 7^3 \bmod 55 = 343 \bmod 55 = 13$$. Người nhận dùng khóa bí mật $$d=27$$ tính $$13^{27} \bmod 55 = 7$$ — khôi phục chính xác bản rõ!

Tính đúng dựa trên số học Euler/Carmichael: số mũ nhân modulo $$\lambda(n)$$ triệt tiêu. **Giả định an ninh thô:** từ $$n$$ khó khôi phục $$p,q$$ (factoring semiprime lớn); và các bài RSA đảo (tính căn $$e$$-th modulo $$n$$) khó khi không biết cửa sập.

**Cơ chế một câu.** *Lũy thừa công khai dễ; nghịch đảo số mũ dễ nếu biết $$\varphi(n)$$, được tin là khó nếu chỉ biết $$n$$.*

**Padding bắt buộc.** RSA textbook không an toàn triển khai: cần OAEP (mã hóa) / PSS (chữ ký) và RNG chất lượng. Side channel (timing, power), modulus dùng chung xấu, và tham số yếu đã phá hệ “đúng công thức” ngoài đời.

---

## 4. ECC: cùng hình, nhóm khác

**Mật mã đường cong elliptic** chuyển DH/DSA sang nhóm điểm trên đường cong over finite field. Nhân vô hướng $$P\mapsto aP$$ dễ; ECDLP được tin khó trên đường cong chọn tốt. Khóa ngắn hơn cho mức an ninh cổ điển tương đương khuyến nghị (chẳng hạn khóa ECC 256-bit tương đương khóa RSA 3072-bit)—lý do điện thoại ưu tiên ECDHE. Cơ chế cửa sập **cùng hình** Diffie–Hellman; chỉ thay “nhóm nào.”

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

Thuật toán **Shor** đặt factoring và DLP (gồm ECDLP trên nhóm dùng phổ biến) vào **BQP**—máy lượng tử đủ lớn, đủ ít lỗi sẽ phá RSA/DH/ECC cổ điển. Do đó lộ trình **PQC**: Kyber/Dilithium (nay được chuẩn hóa thành ML-KEM/ML-DSA) và họ lattice, code-based, hash-based, … Xem [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/) và [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/).

Cần phân biệt: “RSA vỡ ngày mai trên laptop” là sai; “RSA không phải primitive vĩnh cửu trước mô hình lượng tử” là đúng. Giải Turing vinh danh **mô hình khóa công khai**, không phải một modulus cụ thể vĩnh viễn.

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

1. Viết giao thức DH theo từng bước (chọn nhóm, $$a$$, $$A$$, $$b$$, $$B$$, $$K$$) và khoanh chỗ kẻ nghe lén nhìn thấy gì.  
2. Với $$p=23$$, $$g=5$$, $$a=6$$, $$b=15$$ (ví dụ đồ chơi): tính $$A,B,K$$ modulo $$23$$.  
3. RSA đồ chơi: $$p=5$$, $$q=11$$, $$n=55$$, chọn $$e=3$$, tìm $$d$$, mã $$m=7$$. (Chỉ đồ chơi—không phải an ninh.)  
4. Giải thích ≤100 từ vì sao $$\gcd(e,\varphi(n))=1$$ cần cho sự tồn tại $$d$$.  
5. So sánh 1 đoạn: DLP vs factoring—mỗi cái đỡ primitive nào (DH vs RSA).  
6. **≤250 từ:** Vì sao NP-đầy đủ của SAT không tự cho bạn hệ RSA.  
7. Liệt kê ba tầng an ninh: toán primitive / giao thức / triển khai—mỗi tầng một rủi ro.  
8. Đọc một citation Turing liên quan (RSA 2002 hoặc Diffie–Hellman 2015) và gạch chân danh từ toán.

---


## Video và tài liệu

Các video gợi ý nằm ở phần *Video tham khảo* cuối bài. Hãy dùng video để làm quen với bối cảnh, không dùng thay cho chứng minh.

## Tài liệu tham khảo trực tuyến


1. Trang giải Turing của Diffie — https://amturing.acm.org/award_winners/diffie_8371646.cfm  
2. Trang giải Turing của Hellman — https://amturing.acm.org/award_winners/hellman_4055781.cfm  
3. Trang giải Turing của Rivest — https://amturing.acm.org/award_winners/rivest_1562803.cfm  
4. Trang giải Turing của Shamir — https://amturing.acm.org/award_winners/shamir_2327856.cfm  
5. Trang giải Turing của Adleman — https://amturing.acm.org/award_winners/adleman_7308544.cfm  
6. Wikipedia — Public-key cryptography — https://en.wikipedia.org/wiki/Public-key_cryptography  
7. Wikipedia — Diffie–Hellman key exchange — https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange  
8. Wikipedia — RSA (cryptosystem) — https://en.wikipedia.org/wiki/RSA_(cryptosystem)  
9. Bài báo gốc của Diffie–Hellman — https://ee.stanford.edu/~hellman/publications/24.pdf  

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

## Một mô hình tư duy, không phải một con số cụ thể

Di sản được giải Turing ghi nhận ở đây là một **mô hình tư duy**: công khai hóa khả năng mã hóa/thỏa thuận mà không công khai cửa sập; biến giả định số học thành primitive mạng. Modulus 2048-bit cụ thể sẽ lỗi thời; ý tưởng cặp khóa và trao đổi khóa trên kênh công cộng thì đã viết lại kiến trúc tin cậy toàn cầu.

Khi viết bài luận, hãy ưu tiên câu *cơ chế một bước đúng* hơn khẩu hiệu “lý thuyết số dùng trong mật mã.” Hỏi: gì dễ? gì khó? cửa sập là gì? giả định tên gì? tấn công bị loại là thụ động hay chủ động? Bốn câu đó tách người học cơ chế khỏi người thuộc tên giải thưởng.

## Lũy thừa nhanh: chi tiết Knuth gặp mật mã

Tính $$g^a\bmod p$$ bằng bình phương lặp: $$O(\log a)$$ nhân modulo. Đây là chỗ [phân tích thuật toán]({{ site.baseurl }}/contents/vi/chapter09/09_05_Knuth_Algorithms/) gặp mật mã: primitive chỉ khả thi vì lũy thừa **poly-time** trong khi đảo (DLP) được tin không. Hiệu quả và độ khó **đi cặp**—một chiều phải chạy trên điện thoại; chiều kia phải đứng trước adversary poly-time (cổ điển).

## Video tham khảo

- **Xem trước** — [8.Hệ mật RSA_Định nghĩa và ví dụ](https://www.youtube.com/watch?v=QEoRfrSKciI) — Bùi Thị Thùy _CNTT, tiếng Việt. Xem trước: định nghĩa và ví dụ RSA bằng tiếng Việt, để đối chiếu với phần trapdoor và số học mô-đun trong bài.
- [Secret Key Exchange (Diffie-Hellman) - Computerphile](https://www.youtube.com/watch?v=NmM9HA2MQGI) — Computerphile, tiếng Anh. Xem sau khi đã nắm ý chính.
- [Diffie Hellman -the Mathematics bit- Computerphile](https://www.youtube.com/watch?v=Yjrfm_oRO0w) — Computerphile, tiếng Anh. Góc nhìn bổ sung.
