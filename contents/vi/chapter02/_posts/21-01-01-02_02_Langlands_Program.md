---
layout: post
title: "Ngô Bảo Châu và Bổ đề Cơ bản (Huy chương Fields 2010)"
chapter: '02'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Ngô Bảo Châu** (khi đó làm việc tại Université Paris-Sud) nhận **Huy chương Fields 2010** nhờ chứng minh **Bổ đề Cơ bản** (*Fundamental Lemma*) trong lý thuyết dạng tự đẳng cấu, bằng các phương pháp đại số–hình học mới. Kết quả này nằm ở trung tâm của **chương trình Langlands** và tháo gỡ một nút thắt kéo dài nhiều thập niên trong việc so sánh các công thức vết (lý thuyết nội soi, endoscopy). Ngô không "sáng lập" chương trình Langlands, và kết quả của ông cũng không thay thế toàn bộ chương trình; nó chứng minh một đẳng thức so sánh mà trước đó nhiều định lý lớn phải lấy làm giả thiết.

Nội dung bài:

**Tầm nhìn của Langlands → công thức vết → tích phân quỹ đạo → Bổ đề Cơ bản → hình học (Hitchin) → Laumon–Ngô → Ngô → Fields 2010.**

Mục tiêu không phải là tính một tích phân quỹ đạo cụ thể, mà là hiểu **bổ đề dùng để làm gì**, **vì sao nó cản trở sự tiến triển trong một thời gian dài**, và **hình học đã đi vào câu chuyện giải tích như thế nào**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đặt Bổ đề Cơ bản vào chương trình Langlands và vào bộ máy công thức vết Arthur–Selberg.
- Giải thích lý thuyết nội soi như việc "so sánh các nhóm rút gọn được (reductive) mà lẽ ra phải có chung dữ liệu tự đẳng cấu".
- Phân biệt kết quả của Laumon–Ngô (cho một họ nhóm đặc biệt) với định lý tổng quát của Ngô.
- Mô tả ngắn gọn vì sao hình học đại số có thể chứng minh các đẳng thức trong giải tích điều hòa $$p$$-adic.
- Không nhầm "Ngô sáng lập chương trình Langlands" với "Ngô chứng minh một bổ đề trung tâm trong chương trình Langlands".
- Ghi nhận rằng Robert Langlands nhận **Giải Abel 2018** cho toàn bộ chương trình, khác với Huy chương Fields 2010 của Ngô.

**Kiến thức cần có.** Quen với khái niệm nhóm và ý tưởng về biểu diễn. Số $$p$$-adic và nhóm rút gọn được ban đầu chỉ cần biết tên; các chi tiết kỹ thuật không bắt buộc.

---

## 1. Chương trình Langlands trong một trang

Trong những năm 1960–1970, **Robert Langlands** đề xuất một mạng lưới giả thuyết rộng lớn, nối:

- **dạng tự đẳng cấu / biểu diễn tự đẳng cấu** của các nhóm rút gọn được trên trường số (và trên vành adele), với  
- **biểu diễn Galois** (phía số học),

thông qua các hệ **hàm $$L$$** tương thích với nhau.

![Cầu Langlands]({{ site.baseurl }}/img/chapter_img/ngo_langlands_bridge.svg)

*Hình. Sơ đồ tương ứng Langlands, với hàm $$L$$ làm cầu nối.*

Các trường hợp đặc biệt và các hướng liên quan gồm:

- lý thuyết trường các lớp abel (tiền thân cổ điển);
- tính modular của đường cong elliptic (Wiles và các cộng sự; một mặt khác, cũng rất nổi tiếng, của chương trình Langlands);
- chương trình **Langlands hình học** (một phiên bản song song trên đường cong); xem bài chuyên sâu [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) về cầu nối Kapustin–Witten / Hitchin.

Công trình được giải Fields của Ngô là về một đẳng thức giải tích–hình học chính xác, cần cho **phép so sánh nội soi**, chứ không phải viết lại toàn bộ chương trình. Khi đọc lời trích dẫn của giải thưởng, hãy phân biệt hai tầng: **tầm nhìn** (của Langlands) và **nút thắt kỹ thuật** (Bổ đề Cơ bản).

