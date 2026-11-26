---
layout: post
title: "John Pardon: Hình học Symplectic và Tôpô (Huy chương Fields 2026)"
chapter: '02'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Nếu hình học Euclid cho ta thước đo *độ dài* và *góc*, thì **hình học symplectic** — ngôn ngữ hình học của cơ học cổ điển Hamilton — lại chỉ quan tâm đến *diện tích có hướng* trong không gian pha. Trong thế giới kỳ lạ ấy, mọi đa tạp symplectic cùng số chiều nhìn cục bộ đều giống hệt nhau (định lý Darboux), nên không hề có khái niệm "độ cong cục bộ" để phân biệt chúng. Muốn khám phá hình dạng toàn cục của một không gian symplectic, các nhà toán học thả vào đó những "đầu dò" gọi là **đường cong chỉnh hình** rồi đếm xem có bao nhiêu đường cong thỏa điều kiện cho trước.

Nghe thì tưởng gọn gàng, nhưng suốt nhiều thập kỷ, cả một tòa lâu đài lý thuyết (bất biến Gromov–Witten, đồng điều Floer, **phạm trù Fukaya** của đối xứng gương) đứng trước một vết nứt nền móng nguy hiểm: tập hợp mọi đường cong chỉnh hình (không gian moduli) hiếm khi trơn tru và đúng số chiều như kỳ vọng! Nếu không có một cách "đếm" chặt chẽ khi không gian moduli bị méo mó hay có điểm kỳ dị, rất nhiều định lý quan trọng chỉ dừng lại ở mức phác thảo.

**John Pardon** (Stony Brook / Simons Center) nhận **Huy chương Fields 2026** chính vì đã gia cố và xây lại tầng nền móng ấy: phát triển các cách tiếp cận mới cho **chu trình cơ bản ảo** (*virtual fundamental cycle*), xây dựng chặt chẽ **phạm trù Fukaya** cho những lớp đa tạp rộng lớn, và đồng thời đóng góp những kết quả nổi bật cho tôpô chiều thấp như tác động nhóm trên đa tạp 3 chiều (giả thuyết Hilbert–Smith) và lý thuyết nút.

**Trích dẫn ngắn của IMU:**  
For his achievements in symplectic geometry including new approaches to virtual fundamental cycles, Fukaya categories of certain manifolds and counting holomorphic curves, and for his contributions to other areas of geometry and topology, including group actions on 3-manifolds and knot theory.

*Tạm dịch:* Cho các thành tựu trong hình học symplectic, gồm những cách tiếp cận mới cho chu trình cơ bản ảo, phạm trù Fukaya của một số đa tạp và việc đếm đường cong chỉnh hình, cùng những đóng góp cho các lĩnh vực khác của hình học và tôpô, gồm tác động nhóm trên đa tạp 3 chiều và lý thuyết nút.

**Mạch bài học:** Kiến thức cần nhớ (tính tay 2-dạng symplectic bằng ma trận $$J$$, chứng minh số chiều luôn chẵn, định lý con lạc đà Gromov) → Giải thích 4 bước: đường cong chỉnh hình, mất tính hoành, tập bản đồ ẩn (*implicit atlas*) và phạm trù Fukaya → Tôpô chiều thấp → Slide ICM 2026 (Log Derived Regularity).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tự kiểm tra bằng đại số tuyến tính vì sao dạng symplectic $$\omega$$ đo diện tích có hướng và ép **số chiều của đa tạp symplectic phải luôn chẵn**.
- Hiểu trực giác độ cứng symplectic qua **định lý không ép được** (*nonsqueezing*) của Gromov.
- Giải thích vì sao không gian moduli đường cong chỉnh hình thường mất **điều kiện hoành** và hiểu vai trò của **chu trình cơ bản ảo** (*implicit atlas* của Pardon).
- Mô tả **phạm trù Fukaya** (đối tượng là đa tạp con Lagrange, phép hợp thành đếm đĩa chỉnh hình) và vị trí của nó trong **đối xứng gương**.
- Đọc định lý **Log Derived Regularity** trên slide ICM 2026 như một công trình **đang thực hiện**, tách bạch với lời trích dẫn chính thức của IMU.

**Kiến thức cần có.** Đại số tuyến tính (ma trận, định thức), đạo hàm riêng và khái niệm đa tạp trơn cơ bản.

**Liên hệ với khóa học.** So sánh kiểu huy chương "cho nền tảng" (Pardon, [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/)) với kiểu huy chương "cho một giả thuyết nổi tiếng". Có thể đọc cùng bài [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), nơi không gian moduli được hiểu theo nghĩa khác (moduli của mặt Riemann).

