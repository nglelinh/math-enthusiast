---
layout: post
title: "Landau damping phi tuyến và phương trình Boltzmann của Villani (Huy chương Fields 2010)"
chapter: '02'
order: 29
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Cédric Villani** nhận **Huy chương Fields 2010**

> “For his proofs of nonlinear Landau damping and convergence to equilibrium for the Boltzmann equation.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

*Tạm dịch: vì các chứng minh về hiện tượng tắt dần Landau phi tuyến và sự hội tụ về trạng thái cân bằng của phương trình Boltzmann.*

Lời trao giải nói về lý thuyết động học (kinetic theory), không nói về vận chuyển tối ưu. Villani cũng là tác giả hai cuốn sách chuẩn về vận chuyển tối ưu, *Topics in Optimal Transportation* (AMS, 2003) và *Optimal Transport: Old and New* (Springer, 2009), và mảng này rất quan trọng với giải tích và hình học hiện đại. Nhưng đó **không** phải điều IMU nêu năm 2010. Vì vậy khóa học xem vận chuyển tối ưu là một chủ đề lân cận; xem [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/). Cuốn hồi ký *Théorème vivant* (bản tiếng Anh *Birth of a Theorem*) kể lại trải nghiệm làm ra một chứng minh. Đó **không** phải bài báo nghiên cứu và sẽ không được trích dẫn như một bài báo.

Huy chương 2010 ghi nhận hai định lý về phương trình đạo hàm riêng trong vật lý thống kê. **Tắt dần Landau phi tuyến** (cùng Clément Mouhot) là kết quả cho trường hợp không va chạm, thuộc phương trình Vlasov: một trạng thái cân bằng thuần nhất của plasma có thể làm các dao động điện trường vĩ mô tắt đi mà không cần va chạm, kể cả khi vượt ra ngoài phép tuyến tính hóa của Lev Landau (1946). **Hội tụ về cân bằng cho phương trình Boltzmann** (cùng Laurent Desvillettes, và trong chương trình "hypocoercivity" của Villani) là kết quả cho trường hợp có va chạm: dưới các giả thiết về độ trơn và tính dương được nêu rõ trong các bài báo, sự sinh entropy buộc nghiệm tiến về phân bố Maxwell. Không kết quả nào trong hai kết quả là một lý thuyết đầy đủ, không điều kiện, về nghiệm trơn toàn cục cho mọi nhân va chạm có ý nghĩa vật lý. Huy chương ghi nhận **tốc độ và cơ chế** khi đã ở trong chế độ đủ chính quy, và một hiện tượng tắt dần phi tuyến mà các nhà vật lý tin là đúng trong nhiều thập niên nhưng chưa có chứng minh toán học đầy đủ.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt khung **Vlasov** (không va chạm, trường tự hợp) của tắt dần Landau với khung **Boltzmann** (có va chạm) của xu hướng về cân bằng.
- Nêu ngắn gọn phát hiện năm 1946 của Landau: một plasma không va chạm, sau khi tuyến tính hóa, có thể làm dao động điện trường tắt dần.
- Ghi công **Mouhot–Villani** cho định lý phi tuyến (với dữ kiện giải tích, và một số lớp Gevrey; thế tương tác không kỳ dị hơn thế Coulomb/Newton).
- Mô tả định lý $$H$$ của Boltzmann như một phát biểu về sự sinh entropy, và giải thích vì sao trường hợp **không thuần nhất theo không gian** khiến xu hướng về cân bằng khó hơn nhiều so với trường hợp thuần nhất.
- Giải thích ngắn gọn **hypocoercivity**: một quá trình tiêu tán suy biến vẫn có thể tạo ra khe phổ khi kết hợp với một cơ chế trộn các biến còn lại.
- Nêu rằng các kết quả hội tụ kiểu Desvillettes–Villani là **có điều kiện** về độ trơn, độ suy giảm và tính dương, không phải một lý thuyết chính quy toàn cục không điều kiện.
- Tách lời trao giải của IMU năm 2010 khỏi các sách về **vận chuyển tối ưu** của Villani và khỏi cuốn hồi ký phổ thông *Birth of a Theorem*.

**Kiến thức nền.** Phương trình vi phân thường và phương trình đạo hàm riêng ở mức một giáo trình giải tích nghiêm túc đầu tiên; hàm mật độ xác suất $$f(t,x,v)$$ trên không gian vị trí–vận tốc; entropy như một hàm Lyapunov. Biết cơ học Hamilton và biến đổi Fourier sẽ giúp hiểu tắt dần Landau, nhưng không bắt buộc.

