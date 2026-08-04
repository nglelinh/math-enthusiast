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

**John Pardon** (Stony Brook / Simons Center) nhận **Huy chương Fields 2026** nhờ thành tựu hình học symplectic và đóng góp xuyên hình học–tôpô. Nếu nhiều huy chương gắn với *một* định lý khẩu hiệu dễ kể (Poincaré, xếp cầu, bounded gaps), trích dẫn của Pardon nhấn **nền tảng**: làm sao đếm đường cong chỉnh hình và xây bất biến phạm trù khi transversality cổ điển thất bại—và đồng thời tôpô chiều thấp (tác động nhóm trên 3-đa tạp, lý thuyết nút).

**Trích dẫn ngắn IMU:**  
For his achievements in symplectic geometry including new approaches to virtual fundamental cycles, Fukaya categories of certain manifolds and counting holomorphic curves, and for his contributions to other areas of geometry and topology, including group actions on 3-manifolds and knot theory.

Bài này dành cho người học có tôpô vi phân cơ bản và muốn hiểu *vì sao* “đếm đường cong” lại cần công nghệ ảo, *Fukaya category* là bất biến kiểu gì, và *làm sao* đọc slide ICM 2026 về log derived regularity mà không nhầm với trích dẫn giải thưởng đã hoàn tất.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu hình học symplectic nghiên cứu gì: 2-dạng đóng không suy biến; động lực Hamilton; đường cong chỉnh hình như đầu dò toàn cục.
- Giải thích vì sao không gian moduli đường cong **thường** không phải đa tạp trơn chiều kỳ vọng, và vì sao cần **virtual fundamental cycles**.
- Kể **Fukaya category** như bất biến đồng điều / phạm trù xây từ Lagrangian và đĩa chỉnh hình—trung tâm mirror symmetry.
- Thấy portfolio Pardon trải dài **symplectic** và **tôpô chiều thấp** (group actions, knot theory).
- Đọc định lý **Log Derived Regularity** trên slide ICM như công trình **đang tiến hành**, không thay trích dẫn IMU.
- Tránh nhầm virtual cycles với “sổ sách kỹ thuật vô hại” và nhầm reel Facebook với toàn bộ bài giảng.

**Kiến thức nền.** Đa tạp trơn; dạng vi phân; ý tưởng đồng điều; “moduli = không gian tham số hóa đối tượng”.

**Liên kết seminar.** So “medal nền tảng” (Pardon, [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/)) với “medal một giả thuyết khẩu hiệu”. Ghép [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) về moduli theo nghĩa khác (bề mặt Riemann / không gian moduli đo được).

---

## 1. Hình học symplectic một trang

Một **đa tạp symplectic** $$(M,\omega)$$ mang một 2-dạng $$\omega$$ thỏa:

1. **Đóng:** $$d\omega=0$$;  
2. **Không suy biến:** tại mỗi điểm, $$\omega_p$$ là dạng song tuyến tính không suy biến trên $$T_pM$$ (kéo theo chiều chẵn).

**Ví dụ gốc.** Không gian cotangent $$T^*Q$$ với dạng Liouville–canonical; không gian Euclid chẵn với dạng chuẩn. Cơ học Hamilton sống tự nhiên trên symplectic manifold: hàm Hamilton $$H$$ sinh trường vector $$X_H$$ bởi

$$
\iota_{X_H}\omega = dH,
$$

và flow của $$X_H$$ bảo toàn $$\omega$$ (định lý Liouville hình học).

**Gần như phức.** Thường chọn almost complex structure $$J$$ tương thích với $$\omega$$ để nói về **đường cong chỉnh hình**: ánh xạ $$u:(\Sigma,j)\to(M,J)$$ thỏa phương trình Cauchy–Riemann

$$
du\circ j = J\circ du.
$$

Từ Gromov trở đi, đường cong chỉnh hình (và biến thể Floer) trở thành **đầu dò tôpô symplectic toàn cục**: chúng “thấy” các ràng buộc mà mô tả địa phương bằng tọa độ Darboux không thấy—vì mọi symplectic manifold đều trông giống nhau locally.

**Khẩu hiệu.** Symplectic geometry = hình học của diện tích định hướng / form 2 không suy biến + động lực bảo toàn + đường cong chỉnh hình làm bất biến.

