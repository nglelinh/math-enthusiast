---
layout: post
title: "Giả thuyết Birch và Swinnerton-Dyer"
chapter: '01'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

**Giả thuyết Birch–Swinnerton-Dyer (BSD)** là một bài toán Thiên niên kỷ nối hai đại lượng của một đường cong elliptic trên trường số hữu tỷ $$\mathbb{Q}$$:

- một bất biến **đại số**: **hạng** của nhóm các điểm hữu tỷ;
- một bất biến **giải tích**: bậc triệt tiêu của **hàm $$L$$** gắn với đường cong tại điểm trung tâm $$s=1$$.

Ý chính: *giá trị đặc biệt của hàm $$L$$ chứa thông tin số học.* BSD là ví dụ hiện đại tiêu biểu cho quan điểm "hàm giải tích ghi nhớ thông tin số học", cùng tinh thần với việc hàm zeta Riemann chứa thông tin về số nguyên tố, nhưng ở đây đối tượng là đường cong elliptic và các điểm hữu tỷ của nó.

Bài này không giả sử bạn đã học hình học đại số. Mục tiêu là phát biểu giả thuyết rõ ràng, giải thích vì sao tính modular quan trọng, kể ra các kết quả từng phần chính, và lưu ý các lỗi hiểu sai (mục tiêu 6) khi đọc cơ sở dữ liệu LMFDB hay tin tức về mật mã đường cong elliptic.

**Nội dung bài:** đường cong elliptic và định lý Mordell–Weil → hạng → hàm $$L$$ → phát biểu BSD → vì sao khó → bằng chứng và các định lý từng phần → các giả thuyết cùng tinh thần → hiểu lầm thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa **đường cong elliptic** trên $$\mathbb{Q}$$ ở mức đủ dùng (đường bậc ba dạng Weierstrass không kỳ dị).
- Phát biểu **định lý Mordell–Weil**: $$E(\mathbb{Q})$$ hữu hạn sinh; tách thành phần hạng và phần xoắn.
- Giải thích **hạng** $$r$$ đo phần tự do của nhóm điểm hữu tỷ (có bao nhiêu điểm cấp vô hạn độc lập).
- Phát biểu phần hạng của BSD: $$r$$ bằng bậc triệt tiêu của $$L(E,s)$$ tại $$s=1$$; nêu tóm tắt công thức cho hệ số dẫn đầu (chu kỳ, regulator, phần xoắn, số Tamagawa, $$|Ш|$$).
- Giải thích vì sao **tính modular** quan trọng để định nghĩa và thác triển $$L(E,s)$$.
- Kể ít nhất một kết quả từng phần: Coates–Wiles; Gross–Zagier / Kolyvagin; các tiến bộ về phân bố hạng (Bhargava và cộng sự, ở mức biết tên).
- Phân biệt mật mã đường cong elliptic (ECC, dùng nhóm điểm hữu hạn trên trường hữu hạn) với BSD (số học trên $$\mathbb{Q}$$).

**Kiến thức cần có.** Đồng dư modulo; hiểu "nhóm điểm" như một cấu trúc đại số. Không cần học hình học đại số. Biết sơ qua về hàm zeta từ [bài Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) sẽ có ích, nhưng không bắt buộc.

**Liên hệ với khóa học.** **Mục tiêu 1**; [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) (hàm $$L$$ và không điểm); [Mật mã ECC]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) (đường cong elliptic trong thực tế).

---

## 1. Đường cong elliptic và điểm hữu tỷ

Một **đường cong elliptic** trên $$\mathbb{Q}$$ (sau một phép đổi biến) có thể viết dưới dạng Weierstrass

$$
y^2 = x^3 + Ax + B
$$

với $$A,B\in\mathbb{Q}$$ và biệt thức khác 0 (không kỳ dị). Tập các điểm hữu tỷ $$E(\mathbb{Q})$$, cùng với **điểm ở vô cùng**, tạo thành một nhóm abel với **phép cộng dây cung–tiếp tuyến**: đường thẳng qua hai điểm cắt đường cong tại một điểm thứ ba; lấy đối xứng điểm này qua trục $$x$$ ta được tổng của hai điểm.

