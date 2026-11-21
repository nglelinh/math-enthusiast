---
layout: post
title: "Bài toán Navier–Stokes"
chapter: '01'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

**Hệ phương trình Navier–Stokes** mô tả chuyển động của chất lỏng nhớt không nén. Đây là nền tảng của cơ học chất lưu trong kỹ thuật, đồng thời là một bài toán Thiên niên kỷ của Viện Clay về sự tồn tại **nghiệm trơn toàn cục** trong không gian ba chiều.

Câu hỏi ở đây **không** phải là "ta có chạy mô phỏng được không?". Kỹ sư dùng các bộ giải Navier–Stokes hằng ngày cho máy bay, dự báo thời tiết, đường ống, sinh học. Câu hỏi của Viện Clay là: mô hình toán học liên tục, tức là hệ phương trình đạo hàm riêng lý tưởng, có được **bảo đảm** luôn trơn với mọi thời gian khi dữ liệu ban đầu trơn (và có năng lượng hữu hạn) hay không, hay là **điểm kỳ dị** (gradient hoặc độ xoáy tăng vô hạn) có thể xuất hiện sau một khoảng thời gian hữu hạn?

Bài này tách rõ **thực hành kỹ thuật**, **nghiệm yếu Leray** và **bài toán chính quy Thiên niên kỷ**, kể ra các kết quả từng phần chính, và nối với các chủ đề nhiều thang đo (mô phỏng số trực tiếp, chảy rối) mà không đánh đồng chi phí tính toán trên lưới với giải thưởng của Viện Clay.

**Nội dung bài:** phương trình → ý nghĩa vật lý → Viện Clay hỏi gì → những gì đã biết → vì sao khó → công trình của Deng về động học → kỹ thuật và bài toán Thiên niên kỷ → hiểu lầm thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết hệ Navier–Stokes **không nén** (vận tốc và áp suất, ràng buộc $$\nabla\cdot u=0$$) và gọi tên các số hạng phi tuyến, nhớt, áp suất.
- Phân biệt **việc dùng hệ Navier–Stokes trong kỹ thuật** với **bài toán chính quy Thiên niên kỷ**.
- Giải thích sự khác nhau giữa nghiệm yếu **Leray** và nghiệm trơn cổ điển (có nghiệm yếu toàn cục không có nghĩa là có tính chính quy và tính duy nhất đầy đủ).
- Phát biểu bài toán mở: tồn tại và duy nhất nghiệm trơn toàn cục trong 3 chiều, hoặc nghiệm bùng nổ (blow-up) sau thời gian hữu hạn từ dữ liệu trơn.
- Kể một số kết quả từng phần: Beale–Kato–Majda; dữ liệu nhỏ và nghiệm mild; chính quy từng phần (Caffarelli–Kohn–Nirenberg); tính chính quy trong 2 chiều.
- Liên hệ với [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): suy ra mô hình liên tục từ lý thuyết động học là vấn đề **khác** với tính chính quy của hệ Navier–Stokes 3 chiều.
- Tránh các lỗi (mục tiêu 6): "máy bay bay được nên Navier–Stokes đã được giải", "mô phỏng thấy bùng nổ là chứng minh".

**Kiến thức cần có.** Giải tích nhiều biến; hiểu phương trình đạo hàm riêng như các định luật cân bằng địa phương. Không cần khóa học nâng cao về phương trình đạo hàm riêng; các định lý chỉ được nêu tên và ý chính.

