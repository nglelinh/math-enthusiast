---
layout: post
title: "Tái chuẩn hóa của Avila trong các hệ động lực (Huy chương Fields 2014)"
chapter: '02'
order: 16
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Artur Avila** nhận **Huy chương Fields 2014** vì, theo đúng lời IMU, “những đóng góp sâu sắc cho lý thuyết các hệ động lực, đã làm thay đổi diện mạo của lĩnh vực, lấy ý tưởng mạnh mẽ của **tái chuẩn hóa** (renormalization) làm nguyên lý thống nhất.” Citation nêu một *phương pháp*, không phải một giả thuyết cô lập bị khép. Avila không phát minh tái chuẩn hóa—vật lý của Wilson, cascade nhân đôi chu kỳ của Feigenbaum, động lực chỉnh hình của Sullivan, cùng trường phái một chiều Brazil–Pháp đã có trước. Huy chương ghi nhận một thân định lý trong đó việc nhìn hệ ở một thang mới, rồi lại một thang mới, trở thành *từ điển* xuyên qua ánh xạ một chiều, toán tử Schrödinger gần tuần hoàn, và động lực Teichmüller.

Bài này dành cho người đã thấy iteration của một ánh xạ $$f:[0,1]\to[0,1]$$, hoặc một hệ tuyến tính với hệ số biến thiên, và muốn nắm **kiến trúc** bức tranh Avila. Bài **không** khẳng định ông phân loại mọi hệ động lực, cũng không gán định lý phổ Ten Martini cho một mình ông. Các khẩu hiệu cần giữ đúng: ánh xạ unimodal regular versus stochastic; cocycle và almost reducibility; phổ Cantor của toán tử almost Mathieu; weak mixing của ánh xạ trao đổi khoảng; và cách ghi công các cộng sự như Jitomirskaya, Forni, Viana, de Melo, Lyubich.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu citation IMU 2014 trong một câu cẩn thận, với **tái chuẩn hóa** là công cụ thống nhất chứ không phải phát minh cá nhân.
- Giải thích, mức khẩu hiệu, **tái chuẩn hóa** một hệ động lực nghĩa là gì: chuyển sang ánh xạ trở-lại-lần-đầu (first-return) hoặc ánh xạ đã rescale, rồi xem đối tượng mới như cùng một lớp.
- Mô tả **toán tử almost Mathieu** và câu hỏi **Ten Martini** (phổ là tập Cantor), và gán lời giải **chung** cho **Avila–Jitomirskaya**.
- Phân biệt cocycle Schrödinger gần tuần hoàn một tần số với khẳng định “mọi phổ lượng tử đều là tập Cantor.”
- Phác ánh xạ trao đổi khoảng / động lực Teichmüller và vai trò **số mũ Lyapunov**, nêu cộng sự (Forni, Viana, và những người khác) thay vì một anh hùng đơn lẻ.
- Luyện **LO6**: “Avila phân loại hỗn độn” là hype; các định lý sắp xếp lại những lớp cụ thể, khó.

**Kiến thức nền.** Iteration của ánh xạ thực; quỹ đạo và phụ thuộc nhạy; ma trận và trị riêng đủ để nghe “số mũ Lyapunov” như tốc độ tăng mũ; tập Cantor như tập hoàn thiện, nowhere dense trên đường thẳng. Không cần Teichmüller hay phổ toán tử ergodic trước.

**Liên kết seminar.** Họ hàng động lực: [Mirzakhani / moduli và Teichmüller]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (cùng lớp 2014; mặt chứ không phải phổ). Động lực số học khác giọng: [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/). Về “ngôn ngữ thống nhất” ở chỗ khác trong chương, so [Scholze / tilting]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/) như hạ tầng, không cùng hộp công cụ.

---

## 1. Lịch sử của việc nhìn lại ở thang nhỏ hơn