Một hình ảnh dễ nhớ: Langlands vẽ bản đồ các cây cầu giữa số học và giải tích; lý thuyết nội soi là quy tắc cho phép chuyển dữ liệu giữa các nhóm; Bổ đề Cơ bản là tấm biển báo còn thiếu, khiến nhiều đoạn đường chỉ được mở "có điều kiện".

---

## 2. Công thức vết như một công cụ so sánh

Công thức vết **Arthur–Selberg** (và dạng ổn định của nó) cân bằng **phía phổ** (các biểu diễn tự đẳng cấu và bội của chúng) với **phía hình học** (các tích phân quỹ đạo, các lớp liên hợp).

Để đồng nhất dữ liệu tự đẳng cấu trên nhóm $$G$$ với dữ liệu trên một nhóm nội soi $$H$$, cần khớp các số hạng hình học: một số tích phân quỹ đạo trên $$G$$ phải bằng các tích phân tương ứng trên $$H$$ (kèm theo **hệ số chuyển**, transfer factor). Họ các đẳng thức đó chính là **Bổ đề Cơ bản** và các biến thể của nó.

![Nút thắt công thức vết]({{ site.baseurl }}/img/chapter_img/ngo_trace_formula_bottleneck.svg)

*Hình. Nếu chưa có đẳng thức giữa các tích phân quỹ đạo, phép chuyển nội soi vẫn phải kèm điều kiện.*

### Vì sao việc này khó

Tích phân quỹ đạo thuộc về **giải tích điều hòa địa phương**, thường trên trường $$p$$-adic, nơi việc tính toán cụ thể cực kỳ khó, trừ khi hạng thấp. Trong nhiều thập niên, nhiều định lý sâu của chương trình Langlands chỉ được chứng minh **có điều kiện**: "nếu Bổ đề Cơ bản đúng thì …"

Về mặt ý tưởng, đây là một ví dụ kinh điển: một đẳng thức **địa phương** cản trở các ứng dụng **toàn cục**. Phía phổ của công thức vết nói về các dạng tự đẳng cấu toàn cục; phía hình học đòi hỏi các số liệu địa phương phải khớp nhau. Lý thuyết nội soi muốn chuyển thông tin giữa các nhóm; nếu các tích phân không khớp, phép chuyển không hoàn tất được.

---

## 3. Bổ đề Cơ bản phát biểu gì (tóm tắt)

Dạng thô (bỏ qua hệ số chuyển và miền xác định chính xác):

> Một số tích phân quỹ đạo đã chuẩn hóa trên một nhóm rút gọn được, ứng với các phần tử chính quy, bằng các tích phân tương ứng trên nhóm nội soi.

Có phiên bản cho **đại số Lie** và cho **nhóm**; dạng đại số Lie thường là phần kỹ thuật cốt lõi trong công trình của Ngô.

Không cần công thức đầy đủ vẫn hiểu được **vai trò** của bổ đề: đó là đẳng thức còn thiếu để phía hình học của hai công thức vết "nói chuyện" được với nhau. Chữ "bổ đề" trong tên gọi phản ánh vị trí lịch sử của nó (từng được xem là một bước kỹ thuật trung gian), nhưng tầm ảnh hưởng của nó là ở **cấu trúc tổng thể**, không phải một chi tiết nhỏ.

### Lý thuyết nội soi trong một câu

Lý thuyết nội soi so sánh dữ liệu tự đẳng cấu (và các số hạng hình học) của nhóm $$G$$ với dữ liệu của các nhóm "nội soi" $$H$$ nhỏ hơn hoặc có cấu trúc khác, theo các quy tắc do Langlands–Shelstad và những người kế tục xây dựng. Hệ số chuyển đóng vai trò như hệ số trong một cuốn từ điển; Bổ đề Cơ bản là đẳng thức tích phân cốt lõi.

---

## 4. Các kết quả từng phần trước định lý tổng quát

Rất nhiều nhà toán học đã đóng góp các trường hợp đặc biệt và các cách phát biểu lại (hệ số chuyển của Langlands–Shelstad; công trình của Kottwitz, Waldspurger, Hales, Laumon, …). Đây là một cuộc chạy tiếp sức.

**Laumon–Ngô (2004).**  
Chứng minh Bổ đề Cơ bản cho **nhóm unita** trong một bối cảnh quan trọng, cho thấy cách tiếp cận hình học có thể đi xa hơn những tính toán riêng lẻ cho hạng thấp.

