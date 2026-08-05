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

**Phương trình Navier–Stokes** mô hình chuyển động của chất lỏng nhớt không nén. Chúng là xương sống của cơ học chất lưu kỹ thuật—và đồng thời là bài toán Thiên niên kỷ của Viện Clay về lý thuyết **nghiệm trơn toàn cục** trong ba chiều.

Đây **không** phải câu hỏi “ta có chạy mô phỏng được không?” Kỹ sư chạy solver Navier–Stokes mỗi ngày cho máy bay, thời tiết, ống dẫn, sinh học. Câu hỏi Clay là: mô hình continuum toán học—hệ PDE lý tưởng—có được **bảo đảm** giữ trơn mọi thời gian từ dữ liệu ban đầu trơn (năng lượng hữu hạn), hay **singularity** (thổi phồng gradient / vorticity) có thể hình thành trong thời gian hữu hạn?

Bài này tách rõ **thực hành kỹ thuật**, **nghiệm yếu Leray**, và **bài toán chính quy Thiên niên kỷ**, kể kết quả từng phần có tên, và nối văn hóa đa thang (DNS, rối) mà không đồng nhất chi phí lưới với giải thưởng Clay.

**Lộ trình:** phương trình → ý nghĩa vật lý → Clay hỏi gì → điều đã biết → vì sao khó → Deng/kinetic → kỹ thuật vs Millennium → nhầm lẫn.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết hệ Navier–Stokes **không nén** (vận tốc + áp suất, ràng buộc $$\nabla\cdot u=0$$) ở mức khẩu hiệu và gọi tên hạng phi tuyến, nhớt, áp suất.
- Phân biệt **dùng kỹ thuật** NS với **bài toán chính quy Thiên niên kỷ**.
- Giải thích nghiệm yếu **Leray** so với nghiệm trơn cổ điển (tồn tại yếu toàn cục ≠ chính quy/duy nhất đầy đủ).
- Phát biểu bài toán mở: tồn tại–duy nhất trơn 3D toàn cục, hoặc blow-up thời gian hữu hạn từ dữ liệu trơn.
- Kể một họ kết quả từng phần: Beale–Kato–Majda; dữ liệu nhỏ / mild solutions; partial regularity (Caffarelli–Kohn–Nirenberg); chính quy 2D.
- Nối với [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): suy dẫn continuum từ kinetic **khác** chính quy NS 3D.
- Tránh LO6: “máy bay bay được nên NS đã giải,” “mô phỏng blow-up = chứng minh.”

**Tiên quyết.** Giải tích nhiều biến; ý tưởng PDE như định luật cân bằng địa phương. Không cần khóa học PDE nâng cao—các định lý được kể ở mức khẩu hiệu có tên.

