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

Năm 1940, nhà toán học lừng danh G. H. Hardy viết trong cuốn tự truyện *A Mathematician's Apology* một lời tự hào nổi tiếng: ông hạnh phúc vì cả đời mình chỉ nghiên cứu lý thuyết số — một nhánh toán học "thuần khiết và hoàn toàn vô dụng", sẽ chẳng bao giờ bị mang ra dùng trong chiến tranh hay thương mại. Thế nhưng lịch sử lại có khiếu hài hước kỳ lạ: chỉ 36 năm sau, chính những định lý cổ điển về số nguyên tố và phép chia lấy dư mà Hardy tôn thờ lại biến thành ổ khóa vạn năng bảo vệ toàn bộ mạng Internet.

Mỗi lần bạn mở trình duyệt thấy biểu tượng ổ khóa HTTPS, chuyển khoản trên ứng dụng ngân hàng, hay tải một bản cập nhật phần mềm, điện thoại của bạn đang âm thầm chạy hàng loạt phép tính số học đồng dư, kiểm tra số nguyên tố và nhân điểm trên đường cong elliptic.

Đây là **bài trọng tâm của Chương 3**, đi theo một chuỗi cơ chế rõ ràng từ bảng đen đến hạ tầng bảo mật toàn cầu:

**số học đồng dư → hàm cửa sập → mật mã khóa công khai (RSA, Diffie–Hellman, ECC) → các giao thức Internet thực tế → mối đe dọa lượng tử và mật mã hậu lượng tử dựa trên lưới.**

**Lộ trình:** bản đồ lý thuyết số & mật mã học → đồng dư → mật mã đối xứng và khóa công khai → RSA → Diffie–Hellman → ECC → chữ ký, chứng chỉ, mã hóa lai → độ khó tính toán → mật mã hậu lượng tử → nhầm lẫn thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tính và hiểu ý nghĩa của $$a\equiv b\pmod n$$; giải thích cách lũy thừa nhanh theo modulo.
- Giải thích **ý tưởng khóa công khai**: tách việc mã hóa khỏi việc giải mã nhờ một cửa sập.
- Trình bày **cơ chế RSA** ở mức $$n=pq$$, các số mũ $$e,d$$, và giả định về độ khó của bài toán phân tích thừa số.
- Mô tả **Diffie–Hellman** như cách hai bên cùng tính được $$g^{ab}$$ từ các giá trị công khai $$g^a,g^b$$.
- Giải thích vì sao **đường cong elliptic** giúp rút ngắn khóa, và vì sao **mật mã hậu lượng tử** chuyển sang lưới, mã sửa sai và hàm băm.
- Tránh các nhầm lẫn: RSA không chỉ là "nhân hai số nguyên tố"; độ an toàn đến từ độ khó tính toán cộng với kỹ thuật triển khai; mật mã hậu lượng tử (PQC) không phải chỉ là phân phối khóa lượng tử (QKD).

**Kiến thức nền.** Số nguyên, số nguyên tố, lũy thừa.

**Liên kết.** [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/).

---

## Bản đồ kiến thức nền: Lý thuyết số và mật mã học hiện đại là gì, nghiên cứu những gì?

Thoạt nhìn, **lý thuyết số (number theory)** nghe có vẻ sơ cấp vì nó chỉ nghiên cứu các số nguyên $$1, 2, 3, \dots$$ — thứ trẻ em tiểu học đã biết. Nhưng càng đi sâu, các nhà toán học càng phát hiện ra cấu trúc của số nguyên tố ẩn chứa những quy luật sâu thẳm bậc nhất của toàn bộ toán học. Ở tầm đại học, lý thuyết số không chỉ dừng ở phép chia hết mà còn gắn chặt với **đại số trừu tượng** (nhóm, vành, trường hữu hạn) và **hình học đại số** (đường cong elliptic).

Trong khi đó, **mật mã học hiện đại (modern cryptography)** không còn là nghệ thuật "chế ra bộ mã bí mật rồi cầu mong kẻ địch không đoán ra". Nó là một ngành khoa học toán học chặt chẽ nghiên cứu cách xây dựng **sự bất đối xứng có kiểm soát**: những bài toán mà làm theo chiều xuôi chỉ mất vài mili-giây trên điện thoại, nhưng làm theo chiều ngược lại phải tốn hàng tỷ năm ngay cả với siêu máy tính mạnh nhất — trừ khi bạn nắm trong tay một mảnh thông tin bí mật gọi là **cửa sập (trapdoor)**.

