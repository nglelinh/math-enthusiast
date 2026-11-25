---
layout: post
title: "Mật mã (Tiên phong)"
chapter: '06'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Mỗi lần bạn mở trình duyệt và thấy biểu tượng ổ khóa nhỏ bên cạnh địa chỉ ngân hàng, toàn bộ phiên giao dịch đó đang đứng trên một niềm tin toán học: rằng nhân hai số nguyên tố khổng lồ thì mất một phần triệu giây, nhưng làm ngược lại — phân tích tích đó ra hai thừa số nguyên tố — sẽ khiến mọi siêu máy tính cổ điển mất hàng triệu năm. Suốt gần nửa thế kỷ, hệ mật khóa công khai (RSA, Diffie–Hellman, ECC) đã bảo vệ hầu như toàn bộ internet bằng chính sự bất đối xứng tuyệt đẹp ấy.

Thế nhưng vào năm 1994, Peter Shor chỉ ra một vết nứt sâu trong nền móng đó: nếu một ngày con người xây dựng được máy tính lượng tử chịu lỗi đủ lớn, thuật toán Shor sẽ phá vỡ bài toán phân tích thừa số và logarit rời rạc trong thời gian đa thức. Điều đáng lo không chỉ là ngày mai có máy lượng tử hay chưa, mà là kẻ tấn công có thể **thu thập dữ liệu mã hóa ngay hôm nay và đợi mười lăm năm sau mới giải mã**. Bởi vậy, “mật mã cho tương lai” không phải một trào lưu tiếp thị; đó là cuộc di cư hạ tầng lớn nhất trong lịch sử an ninh mạng, được dẫn dắt bởi định lý, phép quy dẫn (reduction) và phân tích mật mã nghiêm ngặt.

**Mật mã học** là toán học của **giao tiếp trong môi trường có đối thủ**: làm sao để bí mật được giữ kín, danh tính được xác thực, và thậm chí nhiều bên không tin nhau vẫn tính toán chung được kết quả đúng. Bài này tách bạch rõ các lớp của bức tranh hiện đại: nguyên thủy **đối xứng**, mật mã **khóa công khai**, các họ **hậu lượng tử (PQC)**, **QKD**, và những giao thức tưởng như phép thuật như **ZK, FHE, MPC** — luôn kèm câu hỏi cốt lõi: ta chứng minh được điều gì, và *dựa trên* giả thiết nào?

---

## Kiến thức cần nhớ: Mật mã hậu lượng tử là gì và nghiên cứu những gì?

Nếu bạn đã quen với đại số tuyến tính và số học cơ bản, bạn có thể nắm ngay bức tranh của **Mật mã Học Hiện Đại & Hậu Lượng Tử** (Modern & Post-Quantum Cryptography) qua **bốn câu hỏi cốt lõi**:

