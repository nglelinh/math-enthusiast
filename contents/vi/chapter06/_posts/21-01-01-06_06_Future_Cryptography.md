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

Mật mã là toán học của **giao tiếp trong môi trường có đối thủ**: tính toán và tương tác sao cho bí mật được giữ, tính xác thực đứng vững, và giao thức vẫn đúng khi có bên gian lận. Hệ mật khóa công khai cổ điển bảo vệ phần lớn internet nhờ các giả thiết khó về số học, như phân tích thừa số và logarit rời rạc. Ta **tin** là chúng khó với máy tính cổ điển, và **biết** là chúng bị phá trong thời gian đa thức bởi một máy lượng tử chịu lỗi đủ lớn, qua thuật toán Shor. Vì vậy “mật mã cho tương lai” không phải một mốt nhất thời; đó là một cuộc chuyển đổi kỹ thuật được dẫn dắt bởi định lý, phép quy dẫn (reduction) và phân tích mật mã.

Bài này tách riêng các nhóm: nguyên thủy **đối xứng**, giả thiết **khóa công khai**, các ứng viên **hậu lượng tử**, **QKD**, và các giao thức nâng cao (ZK, FHE, MPC), với một lưu ý xuyên suốt: ta chứng minh được điều gì, *dựa trên* giả thiết nào.

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

Mã khối, mã dòng, hàm băm và MAC bảo vệ lượng dữ liệu lớn sau khi hai bên đã có khóa. Người ta không biết AES hay họ hàm băm SHA bị sụp đổ kiểu Shor như bài toán phân tích thừa số. Grover tăng tốc bậc hai cho việc tìm kiếm vét cạn, nên trong một số mô hình đe dọa người ta khuyến nghị khóa dài hơn (ví dụ AES-256 thay cho AES-128).

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

Việc NIST chuẩn hóa (và các quy trình tương đương ở từng quốc gia) là một quá trình kéo dài nhiều năm, gồm phân tích mật mã và đánh giá kỹ thuật, không phải một cuộc thi toán thuần túy. Việc chọn tham số phải cân bằng giữa ước lượng độ an toàn, kích thước khóa và hiệu năng. “Lattice” không tự động an toàn: tham số sai, triển khai yếu hay một thuật toán mới vẫn có thể phá được.

Nền tảng toán học gồm hình học số, đại số số (lattice module), lý thuyết mã, và phép quy dẫn từ trường hợp trung bình về trường hợp xấu nhất cho LWE (Regev và các công trình tiếp theo), một trong những kết quả đẹp nhất của mật mã lý thuyết hiện đại.

---

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

**Zero-knowledge:** chứng minh một phát biểu là đúng mà không để lộ chứng cứ (ngoài những hệ quả logic của chính phát biểu), theo mô hình mô phỏng. Các chứng minh ngắn hiện đại là nền cho blockchain và các ứng dụng riêng tư; nhưng giả thiết mật mã, bước thiết lập đáng tin (ở một số hệ) và lỗi triển khai vẫn là nguy cơ.

**FHE:** tính trực tiếp trên bản mã: $$\mathsf{Dec}(f(\mathsf{Enc}(x)))=f(x)$$ với một lớp hàm $$f$$ rộng. Đột phá dựa trên lattice (Gentry và các thế hệ sau); chi phí vẫn còn cao với nhiều ứng dụng, dù đang được cải thiện.

**MPC:** nhiều bên cùng tính một hàm chung mà không lộ đầu vào của mình ngoài kết quả. Các mô hình đa số trung thực và đa số không trung thực dùng những công cụ khác nhau (chia sẻ bí mật, mạch garbled, OT).

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

## Bài tập

1. Ghép: bảo mật dữ liệu lớn / trao đổi khóa / chống chối bỏ với: mã đối xứng / KEM / chữ ký.
2. Viết ba câu: vì sao bí mật dài hạn khiến phải chuyển sang PQC trước khi có máy lượng tử lớn.
3. Viết một đoạn so sánh Shor và Grover (mật mã công khai và mật mã đối xứng).
4. Phép quy dẫn từ LWE đến một hệ mật cho thấy điều gì và không cho thấy điều gì?
5. Tự dựng lại bảng so sánh QKD và PQC từ trí nhớ.
6. Kể một câu chuyện ZK đơn giản: chứng minh “tôi biết tiền ảnh của một giá trị băm”.
7. Nhận xét một tuyên bố “quantum-safe” của nhà cung cấp: còn thiếu những gì?

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
