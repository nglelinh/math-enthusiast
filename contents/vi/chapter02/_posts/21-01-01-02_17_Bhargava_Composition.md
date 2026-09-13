---
layout: post
title: "Luật hợp thành của Bhargava và hạng trung bình (Huy chương Fields 2014)"
chapter: '02'
order: 17
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Manjul Bhargava** nhận **Huy chương Fields 2014** vì, theo lời IMU, “phát triển những phương pháp mới mạnh mẽ trong **hình học các số**, rồi áp dụng chúng để **đếm các vành hạng nhỏ** và để **chặn hạng trung bình của đường cong elliptic**.” Citation là một cặp ứng dụng của cùng một khẩu vị: tham số hóa đối tượng số học bằng các điểm nguyên trong biểu diễn của nhóm đại số, rồi đếm các điểm đó với sai số đủ kiểm soát để rút ra mật độ và trung bình. Gauss đã biết một luật hợp thành cho dạng toàn phương nhị phân. Bhargava tìm ra một mạng **luật hợp thành bậc cao** và dùng chúng để liệt kê các order trong trường số bậc $$2,3,4,5$$ và, cùng **Arul Shankar**, để chặn hạng Mordell–Weil của một đường cong elliptic trên $$\mathbb{Q}$$ *trung bình lớn đến đâu*.

Bài này dành cho người đã thấy nhóm lớp của một order bậc hai, hoặc nhóm $$E(\mathbb{Q})$$ các điểm hữu tỷ trên đường cong elliptic, và muốn nắm kiến trúc chương trình đếm của Bhargava. Bài **không** khẳng định ông giải [giả thuyết Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/). Các phát biểu đã chứng minh nói về **nhóm Selmer** và do đó về hạng đại số: một tỷ lệ dương các đường cong elliptic có hạng $$0$$; hạng trung bình, khi sắp theo height, là hữu hạn và thật ra bị chặn bởi một hằng số tường minh; hầu hết các đường cong, trong cùng thứ tự, có hạng $$0$$ hoặc $$1$$. Heuristic cho rằng hạng trung bình phải là $$1/2$$ vẫn là heuristic.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu citation IMU 2014 trong một đoạn, nêu **hình học các số**, **vành hạng nhỏ**, và **hạng elliptic trung bình**.
- Giải thích luật hợp thành Gauss của dạng toàn phương nhị phân như luật nhóm trên các dạng discriminant cố định, và nói một **luật hợp thành bậc cao** được phép là gì (một tham số hóa đại số, không phải phép toán hai ngôi bí ẩn trên mọi dạng).
- Mô tả, mức khẩu hiệu, quỹ đạo trong các biểu diễn nguyên tham số hóa vành hạng $$2,3,4,5$$ trên $$\mathbb{Z}$$ ra sao.
- Phân biệt **kích thước trung bình của một nhóm Selmer** với một chứng minh BSD, và trích một kết luận hạng đúng (tỷ lệ dương hạng $$0$$; hạng trung bình bị chặn).
- Đặt phương pháp vào truyền thống **không gian vectơ tiền thuần nhất** (Sato–Shintani, Wright, Yukie, Datskovsky–Wright) chứ không vào chân không.
- Ghi nhận tường thuật tiểu sử phổ biến: Bhargava là **người gốc Ấn đầu tiên** nhận Huy chương Fields. Luyện **LO6** trước câu “ông giải xong đường cong elliptic.”

**Kiến thức nền.** Vành và ideal ở mức đại số năm nhất; dạng toàn phương nhị phân $$ax^2+bxy+cy^2$$ và discriminant $$b^2-4ac$$; khẩu hiệu rằng một đường cong elliptic trên $$\mathbb{Q}$$ có nhóm điểm hữu tỷ hữu hạn sinh $$E(\mathbb{Q})\simeq\mathbb{Z}^r\oplus E(\mathbb{Q})_{\mathrm{tors}}$$. Không cần class-field theory trước.