1. **Tìm bài toán "khó ngay cả với máy lượng tử" (Lattice, Mã sửa lỗi, Hàm băm):** Thuật toán Shor chỉ giỏi tìm *chu kỳ ẩn* trên nhóm abel (như số học modulo trong RSA hay đường cong elliptic). Mật mã hậu lượng tử (PQC) chuyển sang những bài toán hình học và tổ hợp không có cấu trúc tuần hoàn kiểu đó — nổi bật nhất là **mạng tinh thể chiều cao (lattice)**, nơi việc tìm một vector ngắn trong lưới 500–1000 chiều hoặc giải hệ phương trình tuyến tính bị trộn thêm một chút nhiễu nhỏ (LWE) được tin là khó với cả máy cổ điển lẫn máy lượng tử.
2. **Chứng minh bằng phép quy dẫn (Provable Security):** Trong mật mã, ta hiếm khi chứng minh tuyệt đối rằng "không ai phá được". Thay vào đó, ta chứng minh: *nếu* có kẻ phá được hệ mật của tôi, tôi có thể dùng chính kẻ đó làm hộp đen để giải một bài toán toán học nổi tiếng là khó.
3. **Giao thức bảo mật nâng cao (ZK, FHE, MPC):** Vượt xa chuyện "khóa hộp gửi thư", mật mã biên giới hỏi những câu tưởng như nghịch lý: làm sao chứng minh tôi biết mật khẩu mà không hé lộ một bit nào của nó (Zero-Knowledge)? Làm sao nhờ máy chủ đám mây tính toán trên dữ liệu *đang bị mã hóa* mà máy chủ không đọc được nội dung (FHE)?
4. **Cầu nối từ toán học đến phần cứng (Side-Channel & Crypto-Agility):** Một định lý hoàn hảo vẫn có thể sụp đổ ngoài đời thực nếu chip xử lý mất thêm vài nano giây khi xử lý bit `1` so với bit `0`. Vì vậy mật mã hiện đại vừa là đại số và độ phức tạp, vừa là kỹ thuật chống rò rỉ kênh phụ.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Phân biệt mã đối xứng (khóa chung) với mã khóa công khai và chữ ký, ở mức vai trò trong giao thức.
- Giải thích vì sao RSA và ECC bị Shor đe dọa, trong khi mã đối xứng tốt chủ yếu chỉ chịu ảnh hưởng của Grover (chỉnh độ dài khóa), nên không thể thổi phồng cả hai phía như nhau.
- Kể tên các họ **PQC** chính (lattice, mã sửa lỗi, hàm băm, đa biến, isogeny, và vẫn phải thận trọng) và các phép quy dẫn an ninh nhắm tới điều gì.
- So sánh **QKD** và **PQC**.
- Nêu, ở mức không hình thức, ZK, FHE, MPC cho phép làm gì, và vì sao hiệu năng cùng các giả thiết đi kèm quan trọng.
- Nhận xét nhãn “quantum-safe” khi thiếu tham số, chứng minh hoặc phân tích kênh phụ.

**Kiến thức nền.** Số học modulo; xác suất cơ bản; vài khẩu hiệu về độ phức tạp. Xem bài về độ phức tạp để hiểu sâu hơn về các lớp.

---

## 1. Mục tiêu và mô hình đe dọa

Một hệ mật gồm **thuật toán** cùng **mô hình đe dọa**: đối thủ thấy được gì (chỉ bản mã? hay cả bản rõ do họ chọn?), làm được gì (truy vấn trực tuyến? có máy lượng tử?), và thế nào thì gọi là bị phá (khôi phục khóa, phân biệt được bản mã, hay giả mạo một chữ ký).

An ninh được chứng minh thường có dạng quy dẫn: *nếu* phá được hệ mật *thì* phá được một bài toán khó đã được đặt tên (ví dụ LWE) với tài nguyên tương đương. Phép quy dẫn có thể chặt hoặc lỏng; mô hình có thể lý tưởng hóa (random oracle). An ninh **dựa trên kinh nghiệm** (đã chịu được phân tích mật mã) vẫn thiết yếu, vì giả thiết có thể sai và mô hình có thể bỏ sót kênh phụ.

---

## 2. Mật mã đối xứng: vẫn là xương sống

Mã khối, mã dòng, hàm băm và MAC bảo vệ lượng dữ liệu lớn sau khi hai bên đã có khóa. Người ta không biết AES hay họ hàm băm SHA bị sụp đổ kiểu Shor như bài toán phân tích thừa số. Grover tăng tốc bậc hai cho việc tìm kiếm vét cạn, nên trong một số mô hình đe dọa người ta khuyến nghị khóa dài hơn (ví dụ AES-256 thay cho AES-128 — tăng gấp đôi độ dài khóa là đủ triệt tiêu lợi thế căn bậc hai của Grover).

Mã đối xứng không tự giải quyết việc phân phối khóa, nên mới có mật mã công khai và QKD. Các tấn công vào khâu triển khai (đo thời gian, đo năng lượng, gây lỗi) phá được hệ thống mà không phá nguyên thủy toán học.

---

## 3. Mật mã công khai và cú đánh từ máy lượng tử

RSA dựa trên giả thiết liên quan đến phân tích thừa số; Diffie–Hellman và ECC dựa trên logarit rời rạc trong các nhóm được chọn cẩn thận. Shor giải chúng trong thời gian đa thức trên máy lượng tử chịu lỗi. Bí mật cần giữ lâu dài, cộng với kiểu tấn công “thu thập bây giờ, giải mã sau”, thúc đẩy việc **chuyển sang PQC sớm**, trước khi máy lượng tử lớn xuất hiện.

