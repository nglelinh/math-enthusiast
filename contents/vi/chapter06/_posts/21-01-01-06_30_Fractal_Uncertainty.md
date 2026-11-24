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

Trong bài trước, ta biết nguyên lý bất định cổ điển cấm một làn sóng và biến đổi Fourier của nó cùng chui vào một **khoảng** nhỏ hẹp. Nhưng điều gì xảy ra nếu ta không nhốt sóng vào một khoảng liền mạch, mà cho nó "lẩn trốn" trên một đám **bụi fractal** — giống tập Cantor bị khoét thủng vô số lỗ hổng ở mọi độ phóng đại, trải rộng ra cả đoạn thẳng nhưng tổng độ dài bằng không? Nếu là một viên bi cổ điển nảy giữa các bức tường cong hỗn loạn, nó hoàn toàn có thể bị giam giữ mãi mãi trên một bụi fractal như vậy mà không bao giờ thoát ra ngoài. Còn một **làn sóng lượng tử** thì sao? Liệu nó có thể co mình ẩn nấp mãi trên đám bụi fractal ấy không?

Câu trả lời là **không** — và định lý giải tích Fourier khẳng định điều đó mang tên **nguyên lý bất định fractal** (fractal uncertainty principle, viết tắt **FUP**). Đây là một câu chuyện toán học đang diễn ra ngay trước mắt chúng ta: phiên bản 1 chiều do Jean Bourgain và Semyon Dyatlov chứng minh năm 2016; rồi gần một thập kỷ sau, nghiên cứu sinh Alex Cohen (MIT) giải được phiên bản nhiều chiều dưới điều kiện hình học **tính xốp theo đường thẳng** (*Annals of Mathematics* 2025; bản arXiv 2023), mở đường cho những đột phá mới trong **hỗn loạn lượng tử (quantum chaos)** — dù giả thuyết lớn nhất của ngành là tính ergodic duy nhất lượng tử (QUE) trong trường hợp tổng quát vẫn còn **mở**. Bài đi kèm [nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/).

---

## Bản đồ kiến thức nền: Giải tích bán cổ điển, hỗn loạn lượng tử và bất định fractal nghiên cứu những gì?

Nếu bạn đã quen với biến đổi Fourier, phương trình sóng và hình ảnh tập Cantor từ toán đại học, hãy ghép ba mảnh ghép sau lại để nhìn trọn vẹn ngành toán học đằng sau FUP:

- **Hỗn loạn lượng tử (quantum chaos) nghiên cứu gì?** Khi một hạt cổ điển chuyển động trên một mặt cong có độ cong âm (như mặt yên ngựa ghép kín — mặt hyperbolic) hay trong bàn bi-a hình sân vận động, quỹ đạo của nó cực kỳ hỗn loạn: hầu hết quỹ đạo đi qua khắp mọi ngóc ngách, nhưng vẫn còn lại một tập "bụi fractal" cực hiếm gồm những quỹ đạo mắc kẹt mãi không bao giờ chạm tới một vùng nào đó. Hỗn loạn lượng tử hỏi: *các hàm sóng riêng năng lượng cao (tương ứng với bước sóng cực ngắn $$h \to 0$$) có "quên" các bẫy fractal cổ điển đó để phân bố đều khắp không gian hay không?*
- **Giải tích bán cổ điển (semiclassical analysis) là cầu nối:** Để nối quỹ đạo cổ điển (vị trí $$x$$ và động lượng $$\xi$$ cùng lúc) với sóng lượng tử, các nhà toán học dùng biến đổi Fourier bán cổ điển với tham số bước sóng nhỏ $$h \ll 1$$:
  $$
  (\mathcal{F}_h f)(\xi) = \frac{1}{(2\pi h)^{d/2}} \int_{\mathbb{R}^d} e^{-i x \cdot \xi / h} f(x)\,dx.
  $$
  Ở thang bước sóng $$h$$, "độ mờ" của một điểm trong không gian pha cỡ $$h$$, nên một tập fractal $$X$$ được thay bằng lân cận dày $$h$$ quanh nó (ký hiệu $$X(h)$$).
- **FUP phát biểu điều gì?** Thay vì hỏi "khoảng nhỏ", FUP hỏi: nếu ta cắt hàm sóng lên lân cận $$X(h)$$ của một tập fractal xốp, biến đổi Fourier bán cổ điển, rồi lại cắt lên lân cận $$Y(h)$$ của một tập fractal xốp khác, thì biên độ sống sót có bị suy giảm theo **một lũy thừa dương $$O(h^\beta)$$** ($$\beta > 0$$) khi $$h \to 0$$ hay không? Nói ngắn gọn: một sóng bước sóng ngắn không thể cùng lúc "tránh hết các lỗ hổng" ở cả miền không gian lẫn miền tần số!