---

## Kiến thức cần nhớ: Hình học symplectic và Không gian pha là gì?

### 1. Dạng symplectic $$\omega$$ — Tính tay với ma trận $$2\times 2$$ và chứng minh số chiều luôn chẵn
Trong cơ học cổ điển, trạng thái của một hạt chuyển động trên đường thẳng được mô tả bởi cặp $$(q, p)$$ (vị trí và động lượng) trên mặt phẳng pha $$\mathbb{R}^2$$. Trên mặt phẳng đó, ta có **2-dạng symplectic chuẩn** $$\omega = dq \wedge dp$$, viết dưới dạng ma trận đối xứng lệch:

$$
J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad \omega(u, v) = u^T J v = u_1 v_2 - u_2 v_1 = \det(u, v).
$$

$$\omega(u, v)$$ chính là **diện tích có hướng** của hình bình hành sinh bởi hai vectơ $$u, v$$!
Một **đa tạp symplectic** $$(M, \omega)$$ tổng quát là đa tạp trang bị 2-dạng $$\omega$$ thỏa hai tiên đề: **đóng** ($$d\omega = 0$$) và **không suy biến** (ma trận đối xứng lệch $$J$$ đại diện cho $$\omega$$ tại mỗi điểm có $$\det(J) \neq 0$$).

**Chứng minh 2 dòng vì sao đa tạp symplectic luôn có số chiều chẵn:** Giả sử $$\dim M = m$$. Vì $$J^T = -J$$, lấy định thức hai vế ta có:

$$
\det(J) = \det(J^T) = \det(-J) = (-1)^m \det(J).
$$

Nếu $$m$$ là số lẻ thì $$\det(J) = -\det(J) \implies \det(J) = 0$$ (suy biến — vô lý!). Vậy $$m = 2n$$ **bắt buộc phải là số chẵn**!

### 2. "Cứng" hay "mềm"? Định lý không ép được (Nonsqueezing) của Gromov
Trong không gian bảo toàn thể tích thông thường, bạn luôn có thể bóp một quả cầu cao su bán kính $$R$$ thành một sợi dây siêu mảnh để luồn vừa vào một ống trụ bán kính $$r$$ nhỏ tùy ý. Nhưng năm 1985, **Mikhail Gromov** gây chấn động khi chứng minh **Định lý không ép được** (thường gọi vui là *định lý con lạc đà symplectic*):
- Xét quả cầu 4 chiều $$B^4(R) = \{q_1^2 + p_1^2 + q_2^2 + p_2^2 \le R^2\}$$ (thể tích hữu hạn $$\frac{\pi^2}{2}R^4$$) và ống trụ symplectic $$Z^4(r) = \{q_1^2 + p_1^2 \le r^2\} \times \mathbb{R}^2$$ (thể tích **vô hạn**!).
- Nếu $$r < R$$, **không tồn tại bất kỳ phép biến đổi symplectic nào** nhét được $$B^4(R)$$ vào trong $$Z^4(r)$$!

Điều này chứng tỏ hình học symplectic mang một kiểu **độ cứng toàn cục** bí ẩn — dù cục bộ mọi đa tạp symplectic đều giống hệt $$\mathbb{R}^{2n}$$ (định lý Darboux)!

### 3. Đường cong chỉnh hình & Ví dụ trực quan về "Mất tính hoành"
Để phát hiện độ cứng toàn cục đó, Gromov đưa vào **đường cong chỉnh hình** $$u: (\Sigma, j) \to (M, J)$$ thỏa phương trình Cauchy–Riemann $$du \circ j = J \circ du$$. Muốn biến việc "đếm đường cong" thành bất biến tô pô, ta cần **điều kiện hoành** (*transversality*). Hãy hình dung bằng hai đường tròn trên mặt phẳng:
- **Cắt ngang (hoành):** cắt nhau tại đúng 2 điểm rõ ràng → số giao đếm được bằng $$2$$.
- **Tiếp xúc (mất hoành):** chạm nhau tại 1 điểm duy nhất.
- **Trùng khít nhau (sai hẳn số chiều!):** giao nhau là cả một đường tròn 1 chiều thay vì tập điểm 0 chiều!

Khi không gian moduli các đường cong chỉnh hình bị "trùng khít" hoặc xuất hiện các **đường cong phủ bội** (như ánh xạ $$z \mapsto z^2$$ quấn nhiều vòng lên cùng một hình cầu), phép đếm ngây thơ sụp đổ — đó là nơi **chu trình cơ bản ảo** ra tay.

---

