---
layout: post
title: "Mirror Symmetry (Deep Dive)"
chapter: '06'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: deep-dive
---

**Đối xứng gương** (mirror symmetry) bắt đầu từ một phát hiện bất ngờ của lý thuyết dây: hai không gian Calabi–Yau trông rất khác nhau về hình học phức và hình học symplectic lại có thể cho **cùng các dự đoán vật lý**. Toán học tiếp nhận phát hiện đó và phát triển thành hai chương trình lớn, **đối xứng gương đồng điều (HMS)** và bức tranh hình học **Strominger–Yau–Zaslow (SYZ)**, cùng với một mạng lưới các phép đối ngẫu trong hình học đếm. Bài đọc sâu này mở rộng ý chính trong bài [Đối ngẫu như một nguyên lý]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/). Bài **không** chứng minh HMS và không dựng cặp gương bằng tay.

**Lộ trình:** nguồn gốc vật lý → mô hình A và mô hình B → lật số Hodge và hình học đếm → SYZ như phép đối ngẫu T hình học → HMS (Kontsevich) → bảng trạng thái → cầu nối với Langlands → bài tập.

Gói nghiên cứu: `research/video-research/mirror-symmetry/`.

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- Phát biểu **ý chính về mặt vật lý** của đối xứng gương và phân biệt **mô hình A / mô hình B** trong toán học.
- Giải thích trực giác về **kim cương Hodge** (số moduli phức và số moduli Kähler đổi vai cho nhau).
- Phân biệt **SYZ** (đối ngẫu T hình học của một phân thớ xuyến) với **HMS** (tương đương giữa các phạm trù).
- Ghi trạng thái trung thực: đâu là các định lý đã chứng minh cho từng trường hợp, đâu là chương trình còn mở (**tính đến 2026**).
- Liên hệ đối xứng gương với đối ngẫu T và với Langlands hình học / đối ngẫu Hitchin ở mức ý tưởng.
- Tránh khẳng định "lý thuyết dây đã chứng minh hết hình học đại số".

**Kiến thức cần có.** Bài nguyên lý đối ngẫu; biết tên các khái niệm "đa tạp phức" và "dạng symplectic". Phạm trù dẫn xuất và đồng điều Floer chỉ cần ở mức ý tưởng.

---

## 1. Ý tưởng đến từ đâu?

Cuối thập niên 1980 và đầu 1990, việc compact hóa lý thuyết dây trên các đa tạp Calabi–Yau ba chiều cho thấy những lý thuyết trên mặt quét (worldsheet) gắn với các hình học khác nhau lại cho cùng các hàm tương quan. Sự trùng khớp đó gợi ý một **ánh xạ gương**: không gian moduli cấu trúc phức của $$X$$ ghép cặp với không gian moduli Kähler của đa tạp đối ngẫu $$\check X$$, và ngược lại. Việc đếm các đường cong chỉnh hình ở một phía khớp với các tích phân chu kỳ (period) và biến thiên cấu trúc Hodge ở phía kia. Đây là một công cụ tính toán mạnh đáng kinh ngạc.

Câu hỏi của toán học là: *định lý nào nằm bên dưới từ điển vật lý này?* Có hai câu trả lời chính trong nghiên cứu hiện đại.

---

## 2. Mô hình A và mô hình B

| Phía | Hình học được dùng | Dữ liệu điển hình |
|-----|---------------|-------------------|
| **Mô hình A** | Cấu trúc symplectic của $$X$$ | Đường cong giả chỉnh hình; bất biến Gromov–Witten; **phạm trù Fukaya** gồm các đa tạp con Lagrange và đồng điều Floer |
| **Mô hình B** | Cấu trúc phức của $$\check X$$ | Phân thớ / bó chỉnh hình; **phạm trù dẫn xuất** $$D^b\mathrm{Coh}(\check X)$$; tích phân chu kỳ |