**Liên hệ với khóa học.** **Mục tiêu 1**; bài [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (nền tảng động học của chất lưu); phần ứng dụng phương trình vi phân trong khóa học.

---

## 1. Hệ phương trình (dạng không nén)

Cho trường vận tốc $$u(x,t)\in\mathbb{R}^3$$ và áp suất $$p(x,t)$$,

$$
\begin{aligned}
\partial_t u + (u\cdot\nabla)u &= \nu \Delta u - \nabla p + f,\\
\nabla\cdot u &= 0,
\end{aligned}
$$

với độ nhớt $$\nu>0$$ và ngoại lực $$f$$ (có thể không có). Trên $$\mathbb{R}^3$$ hoặc trên xuyến $$\mathbb{T}^3$$, dữ liệu ban đầu thường được cho là trơn, có divergence bằng 0 và năng lượng hữu hạn.

**Ý nghĩa từng số hạng:**

- $$\partial_t u$$: gia tốc cục bộ của vận tốc.  
- $$(u\cdot\nabla)u$$: **số hạng đối lưu phi tuyến**; chất lỏng mang động lượng đi theo các đường dòng. Đây là nguồn gốc toán học của nhiều khó khăn.  
- $$\nu\Delta u$$: **khuếch tán nhớt**; độ nhớt làm trơn gradient vận tốc. $$\nu$$ càng lớn thì chất lỏng càng "đặc" (so sánh thô: mật ong và nước).  
- $$-\nabla p$$: gradient áp suất; áp suất điều chỉnh tức thời để giữ ràng buộc không nén.  
- $$\nabla\cdot u=0$$: **không nén**; dòng chảy bảo toàn thể tích (mật độ không đổi trong mô hình đơn giản).  
- $$f$$: lực khối (trọng lực, khuấy trộn, …), thường bằng 0 trong bài toán Clay thuần túy.

Áp suất không phải một trường tự do độc lập như $$u$$: lấy divergence của phương trình động lượng, ta khôi phục được $$p$$ (sai khác một hằng số) qua một phương trình kiểu Poisson. Tính không nén là một ràng buộc; áp suất đóng vai trò nhân tử Lagrange để giữ ràng buộc đó.

**Ý nghĩa vật lý ngắn gọn.** Số Reynolds lớn tương ứng với độ nhớt tương đối nhỏ: quán tính và sự vận chuyển lấn át khuếch tán, dẫn đến chế độ chảy rối với nhiều thang đo. Viện Clay không hỏi "chảy rối trên máy tính trông như thế nào", mà hỏi liệu mô hình liên tục có thể tự sinh ra điểm kỳ dị toán học hay không.

**Năng lượng.** Nhân phương trình động lượng với $$u$$ rồi lấy tích phân (với điều kiện biên hoặc điều kiện tắt dần phù hợp), ta được **bất đẳng thức năng lượng**: động năng $$E(t)=\frac12\int|u|^2\,dx$$ bị chặn bởi dữ liệu ban đầu và công của ngoại lực, trong khi độ nhớt làm tiêu hao một đại lượng kiểu enstrophy. Kiểm soát năng lượng đủ để xây dựng nghiệm yếu, nhưng tự nó **không** đủ để ngăn gradient tập trung trong 3 chiều.

---

## 2. Bài toán Thiên niên kỷ hỏi gì

Đại ý (xem bài của Fefferman cho Viện Clay để có phát biểu và không gian hàm chính xác), trên $$\mathbb{R}^3$$ (hoặc trên xuyến):

Chứng minh một trong hai khẳng định:

- **Chính quy toàn cục:** với dữ liệu trơn, divergence bằng 0, năng lượng hữu hạn (và ngoại lực phù hợp), tồn tại nghiệm trơn duy nhất $$u,p$$ với mọi $$t>0$$, và các chuẩn tự nhiên không bùng nổ sau thời gian hữu hạn; hoặc  
- **Bùng nổ:** tồn tại dữ liệu trơn có năng lượng hữu hạn sao cho nghiệm trơn không kéo dài được qua một thời điểm hữu hạn $$T_*$$, tức là một chuẩn của vận tốc hoặc độ xoáy không bị chặn khi $$t\to T_*^-$$.

Các câu hỏi liên quan: **tính duy nhất** của nghiệm yếu Leray–Hopf; cấu trúc hình học của tập kỳ dị nếu có. Giải thưởng dành cho một định lý về phương trình đạo hàm riêng liên tục, không dành cho một thí nghiệm số "trông như kỳ dị" trên lưới.

**Tình trạng (2026):** **còn mở**. Đây là một trong sáu bài toán Thiên niên kỷ chưa được giải; giả thuyết Poincaré là bài duy nhất đã được giải (Perelman).

"Còn mở" nghĩa là chưa có **định lý về tồn tại và chính quy cho mô hình liên tục**, chứ không phải "chưa ai mô phỏng được nước".

---

## 3. Những gì *đã* biết: thời gian ngắn, 2 chiều, nghiệm yếu

**Tồn tại trong thời gian ngắn.** Với dữ liệu trơn có divergence bằng 0, tồn tại nghiệm trơn duy nhất trên $$[0,T)$$, với $$T$$ phụ thuộc vào độ lớn của dữ liệu (trong không gian Sobolev hoặc Hölder phù hợp). Câu hỏi là: có phải luôn có $$T=\infty$$, hay với một số dữ liệu thì $$T$$ hữu hạn?

**Hai chiều.** Tính chính quy toàn cục trong 2 chiều là kết quả cổ điển. Lý do nằm ở cấu trúc: hiện tượng **kéo giãn xoáy** (vortex stretching) không có hoặc dễ kiểm soát hơn. Độ xoáy $$\omega=\nabla\times u$$ thỏa một phương trình vận chuyển–khuếch tán không có số hạng kéo giãn $$(\omega\cdot\nabla)u$$ như trong 3 chiều. Câu "Navier–Stokes 2 chiều chưa được giải" là sai; cái khó của bài toán Thiên niên kỷ nằm ở **ba chiều**.

**Leray (1934).** Jean Leray xây dựng nghiệm **yếu** toàn cục trong 3 chiều: các trường thỏa phương trình theo nghĩa phân bố, thỏa bất đẳng thức năng lượng và khớp với dữ liệu ban đầu theo một tôpô phù hợp. Như vậy sự tồn tại không phải là câu hỏi bỏ ngỏ. Điều còn mở là: nghiệm yếu có trơn khi dữ liệu trơn không; có duy nhất không; mọi nghiệm yếu có phải nghiệm cổ điển khi dữ liệu đẹp không.

Tóm lại: "đã biết có nghiệm yếu toàn cục; chưa biết bài toán có đặt chỉnh với nghiệm trơn toàn cục hay không".

---

## 4. Vì sao tính chính quy trong 3 chiều khó

Khó khăn chính đến từ **số hạng phi tuyến** cùng hiện tượng **kéo giãn xoáy** trong 3 chiều. Ước lượng năng lượng kiểm soát chuẩn $$L^2$$ của vận tốc, nhưng không tự khép kín được các ước lượng cho đạo hàm bậc cao. Sự truyền năng lượng xuống các thang đo nhỏ (hình ảnh toán học của chảy rối), trong kịch bản xấu nhất của mô hình liên tục, có thể đẩy gradient lên vô hạn trong thời gian hữu hạn.

Hai trực giác trái ngược:

- Độ nhớt *làm trơn*, nên có lẽ không thể có điểm kỳ dị.  
- Số hạng phi tuyến *làm tập trung*, nên với một số dữ liệu, độ nhớt có thể không đủ.

Không trực giác nào là chứng minh. Mô phỏng số về chảy rối rất mạnh, nhưng do rời rạc hóa, độ phân giải chưa đủ hay mô hình đóng, "bùng nổ trên máy tính" không phải là lời giải cho bài toán Clay; và mô phỏng chạy êm cũng không phải định lý chính quy toàn cục.

So sánh với [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/): kiểm tra hữu hạn trường hợp không chứng minh được một phát biểu về vô hạn trường hợp; ở đây, kiểm tra bằng số trên phương trình rời rạc không chứng minh được một phát biểu về mô hình liên tục. **Bằng chứng không phải là chứng minh.**

---

## 5. Tiêu chí chính quy, dữ liệu nhỏ, chính quy từng phần

**Chính quy có điều kiện.** Nếu một số chuẩn nhất định giữ hữu hạn trên $$[0,T]$$ thì nghiệm trơn đến thời điểm $$T$$. Ví dụ nổi tiếng là **Beale–Kato–Majda**: nếu tích phân theo thời gian của $$\|\omega(\cdot,t)\|_{L^\infty}$$ hữu hạn thì nghiệm không bùng nổ trước $$T$$. Có nhiều biến thể (Prodi–Serrin; trường hợp điểm mút của Escauriaza–Seregin–Šverák). Các kết quả này quy bài toán Thiên niên kỷ về: *chứng minh các chuẩn đó không bùng nổ*, hoặc *dựng dữ liệu làm chúng bùng nổ*.

**Dữ liệu nhỏ.** Nếu dữ liệu đủ nhỏ trong một không gian tới hạn phù hợp thì có nghiệm trơn toàn cục. Dữ liệu lớn mới là vấn đề: về nguyên tắc, số hạng phi tuyến có thể dồn năng lượng vào các thang đo nhỏ.

**Chính quy từng phần.** Với các nghiệm yếu phù hợp, **Caffarelli–Kohn–Nirenberg** (dựa trên công trình của Scheffer) chỉ ra rằng tập kỳ dị trong không–thời gian có **chiều Hausdorff parabolic** ≤1: nếu có điểm kỳ dị thì tập đó "nhỏ" theo nghĩa lý thuyết độ đo hình học. Đây là một định lý chính quy sâu sắc, nhưng **không** phải tính chính quy đầy đủ. Các bài toán biên tự do và mặt cực tiểu có tinh thần tương tự: kiểm soát kích thước của tập xấu khi chưa chứng minh được tập đó rỗng.

**Các mốc khác** (chỉ cần biết tên): Ladyzhenskaya, Prodi, Serrin; nghiệm mild của Kato; tích phân lồi và tính không duy nhất cho các nghiệm *yếu hơn* (theo hướng giả thuyết Onsager). Đây là lĩnh vực phát triển nhanh; cần đọc các bài phổ thông một cách thận trọng.

---

## 6. Nền tảng động học, bài toán thứ sáu của Hilbert, và Deng

Có một câu hỏi thứ hai về chất lưu: không chỉ "phương trình liên tục có trơn không?" mà còn "phương trình liên tục có thực sự là giới hạn của hệ hạt không?". Đây là tinh thần của **bài toán thứ sáu của Hilbert** (đi từ cơ học nguyên tử qua cơ học thống kê đến mô hình liên tục).

Chương trình nghiên cứu được Giải Fields ghi nhận của **Yu Deng** (cùng các cộng sự, trong đó có Hani và Ma) xây dựng cầu nối chặt chẽ từ mô hình quả cầu cứng đến phương trình Boltzmann và, trong chế độ phù hợp, đến các phương trình chất lưu. Kết quả này hỗ trợ việc *suy ra* mô hình liên tục với các giả thiết đã nêu, nhưng **không** tự chứng minh tính chính quy của Navier–Stokes 3 chiều theo phát biểu của bài toán Thiên niên kỷ.

Đọc bài [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) để hiểu **vì sao phương trình chất lưu xuất hiện như một giới hạn**. Đọc *bài này* để hiểu **phương trình liên tục đó có luôn trơn hay không**. Việc suy ra phương trình và tính chính quy là hai vấn đề liên quan nhưng không phải cùng một định lý.

Hướng nghiên cứu về tính chính quy của Caffarelli (biên tự do, phương trình đạo hàm riêng phi tuyến), người nhận Giải Abel, là một cầu nối khác: tính chính quy từng phần của Navier–Stokes có cùng tinh thần với lý thuyết độ đo hình học, tức là phân tích để kiểm soát điểm kỳ dị mà không phải lúc nào cũng loại bỏ được chúng.

---

## 7. Tính toán chất lưu trong kỹ thuật không phải bài toán Thiên niên kỷ (mục tiêu 6)

| Thực tiễn | Bài toán Clay |
|-----------|---------------|
| DNS / LES / RANS | Lý thuyết nghiệm trơn toàn cục cho hệ Navier–Stokes không nén lý tưởng |
| Lưới, bước thời gian, mô hình chảy rối | Định lý về tồn tại, duy nhất, chính quy |
| Chi phí tính toán theo số Reynolds khi giải đủ các xoáy | Ước lượng giải tích và khả năng bùng nổ |
| Kiểm chứng bằng thí nghiệm | Chứng minh trong không gian hàm |

Cả hai đều quan tâm đến sự truyền năng lượng qua nhiều thang đo, nhưng chỉ một bên là bài toán Clay. Câu "Navier–Stokes đã được giải vì ANSYS chạy được" là sai (mục tiêu 6); câu "máy bay không nên bay vì bài toán Clay còn mở" vừa sai với lẽ thường vừa sai với mục tiêu 6.

**Mô phỏng số trực tiếp (DNS)** cố gắng giải hệ Navier–Stokes đến tận thang đo nhớt; chi phí tăng rất nhanh theo số Reynolds. **LES và RANS** dùng mô hình cho các thang đo nhỏ. Thành công về kỹ thuật không trả lời câu hỏi của Viện Clay.

---

## 8. Toán học quanh hệ Navier–Stokes

- **Tiêu chí chính quy:** các định lý có điều kiện dạng "nếu có điểm kỳ dị thì …".  
- **Nghiệm yếu:** tồn tại toàn cục với ít tính chính quy, rồi tìm cách nâng tính chính quy.  
- **Dữ liệu nhỏ:** số hạng phi tuyến không phải lúc nào cũng thắng.  
- **Chính quy từng phần:** nếu có điểm kỳ dị thì chúng "hiếm" theo nghĩa độ đo.

Đây là kiểu "toán học quanh một bài toán mở" giống như [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): câu hỏi gốc chưa giải được, nhưng xung quanh có rất nhiều định lý.

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) về cuốn *Six Math Essentials*, Terence Tao đưa ra một ví dụ động lực học nhẹ nhàng hơn: bài toán **hai vật** của Newton giải được chính xác; bài toán **ba vật** đã gây đau đầu, vì quy tắc thì đơn giản nhưng dáng điệu dài hạn lại khó lường, và dự báo trung thực về lâu dài phải chuyển sang xác suất. Navier–Stokes không phải là "bài toán ba vật cho nước". Đó là một chỗ khác mà cả động lực học lẫn giải tích vẫn còn thiếu một định lý chính quy toàn cục. Bài tổng hợp: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/). Xem thêm [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/).

