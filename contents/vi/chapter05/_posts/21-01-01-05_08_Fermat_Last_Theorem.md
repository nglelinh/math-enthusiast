---
layout: post
title: "Định lý Cuối cùng của Fermat"
chapter: '05'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter05
---

Khoảng năm 1637, bên lề cuốn sách *Arithmetica* của Diophantus, vị thẩm phán kiêm nhà toán học người Pháp **Pierre de Fermat** nguệch ngoạc một dòng ghi chú ngắn ngủi đã trở thành lời thách thức nổi tiếng nhất lịch sử toán học: với mọi số nguyên $$n \ge 3$$, phương trình

$$
a^n + b^n = c^n
$$

không có nghiệm nguyên dương $$a, b, c$$ nào — và ông viết thêm: *"Tôi đã tìm ra một chứng minh thực sự kỳ diệu cho mệnh đề này, nhưng lề sách quá hẹp để viết vào."*

Dòng ghi chú bên lề ấy đã ám ảnh nhân loại suốt **358 năm**. Hàng nghìn lời giải sai đổ về các viện hàn lâm; những bộ óc vĩ đại như Euler, Sophie Germain, Kummer khai sinh cả những ngành đại số mới chỉ để chinh phục từng phần nhỏ của nó. Mãi đến thập niên 1990, sau bảy năm làm việc bí mật trên căn gác mái ở Princeton, **Andrew Wiles** (cùng phần sửa chữa bước ngoặt với **Richard Taylor**) mới khép lại câu chuyện. Điều làm giới toán học kinh ngạc nhất không phải độ dài của bản chứng minh, mà là **chiếc cầu nối xuyên lục địa** giữa hai thế giới tưởng chừng không liên quan gì đến nhau:

**Phương trình Diophantine → đường cong elliptic Frey → tính modular → mâu thuẫn.**

**Mạch bài học:** Bản đồ kiến thức nền (lý thuyết số đại số, đường cong elliptic, dạng modular và Chương trình Langlands) → Từ bộ ba Pythagore đến bức tường bậc 3 → Vì sao phương pháp sơ cấp bế tắc → Khung giải thích chậm: tự tay đếm điểm trên đường cong elliptic modulo $$5$$ và giải phẫu chiếc gọng kìm Frey–Ribet–Wiles → Ghi công và ý nghĩa lịch sử.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Phát biểu chính xác FLT và kiểm các trường hợp nhỏ $$n=3,4$$ như những mốc lịch sử (ở mức ý tưởng).
- Giải thích vì sao phép xuống thang vô hạn giải quyết được một số số mũ sớm, trong khi trường hợp tổng quát thì kháng cự.
- Mô tả đường cong Frey gắn với một nghiệm giả định và vì sao nó "quá kỳ lạ".
- Phác thảo chuỗi logic: Frey → Ribet (giả thuyết ε, hạ level) → tính modular (Wiles–Taylor) → mâu thuẫn.
- Ghi công đúng người (Wiles; Taylor–Wiles; Frey, Serre, Ribet, Taniyama–Shimura–Weil).
- Phân biệt *ý tưởng chứng minh* với các huyền thoại phổ biến (chứng minh sơ cấp ở lề sách; hay việc cho rằng chỉ cần đường cong elliptic mà không cần dạng modular).

**Kiến thức cần có.** Phương trình nghiệm nguyên; sẵn sàng chấp nhận đường cong elliptic và dạng modular như những "hộp đen" có tên, mỗi cái kèm một câu nói về vai trò. Các bài lý thuyết số hiện đại ở chương 2 là phần mở rộng tùy chọn.

---

## Bản đồ kiến thức nền: Lý thuyết số đại số, Đường cong elliptic và Chương trình Langlands là gì?

Vì sao một phương trình lớp 6 lại phải huy động đến toán học đỉnh cao cuối thế kỷ XX? Hãy nhìn lên bản đồ ba trụ cột giúp người tốt nghiệp đại học nắm trọn "vũ trụ" phía sau chứng minh của Wiles:

### 1. Phương trình Diophantine và Lý thuyết số đại số
Phương trình chỉ tìm nghiệm nguyên gọi là **phương trình Diophantine**. Vào thế kỷ XIX, các nhà toán học thử phân tích $$a^p + b^p$$ thành nhân tử bằng cách mở rộng tập số nguyên sang các vành số phức (như $$\mathbb{Z}[\zeta_p]$$, với $$\zeta_p = e^{2\pi i/p}$$). Thế nhưng họ gặp cú sốc lớn: trong nhiều vành mở rộng, **phân tích thừa số nguyên tố không còn duy nhất!** Ví dụ cầm tay trong vành $$\mathbb{Z}[\sqrt{-5}]$$:

$$
6 \;=\; 2 \cdot 3 \;=\; \bigl(1 + \sqrt{-5}\bigr)\bigl(1 - \sqrt{-5}\bigr),
$$

trong khi cả $$2, 3, 1+\sqrt{-5}, 1-\sqrt{-5}$$ đều không phân tích nhỏ hơn được nữa! Nỗ lực khôi phục tính duy nhất bằng khái niệm **ideal** của Ernst Kummer đã khai sinh **Lý thuyết số đại số**, nhưng các "số nguyên tố không chính quy" (bắt đầu từ $$p = 37$$) vẫn chặn đứng cách tiếp cận trực tiếp.

### 2. Đường cong elliptic (Elliptic Curve) là gì?
Không phải hình elip! Một **đường cong elliptic** trên $$\mathbb{Q}$$ là tập nghiệm của phương trình bậc ba trơn dạng $$y^2 = x^3 + Ax + B$$ (có biệt thức $$\Delta = -16(4A^3 + 27B^2) \neq 0$$) cùng một điểm ở vô cùng $$\mathcal{O}$$. Điểm kỳ diệu là các điểm trên đường cong này có một **phép cộng hình học** biến chúng thành nhóm giao hoán (nền tảng của mật mã đường cong elliptic **ECC** ngày nay). Quan trọng hơn với FLT: với mỗi số nguyên tố $$p$$, ta đếm được số điểm của đường cong trên trường hữu hạn $$\mathbb{F}_p$$ để lập thành dãy "dấu vân tay số học" $$a_p$$.

### 3. Dạng modular (Modular Form) và Chương trình Langlands
Ở một lục địa hoàn toàn khác — **giải tích phức** — tồn tại các **dạng modular**: những hàm biến phức trên nửa mặt phẳng trên có tính đối xứng cực mạnh, khai triển được thành chuỗi Fourier $$f(q) = \sum c_n q^n$$. **Định lý Modular** (trước đây là giả thuyết Taniyama–Shimura–Weil) khẳng định điều phi thường: *với mọi đường cong elliptic $$E$$ trên $$\mathbb{Q}$$, tồn tại một dạng modular $$f$$ sao cho dấu vân tay số học $$a_p(E)$$ trùng khít từng con số với hệ số Fourier $$c_p(f)$$ tại mọi số nguyên tố $$p$$!* Đây là một mũi nhọn rực rỡ của **Chương trình Langlands**.

---

## 1. Từ chiếc ê-ke thợ mộc đến bức tường tuyệt đối ở bậc 3

Trong đời thường, bất kỳ người thợ mộc nào cũng biết bộ ba Pythagore $$3^2 + 4^2 = 5^2$$ (cùng vô hạn bộ khác như $$5^2 + 12^2 = 13^2$$ hay $$8^2 + 15^2 = 17^2$$) để dựng góc vuông chuẩn xác. Thậm chí ở bậc cao hơn, tồn tại những bộ số "suýt đúng" kỳ lạ đến mức từng đánh lừa cả máy tính bỏ túi thông thường — nổi tiếng nhất là trò đùa toán học trong phim *The Simpsons*:

$$
1782^{12} + 1841^{12} \;\approx\; 1922^{12}
$$

(Nếu bấm máy tính 10 chữ số, hai vế hiện ra giống hệt nhau; nhưng chỉ cần kiểm tra tính chẵn lẻ bằng mắt thường là thấy ngay nó sai: vế trái là chẵn $$+$$ lẻ $$=$$ **lẻ**, còn vế phải là **chẵn**!).

Đó chính là nghịch lý quyến rũ của Định lý lớn Fermat: với $$n = 1$$ ($$a + b = c$$) và $$n = 2$$ ($$a^2 + b^2 = c^2$$), nghiệm nguyên dương nhiều vô kể; nhưng chỉ cần nhích số mũ từ $$2$$ lên $$3$$ — và mọi $$n \ge 3$$ sau đó — thì cánh cửa đóng sập hoàn toàn, không còn lấy một nghiệm nguyên dương nào.