**Ngô (trường hợp tổng quát).**  
Mở rộng phương pháp hình học để chứng minh bổ đề ở mức tổng quát cần cho các ứng dụng nội soi chính, trình bày trong bài *Le lemme fondamental pour les algèbres de Lie*, *Publications Mathématiques de l’IHÉS* (2010).

Phân biệt giữa kết quả năm 2004 và kết quả tổng quát rất quan trọng khi viết tiểu luận hay trả lời câu hỏi thảo luận: Laumon–Ngô là bước đột phá cho thấy "phương pháp hình học hiệu quả"; còn Ngô là người hoàn tất cho họ ứng dụng trung tâm.

---

## 5. Hình học xuất hiện: phân thớ kiểu Hitchin

Bước ngoặt về ý tưởng của Ngô không phải là một phép tính $$p$$-adic dài hơn. Đó là một phép **chuyển ngôn ngữ**:

1. Diễn đạt đẳng thức tích phân cần chứng minh bằng việc đếm điểm / các bất biến đối đồng điều của những đối tượng hình học.  
2. Sắp xếp các đối tượng đó thành các thớ của một ánh xạ giống **phân thớ Hitchin** trong hình học các phân thớ Higgs / phân thớ đại số Lie trên đường cong.  
3. Dùng định lý về giá (support theorem) và sự phân tách của đối đồng điều để so sánh các thớ ứng với dữ liệu nội soi.  
4. Suy ra đẳng thức giải tích.

![Hình học bước vào]({{ site.baseurl }}/img/chapter_img/ngo_geometry_hitchin.svg)

*Hình. Từ tích phân quỹ đạo $$p$$-adic đến các thớ hình học, rồi quay về Bổ đề Cơ bản.*

Đó là lý do lời trích dẫn giải Fields nhấn mạnh **các phương pháp đại số–hình học mới**: hình học không phải để trang trí, mà chính là công cụ chứng minh. Một thớ riêng lẻ cho một con số; cả một **phân thớ** cho một họ, cho phép so sánh theo tham số, kiểm soát giá, và truyền thông tin giữa các thớ nội soi.

### Vì sao hình học có thể "biết" giá trị của tích phân

Trong nhiều bối cảnh, tích phân quỹ đạo liên quan đến việc đếm (có trọng số) các điểm trên các quỹ đạo hoặc trên các không gian liên quan. Đối đồng điều étale / ℓ-adic của thớ mang thông tin số học đó dưới dạng vết của phép Frobenius. Nếu hai phía nội soi có cùng "gói đối đồng điều" (sau một phép so sánh thích hợp) thì các tích phân bằng nhau. Tóm tắt:

$$
\text{tích phân quỹ đạo}
\;\longleftrightarrow\;
\text{hình học thớ Hitchin}
\;\longleftrightarrow\;
\text{so sánh endoscopic}.
$$

---

## 6. Hệ quả sau khi có bổ đề

Khi đã có Bổ đề Cơ bản, nhiều định lý có điều kiện trở thành vô điều kiện, theo các hướng:

- ổn định hóa công thức vết;  
- chương trình phân loại nội soi (Arthur và những người kế tục);  
- các phép so sánh dẫn đến những trường hợp đặc biệt của **tính hàm tử** (functoriality) Langlands.

Bổ đề chỉ "kỹ thuật" ở chỗ phát biểu của nó rất chuyên biệt; còn **tác động** của nó là mở khóa cả cấu trúc so sánh. Sau năm 2010, các nhà toán học không còn phải viết "giả sử Bổ đề Cơ bản đúng" trong hàng loạt ứng dụng trung tâm.

---

## 7. Huy chương Fields 2010 và bối cảnh

- Trao tại Đại hội Toán học Thế giới (ICM) ở Hyderabad (2010).  
- Nơi công tác khi đó: **Université Paris-Sud**.  
- Sau này Ngô làm việc tại Đại học Chicago và vẫn là một nhân vật trung tâm của hình học số học.  
- Với cộng đồng toán học Việt Nam, giải thưởng là một cột mốc lớn; bản thân toán học thì mang tính quốc tế và hợp tác.

