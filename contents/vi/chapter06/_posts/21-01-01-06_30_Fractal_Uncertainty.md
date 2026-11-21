---
layout: post
title: "Nguyên lý bất định fractal"
chapter: '06'
order: 30
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Nguyên lý bất định cổ điển nói rằng một hàm và biến đổi Fourier của nó không thể cùng tập trung gần một **khoảng** nhỏ. Thay khoảng bằng một **fractal**, tức một tập có lỗ ở mọi thang đo, ta được một điều cấm mạnh hơn: chúng cũng không thể cùng tập trung gần một "bụi" fractal. Phiên bản mạnh hơn này là **nguyên lý bất định fractal** (fractal uncertainty principle, viết tắt FUP). Đó là một định lý của giải tích Fourier, và là công cụ trong hỗn loạn lượng tử: sóng không thể ẩn mãi trên một "bẫy" fractal, trong khi hạt bi-a cổ điển thì có thể ở đó mãi.

Đây là bài về hướng nghiên cứu mới, đi kèm [bài nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/). FUP một chiều do Bourgain–Dyatlov chứng minh (2016). Phát biểu cho nhiều chiều, với một giả thiết hình học bổ sung gọi là **tính xốp theo đường thẳng** (line porosity), thuộc về Alex Cohen (*Annals of Mathematics* 2025; bản arXiv 2023). Giả thuyết tính ergodic duy nhất lượng tử (QUE) trong trường hợp tổng quát vẫn còn **mở**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu **ý chính** của FUP: $$f$$ và $$\hat f$$ không thể cùng tập trung gần một tập fractal xốp.
- Giải thích **tính xốp** qua tập Cantor bỏ một phần ba ở giữa, và vì sao đó là ràng buộc tập trung mạnh hơn "khoảng nhỏ".
- Mô tả **vật cản đường thẳng** ở chiều $$\ge 2$$ (một tập chứa cả một đường thẳng có thể "đầy lỗ" nhưng vẫn làm FUP thất bại).
- Định nghĩa **tính xốp theo đường thẳng** ở mức ý chính, và biết định lý Cohen là FUP dưới giả thiết đó.
- Phân biệt **định lý** (FUP; kết quả không định xứ của Dyatlov–Jin trên mặt hyperbolic) với **giả thuyết** (QUE của Rudnick–Sarnak).
- Tránh nói "mọi fractal ở mọi số chiều đều tuân theo FUP".

**Kiến thức nền.** [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/); tập Cantor trong bài [fractal]({{ site.baseurl }}/contents/vi/chapter04/04_03_Fractals/); biến đổi Fourier như ở Chương 3. Hình học hyperbolic chỉ cần ở mức hình dung.

---

## 1. Từ khoảng đến lỗ ở mọi thang đo

Bất đẳng thức Pauli–Weyl cổ điển cấm một hàm tập trung đồng thời trên hai khoảng nhỏ, một trong không gian và một trong tần số. Một fractal có thể có **độ đo bằng không** mà vẫn "lớn" theo nghĩa số chiều: tập Cantor bỏ một phần ba ở giữa là không đếm được, có độ dài bằng không, và bị khoét lỗ ở mọi thế hệ.

![Xây Cantor bỏ phần ba giữa, sáu thế hệ]({{ site.baseurl }}/img/chapter_img/fup_cantor_porosity.png)

*Hình. Ở mọi thang đo, tập thiếu một tỉ lệ cố định của mỗi khoảng còn lại. Đó là tính xốp, chứ không chỉ là "nhỏ".*

**Ý chính của FUP (một chiều).** Nếu bạn cố dựng một hàm có khối lượng tập trung gần một tập kiểu Cantor, thì biến đổi Fourier của nó **không thể** cũng tập trung gần một tập kiểu Cantor. Cộng các sóng có tần số nằm trên một bụi fractal sẽ không cho ra một đường bao trông như fractal: các lỗ bị lấp đầy.

