---
layout: post
title: "Động lực chỉnh hình và hình học Teichmüller của McMullen (Huy chương Fields 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Ai từng phóng to biên của **tập Mandelbrot** đều khó quên cảm giác choáng ngợp: ẩn sâu trong những sợi ren fractal vô tận lại hiện ra vô số bản sao tí hon của chính tập Mandelbrot ban đầu! Thoạt nhìn, thế giới của phép lặp hàm phức $$z \mapsto z^2 + c$$ trên mặt phẳng và thế giới của **hình học không gian ba chiều cong âm** (những đa tạp hyperbolic 3D trong chương trình hình học hóa của William Thurston) chẳng có chút liên hệ nào. Ấy vậy mà vào thập niên 1980–1990, từ điển Sullivan cùng những công trình sắc sảo của **Curtis T. McMullen** đã hé lộ một sự thật kỳ diệu: hai thế giới đó được vận hành bởi *cùng một động cơ* — **tái chuẩn hóa** và **tính cứng của hệ động lực bảo giác**.

Tại ICM Berlin năm 1998, **Curtis T. McMullen** nhận **Huy chương Fields** với lời trao giải chính thức:

> For his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.

*Tạm dịch: vì những đóng góp cho lý thuyết động lực học chỉnh hình và hình học hóa đa tạp ba chiều, trong đó có chứng minh giả thuyết Bers về tính trù mật của các điểm cusp trên biên không gian Teichmüller, và giả thuyết hàm theta của Kra.*