## 1. Giải thích: Chu trình cơ bản ảo và Phạm trù Fukaya hoạt động như thế nào?

Tại sao đóng góp "xây nền móng" của John Pardon lại được IMU trao Huy chương Fields 2026? Hãy theo dõi mạch 4 bước dưới đây:

#### Bước 1: Không gian moduli $$\mathcal{M}$$ và rào cản phủ bội
Muốn định nghĩa bất biến Gromov–Witten hay đồng điều Floer, ta gom tất cả đường cong chỉnh hình thỏa điều kiện biên thành **không gian moduli** $$\mathcal{M}$$. Lý tưởng là $$\mathcal{M}$$ phải là đa tạp trơn có số chiều đúng bằng chỉ số Fredholm để ta tích phân hay đếm điểm trên đó. Nhưng trên đa tạp symplectic tổng quát, các đường cong phủ bội mang nhiều phép tự đẳng cấu khiến ta **không thể nhiễu cấu trúc gần phức $$J$$** để làm $$\mathcal{M}$$ trở nên trơn — $$\mathcal{M}$$ bị biến thành một không gian kỳ dị (kiểu orbifold) với số chiều sai lệch!

#### Bước 2: Tập bản đồ ẩn (*Implicit Atlas*) của Pardon tạo ra Chu trình cơ bản ảo
Để đếm được ngay cả khi $$\mathcal{M}$$ xấu xí, ta cần xây dựng **chu trình cơ bản ảo** $$[\mathcal{M}]^{\mathrm{vir}}$$ — một lớp đồng điều thay thế mang đúng số chiều lý thuyết, bất biến dưới biến dạng. Trước Pardon, các cách tiếp cận (cấu trúc Kuranishi của Fukaya–Ono, polyfold của Hofer–Wysocki–Zehnder) đòi hỏi bộ máy giải tích khổng lồ và gây nhiều tranh cãi kỹ thuật suốt 20 năm. **John Pardon** đã phát minh ra khái niệm **tập bản đồ ẩn** (*implicit atlas*) thuần túy đại số–tô pô cực kỳ trong sáng: chỉ cần phủ cục bộ không gian moduli bằng những lát cắt hữu hạn chiều đơn giản rồi dùng đại số đồng điều để dán thành một **chu trình cơ bản ảo** hoàn toàn chặt chẽ!

#### Bước 3: Xây dựng và tính toán Phạm trù Fukaya (Phía A của Đối xứng gương)
Một **đa tạp con Lagrange** $$L \subset (M, \omega)$$ có số chiều bằng một nửa $$\dim M$$ (tức $$n$$ trong không gian $$2n$$ chiều) và thỏa $$\omega\vert_L = 0$$ (ví dụ không gian vị trí $$(q_1, \dots, q_n)$$ trong không gian pha). **Phạm trù Fukaya** gom các đa tạp con Lagrange làm đối tượng, lấy giao điểm giữa chúng làm cấu xạ, và định nghĩa phép hợp thành bằng cách **đếm các đĩa chỉnh hình** căng giữa 3 (hay $$k$$) đa tạp con Lagrange (tạo thành cấu trúc phạm trù $$A_\infty$$). Giả thuyết **đối xứng gương đồng điều** của Kontsevich dự đoán phạm trù Fukaya này tương đương với phạm trù các bó nhất quán bên hình học đại số phức! Nhờ bộ máy chu trình ảo và kỹ thuật cắt dán *Liouville sectors* (cùng Sheel Ganatra và Vivek Shende), Pardon đã biến phạm trù Fukaya từ một ý tưởng đầy hứa hẹn thành công cụ tính toán được một cách chặt chẽ.

#### Bước 4: Vượt ra ngoài Symplectic — Tôpô chiều thấp và Giả thuyết Hilbert–Smith
Không chỉ làm nền móng cho hình học symplectic, Pardon còn giải quyết **giả thuyết Hilbert–Smith trong 3 chiều** (chứng minh nhóm số nguyên $$p$$-adic $$\mathbb{Z}_p$$ không thể tác động trung thành lên đa tạp 3 chiều) và đóng góp sâu sắc vào lý thuyết nút — cho thấy tầm vóc toàn diện về cả hình học lẫn tôpô.

Tóm tắt mạch đóng góp:

$$
\text{Đường cong chỉnh hình}
\;\xrightarrow{\text{Mất tính hoành}}\;
\text{Tập bản đồ ẩn (Pardon)}
\;\longrightarrow\;
\text{Chu trình ảo } [\mathcal{M}]^{\mathrm{vir}}
\;\longrightarrow\;
\text{Phạm trù Fukaya \& Đối xứng gương}.
$$