---

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Navier–Stokes chưa được giải nên máy bay không được bay." | Mô hình kỹ thuật cùng thực nghiệm vẫn hoạt động tốt; Viện Clay hỏi về một định lý thuần túy về tồn tại và chính quy. |
| "Ai đó mô phỏng được bùng nổ là bài toán đã xong." | Mô phỏng không phải chứng minh cho phương trình liên tục. |
| "Deng đã giải bài toán Navier–Stokes." | Deng có bước tiến trong việc suy ra phương trình từ lý thuyết động học; tính chính quy 3 chiều vẫn còn mở. |
| "2 chiều và 3 chiều cũng như nhau." | Tính chính quy trong 2 chiều đã biết; 3 chiều mới là trường hợp khó. |
| "Leray đã giải xong vì có nghiệm toàn cục." | Đó là nghiệm yếu; tính chính quy và tính duy nhất đầy đủ vẫn còn mở. |
| "Bài toán Clay là về cách chọn bước lưới tối ưu." | Không; đây là câu hỏi về lý thuyết giải tích của phương trình đạo hàm riêng. |

---

## Bài tập

1. Trong hệ Navier–Stokes, chỉ ra số hạng phi tuyến và số hạng nhớt; viết một câu về vai trò của mỗi số hạng.  
2. Ràng buộc $$\nabla\cdot u=0$$ có ý nghĩa vật lý gì trong mô hình không nén?  
3. So sánh nghiệm yếu Leray với nghiệm trơn cổ điển (về tồn tại, chính quy, duy nhất).  
4. **Mục tiêu 1 (không quá 300 từ):** phát biểu bài toán Clay về Navier–Stokes, giải thích vì sao khó, nêu một kết quả từng phần có tên.  
5. Sau khi đọc bài [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): viết ba câu phân biệt việc *suy ra* hệ Navier–Stokes với *tính chính quy* của nó.  
6. **Mục tiêu 6:** sửa câu trên báo "Nhà toán học mô phỏng chảy rối 3 chiều, sắp nhận giải thưởng Clay".  
7. Nêu hai lý do vì sao tính toán số không chứng minh được sự bùng nổ của mô hình liên tục.  
8. Mở rộng: đọc mô tả bài toán của Fefferman trên trang Viện Clay và ghi lại (ngắn gọn) các không gian hàm ông sử dụng.

