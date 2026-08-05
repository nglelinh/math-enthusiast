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

Mật mã là toán của **giao tiếp đối kháng**: tính toán và tương tác sao cho bí mật được giữ, tính xác thực đứng vững, giao thức còn đúng khi có bên gian. Hệ công khai cổ điển bảo vệ phần lớn internet dựa trên giả thiết khó số học—phân tích thừa số, log rời rạc—**tin** là khó với máy cổ điển và **biết** là bị phá thời gian đa thức bởi máy lượng tử fault-tolerant lớn qua thuật toán Shor. Vì thế “mật mã tương lai” không phải mốt; là di trú kỹ thuật được dẫn bởi định lý, reduction và cryptanalysis.

Bài tách primitive **đối xứng**, giả thiết **công khai**, ứng viên **hậu lượng tử**, **QKD**, và giao thức nâng cao (ZK, FHE, MPC)—với chú ý dai dẳng: chứng minh gì *tương đối với* giả thiết nào.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt mã đối xứng (khóa chung) và công khai / chữ ký ở mức vai trò giao thức.
- Giải thích vì sao RSA/ECC bị đe dọa bởi Shor, trong khi đối xứng tốt chủ yếu đụng Grover (điều chỉnh độ dài khóa)—không thổi cả hai phía.
- Nêu họ **PQC** chính (lattice, code, hash, multivariate, isogeny thận trọng) và reduction an ninh nhắm gì.
- Đối chiếu **QKD** và **PQC**.
- Nêu mức không formal ZK, FHE, MPC cho phép gì và vì sao hiệu năng/giả thiết quan trọng.
- Phê nhãn “quantum-safe” thiếu tham số, chứng minh, side-channel (**LO6**).

**Kiến thức nền.** Số học modulo; xác suất cơ bản; slogan độ phức tạp. Xem bài độ phức tạp cho độ sâu lớp.

---

## 1. Mục tiêu và mô hình đe dọa

Mật mã chỉ rõ **thuật toán** + **mô hình đe dọa**: đối thủ thấy gì (chỉ ciphertext? plaintext chọn?), làm được gì (truy vấn online? máy lượng tử?), thế nào là phá (khôi phục khóa vs phân biệt ciphertext vs giả một chữ ký).

An ninh chứng minh thường là reduction: *nếu* phá scheme *thì* phá bài toán khó đặt tên (ví dụ LWE) với tài nguyên tương đương. Reduction có thể chặt hoặc lỏng; mô hình có thể lý tưởng (random oracle). An ninh **heuristic** (sống sót cryptanalysis) vẫn thiết yếu vì giả thiết có thể sai và mô hình có thể bỏ side-channel.

---

## 2. Mật mã đối xứng: vẫn là xương sống

Block cipher, stream cipher, hash, MAC bảo vệ dữ liệu số lượng lớn khi đã có khóa. AES và hash họ SHA **không** được biết sụp kiểu Shor như factoring. Grover cho tăng tốc bậc hai tìm kiếm brute-force—khuyến nghị khóa dài hơn trong một số mô hình đe dọa (ví dụ AES-256 vs AES-128).

Đối xứng không tự giải phân phối khóa—vì thế mới có công khai và QKD. Tấn công triển khai (timing, năng lượng, fault) phá hệ mà không phá primitive toán.

---

## 3. Công khai và cú phá lượng tử

RSA dựa giả thiết liên quan factoring; Diffie–Hellman/ECC dựa log rời rạc nhóm chọn cẩn. Shor giải chúng poly-time trên QC fault-tolerant. Bí mật dài hạn + “thu hoạch nay, giải mã sau” thúc **di trú sớm** PQC—trước khi máy lớn xuất hiện.

Định lý là về độ phức tạp tiệm cận lượng tử; quản trị rủi ro là timeline kỹ thuật và tuổi thọ bí mật: toán thuật toán gặp lộ trình kỹ thuật.

---

## 4. Mật mã hậu lượng tử (PQC)

| Họ | Trực giác khó (không formal) | Ghi chú |
|----|------------------------------|---------|
| Lattice (Kyber/ML-KEM, Dilithium/ML-DSA…) | Vector ngắn / LWE / Module-LWE | NIST; nền tảng nghiên cứu mạnh |
| Code | Giải mã mã tuyến tính ngẫu nhiên | McEliece; khóa lớn |
| Hash-based signature | An ninh hash | Bảo thủ; stateful vs stateless |
| Multivariate | Hệ đa thức bậc hai | Lịch sử lẫn; cryptanalysis cẩn |
| Isogeny | Ánh xạ giữa đường cong elliptic | Một số scheme đã gãy (SIDH); lĩnh vực tiếp |

Chuẩn hóa NIST (và tương đương quốc gia) là quy trình cryptanalysis + kỹ thuật nhiều năm—không phải cuộc thi toán thuần. Tham số cân ước lượng an ninh, kích thước khóa, hiệu năng. “Lattice” không tự động an toàn: tham số sai, triển khai yếu, thuật toán mới vẫn có thể phá.

