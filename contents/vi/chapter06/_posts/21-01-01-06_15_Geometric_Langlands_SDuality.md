---
layout: post
title: "Geometric Langlands & S-Duality (Deep Dive)"
chapter: '06'
order: 15
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: deep-dive
---

Vào năm 1967, Robert Langlands viết một bức thư tay dài 17 trang gửi André Weil, đề xuất một mạng lưới đối ngẫu đầy tham vọng nối lý thuyết số với giải tích điều hòa thông qua một đối tượng kỳ lạ gọi là **nhóm đối ngẫu** $$G^\vee$$. Mười năm sau, ở một vũ trụ hoàn toàn khác — vật lý hạt cơ bản — hai nhà vật lý Claus Montonen và David Olive tìm cách tổng quát hóa tính đối xứng điện–từ của Maxwell sang lý thuyết gauge không giao hoán, và họ tình cờ gặp lại **chính xác cùng một nhóm đối ngẫu $$G^\vee$$ đó**!

Suốt gần ba thập kỷ, sự trùng hợp kỳ lạ ấy giống như hai đoàn thợ đào hầm từ hai sườn núi khác nhau nghe tiếng cuốc của nhau vọng qua vách đá. Cho đến năm 2006, Anton Kapustin và Edward Witten đã đục thông vách đá đó bằng một bài báo kinh điển: họ chỉ ra rằng **Langlands hình học** (phiên bản hình học đại số của chương trình Langlands trên một mặt Riemann) chính là hình bóng toán học của **đối ngẫu S** (đối ngẫu điện–từ, hay mạnh–yếu) trong lý thuyết gauge siêu đối xứng bốn chiều $$\mathcal N=4$$ super Yang–Mills, với cơ chế bên trong là **đối xứng gương của hệ Hitchin**.

Bài đọc sâu này nằm ngay tại ngã ba lớn nhất của toán và vật lý hiện đại, nơi giao nhau của:

- [Đối ngẫu như một nguyên lý]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)  
- [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) (chương trình số học; nhóm đối ngẫu)  
- [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) (hình học SYZ của hệ Hitchin)

**Đừng** nhầm Bổ đề cơ bản của Ngô với "chương trình Langlands đã xong", và đừng nhầm từ điển vật lý với chứng minh đầy đủ mọi tương ứng hình học.

Gói nghiên cứu: `research/video-research/geometric-langlands-sduality/`.

---

## Bản đồ kiến thức nền: Langlands hình học và đối ngẫu S là gì và nghiên cứu những gì?

Thoạt nhìn, thuật ngữ trong bài này ("stack moduli $$\mathrm{Bun}_G(C)$$", "bó riêng Hecke", "$$\mathcal N=4$$ SYM") có thể khiến người mới choáng ngợp. Nhưng bạn chỉ cần nắm **ba mảnh ghép trực giác** là đọc thông toàn bộ bài:

1. **Nhóm đối ngẫu Langlands $$G^\vee$$:** Mọi nhóm ma trận đối xứng quen thuộc $$G$$ (nhóm Lie khử được) đều có một "bản song sinh đối ngẫu" $$G^\vee$$ thu được bằng cách đảo ngược lưới nghiệm của nó. Đôi khi $$G$$ tự đối ngẫu ($$\mathrm{GL}_n^\vee = \mathrm{GL}_n$$), đôi khi hai họ khác nhau lại là cặp đối ngẫu của nhau (nhóm trực giao lẻ $$\mathrm{SO}_{2n+1}$$ đối ngẫu với nhóm symplectic $$\mathrm{Sp}_{2n}$$, còn $$\mathrm{SU}(n)$$ đối ngẫu với $$\mathrm{PSU}(n)$$).
2. **Langlands hình học (Thế giới Toán):** Thay vì nghiên cứu số nguyên tố trên trường số $$\mathbb{Q}$$ như Langlands số học, ta làm việc trên một **đường cong đại số / mặt Riemann** $$C$$ (như mặt cầu hay mặt bánh donut). Bên trái là thế giới "hàm sóng / bó" sống trên không gian tất cả các phân thớ $$G$$ trên $$C$$ (ký hiệu $$\mathrm{Bun}_G(C)$$); bên phải là thế giới "phổ / liên thông phẳng" của nhóm đối ngẫu $$G^\vee$$ trên $$C$$. Phép đối ngẫu nối hai phạm trù đó giống như một phép **biến đổi Fourier phi tuyến khổng lồ**.
3. **Đối ngẫu S (Thế giới Vật lý):** Mở rộng tính đối xứng điện ↔ từ của phương trình Maxwell sang các lý thuyết trường lượng tử 4 chiều: khi ta đổi hằng số tương tác mạnh $$g$$ thành yếu $$1/g$$, các hạt mang *điện tích* của nhóm $$G$$ biến thành các *đơn cực từ* của đúng nhóm đối ngẫu $$G^\vee$$!

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- Phân biệt Langlands **số học** với Langlands **hình học** (đối tượng và trường nền khác nhau; chung ý tưởng nhóm đối ngẫu).
- Phát biểu ý chính của Langlands hình học: bó trên $$\mathrm{Bun}_G(C)$$ ↔ dữ liệu phổ cho $$G^\vee$$.
- Giải thích **đối ngẫu S** của $$\mathcal N=4$$ SYM: đổi mạnh thành yếu và $$G\leftrightarrow G^\vee$$.
- Phác họa bức tranh compact hóa của **Kapustin–Witten** (lý thuyết 4 chiều trên $$C\times\Sigma$$ → mô hình sigma 2 chiều / phạm trù brane).
- Nối **hệ Hitchin** của $$G$$ và $$G^\vee$$ với đối xứng gương.
- Nói đúng trạng thái: vật lý là **cầu nối và nguồn gợi ý**, không tự động cho chứng minh.

**Kiến thức cần có.** Bài nguyên lý đối ngẫu; tổng quan Langlands ở Chương 2. Nhóm khử được (reductive) và stack moduli chỉ cần biết tên.

---

## 1. Hai thế giới Langlands

| | Langlands số học | Langlands hình học |
|--|------------------|--------------------|
| Nền | Trường số / adele | Đường cong đại số (thường trên $$\mathbb{C}$$) |
| Phía tự đẳng cấu | Biểu diễn tự đẳng cấu của $$G(\mathbb{A})$$ | Bó / D-module trên $$\mathrm{Bun}_G(C)$$ |
| Phía Galois / phổ | Biểu diễn Galois | Hệ địa phương / phân thớ Higgs / phủ phổ cho $$G^\vee$$ |
| Nhóm đối ngẫu | $$G^\vee$$ | $$G^\vee$$ |
| Công cụ chính | Công thức vết, nội soi (endoscopy), $$L$$-hàm | Bó riêng Hecke, phạm trù dẫn xuất, hệ Hitchin |

**Công trình được giải Fields của Ngô** chứng minh Bổ đề cơ bản, phục vụ việc **so sánh nội soi** trong công thức vết của Langlands số học. Đó *không* phải chứng minh tương ứng hình học đầy đủ, và *không* có nghĩa "chương trình Langlands đã xong".

---

## 2. Ý chính của Langlands hình học

Cố định một đường cong xạ ảnh trơn $$C$$ và một nhóm khử được $$G$$. Nói gần đúng:

> Phạm trù các bó (thích hợp) trên stack moduli $$\mathrm{Bun}_G(C)$$ đối ngẫu với một phạm trù dựng từ các $$G^\vee$$-hệ địa phương (hoặc dữ liệu phổ liên quan) trên $$C$$.

