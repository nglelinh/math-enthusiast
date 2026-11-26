---
layout: post
title: "Jacob Tsimerman: O-Minimality và Hình học Số học (Huy chương Fields 2026)"
chapter: '02'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Nếu bạn hỏi một nhà hình học số học từ thập niên 1980 rằng *logic toán học* có giúp giải được các giả thuyết lớn về phương trình Diophantine hay đa tạp Shimura không, có lẽ họ sẽ mỉm cười lắc đầu. Logic và lý thuyết mô hình từ lâu được coi là một ngành nghiên cứu nền tảng trừu tượng, tách biệt hẳn với thế giới của đường cong elliptic và lý thuyết Hodge.

Vậy mà trong hai thập kỷ gần đây, một khái niệm bắt nguồn từ logic toán — **tính o-tối tiểu** (*o-minimality*, hay "hình học thuần") — đã bất ngờ trở thành một trong những chiếc chìa khóa vạn năng mạnh nhất của hình học số học hiện đại! **Jacob Tsimerman** (Đại học Toronto) nhận **Huy chương Fields 2026** chính vì vai trò trung tâm trong cuộc cách mạng đó: biến tính o-tối tiểu thành phương pháp nền tảng của hình học số học và hình học đại số phức, đồng thời cùng các cộng sự chinh phục hai giả thuyết biểu tượng là **giả thuyết André–Oort** (cho đa tạp modular Siegel, rồi mở rộng ra toàn bộ đa tạp Shimura) và **giả thuyết Griffiths** về tính đại số của ảnh ánh xạ chu kỳ.

**Trích dẫn ngắn của IMU:**  
For his contribution in the recasting of o-minimality as a fundamental method of arithmetic and complex algebraic geometry, and his role in the proof of many central conjectures including Griffiths’ conjecture on the algebraicity of images of the period maps, and the André–Oort conjecture for Siegel modular varieties.

*Tạm dịch:* Cho đóng góp trong việc đặt lại tính o-tối tiểu thành một phương pháp cơ bản của hình học số học và hình học đại số phức, và cho vai trò của ông trong việc chứng minh nhiều giả thuyết trung tâm, gồm giả thuyết Griffiths về tính đại số của ảnh các ánh xạ chu kỳ và giả thuyết André–Oort cho các đa tạp modular Siegel.

**Mạch bài học:** Kiến thức cần nhớ (tính tay "thuần" vs "hoang" qua $$\sin x$$, kiểm tra điểm CM trên lưới vuông $$\mathbb{Z}[i]$$ và đếm điểm hữu tỷ trên $$y = 2^x$$) → Đa tạp Shimura & giao không điển hình → Giải thích 4 bước: Pila–Zannier, đột phá Tsimerman cho André–Oort và Giả thuyết Griffiths → So sánh các cầu nối số học–giải tích.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt trực giác **hình học "thuần" (o-tối tiểu)** và **hình học "hoang"** qua ví dụ $$\sin(x)$$ và đồ thị $$y = 2^x$$.
- Tự kiểm tra bằng tay vì sao lưới vuông $$\mathbb{Z}[i]$$ tạo ra một **điểm đặc biệt (CM)** trên đường cong modular.
- Phát biểu ý chính của **giả thuyết André–Oort** (cho đa tạp modular Siegel) và **giả thuyết Griffiths** (tính đại số của ảnh ánh xạ chu kỳ).
- Hiểu mạch 4 bước của chiến lược o-tối tiểu: cắt miền cơ bản → đếm điểm Pila–Wilkie → cận dưới quỹ đạo Galois (Tsimerman) → Ax–Schanuel & định lý Chow định nghĩa được.
- Tránh hai nhầm lẫn: coi tính o-tối tiểu "chỉ là tập nửa đại số", và coi André–Oort "chỉ nói về đường cong modular".

**Kiến thức cần có.** Hàm giải tích cơ bản ($$\sin x, e^x$$), số phức, lưới phẳng và khái niệm đa tạp đại số. Không đòi hỏi đã học lý thuyết Hodge hay logic hình thức.