Người ta nhanh chóng quy bài toán về số mũ nguyên tố lẻ và $$n = 4$$: một phản ví dụ với $$n$$ hợp số sẽ cho một phản ví dụ với một ước của $$n$$ (ví dụ nếu $$a^6 + b^6 = c^6$$ thì $$(a^2)^3 + (b^2)^3 = (c^2)^3$$). Chính Fermat chứng minh trường hợp $$n=4$$ bằng phép xuống thang vô hạn. Euler và những người sau đó xử lý $$n=3$$ và các số nguyên tố nhỏ. Tuy vậy, một chứng minh chung cho mọi $$n$$ vẫn còn bỏ ngỏ suốt hơn ba thế kỷ.

---

## 2. Thế kỷ phương pháp sơ cấp không làm được gì

Phương trình thì đơn giản, nhưng việc chứng minh tập nghiệm rỗng thì không. Phép xuống thang trực tiếp chạy được với một số số mũ đặc biệt nhờ các hằng đẳng thức phân tích hoặc nhờ vành có phân tích duy nhất ra nhân tử (UFD). Với $$n$$ tổng quát, các vành mà người ta muốn phân tích không nhất thiết là UFD. Lý thuyết ideal của Kummer sửa được một phần, nhưng các số nguyên tố không chính quy chặn đường. Sang thế kỷ XX, FLT không còn là câu đố giải trí nữa mà là một **thước đo**: phương pháp nào đủ mạnh để xử lý mọi số mũ có lẽ sẽ sắp xếp lại phần lớn lý thuyết số.

---

## 3. Khung giải thích: tự tay đếm điểm đường cong elliptic modulo $$5$$ và giải phẫu bẫy Frey–Ribet–Wiles (nên đọc chậm)

Để cụm từ *"dấu vân tay số học của đường cong elliptic"* và *"hạ level"* không còn là hộp đen mơ hồ, hãy tự tay kiểm tra từng bước nhỏ sau:

### Bước 1: Tự tay tính "dấu vân tay" $$a_5$$ của một đường cong elliptic cụ thể
Xét đường cong elliptic đơn giản $$E:\ y^2 = x^3 + x + 1$$ trên trường hữu hạn $$\mathbb{F}_5 = \{0, 1, 2, 3, 4\}$$ (tính theo modulo $$5$$). Hãy thử lần lượt 5 giá trị của $$x$$ và tìm mọi $$y \in \{0, 1, 2, 3, 4\}$$ thỏa $$y^2 \equiv x^3 + x + 1 \pmod 5$$ (nhớ rằng các số chính phương modulo $$5$$ là $$0^2\equiv 0,\ 1^2\equiv 4^2\equiv 1,\ 2^2\equiv 3^2\equiv 4$$):

| $$x \in \mathbb{F}_5$$ | $$x^3 + x + 1 \pmod 5$$ | Nghiệm $$y \pmod 5$$ | Các điểm $$(x, y)$$ trên $$E(\mathbb{F}_5)$$ |
|------------------------|-------------------------|----------------------|----------------------------------------------|
| $$0$$ | $$0 + 0 + 1 = 1$$ | $$y = 1, 4$$ | $$(0, 1),\ (0, 4)$$ |
| $$1$$ | $$1 + 1 + 1 = 3$$ | Không có | — |
| $$2$$ | $$8 + 2 + 1 = 11 \equiv 1$$ | $$y = 1, 4$$ | $$(2, 1),\ (2, 4)$$ |
| $$3$$ | $$27 + 3 + 1 = 31 \equiv 1$$ | $$y = 1, 4$$ | $$(3, 1),\ (3, 4)$$ |
| $$4$$ | $$64 + 4 + 1 = 69 \equiv 4$$ | $$y = 2, 3$$ | $$(4, 2),\ (4, 3)$$ |

Đếm bằng tay: ta có $$8$$ điểm hữu hạn cộng thêm $$1$$ điểm ở vô cùng $$\mathcal{O}$$, tổng cộng $$\#E(\mathbb{F}_5) = 9$$ điểm. Dấu vân tay số học tại $$p = 5$$ được định nghĩa là độ lệch so với kỳ vọng $$p + 1 = 6$$:

$$
a_5(E) \;=\; (p + 1) - \#E(\mathbb{F}_5) \;=\; 6 - 9 \;=\; -3.
$$

Lặp lại phép đếm tay đó cho $$p = 2, 3, 5, 7, 11, \ldots$$, ta thu được cả một dãy số $$(a_2, a_3, a_5, a_7, \ldots)$$ — và **Định lý Modular** khẳng định dãy số ấy trùng khít hoàn toàn với các hệ số Fourier $$(c_2, c_3, c_5, c_7, \ldots)$$ của một dạng modular có **level $$N$$** (trong đó $$N$$ là *conductor*, chỉ chứa các ước nguyên tố "xấu" nơi đường cong bị suy biến)!

### Bước 2: Đường cong Frey biến nghiệm $$a^n + b^n = c^n$$ thành "con quái vật" như thế nào?
Giả sử tồn tại một nghiệm nguyên tố cùng nhau $$a^n + b^n = c^n$$ (với $$n \ge 5$$ nguyên tố, quy ước $$a \equiv -1 \pmod 4$$ và $$b$$ chẵn). **Gerhard Frey** (1984) dựng ngay đường cong elliptic:

$$
E_{\text{Frey}}:\quad y^2 \;=\; x\bigl(x - a^n\bigr)\bigl(x + b^n\bigr).
$$

Ba nghiệm của vế phải là $$0,\ a^n,\ -b^n$$. Biệt thức tối giản của đường cong này tỉ lệ với tích bình phương các hiệu nghiệm:

$$
\bigl(a^n - 0\bigr)^2 \bigl(0 - (-b^n)\bigr)^2 \bigl(a^n - (-b^n)\bigr)^2 \;=\; a^{2n} b^{2n} (a^n + b^n)^2 \;=\; (abc)^{2n}!
$$

Hãy nhìn điều kỳ dị chưa từng thấy: **mọi thừa số nguyên tố của biệt thức đều mang số mũ là bội của $$2n$$** (một lũy thừa cực cao!).

### Bước 3: Chiếc gọng kìm Wiles–Taylor và Ribet khép lại
1. **Nhánh Wiles–Taylor (1995):** Vì $$a, b, c$$ nguyên tố cùng nhau, đường cong Frey có tính chất *semistable*. Andrew Wiles (cùng Richard Taylor) chứng minh mọi đường cong elliptic semistable trên $$\mathbb{Q}$$ đều **modular** → vậy $$E_{\text{Frey}}$$ **bắt buộc** ứng với một dạng modular trọng số 2 có level $$N$$ là tích các ước nguyên tố của $$abc$$.
2. **Nhánh Ribet (1986, chứng minh giả thuyết $$\varepsilon$$ của Serre):** Chính vì mọi ước nguyên tố lẻ $$p \mid abc$$ đều xuất hiện trong biệt thức với số mũ $$2n$$ chia hết cho $$n$$, Định lý hạ level của Ken Ribet cho phép **lột bỏ từng ước nguyên tố lẻ một** ra khỏi level $$N$$ mà vẫn giữ được dạng modular tương thích modulo $$n$$ — cho đến khi level tụt xuống chỉ còn **$$N = 2$$**!
3. **Mâu thuẫn tuyệt đối:** Không gian các dạng modular cusp trọng số 2 ở level 2 có số chiều bằng **0** ($$\dim S_2(\Gamma_0(2)) = 0$$ — không tồn tại bất kỳ dạng modular khác không nào như vậy!). Vậy $$E_{\text{Frey}}$$ không thể tồn tại, kéo theo không có nghiệm $$a^n + b^n = c^n$$ nào!

---

## 4. Ý tưởng chứng minh (nên kể thế nào)

**Đừng** kể FLT như "Wiles tính toán rất dài". Hãy kể:

- **Dịch** việc không thể giải phương trình Diophantine thành việc không tồn tại một đường cong elliptic nhất định (Frey).
- **Gọi tên** sự tương ứng (tính modular) giữa các đường cong đó và các dạng modular (Taniyama–Shimura–Weil).
- **Suy ra** một ràng buộc mạnh đến mức dạng tương ứng không thể tồn tại (Serre–Ribet).
- **Cung cấp** định lý modular còn thiếu cho các đường cong semistable (Wiles–Taylor).

