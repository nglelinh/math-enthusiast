---
layout: post
title: "John Pardon: Hình học Symplectic và Tôpô (Huy chương Fields 2026)"
chapter: '02'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Nếu hình học Euclid cho ta thước đo *độ dài* và *góc*, thì **hình học symplectic** — ngôn ngữ hình học của cơ học cổ điển Hamilton — lại chỉ quan tâm đến *diện tích có hướng* trong không gian pha. Trong thế giới kỳ lạ ấy, mọi đa tạp symplectic cùng số chiều nhìn cục bộ đều giống hệt nhau (định lý Darboux), nên không có khái niệm "độ cong cục bộ" để phân biệt chúng. Muốn khám phá hình dạng toàn cục của một không gian symplectic, các nhà toán học thả vào đó những "đầu dò" gọi là **đường cong chỉnh hình** rồi đếm xem có bao nhiêu đường cong thỏa điều kiện cho trước.

Nghe thì tưởng gọn gàng, nhưng suốt nhiều thập kỷ, cả một tòa lâu đài lý thuyết (bất biến Gromov–Witten, đồng điều Floer, **phạm trù Fukaya** của đối xứng gương) đứng trước một vết nứt nền móng nguy hiểm: tập hợp mọi đường cong chỉnh hình (không gian moduli) hiếm khi trơn tru và đúng số chiều như kỳ vọng! Nếu không có một cách "đếm" chặt chẽ khi không gian moduli bị méo mó hay có điểm kỳ dị, rất nhiều định lý quan trọng chỉ dừng lại ở mức phác thảo.

**John Pardon** (Stony Brook / Simons Center) nhận **Huy chương Fields 2026** chính vì đã gia cố và xây lại tầng nền móng ấy: phát triển các cách tiếp cận mới cho **chu trình cơ bản ảo** (*virtual fundamental cycle*), xây dựng chặt chẽ **phạm trù Fukaya** cho những lớp đa tạp rộng lớn, và đồng thời đóng góp những kết quả nổi bật cho tôpô chiều thấp như tác động nhóm trên đa tạp 3 chiều và lý thuyết nút.

**Trích dẫn ngắn của IMU:**  
For his achievements in symplectic geometry including new approaches to virtual fundamental cycles, Fukaya categories of certain manifolds and counting holomorphic curves, and for his contributions to other areas of geometry and topology, including group actions on 3-manifolds and knot theory.

*Tạm dịch:* Cho các thành tựu trong hình học symplectic, gồm những cách tiếp cận mới cho chu trình cơ bản ảo, phạm trù Fukaya của một số đa tạp và việc đếm đường cong chỉnh hình, cùng những đóng góp cho các lĩnh vực khác của hình học và tôpô, gồm tác động nhóm trên đa tạp 3 chiều và lý thuyết nút.

Bài này dành cho người học đã biết tôpô vi phân cơ bản và muốn hiểu: *vì sao* việc "đếm đường cong" lại cần đến kỹ thuật ảo, *phạm trù Fukaya* là loại bất biến gì, và *cách* đọc slide ICM 2026 về tính chính quy dẫn xuất loga (*log derived regularity*) mà không nhầm nó với nội dung đã được trao giải.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu hình học symplectic nghiên cứu gì: 2-dạng đóng không suy biến, động lực Hamilton, và đường cong chỉnh hình như công cụ dò cấu trúc toàn cục.
- Giải thích vì sao không gian moduli của các đường cong **thường** không phải là đa tạp trơn với số chiều như dự kiến, và vì sao cần **chu trình cơ bản ảo** (virtual fundamental cycle).
- Mô tả **phạm trù Fukaya** như một bất biến dạng phạm trù, xây dựng từ các đa tạp con Lagrange và các đĩa chỉnh hình, đóng vai trò trung tâm trong đối xứng gương.
- Thấy rằng công trình của Pardon trải rộng từ **hình học symplectic** đến **tôpô chiều thấp** (tác động nhóm, lý thuyết nút).
- Đọc định lý **Log Derived Regularity** trên slide ICM như một công trình **đang thực hiện**, không phải nội dung của lời trích dẫn IMU.
- Tránh hai hiểu lầm: coi chu trình ảo chỉ là "chi tiết kỹ thuật vô hại", và coi đoạn reel trên Facebook là toàn bộ bài giảng.