---

## 2. Đếm đường cong: khi transversality thất bại

Muốn “đếm” đường cong chỉnh hình với điều kiện biên hoặc đánh dấu, người ta xây **không gian moduli** $$\mathcal{M}$$ các ánh xạ thỏa phương trình Cauchy–Riemann (modulo tự đẳng cấu miền).

Trong thế giới lý tưởng:

- toán tử tuyến tính hóa là Fredholm;
- transversality cho $$\mathcal{M}$$ là đa tạp trơn chiều bằng chỉ số Fredholm;
- compact hóa tốt cho phép lấy **lớp cơ bản** $$[\mathcal{M}]\in H_*(\overline{\mathcal{M}})$$ và tích phân / đếm.

**Thực tế.** Với almost complex structure tổng quát, transversality có thể đạt trong một số thiết lập—nhưng trên nhiều đa tạp thú vị, với điều kiện biên Lagrangian, với multiple covers, với degenerations, không gian moduli **không** phải đa tạp trơn chiều kỳ vọng. Có orbifold singularities, components chiều sai, và obstruction bundles.

Nếu không có lớp cơ bản đáng tin, “số đếm Gromov–Witten / Floer” có thể **không định nghĩa được** một cách nhất quán.

### 2.1. Virtual fundamental cycles

**Chu kỳ / lớp cơ bản ảo** (virtual fundamental class/cycle) cung cấp một lớp đồng điều (hoặc chuỗi) thay thế, sống trên compact hóa moduli, sao cho vẫn có thể tích phân và đếm *như thể* transversality đã đạt—miễn hệ thống perturbation / Kuranishi / polyfold / derived geometry được thiết lập đúng.

Đây không phải trang trí: là **ranh giới giữa định lý và khẩu hiệu**. Nhiều bất biến “tồn tại trên slide” chỉ trở thành toán học khi virtual technique đứng vững.

**Đóng góp được trích dẫn của Pardon.** Các tiếp cận mới cho virtual fundamental cycles và việc đếm đường cong chỉnh hình trong các thiết lập khó—làm nền cho bất biến đáng tin.

---

## 3. Fukaya category: Lagrangian thành bất biến phạm trù

**Dưới-đa tạp Lagrangian** $$L\subset(M,\omega)$$ có chiều một nửa $$\dim M$$ và $$\omega|_L=0$$. Trong cơ học, chúng liên quan điều kiện biên và điều kiện ban đầu “nửa chiều”; trong mirror symmetry, chúng là đối tượng bên A-model.

**Fukaya category** (và biến thể) tổ chức:

- đối tượng ≈ Lagrangian (với dữ liệu grading, spin, perturbation…);
- morphisms ≈ phức Floer từ giao điểm Lagrangian (hoặc đường cong với biên trên Lagrangian);
- composition ≈ đếm đĩa chỉnh hình có biên trên các Lagrangian liên quan.

Kết quả là một **bất biến phạm trù** (thường $$A_\infty$$) của đa tạp symplectic—mạnh hơn một nhóm đồng điều đơn lẻ, vì mã hóa cách các Lagrangian giao và bị đường cong “ràng buộc” lẫn nhau.

**Mirror symmetry (khẩu hiệu người dùng).** Bên B-model: đa tạp phức / hạng mục kết hợp. Bên A-model: Fukaya. Tương đương đồng điều dự đoán cầu nối sâu giữa hình học phức và symplectic.

**Điểm Fields.** Xây Fukaya category **nghiêm ngặt** trên các đa tạp thú vị (không chỉ ví dụ đồ chơi) đòi hỏi đúng những nền tảng virtual / compactness / transversality ở trên. Trích dẫn IMU nêu rõ Fukaya categories of certain manifolds—không phải khẩu hiệu chung chung.

---

## 4. Tôpô chiều thấp: group actions và knot theory

Trích dẫn không dừng ở symplectic. Pardon còn được ghi nhận vì đóng góp **tác động nhóm trên 3-đa tạp** và **lý thuyết nút**. Đây là tín hiệu portfolio: cùng một nhà toán học có thể mang trực giác tôpô hình học cổ điển (phân tích tác động, cấu trúc 3-manifold, nút) vào và ra khỏi thế giới đường cong chỉnh hình.

