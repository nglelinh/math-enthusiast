---
layout: post
title: "Không gian Perfectoid của Scholze (Huy chương Fields 2018)"
chapter: '02'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Trong toán học, có những giải thưởng lớn trao cho người chinh phục một đỉnh núi cụ thể — một giả thuyết trăm năm cuối cùng đã chịu khuất phục. Nhưng cũng có những giải thưởng trao cho người phát minh ra **một loại bản đồ và ngôn ngữ hoàn toàn mới**, khiến cả một vùng núi hiểm trở bỗng trở nên có thể đi lại được. Câu chuyện của **Peter Scholze** và **Huy chương Fields 2018** thuộc về kiểu thứ hai.

Từ lâu, các nhà hình học số học sống giữa hai thế giới gần giống nhau như anh em sinh đôi nhưng ngăn cách nhau bởi một bức tường kỳ lạ: thế giới **đặc số 0** (nơi các số nguyên thông thường và số $$p$$-adic sinh sống) và thế giới **đặc số $$p$$** (nơi ta làm toán theo modulo số nguyên tố $$p$$, nên mọi phép tính đều có một đối xứng thần kỳ gọi là *phép Frobenius*). Nhiều định lý lớn đã được chứng minh xong ở đặc số $$p$$ nhưng lại bế tắc hoàn toàn ở đặc số $$0$$. Khi mới 24 tuổi, trong bài báo mốc năm 2012, Scholze đã sáng tạo ra **không gian perfectoid** và một cỗ máy phiên dịch gọi là **phép nghiêng** (*tilting*), biến những hiện tượng từng bị coi là cơn ác mộng (như *phân nhánh vô hạn*) thành chính chiếc cầu nối thông suốt giữa hai thế giới.

**Mạch bài học:** Kiến thức cần nhớ (tính tay số $$5$$-adic, phép màu Frobenius ở đặc số $$p$$, vì sao phép nhớ tạo ra bức tường) → Đặc số hỗn hợp → Giải thích 4 bước: trích căn bậc $$p$$, không gian perfectoid, phép nghiêng $$X \mapsto X^\flat$$ và đơn đạo trọng số → Tác động nền tảng & toán học cô đặc.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tự kiểm tra bằng tay phép cộng/khoảng cách trong số $$5$$-adic và đẳng thức Frobenius $$(x+y)^p = x^p + y^p$$ ở đặc số $$p$$.
- Giải thích khó khăn của **đặc số hỗn hợp** (*mixed characteristic*) và lý do phép "nhớ" làm lệch pha giữa $$\mathbb{Q}_p$$ và $$\mathbb{F}_p((t))$$.
- Hiểu mạch 4 bước của **không gian perfectoid** và **phép nghiêng** (*tilting*): vì sao gắn thêm vô hạn căn bậc $$p$$ lại xóa được sự khác biệt về phép nhớ.
- Nêu ít nhất hai lĩnh vực ứng dụng (giả thuyết đơn đạo trọng số, đối đồng điều $$p$$-adic / đối đồng điều lăng trụ, Langlands địa phương).
- Phân biệt Huy chương Fields 2018 (tập trung vào perfectoid) với chương trình **toán học cô đặc** (*condensed mathematics*, cùng Clausen) ra đời sau đó.

**Kiến thức cần có.** Số học modulo $$p$$, khai triển nhị thức Newton, và khái niệm cơ bản về vành/trường. Không cần biết trước về lược đồ hay không gian adic.

