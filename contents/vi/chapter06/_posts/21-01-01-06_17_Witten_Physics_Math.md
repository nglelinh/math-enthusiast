---
layout: post
title: "Edward Witten: Vật lý đi vào hình học hiện đại"
chapter: '06'
order: 17
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: profile
---

Tháng 8 năm 1990, tại Đại hội Toán học Thế giới ở Kyoto, cả hội trường lặng đi khi **Huy chương Fields** — giải thưởng danh giá nhất của toán học thuần túy — được trao cho một nhà vật lý lý thuyết: **Edward Witten** (Viện Nghiên cứu Cao cấp Princeton, IAS). Trong suốt thế kỷ XX, toán học và vật lý đôi khi giống hai người hàng xóm nói hai thứ tiếng khác nhau: một bên đòi hỏi mọi viên gạch chứng minh phải khớp kín kẽ, bên kia lại sẵn sàng nhảy qua vực sâu bằng trực giác vật lý để chạm tới chân lý tự nhiên. Witten đã làm một điều hiếm có trong lịch sử khoa học hiện đại: ông lắng nghe những phép đối ngẫu táo bạo của lý thuyết trường lượng tử và lý thuyết dây, rồi dịch chúng thành những bài toán hình học và tô pô sắc nét đến mức cộng đồng toán học phải vẽ lại cả bản đồ nghiên cứu suốt ba thập kỷ sau đó.

Đây là một **chân dung ngắn** về phương pháp làm việc của Witten trong **nhánh đối ngẫu** của khóa học — không phải tiểu sử cá nhân, và cũng không phải giáo trình lý thuyết trường lượng tử. Điều ta muốn giữ lại sau bài này không phải là hào quang quanh một cái tên, mà là *cách một trực giác vật lý biến thành cấu trúc toán học chặt chẽ*.

---

## Kiến thức cần nhớ: Vật lý toán kiểu Witten là gì và nghiên cứu những gì?

Nếu bạn tốt nghiệp đại học với hành trang là giải tích nhiều biến, đại số tuyến tính, phương trình vi phân và chút cơ học lượng tử sơ cấp, bạn có thể thắc mắc: *vật lý toán hiện đại* — đặc biệt là phong cách của Witten — thực chất đang nối những nhánh toán học nào lại với nhau?

### 1. Tô pô chiều thấp và lý thuyết bất biến (Nút & Đa tạp 3–4 chiều)
Tô pô nghiên cứu những tính chất không đổi khi ta kéo giãn, uốn cong nhưng không cắt xé không gian — chẳng hạn phân biệt hai sợi dây thắt nút trong không gian 3 chiều, hay phân biệt hai cấu trúc khả vi khác nhau trên cùng một không gian 4 chiều. Công cụ truyền thống là các bất biến đại số (nhóm cơ bản, đa thức nút). Phong cách Witten tạo ra những bất biến hoàn toàn mới bằng cách đặt một **lý thuyết trường lượng tử tô pô (TQFT)** lên chính đa tạp đó.

### 2. Hình học đếm và không gian moduli (Moduli Spaces)
Một câu hỏi kinh điển của hình học đại số: trên một mặt cong phức (hay đa tạp Calabi–Yau 6 chiều), có bao nhiêu đường cong đại số bậc $$d$$ đi qua một số điểm cho trước? Việc đếm trực tiếp cực kỳ khó khi bậc $$d$$ tăng. Khi nhìn bằng con mắt lý thuyết dây (đối xứng gương), số đường cong đó trở thành hệ số trong khai triển năng lượng của một hệ vật lý — và phép đối ngẫu biến bài toán đếm siêu khó trên không gian $$X$$ thành phép tính tích phân giải tích cổ điển trên không gian gương $$Y$$!

