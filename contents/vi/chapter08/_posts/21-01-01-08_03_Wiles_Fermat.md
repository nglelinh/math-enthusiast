---
layout: post
title: "Andrew Wiles: Modularity và Định lý Cuối Fermat (Abel 2016)"
chapter: '08'
order: 3
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

**Sir Andrew J. Wiles** (Đại học Oxford) nhận **Giải Abel năm 2016**

> “for his stunning proof of Fermat’s Last Theorem by way of the modularity conjecture for semistable elliptic curves, opening a new era in number theory.”  
> — [Lời trao giải của Ủy ban Abel](https://abelprize.no/abel-prize-laureates/2016)

(Tạm dịch: "vì chứng minh xuất sắc Định lý Cuối cùng của Fermat thông qua giả thuyết modular cho các đường cong elliptic nửa ổn định, mở ra một kỷ nguyên mới cho lý thuyết số.")

Bài này đi sâu vào các câu hỏi: Định lý Fermat nói gì; làm thế nào một phát biểu về phương trình nghiệm nguyên lại trở thành phát biểu về đường cong elliptic và dạng modular; Wiles thực sự chứng minh gì về **tính modular của đường cong nửa ổn định**; và vì sao Ủy ban Abel coi đó là **một phương pháp mở ra kỷ nguyên mới**, chứ không chỉ là lời giải của một phương trình. Tài liệu chính thức: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể: phát biểu chính xác Định lý Fermat với số nguyên $$n\ge 3$$; giải thích ở mức ý tưởng chiến lược Frey → Ribet → tính modular → mâu thuẫn; phân biệt kết quả của Wiles cho đường cong nửa ổn định với định lý modular đầy đủ được chứng minh sau đó (Breuil–Conrad–Diamond–Taylor); nêu ngắn gọn mối liên hệ giữa tính modular, biểu diễn Galois và hàm $$L$$; tránh nhầm "Định lý Fermat đã được chứng minh" với "mọi phương trình nghiệm nguyên đã được giải" hay "chương trình Langlands đã xong".

**Kiến thức cần có.** Số nguyên, đa thức, đường cong cho bởi phương trình. Không cần biết trước về dạng modular. Bài liên quan: [Định lý Fermat (Chương 5)]({{ site.baseurl }}/contents/vi/chapter05/05_08_Fermat_Last_Theorem/), [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/).

---

## 1. Bài toán chờ hơn ba thế kỷ

**Định lý Cuối cùng của Fermat.** Với mọi số nguyên $$n \ge 3$$, không tồn tại các số nguyên dương $$a,b,c$$ thỏa mãn

$$
a^n + b^n = c^n.
$$

Khoảng năm 1637, Pierre de Fermat ghi bên lề một cuốn sách rằng ông có "một chứng minh tuyệt vời" nhưng lề sách quá hẹp để viết ra. Trước thập niên 1990, không có chứng minh tổng quát nào được giới toán học chấp nhận. Qua nhiều thế kỷ, người ta chứng minh được từng trường hợp riêng: Fermat với $$n=4$$ (phương pháp xuống thang vô hạn); Euler và những người khác với các số mũ nhỏ; Kummer dùng lý thuyết số đại số cho các số nguyên tố chính quy; máy tính kiểm tra cho nhiều khoảng số mũ. Nhưng không phần nào trong số đó là một chứng minh chung cho mọi $$n\ge 3$$.

Lời giải cuối cùng **không** quy về đại số sơ cấp. Nó viết lại bài toán nghiệm nguyên bằng ngôn ngữ **đường cong elliptic** và **dạng modular**, rồi dùng các công cụ sâu của hình học số học. Giải Abel 2016 ghi nhận cả định lý lẫn việc đổi mới phương pháp. Đây là loại thành tựu cả đời mà chương này muốn giúp bạn nhận ra: công chúng nhớ đến phương trình, còn lời trao giải nhấn mạnh **phương pháp mở ra một kỷ nguyên**.

---

## 2. Đường cong elliptic xuất hiện

Sau một phép biến đổi chuẩn, một đường cong elliptic trên $$\mathbb{Q}$$ có thể viết dưới dạng một đường bậc ba không suy biến

$$
y^2 = x^3 + Ax + B
$$

với $$A,B\in\mathbb{Q}$$ (biệt thức khác 0). Các điểm hữu tỷ cùng với điểm ở vô cùng tạo thành một nhóm abel hữu hạn sinh; đó là **định lý Mordell–Weil**. Mỗi đường cong elliptic còn có một **hàm $$L$$** $$L(E,s)$$ chứa thông tin số học về nó; tính modular nối đối tượng giải tích này với một dạng modular.

**Ý tưởng của Frey (thập niên 1980).** Giả sử phương trình $$a^n+b^n=c^n$$, $$n\ge 3$$ có nghiệm không tầm thường. Từ nghiệm đó ta dựng được **đường cong Frey**, có tính chất số học bất thường đến mức (theo giả thuyết modular) nó không thể là modular. Để biến lập luận gần đúng này thành định lý cần đến công trình của Serre, Ribet và nhiều người khác.

Bước chuyển quan trọng về tư duy là: câu hỏi "phương trình có nghiệm nguyên hay không" trở thành câu hỏi "**những đường cong elliptic nào có thể tồn tại**" trong bức tranh phân loại theo tính modular. Khi thảo luận trong nhóm, nên dừng lại ở điểm này: đây không chỉ là một mẹo kỹ thuật, mà là viết lại bài toán bằng ngôn ngữ hình học số học.

---

## 3. Tính modular là động lực chính

**Định lý modular** (trước đây là giả thuyết Taniyama–Shimura–Weil) nói rằng, nói một cách đại khái, mỗi đường cong elliptic $$E$$ trên $$\mathbb{Q}$$ tương ứng với một dạng modular, tức là một hàm giải tích trên nửa mặt phẳng trên

$$
\mathbb{H} = \{ z\in\mathbb{C} : \operatorname{Im}(z)>0 \}
$$

thỏa mãn các quy luật biến đổi rất chặt dưới các nhóm con đồng dư của $$\mathrm{SL}_2(\mathbb{Z})$$. Qua tương ứng này, tính chất số học của đường cong được phản ánh trong các hệ số Fourier và hàm $$L$$ của dạng modular.

**Ken Ribet** chứng minh định lý hạ mức (level-lowering), cho thấy đường cong Frey dựng từ một phản ví dụ của Định lý Fermat **không thể là modular**. Do đó:

> Nếu chứng minh được tính modular cho lớp đường cong liên quan, Định lý Fermat sẽ suy ra.

**Wiles** chứng minh tính modular cho lớp then chốt là các đường cong **nửa ổn định** (semistable) trên $$\mathbb{Q}$$. Tính nửa ổn định là một điều kiện về kiểu rút gọn tại các số nguyên tố; đường cong Frey thuộc lớp này. Phương pháp của ông, gồm **lý thuyết biến dạng của biểu diễn Galois** và tiêu chuẩn số cho **định lý nâng modular** (modularity lifting), đã trở thành công cụ chuẩn của ngành. Lỗ hổng trong bản chứng minh đầu tiên được sửa cùng với **Richard Taylor** (phương pháp Taylor–Wiles).

Sau đó **Breuil–Conrad–Diamond–Taylor** chứng minh tính modular cho **mọi** đường cong elliptic trên $$\mathbb{Q}$$, không chỉ các đường cong nửa ổn định. Lời trao giải Abel viết rất cẩn thận: "modularity conjecture for **semistable** elliptic curves", đúng với lịch sử. Mục tiêu 6 của phần thảo luận: đọc kỹ lời trao giải là một kỹ năng, không phải chi tiết trang trí.

---

## 4. Khung lập luận (ý tưởng chứng minh)

1. Giả sử $$a^n+b^n=c^n$$, $$n\ge 3$$, $$abc\neq 0$$.  
2. Dựng đường cong Frey từ $$(a,b,c)$$.  
3. Theo Ribet: đường cong này không modular.  
4. Theo Wiles (trường hợp nửa ổn định): đường cong này phải modular.  
5. Mâu thuẫn. Vậy không tồn tại $$(a,b,c)$$ như vậy.

Đây là **ý tưởng**. Phần kỹ thuật nặng nằm ở bước 4: kiểm soát biểu diễn Galois gắn với đường cong, nâng tính modular từ modulo một số nguyên tố lên, và kiểm tra các giả thiết để áp dụng được định lý nâng. Khi thảo luận, trình bày rõ ràng các bước 1–5 đã đủ để phân biệt hiểu thật với chỉ nhắc lại khẩu hiệu. Bài tập A4 kiểu "ý tưởng chứng minh" trong khóa học chính là để luyện khung này, chứ không phải giả vờ đã đọc hết bài báo trên Annals năm 1995.

---

## 5. Biểu diễn Galois: nhìn sâu hơn

Phương pháp của Wiles nghiên cứu **biểu diễn Galois** gắn với đường cong elliptic, tức là đồng cấu

$$
\rho_{E,\ell} : \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\mathbb{Z}_\ell)
$$

