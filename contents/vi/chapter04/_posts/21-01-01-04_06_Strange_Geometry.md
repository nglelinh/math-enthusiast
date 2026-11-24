---
layout: post
title: "Đối tượng hình học lạ"
chapter: '04'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
---

Hãy thử một thí nghiệm nhỏ ngay trên bàn làm việc: cắt một dải giấy dài, xoắn một đầu đúng nửa vòng ($$180^\circ$$) rồi dán hai đầu lại thành một vòng kín. Bạn vừa cầm trên tay một **dải Möbius**. Bây giờ, lấy kéo cắt dọc theo chính giữa dải giấy đó. Trực giác bảo bạn sẽ thu được hai vòng giấy rời nhau — nhưng khi nhát kéo khép lại, trước mắt bạn chỉ có **một vòng duy nhất dài gấp đôi**!

Đó mới chỉ là màn khởi động. Toán học hiện đại còn tạo ra những không gian đi ngược trực giác mạnh mẽ hơn nhiều: một đường cong một chiều đi qua *mọi điểm* của một hình vuông, một mặt cầu nằm trong không gian ba chiều theo cách "hoang dại" đến mức vòng dây bên ngoài không thể rút ra được, hay định lý cho phép cắt một quả cầu thành hữu hạn mảnh rồi xoay ghép lại thành **hai** quả cầu y hệt ban đầu. Mỗi **đối tượng hình học lạ** không phải là trò ảo thuật, mà là một phép thử sắc bén buộc ta định nghĩa lại chính xác thế nào là "mặt", "đường cong", "biên" và "thể tích".

**Nội dung bài:** mặt không định hướng → đường cong lấp đầy → phép nhúng hoang dại → các nghịch lý dựa trên tiên đề chọn → số chiều và các ví dụ bệnh lý → vì sao chủ đề này quan trọng → hiểu lầm thường gặp, bài tập, hướng đọc tiếp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô tả **dải Möbius** và **chai Klein**, giải thích một cách sơ cấp thế nào là mặt không định hướng.
- Phát biểu thế nào là **đường cong lấp đầy** và vì sao đường cong Peano/Hilbert không mâu thuẫn với lý thuyết số chiều.
- Phác họa ý tưởng của **mặt cầu có sừng Alexander**, một phép nhúng hoang dại của $$S^2$$ vào $$\mathbb{R}^3$$.
- Giải thích ngắn gọn **nghịch lý Banach–Tarski** và vai trò của **tiên đề chọn**.
- Phân biệt "ví dụ bệnh lý cần tiên đề chọn" với "ví dụ bệnh lý fractal được dựng tường minh".
- Tránh hai hiểu lầm: "chai Klein đựng được nước trong 3D" và "đường cong lấp đầy làm tăng số chiều của miền xác định".

**Kiến thức cần có.** Biết một số thuật ngữ tôpô cơ bản sẽ có ích, nhưng bài chủ yếu dựa vào mô tả hình học trực quan. Hàm $$[0,1]\to\mathbb{R}^2$$.

---

## Bản đồ kiến thức nền: Tôpô học và hình học "bệnh lý" là gì và nghiên cứu những gì?

Khi nói đến hình học, ta thường nghĩ ngay đến thước kẻ, góc vuông và công thức diện tích. **Tôpô học** gạt bỏ hết khoảng cách và độ cong, chỉ giữ lại những tính chất không đổi khi ta kéo giãn, uốn cong liên tục mà không xé rách hay dán thêm (ví dụ: số lỗ thủng, tính liên thông, tính định hướng).

