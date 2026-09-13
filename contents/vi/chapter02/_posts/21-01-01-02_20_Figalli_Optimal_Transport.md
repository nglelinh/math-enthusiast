---
layout: post
title: "Vận chuyển tối ưu và tính chính quy của Figalli (Huy chương Fields 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Alessio Figalli** nhận **Huy chương Fields 2018**

> “for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability.”
> — [IMU, Fields Medals 2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)

Citation này là citation của một **chương trình**, không phải tuyên bố một người đã phát minh cả một lĩnh vực. **Vận chuyển tối ưu (OT)** già hơn Figalli: Monge đặt bài map năm 1781, Kantorovich viết lại thành chương trình tuyến tính trên các coupling, Brenier đồng nhất map chi phí bình phương với gradient của thế lồi, Caffarelli xây lý thuyết chính quy sâu đầu tiên cho các thế ấy, còn Ambrosio, Villani và nhiều người khác biến OT thành ngôn ngữ cho PDE, hình học metric và xác suất. Huy chương của Figalli ghi nhận những gì ông làm *bên trong* ngôn ngữ đó: ông làm cho lý thuyết chính quy, ổn định và free-boundary của các map vận chuyển đủ sắc để nuôi bất đẳng thức hình học, mô hình khí quyển, và giải tích định lượng.

Bài này dành cho người đã thấy slogan Monge–Kantorovich trong [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) và muốn chương **tính chính quy** mà bài đó chỉ chỉ tới. Nó **không** coi Figalli là người sáng lập OT, và **không** nhầm Fields 2018 với huy chương 2010 của Villani. Chân dung động học sau này sẽ nằm ở [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đặt citation 2018 của Figalli vào lịch sử OT dài hơn (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) mà không gom lịch sử ấy thành một tên.
- Phát biểu slogan Brenier: với chi phí bình phương, map tối ưu là gradient của một thế lồi, và thế ấy thỏa phương trình **Monge–Ampère**.
- Giải thích vì sao **tính chính quy của map** là câu hỏi PDE, và vì sao lý thuyết Caffarelli là tiền bối chứ không phải chú thích.
- Mô tả, ở mức slogan, chính quy trong, ổn định, và chính quy từng phần / kiểm soát free-boundary của map OT, với công lao cho De Philippis và các cộng sự khác.
- Nêu hai vùng ứng dụng (bất đẳng thức đẳng chu định lượng; phương trình semigeostrophic) và nói vì sao chính quy của map là cầu nối.
- Phân biệt **Figalli 2018 (OT + ứng dụng)** với **Villani 2010 (Landau damping / Boltzmann)**.

**Kiến thức nền.** Công thức Monge và Kantorovich cùng ý push-forward $$T_\#\mu=\nu$$, như trong bài OT Chương 6; hàm lồi và Hessian; slogan rằng một PDE elliptic fully nonlinear có thể có lý thuyết chính quy. Không đòi giáo trình Monge–Ampère trước.

**Liên kết seminar.** Ghép với [Caffarelli / free boundary và Monge–Ampère]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) cho văn hóa chính quy cấp Abel mà Figalli thừa kế, và với [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) chỉ như *một* câu chuyện Fields PDE khác (giới hạn kinetic, không phải map vận chuyển).

---

## 1. Một lĩnh vực Figalli không phát minh

Nhiệm vụ sư phạm mở đầu vừa phủ định vừa hữu ích. Nếu bạn chỉ nhớ một câu từ hồ sơ phổ thông, hãy để là câu này: **Figalli không phát minh vận chuyển tối ưu.**

Monge hỏi làm sao chuyển một đống đất tới đích cho trước với chi phí tối thiểu, và đòi một **map** $$T$$. Kantorovich cho phép khối lượng tách, thay map bằng **coupling** $$\pi$$ với biên cố định, và mở dual lồi. Trong những năm 1980–1990, Brenier chứng minh rằng với cost $$c(x,y)=\|x-y\|^2$$ (dưới giả thuyết moment chuẩn), tồn tại map tối ưu dạng

$$
T=\nabla\phi,
$$