Hiểu sự kết hợp giữa **tính xốp hình học của fractal** và **độ rò rỉ của biến đổi Fourier**, bạn sẽ thấy ngay vì sao một bài toán giải tích điều hòa thuần túy lại trở thành vũ khí sắc bén nhất cho vật lý hỗn loạn lượng tử hiện đại.

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

Bất đẳng thức Pauli–Weyl cổ điển cấm một hàm tập trung đồng thời trên hai khoảng nhỏ, một trong không gian và một trong tần số. Nhưng một tập fractal có thể có **độ đo (độ dài) bằng không** mà vẫn trải rộng khắp đoạn $$[0,1]$$ — khiến phương sai của nó không hề nhỏ! Lấy ví dụ **tập Cantor bỏ một phần ba ở giữa**: sau bước $$n$$, ta chỉ còn $$2^n$$ đoạn nhỏ độ dài $$3^{-n}$$, tổng độ dài là $$(2/3)^n \to 0$$, nhưng bên trong *bất kỳ* khoảng con nào ta phóng to lên, luôn có ít nhất một phần ba bị khoét rỗng. Tính chất "luôn có một khoảng trống tỉ lệ cố định ở mọi thang đo từ $$h$$ đến $$1$$" được gọi là **tính xốp (porosity)**.

![Xây Cantor bỏ phần ba giữa, sáu thế hệ]({{ site.baseurl }}/img/chapter_img/fup_cantor_porosity.png)

*Hình. Ở mọi thang đo, tập thiếu một tỉ lệ cố định của mỗi khoảng còn lại. Đó là tính xốp, chứ không chỉ là "nhỏ".*

**Ý chính của FUP (một chiều).** Nếu bạn cố dựng một hàm có khối lượng tập trung gần một tập kiểu Cantor, thì biến đổi Fourier của nó **không thể** cũng tập trung gần một tập kiểu Cantor. Cộng các sóng có tần số nằm trên một bụi fractal sẽ không thể tạo ra một đường bao khớp sạch vào các khoảng còn lại của fractal: các lỗ hổng tất yếu bị sóng "tràn vào" lấp đầy.

Phát biểu chính xác đo "gần" bằng bán kính lân cận $$h$$ (tham số bán cổ điển), và đo "kiểu Cantor" bằng hằng số xốp $$\nu > 0$$. Khi đó bất đẳng thức khẳng định rằng toán tử chiếu lên $$h$$-lân cận $$X(h)$$ của fractal, kết hợp với biến đổi Fourier bán cổ điển $$\mathcal{F}_h$$ rồi chiếu lên $$Y(h)$$, thỏa mãn ước lượng suy giảm:

$$
\|\mathbf{1}_{X(h)}\,\mathcal{F}_h\,\mathbf{1}_{Y(h)}\|_{L^2 \to L^2} \le C h^\beta
$$

với một số mũ cải thiện $$\beta > 0$$ nào đó (càng nhỏ $$h$$, năng lượng sống sót càng tắt về $$0$$!). Ở mức bài học, chỉ cần nắm ý chính cùng các giả thiết hình học; các ước lượng kỹ thuật nằm trong bài báo.

---

## 2. Vì sao nhà vật lý quan tâm: bụi bị giam giữ

Một hạt cổ điển trong bàn bi-a hỗn loạn thường đi khắp bàn. Nhưng trong những trường hợp cực hiếm, nó có thể nảy đi nảy lại mãi giữa vài chướng ngại vật (giống một tia sáng kẹt giữa ba chiếc gương hình tròn). Nếu đánh dấu tất cả các điểm xuất phát tạo ra quỹ đạo không bao giờ thoát ra ngoài, ta thu được một **bụi fractal** xốp: tập các quỹ đạo bị giam giữ.

Hạt lượng tử là sóng, và sóng thì nhiễu xạ, rò rỉ qua khe hở. Câu hỏi Semyon Dyatlov đặt ra là liệu sự rò rỉ đó có bị hình học Fourier ép buộc bằng một định lý chặt chẽ hay không: nếu tập bị giam giữ là fractal xốp, hàm sóng có thể tập trung trên nó cả về vị trí lẫn tần số không? FUP trả lời dứt khoát là **không**. Do đó, trên một mặt hyperbolic compact, một hàm sóng riêng năng lượng cao **không bao giờ có thể né tránh hoàn toàn một miền mở** (dù nhỏ đến đâu): bởi nếu xóa bỏ mọi quỹ đạo cổ điển đi vào miền mở đó, phần còn lại chỉ là một bụi fractal xốp, và FUP cấm sóng co cụm lên phần còn lại ấy! Đây chính là khung lập luận nổi tiếng của **Dyatlov–Jin** (2017) trong hai chiều.