Trong bài học này, người tốt nghiệp đại học sẽ gặp ba câu hỏi nền tảng của tôpô học và lý thuyết độ đo:
1. **Tính nội tại so với phép nhúng:** Một không gian *tự nó* trông ra sao (tôpô nội tại) là chuyện hoàn toàn khác với việc *nó nằm trong không gian bao quanh* thế nào (phép nhúng). Chai Klein hoàn toàn trơn tru trong không gian 4 chiều nhưng buộc phải tự cắt trong 3 chiều; mặt cầu có sừng Alexander nội tại vẫn là mặt cầu $$S^2$$ nhưng đặt vào $$\mathbb{R}^3$$ theo kiểu rối rắm vô tận.
2. **Đâu là giả thiết tối thiểu cho một định lý?** Khi Peano dựng được đường cong liên tục phủ kín hình vuông, các nhà toán học nhận ra: "liên tục" thôi chưa đủ để giữ nguyên số chiều — ta cần thêm tính đơn ánh hai chiều (đồng phôi).
3. **Phản ví dụ tường minh so với phản ví dụ tiên đề:** Có những vật thể lạ ta vẽ và lập trình được từng bước (đường Hilbert, dải Möbius), và có những vật thể chỉ chứng minh được sự tồn tại nhờ **tiên đề chọn** mà không bao giờ cắt được bằng kéo (Banach–Tarski).

---

## 1. Mặt một phía: dải Möbius và chai Klein

Lấy một dải giấy hình chữ nhật, xoắn một đầu nửa vòng rồi dán hai đầu lại, ta được **dải Möbius**. Nếu tô màu dọc theo đường giữa, ta sẽ quay về điểm xuất phát sau khi đã đi qua cả hai "mặt" mà ban đầu ta tưởng là khác nhau. Dải Möbius chỉ có một mặt, và biên của nó chỉ gồm một đường cong khép kín. Thú vị hơn nữa: nếu bạn cắt dải Möbius theo đường cách mép $$1/3$$ bề rộng, kéo sẽ đi hết hai vòng rồi cho ra **hai vòng lồng vào nhau** — một vòng vẫn là dải Möbius nhỏ ở giữa và một vòng hai mặt dài gấp đôi!

**Chai Klein** được tạo bằng cách dán hai cặp cạnh đối diện của một hình chữ nhật: một cặp dán thẳng thành hình trụ, cặp kia dán ngược chiều (như dán hai miệng trụ lại với nhau sau khi lộn ngược một đầu). Trong $$\mathbb{R}^3$$, thao tác này không thể thực hiện nếu không cho mặt tự cắt. Xét như một mặt trừu tượng (hoặc nhúng không tự cắt trong $$\mathbb{R}^4$$), chai Klein là mặt đóng, không định hướng và không có biên. Mô hình thủy tinh trong bảo tàng chỉ là một *phép nhúng chìm* có vòng tự cắt; không tồn tại phép nhúng thật sự của chai Klein vào $$\mathbb{R}^3$$.

Một mặt là **không định hướng** khi không thể chọn chiều "thuận kim đồng hồ" một cách nhất quán trên toàn bộ mặt: nếu bạn cho một bàn tay phải trượt hết một vòng trên dải Möbius, khi quay về chỗ cũ nó sẽ biến thành bàn tay trái! Mặt không định hướng không phải là lỗi; chúng là những đối tượng hình học được phân loại cùng với mặt cầu, mặt xuyến và mặt phẳng xạ ảnh.

---

### Video ngắn: Đường cong Hilbert, từng bậc

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/hilbert-curve_vi.mp4"></video>
</div>

Đường cong bậc $$n$$ đi qua tất cả $$4^n$$ ô của lưới $$2^n \times 2^n$$ bằng một nét liền, và mỗi bậc sau là phiên bản mịn hơn của bậc trước. Độ dài tăng gấp đôi sau mỗi bậc, còn đường cong giới hạn đi qua mọi điểm của hình vuông.


### Tự tay thử: Khám phá đường cong Hilbert

<div class="mex-explainer" data-mex="hilbert" data-lang="vi"></div>


## 2. Đường cong lấp đầy

Có đường cong liên tục nào lấp kín cả một hình vuông không? Năm 1890, Giuseppe **Peano** gây chấn động giới toán học (và David **Hilbert** ngay sau đó đưa ra phiên bản trực quan hơn) khi dựng được một toàn ánh liên tục

$$
\gamma:[0,1]\to[0,1]^2.
$$