(hoặc phiên bản rút gọn modulo $$\ell$$), và hỏi khi nào chúng đến từ một dạng modular. **Định lý nâng modular** nói: nếu một biểu diễn có vẻ modular khi xét modulo một số nguyên tố thì, với các giả thiết phù hợp, nó modular ở đặc số 0.

Ý tưởng này nay là cơ sở cho phần lớn chương trình Langlands với $$\mathrm{GL}_2$$ và xa hơn nữa. Chứng minh Định lý Fermat hiện đại là **lý thuyết biểu diễn**, không phải mẹo phân tích thừa số. Cụm "opening a new era" trong lời trao giải nói về phương pháp, không chỉ về việc phương trình $$a^n+b^n=c^n$$ vô nghiệm.

Về sau, định lý modular đầy đủ hỗ trợ lý thuyết giải tích của hàm $$L$$ của đường cong elliptic trong bối cảnh [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): khi so sánh hạng số học với hạng giải tích, tính modular là một phần của "từ điển" giúp giả thuyết đó có nghĩa.

---

## 6. Vì sao Ủy ban Abel nói đến "kỷ nguyên mới"

Có ba lý do cho cách nói đó.

**Phương pháp mới.** Vành biến dạng, kỹ thuật ghép Taylor–Wiles (patching), định lý nâng modular là những công cụ cốt lõi. Nhiều định lý về sau bắt đầu từ bộ công cụ Wiles để lại.

