---
layout: post
title: "Thông tin Lượng tử"
chapter: '06'
order: 3
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Suốt bảy thập niên qua, mọi bức ảnh bạn chụp, mọi dòng tin nhắn bạn gửi đi, và cả mô hình AI phức tạp nhất đều được dựng nên từ một viên gạch duy nhất: **bit cổ điển** — hoặc $$0$$, hoặc $$1$$, giống như một công tắc đèn chỉ có hai trạng thái bật và tắt. Nhưng vào những năm 1980, Richard Feynman đặt ra một câu hỏi ngược đời: nếu tự nhiên ở tầng vi mô vận hành theo cơ học lượng tử chứ không phải cơ học cổ điển, thì điều gì xảy ra khi ta dùng chính một hệ lượng tử làm đơn vị mang thông tin?

Câu trả lời mở ra cả một thế giới mới: **qubit**. Không còn là một công tắc hai nấc, qubit là một vector đơn vị trong không gian phức hai chiều $$\mathbb{C}^2$$, nơi hai trạng thái $$0$$ và $$1$$ có thể chồng chập với biên độ là *số phức*, có thể cộng hưởng tăng cường hoặc triệt tiêu lẫn nhau như sóng nước. Và khi ghép nhiều qubit lại, không gian trạng thái không cộng lại mà nhân lên theo **tích tensor**, mở đường cho hiện tượng kỳ lạ nhất của tự nhiên: **vướng víu lượng tử** (entanglement).

Chồng chập, vướng víu và phép đo hoàn toàn không phải phép thuật khoa học viễn tưởng. Chúng là những cấu trúc trong sáng của đại số tuyến tính và xác suất, đi kèm những định lý rõ ràng, các kết quả cấm bất khả xâm phạm và những hệ quả thuật toán chấn động. Bài này giúp bạn **đọc tỉnh táo vùng biên** của khoa học thông tin lượng tử: đâu là toán học vững chắc, đâu là lộ trình kỹ thuật đầy thách thức, và đâu chỉ là lời thổi phồng kiểu “thượng đẳng lượng tử” hay “AI lượng tử”.

---

## Bản đồ kiến thức nền: Thông tin lượng tử là gì và nghiên cứu những gì?

Nếu lý thuyết thông tin cổ điển của Shannon nghiên cứu cách nén, truyền và bảo vệ các chuỗi bit $$0/1$$ qua kênh nhiễu, thì **Khoa học Thông tin Lượng tử** (Quantum Information Science) đặt lại đúng những câu hỏi đó khi vật mang tin tuân theo định luật lượng tử. Bạn không cần học trước cơ học lượng tử vật lý để nắm trục xương sống toán học của ngành này — cốt lõi của nó đứng trên **bốn trụ cột**:

1. **Hình học trạng thái & tiến hóa (Đại số tuyến tính trên $$\mathbb{C}$$):** Một qubit là vector đơn vị trong $$\mathbb{C}^2$$; $$n$$ qubit sống trong không gian khổng lồ $$\mathbb{C}^{2^n}$$. Các phép biến đổi (cổng lượng tử) là ma trận unitary bảo toàn độ dài, giống như phép xoay trong không gian phức.
2. **Thuật toán lượng tử (Giao thoa biên độ & Độ phức tạp):** Điểm mạnh của máy tính lượng tử không phải là "thử mọi đáp án cùng lúc", mà là thiết kế phép xoay sao cho các nhánh sai **giao thoa triệt tiêu** (như hai con sóng ngược pha gặp nhau thành phẳng lặng), còn nhánh đúng **giao thoa cộng hưởng** để khi đo ta trúng đáp án với xác suất cao.
3. **Sửa sai lượng tử (Mã hóa trên không gian Hilbert):** Qubit ngoài đời rất mong manh — chỉ một rung động nhiệt nhỏ cũng làm mất pha (decoherence). Khác với bit cổ điển có thể chép thành 3 bản để bỏ phiếu đa số, định lý không nhân bản cấm ta sao chép qubit. Ngành sửa sai lượng tử tìm cách "trải" một qubit logic vào trạng thái vướng víu của nhiều qubit vật lý để phát hiện lỗi mà không cần đọc trực tiếp trạng thái.
4. **Truyền thông & mật mã lượng tử:** Dùng vướng víu và phép đo để phân phối khóa bí mật (QKD) sao cho mọi nỗ lực nghe lén đều để lại dấu vết thống kê không thể che giấu.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Biểu diễn qubit như một vector đơn vị trong $$\mathbb{C}^2$$; đo trong một cơ sở trực chuẩn để ra xác suất.
- Giải thích cấu trúc **tích tensor**, và vì sao vướng víu không đơn thuần là tương quan giữa các bit đã được định sẵn như trong cổ điển.
- Nêu được, ở mức khẩu hiệu kèm công thức, Shor và Grover làm được gì và *không* khẳng định điều gì.
- Mô tả vì sao cần **sửa sai lượng tử**, và rào cản decoherence; không coi máy NISQ là máy giải được mọi bài toán.
- Phân biệt **QKD** với mật mã hậu lượng tử cổ điển (PQC).
- Nhận xét một tuyên bố phổ thông theo ba loại: định lý, thí nghiệm hay lộ trình. Đừng để lời quảng cáo lẫn vào định lý.

**Kiến thức nền.** Số phức, tích vô hướng, xác suất cơ bản. Biết đại số tuyến tính thì càng tốt; không cần học cơ học lượng tử trước.

---

## 1. Trạng thái: không gian Hilbert, không có gì huyền bí

Trạng thái thuần của một qubit:

$$
\lvert\psi\rangle = \alpha\lvert 0\rangle + \beta\lvert 1\rangle,
\qquad
\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1.
$$

$$\lvert 0\rangle,\lvert 1\rangle$$ là cơ sở trực chuẩn của $$\mathbb{C}^2$$. Pha toàn cục $$e^{i\phi}\lvert\psi\rangle$$ không làm thay đổi trạng thái thuần; nhưng **pha tương đối** giữa $$\alpha$$ và $$\beta$$ lại quyết định toàn bộ hiện tượng giao thoa. Khi có nhiễu, trạng thái là trạng thái hỗn hợp, được mô tả bằng **toán tử mật độ**: ma trận Hermitian nửa xác định dương, có vết bằng 1.

Đo trong cơ sở tính toán cho kết quả $$0$$ hoặc $$1$$ với xác suất bằng bình phương môđun của biên độ (quy tắc Born); sau một phép đo lý tưởng, trạng thái trở thành vector cơ sở tương ứng. Đo trong cơ sở khác sẽ cho thống kê khác. Nói gọn: biên độ là số phức, còn xác suất là bình phương môđun của nó.

**Tiến hóa unitary.** Giữa hai lần đo, hệ kín tiến hóa theo một ma trận $$U$$ thỏa $$U^\dagger U=I$$. Cổng lượng tử là (xấp xỉ) một ma trận unitary; ghép các cổng nối tiếp là nhân ma trận, còn các dây chạy song song là tích tensor.

**Một ví dụ trực quan về giao thoa.** Xét cổng Hadamard $$H = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$$. Nếu bạn bắt đầu từ $$\lvert 0\rangle$$ và áp dụng $$H$$ một lần, bạn thu được $$\frac{1}{\sqrt{2}}(\lvert 0\rangle + \lvert 1\rangle)$$ — đo lúc này sẽ ra $$0$$ hoặc $$1$$ với xác suất 50/50 như tung đồng xu. Nhưng nếu bạn *không đo* mà áp dụng $$H$$ thêm một lần nữa, trạng thái trở thành:

$$
H\Bigl(\frac{\lvert 0\rangle + \lvert 1\rangle}{\sqrt{2}}\Bigr)
= \frac{1}{2}\bigl((\lvert 0\rangle + \lvert 1\rangle) + (\lvert 0\rangle - \lvert 1\rangle)\bigr)
= \lvert 0\rangle.
$$