Cách dựng dùng phép lặp: đường Hilbert bậc $$1$$ đi qua $$4$$ ô vuông; bậc $$2$$ qua $$16$$ ô; bậc $$3$$ qua $$64$$ ô; bậc $$n$$ qua $$4^n$$ ô của lưới $$2^n \times 2^n$$ bằng một nét gấp khúc không tự cắt, với độ dài tăng gần gấp đôi sau mỗi bậc. Điểm kỳ diệu là vị trí của một điểm tại thời điểm $$t \in [0,1]$$ hội tụ đều khi $$n\to\infty$$, tạo nên một hàm liên tục đi qua **mọi điểm** của hình vuông $$[0,1]^2$$ (thậm chí ngoài đời thực, đường Hilbert còn được dùng trong cơ sở dữ liệu không gian để ánh xạ tọa độ 2D thành chỉ mục 1D mà vẫn giữ các điểm gần nhau ở gần nhau!).

Vì sao điều này không phá vỡ khái niệm số chiều?

- Tính liên tục thôi thì không bảo toàn số chiều. $$\gamma$$ liên tục và toàn ánh, nhưng **không đơn ánh** (có những điểm trong hình vuông mà đường cong đi qua tới 2, 3 hoặc 4 lần), nên không phải là phép đồng phôi. Thật vậy, không thể có phép đồng phôi giữa $$[0,1]$$ và $$[0,1]^2$$: nếu bỏ đi một điểm ở giữa đoạn $$[0,1]$$, đoạn thẳng đứt làm hai mảnh rời; trong khi bỏ đi một điểm bất kỳ khỏi hình vuông $$[0,1]^2$$, phần còn lại vẫn liên thông một mảnh!
- Số chiều tôpô của miền xác định vẫn là $$1$$; ảnh có số chiều tôpô $$2$$.
- Các đường cong lấp đầy điển hình không khả vi tại bất kỳ điểm nào; việc dao động vô hạn là cái giá phải trả.

Những ví dụ này buộc ta phải định nghĩa lại chính xác các khái niệm "đường cong", "quỹ đạo", "số chiều", và mở đường cho lý thuyết độ đo hình học và fractal.

---

## 3. Phép nhúng hoang dại: mặt cầu có sừng Alexander

Trong mặt phẳng 2D, định lý đường cong Jordan–Schoenflies khẳng định mọi đường tròn biến dạng liên tục (không tự cắt) đều có thể kéo giãn nhẹ nhàng về lại đường tròn chuẩn. Người ta từng tin điều tương tự cũng đúng cho mặt cầu $$S^2$$ trong không gian 3D — cho đến năm 1924, khi **J. W. Alexander** dựng ra **mặt cầu có sừng**.

Hãy hình dung một quả bóng cao su: kéo ra hai chiếc sừng gần chạm nhau, rồi từ đầu mỗi sừng lại mọc ra hai sừng nhỏ hơn ngoắc vào nhau, cứ thế lặp vô hạn lần sao cho các đầu sừng nhỏ dần về một tập Cantor các điểm giới hạn. Về mặt tôpô nội tại, đối tượng này vẫn hoàn toàn đồng phôi với mặt cầu $$S^2$$ (không hề bị rách hay dán dính). Nhưng phần không gian bên ngoài lại **không đơn liên**: một vòng dây luồn qua cặp sừng đầu tiên không thể nào co về một điểm hay rút ra ngoài mà không chạm vào mặt, vì ở mọi cấp nhỏ hơn các cặp sừng vẫn ngoắc chặt lấy nhau!

Điểm lạ ở đây là sự khác biệt sắc nét giữa **một không gian là gì** (tôpô nội tại) và **nó nằm trong một không gian khác như thế nào** (phép nhúng).

---

## 4. Nghịch lý Banach–Tarski và tiên đề chọn

**Nghịch lý Banach–Tarski** (1924): có thể chia một quả cầu đặc trong $$\mathbb{R}^3$$ thành hữu hạn mảnh (chỉ cần đúng 5 mảnh!), rồi dùng các phép dời hình cứng (quay và tịnh tiến, không kéo giãn) ghép lại thành **hai** quả cầu đặc có cùng bán kính với quả cầu ban đầu.

Điều này không mâu thuẫn với định luật bảo toàn khối lượng: các mảnh không phải là những vật thể có thể cắt bằng dao hay tia laser. Chúng là những **tập không đo được**, được dựng nhờ **tiên đề chọn** và dựa vào cấu trúc phong phú của nhóm phép quay không giao hoán $$SO(3)$$ trong không gian 3D (nó chứa một nhóm tự do hai phần tử sinh, cho phép "nhân đôi" tập hợp tương tự cách khách sạn Hilbert tách một dãy vô hạn thành hai dãy vô hạn). Không có công thức tường minh nào mô tả các mảnh như tập mở hay đa diện. Banach–Tarski là một định lý về **giới hạn của khái niệm thể tích**: ta không thể gán thể tích bất biến qua phép quay cho *mọi* tập con tùy ý của $$\mathbb{R}^3$$.

