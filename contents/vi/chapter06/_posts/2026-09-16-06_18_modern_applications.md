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

Nếu bước vào một phòng thí nghiệm AI, một viện sinh học cấu trúc hay một cuộc họp hạ tầng an ninh mạng vào giữa thập niên 2020, bạn sẽ thấy những ý tưởng tưởng chừng rất trừu tượng của toán học hiện đại đang chạy ầm ầm trên các cụm máy chủ thật. Chỉ trong bốn năm 2022–2026, bốn cột mốc nối tiếp nhau đã làm đổi hẳn thói quen làm việc của giới kỹ sư và nhà khoa học: một đường cong thực nghiệm buộc các phòng thí nghiệm AI phải phân bổ lại hàng triệu đô la ngân sách tính toán; một mô hình khuếch tán dựng được hình khối nguyên tử của cả phức hợp protein–DNA–thuốc; một thế hệ mạng nơ-ron học trực tiếp ánh xạ giữa các không gian hàm để mô phỏng dòng chảy chất lỏng; và Viện Tiêu chuẩn Quốc gia Hoa Kỳ (NIST) chính thức khóa chuẩn ba thuật toán mật mã hậu lượng tử dựa trên lưới và hàm băm.

Nhưng càng đứng gần vùng biên giới, ranh giới giữa **định lý đã chứng minh**, **quy luật thực nghiệm đo được**, và **tiêu chuẩn kỹ thuật dựa trên giả thiết độ khó** càng dễ bị truyền thông trộn lẫn. Bài đọc cập nhật không bắt buộc này giúp bạn đặt bốn cột mốc ấy đúng chỗ trên bản đồ của Chương 6 — không viết lại nội dung của các bài [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) hay [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), mà rèn thói quen đọc tin khoa học với nhãn nhận thức rõ ràng.

---

## Bản đồ kiến thức nền: Toán ứng dụng biên giới 2022–2026 nằm ở đâu?

Với một người tốt nghiệp đại học quen với tối ưu hóa cổ điển, xác suất thống kê và phương trình vi phân, câu hỏi tự nhiên nhất là: *điều gì nối bốn mảng tưởng chừng rời rạc này — mô hình ngôn ngữ, gấp cuộn protein, mô phỏng chất lỏng, và mật mã học — lại với nhau trong cùng một bài học?*

Điểm chung nằm ở **cách toán học hiện đại làm việc với đối tượng nhiều chiều và bất định**, nhưng theo ba kiểu cam kết hoàn toàn khác nhau:

- **Tối ưu hóa thực nghiệm và định luật tỉ lệ (scaling laws):** Thay vì chứng minh bề mặt hàm mất mát lồi (điều không đúng với mạng sâu), người ta đo thực nghiệm cách sai số suy giảm theo hàm lũy thừa của số tham số $$N$$ và lượng dữ liệu $$D$$, rồi giải một bài toán tối ưu có ràng buộc ngân sách tính toán $$C$$.
- **Mô hình sinh trên không gian hình học và không gian hàm:** Ở sinh học cấu trúc, mô hình khuếch tán (diffusion) học cách khử nhiễu ngược dần từ đám mây ngẫu nhiên về tọa độ 3D của hàng nghìn nguyên tử — bản chất là một phương trình vi phân ngẫu nhiên đảo ngược thời gian. Ở mô phỏng vật lý, **toán tử nơ-ron** nâng cấp mạng nơ-ron từ hàm $$\mathbb{R}^d \to \mathbb{R}^k$$ lên ánh xạ giữa hai không gian hàm (ví dụ từ trường điều kiện ban đầu sang trường vận tốc ở thời điểm $$t$$), biến bài toán giải phương trình đạo hàm riêng thành bài toán học toán tử.
- **Độ phức tạp tính toán trong mật mã hậu lượng tử:** Khi máy tính lượng tử tiềm năng đe dọa phá vỡ bài toán phân tích thừa số nguyên tố (RSA) nhờ thuật toán Shor, cộng đồng mật mã chuyển sang những bài toán hình học rời rạc trên **mạng lưới nhiều chiều** (lattice) — chẳng hạn tìm vectơ ngắn nhất hoặc giải hệ tuyến tính có nhiễu (Learning With Errors) — vốn hiện chưa có thuật toán lượng tử nào giải nhanh.