**Liên hệ với khóa học.** So sánh bộ công cụ của Tsimerman (o-tối tiểu và giao không điển hình) với [chương trình Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) như *một cầu nối khác giữa số học và giải tích*. Bài [Birkar]({{ site.baseurl }}/contents/vi/chapter02/02_10_Birkar_Algebraic_Geometry/) thuộc hình học đại số song hữu tỉ, là một nhánh khác với hướng số học và ánh xạ chu kỳ ở đây.

---

## Kiến thức cần nhớ: Tính o-tối tiểu, Điểm CM và Định lý Pila–Wilkie là gì?

### 1. Hình học "thuần" (o-tối tiểu) vs Hình học "hoang" — Ví dụ cầm tay với $$\sin(x)$$
Một **cấu trúc o-tối tiểu** trên $$\mathbb{R}$$ là một hệ các tập hợp định nghĩa được (bằng phép toán logic từ các hàm cho phép) thỏa đúng một tiên đề cực kỳ giản dị: **mọi tập con 1 chiều của $$\mathbb{R}$$ định nghĩa được trong hệ đều chỉ gồm hữu hạn điểm và hữu hạn khoảng mở**!
- **Hàm "hoang":** Nếu ta đưa hàm $$\sin(x)$$ trên *toàn bộ* trục thực $$\mathbb{R}$$ vào hệ, tập nghiệm của $$\sin(x) = 0$$ là $$\{k\pi : k \in \mathbb{Z}\}$$ — có **vô hạn** điểm rời rạc! Hệ lập tức bị nhiễm tính "hoang" của số nguyên $$\mathbb{Z}$$ (nơi các câu hỏi logic trở nên không giải quyết được theo định lý Gödel).
- **Hàm "thuần" (o-tối tiểu):** Nếu ta chỉ cho phép dùng $$\sin(x)$$ trên đoạn đóng hữu hạn $$[0, 2\pi]$$, phương trình $$\sin(x) = 0$$ chỉ có đúng **3 nghiệm** $$\{0, \pi, 2\pi\}$$! Hai cấu trúc o-tối tiểu nổi tiếng nhất vượt xa đa thức là $$\mathbb{R}_{\mathrm{an}}$$ (thêm mọi hàm giải tích bị giới hạn trên miền compact) và **$$\mathbb{R}_{\mathrm{an,exp}}$$** (thêm cả hàm mũ toàn cục $$e^x$$!).

### 2. Điểm đặc biệt (CM) là gì? — Kiểm tra bằng tay trên lưới vuông $$\mathbb{Z}[i]$$
Nhớ lại bài [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/): mỗi mặt xuyến phức (đường cong elliptic) ứng với một lưới $$\Lambda_\tau = \mathbb{Z} + \mathbb{Z}\tau$$ trên $$\mathbb{C}$$.
- Với hầu hết các điểm $$\tau$$ ngẫu nhiên (ví dụ $$\tau = \pi i$$), chỉ có phép nhân với **số nguyên** $$n \in \mathbb{Z}$$ mới giữ nguyên lưới ($$n \Lambda_\tau \subset \Lambda_\tau$$).
- Nhưng hãy thử với **$$\tau = i$$** (lưới vuông $$\Lambda_i = \mathbb{Z} + \mathbb{Z}i$$, tương ứng đường cong elliptic $$y^2 = x^3 - x$$): nhân với số ảo $$i$$ cho $$i(m + ni) = -n + mi \in \Lambda_i$$! Lưới vuông có **thêm phép đối xứng nhân với số phức $$i$$** — gọi là **phép nhân phức** (*Complex Multiplication*, CM)! Các điểm CM (như $$\tau = i$$ với $$j(i) = 1728$$ hay $$\tau = \frac{1 + i\sqrt{3}}{2}$$ với $$j = 0$$) là những **điểm đặc biệt** chứa thông tin số học cực sâu (sinh ra trường lớp của trường bậc hai ảo).

