---
layout: post
title: "Làm sao xếp cầu hiệu quả nhất?"
chapter: '07'
order: 3
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Lộ trình xếp cầu**  
> **Đọc sâu:** [Viazovska Ch.2]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/)  
> **Bạn đang ở đây:** Studio Ch.7 (thí nghiệm + log)  
> *Tùy chọn:* kissing number, lattice vs nonlattice, kỳ lạ chiều cao.

Studio hỏi câu mang vẻ vật lý: cách xếp các quả cầu bằng nhau không chồng lấn trong $$\mathbb{R}^n$$ dày đặc nhất là gì? Mặt phẳng có thể quyết bằng đồng xu. Ba chiều: giả thuyết Kepler chờ hàng thế kỷ. Chiều 8 và 24: modular forms và Fourier quyết định tối ưu. Hầu hết chiều vẫn mở.

Bạn không dựng “magic function” của Viazovska. Bạn **định nghĩa mật độ**, **đo packing thật**, **so sánh ứng viên**, và phân biệt định lý sắc trong chiều đặc biệt với heuristic/cận số ở nơi khác. Cùng kỷ luật nhãn như studio Kakeya: conjecture, construction, quan sát, định lý—không trộn.

---

## Mục tiêu học tập

Sau studio bạn cần:

- Định nghĩa mật độ packing như giới hạn tỉ lệ thể tích phủ; tính đúng packing lưới vuông và lục giác 2D.
- Giải thích kissing number; nêu giá trị cổ điển 2D/3D và bước nhảy chiều cao.
- Phân biệt packing **lattice** và packing tổng quát; vì sao nonlattice đôi khi có thể thắng.
- Tóm tắt bảng: hex (2), Kepler/Hales (3), $$E_8$$ (8), Leech (24), generic mở.
- Thiết kế ≥2 thí nghiệm + log có nhãn conjecture/quan sát.
- Nêu ý Cohn–Elkies ở mức slogan: cận trên qua hàm radial và biến đổi Fourier.

**Tiên quyết.** Diện tích/thể tích quả cầu; vector 2D/3D; lattice như nhóm con rời rạc sinh không gian.

---

## 1. Toán nền

### 1.1 Mật độ

Cố định chiều $$n$$ và xếp các quả cầu đóng bán kính bằng nhau, không chồng lấn trong $$\mathbb{R}^n$$. Một định nghĩa chuẩn của **mật độ** là

$$
\delta=\limsup_{R\to\infty}\frac{\text{thể tích cầu trong }B(0,R)}{\operatorname{Vol} B(0,R)}.
$$

Với **packing lattice** có tâm tại $$\Lambda$$ và khoảng cách khác không tối thiểu $$2r$$ (cầu bán kính $$r$$ vừa chạm):

$$
\delta(\Lambda)=\frac{\operatorname{Vol}(B(0,r))}{\operatorname{Vol}(\mathbb{R}^n/\Lambda)}.
$$

**Câu hỏi.** $$\delta_n=\sup$$ mật độ trên mọi packing trong chiều $$n$$ là bao nhiêu? Cấu hình nào đạt?

Hiệu ứng biên quan trọng: nếu chỉ đếm “bao nhiêu quả trong hộp”, phần mép làm lệch. Định nghĩa giới hạn tồn tại đúng vì lý do đó. Trong thí nghiệm xu, hãy dùng vùng nội tiếp lớn để giảm bias.

### 1.2 Hai chiều: vuông vs lục giác

Xếp đồng xu trên bàn.

- **Lưới vuông.** Tâm tại $$(2r\,i,\,2r\,j)$$. Mỗi quả chiếm hình vuông cạnh $$2r$$, nên

$$
\delta_{\square}=\frac{\pi r^2}{4r^2}=\frac{\pi}{4}\approx 0.785.
$$

- **Lưới lục giác.** Mỗi tâm có sáu láng giềng khoảng cách $$2r$$. Cell cơ bản chuẩn cho

$$
\delta_{\mathrm{hex}}=\frac{\pi}{2\sqrt{3}}\approx 0.907.
$$

Packing lục giác tối ưu trong mặt phẳng (cổ điển). Thí nghiệm đầu tiên nên **cảm** khoảng cách 0.78 so 0.91 trước khi trích định lý.

### 1.3 Ba chiều và kissing

**Giả thuyết Kepler** khẳng định không packing nào trong $$\mathbb{R}^3$$ vượt mật độ FCC/HCP

$$
\delta_{\mathrm{FCC}}=\frac{\pi}{3\sqrt{2}}\approx 0.74048.
$$

