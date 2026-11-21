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

**Lý thuyết số** từng được xem là ngành thuần túy nhất, "nữ hoàng của toán học". Ngày nay nó bảo vệ việc trao đổi thông tin an toàn trên internet. Mỗi lần trình duyệt bắt tay TLS, mỗi chữ ký trên phần mềm, mỗi biểu tượng ổ khóa trong ứng dụng nhắn tin đều dùng đến số học đồng dư, việc sinh số nguyên tố và các bài toán khó trên nhóm.

Đây là **bài trọng tâm của Phần 3**, đi theo một chuỗi rõ ràng:

**số học đồng dư → hàm cửa sập → mật mã khóa công khai (RSA, Diffie–Hellman, ECC) → các giao thức internet thực tế → mối đe dọa từ máy tính lượng tử và mật mã hậu lượng tử dựa trên lưới.**

Mục tiêu của bài: nối một lĩnh vực toán cổ điển với những công nghệ cụ thể, và nêu đúng cơ chế ở từng bước, thay vì chỉ nói chung chung "lý thuyết số được dùng trong mật mã".

**Lộ trình:** đồng dư → mật mã đối xứng và mật mã khóa công khai → RSA → Diffie–Hellman → ECC → chữ ký, hạ tầng khóa công khai, mã hóa lai → độ khó tính toán → mật mã hậu lượng tử → nhầm lẫn thường gặp.

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

## 1. Số học đồng dư: tính toán với số dư

Cố định một số nguyên dương $$n$$ (gọi là **modulo**). Ta viết

$$
a \equiv b \pmod{n}
$$

khi $$n$$ chia hết $$a-b$$, tức là $$a$$ và $$b$$ có cùng số dư khi chia cho $$n$$.

Tính toán **theo modulo $$n$$** giống như xem một chiếc đồng hồ có $$n$$ vạch: sau $$n-1$$ thì quay về $$0$$. Phép cộng và phép nhân tương thích với đồng dư:

$$
a\equiv a',\quad b\equiv b' \pmod{n} \implies a+b\equiv a'+b',\quad ab\equiv a'b' \pmod{n}.
$$

Vành $$\mathbb{Z}/n\mathbb{Z}$$ là cấu trúc đại số cơ bản trong sách giáo khoa mật mã. Khi $$n=p$$ là số nguyên tố, mọi số dư khác 0 đều có nghịch đảo theo phép nhân, nên $$\mathbb{Z}/p\mathbb{Z}$$ là một **trường**. Nhờ đó ta chia được và làm được đại số tuyến tính trên trường hữu hạn (AES dùng số học trên trường hữu hạn; đường cong elliptic được xét trên $$\mathbb{F}_p$$).

**Lũy thừa nhanh.** Có thể tính $$a^e\bmod n$$ với $$e$$ rất lớn bằng phương pháp **bình phương liên tiếp**, chỉ cần $$O(\log e)$$ phép nhân. Ngược lại, tính *căn bậc $$e$$* hay *logarit rời rạc* được tin là khó nếu các tham số được chọn cẩn thận. Sự bất đối xứng này (tính lũy thừa thì dễ, tính ngược thì khó) là nguyên liệu của mật mã khóa công khai.

**Định lý Fermat và Euler.** Nếu $$p$$ là số nguyên tố và $$p\nmid a$$ thì $$a^{p-1}\equiv 1\pmod p$$ (định lý Fermat nhỏ). Tổng quát hơn, định lý Euler dùng hàm $$\varphi(n)$$, số các số dư nguyên tố cùng nhau với $$n$$. Tính đúng đắn của RSA dựa trên việc số mũ "triệt tiêu" theo modulo như vậy, **không** dựa trên việc giấu thuật toán (thuật toán được công bố công khai).

**Thuật toán Euclid** tính $$\gcd$$ và nghịch đảo theo modulo trong thời gian logarit. Một kết quả lý thuyết số cổ điển trở thành một hàm con trong phần mềm thế kỷ XXI.

---

## 2. Mật mã đối xứng và mật mã khóa công khai

**Mật mã đối xứng:** Alice và Bob có chung một khóa bí mật từ trước; mã hóa và giải mã dùng cùng một khóa (AES-GCM, ChaCha20-Poly1305, …). Cách này rất tốt để mã hóa khối lượng dữ liệu lớn ở tốc độ đường truyền. Nhưng nó không trả lời được câu hỏi ban đầu: *nếu hai bên chưa từng gặp nhau và mạng đầy kẻ nghe lén, làm sao bắt đầu nói chuyện an toàn?*