**Liên kết với các bài khác.** Bài này minh họa một chương trình biến cơ chế vật lý thành các đánh giá toán học. Đọc cùng [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/) cho mảng còn lại của Villani, và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) cho bối cảnh rộng hơn. Người cùng năm: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/).

---

## 1. Hai thế giới của lý thuyết động học

Một phương trình động học mô tả chất khí hoặc plasma bằng mật độ $$f(t,x,v)$$ của các hạt tại thời điểm $$t$$, vị trí $$x$$, vận tốc $$v$$. Huy chương liên quan tới hai mô hình ở hai thái cực.

Trong mô hình **Vlasov–Poisson** (hoặc Vlasov–Maxwell), các hạt không va chạm. Chúng chịu tác dụng của trường tự hợp $$E$$, tính từ mật độ điện tích $$\rho=\int f\,dv-1$$ (đã trừ điện tích nền chuẩn hóa). Phương trình có dạng

$$
\partial_t f + v\cdot\nabla_x f + E[f]\cdot\nabla_v f = 0.
$$

Phương trình này thuận nghịch, thấy ngay khi nhìn dọc các đường đặc trưng: không có toán tử va chạm Boltzmann nên không có định lý $$H$$ nào cho ta sự tắt dần ngay lập tức. Nếu có tắt dần, nó phải đến từ **trộn pha**: hàm $$f$$ bị kéo thành các sợi mảnh trong không gian $$(x,v)$$, và khi lấy trung bình theo vận tốc thì mật độ trong không gian trở nên đều. Tắt dần không đến từ va chạm.

Trong mô hình **Boltzmann**, các hạt va chạm với nhau. Phương trình có dạng

$$
\partial_t f + v\cdot\nabla_x f = Q(f,f),
$$

trong đó $$Q$$ là toán tử va chạm song tuyến tính, mã hóa định luật va chạm vi mô (quả cầu cứng, nhân có cắt (cutoff), kỳ dị kiểu Coulomb, …). Phiếm hàm $$H$$ của Boltzmann, $$H(f)=\int f\log f$$, giảm theo thời gian (dưới các giả thiết thích hợp), và các trạng thái cân bằng duy nhất là các phân bố Maxwell. Câu hỏi toán học là sự tồn tại, tính chính quy, và $$f(t)$$ tiến **nhanh đến mức nào** về phân bố Maxwell tương thích với các đại lượng bảo toàn (khối lượng, động lượng, năng lượng).

Lời trao giải cho Villani bao gồm cả hai thế giới. Nếu gộp chúng vào một câu như "ông chứng minh chất khí đạt cân bằng", ta sẽ xóa mất sự phân biệt mà IMU đã viết rất cẩn thận.

---

## 2. Tắt dần Landau: từ tuyến tính đến phi tuyến

Năm 1946, Lev Landau phân tích phương trình Vlasov–Poisson tuyến tính hóa quanh một trạng thái cân bằng thuần nhất $$f^0(v)$$ (ví dụ một phân bố Maxwell). Ông phát hiện điện trường có thể giảm theo hàm mũ theo thời gian, dù phương trình thuận nghịch và không có va chạm. Cơ chế ở đây không phải tiêu tán theo nghĩa $$L^2$$ thông thường. Đó là sự triệt tiêu do **trộn pha**, nhìn thấy được sau khi lấy biến đổi Fourier theo $$x$$ và dịch chuyển đường lấy tích phân một cách cẩn thận trên mặt phẳng vận tốc phức (đường tích phân Landau). Tắt dần Landau tuyến tính trở thành một trụ cột của vật lý plasma.

Tắt dần phi tuyến là một định lý khác. Số hạng phi tuyến $$E[f]\cdot\nabla_v f$$ sinh ra các hiện tượng "tiếng vọng" (echo) và cộng hưởng, và trong thời gian dài người ta không biết chúng có phá vỡ sự suy giảm tuyến tính hay không. **Clément Mouhot** và **Cédric Villani** chứng minh rằng với nhiễu giải tích của một trạng thái cân bằng thuần nhất ổn định (và, trong một mở rộng, với một số lớp Gevrey), và với thế tương tác không kỳ dị hơn thế Coulomb hay Newton, phương trình Vlasov phi tuyến có tắt dần Landau với tốc độ hàm mũ. Trường lực giảm dần, mật độ hội tụ về một trạng thái thuần nhất gần đó, còn hàm phân bố vẫn gần với một nghiệm của phương trình vận chuyển tự do, đo bằng các chuẩn giải tích được điều chỉnh thích hợp. Bài báo là Mouhot–Villani, "On Landau damping", *Acta Mathematica* 207 (2011), 29–201, arXiv:0904.2760.