Hai nhánh dẫn tới $$\lvert 1\rangle$$ mang dấu trái ngược nhau ($$+1/2$$ và $$-1/2$$) nên **tự triệt tiêu hoàn toàn**, đẩy xác suất ra $$\lvert 0\rangle$$ về 100%! Một đồng xu xác suất cổ điển tung hai lần chỉ cho ra 50/50 mãi mãi; chỉ nhờ biên độ mang dấu âm (và số phức) mà phép tính lượng tử làm được điều không tưởng đó.

---

### Video ngắn: Trò chơi CHSH và giới hạn 2

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/chsh-bell-game_vi.mp4"></video>
</div>

Mọi chiến lược cổ điển cố định đều cho $$|S| = 2$$, nên không hỗn hợp nào vượt 2. Với một cặp vướng víu đo ở 0°, 90°, 45° và −45°, lý thuyết lượng tử dự đoán $$S = 2\sqrt{2} \approx 2.83$$, và các thí nghiệm Bell quan sát thấy vi phạm giới hạn 2.


### Tự tay thử: Chơi với các góc CHSH

<div class="mex-explainer" data-mex="chsh" data-lang="vi"></div>


## 2. Nhiều qubit: vướng víu

Hai qubit sống trong $$\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathbb{C}^4$$. Trạng thái tích có dạng $$\lvert\psi\rangle\otimes\lvert\phi\rangle$$; trạng thái không viết được như vậy (hoặc không phải tổ hợp lồi của các trạng thái tích, trong trường hợp hỗn hợp) là trạng thái **vướng víu**. Trạng thái Bell

$$
\lvert\Phi^+\rangle=\frac{1}{\sqrt{2}}(\lvert 00\rangle+\lvert 11\rangle)
$$

là ví dụ chuẩn. Thử kiểm tra nhanh bằng đại số: nếu $$\lvert\Phi^+\rangle = (\alpha_1\lvert 0\rangle + \beta_1\lvert 1\rangle)\otimes(\alpha_2\lvert 0\rangle + \beta_2\lvert 1\rangle)$$, thì hệ số của $$\lvert 01\rangle$$ và $$\lvert 10\rangle$$ buộc $$\alpha_1\beta_2 = 0$$ và $$\beta_1\alpha_2 = 0$$, suy ra tích $$(\alpha_1\alpha_2)(\beta_1\beta_2) = 0$$ — mâu thuẫn vì cả hệ số của $$\lvert 00\rangle$$ lẫn $$\lvert 11\rangle$$ đều bằng $$1/\sqrt{2}\neq 0$$! Về vật lý, kết quả đo ở hai phía tương quan theo cách mà không thể mô phỏng chỉ bằng ngẫu nhiên cổ điển dùng chung (như hai chiếc găng tay trái–phải bỏ vào hai hộp kín), nếu giữ ràng buộc về tính địa phương (định lý Bell và các thí nghiệm vi phạm bất đẳng thức Bell).

**Cần hiểu đúng.** Vướng víu là một tài nguyên có thể đo lường, có tỷ lệ chuyển đổi và tính “monogamy”; nó không phải “băng thông vô hạn”. Định lý không-giao-tiếp cấm dùng riêng vướng víu để gửi tin nhanh hơn ánh sáng; teleportation vẫn cần một kênh cổ điển.

---

### Khung giải thích: tự tay dựng trạng thái Bell và vượt ngưỡng cổ điển CHSH (nên đọc chậm)

Để thấy "vướng víu lượng tử" không phải là câu chuyện siêu hình mà là phép nhân ma trận $$4	imes 4$$ rất cụ thể, hãy tự tay biến hai qubit độc lập $$\lvert 00angle$$ thành trạng thái vướng víu Bell $$\lvert \Phi^+angle$$, rồi kiểm tra tại sao nó phá vỡ giới hạn $$2$$ của mọi chiến lược cổ điển.

