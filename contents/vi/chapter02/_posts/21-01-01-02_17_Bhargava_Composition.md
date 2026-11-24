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

Năm 1801, trong kiệt tác *Disquisitiones Arithmeticae*, Carl Friedrich Gauss viết ra hàng chục trang công thức dày đặc để mô tả một phép "nhân" bí ẩn giữa hai biểu thức bậc hai dạng $$ax^2 + bxy + cy^2$$ — gọi là **luật hợp thành Gauss**. Suốt đúng hai trăm năm sau đó, các nhà toán học ngỡ rằng quy luật kỳ diệu ấy chỉ là một phép màu độc nhất vô nhị ở bậc 2.

Rồi vào mùa hè năm 1998, một nghiên cứu sinh trẻ tuổi tại Princeton (đồng thời là tay trống tabla cừ khôi) tên là **Manjul Bhargava** ngồi xoay khối lập phương Rubik mini trong phòng ký túc xá và chợt nảy ra một ý tưởng làm rúng động giới lý thuyết số: nếu viết 8 số nguyên lên 8 đỉnh của một **khối lập phương $$2\times 2\times 2$$**, rồi cắt khối lập phương ấy theo 3 hướng (trên–dưới, trước–sau, trái–phải), bạn lập tức thu được đúng 3 dạng toàn phương nhị phân thỏa mãn luật hợp thành Gauss! Từ chiếc chìa khóa trực quan đó, Bhargava không chỉ viết lại Gauss trong vài dòng, mà còn khám phá ra **13 luật hợp thành bậc cao** mới, dùng chúng để đếm các trường số bậc $$2, 3, 4, 5$$, và cùng **Arul Shankar** chứng minh những định lý mang tính bước ngoặt về **hạng trung bình của đường cong elliptic** — thành tựu mang về cho ông **Huy chương Fields 2014**.

Theo lời trích dẫn của IMU, giải thưởng dành cho việc *"phát triển những phương pháp mới mạnh mẽ trong hình học các số, và áp dụng chúng để đếm các vành hạng nhỏ và để chặn hạng trung bình của đường cong elliptic."* Bài này dành cho người đã biết nhóm lớp của một order bậc hai, hoặc nhóm $$E(\mathbb{Q})$$ các điểm hữu tỷ trên đường cong elliptic, và muốn hiểu cấu trúc chương trình đếm của Bhargava. Cần nói rõ ngay từ đầu: Bhargava **không** chứng minh [giả thuyết Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), nhưng các kết quả của ông về **nhóm Selmer** và hạng trung bình đã lần đầu tiên cho thấy hành vi thống kê của đa số đường cong elliptic khớp ngoạn mục với những gì BSD dự đoán.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lời trích dẫn của IMU năm 2014 trong một đoạn, nêu được **hình học các số**, **vành hạng nhỏ** và **hạng trung bình của đường cong elliptic**.
- Giải thích luật hợp thành Gauss của dạng toàn phương nhị phân như một luật nhóm trên các dạng có cùng biệt thức, và nói được một **luật hợp thành bậc cao** là gì (một phép tham số hóa đại số, không phải một phép toán hai ngôi bí ẩn trên mọi dạng).
- Mô tả ở mức ý tưởng cách các quỹ đạo trong những biểu diễn nguyên tham số hóa vành hạng $$2,3,4,5$$ trên $$\mathbb{Z}$$.
- Phân biệt **kích thước trung bình của nhóm Selmer** với một chứng minh của BSD, và trích dẫn đúng một kết luận về hạng (tỷ lệ dương có hạng $$0$$; hạng trung bình bị chặn).
- Đặt phương pháp này vào truyền thống **không gian vector tiền thuần nhất** (Sato–Shintani, Wright, Yukie, Datskovsky–Wright).
- Biết chi tiết tiểu sử thường được nhắc: Bhargava là **người gốc Ấn đầu tiên** nhận Huy chương Fields, và đánh giá tỉnh táo trước những câu nói quá kiểu "ông đã giải xong bài toán đường cong elliptic".