So sánh với fractal: tập Cantor và đường Koch được dựng tường minh, không cần tiên đề chọn. Banach–Tarski "lạ" theo một kiểu khác: đó là **vấn đề về nền tảng toán học**, không phải về hình học của phép lặp.

---

## 5. Một số ví dụ kinh điển khác

- **Vòng cổ Antoine:** một phép nhúng hoang dại của tập Cantor vào $$\mathbb{R}^3$$ (tạo từ chuỗi vòng xuyến lồng vào nhau vô hạn cấp), với phần bù không đơn liên.
- **Hồ Wada:** ba "hồ nước" rời nhau là các tập mở trong mặt phẳng nhưng lại có **chung hoàn toàn một đường biên fractal** — đứng ở bất kỳ điểm bờ nào, chỉ cần nhích một khoảng bé tùy ý bạn cũng chạm được cả ba hồ!
- **Mặt cầu lạ (Exotic spheres):** các đa tạp trơn đồng phôi (giống nhau về mặt tôpô) nhưng không vi phôi (khác nhau về phép tính vi phân) với mặt cầu chuẩn $$S^7$$ (John Milnor, 1956); hóa ra cấu trúc trơn trên một không gian có thể không duy nhất.
- **Biên fractal và tập Julia:** phương trình trơn nhưng tập bất biến lại không trơn.

Bài học chung: **trực giác Euclid đơn giản chỉ là phần ít phức tạp nhất của hình học**.

---

## 6. Vì sao chủ đề này quan trọng

- **Nền tảng của tôpô.** Các khái niệm "mặt", "nút", "phép nhúng" nên được định nghĩa thế nào?
- **Lý thuyết độ đo.** Tập Vitali và nghịch lý Banach–Tarski giải thích vì sao không thể áp dụng độ đo Lebesgue cho mọi tập con nếu muốn giữ tính bất biến qua phép dời hình và tính cộng tính đếm được.
- **Giải tích hình học.** Biên hoang dại xuất hiện trong các bài toán biên tự do; ý tưởng đường cong lấp đầy xuất hiện trong giải tích trên không gian metric và cả khoa học máy tính.
- **Thói quen dùng phản ví dụ.** Một phản ví dụ rõ ràng bác bỏ một giả thuyết sai nhanh hơn hàng nghìn ví dụ ủng hộ nó.

---

## 7. Hiểu lầm thường gặp

1. "Chai Klein là một cái bình 3D." Mô hình chuẩn trong $$\mathbb{R}^3$$ có tự cắt; chai Klein là một mặt trừu tượng hai chiều.
2. "Đường cong lấp đầy làm $$[0,1]$$ thành hai chiều." Miền xác định vẫn là 1 chiều; ảnh liên tục có thể là 2 chiều mà không có phép đồng phôi.
3. "Banach–Tarski chứng tỏ vật lý sai." Các mảnh không đo được không phải là một cách chia vật thể thực.
4. "Mọi đối tượng lạ đều cần tiên đề chọn." Nhiều ví dụ fractal hoặc được dựng tường minh không cần tiên đề này.
5. "Một mặt đồng phôi với mặt cầu thì luôn nằm trong không gian một cách đơn giản." Mặt cầu có sừng Alexander là phản ví dụ.
6. "Mặt không định hướng thì không tồn tại." Dải Möbius vẫn làm được bằng giấy.

---

### Lưu ý khi học hình học lạ (rút ra từ các video)