Bức tranh này cũng cho thấy FUP không chỉ là một sự tò mò về tập Cantor. Nó là cỗ máy biến **tập bị giam giữ cổ điển** thành **tính không định xứ lượng tử**.

---

## 3. Một chiều: Bourgain–Dyatlov

Jean Bourgain và Semyon Dyatlov chứng minh nguyên lý bất định fractal trên đường thẳng (2016), bằng một phương pháp khác thường ngay cả trong giải tích điều hòa. Đại ý:

1. Tách từng đỉnh của một hàm kiểu fractal bằng cách nhân với một **hàm làm tắt** (damping function) gần bằng 1 trên đỉnh đó và gần bằng 0 trên các đỉnh khác.
2. Mỗi đỉnh tách ra có biến đổi Fourier **trải rộng**.
3. Các phần trải rộng này không thể "cùng nhau" triệt tiêu trên một tập xốp đủ thường xuyên để $$\hat f$$ trông giống fractal.

Bước khó nhất của toàn chứng minh là dựng hàm làm tắt. Nó có họ hàng trực tiếp với định lý nhân tử **Beurling–Malliavin** lừng danh từ thập niên 1960: cần dựng một hàm giải tích có biên độ và tốc độ giảm Fourier cực kỳ khắt khe, phải đi đường vòng tinh vi qua giải tích phức (hàm nguyên loại mũ). Bourgain qua đời năm 2018; nhưng các ghi chú chưa công bố ông để lại sau đó đã truyền cảm hứng trực tiếp giúp mở khóa trường hợp nhiều chiều.

**Trạng thái.** FUP một chiều là định lý. Nó đã dẫn đến các kết quả về khe phổ cốt yếu trong một số bối cảnh tán xạ hyperbolic, và kết quả không định xứ của Dyatlov–Jin cho các mặt cong âm.

---

## 4. Nhiều chiều: đường thẳng phá vỡ phát biểu ngây thơ

Khi bước từ đường thẳng $$\mathbb{R}$$ lên mặt phẳng $$\mathbb{R}^2$$, một cái bẫy hình học bất ngờ lập tức xuất hiện! Xét một đường thẳng đứng $$X = \{(0, y) : y \in \mathbb{R}\}$$. Xét về diện tích 2 chiều, đường thẳng này có diện tích bằng không và trông "đầy lỗ" ở mọi quả cầu 2 chiều! Thế nhưng biến đổi Fourier của một hàm chỉ sống trên đường thẳng đứng $$x = 0$$ lại tập trung hoàn toàn trên **đường thẳng ngang** $$\xi_2 = 0$$ (vì hàm hằng theo $$y$$ có tần số $$\xi_2 = 0$$, còn xung hẹp theo $$x$$ trải rộng theo $$\xi_1$$). Như vậy, **một đường thẳng và đường thẳng vuông góc với nó đều "xốp theo quả cầu"**, nhưng chuẩn toán tử của chúng không hề suy giảm — chúng là phản ví dụ phá vỡ ngay mọi khẩu hiệu cẩu thả kiểu "không thể có hai fractal"!

Tam giác Sierpiński và nhiều thảm Sierpiński quen thuộc chứa trọn các đoạn thẳng dài (như cạnh đáy). Những tập đó trông rất thưa thớt trong mặt phẳng nhưng vẫn làm FUP ngây thơ thất bại, chính vì hiệu ứng đường thẳng này.

![Gasket Sierpiński với cạnh đáy tô như một đường đầy đủ]({{ site.baseurl }}/img/chapter_img/fup_sierpinski_line_obstruction.png)

*Hình. Một tập có thể trông đầy lỗ nhưng vẫn chứa một đường thẳng. Biến đổi Fourier đưa đường thẳng đó sang một đường thẳng khác. Vì vậy FUP ngây thơ không thể đúng cho mọi fractal ở chiều $$\ge 2$$.*

Cách Alex Cohen vượt qua là **loại trừ chính xác họ phản ví dụ đường thẳng này bằng một giả thiết hình học sắc bén**, chứ không bỏ qua chúng.