với $$\phi$$ lồi. McCann, Gangbo và những người khác mở bức tranh thế lồi sang hình học Riemannian và các cost tổng quát hơn. Caffarelli rồi hỏi câu của nhà giải tích: nếu mật độ đẹp, $$\phi$$ đẹp đến mức nào? Ambrosio phát triển OT như công cụ cho gradient flow và lý thuyết BV; Villani viết những cuốn sách biến chủ đề thành ngôn ngữ chung và dùng nó cho bất đẳng thức hình học cùng độ cong kiểu Ricci—trong khi **Huy chương Fields 2010** của ông là về phương trình kinetic, không phải về việc sáng lập OT.

Figalli học với **Luigi Ambrosio** (Pisa) và **Cédric Villani** (ENS Lyon), bảo vệ tiến sĩ năm 2007, và làm việc tại ETH Zürich từ 2016. Huy chương là giải thưởng chính quy-và-ứng dụng bên trong một lĩnh vực đã trưởng thành.

---

## 2. Từ map Brenier đến Monge–Ampère

Giả sử $$\mu=f\,dx$$ và $$\nu=g\,dy$$ là xác suất tuyệt đối liên tục trên (miền của) $$\mathbb{R}^n$$, và $$T=\nabla\phi$$ đẩy $$\mu$$ lên $$\nu$$. Đổi biến hình thức cho đồng nhất Jacobian

$$
f(x)=g\bigl(\nabla\phi(x)\bigr)\,\det D^2\phi(x).
$$

Đó là phương trình **Monge–Ampère** cho thế lồi $$\phi$$. Phương trình fully nonlinear: ẩn xuất hiện trong định thức các đạo hàm cấp hai. Các khái niệm nghiệm yếu (nghiệm Alexandrov, nghiệm viscosity) tồn tại rất lâu trước khi ta biết $$\phi$$ có $$C^2$$ hay không.

Vì sao chính quy quan trọng. Nếu $$\phi$$ chỉ lồi, $$T=\nabla\phi$$ xác định hầu khắp nơi nhưng có thể nhảy, gấp, hoặc không khả vi trên một tập lớn. Ứng dụng hình học muốn hơn: chúng muốn map là diffeomorphism trên các tập mở lớn, hoặc muốn kiểm soát định lượng mức map lệch khỏi map mô hình (tịnh tiến, đẳng cự tuyến tính, đồng nhất). Trong mô hình khí quyển, cùng map ấy là một phép đổi tọa độ; nếu quá thô, PDE trên không gian vật lý thậm chí không có nghĩa phân phối.

Vậy chương trình chính quy OT không phải đánh bóng thẩm mỹ. Nó là khoảng cách giữa “tồn tại map hầu khắp nơi” và “map là phép đổi biến dùng được.”

---

## 3. Lý thuyết chính quy Caffarelli như tiền bối

Lý thuyết chính quy sâu đầu tiên cho map OT chi phí bình phương là của **Caffarelli**. Đầu những năm 1990 ông chỉ ra rằng nghiệm Alexandrov của Monge–Ampère có $$C^{1,\alpha}$$ trong, và—dưới tính lồi của đích cùng tính trơn của mật độ—chính quy cao hơn, cuối cùng $$C^\infty$$ trong khi data trơn và miền hợp tác. Chính quy biên cần còn nhiều hình học hơn.

Citation Abel 2023 cho Caffarelli đúng văn hóa này: chính quy PDE phi tuyến, free boundary, và Monge–Ampère. Figalli nằm hạ lưu. Một câu seminar công bằng:

> Caffarelli chỉ ra rằng, trong khung Euclid lồi với cost bình phương, map tối ưu có thể chính quy bằng mật độ; Figalli và cộng sự hỏi điều gì còn lại khi tính lồi, cost, hoặc hình học nền không còn thuộc loại ấy.

Điều kiện Ma–Trudinger–Wang về sau cô lập một giả thuyết cấu trúc trên cost tổng quát giúp khôi phục tính trơn đầy đủ. Khi nó thất bại, hoặc khi giá không lồi, người ta không còn kỳ vọng map trơn toàn cục. Câu hỏi hiện đại trở thành **chính quy từng phần**: tập kỳ dị có nhỏ không?