Chứng minh hiểu sự tắt dần là sự **chuyển tính chính quy** từ biến động học sang biến không gian, chứ không phải sự mất năng lượng. Nó dùng các chuẩn giải tích đo so với vận chuyển tự do, các đánh giá cho tiếng vọng phi tuyến, và một sơ đồ lặp kiểu Newton mà chính các tác giả so sánh với lý thuyết KAM. **Hãy ghi công Mouhot.** Đây là kết quả chung; các bài phổ biến viết "Villani chứng minh tắt dần Landau" là chưa đủ.

**Định lý không khẳng định gì.** Nó không phải một phát biểu không điều kiện cho mọi dữ kiện Sobolev, cũng không phân loại mọi bất ổn định có thể có (bất ổn định hai dòng (two-stream) và các trường hợp tương tự vẫn bất ổn định ngay ở mức tuyến tính). Đó là một định lý về ổn định và tắt dần phi tuyến khi dữ kiện có độ chính quy cao.

---

## 3. Phương trình Boltzmann: entropy, tính không thuần nhất, và các điều kiện

Với phương trình Boltzmann **thuần nhất theo không gian** (không phụ thuộc $$x$$), phương pháp entropy và các đánh giá khe phổ đã có lịch sử lâu dài. Villani đóng góp các định lý $$H$$ định lượng và các kết quả về bất đẳng thức kiểu Cercignani (trong đó có bài "Cercignani’s conjecture is sometimes true and always almost true", *Comm. Math. Phys.* 234 (2003)). Cụm "hội tụ về cân bằng" trong lời trao giải nhắm cụ thể vào phương trình **không thuần nhất theo không gian**, nơi số hạng vận chuyển $$v\cdot\nabla_x$$ và toán tử va chạm $$Q$$ tương tác với nhau.

Desvillettes và Villani, trong bài "On the trend to global equilibrium for spatially inhomogeneous kinetic systems: The Boltzmann equation", *Invent. Math.* 159 (2005), 245–316, thu được tốc độ hội tụ dạng $$O(t^{-\infty})$$, tức nhanh hơn mọi lũy thừa của $$t$$. Kết quả này **có điều kiện**: cần các đánh giá mạnh và tự nhiên về độ trơn, độ suy giảm khi vận tốc lớn, và tính dương chặt. Bài báo nói rõ rằng vào thời điểm đó các đánh giá này mới được chứng minh trong một số trường hợp đặc biệt. Các công trình sau (trường phái của Guo; các đánh giá hypocoercivity của nhiều tác giả) đã mở rộng vùng kết quả không điều kiện, nhưng khóa học sẽ không biến định lý năm 2005 thành một lý thuyết chính quy toàn cục đầy đủ cho phương trình Boltzmann.

Chiến lược chứng minh kết hợp nhiều thành phần: định lý $$H$$ định lượng (sự sinh entropy kiểm soát khoảng cách tới phân bố Maxwell địa phương); một kết quả định lượng rằng nghiệm không thể mãi mãi trông như một chất lưu tiến hóa chậm (mô tả thủy động lực không ổn định); các bất đẳng thức hình học (trong đó có bất đẳng thức kiểu Korn từ công trình trước đó của Desvillettes–Villani); và một hệ bất đẳng thức vi phân chuyển sự sinh entropy địa phương thành sự suy giảm toàn cục.

---

## 4. Hypocoercivity, vận chuyển tối ưu, và vì sao được Fields