Lý thuyết số vô tình cung cấp đúng kho báu các bài toán bất đối xứng đó: nhân hai số nguyên tố thì dễ nhưng tách ngược lại thì cực khó; tính lũy thừa trong nhóm hữu hạn thì nhanh nhưng tìm lại số mũ (logarit rời rạc) thì cực khó.

---

## 1. Số học đồng dư: tính toán với số dư

Cố định một số nguyên dương $$n$$ (gọi là **modulo**). Ta viết

$$
a \equiv b \pmod{n}
$$

khi $$n$$ chia hết $$a-b$$, tức là $$a$$ và $$b$$ có cùng số dư khi chia cho $$n$$.

Tính toán **theo modulo $$n$$** giống như xem một chiếc đồng hồ có $$n$$ vạch: sau $$n-1$$ thì quay về $$0$$. Điểm kỳ diệu là phép cộng và phép nhân vẫn tương thích hoàn hảo với đồng dư:

$$
a\equiv a',\quad b\equiv b' \pmod{n} \implies a+b\equiv a'+b',\quad ab\equiv a'b' \pmod{n}.
$$

Vành $$\mathbb{Z}/n\mathbb{Z}$$ là cấu trúc đại số cơ bản trong mật mã. Khi $$n=p$$ là số nguyên tố, mọi số dư khác 0 đều có nghịch đảo theo phép nhân, nên $$\mathbb{Z}/p\mathbb{Z}$$ là một **trường hữu hạn** $$\mathbb{F}_p$$. Nhờ đó ta có thể chia và làm đại số tuyến tính gọn gàng không hề có sai số làm tròn (AES và đường cong elliptic đều chạy trên các trường hữu hạn).

**Lũy thừa nhanh (bình phương liên tiếp).** Muốn tính $$3^{13} \bmod 17$$, bạn không cần nhân 12 lần. Viết $$13 = 8 + 4 + 1$$ (nhị phân `1101`), rồi bình phương liên tiếp:
- $$3^1 \equiv 3$$
- $$3^2 \equiv 9$$
- $$3^4 \equiv 9^2 = 81 \equiv 13 \pmod{17}$$
- $$3^8 \equiv 13^2 = 169 \equiv 16 \equiv -1 \pmod{17}$$
- Ghép lại: $$3^{13} = 3^8 \cdot 3^4 \cdot 3^1 \equiv (-1)\cdot 13 \cdot 3 = -39 \equiv 12 \pmod{17}$$.

Với số mũ $$e$$ có 2.048 bit, phương pháp này chỉ cần khoảng $$O(\log e)$$ — vài nghìn phép nhân, chạy trong chưa tới 1 mili-giây! Ngược lại, biết $$3^x \equiv 12 \pmod{17}$$ mà tìm lại $$x$$ (bài toán *logarit rời rạc*) lại cực kỳ khó khi modulo dài hàng nghìn bit. Sự bất đối xứng cực đoan này chính là nhiên liệu của mật mã khóa công khai.

**Định lý Fermat và Euler.** Nếu $$p$$ là số nguyên tố và $$p\nmid a$$ thì $$a^{p-1}\equiv 1\pmod p$$ (định lý Fermat nhỏ). Tổng quát hơn, định lý Euler dùng hàm $$\varphi(n)$$, số các số nguyên dương nhỏ hơn $$n$$ và nguyên tố cùng nhau với $$n$$: $$a^{\varphi(n)}\equiv 1\pmod n$$ khi $$\gcd(a,n)=1$$. Tính đúng đắn của RSA dựa vào việc số mũ tự "triệt tiêu" theo chu kỳ $$\varphi(n)$$ như vậy.

**Thuật toán Euclid mở rộng** tìm ước chung lớn nhất và nghịch đảo theo modulo trong thời gian logarit — một kết quả 2.300 năm tuổi trở thành hàm con thiết yếu trong mọi thư viện bảo mật thế kỷ XXI.

---

## 2. Mật mã đối xứng và mật mã khóa công khai