**Kiến thức cần có.** Đa tạp trơn, dạng vi phân, ý tưởng về đồng điều, và hiểu "không gian moduli là không gian tham số hóa một họ đối tượng".

**Liên hệ với khóa học.** So sánh kiểu huy chương "cho nền tảng" (Pardon, [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/)) với kiểu huy chương "cho một giả thuyết nổi tiếng". Có thể đọc cùng bài [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), nơi không gian moduli được hiểu theo nghĩa khác (moduli của mặt Riemann).

---

## Bản đồ kiến thức nền: Hình học symplectic và Không gian pha là gì?

Để hình dung rõ ngành toán học phía sau công trình của Pardon, hãy quay về một hình ảnh rất quen thuộc của vật lý đại học:

- **Không gian pha và dạng symplectic $$\omega$$:** Khi mô tả một hạt chuyển động trong không gian $$n$$ chiều, trạng thái của nó tại mỗi thời điểm được xác định bởi $$n$$ tọa độ vị trí $$(q_1, \dots, q_n)$$ và $$n$$ tọa độ động lượng $$(p_1, \dots, p_n)$$ — tổng cộng là $$2n$$ chiều (luôn là **số chiều chẵn**!). Dạng symplectic chuẩn $$\omega = \sum_{i=1}^n dq_i \wedge dp_i$$ đo tổng diện tích có hướng của hình chiếu lên từng mặt phẳng $$(q_i, p_i)$$. Trong cơ học cổ điển, khi hệ tiến hóa theo phương trình Hamilton, thể tích không gian pha không chỉ được bảo toàn, mà chính 2-dạng $$\omega$$ cũng được bảo toàn tuyệt đối.
- **"Cứng" hay "mềm"? Định lý con lạc đà symplectic của Gromov:** Trong không gian bảo toàn thể tích thông thường, bạn luôn có thể bóp một quả cầu cao su bán kính $$R$$ thành một sợi dây dài vô tận để luồn vừa khít vào một ống trụ bán kính $$r$$ nhỏ tùy ý. Nhưng năm 1985, Mikhail Gromov gây chấn động khi chứng minh **định lý không ép được** (*nonsqueezing theorem*): nếu chỉ dùng các phép biến đổi bảo toàn dạng symplectic $$\omega$$, bạn **không bao giờ** nhét được quả cầu 4 chiều bán kính $$R$$ vào ống trụ symplectic bán kính $$r < R$$ — dù thể tích của ống trụ là vô hạn! Điều này cho thấy hình học symplectic mang một kiểu "độ cứng toàn cục" bí ẩn, nằm giữa hình học Riemann (rất cứng) và tô pô bảo toàn thể tích (rất mềm).
- **Vì sao cần "đếm đường cong ảo"?** Gromov đã chứng minh định lý trên bằng cách cho các **đường cong chỉnh hình** (phiên bản 2 chiều của đường trắc địa) đi qua đa tạp symplectic. Muốn biến kỹ thuật đó thành các bất biến đếm được (đếm số đĩa chỉnh hình căng giữa các đa tạp con Lagrange để lập nên *phạm trù Fukaya*), ta cần giao cắt đẹp (**điều kiện hoành**, giống như hai đường thẳng trên mặt phẳng cắt nhau tại 1 điểm rõ ràng thay vì trùng khít lên nhau). Khi hai đường cong lại cứ trùng nhau (như hiện tượng *phủ bội* — một đường cong quấn nhiều vòng quanh chính nó), phép đếm ngây thơ hỏng hoàn toàn, và đó là lúc **chu trình cơ bản ảo** ra tay.

---

## 1. Hình học symplectic tóm tắt trong một trang

Một **đa tạp symplectic** $$(M,\omega)$$ là một đa tạp có 2-dạng $$\omega$$ thỏa:

1. **Đóng:** $$d\omega=0$$;  
2. **Không suy biến:** tại mỗi điểm, $$\omega_p$$ là dạng song tuyến tính đối xứng lệch không suy biến trên $$T_pM$$ (từ đại số tuyến tính suy ra số chiều của $$M$$ bắt buộc phải chẵn).

**Ví dụ cơ bản.** Phân thớ đối tiếp xúc $$T^*Q$$ với dạng symplectic chính tắc (lấy vi phân của dạng Liouville); không gian Euclid chiều chẵn $$\mathbb{R}^{2n}$$ với dạng chuẩn $$\sum dq_i \wedge dp_i$$. Cơ học Hamilton được phát biểu tự nhiên trên đa tạp symplectic: mỗi hàm năng lượng Hamilton $$H$$ sinh ra một trường vector $$X_H$$ theo công thức

$$
\iota_{X_H}\omega = dH,
$$

và dòng của $$X_H$$ bảo toàn $$\omega$$ (dạng hình học của định lý Liouville).

**Cấu trúc gần phức.** Người ta thường chọn một cấu trúc gần phức (*almost complex structure*) $$J$$ tương thích với $$\omega$$ (tức $$J^2 = -\mathrm{Id}$$) để định nghĩa **đường cong chỉnh hình**: đó là ánh xạ $$u:(\Sigma,j)\to(M,J)$$ thỏa phương trình Cauchy–Riemann phi tuyến

$$
du\circ j = J\circ du.
$$

Từ công trình của Gromov, đường cong chỉnh hình (và các biến thể trong lý thuyết Floer) trở thành **công cụ dò tôpô symplectic toàn cục**. Theo định lý Darboux, mọi đa tạp symplectic nhìn cục bộ đều giống hệt $$\mathbb{R}^{2n}$$ chuẩn, nên tọa độ cục bộ không phân biệt được chúng. Đường cong chỉnh hình phát hiện được những ràng buộc toàn cục mà tọa độ cục bộ không thấy.

**Tóm lại.** Hình học symplectic nghiên cứu "diện tích có hướng" cho bởi một 2-dạng không suy biến, các động lực bảo toàn nó, và dùng đường cong chỉnh hình để xây dựng bất biến.

---

## 2. Đếm đường cong: khi điều kiện hoành không thỏa

Để "đếm" các đường cong chỉnh hình thỏa điều kiện biên hoặc đi qua các điểm cho trước, người ta xây dựng **không gian moduli** $$\mathcal{M}$$ gồm các ánh xạ thỏa phương trình Cauchy–Riemann (sai khác các tự đẳng cấu của miền xác định).

Trong trường hợp lý tưởng:

- toán tử tuyến tính hóa là toán tử Fredholm;
- điều kiện hoành (*transversality*) đảm bảo $$\mathcal{M}$$ là đa tạp trơn có số chiều bằng chỉ số Fredholm;
- một phép compact hóa tốt cho phép lấy **lớp cơ bản** $$[\mathcal{M}]\in H_*(\overline{\mathcal{M}})$$ rồi tích phân hoặc đếm trên đó.

**Trên thực tế.** Với cấu trúc gần phức tổng quát, điều kiện hoành có thể đạt được trong một số trường hợp đơn giản. Nhưng trên nhiều đa tạp đáng quan tâm, khi có điều kiện biên Lagrange, khi có các đường cong **phủ bội** (*multiple cover*, kiểu như ánh xạ $$z \mapsto z^2$$ quấn hai vòng lên cùng một hình cầu), hay khi đường cong suy biến thành nhiều mảnh nối nhau, không gian moduli **không** phải là đa tạp trơn với số chiều như dự kiến. Nó có thể có điểm kỳ dị kiểu orbifold, có thành phần với số chiều lớn hơn dự kiến, và có các phân thớ cản trở (*obstruction bundle*).

Nếu không có một lớp cơ bản đáng tin cậy, các "số đếm Gromov–Witten hay Floer" có thể **không được định nghĩa** một cách nhất quán.