Với người học: đừng đóng khung “Fields symplectic = chỉ GW invariants”. Hãy đọc trích dẫn đủ hai nửa.

---

## 5. Bài giảng Fields ICM 2026: log derived regularity (đang tiến hành)

Tại **ICM 2026** (Philadelphia), bài giảng Fields của Pardon gồm công trình moduli nâng cao vượt các mục headline trong trích dẫn IMU ngắn. Một reel công khai cho thấy slide cuối (19/19) mang tiêu đề **Logarithmic derived regularity**.

### Định lý (Log Derived Regularity Theorem; in progress)

*Tái dựng từ slide bài giảng (không phải transcript miệng đầy đủ).*

Cho

$$
W \xrightarrow{\mathrm{strict}} C \xrightarrow{\mathrm{exact}} B
$$

là một **bài toán section elliptic** trên đa tạp **log smooth** $$B$$. Giả sử $$C\to B$$ proper và depth one, và giả sử **đầu mút non-degenerate** hoặc **Morse–Bott** với cấu trúc suy giảm mũ tương thích.

Khi đó:

1. **Stack moduli log derived smooth** đầy đủ là representable:
   $$
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}} \in \mathrm{LogDSm}.
   $$
2. Ánh xạ so sánh sang moduli **log topological** là đẳng cấu:
   $$
   (\mathrm{LogDSm}\to\mathrm{LogTop})_*\,
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}}
   \;\simeq\;
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogTop}}.
   $$

![Slide ICM 2026: Log Derived Regularity]({{ site.baseurl }}/img/chapter_img/pardon_log_derived_regularity_icm2026.jpg)

*Hình. Slide bài giảng Fields 2026 của John Pardon (ICM 2026), từ reel công khai — slide ghi **in progress**.*

### Cách đọc trong khóa học

- **Không** thay trích dẫn IMU (virtual cycles, Fukaya, tôpô 3-đa tạp). Đây là công trình **đang tiến hành / nâng cao** trình bày trên bục giải thưởng.
- Chủ đề nối tiếp: cả công trình Fields và định lý này đều về **moduli ánh xạ/section** khi smoothness và transversality cổ điển thất bại—ở đây trong bối cảnh **log + derived**.
- Từ vựng chạm:
  - **Log smooth / log geometry:** compact hóa và degeneration với cấu trúc kiểu normal crossings được kiểm soát.
  - **Derived moduli:** stack nhớ obstruction theory bậc cao, không chỉ scheme/orbifold cổ điển.
  - **Representability trong LogDSm:** đối tượng moduli là đối tượng hình học hợp lệ trong phạm trù log derived smooth.
  - **So sánh LogTop:** moduli giải tích/tôpô khớp mô tả derived-smooth dưới giả thuyết đầu mút.

### Ghi chú độ chính xác từ video nguồn

| Hạng mục | Bằng chứng |
|----------|------------|
| Sự kiện | Banner sân khấu: ICM 2026 |
| Bối cảnh | Tiêu đề reel: 2026 Fields Medal Lecture — John Pardon |
| Trạng thái định lý | Slide: **in progress** |
| Nguồn | Facebook reel `1666056391140628` (~24 giây) |
| Transcript miệng | Không có caption; tái dựng từ chữ trên slide |

---

## 6. Vì sao quan trọng

**Nền tảng tôpô symplectic.** Không có virtual cycles và xây dựng Fukaya đáng tin, nhiều “định lý đếm” chỉ là phác thảo. Pardon được thưởng ở tầng *làm cho máy chạy được*.

**Cầu phạm trù–hình học.** Fukaya không phải phức xích trang trí: nó mã hóa hình học đường cong thành ngôn ngữ mirror và đồng điều hiện đại.

**Bề rộng.** Group actions và knot theory nhắc rằng hình học chiều thấp cổ điển vẫn sống song song—và cùng một sự nghiệp có thể nối hai thế giới.

**Bài học ICM.** Ngay trên bục Fields, nhà toán học vẫn đẩy **nền tảng moduli** (log/derived regularity). Giải thưởng không đóng chương nghiên cứu; đôi khi nó chiếu sáng biên giới *đang viết*.