Phát biểu chính xác đo "gần" bằng bán kính lân cận $$h$$ (tham số bán cổ điển), và đo "kiểu Cantor" bằng số chiều và hằng số xốp. Khi đó bất đẳng thức nói rằng toán tử chiếu lên $$h$$-lân cận của fractal, kết hợp với biến đổi Fourier (hoặc biến đổi bán cổ điển), có chuẩn toán tử $$O(h^\beta)$$ với một $$\beta>0$$ nào đó. Ở mức bài học, chỉ cần nắm ý chính cùng các giả thiết hình học; các ước lượng nằm trong bài báo.

---

## 2. Vì sao nhà vật lý quan tâm: bụi bị giam giữ

Một hạt cổ điển trong bàn bi-a hỗn loạn thường đi khắp bàn. Trong những trường hợp hiếm, nó có thể nảy mãi giữa vài chướng ngại vật. Nếu đánh dấu các điểm va chạm trên thành bàn trong thời gian vô hạn, ta thường thấy một **bụi fractal**: tập các quỹ đạo bị giam giữ, không bao giờ thoát ra.

Hạt lượng tử là sóng, và sóng thì rò rỉ. Câu hỏi Dyatlov đặt ra là liệu sự rò rỉ đó có bị hình học Fourier ép buộc hay không: nếu tập bị giam là fractal, hàm sóng có thể tập trung trên nó cả về vị trí lẫn tần số không? FUP trả lời là không. Do đó sóng trên một mặt hyperbolic compact không thể né mãi một miền mở: nếu xóa mọi quỹ đạo đi vào miền đó, phần còn lại là một bụi fractal, và sóng không được phép tập trung trên đó. Đây là khung lập luận của **Dyatlov–Jin** (2017) trong hai chiều.

Bức tranh này cũng cho thấy FUP không chỉ là một sự tò mò về tập Cantor. Nó là công cụ biến **tập bị giam giữ cổ điển** thành **tính không định xứ lượng tử**.

---

## 3. Một chiều: Bourgain–Dyatlov

Jean Bourgain và Semyon Dyatlov chứng minh nguyên lý bất định fractal trên đường thẳng (2016), bằng một phương pháp khác thường ngay cả trong giải tích điều hòa. Đại ý:

1. Tách từng đỉnh của một hàm kiểu fractal bằng cách nhân với một **hàm làm tắt** (damping function) gần bằng 1 trên đỉnh đó và gần bằng 0 trên các đỉnh khác.
2. Mỗi đỉnh tách ra có biến đổi Fourier **trải rộng**.
3. Các phần trải rộng này không thể "cùng nhau" triệt tiêu trên một tập xốp đủ thường xuyên để $$\hat f$$ trông giống fractal.

Bước khó là dựng hàm làm tắt. Nó có họ hàng với định lý nhân tử **Beurling–Malliavin** từ những năm 1960: cần một hàm có kích thước và tốc độ giảm Fourier rất đặc biệt, được dựng bằng đường vòng qua giải tích phức. Bourgain mất năm 2018; các ghi chú chưa công bố của ông sau này đã giúp mở khóa trường hợp nhiều chiều.

**Trạng thái.** FUP một chiều là định lý. Nó đã dẫn đến các kết quả về khe phổ cốt yếu trong một số bối cảnh hyperbolic, và kết quả không định xứ của Dyatlov–Jin cho các mặt.

---

## 4. Nhiều chiều: đường thẳng phá vỡ phát biểu ngây thơ

Trong mặt phẳng, một đường thẳng có diện tích bằng không và "đầy lỗ" nếu chỉ nhìn vào diện tích. Biến đổi Fourier của nó (xem như một độ đo, hoặc xét một lân cận hình ống) tập trung trên đường thẳng vuông góc. Vậy **một đường thẳng và đường thẳng đối ngẫu của nó đều "xốp" theo nghĩa ngây thơ**, và chúng là phản ví dụ cho mọi khẩu hiệu cẩu thả kiểu "không thể có hai fractal".