Hiểu ba trụ cột này, bạn sẽ lập tức phân biệt được: đâu là công cụ kỹ thuật cực mạnh có thể hỏng ngoài miền huấn luyện, và đâu là phát biểu toán học mang tính bảo chứng.

---

## Mục tiêu học tập

Sau bài cập nhật không bắt buộc này, bạn có thể đặt bốn kết quả của giai đoạn 2022–2026 vào bức tranh chung của chương: cách huấn luyện mô hình ngôn ngữ lớn tối ưu theo chi phí tính toán, AlphaFold 3, toán tử nơ-ron để giải phương trình đạo hàm riêng, và cơ chế trao đổi khóa (KEM) dựa trên lưới đã được chuẩn hóa. Với mỗi khẳng định, bạn ghi rõ nó là định lý, quy luật thực nghiệm, hay tiêu chuẩn kỹ thuật.

## Kiến thức cần có

Bài chính về AI và các bài về [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), và [sinh học toán]({{ site.baseurl }}/contents/vi/chapter06/06_04_Mathematical_Biology/).

---

## Mở đầu: Đọc đúng những gì còn đang chuyển động

Chương 6 nói về những lĩnh vực còn đang phát triển. Kỹ năng quan trọng nhất khi đứng ở vùng biên không phải là thuộc lòng mọi từ khóa mới, mà là đọc hiểu được *những gì còn chưa chắc chắn*. Không sự kiện nào trong bốn cột mốc 2022–2026 giải quyết trọn vẹn các câu hỏi lý thuyết nền tảng nêu trong bài chính về AI (như vì sao mạng sâu tổng quát hóa tốt dù quá nhiều tham số). Nhưng cả bốn đều làm thay đổi sâu sắc hộp công cụ mà nhà khoa học dữ liệu, nhà sinh học tính toán và kỹ sư bảo mật sử dụng hằng ngày.

## Phát triển khái niệm

Hoffmann và cộng sự (2022) nhìn việc huấn luyện trước (pretraining) như một bài toán phân bổ tài nguyên: với ngân sách tính toán $$C$$ cố định (xấp xỉ tỉ lệ với $$6ND$$), cần chọn kích thước mô hình $$N$$ và số token dữ liệu $$D$$ sao cho hàm mất mát đạt cực tiểu. Kết quả khớp thực nghiệm của họ cho thấy nên tăng $$N$$ và $$D$$ cùng tỉ lệ với nhau (quy luật "Chinchilla") — tương tự như cách bạn chọn chiều rộng và chiều dài một khu vườn để tối đa hóa diện tích với chu vi rào cố định, nhưng ở đây "công thức diện tích" không suy từ hình học tiên đề mà được khớp từ hàng trăm lần chạy thử. Do đó, đây không phải một định lý về khả năng tổng quát hóa, mà là một phép đo trên một quy trình huấn luyện cụ thể.

Ngược lại, AlphaFold 3 là một hệ thống đã huấn luyện, trong đó mô-đun khuếch tán trực tiếp dựng lên tọa độ 3D của các nguyên tử. Những gì nó khẳng định là các con số đo được trên bộ dữ liệu kiểm tra dạng PDB, không phải suy ra cơ chế vật lý nhiệt động lực học của quá trình protein gấp cuộn từ các nguyên lý đầu tiên.

### Khung giải thích: tối ưu ngân sách Chinchilla bằng giải tích một biến (nên đọc chậm)

Khi nghe nói "Chinchilla tối ưu hóa số tham số $$N$$ và số token dữ liệu $$D$$ dưới ngân sách tính toán cố định $$C$$", người đọc dễ tưởng đây là phép toán bí ẩn của siêu máy tính. Thực ra, phần lõi toán học chính là một bài toán cực trị có điều kiện ở giải tích năm nhất — và bạn có thể kiểm tra ngay bằng tay.