**Mật mã khóa công khai** (Diffie–Hellman 1976; RSA 1978; các biến thể dùng đường cong elliptic về sau): mỗi bên công bố một khóa **công khai** và giữ một khóa **bí mật**. Ai cũng có thể dùng khóa công khai của bạn để mã hóa thông điệp gửi bạn, nhưng chỉ bạn giải mã được. Chữ ký số thì ngược lại: chỉ bạn ký được, nhưng ai cũng kiểm tra được bằng khóa công khai của bạn.

Ý tưởng toán học then chốt là **hàm một chiều có cửa sập**: dễ tính, khó tính ngược nếu không biết thông tin bí mật, nhưng dễ tính ngược nếu biết "cửa sập".

**Nguyên lý Kerckhoffs.** Độ an toàn phải dựa trên việc giữ bí mật khóa, không dựa trên việc giấu thuật toán. Mật mã hiện đại giả định thuật toán được công khai và bị các chuyên gia tìm cách tấn công.

---

## 3. RSA: phân tích thừa số làm cửa sập

**Thiết lập (phiên bản RSA đơn giản trong sách giáo khoa).**

1. Chọn hai số nguyên tố lớn bí mật $$p,q$$; công bố $$n=pq$$ (không công bố $$p,q$$).  
2. Tính $$\varphi(n)=(p-1)(q-1)$$ (giữ bí mật).  
3. Chọn số mũ công khai $$e$$ nguyên tố cùng nhau với $$\varphi(n)$$ (trong thực tế thường là $$e=65537$$).  
4. Tính số mũ bí mật $$d$$ sao cho $$ed\equiv 1\pmod{\varphi(n)}$$ (nghịch đảo theo modulo).  
5. Mã hóa thông điệp (đã được biểu diễn thành số) $$m$$: $$c\equiv m^e\pmod n$$.  
6. Giải mã: $$m\equiv c^d\pmod n$$.

**Tóm tắt trong một câu.**  
*Mã hóa là lũy thừa theo modulo với số mũ công khai; giải mã cần số mũ nghịch đảo, và số mũ này dễ tìm nếu biết $$\varphi(n)$$ (tức là biết $$p,q$$), nhưng được tin là khó tìm nếu chỉ biết $$n$$.*

**Giả định về độ khó (phát biểu không chính thức).** Phân tích một tích của hai số nguyên tố lớn là bất khả thi ở kích thước khuyến nghị (hàng nghìn bit). Nếu việc phân tích thừa số trở nên dễ, cửa sập của RSA sụp đổ. Cần lưu ý: các chứng minh an toàn chỉ liên hệ một phần việc phá RSA với bài toán phân tích thừa số. Ngoài ra **phần đệm (padding)** như OAEP, PSS là bắt buộc: RSA dạng sách giáo khoa dễ bị kẻ tấn công biến đổi bản mã, nên không thể dùng trực tiếp.

**Lý thuyết số thuần túy đóng góp gì.** Thuật toán Euclid, nghịch đảo theo modulo, hàm $$\varphi$$ Euler, việc sinh số nguyên tố (kể cả kiểm tra tính nguyên tố theo xác suất), và các hiểu biết về độ phức tạp của bài toán phân tích thừa số. Hàng thế kỷ nghiên cứu, từ Gauss đến các nhà mật mã hiện đại, được gói gọn trong một lần bắt tay trao khóa.

**Chọn tham số cẩn thận.** Số mũ $$e$$ nhỏ đi kèm phần đệm kém, các modulo dùng chung số nguyên tố, bộ sinh số ngẫu nhiên bị lệch, tấn công kênh kề: tất cả đều đã từng phá được những hệ RSA "đúng về toán" trong thực tế. Lý thuyết số cung cấp cửa sập; kỹ thuật phải lo phần còn lại của bề mặt tấn công.

---

### Video ngắn: Trao đổi khóa với p = 23

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/diffie-hellman-mod23_vi.mp4"></video>
</div>