Dạng cổ điển nhấn mạnh **bó riêng Hecke** (Hecke eigensheaf): bó là vectơ riêng của các toán tử Hecke, với "giá trị riêng" là một hệ địa phương của $$G^\vee$$. Hãy liên hệ với điều bạn đã biết ở đại số tuyến tính và giải tích: với một nhóm abel $$G = \mathbb{C}^\times$$, Langlands hình học thực chất rút về **biến đổi Fourier–Mukai** trên đa tạp Jacobian của đường cong $$C$$ (biến hàm/bó trên một xuyến thành hàm/bó trên xuyến đối ngẫu!). Cái khó vĩ đại của Langlands hình học nằm ở chỗ khi $$G$$ không giao hoán (như $$\mathrm{GL}_n$$ với $$n\ge 2$$), không gian $$\mathrm{Bun}_G(C)$$ không còn là nhóm nữa mà là một không gian moduli phức tạp hơn nhiều. Cách phát biểu hiện đại dùng hình học đại số dẫn xuất và các tương đương phạm trù tinh tế hơn; phát biểu chính xác thay đổi theo từng tài liệu.

**Gợi ý học.** Hãy nhớ **hình dạng** của phát biểu: hình học tự đẳng cấu của $$G$$ đối ngẫu với hình học phổ của $$G^\vee$$. Không cần định nghĩa đầy đủ stack.

---

## 3. Đối ngẫu S trong lý thuyết gauge

Phương trình **Maxwell** đã có đối ngẫu điện–từ. **Montonen–Olive** và các công trình sau mở rộng thành **đối ngẫu S** không giao hoán: hằng số tương tác mạnh được ánh xạ thành hằng số tương tác yếu của lý thuyết đối ngẫu, và nhóm gauge được thay bằng **nhóm đối ngẫu Langlands** $$G^\vee$$.

Với $$\mathcal N=4$$ SYM bốn chiều, đối ngẫu S đặc biệt rõ: hằng số tương tác phức $$\tau = \frac{\theta}{2\pi} + \frac{4\pi i}{g^2}$$ biến đổi theo nhóm kiểu $$\mathrm{SL}(2,\mathbb{Z})$$ (trong đó phép biến đổi $$S: \tau \mapsto -1/\tau$$ lật ngược hằng số tương tác $$g \leftrightarrow 1/g$$ khi $$\theta=0$$!), và hai lý thuyết đối ngẫu có cùng phổ BPS trong các chế độ kiểm soát được.

---

## 4. Cầu nối Kapustin–Witten

**Kapustin–Witten** (arXiv:hep-th/0604151) lập luận, nói gần đúng:

1. Bắt đầu từ phiên bản xoắn tôpô của $$\mathcal N=4$$ SYM bốn chiều với nhóm $$G$$.  
2. Compact hóa trên mặt Riemann $$C$$ (chính là đường cong trong Langlands hình học) — tức là cho hai trong bốn chiều không–thời gian cuộn lại thành mặt $$C$$ có kích thước rất nhỏ.  
3. Lý thuyết hiệu dụng trên 2 chiều còn lại là một mô hình sigma với đích là không gian moduli Higgs (Hitchin), kèm theo **phạm trù các brane** trên không gian đó.  
4. **Đối ngẫu S** của lý thuyết 4 chiều trở thành một đối ngẫu giữa các phạm trù 2 chiều, khớp với Langlands hình học cho $$G$$ và $$G^\vee$$.  
5. Trên đường đi, **đối xứng gương** của hệ Hitchin (A-brane ↔ B-brane) xuất hiện như cơ chế hình học. Điều này nối bài này với bài đối xứng gương.

**Cách đọc đúng.** Đây là **từ điển và động lực đến từ vật lý**, định hướng cho một chương trình nghiên cứu toán. Nó không thay cho chứng minh toán học.

---

### Khung giải thích: kiểm tra tay phép lật $$\tau \mapsto -1/\tau$$ của đối ngẫu S và phổ điện–từ (nên đọc chậm)

Thuật ngữ "đối ngẫu S biến tương tác mạnh thành yếu và hoán đổi hạt mang điện tích với đơn cực từ" trở nên trong suốt ngay lập tức khi bạn kiểm tra trực tiếp hai công thức đại số số phức ngắn gọn dưới đây.