**Kiến thức cần có.** Vành và ideal ở mức đại số năm nhất; dạng toàn phương nhị phân $$ax^2+bxy+cy^2$$ và biệt thức $$b^2-4ac$$; biết rằng nhóm điểm hữu tỷ của một đường cong elliptic trên $$\mathbb{Q}$$ là hữu hạn sinh, $$E(\mathbb{Q})\simeq\mathbb{Z}^r\oplus E(\mathbb{Q})_{\mathrm{tors}}$$. Không cần biết trước lý thuyết trường lớp.

**Liên hệ với khóa học.** Câu chuyện về hạng có liên quan chặt với [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/): cùng đối tượng nhưng câu hỏi khác (giá trị trung bình, thay vì hàm $$L$$). Các bài liên quan: [Tsimerman]({{ site.baseurl }}/contents/vi/chapter02/02_14_Tsimerman_Arithmetic/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/), [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/). Cùng được trao giải năm 2014: [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

---

## Bản đồ kiến thức nền: Hình học các số, Khối lập phương Bhargava và Đường cong elliptic

Ba khái niệm nền tảng giúp bạn nắm trọn ý tưởng của bài học mà không bị lạc vào kỹ thuật đại số:

- **Hình học các số (Geometry of Numbers) nghiên cứu gì?** Bắt nguồn từ Hermann Minkowski cuối thế kỷ XIX, ngành này biến bài toán đếm số nguyên thành bài toán **đo thể tích**: số điểm lưới nguyên $$\mathbb{Z}^n$$ nằm bên trong một miền hình học lớn gần bằng chính *thể tích* của miền đó (sai khác một phần sai số ở biên). Nghe thì đơn giản, nhưng trong lý thuyết số hiện đại, miền cần đếm thường có những "mũi nhọn" dài vô tận (*cusp*), nên việc kiểm soát sai số là cả một nghệ thuật giải tích.
- **Ví dụ cụ thể về khối lập phương $$2\times 2\times 2$$ của Bhargava:** Hãy tưởng tượng một khối lập phương với 8 đỉnh ghi 8 số nguyên $$(a, b, c, d, e, f, g, h)$$. Cắt khối theo chiều trên–dưới, ta được hai ma trận $$2\times 2$$ là $$M_1$$ và $$M_2$$; lập định thức $$Q_1(x, y) = -\det(M_1 x + M_2 y)$$, ta thu được ngay một dạng toàn phương nhị phân bậc hai! Làm tương tự theo chiều trái–phải và trước–sau, ta được thêm $$Q_2$$ và $$Q_3$$. Điều kỳ diệu là cả ba dạng $$Q_1, Q_2, Q_3$$ đều có **cùng một biệt thức $$D$$**, và trong nhóm lớp các dạng toàn phương, tích của chúng luôn bằng phần tử đơn vị: $$Q_1 \cdot Q_2 \cdot Q_3 = 1$$! Từ đó, muốn "hợp thành" $$Q_1$$ và $$Q_2$$, ta chỉ việc đặt chúng vào hai mặt của khối lập phương rồi đọc ra $$Q_3^{-1}$$ ở mặt thứ ba!
- **Hạng của đường cong elliptic là gì (qua ví dụ nhỏ)?** Xét phương trình $$y^2 = x^3 + Ax + B$$ và tìm các nghiệm hữu tỷ $$(x, y) \in \mathbb{Q}^2$$. Các nghiệm hữu tỷ tạo thành một nhóm giao hoán hữu hạn sinh $$E(\mathbb{Q}) \simeq \mathbb{Z}^r \oplus E(\mathbb{Q})_{\mathrm{tors}}$$, trong đó số nguyên $$r \ge 0$$ gọi là **hạng** (*rank*). Ví dụ, đường cong $$y^2 = x^3 - x$$ chỉ có hữu hạn nghiệm hữu tỷ ($$(0,0), (1,0), (-1,0)$$ và điểm ở vô cực) nên có hạng $$r = 0$$; còn đường cong $$y^2 = x^3 - 2$$ có vô hạn nghiệm hữu tỷ sinh ra từ điểm cơ bản $$(3, 5)$$ nên có hạng $$r = 1$$. Thay vì hỏi hạng của *một* đường cong cụ thể (bài toán cực khó gắn với BSD), Bhargava và Shankar chuyển ngôn ngữ sang **thống kê số học**: nếu bốc ngẫu nhiên một đường cong elliptic, hạng trung bình của nó bằng bao nhiêu?

---

## 1. Lịch sử của luật hợp thành các dạng

Năm 1801, **Gauss** mô tả một luật hợp thành cho hai dạng toàn phương nhị phân nguyên thủy có cùng biệt thức (chẳng hạn với biệt thức $$D = -23$$, có đúng 3 lớp dạng là $$x^2 + xy + 6y^2$$, $$2x^2 + xy + 3y^2$$ và $$2x^2 - xy + 3y^2$$, tạo thành nhóm cyclic cấp 3!). Theo ngôn ngữ hiện đại, các lớp dạng như vậy tương ứng với các lớp ideal trong order bậc hai có biệt thức đó, và phép hợp thành chính là luật nhóm của nhóm lớp, viết bằng các hệ số $$(a,b,c)$$. Cách xây dựng của Gauss sơ cấp nhưng nổi tiếng là dài dòng và khó nhớ.

Trong thế kỷ XX, hiện tượng này được viết lại bằng **lý thuyết biểu diễn kết hợp với hình học các số**. Các quỹ đạo nguyên của một nhóm kiểu $$\mathrm{SL}_2(\mathbb{Z})$$ tác động trên một lưới các dạng tham số hóa các đối tượng số học. Hình học các số của Minkowski, và sau đó lý thuyết **không gian vector tiền thuần nhất** (Sato, Shintani, cùng các phát triển số học của Wright, Yukie, Datskovsky–Wright và những người khác), cho cách *đếm* các quỹ đạo có biệt thức bị chặn. Vành bậc ba và trường bậc ba đã được xử lý bằng ngôn ngữ đó. Vành bậc bốn và bậc năm thì khó hơn rất nhiều: không gian các dạng tự nhiên lớn hơn, các nhóm ổn định phức tạp hơn, và khi đi từ một order sang trường các thương, ta mất những thông tin mà phép đếm *trường* vẫn cần.

Luận án *Higher composition laws* của Bhargava (Princeton, 2001, người hướng dẫn là **Andrew Wiles**) và loạt bài trên *Annals* sau đó (2004–2008) xây dựng lại toàn bộ hệ thống tương ứng. Khối lập phương $$2\times 2\times 2$$ chính là trường hợp hạng $$2$$ của một quy luật tổng quát: các vành bậc $$2, 3, 4, 5$$ xuất hiện tự nhiên như các quỹ đạo nguyên trong những biểu diễn đại số cụ thể (như cặp dạng toàn phương ba biến cho bậc 4, hay bộ tứ dạng đối xứng lệch $$5\times 5$$ cho bậc 5!).

**Ý chính.** Muốn đếm vành hay trường số, trước hết hãy *tham số hóa* chúng bằng các điểm nguyên trong một không gian vector, rồi dùng hình học các số để đếm các điểm đó. Luật hợp thành chính là cấu trúc đại số cho thấy phép tham số hóa đó sâu sắc chứ không hề ngẫu nhiên.

---

## 2. Các định lý về vành hạng 2, 3, 4, 5

Một **vành hạng $$n$$** trên $$\mathbb{Z}$$ là một vành có nhóm cộng đẳng cấu với $$\mathbb{Z}^n$$ (trong trường hợp số học điển hình, đó là một order trong một $$\mathbb{Q}$$-đại số étale chiều $$n$$). Biệt thức của vành là một số nguyên. Bài toán đếm hỏi: có bao nhiêu lớp đẳng cấu với $$\vert\mathrm{disc}\vert<X$$, khi $$X\to\infty$$?

Các luật hợp thành bậc cao của Bhargava cho các phép tham số hóa bằng quỹ đạo:

- **Hạng 2.** Vành bậc hai, thu lại từ luật Gauss và từ khối lập phương / cặp dạng.
- **Hạng 3.** Vành bậc ba, liên quan đến dạng bậc ba nhị phân và cặp dạng toàn phương ba biến, tương tự luật Gauss ở bậc ba (*Higher composition laws II*).
- **Hạng 4.** Vành bậc bốn, được tham số hóa bởi cặp dạng toàn phương ba biến trong *Higher composition laws III*.
- **Hạng 5.** Vành bậc năm, được tham số hóa trong *Higher composition laws IV*.

Khi đã có tham số hóa, các ước lượng của hình học các số (thể tích miền cơ bản, xử lý các đỉnh nhọn *cusp*, và sai số trong phép đếm điểm lưới) cho ra **công thức tiệm cận về mật độ biệt thức** của các vành và trường bậc bốn, bậc năm. Đó là ý nghĩa của việc IMU nói ông *đếm* các vành hạng nhỏ: không phải lập một danh sách hữu hạn, mà là tìm số hạng chính theo $$X$$ (cùng sai số được kiểm soát) cho mỗi $$n$$ nhỏ.

**Bức tranh thay đổi thế nào.** Trước các bài báo này, trường bậc ba đã có kết quả về mật độ kiểu Davenport–Heilbronn, còn trường bậc bốn và bậc năm nằm ở giới hạn của những gì phương pháp tiền thuần nhất làm được. Sau các bài báo, trường hợp bậc $$\le 5$$ trở thành một chương thống nhất: cùng một phương pháp đếm quỹ đạo, chỉ khác là biểu diễn phức tạp hơn. Từ bậc $$6$$ trở đi vẫn là bài toán mở lớn (chưa có một tham số hóa bằng quỹ đạo nguyên cùng kiểu và đủ đầy đủ).

**Nói đúng về truyền thống.** Phương pháp này tiếp nối dòng nghiên cứu của Minkowski, Siegel, Davenport–Heilbronn và các phép đếm trên không gian vector tiền thuần nhất của Wright, Yukie, Datskovsky–Wright. Đóng góp của Bhargava là một nguồn tham số hóa mới (đặc biệt là những tham số hóa bất ngờ cho vành bậc bốn và bậc năm) và một mức kiểm soát sai số đủ tốt để sau đó áp dụng được cho đường cong elliptic. Hình học các số không bắt đầu từ năm 2001.

---

## 3. Hạng trung bình của đường cong elliptic (cùng Shankar)

Một đường cong elliptic trên $$\mathbb{Q}$$ có thể viết ở dạng Weierstrass rút gọn $$y^2=x^3+Ax+B$$, và được sắp xếp theo một **độ cao** (*height*) tính từ $$A,B$$ (chẳng hạn $$\max(4\vert A\vert^3, 27B^2)$$). Định lý Mordell–Weil nói

$$
E(\mathbb{Q})\simeq\mathbb{Z}^{r_E}\oplus E(\mathbb{Q})_{\mathrm{tors}},
$$

trong đó số nguyên $$r_E$$ là **hạng đại số**. [Giả thuyết BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) dự đoán $$r_E$$ bằng cấp của không điểm của hàm $$L$$ $$L(E,s)$$ tại $$s=1$$. Bhargava **không** chứng minh đẳng thức này.

Điều *làm được*, nếu đếm được các quỹ đạo nguyên của dạng bậc bốn nhị phân (và sau đó dạng bậc ba ba biến, cùng các biểu diễn Selmer bậc cao hơn), là nghiên cứu **nhóm 2-Selmer** $$\mathrm{Sel}_2(E)$$. Nhóm này nằm trong một dãy khớp giúp chặn hạng:

$$
0\to E(\mathbb{Q})/2E(\mathbb{Q})\to\mathrm{Sel}_2(E)\to\Sha(E)[2]\to 0.
$$

Vì vậy, một chặn trên cho kích thước trung bình của $$\mathrm{Sel}_2$$ cũng là một chặn trên cho trung bình của $$2^{r_E}$$ (sai khác phần 2-xoắn, phần này dễ kiểm soát). **Bhargava–Shankar** chứng minh rằng khi sắp các đường cong elliptic trên $$\mathbb{Q}$$ theo độ cao, kích thước trung bình của nhóm 2-Selmer bằng đúng **$$3$$**! Vì $$2^r \ge 2r$$ với mọi số nguyên $$r \ge 0$$ (hoặc chính xác hơn $$r \le \frac{1}{2} \cdot 2^r$$), hệ quả trực tiếp là **hạng trung bình không quá $$1.5$$** — nói riêng là hữu hạn, điều trước đó chưa hề được biết mà không cần giả thiết chưa chứng minh! Các bài báo tiếp theo trong cùng chương trình (dùng 3-Selmer, 4-Selmer, 5-Selmer, cho kích thước trung bình lần lượt bằng $$4, 7, 6$$!) kéo chặn trên của hạng trung bình xuống còn **dưới $$0{,}885$$**, đồng thời chứng minh một **tỷ lệ dương** các đường cong có hạng $$0$$ và phần lớn các đường cong có hạng $$0$$ hoặc $$1$$. Kết hợp với **Christopher Skinner**, Bhargava còn chứng minh một tỷ lệ dương các đường cong có hạng bằng $$1$$ và thỏa mãn BSD!

**Những điều không được nói.** Không được nói hạng trung bình *bằng* $$1/2$$ như một định lý. Mô hình ma trận ngẫu nhiên và BSD gợi ý rằng hầu hết các đường cong có hạng $$0$$ hoặc $$1$$, trong đó hạng $$0$$ chiếm khoảng một nửa và hạng $$1$$ chiếm khoảng một nửa, nên hạng trung bình kỳ vọng bằng $$1/2$$. Nhưng đó là giá trị **dự đoán**, không phải định lý Bhargava–Shankar. Cũng không được nói BSD đã được chứng minh. Biết $$r_E\le 1$$ với phần lớn các $$E$$ là phù hợp với BSD và là một kết quả số học quan trọng, nhưng nó không phải là chứng minh rằng $$r_E$$ bằng hạng giải tích với mọi đường cong.

**Tóm lại.** Nhóm Selmer là *hình ảnh hữu hạn, đếm được* của nhóm Mordell–Weil. Tính kích thước Selmer trung bình là một bài toán hình học các số. Hạng trung bình là phần còn lại sau khi trừ đi phần của nhóm Selmer có thể đến từ nhóm Sha.

---

## 4. Ghi nhận công lao và tiểu sử

| Thành phần | Vai trò |
|------------|---------|
| Luật hợp thành Gauss | Tiền thân của trường hợp hạng 2 |
| Sato–Shintani, Wright, Yukie, Datskovsky–Wright | Phép đếm trên không gian tiền thuần nhất; mật độ bậc ba |
| Bhargava, *Higher composition laws* I–IV | Tham số hóa vành hạng $$2$$–$$5$$ |
| Bhargava–Shankar | Kích thước 2-Selmer trung bình bằng $$3$$; tỷ lệ dương có hạng $$0$$; hạng trung bình bị chặn |
| Các bài Selmer sau đó; Bhargava–Skinner và những người khác | Phần lớn đường cong có hạng $$0$$ hoặc $$1$$; tỷ lệ dương có hạng một |
| BSD (Birch, Swinnerton-Dyer; bài toán Clay) | Vẫn mở: sự bằng nhau giữa hạng đại số và hạng giải tích nói chung |

Bhargava sinh năm 1974 tại Hamilton, Ontario (Canada), lớn lên chủ yếu ở Long Island (Mỹ), và gắn bó lâu dài với Ấn Độ qua gia đình và việc học tiếng Phạn. Ông là nhà toán học người Mỹ gốc Ấn, quốc tịch Canada–Mỹ, làm việc tại Princeton. Báo chí thường nhắc ông là **người gốc Ấn đầu tiên** nhận Huy chương Fields. Đó là một chi tiết về lịch sử giải thưởng, không phải một định lý. Người hướng dẫn tiến sĩ của ông là Wiles, nhưng điều đó không có nghĩa luật hợp thành là một phần của chứng minh Định lý lớn Fermat.

---

## 5. Vì sao ông nhận Huy chương Fields

Huy chương ghi nhận một *phương pháp có thể sinh ra nhiều kết quả*. Các luật hợp thành bậc cao tự thân đã thú vị về mặt đại số. Chúng đạt tầm Fields khi chính các không gian quỹ đạo dùng để phân loại vành cũng phân loại được các phần tử của nhóm 2-Selmer của đường cong elliptic. Phép đếm sau đó cho ra những định lý mà các nhà lý thuyết số mong muốn ít nhất từ thập niên 1960: Có bao nhiêu trường số? Hạng của một đường cong điển hình lớn đến đâu? Câu trả lời ở dạng tiệm cận và trung bình, đúng là thang đo mà thống kê số học hiện đại quan tâm.

Trong khóa học, hãy so sánh huy chương này với các huy chương "giải một giả thuyết cụ thể". BSD vẫn là bài toán mở hàng đầu ở Chương 1. Công trình năm 2014 của Bhargava *làm rõ bức tranh xung quanh* bài toán đó: ta biết rằng một đường cong elliptic điển hình trên $$\mathbb{Q}$$ có hạng nhỏ. Đây là một kiểu thành tựu khác với việc chứng minh $$L(E,1)\neq 0$$ cho một đường cong cụ thể.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Bhargava giải được BSD." | Ông chặn hạng *đại số* trung bình thông qua nhóm Selmer. BSD vẫn còn mở. |
| "Hạng trung bình bằng $$1/2$$." | Đó là dự đoán heuristic. Định lý nói hạng trung bình hữu hạn (ví dụ $$\le 1.5$$ từ 2-Selmer) và phần lớn các hạng là $$0$$ hoặc $$1$$. |
| "Ông phát minh ra hình học các số." | Minkowski, Davenport–Heilbronn và trường phái tiền thuần nhất đã có trước. |
| "Hợp thành bậc cao là luật áp dụng cho mọi dạng nhị phân ở mọi bậc." | Đó là một họ các phép tham số hóa bằng quỹ đạo, xác định trên những biểu diễn cụ thể. |
| "Đếm vành nghĩa là liệt kê chúng." | Nghĩa là tìm tiệm cận của số lớp đẳng cấu có biệt thức bị chặn. |
| "Tỷ lệ dương có hạng 0 chứng minh hàm $$L$$ không triệt tiêu." | Hạng đại số $$0$$ không tự động kéo theo hạng giải tích $$0$$; điều đó là một phần của BSD. |

---

## Bài tập

1. Trong một đoạn, luật hợp thành Gauss *làm gì* cho các order bậc hai? Dùng các từ "nhóm lớp" và "biệt thức".
2. Vì sao một khối lập phương $$2\times 2\times 2$$ các số nguyên cho ra *ba* dạng toàn phương nhị phân một cách tự nhiên? (Gợi ý: các hướng cắt.) Không cần viết hết các đồng nhất thức.
3. Ở mức ý tưởng, vành hạng $$4$$ trên $$\mathbb{Z}$$ là gì? Vì sao đếm chúng khó hơn đếm các order bậc hai?
4. Viết dãy khớp liên hệ $$E(\mathbb{Q})/2E(\mathbb{Q})$$, $$\mathrm{Sel}_2(E)$$ và $$\Sha(E)[2]$$. Hạng xuất hiện ở đâu trong dãy này?
5. **Luyện độ chính xác.** Một bài báo đặt tiêu đề "Nhà toán học giải bí ẩn 350 năm về đường cong elliptic". Viết lại thành hai câu có thể xuất hiện trong khóa học này.
6. Nếu có chứng minh BSD, *kết hợp với* kết quả Bhargava–Shankar, thì ta sẽ biết thêm gì về "hạng giải tích trung bình"? Viết một đoạn cẩn thận.
7. Đọc lướt bản tin của IMU năm 2014 về Bhargava và liệt kê hai kết quả *không* liên quan đến đường cong elliptic (ví dụ về điểm trên đường cong siêu elliptic, định lý 290 cùng Hanke).
8. **Seminar mở rộng.** So sánh "hạng trung bình của đường cong elliptic" với "ánh xạ đơn mốt điển hình" của [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/): cả hai đều thay việc phân loại từng đối tượng bằng một độ đo trên không gian các đối tượng. Ở đây độ đo đó là gì?

---

## Nguồn video và đọc thêm

Bài này không có bộ tài liệu video riêng của khóa học.

1. Lời trích dẫn Huy chương Fields 2014 của IMU: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. Bản tin của IMU, *The Work of Manjul Bhargava*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_bhargava.pdf).
3. Bách khoa: [Manjul Bhargava](https://en.wikipedia.org/wiki/Manjul_Bhargava).
4. Bài giới thiệu của Quanta (2014): [The Musical, Magical Number Theorist](https://www.quantamagazine.org/number-theorist-manjul-bhargava-is-awarded-fields-medal-20140812/).
5. Tìm trên arXiv: [Bhargava composition](https://arxiv.org/search/?query=Bhargava+composition&searchtype=all); [Bhargava Shankar elliptic](https://arxiv.org/search/?query=Bhargava+Shankar+elliptic&searchtype=all).
6. Bài đọc sâu trong khóa học về hạng và hàm $$L$$: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/).

**Ghi nhớ:** Đây là các định lý về kích thước Selmer trung bình và hạng trung bình, **không** phải lời giải của BSD.

---

## Tài liệu tham khảo

1. International Mathematical Union, Huy chương Fields 2014: lời trích dẫn và bản tin về Manjul Bhargava.
2. **M. Bhargava**, *Higher composition laws* I–IV, *Ann. of Math.* (2004–2008).
3. **M. Bhargava, A. Shankar**, *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, *Ann. of Math.* 181 (2015).
4. **M. Bhargava, A. Shankar**, *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0*, *Ann. of Math.* 181 (2015).
5. Truyền thống đếm trước đó: Davenport–Heilbronn; Datskovsky–Wright; các bài tổng quan về không gian vector tiền thuần nhất (Wright, Yukie).
6. Trong khóa học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/), [Tsimerman]({{ site.baseurl }}/contents/vi/chapter02/02_14_Tsimerman_Arithmetic/), [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/).

---

## Hướng đi tiếp

- Tự tính một ví dụ về luật Gauss (biệt thức $$-23$$ hoặc $$-31$$) trước khi đọc *Higher composition laws I*.
- Đọc một tài liệu giải thích về nhóm 2-Selmer (ví dụ một chương đầu trong sách của Silverman, kèm một bài tổng quan về thống kê số học) cho đến khi dãy khớp ở trên trở nên tự nhiên với bạn.
- Bài seminar A3 (tùy chọn): viết một trang về *những gì vẫn còn mở* (giá trị đúng của hạng trung bình, BSD, đếm trường bậc $$\ge 6$$), không thổi phồng công trình năm 2014 thành việc khép lại lý thuyết số.
- Nếu bạn thích khối lập phương hơn hạng, hãy tiếp tục với các phép tham số hóa. Nếu thích hạng hơn, hãy chuyển sang bài [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) và luôn phân biệt rõ nhóm Selmer với hàm $$L$$.

## Video tham khảo

- **Xem trước** — [Manjul Bhargava, The average rank of elliptic curves](https://www.youtube.com/watch?v=t5S8PO2PQgU) — Clay Mathematics Institute, tiếng Anh. Bài giảng của Bhargava về hạng trung bình của đường cong elliptic, nội dung chính của mục 3. Nên xem trước khi đọc bài.
- [Manjul Bhargava - The average rank of elliptic curves: data, conjectures, and theorems](https://www.youtube.com/watch?v=zm1v_FaTglw) — princetonmathematics, tiếng Anh. Trình bày dữ liệu, các dự đoán và các định lý về hạng trung bình, giúp phân biệt rõ phần đã chứng minh và phần còn là giả thuyết. Nên xem sau khi đọc mục 3.
- [Manjul Bhargava - Rational points on elliptic and hyperelliptic curves MCA 2013](https://www.youtube.com/watch?v=6NHO-0FKAjM) — MCA2013, tiếng Anh. Bài giảng về điểm hữu tỷ trên đường cong elliptic và siêu elliptic, mở rộng phương pháp sang các đường cong khác. Dành cho người muốn tìm hiểu thêm.