---


### Video ngắn 1: Hình học Symplectic & Chu trình Cơ bản Ảo của John Pardon

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/pardon-symplectic-vfc_vi.mp4"></video>
</div>

Video dài khoảng 37 giây (có thuyết minh tiếng Việt): bảo toàn diện tích pha ω, định lý lạc đà Gromov, kỳ dị không gian mô đun đường cong J-chỉnh hình và chu trình cơ bản ảo.

## 2. Bài giảng Fields tại ICM 2026: Tính chính quy dẫn xuất loga (đang thực hiện)

Tại **ICM 2026** (Philadelphia), bài giảng Fields của Pardon trình bày cả những công trình về không gian moduli vượt ra ngoài các mục chính trong lời trích dẫn ngắn của IMU. Một đoạn reel công khai cho thấy slide cuối cùng (19/19) có tiêu đề **Logarithmic derived regularity**.

### Định lý (Log Derived Regularity Theorem; đang thực hiện)

*Viết lại từ nội dung trên slide, không phải từ lời giảng đầy đủ.*

Cho

$$
W \xrightarrow{\mathrm{strict}} C \xrightarrow{\mathrm{exact}} B
$$

là một **bài toán lát cắt elliptic** (*elliptic section problem*) trên một đa tạp **log trơn** (*log smooth*) $$B$$. Giả sử $$C\to B$$ là ánh xạ riêng (*proper*) và có độ sâu một (*depth one*), và giả sử **các đầu mút không suy biến** hoặc **kiểu Morse–Bott** với cấu trúc tắt dần theo hàm mũ tương thích.

Khi đó:

1. **Stack moduli log dẫn xuất trơn** đầy đủ là biểu diễn được:
   $$
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}} \in \mathrm{LogDSm}.
   $$
2. Ánh xạ so sánh sang không gian moduli **log tôpô** là một đẳng cấu:
   $$
   (\mathrm{LogDSm}\to\mathrm{LogTop})_*\,
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}}
   \;\simeq\;
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogTop}}.
   $$

![Slide ICM 2026: Log Derived Regularity]({{ site.baseurl }}/img/chapter_img/pardon_log_derived_regularity_icm2026.jpg)

*Hình. Slide trong bài giảng Fields 2026 của John Pardon (ICM 2026), lấy từ reel công khai. Slide ghi **in progress** (đang thực hiện).*

### Cách đọc và ghi chú nguồn

- Định lý này là công trình **đang thực hiện** (*in progress*), trình bày trong bài giảng nhận giải, **không** thay thế nội dung trích dẫn IMU (chu trình ảo, phạm trù Fukaya, tôpô đa tạp 3 chiều).
- **Hình học log** xử lý các biên suy biến kiểu giao cắt chuẩn tắc; **stack dẫn xuất** ghi nhớ cả cấu trúc cản trở bậc cao.

| Mục | Căn cứ |
|----------|------------|
| Sự kiện | Băng rôn sân khấu: ICM 2026 |
| Bối cảnh | Tiêu đề reel: 2026 Fields Medal Lecture — John Pardon |
| Trạng thái định lý | Slide ghi: **in progress** |
| Nguồn | Facebook reel `1666056391140628` (khoảng 24 giây) |
| Lời giảng | Không có phụ đề; nội dung được viết lại từ chữ trên slide |

---


### Video ngắn 2: Phạm trù Fukaya & Tính chính quy Dẫn xuất Loga

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/pardon-fukaya-logderived_vi.mp4"></video>
</div>

Video dài khoảng 36 giây (có thuyết minh tiếng Việt): đa tạp con Lagrangian, đĩa giả chỉnh hình đa giác, đa tạp có góc và cầu nối đối xứng gương đồng điều.

## Nhầm lẫn thường gặp

| Khẳng định | Kết luận | Sửa lại |
|------------|----------|---------|
| "Chu trình ảo chỉ là chi tiết kỹ thuật." | Sai | Đó là ranh giới giữa một số đếm không định nghĩa được và một định lý chặt chẽ. |
| "Phạm trù Fukaya chỉ là một phức xích hình thức." | Sai | Nó ghi lại hình học của đường cong chỉnh hình dưới dạng một phạm trù $$A_\infty$$. |
| "Log Derived Regularity đã là định lý hoàn chỉnh được trao giải." | Sai | Slide ghi rõ **in progress** (đang thực hiện). |
| "Reel trên Facebook là toàn bộ bài giảng." | Sai | Đó là đoạn clip ngắn khoảng 24 giây, chỉ có một slide. |
| "Hình học symplectic chỉ là cơ học Hamilton cổ điển." | Sai | Cơ học là xuất phát điểm; bất biến từ đường cong chỉnh hình và phạm trù Fukaya là cấu trúc toàn cục. |
| "Mọi đa tạp con có một nửa số chiều đều là Lagrange." | Sai | Cần thêm điều kiện $$\omega\vert_L=0$$ (và thường cần thêm dữ liệu phân bậc/spin). |

