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

Citation là lý thuyết động học (kinetic theory), không phải vận chuyển tối ưu. Villani cũng là tác giả hai cuốn sách chuẩn về optimal transportation—*Topics in Optimal Transportation* (AMS, 2003) và *Optimal Transport: Old and New* (Springer, 2009)—và mặt đó thiết yếu cho giải tích và hình học hiện đại. Đó **không** phải điều IMU nêu năm 2010. Khóa học này vì thế coi vận chuyển như ngôn ngữ láng giềng: xem [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/). Hồi ký *Théorème vivant* / *Birth of a Theorem* kể cảm giác của một chứng minh; đó **không** phải bài báo nghiên cứu và sẽ không được trích như bài báo.

Huy chương 2010 ghi nhận hai định lý PDE trong vật lý thống kê. **Landau damping phi tuyến** (cùng Clément Mouhot) là phát biểu không va chạm, thuộc Vlasov: một cân bằng plasma thuần nhất có thể xóa dao động điện vĩ mô mà không cần va chạm, kể cả sau khi rời tuyến tính hóa của Lev Landau (1946). **Hội tụ về cân bằng cho phương trình Boltzmann** (cùng Laurent Desvillettes và trong chương trình hypocoercivity của Villani) là phát biểu có va chạm: sản xuất entropy, dưới các giả thuyết chính quy và dương tính được nêu rõ trong các bài báo, buộc nghiệm tiến tới Maxwellian. Không kết quả nào là lý thuyết đầy đủ, không điều kiện, về nghiệm trơn toàn cục cho mọi nhân va chạm thú vị về mặt vật lý. Huy chương nói về **tốc độ và cơ chế** khi đã ở chế độ chính quy, và về một hiện tượng tắt dần phi tuyến mà các nhà vật lý tin tưởng hàng thập niên mà chưa có chứng minh toán học đầy đủ.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt khung **Vlasov** (không va chạm, trường tự hợp) của Landau damping với khung **Boltzmann** (có va chạm) của xu hướng về cân bằng.
- Nêu khám phá 1946 của Landau ở mức khẩu hiệu: plasma tuyến tính hóa, không va chạm, có thể tắt dao động điện trường.
- Ghi công **Mouhot–Villani** cho định lý phi tuyến (chính quy analytic, và một số lớp Gevrey; thế không thô hơn Coulomb/Newton).
- Mô tả định lý $$H$$ của Boltzmann như sản xuất entropy, và giải thích vì sao **không thuần nhất không gian** làm xu hướng về cân bằng khó hơn nhiều so với trường hợp thuần nhất.
- Giải thích **hypocoercivity** ở mức khẩu hiệu: tiêu tán suy biến vẫn sinh khe phổ sau khi trộn các biến bổ sung.
- Nêu các kết quả hội tụ kiểu Desvillettes–Villani là **có điều kiện** trên độ trơn, suy giảm, và dương tính—không phải lý thuyết chính quy toàn cục không điều kiện.
- Tách citation IMU 2010 khỏi sách **vận chuyển tối ưu** của Villani và khỏi hồi ký phổ thông *Birth of a Theorem*.

**Kiến thức nền.** Phương trình vi phân thường và đạo hàm riêng ở mức khóa giải tích nghiêm túc đầu tiên; mật độ xác suất $$f(t,x,v)$$ trên không gian vị trí–vận tốc; entropy như phiếm hàm Lyapunov. Cơ học Hamilton và Fourier giúp cho Landau damping nhưng không giả định đầy đủ.

**Liên kết seminar.** LO1 (chương trình biến cơ chế vật lý thành ước lượng). Ghép [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/) cho mặt kia của Villani, và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) cho văn hóa rộng hơn. Láng giềng cùng năm: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/).

---

## 1. Hai thế giới động học