Định lý nói về độ phức tạp tiệm cận trong mô hình lượng tử; còn quản trị rủi ro dựa vào lộ trình kỹ thuật và thời gian bí mật cần được giữ. Ở đây toán học của thuật toán gặp lộ trình công nghệ.

---

## 4. Mật mã hậu lượng tử (PQC)

| Họ | Trực giác về độ khó (không hình thức) | Ghi chú |
|----|---------------------------------------|---------|
| Lattice (Kyber/ML-KEM, Dilithium/ML-DSA…) | Vector ngắn / LWE / Module-LWE | NIST chọn; nền tảng nghiên cứu mạnh |
| Mã sửa lỗi | Giải mã một mã tuyến tính ngẫu nhiên | McEliece; khóa lớn |
| Chữ ký dựa trên hàm băm | An ninh của hàm băm | Bảo thủ; loại có trạng thái và không trạng thái |
| Đa biến | Hệ đa thức bậc hai | Lịch sử nhiều biến động (một số đề xuất đã bị phá); cần phân tích kỹ |
| Isogeny | Ánh xạ giữa các đường cong elliptic | Một số hệ đã bị phá (SIDH); lĩnh vực vẫn tiếp tục |

**Một ví dụ trực quan về LWE (Learning With Errors).** Nếu ai đó cho bạn một hệ phương trình tuyến tính sạch sẽ $$A s = b \pmod{q}$$, bạn chỉ cần khử Gauss học từ năm nhất đại học là tìm ngay ra vector bí mật $$s$$ trong tích tắc. Nhưng giờ hãy cộng thêm một vector **nhiễu rất nhỏ** $$e$$ vào vế phải:

$$
b = A s + e \pmod{q}.
$$

Chỉ một chút nhiễu nhỏ ấy làm phép khử Gauss sụp đổ hoàn toàn: mỗi bước cộng trừ hàng lại khuếch đại nhiễu lên theo cấp số nhân cho tới khi mọi thông tin chìm nghỉm trong hỗn loạn. Việc tìm lại $$s$$ từ $$(A, b)$$ tương đương với việc tìm điểm lưới gần nhất trong một mạng tinh thể hàng trăm chiều — bài toán mà cho đến nay cả máy tính cổ điển lẫn máy tính lượng tử đều chưa có thuật toán hiệu quả.

Việc NIST chuẩn hóa (và các quy trình tương đương ở từng quốc gia) là một quá trình kéo dài nhiều năm, gồm phân tích mật mã và đánh giá kỹ thuật, không phải một cuộc thi toán thuần túy. Việc chọn tham số phải cân bằng giữa ước lượng độ an toàn, kích thước khóa và hiệu năng. “Lattice” không tự động an toàn: tham số sai, triển khai yếu hay một thuật toán mới vẫn có thể phá được.

Nền tảng toán học gồm hình học số, đại số số (lattice module), lý thuyết mã, và phép quy dẫn từ trường hợp trung bình về trường hợp xấu nhất cho LWE (Regev và các công trình tiếp theo), một trong những kết quả đẹp nhất của mật mã lý thuyết hiện đại.

---

### Giải thích: tự tay mã hóa và giải mã 1 bit bằng mật mã lưới LWE

Mật mã hậu lượng tử dựa trên LWE (*Learning With Errors*, nền tảng của chuẩn NIST ML-KEM) nghe có vẻ rất cao siêu, nhưng cơ chế lõi của nó chỉ dùng phép cộng, nhân số nguyên modulo $$q$$ và một chút nhiễu nhỏ. Hãy tự tay chạy trọn một phiên mã hóa – giải mã với mô-đun tí hon $$q = 17$$ (chú ý $$\lfloor q/2 \rfloor = 8$$).