1. **Kiểm tra phép lật mạnh ↔ yếu:** Trong lý thuyết $$\mathcal N=4$$ super Yang–Mills 4 chiều, hằng số tương tác gauge $$g > 0$$ và góc tôpô $$\theta$$ được gói vào một số phức duy nhất trên nửa mặt phẳng trên:

   $$
   \tau = \frac{\theta}{2\pi} + i\,\frac{4\pi}{g^2}.
   $$

   Xét trường hợp đơn giản $$\theta = 0$$, khi đó $$\tau = i\,\frac{4\pi}{g^2}$$. Áp dụng phép biến đổi đối ngẫu S $$\tau \mapsto \tilde\tau = -\frac{1}{\tau}$$:

   $$
   \tilde\tau = -\frac{1}{i\,(4\pi/g^2)} = i\,\frac{g^2}{4\pi} = i\,\frac{4\pi}{\tilde g^2}
   \;\Longrightarrow\;
   \tilde g = \frac{4\pi}{g}.
   $$

   **Thử bằng số cụ thể:** Giả sử lý thuyết gốc có hằng số tương tác cực mạnh $$g = 40\pi \approx 125.7$$ (mọi chuỗi nhiễu loạn theo lũy thừa của $$g^2$$ đều phân kỳ vô vọng). Sau phép đối ngẫu S, lý thuyết đối ngẫu có hằng số tương tác

   $$
   \tilde g = \frac{4\pi}{40\pi} = 0.1
   \;\Longrightarrow\;
   \tilde g^2 = 0.01!
   $$

   Từ một bài toán phi nhiễu loạn bất khả thi, ta bước sang một lý thuyết tương tác siêu yếu tính gọn trong vài số hạng đầu tiên!