### 3. Lý thuyết trường lượng tử tô pô (TQFT) và đối ngẫu S
Khác với vật lý thông thường phụ thuộc vào khoảng cách (metric), một **TQFT** chỉ phụ thuộc vào dáng tô pô. Nhờ đó, các đại lượng vật lý (hàm phân hoạch $$Z(M)$$, giá trị kỳ vọng vòng Wilson) **tự động trở thành bất biến tô pô** của đa tạp $$M$$. Còn khi hai lý thuyết vật lý khác hẳn nhau lại đối ngẫu (như đối ngẫu S hoán đổi điện tích–từ tích và tương tác mạnh–yếu), hai đối tượng toán học đứng sau chúng buộc phải tương đương — đóng vai trò một **cỗ máy sinh giả thuyết hình học** với độ chính xác đáng kinh ngạc.

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- Đặt Huy chương Fields 1990 của Witten vào bối cảnh "toán học được gợi ý từ vật lý".
- Nêu ít nhất 3 chủ đề có ảnh hưởng lớn trong hình học và tô pô hiện đại (bất biến nút và lý thuyết Chern–Simons, đối xứng gương, Langlands hình học và đối ngẫu S, …).
- Nắm nguyên tắc của khóa học: **vật lý là nguồn cảm hứng và cầu nối, không tự động thành chứng minh**.
- Liên hệ Witten với các bài [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/), [đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/), [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/).
- Tránh việc chỉ tôn vinh tên tuổi: luôn nêu rõ **cấu trúc toán học** cụ thể, không chỉ nêu tên người.

**Kiến thức cần có.** Bài nguyên lý đối ngẫu; bài tổng quan về vật lý toán.

---

## 1. Vì sao một nhà vật lý xuất hiện trong khóa học toán

Lịch sử giao thoa giữa hình học và vật lý vốn đã rất dài: thuyết tương đối rộng của Einstein đưa hình học Riemann lên sân khấu trung tâm, còn lý thuyết trường chuẩn (gauge) và lý thuyết chỉ số Atiyah–Singer kéo giải tích, tô pô và vật lý hạt lại gần nhau. Nhưng bước ngoặt từ thập niên 1980 mang một sắc thái hoàn toàn mới: **lý thuyết trường lượng tử và lý thuyết dây** bắt đầu sinh ra hàng loạt *từ điển dạng giả thuyết* vô cùng cụ thể — hàm tương quan ứng với số giao của các đa tạp con, đối ngẫu vật lý ứng với tương đương phạm trù, còn dị thường lượng tử ứng với chỉ số tô pô của toán tử vi phân.

Hãy lấy ví dụ nổi tiếng nhất dẫn tới Huy chương Fields 1990: năm 1984, nhà toán học Vaughan Jones bất ngờ tìm ra một đa thức mới (đa thức Jones) giúp phân biệt hai nút thắt trong không gian 3 chiều. Khi mới xuất hiện, công thức tổ hợp của đa thức Jones trông như một phép tính đại số thuần túy, khó thấy ý nghĩa hình học 3 chiều của nó ở đâu. Đến năm 1989, Witten chỉ ra rằng nếu ta xét lý thuyết trường lượng tử tô pô **Chern–Simons** trong không gian 3 chiều, rồi tính giá trị kỳ vọng của một "vòng Wilson" chạy dọc theo chính sợi dây thắt nút đó, kết quả thu được *chính là đa thức Jones* — đồng thời tự động mở rộng sang bất kỳ đa tạp 3 chiều cong nào!

### Giải thích: làm sao một TQFT lại "đếm" được hình dáng không gian?

Để không cảm thấy hai chữ "TQFT" mơ hồ, hãy tự tay tính một **mô hình TQFT 2 chiều** hoàn chỉnh chỉ bằng đại số tuyến tính! Theo định lý phân loại Atiyah–Dijkgraaf, một TQFT 2 chiều tương đương hoàn toàn với một **đại số giao hoán Frobenius** $$(A, \theta)$$: không gian trạng thái trên một đường tròn là đại số $$A$$, phép ghép hai đường tròn thành một ("chiếc quần" — pair of pants) là phép nhân trong $$A$$, còn "nắp đậy" bán cầu là phiếm hàm vết $$\theta: A \to \mathbb{C}$$.