Giả sử hàm mất mát thực nghiệm tuân theo định luật lũy thừa đối xứng đơn giản (xấp xỉ gần với số mũ thực nghiệm $$lpha pprox eta pprox 0.5$$ trong bài báo gốc):

$$
L(N, D) = E + rac{A}{\sqrt{N}} + rac{B}{\sqrt{D}},
$$

với ngân sách tính toán cố định $$C = 6ND$$ (mỗi token đi qua $$N$$ tham số tốn khoảng $$6N$$ phép tính dấu phẩy động cho lượt tiến và lượt ngược).

1. **Khử biến $$D$$ bằng ràng buộc:** Từ $$6ND = C$$, rút ra $$D = rac{C}{6N}$$. Thay vào hàm mất mát:

   $$
   L(N) = E + A N^{-1/2} + B \sqrt{rac{6}{C}}\, N^{1/2}.
   $$

2. **Đặt đạo hàm bằng $$0$$ để tìm cực tiểu:**

   $$
   rac{dL}{dN} = -rac{A}{2} N^{-3/2} + rac{B}{2}\sqrt{rac{6}{C}}\, N^{-1/2} = 0
   \;\Longleftrightarrow\;
   N^* = rac{A}{B}\sqrt{rac{C}{6}}, \qquad
   D^* = rac{B}{A}\sqrt{rac{C}{6}}.
   $$

3. **Kiểm tra bằng số cụ thể:** Đặt $$E = 1.69$$, $$A = B = 400$$, và ngân sách $$C = 6 	imes 10^{22}$$ FLOPs (tức $$ND = 10^{22}$$):
   - **Cách chia cân bằng kiểu Chinchilla** ($$N^* = 10^{11}$$, $$D^* = 10^{11}$$):
     $$L = 1.69 + rac{400}{\sqrt{10^{11}}} + rac{400}{\sqrt{10^{11}}} pprox 1.69 + 0.00126 + 0.00126 = 1.69253.$$
   - **Cách chia lệch kiểu "quá lớn, thiếu dữ liệu"** (tăng $$N$$ gấp 4 lần lên $$4	imes 10^{11}$$, nên $$D$$ giảm 4 lần còn $$2.5	imes 10^{10}$$):
     $$L = 1.69 + rac{400}{\sqrt{4	imes 10^{11}}} + rac{400}{\sqrt{2.5	imes 10^{10}}} pprox 1.69 + 0.00063 + 0.00253 = 1.69316 > 1.69253.$$

**Bài học cần rút ra:** Toàn bộ phép giải tích trên hoàn toàn chặt chẽ, nhưng **đầu vào** (công thức $$L(N,D)$$ và các hằng số $$A, B, lpha, eta$$) lại là đường khớp thực nghiệm từ 400 lần huấn luyện. Đó là lý do Chinchilla là một **quy luật thực nghiệm được tối ưu bằng giải tích**, chứ không phải định lý phổ quát cho mọi kiến trúc hay mọi bộ dữ liệu.

## Bốn kết quả cụ thể

### 1. Chinchilla: một quy luật thực nghiệm về phân bổ

Trước năm 2022, nhiều nhóm nghiên cứu chạy đua tăng kích thước mô hình lên hàng trăm tỉ tham số trong khi giữ lượng dữ liệu huấn luyện tương đối cố định. Hoffmann, Borgeaud, Mensch và cộng sự (2022) huấn luyện hơn 400 mô hình ngôn ngữ và phát hiện các mô hình khổng lồ trước đó bị "đói dữ liệu". Khi giữ nguyên ngân sách tính toán của Gopher (280 tỉ tham số, 300 tỉ token) nhưng chia lại ngân sách để tạo ra **Chinchilla** (70 tỉ tham số, 1,4 nghìn tỉ token — nhỏ hơn 4 lần nhưng học trên lượng văn bản gấp gần 5 lần), Chinchilla vượt trội hơn hẳn trên MMLU và nhiều bộ kiểm tra chuẩn khác.

