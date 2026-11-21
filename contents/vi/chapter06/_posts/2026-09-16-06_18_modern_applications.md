---
layout: post
title: "Ứng dụng hiện đại: Toán biên giới ngoài đời, 2022–2026"
chapter: '06'
order: 18
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: optional
---

## Mục tiêu học tập

Sau bài cập nhật không bắt buộc này, bạn có thể đặt bốn kết quả của giai đoạn 2022–2026 vào bức tranh chung của chương: cách huấn luyện mô hình ngôn ngữ lớn tối ưu theo chi phí tính toán, AlphaFold 3, toán tử nơ-ron để giải phương trình đạo hàm riêng, và cơ chế trao đổi khóa (KEM) dựa trên lưới đã được chuẩn hóa. Với mỗi khẳng định, bạn ghi rõ nó là định lý, quy luật thực nghiệm, hay tiêu chuẩn kỹ thuật. Bài này không viết lại nội dung của các bài [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) hay [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

## Kiến thức cần có

Bài chính về AI và các bài về [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), và [sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/).

## Mở đầu

Chương 6 nói về những lĩnh vực còn đang phát triển. Kỹ năng cần có là đọc hiểu được những gì còn chưa chắc chắn. Từ 2022 đến 2026 có một số thay đổi đáng chú ý: một quy luật về tỉ lệ (scaling) làm các phòng thí nghiệm thay đổi cách phân bổ năng lực tính toán (FLOPs); một mô hình khuếch tán dự đoán được cấu trúc của các phức hợp phân tử sinh học; một loại mạng nơ-ron học toán tử được dùng thay cho bộ giải phương trình đạo hàm riêng; và NIST công bố ba tiêu chuẩn mật mã hậu lượng tử. Không sự kiện nào trong số này giải quyết được các câu hỏi lý thuyết nêu trong bài chính về AI. Nhưng chúng làm thay đổi những gì một nhà khoa học dữ liệu thực sự dùng hằng ngày.

## Phát triển khái niệm

Hoffmann và cộng sự (2022) xem việc huấn luyện trước (pretraining) như một bài toán phân bổ: với ngân sách tính toán $$C$$ cho trước, chọn kích thước mô hình $$N$$ và số token dữ liệu $$D$$ để mất mát nhỏ nhất. Kết quả khớp thực nghiệm của họ cho thấy nên tăng $$N$$ và $$D$$ cùng lúc (quy luật "Chinchilla"). Đây không phải một định lý về khả năng tổng quát hóa. Đây là một phép đo trên một quy trình huấn luyện cụ thể. Ngược lại, AlphaFold 3 là một hệ thống đã huấn luyện, trong đó mô-đun khuếch tán dựng lên vị trí các nguyên tử. Những gì nó khẳng định là các con số trên bộ dữ liệu kiểm tra dạng PDB, không phải suy ra cách protein gấp cuộn từ các nguyên lý vật lý cơ bản.

## Bốn kết quả cụ thể

### 1. Chinchilla: một quy luật thực nghiệm về phân bổ

Hoffmann, Borgeaud, Mensch và cộng sự (2022) huấn luyện hàng trăm mô hình ngôn ngữ và nhận thấy nhiều mô hình lớn trước đó được huấn luyện với quá ít token. Mô hình Chinchilla (70 tỉ tham số, 1,4 nghìn tỉ token) dùng cùng lượng tính toán như Gopher nhưng cho kết quả tốt hơn trên MMLU và các bộ kiểm tra khác. Hãy hiểu điều này đúng tinh thần của bài AI: đây là một *quy luật thực nghiệm* về chi phí tính toán, không phải chứng minh rằng mặt mất mát là lồi, hay rằng mất mát trên tập kiểm tra bằng rủi ro thật.

### 2. AlphaFold 3 và sinh học toán

Abramson, Adler, Dunger, Evans, Green, Pritzel, Ronneberger, Willmore và cộng sự (2024) giới thiệu AlphaFold 3, một kiến trúc dựa trên mô hình khuếch tán để dự đoán cấu trúc phức hợp gồm protein, axit nucleic, phối tử (ligand) và ion. Một trong các cải tiến được báo cáo là độ chính xác khi dự đoán liên kết protein–phối tử cao hơn các công cụ docking chuyên dụng trên bộ kiểm tra PoseBusters. Đây chính là ý "mô hình là một hàm trên không gian cấu trúc nhiều chiều" trong bài sinh học, nay đã thành một dịch vụ chạy trên máy chủ. Điểm tin cậy mà mô hình đưa ra vẫn chỉ là một con số đã hiệu chỉnh, không thay được kết quả thí nghiệm trong phòng lab.

### 3. Toán tử nơ-ron trong học máy cho khoa học

Kovachki và cộng sự (2023) xây dựng khung lý thuyết trên không gian hàm và làm thí nghiệm với các bài toán dạng Navier–Stokes, như đã nhắc ở chương 1 và chương 3. Trong chương này, điều cần chú ý là kiến trúc: nó dùng cùng góc nhìn về hình học nhiều chiều và về toán tử như bài chính về AI, nhưng áp dụng cho mô phỏng các hệ liên tục thay vì cho chuỗi token.

### 4. Tiêu chuẩn mật mã hậu lượng tử: lý thuyết bắt đầu thành thực tế

Các tiêu chuẩn FIPS 203/204/205 (tháng 8 năm 2024) biến các họ mật mã dựa trên lưới và trên hàm băm trong bài [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/) thành các thuật toán có tên cụ thể (ML-KEM, ML-DSA, SLH-DSA). Năm 2024 chưa có máy tính lượng tử phá được mật mã; điều xảy ra là *việc chuyển đổi* sang thuật toán mới đã bắt đầu. Thuật toán Shor vẫn là lý do của việc chuyển đổi này, dù chưa có máy nào chạy nó ở quy mô đủ để đe dọa mật mã thực tế.

## Diễn giải và nhận định

Đọc hiểu các tin tức mới chủ yếu là việc gắn nhãn cho đúng. Chinchilla là một quy luật thực nghiệm. AlphaFold 3 là một công cụ dự đoán đã được đánh giá bằng số liệu. Toán tử nơ-ron là một mô hình thay thế học từ dữ liệu, có định lý xấp xỉ phổ quát *cho toán tử, dưới một số giả thiết*. FIPS 203 là một tiêu chuẩn dựa trên giả thiết rằng một bài toán nào đó là khó. Khi các nhãn này bị trộn lẫn, tin tức dễ bị thổi phồng.

## Giới hạn và hướng mở rộng

Bài này không trình bày lại cách suy ra cơ chế attention, các chặn PAC, hay AdS/CFT. Các bài đọc sâu về đối ngẫu vẫn giữ nguyên. Các tin tức về sửa lỗi lượng tử sau 2024 nên được đọc với cùng sự thận trọng như trong bài về thông tin lượng tử: phân biệt rõ điều đã chứng minh, điều đã đo được và điều chỉ là kỳ vọng.

## Bài tập

1. Viết một câu về Chinchilla mà câu đó sẽ trở thành sai nếu bạn thay "khớp thực nghiệm" bằng "định lý".
2. AlphaFold 3 dùng một mô-đun khuếch tán. Đó là đối tượng nào trong chương 4 hoặc chương 6? Một điểm tin cậy cao *không* bảo đảm điều gì?
3. Vì sao một toán tử nơ-ron có thể có định lý xấp xỉ phổ quát mà vẫn dự đoán sai ở một số Reynolds mới?
4. Nêu tên bài toán khó làm nền cho ML-KEM, và giải thích vì sao một thông cáo về máy *ủ lượng tử* (quantum annealer) không làm ML-KEM trở nên lỗi thời.

## Tài liệu tham khảo

- Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556).
- Abramson, J., et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630, 493–500. [doi:10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w).
- Kovachki, N., et al. (2023). Neural operator. *JMLR*, 24(89). [bài báo](https://jmlr.org/papers/v24/21-1524.html).
- NIST. (2024). FIPS 203/204/205. [thông báo nist.gov](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips).

## Video tham khảo

- **Xem trước:** [Chinchilla Explained: Compute-Optimal Massive Language Models](https://www.youtube.com/watch?v=PZXN7jm9IC0) (Edan Meyer, tiếng Anh). Giải thích sự đánh đổi giữa số tham số và số token khi huấn luyện tối ưu theo tính toán (Chinchilla). Đây là video giải thích bài báo, không phải bài giảng của tác giả.
- [AlphaFold - The Most Useful Thing AI Has Ever Done](https://www.youtube.com/watch?v=P_fHJIYENdI) (Veritasium, tiếng Anh). Kể lại bài toán gấp cuộn protein và cách AlphaFold thay đổi lĩnh vực này. Xem sau khi đã nắm ý chính của bài.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) (Steve Brunton, tiếng Anh). Giới thiệu toán tử nơ-ron Fourier, một dạng toán tử nơ-ron dùng để giải phương trình đạo hàm riêng. Xem thêm cho mục 3.