---

## 5. Tính xốp theo đường thẳng và định lý Cohen

**Tính xốp theo đường thẳng (line porosity — ý chính).** Thay vì chỉ đòi hỏi mỗi hình tròn chứa một lỗ trống, hãy vẽ **một đường thẳng bất kỳ** theo mọi phương cắt qua tập fractal. Tập được gọi là *xốp theo đường thẳng* nếu trên mọi đường thẳng thử ấy, ở mọi thang đo, ta đều liên tục bắt gặp những đoạn trống có tỉ lệ kích thước cố định. Điều kiện này lập tức cấm tập chứa trọn bất kỳ đường thẳng hay đoạn thẳng dài nào! Một thảm Sierpiński nếu bị đục bỏ thêm một số ô để phá vỡ mọi đường thẳng xuyên suốt thì có thể thỏa mãn tính xốp theo đường thẳng; còn thảm thông thường thì không nhất thiết.

![Trái: đường nằm trong tập. Phải: mọi đường thử đều bị khuyết]({{ site.baseurl }}/img/chapter_img/fup_line_porosity.png)

*Hình. Giả thiết hình học bổ sung làm cho FUP nhiều chiều trở nên khả thi. (Đây là sơ đồ; định nghĩa trong bài báo mang tính định lượng.)*

**Định lý (Cohen, arXiv:2305.05022; *Annals of Mathematics* **202** (2025)).** Một tập fractal trong $$\mathbb{R}^d$$ thỏa tính xốp theo đường thẳng thì tuân theo một nguyên lý bất định fractal (với chuẩn suy giảm $$O(h^\beta)$$). Nguyên liệu đột phá chính là **định lý nhân tử Beurling–Malliavin nhiều chiều**: hàm làm tắt được dựng lại cho hàm nhiều biến — điều từng bị nhiều chuyên gia bi quan cho là bất khả thi tại hội thảo IAS năm 2016!

Đây là một định lý đã công bố chính thức, không phải tin đồn hay thông báo sơ bộ. Bài viết trên Quanta kể lại lịch sử thú vị của chứng minh (từ ghi chú của Bourgain đến luận án của Cohen). Trong khóa học, ta chỉ cần nắm phát biểu và giả thiết hình học, không cần dựng lại hàm nhân tử.

---

## 6. Những gì đã mở ra, và những gì còn mở

Khi đã có FUP nhiều chiều, các lập luận không định xứ vốn chỉ chạy được trên mặt 2 chiều lập tức được đẩy lên không gian nhiều chiều hơn. Năm 2025, Elena Kim và Nicholas Miller dùng định lý Cohen để mở rộng kết quả "sóng không thể ẩn" sang không gian hyperbolic nhiều chiều (với giả thiết hình học bảo đảm tập bị giam giữ xốp theo đường thẳng). Peter Sarnak gọi đây là một trong những ứng dụng ấn tượng nhất của FUP cho đến nay.

Mục tiêu mạnh hơn nữa là **tính ergodic duy nhất lượng tử** (quantum unique ergodicity, **QUE**): các hàm riêng năng lượng cao của hệ hỗn loạn không chỉ buộc phải *chạm tới* mọi miền mở (không định xứ), mà còn phải **phân bố đều tuyệt đối** — nhìn gần thì sóng gợn hỗn loạn, nhìn xa thì mật độ năng lượng đều tăm tắp như một mảng màu phẳng, giống tranh ấn tượng của Monet. Rudnick và Sarnak (1994) phỏng đoán QUE cho mọi đa tạp compact có độ cong âm. Trường hợp số học (các hàm riêng Hecke trên mặt số học) đã được Elon Lindenstrauss chứng minh năm 2006 (mang về Huy chương Fields 2010; Kannan Soundararajan hoàn tất trường hợp mặt modular không compact năm 2010). Nhưng trường hợp hình học tổng quát vẫn là **một giả thuyết lớn còn mở**. FUP là một nguyên liệu quý giá người ta hy vọng sẽ tiến gần hơn tới lời giải, chứ chưa phải lời giải trọn vẹn.

**Bài liên quan trong khóa học.** Cách nghĩ hình học (hình ống, tính xốp, cấm tập trung quá nhiều trên đường thẳng) có họ hàng gần với bài toán Kakeya và bài toán hạn chế (restriction) trong [giải tích điều hòa của Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/). FUP không phải bài toán Kakeya, và ngược lại. Chúng chung một trực giác cốt lõi: **sự tập trung của biến đổi Fourier thực chất là một bài toán hình học**.

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