Đối xứng gương (ở dạng chính xác hơn) khẳng định dữ liệu A của $$X$$ bằng dữ liệu B của $$\check X$$. Đây là một **phép đối ngẫu hình học**, không phải một đối xứng liên tục của một đa tạp.

**Đa tạp Calabi–Yau.** Đó là đa tạp phức có phân thớ chính tắc tầm thường (vật lý thường đòi thêm một metric Kähler phẳng Ricci). Hai đa tạp trong một cặp gương không cần vi phôi với nhau; chỉ cần dữ liệu đối ngẫu khớp nhau.

---

## 3. Số Hodge và công cụ cho hình học đếm

Với Calabi–Yau ba chiều, đối xứng gương cổ điển hoán đổi các số Hodge theo một quy luật đặc trưng (ví dụ $$h^{1,1}(X)$$ với $$h^{2,1}(\check X)$$), gọi là **lật kim cương Hodge**. Sâu hơn, hàm sinh các bất biến Gromov–Witten giống 0 ở một phía khớp với các tích phân chu kỳ (hệ số Yukawa) ở phía kia, sau khi đổi tọa độ bằng ánh xạ gương.

**Về mặt học tập.** Bạn không cần tính một bất biến Gromov–Witten nào. Bạn cần nắm **hình dạng** của câu chuyện: bài toán đếm đường cong khó ↔ tích phân của các dạng chỉnh hình sau một phép đổi biến.

---

## 4. SYZ: đối xứng gương như đối ngẫu T

**Strominger, Yau và Zaslow (1996)** đề xuất một cơ chế hình học: cả $$X$$ và $$\check X$$ đều là phân thớ trên cùng một đáy, với thớ là các xuyến **Lagrange đặc biệt**, và các thớ của đa tạp gương là xuyến đối ngẫu (đối ngẫu T theo từng thớ). Các thớ kỳ dị mang theo dữ liệu đơn đạo (monodromy) và tập phân biệt, đóng vai trò then chốt.

| Điểm mạnh của SYZ | Khó khăn của SYZ |
|--------------|-------------|
| Giải thích *vì sao* cặp gương tồn tại, như hai phân thớ xuyến đối ngẫu | Rất khó dựng một phân thớ Lagrange đặc biệt trơn trên toàn cục |
| Nối với đối ngẫu T trong vật lý | Cần các cách phát biểu tinh chỉnh (thường theo hình học đại số): Gross–Siebert, … |

**Trạng thái.** SYZ là một **chương trình nghiên cứu**, không phải một định lý đã hoàn chỉnh cho mọi Calabi–Yau. Các trường hợp địa phương và toric được hiểu tốt hơn; bức tranh trơn toàn cục vẫn còn nhiều khó khăn.

---

## 5. Đối xứng gương đồng điều (Kontsevich)

**Kontsevich (1994)** nâng sự trùng khớp trong hình học đếm lên thành một phát biểu về phạm trù, gọi là **HMS**:

$$
D^\pi\mathrm{Fuk}(X)\;\simeq\; D^b\mathrm{Coh}(\check X)
$$

(có nhiều biến thể: làm đầy Karoubi, mô hình Landau–Ginzburg, phạm trù Fukaya bọc, …). Ở phía A, đối tượng là các đa tạp con Lagrange kèm hệ địa phương, cấu xạ là đối đồng điều Floer. Ở phía B, đối tượng là các phức bó chỉnh hình, cấu xạ là các nhóm Ext.

**Vì sao đây là một nguyên lý đối ngẫu.** Toàn bộ **đại số đồng điều** của hai phía khớp nhau: mọi định lý phát biểu được trong một phạm trù dẫn xuất đều có một bản sao đối ngẫu. Nhiều trường hợp đặc biệt (đường cong elliptic, đa tạp Fano toric, một số Calabi–Yau địa phương, …) **đã được chứng minh**; giả thuyết tổng quát vẫn còn mở.

---

## 6. Bảng trạng thái (đừng bỏ qua)