**Hypocoercivity** là tên Villani đặt (Memoirs of the AMS, 2009) cho hiện tượng một quá trình tiêu tán suy biến vẫn cho đánh giá coercive (suy giảm có tốc độ) nhờ được trộn bởi một phần bảo toàn. Va chạm có thể chỉ làm tắt dần theo biến $$v$$; khi ghép với số hạng vận chuyển, sự tiêu tán lan sang biến $$x$$, theo tinh thần của định lý tổng bình phương Hörmander. Đây không phải một định lý riêng được IMU nêu tên. Đây là một cách tiếp cận, trong đó "hội tụ về cân bằng" trở thành một tốc độ tường minh, chứ không còn là một lập luận compact không cho tốc độ. Báo cáo của ông tại ICM 2006 đã giới thiệu các toán tử khuếch tán hypocoercive; huy chương năm 2010 nhìn lại chương trình đó khi nó được áp dụng cho Boltzmann và Landau.

Bài toán Monge, phép ghép Kantorovich và khoảng cách Wasserstein $$W_p$$ là ngôn ngữ chung mà Villani đã dạy cho cả một thế hệ, qua hai cuốn *Topics in Optimal Transportation* và *Optimal Transport: Old and New*. Độ cong Ricci tổng hợp của Lott–Villani (và độc lập là Sturm) là nhánh hình học; Huy chương Fields 2018 của Figalli thuộc về tính chính quy của ánh xạ vận chuyển. **Không điều nào trong số này nằm trong lời trao giải năm 2010.** Cách nhớ đơn giản là chia hai nhánh: Fields 2010 = tắt dần Landau (Mouhot–Villani) + phương trình Boltzmann (Desvillettes–Villani, hypocoercivity); còn sự nghiệp song song là vận chuyển tối ưu. Đọc [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/) cho nhánh thứ hai.

Lý thuyết động học đã có entropy, định lý $$H$$ và đường tích phân Landau, nhưng có rất ít định lý phi tuyến khớp với các khẳng định vật lý ở mức có tốc độ cụ thể. Mouhot–Villani biến phép tính tuyến tính năm 1946 thành một định lý phi tuyến. Desvillettes–Villani biến câu "entropy tăng" thành một kết quả định lượng cho chất khí không thuần nhất, với các giả thiết được viết rõ. Cuốn hồi ký *Birth of a Theorem* là văn chương về sự cộng tác đó. Còn định lý thì nằm trong bài báo trên *Acta*.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Huy chương 2010 là về vận chuyển tối ưu." | Lời trao giải của IMU nói về tắt dần Landau và cân bằng của phương trình Boltzmann. Vận chuyển tối ưu là một mảng lớn riêng trong sự nghiệp của ông. |
| "Một mình Villani chứng minh tắt dần Landau phi tuyến." | Định lý là của **Mouhot–Villani**. |
| "Landau đã chứng minh kết quả phi tuyến năm 1946." | Phân tích của Landau là **tuyến tính**. Bài toán phi tuyến còn mở trong nhiều thập niên. |
| "Desvillettes–Villani cho nghiệm trơn toàn cục không điều kiện của phương trình Boltzmann." | Tốc độ của họ **có điều kiện** về độ chính quy, độ suy giảm và tính dương, như nêu trong bài báo. |
| "*Birth of a Theorem* là một bài báo." | Đó là hồi ký (bản tiếng Pháp 2012, tiếng Anh 2015), không phải bài nghiên cứu. |
| "Tắt dần Landau là nhờ va chạm." | Đó là hiện tượng **không va chạm** (phương trình Vlasov); phương trình Boltzmann là vế có va chạm trong lời trao giải. |

---

## Bài tập

1. Viết bốn câu mà một nhà vật lý có thể chấp nhận: tắt dần Landau tuyến tính là gì, và vì sao tính thuận nghịch của phương trình Vlasov không mâu thuẫn ngay với nó?
2. Vì sao số hạng phi tuyến đe dọa sự suy giảm tuyến tính? Trả lời ngắn gọn (tiếng vọng / cộng hưởng), không cần dựng lại bài báo trên *Acta*.
3. Nêu sự khác nhau giữa một định lý **có điều kiện** về xu hướng tiến tới cân bằng và một định lý về **tính chính quy toàn cục**. Kết quả Desvillettes–Villani năm 2005 thuộc loại nào?
4. Giải thích hypocoercivity trong một đoạn: tiêu tán suy biến + trộn $$\Rightarrow$$ suy giảm. Vẽ một hình minh họa (vận chuyển theo $$x$$, va chạm theo $$v$$).
5. Mở cuốn *Topics in Optimal Transportation* hoặc bài [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), viết ba câu so sánh bài toán Monge với bài toán Kantorovich, rồi thêm một câu giải thích vì sao nội dung đó **không** thuộc lời trao giải năm 2010.
6. Luyện ghi công: viết cho **Landau (1946)**, **Mouhot**, **Desvillettes** và **Villani** mỗi người một mệnh đề chính xác.
7. **Luyện phát biểu chính xác.** Viết lại câu "Villani chứng minh entropy luôn dập tắt hỗn loạn ngay lập tức" thành hai câu đúng, phù hợp với khóa học.
8. **Thảo luận.** So sánh huy chương này với [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/): cả hai đều thuộc "vật lý thống kê", nhưng một bên là mô hình lưới / hình học bảo giác, bên kia là phương trình động học / phương trình đạo hàm riêng. Trong mỗi câu chuyện, "giới hạn thang đo" nghĩa là gì?