1. **Tạo khóa (Bob):**
   - Bob chọn ngẫu nhiên **khóa bí mật** là một vectơ 2 chiều: $$s = \begin{pmatrix}3\\5\end{pmatrix} \in \mathbb{Z}_{17}^2$$.
   - Bob tạo **khóa công khai** gồm 3 cặp $$(a_i, b_i)$$ bằng công thức $$b_i = a_i^\top s + e_i \pmod{17}$$, trong đó nhiễu $$e_i \in \{-1, 0, 1\}$$ rất nhỏ:
     - $$a_1 = (2, 1),\ e_1 = +1 \;\Longrightarrow\; b_1 = 2(3) + 1(5) + 1 = 12 \pmod{17}$$.
     - $$a_2 = (4, 3),\ e_2 = -1 \;\Longrightarrow\; b_2 = 4(3) + 3(5) - 1 = 26 \equiv 9 \pmod{17}$$.
     - $$a_3 = (1, 6),\ e_3 = 0 \;\Longrightarrow\; b_3 = 1(3) + 6(5) + 0 = 33 \equiv 16 \pmod{17}$$.
   - Bob công bố ba cặp $$(a_i, b_i)$$, giữ kín $$s$$ và các nhiễu $$e_i$$.

2. **Mã hóa bit $$m = 1$$ (Alice gửi cho Bob):**
   - Alice chọn ngẫu nhiên một tập con các phương trình công khai, ví dụ tập $$\{1, 2\}$$, rồi cộng chúng lại và cộng thêm $$8 \cdot m$$ vào vế phải:
     $$
     u = a_1 + a_2 = (2+4,\ 1+3) = (6, 4) \pmod{17},
     $$
     $$
     v = b_1 + b_2 + 8 \cdot 1 = 12 + 9 + 8 = 29 \equiv 12 \pmod{17}.
     $$
   - Alice gửi bản mã $$(u, v) = \bigl((6, 4),\, 12\bigr)$$ qua mạng công khai.

3. **Giải mã (Bob dùng khóa bí mật $$s = (3, 5)^\top$$):**
   - Bob tính hiệu $$d = v - u^\top s \pmod{17}$$:
     $$
     u^\top s = 6(3) + 4(5) = 38 \equiv 4 \pmod{17}
     \;\Longrightarrow\;
     d = 12 - 4 = 8 \pmod{17}.
     $$
   - Vì sao lại ra gần $$8$$ (nếu $$m=1$$) hoặc gần $$0$$ (nếu $$m=0$$)? Thay biểu thức vào ta thấy ngay:
     $$
     v - u^\top s = (e_1 + e_2) + 8m = (1 - 1) + 8(1) = 8.
     $$
   - Bob kiểm tra khoảng cách vòng quanh trên $$\mathbb{Z}_{17}$$: $$d = 8$$ nằm sát $$8$$ (cách $$0$$ tới 8 đơn vị), nên kết luận chính xác **$$m = 1$$**!

**Tại sao an toàn khi tăng lên 500–1000 chiều?** Với Bob biết $$s$$, tích vô hướng $$u^\top s$$ triệt tiêu sạch phần lớn, chỉ chừa lại tổng vài số nhiễu rất nhỏ $$e_1 + e_2$$ cộng với $$8m$$. Còn với kẻ nghe lén không biết $$s$$, việc khử nhiễu để tìm $$s$$ từ hàng trăm phương trình tuyến tính nhiễu đồng nghĩa với tìm điểm lưới gần nhất trong không gian hàng trăm chiều — bài toán hiện vẫn đứng vững trước cả máy tính cổ điển lẫn thuật toán Shor.

## 5. QKD và PQC

**QKD** dùng trạng thái lượng tử để việc nghe lén gây ra nhiễu mà ta phát hiện được bằng thống kê, theo một mô hình vật lý được nêu rõ; thường vẫn cần một kênh cổ điển đã xác thực và các biện pháp chống kênh phụ. **PQC** chạy trên mạng cổ điển với thuật toán mới.

| | PQC | QKD |
|--|-----|-----|
| Kênh | Cổ điển | Lượng tử và cổ điển |
| Loại giả thiết | Độ khó tính toán | Vật lý / lý thuyết thông tin, trong mô hình đã nêu |
| Triển khai | Thư viện hoặc phần cứng mật mã | Hạ tầng quang học / lượng tử |
| Bổ sung cho nhau | Có | Có; không thay thế mọi mục tiêu mật mã |

