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

Từ lâu, các nhà hình học số học sống giữa hai thế giới gần giống nhau nhưng ngăn cách nhau bởi một bức tường kỳ lạ: thế giới **đặc số 0** (nơi các số nguyên thông thường và số $$p$$-adic sinh sống) và thế giới **đặc số $$p$$** (nơi ta làm toán theo modulo số nguyên tố $$p$$, nên mọi phép tính đều có một đối xứng thần kỳ gọi là *phép Frobenius*). Nhiều bài toán lớn chỉ cần có thể "bê" từ thế giới này sang thế giới kia là giải được, nhưng bức tường ngôn ngữ quá dày. Khi mới 24 tuổi, trong bài báo mốc năm 2012, Scholze đã sáng tạo ra **không gian perfectoid** và một cỗ máy phiên dịch gọi là **phép nghiêng** (*tilting*), biến những hiện tượng từng bị coi là cơn ác mộng (như *phân nhánh hoang*) thành chính chiếc cầu nối thông suốt giữa hai thế giới.

Hành trình của bài học này đi qua bảy chặng:

**Hình học $$p$$-adic khó → đặc số hỗn hợp → perfectoid → phép nghiêng → đối đồng điều và ứng dụng → ảnh hưởng tới nền tảng → Fields 2018.**

Mục tiêu không phải là xây dựng không gian adic từ đầu, mà là hiểu **vấn đề nền tảng là gì**, **perfectoid giải quyết theo cách tư duy nào**, và **vì sao cả lĩnh vực thay đổi nhịp độ sau năm 2012**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích khó khăn của **đặc số hỗn hợp** (mixed characteristic) trong một đoạn văn mạch lạc (thớ tổng quát có đặc số 0 ↔ thớ đặc biệt có đặc số $$p$$).
- Phát biểu ý chính của **phép nghiêng**: một từ điển giữa một số đối tượng ở đặc số hỗn hợp và các đối tượng ở đặc số $$p$$ mà trên đó phép Frobenius là song ánh.
- Mô tả vành / không gian **perfectoid** như một lớp đối tượng phân nhánh mạnh, được thiết kế để phép nghiêng hoạt động (hiểu mục đích thiết kế quan trọng hơn thuộc danh sách tiên đề).
- Nêu ít nhất hai lĩnh vực ứng dụng (ví dụ các kết quả kiểu đơn đạo trọng số (weight-monodromy), đối đồng điều $$p$$-adic / các vành chu kỳ).
- So sánh câu chuyện về huy chương của Scholze với các giải thưởng cho "hạ tầng / nền tảng" (nền tảng cho Langlands, viết lại bằng lý thuyết biểu diễn), chứ không chỉ các giải cho "một giả thuyết".
- Biết đến **toán học cô đặc** (condensed mathematics, cùng với Clausen) như một tầng nền tảng ra đời sau; chỉ cần biết là có, không cần nắm vững.
- Đánh giá tỉnh táo giữa lời trích dẫn chuyên môn của IMU và các khẩu hiệu phổ thông kiểu "thiên tài trẻ viết lại toàn bộ toán học".

**Kiến thức cần có.** Vành và trường; ý tưởng về phép làm đầy (số nguyên $$p$$-adic $$\mathbb{Z}_p$$ và trường $$\mathbb{Q}_p$$); phép Frobenius $$x\mapsto x^p$$ trên vành đặc số $$p$$. Biết về lược đồ (scheme) thì có ích nhưng không bắt buộc; có thể hình dung đó là "các không gian hình học dán từ phổ của các vành".

