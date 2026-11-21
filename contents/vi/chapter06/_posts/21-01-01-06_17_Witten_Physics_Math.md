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

**Edward Witten** (Viện Nghiên cứu Cao cấp Princeton, IAS) nhận **Huy chương Fields năm 1990**. Đây là một trong số rất ít lần một công trình xuất phát từ vật lý lý thuyết được cộng đồng toán học thuần túy vinh danh, vì nó đã làm thay đổi cách nhìn về hình học. Trong **nhánh đối ngẫu** của khóa học này, Witten đại diện cho một phương pháp làm việc: xem xét nghiêm túc các phép đối ngẫu và trực giác từ lý thuyết trường lượng tử, viết lại chúng bằng ngôn ngữ hình học và tô pô, và từ đó đặt ra những bài toán có cấu trúc rõ ràng mà nhà toán học có thể chứng minh.

Đây là một **chân dung ngắn**, không phải tiểu sử và cũng không phải giáo trình lý thuyết trường lượng tử.

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

Hình học thế kỷ XX đã có nhiều trao đổi với vật lý (Einstein, lý thuyết gauge, lý thuyết chỉ số). Từ thập niên 1980, **lý thuyết trường lượng tử và lý thuyết dây** sinh ra hàng loạt *từ điển dạng giả thuyết* rất cụ thể: hàm tương quan ứng với số giao, đối ngẫu ứng với tương đương phạm trù, dị thường ứng với chỉ số tô pô.

Vai trò đặc biệt của Witten, được ghi nhận qua Huy chương Fields 1990, là biến nhiều trực giác như vậy thành **các chương trình toán học** với mục tiêu hình học rõ ràng. Các cộng sự và thế hệ sau đã chứng minh được nhiều phần lớn; phương pháp này có ảnh hưởng lâu dài hơn bất kỳ bài báo riêng lẻ nào.

**Bài học.** Khi một phép đối ngẫu xuất hiện trước trong vật lý, hãy hỏi: *phát biểu dạng định lý nào sẽ làm cho nó chặt chẽ?* Câu hỏi đó chính là cây cầu.

---

## 2. Các chủ đề (nói về đối tượng, không nói về hào quang)

| Chủ đề | Đối tượng toán học (ý chính) | Bài liên quan trong khóa học |
|--------|-------------------------|------------------|
| TQFT / Chern–Simons | Bất biến của nút và của đa tạp 3 chiều | Giao giữa tô pô và vật lý |
| Đối xứng gương | Mô hình A và mô hình B; hình học đếm | [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) |
| Seiberg–Witten / đối ngẫu | Bất biến của đa tạp 4 chiều; các lý thuyết trường lượng tử đối ngẫu | Gauge / [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/) |
| Cầu nối Langlands hình học | Đối ngẫu S của lý thuyết $$\mathcal N=4$$ SYM → phạm trù trên không gian moduli Hitchin | [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) |
| Trực giác về chỉ số / dị thường | Toán tử Dirac, lớp đặc trưng | [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) |

Bạn **không** cần thành thạo các lý thuyết này. Bạn cần nhận ra **khuôn mẫu chung**: phép đối ngẫu hoặc tích phân đường → phạm trù hoặc bất biến hình học → một chương trình chứng minh định lý.

---

## 3. Ví dụ cụ thể: Kapustin–Witten

Trong bài đọc sâu về Langlands hình học, **Kapustin và Witten** lập luận rằng đối ngẫu S điện–từ của lý thuyết $$\mathcal N=4$$ SYM 4 chiều (sau khi xoắn, twist), khi compact hóa trên một đường cong, cho ta cấu trúc của tương ứng Langlands hình học, với đối xứng gương của hệ Hitchin là cơ chế chính.

**Những điều cần nhớ:**

1. Cặp nhóm đối ngẫu $$G\leftrightarrow G^\vee$$ xuất hiện ở cả hai phía.  
2. Phạm trù các brane hoặc bó (sheaf) thay cho khái niệm "trạng thái" mơ hồ.  
3. Bài báo là một **cầu nối**, không thay thế được chứng minh thuần túy toán học của Langlands hình học.  
4. Vẫn phải ghi rõ trạng thái: phần lớn chương trình Langlands số học vẫn còn mở.

---

## 4. Văn hóa của giải Fields và giải Abel

| Đặc điểm | Ví dụ trong khóa học |
|----------|------------------|
| Fields (dưới 40 tuổi, đột phá về một đối tượng cụ thể) | Witten 1990; Ngô Bảo Châu 2010; nhiều nhà toán học ở chương 2 |
| Abel (thành tựu cả đời, xây nền tảng) | Serre 2003; Atiyah–Singer 2004; Langlands 2018 |

Lời tuyên dương Fields dành cho Witten gần với ý "mở ra con đường cao tốc giữa vật lý và hình học" hơn là giải một bài toán cụ thể. Về tinh thần, nó giống những giải Abel trao cho các công trình cầu nối, chỉ khác ở giới hạn độ tuổi.

---

## 5. Những nhầm lẫn thường gặp

| Khẳng định | Chỉnh lại |
|------------|-----------|
| "Witten đã chứng minh chương trình Langlands." | Không. Ảnh hưởng và từ điển không đồng nghĩa với việc giải quyết toàn bộ Langlands số học. |
| "Lập luận vật lý thay được chứng minh toán học." | Hai tiêu chuẩn khác nhau; một công trình tốt sẽ mở đường để dịch sang định lý. |
| "Lý thuyết dây chính là Langlands hình học." | Hai lĩnh vực liên quan qua đối ngẫu S, nhưng không phải là một. |
| "Chỉ nhà lý thuyết dây mới cần đến đối ngẫu." | Đối ngẫu tổ chức nhiều phần của toán thuần túy (đối xứng gương, Langlands, lý thuyết chỉ số), không phụ thuộc vào việc có tin vào lý thuyết dây hay không. |

---

## Bài tập

1. Nêu ba *đối tượng* toán học gắn với các chương trình chịu ảnh hưởng của Witten (ba đối tượng, không phải ba tính từ).  
2. **Không quá 120 chữ:** vật lý như nguồn cảm hứng so với vật lý như chứng minh, lấy Kapustin–Witten làm ví dụ.  
3. So sánh Fields 1990 của Witten với Abel 2004 của Atiyah–Singer: một điểm giống và một điểm khác về văn hóa trao giải.  
4. Thêm một dòng liên quan đến Witten vào [bài thực hành từ điển đối ngẫu]({{ site.baseurl }}/contents/vi/chapter07/07_10_Explore_Duality_Dictionary/), ghi trạng thái trung thực.

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