---

## 4. Chính quy trong, ổn định, và free boundary của map

Giải tích OT của Figalli—thường cùng **Guido De Philippis**, và ở các bài khác với Kim, Loeper, và những người khác—có ba slogan đan vào nhau.

**Tích được bậc cao và chính quy Sobolev.** Nghiệm Alexandrov lồi không tiên nghiệm có $$D^2\phi$$ trong $$L^1_{\mathrm{loc}}$$. De Philippis–Figalli chứng minh chính quy $$W^{2,1}$$ cho Monge–Ampère (Inventiones, 2013), một ngưỡng nghe kỹ thuật cho đến khi nhớ rằng $$W^{2,1}$$ cho phép lấy đạo hàm map theo nghĩa $$L^1$$ và chuyển qua giới hạn trong các biểu thức phi tuyến. Các công trình tiếp theo cho ổn định cấp hai: nếu mật độ hội tụ, map hội tụ mạnh theo chuẩn Sobolev, không chỉ yếu.

**Chính quy từng phần.** Trong *Partial regularity for optimal transport maps* (Publ. Math. IHÉS, 2015), De Philippis–Figalli chứng minh rằng với cost tổng quát trên $$\mathbb{R}^n$$, hoặc với $$c=d^2/2$$ trên đa tạp Riemannian, map tối ưu giữa các mật độ trơn thì trơn **bên ngoài một tập kỳ dị đóng đo zero**. Kết quả không cần MTW và không cần giá lồi. Về tinh thần đây là định lý free-boundary / tập kỳ dị: map là diffeomorphism trên một tập mở lớn, và tập xấu đóng và null. Các kết quả $$C^1$$ hai chiều trước đó (Figalli–Loeper) và chính quy từng phần cho nghiệm Brenier (Figalli–Kim) thuộc cùng cụm.

**Ổn định bất đẳng thức.** Chính quy và ổn định đi cùng nhau. Nếu map gần map mô hình, các phiếm hàm hình học (chu vi, hằng số Sobolev, sinh entropy) phải gần tối ưu, với deficit tường minh. Đó là cầu từ ước lượng PDE sang hình học định lượng.

Công trình free-boundary sau này về obstacle và Stefan (Figalli–Serra, Figalli–Ros-Oton–Serra) là giải tích láng giềng, không phải gạch thứ ba của citation 2018. Văn bản huy chương là OT và các ứng dụng của nó.

---

## 5. Ứng dụng: bất đẳng thức, khí quyển, xác suất

**Bất đẳng thức đẳng chu định lượng.** Figalli–Maggi–Pratelli (Inventiones, 2010) dùng vận chuyển khối lượng để chứng minh dạng định lượng sắc của bất đẳng thức đẳng chu **định hướng** (anisotropic): nếu một tập gần cực tiểu hóa chu vi anisotropic thì nó gần (theo một khoảng cách chính xác) một tịnh tiến của hình Wulff. Phương pháp thuộc OT: một map vận chuyển từ tập tới một vật mô hình biến deficit chu vi thành deficit của map, rồi chính quy/ổn định biến thành độ gần hình học. Đây là mệnh đề “hình học metric” trong câu IMU được làm cụ thể.

**Phương trình semigeostrophic.** Hệ semigeostrophic (SG) là mô hình frontogenesis trong khoa học khí quyển. Sau khi đổi sang tọa độ địa chuyển, thế áp suất lồi và gradient của nó là map vận chuyển tối ưu giữa mật độ chất lỏng và một độ đo tham chiếu. Benamou–Brenier và Cullen làm từ điển ấy thành chuẩn; Ambrosio–Colombo–De Philippis–Figalli rồi dùng các ước lượng Sobolev mới cho Monge–Ampère để có nghiệm Euler yếu toàn cục trên torus hai chiều và, dưới giả thuyết lồi, trên miền lồi ba chiều. Ở đây chính quy OT không phải hệ quả. Nó là lý do vận tốc không gian vật lý là một phân phối xác định tốt.