**Định lý Mordell–Weil.** $$E(\mathbb{Q})$$ là nhóm hữu hạn sinh:

$$
E(\mathbb{Q}) \cong \mathbb{Z}^{r} \oplus E(\mathbb{Q})_{\mathrm{tors}}.
$$

Ở đây $$E(\mathbb{Q})_{\mathrm{tors}}$$ là nhóm xoắn hữu hạn (trên $$\mathbb{Q}$$, các nhóm này được phân loại bởi định lý Mazur), và số nguyên $$r\ge 0$$ là **hạng**, đo mức "phong phú" của các điểm hữu tỷ cấp vô hạn. Hạng bằng 0 nghĩa là mọi điểm hữu tỷ đều là điểm xoắn, tức là chỉ có hữu hạn điểm. Hạng dương nghĩa là có vô hạn điểm hữu tỷ, sinh bởi $$r$$ điểm độc lập cùng với phần xoắn.

**Tính hạng là việc khó.** Tìm điểm có thể rất khó; chứng minh rằng không còn điểm "ẩn" nào còn khó hơn. Nhóm **Tate–Shafarevich** $$Ш(E/\mathbb{Q})$$ đo sự thất bại của nguyên lý địa phương–toàn cục trong các nhóm Selmer; nó là trở ngại chính cho các thuật toán tính hạng. Tính hữu hạn của $$Ш$$ đã được chứng minh trong nhiều trường hợp quan trọng gắn với BSD, nhưng không phải là điều "đã biết luôn hữu hạn ngay từ đầu".

Ví dụ: đường cong $$y^2=x^3-2$$ có điểm hữu tỷ $$(x,y)=(3,5)$$ vì $$5^2=25$$ và $$3^3-2=25$$. Nếu điểm này có cấp vô hạn thì hạng ít nhất bằng 1. BSD sẽ *dự đoán* hạng từ dáng điệu giải tích của $$L$$, đôi khi trước cả khi ta tìm đủ các phần tử sinh.

---

## 2. Hàm $$L$$ của đường cong elliptic

Mỗi đường cong $$E/\mathbb{Q}$$ có một **hàm $$L$$** $$L(E,s)$$, được xây dựng từ dữ liệu địa phương tại từng số nguyên tố (kiểu rút gọn của $$E$$ modulo $$p$$: tốt, nhân tính, cộng tính, …). Nhân tử Euler tại $$p$$ đếm số điểm trên trường hữu hạn theo một cách chuẩn hóa; tích Euler hội tụ trên nửa mặt phẳng $$\operatorname{Re}(s)$$ đủ lớn, sau đó cần thác triển.

Nhờ **định lý modular** (Wiles chứng minh trường hợp then chốt cho Định lý Fermat; Breuil–Conrad–Diamond–Taylor hoàn tất cho mọi đường cong elliptic trên $$\mathbb{Q}$$), $$L(E,s)$$ cũng là hàm $$L$$ của một **dạng modular**. Do đó $$L(E,s)$$ có **thác triển giải tích** và **phương trình hàm**, trở thành một đối tượng giải tích toàn cục chứ không chỉ là một tích hình thức.

Giá trị của hàm và các đạo hàm tại điểm trung tâm $$s=1$$ đặc biệt quý về mặt số học: người ta tin rằng chúng chứa thông tin chính xác về hạng và về kích thước số học của các phần tử sinh.

So sánh với hàm zeta Riemann: $$\zeta(s)$$ "ghi nhớ" số nguyên tố qua tích Euler; $$L(E,s)$$ "ghi nhớ" số học của $$E$$. RH hỏi về vị trí các không điểm của zeta; BSD hỏi về **bậc triệt tiêu** (và hệ số dẫn đầu) của $$L(E,\cdot)$$ tại một điểm đặc biệt, không phải trên cả đường tới hạn. Nhưng cả hai cùng chung ý tưởng: không điểm và bậc của chúng chứa thông tin số học.

---

## 3. Phát biểu BSD