**Niềm tin mới.** Các bài toán nghiệm nguyên khó có thể được tấn công bằng tính modular và các công cụ gần với chương trình Langlands. Cách nhìn của ngành thay đổi: một số phương trình "có vẻ bất khả" lại có thể là cửa ngõ dẫn vào hình học.

**Chương trình học mới.** Lý thuyết số ở bậc sau đại học được tổ chức lại quanh tính modular, biểu diễn Galois và dạng tự đẳng cấu. Giải Abel 2016 ghi nhận cả định lý lẫn **sự đổi mới của hình học số học**.

---

## 7. Bối cảnh lịch sử (không huyền thoại hóa)

Wiles công bố chứng minh năm 1993; sau đó một lỗ hổng được phát hiện; bản sửa cùng Taylor ra đời giữa thập niên 1990 (*Annals of Mathematics*, 1995). Sách báo phổ thông đôi khi phóng đại sự đơn độc của Wiles hoặc xem nhẹ những người đi trước: Frey, Serre, Ribet, Mazur, Langlands, Taniyama, Shimura, Weil và nhiều người khác đã xây nền cho bức tranh mà Wiles hoàn tất bằng trường hợp nửa ổn định. Tài liệu của Giải Abel và các nghiên cứu lịch sử nghiêm túc đều ghi nhận chuỗi đóng góp đó.

Máy tính **không** đóng vai trò cốt lõi trong chứng minh. Việc kiểm tra bằng số các trường hợp riêng có ý nghĩa lịch sử, nhưng lời trao giải Abel nói về định lý modular, một chứng minh do con người viết.

### "Nửa ổn định" nghĩa là gì, nói ngắn gọn