Đó là ý tưởng chứng minh. Phần kỹ thuật là lý thuyết biến dạng biểu diễn Galois và nâng tính modular, vốn đòi hỏi nhiều năm học sau đại học, không phải một buổi giảng.

---

## 5. Vì sao quan trọng

- **Kiến trúc chứng minh xuyên lĩnh vực.** Phát biểu sơ cấp, công cụ của thế kỷ XX.
- **Khai sinh và làm lớn mạnh phương pháp modular.** Kỹ thuật trong chứng minh này đã sắp xếp lại phần số học cụ thể của chương trình Langlands.
- **Bài học về lịch sử toán.** Một dòng ghi chú ở lề sách có thể dẫn dắt cả một thế kỷ sáng tạo, dù chứng minh được tuyên bố chưa bao giờ xuất hiện.
- **Kỹ năng đọc chứng minh.** Tách *ý tưởng bắc cầu* khỏi *phần máy móc kỹ thuật* là một kỹ năng quan trọng khi đọc các chứng minh dài.

---

## 6. Điều chứng minh hiện đại *không* mang lại

- Một chứng minh sơ cấp như Fermat tuyên bố (chưa có bản nào được các chuyên gia chấp nhận cho mọi $$n$$).
- Phân loại các trường hợp "suýt đúng" kiểu $$a^n+b^n\approx c^n$$ (đó là chủ đề riêng về xấp xỉ Diophantine).
- Một chứng minh ngắn: lập luận đầy đủ dài và dùng nhiều công cụ nặng, dù bộ khung của nó gọn.

---

## Nhầm lẫn thường gặp

1. "Một mình Wiles nghĩ ra mọi bước." Đây là chiến lược của nhiều người: Frey, Serre, Ribet, Taniyama–Shimura–Weil, Wiles, Taylor...
2. "FLT vẫn là giả thuyết." Nó đã là định lý; các thành phần về tính modular cần thiết đã được chứng minh.
3. "Đường cong Frey là một đường bậc ba bất kỳ." Nó là đường cong dựng *từ nghiệm giả định*, với các bất biến gắn với $$a,b,c$$.
4. "Tính modular nghĩa là đường cong là một hàm modular." Chính xác hơn: đường cong ứng với một dạng modular, theo nghĩa số học nói ở trên.
5. "Ý tưởng chứng minh nghĩa là bỏ qua biểu diễn Galois." Có thể coi chúng là hộp đen, nhưng cần biết chúng là ngôn ngữ hiện đại nối đường cong với dạng modular.

---

## Kiến thức rút ra từ phần tìm hiểu video

Tóm tắt dùng khi thảo luận (đối chiếu với nguồn viết; **không bịa nội dung transcript**). Gói: `research/video-research/fermat-last-theorem/analysis.md`.

### Tình trạng

**Đã được chứng minh** (Wiles, 1995, cùng Taylor; tính modular cho đường cong elliptic semistable cộng với định lý Ribet). Vấn đề đã khép lại; định lý modular đầy đủ được hoàn thành về sau bởi những người khác.

### Phát biểu cốt lõi

Không có số nguyên dương $$a,b,c,n$$ nào với $$n>2$$ thỏa $$a^n+b^n=c^n$$. Ý tưởng hiện đại: đường cong Frey từ một nghiệm giả định sẽ là một đường cong elliptic semistable không modular, mâu thuẫn với tính modular của Wiles–Taylor cùng định lý Ribet.

### Các định nghĩa cần nắm chắc

- **Đường cong elliptic (nói gọn).** Đường cong bậc ba trơn $$y^2=x^3+Ax+B$$ với luật nhóm.
- **Ý tưởng đường cong Frey.** Từ $$a^n+b^n=c^n$$ lập $$y^2=x(x-a^n)(x+b^n)$$; đường cong này quá kỳ lạ để có thể là modular nếu tồn tại trường hợp không modular.

### Những hiểu lầm cần tránh