Các lũy thừa của 5 modulo 23 đi qua mọi số dư từ 1 đến 22 theo thứ tự xáo trộn. An và Bình mỗi người công bố một lũy thừa (8 và 19) mà vẫn cùng đến bí mật 2, còn kẻ nghe lén phải giải một log rời rạc. Với $$p = 23$$ việc đó dễ; với kích thước thật thì không.


### Tự tay thử: Tự chạy một lần trao đổi khóa

<div class="mex-explainer" data-mex="dh" data-lang="vi"></div>


## 4. Diffie–Hellman và logarit rời rạc

Tham số công khai: một nhóm (cổ điển là nhóm nhân theo modulo một số nguyên tố, hoặc nhóm điểm trên đường cong elliptic) và một phần tử sinh $$g$$ của một nhóm con lớn có cấp nguyên tố.

- Alice chọn số bí mật $$a$$, gửi đi $$A=g^a$$.  
- Bob chọn số bí mật $$b$$, gửi đi $$B=g^b$$.  
- Bí mật chung: $$A^b=B^a=g^{ab}$$.

**Bài toán logarit rời rạc (DLP):** biết $$g$$ và $$g^a$$, tìm lại $$a$$. Nếu DLP khó, kẻ nghe lén không thể tính được $$g^{ab}$$ chỉ từ các giá trị công khai (phát biểu chính xác cần các giả định kiểu CDH/DDH).

**Ý chính.**  
*Các giá trị truyền công khai là lũy thừa trong nhóm; bí mật chung có số mũ là tích của hai số bí mật, nên chỉ người biết ít nhất một trong hai số mũ mới tính được.*

**Diffie–Hellman trên trường hữu hạn** cần số nguyên tố lớn và tham số an toàn trước các thuật toán kiểu index-calculus. Áp lực về kích thước này là một lý do dẫn đến việc dùng đường cong elliptic.

---

## 5. Mật mã đường cong elliptic (ECC)

Một **đường cong elliptic** trên một trường (ở đây là trường hữu hạn $$\mathbb{F}_q$$) có thể viết dưới dạng Weierstrass rút gọn

$$
y^2 = x^3 + Ax + B
$$

với biệt thức khác 0. Tập các điểm trên đường cong, thêm một điểm ở vô cực, tạo thành một **nhóm** abel với phép cộng định nghĩa bằng hình học qua cát tuyến và tiếp tuyến. Phép nhân vô hướng $$P\mapsto aP$$ (cộng $$P$$ với chính nó $$a$$ lần) thì dễ tính; bài toán ngược (logarit rời rạc trên đường cong elliptic) được tin là khó với các đường cong được chọn tốt.

**Giao thức Diffie–Hellman vẫn giữ nguyên**, nhưng khóa ngắn hơn cho cùng mức an toàn cổ điển (ví dụ đường cong 256 bit so với modulo RSA 3072 bit; con số cụ thể thay đổi theo từng hướng dẫn). Điện thoại của bạn khi kết nối TLS gần như chắc chắn dùng ECDHE.

**Ý chính.**  
*ECC chuyển Diffie–Hellman từ nhóm nhân của trường hữu hạn sang nhóm điểm trên một đường cong được chọn kỹ; cửa sập vẫn cùng kiểu, nhưng mỗi bit khóa mang lại nhiều an toàn hơn.*

Hình học số học, một lĩnh vực rất sâu, đã âm thầm đi vào các sản phẩm bảo mật đại trà. Đây là một minh họa rõ cho chủ đề của chương: toán "thuần túy" tìm được ứng dụng.

---

## 6. Chữ ký, chứng chỉ và mã hóa lai

Chỉ mã hóa khóa công khai thì chưa đủ để xây dựng web. Còn cần:

- **Chữ ký số** (RSA-PSS, ECDSA, EdDSA, …) để chứng minh nguồn gốc và tính toàn vẹn của bản cập nhật phần mềm và tài liệu.  
- **Chứng chỉ** (PKI / X.509) gắn một khóa công khai với một danh tính, thông qua tổ chức chứng thực đáng tin cậy hoặc một mô hình tin cậy khác.  
- **Mã hóa lai (hybrid):** dùng khóa công khai (hoặc cơ chế đóng gói khóa KEM) để thiết lập khóa phiên đối xứng, rồi dùng AES (hoặc tương tự) cho phần lớn dữ liệu.  
- **Mã hóa có xác thực** để bản mã không bị sửa đổi mà không ai phát hiện.