**Bất đẳng thức hàm và xác suất.** Cùng Carlen, Figalli chứng minh ổn định cho bất đẳng thức Gagliardo–Nirenberg và log-HLS (với ứng dụng Keller–Segel). Cùng Guionnet ông dùng map vận chuyển xấp xỉ cho universality trong mô hình nhiều ma trận. Đó là mệnh đề “xác suất” của citation: vận chuyển như công cụ so độ đo, không chỉ như map giữa các đống cát.

---

## 6. Hai huy chương Fields, hai văn hóa kinetic

Vì Figalli là học trò Villani, dễ bịa hai huy chương thành một. Chúng không cùng một giải.

| Huy chương | Trọng tâm citation | Từ vựng chung | Khẳng định riêng |
|------------|-------------------|---------------|------------------|
| Villani, 2010 | Landau damping phi tuyến; hội tụ cân bằng cho Boltzmann | Entropy, bất đẳng thức, OT như toolkit Villani cũng phát triển | Định lý thư giãn kinetic |
| Figalli, 2018 | Lý thuyết OT và ứng dụng vào PDE, hình học metric, xác suất | Monge–Ampère, map, ổn định | Chính quy/ổn định vận chuyển và hệ quả hình học |

Văn bản IMU 2010 của Villani có nhắc ông tiên phong ứng dụng OT vào bất đẳng thức và viết sách về vận chuyển khối lượng; đó là nền, không phải câu huy chương. Câu 2018 của Figalli *chính là* câu OT. Một bài sau, [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/), sẽ giữ các định lý kinetic trong file riêng.

---

## 7. Vì sao Huy chương Fields

Ba lý do, không lý do nào đòi gọi OT là “lý thuyết của Figalli.”

1. **Độ khó.** Chính quy từng phần và ngưỡng Sobolev cho phương trình fully nonlinear nằm ở mép những gì giải tích lồi và lý thuyết Calderón–Zygmund nhìn thấy; chứng minh trộn nguyên lý cực đại Alexandrov, bất biến affine, và geometric measure theory.
2. **Xuất khẩu.** Một khi map thuộc $$W^{2,1}$$ hoặc trơn ngoài tập null, lĩnh vực khác dùng được: hình Wulff, front SG, mô hình ma trận, Keller–Segel.
3. **Rõ bản đồ còn lại.** Sau Caffarelli, người ta biết câu chuyện Euclid lồi. Sau Figalli–De Philippis và trường phái xung quanh, người ta biết một định lý trông ra sao khi cost tổng quát, miền là đa tạp, hoặc ứng dụng chỉ cần map Sobolev.

Với khóa học này, Figalli là chân dung **chính quy như hạ tầng**: không phải một giả thuyết có tên bị khép, mà một toolkit đủ mạnh để các định lý khác trở nên hợp lệ.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Figalli phát minh vận chuyển tối ưu.” | Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani và những người khác xây lĩnh vực; huy chương Figalli là chính quy cộng ứng dụng. |
| “Fields 2018 giống Villani 2010.” | Villani 2010 là Landau damping và Boltzmann; Figalli 2018 là OT và các cách dùng nó. |
| “Map Brenier luôn trơn.” | Thế lồi cho map hầu khắp nơi; tính trơn cần mật độ, tính lồi, cost, và thường chỉ đúng ngoài tập kỳ dị. |
| “Lý thuyết Caffarelli đã lỗi thời.” | Đó là nền; công trình sau hỏi điều gì còn lại khi bỏ giả thuyết hình học của ông. |
| “Chính quy từng phần nghĩa là map $$C^\infty$$ khắp nơi.” | Nghĩa là trơn ngoài một tập đóng null; tập kỳ dị có thể khác rỗng. |
| “Chính quy OT chỉ mang tính thẩm mỹ.” | Well-posedness SG và đẳng chu định lượng dùng các ước lượng như giả thuyết, không phải trang trí. |

---

## Bài tập