Hai công nghệ này cùng trả lời nỗi lo về bảo mật, nhưng dựa trên **những điểm tựa tin cậy khác nhau**. Truyền thông đại chúng hay gộp chúng làm một.

---

## 6. Giao thức nâng cao: ZK, FHE, MPC

**Zero-knowledge:** chứng minh một phát biểu là đúng mà không để lộ chứng cứ (ngoài những hệ quả logic của chính phát biểu), theo mô hình mô phỏng. Hình dung cổ điển: bạn muốn chứng minh với một người bạn mù màu rằng hai quả bóng trong tay bạn có màu khác nhau. Bạn để bạn ấy giấu hai quả bóng ra sau lưng, có thể tráo tay hoặc không, rồi đưa ra trước mặt để bạn đoán xem họ vừa tráo hay giữ nguyên. Nếu hai quả bóng khác màu thật, bạn đoán đúng 100%; nếu chúng cùng màu, bạn chỉ đoán mò với xác suất $$1/2$$. Lặp lại 20 lần, xác suất ăn may tụt xuống $$2^{-20} < 10^{-6}$$, bạn ấy hoàn toàn tin hai quả bóng khác màu mà vẫn chẳng biết quả nào màu gì! Các chứng minh ngắn hiện đại (zk-SNARK, zk-STARK) nâng ý tưởng đó lên thành nền cho blockchain và ứng dụng riêng tư; nhưng giả thiết mật mã, bước thiết lập đáng tin (ở một số hệ) và lỗi triển khai vẫn là nguy cơ.

**FHE:** tính trực tiếp trên bản mã: $$\mathsf{Dec}(f(\mathsf{Enc}(x)))=f(x)$$ với một lớp hàm $$f$$ rộng. Hãy tưởng tượng một chiếc hộp găng tay khóa kín bằng kính trong suốt: bạn bỏ nguyên liệu vào hộp, khóa lại, rồi đưa cho người thợ kim hoàn (máy chủ đám mây) thò tay qua đôi găng gắn liền với hộp để chế tác thành món trang sức. Người thợ làm xong việc mà không bao giờ chạm tay hay lấy được vàng ra ngoài; chỉ bạn có chìa khóa mới mở hộp lấy kết quả. Đột phá FHE dựa trên lattice (Gentry và các thế hệ sau); chi phí vẫn còn cao với nhiều ứng dụng, dù đang được cải thiện.

**MPC:** nhiều bên cùng tính một hàm chung mà không lộ đầu vào của mình ngoài kết quả (ví dụ: năm công ty cùng tính mức lương trung bình của ngành mà không công ty nào phải tiết lộ bảng lương của riêng mình). Các mô hình đa số trung thực và đa số không trung thực dùng những công cụ khác nhau (chia sẻ bí mật, mạch garbled, OT).

Đây là **lý thuyết giao thức** đã có triển khai thật, và khoảng cách giữa “khả thi về mặt tiệm cận” với “dùng rẻ ở mọi nơi” còn rất rộng. Những lời quảng cáo kiểu “FHE giải quyết mọi vấn đề riêng tư” bỏ qua hiệu năng, rò rỉ qua mẫu truy cập và việc quản lý khóa.

---

## 7. Chuyển đổi và các bài toán mở

1. Bắt tay lai (hybrid) giữa mật mã cổ điển và PQC trong giai đoạn chuyển tiếp.  
2. Phân tích mật mã các nguyên thủy mới (bằng thuật toán cổ điển và lượng tử).  
3. Triển khai chống kênh phụ.  
4. Hợp thành giao thức: chứng minh an ninh của cả hệ từ các thành phần.  
5. Chữ ký dùng lâu dài và khả năng thay thuật toán linh hoạt (key agility).  
6. Kiểm chứng hình thức mã mật mã và các chứng minh.  
7. Đánh giá mối đe dọa lượng tử: không hoảng loạn, cũng không phủ nhận.

### Hình dung cụ thể về chuyển đổi