| Phát biểu | Trạng thái (2026) |
|-----------|-------------|
| Nhiều phép đối ngẫu trong hình học đếm / ánh xạ gương cho các họ cụ thể | Định lý / đã vững chắc |
| HMS cho nhiều lớp ví dụ | Các định lý cho từng trường hợp |
| HMS đầy đủ cho Calabi–Yau tổng quát | Chương trình còn mở |
| Phân thớ SYZ trơn toàn cục | Còn mở / chương trình đang được tinh chỉnh |
| Các dự đoán từ vật lý | Nguồn cảm hứng và từ điển; toán học vẫn phải chứng minh |

---

## 7. Cầu nối trong khóa học

| Bài liên quan | Liên hệ |
|------------|----------|
| [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/) | Bài tổng quan |
| [AdS/CFT]({{ site.baseurl }}/contents/vi/chapter06/06_14_AdS_CFT/) | Một kiểu đối ngẫu vật lý khác (nguyên lý toàn ảnh) |
| [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) | Các hệ Hitchin cho $$G$$ / $$G^\vee$$ là cặp gương kiểu SYZ |
| [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) | Giao diện giữa lý thuyết gauge và lý thuyết dây |
| [Pardon và hình học symplectic]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) | Bối cảnh hình học symplectic |

---

## 8. Những nhầm lẫn thường gặp

| Khẳng định | Chỉnh lại |
|------------|-----------|
| "Cặp gương là cùng một đa tạp viết hai lần." | Hai đa tạp có thể khác nhau về tô pô; chỉ có *dữ liệu* đối ngẫu là khớp nhau. |
| "HMS chỉ là chuyện số Hodge." | Số Hodge chỉ là cái bóng cổ điển; HMS là phát biểu ở mức phạm trù. |
| "SYZ đã được chứng minh đầy đủ." | Đó là một chương trình với các kết quả bộ phận. |
| "Đối ngẫu T luôn luôn là đối xứng gương." | SYZ đề xuất đối ngẫu T như cơ chế; nhưng không phải phép đối ngẫu nào cũng là đối ngẫu theo vòng tròn compact. |
| "Vật lý đã làm xong phần toán." | Vật lý cung cấp từ điển; chứng minh là việc của toán học. |

---

## Bài tập

1. Viết một đoạn so sánh mô hình A và mô hình B.  
2. Việc lật kim cương Hodge giúp ích gì cho tính toán?  
3. Phát biểu SYZ trong không quá 3 câu; nêu một khó khăn.  
4. Viết ý chính của HMS như một tương đương phạm trù (viết không hình thức cũng được).  
5. **Không quá 150 chữ:** vì sao đối xứng gương là một phép *đối ngẫu* theo nghĩa của bài nguyên lý?  
6. Đọc hiểu trạng thái: nêu một định lý cho trường hợp cụ thể và một chương trình còn mở.  
7. **Không bắt buộc:** đọc lướt phần tóm tắt bài của Auroux về phạm trù Fukaya; liệt kê ba thuật ngữ mới.

---

## Ghi chú viết lại từ video chính

*Viết lại từ phụ đề tự động của bài nói của Witten (Fields Medal Symposium 2012). Phụ đề: `research/video-research/mirror-symmetry/transcripts/`. Các đơn vị kiến thức: `knowledge_units_mode_c.json`. Đây là phần viết lại, không chép nguyên văn phụ đề.*

### C1. Vì sao Langlands hình học "cần" bốn chiều

Witten nối ngôn ngữ của **đối xứng gương** với **Langlands hình học**. Một lý thuyết trường lượng tử $$d$$ chiều gán một **phạm trù các điều kiện biên** cho mỗi đa tạp đóng $$d-2$$ chiều. Langlands hình học gán phạm trù cho các **mặt Riemann** (đa tạp 2 chiều), nên $$d=4$$: ta phải bắt đầu từ một lý thuyết bốn chiều.

### C2. $$\mathcal N=4$$ SYM là lựa chọn tự nhiên