### 2.1. Chu trình cơ bản ảo

**Lớp (hay chu trình) cơ bản ảo** (*virtual fundamental class/cycle*) là một lớp đồng điều (hoặc một xích) thay thế, xác định trên phép compact hóa của không gian moduli. Hãy hình dung một ví dụ siêu đơn giản trong mặt phẳng: nếu hai đường tròn cắt nhau ngang (hoành) tại 2 điểm, ta đếm được 2; nếu chúng *tiếp xúc* nhau tại 1 điểm (mất tính hoành), hoặc thậm chí *trùng khít* lên nhau (sai hẳn số chiều!), thì nhiễu nhẹ một đường tròn sẽ giúp đọc ra số giao "ảo" có dấu không phụ thuộc vào cách nhiễu. Trên không gian moduli vô hạn chiều, việc thực hiện phép "nhiễu có hệ thống" này cực kỳ gian nan (đòi hỏi cấu trúc Kuranishi, polyfold hay hình học dẫn xuất).

Đây không phải chi tiết phụ. Nó là **ranh giới giữa định lý và phát biểu chưa chứng minh**. Nhiều bất biến chỉ thực sự trở thành toán học chặt chẽ khi kỹ thuật ảo được xây dựng hoàn hảo.

**Đóng góp của Pardon được nêu trong trích dẫn.** Pardon đưa ra khung **implicit atlas** (tập bản đồ ẩn) thuần túy đại số–tô pô cực kỳ sáng sủa để xây dựng chu trình cơ bản ảo và đếm đường cong chỉnh hình trong các trường hợp khó, làm nền vững chắc cho đồng điều Floer và đồng điều tiếp xúc.

---

## 3. Phạm trù Fukaya: biến các đa tạp con Lagrange thành bất biến

Một **đa tạp con Lagrange** $$L\subset(M,\omega)$$ có số chiều bằng một nửa $$\dim M$$ và thỏa $$\omega\vert_L=0$$ (chẳng hạn trong không gian pha $$2n$$ chiều, không gian cấu hình $$n$$ chiều gồm các tọa độ vị trí $$(q_1, \dots, q_n)$$ là một đa tạp con Lagrange mẫu mực). Trong đối xứng gương, chúng là các đối tượng ở phía mô hình A (*A-model*).

**Phạm trù Fukaya** (và các biến thể) được tổ chức như sau:

- **đối tượng:** các đa tạp con Lagrange (kèm dữ liệu phân bậc, cấu trúc spin, nhiễu…);
- **cấu xạ:** phức Floer, sinh bởi các giao điểm của hai đa tạp con Lagrange (hoặc các đường cong có biên nằm trên chúng);
- **phép hợp thành:** đếm các đĩa chỉnh hình có biên nằm trên các Lagrange liên quan (ví dụ 3 Lagrange $$L_0, L_1, L_2$$ cắt nhau tại $$p, q, r$$, ta đếm số tam giác chỉnh hình nối 3 giao điểm ấy!).

Kết quả là một **bất biến dạng phạm trù** (thường là phạm trù $$A_\infty$$) của đa tạp symplectic. Nó mạnh hơn một nhóm đồng điều đơn lẻ, vì nó ghi lại toàn bộ mạng lưới cách các Lagrange giao nhau và liên hệ với nhau qua các đường cong chỉnh hình.

**Đối xứng gương (nói ngắn gọn).** Phía mô hình B là hình học phức, với phạm trù các bó nhất quán (*coherent sheaf*). Phía mô hình A là phạm trù Fukaya. Giả thuyết **đối xứng gương đồng điều** của Kontsevich dự đoán hai phạm trù từ hai thế giới hoàn toàn khác nhau này lại tương đương với nhau!