Lý thuyết số lo phần bắt tay; kỹ thuật, kinh tế và luật pháp lo mô hình tin cậy. Cả hai đều có thể hỏng: bộ sinh số ngẫu nhiên kém (sự cố OpenSSL trên Debian), tổ chức chứng thực bị xâm nhập, tấn công hạ cấp giao thức. Trong những trường hợp đó, giả định về độ khó bên dưới vẫn chưa hề "sai".

---

## 7. Độ khó tính toán: mật mã gặp lý thuyết độ phức tạp

Mật mã cần những bài toán:

1. Dễ tạo ra các trường hợp cụ thể,  
2. Dễ giải nếu biết cửa sập hay thông tin bí mật,  
3. Khó giải với đối thủ trên các trường hợp **điển hình** (khó trung bình, không chỉ khó trong trường hợp xấu nhất).

Điều này liên quan đến **P vs NP** nhưng không trùng. Tính NP-đầy đủ nói về độ khó trong trường hợp xấu nhất của các bài toán quyết định; mật mã cần độ khó trung bình, có cấu trúc, *dùng được* (xem [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/)). Dù vậy, cả hai đều dựa trên cùng một ý tưởng: **sự bất khả thi về tính toán cũng là một nguồn tài nguyên**.

Hàm một chiều, bộ sinh giả ngẫu nhiên và chứng minh không tiết lộ thông tin (zero-knowledge) phát triển ý tưởng này xa hơn RSA nhiều, nhưng ở bậc đại học câu chuyện vẫn bắt đầu từ số học đồng dư.

---

## 8. Mối đe dọa lượng tử và mật mã hậu lượng tử

**Thuật toán Shor** (trên máy tính lượng tử) phân tích thừa số và tính logarit rời rạc trong thời gian đa thức. Nó đe dọa RSA cũng như Diffie–Hellman và ECC cổ điển nếu có máy tính lượng tử đủ lớn và đủ tin cậy. Thuật toán Grover chỉ tăng tốc theo căn bậc hai cho bài toán tìm kiếm không cấu trúc. Nó buộc phải tăng độ dài khóa đối xứng, nhưng không "phá" được AES với khóa dài gấp đôi theo cách Shor phá RSA.

**Mật mã hậu lượng tử (PQC)** chuyển sang những giả định độ khó chưa bị thuật toán Shor phá, đặc biệt:

- **Lưới** (bài toán Learning With Errors và các biến thể): hình học của số được dùng làm mật mã,  
- **Mã sửa sai** (kiểu McEliece),  
- **Chữ ký dựa trên hàm băm** (thận trọng; loại có trạng thái, hoặc loại không trạng thái như SPHINCS),  
- Các ý tưởng dựa trên đa thức nhiều biến và isogeny, vẫn đang được phân tích mã liên tục (một số hệ isogeny đã bị phá).

Quá trình chuẩn hóa PQC của NIST (Kyber/ML-KEM, Dilithium/ML-DSA, …, tên gọi và tham số vẫn thay đổi theo thời gian) là mặt thể chế của sự chuyển đổi này. Xem [Mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

**Tóm tắt sự chuyển đổi.**  
*Mật mã khóa công khai cổ điển dựa trên tính một chiều của số học trên nhóm nhân và nhóm điểm elliptic; PQC dựa trên độ khó của các bài toán lưới nhiều chiều và các cấu trúc liên quan. Toán thuần túy vẫn là nền móng của hạ tầng.*

---

## 9. Vì sao lý thuyết số đã "sẵn sàng"

Kiểm tra tính nguyên tố, nghịch đảo theo modulo, cấu trúc nhóm và niềm say mê với số nguyên tố đều có từ trước khi có thương mại điện tử. Khi Diffie, Hellman, Rivest, Shamir và Adleman cần một cửa sập, công cụ đã có sẵn. Chuyển từ toán thuần túy sang ứng dụng không đòi hỏi đổi tên ngành. Nó chỉ đòi hỏi nhận ra rằng **một giả định về độ khó tính toán** cũng có giá trị như một công thức tường minh.

Giả thuyết Riemann ([Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/)) vẫn là câu hỏi thuần túy hàng đầu về số nguyên tố. Mật mã dùng số học theo một cách khác, nhưng cả hai đều cho thấy cấu trúc của các số nguyên chưa bao giờ cạn.

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