Hãy hiểu điều này đúng tinh thần của bài AI: đây là một *quy luật thực nghiệm* về chi phí tính toán — một kim chỉ nam cực kỳ giá trị cho kỹ sư huấn luyện — chứ không phải chứng minh rằng mặt mất mát là lồi, hay rằng mất mát trên tập kiểm tra trùng khớp với rủi ro thật ngoài đời. (Hơn nữa, nếu xét cả chi phí *suy luận* lâu dài sau khi triển khai, nhiều nhóm sau này còn cố tình huấn luyện mô hình nhỏ hơn nữa trên nhiều token hơn hẳn tỉ lệ Chinchilla!)

### 2. AlphaFold 3 và sinh học toán

Abramson, Adler, Dunger, Evans, Green, Pritzel, Ronneberger, Willmore và cộng sự (2024) giới thiệu **AlphaFold 3**, một kiến trúc dựa trên mô hình khuếch tán để dự đoán cấu trúc 3D của không chỉ protein đơn lẻ mà cả phức hợp sinh học gồm protein, axit nucleic (DNA/RNA), phối tử nhỏ (ligand, như phân tử thuốc) và ion. Nếu hình dung một phân tử thuốc cần khớp vào "ổ khóa" trên bề mặt protein, mô-đun khuếch tán bắt đầu từ một đám mây nguyên tử nhiễu loạn rồi tinh chỉnh dần từng bước cho đến khi toàn bộ phức hợp vào khớp hình học.

Một trong các cải tiến nổi bật được báo cáo là độ chính xác khi dự đoán liên kết protein–phối tử vượt qua các công cụ docking chuyên dụng truyền thống trên bộ kiểm tra PoseBusters. Đây chính là ý tưởng "mô hình là một hàm trên không gian cấu trúc nhiều chiều" trong bài sinh học, nay đã trở thành một dịch vụ chạy trên máy chủ. Tuy vậy, điểm tin cậy mà mô hình trả về vẫn chỉ là một con số đã hiệu chỉnh theo thống kê — nó giúp thu hẹp nhanh hàng nghìn ứng viên thuốc tiềm năng, nhưng không thay thế được thí nghiệm tinh thể học tia X hay cryo-EM trong phòng lab.

### 3. Toán tử nơ-ron trong học máy cho khoa học

Kovachki và cộng sự (2023) xây dựng khung lý thuyết **toán tử nơ-ron** (neural operator) trên không gian hàm và thử nghiệm với các bài toán dạng Navier–Stokes, như đã nhắc ở chương 1 và chương 3. Để thấy sự khác biệt với mạng nơ-ron thông thường: nếu bạn giải phương trình truyền nhiệt hoặc dòng chảy chất lỏng bằng phương pháp phần tử hữu hạn truyền thống, mỗi khi đổi điều kiện đầu hay đổi độ phân giải lưới tính, bạn phải giải lại từ đầu. Toán tử nơ-ron — chẳng hạn Fourier Neural Operator (FNO), biến đổi dữ liệu sang miền tần số để nhân với bộ lọc học được rồi biến đổi ngược lại — học trực tiếp quy tắc biến *hàm đầu vào* thành *hàm nghiệm*, nên có thể chạy nhanh hơn hàng trăm lần và áp dụng trên lưới có độ phân giải khác nhau.

Trong chương này, điều đáng chú ý là góc nhìn kiến trúc: nó dùng cùng tư duy hình học nhiều chiều và lý thuyết toán tử như bài chính về AI, nhưng áp dụng cho mô phỏng các hệ liên tục thay vì cho chuỗi token rời rạc.

### 4. Tiêu chuẩn mật mã hậu lượng tử: lý thuyết bắt đầu thành thực tế

Tháng 8 năm 2024, NIST công bố chính thức ba tiêu chuẩn **FIPS 203, FIPS 204 và FIPS 205**, biến các họ mật mã dựa trên lưới và trên hàm băm trong bài [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/) thành các thuật toán có tên gọi và đặc tả kỹ thuật cụ thể (**ML-KEM** để đóng gói/trao đổi khóa, **ML-DSA** và **SLH-DSA** để ký số).