### 3. Định lý đếm điểm Pila–Wilkie — Ví dụ cầm tay với $$y = 2^x$$
Tại sao logic o-tối tiểu lại đếm được nghiệm số học? Hãy nhìn đồ thị đường cong **siêu việt** $$y = 2^x$$ (định nghĩa được trong cấu trúc o-tối tiểu $$\mathbb{R}_{\mathrm{an,exp}}$$) và thử đếm xem có bao nhiêu **điểm hữu tỷ** $$(p/q, r/s)$$ nằm trên nó với tử mẫu không quá $$H$$!
- Nếu $$x = p/q$$ không phải số nguyên (ví dụ $$x = 1/2$$), thì $$y = 2^{1/2} = \sqrt{2}$$ là số **vô tỷ**!
- Vậy các điểm hữu tỷ trên $$y = 2^x$$ chỉ có thể xuất hiện tại $$x \in \mathbb{Z}$$ ($$x = 0, 1, 2, \dots, \lfloor \log_2 H \rfloor$$) — tổng cộng chỉ khoảng $$\mathbf{O(\log H)}$$ điểm, nhỏ hơn $$H^\varepsilon$$ với mọi $$\varepsilon > 0$$!

**Định lý Pila–Wilkie (2006)** tổng quát hóa hiện tượng đó lên mọi tập $$X$$ định nghĩa được trong *bất kỳ* cấu trúc o-tối tiểu nào: sau khi bỏ đi phần **đại số** của $$X$$, phần siêu việt còn lại chỉ chứa **cực kỳ ít điểm hữu tỷ** (ít hơn $$C_\varepsilon H^\varepsilon$$ với mọi $$\varepsilon > 0$$!).

---

## 1. Đa tạp Shimura, Giao không điển hình và Hai giả thuyết trung tâm

**Đa tạp Shimura** là tổng quát hóa nhiều chiều của đường cong modular (điển hình nhất là **đa tạp modular Siegel** $$\mathcal{A}_g$$ — không gian moduli của mọi đa tạp abel $$g$$ chiều). Trên đó có các **điểm đặc biệt** (điểm CM) và **đa tạp con đặc biệt**.

**Giả thuyết André–Oort** (trường hợp trọng tâm của chương trình **Zilber–Pink** về *giao không điển hình*) phát biểu: nếu một đa tạp con đại số $$V \subset S$$ chứa một tập điểm đặc biệt trù mật theo Zariski ("quá nhiều" điểm đặc biệt!), thì bản thân $$V$$ **bắt buộc phải là một đa tạp con đặc biệt**.

Song song đó, **Giả thuyết Griffiths** hỏi về **ánh xạ chu kỳ** (*period map*) gắn mỗi đa tạp trong một họ đại số với tọa độ là các tích phân siêu việt (như tích phân elliptic $$\int_\gamma \frac{dx}{y}$$): dù xây bằng giải tích siêu việt, ảnh của ánh xạ chu kỳ có luôn là một **tập đại số** không?

---


### Video ngắn 1: Tính o-tối tiểu & Chiến lược Đếm điểm Pila–Wilkie

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/tsimerman-o-minimal_vi.mp4"></video>
</div>

Video dài khoảng 36 giây (có thuyết minh tiếng Việt): hình học ngoan ℝ_an,exp, định lý Pila–Wilkie và gọng kìm Galois vs Pila–Wilkie.

## 2. Giải thích: O-minimality giải Giả thuyết André–Oort và Giả thuyết Griffiths như thế nào?

Làm thế nào một định lý từ logic toán (Pila–Wilkie) lại chinh phục được cả hai giả thuyết trụ cột của hình học số học và lý thuyết Hodge? Hãy đi chậm qua mạch 4 bước dưới đây:

#### Bước 1: Cắt miền cơ bản để "thuần hóa" ánh xạ siêu việt
Ánh xạ phủ đồng nhất $$\pi: \mathbb{H} \to \mathbb{H}/\mathrm{SL}_2(\mathbb{Z})$$ (như hàm modular $$j(\tau)$$) là hàm tuần hoàn $$j(\tau + 1) = j(\tau)$$ nên **hoang** trên toàn bộ $$\mathbb{H}$$. Nhưng nếu ta cắt lấy đúng một **miền cơ bản** $$\mathcal{F} = \{\tau \in \mathbb{H} : \vert\operatorname{Re}\tau\vert \le 1/2,\; \vert\tau\vert \ge 1\}$$, thì Peterzil–Starchenko (và Bakker–Brunebarbe–Tsimerman cho ánh xạ chu kỳ tổng quát) chứng minh rằng hạn chế $$\pi\vert_{\mathcal{F}}$$ là **định nghĩa được trong cấu trúc o-tối tiểu $$\mathbb{R}_{\mathrm{an,exp}}$$**! Mọi hàm siêu việt phức tạp bỗng trở nên "thuần"!