- [Video của Vsauce về Banach–Tarski](https://www.youtube.com/watch?v=s86-Z-CbaHA) rất hay để có cái nhìn tổng quan; hãy nhớ rằng các mảnh không phải là những khối có thể tích theo nghĩa vật lý.
- Các thí nghiệm với dải Möbius ([Tokieda](https://www.youtube.com/watch?v=wKV0GYvR2X8)) giúp hiểu tính không định hướng tốt hơn là chỉ đọc định nghĩa.
- Đường cong lấp đầy: liên tục và toàn ánh vẫn không đủ để kết luận về số chiều.

## Bài tập

1. Làm một dải Möbius bằng giấy; vẽ một đường dọc theo dải cho đến khi quay về điểm đầu.
2. Vì sao một toàn ánh liên tục $$[0,1]\to[0,1]^2$$ không phải là phép đồng phôi? Nêu một lý do tôpô (ví dụ: bỏ đi một điểm).
3. Viết không quá 200 từ: so sánh tôpô nội tại của $$S^2$$ với hiện tượng nhúng hoang dại.
4. Phát biểu cẩn thận nghịch lý Banach–Tarski; nêu hai yếu tố then chốt (tiên đề chọn; các phép quay trong 3D).
5. Phân biệt đối tượng lạ kiểu fractal dựng được với nghịch lý dựa vào tiên đề chọn; mỗi loại cho một ví dụ.
6. (Mở rộng) Mô tả hiện tượng biên chung của hồ Wada trong một đoạn văn.
7. (Mở rộng) Mặt cầu lạ của Milnor làm thay đổi khẳng định "đồng phôi thì có cùng cấu trúc trơn" như thế nào?
8. Viết ba câu nối bài này với [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/) và [Fractal]({{ site.baseurl }}/contents/vi/chapter04/04_03_Fractals/).

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và xây dựng trực giác**, không thay thế chứng minh hay tài liệu chuẩn. Đánh giá chi tiết: `research/video-research/strange-geometry/`.

**Thứ tự xem gợi ý**

1. **Cốt lõi** — Vsauce — The Banach–Tarski Paradox: [https://www.youtube.com/watch?v=s86-Z-CbaHA](https://www.youtube.com/watch?v=s86-Z-CbaHA).
2. **Định hướng** — Numberphile — Unexpected Shapes / dải Möbius (Tokieda): [https://www.youtube.com/watch?v=wKV0GYvR2X8](https://www.youtube.com/watch?v=wKV0GYvR2X8).
3. **Trực giác** — Numberphile — An Unexpected Twist on Möbius Strips: [https://www.youtube.com/watch?v=izIKV98Awnw](https://www.youtube.com/watch?v=izIKV98Awnw).
4. **Cốt lõi** — Numberphile — Space-Filling Curves: [https://www.youtube.com/watch?v=x-DgL49CFlM](https://www.youtube.com/watch?v=x-DgL49CFlM).
5. **Nâng cao (nhẹ)** — Mặt cầu có sừng Alexander (Wikipedia): [https://en.wikipedia.org/wiki/Alexander_horned_sphere](https://en.wikipedia.org/wiki/Alexander_horned_sphere).
6. **Định hướng** — Numberphile — Klein Bottles: [https://www.youtube.com/watch?v=AAsICMPwGPY](https://www.youtube.com/watch?v=AAsICMPwGPY).

Danh sách URL đầy đủ: `research/video-research/strange-geometry/references.md`.


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/strange-geometry/transcripts/` · trạng thái: `research/video-research/strange-geometry/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/strange-geometry_s86-Z-CbaHA_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/strange-geometry/references.md`.

### Video chính

1. Vsauce — The Banach–Tarski Paradox — https://www.youtube.com/watch?v=s86-Z-CbaHA
2. Numberphile — Unexpected Shapes / Möbius (Tokieda) — https://www.youtube.com/watch?v=wKV0GYvR2X8
3. Numberphile — An Unexpected Twist on Möbius Strips — https://www.youtube.com/watch?v=izIKV98Awnw
4. Numberphile — Space-Filling Curves — https://www.youtube.com/watch?v=x-DgL49CFlM
5. Alexander horned sphere visual topology talks — https://en.wikipedia.org/wiki/Alexander_horned_sphere
6. Numberphile — Klein Bottles — https://www.youtube.com/watch?v=AAsICMPwGPY
7. Hilbert curve / Peano curve algorithm visuals — https://www.youtube.com/watch?v=x-DgL49CFlM
8. Axiom of choice explained carefully (philosophy-math) — https://www.youtube.com/watch?v=s86-Z-CbaHA

### Video bổ sung

9. Các thí nghiệm tôpô của Tadashi Tokieda (danh sách phát Numberphile) — https://www.youtube.com/watch?v=wKV0GYvR2X8

### Bài báo, sách, khóa học mở và trang web

10. Wagon — The Banach–Tarski Paradox (Cambridge): https://www.cambridge.org/core/books/banachtarski-paradox/
11. Wikipedia — Möbius strip: https://en.wikipedia.org/wiki/M%C3%B6bius_strip
12. Wikipedia — Space-filling curve: https://en.wikipedia.org/wiki/Space-filling_curve
13. Wikipedia — Banach–Tarski paradox: https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox
14. Wikipedia — Alexander horned sphere: https://en.wikipedia.org/wiki/Alexander_horned_sphere
15. Wikipedia — Axiom of choice: https://en.wikipedia.org/wiki/Axiom_of_choice

### Trong khóa học

16. Bài liên quan: [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/), [Fractal]({{ site.baseurl }}/contents/vi/chapter04/04_03_Fractals/), [Không gian nhiều chiều]({{ site.baseurl }}/contents/vi/chapter04/04_08_Higher_Dimensions/), [Hình bất khả]({{ site.baseurl }}/contents/vi/chapter04/04_11_Impossible_Shapes/). Bộ tư liệu: `research/video-research/strange-geometry/`.

## Hướng đọc tiếp

Liên quan về logic: [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/). Độ gồ ghề theo tỉ lệ: [Fractal]({{ site.baseurl }}/contents/vi/chapter04/04_03_Fractals/). Mâu thuẫn thị giác: [Hình bất khả]({{ site.baseurl }}/contents/vi/chapter04/04_11_Impossible_Shapes/). Số chiều như một tham số: [Không gian nhiều chiều]({{ site.baseurl }}/contents/vi/chapter04/04_08_Higher_Dimensions/).


## "Lạ" so với trực giác Euclid, không có nghĩa là "sai"

Các đối tượng hình học lạ trong chương này (mặt không định hướng, khoảng cách khác thường, hình có diện tích vô hạn nhưng thể tích hữu hạn, v.v.) thường hoàn toàn **nhất quán** trong hệ tiên đề đã chọn. Cái "lạ" chỉ là chúng trái với thói quen nhìn hình phẳng của ta. Thói quen tốt trong seminar: trước khi nói "không thể", hãy nêu rõ **định nghĩa khoảng cách / tôpô / độ đo** đang dùng.

## Liên hệ với các bài khác

- [Nghịch lý]({{ site.baseurl }}/contents/vi/chapter04/04_07_Paradoxes/) phân biệt bất ngờ do định nghĩa với bất ngờ do tiên đề.
- [Vô hạn]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/) và bài thực hành ở Chương 7 về mô tả vô hạn giúp luyện ngôn ngữ về lực lượng.
- [Không gian nhiều chiều]({{ site.baseurl }}/contents/vi/chapter04/04_08_Higher_Dimensions/) cho thấy mức độ "lạ" càng tăng khi số chiều tăng, dù công thức vẫn là đại số quen thuộc.

## Thực hành

Chọn một đối tượng (hình chiếu của chai Klein, đường cong lấp đầy hình vuông, hoặc khoảng cách taxi). Viết một đoạn 150 từ: (a) định nghĩa, (b) tính chất trái trực giác, (c) vì sao nó không mâu thuẫn về logic.


## Video tham khảo

- **Xem trước:** [The Banach–Tarski Paradox](https://www.youtube.com/watch?v=s86-Z-CbaHA) — Vsauce, tiếng Anh. Giới thiệu nghịch lý Banach–Tarski; nên xem trước khi đọc bài.
- [Unexpected Shapes (Part 1) - Numberphile](https://www.youtube.com/watch?v=wKV0GYvR2X8) — Numberphile, tiếng Anh. Tokieda với các thí nghiệm về hình dạng bất ngờ; nên xem sau khi đã nắm ý chính của bài.
- [An Unexpected Twist on Möbius Strips - Numberphile](https://www.youtube.com/watch?v=izIKV98Awnw) — Numberphile, tiếng Anh. Xem thêm sau hai video trên, về dải Möbius.