**Giải thưởng liên quan.** Robert Langlands nhận **Giải Abel 2018** cho toàn bộ chương trình, khác với Huy chương Fields của Ngô cho Bổ đề Cơ bản.

Ghi nhận công lao cho rõ ràng: Langlands đưa ra tầm nhìn; nhiều người xây dựng lý thuyết nội soi; Laumon–Ngô mở ra hướng hình học; Ngô chứng minh trường hợp tổng quát; cả cộng đồng "gỡ điều kiện" khỏi các định lý.

---

## 8. Vì sao bài này quan trọng trong chương

Chủ đề của Chương 2 là toán học hiện đại ở tầm giải thưởng lớn, xem như những **cây cầu nối** giữa các lĩnh vực:

| Cầu nối | Bài |
|---------|-----|
| Giải tích ↔ tô pô | [Perelman]({{ site.baseurl }}/contents/vi/chapter02/) |
| Tổ hợp ↔ số nguyên tố | [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/) |
| Hình học ↔ giải tích tự đẳng cấu | **Ngô** |
| Hệ động lực ↔ không gian moduli | [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/) |
| Nền tảng $$p$$-adic | [Scholze]({{ site.baseurl }}/contents/vi/chapter02/) |
| Giải tích điều hòa nhiều thang đo | Wang |

Câu chuyện của Ngô là ví dụ rõ nhất về việc "hình học bất ngờ giải được một bài toán giải tích khó" trong số các huy chương đầu tiên của chương.

---

## 9. Nhìn lại điều nghịch lý

Một đẳng thức **tích phân địa phương** đã cản trở cả một chương trình **toàn cục** về dạng tự đẳng cấu và biểu diễn Galois. Đẳng thức đó được chứng minh bằng **phép đếm hình học** trên trường hữu hạn và trường địa phương. Điều đáng nhớ: chữ "bổ đề" nghe thì nhỏ; vai trò thì lớn; còn công cụ chứng minh lại đến từ một lĩnh vực có vẻ khác hẳn (hình học Hitchin) so với ngôn ngữ ban đầu (tích phân quỹ đạo $$p$$-adic).

---

## 9b. Langlands số học và Langlands hình học: phân biệt cho rõ

*Tổng hợp từ các video trong khóa học (theo phong cách Frenkel, bộ tư liệu Langlands) và các bài tổng quan; không chép phụ đề tự động. Bài chuyên sâu: [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/).*

### C1. Hai chương trình, cùng ý tưởng về nhóm đối ngẫu

| | **Langlands số học** (chủ đề của bài này) | **Langlands hình học** |
|--|----------------------------------------|-------------------------|
| Nền | Trường số / adele | Đường cong (thường trên $$\mathbb{C}$$) |
| Đối tượng "tự đẳng cấu" | Biểu diễn tự đẳng cấu của $$G(\mathbb{A})$$ | Bó / D-môđun trên $$\mathrm{Bun}_G(C)$$ |
| Đối tượng "Galois / phổ" | Biểu diễn Galois / motive | Hệ địa phương / dữ liệu phổ cho $$G^\vee$$ |
| Nhóm đối ngẫu | $$G^\vee$$ | $$G^\vee$$ |
| Bổ đề của Ngô | Công cụ cho **nội soi / công thức vết** | Không phải cùng một định lý |

**Điều cần nhớ.** Nói "Langlands" mà không nói rõ loại nào là mơ hồ. Công trình được giải Fields của Ngô chứng minh **một đẳng thức so sánh** trong bộ máy công thức vết của chương trình số học. Điều đó **không** có nghĩa "Langlands hình học đã xong", và **không** có nghĩa "toàn bộ chương trình Langlands đã được chứng minh".

### C2. Cầu nối với vật lý (nói đúng tình trạng)

Kapustin–Witten và các công trình liên quan diễn giải Langlands hình học như được chi phối bởi **đối ngẫu S** của lý thuyết siêu Yang–Mills $$\mathcal N=4$$ trong 4 chiều (với đối xứng gương của không gian Hitchin làm phần hình học). Đó là một **bộ từ điển và nguồn cảm hứng nghiên cứu** mạnh, nhưng không thay thế chứng minh toán học. Xem thêm [bài ngắn về Witten]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/).