---

## Liên kết

- IMU Fields Medals 2010 (chỉ mục được yêu cầu): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- Trang Villani IMU / ICM 2010: [Fields Medal – Cédric Villani](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-cedric-villani.html)
- Wikipedia: [Cédric Villani](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani)
- arXiv: [0904.2760](https://arxiv.org/abs/0904.2760) (Mouhot–Villani); tìm [Desvillettes Villani Boltzmann](https://arxiv.org/search/?query=Desvillettes+Villani+Boltzmann&searchtype=all)
- Khóa học: [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/)

---

## Tài liệu tham khảo

1. International Mathematical Union, citation Fields Medals 2010 cho Cédric Villani (tài liệu IMU / ICM Hyderabad 2010).
2. **C. Mouhot and C. Villani**, “On Landau damping,” *Acta Math.* 207 (2011), 29–201, arXiv:0904.2760.
3. **L. Desvillettes and C. Villani**, “On the trend to global equilibrium for spatially inhomogeneous kinetic systems: The Boltzmann equation,” *Invent. Math.* 159 (2005), 245–316.
4. **C. Villani**, *Hypocoercivity*, Mem. Amer. Math. Soc. 202 (2009), no. 950.
5. **C. Villani**, *Topics in Optimal Transportation*, Grad. Stud. Math. 58, AMS, 2003; *Optimal Transport: Old and New*, Grundlehren 338, Springer, 2009. (Bối cảnh; không phải citation Fields.)
6. **C. Villani**, *Théorème vivant*, Grasset, 2012; bản Anh *Birth of a Theorem*, Farrar, Straus and Giroux, 2015. (Hồi ký, không phải bài nghiên cứu.)
7. Wikipedia, [Cédric Villani](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani); các chương khóa học đã dẫn.

---

## Hướng đi tiếp

- Đọc phần mở đầu bài Mouhot–Villani (trộn pha khác với mất năng lượng thế nào) trước khi đọc phần về các chuẩn giải tích. So sánh định lý $$H$$ cho trường hợp thuần nhất với sơ đồ chứng minh của Desvillettes–Villani cho trường hợp không thuần nhất.
- Câu hỏi thảo luận: bạn đoán tắt dần Landau phi tuyến có thể không còn đúng với lớp chính quy nào, và vì sao điều đó không mâu thuẫn với định lý trên *Acta*?

## Video tham khảo

- **Xem trước**: [Conferências Magnas: Cédric Villani - Large particle systems and Landau damping (2012)](https://www.youtube.com/watch?v=3Aa1Fyd1pW0) (Instituto de Matemática Pura e Aplicada, tiếng Anh). Bài giảng lớn của Villani tại IMPA về hệ nhiều hạt và tắt dần Landau. Nên xem trước để nắm sự khác nhau giữa mô hình không va chạm và mô hình có va chạm.
- [Cédric Villani - From KAM Theory to Landau Damping, IHP 30/09/2013 - Part 1](https://www.youtube.com/watch?v=pHJV-E1EOA8) (Institut Henri Poincaré, tiếng Anh). Phần đầu bài giảng nối lý thuyết KAM với tắt dần Landau, đúng với mạch chứng minh ở mục 2.
- [Landau damping: Gevrey regularity and paraproducts - Clément Mouhot](https://www.youtube.com/watch?v=eja7NTV7Igs) (Institute for Advanced Study, tiếng Anh). Bài giảng của đồng tác giả Mouhot về lớp chính quy Gevrey và kỹ thuật paraproduct. Dành cho người muốn đi sâu vào kỹ thuật sau khi đọc xong bài.