Một phương trình động học mô tả khí hoặc plasma bằng mật độ $$f(t,x,v)$$ của hạt tại thời $$t$$, vị trí $$x$$, vận tốc $$v$$. Hai đóng kín cực trị thống trị huy chương.

Trong thế giới **Vlasov–Poisson** (hoặc Vlasov–Maxwell), hạt không va chạm. Chúng cảm nhận trường tự hợp $$E$$ lấy từ mật độ điện tích $$\rho=\int f\,dv-1$$ (điện tích nền chuẩn hóa). Phương trình sơ đồ là

$$
\partial_t f + v\cdot\nabla_x f + E[f]\cdot\nabla_v f = 0.
$$

Tính thuận nghịch hiển nhiên ở mức đặc trưng: không có toán tử va chạm Boltzmann, nên không có định lý $$H$$ tức thì. Tắt dần, nếu xảy ra, phải đến từ **trộn pha**—các sợi trong $$(x,v)$$ trung bình hóa thành mật độ không gian yên—không từ va chạm.

Trong thế giới **Boltzmann**, hạt va chạm. Phương trình sơ đồ là

$$
\partial_t f + v\cdot\nabla_x f = Q(f,f),
$$

trong đó $$Q$$ là toán tử va chạm song tuyến mã hóa luật va chạm vi mô (cầu cứng, nhân cutoff, kỳ dị kiểu Coulomb, \ldots). Phiếm hàm $$H$$ của Boltzmann $$H(f)=\int f\log f$$ giảm (dưới giả thuyết thích hợp), và các cân bằng duy nhất là Maxwellian. Câu hỏi toán học là tồn tại, chính quy, và $$f(t)$$ tiến **nhanh thế nào** tới Maxwellian tương thích với khối lượng, động lượng, năng lượng bảo toàn.

Citation của Villani sống ở cả hai thế giới. Trộn chúng trong một câu—“ông chứng minh khí cân bằng”—xóa sự phân biệt mà IMU viết cẩn thận.

---

## 2. Landau damping: tuyến tính rồi phi tuyến

Năm 1946, Lev Landau phân tích phương trình Vlasov–Poisson tuyến tính hóa quanh cân bằng thuần nhất $$f^0(v)$$ (ví dụ Maxwellian). Ông thấy điện trường có thể suy giảm hàm mũ theo thời gian dù phương trình thuận nghịch và không va chạm. Cơ chế không phải tiêu tán theo nghĩa $$L^2$$ thông thường: đó là triệt **trộn pha**, thấy được sau biến đổi Fourier theo $$x$$ và biến dạng contour cẩn thận trên mặt phẳng vận tốc phức (contour Landau). Landau damping tuyến tính trở thành trụ cột vật lý plasma.

Tắt dần phi tuyến là định lý khác. Số hạng phi tuyến $$E[f]\cdot\nabla_v f$$ sinh echo và cộng hưởng; lâu nay không rõ chúng có phá hủy suy giảm tuyến tính không. **Clément Mouhot** và **Cédric Villani** chứng minh rằng, với nhiễu analytic của một cân bằng thuần nhất ổn định (và, trong một mở rộng, một số lớp Gevrey), và với thế tương tác không kỳ dị hơn Coulomb hoặc Newton, phương trình Vlasov phi tuyến thể hiện Landau damping hàm mũ: trường lực suy giảm, mật độ hội tụ tới trạng thái thuần nhất gần đó, trong khi hàm phân bố vẫn gần một tiến hóa free-transport trong các chuẩn analytic thích nghi. Bài báo là Mouhot–Villani, “On Landau damping,” *Acta Mathematica* 207 (2011), 29–201, arXiv:0904.2760.

Chứng minh diễn giải tắt dần như **chuyển chính quy** giữa biến động học và biến không gian, chứ không như mất năng lượng. Nó dùng chuẩn analytic đo so với free transport, ước lượng echo phi tuyến, và sơ đồ Newton với hương vị các tác giả so với lý thuyết KAM. **Ghi công Mouhot.** Kết quả là chung; các tường thuật phổ thông “Villani chứng minh Landau damping” là không đủ.