### C3. Một câu tóm tắt khi thảo luận

Có thể dùng câu: *"Ngô chứng minh Bổ đề Cơ bản cho phép so sánh nội soi; chương trình Langlands vẫn là một mạng lưới giả thuyết; Langlands hình học là một chương trình song song (ở ngôn ngữ phạm trù) có chung nhóm đối ngẫu $$G^\vee$$."*

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Ngô sáng lập chương trình Langlands." | **Sai** | Langlands đề ra chương trình; Ngô chứng minh một bổ đề trung tâm. |
| "Bổ đề Cơ bản chỉ là một chi tiết kỹ thuật nhỏ." | **Sai** | Nó cản trở các ứng dụng lớn trong nhiều thập niên. |
| "Chứng minh chỉ là biến đổi các tích phân $$p$$-adic." | **Sai** | Hình học là then chốt. |
| "Laumon–Ngô năm 2004 đã giải xong trường hợp tổng quát." | **Sai** | Năm 2004 là một họ đặc biệt quan trọng; trường hợp tổng quát đến sau. |
| "Langlands đoạt giải Fields nhờ điều này." | **Sai** | Langlands: Giải Abel 2018; Ngô: Huy chương Fields 2010. |
| "Ngô đã chứng minh Langlands hình học / toàn bộ Langlands." | **Sai** | Bổ đề Cơ bản phục vụ lý thuyết nội soi; xem mục 9b. |
| "Langlands số học và Langlands hình học là cùng một định lý." | **Sai** | Cùng ý tưởng về nhóm đối ngẫu, nhưng đối tượng và bối cảnh khác nhau. |

---

## Bài tập