**Thomas Hales** chứng minh (hỗ trợ máy đáng kể); kết quả đã formalize trong proof assistant. **Kissing number** 3D = 12: một quả trung tâm chạm tối đa mười hai quả bằng nhau (có “wiggle room” gây nhầm lịch sử—icosahedron một mình không “hiển nhiên” quyết).

### 1.4 Chiều đặc biệt 8 và 24

| $$n$$ | Packing tối ưu (trạng thái) |
|-------|------------------------------|
| 1 | Đoạn trên đường (tầm thường) |
| 2 | Lưới lục giác — cổ điển |
| 3 | Mật độ FCC/HCP — Hales |
| 8 | $$E_8$$ — **Viazovska (2016)** |
| 24 | Leech — **Cohn–Kumar–Miller–Radchenko–Viazovska** |
| generic | Chủ yếu mở; có cận tiệm cận |

Lưới $$E_8$$ và Leech là kỳ quan đối xứng: vỏ vector tối thiểu cực dày và nhóm tự đẳng cấu giàu. Viazovska dựng hàm radial “magic” có mẫu dấu Fourier khớp đúng cận lập trình tuyến tính Cohn–Elkies ở chiều 8, chứng minh $$E_8$$ tối ưu trong **mọi** packing (không chỉ lattice).

### 1.5 Cohn–Elkies trong một đoạn

Đại khái: nếu hàm radial Schwartz $$f$$ trên $$\mathbb{R}^n$$ thỏa $$f(x)\le 0$$ khi $$\lvert x\rvert\ge 1$$ và $$\hat f(\xi)\ge 0$$ mọi $$\xi$$, với $$f(0)$$ và $$\hat f(0)$$ dương, thì mật độ packing bị chặn trên bởi hằng số xây từ $$f(0)/\hat f(0)$$ (sau scale). Công thức Poisson là cầu: nối giá trị $$f$$ trên lattice với $$\hat f$$ trên dual lattice, biến ràng buộc hình học không chồng thành ràng buộc dấu giải tích. Sắc cần hàm “chạm” ràng buộc tương thích tập khoảng cách lattice—triệt tiêu ở bán kính đúng. Modular forms cung cấp hàm như vậy ở chiều 8 và 24. Bạn không cần dựng $$f$$; bạn cần hiểu **packing trở thành thiết kế hàm**—vì sao Fields có thể trao cho việc dựng hàm phụ trợ đúng chứ không phải xếp thêm cam.

### 1.6 Kỳ lạ chiều cao

Thể tích quả cầu đơn vị

$$
V_n=\frac{\pi^{n/2}}{\Gamma(n/2+1)}
$$

tăng rồi $$\to 0$$ khi $$n\to\infty$$. Hầu hết thể tích khối cao chiều nằm gần biên; cầu trở nên kém lấp không gian trong tọa độ ngây thơ. Packing tốt nhất, kissing, và khoảng cách lattice/nonlattice hành xử không đều. Nối studio [chiều thứ tư]({{ site.baseurl }}/contents/vi/chapter07/07_06_Explore_Fourth_Dimension/) nếu thích nghịch lý thể tích.

---

## 2. Conjecture / chứng minh / thí nghiệm

| Nhãn | Nghĩa | Ví dụ |
|------|-------|-------|
| **Định lý** | Đã chốt | Hex 2D; $$E_8$$; Leech |
| **Mở** | Chưa biết tối ưu chính xác | Hầu hết $$n\notin\{1,2,3,8,24\}$$ |
| **Cận dưới** | Packing tường minh | Xu của bạn; bảng lattice |
| **Cận trên** | Analytic/LP | Cohn–Elkies số |

**Tiêu chí thành công (ghi trong đề xuất):**

1. Đo mật độ ≥2 packing 2D (vuông và hex) sai số <2% so công thức.  
2. Một artifact: ảnh xu, sơ đồ, hoặc mô phỏng.  
3. Bảng trạng thái $$n=2,3,8,24$$ và “generic $$n$$”.  
4. Một đoạn Cohn–Elkies/magic không nhận đã dựng $$f$$.  
5. Một hiểu nhầm đã sửa (ví dụ “12 kissing hiển nhiên từ icosahedron”).

---

## 3. Chuẩn log

**Ngày · Ý định · Hành động · Kết quả · Nhãn · Diễn giải · Tiếp.**

Ghi đường kính xu, spacing lưới, tham số code. Packing thất bại—chồng phải tháo—thuộc log.