Nền tảng toán: hình học số, đại số số (module lattice), lý thuyết mã, reduction average-case ↔ worst-case cho LWE (Regev và hậu duệ)—viên ngọc của mật mã lý thuyết hiện đại.

---

## 5. QKD vs PQC

**QKD** dùng trạng thái lượng tử để nghe lén nhiễu thống kê, phát hiện dưới mô hình vật lý nêu rõ; thường vẫn cần kênh cổ điển xác thực và kỹ thuật chống side-channel. **PQC** chạy trên mạng cổ điển với thuật toán mới.

| | PQC | QKD |
|--|-----|-----|
| Kênh | Cổ điển | Lượng tử + cổ điển |
| Kiểu giả thiết | Khó tính toán | Vật lý/thông tin-lý thuyết trong mô hình |
| Triển khai | Thư viện/phần cứng crypto | Hạ tầng quang/lượng tử |
| Bổ sung nhau | Có | Có—không thay mọi mục tiêu crypto |

Chúng trả lời lo âu bảo mật liên quan với **neo tin cậy khác**. Truyền thông đại chúng hay trộn hai thứ này.

---

## 6. Giao thức nâng cao: ZK, FHE, MPC

**Zero-knowledge:** chứng minh phát biểu đúng mà không lộ witness (ngoài hệ quả logic của phát biểu)—theo paradigm simulation. Proof ngắn hiện đại nuôi blockchain/privacy; giả thiết crypto, setup tin cậy (một số hệ), lỗi triển khai vẫn nguy.

**FHE:** tính trên bản mã: $$\mathsf{Dec}(f(\mathsf{Enc}(x)))=f(x)$$ cho lớp $$f$$ rộng. Đột phá lattice (Gentry và thế hệ sau); chi phí còn cao cho nhiều ứng dụng, dù đang cải thiện.

**MPC:** nhiều bên tính hàm chung không lộ input ngoài output—mô hình honest/dishonest majority khác công cụ (secret sharing, garbled circuit, OT).

Đây là **lý thuyết giao thức toán** có triển khai thật—và khoảng cách rộng giữa khả thi tiệm cận và dùng rẻ khắp nơi. Hype (“FHE giải mọi privacy”) bỏ qua hiệu năng, rò rỉ pattern truy cập, quản trị khóa.

---

## 7. Di trú và bài toán mở

1. Handshake hybrid cổ điển+PQC trong giai đoạn chuyển.  
2. Cryptanalysis primitive mới (thuật toán cổ điển và lượng tử).  
3. Triển khai chống side-channel.  
4. Composition giao thức: chứng an ninh hệ từ mảnh.  
5. Chữ ký dài hạn và key agility.  
6. Formal verification mã crypto và chứng minh.  
7. Đánh giá đe dọa lượng tử không hoảng loạn cũng không chối.

### Ảnh di trú cụ thể (khái niệm)

Handshake kiểu TLS có thể đàm phán trao đổi khóa đường cong elliptic **và** KEM lattice, trộn bí mật phiên để kẻ tấn phải phá **cả hai** (hybrid). Chữ ký cập nhật phần mềm có thể chuyển sang hash-based hoặc lattice với profile kích thước/hiệu năng khác. Certificate, HSM, IoT ràng buộc, chữ ký tài liệu dài hạn—không có nút “bật PQC” duy nhất.

Rủi ro **thu hoạch nay–giải mã sau** lệch theo loại dữ liệu: mật 50 năm khẩn hơn session key vài phút. Quản trị rủi ro × (giá trị bí mật) × (thời gian cần giữ) × (xác suất máy lượng tử cryptographically relevant trong horizon)—ước Fermi, không định lý, nhưng hơn vibe.

### Side-channel: toán vs silicon

Reduction hoàn hảo vẫn gãy nếu triển khai rò khóa qua timing, cache, năng lượng, fault. Constant-time, masking, formal verification là công việc an ninh hạng nhất. PQC khóa lớn và số học mới (NTT lattice, ma trận lớn code…) tạo bề mặt side-channel **mới**. Biết đọc: scheme “NIST-selected” vẫn có thể gãy trong sản phẩm vì RNG xấu hoặc so sánh rò.

### Studio seminar

Lấy một claim vendor “quantum-safe / quantum-ready”. Checklist LO6: tên scheme? tham số? hybrid mode? threat model (chỉ máy lượng tử hay cả side-channel)? chứng minh/paper? Viết ba câu phản biện seminar: “được phép nói gì / không được phép nói gì trên slide”.

---

## Nhầm lẫn thường gặp