Lý thuyết hệ động lực hỏi điều gì xảy ra khi ta lặp một quy tắc. Họ logistic $$x\mapsto rx(1-x)$$ đã là cú sốc sư phạm thập niên 1970: một đa thức bậc hai, khi tham số $$r$$ đổi, có thể đi từ chu kỳ hút qua cascade nhân đôi chu kỳ vào hỗn độn. **Mitchell Feigenbaum** rút ra các hằng số tỷ lệ phổ quát từ cascade đó. Trong vật lý, **Kenneth Wilson** đã biến tái chuẩn hóa thành cách chuyển thang trong cơ học thống kê. Trong động lực chỉnh hình, **Dennis Sullivan** và những người khác viết lại ánh xạ một chiều sao cho ánh xạ trở-lại-lần-đầu, sau rescale afin, lại trông như ánh xạ cùng lớp—một toán tử trên không gian các ánh xạ, không phải một quỹ đạo.

Sang thập niên 1990, trường phái Brazil quanh IMPA (de Melo, Palis, ảnh hưởng của Yoccoz lên động lực một chiều, công trình của Lyubich về họ bậc hai) có một giấc mơ chính xác: với ánh xạ unimodal điển hình, hành vi dài hạn phải hoặc **regular** (một chu kỳ hút tổ chức tương lai) hoặc **stochastic** (một độ đo bất biến tuyệt đối liên tục, hỗn độn mô tả được bằng xác suất). Nhiều trường hợp đặc biệt đã biết. Một bài năm 2003 của **Avila, Welington de Melo và Mikhail Lyubich** khép một chương dài cho các họ unimodal giải tích thực: một ánh xạ chọn ngẫu nhiên trong họ như vậy là regular hoặc stochastic. Tái chuẩn hóa là máy so sánh ánh xạ trở-lại ở thang nhỏ với họ ban đầu và biến “điển hình” thành định lý.

**Khẩu hiệu.** Tái chuẩn hóa không phải phương trình chuyển động mới. Đó là *đổi tọa độ trên không gian các hệ*: phóng to, rescale, rồi hỏi hệ mới có đơn giản hơn, liên hợp với một mô hình đã biết, hay lại tái chuẩn hóa được lần nữa.

Công trình sau này của Avila coi khẩu hiệu đó là **mang đi được**. Cùng bản năng—so sánh một cocycle trên phép quay với cocycle đã tái chuẩn hóa, hoặc first-return của một phép trao đổi khoảng với một phép trao đổi đơn giản hơn—tái xuất hiện trong lý thuyết phổ và động lực Teichmüller. Tính mang đi được đó chính là điều IMU gọi là nguyên lý thống nhất.

---

## 2. Định lý tái chuẩn hóa sắp xếp lại điều gì

Một định lý “khó” điển hình trong bức tranh này không liệt kê mọi quỹ đạo. Nó **sắp xếp lại không gian tham số**. Trước định lý, ta có một vườn thú: tần số Diophantine và Liouville; tổ hợp hyperbolic và parabolic; ánh xạ tái chuẩn hóa vô hạn lần và ánh xạ không. Sau định lý, những vùng lớn của vườn thú được tuyên bố tương đương, hoặc được rút về một mô hình mà số mũ Lyapunov, phổ, hay tính chất trộn đã hiểu.

Ba sự sắp xếp lại an toàn để nêu ở mức seminar.

**Ánh xạ unimodal (với de Melo và Lyubich).** Nhị phân regular/stochastic cho ánh xạ unimodal giải tích điển hình biến một chuỗi case study nhiều thập niên thành bức tranh toàn cục: hỗn độn không phải phần thừa ngoại lai; đó là một trong hai pha điển hình, và tái chuẩn hóa tổ chức biên.

**Toán tử Schrödinger một tần số và cocycle.** Một thế gần tuần hoàn, đơn giản nhất là cosine lấy mẫu theo một phép quay vô tỷ, sinh ra toán tử Schrödinger rời rạc trên $$\ell^2(\mathbb{Z})$$. **Cocycle Schrödinger** kèm theo là ánh xạ cập nhật nghiệm bằng ma trận $$2\times 2$$ phụ thuộc pha. **Lý thuyết toàn cục về cocycle một tần số** của Avila (hình thành qua những năm 2000, công bố thập niên sau) dùng tái chuẩn hóa và phức hóa năng lượng để chia trục năng lượng thành các chế độ: ở một số chế độ, cocycle gần hằng sau đổi tọa độ (**almost reducibility**); ở chế độ khác, số mũ Lyapunov dương và độ đo phổ kỳ dị hơn. Họ almost Mathieu là ví dụ biểu trưng, không phải ví dụ duy nhất.