Tam giác Sierpiński và nhiều thảm Sierpiński chứa các đoạn thẳng. Những tập đó có thể rất xốp trong mặt phẳng nhưng vẫn làm FUP thất bại, chính vì lý do này.

![Gasket Sierpiński với cạnh đáy tô như một đường đầy đủ]({{ site.baseurl }}/img/chapter_img/fup_sierpinski_line_obstruction.png)

*Hình. Một tập có thể trông đầy lỗ nhưng vẫn chứa một đường thẳng. Biến đổi Fourier đưa đường thẳng đó sang một đường thẳng khác. Vì vậy FUP ngây thơ không thể đúng cho mọi fractal ở chiều $$\ge 2$$.*

Cách Cohen vượt qua là **loại các phản ví dụ này bằng một giả thiết**, chứ không bỏ qua chúng.

---

## 5. Tính xốp theo đường thẳng và định lý Cohen

**Tính xốp theo đường thẳng (ý chính).** Vẽ một đường thẳng bất kỳ. Đường đó phải gặp tập một cách xốp: khi đi dọc theo đường, ta liên tục gặp những lỗ có kích thước xác định, ở mọi thang đo, với các hằng số định lượng. Tập không được chứa trọn một đường thẳng. Một thảm Sierpiński bị xóa thêm một số ô có thể thỏa điều kiện này; thảm thông thường thì không nhất thiết.

![Trái: đường nằm trong tập. Phải: mọi đường thử đều bị khuyết]({{ site.baseurl }}/img/chapter_img/fup_line_porosity.png)

*Hình. Giả thiết hình học bổ sung làm cho FUP nhiều chiều trở nên khả thi. (Đây là sơ đồ; định nghĩa trong bài báo mang tính định lượng.)*

**Định lý (Cohen, arXiv:2305.05022; *Annals of Mathematics* **202** (2025)).** Một tập fractal trong $$\mathbb{R}^d$$ thỏa tính xốp theo đường thẳng thì tuân theo một nguyên lý bất định fractal. Nguyên liệu mới chính là **định lý nhân tử Beurling–Malliavin nhiều chiều**: hàm làm tắt được dựng lại cho nhiều biến.

Đây là một định lý đã công bố, không phải một thông báo. Bài viết trên Quanta tháng 8/2026 kể lại lịch sử chứng minh (ghi chú của Bourgain, sự bi quan tại hội thảo IAS năm 2016, luận án của Cohen). Trong khóa học, ta chỉ cần nắm phát biểu và giả thiết, không cần dựng lại hàm nhân tử.

---

## 6. Những gì đã mở ra, và những gì còn mở

Khi đã có FUP nhiều chiều, các lập luận không định xứ vốn dùng cho mặt có thể được thử ở số chiều cao hơn. Năm 2025, Elena Kim và Nicholas Miller dùng định lý Cohen để mở rộng kết quả "sóng không thể ẩn" sang không gian hyperbolic nhiều chiều (với giả thiết hình học bảo đảm tập bị giam giữ xốp theo đường thẳng). Peter Sarnak gọi đây là một trong những ứng dụng ấn tượng nhất cho đến nay.

Mục tiêu mạnh hơn là **tính ergodic duy nhất lượng tử** (quantum unique ergodicity, QUE): các hàm riêng của hệ hỗn loạn không chỉ chạm tới mọi miền, mà còn phải **phân bố đều**. Nhìn gần thì chúng lộn xộn, nhìn xa thì đều như một mảng màu phẳng, giống tranh Monet. Rudnick–Sarnak (1994) phỏng đoán QUE cho mọi đa tạp compact có độ cong âm. Trường hợp số học (các hàm riêng Hecke) đã được Lindenstrauss chứng minh (2006; Soundararajan hoàn tất cho mặt modular năm 2010). Trường hợp tổng quát vẫn là **một giả thuyết lớn còn mở**. FUP là một nguyên liệu người ta hy vọng sẽ dùng được, không phải lời giải.