1. **Dựng mạch Bell bằng ma trận:** Trong cơ sở $$\{\lvert 00angle, \lvert 01angle, \lvert 10angle, \lvert 11angle\}$$, trạng thái đầu là $$\lvert 00angle = (1, 0, 0, 0)^	op$$.
   - **Bước 1 — Cổng Hadamard lên qubit thứ nhất ($$H \otimes I$$):** biến $$\lvert 0angle \mapsto rac{\lvert 0angle + \lvert 1angle}{\sqrt{2}}$$ và giữ nguyên qubit thứ hai:
     $$\lvert \psi_1angle = rac{1}{\sqrt{2}}(\lvert 00angle + \lvert 10angle) = rac{1}{\sqrt{2}}(1, 0, 1, 0)^	op.$$
     Lúc này hai qubit vẫn hoàn toàn tách rời (chưa vướng víu).
   - **Bước 2 — Cổng CNOT (lật qubit 2 nếu qubit 1 bằng 1):** tác động lên $$\lvert 10angle \mapsto \lvert 11angle$$ và giữ nguyên $$\lvert 00angle$$:
     $$\mathrm{CNOT}\,\lvert \psi_1angle = egin{pmatrix}1&0&0&0\0&1&0&0\0&0&0&1\0&0&1&0\end{pmatrix}rac{1}{\sqrt{2}}egin{pmatrix}1\0\1\0\end{pmatrix} = rac{1}{\sqrt{2}}egin{pmatrix}1\0\0\1\end{pmatrix} = rac{\lvert 00angle + \lvert 11angle}{\sqrt{2}} = \lvert \Phi^+angle.$$

2. **Kiểm tra bằng tay giới hạn CHSH $$2\sqrt{2} > 2$$:**
   - **Chiến lược cổ điển:** Alice chọn hai số định sẵn $$a_0, a_1 \in \{-1, +1\}$$ và Bob chọn $$b_0, b_1 \in \{-1, +1\}$$. Xét tổ hợp
     $$S = a_0 b_0 + a_0 b_1 + a_1 b_0 - a_1 b_1 = a_0(b_0 + b_1) + a_1(b_0 - b_1).$$
     Vì $$b_0, b_1 \in \{\pm 1\}$$, một trong hai ngoặc $$(b_0 + b_1)$$ hoặc $$(b_0 - b_1)$$ bắt buộc bằng $$0$$, ngoặc còn lại bằng $$\pm 2$$. Do đó mọi chiến lược cổ điển (kể cả trộn ngẫu nhiên) luôn thỏa $$\lvert S vert \le 2$$.
   - **Chiến lược lượng tử trên cặp $$\lvert \Phi^+angle$$:** Nếu Alice đo theo góc $$lpha$$ và Bob đo theo góc $$eta$$ (quy ước góc spin trên mặt phẳng Bloch), kỳ vọng tích hai kết quả đo bằng $$E(lpha, eta) = \cos(lpha - eta)$$. Chọn đúng bốn góc trong video trên: $$lpha_0 = 0^\circ,\ lpha_1 = 90^\circ,\ eta_0 = 45^\circ,\ eta_1 = -45^\circ$$:
     - $$E(0^\circ, 45^\circ) = \cos(-45^\circ) = rac{\sqrt{2}}{2}$$,
     - $$E(0^\circ, -45^\circ) = \cos(45^\circ) = rac{\sqrt{2}}{2}$$,
     - $$E(90^\circ, 45^\circ) = \cos(45^\circ) = rac{\sqrt{2}}{2}$$,
     - $$E(90^\circ, -45^\circ) = \cos(135^\circ) = -rac{\sqrt{2}}{2}$$.
     Cộng lại theo công thức CHSH:
     $$S = rac{\sqrt{2}}{2} + rac{\sqrt{2}}{2} + rac{\sqrt{2}}{2} - \Bigl(-rac{\sqrt{2}}{2}\Bigr) = 2\sqrt{2} pprox 2.828 > 2.$$

Chỉ bằng bốn dòng lượng giác cấp ba, bạn đã tự tay chứng minh điều làm Einstein trăn trở suốt đời: tương quan lượng tử vượt hẳn mọi mô hình biến ẩn cục bộ cổ điển.