#### Bước 2: Đối đầu hai bất đẳng thức — Đếm điểm Pila–Wilkie vs Quỹ đạo Galois (Đột phá Tsimerman!)
Giả sử đa tạp con $$V$$ chứa nhiều điểm đặc biệt $$x$$. Ta kéo ngược $$V$$ lên miền cơ bản thành tập o-tối tiểu $$Z = \pi^{-1}(V) \cap \mathcal{F}$$; mỗi điểm CM $$x \in V$$ tương ứng với một điểm bậc số học thấp (độ cao $$H$$) trên $$Z$$:
- **Chặn dưới (Số học — Quỹ đạo Galois):** Nếu $$x$$ là điểm CM với biệt thức $$D$$, các liên hợp Galois của $$x$$ đều nằm trên $$V$$ và số lượng của chúng phải tăng **nhanh theo đa thức** $$D^\delta$$! Suốt nhiều năm, nút thắt khó nhất của André–Oort cho đa tạp modular Siegel $$\mathcal{A}_g$$ là chưa chứng minh được chặn dưới Galois này. Năm 2018, **Jacob Tsimerman** phá vỡ nút thắt đó bằng cách vận dụng công thức Colmez trung bình (Andreatta–Goren–Howard–Madapusi Pera / Yuan–Zhang), chứng minh trọn vẹn **André–Oort cho $$\mathcal{A}_g$$**!
- **Chặn trên (Logic — Pila–Wilkie):** Trên phần siêu việt của $$Z$$, số điểm độ cao $$\le D$$ lại tăng **chậm hơn mọi lũy thừa** $$D^\varepsilon$$!

#### Bước 3: Cuộc đụng độ ép ra mảnh đại số & Định lý Ax–Schanuel hàm
Vì $$D^\delta \gg D^\varepsilon$$ khi $$D$$ lớn, hai bất đẳng thức đụng độ nảy lửa — cách duy nhất để không mâu thuẫn là tập o-tối tiểu $$Z$$ **bắt buộc phải chứa một mảnh đại số thực sự** (không nằm trong phần siêu việt)! Sau đó, bằng phiên bản hàm của **định lý siêu việt Ax–Schanuel** (Mok–Pila–Tsimerman), mảnh đại số ấy bị ép phải là một **đa tạp con đặc biệt**!

#### Bước 4: Nâng o-minimality thành công cụ của Lý thuyết Hodge (Giả thuyết Griffiths)
Cùng với **Benjamin Bakker và Yohan Brunebarbe**, Tsimerman phát hiện tính o-tối tiểu còn mạnh hơn cả việc đếm điểm: họ chứng minh một phiên bản **Định lý Chow cho không gian giải tích định nghĩa được** (nếu một tập giải tích phức định nghĩa được trong cấu trúc o-tối tiểu thì nó tự động mang cấu trúc đại số!). Áp dụng định lý này cho ảnh của **ánh xạ chu kỳ** (đã được họ chứng minh định nghĩa được trong $$\mathbb{R}_{\mathrm{an,exp}}$$), họ chứng minh trọn vẹn **Giả thuyết Griffiths** về tính đại số của ảnh ánh xạ chu kỳ!

Tóm tắt toàn bộ cây cầu:

$$
\text{Ánh xạ chu kỳ / Đa tạp Shimura}
\;\xrightarrow{\text{Miền cơ bản}}\;
\text{Tập o-tối tiểu } (\mathbb{R}_{\mathrm{an,exp}})
\;\xrightarrow{\text{Pila–Wilkie + Galois + Ax–Schanuel}}\;
\text{André–Oort \& Griffiths}.
$$

---


### Video ngắn 2: Giải quyết Giả thuyết André–Oort & Giả thuyết Griffiths

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/tsimerman-andre-oort_vi.mp4"></video>
</div>