Tại mỗi số nguyên tố $$p$$, một đường cong elliptic trên $$\mathbb{Q}$$ có một kiểu rút gọn, mô tả thớ đặc biệt của mô hình tối tiểu. Rút gọn **nửa ổn định** (nói gọn là khi rút gọn xấu thì đường cong có điểm nút chứ không có điểm lùi) là một điều kiện về tính chính quy của các phép rút gọn đó. Đường cong Frey dựng từ phản ví dụ của Định lý Fermat là nửa ổn định; vì vậy chứng minh tính modular cho lớp nửa ổn định chính là điều mà định lý Ribet cần. Định lý modular đầy đủ bỏ điều kiện nửa ổn định, áp dụng cho mọi đường cong elliptic trên $$\mathbb{Q}$$, gọn hơn về khái niệm và mạnh hơn cho lý thuyết hàm $$L$$; nhưng về mặt lịch sử, Định lý Fermat đã được giải quyết ngay khi có kết quả cho trường hợp nửa ổn định.

---

## 8. Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-------|
| "Wiles chỉ kiểm tra bằng máy tính." | Cốt lõi là định lý modular do con người chứng minh. |
| "Fermat đã có chứng minh tổng quát." | Trước Wiles không có chứng minh nào được chấp nhận. |
| "Wiles chứng minh tính modular cho mọi đường cong elliptic trên $$\mathbb{Q}$$. " | Ông chứng minh trường hợp **nửa ổn định**, đủ cho Định lý Fermat; trường hợp đầy đủ được chứng minh sau (BCDT). |
| "Tính modular nghĩa là chương trình Langlands đã xong." | Đó là một trường hợp lớn trong một chương trình rộng hơn nhiều. |
| "Định lý Fermat giải quyết mọi bài toán nghiệm nguyên." | Còn rất nhiều bài toán mở (BSD, hình học Diophantine ở chiều cao hơn, …). |

---

## Bài tập

1. Viết Định lý Fermat với số mũ 4 bằng lời và bằng phương trình; giải thích vì sao chứng minh một trường hợp riêng chưa phải là chứng minh tổng quát.  
2. Tóm tắt chuỗi Frey–Ribet–Wiles trong bốn gạch đầu dòng, chỉ dùng hai thuật ngữ chuyên môn là "modular" và "đường cong elliptic".  
3. Điều kiện "nửa ổn định" giúp được gì trong câu chuyện này (viết một đoạn ngắn)?  
4. **Không quá 300 từ:** diễn giải lời trao giải Abel 2016 bằng lời của bạn, nêu được phương pháp chứ không chỉ Định lý Fermat.  
5. So sánh với [bài về Định lý Fermat]({{ site.baseurl }}/contents/vi/chapter05/05_08_Fermat_Last_Theorem/): nêu hai điểm khác nhau về trọng tâm (ý tưởng chứng minh so với phương pháp của cả một sự nghiệp).  
6. **Mở rộng:** viết một đoạn giải thích biểu diễn Galois cố gắng ghi lại điều gì (đối xứng số học được biểu diễn bằng đại số tuyến tính).

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và làm quen với không khí nghiên cứu**, không thay thế chứng minh. Chi tiết: `research/video-research/wiles-fermat/`.

**Ý chính rút ra từ bộ tư liệu**

- Giải Abel 2016: Wiles chứng minh Định lý Fermat qua tính modular của đường cong **nửa ổn định**.
- Frey → Ribet → Wiles; Taylor–Wiles sửa lỗ hổng; định lý modular đầy đủ được chứng minh sau (BCDT).

**Thứ tự xem gợi ý**