**Mật mã đối xứng:** Alice và Bob có chung một khóa bí mật từ trước; mã hóa và giải mã dùng cùng một khóa (AES-GCM, ChaCha20-Poly1305…). Cách này siêu nhanh, thích hợp mã hóa hàng gigabyte dữ liệu. Nhưng nó vướng phải **bài toán phân phối khóa**: *nếu bạn lần đầu mua hàng trên một trang web ở nửa kia Trái Đất và toàn bộ đường truyền Internet có thể bị nghe lén, làm sao hai bên thống nhất được khóa bí mật chung?*

**Mật mã khóa công khai** (Diffie–Hellman 1976; RSA 1978; sau này là đường cong elliptic) giải quyết ngoạn mục bài toán đó: mỗi người công bố một **khóa công khai** (giống như một chiếc ổ khóa bấm đang mở, ai cũng lấy dùng được) và giữ riêng **khóa bí mật** (chiếc chìa duy nhất mở được ổ khóa ấy). Ai cũng có thể khóa tin nhắn gửi cho bạn, nhưng chỉ bạn mới mở được. Chữ ký số thì đảo ngược lại: chỉ bạn mới ký được bằng khóa bí mật, còn cả thế giới đều kiểm tra được bằng khóa công khai của bạn.

Ý tưởng toán học cốt lõi là **hàm một chiều có cửa sập**: dễ tính xuôi, bất khả thi tính ngược nếu chỉ biết thông tin công khai, nhưng lại dễ tính ngược nếu nắm giữ bí mật "cửa sập".

**Nguyên lý Kerckhoffs.** Độ an toàn của hệ mật phải dựa hoàn toàn vào việc giữ bí mật *khóa*, tuyệt đối không dựa vào việc giấu *thuật toán*. Mọi hệ mật đáng tin cậy ngày nay đều công khai mã nguồn để hàng nghìn chuyên gia toàn cầu kiểm chứng.

---

## 3. RSA: phân tích thừa số làm cửa sập

**Thiết lập (phiên bản RSA cơ bản trong sách giáo khoa).**

1. Chọn hai số nguyên tố lớn bí mật $$p,q$$; công bố $$n=pq$$ (giữ kín $$p,q$$).  
2. Tính $$\varphi(n)=(p-1)(q-1)$$ (giữ kín).  
3. Chọn số mũ công khai $$e$$ nguyên tố cùng nhau với $$\varphi(n)$$ (trong thực tế thường chọn $$e=65537$$).  
4. Dùng thuật toán Euclid mở rộng tìm số mũ bí mật $$d$$ sao cho $$ed\equiv 1\pmod{\varphi(n)}$$.  
5. Mã hóa thông điệp (đã đổi thành số $$m < n$$): $$c\equiv m^e\pmod n$$.  
6. Giải mã: $$m\equiv c^d\pmod n$$.

**Ví dụ số trọn vẹn (RSA thu nhỏ để hiểu cơ chế).**
- Chọn $$p = 11,\ q = 13 \implies n = 143$$ và $$\varphi(n) = 10 \times 12 = 120$$.
- Chọn khóa công khai $$e = 7$$ (vì $$\gcd(7,120)=1$$). Tìm $$d$$ sao cho $$7d \equiv 1 \pmod{120}$$ → được $$d = 103$$ (kiểm tra: $$7 \times 103 = 721 = 6 \times 120 + 1$$).
- Công bố cặp $$(n, e) = (143, 7)$$; cất kỹ $$d = 103$$ (và hủy $$p, q, \varphi(n)$$).
- **Mã hóa** thông điệp $$m = 9$$: tính $$c = 9^7 \bmod 143 = 48$$. Gửi số $$48$$ qua mạng.
- **Giải mã:** tính $$48^{103} \bmod 143$$. Nhờ định lý Euler, $$48^{103} \equiv (9^7)^{103} = 9^{721} = (9^{120})^6 \cdot 9^1 \equiv 1^6 \cdot 9 = 9 \pmod{143}$$ — thu lại đúng bản gốc $$m=9$$!

**Tóm tắt trong một câu.**  
*Mã hóa là lũy thừa theo modulo với số mũ công khai; giải mã cần số mũ nghịch đảo, và số mũ này dễ tìm nếu biết $$\varphi(n)$$ (tức là biết $$p,q$$), nhưng được tin là bất khả thi nếu chỉ biết tích $$n$$.*