## 3. Mô hình tính toán và độ phức tạp

Mạch lượng tử là một dãy cổng unitary lấy từ một tập phổ quát, tác dụng lên các qubit khởi tạo $$\lvert 0\rangle^{\otimes n}$$, rồi đo. Lớp **BQP** được so với **BPP** và **P**. Ta tách được hai lớp này trong mô hình oracle; còn tách tuyệt đối thì gặp cùng độ khó như tách các lớp cổ điển (ta chưa biết $$\mathbf{P}\neq\mathbf{NP}$$, và cũng chưa có bản đồ đầy đủ về các quan hệ bao hàm với lớp lượng tử).

**Shor** phân tích thừa số và tính logarit rời rạc trong thời gian đa thức trên một máy lượng tử chịu lỗi lý tưởng. Ý tưởng thiên tài của Shor là biến bài toán phân tích số $$N$$ thành bài toán **tìm chu kỳ** $$r$$ của hàm mũ mô-đun $$f(x) = a^x \bmod N$$: một bài toán cổ điển đòi hỏi thử rất nhiều điểm, nhưng Biến đổi Fourier Lượng tử (QFT) lại phát hiện tần số tuần hoàn $$1/r$$ chỉ trong vài bước nhờ giao thoa biên độ. Hệ quả: RSA, Diffie–Hellman trên trường hữu hạn và ECC phổ biến sẽ bị phá *trong mô hình đó*. Điều này không có nghĩa là máy như vậy đã tồn tại hôm nay.

**Grover** tìm một phần tử trong tập không có cấu trúc kích thước $$N$$ với $$O(\sqrt{N})$$ truy vấn (và chặn dưới trong mô hình hộp đen cùng bậc). Về hình học, mỗi bước Grover xoay vector trạng thái trong một mặt phẳng 2 chiều hướng dần về phía đáp án đúng. Với $$N = 10^6$$ mục, thay vì trung bình $$500{,}000$$ lượt kiểm tra cổ điển, Grover chỉ cần khoảng $$1{,}000$$ bước. Tuy nhiên, đó là tăng tốc **bậc hai**, không phải tăng tốc mũ, cho bài toán tìm kiếm tổng quát; với thuật toán đã biết, nó không “giải bài toán NP-đầy đủ trong thời gian đa thức”.

**Mô phỏng Hamiltonian và đại số tuyến tính lượng tử.** Nhiều đề xuất ứng dụng quy về mô phỏng động lực lượng tử hoặc ước lượng tính chất của toán tử. Các thuật toán này tồn tại, kèm ước lượng tài nguyên khá chặt trong mô hình lý tưởng; còn trong thực tế, các hằng số, tỷ lệ lỗi và chi phí nạp dữ liệu mới là thứ chi phối.

---

## 4. Nhiễu, NISQ và sửa sai

Qubit vật lý luôn tương tác với môi trường. **Decoherence** kéo trạng thái chồng chập thuần về hỗn hợp cổ điển; lỗi cổng và lỗi đọc cũng tích lũy dần. **NISQ** là giai đoạn máy có quy mô trung bình (thường vài chục đến vài trăm qubit không hoàn hảo), còn nhiễu và chưa chịu lỗi đầy đủ.

**Mã sửa sai lượng tử** mã hóa thông tin logic vào trạng thái vướng víu của nhiều qubit vật lý (surface code, stabilizer, …), để lỗi cục bộ được phát hiện và sửa mà không làm hỏng trạng thái logic. Nền tảng toán học nằm ở nhóm Pauli và hình học symplectic trên trường hữu hạn. **Định lý ngưỡng** nói rằng nếu tỷ lệ lỗi dưới một ngưỡng và mô hình lỗi đủ tốt thì tính toán chịu lỗi là khả thi với chi phí phụ trội polylog. Đây là kết quả về sự tồn tại, kèm nhiều giả thiết kỹ thuật nặng.