**Liên hệ trong khóa học.** Các bài gần gũi về hình học số học: [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), [Wiles / Fermat]({{ site.baseurl }}/contents/vi/chapter08/08_03_Wiles_Fermat/), [mật mã / lý thuyết số]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) (động lực đến từ số $$p$$-adic; không khẳng định perfectoid có "ứng dụng trong mật mã"). Về các giải thưởng cho cả sự nghiệp: [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

---

## Bản đồ kiến thức nền: Số $$p$$-adic, Đặc số $$p$$ và Hình học số học là gì?

Nếu bạn từng nghe cụm từ "số $$p$$-adic" mà chưa kịp hình dung nó là gì, hãy thử một ví dụ nhỏ với $$p = 5$$:

- **Số $$p$$-adic ($$p$$-adic Numbers) là gì?** Thông thường, ta nói hai số gần nhau nếu hiệu của chúng nhỏ về giá trị tuyệt đối (ví dụ $$1$$ và $$1{,}001$$). Trong thế giới **$$5$$-adic**, ta định nghĩa một kiểu "khoảng cách" hoàn toàn khác: hai số nguyên càng **gần nhau** nếu hiệu của chúng chia hết cho lũy thừa càng cao của $$5$$! Do đó, $$26$$ rất gần $$1$$ (vì $$26 - 1 = 25 = 5^2$$, nên khoảng cách $$5$$-adic là $$5^{-2} = 1/25$$), còn $$626$$ còn gần $$1$$ hơn nữa (khoảng cách $$5^{-4} = 1/625$$). Khi làm đầy tập số hữu tỷ $$\mathbb{Q}$$ theo khoảng cách thông thường, ta được số thực $$\mathbb{R}$$; khi làm đầy $$\mathbb{Q}$$ theo khoảng cách $$p$$-adic, ta được trường **số $$p$$-adic** $$\mathbb{Q}_p$$ (và vành số nguyên $$p$$-adic $$\mathbb{Z}_p$$). Số $$p$$-adic đóng vai trò như một chiếc kính lúp cực mạnh để nghiên cứu phương trình nghiệm nguyên từng số nguyên tố $$p$$ một!
- **Thế giới đặc số $$p$$ đẹp ở điểm nào?** Trong trường hữu hạn $$\mathbb{F}_p$$ (hay vành chuỗi Laurent $$\mathbb{F}_p((t))$$), ta có $$p = 0$$. Điều này dẫn đến một phép tính mơ ước mà học sinh hay viết nhầm ở số thực nhưng lại **đúng tuyệt đối** ở đặc số $$p$$: $$(x + y)^p = x^p + y^p$$ (vì mọi hệ số nhị thức ở giữa đều chia hết cho $$p$$!). Do đó, ánh xạ **Frobenius** $$\varphi(x) = x^p$$ là một đồng cấu vành tự nhiên — một phép đối xứng cực mạnh mà thế giới đặc số $$0$$ (như $$\mathbb{Q}_p$$) không có.
- **Vì sao cần không gian perfectoid?** $$\mathbb{Q}_p$$ (đặc số $$0$$) và $$\mathbb{F}_p((t))$$ (đặc số $$p$$) trông giống anh em sinh đôi (cả hai đều là chuỗi lũy thừa theo $$p$$ hoặc theo $$t$$), nhưng phép cộng của $$\mathbb{Q}_p$$ có "nhớ" sang hàng kế tiếp (như $$3 + 4 = 7 = 2 + 1 \cdot 5$$) còn $$\mathbb{F}_p((t))$$ thì không! Nếu ta cố ý mở rộng $$\mathbb{Q}_p$$ bằng cách gắn thêm vô hạn căn bậc $$p$$: $$p^{1/p}, p^{1/p^2}, p^{1/p^3}, \dots$$, thì sự khác biệt khó chịu về phép nhớ ấy bỗng "tan biến" ở giới hạn, cho phép Scholze dựng một cây cầu song ánh (**phép nghiêng**) nối trực tiếp hai thế giới!

---

## 1. Vì sao hình học $$p$$-adic khó

Hình học số học thường làm việc trên vành số nguyên của một trường $$p$$-adic, ví dụ $$\mathbb{Z}_p$$ hoặc vành định giá của một mở rộng, nơi:

- thớ đặc biệt (ứng với trường thặng dư $$\mathbb{F}_p = \mathbb{Z}_p / p\mathbb{Z}_p$$) có **đặc số $$p$$**;  
- thớ tổng quát (ứng với trường thương $$\mathbb{Q}_p$$) có **đặc số $$0$$**.

Đó là **đặc số hỗn hợp** (*mixed characteristic*). Các công cụ của hình học đại số "thuần" (trên một trường, hoặc trên những vành "dễ") gặp khó khăn lớn trước:

- **phân nhánh hoang** (*wild ramification*, khi bậc của mở rộng trường chia hết cho chính số nguyên tố $$p$$);  
- định giá không rời rạc / các mở rộng phân nhánh vô hạn;  
- đối đồng điều khó kiểm soát;  
- việc so sánh giữa "thế giới đặc số $$p$$" và "thế giới đặc số 0".

Nhiều định lý sâu muốn dùng thông tin ở đặc số $$p$$ (nơi có phép Frobenius) để nói về số học ở đặc số 0, hoặc ngược lại. Không có một bộ từ điển tốt, mỗi bài toán lại phải xử lý theo một cách riêng.

![Mixed characteristic]({{ site.baseurl }}/img/chapter_img/scholze_mixed_char.svg)

*Hình (minh họa ý tưởng). Thớ tổng quát đặc số 0 và thớ đặc biệt đặc số $$p$$ cùng nằm trong một "họ".*

---

## 2. Perfectoid: phép Frobenius trở thành đẳng cấu (gần như)

Ở đặc số $$p$$, mọi vành $$R$$ đều có tự đồng cấu Frobenius $$\varphi:R\to R$$, $$x\mapsto x^p$$. Nếu $$\varphi$$ là **đẳng cấu** thì $$R$$ được gọi là **hoàn hảo** (*perfect*). Ví dụ, $$\mathbb{F}_p((t))$$ chưa hoàn hảo vì $$t$$ không có căn bậc $$p$$; nhưng nếu gắn thêm $$t^{1/p}, t^{1/p^2}, \dots$$ rồi làm đầy, ta được trường hoàn hảo $$\mathbb{F}_p((t^{1/p^\infty}))$$. Vành hoàn hảo thường dễ làm việc hơn: có thể lấy căn bậc $$p$$ một cách thoải mái, và nhiều lý thuyết đối đồng điều trở nên đơn giản hơn hẳn.

Scholze tách ra lớp đại số **perfectoid**: các vành tô pô đầy đủ, phân nhánh mạnh (với một tô pô phi Archimedes cụ thể), có một ánh xạ "kiểu Frobenius" toàn ánh modulo $$p$$, sao cho sau phép nghiêng ta bước vào thế giới các vành hoàn hảo. Định nghĩa đại số đầy đủ liên quan đến "toán học gần đúng" (*almost mathematics*), các vành chu kỳ của Fontaine, và phép hoàn hảo hóa có làm đầy. Để thảo luận, điều cần nắm là **mục đích thiết kế** hơn là danh sách tiên đề:

> Đối tượng perfectoid là những đối tượng có đủ căn bậc $$p$$ lặp vô hạn một cách nhất quán — ví dụ mẫu là làm đầy của $$\mathbb{Q}_p(p^{1/p^\infty})$$ — khiến chúng "hoàn hảo đến mức mà đặc số hỗn hợp cho phép".

**Không gian perfectoid** là các đối tượng hình học được dán từ phổ của các đại số perfectoid theo kiểu không gian adic (khuôn khổ của Huber), không phải đa tạp cổ điển trên một trường. Chúng đủ phong phú để mang đối đồng điều và tác động Galois, nhưng đủ cứng để phép nghiêng hoạt động.

Điểm cần lưu ý: perfectoid **không** thay thế mọi lược đồ. Đó là một lớp đối tượng **mạnh và linh hoạt**, nơi nhiều phép so sánh trở nên rõ ràng, giống như một "hệ tọa độ tốt" cho vùng khó của bản đồ.

---

## 3. Phép nghiêng: từ điển giữa hai thế giới

**Phép nghiêng** (*tilting*, ký hiệu $$X \mapsto X^\flat$$) gắn mỗi đối tượng perfectoid ở đặc số hỗn hợp với một đối tượng perfectoid ở đặc số $$p$$. Ví dụ kinh điển nhất là trường perfectoid $$\widehat{\mathbb{Q}_p(p^{1/p^\infty})}$$ ở đặc số $$0$$ khi "nghiêng" đi sẽ trở thành trường chuỗi Laurent hoàn hảo $$\widehat{\mathbb{F}_p((t^{1/p^\infty}))}$$ ở đặc số $$p$$ — và điều kỳ diệu của định lý Fontaine–Wintenberger (được Scholze nâng lên thành hình học cho mọi không gian perfectoid) là **nhóm Galois và cấu trúc không gian của chúng tương đương hoàn toàn**!

Tóm tắt:

$$
\{\text{perfectoid mixed char}\}
\;\overset{\text{tilt}}{\longleftrightarrow}\;
\{\text{perfectoid char }p\}.
$$

Cách suy nghĩ điển hình:

1. Phát biểu câu hỏi ở đặc số hỗn hợp (nơi rất khó tính).  
2. Chuyển (nghiêng) sang đặc số $$p$$.  
3. Giải hoặc đơn giản hóa bài toán ở đó nhờ phép Frobenius và hình học đặc số $$p$$.  
4. Chuyển ngược phần thông tin cần thiết về bài toán gốc.

Phép nghiêng **không xóa bỏ** số học, mà **sắp xếp lại** nó. Sau khi chuyển thông tin, người ta vẫn quay về bài toán số học ban đầu, nhưng đã có thêm hiểu biết mới.

### Vì sao "Frobenius là đẳng cấu" lại có ích

Phép Frobenius $$x\mapsto x^p$$ là phép biến đổi tự nhiên nhất ở đặc số $$p$$. Khi nó là đẳng cấu, nhiều dãy khớp, phép phủ và đối đồng điều trở nên kiểm soát được theo $$p$$. Hiện tượng phân nhánh hoang, vốn thường làm hỏng các ước lượng, được "hấp thụ" ngay vào định nghĩa của lớp perfectoid thay vì phải xử lý từng trường hợp.

---

## 4. Tác động: không chỉ một định lý

Ảnh hưởng của hình học perfectoid bao gồm (danh sách chưa đầy đủ):

- tiến bộ trong lý thuyết **đối đồng điều $$p$$-adic** và các định lý so sánh giữa các lý thuyết đối đồng điều;  
- cách tiếp cận mới cho **giả thuyết đơn đạo trọng số** (*weight-monodromy*, vốn đã được Deligne chứng minh ở đặc số $$p$$ — nhờ phép nghiêng, Scholze chuyển được nó sang đặc số $$0$$ cho các giao đầy đủ trong không gian xạ ảnh!);  
- ngôn ngữ mới cho **đa tạp Shimura** và hình học liên quan đến **Langlands địa phương** (đặc biệt là chương trình Fargues–Scholze);  
- công cụ cho **đối đồng điều lăng trụ** (*prismatic cohomology*) và các lý thuyết đồng điều hiện đại (cùng các cộng sự: Bhatt–Scholze, … trong các chương trình tiếp theo);  
- thay đổi trong thực tế làm toán: các bài báo sau năm 2012 thường mặc định người đọc đã "nói được" ngôn ngữ perfectoid.

![Tilting bridge]({{ site.baseurl }}/img/chapter_img/scholze_tilting.svg)

*Hình (minh họa ý tưởng). Phép nghiêng như một cây cầu chuyển thông tin giữa hai đặc số.*

### Nền tảng tiếp theo: toán học cô đặc và hình học giải tích

Sau perfectoid, Scholze (cùng **Dustin Clausen** và các cộng sự) phát triển hướng **toán học cô đặc** (*condensed mathematics*) và một kiểu hình học giải tích mới, nhằm thống nhất tô pô, giải tích và đại số ở tầng nền tảng. Huy chương Fields 2018 **tập trung** vào perfectoid / hình học $$p$$-adic; toán học cô đặc là chương trình **tiếp nối**, không nên gộp chung thành "cùng một định lý".

---

## 5. Vì sao bài này quan trọng trong chương

Chương 2 nhấn mạnh toán học ở tầm giải thưởng như những **cây cầu và những lần viết lại ngôn ngữ**. Perfectoid là một ví dụ điển hình:

| Kiểu thành tựu được trao huy chương | Ví dụ |
|-----------------|--------|
| Giải một giả thuyết cổ điển | Perelman (Poincaré / hình học hóa) |
| Tìm chính xác cấu hình tối ưu | Viazovska ($$E_8$$) |
| Chứng minh một bổ đề so sánh then chốt | Ngô (Bổ đề Cơ bản) |
| **Viết lại nền tảng** | **Scholze (perfectoid)** |

So với [Ngô]({{ site.baseurl }}/contents/vi/chapter02/): cả hai đều đưa hình học vào số học / dạng tự đẳng cấu, nhưng Ngô nhắm tới một đẳng thức so sánh cụ thể, còn Scholze thay đổi **hệ tọa độ toàn cục** của hình học $$p$$-adic.

---

## 6. Điều nghịch lý

Phân nhánh "càng mạnh" thường càng khó, vậy mà lớp perfectoid lại **cố ý** đi thẳng vào vùng phân nhánh vô hạn cực mạnh để đổi lấy phép nghiêng đẹp. Điều đáng nhớ: đôi khi phải đi **sâu hơn vào chỗ khó** mới tìm được đối xứng giúp đơn giản hóa. Tương tự các ý tưởng "compact hóa trước khi đếm" hay "nâng lên không gian phủ trước khi chiếu xuống": chọn đúng không gian quan trọng hơn cố tính toán trên không gian sai.

---

## 7. Lưu ý cho chính xác

- Huy chương Fields 2018: trọng tâm là perfectoid và hình học $$p$$-adic.  
- Nhiều kết quả là **công trình hợp tác**; luôn kiểm tra đồng tác giả của từng định lý cụ thể.  
- Bài "Perfectoid spaces" (*Publ. Math. IHÉS*, 2012) là văn bản mốc trung tâm.  
- Không khẳng định perfectoid "thay thế mọi lược đồ" hay "giải xong Langlands địa phương".

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Perfectoid thay thế mọi lược đồ." | **Sai** | Đây là một lớp đối tượng mạnh, không thay thế toàn bộ. |
| "Phép nghiêng xóa bỏ số học." | **Sai** | Nó sắp xếp lại; số học quay trở lại sau khi chuyển thông tin. |
| "Chỉ là một định lý riêng lẻ." | **Sai** | Nó thay đổi nền tảng và ngôn ngữ của cả lĩnh vực. |
| "Toán học cô đặc là toàn bộ lý do của Fields 2018." | **Sai** | Toán học cô đặc là hướng đi sau này; lời trích dẫn tập trung vào perfectoid. |
| "Chỉ thuần đại số, không có hình học." | **Sai** | Không gian, đối đồng điều và hình học adic là trung tâm. |

---

## Bài tập

1. "Đặc số hỗn hợp" là gì, nói trong một câu? Cho một ví dụ về vành.  
2. Vì sao việc phép Frobenius trở thành đẳng cấu có thể giúp kiểm soát đối đồng điều?  
3. Kể hai lĩnh vực **ngoài** phần nền tảng thuần túy có dùng ý tưởng perfectoid / hình học $$p$$-adic hiện đại.  
4. Viết một đoạn so sánh huy chương cho "một nền tảng mới" (Scholze) với huy chương cho "một bài toán tối ưu" (Viazovska).  
5. Đọc lướt phần mở đầu của một bài tổng quan về perfectoid; liệt kê ba từ khóa nên học tiếp (không gian adic, phép bỏ nghiêng (untilt), vị trí pro-étale, …).  
6. **Liên hệ trong chương.** Viết một đoạn nối phép nghiêng của Scholze với ý "hình học mở khóa giải tích" của Ngô: điểm giống và điểm khác.  
7. Giải thích vì sao "phân nhánh mạnh" lại có thể là một **lợi thế** trong định nghĩa perfectoid.  
8. Phân biệt sơ lược thớ tổng quát và thớ đặc biệt trên $$\operatorname{Spec}\mathbb{Z}_p$$.

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
- So sánh với bài [Ngô]({{ site.baseurl }}/contents/vi/chapter02/) và bài [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/).  
- Ghi lại một câu hỏi cụ thể, ví dụ "phép bỏ nghiêng không duy nhất có ý nghĩa gì trong thực tế?"  
- Nếu thích phần nền tảng: xem một bài giảng ngắn về vị trí pro-étale trước khi đọc các bài báo nặng.

## Video tham khảo

- **Xem trước:** [Fields Medal Winner 2018 Peter Scholze](https://www.youtube.com/watch?v=jGHyAqztdLY) — International Mathematical Union, tiếng Anh. Video giới thiệu Scholze và công trình được giải Fields; nên xem trước khi đọc bài.
- [Fields Medal Symposium 2021: Jared Weinstein introduces Perfectoid Spaces](https://www.youtube.com/watch?v=RApkRqoiZ1I) — Fields Institute, tiếng Anh. Jared Weinstein giới thiệu không gian perfectoid; nên xem sau khi đã nắm ý chính của bài.