**Liên kết seminar.** Câu chuyện hạng là anh em số học của [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): cùng đối tượng, câu hỏi khác (trung bình versus hàm $$L$$). Chân dung láng giềng: [Tsimerman]({{ site.baseurl }}/contents/vi/chapter02/02_14_Tsimerman_Arithmetic/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/), [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/). Cùng lớp 2014: [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

---

## 1. Lịch sử hợp thành các dạng

Năm 1801, **Gauss** mô tả một luật hợp thành hai dạng toàn phương nhị phân nguyên thủy cùng discriminant. Ngôn ngữ hiện đại: các lớp dạng như vậy tương ứng với các lớp ideal trong order bậc hai của discriminant đó, và hợp thành là luật nhóm lớp viết bằng tọa độ $$(a,b,c)$$. Xây dựng sơ cấp và tai tiếng: sinh viên gặp nó như một bụi đồng nhất thức lâu trước khi gặp nhóm Picard.

Thế kỷ XX viết lại cùng hiện tượng như **lý thuyết biểu diễn cộng hình học các số**. Các quỹ đạo nguyên của một nhóm kiểu $$\mathrm{SL}_2(\mathbb{Z})$$ tác động trên một lattice các dạng tham số hóa đối tượng số học; hình học các số Minkowski, rồi hình học **không gian vectơ tiền thuần nhất** (Sato, Shintani, và các phát triển số học của Wright, Yukie, Datskovsky–Wright, cùng những người khác), cung cấp cách *đếm* các quỹ đạo với discriminant bị chặn. Vành bậc ba và trường bậc ba đã tiếp cận được bằng ngôn ngữ đó. Vành bậc bốn và bậc năm trông rối hơn: không gian dạng tự nhiên lớn hơn, các nhóm ổn định tinh tế hơn, và bước từ một order sang trường các thương làm mất thông tin mà một phép đếm *trường* vẫn cần.

Luận án *Higher composition laws* của Bhargava (Princeton, 2001, hướng dẫn **Andrew Wiles**) và loạt *Annals* tiếp theo (2004–2008) xây lại từ điển. Một mảnh đại số tuyến tính đáng nhớ—**khối lập phương Bhargava**, một hộp $$2\times 2\times 2$$ các số nguyên—có thể cắt theo ba cách thành các cặp ma trận $$2\times 2$$, cho ba dạng toàn phương nhị phân mà luật Gauss của chúng được khối lập phương mã hóa. Đó không phải trò chơi. Đó là trường hợp hạng $$2$$ của một mẫu có hệ thống: các vành thú vị xuất hiện như quỹ đạo trong những biểu diễn nguyên cụ thể, và luật hợp thành là các đồng nhất thức đại số khiến không gian quỹ đạo thành một groupoid hoặc tích thớ của các nhóm lớp.

**Khẩu hiệu.** Để đếm vành, trước hết *tham số hóa* chúng bằng điểm nguyên; rồi đếm các điểm. Hợp thành là cấu trúc nói với bạn rằng tham số hóa không phải tình cờ.

---

## 2. Các định lý sắp xếp lại điều gì: vành hạng 2, 3, 4, 5

Một **vành hạng $$n$$** trên $$\mathbb{Z}$$ là vành có nhóm cộng đẳng cấu với $$\mathbb{Z}^n$$ (một order trong một đại số $$\mathbb{Q}$$ étale chiều $$n$$, trong trường hợp số học điển hình). Discriminant của vành đó là một số nguyên; bài toán đếm hỏi số lớp đẳng cấu với $$|\mathrm{disc}|<X$$, khi $$X\to\infty$$.

Các luật hợp thành bậc cao của Bhargava cho tham số hóa quỹ đạo:

- **Hạng 2.** Vành bậc hai, lấy lại từ luật Gauss và từ khối lập phương / cặp dạng.
- **Hạng 3.** Vành bậc ba, liên quan dạng bậc ba nhị phân và cặp dạng toàn phương tam nguyên—tương tự bậc ba của luật Gauss (*Higher composition laws II*).
- **Hạng 4.** Vành bậc bốn, tham số hóa trong *Higher composition laws III*.
- **Hạng 5.** Vành bậc năm, tham số hóa trong *Higher composition laws IV*.

Khi tham số hóa đã có, các ước lượng hình học các số—thể tích miền cơ bản, cusp, và số hạng sai của số điểm lattice—sinh ra **tiệm cận mật độ discriminant** của vành và trường bậc bốn, bậc năm. Đó là nghĩa IMU nói ông *đếm* vành hạng nhỏ: không phải danh sách hữu hạn, mà một số hạng chính theo $$X$$ (và sai số kiểm soát) cho mỗi $$n$$ nhỏ.

**Điều được sắp xếp lại.** Trước các bài, trường bậc ba đã có câu chuyện mật độ kiểu Davenport–Heilbronn, trong khi trường bậc bốn và bậc năm nằm ở mép những gì phương pháp tiền thuần nhất đã tiêu hóa. Sau các bài, bậc $$\le 5$$ là một chương mạch lạc: cùng máy đếm quỹ đạo, với biểu diễn phức tạp hơn. Bậc $$6$$ trở đi vẫn là thế giới khác (không có câu chuyện quỹ đạo nguyên cùng phong cách, đủ đầy đủ).

**Trung thực về truyền thống.** Phương pháp nằm trên dòng Minkowski, Siegel, Davenport–Heilbronn, và các phép đếm không gian vectơ tiền thuần nhất của Wright, Yukie, Datskovsky–Wright. Đóng góp của Bhargava là một nguồn tham số hóa mới—đặc biệt những tham số hóa bất ngờ cho vành bậc bốn và bậc năm—và một mức kiểm soát sai số sau đó mở khóa đường cong elliptic. Không phải “hình học các số bắt đầu năm 2001.”

---

## 3. Hạng trung bình đường cong elliptic, với Shankar

Một đường cong elliptic trên $$\mathbb{Q}$$ có thể viết dạng Weierstrass ngắn $$y^2=x^3+Ax+B$$, và sắp theo một **height** xây từ $$A,B$$. Mordell–Weil nói

$$
E(\mathbb{Q})\simeq\mathbb{Z}^{r_E}\oplus E(\mathbb{Q})_{\mathrm{tors}},
$$

và số nguyên $$r_E$$ là **hạng đại số**. [Giả thuyết BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) tiên đoán $$r_E$$ bằng cấp zero của hàm $$L$$ $$L(E,s)$$ tại $$s=1$$. Đẳng thức đó **không** phải điều Bhargava chứng minh.

Điều *tiếp cận được*, nếu ta đếm được quỹ đạo nguyên của dạng bậc bốn nhị phân (rồi dạng bậc ba tam nguyên, và các biểu diễn Selmer cao hơn), là **nhóm 2-Selmer** $$\mathrm{Sel}_2(E)$$. Nó nằm trong một dãy khớp siết hạng:

$$
0\to E(\mathbb{Q})/2E(\mathbb{Q})\to\mathrm{Sel}_2(E)\to\Sha(E)[2]\to 0.
$$

Một chặn trên cho kích thước trung bình của $$\mathrm{Sel}_2$$ vì thế là một chặn trên cho trung bình của $$2^{r_E}$$ (sai khác 2-xoắn, phần rẻ). **Bhargava–Shankar** chứng minh rằng kích thước trung bình của nhóm 2-Selmer, với đường cong elliptic trên $$\mathbb{Q}$$ sắp theo height, bằng **$$3$$**. Hệ quả hình thức: **hạng trung bình nhiều nhất $$1.5$$**—nói riêng là hữu hạn, điều chưa biết vô điều kiện trong thứ tự này. Bài về dạng bậc ba tam nguyên của họ cho thấy một **tỷ lệ dương** các đường cong có hạng $$0$$. Các bài sau trong cùng chương trình (3-Selmer, 4-Selmer, 5-Selmer, và công trình với cộng sự khác) làm bức tranh chắc hơn: đa số đường cong có hạng $$0$$ hoặc $$1$$. Một bản in sẵn kèm theo của Bhargava–Skinner, đã được bản tin IMU 2014 nêu, cho thấy một tỷ lệ dương có hạng một.

**Điều bạn không được nói.** Không được nói hạng trung bình *bằng* $$1/2$$ như một định lý. Heuristic ma trận ngẫu nhiên và BSD gợi ý hầu hết đường cong có hạng $$0$$ hoặc $$1$$ với thiên lệch nhẹ về hạng $$0$$, nên trung bình phải là $$1/2$$; đó là trung bình **giả thuyết**, không phải định lý Bhargava–Shankar. Không được nói BSD đã được chứng minh. Biết $$r_E\le 1$$ với hầu hết $$E$$ tương thích với BSD và là một đầu vào số học lớn; đó không phải đồng nhất $$r_E$$ với hạng giải tích cho mọi đường cong.

**Khẩu hiệu.** Nhóm Selmer là *bóng hữu hạn, đếm được* của nhóm Mordell–Weil. Kích thước Selmer trung bình là bài toán hình học các số. Hạng trung bình là phần còn lại sau khi bỏ phần Selmer có thể là Sha.

---

## 4. Gán công lao và tiểu sử

| Thành phần | Vai trò |
|------------|---------|
| Luật hợp thành Gauss | Tổ tiên hạng 2 |
| Sato–Shintani, Wright, Yukie, Datskovsky–Wright | Đếm tiền thuần nhất; mật độ bậc ba |
| Bhargava, *Higher composition laws* I–IV | Tham số hóa vành hạng $$2$$–$$5$$ |
| Bhargava–Shankar | Kích thước 2-Selmer trung bình $$3$$; tỷ lệ dương hạng $$0$$; hạng trung bình bị chặn |
| Các bài Selmer sau; Bhargava–Skinner và những người khác | Hạng $$0$$ hoặc $$1$$ với hầu hết đường cong; tỷ lệ dương hạng một |
| BSD (Birch, Swinnerton-Dyer; bài toán Clay) | Vẫn mở như đồng nhất hạng đại số và hạng giải tích nói chung |

Bhargava sinh năm 1974 tại Hamilton, Ontario, lớn lên chủ yếu ở Long Island, và có gắn bó lâu với Ấn Độ qua gia đình và việc học Sanskrit; ông là nhà toán học Ấn–Canada–Mỹ tại Princeton. Tường thuật công chúng chuẩn là ông là **người gốc Ấn đầu tiên** thắng Huy chương Fields. Đó là sự thật tiểu sử về lịch sử huy chương, không phải một định lý. Người hướng dẫn tiến sĩ là Wiles—một tình cờ của Princeton, không phải tuyên bố rằng luật hợp thành là một chương của Định lý cuối cùng của Fermat.

---

## 5. Vì sao Huy chương Fields

Huy chương dành cho một *phương pháp trở thành nhà máy*. Luật hợp thành bậc cao thú vị như đại số; chúng đạt tầm Fields khi cùng những không gian quỹ đạo phân loại vành cũng phân loại phần tử 2-Selmer của đường cong elliptic. Đếm rồi sinh ra những định lý lý thuyết số muốn có ít nhất từ thập niên 1960: Có bao nhiêu trường số? Hạng điển hình lớn đến đâu? Câu trả lời là tiệm cận và trung bình-trường-hợp, đúng thang mà thống kê số học hiện đại sống.

So, trong khóa học này, một huy chương “khép một giả thuyết sắc” với huy chương này. BSD vẫn là bài toán mở đầu bảng ở Chương 1. Công trình 2014 của Bhargava *sắp xếp lại phong cảnh quanh* bài toán đó: ta nay biết đường cong elliptic điển hình trên $$\mathbb{Q}$$ nhỏ về mặt số học. Đó là một hình dạng thành tựu khác với việc chứng minh $$L(E,1)\neq 0$$ cho một đường cong nổi tiếng đơn lẻ.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Bhargava giải BSD.” | Ông chặn hạng *đại số* trung bình qua nhóm Selmer. BSD vẫn mở. |
| “Hạng trung bình là $$1/2$$.” | Đó là heuristic. Định lý là trung bình hữu hạn (ví dụ $$\le 1.5$$ từ 2-Selmer) và hầu hết hạng là $$0$$ hoặc $$1$$. |
| “Ông phát minh hình học các số.” | Minkowski, Davenport–Heilbronn, và trường phái tiền thuần nhất đi trước. |
| “Hợp thành bậc cao là luật trên mọi dạng nhị phân mọi bậc.” | Đó là một họ tham số hóa quỹ đạo xác định trên những biểu diễn cụ thể. |
| “Đếm vành nghĩa là liệt kê chúng.” | Nghĩa là tiệm cận số lớp đẳng cấu discriminant bị chặn. |
| “Hạng 0 với tỷ lệ dương chứng minh hàm $$L$$ không triệt tiêu.” | Hạng đại số $$0$$ không tự động là hạng giải tích $$0$$; hàm ý đó là một mảnh của BSD. |

---

## Bài tập

1. Trong một đoạn, luật hợp thành Gauss *làm gì* cho các order bậc hai? Dùng các từ “nhóm lớp” và “discriminant.”
2. Vì sao một khối lập phương $$2\times 2\times 2$$ các số nguyên có *ba* cặp dạng toàn phương nhị phân tự nhiên? (Các hướng cắt.) Không cần hết đồng nhất thức.
3. Vành hạng $$4$$ trên $$\mathbb{Z}$$ là gì, mức khẩu hiệu? Vì sao đếm chúng khó hơn đếm order bậc hai?
4. Viết dãy khớp liên hệ $$E(\mathbb{Q})/2E(\mathbb{Q})$$, $$\mathrm{Sel}_2(E)$$, và $$\Sha(E)[2]$$. Hạng trung bình ẩn ở đâu?
5. **Luyện độ chính xác.** Một tiêu đề đọc “Nhà toán học giải bí ẩn đường cong elliptic 350 năm.” Viết lại thành hai câu có thể xuất hiện trong khóa học này.
6. Một chứng minh BSD *cộng* Bhargava–Shankar sẽ đổi nghĩa “hạng giải tích trung bình” ra sao? Một đoạn cẩn thận.
7. Lướt bản tin IMU 2014 về Bhargava và liệt kê hai kết quả *không* về đường cong elliptic (ví dụ điểm hyperelliptic, định lý 290 với Hanke).
8. **Seminar mở rộng.** So “hạng trung bình đường cong elliptic” với “ánh xạ unimodal điển hình” của [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/): cả hai thay phân loại bằng một độ đo trên không gian đối tượng. Độ đo ở đây là gì?

---

## Nguồn video và đọc thêm

Bài này không kèm gói nghiên cứu video của khóa học.

1. IMU Fields Medals 2014 (citation): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. IMU news release, *The Work of Manjul Bhargava*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_bhargava.pdf).
3. Bách khoa: [Manjul Bhargava](https://en.wikipedia.org/wiki/Manjul_Bhargava).
4. Profile Quanta (2014): [The Musical, Magical Number Theorist](https://www.quantamagazine.org/number-theorist-manjul-bhargava-is-awarded-fields-medal-20140812/).
5. Tìm arXiv: [Bhargava composition](https://arxiv.org/search/?query=Bhargava+composition&searchtype=all); [Bhargava Shankar elliptic](https://arxiv.org/search/?query=Bhargava+Shankar+elliptic&searchtype=all).
6. Đọc sâu của khóa về hạng và hàm $$L$$: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/).

**Nhắc:** Định lý Selmer trung bình / hạng trung bình—**không** phải lời giải BSD.

---

## Tài liệu tham khảo

1. International Mathematical Union, Fields Medals 2014 — citation và news release Manjul Bhargava.
2. **M. Bhargava**, *Higher composition laws* I–IV, *Ann. of Math.* (2004–2008).
3. **M. Bhargava, A. Shankar**, *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, *Ann. of Math.* 181 (2015).
4. **M. Bhargava, A. Shankar**, *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0*, *Ann. of Math.* 181 (2015).
5. Con trỏ truyền thống đếm cũ hơn: Davenport–Heilbronn; Datskovsky–Wright; các survey không gian vectơ tiền thuần nhất (Wright, Yukie).
6. Khóa học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), [Tsimerman]({{ site.baseurl }}/contents/vi/chapter02/02_14_Tsimerman_Arithmetic/), [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/).

---

## Hướng đi tiếp

- Làm một ví dụ luật Gauss bằng tay (discriminant $$-23$$ hoặc $$-31$$) trước khi đọc *Higher composition laws I*.
- Đọc một tài liệu giải thích nhóm 2-Selmer (ví dụ một chương đầu Silverman cộng một survey thống kê số học) cho đến khi dãy khớp ở trên cảm thấy tất yếu.
- Tùy chọn seminar A3: bản một trang về *những gì vẫn mở*—hạng trung bình đúng, BSD, và đếm trường bậc $$\ge 6$$—không thổi 2014 thành việc khép lý thuyết số.
- Nếu thích khối lập phương hơn hạng, ở lại với các tham số hóa; nếu thích hạng hơn khối, sang [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) và giữ phân biệt Selmer/hàm $$L$$ trên trang.