**Giới hạn sư phạm.** Bài này không dạy đủ polyfold hay Kuranishi để bạn chứng minh lemma virtual. Nó dạy *vì sao* các từ đó xuất hiện và *cách* đọc trích dẫn / slide mà không phóng đại.

---

## Nhầm lẫn phổ biến

| Khẳng định | Kết luận | Sửa |
|------------|----------|-----|
| “Virtual cycles chỉ là sổ sách kỹ thuật.” | Sai | Là khác biệt giữa đếm không định nghĩa được và định lý. |
| “Fukaya chỉ là phức xích dạng.” | Sai | Mã hóa hình học đường cong chỉnh hình theo phạm trù $$A_\infty$$. |
| “Log Derived Regularity đã là định lý giải thưởng hoàn tất trên slide.” | Sai | Slide ghi **in progress**. |
| “Reel Facebook là toàn bộ bài giảng.” | Sai | Clip ngắn ~24 giây, một slide. |
| “Symplectic = chỉ cơ học Hamilton cổ điển.” | Sai | Cơ học là gốc; bất biến đường cong và Fukaya là tầng toàn cục. |
| “Lagrangian = mọi dưới-đa tạp nửa chiều.” | Sai | Cần $$\omega|_L=0$$ (và thường thêm dữ liệu). |

---

## Bài tập

1. Không suy biến của 2-dạng nghĩa tuyến tính là gì? Viết điều kiện trên không gian vector và suy ra chiều chẵn.
2. Vì sao moduli “thường” thất bại transversality? Nêu ít nhất hai hiện tượng (multiple cover, obstruction, điều kiện biên…).
3. Dưới-đa tạp Lagrangian, khẩu hiệu? Một câu có $$\omega$$ và một câu không ký hiệu.
4. Hai chủ đề **không** symplectic thuần trong trích dẫn Pardon?
5. Lướt survey Fukaya / Floer; liệt kê ba tiên quyết bạn chưa có.
6. **Từ slide ICM:** Tách (a) giả thuyết về $$W\to C\to B$$ và (b) hai kết luận (representability; đẳng cấu so sánh).
7. **Research literacy:** Vì sao hình học “log” xuất hiện khi nghiên cứu moduli gần degeneration / strata biên?
8. **So sánh medal.** Một giống giữa Pardon và Scholze ở mức “nền tảng ngôn ngữ”, không đồng nhất lĩnh vực.

---


## Nguồn video (gói math-video-researcher)

Chi tiết: `research/video-research/Pardon_Symplectic/`.

**Thứ tự xem gợi ý**

1. Quanta Fields 2026: [link](https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/).  
2. IMU citation PDF: [link](https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf).  
3. ICM reel: [Facebook](https://www.facebook.com/reel/1666056391140628).

**Nhắc:** Virtual cycles = nền tảng đếm đường cong khi thiếu transversality.

---

## Tài liệu tham khảo


Danh mục URL đầy đủ (mọi link khi nghiên cứu video): `research/video-research/Pardon_Symplectic/references.md`.

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

1. IMU Fields Medal 2026 — John Pardon (trích dẫn chính thức).
2. Bài chọn lọc của Pardon về virtual cycles / symplectic topology.
3. Nền: D. McDuff, D. Salamon — *J-holomorphic Curves and Symplectic Topology*; survey Floer/Fukaya.
4. Thông cáo trường / Simons Center (2026).
5. **Video nguồn (reel ICM 2026):** [2026 Fields Medal Lecture: John Pardon](https://www.facebook.com/reel/1666056391140628) — slide logarithmic derived regularity (truy cập 2026-08-03). Tái dựng hình ảnh; reel không có caption chính thức.
6. Khóa học: [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Khám phá **mirror symmetry** như “người dùng” Fukaya category (Khovanov, Homological mirror conjecture ở mức khẩu hiệu).
- So medal nền tảng (Pardon, Scholze) với medal một giả thuyết dễ kể (Perelman, Viazovska) — khác kiểu đóng góp, cùng chuẩn IMU.
- Học từ vựng **log geometry** / **derived stacks** trước khi đọc paper nghiên cứu moduli.
- Nếu có video bài giảng ICM đầy đủ, chạy lại phân đoạn nhiều unit (virtual cycles; Fukaya; 3-manifolds; log derived).