**Liên hệ trong khóa học.** Các bài gần gũi về hình học số học: [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), [Wiles / Fermat]({{ site.baseurl }}/contents/vi/chapter08/08_03_Wiles_Fermat/), [mật mã / lý thuyết số]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) (động lực đến từ số $$p$$-adic; không khẳng định perfectoid có "ứng dụng trong mật mã"). Về các giải thưởng cho cả sự nghiệp: [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

---

## Kiến thức cần nhớ: Số $$p$$-adic, Đặc số $$p$$ và "Bức tường phép nhớ"

### 1. Số $$p$$-adic là gì? (Tính tay với $$p = 5$$)
Trong giải tích thực, khoảng cách giữa $$a$$ và $$b$$ là $$\vert a - b\vert$$. Trong thế giới **$$5$$-adic**, hai số càng **gần nhau** nếu hiệu của chúng chia hết cho lũy thừa càng cao của $$5$$: viết $$n = 5^k \cdot m$$ (với $$5 \nmid m$$), ta định nghĩa chuẩn $$5$$-adic $$\vert n\vert_5 = 5^{-k}$$.

Hãy tự kiểm tra hai phép tính gây kinh ngạc trong vành số nguyên $$5$$-adic $$\mathbb{Z}_5$$:
- **Khoảng cách:** $$\vert 26 - 1\vert_5 = \vert 5^2\vert_5 = 1/25 = 0{,}04$$; còn $$\vert 626 - 1\vert_5 = \vert 5^4\vert_5 = 1/625 = 0{,}0016$$ — tức $$626$$ cực kỳ gần $$1$$!
- **Chuỗi vô hạn hội tụ về $$-1$$:** Xét chuỗi $$S = 4 + 4\cdot 5 + 4\cdot 5^2 + 4\cdot 5^3 + \cdots$$ Trong số thực, chuỗi này nổ ra $$+\infty$$. Nhưng trong $$\mathbb{Z}_5$$, số hạng thứ $$k$$ có chuẩn $$5^{-k} \to 0$$ nên chuỗi **hội tụ**! Ta cộng thêm $$1$$ vào $$S$$ (nhớ sang hàng kế tiếp hệt như cộng tiểu học trong hệ cơ số 5!):
  - Hàng đơn vị: $$1 + 4 = 5 = 0$$ (nhớ $$1$$ sang hàng $$5$$).
  - Hàng $$5$$: $$1 + 4 = 5 = 0$$ (nhớ $$1$$ sang hàng $$5^2$$).
  - Cứ thế mãi mãi → $$1 + S = 0 \implies S = -1$$! (Kiểm tra bằng công thức cấp số nhân: $$4 \cdot \frac{1}{1 - 5} = -1$$!)

Làm đầy $$\mathbb{Q}$$ theo chuẩn $$p$$-adic cho ta **trường số $$p$$-adic** $$\mathbb{Q}_p$$ (mọi phần tử là chuỗi $$\sum_{k \ge k_0} a_k p^k$$ với $$a_k \in \{0, \dots, p-1\}$$). Ngành **hình học số học $$p$$-adic** dùng $$\mathbb{Q}_p$$ làm kính lúp để nghiên cứu nghiệm phương trình đa thức và biểu diễn Galois tại từng số nguyên tố $$p$$.

### 2. Thế giới đặc số $$p$$ và phép màu Frobenius (Tính tay với $$p = 3$$)
Bây giờ hãy nhìn "người anh em song sinh" của $$\mathbb{Q}_p$$: đó là trường chuỗi Laurent $$\mathbb{F}_p((t))$$ gồm các chuỗi $$\sum_{k \ge k_0} a_k t^k$$ với hệ số $$a_k \in \mathbb{F}_p = \{0, \dots, p-1\}$$, chỉ khác là ta thay số nguyên tố $$p$$ bằng biến hình thức $$t$$ và đặt $$p = 0$$ (**đặc số $$p$$**)!

Thế giới đặc số $$p$$ có một siêu năng lực mà đặc số $$0$$ không có: **phép nâng lũy thừa $$p$$ (phép Frobenius)** $$\varphi(x) = x^p$$ bảo toàn phép cộng! Thử ngay với $$p = 3$$:

$$
(x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3 \;\equiv\; x^3 + y^3 \pmod 3.
$$

Mọi hệ số nhị thức $$\binom{p}{k}$$ ở giữa đều chia hết cho $$p$$ nên biến mất sạch! Nhờ phép Frobenius là đồng cấu vành, hình học đại số ở đặc số $$p$$ dễ kiểm soát hơn rất nhiều.

### 3. Bức tường ngăn cách: "Phép nhớ" trong đặc số hỗn hợp
Nếu $$\mathbb{Q}_p$$ (chuỗi theo $$p$$) và $$\mathbb{F}_p((t))$$ (chuỗi theo $$t$$) trông giống nhau như hai giọt nước, tại sao không thể đổi $$p \leftrightarrow t$$ là xong? Hãy thử cộng hai số trong $$\mathbb{Q}_5$$ và $$\mathbb{F}_5((t))$$:
- Trong $$\mathbb{F}_5((t))$$: $$(3 + 0\cdot t) + (4 + 0\cdot t) = 2 + 0\cdot t$$ (vì $$3 + 4 = 7 \equiv 2 \pmod 5$$, **không có nhớ**!).
- Trong $$\mathbb{Q}_5$$: $$(3 + 0\cdot 5) + (4 + 0\cdot 5) = 2 + \mathbf{1}\cdot 5$$ (**có nhớ 1 sang hàng kế tiếp**!).

Chính sự chênh lệch do **phép nhớ** (tức bản chất của **đặc số hỗn hợp**: thớ tổng quát $$\mathbb{Q}_p$$ có đặc số $$0$$, còn thớ đặc biệt $$\mathbb{F}_p = \mathbb{Z}_p/p\mathbb{Z}_p$$ có đặc số $$p$$) đã ngăn không cho ta chuyển trực tiếp bài toán từ $$\mathbb{Q}_p$$ sang $$\mathbb{F}_p((t))$$!

![Mixed characteristic]({{ site.baseurl }}/img/chapter_img/scholze_mixed_char.svg)

*Hình (minh họa ý tưởng). Thớ tổng quát đặc số 0 và thớ đặc biệt đặc số $$p$$ cùng nằm trong một "họ".*

---

## 1. Giải thích: Không gian Perfectoid và Phép nghiêng xóa "phép nhớ" như thế nào?

Làm sao Peter Scholze bắc được cây cầu song ánh giữa hai thế giới vốn bị chia cắt bởi phép nhớ? Hãy đọc chậm chuỗi 4 bước thiên tài này:

![Tilting bridge]({{ site.baseurl }}/img/chapter_img/scholze_tilting.svg)

*Hình (minh họa ý tưởng). Phép nghiêng như một cây cầu chuyển thông tin giữa hai đặc số.*

#### Bước 1: Gắn thêm vô hạn căn bậc $$p$$ — Trở nên "Perfectoid"
Ở đặc số $$p$$, một trường gọi là **hoàn hảo** (*perfect*) nếu phép Frobenius $$x \mapsto x^p$$ là song ánh — tức *mọi phần tử đều rút được căn bậc $$p$$* (ví dụ mở rộng $$\mathbb{F}_p((t))$$ bằng cách gắn thêm $$t^{1/p}, t^{1/p^2}, t^{1/p^3}, \dots$$ rồi làm đầy).

Ở đặc số $$0$$ ($$\mathbb{Q}_p$$), ta làm điều tương tự: cố ý nhảy thẳng vào vùng **phân nhánh vô hạn** bằng cách gắn thêm toàn bộ dãy căn bậc $$p$$ của $$p$$:

$$
K \;=\; \widehat{\mathbb{Q}_p\bigl(p^{1/p},\; p^{1/p^2},\; p^{1/p^3},\; \dots\bigr)}.
$$

Đây là ví dụ mẫu mực của một **trường perfectoid**: một trường đầy đủ ở đặc số hỗn hợp có đủ căn bậc $$p$$ lặp vô hạn sao cho ánh xạ $$x \mapsto x^p$$ là toàn ánh trên vành thương $$\mathcal{O}_K / p\mathcal{O}_K$$.

#### Bước 2: Định nghĩa Phép nghiêng (Tilting) $$K \mapsto K^\flat$$ bằng dãy căn bậc $$p$$
Bây giờ ta xây "phiên bản đặc số $$p$$" của $$K$$, ký hiệu là $$K^\flat$$ (đọc là *K-flat*): mỗi phần tử của $$K^\flat$$ là một **dãy vô hạn tương thích** các căn bậc $$p$$:

$$
x = \bigl(x^{(0)},\; x^{(1)},\; x^{(2)},\; \dots\bigr) \quad \text{sao cho} \quad \bigl(x^{(n+1)}\bigr)^p = x^{(n)}.
$$

- **Phép nhân** định nghĩa ngay theo từng tọa độ: $$(x \cdot y)^{(n)} = x^{(n)} y^{(n)}$$.
- **Phép cộng (đây là phép màu!):** ta không thể cộng thẳng tọa độ vì $$\bigl(x^{(n+1)} + y^{(n+1)}\bigr)^p \neq x^{(n)} + y^{(n)}$$ do sai số chia hết cho $$p$$. Nhưng nếu lấy lũy thừa $$p^m$$ rồi cho $$m \to \infty$$:

$$
(x + y)^{(n)} \;=\; \lim_{m \to \infty} \bigl(x^{(n+m)} + y^{(n+m)}\bigr)^{p^m}.
$$

**Tự kiểm tra bằng tay vì sao phép nhớ biến mất:** Khi nâng lên lũy thừa $$p^m$$, mọi số hạng "nhớ" sinh ra đều chia hết cho $$p^m$$ nên trong chuẩn $$p$$-adic chúng co về $$0$$ với tốc độ $$p^{-m} \to 0$$! Và hãy thử tính $$p \cdot x$$ trong $$K^\flat$$: phần tử $$p^\flat = (p, p^{1/p}, p^{1/p^2}, \dots)$$ chính là biến $$t$$, còn tổng $$1 + 1 + \cdots + 1$$ ($$p$$ lần) cho giới hạn $$\lim_{m\to\infty} p^{p^m} = 0$$ trong $$K^\flat$$ — nghĩa là $$K^\flat$$ có **đặc số $$p$$**! Cụ thể hơn:

$$
\widehat{\mathbb{Q}_p(p^{1/p^\infty})}^\flat \;\simeq\; \widehat{\mathbb{F}_p((t^{1/p^\infty}))}.
$$

#### Bước 3: Định lý tương đương (Tilting Equivalence) cho Không gian Perfectoid
Phát hiện nền tảng của Fontaine–Wintenberger (1979) cho thấy nhóm Galois của $$K$$ và $$K^\flat$$ đẳng cấu với nhau. Bước nhảy vọt tầm Fields của **Peter Scholze (2012)** là nâng phép nghiêng từ *một điểm* (trường) lên **toàn bộ hình học** (**không gian perfectoid**, dán từ phổ của các đại số perfectoid theo ngôn ngữ không gian adic của Huber):
- Hai không gian perfectoid $$X$$ (đặc số $$0$$) và $$X^\flat$$ (đặc số $$p$$) có **cùng không gian tô pô** và **cùng phạm trù các phủ étale** (do đó cùng đối đồng điều étale!).

#### Bước 4: Đưa bài toán khó từ đặc số 0 sang đặc số $$p$$ để giải rồi đưa về
Một ứng dụng kinh điển ngay trong bài báo 2012 của Scholze là **giả thuyết đơn đạo trọng số** (*weight-monodromy conjecture*): Deligne đã chứng minh nó ở đặc số $$p$$ từ năm 1980, nhưng ở đặc số $$0$$ nó bế tắc suốt 30 năm. Scholze nhúng đa tạp xạ ảnh (đặc số $$0$$) vào không gian xạ ảnh perfectoid $$\mathbb{P}^{n, \text{perf}}$$, **nghiêng** sang đặc số $$p$$, dùng kết quả của Deligne để chứng minh trên không gian nghiêng, rồi chuyển ngược đối đồng điều về đặc số $$0$$!

Tóm tắt mạch chứng minh:

$$
\text{Đặc số hỗn hợp } (\mathbb{Q}_p)
\;\xrightarrow{\text{Gắn } p^{1/p^\infty}}\;
\text{Không gian Perfectoid } X
\;\xrightarrow{\text{Phép nghiêng } (\cdot)^\flat}\;
\text{Đặc số } p \; (X^\flat)
\;\xrightarrow{\text{Frobenius}}\;
\text{Giải & Chuyển ngược}.
$$

---

## 2. Tác động: không chỉ một định lý, mà là viết lại hạ tầng

Ảnh hưởng của hình học perfectoid lan tỏa khắp hình học số học hiện đại:

- **Đối đồng điều $$p$$-adic và Đối đồng điều lăng trụ (*prismatic cohomology*):** Cùng Bhargav Bhatt và các cộng sự, Scholze thống nhất hàng loạt lý thuyết đối đồng điều rời rạc (étale, de Rham, crystalline) vào chung một mái nhà duy nhất.
- **Đa tạp Shimura và Langlands địa phương:** Biến không gian moduli các dạng modular $$p$$-adic thành không gian perfectoid (mở đường cho chương trình **Fargues–Scholze** về hình học hóa tương ứng Langlands địa phương).
- **Thay đổi ngôn ngữ nghiên cứu:** Sau bài báo *Perfectoid spaces* (*Publ. Math. IHÉS*, 2012), các bài báo hình học $$p$$-adic mặc định người đọc đã "nói được" ngôn ngữ perfectoid.

**Nền tảng tiếp theo: Toán học cô đặc (*Condensed Mathematics*).** Sau Huy chương Fields 2018, Scholze cùng **Dustin Clausen** phát triển *toán học cô đặc* nhằm thống nhất giải tích hàm, tô pô và đại số ở tầng nền tảng. Cần phân biệt rạch ròi: Fields 2018 trao cho **không gian perfectoid và hình học $$p$$-adic**; toán học cô đặc là chương trình nối tiếp về sau.

---

## 3. Vị trí trong Chương 2 và điều nghịch lý

| Kiểu thành tựu được trao huy chương | Ví dụ |
|-----------------|--------|
| Giải một giả thuyết cổ điển | Perelman (Poincaré / hình học hóa) |
| Tìm chính xác cấu hình tối ưu | Viazovska ($$E_8$$) |
| Chứng minh một bổ đề so sánh then chốt | Ngô (Bổ đề Cơ bản) |
| **Viết lại nền tảng / hệ tọa độ** | **Scholze (perfectoid)** |

**Nghịch lý đáng nhớ:** Trong lý thuyết số cổ điển, mở rộng trường phân nhánh càng mạnh càng bị coi là "ác mộng" khó kiểm soát. Vậy mà Scholze lại **cố ý đi thẳng vào vùng phân nhánh vô hạn cực mạnh** (gắn thêm vô hạn căn bậc $$p$$) để đổi lấy một phép đối xứng hoàn hảo khiến bức tường giữa đặc số 0 và đặc số $$p$$ sụp đổ!

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|---------|
| "Perfectoid thay thế mọi lược đồ." | **Sai** | Đây là một lớp đối tượng mạnh bổ trợ cho hình học $$p$$-adic, không thay thế toàn bộ lược đồ cổ điển. |
| "Phép nghiêng xóa bỏ số học." | **Sai** | Nó sắp xếp lại thông tin; số học quay trở lại sau khi chuyển ngược kết quả. |
| "Chỉ là một định lý riêng lẻ." | **Sai** | Nó thay đổi nền tảng và ngôn ngữ của cả lĩnh vực. |
| "Toán học cô đặc là toàn bộ lý do của Fields 2018." | **Sai** | Toán học cô đặc là chương trình sau này (cùng Clausen); lời trích dẫn 2018 tập trung vào perfectoid. |
| "Chỉ thuần đại số, không có hình học." | **Sai** | Không gian adic, phủ étale và đối đồng điều là trung tâm. |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Scholze_Perfectoid/`.

**Thứ tự xem gợi ý**

1. Video của IMU về Scholze nhận giải Fields: [YouTube](https://www.youtube.com/watch?v=jGHyAqztdLY).  
2. Weinstein giới thiệu không gian perfectoid: [YouTube](https://www.youtube.com/watch?v=RApkRqoiZ1I).  
3. Bài chân dung trên Quanta: [link](https://www.quantamagazine.org/peter-scholze-becomes-one-of-the-youngest-fields-medalists-ever-20180801/).

**Nhắc lại:** perfectoid là một **bộ công cụ** cho hình học $$p$$-adic, không thay thế các lược đồ cổ điển.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Scholze_Perfectoid/transcripts/` · trạng thái: `research/video-research/Scholze_Perfectoid/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Scholze_Perfectoid_jGHyAqztdLY_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Scholze_Perfectoid/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=jGHyAqztdLY  
2. https://www.youtube.com/watch?v=RApkRqoiZ1I  
3. https://www.simonsfoundation.org/2018/08/01/fields-medal-video-peter-schloze/  
4. https://www.carmin.tv/en/collections/fields-medallists-2018/video/interview-at-cirm-peter-scholze  
5. https://arxiv.org/search/?query=perfectoid+Scholze&searchtype=all  
6. https://www.quantamagazine.org/peter-scholze-becomes-one-of-the-youngest-fields-medalists-ever-20180801/  
7. https://plus.maths.org/ps  
8. https://en.wikipedia.org/wiki/Perfectoid_space  
9. https://en.wikipedia.org/wiki/Peter_Scholze  
10. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018  
11. https://en.wikipedia.org/wiki/P-adic_number  
12. https://www.mathematics.uni-bonn.de/people/scholze  

### Bộ tư liệu nghiên cứu

13. Bộ tư liệu của khóa học: `research/video-research/Scholze_Perfectoid/`.

1. IMU, Huy chương Fields 2018 — Peter Scholze.  
2. **P. Scholze**, *Perfectoid spaces*, *Publ. Math. IHÉS* (2012).  
3. Các bài tổng quan / bài giảng về perfectoid (ghi chú Berkeley; các loạt bài giảng).  
4. Bối cảnh: toán học cô đặc (Scholze–Clausen); nên đọc sau khi đã hiểu perfectoid.  
5. Nhập môn: số $$p$$-adic, định giá, mở rộng phân nhánh (mức sơ lược).

---

## Hướng đi tiếp

- Tìm hiểu Langlands địa phương và đa tạp Shimura trong hình học $$p$$-adic.  
- Đọc một bài chân dung phổ thông cùng với một phần mở đầu kỹ thuật (hai kiểu người đọc).  
- So sánh với bài [Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) và bài [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/).  
- Ghi lại một câu hỏi cụ thể, ví dụ "phép bỏ nghiêng không duy nhất có ý nghĩa gì trong thực tế?"  
- Nếu thích phần nền tảng: xem một bài giảng ngắn về vị trí pro-étale trước khi đọc các bài báo nặng.

## Video tham khảo

- **Xem trước:** [Fields Medal Winner 2018 Peter Scholze](https://www.youtube.com/watch?v=jGHyAqztdLY) — International Mathematical Union, tiếng Anh. Video giới thiệu Scholze và công trình được giải Fields; nên xem trước khi đọc bài.
- [Fields Medal Symposium 2021: Jared Weinstein introduces Perfectoid Spaces](https://www.youtube.com/watch?v=RApkRqoiZ1I) — Fields Institute, tiếng Anh. Jared Weinstein giới thiệu không gian perfectoid; nên xem sau khi đã nắm ý chính của bài.