**Ánh xạ trao đổi khoảng và dòng Teichmüller (với cộng sự).** Cắt một khoảng thành các khoảng con rồi hoán vị chúng—**ánh xạ trao đổi khoảng (IET)**—là bóng một chiều của dòng tịnh tiến trên mặt phẳng. **Avila–Forni** chứng minh hầu hết mọi IET (không phải phép quay) là weakly mixing. **Avila–Viana** chứng minh giả thuyết Zorich–Kontsevich về tính đơn của các số mũ Lyapunov không tầm thường của dòng trắc địa Teichmüller trên không gian moduli các vi phân Abel. Đây là định lý về hệ *điển hình* theo nghĩa lý thuyết độ đo, không phải phân loại mọi mặt hay mọi hoán vị.

**Điều không được sắp xếp lại.** Không có định lý, của Avila hay của ai, “phân loại mọi hệ động lực.” Động lực trơn chiều cao, vi phôi bảo toàn, và nhiều câu chuyện hyperbolic từng phần vẫn đang mở; chính Avila sau đó còn đóng góp (với Crovisier, Wilkinson, và những người khác) vào entropy và ergodicity, xa ánh xạ unimodal. Citation Fields nói về một *phong cách rút gọn*, không phải một bách khoa toàn thư.

---

## 3. Toán tử almost Mathieu và bài toán Ten Martini

**Toán tử almost Mathieu** trên $$\ell^2(\mathbb{Z})$$ là

$$
(H_{\lambda,\alpha}\psi)_n=\psi_{n+1}+\psi_{n-1}+2\lambda\cos\bigl(2\pi n\alpha\bigr)\,\psi_n,
$$

với hằng số liên kết $$\lambda\in\mathbb{R}$$ và tần số $$\alpha$$. Khi $$\alpha$$ hữu tỷ, phổ là hợp hữu hạn các dải. Khi $$\alpha$$ vô tỷ, phổ không phụ thuộc tham số pha (ta lược ở đây) và từ công trình của Azbel cùng hình **Hofstadter butterfly**, người ta kỳ vọng đó là một **tập Cantor**: đóng, nowhere dense, không điểm cô lập. **Mark Kac** treo thưởng mười ly martini cho một chứng minh; **Barry Simon** đặt tên **bài toán Ten Martini**.

Các kết quả bộ phận chồng chất nhiều thập niên (Bellissard–Simon, Sinai, Helffer–Sjöstrand, Last, Puig, và những người khác), thường dưới điều kiện Diophantine trên $$\alpha$$ hoặc tránh coupling **tới hạn** $$|\lambda|=1$$. Trong 2005–2009, **Artur Avila** và **Svetlana Jitomirskaya** chứng minh phát biểu đầy đủ: phổ là tập Cantor với **mọi tần số vô tỷ và mọi coupling khác không**. Chế độ không tới hạn $$|\lambda|\neq 1$$ là khẩu hiệu sạch nhất cho lần đọc đầu; độ khó của bài nằm ở chỗ kỹ thuật Diophantine và Liouville không khớp tự động, và một “vùng giao” mỏng các tham số phải xử lý bằng tay. Gán định lý **chung**. Các công trình sau của Jitomirskaya và những người khác mở rộng hiện tượng phổ Cantor ra ngoài thế cosine đúng; đó là chương tiếp, không phải citation 2014.

**Độ chính xác.** Ten Martini nói về *hình dạng* của phổ như tập con của $$\mathbb{R}$$. Các giả thuyết tách biệt nói về *độ đo* của phổ (Aubry–André / độ đo Lebesgue $$|4-4|\lambda||$$) và định xứ của hàm riêng. Đừng gộp chúng thành một câu.

---

## 4. Gán công lao trung thực

Bản tin IMU về công trình Avila nói khá thẳng: gần như toàn bộ được làm với cộng sự—cỡ ba mươi nhà toán học. Một bảng seminar công bằng trông như sau.