Hãy chọn ví dụ cụ thể nhỏ nhất: lấy $$A = \mathbb{C}e_1 \oplus \mathbb{C}e_2$$ với quy tắc nhân trực giao $$e_1^2 = e_1,\ e_2^2 = e_2,\ e_1 e_2 = 0$$ (đơn vị $$1 = e_1 + e_2$$) và chọn vết $$\theta(e_1) = 1,\ \theta(e_2) = \frac{1}{2}$$.

1. **Dựng "toán tử tay cầm" $$H$$ (gắn thêm một lỗ donut vào mặt cong):** Dạng song tuyến tính $$\eta(a,b) = \theta(ab)$$ là ma trận đường chéo $$\operatorname{diag}(1, \tfrac{1}{2})$$, nên cơ sở đối ngẫu là $$e^1 = e_1$$ và $$e^2 = 2e_2$$. Phép cắt rồi dán lại một tay cầm ứng với phép nhân với phần tử
   $$
   H = e_1 e^1 + e_2 e^2 = e_1 + 2e_2.
   $$
2. **Tính hàm phân hoạch $$Z(\Sigma_g)$$ cho mặt cong kín có $$g$$ lỗ bằng cách nhân $$H$$ đúng $$g$$ lần rồi lấy vết $$\theta$$:**
   - **Mặt cầu $$S^2$$ ($$g=0$$ lỗ):** $$Z(S^2) = \theta(1) = \theta(e_1 + e_2) = 1 + \frac{1}{2} = \frac{3}{2}$$.
   - **Mặt xuyến $$T^2$$ ($$g=1$$ lỗ):** $$Z(T^2) = \theta(H) = \theta(e_1 + 2e_2) = 1 + 2\cdot\frac{1}{2} = 2$$ (đúng bằng $$\dim A = 2$$ — một định lý tổng quát của mọi TQFT: hàm phân hoạch trên mặt xuyến luôn đếm số chiều không gian trạng thái!).
   - **Mặt 2 lỗ $$\Sigma_2$$ ($$g=2$$):** $$H^2 = (e_1 + 2e_2)^2 = e_1 + 4e_2 \implies Z(\Sigma_2) = \theta(e_1 + 4e_2) = 1 + 4\cdot\frac{1}{2} = 3$$.
   - **Tổng quát mặt $$g$$ lỗ:** $$Z(\Sigma_g) = 1 + 2^{g-1}$$.
3. **Nhìn ra nguyên lý:** Chỉ từ một phép nhân đại số cực nhỏ, ta thu được một hàm phân hoạch $$Z(\Sigma_g)$$ không hề biết mặt cong to hay nhỏ, méo hay tròn — nó **chỉ phụ thuộc vào số lỗ $$g$$**! Ở chiều 3 (Chern–Simons) và chiều 4 (Donaldson–Witten), Witten nâng đúng tư duy "cắt–dán–lấy vết" này lên để sinh ra các bất biến nút và bất biến đa tạp 4 chiều.

Vai trò đặc biệt của Witten nằm ở khả năng biến những trực giác như vậy thành **các chương trình toán học** có mục tiêu hình học rõ ràng. Các cộng sự và thế hệ nhà toán học sau đó đã chứng minh chặt chẽ được nhiều mảng rất lớn; chính phương pháp tư duy "dịch vật lý thành cấu trúc hình học" ấy có ảnh hưởng lâu dài hơn bất kỳ một bài báo riêng lẻ nào.

**Bài học.** Khi một phép đối ngẫu xuất hiện trước trong vật lý, hãy hỏi: *phát biểu dạng định lý nào sẽ làm cho nó chặt chẽ?* Câu hỏi đó chính là cây cầu.

---

## 2. Các chủ đề (nói về đối tượng, không nói về hào quang)