**Giả định về độ khó và lưu ý thực tế.** Với $$n$$ cỡ 2048–3072 bit (hơn 600–900 chữ số thập phân), các thuật toán phân tích thừa số tốt nhất hiện nay (như Number Field Sieve) vẫn cần thời gian vượt xa tuổi vũ trụ trên máy tính cổ điển. Tuy nhiên, RSA dạng sách giáo khoa **không bao giờ** được dùng trực tiếp ngoài đời thực vì nó mang tính tất định (cùng thông điệp cho ra cùng bản mã) và nhân tính ($$E(m_1)E(m_2)=E(m_1m_2)$$). Thực tế luôn bắt buộc kèm **phần đệm ngẫu nhiên (padding)** như OAEP (cho mã hóa) hoặc PSS (cho chữ ký).

**Chọn tham số cẩn thận.** Số mũ $$e$$ nhỏ đi kèm phần đệm kém, các khóa dùng chung thừa số nguyên tố, bộ sinh số ngẫu nhiên lỗi, hay tấn công kênh kề (đo thời gian hoặc điện năng tiêu thụ của chip) đều từng phá vỡ những hệ RSA "đúng về mặt toán". Lý thuyết số cung cấp cửa sập; kỹ thuật phần mềm phải bảo vệ phần còn lại.

---

### Video ngắn: Trao đổi khóa với p = 23

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/diffie-hellman-mod23_vi.mp4"></video>
</div>

Các lũy thừa của 5 modulo 23 đi qua mọi số dư từ 1 đến 22 theo thứ tự xáo trộn. An và Bình mỗi người công bố một lũy thừa (8 và 19) mà vẫn cùng đến bí mật 2, còn kẻ nghe lén phải giải một log rời rạc. Với $$p = 23$$ việc đó dễ; với kích thước thật thì không.


### Tự tay thử: Tự chạy một lần trao đổi khóa

<div class="mex-explainer" data-mex="dh" data-lang="vi"></div>


## 4. Diffie–Hellman và logarit rời rạc

Làm sao hai người chưa từng gặp nhau có thể thống nhất một mật khẩu chung ngay giữa quảng trường đông người nghe lén? Diffie và Hellman (1976) dùng một cấu trúc cực đẹp: một nhóm hữu hạn và phần tử sinh $$g$$ công khai.

**Ví dụ số khớp với video trên ($$p=23, g=5$$):**
- An chọn bí mật $$a = 6$$, tính và gửi công khai $$A = 5^6 \bmod 23 = 8$$.  
- Bình chọn bí mật $$b = 15$$, tính và gửi công khai $$B = 5^{15} \bmod 23 = 19$$.  
- An lấy $$B$$ của Bình nâng lên mũ $$a$$: $$19^6 \bmod 23 = 2$$.  
- Bình lấy $$A$$ của An nâng lên mũ $$b$$: $$8^{15} \bmod 23 = 2$$.  
- Cả hai cùng thu được bí mật chung $$s = g^{ab} \bmod 23 = 2$$ mà chưa từng gửi $$a, b$$ hay $$2$$ ra ngoài!

**Bài toán logarit rời rạc (DLP):** kẻ nghe lén thấy rõ $$g=5, p=23, A=8, B=19$$, nhưng muốn tìm lại $$a$$ từ $$5^a \equiv 8 \pmod{23}$$ thì phải giải logarit rời rạc. Khi $$p$$ là số nguyên tố 2048–3072 bit, việc tính ngược lại là bất khả thi với máy tính cổ điển (chính xác hơn, độ an toàn gắn với giả định CDH/DDH).

**Ý chính.**  
*Các giá trị truyền công khai là lũy thừa trong nhóm; bí mật chung có số mũ là tích của hai số bí mật, nên chỉ người biết ít nhất một trong hai số mũ mới tính được.*

**Hạn chế về kích thước.** Diffie–Hellman trên trường hữu hạn $$\mathbb{F}_p^\times$$ chịu áp lực từ các thuật toán kiểu index-calculus nên phải dùng khóa rất dài (2048–3072 bit). Đó là lý do công nghệ hiện đại chuyển mạnh sang đường cong elliptic.

---

## 5. Mật mã đường cong elliptic (ECC)

Một **đường cong elliptic** trên trường hữu hạn $$\mathbb{F}_q$$ có dạng Weierstrass rút gọn:

$$
y^2 = x^3 + Ax + B
$$

với điều kiện không suy biến $$4A^3 + 27B^2 \neq 0$$. Điểm tuyệt vời của hình học đại số là tập các điểm $$(x,y)$$ trên đường cong, thêm một "điểm ở vô cực" $$\mathcal{O}$$ làm phần tử đơn vị, lập thành một **nhóm abel** với phép cộng định nghĩa trực quan bằng kẻ đường thẳng (cát tuyến cắt đường cong tại điểm thứ ba rồi lấy đối xứng qua trục hoành).