| Kết quả (khẩu hiệu) | Công lao |
|---------------------|----------|
| Regular vs stochastic cho unimodal điển hình | Avila–de Melo–Lyubich (2003) |
| Weak mixing của hầu hết IET / dòng tịnh tiến | Avila–Forni (2007) |
| Phổ Cantor của almost Mathieu (Ten Martini) | Avila–Jitomirskaya (*Annals*, 2009) |
| Tính đơn của số mũ Lyapunov dòng Teichmüller | Avila–Viana (Zorich–Kontsevich) |
| Lý thuyết toàn cục toán tử Schrödinger một tần số | Avila (và cộng đồng lý thuyết phổ dài) |
| Tái chuẩn hóa như ý tưởng | Wilson, Feigenbaum, Sullivan, Lyubich, Yoccoz, … |

Avila lớn lên ở Rio de Janeiro, bảo vệ tiến sĩ tại **IMPA** năm 2001 dưới hướng dẫn của **Welington de Melo**, và gắn với CNRS Pháp rồi Đại học Zurich. Ông là **Fields Medalist Brazil đầu tiên**, và theo các tường thuật phổ biến là người đầu tiên từ Nam Mỹ (rộng hơn: Latin America đầu tiên). Những sự thật tiểu sử giải thích một narrative công chúng; chúng không thay thế định lý.

---

## 5. Vì sao Huy chương Fields

Ba lý do lồng nhau, không có lý do nào là “ông thuần hóa hỗn độn nói chung.”

1. **Độ khó xuyên chế độ.** Lý thuyết phổ gần tuần hoàn tách thành thế giới Diophantine và Liouville trông như hai môn khác. Khép Ten Martini, và xây lý thuyết cocycle toàn cục, đòi hỏi đi giữa hai thế giới thay vì chọn thế giới tiện.
2. **Tính trung tâm của một phương pháp mang đi được.** Tái chuẩn hóa đã tồn tại. Biến nó thành *ngôn ngữ mặc định* cho vài bài toán đầu bảng đã đổi điều một bài động lực được phép thử.
3. **Định lý tính điển hình.** Weak mixing của IET và unimodal regular/stochastic là phát biểu về hầu hết mọi hệ theo một độ đo tự nhiên. Đó là vật thay thế hiện đại, ở nhiều nhánh động lực, cho một phân loại từng điểm vô vọng.

Trong khóa học này, Avila ngồi cạnh [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) như một câu chuyện 2014 về moduli mặt và các dòng trên đó—hình học kề nhau, câu hỏi khác—và cạnh các huy chương “chương trình” hơn là một giả thuyết số học đơn lẻ.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Avila phát minh tái chuẩn hóa.” | Ý tưởng cũ hơn (Wilson, Feigenbaum, Sullivan, …). Ông dùng nó như công cụ thống nhất. |
| “Ông phân loại mọi hệ động lực.” | Ông chứng minh các định lý sâu cho những lớp trung tâm, cụ thể. |
| “Ten Martini là của một mình Avila.” | Đó là **Avila–Jitomirskaya**. |
| “Phổ là tập Cantor với mọi toán tử Schrödinger.” | Định lý dành cho họ almost Mathieu (và các mở rộng sau); toán tử một tần số tổng quát có giản đồ pha giàu hơn. |
| “Weak mixing cũng là mixing.” | IET không bao giờ strongly mixing; Avila–Forni nói về weak mixing của phép trao đổi điển hình. |
| “Số mũ Lyapunov dòng Teichmüller là định lý đơn của Avila.” | Tính đơn là Avila–Viana, hoàn tất giả thuyết Zorich–Kontsevich; Forni và những người khác thuộc cùng câu chuyện. |

---

## Bài tập