**Vì sao điều này liên quan đến giải Fields.** Xây dựng phạm trù Fukaya một cách **chặt chẽ** trên những đa tạp đáng quan tâm (và tính toán chúng bằng kỹ thuật địa phương hóa/cắt dán như công trình của Ganatra–Pardon–Shende về *Liouville sectors*) đòi hỏi chính các nền tảng về chu trình ảo, tính compact và điều kiện hoành ở trên. Trích dẫn của IMU ghi rõ là "phạm trù Fukaya của một số đa tạp" (*Fukaya categories of certain manifolds*), không phải một phát biểu chung chung.

---

## 4. Tôpô chiều thấp: tác động nhóm và lý thuyết nút

Lời trích dẫn không chỉ nói về hình học symplectic. Pardon còn được ghi nhận vì các đóng góp sâu sắc về **tác động nhóm trên đa tạp 3 chiều** (chứng minh **giả thuyết Hilbert–Smith** trong 3 chiều — một bài toán mở hàng chục năm hỏi liệu nhóm số nguyên $$p$$-adic có thể tác động hữu hiệu lên một đa tạp 3 chiều không!) và **lý thuyết nút** (cùng những kết quả nối lý thuyết nút với đồng điều tiếp xúc). Điều này cho thấy cùng một nhà toán học có thể kết hợp nhuần nhuyễn trực giác của tôpô hình học cổ điển cả trong lẫn ngoài lĩnh vực đường cong chỉnh hình.

Lời khuyên cho người học: đừng nghĩ "Fields cho hình học symplectic nghĩa là chỉ có bất biến Gromov–Witten". Hãy đọc cả hai nửa của lời trích dẫn.

---

## 5. Bài giảng Fields tại ICM 2026: tính chính quy dẫn xuất loga (đang thực hiện)

Tại **ICM 2026** (Philadelphia), bài giảng Fields của Pardon trình bày cả những công trình về không gian moduli vượt ra ngoài các mục chính trong lời trích dẫn ngắn của IMU. Một đoạn reel công khai cho thấy slide cuối cùng (19/19) có tiêu đề **Logarithmic derived regularity**.

### Định lý (Log Derived Regularity Theorem; đang thực hiện)

*Viết lại từ nội dung trên slide, không phải từ lời giảng đầy đủ.*

Cho

$$
W \xrightarrow{\mathrm{strict}} C \xrightarrow{\mathrm{exact}} B
$$

là một **bài toán lát cắt elliptic** (elliptic section problem) trên một đa tạp **log trơn** (log smooth) $$B$$. Giả sử $$C\to B$$ là ánh xạ riêng (proper) và có độ sâu một (depth one), và giả sử **các đầu mút không suy biến** hoặc **kiểu Morse–Bott** với cấu trúc tắt dần theo hàm mũ tương thích.

Khi đó:

1. **Stack moduli log dẫn xuất trơn** đầy đủ là biểu diễn được:
   $$
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}} \in \mathrm{LogDSm}.
   $$
2. Ánh xạ so sánh sang không gian moduli **log tôpô** là một đẳng cấu:
   $$
   (\mathrm{LogDSm}\to\mathrm{LogTop})_*\,
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}}
   \;\simeq\;
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogTop}}.
   $$

![Slide ICM 2026: Log Derived Regularity]({{ site.baseurl }}/img/chapter_img/pardon_log_derived_regularity_icm2026.jpg)

*Hình. Slide trong bài giảng Fields 2026 của John Pardon (ICM 2026), lấy từ reel công khai. Slide ghi **in progress** (đang thực hiện).*

### Cách đọc trong khóa học

- Định lý này **không** thay thế nội dung trích dẫn của IMU (chu trình ảo, phạm trù Fukaya, tôpô đa tạp 3 chiều). Đây là công trình **đang thực hiện**, được trình bày trong bài giảng nhận giải.
- Chủ đề xuyên suốt: cả các công trình được trao giải lẫn định lý này đều nói về **không gian moduli của ánh xạ hoặc lát cắt** khi tính trơn và điều kiện hoành cổ điển không còn đúng. Ở đây bối cảnh là hình học **log** kết hợp với hình học **dẫn xuất**.
- Một số thuật ngữ:
  - **Log trơn / hình học log:** cách xử lý compact hóa và suy biến khi biên có cấu trúc kiểu giao cắt chuẩn tắc (normal crossings) được kiểm soát.
  - **Moduli dẫn xuất:** một stack ghi nhớ cả lý thuyết cản trở bậc cao, không chỉ là scheme hay orbifold cổ điển.
  - **Biểu diễn được trong LogDSm:** đối tượng moduli là một đối tượng hình học hợp lệ trong phạm trù log dẫn xuất trơn.
  - **So sánh với LogTop:** không gian moduli giải tích/tôpô trùng với mô tả dẫn xuất trơn, dưới các giả thiết về đầu mút.