**AI.** Được hỗ trợ code nếu disclose; mật độ *bạn* đo phải tái lập được từ ghi chú.

---

## 4. Thí nghiệm

Làm ≥2 trong A–E.

### A — Xếp xu (25–40′)

Xếp xu bằng nhau trong khay chữ nhật (hoặc giấy vẽ vòng).

1. Ép lưới vuông; ước mật độ = (số xu × diện tích xu) / diện tích khay (vùng nội tiếp giảm biên).  
2. Ép pattern lục giác; ước mật độ.  
3. So $$\pi/4$$ và $$\pi/(2\sqrt{3})$$.

**Giả thuyết trước đo:** “Hiệu ứng biên chi phối; tôi không thấy khoảng 0.78 vs 0.91.” Rồi kiểm vùng đủ lớn có lộ không.

**Tiêu chí:** hai ước lượng + % sai so công thức.

### B — Kissing 2D/3D (20–40′)

- 2D: 6 vòng chạm trung tâm; 7 không (góc $$60^\circ$$).  
- 3D: thử 12 (bóng, cam, hoặc phác); viết vì sao “rattle” gây nhầm lịch sử. Tra kissing $$n=4,8,24$$ **có trích dẫn**—không bịa.

**Tiêu chí:** phác chứng 2D + tường thuật 3D + bảng cao chiều có nguồn.

### C — Máy tính mật độ lattice (30–60′)

Code: vector sinh 2D + khoảng cách tối thiểu → mật độ; kiểm vuông/hex. Tùy chọn: quét góc/tỉ lệ và vẽ landscape mật độ.

**Tiêu chí:** code + hex thắng vuông; contour tùy chọn.

### D — Thông cáo trạng thái (20–30′)

Sau khi đọc Ch.2 Viazovska (hoặc bảng trạng thái):

- Trước 2016 biết gì?  
- Viazovska solo chứng minh gì ($$E_8$$)?  
- Cộng tác chiều 24 ra sao?  
- Còn mở gì?

**Tiêu chí:** không trộn solo $$E_8$$ với Leech cộng tác; slogan mật độ đúng.

### E — Thể tích và “lãng phí” (mở rộng)

Bảng/plot $$V_n$$ cho $$n=1..20$$; nối trực giác packing: nếu cầu có thể tích nhỏ so khối, mật độ nên hành xử thế nào? So intuition với bảng cận tin cậy (trích dẫn).

**Tiêu chí:** bảng/plot + hai câu nối suy giảm thể tích với độ khó packing.

---

## 5. Nhầm lẫn thường gặp

1. Hex chỉ tối ưu địa phương — trong 2D là tối ưu toàn cục trong mọi packing.  
2. Viazovska giải mọi chiều — 8 và (đồng tác giả) 24; không phải mọi $$n$$.  
3. Lattice luôn thắng — không biết tổng quát; một số chiều có thể ưa nonlattice.  
4. Kissing = số phối trí packing dày nhất — liên quan, không tự động.  
5. Mật độ = “bao nhiêu quả trong hộp” — hiệu ứng biên quan trọng; định nghĩa giới hạn có lý do.

---

## 6. Bài tập

1. Suy ra $$\delta_{\square}=\pi/4$$ từ nguyên lý đầu.  
2. Giải thích $$\delta_{\mathrm{hex}}=\pi/(2\sqrt{3})$$ với cell cơ bản rõ.  
3. Scale mọi độ dài bởi $$\lambda>0$$ không đổi mật độ — vì sao quan trọng cho định nghĩa?  
4. Fourier cận trên loại packing dày hơn lattice thế nào (lời mình), dù không liệt kê mọi packing.  
5. Đề xuất ≤200 từ: câu hỏi, phương pháp, tiêu chí, rủi ro (biên, đơn vị, bug phần mềm).

---

## 7. Rubric