Phép nhân vô hướng $$P \mapsto aP = \underbrace{P + P + \dots + P}_{a\text{ lần}}$$ tính cực nhanh nhờ phương pháp nhân đôi liên tiếp (tương tự bình phương liên tiếp). Ngược lại, biết $$P$$ và $$Q=aP$$ mà tìm lại số nguyên $$a$$ (bài toán **ECDLP**) lại chưa có thuật toán cận hàm mũ nào hiệu quả như index-calculus trên trường hữu hạn!

**Vì sao ECC lại được ưa chuộng đến thế?** Hãy nhìn bảng so sánh độ dài khóa để đạt cùng mức an toàn cổ điển 128 bit:

| Hệ mật | Độ dài khóa công khai (mức an toàn 128-bit) | Tốc độ & băng thông |
|---|---|---|
| RSA / Diffie–Hellman cổ điển | ~3.072 bit | Chậm hơn, gói tin bắt tay lớn |
| Đường cong elliptic (ECC, ví dụ Curve25519 / P-256) | **256 bit** (ngắn hơn 12 lần!) | Rất nhanh, lý tưởng cho điện thoại và IoT |

Điện thoại của bạn khi kết nối HTTPS (TLS 1.3) ngày nay gần như chắc chắn đang dùng **ECDHE** (Diffie–Hellman tạm thời trên đường cong elliptic).

**Ý chính.**  
*ECC giữ nguyên kịch bản Diffie–Hellman nhưng thay "sân chơi" từ nhóm nhân của trường hữu hạn sang nhóm điểm trên đường cong elliptic; mỗi bit khóa mang lại hiệu suất bảo mật cao vượt trội.*

Hình học số học — một lĩnh vực từng được xem là đỉnh cao trừu tượng — đã âm thầm đi vào từng chiếc điện thoại thông minh.

---

## 6. Chữ ký, chứng chỉ và mã hóa lai

Một mình mã hóa khóa công khai chưa đủ để xây dựng mạng web an toàn. Hạ tầng thực tế ghép bốn lớp lại với nhau:

- **Chữ ký số** (RSA-PSS, ECDSA, Ed25519…) để xác thực tác giả và tính toàn vẹn của bản cập nhật phần mềm, giao dịch ngân hàng hay tài liệu điện tử.  
- **Chứng chỉ số** (PKI / X.509) gắn khóa công khai với một tên miền thật (như `nganhang.vn`) thông qua chữ ký của các Tổ chức Chứng thực (CA), chặn đứng kẻ giả mạo xen giữa (Man-in-the-Middle).  
- **Mã hóa lai (hybrid):** khóa công khai tính toán chậm hơn mã hóa đối xứng hàng trăm đến hàng nghìn lần. Vì vậy TLS chỉ dùng ECC/RSA (hoặc cơ chế đóng gói khóa KEM) trong vài mili-giây đầu để thỏa thuận một khóa phiên đối xứng 256-bit, rồi chuyển toàn bộ luồng dữ liệu sang AES-GCM hoặc ChaCha20.  
- **Mã hóa có xác thực (AEAD):** vừa giấu nội dung, vừa phát hiện ngay nếu bản mã bị sửa đổi dù chỉ 1 bit trên đường truyền.

Lý thuyết số lo phần bắt tay toán học; kỹ thuật hệ thống và mô hình tin cậy lo phần còn lại. Các sự cố bảo mật lớn trong lịch sử (như lỗi sinh số ngẫu nhiên trên Debian OpenSSL hay CA bị xâm nhập) hầu hết đến từ lỗi triển khai chứ không phải vì định lý Euler bỗng dưng sai.

---

## 7. Độ khó tính toán: mật mã gặp lý thuyết độ phức tạp

Mật mã học cần những bài toán thỏa mãn đồng thời ba yêu cầu khắt khe:

1. **Dễ sinh bài toán** (chọn hai số nguyên tố lớn rồi nhân lại rất nhanh),  
2. **Dễ giải khi có cửa sập** (biết $$p,q$$ thì giải mã tức thì),  
3. **Khó giải trên trường hợp điển hình (average-case hardness)** — không chỉ khó ở vài trường hợp dị biệt hiếm gặp.