**Liên kết seminar.** **LO1**; essay [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (nền tảng kinetic của chất lưu); ứng dụng phương trình vi phân trong khóa khi có.

---

## 1. Phương trình (dạng không nén)

Cho trường vận tốc $$u(x,t)\in\mathbb{R}^3$$ và áp suất $$p(x,t)$$,

$$
\begin{aligned}
\partial_t u + (u\cdot\nabla)u &= \nu \Delta u - \nabla p + f,\\
\nabla\cdot u &= 0,
\end{aligned}
$$

với độ nhớt $$\nu>0$$ và lực ngoài tùy chọn $$f$$. Trên $$\mathbb{R}^3$$ hoặc xuyến $$\mathbb{T}^3$$, thường cho dữ liệu ban đầu trơn, divergence-free, năng lượng hữu hạn.

**Hạng từng cái:**

- $$\partial_t u$$ — gia tốc cục bộ của vận tốc.  
- $$(u\cdot\nabla)u$$ — **advection phi tuyến**: chất lỏng mang động lượng theo streamline—nguồn toán học của nhiều khó khăn.  
- $$\nu\Delta u$$ — **khuếch tán nhớt**: nhớt làm trơn gradient vận tốc; $$\nu$$ lớn → “dính” hơn (mật ong vs nước, ẩn dụ thô).  
- $$-\nabla p$$ — gradient áp suất; áp suất điều chỉnh tức thì để giữ ràng buộc.  
- $$\nabla\cdot u=0$$ — **không nén**: dòng bảo toàn thể tích (mật độ hằng trong mô hình đơn giản).  
- $$f$$ — lực khối (trọng lực, khuấy, …), thường =0 trong bài toán Clay thuần.

Áp suất không phải trường tự do độc lập như $$u$$: lấy divergence phương trình động lượng, $$p$$ được khôi phục (sai hằng số) qua phương trình kiểu Poisson. Không nén là ràng buộc; áp suất là nhân tử Lagrange giữ nó.

**Đọc vật lý ngắn.** Số Reynolds lớn ≈ nhớt tương đối nhỏ: quán tính/vận chuyển thắng khuếch tán—chế độ rối, nhiều thang. Clay không hỏi “rối trông như thế nào trên máy,” mà hỏi liệu mô hình continuum có thể tự tạo singularity toán học.

**Năng lượng.** Nhân trong phương trình động lượng với $$u$$ và tích phân (biên/suy giảm phù hợp) cho **bất đẳng thức năng lượng**: động năng $$E(t)=\frac12\int|u|^2\,dx$$ bị kiểm soát bởi dữ liệu ban đầu và công của lực, trong khi nhớt tiêu tán đại lượng kiểu enstrophy. Kiểm soát năng lượng đủ để xây nghiệm yếu—và **không** đủ, một mình, để ngăn tập trung gradient trong 3D.

---

## 2. Bài toán Thiên niên kỷ hỏi gì

Đại ý (xem Fefferman / Clay cho wording và không gian hàm chính xác) trên $$\mathbb{R}^3$$ (hoặc torus):

Chứng minh một trong hai hướng:

- **Chính quy toàn cục:** dữ liệu trơn, divergence-free, năng lượng hữu hạn (và lực phù hợp) cho nghiệm trơn duy nhất $$u,p$$ mọi $$t>0$$, không blow-up hữu hạn thời gian của các chuẩn tự nhiên; hoặc  
- **Blow-up:** tồn tại dữ liệu trơn năng lượng hữu hạn sao cho nghiệm trơn không tiếp tục sau thời gian hữu hạn $$T_*$$—một chuẩn vận tốc hoặc vorticity unbounded khi $$t\to T_*^-$$.

Liên quan: **duy nhất** nghiệm yếu Leray–Hopf; bản chất hình học tập kỳ dị khả dĩ. Giải thưởng cho định lý continuum PDE, không cho thí nghiệm số “trông kỳ dị” trên lưới.

**Tình trạng (2026):** **mở**. Một trong sáu bài Thiên niên kỷ chưa giải. Poincaré là bài duy nhất đã giải (Perelman).

“Mở” = **định lý tồn tại/chính quy continuum**, không phải “chưa ai mô phỏng được nước.”

---

## 3. Điều *đã* biết: thời gian ngắn, 2D, nghiệm yếu

**Tồn tại thời gian ngắn.** Dữ liệu trơn divergence-free cho nghiệm trơn duy nhất trên $$[0,T)$$ với $$T$$ phụ thuộc cỡ dữ liệu (Sobolev/Hölder phù hợp). Câu hỏi: $$T=\infty$$ luôn, hay $$T$$ hữu hạn với một số dữ liệu?

**Hai chiều.** Chính quy toàn cục 2D là cổ điển. Lý do cấu trúc: **vortex stretching** vắng hoặc dễ kiểm soát hơn. Vorticity $$\omega=\nabla\times u$$ thỏa transport-diffusion không có hạng stretching đầy đủ $$(\omega\cdot\nabla)u$$ của 3D. “NS 2D chưa giải” là sai; độ khó Millennium là **ba chiều**.

**Leray (1934).** Jean Leray dựng nghiệm **yếu** toàn cục 3D: trường thỏa phương trình theo nghĩa phân bố, bất đẳng thức năng lượng, khớp dữ liệu ban đầu trong topology phù hợp. Tồn tại không phải phần trống. Còn mở: nghiệm yếu có trơn với dữ liệu trơn không; có duy nhất không; mọi nghiệm yếu có cổ điển khi dữ liệu đẹp không.

Cảnh quan: “tồn tại yếu toàn cục đã biết; well-posedness trơn toàn cục thì chưa.”

---

## 4. Vì sao chính quy 3D khó

Kẻ thù là **hạng phi tuyến** cùng **vortex stretching** 3D. Ước lượng năng lượng kiểm soát $$L^2$$ của vận tốc nhưng không tự đóng ước lượng đạo hàm cao. Cascade năng lượng xuống thang nhỏ—bóng toán của turbulence—có thể, trong kịch bản continuum xấu nhất, đẩy gradient ra vô hạn trong thời gian hữu hạn.

Hai slogan đối nghịch:

- Nhớt *làm trơn*, nên singularity có lẽ không thể.  
- Phi tuyến *tập trung*, nên nhớt có thể thua với một số dữ liệu.

Không slogan nào là chứng minh. Numerics rối dữ dội nhưng rời rạc hóa / dưới-độ-phân-giải / mô hình đóng nghĩa “nổ trên máy” ≠ chứng minh Clay—và mô phỏng êm ≠ định lý chính quy toàn cục.

So [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/): kiểm hữu hạn không kết thúc phát biểu vô hạn; ở đây kiểm số PDE rời rạc không kết thúc phát biểu continuum. **Evidence ≠ proof.**

---

## 5. Tiêu chí chính quy, dữ liệu nhỏ, partial regularity

**Chính quy điều kiện.** Nếu một số chuẩn giữ hữu hạn trên $$[0,T]$$ thì nghiệm trơn đến $$T$$. Ví dụ nổi: **Beale–Kato–Majda**—tích phân thời gian của $$\|\omega(\cdot,t)\|_{L^\infty}$$ hữu hạn ngăn blow-up đến $$T$$. Nhiều biến thể (Prodi–Serrin; Escauriaza–Seregin–Šverák endpoint). Chúng rút Millennium về: *chứng minh các chuẩn đó không nổ*—hoặc *dựng dữ liệu làm chúng nổ*.

**Dữ liệu nhỏ.** Dữ liệu đủ nhỏ trong không gian tới hạn phù hợp ⇒ nghiệm trơn toàn cục. Dữ liệu lớn là chiến trường: phi tuyến có thể, về nguyên tắc, tập trung năng lượng vào thang nhỏ.

**Partial regularity.** Với nghiệm yếu phù hợp, **Caffarelli–Kohn–Nirenberg** (trên Scheffer) cho thấy tập kỳ dị không–thời gian có **chiều Hausdorff parabolic** ≤1—singularity, nếu có, “nhỏ” theo nghĩa geometric measure. Đó là định lý chính quy sâu; **không** phải chính quy đầy đủ. Họ hàng free-boundary / minimal surface: kiểm soát cỡ tập xấu khi chưa chứng minh tập rỗng.

**Mốc khác** (biết tên, không catalog đủ): Ladyzhenskaya, Prodi, Serrin; nghiệm mild Kato; convex integration / non-uniqueness cho nghiệm *yếu hơn* (văn hóa Onsager)—khu vực nhanh, đọc phổ thông cẩn thận.

---

## 6. Kinetic foundations, Hilbert thứ sáu, và Deng

Câu hỏi thứ hai về chất lưu: không chỉ “PDE continuum có trơn?” mà “PDE continuum có đúng là giới hạn của hệ hạt?”—tinh thần **bài toán thứ sáu Hilbert** (từ cơ học nguyên tử qua thống kê tới continuum).

Chương trình Fields-recognized của **Yu Deng** (cùng cộng sự, gồm Hani và Ma) xây cầu chặt từ hard-sphere tới Boltzmann và, trong chế độ phù hợp, tới phương trình chất lưu. Điều đó hỗ trợ *suy dẫn* mô hình continuum dưới giả thiết nêu. **Không** tự chứng minh chính quy NS 3D cho phát biểu Millennium continuum.

Dùng [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) để hiểu **vì sao PDE chất lưu tồn tại như giới hạn**. Dùng *bài này* để hiểu **liệu PDE continuum đó có giữ trơn**. Derivation và regularity là chương kề, không cùng định lý.

Văn hóa chính quy Abel-era của Caffarelli (free boundary, PDE phi tuyến) là cầu khác: partial regularity NS là họ hàng geometric measure—phân tích kiểm soát singularity mà không luôn xóa hết.

---

## 7. CFD kỹ thuật không phải bài Millennium (LO6)

| Thực tiễn | Bài toán Clay |
|-----------|---------------|
| DNS / LES / RANS | Lý thuyết trơn toàn cục cho NS không nén lý tưởng |
| Lưới, bước thời gian, mô hình rối | Định lý tồn tại / duy nhất / chính quy |
| Chi phí Reynolds khi resolve eddy | Ước lượng giải tích và blow-up khả dĩ |
| Validation thí nghiệm | Chứng minh trong không gian hàm |

Cả hai quan tâm cascade đa thang. Chỉ một cái là Clay. “NS đã giải vì ANSYS chạy” fail LO6; “máy bay không được bay vì Clay mở” fail common sense và LO6 ngang nhau.

**DNS** cố gắng giải NS xuống thang nhớt—chi phí tăng nhanh với Reynolds. **LES/RANS** mô hình thang nhỏ. Thành công kỹ thuật không trả lời Clay.

---

## 8. Văn hóa toán học quanh NS

- **Tiêu chí chính quy:** “nếu singularity thì …” — định lý điều kiện.  
- **Nghiệm yếu:** tồn tại toàn cục với ít chính quy—rồi hỏi nâng cấp.  
- **Dữ liệu nhỏ:** phi tuyến không luôn thắng.  
- **Partial regularity:** singularity, nếu có, “hiếm” theo độ đo.

Mẫu “toán quanh bài mở” giống [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): câu hỏi gốc kháng cự, ngành đầy định lý.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “NS chưa giải nên máy bay không được bay.” | Mô hình kỹ thuật + thực nghiệm hoạt động; Clay hỏi định lý tồn tại/chính quy thuần. |
| “Ai đó mô phỏng blow-up thì bài toán xong.” | Mô phỏng ≠ chứng minh PDE continuum. |
| “Deng đã giải Navier–Stokes.” | Deng đẩy suy dẫn kinetic; chính quy NS 3D vẫn mở. |
| “2D và 3D như nhau.” | Chính quy 2D đã biết; 3D là case khó. |
| “Leray đã giải vì có nghiệm toàn cục.” | Nghiệm yếu; chính quy/duy nhất đầy đủ mở. |
| “Clay là về chọn bước lưới tối ưu.” | Không—là về lý thuyết giải tích PDE. |

---

## Bài tập

1. Trong hệ NS, chỉ rõ hạng phi tuyến và hạng nhớt; một câu vai trò mỗi hạng.  
2. $$\nabla\cdot u=0$$ nghĩa vật lý gì trong mô hình không nén?  
3. Đối chiếu nghiệm yếu Leray với nghiệm trơn cổ điển (tồn tại, chính quy, duy nhất).  
4. **LO1 (≤300 từ):** phát biểu bài toán Clay NS, vì sao khó, một kết quả từng phần có tên.  
5. Sau khi đọc [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): viết ba câu phân biệt *suy dẫn* NS và *chính quy* NS.  
6. **LO6:** sửa câu báo “Nhà toán học mô phỏng rối 3D, giải thưởng Clay sắp về tay.”  
7. Liệt kê hai lý do numerics không chứng minh blow-up continuum.  
8. Stretch: đọc mô tả Clay của Fefferman và ghi lại (khẩu hiệu) bối cảnh không gian hàm ông dùng.

---

## Từ các bài giảng: văn hóa blow-up (Tao) và văn hóa chính quy (Caffarelli)

Numberphile (Crawford), bài Clay của Caffarelli, và Einstein Lecture của Tao bổ sung khẩu hiệu:

- **Dòng Caffarelli:** chính quy từng phần (CKN) ràng buộc *mức độ xấu* của tập kỳ dị nghiệm yếu phù hợp—tập “nhỏ” không đồng nghĩa tập rỗng.  
- **Dòng Tao:** blow-up hữu hạn thời gian cho mô hình *trung bình* / toy nhấn mạnh **supercriticality**—ước lượng năng lượng không đủ scale để đóng bootstrap cho dữ liệu trơn lớn. Blow-up trên phương trình sửa đổi **không** là giải Clay cho NS thật.  
- **Đồng tồn kỹ thuật:** DNS/LES/RANS sống trong thế giới rời rạc; Clay hỏi định lý continuum.

**Tình trạng (2026):** chính quy toàn cục / blow-up 3D **mở** (Millennium).

---

## Nguồn video (gói math-video-researcher)

Xếp hạng: `research/video-research/Navier_Stokes/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *Navier-Stokes Equations* (Crawford): [YouTube](https://www.youtube.com/watch?v=ERBVFcutl3M).  
2. **Trực giác** — vcubingx, *The million dollar equation*: [YouTube](https://www.youtube.com/watch?v=Ra7aQlenTb8).  
3. **Nền** — Caffarelli, bài Clay về NS: [YouTube](https://www.youtube.com/watch?v=ta6Q70y6YVU).  
4. **Nghiên cứu** — Tao, *Can NS Blow Up in Finite Time?*: [YouTube](https://www.youtube.com/watch?v=DgmuGqeRTto).  
5. **Văn bản gốc** — Fefferman PDF: [navierstokes.pdf](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) · [Clay](https://www.claymath.org/millennium/navier-stokes-equation/).

**Sau video:** CFD thành công ≠ định lý Clay. Yếu ≠ trơn. Tình trạng **mở** năm 2026.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/Navier_Stokes/transcripts/` · trạng thái: `research/video-research/Navier_Stokes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Navier_Stokes_ERBVFcutl3M_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Thư mục URL: `research/video-research/Navier_Stokes/references.md`.

1. Clay — [NS](https://www.claymath.org/millennium/navier-stokes-equation/) · Fefferman PDF: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf  
2. Robinson — [survey](https://royalsocietypublishing.org/rsta/article/378/2174/20190526/111659/The-Navier-Stokes-regularity-problem).  
3. Wikipedia — [NS existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness).  
4. Numberphile: https://www.youtube.com/watch?v=ERBVFcutl3M  
5. vcubingx: https://www.youtube.com/watch?v=Ra7aQlenTb8  
6. Caffarelli: https://www.youtube.com/watch?v=ta6Q70y6YVU  
7. Tao: https://www.youtube.com/watch?v=DgmuGqeRTto  
8. [Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/). Gói: `research/video-research/Navier_Stokes/`.

---

## Hướng đi tiếp

Ứng viên **A3**. Studio: cascade Kolmogorov như *heuristic*—không phải chứng minh. Đọc Deng cho “từ hạt tới continuum,” rồi giữ ranh giới kỹ thuật vs Clay.