**Bài liên quan trong khóa học.** Cách nghĩ hình học (hình ống, tính xốp, cấm tập trung quá nhiều trên đường thẳng) có họ hàng với bài toán Kakeya và bài toán hạn chế (restriction) trong [giải tích điều hòa của Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/). FUP không phải bài toán Kakeya, và ngược lại. Chúng chung một trực giác: **sự tập trung của biến đổi Fourier là một bài toán hình học**.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Chỉnh lại |
|------------|------|-----|
| "FUP nói không hàm nào có thể có dạng fractal." | Sai | Nó ràng buộc một hàm **và** biến đổi Fourier của nó cùng một lúc. |
| "Mọi fractal ở mọi số chiều đều tuân theo FUP." | Sai | Đường thẳng (và các tập chứa đường thẳng) là phản ví dụ nếu thiếu tính xốp theo đường thẳng. |
| "Cohen đã giải quyết hỗn loạn lượng tử." | Phóng đại | Ông chứng minh một định lý Fourier được dùng trong một số lập luận về hỗn loạn lượng tử. QUE tổng quát vẫn còn mở. |
| "Hạt cổ điển và sóng lượng tử bị giam trên cùng một tập." | Sai | Sự khác biệt đó chính là điểm mấu chốt khi áp dụng FUP. |
| "Quanta đã chứng minh định lý." | Sai | Bài báo của Cohen trên *Annals* mới là chứng minh. Báo chí chỉ là bản đồ. |

---

## Bài tập

1. **Vẽ tập Cantor.** Vẽ các thế hệ $$n=0,1,2$$ của tập Cantor bỏ một phần ba ở giữa. Viết một câu: vì sao "độ dài bằng không" khác với "không có chỗ cho hàm ẩn"?
2. **Vật cản đường thẳng.** Giải thích bằng lời: vì sao một đường thẳng đứng trong mặt phẳng, cùng với đối ngẫu Fourier của nó, phá vỡ FUP nhiều chiều phát biểu ngây thơ?
3. **Hiểu giả thiết.** Cho một ví dụ (định tính) về một tập phẳng trông đầy lỗ nhưng không xốp theo đường thẳng, và một cách sửa có thể khôi phục tính chất đó.
4. **Bảng trạng thái.** Lập bảng bốn hàng, ghi định lý hay còn mở: FUP một chiều; FUP nhiều chiều của Cohen; tính không định xứ của Dyatlov–Jin trên mặt hyperbolic; QUE của Rudnick–Sarnak.
5. **Đoạn nối.** Viết một đoạn nối tính xốp ở đây với tập Cantor trong bài [fractal]({{ site.baseurl }}/contents/vi/chapter04/04_03_Fractals/), mà không khẳng định FUP chỉ là một phát biểu về chiều Hausdorff.

---

## Tài liệu tham khảo

- Alex Cohen — [Fractal uncertainty in higher dimensions](https://arxiv.org/abs/2305.05022), *Annals of Mathematics* **202** (2025).
- Bourgain–Dyatlov — [Spectral gaps without the pressure condition](https://arxiv.org/abs/1612.09040) (FUP 1D như dụng cụ).
- Shalma Wegsman — [Graduate Student Proves a Quantum Uncertainty Principle for Fractals](https://www.quantamagazine.org/graduate-student-proves-the-fractal-uncertainty-principle-20260812/), *Quanta*, 12/08/2026 (truy cập 2026-08-19).
- [Literacy bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/); [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/); [fractal]({{ site.baseurl }}/contents/vi/chapter04/04_03_Fractals/); [chaos]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/).
- Gói: `research/video-research/uncertainty-principles/`.