Bài học này sẽ dẫn bạn đi từ những bức tranh tập Julia quen thuộc đến **không gian Teichmüller**, **biên Bers**, toán tử chuỗi Poincaré của **Kra**, và cầu nối sang **đa tạp hyperbolic ba chiều phân thớ trên đường tròn**. Cũng cần phân định rõ ngay từ đầu: McMullen đóng góp những công cụ sâu sắc *bên trong* chương trình hình học hóa của Thurston, chứ **không** phải người hoàn tất toàn bộ giả thuyết hình học hóa hay giả thuyết Poincaré — kỳ tích hoàn tất chương trình Hamilton–Thurston thuộc về [Grigori Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại lời trao giải chính thức năm 1998 và nêu tên hai giả thuyết lớn được giải quyết (tính trù mật của các điểm cusp theo Bers; giả thuyết hàm theta của Kra).
- Phác họa trực giác **động lực học chỉnh hình** của một ánh xạ hữu tỷ: tập Fatou, tập Julia, và giải thích vì sao **tái chuẩn hóa** (Sullivan, Douady–Hubbard, McMullen) là một cỗ máy về tính cứng chứ không chỉ là phóng to hình ảnh.
- Giải thích trực quan **không gian Teichmüller** của một mặt cong, phép nhúng Bers, và hình ảnh một **cusp** trên biên Bers khi đường cong trên mặt bị bóp thắt lại.
- Phân biệt rành mạch đóng góp của McMullen trong **chương trình hình học hóa của Thurston** (đặc biệt cho đa tạp phân thớ trên đường tròn) với chứng minh toàn bộ giả thuyết hình học hóa của Perelman.
- Kết nối dòng truyền thừa sang [không gian moduli của Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (học trò tiến sĩ của McMullen) mà vẫn tách bạch định lý của mỗi người.
- Tránh phóng đại: huy chương ghi nhận một hệ thống kết quả về tính cứng, tính trù mật và tái chuẩn hóa, không phải việc "phân loại mọi tập Julia".

**Kiến thức nền.** Hàm chỉnh hình trên $$\mathbb{C}$$ và mặt cầu Riemann $$\widehat{\mathbb{C}}$$; khái niệm mặt Riemann compact giống $$g\ge 2$$ với mêtric hyperbolic; quen với việc lặp một ánh xạ nhiều lần. Không cần học trước nhóm Klein (Kleinian groups).

**Liên kết với các bài khác.** Bài này minh họa một chương trình nghiên cứu tổ chức lại cả hình học lẫn động lực học. Các bài hình học liên quan: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Những tên tuổi chính của động lực học phức: Fatou, Julia, Sullivan, Douady–Hubbard, Thurston, Yoccoz.

---

## Bản đồ kiến thức nền: Động lực chỉnh hình và không gian Teichmüller nghiên cứu gì?

Ba từ khóa trong bài — động lực chỉnh hình, không gian Teichmüller, và nhóm Klein — thực ra cùng xoay quanh một khái niệm quen thuộc từ đại học: **ánh xạ bảo giác** (ánh xạ bảo toàn góc).

**1. Động lực học chỉnh hình — trò chơi lặp hàm trên mặt cầu phức.**
Chọn một hàm hữu tỷ $$f(z) = P(z)/Q(z)$$ trên mặt cầu Riemann $$\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$$ (đơn giản nhất là đa thức bậc hai $$f_c(z) = z^2 + c$$). Xuất phát từ một điểm $$z_0$$, ta lặp mãi $$z_1 = f(z_0), z_2 = f(z_1), \ldots$$ và chia mặt cầu thành hai vùng:
- **Tập Fatou (vùng ổn định):** các điểm mà mọi điểm lân cận đều có số phận giống hệt nhau (ví dụ cùng chạy về $$\infty$$ hoặc cùng hút về một chu kỳ).
- **Tập Julia $$J(f)$$ (vùng hỗn loạn):** ranh giới mong manh giữa các số phận, thường là một hình fractal tuyệt đẹp — chỉ cần dịch chuyển điểm xuất phát một chút là quỹ đạo rẽ sang hướng hoàn toàn khác.
Còn khi giữ cố định điểm xuất phát $$z_0 = 0$$ và thay đổi tham số $$c \in \mathbb{C}$$, tập các giá trị $$c$$ mà quỹ đạo $$0 \mapsto c \mapsto c^2+c \mapsto \cdots$$ không thoát ra vô cực chính là **tập Mandelbrot** nổi tiếng!

**2. Không gian Teichmüller — "tập mọi cách uốn dáng" của một mặt cong.**
Hãy cầm một chiếc bánh vòng hai lỗ (mặt đóng giống $$g = 2$$) làm bằng cao su. Về mặt tôpô, mọi chiếc bánh vòng hai lỗ đều giống nhau; nhưng về mặt **hình học hyperbolic** (hay cấu trúc phức), bạn có thể kéo dài cổ bánh, nới rộng lỗ bên trái, bóp nhỏ lỗ bên phải... Mỗi cách trang bị một cấu trúc hyperbolic (kèm theo một "nhãn đánh dấu" ghi nhớ đâu là vòng gốc) cho một điểm trong **không gian Teichmüller** $$\mathcal{T}(S)$$. Nếu ta quên nhãn đánh dấu đi (lấy thương theo nhóm lớp ánh xạ), ta thu được **không gian moduli** $$\mathcal{M}_g$$ trong bài về Mirzakhani.

**3. Từ điển Sullivan — phép đối xứng kỳ lạ giữa 2D và 3D.**
Tại sao lặp hàm $$z^2 + c$$ lại liên quan đến đa tạp hyperbolic 3 chiều? Một nhóm các phép biến đổi Möbius $$z \mapsto \frac{az+b}{cz+d}$$ (gọi là **nhóm Klein**) vừa tác động bảo giác lên mặt cầu Riemann $$\widehat{\mathbb{C}}$$ ở vô cực (chia mặt cầu thành vùng ổn định và **tập giới hạn** fractal, giống hệt Fatou và Julia!), vừa là nhóm đẳng cự của **không gian hyperbolic 3 chiều** $$\mathbb{H}^3$$ nằm bên trong mặt cầu đó! **Dennis Sullivan** phát hiện một bộ từ điển song song tuyệt đẹp giữa hai thế giới — và Curtis McMullen là bậc thầy biến bộ từ điển ấy thành những định lý giải tích và hình học sắc như dao.

---

## 1. Động lực học chỉnh hình: ánh xạ, tập Julia, tập Fatou và tái chuẩn hóa

Trong họ đa thức bậc hai $$f_c(z) = z^2 + c$$, câu hỏi trung tâm nhất của động lực học phức (vẫn còn mở đến ngày nay) là **giả thuyết MLC** (tập Mandelbrot có liên thông địa phương không?) và câu hỏi đi kèm: các đa thức **hyperbolic** (những đa thức có quỹ đạo ổn định rõ ràng) có trù mật trong tập Mandelbrot hay không?

Chìa khóa để tấn công câu hỏi đó là **tái chuẩn hóa** (*renormalization*). Hãy tưởng tượng bạn chọn một tham số $$c$$ nằm trong một "tập Mandelbrot tí hon" ẩn sâu ở mép tập Mandelbrot lớn. Khi đó, nếu ta lặp $$f_c$$ đúng $$p$$ lần ($$f_c^{\circ p}$$) và chỉ nhìn vào một đĩa nhỏ quanh điểm tới hạn $$0$$, ánh xạ $$f_c^{\circ p}$$ hành xử **y hệt một đa thức bậc hai mới** (Douady–Hubbard gọi đây là **ánh xạ dạng bậc hai**, *quadratic-like*). Nếu quá trình phóng to và thu hẹp đó có thể lặp đi lặp lại **vô hạn lần**, ta có một đa thức *tái chuẩn hóa được vô hạn lần* (ví dụ điểm Feigenbaum huyền thoại).

- **Jean-Christophe Yoccoz** (Huy chương Fields 1994) giải quyết được trường hợp tái chuẩn hóa *hữu hạn lần* bằng phương pháp mảnh ghép Yoccoz.
- **Curtis McMullen**, trong chuyên khảo kinh điển *Complex Dynamics and Renormalization* (1994), tấn công đúng phần cứng đầu còn lại: các đa thức **tái chuẩn hóa được vô hạn lần** (loại bị chặn). Bằng cách xây dựng các "tháp" (*towers*) ánh xạ dạng bậc hai và dùng lý thuyết biến dạng tựa bảo giác của Sullivan, ông chứng minh tính cứng cho nhiều lớp đa thức tái chuẩn hóa vô hạn lần — cho thấy rằng khi hai ánh xạ trùng khớp về tổ hợp, hình học bảo giác buộc chúng phải hội tụ về cùng một điểm bất động tái chuẩn hóa duy nhất!

**Tóm tắt.** Động lực học chỉnh hình không phải chuyện vẽ hình fractal cho đẹp mắt; nó là khoa học về **tính cứng**: biến những sự trùng khớp rời rạc về mặt tổ hợp thành đẳng thức chặt chẽ về mặt hình học.

(Trước đó, ngay từ luận án tiến sĩ tại Harvard năm 1985 dưới sự hướng dẫn của **Dennis Sullivan**, McMullen đã gây tiếng vang khi chứng minh không tồn tại thuật toán lặp hữu tỷ thuần túy nào kiểu Newton luôn hội tụ về nghiệm cho mọi đa thức bậc $$\ge 4$$. Tuy nhiên, Huy chương Fields 1998 tôn vinh cả hệ thống lý thuyết sâu rộng hơn nhiều trong thập niên 1990.)

---

## 2. Không gian Teichmüller và biên Bers: khi mặt cong bị bóp thắt

Với một mặt đóng định hướng giống $$g \ge 2$$, **không gian Teichmüller** $$\mathcal{T}(S)$$ là một không gian mượt có chiều thực $$6g - 6$$ (ví dụ với bánh vòng 2 lỗ $$g = 2$$, ta có đúng $$6$$ thông số tự do để thay đổi dáng hình hyperbolic của nó).

**Lipman Bers** đã tìm ra một cách tuyệt vời để "chụp ảnh" toàn bộ không gian $$\mathcal{T}(S)$$ dưới dạng một miền bị chặn nằm trong không gian vector hữu hạn chiều các vi phân bậc hai chỉnh hình (gọi là **phép nhúng Bers**). Cũng giống như một hình cầu mở trong $$\mathbb{R}^n$$ có mặt biên bao quanh, ảnh của $$\mathcal{T}(S)$$ có một đường viền cực kỳ phức tạp gọi là **biên Bers** $$\partial \mathcal{T}(S)$$.

Điều gì xảy ra khi một mặt hyperbolic trôi dần ra đến **biên Bers**? Hãy tưởng tượng bạn buộc một sợi dây quanh một vòng eo của chiếc bánh vòng rồi siết chặt dần cho đến khi chu vi vòng eo thu về $$0$$! Chiếc bánh vòng bị bóp thắt tại vòng eo đó thành hai cái phễu nhọn dài vô tận — gọi là một **cusp** (điểm nhọn). Khi ta bóp thắt đồng thời một hệ cực đại gồm $$3g - 3$$ vòng eo rời nhau (cắt mặt cong thành các "chiếc quần" ba ống rời nhau), ta thu được một **cusp cực đại** (*maximal cusp*) trên biên Bers.

**Giả thuyết Bers (1970)** đặt câu hỏi: những điểm cusp cực đại "gãy gập" đó là những trường hợp hiếm hoi, hay chúng nằm rải rác **trù mật** khắp toàn bộ biên Bers (tức là gần bất kỳ điểm biên kỳ dị nào cũng luôn có một điểm cusp cực đại)? Trong bài báo mang tựa đề ngắn gọn nổi tiếng *"Cusps are dense"* (*Annals of Mathematics*, 1991), **McMullen chứng minh giả thuyết Bers là đúng!** Ý tưởng đột phá của ông là đặt một biến dạng tựa bảo giác có chuẩn đơn vị vào phần "cổ mỏng" của mặt cong và ước lượng chính xác tác động đại số của nó lên độ dài các đường trắc địa, chứng tỏ ta luôn có thể đẩy nhẹ bất kỳ điểm biên nào vào một cusp cực đại.

**Tóm tắt.** "Đường chân trời" của không gian các mặt hyperbolic không hề trơn láng: nó được phủ dày đặc bởi những mặt cong đã bị bóp thắt đến tận cùng thành các điểm nhọn cusp.

---

## 3. Giả thuyết hàm theta của Kra: tiêu chuẩn khả trung bình sắc bén

Xét một phép phủ giữa hai mặt Riemann hyperbolic $$Y \to X$$ (ví dụ phủ phổ dụng từ đĩa đơn vị $$\mathbb{D}$$ xuống mặt cong $$X = \mathbb{D}/\Gamma$$). Phép phủ này tự nhiên cảm sinh một phép nhúng ngược giữa các không gian Teichmüller $$\mathcal{T}(X) \hookrightarrow \mathcal{T}(Y)$$. Câu hỏi giải tích cổ điển đặt ra là: đối với mêtric Teichmüller, phép nhúng này giữ nguyên khoảng cách (**đẳng cự**) hay làm **co chặt** khoảng cách?

Tương đương theo ngôn ngữ đối ngẫu, ta xét **toán tử chuỗi Poincaré** $$\Theta$$ (còn gọi là toán tử theta của Kra), lấy một vi phân bậc hai chỉnh hình khả tích trên đĩa $$\mathbb{D}$$ rồi lấy tổng trung bình theo nhóm phủ $$\Gamma$$ để tạo thành vi phân bậc hai trên $$X$$. Dễ thấy chuẩn toán tử luôn thỏa $$\|\Theta\| \le 1$$; **giả thuyết hàm theta của Irwin Kra** khẳng định rằng đối với phủ phổ dụng của mặt kiểu hữu hạn, toán tử này phải **co chặt**: $$\|\Theta\| < 1$$.

Trong bài báo bước ngoặt năm 1989 (*Inventiones Mathematicae*), **McMullen** không chỉ chứng minh giả thuyết Kra mà còn tìm ra một **tiêu chuẩn tôpô–đại số hoàn hảo** cho mọi phép phủ $$Y \to X$$: chuẩn $$\|\Theta\| = 1$$ **khi và chỉ khi** phép phủ là **khả trung bình** (*amenable*, theo nghĩa nhóm cơ bản tương đối có tính khả trung bình — một khái niệm từ lý thuyết nhóm hình học)! Vì nhóm cơ bản của mặt hyperbolic kiểu hữu hạn chứa nhóm tự do nên *không* khả trung bình, bất đẳng thức chặt $$\|\Theta\| < 1$$ lập tức suy ra!

Tại sao một bất đẳng thức $$\|\Theta\| < 1$$ lại có sức mạnh lớn đến vậy? Trong hình học, **một phép co chặt luôn dẫn đến điểm bất động duy nhất** (như định lý điểm bất động Banach). Chính ước lượng co chặt này đã trở thành đòn bẩy giải tích sắc bén mà McMullen dùng để chứng minh sự tồn tại mêtric hyperbolic trên các đa tạp ba chiều trong chương trình Thurston!

---

## 4. Chương trình hình học hóa, không phải định lý của Perelman

**Giả thuyết hình học hóa của William Thurston** (cuối thập niên 1970) là tầm nhìn vĩ đại nhằm phân loại mọi đa tạp ba chiều đóng: cắt chúng dọc theo các mặt cầu và hình xuyến thành các mảnh sơ cấp, mỗi mảnh mang một trong tám hình học chuẩn tắc, trong đó mảnh **hyperbolic** là phong phú và khó nhất. Chính Thurston đã chứng minh các trường hợp nền tảng (đa tạp Haken), và sau này **Grigori Perelman** (2002–2003) đã hoàn tất *toàn bộ* giả thuyết hình học hóa (kéo theo giả thuyết Poincaré) bằng dòng Ricci có phẫu thuật — xem [bài Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

Đóng góp của McMullen nằm ở một con đường khác hẳn, trực tiếp tiếp nối hình học bảo giác của Thurston. Trong chuyên khảo *Renormalization and 3-Manifolds Which Fiber over the Circle* (1996), ông xét một **đa tạp ba chiều phân thớ trên đường tròn** — hãy hình dung bạn lấy một mặt cong $$S$$ nhân với đoạn thẳng $$[0,1]$$ rồi dán đáy trên $$S \times \{1\}$$ vào đáy dưới $$S \times \{0\}$$ thông qua một phép xoắn (đồng phôi giả Anosov) $$\psi: S \to S$$. Để đặt một mêtric hyperbolic lên đa tạp 3D đó, Thurston cần tìm điểm bất động của toán tử "dán da" (*skinning map*) tác động trên không gian Teichmüller. Bằng chính các công cụ **tái chuẩn hóa**, **tính không uốn được định lượng** (*inflexibility* của đa tạp hyperbolic mở, bổ sung cho định lý cứng Mostow) và **bất đẳng thức co kiểu Kra**, McMullen đã xây dựng một chứng minh hoàn toàn mới, trong sáng và thống nhất cho định lý hyperbolic hóa của Thurston trên lớp đa tạp phân thớ này, chạy song song một-một với định lý điểm bất động tái chuẩn hóa trong động lực học phức!

**Câu phát biểu chính xác cần ghi nhớ:** McMullen xây dựng công cụ tái chuẩn hóa và tính cứng *bên trong* chương trình hình học hóa của Thurston (đặc biệt cho đa tạp phân thớ); còn Perelman *hoàn tất* toàn bộ giả thuyết hình học hóa và giả thuyết Poincaré bằng dòng Ricci.

---

## 5. Vì sao hai giả thuyết được nêu tên lại đi cùng nhau

Thoạt nhìn, tính trù mật của cusp (Bers) và chuẩn toán tử chuỗi Poincaré (Kra) thuộc giải tích trên không gian Teichmüller, còn tập Julia và tái chuẩn hóa thuộc phép lặp hàm phức. Sợi chỉ đỏ nối tất cả lại với nhau chính là **tính cứng của các hệ động lực bảo giác**: dù hệ đó là một ánh xạ hữu tỷ lặp trên mặt cầu Riemann hay một nhóm Klein tác động trên không gian hyperbolic ba chiều, cả hai đều được điều khiển bởi các biến dạng tựa bảo giác, không gian Teichmüller và giới hạn hình học. Bộ từ điển Sullivan vẽ ra bức tranh song song đó; McMullen là người biến từng mục từ điển thành những ước lượng giải tích sắc bén để sinh ra định lý thật.

Cũng từ mái trường Harvard và dòng tư duy hình học–động lực học này của McMullen, thế hệ học trò xuất sắc của ông — nổi bật nhất là **Maryam Mirzakhani** — đã mở ra những chân trời mới về thể tích không gian moduli và động lực học trên các mặt phẳng dịch chuyển (xem [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/)).

---

## 6. Vì sao là Huy chương Fields

1. **Chinh phục các bài toán mang tên tuổi tồn tại lâu năm.** Giả thuyết trù mật cusp của Bers và giả thuyết hàm theta $$\|\Theta\|<1$$ của Kra là những cột mốc giải tích–hình học nổi tiếng; lời giải của McMullen vừa ngắn gọn vừa mở ra tiêu chuẩn tổng quát (tính khả trung bình).
2. **Biến từ điển tái chuẩn hóa thành cỗ máy chứng minh.** Hai chuyên khảo năm 1994 và 1996 của ông đã chứng tỏ tái chuẩn hóa không chỉ là triết lý vật lý hay hình ảnh đẹp, mà là một phương pháp chứng minh thống nhất cho cả động lực học phức lẫn đa tạp hyperbolic ba chiều.
3. **Vị trí trung tâm kết nối ba lĩnh vực lớn.** Công trình của McMullen cho thấy động lực học chỉnh hình, lý thuyết Teichmüller và tôpô ba chiều dùng chung cùng một cơ chế về tính compact và tính cứng bảo giác.

Cùng nhận Huy chương Fields năm 1998 tại Berlin với McMullen là **Richard Borcherds**, **Timothy Gowers** và **Maxim Kontsevich** — một mùa giải rực rỡ tôn vinh bốn trụ cột khác nhau của toán học cuối thế kỷ XX.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "McMullen đã chứng minh hình học hóa / Poincaré." | Hình học hóa đầy đủ là của Perelman. McMullen đóng góp trong chương trình Thurston (hyperbolic hóa đa tạp phân thớ / tái chuẩn hóa). |
| "Cusp trù mật nghĩa là mọi mặt Riemann đều có cusp." | Định lý nói về *biên Bers* của không gian Teichmüller, không nói về một mặt trơn điển hình ở bên trong. |
| "Không gian Teichmüller là không gian moduli." | Không gian Teichmüller giữ thông tin đánh dấu; không gian moduli là thương theo nhóm lớp ánh xạ. |
| "Tập Julia = tập Mandelbrot." | Tập Julia nằm trên mặt phẳng động lực của một ánh xạ; tập Mandelbrot nằm trên mặt phẳng tham số của cả một họ. |
| "Tái chuẩn hóa chỉ là phóng to một bức tranh." | Đó là phép dựng một ánh xạ mới từ ánh xạ dạng bậc hai, kèm một lý thuyết về tính cứng. |
| "Huy chương chỉ vì Bers + Kra." | Đó là hai mục được nêu tên; lời trao giải còn nhắc tới động lực học chỉnh hình và hình học hóa đa tạp ba chiều. |
| "McMullen đã phân loại mọi ánh xạ hữu tỷ." | Không. Công trình nói về tính cứng, tính trù mật và tái chuẩn hóa, không phải liệt kê các lớp liên hợp. |

---

## Bài tập

1. Định nghĩa tập Fatou và tập Julia của một ánh xạ hữu tỷ trong hai câu. Vì sao $$J(f)$$ thường là nơi "đáng chú ý" khi nghiên cứu tính cứng?
2. Ánh xạ dạng bậc hai (quadratic-like) là gì, theo cách nói của Douady–Hubbard? Vì sao phép tái chuẩn hóa tạo ra một ánh xạ như vậy?
3. Phát biểu giả thuyết trù mật cusp của Bers trong một câu cẩn thận, có các từ **biên** và **Teichmüller**.
4. Giả thuyết Kra là bất đẳng thức về chuẩn toán tử $$\|\Theta\|<1$$. Vì sao một phép *co chặt* trên không gian Teichmüller có thể hữu ích về mặt hình học?
5. Viết bốn câu mà một bạn học có thể dùng để phân biệt McMullen với Perelman về chuyện "hình học hóa".
6. Đọc lại lời trao giải chính thức. Hai giả thuyết nào được nêu tên? Hai chủ đề lớn nào bao quanh chúng?
7. **Mở rộng.** So sánh không gian Teichmüller ở đây với không gian moduli trong [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/): thông tin nào được giữ, thông tin nào bị bỏ, và vì sao có thể nghiên cứu động lực học trên cả hai?

---

## Liên kết

- Trang Huy chương Fields của IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Huy chương Fields 1998: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998)
- Wikipedia, Curtis T. McMullen: [https://en.wikipedia.org/wiki/Curtis_T._McMullen](https://en.wikipedia.org/wiki/Curtis_T._McMullen)
- Trang Harvard của McMullen: [https://people.math.harvard.edu/~ctm/](https://people.math.harvard.edu/~ctm/)
- Khóa học: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)
- Tìm arXiv, McMullen dynamics: [https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all](https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all)

---

## Tài liệu tham khảo

1. Citation chính thức Fields Medal 1998 cho C. T. McMullen (IMU / ICM Berlin); xem thêm diễn từ của Yuri Manin với tư cách chủ tịch ủy ban.
2. **S. Smale**, “The work of Curtis T. McMullen,” *Doc. Math.*, Extra Vol. ICM 1998.
3. **C. T. McMullen**, “Cusps are dense,” *Ann. of Math.* **133** (1991).
4. **C. T. McMullen**, “Amenability, Poincaré series and quasiconformal maps,” *Invent. Math.* **97** (1989) (giả thuyết theta của Kra).
5. **C. T. McMullen**, *Complex Dynamics and Renormalization*, Ann. of Math. Studies **135**, Princeton, 1994.
6. **C. T. McMullen**, *Renormalization and 3-Manifolds Which Fiber over the Circle*, Ann. of Math. Studies **142**, Princeton, 1996.
7. Nền: Douady–Hubbard về ánh xạ quadratic-like và tập Mandelbrot; Sullivan về phân thớ mặt Riemann và từ điển với nhóm Kleinian; Thurston về hình học hóa (các trường hợp Haken / phân thớ).
8. Khóa học: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

---

## Hướng đi tiếp

- Đọc bài giới thiệu ngắn của Smale tại ICM trước khi đọc hai cuốn sách năm 1994 và 1996.
- So sánh biên Bers với biên của tập Mandelbrot: cả hai được dự đoán là có cấu trúc phân lá (Thurston; Douady–Hubbard). Kết quả trù mật cusp của McMullen ủng hộ một phía của sự tương tự này.
- Bài tập thêm: lập một "từ điển" một trang gồm ba cặp khái niệm song song (ánh xạ hữu tỷ / nhóm Klein; tập Julia / tập giới hạn; tái chuẩn hóa / hyperbolic hóa đa tạp phân thớ), nhưng không khẳng định rằng từ điển này là một tương đương chặt chẽ.

## Video tham khảo

- **Xem trước**: [Curtis McMullen: Manifolds, topology and dynamics](https://www.youtube.com/watch?v=g0fQDrV-UuE) (The Abel Prize, tiếng Anh). McMullen nói về đa tạp, tôpô và động lực học ở mức đại chúng. Phù hợp để làm quen với các chủ đề trước khi đọc bài.
- [Planes in number theory, geometry and dynamics: C. McMullen](https://www.youtube.com/watch?v=hlDDHnk5aRU) (Fields Institute, tiếng Anh). Bài giảng về vai trò của các mặt phẳng trong lý thuyết số, hình học và động lực học. Thuộc giai đoạn sau giải Fields, nên xem sau khi đã đọc xong bài.
- [Dynamics on K3 Surfaces - Curtis McMullen](https://www.youtube.com/watch?v=gWTi1xvGMb8) (Stony Brook Mathematics, tiếng Anh). Bài giảng về động lực học trên mặt K3, một hướng nghiên cứu khác của McMullen. Dùng làm góc nhìn bổ sung, không thuộc lời trao giải 1998.