| Tuyên bố | Sửa |
|----------|-----|
| “Máy lượng tử đã phá RSA ngoài đời.” | Chưa có break cryptographically relevant công khai. |
| “AES gãy vì Shor.” | Grover ảnh hưởng brute force; không phải factoring. |
| “PQC chưa chứng minh nên vô dụng.” | Mọi PK dùng giả thiết; PQC mới hơn, đang soi gay gắt. |
| “QKD làm hết crypto lỗi thời.” | Phạm vi hẹp; xác thực và mục tiêu rộng vẫn cần. |
| “ZK = zero information mọi nghĩa.” | Định nghĩa theo simulation; triển khai có thể rò. |
| “NIST chuẩn hóa ⇒ vĩnh viễn an toàn.” | Giảm rủi ro; cryptanalysis tiếp tục. |

---

## Bài tập

1. Ghép: bảo mật bulk / trao đổi khóa / non-repudiation → đối xứng / KEM / chữ ký.
2. Ba câu: vì sao bí mật dài hạn thúc PQC trước máy lượng tử lớn.
3. Một đoạn Shor vs Grover (công khai vs đối xứng).
4. Reduction LWE→scheme cho thấy gì / không cho thấy gì?
5. Tái lập bảng QKD vs PQC từ trí nhớ.
6. Câu chuyện ZK đồ chơi “biết preimage hash”.
7. Phê claim vendor “quantum-safe”: thiếu gì?

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/future-cryptography/analysis.md`.

### Trạng thái

**Standards evolving.** NIST released first PQC FIPS (203–205) in 2024; migration is ongoing. QKD is a different technology stack from classical PQC algorithms.

### Phát biểu / slogan cốt lõi

Shor's algorithm breaks RSA/ECC on a large fault-tolerant quantum computer (theorem in circuit model). PQC bases security on lattice/code/hash/isogeny-type problems believed hard for quantum adversaries — hardness is *conjectural*, not proved.

### Định nghĩa cần cố định

- **PQC.** Classical crypto designed to resist quantum adversaries.
- **Crypto-agility.** Ability to swap algorithms as standards/attacks evolve.

### Vệ sinh khái niệm

- Assuming quantum computers already break RSA at scale today.
- Equating QKD with PQC (different trust and deployment models).


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/future-cryptography/`.

**Thứ tự gợi ý**

1. **Định hướng** — SandboxAQ — NIST's PQC Standardization Explained: [https://www.youtube.com/watch?v=crPe69NeTdk](https://www.youtube.com/watch?v=crPe69NeTdk).  
2. **Cốt lõi** — IBM Research — NIST post-quantum standards webcast: [https://www.youtube.com/watch?v=YJ00O4gBs0I](https://www.youtube.com/watch?v=YJ00O4gBs0I).  
3. **Nền tảng** — Cryptography 101 — PQC Standards explained: [https://www.youtube.com/watch?v=P9g1CMCu8DI](https://www.youtube.com/watch?v=P9g1CMCu8DI).  

**Nhắc trạng thái:** **Standards evolving.** NIST released first PQC FIPS (203–205) in 2024; migration is ongoing. QKD is a different technology stack from classical PQC algorithms.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/future-cryptography/transcripts/` · trạng thái: `research/video-research/future-cryptography/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/future-cryptography_crPe69NeTdk_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo

1. Katz & Lindell — *Introduction to Modern Cryptography*.
2. Tài liệu NIST PQC và spec thuật toán được chọn.
3. Regev — LWE; Shor — factoring/dlog lượng tử.
4. Survey FHE, ZK, MPC (Boneh–Shoup; SoK gần đây).
5. [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) (pattern hype vs threat model).

---


Danh mục URL đầy đủ: `research/video-research/future-cryptography/references.md`.

### Video (lộ trình gợi ý)

- SandboxAQ — NIST's PQC Standardization Explained (ORIENTATION): https://www.youtube.com/watch?v=crPe69NeTdk
- IBM Research — NIST post-quantum standards webcast (CORE): https://www.youtube.com/watch?v=YJ00O4gBs0I
- Cryptography 101 — PQC Standards explained (FOUNDATION): https://www.youtube.com/watch?v=P9g1CMCu8DI

### Bài báo và web (từ gói nghiên cứu)

- NIST — What is Post-Quantum Cryptography?: https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography
- NIST PQC project: https://csrc.nist.gov/projects/post-quantum-cryptography
- Wikipedia — NIST PQC Standardization: https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization
- NIST video page — PQC Good/Bad/Powerful: https://www.nist.gov/video/post-quantum-cryptography-good-bad-and-powerful
- Wikipedia — Post-quantum cryptography: https://en.wikipedia.org/wiki/Post-quantum_cryptography
- Wikipedia — Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm

### Khóa học

- Gói: `research/video-research/future-cryptography/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) cho mô hình đe dọa đầy đủ.
- [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) cho ngôn ngữ độ khó.
- So sánh kích thước khóa/hiệu năng ECC vs lattice KEM (bậc độ lớn, benchmark công khai).
- Đọc: Katz–Lindell lõi → NIST PQC FAQ → một đoạn survey LWE mỗi ngày.
- Checklist threat model trước khi tin “không phá nổi”.