**Định lý không nói gì.** Không phải phát biểu không điều kiện cho dữ liệu Sobolev tùy ý, cũng không phân loại mọi bất ổn định có thể (bất ổn định two-stream và họ hàng tuyến tính vẫn bất ổn). Đó là định lý ổn định-và-tắt dần phi tuyến ở chính quy cao.

---

## 3. Boltzmann: entropy, không thuần nhất, tính có điều kiện

Với phương trình Boltzmann **thuần nhất không gian** (không phụ thuộc $$x$$), phương pháp entropy và ước lượng khe phổ có lịch sử dài; Villani đóng góp các định lý $$H$$ định lượng và công trình về bất đẳng thức kiểu Cercignani (gồm “Cercignani’s conjecture is sometimes true and always almost true,” *Comm. Math. Phys.* 234 (2003)). “Hội tụ về cân bằng” trong citation huy chương nhằm đặc biệt vào phương trình **không thuần nhất không gian**, nơi vận chuyển $$v\cdot\nabla_x$$ và va chạm $$Q$$ tương tác.

Desvillettes và Villani, “On the trend to global equilibrium for spatially inhomogeneous kinetic systems: The Boltzmann equation,” *Invent. Math.* 159 (2005), 245–316, thu được tốc độ dạng $$O(t^{-\infty})$$—nhanh hơn mọi đa thức—**có điều kiện** trên các chặn mạnh, tự nhiên: độ trơn, suy giảm ở vận tốc lớn, và dương tính chặt. Bài báo nói rõ các chặn đó, vào thời điểm ấy, mới được thiết lập trong một số trường hợp đặc biệt. Công trình sau (trường phái Guo; ước lượng hypocoercivity của nhiều tác giả) đã mở rộng lãnh thổ không điều kiện, nhưng khóa học này sẽ không viết lại định lý 2005 thành lý thuyết chính quy toàn cục đầy đủ cho Boltzmann.

Chiến lược kết hợp định lý $$H$$ định lượng (sản xuất entropy kiểm soát khoảng cách tới Maxwellian địa phương), bất ổn định định lượng của mô tả thủy động khi số Knudsen không nhỏ (không thể ẩn mãi trong một chất lưu tiến hóa chậm), các bất đẳng thức hình học (gồm bất đẳng thức kiểu Korn từ công trình Desvillettes–Villani trước đó), và một hệ bất đẳng thức vi phân chuyển sản xuất entropy địa phương thành suy giảm toàn cục.

---

## 4. Hypocoercivity, vận chuyển, và vì sao có Fields

**Hypocoercivity** là tên Villani đặt (Memoirs of the AMS, 2009) cho tiêu tán suy biến vẫn cho ước lượng coercive sau khi trộn bởi một phần bảo toàn. Va chạm có thể chỉ tắt theo $$v$$; móc với vận chuyển sinh tiêu tán theo $$x$$, theo tinh thần tổng bình phương Hörmander. Đó không phải một định lý IMU đơn lẻ; đó là văn hóa trong đó “hội tụ về cân bằng” trở thành tốc độ constructive chứ không phải lập luận compact không có tốc độ. Bài giảng ICM 2006 đã quảng bá khuếch tán hypocoercive; huy chương 2010 nhìn lại chương trình đó khi nó gặp Boltzmann và Landau.

Bài toán Monge, coupling Kantorovich, và khoảng cách Wasserstein $$W_p$$ là lingua franca mà Villani dạy một thế hệ, qua *Topics in Optimal Transportation* và *Optimal Transport: Old and New*; độ cong Ricci tổng hợp Lott–Villani (và độc lập Sturm) là nhánh hình học; Fields 2018 của Figalli nằm ở chính quy ánh xạ vận chuyển. **Không điều nào là câu 2010.** Thói quen seminar là một chạc: Fields 2010 = tắt dần Mouhot–Villani + Desvillettes–Villani / Boltzmann hypocoercive; sự nghiệp song song = vận chuyển. Đọc [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/) cho chạc thứ hai.