---

## Nguồn video và tài liệu đọc

Chi tiết: `research/video-research/Pardon_Symplectic/`.

**Thứ tự xem gợi ý**

1. Bài của Quanta về giải Fields 2026: [link](https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/).  
2. Lời trích dẫn của IMU (PDF): [link](https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf).  
3. Reel ICM: [Facebook](https://www.facebook.com/reel/1666056391140628).

**Ghi nhớ:** Chu trình ảo là nền tảng để đếm đường cong khi điều kiện hoành không thỏa.

---

## Tài liệu tham khảo


Danh mục URL đầy đủ (gồm mọi link dùng khi tìm video): `research/video-research/Pardon_Symplectic/references.md`.

### Danh sách URL đầy đủ

1. https://www.facebook.com/reel/1666056391140628  
2. https://www.math.stonybrook.edu/~jpardon/  
3. https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/  
4. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026  
5. https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf  
6. https://news.stonybrook.edu/university/john-pardon-wins-2026-fields-medal-for-outstanding-mathematical-achievement/  
7. https://www.claymath.org/news/2026-fields-medals/  
8. https://www.princeton.edu/news/2026/07/23/princeton-alumni-awarded-three-four-2026-fields-medals-math  
9. https://en.wikipedia.org/wiki/John_Pardon  
10. https://arxiv.org/search/?query=Pardon+virtual+fundamental&searchtype=all  
11. https://en.wikipedia.org/wiki/Symplectic_geometry  
12. https://en.wikipedia.org/wiki/Fukaya_category  
13. https://scgp.stonybrook.edu/  

### Gói nghiên cứu

14. Gói khóa học: `research/video-research/Pardon_Symplectic/`.

1. IMU, Huy chương Fields 2026, John Pardon (trích dẫn chính thức).
2. Các bài báo chọn lọc của Pardon về chu trình ảo và tôpô symplectic.
3. Tài liệu nền: D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*; các bài tổng quan về Floer/Fukaya.
4. Thông cáo của trường và của Simons Center (2026).
5. **Video nguồn (reel ICM 2026):** [2026 Fields Medal Lecture: John Pardon](https://www.facebook.com/reel/1666056391140628). Slide về logarithmic derived regularity (truy cập 2026-08-03). Nội dung được viết lại từ hình ảnh; reel không có phụ đề chính thức.
6. Trong khóa học: [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Tìm hiểu **đối xứng gương** như một nơi dùng đến phạm trù Fukaya (ở mức ý tưởng: giả thuyết đối xứng gương đồng điều do Kontsevich đề xuất).
- So sánh các huy chương cho nền tảng (Pardon, Scholze) với các huy chương cho một giả thuyết dễ phát biểu (Perelman, Viazovska). Kiểu đóng góp khác nhau nhưng cùng một tiêu chuẩn của IMU.
- Học trước các thuật ngữ về **hình học log** và **stack dẫn xuất** trước khi đọc các bài báo nghiên cứu về không gian moduli.
- Nếu có video đầy đủ của bài giảng ICM, chia nó thành nhiều phần theo chủ đề (chu trình ảo; phạm trù Fukaya; đa tạp 3 chiều; log dẫn xuất).

## Video tham khảo

- **Xem trước** — [2026 Fields Medal: John Pardon](https://www.youtube.com/watch?v=E4KP07YL0Js) — Simons Foundation, tiếng Anh. Video giới thiệu ngắn về John Pardon và công trình được trao giải. Nên xem trước khi đọc bài.
- [ICM 2026 Fields Medal Award Lecture - John Pardon](https://www.youtube.com/watch?v=YZ7hKBlCeGs) — Simons Foundation, tiếng Anh. Bài giảng nhận giải tại ICM 2026, có phần về tính chính quy dẫn xuất loga ở mục 5. Nên xem sau khi đọc xong bài.
- [Contact homology and virtual fundamental cycles - John Pardon](https://www.youtube.com/watch?v=Eh8Hrg1mQVk) — Institute for Advanced Study, tiếng Anh. Bài giảng chuyên sâu của Pardon về đồng điều tiếp xúc và chu trình cơ bản ảo, liên quan trực tiếp đến mục 2. Dành cho người muốn đi sâu về kỹ thuật.