1. **Khởi động.** Bằng lời của bạn: chương trình Langlands muốn nối hai thế giới nào?  
2. **Vai trò.** Điền vào ba ô: phía phổ / phía hình học / Bổ đề Cơ bản.  
3. **Lịch sử.** Vẽ trục thời gian: Langlands (thập niên 1960–1970) → các trường hợp riêng của Bổ đề Cơ bản → Laumon–Ngô (2004) → Ngô, trường hợp tổng quát → Fields 2010.  
4. **Hình học.** Vì sao đối đồng điều của các thớ có thể mã hóa một đẳng thức giữa các con số (tích phân)?  
5. **Ghi nhận công lao.** Viết hai câu theo văn phong phổ thông, nhắc đến cả Laumon–Ngô lẫn định lý tổng quát của Ngô.  
6. **Đọc tài liệu nghiên cứu.** Mở phần tóm tắt của một bài tổng quan về Bổ đề Cơ bản; liệt kê ba thuật ngữ cần tra tiếp (ví dụ hệ số chuyển, liên hợp ổn định, nội soi).  
7. **Liên hệ trong chương.** Viết một đoạn so sánh ý "hình học mở khóa giải tích" của Ngô với cách Scholze viết lại hình học $$p$$-adic bằng không gian perfectoid (công cụ khác nhau, cùng một tinh thần).  
8. **So sánh.** Nêu một khác biệt giữa thành công kiểu Wiles (tính modular) và thành công kiểu Ngô (Bổ đề Cơ bản) trong chương trình Langlands.

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Video và tài liệu gốc dùng để **định hướng và làm quen với không khí nghiên cứu**. Chi tiết: `research/video-research/Langlands_Program/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Quanta, *The Biggest Project in Modern Mathematics*: [YouTube](https://www.youtube.com/watch?v=_bJeKUosqoY).  
2. **Bối cảnh** — Numberphile, *The Langlands Program* (Frenkel): [YouTube](https://www.youtube.com/watch?v=4dyytPboqvE).  
3. **Nghiên cứu** — Ngô B. C., tích phân quỹ đạo (IHÉS, phần 1/3): [YouTube](https://www.youtube.com/watch?v=74aq5gIDrFQ).  
4. **Không bắt buộc** — bài giảng Abel của Frenkel: [YouTube](https://www.youtube.com/watch?v=b8e_HMEwKIY); Wiles (Oxford): [YouTube](https://www.youtube.com/watch?v=ZFOPxZtlkig).

**Nhắc lại:** Bổ đề Cơ bản **đã được chứng minh**. Chương trình Langlands nói chung vẫn **còn mở**. Đừng nhầm "Ngô đã giải xong Langlands".

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Langlands_Program/transcripts/` · trạng thái: `research/video-research/Langlands_Program/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Langlands_Program_74aq5gIDrFQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Langlands_Program/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=74aq5gIDrFQ  
2. https://www.youtube.com/watch?v=4dyytPboqvE  
3. https://arxiv.org/abs/0801.0446  
4. https://arxiv.org/pdf/0801.0446  
5. https://arxiv.org/abs/1103.4066  
6. https://www.claymath.org/library/cw/arthur/pdf/icm-ngo.pdf  
7. https://math.uchicago.edu/~ngo/survey.pdf  
8. https://www.ias.edu/ideas/2010/fundamental-lemma  
9. https://en.wikipedia.org/wiki/Fundamental_lemma_(Langlands_program)  
10. https://en.wikipedia.org/wiki/Langlands_program  
11. https://en.wikipedia.org/wiki/Ng%C3%B4_B%E1%BA%A3o_Ch%C3%A2u  
12. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010  
13. https://www.youtube.com/watch?v=_bJeKUosqoY  
14. https://www.youtube.com/watch?v=b8e_HMEwKIY  
15. https://www.youtube.com/watch?v=ZFOPxZtlkig  
16. https://www.numberphile.com/videos/the-langlands-program  

### Bộ tư liệu nghiên cứu

17. Bộ tư liệu của khóa học: `research/video-research/Langlands_Program/`.

1. Tư liệu của **IMU về Huy chương Fields 2010** cho Ngô Bảo Châu.  
2. **B. C. Ngô** (2010). *Le lemme fondamental pour les algèbres de Lie*. *Publ. Math. IHÉS*.  
3. **G. Laumon & B. C. Ngô** — công trình về Bổ đề Cơ bản cho nhóm unita (giai đoạn 2004).  
4. Các bài tổng quan về lý thuyết nội soi / Bổ đề Cơ bản (Arthur; Bourbaki / ICM).  
5. Kiến thức nền: sách nhập môn về dạng tự đẳng cấu của Knapp / Bump; nâng cao: các tập về phân loại nội soi của Arthur.  
6. Các bài giới thiệu phổ thông / của các viện: chỉ dùng cho tiểu sử, không thay thế các bài tổng quan kỹ thuật.

*Ghi chú.* Khung lịch sử theo các tài liệu chuẩn của IMU / bài ca ngợi tại lễ trao giải, và theo bài báo của Ngô trên IHÉS. Các hình trong bài là sơ đồ minh họa ý tưởng.

---

## Hướng đi tiếp

- Nghe một bài giảng tổng quan khoảng một giờ về lý thuyết nội soi dành cho người ngoài ngành.  
- Xem lại tính modular của đường cong elliptic như một cột mốc khác của chương trình Langlands, với cách chứng minh hoàn toàn khác.  
- Nếu muốn đi xa hơn: tìm hiểu hệ số chuyển Langlands–Shelstad, "hệ số từ điển" đi kèm với bổ đề.  
- Ghi lại một câu hỏi cụ thể bạn vẫn còn thắc mắc; đặt được câu hỏi tốt cũng là một phần của việc làm toán.  
- Đọc song song bài [Scholze]({{ site.baseurl }}/contents/vi/chapter02/) để so sánh hai cách hình học đi vào số học.

## Video tham khảo

- **Xem trước:** [The Biggest Project in Modern Mathematics](https://www.youtube.com/watch?v=_bJeKUosqoY) — Quanta Magazine, tiếng Anh. Giới thiệu tổng quan chương trình Langlands; nên xem trước khi đọc bài.
- [The Langlands Program - Numberphile](https://www.youtube.com/watch?v=4dyytPboqvE) — Numberphile, tiếng Anh. Edward Frenkel giải thích ý tưởng của chương trình Langlands; nên xem sau khi đã nắm ý chính của bài.
- [Bao Chau Ngo - 1/3 Orbital integrals, moduli spaces and invariant theory](https://www.youtube.com/watch?v=74aq5gIDrFQ) — Institut des Hautes Etudes Scientifiques (IHES), tiếng Anh. Xem thêm sau hai video trên; bài giảng của chính Ngô Bảo Châu về tích phân quỹ đạo và không gian moduli.