Cần đọc đúng bối cảnh lịch sử của cột mốc này: năm 2024 chưa có máy tính lượng tử nào phá được mật mã RSA hay ECC đang dùng trên internet; điều thực sự xảy ra là *cuộc di cư hạ tầng* sang thuật toán mới đã bắt đầu (vì dữ liệu mã hóa hôm nay có thể bị thu thập và lưu lại chờ giải mã trong tương lai, gọi là rủi ro "thu thập trước, giải mã sau"). Thuật toán Shor vẫn là động lực toán học phía sau cuộc chuyển đổi này, dù chưa có cỗ máy nào chạy nó ở quy mô đủ để đe dọa mật mã thực tế.

## Diễn giải và nhận định

Đọc hiểu các tin tức khoa học mới chủ yếu là bài tập **gắn nhãn cho đúng**. Hãy đặt bốn cột mốc cạnh nhau để thấy rõ sự khác biệt:

| Cột mốc | Nhãn nhận thức đúng | Điều nó KHÔNG khẳng định |
|---------|---------------------|--------------------------|
| Chinchilla (2022) | Quy luật thực nghiệm về phân bổ $$N, D$$ theo ngân sách $$C$$ | Không phải định lý tổng quát hóa hay chứng minh hội tụ toàn cục |
| AlphaFold 3 (2024) | Hệ thống dự đoán đo đạc trên benchmark (PDB, PoseBusters) | Không suy ra động học gấp cuộn từ vật lý cơ bản; không thay thí nghiệm lab |
| Toán tử nơ-ron (2023) | Mô hình thay thế học từ dữ liệu, có định lý xấp xỉ phổ quát *dưới giả thiết* | Không bảo đảm đúng ngoài phân phối huấn luyện (ví dụ chế độ chảy rối mới) |
| FIPS 203/204/205 (2024) | Tiêu chuẩn kỹ thuật dựa trên giả thiết độ khó tính toán | Không phải chứng minh toán học tuyệt đối rằng bài toán lưới bất khả xâm phạm |

Khi các nhãn này bị trộn lẫn — chẳng hạn gọi một đường khớp thực nghiệm là "định luật vật lý", hay nhầm định lý xấp xỉ phổ quát với sự bảo đảm chính xác ở mọi chế độ dòng chảy — tin tức khoa học rất dễ bị thổi phồng.

## Giới hạn và hướng mở rộng

Bài này không trình bày lại cách suy ra cơ chế attention, các chặn PAC, hay AdS/CFT. Các bài đọc sâu về đối ngẫu vẫn giữ nguyên. Các tin tức về sửa lỗi lượng tử sau năm 2024 nên được đọc với cùng sự thận trọng như trong bài về thông tin lượng tử: phân biệt rõ điều đã chứng minh, điều đã đo được trong phòng thí nghiệm và điều chỉ mới là kỳ vọng kỹ thuật.

## Tài liệu tham khảo

- Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556).
- Abramson, J., et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630, 493–500. [doi:10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w).
- Kovachki, N., et al. (2023). Neural operator. *JMLR*, 24(89). [bài báo](https://jmlr.org/papers/v24/21-1524.html).
- NIST. (2024). FIPS 203/204/205. [thông báo nist.gov](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips).

## Video tham khảo

- **Xem trước:** [Chinchilla Explained: Compute-Optimal Massive Language Models](https://www.youtube.com/watch?v=PZXN7jm9IC0) (Edan Meyer, tiếng Anh). Giải thích sự đánh đổi giữa số tham số và số token khi huấn luyện tối ưu theo tính toán (Chinchilla). Đây là video giải thích bài báo, không phải bài giảng của tác giả.
- [AlphaFold - The Most Useful Thing AI Has Ever Done](https://www.youtube.com/watch?v=P_fHJIYENdI) (Veritasium, tiếng Anh). Kể lại bài toán gấp cuộn protein và cách AlphaFold thay đổi lĩnh vực này. Xem sau khi đã nắm ý chính của bài.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) (Steve Brunton, tiếng Anh). Giới thiệu toán tử nơ-ron Fourier, một dạng toán tử nơ-ron dùng để giải phương trình đạo hàm riêng. Xem thêm cho mục 3.