Lý thuyết động học có entropy, định lý $$H$$, và contour Landau, nhưng ít định lý phi tuyến khớp khẩu hiệu vật lý ở mức tốc độ. Mouhot–Villani biến tính toán tuyến tính 1946 thành định lý phi tuyến; Desvillettes–Villani làm “entropy tăng” định lượng cho khí không thuần nhất, với giả thuyết viết công khai. Hồi ký *Birth of a Theorem* là văn chương về sự cộng tác đó. Định lý là bài *Acta*.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Huy chương 2010 là về vận chuyển tối ưu.” | Citation IMU là Landau damping và cân bằng Boltzmann. Vận chuyển là sự nghiệp lớn riêng. |
| “Villani một mình chứng minh Landau damping phi tuyến.” | Định lý là **Mouhot–Villani**. |
| “Landau đã chứng minh kết quả phi tuyến năm 1946.” | Phân tích của Landau là **tuyến tính**. Bài toán phi tuyến còn mở hàng thập niên. |
| “Desvillettes–Villani cho nghiệm trơn toàn cục không điều kiện của Boltzmann.” | Tốc độ của họ **có điều kiện** trên chính quy, suy giảm, và dương tính nêu trong bài. |
| “*Birth of a Theorem* là bài báo.” | Đó là hồi ký (Pháp 2012, Anh 2015), không phải bài nghiên cứu. |
| “Landau damping dùng va chạm.” | Đó là hiện tượng **không va chạm** (Vlasov); Boltzmann là đối tác có va chạm trong citation. |

---

## Bài tập

1. Viết bốn câu một nhà vật lý chấp nhận được: Landau damping tuyến tính hóa là gì, và vì sao tính thuận nghịch của Vlasov không phải mâu thuẫn tức thì?
2. Vì sao số hạng phi tuyến đe dọa suy giảm tuyến tính? Trả lời ở mức khẩu hiệu (echo / cộng hưởng), không giả vờ tái tạo bài *Acta*.
3. Nêu khác biệt giữa định lý xu hướng về cân bằng **có điều kiện** và định lý **chính quy toàn cục**. Desvillettes–Villani 2005 thuộc loại nào?
4. Hypocoercivity trong một đoạn: tiêu tán suy biến + trộn $$\Rightarrow$$ suy giảm. Vẽ cartoon (vận chuyển theo $$x$$, va chạm theo $$v$$).
5. Mở *Topics in Optimal Transportation* hoặc chương [vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và viết ba câu về Monge versus Kantorovich. rồi một câu giải thích vì sao tư liệu đó **không** phải citation 2010.
6. Luyện gán công: viết cho **Landau (1946)**, **Mouhot**, **Desvillettes**, và **Villani** mỗi người một mệnh đề chính xác.
7. **Luyện độ chính xác.** Viết lại “Villani chứng minh entropy luôn diệt hỗn loạn tức thì” thành hai câu khóa học này chấp nhận.
8. **Seminar.** So huy chương này với [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/): cả hai đều “vật lý thống kê,” nhưng một là lattice/conformal và một là động học/PDE. “Giới hạn scaling” nghĩa là gì trong mỗi câu chuyện?

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

- Đọc phần mở Mouhot–Villani (trộn pha versus mất năng lượng) trước các chuẩn analytic; so định lý $$H$$ thuần nhất với sơ đồ Desvillettes–Villani không thuần nhất.
- Gợi ý seminar: bạn kỳ vọng Landau damping phi tuyến thất bại ở lớp chính quy nào, và vì sao điều đó không mâu thuẫn với định lý *Acta*?
