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

Sau bài cập nhật tùy chọn này, bạn đặt được bốn hiện vật 2022–2026—huấn luyện LLM tối ưu tính toán, AlphaFold 3, toán tử PDE nơ-ron, và KEM lattice đã chuẩn hóa—lên bản đồ biên giới của chương, gắn mỗi câu nhãn định lý, regularity thực nghiệm, hoặc tiêu chuẩn kỹ thuật, mà không viết lại [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) hay [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

## Kiến thức cần có

Bài flagship AI và các bài sau về [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), và [sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/).

## Mở đầu

Chương 6 là vùng chưa xong. Kỹ năng là biết chữ dưới bất định. Giữa 2022 và 2026 vài đối tượng biên giới *đã chuyển*: một quy tắc scale đổi cách phòng lab tiêu FLOPs, một mô hình khuếch tán dự đoán phức hợp sinh phân tử, một mạng toán tử giả làm bộ giải PDE, và ba tiêu chuẩn hậu lượng tử NIST. Không sự kiện nào khép các câu hỏi lý thuyết trong flagship AI. Chúng đổi điều một nhà khoa học dữ liệu sẽ thực sự chạm.

## Phát triển khái niệm

Hoffmann et al. (2022) xem pretraining như bài toán phân bổ: cho ngân sách tính toán $$C$$, chọn kích thước mô hình $$N$$ và số token $$D$$ để cực tiểu hóa mất mát. Khớp thực nghiệm của họ gợi ý scale $$N$$ và $$D$$ cùng lúc (regularity “Chinchilla”). Đó không phải định lý tổng quát hóa. Đó là một phép đo về một chồng huấn luyện. AlphaFold 3, ngược lại, là một hệ thống đã huấn luyện mà mô-đun khuếch tán lắp ráp đám mây nguyên tử; các tuyên bố của nó là số trên benchmark kiểu PDB, không phải suy ra gấp cuộn từ nguyên lý đầu.

## Bốn chỗ đáp

### 1. Chinchilla như regularity phân bổ

Hoffmann, Borgeaud, Mensch, et al. (2022) huấn luyện hàng trăm mô hình ngôn ngữ và báo nhiều mô hình lớn trước đó bị thiếu token. Chinchilla (70B tham số, 1.4T token) khớp tính toán của Gopher và thắng trên MMLU cùng các bộ khác. Hãy dùng điều này theo tinh thần bài AI: một *regularity thực nghiệm* về tính toán, không phải chứng minh mặt mất mát lồi hay mất mát kiểm bằng rủi ro thật.

### 2. AlphaFold 3 và sinh học toán

Abramson, Adler, Dunger, Evans, Green, Pritzel, Ronneberger, Willmore, et al. (2024) giới thiệu AlphaFold 3, một kiến trúc dựa trên khuếch tán cho phức hợp protein, acid nucleic, ligand và ion. Các mức tăng được báo gồm độ chính xác protein–ligand so với công cụ docking chuyên biệt trên PoseBusters. Đây là “mô hình như hàm trên cấu trúc chiều cao” của bài sinh học, nay là một máy chủ. Metric độ tin vẫn là số đã hiệu chỉnh, không phải chứng chỉ phòng ướt.

### 3. Neural operator như học máy khoa học

Kovachki et al. (2023) đưa khung không gian hàm và các thí nghiệm kiểu Navier–Stokes đã dùng ở Chương 1 và 3. Trong chương này, điểm là kiến trúc: cùng hình học chiều cao và góc nhìn toán tử như flagship AI, áp vào mô phỏng liên tục chứ không vào token.

### 4. Tiêu chuẩn PQC như dạng chuyển đầu tiên của biên mật mã

FIPS 203/204/205 (tháng 8 năm 2024) biến các họ lattice và hàm băm của bài [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/) thành thuật toán có tên (ML-KEM, ML-DSA, SLH-DSA). Thuật toán lượng tử không “đến” năm 2024; *cuộc di cư* thì có. Thuật toán Shor vẫn là lý do cuộc di cư tồn tại, không phải một trình diễn trên máy có nghĩa mật mã.

## Diễn giải và nhận định

Biết chữ biên giới là bài tập gắn nhãn. Chinchilla: regularity. AlphaFold 3: bộ dự đoán đã đo. Neural operator: surrogate học được với định lý xấp xỉ phổ quát *cho toán tử dưới giả thuyết*. FIPS 203: tiêu chuẩn dưới một giả thuyết độ khó. Trộn các nhãn ấy là cách hype được viết.

## Giới hạn và hướng mở rộng

Trang này không làm lại suy ra attention, bound PAC, hay AdS/CFT. Các deep dive đối ngẫu ở nguyên chỗ. Tiêu đề sửa lỗi lượng tử sau 2024 nên đọc với cùng vệ sinh LO6 như bài lượng tử.

## Bài tập

1. Viết một câu về Chinchilla sẽ sai nếu bạn thay “khớp thực nghiệm” bằng “định lý.”
2. AlphaFold 3 dùng một mô-đun khuếch tán. Đó là đối tượng nào của Chương 4 hoặc Chương 6, và một điểm tin cao *không* bảo đảm điều gì?
3. Vì sao một neural operator có thể có định lý xấp xỉ phổ quát mà vẫn thất bại ở một số Reynolds mới?
4. Gọi tên đối tượng độ khó đứng sau ML-KEM và nói vì sao một thông cáo *annealer* lượng tử không cho nó nghỉ hưu.

## Tài liệu tham khảo

- Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556).
- Abramson, J., et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630, 493–500. [doi:10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w).
- Kovachki, N., et al. (2023). Neural operator. *JMLR*, 24(89). [bài báo](https://jmlr.org/papers/v24/21-1524.html).
- NIST. (2024). FIPS 203/204/205. [thông báo nist.gov](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips).