Để nhìn rõ di sản của Witten mà không sa vào lời khen chung chung, cách tốt nhất là đặt từng chủ đề cạnh **đối tượng toán học** cụ thể mà nó tạo ra hoặc biến đổi:

| Chủ đề | Đối tượng toán học (ý chính) | Bài liên quan trong khóa học |
|--------|-------------------------|------------------|
| TQFT / Chern–Simons | Bất biến của nút và của đa tạp 3 chiều | Giao giữa tô pô và vật lý |
| Đối xứng gương | Mô hình A và mô hình B; hình học đếm | [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) |
| Seiberg–Witten / đối ngẫu | Bất biến của đa tạp 4 chiều; các lý thuyết trường lượng tử đối ngẫu | Gauge / [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/) |
| Cầu nối Langlands hình học | Đối ngẫu S của lý thuyết $$\mathcal N=4$$ SYM → phạm trù trên không gian moduli Hitchin | [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) |
| Trực giác về chỉ số / dị thường | Toán tử Dirac, lớp đặc trưng | [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) |

Một điểm rất đáng chú ý ở bảng trên là sự lặp lại của cùng một nhịp điệu. Chẳng hạn, với **tô pô 4 chiều**: vào thập niên 1980, Simon Donaldson dùng phương trình Yang–Mills phi tuyến rất khó để phân biệt các cấu trúc trơn khác nhau trên cùng một không gian 4 chiều. Đến năm 1994, Nathan Seiberg và Edward Witten dùng đối ngẫu điện–từ trong lý thuyết trường siêu đối xứng để đưa ra một hệ phương trình đơn giản hơn hẳn (phương trình Seiberg–Witten) — vẫn thu được sức mạnh phân biệt tương đương, nhưng việc tính toán trở nên nhẹ nhàng hơn rất nhiều.

Bạn **không** cần thành thạo tất cả các lý thuyết này. Điều quan trọng là nhận ra **khuôn mẫu chung**: phép đối ngẫu hoặc tích phân đường → phạm trù hoặc bất biến hình học → một chương trình chứng minh định lý.

---

## 3. Ví dụ cụ thể: Kapustin–Witten

Trong nhánh đối ngẫu của khóa học, một trong những cây cầu ngoạn mục nhất là công trình năm 2006 của **Anton Kapustin và Edward Witten**. Ở toán học thuần túy, *chương trình Langlands hình học* đặt ra một câu hỏi đầy tham vọng: liệu có một sự tương đương sâu sắc giữa hai thế giới trông chẳng liên quan gì nhau trên cùng một mặt Riemann $$C$$ — một bên là các phân thớ phẳng gắn với nhóm đối ngẫu $$G^\vee$$, bên kia là các bó ($$D$$-module) sống trên không gian moduli các phân thớ chính của nhóm $$G$$?

Kapustin và Witten đề xuất đặt cả hai thế giới đó vào cùng một mái nhà vật lý: xét lý thuyết trường chuẩn siêu đối xứng $$\mathcal N=4$$ Yang–Mills trong không–thời gian 4 chiều (đã được "xoắn" tô pô), rồi thu gọn hai chiều không gian thành một đường cong (mặt Riemann) $$C$$. Khi đó, **đối ngẫu S điện–từ** — phép hoán đổi điện tích và từ tích, đồng thời lật ngược hằng số ghép mạnh $$g$$ thành yếu $$1/g$$ — tự động hoán đổi nhóm chuẩn $$G$$ với nhóm đối ngẫu Langlands $$G^\vee$$. Ở chiều 2 sau khi thu gọn, phép đối ngẫu ấy biến thành **đối xứng gương** giữa hai mô hình trên không gian moduli Hitchin!

**Những điều cần nhớ:**