Một cuộc bắt tay kiểu TLS có thể thương lượng trao đổi khóa bằng đường cong elliptic **và** một KEM lattice, rồi trộn hai bí mật phiên lại để kẻ tấn công phải phá **cả hai** (hybrid). Chữ ký cập nhật phần mềm có thể chuyển sang dựa trên hàm băm hoặc lattice, với kích thước và hiệu năng khác. Với chứng chỉ, HSM, thiết bị IoT bị ràng buộc tài nguyên, chữ ký tài liệu dùng lâu dài, không có một nút “bật PQC” duy nhất.

Rủi ro **thu thập bây giờ, giải mã sau** khác nhau tùy loại dữ liệu: bí mật cần giữ 50 năm khẩn cấp hơn khóa phiên chỉ dùng vài phút. Quản trị rủi ro là tích của (giá trị bí mật) × (thời gian cần giữ) × (xác suất có máy lượng tử đủ mạnh để phá mật mã trong khoảng thời gian đó). Đó là một ước lượng kiểu Fermi, không phải định lý, nhưng tốt hơn cảm tính.

### Kênh phụ: toán học và phần cứng

Phép quy dẫn hoàn hảo vẫn thất bại nếu triển khai làm rò khóa qua thời gian chạy, cache, năng lượng tiêu thụ hay lỗi phần cứng. Mã chạy thời gian hằng, che dữ liệu (masking) và kiểm chứng hình thức là công việc an ninh hàng đầu. PQC có khóa lớn và số học mới (NTT cho lattice, ma trận lớn cho mã sửa lỗi…) nên tạo ra bề mặt kênh phụ **mới**. Cần nhớ: một hệ được NIST chọn vẫn có thể bị phá trong sản phẩm thật vì bộ sinh số ngẫu nhiên kém hoặc phép so sánh làm rò thông tin.

### Hoạt động nhóm

Lấy một tuyên bố của nhà cung cấp kiểu “quantum-safe” hoặc “quantum-ready”. Kiểm tra bằng danh sách: tên hệ mật? tham số? có chế độ lai không? mô hình đe dọa (chỉ máy lượng tử hay cả kênh phụ)? có chứng minh hoặc bài báo không? Viết ba câu phản biện cho seminar: điều gì được phép nói và điều gì không được phép nói trên slide.

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|-----------|
| “Máy lượng tử đã phá RSA ngoài đời thực.” | Chưa có vụ phá mật mã có ý nghĩa thực tế nào được công bố. |
| “AES gãy vì Shor.” | Grover ảnh hưởng đến tìm kiếm vét cạn; Shor không áp dụng như với phân tích thừa số. |
| “PQC chưa được chứng minh nên vô dụng.” | Mọi hệ khóa công khai đều dựa trên giả thiết; PQC mới hơn và đang bị soi kỹ. |
| “QKD làm mật mã khác lỗi thời.” | Phạm vi hẹp; xác thực và nhiều mục tiêu rộng hơn vẫn cần mật mã. |
| “ZK nghĩa là không lộ chút thông tin nào, theo mọi nghĩa.” | Được định nghĩa theo mô phỏng; triển khai có thể rò rỉ. |
| “NIST chuẩn hóa rồi thì an toàn vĩnh viễn.” | Giảm rủi ro; việc phân tích mật mã vẫn tiếp tục. |

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**Chuẩn đang tiến triển.** NIST đã công bố các chuẩn PQC đầu tiên (FIPS 203–205) vào năm 2024; việc chuyển đổi đang diễn ra. QKD là một chồng công nghệ khác với các thuật toán PQC cổ điển.

### Phát biểu cốt lõi

Thuật toán Shor phá RSA và ECC trên một máy lượng tử chịu lỗi lớn (định lý trong mô hình mạch). PQC đặt an ninh trên các bài toán thuộc loại lattice, mã, hàm băm, isogeny mà ta tin là khó với đối thủ lượng tử; độ khó này chỉ là *giả thuyết*, chưa được chứng minh.

### Định nghĩa cần nhớ

- **PQC.** Mật mã cổ điển được thiết kế để chống lại đối thủ lượng tử.
- **Linh hoạt thuật toán (crypto-agility).** Khả năng thay thuật toán khi chuẩn và các cuộc tấn công thay đổi.