### Ghi chú về độ chính xác của nguồn video

| Mục | Căn cứ |
|----------|------------|
| Sự kiện | Băng rôn sân khấu: ICM 2026 |
| Bối cảnh | Tiêu đề reel: 2026 Fields Medal Lecture — John Pardon |
| Trạng thái định lý | Slide ghi: **in progress** |
| Nguồn | Facebook reel `1666056391140628` (khoảng 24 giây) |
| Lời giảng | Không có phụ đề; nội dung được viết lại từ chữ trên slide |

---

## 6. Vì sao công trình này quan trọng

**Nền tảng cho tôpô symplectic.** Nếu không có chu trình ảo và một cách xây dựng phạm trù Fukaya đáng tin cậy, nhiều "định lý đếm" chỉ là phác thảo. Pardon được trao giải cho việc làm các công cụ này hoạt động được một cách chặt chẽ.

**Cầu nối giữa phạm trù và hình học.** Phạm trù Fukaya không chỉ là một phức xích hình thức. Nó chuyển thông tin hình học về đường cong thành ngôn ngữ của đối xứng gương và đại số đồng điều hiện đại.

**Bề rộng.** Các kết quả về tác động nhóm và lý thuyết nút cho thấy hình học chiều thấp cổ điển vẫn phát triển song song, và một nhà toán học có thể làm việc ở cả hai lĩnh vực.

**Bài học từ ICM.** Ngay trong bài giảng nhận giải Fields, Pardon vẫn đang phát triển **nền tảng cho không gian moduli** (tính chính quy log/dẫn xuất). Giải thưởng không kết thúc một hướng nghiên cứu, mà nhiều khi cho thấy những gì đang được làm.

**Giới hạn của bài.** Bài này không dạy đủ lý thuyết polyfold hay cấu trúc Kuranishi để bạn tự chứng minh các bổ đề về chu trình ảo. Bài chỉ giải thích *vì sao* các khái niệm đó xuất hiện và *cách* đọc lời trích dẫn hay slide mà không nói quá.

---

## Nhầm lẫn thường gặp

| Khẳng định | Kết luận | Sửa lại |
|------------|----------|-----|
| "Chu trình ảo chỉ là chi tiết kỹ thuật." | Sai | Đó là khác biệt giữa một số đếm không định nghĩa được và một định lý. |
| "Phạm trù Fukaya chỉ là một phức xích hình thức." | Sai | Nó ghi lại hình học của đường cong chỉnh hình dưới dạng một phạm trù $$A_\infty$$. |
| "Log Derived Regularity đã là định lý hoàn chỉnh được trao giải." | Sai | Slide ghi rõ **in progress** (đang thực hiện). |
| "Reel trên Facebook là toàn bộ bài giảng." | Sai | Đó là đoạn clip ngắn khoảng 24 giây, chỉ có một slide. |
| "Hình học symplectic chỉ là cơ học Hamilton cổ điển." | Sai | Cơ học là xuất phát điểm. Bất biến từ đường cong và phạm trù Fukaya là phần cấu trúc toàn cục. |
| "Mọi đa tạp con có một nửa số chiều đều là Lagrange." | Sai | Cần thêm điều kiện $$\omega\vert_L=0$$ (và thường cần thêm dữ liệu khác). |

---

## Nguồn video và tài liệu đọc

Chi tiết: `research/video-research/Pardon_Symplectic/`.

**Thứ tự xem gợi ý**