Trong số các lý thuyết gauge 4 chiều, lý thuyết có siêu đối xứng cực đại, **$$\mathcal N=4$$ super Yang–Mills**, là lựa chọn tự nhiên. Nhóm gauge $$G$$ và nhóm đối ngẫu của nó xuất hiện qua phép đối ngẫu; các "đối xứng lẻ" siêu đối xứng cung cấp vi phân dùng để xây dựng cấu trúc phạm trù.

### C3. Đối xứng gương và hệ Hitchin (không phải chứng minh)

Bài nói kết hợp **đối xứng gương** (brane, hình học đối ngẫu) với dữ liệu về **hệ Hitchin / không gian moduli các phân thớ**, vốn là nền tảng của Langlands hình học. Với khóa học này, đó là **bối cảnh nghiên cứu và từ điển**, không phải chứng minh đầy đủ HMS hay giả thuyết Langlands hình học. Đọc kèm [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) và [chân dung Witten]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/).

### C4. Ghi chú về phụ đề

- **Witten `S02ghGCdNDo`:** đã trích phụ đề tự động tiếng Anh (2026-08-05).  
- **Chan, HMS qua SYZ `Kz6Dj8KSFjM`:** không có phụ đề, chỉ xem hình; không tự đặt nội dung khi thiếu phụ đề.

---

## Nguồn video (gói nghiên cứu)

Dùng để định hướng, không thay cho các bài tổng quan khoa học. Gói: `research/video-research/mirror-symmetry/`.

1. **Định hướng / ghi chú ở trên:** Witten: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo) · phụ đề có trong gói  
2. **Nội dung chính (không có phụ đề):** Chan, HMS qua SYZ: [https://www.youtube.com/watch?v=Kz6Dj8KSFjM](https://www.youtube.com/watch?v=Kz6Dj8KSFjM)  
3. **Nghiên cứu:** Zaslow: [https://www.youtube.com/watch?v=Y3-sw3tjZiU](https://www.youtube.com/watch?v=Y3-sw3tjZiU)  
4. **Bài giảng:** MIT OCW, Mirror Symmetry: [https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/](https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/)  

Danh sách URL đầy đủ: `research/video-research/mirror-symmetry/references.md`.  
Trạng thái phụ đề: `research/video-research/mirror-symmetry/TRANSCRIPT_STATUS.md`.

---

## Tài liệu tham khảo

1. Kontsevich — https://arxiv.org/abs/alg-geom/9411018  
2. Strominger–Yau–Zaslow — https://arxiv.org/abs/hep-th/9606040  
3. Gross — SYZ survey — https://arxiv.org/abs/1212.4220  
4. Auroux — Fukaya — https://arxiv.org/abs/1301.7056  
5. Hori et al. — *Mirror Symmetry* (Clay)  
6. Wikipedia — Homological mirror symmetry; SYZ  
7. Gói: `research/video-research/mirror-symmetry/`  

## Video tham khảo

- **Xem trước:** [Edward Witten: Mirror Symmetry & Geometric Langlands (2012)](https://www.youtube.com/watch?v=S02ghGCdNDo) (Graduate Mathematics, tiếng Anh). Witten nối đối xứng gương với Langlands hình học, là nguồn của phần ghi chú ở trên. Nên xem trước để nắm bối cảnh.
- [HMS for local CY manifolds via SYZ | Kwokwai Chan](https://www.youtube.com/watch?v=Kz6Dj8KSFjM) (Harvard CMSA, tiếng Anh). Bài giảng nghiên cứu về HMS cho Calabi–Yau địa phương thông qua SYZ. Xem sau khi đã đọc mục 4 và 5.
- [Lagrangian fillings what does the sheaf say? | Eric Zaslow](https://www.youtube.com/watch?v=Y3-sw3tjZiU) (Harvard CMSA, tiếng Anh). Bài giảng nghiên cứu về các mặt lấp Lagrange và bó. Dành cho ai muốn đi sâu hơn.