2. **Kiểm tra sự hoán đổi điện tích $$n_e$$ ↔ từ tích $$n_m$$:** Trong phổ BPS của lý thuyết, khối lượng của một hạt mang cặp điện tích–từ tích $$(n_e, n_m) \in \mathbb{Z}^2$$ tỉ lệ với $$\lvert n_e + n_m \tau \rvert$$. Khi thay $$\tau \mapsto -1/\tau$$, ta nhân gọn biểu thức bằng tay:

   $$
   \Bigl\lvert n_e + n_m\Bigl(-\frac{1}{\tau}\Bigr)\Bigr\rvert
   = \frac{1}{\lvert \tau \rvert}\,\lvert -n_m + n_e\tau \rvert.
   $$

   Nhìn vào cặp hệ số mới $$(n'_e, n'_m) = (-n_m, n_e)$$: một hạt **thuần điện** $$(1, 0)$$ (gắn với đường Wilson) biến thành một **đơn cực thuần từ** $$(0, 1)$$ (gắn với đường 't Hooft), và ngược lại! Khi tổng quát hóa từ nhóm abel $$U(1)$$ lên nhóm ma trận không giao hoán $$G$$, mạng lưới điện tích sinh ra nhóm $$G$$, còn mạng lưới đơn cực từ sinh ra chính xác **nhóm đối ngẫu Langlands $$G^\vee$$** — đó là nhịp cầu tự nhiên dẫn từ vật lý 4 chiều sang Langlands hình học.

## 5. Hệ Hitchin và đối xứng gương

**Phân thớ Hitchin** biểu diễn không gian moduli các phân thớ Higgs như một hệ khả tích trên một cơ sở gồm các hệ số của đa thức đặc trưng. Với hai nhóm đối ngẫu $$G$$ và $$G^\vee$$, các thớ (trong trường hợp tổng quát) là những đa tạp abel đối ngẫu nhau. Đó là một cặp **gương kiểu SYZ** (Hausel–Thaddeus và các công trình liên quan). Tóm lại:

```text
S-duality (gauge 4d)
    ↓ compact hóa
Mirror symmetry của hệ Hitchin
    ↓ category brane
Geometric Langlands correspondence
```

Sơ đồ này là nội dung cốt lõi trong cách nhìn của Kapustin–Witten.

---

## 6. Bản đồ trạng thái (2026)

| Phát biểu | Trạng thái |
|-----------|------|
| Nhóm đối ngẫu tổ chức cả chương trình số học lẫn hình học | Nguyên lý thiết kế đã ổn định |
| Bổ đề cơ bản (Ngô và các tác giả khác) | **Định lý** (công cụ nội soi trong Langlands số học) |
| Langlands hình học (các cách phát biểu) | Tiến bộ lớn: năm 2024, nhóm Gaitsgory–Raskin và cộng sự công bố chứng minh phỏng đoán không phân nhánh (dạng de Rham); các dạng khác vẫn đang nghiên cứu |
| Từ điển Kapustin–Witten | Ảnh hưởng lớn; cầu nối vật lý ↔ toán |
| Tính hàm tử (functoriality) đầy đủ của Langlands số học | Phần lớn còn **mở** |

---

## 7. Bản đồ khóa học

| Bài | Liên hệ |
|-----|----------|
| [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) | Chương trình số học và Bổ đề cơ bản |
| [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/) | Bài tổng quan |
| [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) | HMS / SYZ; gương của hệ Hitchin |
| [AdS/CFT]({{ site.baseurl }}/contents/vi/chapter06/06_14_AdS_CFT/) | Một phép đối ngẫu khác (nguyên lý toàn ảnh) |
| [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) | Chỉ số và lớp đặc trưng |
| [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/) | Nền tảng giải tích của lý thuyết gauge |

---

## 8. Những nhầm lẫn thường gặp

| Khẳng định | Chỉnh lại |
|------------|-----------|
| "Langlands hình học = Langlands số học." | Chung ý tưởng nhóm đối ngẫu; đối tượng toán học khác nhau. |
| "Ngô chứng minh Langlands hình học." | Ngô chứng minh Bổ đề cơ bản, phục vụ nội soi trong công thức vết. |
| "Vật lý chứng minh Langlands." | Vật lý cho từ điển đối ngẫu S; phát biểu toán học phải được chứng minh bằng toán. |
| "Đối ngẫu S chỉ có trong lý thuyết dây." | Nó có ngay trong lý thuyết trường lượng tử ($$\mathcal N=4$$ SYM), không cần lý thuyết dây đầy đủ. |
| "Hitchin = đối xứng gương thuần nhất (HMS) cho mọi đa tạp Calabi–Yau." | Gương của hệ Hitchin là một họ ví dụ hình học đặc biệt và quan trọng. |

---

## Ghi chú viết lại từ các video chính

*Viết lại từ phụ đề tự động các bài giảng của Kapustin, Gukov, Frenkel. Phụ đề: `research/video-research/geometric-langlands-sduality/transcripts/`. Các đơn vị kiến thức: `knowledge_units_mode_c.json`. Đây là phần viết lại, không chép phụ đề.*

### C1. Kapustin: mầm mống điện–từ

Phương trình Maxwell cổ điển (không có điện tích) có một đối xứng: đổi trường từ thành trừ trường điện, và trường điện thành trường từ. Đó là **mầm mống của đối ngẫu S**. Trong lý thuyết gauge không giao hoán và siêu đối xứng, ta có nhóm đối ngẫu $$G^\vee$$, các toán tử đường đối ngẫu, và các đại lượng quan sát được tương ứng với nhau.

### C2. Đường Wilson (điện) và khuyết tật từ

**Vòng hay đường Wilson** mô tả việc đưa vào đường thế giới của một điện tích. **Toán tử đường từ** đối ngẫu (toán tử 't Hooft) là đại lượng quan sát tương ứng ở phía đối ngẫu. Trong từ điển vật lý, Langlands hình học sắp xếp các phạm trù từ dữ liệu đối ngẫu sau khi compact hóa trên đường cong. Đây là **cầu nối, không phải chứng minh toán học**.

### C3. Gukov: vì sao có Langlands hình học, rồi đến vật lý

Nửa đầu bài giảng: Langlands hình học nằm ở chỗ giao nhau của **số học** (Langlands cổ điển), **hình học** và **lý thuyết biểu diễn**. Nửa sau: **cách tiếp cận vật lý** qua đối ngẫu S của lý thuyết gauge kiểu $$\mathcal N=4$$. Cách đóng gói khác toán thuần túy, nhưng cùng ý tưởng nhóm đối ngẫu.

### C4. Frenkel: video định hướng dự phòng

Bài nói của Frenkel nhẹ hơn, dùng khi bài của Kapustin hay Gukov quá nặng. Nó cho cái nhìn chung, không đầy đủ về kỹ thuật.

### C5. Nói cho chính xác (giống Chương 2, §9b)

Bổ đề cơ bản của Ngô thuộc về **nội soi trong Langlands số học**, không có nghĩa "Langlands hình học đã xong". Từ điển đối ngẫu của vật lý định hướng nghiên cứu nhưng không thay cho chứng minh toán học. Xem [bài ngắn về Witten]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/).

---

## Nguồn video

Gói: `research/video-research/geometric-langlands-sduality/`.

1. **Nội dung chính / ghi chú ở trên:** Kapustin: [https://www.youtube.com/watch?v=oJRD3PshFjY](https://www.youtube.com/watch?v=oJRD3PshFjY) · phụ đề có trong gói  
2. **Nội dung chính / ghi chú ở trên:** Gukov: [https://www.youtube.com/watch?v=bCpVL6flCxo](https://www.youtube.com/watch?v=bCpVL6flCxo) · phụ đề có trong gói  
3. **Định hướng / ghi chú ở trên:** Frenkel: [https://www.youtube.com/watch?v=8Pkw25J-Bg0](https://www.youtube.com/watch?v=8Pkw25J-Bg0) · phụ đề có trong gói  
4. **Cầu nối:** Witten: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo) · phụ đề nằm trong gói đối xứng gương  

Danh sách URL đầy đủ: `research/video-research/geometric-langlands-sduality/references.md`.  
Trạng thái phụ đề: `research/video-research/geometric-langlands-sduality/TRANSCRIPT_STATUS.md`.

---

## Tài liệu tham khảo

1. Kapustin–Witten — https://arxiv.org/abs/hep-th/0604151  
2. Frenkel — https://arxiv.org/abs/hep-th/0512172  
3. Gukov–Witten — https://arxiv.org/abs/hep-th/0612073  
4. Hausel–Thaddeus — https://arxiv.org/abs/math/0205236  
5. Khóa: [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/)  
6. Gói: `research/video-research/geometric-langlands-sduality/`  

## Video tham khảo

- **Xem trước:** [Lecture 1: Geometric Langlands and S-duality in N = 4 SYM by Sergei Gukov](https://www.youtube.com/watch?v=bCpVL6flCxo) (International Centre for Theoretical Sciences, tiếng Anh). Bài giảng đầu tiên của Gukov: vì sao có Langlands hình học, rồi cách tiếp cận qua đối ngẫu S. Nên xem trước khi đọc mục 1 đến 4.
- [Gauge Theory, Geometric Langlands, and All That - Edward Witten](https://www.youtube.com/watch?v=8Pkw25J-Bg0) (Viktór, tiếng Anh). Bài nói tổng quan về lý thuyết gauge và Langlands hình học. Nên xem lần thứ hai, khi ý chính đã rõ.
- [Edward Witten: Mirror Symmetry & Geometric Langlands (2012)](https://www.youtube.com/watch?v=S02ghGCdNDo) (Graduate Mathematics, tiếng Anh). Witten nói về mối liên hệ giữa đối xứng gương và Langlands hình học; bổ sung cho mục 4 và 5.