1. **Cốt lõi** — Bài giảng Abel của Wiles — FLT abelian/non-abelian: [https://www.youtube.com/watch?v=4t1mgEBx1nQ](https://www.youtube.com/watch?v=4t1mgEBx1nQ).  
2. **Cốt lõi** — Darmon — Wiles' marvelous proof: [https://www.youtube.com/watch?v=oqMaziDIBYY](https://www.youtube.com/watch?v=oqMaziDIBYY).  
3. **Lịch sử** — Phỏng vấn Wiles của Giải Abel: [https://www.youtube.com/watch?v=cWKAzX5U85Q](https://www.youtube.com/watch?v=cWKAzX5U85Q).  
4. **Định hướng** — Phỏng vấn trực tiếp Wiles (Oslo): [https://www.youtube.com/watch?v=baUlp5EWhCk](https://www.youtube.com/watch?v=baUlp5EWhCk).  
5. **Định hướng** — Alex Bellos nói về Wiles và Định lý Fermat: [https://www.youtube.com/watch?v=2Pu4vZZu3JA](https://www.youtube.com/watch?v=2Pu4vZZu3JA).  
6. **Lịch sử** — INI — Ba mươi năm chứng minh (kỷ niệm Wiles): [https://www.youtube.com/watch?v=nlUimyJpWtI](https://www.youtube.com/watch?v=nlUimyJpWtI).  

**Trang chính thức**

- Trang Giải Abel 2016 về Wiles: https://abelprize.no/abel-prize-laureates/2016  

Danh sách URL đầy đủ: `research/video-research/wiles-fermat/references.md`.


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/wiles-fermat/transcripts/` · trạng thái: `research/video-research/wiles-fermat/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/wiles-fermat_4t1mgEBx1nQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu


### Bộ tư liệu nghiên cứu video (mọi URL)

Danh sách đầy đủ: `research/video-research/wiles-fermat/references.md`.

1. Abel 2016 Wiles page — https://abelprize.no/abel-prize-laureates/2016  
2. Wiles Abel lecture — FLT abelian/non-abelian — https://www.youtube.com/watch?v=4t1mgEBx1nQ  
3. Darmon — Wiles' marvelous proof — https://www.youtube.com/watch?v=oqMaziDIBYY  
4. Abel interview with Wiles — https://www.youtube.com/watch?v=cWKAzX5U85Q  
5. Live interview Wiles (Oslo) — https://www.youtube.com/watch?v=baUlp5EWhCk  
6. Alex Bellos on Wiles/FLT — https://www.youtube.com/watch?v=2Pu4vZZu3JA  
7. INI — Thirty years of proof (Wiles anniversary) — https://www.youtube.com/watch?v=nlUimyJpWtI  
8. Nature — Wiles Abel Prize — https://www.nature.com/articles/nature.2016.19552  
9. Wikipedia — Wiles's proof of FLT — https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem  
10. Wikipedia — Modularity theorem — https://en.wikipedia.org/wiki/Modularity_theorem  
11. Thư mục bộ tư liệu: `research/video-research/wiles-fermat/`.

1. [Abel 2016](https://abelprize.no/abel-prize-laureates/2016): lời trao giải, tiểu sử, bài viết phổ thông.  
2. Wiles, *Modular elliptic curves and Fermat’s Last Theorem*, Ann. of Math. 1995; bài của Taylor–Wiles.  
3. Bài tổng quan: Darmon và các tác giả khác về tính modular; sách phổ thông: Singh, *Fermat’s Enigma*.  
4. Trong khóa học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/); [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/); [Định lý Fermat ở Chương 5]({{ site.baseurl }}/contents/vi/chapter05/05_08_Fermat_Last_Theorem/).

---

## Hướng đi tiếp

- Thảo luận: các kết quả về tính modular trong thập niên 1990 đã chứng minh được gì, và còn lại gì cho những người đi sau?  
- Trình bày khung lập luận Frey–Ribet–Wiles như một ý tưởng chứng minh.  
- Nhận xét một phim tài liệu về Định lý Fermat: chỗ nào nói quá (phương pháp so với huyền thoại)?  
- Ghi lại chính xác một bài toán mở liên quan: một khía cạnh của BSD; tính modular ở chiều cao hơn; chương trình Langlands rộng hơn.  
- So sánh với [Giải Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Bài tiếp theo: [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/).

## Video tham khảo

- **Xem trước:** [Andrew Wiles: Fermat's Last theorem: abelian and non-abelian approaches](https://www.youtube.com/watch?v=4t1mgEBx1nQ) — The Abel Prize, tiếng Anh. Chính Wiles giới thiệu các hướng tiếp cận Định lý Fermat; nên xem trước khi đọc bài.
- [Henri Darmon: Andrew Wiles' marvelous proof](https://www.youtube.com/watch?v=oqMaziDIBYY) — The Abel Prize, tiếng Anh. Darmon giải thích cấu trúc chứng minh của Wiles; nên xem sau khi đã nắm ý chính của bài.
- [Andrew Wiles - The Abel Prize interview 2016](https://www.youtube.com/watch?v=cWKAzX5U85Q) — The Abel Prize, tiếng Anh. Xem thêm sau hai video trên, để nghe Wiles kể về quá trình làm việc.