---

## Từ các bài giảng: hướng bùng nổ (Tao) và hướng chính quy (Caffarelli)

Video của Numberphile (Crawford), bài giảng của Caffarelli cho Viện Clay và bài giảng Einstein của Tao bổ sung các ý sau:

- **Hướng Caffarelli:** chính quy từng phần (CKN) giới hạn *mức độ xấu* của tập kỳ dị với nghiệm yếu phù hợp; tập "nhỏ" không có nghĩa là tập rỗng.  
- **Hướng Tao:** bùng nổ sau thời gian hữu hạn cho các mô hình *lấy trung bình* hay mô hình đơn giản hóa nhấn mạnh tính **siêu tới hạn**: ước lượng năng lượng không có thang đo phù hợp để khép kín lập luận bootstrap cho dữ liệu trơn lớn. Bùng nổ cho một phương trình đã sửa đổi **không** phải lời giải bài toán Clay cho hệ Navier–Stokes thật.  
- **Hai thế giới cùng tồn tại:** DNS/LES/RANS hoạt động trong thế giới rời rạc; Viện Clay hỏi về định lý cho mô hình liên tục.

**Tình trạng (2026):** câu hỏi chính quy toàn cục hay bùng nổ trong 3 chiều vẫn **còn mở** (bài toán Thiên niên kỷ).

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Đánh giá: `research/video-research/Navier_Stokes/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *Navier-Stokes Equations* (Crawford): [YouTube](https://www.youtube.com/watch?v=ERBVFcutl3M).  
2. **Trực giác** — vcubingx, *The million dollar equation*: [YouTube](https://www.youtube.com/watch?v=Ra7aQlenTb8).  
3. **Nền tảng** — Caffarelli, bài giảng của Viện Clay về Navier–Stokes: [YouTube](https://www.youtube.com/watch?v=ta6Q70y6YVU).  
4. **Nghiên cứu** — Tao, *Can NS Blow Up in Finite Time?*: [YouTube](https://www.youtube.com/watch?v=DgmuGqeRTto).  
5. **Văn bản gốc** — Fefferman, bản PDF: [navierstokes.pdf](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) · [Clay](https://www.claymath.org/millennium/navier-stokes-equation/).

**Sau khi xem:** thành công của tính toán chất lưu không phải định lý Clay. Nghiệm yếu không phải nghiệm trơn. Tình trạng năm 2026: **còn mở**.

---


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/Navier_Stokes/transcripts/` · trạng thái: `research/video-research/Navier_Stokes/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Navier_Stokes_ERBVFcutl3M_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

Danh sách URL: `research/video-research/Navier_Stokes/references.md`.

1. Clay — [NS](https://www.claymath.org/millennium/navier-stokes-equation/) · Fefferman PDF: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf  
2. Robinson — [survey](https://royalsocietypublishing.org/rsta/article/378/2174/20190526/111659/The-Navier-Stokes-regularity-problem).  
3. Wikipedia — [NS existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness).  
4. Numberphile: https://www.youtube.com/watch?v=ERBVFcutl3M  
5. vcubingx: https://www.youtube.com/watch?v=Ra7aQlenTb8  
6. Caffarelli: https://www.youtube.com/watch?v=ta6Q70y6YVU  
7. Tao: https://www.youtube.com/watch?v=DgmuGqeRTto  
7b. Tao trên Big Think (sáu trụ cột; bài toán hai vật và ba vật): https://www.youtube.com/watch?v=OOMx2BHHWtE  
8. [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/). Bộ tư liệu: `research/video-research/Navier_Stokes/`.

---

## Hướng đi tiếp

Có thể chọn làm đề tài cho bài **A3**. Bài thực hành: xem chuỗi truyền năng lượng của Kolmogorov như một *lập luận gần đúng*, không phải chứng minh. Đọc bài Deng để hiểu "từ hạt đến mô hình liên tục", rồi giữ rõ ranh giới giữa kỹ thuật và bài toán Clay.

## Video tham khảo

- **Xem trước:** [Navier-Stokes Equations - Numberphile](https://www.youtube.com/watch?v=ERBVFcutl3M) — Numberphile, tiếng Anh. Giới thiệu hệ phương trình và bài toán giải thưởng một triệu đô la; nên xem trước khi đọc bài.
- [The million dollar equation (Navier-Stokes equations)](https://www.youtube.com/watch?v=Ra7aQlenTb8) — vcubingx, tiếng Anh. Giải thích trực quan từng số hạng của phương trình; nên xem sau khi đã nắm ý chính của bài.
- [Luis Caffarelli, Navier-Stokes existence and smoothness](https://www.youtube.com/watch?v=ta6Q70y6YVU) — Clay Mathematics Institute, tiếng Anh. Xem thêm sau hai video trên, để nghe phát biểu bài toán từ góc nhìn của một chuyên gia về tính chính quy.