1. Trong hai câu, định lý Brenier thêm gì vào lý thuyết tồn tại Kantorovich cho cost bình phương?
2. Viết phương trình Monge–Ampère hình thức liên hệ mật độ $$f,g$$ với thế lồi $$\phi$$. Số hạng nào phi tuyến, và vì sao điều đó cản chính quy elliptic ngây thơ?
3. Vì sao **tính lồi của đích** xuất hiện trong các định lý chính quy đầy đủ của Caffarelli? Cho slogan, không chứng minh.
4. Phát biểu slogan chính quy từng phần De Philippis–Figalli (trơn ngoài tập đóng null). Nó *bỏ* những giả thuyết nào so với khung cổ điển của Caffarelli?
5. Giải thích, không quá tám câu, map tối ưu vào từ điển semigeostrophic thế nào. Vì sao chính quy $$W^{2,1}$$ của thế lại quan trọng cho công thức Euler yếu?
6. **Luyện độ chính xác.** Tìm một câu nói Figalli “tạo ra vận chuyển tối ưu.” Viết lại bằng hai câu chính xác phù hợp khóa học này.
7. So sánh Figalli 2018 với Villani 2010 trong một bảng bốn hàng của bạn: citation, phương trình, vai trò OT, điều không được claim.
8. **Seminar mở rộng.** Lướt phần mở của De Philippis–Figalli, *The Monge–Ampère equation and its link to optimal transportation* (Bull. AMS, 2014), và liệt kê năm từ khóa cần học tiếp (ví dụ nghiệm Alexandrov, MTW, c-convexity, hình Wulff, tọa độ Cullen–Purser).

---

## Liên kết

- IMU Fields Medals 2018: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)
- Wikipedia — Alessio Figalli: [https://en.wikipedia.org/wiki/Alessio_Figalli](https://en.wikipedia.org/wiki/Alessio_Figalli)
- Trang ETH (chính quy map): [https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps](https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps)
- Hồ sơ Quanta (2018): [https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/](https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/)
- Tìm arXiv — Figalli Monge–Ampère: [https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all](https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all)
- De Philippis–Figalli $$W^{2,1}$$ (arXiv:1111.7207): [https://arxiv.org/abs/1111.7207](https://arxiv.org/abs/1111.7207)
- De Philippis–Figalli chính quy từng phần (arXiv:1209.5640): [https://arxiv.org/abs/1209.5640](https://arxiv.org/abs/1209.5640)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 2018 — Alessio Figalli.
2. Y. Brenier, “Polar factorization and monotone rearrangement of vector-valued functions,” *Comm. Pure Appl. Math.* 44 (1991).
3. L. A. Caffarelli, các bài về chính quy Monge–Ampère và map OT (đầu thập niên 1990); citation Abel 2023.
4. G. De Philippis và A. Figalli, “$$W^{2,1}$$ regularity for solutions of the Monge–Ampère equation,” *Invent. Math.* 192 (2013); “Partial regularity for optimal transport maps,” *Publ. Math. IHÉS* 121 (2015); survey trong *Bull. Amer. Math. Soc.* 51 (2014).
5. A. Figalli, F. Maggi và A. Pratelli, “A mass transportation approach to quantitative isoperimetric inequalities,” *Invent. Math.* 182 (2010).
6. L. Ambrosio, M. Colombo, G. De Philippis và A. Figalli, các kết quả well-posedness Euler cho phương trình semigeostrophic (khung 2D tuần hoàn và 3D lồi).
7. A. Figalli, *The Monge–Ampère Equation and Its Applications*, EMS (2017).
8. C. Villani, *Topics in Optimal Transportation*; *Optimal Transport: Old and New* — ngôn ngữ nền, không phải citation Fields 2010.
9. Khóa học: [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/), tương lai [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Hướng đi tiếp

- Đọc ước lượng trong của Caffarelli cạnh chính quy từng phần De Philippis–Figalli: những giả thuyết hình học nào chuyển từ “được giả sử” sang “không cần cho tính trơn hầu khắp nơi”?
- So OT tính toán (Sinkhorn, Chương 6) với lý thuyết giải tích: số học regularize; lý thuyết chính quy giải thích khi nào map chưa regularize đã gần như trơn.