**BSD (phần hạng).** Với mọi đường cong elliptic $$E/\mathbb{Q}$$,

$$
\operatorname{ord}_{s=1} L(E,s) = r = \operatorname{rank} E(\mathbb{Q}).
$$

Nghĩa là: bậc của không điểm của $$L(E,s)$$ tại $$s=1$$ bằng hạng Mordell–Weil. Nếu $$L(E,1)\ne 0$$ thì dự đoán hạng bằng $$0$$ (chỉ có điểm xoắn). Nếu $$L$$ triệt tiêu với bậc đúng bằng 1 thì dự đoán hạng bằng 1, v.v.

**BSD (phần chính xác hóa).** Viết khai triển Taylor

$$
L(E,s) = c\, (s-1)^{r} + \text{các hạng bậc cao hơn},
$$

với hệ số dẫn đầu $$c \ne 0$$. BSD dự đoán một công thức tường minh cho $$c$$ dưới dạng tích các bất biến số học (viết dạng sơ đồ, theo chuẩn hóa trong sách giáo khoa):

$$
c = \frac{\Omega \cdot \operatorname{Reg} \cdot \#Ш \cdot \prod_p c_p}{(\# E(\mathbb{Q})_{\mathrm{tors}})^2}.
$$

Ở đây: $$\Omega$$ là **chu kỳ thực**; $$\operatorname{Reg}$$ là **regulator** (định thức của dạng song tuyến tính độ cao Néron–Tate); $$\# E(\mathbb{Q})_{\mathrm{tors}}$$ là cấp của nhóm xoắn; $$c_p$$ là các **số Tamagawa** (chỉ số địa phương tại các số nguyên tố có rút gọn xấu); $$\#Ш$$ là cấp của nhóm Tate–Shafarevich (được giả thuyết là hữu hạn).

Công thức chính xác hóa quan trọng không kém đẳng thức về hạng: nó không chỉ dự đoán có *bao nhiêu* điểm độc lập, mà còn cho một **thước đo** kích thước số học của chúng, và biến nhóm Ш thành một số nguyên cụ thể chứ không chỉ là một trở ngại. Theo nghĩa này, BSD là "công thức số lớp cho đường cong elliptic".

---

## 4. Vì sao khó

- **Hạng** là một bất biến toàn cục về phương trình nghiệm hữu tỷ; **hàm $$L$$** là một đối tượng giải tích. Để nối hai thế giới cần các công cụ sâu (dạng modular, hệ Euler, điểm Heegner, lý thuyết Iwasawa, …).
- $$Ш$$ khó tính và khó kiểm soát; nó vừa là trở ngại cho thuật toán, vừa là một thừa số trong công thức chính xác hóa.
- Đường cong có hạng cao tồn tại nhưng hiếm; **phân bố của hạng** là một hướng nghiên cứu lớn hiện nay (mô hình xác suất cho hạng, tỷ lệ các đường cong có hạng 0 và hạng 1).
- Ngay cả việc định nghĩa đúng $$L$$ và thác triển nó cũng đã cần tính modular, một định lý chỉ được hoàn tất khá gần đây (thập niên 1990–2000) cho mọi $$E/\mathbb{Q}$$. BSD *giả sử* có sẵn khung giải tích đó rồi đặt câu hỏi sâu hơn về giá trị đặc biệt.

Cái khó không nằm ở việc "thiếu ví dụ tính toán", mà ở chỗ phải chứng minh **một đẳng thức chính xác giữa hai thế giới** cho mọi đường cong, chứ không chỉ kiểm tra từng trường hợp.

---

## 5. Bằng chứng và kết quả từng phần

BSD **chưa** được chứng minh đầy đủ. Nhưng "còn mở" không có nghĩa là "chưa có gì":

- **Kiểm tra bằng tính toán.** Bảng của Cremona và cơ sở dữ liệu LMFDB ghi lại hạng, phần xoắn và giá trị đặc biệt của $$L$$. Với một số lượng rất lớn đường cong, hạng giải tích và hạng đại số khớp nhau, và công thức chính xác hóa khớp với độ chính xác cao khi kiểm soát được Ш. Đây là bằng chứng mạnh, nhưng không phải chứng minh tổng quát.  
- **Coates–Wiles.** Với một số đường cong có **phép nhân phức (CM)**, Coates–Wiles và các công trình liên quan chứng minh kết quả kiểu BSD trong trường hợp hạng 0: nếu $$L(E,1)$$ khác 0 thì không có điểm cấp vô hạn, trong các trường hợp mà định lý áp dụng được.  
- **Gross–Zagier và điểm Heegner.** Gross–Zagier liên hệ $$L'(E,1)$$ với độ cao Néron–Tate của **điểm Heegner** lấy từ một trường bậc hai ảo. Khi $$L(E,1)=0$$ nhưng $$L'(E,1)\ne 0$$, ta thu được một điểm hữu tỷ cấp vô hạn.  
- **Hệ Euler của Kolyvagin.** Hệ Euler dựng từ các điểm Heegner giúp kiểm soát nhóm Selmer và cho BSD với nhiều đường cong có hạng giải tích 0 và 1: với các giả thiết của phương pháp, khi hạng giải tích ≤1, hạng đại số bằng hạng giải tích và Ш hữu hạn.  

Kết hợp Gross–Zagier và Kolyvagin, ta có một lý thuyết khá đầy đủ cho trường hợp **hạng ≤1**. Trường hợp hạng giải tích cao hơn khó hơn rất nhiều.

- **Kết quả trung bình.** Các công trình của Bhargava, Shankar và cộng sự về hạng trung bình (và cỡ trung bình của nhóm Selmer), cùng Skinner–Urban, Zhang, …, cho bức tranh về "hạng điển hình": hầu hết đường cong được kỳ vọng có hạng 0 hoặc 1, trong khi BSD cho từng đường cong có hạng cao vẫn còn mở.

**Tình trạng (2026).** BSD vẫn **còn mở** ở dạng tổng quát; đây là một trong sáu bài toán Thiên niên kỷ chưa được giải (chỉ có giả thuyết Poincaré đã được Perelman giải).

Khi đọc câu "BSD đã được chứng minh cho hạng ≤1 trong nhiều trường hợp", hãy hiểu đó là **một lớp lớn và quan trọng**, không phải mọi đường cong với mọi hạng.

---

## 6. Các giả thuyết cùng tinh thần: giá trị đặc biệt chứa thông tin số học

BSD nằm trong một mạng lưới cùng với **công thức số lớp**, giả thuyết **Bloch–Kato**, và quan điểm chung "hàm $$L$$ biết về số học". [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) nói về phân bố số nguyên tố; BSD nói về đường cong elliptic. Nếu RH hỏi *các không điểm nằm ở đâu*, thì BSD hỏi *không điểm tại tâm có bậc bao nhiêu*, và bậc đó có ý nghĩa gì với các điểm hữu tỷ.

Hàm zeta Riemann chứa thông tin về số nguyên tố; hàm $$L$$ của đường cong elliptic chứa thông tin về điểm hữu tỷ. Khi thảo luận, có thể *mở rộng* bài Riemann: không chỉ hỏi "không điểm ở đâu", mà còn hỏi "bậc triệt tiêu và hệ số dẫn đầu cho biết điều gì".

---

## 7. Mật mã đường cong elliptic không cần BSD (mục tiêu 6)

**ECC** dùng nhóm $$E(\mathbb{F}_q)$$ trên **trường hữu hạn**, chứ không phải chủ yếu là $$E(\mathbb{Q})$$. Độ an toàn dựa trên độ khó của bài toán logarit rời rạc trong một nhóm được chọn cẩn thận. Người triển khai cần đường cong không kỳ dị, có nhóm con cấp nguyên tố lớn, chống được các kiểu tấn công đã biết; họ không cần chứng minh hạng đại số bằng hạng giải tích trên $$\mathbb{Q}$$.

| Thực tiễn (ECC) | BSD (bài toán Thiên niên kỷ) |
|-----------------|-------------------|
| Phép cộng điểm trên trường hữu hạn | Hạng của $$E(\mathbb{Q})$$ so với $$\operatorname{ord}_{s=1}L(E,s)$$ |
| Độ khó của logarit rời rạc | Đẳng thức giữa giải tích và đại số, công thức chính xác hóa |
| Tiêu chí chọn đường cong | Ш, regulator, số Tamagawa |

**Dùng** đường cong elliptic và **giải** BSD là hai việc khác nhau. Chương 3 trình bày ECC; bài này chỉ **nêu rõ** ranh giới (mục tiêu 6). Đừng viết trong bài A3 rằng "BSD quan trọng vì Bitcoin"; hãy viết: cùng *đối tượng hình học*, khác *câu hỏi số học*. Xem bài [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/).

---

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Đường cong elliptic là đường elip." | Hai đối tượng khác nhau; tên gọi "elliptic" có nguồn gốc lịch sử (liên quan đến tích phân elliptic). |
| "BSD là về việc vẽ đường cong." | BSD là về số học của điểm hữu tỷ và giải tích của hàm $$L$$. |
| "Có tính modular là xong BSD." | Tính modular cho phép thác triển $$L$$; đẳng thức về hạng vẫn còn mở. |
| "Tính hạng dễ: tìm được điểm là xong." | Tìm và chứng minh đã có đủ phần tử sinh có thể cực khó; Ш và độ cao đều ảnh hưởng. |
| "ECC không an toàn cho đến khi BSD được chứng minh." | ECC dùng nhóm trên trường hữu hạn; nó không phụ thuộc vào bài toán Thiên niên kỷ trên $$\mathbb{Q}$$. |
| "Hạng giải tích bằng 0 nghĩa là không có điểm hữu tỷ." | Dự đoán là không có điểm hữu tỷ *cấp vô hạn*; điểm xoắn vẫn có thể tồn tại. |

---

## Bài tập

1. Với $$y^2=x^3-2$$, kiểm tra $$(3,5)$$ là điểm hữu tỷ. Viết một câu: "hạng ít nhất bằng 1" nghĩa là gì nếu $$(3,5)$$ có cấp vô hạn.  
2. Phát biểu định lý Mordell–Weil bằng lời, không dùng ký hiệu, rồi viết lại $$E(\mathbb{Q})\cong\mathbb{Z}^r\oplus E(\mathbb{Q})_{\mathrm{tors}}$$.  
3. Theo BSD, $$\operatorname{ord}_{s=1}L(E,s)=0$$ dự đoán điều gì về các điểm cấp vô hạn?  
4. Vì sao điều kiện $$\Delta\neq 0$$ quan trọng cho phép cộng điểm?  
5. **Mục tiêu 1 (không quá 350 từ):** phát biểu BSD (phần hạng), giải thích vì sao khó, nêu hai công cụ liên quan (tính modular; điểm Heegner / Kolyvagin).  
6. **Ranh giới (mục tiêu 6).** Viết ba câu phân biệt "đường cong elliptic trong mật mã" với "BSD như một bài toán Thiên niên kỷ".  
7. Viết một câu nối BSD với cách tư duy về không điểm và bậc của hàm $$L$$ trong bài [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/).  
8. Mở rộng: mở LMFDB hoặc bảng của Cremona, chọn một đường cong, ghi lại hạng, phần xoắn, và $$L(E,1)$$ bằng 0 hay khác 0.

---

## Từ các bài giảng: trường hợp hạng ≤ 1 cho ta gì, BSD đầy đủ còn thiếu gì

Bhargava (Giải Abel) và Mazur (Clay/CMSA 2026) đều nhấn mạnh cách phân lớp sau (mục tiêu 1):

- **Nền tảng (đã có cho mọi $$E/\mathbb{Q}$$):** tính modular cho phép thác triển giải tích $$L(E,s)$$, nên **hạng giải tích** $$\operatorname{ord}_{s=1}L(E,s)$$ được định nghĩa.  
- **Số học khi hạng thấp (đã có lý thuyết lớn, dù chưa đầy đủ):** Gross–Zagier và Kolyvagin (cùng Coates–Wiles cho trường hợp CM) cho kết luận kiểu BSD với nhiều đường cong có hạng giải tích $$0$$ hoặc $$1$$.  
- **Vẫn còn mở:** hạng tùy ý; công thức chính xác hóa đầy đủ cho mọi $$E/\mathbb{Q}$$.

**Tình trạng (2026):** BSD **còn mở** ở dạng tổng quát (theo Viện Clay), dù lý thuyết cho trường hợp hạng $$\le 1$$ là một thành tựu lớn của lý thuyết số hiện đại.

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Đánh giá: `research/video-research/Birch_Swinnerton_Dyer/`.

**Thứ tự gợi ý**

1. **Định hướng** — Bhargava (Giải Abel), *What is the BSD Conjecture?*: [YouTube](https://www.youtube.com/watch?v=_-feKGb6-gc).  
2. **Nền tảng** — Borcherds, *BSD: Introduction*: [YouTube](https://www.youtube.com/watch?v=3vGiWK_ZyKs).  
3. **Góc nhìn nghiên cứu** — Mazur, *About BSD* (CMSA/Clay 2026): [YouTube](https://www.youtube.com/watch?v=14-9iCoclFE).  
4. **Trang của Viện Clay** — [BSD Millennium](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/).  
5. **Thực hành với dữ liệu** — [LMFDB](https://www.lmfdb.org/).

**Sau khi xem:** tính modular tạo nền tảng; các định lý cho hạng $$\le 1$$ là kết quả từng phần sâu sắc; BSD đầy đủ vẫn **còn mở**. ECC **không** phải chờ giải thưởng của Viện Clay.

---


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/Birch_Swinnerton_Dyer/transcripts/` · trạng thái: `research/video-research/Birch_Swinnerton_Dyer/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Birch_Swinnerton_Dyer__-feKGb6-gc_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

Danh sách URL: `research/video-research/Birch_Swinnerton_Dyer/references.md`.

1. Clay — [BSD](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/) · [BSD at 25](https://www.claymath.org/lectures/the-birch-swinnerton-dyer-conjecture-a-millennium-prize-problem-at-25/).  
2. Silverman; Silverman–Tate.  
3. Wikipedia — [BSD](https://en.wikipedia.org/wiki/Birch_and_Swinnerton-Dyer_conjecture).  
4. LMFDB — https://www.lmfdb.org/  
5. Bhargava: https://www.youtube.com/watch?v=_-feKGb6-gc  
6. Borcherds: https://www.youtube.com/watch?v=3vGiWK_ZyKs  
7. Mazur: https://www.youtube.com/watch?v=14-9iCoclFE  
8. [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), [Mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/). Bộ tư liệu: `research/video-research/Birch_Swinnerton_Dyer/`.

---

## Hướng đi tiếp

Có thể chọn làm đề tài cho bài **A3**. So sánh ECC và BSD: "cùng công cụ, khác câu hỏi". Về mặt giải tích: đọc lại phần hàm $$L$$ trong bài Riemann. Về mặt đại số: thử tìm vài điểm trên một đường cong Weierstrass trước khi bàn về $$L$$.

## Video tham khảo

- **Xem trước:** [Manjul Bhargava: What is the Birch-Swinnerton-Dyer Conjecture, and what is known about it?](https://www.youtube.com/watch?v=_-feKGb6-gc) — The Abel Prize, tiếng Anh. Bhargava giới thiệu giả thuyết BSD và những gì đã biết; nên xem trước khi đọc bài.
- [Birch Swinnerton-Dyer conjecture: Introduction](https://www.youtube.com/watch?v=3vGiWK_ZyKs) — Richard E Borcherds, tiếng Anh. Bài giảng nhập môn có nhiều chi tiết kỹ thuật hơn; nên xem sau khi đã nắm ý chính của bài.
- [Barry Mazur | About the Birch and Swinnerton–Dyer Conjecture](https://www.youtube.com/watch?v=14-9iCoclFE) — Harvard CMSA, tiếng Anh. Xem thêm sau hai video trên, để nghe góc nhìn của Mazur về giả thuyết.