- Cho rằng Wiles đã chứng minh tính modular cho mọi đường cong elliptic vào năm 1995 (ông chứng minh trường hợp semistable cần cho FLT).
- Coi các phim tài liệu phổ biến là chứng minh.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và làm quen với cách nghiên cứu**, không thay cho chứng minh hay bài báo gốc khi cần khẳng định quan trọng. Chi tiết xếp hạng: `research/video-research/fermat-last-theorem/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile — Fermat's Last Theorem: [https://www.youtube.com/watch?v=qiNcEguuFSA](https://www.youtube.com/watch?v=qiNcEguuFSA).  
2. **Cốt lõi** — Numberphile — Bridges to Fermat's Last Theorem (Ken Ribet): [https://www.youtube.com/watch?v=nUN4NDVIfVI](https://www.youtube.com/watch?v=nUN4NDVIfVI).  
3. **Phụ** — Numberphile Podcast — FLT with Ken Ribet: [https://www.youtube.com/watch?v=NPOw4iIxN6o](https://www.youtube.com/watch?v=NPOw4iIxN6o).  

**Nhắc tình trạng:** **Đã được chứng minh** (Wiles, 1995, cùng Taylor; tính modular cho đường cong elliptic semistable cộng với định lý Ribet). Vấn đề đã khép lại; định lý modular đầy đủ được hoàn thành về sau bởi những người khác.

---


### Transcript và khung hình (trích theo lô)

Transcript caption và unit theo thời gian: `research/video-research/fermat-last-theorem/transcripts/` · trạng thái: `research/video-research/fermat-last-theorem/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/fermat-last-theorem_qiNcEguuFSA_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói nghiên cứu để biết mốc thời gian).*

## Tài liệu

1. Wiles (1995). Modular elliptic curves and Fermat's Last Theorem. *Annals of Mathematics*.
2. Taylor & Wiles (1995). Ring-theoretic properties of certain Hecke algebras.
3. Ribet — hạ level và giả thuyết ε của Serre.
4. Hellegouarch, Frey — dựng đường cong từ nghiệm của FLT.
5. Sách dễ tiếp cận: Singh — *Fermat's Enigma*; Edwards; các bài tổng quan nâng cao hơn về tính modular.
6. Trong khóa học: bài lý thuyết số hiện đại ở chương 2.

---


Danh mục URL đầy đủ: `research/video-research/fermat-last-theorem/references.md`.

### Video (lộ trình gợi ý)

- Numberphile — Fermat's Last Theorem (ORIENTATION): https://www.youtube.com/watch?v=qiNcEguuFSA
- Numberphile — Bridges to Fermat's Last Theorem (Ken Ribet) (CORE): https://www.youtube.com/watch?v=nUN4NDVIfVI
- Numberphile Podcast — FLT with Ken Ribet (SECONDARY): https://www.youtube.com/watch?v=NPOw4iIxN6o

### Bài báo và web (từ gói nghiên cứu)

- Wikipedia — Wiles's proof of Fermat's Last Theorem: https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem
- Wikipedia — Fermat's Last Theorem: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem
- Cambridge Maths feature — 30 years since announcement: https://www.maths.cam.ac.uk/features/fermats-last-theorem-history-new-mathematics
- Wiles, Modular elliptic curves and Fermat's Last Theorem, Annals 1995 (paywall/library): https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem
- Numberphile podcast page: https://www.numberphile.com/videos/podcast-ken-ribet
- Clay / public expositions of modularity idea: https://en.wikipedia.org/wiki/Modularity_theorem

### Khóa học

- Gói: `research/video-research/fermat-last-theorem/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- Học luật nhóm elliptic và các ví dụ dạng modular đầu tiên ($$\Delta$$, Eisenstein) trong một khóa số học nhập môn.
- So sánh chiếc cầu của FLT với chiếc cầu PDE của Poincaré (chuyển giao phương pháp).
- Tìm hiểu "semistable" nghĩa là gì và vì sao đường cong Frey nằm trong phạm vi định lý của Wiles.
- Ghi lại một câu hỏi chính xác mà bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước** — [Fermat's Last Theorem - Numberphile](https://www.youtube.com/watch?v=qiNcEguuFSA) — Numberphile, tiếng Anh. Video định hướng cho mục tiêu của bài: phát biểu chính xác FLT và kiểm các trường hợp nhỏ n=3,4 như mốc lịch sử.
- [The Bridges to Fermat's Last Theorem - Numberphile](https://www.youtube.com/watch?v=nUN4NDVIfVI) — Numberphile, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ.
- [Fermat's Last Theorem (with Ken Ribet) - Numberphile Podcast](https://www.youtube.com/watch?v=NPOw4iIxN6o) — Numberphile2, tiếng Anh. Góc nhìn bổ sung sau hai video đầu.