1. Cặp nhóm đối ngẫu $$G\leftrightarrow G^\vee$$ xuất hiện ở cả hai phía (ví dụ $$SU(n)$$ đi cặp với $$PSU(n)$$, còn $$SO(2n+1)$$ đi cặp với $$Sp(2n)$$).  
2. Phạm trù các brane hoặc bó (sheaf) thay cho khái niệm "trạng thái" mơ hồ, giúp nhà toán học có đối tượng xác định để kiểm tra.  
3. Bài báo là một **cầu nối**, không thay thế được chứng minh thuần túy toán học của Langlands hình học.  
4. Vẫn phải ghi rõ trạng thái: phần lớn chương trình Langlands số học (gắn với lý thuyết số và các trường hữu hạn hay trường số) vẫn còn mở.

---

## 4. Văn hóa của giải Fields và giải Abel

Khi đọc lịch sử toán học hiện đại, ta thường gặp hai giải thưởng lớn có "tính cách" khá khác nhau:

| Đặc điểm | Ví dụ trong khóa học |
|----------|------------------|
| Fields (dưới 40 tuổi, đột phá về một đối tượng cụ thể) | Witten 1990; Ngô Bảo Châu 2010; nhiều nhà toán học ở chương 2 |
| Abel (thành tựu cả đời, xây nền tảng) | Serre 2003; Atiyah–Singer 2004; Langlands 2018 |

Lời tuyên dương Fields dành cho Witten gần với ý "mở ra con đường cao tốc giữa vật lý và hình học" hơn là giải quyết trọn vẹn một bài toán đơn lẻ. Về tinh thần, nó mang dáng dấp của những giải Abel trao cho các công trình kiến tạo cầu nối, chỉ khác ở giới hạn độ tuổi của Huy chương Fields.

---

## 5. Những nhầm lẫn thường gặp

| Khẳng định | Chỉnh lại |
|------------|-----------|
| "Witten đã chứng minh chương trình Langlands." | Không. Ảnh hưởng và từ điển không đồng nghĩa với việc giải quyết toàn bộ Langlands số học. |
| "Lập luận vật lý thay được chứng minh toán học." | Hai tiêu chuẩn khác nhau; một công trình tốt sẽ mở đường để dịch sang định lý. |
| "Lý thuyết dây chính là Langlands hình học." | Hai lĩnh vực liên quan qua đối ngẫu S, nhưng không phải là một. |
| "Chỉ nhà lý thuyết dây mới cần đến đối ngẫu." | Đối ngẫu tổ chức nhiều phần của toán thuần túy (đối xứng gương, Langlands, lý thuyết chỉ số), không phụ thuộc vào việc có tin vào lý thuyết dây hay không. |

---

## Tài liệu

1. Tư liệu của IMU về Huy chương Fields 1990 trao cho Witten.  
2. Kapustin–Witten — https://arxiv.org/abs/hep-th/0604151  
3. Nhánh đối ngẫu, các bài 12–15; Atiyah–Singer; Langlands ở chương 2.  
4. Bài nói định hướng (Frenkel, hội nghị chuyên đề về Witten), chỉ để hiểu bối cảnh.  

## Video tham khảo

- **Xem trước:** [Prof. Edward Witten | Duality, the Langlands Correspondence, and the Influence of Michael Atiyah](https://www.youtube.com/watch?v=fqHGe3acpC0) (INI Seminar Room 1, tiếng Anh). Witten nói về đối ngẫu, tương ứng Langlands và ảnh hưởng của Atiyah. Nên xem trước để thấy phong cách làm việc của ông.
- [Edward Witten, Gauge theory and the analytic approach to geometric Langlands](https://www.youtube.com/watch?v=QOi_yBoE2kA) (Clay Mathematics Institute, tiếng Anh). Bài giảng về lý thuyết gauge và cách tiếp cận giải tích cho Langlands hình học. Xem sau khi đã đọc mục 3.
- [The Universe Speaks in Numbers: Robbert Dijkgraaf and Edward Witten in Conversation](https://www.youtube.com/watch?v=RjthuCDzAnY) (Institute for Advanced Study, tiếng Anh). Cuộc trò chuyện về mối quan hệ giữa toán học và vật lý. Phù hợp để hiểu thêm bối cảnh.