Video dài khoảng 37 giây (có thuyết minh tiếng Việt): điểm CM trên đa tạp Shimura A_g, cận dưới quỹ đạo Galois của Tsimerman (2018) và ánh xạ chu kỳ Bakker–Brunebarbe–Tsimerman.

## 3. Các giả thuyết được nêu tên & So sánh các cầu nối

| Giả thuyết / kết quả | Nội dung chính | Vai trò trong lời trích dẫn |
|----------------------|-----------|-------------------------|
| Tính đại số của ảnh ánh xạ chu kỳ (giả thuyết Griffiths) | Ảnh của ánh xạ chu kỳ là tập đại số (Bakker–Brunebarbe–Tsimerman) | Được nêu đích danh |
| André–Oort cho đa tạp modular Siegel | Bao đóng Zariski của tập điểm đặc biệt là đa tạp con đặc biệt (Tsimerman và cộng sự) | Được nêu đích danh |
| Bối cảnh rộng hơn: Zilber–Pink | Giao không điển hình nói chung | Bối cảnh xung quanh; nhiều trường hợp vẫn còn mở |

| Chương trình | Cầu nối | Công cụ tiêu biểu |
|--------------|---------|-------------------|
| Định lý modular / Langlands | Dạng tự đẳng cấu ↔ biểu diễn Galois / motive | Công thức vết, endoscopy, phân thớ Hitchin |
| Green–Tao / Maynard | Cấu trúc trong tập số nguyên tố | Nguyên lý chuyển; phương pháp sàng đa chiều |
| **Tsimerman / o-tối tiểu** | Ánh xạ chu kỳ và đa tạp Shimura ↔ hình học Diophantine | Tính o-tối tiểu $$\mathbb{R}_{\mathrm{an,exp}}$$; Pila–Wilkie; đơn đạo |

**Ghi nhận công lao:** Các định lý lớn này là thành quả của cả một cộng đồng nghiên cứu (Pila, Zannier, Ullmo, Yafaev, Klingler, Bakker, Brunebarbe, Mok, Tsimerman…). Giải Fields 2026 ghi nhận vai trò trung tâm của Tsimerman trong việc đặt lại tính o-tối tiểu thành phương pháp nền tảng và giải quyết các mắt xích quyết định.

---

## Nhầm lẫn thường gặp

| Khẳng định | Kết luận | Sửa lại |
|------------|----------|---------|
| "Tính o-tối tiểu chỉ nói về tập nửa đại số." | Sai | Tập nửa đại số chỉ là ví dụ sơ khai; ánh xạ chu kỳ cần mở rộng mạnh như $$\mathbb{R}_{\mathrm{an,exp}}$$. |
| "André–Oort chỉ nói về đường cong modular." | Sai | Bối cảnh tổng quát là đa tạp Shimura; trường hợp đa tạp modular Siegel $$\mathcal{A}_g$$ là trọng tâm trong lời trích dẫn. |
| "Ánh xạ chu kỳ hiển nhiên có ảnh đại số." | Sai | Tọa độ của nó là tích phân siêu việt; tính đại số là một định lý sâu (giả thuyết Griffiths). |
| "Tính o-tối tiểu thay thế được đơn đạo và số học Galois." | Sai | Luôn phải kết hợp cả ba: o-tối tiểu (chặn trên), quỹ đạo Galois (chặn dưới) và Ax–Schanuel/đơn đạo. |
| "'Không điển hình' nghĩa là xác suất thấp." | Chưa chính xác | Đó chỉ là cách nói hình ảnh; nội dung toán học là về số chiều và bao đóng Zariski. |

---

## Nguồn video và tài liệu đọc

Chi tiết: `research/video-research/Tsimerman_Arithmetic/`.

**Thứ tự xem gợi ý**