### Cần phân biệt rõ

- Cho rằng máy lượng tử ngày nay đã phá được RSA ở quy mô thực tế.
- Đánh đồng QKD với PQC (mô hình tin cậy và cách triển khai khác nhau).

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Định hướng**: SandboxAQ, NIST's PQC Standardization Explained: [https://www.youtube.com/watch?v=crPe69NeTdk](https://www.youtube.com/watch?v=crPe69NeTdk).  
2. **Cốt lõi**: IBM Research, NIST post-quantum standards webcast: [https://www.youtube.com/watch?v=YJ00O4gBs0I](https://www.youtube.com/watch?v=YJ00O4gBs0I).  
3. **Nền tảng**: Cryptography 101, PQC Standards explained: [https://www.youtube.com/watch?v=P9g1CMCu8DI](https://www.youtube.com/watch?v=P9g1CMCu8DI).  

**Lưu ý về hiện trạng:** các chuẩn vẫn đang tiến triển. NIST đã công bố các chuẩn PQC đầu tiên (FIPS 203–205) vào năm 2024 và việc chuyển đổi đang diễn ra. QKD là một chồng công nghệ khác với các thuật toán PQC cổ điển.

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/future-cryptography_crPe69NeTdk_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Katz & Lindell — *Introduction to Modern Cryptography*.
2. Tài liệu NIST về PQC và đặc tả các thuật toán được chọn.
3. Regev — LWE; Shor — phân tích thừa số và logarit rời rạc lượng tử.
4. Bài khảo sát về FHE, ZK, MPC (Boneh–Shoup; các bài SoK gần đây).
5. [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) (cách nhận ra lời thổi phồng so với mô hình đe dọa).

---

### Video (lộ trình gợi ý)

- SandboxAQ, NIST's PQC Standardization Explained (định hướng): https://www.youtube.com/watch?v=crPe69NeTdk
- IBM Research, NIST post-quantum standards webcast (cốt lõi): https://www.youtube.com/watch?v=YJ00O4gBs0I
- Cryptography 101, PQC Standards explained (nền tảng): https://www.youtube.com/watch?v=P9g1CMCu8DI

### Bài báo và web

- NIST — What is Post-Quantum Cryptography?: https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography
- NIST PQC project: https://csrc.nist.gov/projects/post-quantum-cryptography
- Wikipedia — NIST PQC Standardization: https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization
- NIST video page — PQC Good/Bad/Powerful: https://www.nist.gov/video/post-quantum-cryptography-good-bad-and-powerful
- Wikipedia — Post-quantum cryptography: https://en.wikipedia.org/wiki/Post-quantum_cryptography
- Wikipedia — Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm

## Hướng đi tiếp

- [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) cho mô hình đe dọa đầy đủ.
- [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) cho ngôn ngữ về độ khó.
- So sánh kích thước khóa và hiệu năng giữa ECC và KEM lattice (theo bậc độ lớn, dựa trên các benchmark công khai).
- Đọc: phần lõi của Katz–Lindell, rồi NIST PQC FAQ, rồi mỗi ngày một đoạn trong bài khảo sát về LWE.
- Lập danh sách kiểm tra mô hình đe dọa trước khi tin vào cụm từ “không thể phá”.

## Video tham khảo

- **Xem trước** — [NIST's Post-Quantum Cryptography Standardization Explained](https://www.youtube.com/watch?v=crPe69NeTdk) — SandboxAQ, tiếng Anh. Xem trước để nắm quy trình chuẩn hóa PQC của NIST và vai trò của từng thuật toán.
- [The next big leap in cryptography: NIST’s post-quantum cryptography standards](https://www.youtube.com/watch?v=YJ00O4gBs0I) — IBM Research, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe góc nhìn của các nhà nghiên cứu tham gia xây dựng chuẩn.
- [PQC Standards (Post-Quantum Cryptography Explained)](https://www.youtube.com/watch?v=P9g1CMCu8DI) — Cryptography 101, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, giải thích các chuẩn bằng ví dụ dễ theo dõi.