**Cảnh báo.** Thuật toán biến phân trên máy NISQ là nghiên cứu thực nghiệm, không phải chứng minh rằng ta đã “giải xong hóa học hay tối ưu hóa”. Một tuyên bố “quantum advantage” phải nói rõ bài toán nào, đối chiếu với thuật toán cổ điển nào, sai số bao nhiêu, và bài toán đó hữu ích hay chỉ được dựng ra cho vừa.

---

## 5. Truyền thông và mật mã (phía lượng tử)

**QKD** (BB84 và các hậu duệ): kẻ nghe lén làm nhiễu thống kê của tín hiệu, với các giả thiết về vật lý và triển khai. Chứng minh an ninh là lý thuyết thông tin *trong mô hình đã nêu*; còn kênh phụ (side-channel) là bài toán của kỹ thuật và phương pháp hình thức.

**Teleportation lượng tử** chuyển một trạng thái chưa biết nhờ vướng víu cộng với liên lạc cổ điển. Nó không vận chuyển hạt vật chất và không có tín hiệu nào nhanh hơn ánh sáng.

Đừng nhầm QKD với **PQC**. PQC là thiết kế lại *các thuật toán khóa công khai cổ điển* để chống kẻ tấn công có máy lượng tử (dựa trên lattice, mã sửa lỗi, hàm băm, isogeny, và vẫn cần thận trọng). Cả hai đều nhằm bảo mật cho tương lai, nhưng mô hình đe dọa và điểm tựa tin cậy khác nhau. Xem [Mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

---

## 6. Hộp công cụ toán

| Công cụ | Vai trò |
|---------|---------|
| Không gian Hilbert, tích tensor | Không gian trạng thái của hệ ghép |
| Nhóm unitary, đại số Lie | Họ cổng liên tục; điều khiển |
| Ý tưởng C*-đại số | Hệ vô hạn; giao với QFT đại số |
| Lý thuyết biểu diễn | Đối xứng; một số phân tích thuật toán |
| Stabilizer, dạng symplectic trên $$\mathbb{F}_2$$ | Mô phỏng Clifford trên máy cổ điển; thiết kế mã |
| Mạng tensor | Trạng thái nhiều vật; co tensor và độ phức tạp |
| Ma trận ngẫu nhiên, hiện tượng tập trung | Mạch ngẫu nhiên, nhiễu điển hình, các giả thuyết về độ phức tạp |

Thông tin lượng tử vừa là **toán và khoa học máy tính lý thuyết**, vừa là vật lý thực nghiệm. Đại số tuyến tính là lối vào; độ phức tạp tính toán và lý thuyết mã đào sâu phần máy tính.

---

## 7. Định lý, thí nghiệm, lộ trình

| Loại | Ví dụ | Tình trạng |
|------|--------|------------|
| Định lý (mô hình lý tưởng) | Shor chạy trong thời gian đa thức trên máy chịu lỗi | Thuật toán và phân tích độ phức tạp |
| Kết quả cấm / cấu trúc | Không thể nhân bản trạng thái; Bell | Chứng minh dưới các tiên đề đã nêu |
| Thí nghiệm | Kiểm tra Bell; thuật toán nhỏ; tỷ lệ lỗi | Thực nghiệm, phụ thuộc thiết bị |
| Lộ trình kỹ thuật | Máy chịu lỗi quy mô lớn | R&D hợp lý, không có mốc thời gian đảm bảo |
| Quảng cáo | “Máy lượng tử sẽ thay mọi máy tính cổ điển vào năm sau” | Bỏ qua; sai về mô hình độ phức tạp và chi phí |

Đọc được vùng biên nghĩa là **không gộp các dòng này lại với nhau**.

### Ví dụ tối thiểu: bài toán Deutsch (trực giác)

Bài toán Deutsch hay Deutsch–Jozsa: phân biệt một hàm Boolean là hằng hay cân bằng với ít truy vấn hơn mức tồi nhất của thuật toán cổ điển, nhờ chồng chập và giao thoa. Điểm đáng nói không phải ứng dụng công nghiệp, mà là **thuật toán lượng tử sắp xếp thông tin bằng giao thoa**, rồi rút ra một tính chất toàn cục. Bài toán tìm chu kỳ của Shor là phiên bản mạnh hơn (biến đổi Fourier trên nhóm abel). Grover là một mẫu khác: khuếch đại biên độ. Nhận ra các mẫu này quan trọng hơn là thuộc lòng sơ đồ mạch ngay từ lần đầu.

### Vài điều về độ phức tạp lượng tử

- **BQP**: những bài toán giải hiệu quả bằng máy lượng tử, với xác suất sai bị chặn.  
- Phân tích thừa số thuộc **BQP**; quan hệ giữa **BQP** và **NP** chưa được xác định; chưa ai biết bài toán NP-đầy đủ nào nằm trong **BQP**.  
- Các tách biệt oracle cho thấy trong thế giới truy vấn, máy lượng tử thắng máy cổ điển. Điều này tạo trực giác, nhưng chưa phải chứng minh tuyệt đối về luận đề Church–Turing vật lý.  
- Người ta tin rằng việc mô phỏng mạch lượng tử tổng quát bằng máy cổ điển là khó, và đó là nền cho mối quan tâm về mật mã và các giả thuyết, nhưng “được tin là khó” không phải định lý.

### Hoạt động nhóm

Trong 20 phút: (1) mỗi nhóm viết một tuyên bố báo chí về “AI lượng tử”; (2) gắn nhãn cho từng mệnh đề chính: *định lý / thí nghiệm / lộ trình / quảng cáo*; (3) nêu một câu hỏi đo được (tỷ lệ lỗi? kích thước bài toán? thuật toán đối chứng?) mà bài báo nên trả lời nhưng thường bỏ qua. Trình bày 3 phút; cả lớp bỏ phiếu xem nên trích dẫn hay cần xem xét lại.

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|-----------|
| “Chồng chập là thử mọi đáp án cùng một lúc.” | Các biên độ giao thoa với nhau; ta không đọc được “miễn phí” kết quả của mọi nhánh. |
| “Vướng víu là nhắn tin nhanh hơn ánh sáng.” | Sai; teleportation cần thêm kênh cổ điển. |
| “Grover giải bài toán NP-đầy đủ một cách hiệu quả.” | Không, với những gì ta biết hiện nay. |
| “Shor đã phá RSA trên internet.” | Chưa có máy đủ mạnh để phá mật mã được công bố. |
| “Thuật toán biến phân trên NISQ đã chứng minh tối ưu hóa hóa học.” | Đó là nghiên cứu thực nghiệm; thuật toán cổ điển cạnh tranh rất mạnh. |
| “AI lượng tử ⇒ AGI.” | Chỉ là lời quảng cáo; không có định lý nào như vậy. |

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**Khung toán học đã chín muồi** (trạng thái, kênh, vướng víu), trong khi **ranh giới kỹ thuật** (chịu lỗi, thuật toán NISQ) vẫn đang mở. Shor và Grover là định lý trong mô hình mạch; khả năng mở rộng quy mô vật lý thì còn là thực nghiệm.

### Phát biểu cốt lõi

Trạng thái qubit $$|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$$ trong $$\mathbb{C}^2$$; hệ nhiều phần dùng tích tensor. Tiến hóa unitary và các phép chiếu đo. Định lý không nhân bản là một định lý; tính phi địa phương Bell đã được xác nhận bằng thực nghiệm.

### Định nghĩa cần nhớ

- **Qubit.** Vector đơn vị trong $$\mathbb{C}^2$$ sai khác một pha toàn cục; trạng thái hỗn hợp dùng ma trận mật độ.
- **Vướng víu.** Trạng thái nhiều phần không phải trạng thái tích; không thể viết thành $$|\psi\rangle\otimes|\phi\rangle$$.

### Cần phân biệt rõ

- Nghĩ rằng phép đo “tính ra mọi đáp án cùng lúc”, mà bỏ qua cấu trúc của bước đọc kết quả và xử lý sau đó.
- Nhầm QKD với mật mã cổ điển hậu lượng tử.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Cốt lõi**: Michael Nielsen, Quantum computing for the determined (danh sách phát): [https://www.youtube.com/playlist?list=PL1826E60FD05B44E4](https://www.youtube.com/playlist?list=PL1826E60FD05B44E4).  
2. **Định hướng**: Veritasium, How does a quantum computer work?: [https://www.youtube.com/watch?v=g_IaVepNDT4](https://www.youtube.com/watch?v=g_IaVepNDT4).  
3. **Định hướng**: Veritasium, How to make a quantum bit: [https://www.youtube.com/watch?v=zNzzGgr2mhk](https://www.youtube.com/watch?v=zNzzGgr2mhk).  
4. **Nền tảng**: Ronald de Wolf, Intro to Quantum Computing (bài 1): [https://www.youtube.com/watch?v=MvSYyxZcAr8](https://www.youtube.com/watch?v=MvSYyxZcAr8).  

**Lưu ý về hiện trạng:** khung toán học về trạng thái, kênh và vướng víu đã chín muồi; phần kỹ thuật (chịu lỗi, thuật toán NISQ) vẫn là biên giới nghiên cứu. Shor và Grover là định lý trong mô hình mạch, còn khả năng mở rộng quy mô vật lý mới ở mức thực nghiệm.

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/quantum-information_g_IaVepNDT4_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Nielsen & Chuang — *Quantum Computation and Quantum Information*.
2. Preskill — ghi chú về NISQ; các bài luận về tính toán lượng tử.
3. Shor (1994/1997); Grover (1996).
4. Bài khảo sát về sửa sai và surface code (Gottesman; Fowler và cộng sự, cùng các bài tổng quan sau này).
5. [Mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) (để đối chiếu cách nhận ra lời thổi phồng).

---

### Video (lộ trình gợi ý)

- Michael Nielsen, Quantum computing for the determined (danh sách phát) (cốt lõi): https://www.youtube.com/playlist?list=PL1826E60FD05B44E4
- Veritasium, How does a quantum computer work? (định hướng): https://www.youtube.com/watch?v=g_IaVepNDT4
- Veritasium, How to make a quantum bit (định hướng): https://www.youtube.com/watch?v=zNzzGgr2mhk
- Ronald de Wolf, Intro to Quantum Computing (bài 1) (nền tảng): https://www.youtube.com/watch?v=MvSYyxZcAr8

### Bài báo và web

- Nielsen & Chuang — Quantum Computation and Quantum Information: https://en.wikipedia.org/wiki/Quantum_Computation_and_Quantum_Information
- Wikipedia — Quantum information: https://en.wikipedia.org/wiki/Quantum_information
- Wikipedia — Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm
- OSU QIS prep resources (video list): https://u.osu.edu/quantinfo/research/researchprep/
- Wikipedia — Qubit: https://en.wikipedia.org/wiki/Qubit

## Hướng đi tiếp

- Cặp bài về bảo mật: bài này và [Mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).
- [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) cho bản đồ về BQP.
- Thực hành: mô phỏng mạch Bell hai qubit (statevector) và đo tương quan.
- Đọc: phần trạng thái và phép đo trong Nielsen–Chuang, rồi Shor ở mức tổng quan, rồi một bài khảo sát hiện đại về sửa sai.
- Từ vựng của riêng bạn: *trạng thái, unitary, vướng víu, hỗn hợp, chịu lỗi, tách biệt oracle*.

## Video tham khảo

- **Xem trước** — [How Does a Quantum Computer Work?](https://www.youtube.com/watch?v=g_IaVepNDT4) — Veritasium, tiếng Anh. Xem trước để có hình dung chung về qubit và cách đo cho ra xác suất.
- [How To Make a Quantum Bit](https://www.youtube.com/watch?v=zNzzGgr2mhk) — Veritasium, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để thấy qubit được tạo ra về mặt vật lý như thế nào.