1. Bằng lời của bạn: một **bước tái chuẩn hóa** quên gì và giữ gì, khi đi từ ánh xạ unimodal sang ánh xạ first-return đã rescale?
2. Vì sao nhà vật lý và nhà toán học đều có thể quan tâm phổ có phải tập Cantor? Tách “hình đẹp (Hofstadter)” khỏi “định lý (tập đóng, phần trong rỗng, không điểm cô lập).”
3. Viết toán tử almost Mathieu và đánh dấu **coupling** cùng **tần số**. Ở mức khẩu hiệu, điều gì xảy ra nếu tần số hữu tỷ?
4. Ten Martini: phát biểu định lý trong một câu và nêu **cả hai** tác giả. Rồi viết một câu bạn *từ chối* in (“Avila chứng minh mọi phổ lượng tử đều fractal”).
5. Ánh xạ trao đổi khoảng: giải thích bằng một hình phác vì sao cắt-và-chồng không nhất thiết trộn như riffle shuffle, và “weak mixing” định cứu gì.
6. **Luyện gán công.** Lấy bất kỳ câu phổ thông nào nói Avila “giải được hỗn độn.” Viết lại thành hai câu chính xác cho khóa học này.
7. Lướt văn bản IMU 2014 về Avila (hoặc PDF news-release) và liệt kê **ba** kết quả *không phải* Ten Martini.
8. **Seminar mở rộng.** So các định lý “ánh xạ unimodal điển hình” của Avila với các định lý của [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) về trắc địa điển hình trên không gian moduli: cả hai đều nói về *không gian các hệ*. Không gian trong mỗi câu chuyện là gì?

---

## Nguồn video và đọc thêm

Bài này không kèm gói nghiên cứu video của khóa học. Ưu tiên nguồn chính thức và bách khoa.

1. IMU Fields Medals 2014 (citation): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. IMU news release, *The Work of Artur Avila*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_avila.pdf).
3. Định hướng bách khoa: [Artur Avila](https://en.wikipedia.org/wiki/Artur_Avila); [almost Mathieu operator](https://en.wikipedia.org/wiki/Almost_Mathieu_operator).
4. Profile Quanta (2014): [A Brazilian Wunderkind Who Calms Chaos](https://www.quantamagazine.org/artur-avila-is-first-brazilian-mathematician-to-win-fields-medal-20140812/).
5. Tìm arXiv (renormalization + Avila): [query](https://arxiv.org/search/?query=Avila+renormalization&searchtype=all).
6. Avila–Jitomirskaya, *The Ten Martini Problem*, *Annals of Mathematics* (2009): [trang Annals](https://annals.math.princeton.edu/2009/170-1/p08).

**Nhắc:** Tái chuẩn hóa như phương pháp thống nhất; Ten Martini là công trình chung; không phân loại mọi động lực.

---

## Tài liệu tham khảo

1. International Mathematical Union, Fields Medals 2014 — citation và news release Artur Avila (mathunion.org).
2. **A. Avila, S. Jitomirskaya**, *The Ten Martini Problem*, *Ann. of Math.* 170 (2009).
3. **A. Avila, G. Forni**, *Weak mixing for interval exchange transformations and translation flows*, *Ann. of Math.* (2007).
4. **A. Avila, W. de Melo, M. Lyubich**, *Regular or stochastic dynamics in real analytic families of unimodal maps*, *Invent. Math.* (2003).
5. **A. Avila, M. Viana**, công trình về tính đơn số mũ Lyapunov của dòng Teichmüller (giả thuyết Zorich–Kontsevich).
6. Con trỏ nền (không nhận là định lý của Avila): period-doubling Feigenbaum; tái chuẩn hóa chỉnh hình Sullivan; các survey toán tử Schrödinger gần tuần hoàn.
7. Khóa học: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Đọc một survey ngắn về cocycle một tần số cho đến khi nói được “almost reducibility” mà không trích blog.
- So weak mixing của IET với dòng tịnh tiến trên mặt phẳng; đó là cầu sang thế giới moduli của Mirzakhani và sang billiard.
- Tùy chọn seminar A3: bản một trang “các bài toán mở sau Avila” (toán tử Schrödinger nhiều tần số; hằng số hiệu quả; vi phôi bảo toàn)—không tuyên bố huy chương đã khép lý thuyết hệ động lực.
- Khi gặp hình Hofstadter butterfly, viết *định lý* Ten Martini bên cạnh để hình không thay thế phát biểu.