Điều này liên hệ mật thiết với bài toán thiên niên kỷ **P vs NP** nhưng không đồng nhất. Tính NP-đầy đủ nói về độ khó trong *trường hợp xấu nhất*; mật mã lại cần độ khó *trung bình* có cấu trúc cửa sập (xem [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/)). Dù vậy, cả hai cùng chia sẻ một triết lý sâu sắc: **sự bất khả thi về tính toán không phải rào cản — nó là một nguồn tài nguyên quý giá có thể dùng để bảo vệ con người.**

---

## 8. Mối đe dọa lượng tử và mật mã hậu lượng tử

Năm 1994, Peter Shor phát hiện ra **thuật toán Shor** chạy trên máy tính lượng tử có thể phân tích thừa số nguyên tố và giải logarit rời rạc (cả trên trường hữu hạn lẫn đường cong elliptic!) trong **thời gian đa thức**. Nếu một ngày máy tính lượng tử chịu lỗi đủ lớn ra đời, cả RSA, Diffie–Hellman lẫn ECC đều sẽ sụp đổ. Trong khi đó, thuật toán Grover chỉ tăng tốc theo căn bậc hai cho tìm kiếm vét cạn — nghĩa là mã hóa đối xứng như AES chỉ cần tăng gấp đôi độ dài khóa (từ 128 lên 256 bit) là vẫn đứng vững.

Để chuẩn bị từ sớm (chống cả kịch bản *"thu thập hôm nay, giải mã tương lai"*), **Mật mã hậu lượng tử (PQC)** chuyển sang các bài toán toán học mà ngay cả máy tính lượng tử cũng chưa biết cách phá nhanh:

- **Mật mã dựa trên lưới (Lattice-based — bài toán LWE):** trực giác cực kỳ thú vị! Giải một hệ phương trình tuyến tính $$A\mathbf{s} = \mathbf{b} \pmod q$$ cực dễ bằng khử Gauss. Nhưng chỉ cần cộng thêm một chút **nhiễu ngẫu nhiên nhỏ** $$\mathbf{e}$$ vào vế phải ($$\mathbf{b} = A\mathbf{s} + \mathbf{e} \pmod q$$), phép khử Gauss lập tức khuếch đại nhiễu lên hỗn loạn, biến bài toán thành việc tìm điểm lưới gần nhất trong không gian hàng trăm chiều — bài toán khó với cả máy tính cổ điển lẫn lượng tử!
- **Mã sửa sai** (kiểu McEliece),  
- **Chữ ký dựa trên hàm băm** (như SPHINCS+ / SLH-DSA, độ an toàn chỉ dựa vào tính một chiều của hàm băm),  
- Các hướng nghiên cứu khác (đa thức nhiều biến, isogeny — một số đề xuất isogeny đã bị phá, cho thấy phân tích mã vẫn luôn sôi động).

Viện Tiêu chuẩn và Công nghệ Quốc gia Mỹ (NIST) đã chính thức ban hành các chuẩn PQC đầu tiên (như **ML-KEM** từ Kyber cho trao đổi khóa, **ML-DSA** từ Dilithium và **SLH-DSA** cho chữ ký số), và các trình duyệt lớn đã bắt đầu triển khai lai ghép ECC + ML-KEM. Xem thêm [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/) và [Cập nhật 2022–2026]({{ site.baseurl }}/contents/vi/chapter03/03_10_modern_applications/).

**Tóm tắt sự chuyển đổi.**  
*Mật mã khóa công khai cổ điển dựa trên số học của nhóm nhân và đường cong elliptic; mật mã hậu lượng tử chuyển sang hình học của lưới nhiều chiều và hàm băm. Toán học thuần túy vẫn tiếp tục là nền móng của an ninh số.*

---

## 9. Vì sao lý thuyết số đã "sẵn sàng"

Kiểm tra tính nguyên tố, nghịch đảo modulo, định lý Euler, cấu trúc nhóm và đường cong elliptic đều đã được các nhà toán học mài giũa hàng thế kỷ trước khi có mạng Internet. Khi Diffie, Hellman, Rivest, Shamir và Adleman đi tìm một hàm cửa sập, cả một kho vũ khí toán học đã nằm sẵn trên kệ. Bước đột phá không nằm ở việc đổi tên ngành học, mà ở việc nhận ra rằng **một bài toán khó giải cũng hữu ích ngang bằng một công thức giải được**.