1. Bài của Quanta về giải Fields 2026: [link](https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/).  
2. Lời trích dẫn của IMU (PDF): [link](https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf).  
3. Reel ICM: [Facebook](https://www.facebook.com/reel/1666056391140628).

**Ghi nhớ:** Chu trình ảo là nền tảng để đếm đường cong khi điều kiện hoành không thỏa.

---

## Tài liệu tham khảo


Danh mục URL đầy đủ (gồm mọi link dùng khi tìm video): `research/video-research/Pardon_Symplectic/references.md`.

### Danh sách URL đầy đủ

1. https://www.facebook.com/reel/1666056391140628  
2. https://www.math.stonybrook.edu/~jpardon/  
3. https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/  
4. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026  
5. https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf  
6. https://news.stonybrook.edu/university/john-pardon-wins-2026-fields-medal-for-outstanding-mathematical-achievement/  
7. https://www.claymath.org/news/2026-fields-medals/  
8. https://www.princeton.edu/news/2026/07/23/princeton-alumni-awarded-three-four-2026-fields-medals-math  
9. https://en.wikipedia.org/wiki/John_Pardon  
10. https://arxiv.org/search/?query=Pardon+virtual+fundamental&searchtype=all  
11. https://en.wikipedia.org/wiki/Symplectic_geometry  
12. https://en.wikipedia.org/wiki/Fukaya_category  
13. https://scgp.stonybrook.edu/  

### Gói nghiên cứu

14. Gói khóa học: `research/video-research/Pardon_Symplectic/`.

1. IMU, Huy chương Fields 2026, John Pardon (trích dẫn chính thức).
2. Các bài báo chọn lọc của Pardon về chu trình ảo và tôpô symplectic.
3. Tài liệu nền: D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*; các bài tổng quan về Floer/Fukaya.
4. Thông cáo của trường và của Simons Center (2026).
5. **Video nguồn (reel ICM 2026):** [2026 Fields Medal Lecture: John Pardon](https://www.facebook.com/reel/1666056391140628). Slide về logarithmic derived regularity (truy cập 2026-08-03). Nội dung được viết lại từ hình ảnh; reel không có phụ đề chính thức.
6. Trong khóa học: [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Tìm hiểu **đối xứng gương** như một nơi dùng đến phạm trù Fukaya (ở mức ý tưởng: giả thuyết đối xứng gương đồng điều do Kontsevich đề xuất).
- So sánh các huy chương cho nền tảng (Pardon, Scholze) với các huy chương cho một giả thuyết dễ phát biểu (Perelman, Viazovska). Kiểu đóng góp khác nhau nhưng cùng một tiêu chuẩn của IMU.
- Học trước các thuật ngữ về **hình học log** và **stack dẫn xuất** trước khi đọc các bài báo nghiên cứu về không gian moduli.
- Nếu có video đầy đủ của bài giảng ICM, chia nó thành nhiều phần theo chủ đề (chu trình ảo; phạm trù Fukaya; đa tạp 3 chiều; log dẫn xuất).

## Video tham khảo

- **Xem trước** — [2026 Fields Medal: John Pardon](https://www.youtube.com/watch?v=E4KP07YL0Js) — Simons Foundation, tiếng Anh. Video giới thiệu ngắn về John Pardon và công trình được trao giải. Nên xem trước khi đọc bài.
- [ICM 2026 Fields Medal Award Lecture - John Pardon](https://www.youtube.com/watch?v=YZ7hKBlCeGs) — Simons Foundation, tiếng Anh. Bài giảng nhận giải tại ICM 2026, có phần về tính chính quy dẫn xuất loga ở mục 5. Nên xem sau khi đọc xong bài.
- [Contact homology and virtual fundamental cycles - John Pardon](https://www.youtube.com/watch?v=Eh8Hrg1mQVk) — Institute for Advanced Study, tiếng Anh. Bài giảng chuyên sâu của Pardon về đồng điều tiếp xúc và chu trình cơ bản ảo, liên quan trực tiếp đến mục 2. Dành cho người muốn đi sâu về kỹ thuật.