| ☐ | Mật độ vuông + hex (xu hoặc mô phỏng) |
| ☐ | Định nghĩa mật độ bằng lời mình |
| ☐ | Bảng 2, 3, 8, 24 + generic |
| ☐ | Một câu magic/Cohn–Elkies |
| ☐ | Log ≥3 mục có ngày |
| ☐ | Câu hỏi mở (ví dụ một $$n$$ cụ thể) |

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/explore-sphere-packing/`.

**Khẩu hiệu từ gói nghiên cứu**

- **Mật độ** là giới hạn tỉ lệ thể tích; hiệu ứng biên quan trọng trong hộp hữu hạn.
- Xếp lục giác tối ưu 2D; Kepler 3D (Hales); **Viazovska** cho chiều 8 và 24.
- Chặn Fourier/LP (Cohn–Elkies) loại packing dày hơn mà không liệt kê hết.
- Studio: đo cẩn thận; tách định lý / conjecture / quan sát số.

**Thứ tự xem gợi ý**

1. **CORE** — Viazovska — Einstein Lectures sphere packing: [https://www.youtube.com/watch?v=fH6KNlUJux0](https://www.youtube.com/watch?v=fH6KNlUJux0).  
2. **CORE** — Viazovska — Sphere packing intro (ICMU): [https://www.youtube.com/watch?v=VR3Ezxo5wo8](https://www.youtube.com/watch?v=VR3Ezxo5wo8).  
3. **RESEARCH** — Viazovska — Simons Lecture Day 1 (MIT): [https://www.youtube.com/watch?v=mf_XOB7594c](https://www.youtube.com/watch?v=mf_XOB7594c).  
4. **INTUITION** — Numberphile — Best Way to Pack Spheres: [https://www.youtube.com/watch?v=mceaM2_zQd8](https://www.youtube.com/watch?v=mceaM2_zQd8).  

**Cổng chính thức / tài liệu**

- Viazovska E8 packing (arXiv:1603.04246): https://arxiv.org/abs/1603.04246  
- Cohn et al. dimension 24 (arXiv:1603.06518): https://arxiv.org/abs/1603.06518  
- Cohn–Elkies LP bounds (arXiv survey lineage): https://arxiv.org/abs/math/0110009  

Danh mục URL đầy đủ: `research/video-research/explore-sphere-packing/references.md`.

## 8. Tài liệu


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/explore-sphere-packing/references.md`.

1. Viazovska — Einstein Lectures sphere packing — https://www.youtube.com/watch?v=fH6KNlUJux0  
2. Viazovska — Sphere packing intro (ICMU) — https://www.youtube.com/watch?v=VR3Ezxo5wo8  
3. Viazovska — Simons Lecture Day 1 (MIT) — https://www.youtube.com/watch?v=mf_XOB7594c  
4. Numberphile — Best Way to Pack Spheres — https://www.youtube.com/watch?v=mceaM2_zQd8  
5. Viazovska E8 packing (arXiv:1603.04246) — https://arxiv.org/abs/1603.04246  
6. Cohn et al. dimension 24 (arXiv:1603.06518) — https://arxiv.org/abs/1603.06518  
7. Cohn–Elkies LP bounds (arXiv survey lineage) — https://arxiv.org/abs/math/0110009  
8. Quanta — Sphere packing higher dimensions — https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/  
9. Quanta — Viazovska Fields profile — https://www.quantamagazine.org/ukrainian-mathematician-maryna-viazovska-wins-fields-medal-20220705/  
10. Wikipedia — Sphere packing — https://en.wikipedia.org/wiki/Sphere_packing  
11. Simons Foundation Fields video page (Viazovska) — https://www.simonsfoundation.org/2022/07/05/fields-medal-video-maryna-viazovska/  
12. Thư mục gói: `research/video-research/explore-sphere-packing/`.

1. [Viazovska Ch.2]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).  
2. Conway–Sloane, *Sphere Packings, Lattices and Groups* (cẩm nang cổ điển).  
3. Cohn–Elkies LP bounds; Viazovska 2016 $$E_8$$.  
4. Studio: [Kakeya]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/), [chiều 4]({{ site.baseurl }}/contents/vi/chapter07/07_06_Explore_Fourth_Dimension/).

---

## Hướng đi tiếp

Nếu công thức mật độ dễ mà cận Fourier mờ, đọc lại đoạn Cohn–Elkies Ch.2 và viết lại thành năm câu cho bạn chỉ biết tích phân. Nếu thích hình học rời rạc hơn phân tích, xoay thí nghiệm sang kissing và root lattices. Nối [chiều thứ tư]({{ site.baseurl }}/contents/vi/chapter07/07_06_Explore_Fourth_Dimension/) khi $$V_n\to 0$$ làm bạn tò mò về “không gian nhọn”.

**Gợi ý tổng hợp một trang.** (i) mật độ vuông và hex bạn đo được bao nhiêu; (ii) định nghĩa giới hạn tránh biên thế nào; (iii) bảng 2/3/8/24; (iv) packing trở thành thiết kế hàm nghĩa là gì; (v) một $$n$$ bạn muốn hỏi tiếp.

### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/explore-sphere-packing/transcripts/` · trạng thái: `research/video-research/explore-sphere-packing/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/explore-sphere-packing_fH6KNlUJux0_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