1. Bài của Quanta về giải Fields 2026: [link](https://www.quantamagazine.org/jacob-tsimerman-wins-2026-fields-medal-for-andre-oort-conjecture-proof-20260723/).  
2. Thông cáo của Đại học Toronto và Harvard.  
3. Wikipedia: André–Oort, o-minimality.

**Ghi nhớ:** Tính o-tối tiểu là công cụ cho số học; giả thuyết Zilber–Pink rộng hơn và vẫn còn mở.

---

## Tài liệu tham khảo


Danh mục URL đầy đủ (gồm mọi link dùng khi tìm video): `research/video-research/Tsimerman_Arithmetic/references.md`.

### Danh sách URL đầy đủ

1. https://www.quantamagazine.org/jacob-tsimerman-wins-2026-fields-medal-for-andre-oort-conjecture-proof-20260723/  
2. https://arxiv.org/search/?query=Tsimerman+Andr%C3%A9-Oort&searchtype=all  
3. https://www.utoronto.ca/celebrates/jacob-tsimerman-awarded-2026-fields-medal  
4. https://www.math.harvard.edu/jacob-tsimerman-receives-2026-fields-medal/  
5. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026  
6. https://en.wikipedia.org/wiki/Andr%C3%A9%E2%80%93Oort_conjecture  
7. https://en.wikipedia.org/wiki/Jacob_Tsimerman  
8. https://arxiv.org/search/?query=Pila+Wilkie&searchtype=all  
9. https://arxiv.org/search/?query=Tsimerman+Siegel&searchtype=all  
10. https://en.wikipedia.org/wiki/O-minimality  
11. https://en.wikipedia.org/wiki/Shimura_variety  
12. https://en.wikipedia.org/wiki/Unlikely_intersections  

### Gói nghiên cứu

13. Gói khóa học: `research/video-research/Tsimerman_Arithmetic/`.

1. IMU, Huy chương Fields 2026, Jacob Tsimerman (trích dẫn chính thức).
2. Các bài báo về André–Oort cho đa tạp modular Siegel và về tính đại số của ảnh ánh xạ chu kỳ (Tsimerman và cộng sự).
3. Các bài tổng quan về tính o-tối tiểu và giao không điển hình (Pila–Zannier; các phát triển sau; các bài giảng giới thiệu).
4. J. Pila, A. Wilkie: định lý đếm điểm trên tập o-tối tiểu (kết quả nền).
5. Thông cáo của Đại học Toronto (2026).
6. Trong khóa học: [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Birkar]({{ site.baseurl }}/contents/vi/chapter02/02_10_Birkar_Algebraic_Geometry/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Tìm hiểu định lý đếm điểm **Pila–Wilkie** như bước đầu vào hình học Diophantine dùng tính o-tối tiểu, trước khi đọc André–Oort đầy đủ.
- So sánh với định lý modular, một cầu nối số học–giải tích khác: cả hai đều cho thấy đối tượng có cấu trúc chặt hơn ta tưởng, nhưng bằng ngôn ngữ khác nhau.
- Đọc một bài ngắn về điểm CM trên đường cong modular để có ví dụ trực quan về "điểm đặc biệt".
- Nếu theo hướng lý thuyết Hodge: đọc một bài tổng quan cho học viên cao học về ánh xạ chu kỳ và biến thiên cấu trúc Hodge, song song với tính o-tối tiểu. Hai phần này bổ sung cho nhau chứ không thay thế nhau.

## Video tham khảo

- **Xem trước** — [2026 Fields Medal: Jacob Tsimerman](https://www.youtube.com/watch?v=TAh5tZ8QAzQ) — Simons Foundation, tiếng Anh. Video giới thiệu ngắn về Jacob Tsimerman và công trình được trao giải. Nên xem trước khi đọc bài.
- [Jacob Tsimerman - o-minimality and Unlikely Intersections](https://www.youtube.com/watch?v=2N9lZRawi3I) — princetonmathematics, tiếng Anh. Bài giảng của Tsimerman về tính o-tối tiểu và giao không điển hình, tương ứng với mục 1 và 3. Nên xem sau khi đọc bài.
- [Period mappings are definable in the o-minimal structure ℝan,exp - Jacob Tsimerman](https://www.youtube.com/watch?v=6lsOOBPHXRk) — Institute for Advanced Study, tiếng Anh. Bài giảng chuyên sâu về việc ánh xạ chu kỳ định nghĩa được trong cấu trúc ℝan,exp, liên quan đến mục 2 và 3. Dành cho người muốn đi sâu về kỹ thuật.