Giả thuyết Riemann ([Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/)) vẫn là câu hỏi thuần túy hàng đầu về sự phân bố của số nguyên tố. Mật mã tiếp cận số nguyên từ góc độ tính toán, nhưng cả hai cùng chứng minh rằng thế giới của những con số nguyên chưa bao giờ cạn kiệt bất ngờ.

---

### Lưu ý khi xem video về mật mã (từ phần tìm hiểu)

Trình tự xem phổ biến: [Numberphile RSA](https://www.youtube.com/watch?v=M7kEpw1tn50) → [RSA-129](https://www.youtube.com/watch?v=YQw124CtvO0) → [Computerphile public key](https://www.youtube.com/watch?v=GSIDS_lvRv4) → [Diffie–Hellman](https://www.youtube.com/watch?v=NmM9HA2MQGI).

- Các video giải thích ý tưởng *cửa sập* rất tốt, nhưng thường bỏ qua phần đệm, tấn công kênh kề và việc chọn tham số.
- Tính đúng của RSA dùng định lý Euler/Fermat; độ an toàn là an toàn tính toán, không phải an toàn theo lý thuyết thông tin.
- Về mật mã hậu lượng tử: xem [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography).

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "RSA an toàn vì phép nhân khó." | Phép nhân dễ; *phân tích thừa số* mới là chiều khó. |
| "Giấu thuật toán là an toàn." | Theo Kerckhoffs, thuật toán được công khai; chỉ khóa là bí mật. |
| "$$n$$ càng lớn càng an toàn, thế là đủ." | Kích thước quan trọng, nhưng phần đệm, kênh kề, bộ sinh số ngẫu nhiên và giao thức cũng quan trọng. |
| "ECC an toàn vì đường cong phức tạp." | ECC dựa trên độ khó của ECDLP trên nhóm được chọn, cộng với cài đặt đúng. |
| "Hậu lượng tử nghĩa là mật mã lượng tử." | PQC thường là các thuật toán cổ điển, chạy trên máy tính thường, chống được tấn công lượng tử. |
| "Nếu P≠NP thì RSA an toàn mãi mãi." | Cần độ khó trung bình của một bài toán cụ thể, không chỉ P≠NP. |

---

## Bài tập

1. Tính $$17\bmod 5$$ và $$2^8\bmod 7$$; tìm $$x$$ sao cho $$3x\equiv 1\pmod 7$$.  
2. Giải thích khóa công khai và khóa bí mật trong hai câu cho một người không học toán.  
3. Vì sao công bố $$n=pq$$ không làm lộ ngay $$p,q$$ khi các số nguyên tố đủ lớn?  
4. Trong Diffie–Hellman, kẻ nghe lén thấy $$g^a,g^b$$. Nếu giải được logarit rời rạc, kẻ đó làm được gì?  
5. **Bài viết ngắn (≤300 từ).** Trình bày cơ chế nối lũy thừa theo modulo với mã hóa khóa công khai, từng bước một.  
6. Tìm một bài báo nói "mật mã không thể bị phá" và chỉ ra một câu nói quá.  
7. Nâng cao: vì sao web dùng mã hóa lai thay vì dùng RSA cho toàn bộ dữ liệu?

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

- Đây là bài trọng tâm của phần. Hãy thử RSA với các số nguyên tố nhỏ (không an toàn, chỉ để hiểu) và thảo luận vì sao cần phần đệm.  
- [Đồ thị → Mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) hoặc [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [8.Hệ mật RSA_Định nghĩa và ví dụ](https://www.youtube.com/watch?v=QEoRfrSKciI) (Bùi Thị Thùy _CNTT, tiếng Việt). Định nghĩa và ví dụ tính toán RSA bằng tiếng Việt. Dùng để đối chiếu với §1 và §3.
- [Encryption and HUGE numbers - Numberphile](https://www.youtube.com/watch?v=M7kEpw1tn50) (Numberphile, tiếng Anh). Giới thiệu RSA và vai trò của các số rất lớn trong mã hóa. Xem sau khi đọc §3.
- [RSA-129 - Numberphile](https://www.youtube.com/watch?v=YQw124CtvO0) (Numberphile, tiếng Anh). Câu chuyện về thử thách RSA-129 và lần nó bị phân tích thừa số. Minh họa vì sao kích thước khóa phải tăng theo thời gian.
