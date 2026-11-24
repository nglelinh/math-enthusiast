---
layout: post
title: "Sinh học Toán học"
chapter: '06'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Vào năm 1952, khi tên tuổi đã gắn liền với máy tính và mật mã Enigma, Alan Turing bất ngờ công bố một bài báo chẳng liên quan gì đến máy tính: ông hỏi tại sao con báo có đốm, ngựa vằn có vằn, và một quả cầu tế bào đồng nhất ban đầu lại tự phân chia thành hình hài phức tạp của sinh vật sống. Ông viết xuống hai phương trình phản ứng–khuếch tán đơn giản — và thấy hoa văn tự hiện ra từ sự mất ổn định toán học.

Từ lâu, sinh học vẫn nổi tiếng là thế giới ồn ào, nhiều tầng thang đo và đầy ngoại lệ, trái ngược hẳn với vẻ sạch sẽ của vật lý. Thế nhưng hễ muốn trả lời một câu hỏi định lượng nghiêm túc — dịch bệnh sẽ đạt đỉnh vào tuần nào, một gen có thể bật/tắt ngẫu nhiên ra sao, hay loài ăn thịt và con mồi có cùng tồn tại nổi không — ta đều phải tìm đến toán học: tốc độ biến thiên, trạng thái cân bằng, hình học không gian, quá trình ngẫu nhiên và suy luận từ dữ liệu nhiễu. **Sinh học toán học** không phải là một định lý duy nhất; nó là nghệ thuật chọn đúng ngôn ngữ toán cho đúng thang đo của sự sống.

Điều khó nhất trong ngành này là sự **trung thực về thang đo**: một hệ phương trình vi phân đẹp có thể mô tả tốt một bể vi khuẩn khuấy đều nhưng hoàn toàn sai cho một khối mô rắn; một mạng lưới tương tác ở quy mô toàn bộ hệ gen trông rất ấn tượng về mặt đồ thị nhưng vẫn không đủ tham số để dự đoán điều gì sẽ xảy ra khi tế bào nhận thuốc. Bài này điểm qua những lớp mô hình cốt lõi của sinh học toán học và giúp bạn giữ đầu óc tỉnh táo trước làn sóng “AI đã giải xong sinh học”.

---

## Bản đồ kiến thức nền: Sinh học toán học là gì và nghiên cứu những gì?

Nếu vật lý cổ điển thường đi tìm *một* phương trình nền tảng đúng ở mọi nơi, thì **Sinh học Toán học** (Mathematical Biology) lại hoạt động giống như một xưởng chế tác bản đồ ở nhiều tỷ lệ khác nhau. Tùy vào câu hỏi sinh học bạn đang hỏi, ngôn ngữ toán học thay đổi hoàn toàn:

1. **Ở thang quần thể và dịch tễ (Phương trình vi phân thường — ODE):** Bỏ qua vị trí từng cá thể, ta theo dõi tổng số lượng (hoặc tỷ lệ) các nhóm theo thời gian: mô hình tăng trưởng logistic, thú ăn thịt–con mồi Lotka–Volterra, hay mô hình dịch bệnh SIR.
2. **Ở thang mô và hình thái học (Phương trình đạo hàm riêng — PDE):** Khi không gian đóng vai trò quyết định — tế bào di chuyển, hóa chất khuếch tán qua mô phôi — ta cần PDE phản ứng–khuếch tán để giải thích sóng lan truyền và sự hình thành mẫu (mẫu Turing).
3. **Ở thang bên trong tế bào (Quá trình ngẫu nhiên — Xích Markov & Phương trình Master):** Trong một tế bào đơn lẻ, có những loại phân tử mRNA chỉ tồn tại vài bản sao. Lúc này khái niệm "nồng độ liên tục" sụp đổ; từng phản ứng hóa học riêng lẻ là một cú tung xúc xắc ngẫu nhiên.
4. **Ở thang tiến hóa và hệ thống (Lý thuyết trò chơi & Đồ thị):** Chọn lọc tự nhiên không chỉ là bài toán tối ưu hóa tĩnh, mà là trò chơi nhiều bên nơi độ thích nghi của một chiến lược phụ thuộc vào việc *những cá thể khác đang chơi chiến lược gì*; còn mạng lưới gen và protein tạo nên các đồ thị phản hồi phức tạp.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Viết và diễn giải các mô hình ODE theo ngăn (logistic, SIR); nêu được giả thiết “trộn đều”.
- Mô tả động học phản ứng theo định luật tác dụng khối lượng dưới dạng $$\dot x=f(x)$$, và biết khi nào cần mô hình ngẫu nhiên.
- Nêu ý tưởng về **mẫu Turing** (mất ổn định do khuếch tán) mà không gán nó cho mọi mẫu trong sinh học.
- Giải thích vì sao nhiễu ở mức phân tử quan trọng trong điều hòa gene (quá trình sinh–tử và phương trình master).
- Phân biệt tính chất cấu trúc của mạng với việc dự đoán động lực học, vốn cần có tham số.
- Nhận xét một tuyên bố thổi phồng kiểu “mô hình dự đoán được sự sống” hay “AI đã giải xong sinh học”.

**Kiến thức nền.** ODE sơ cấp; xác suất cơ bản; ý niệm “tốc độ biến thiên”. Đại số tuyến tính giúp ích khi làm việc với hệ nhiều biến.

---

### Video ngắn: Dịch SIR với ba giá trị R₀

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sir-r0-epidemic_vi.mp4"></video>
</div>

Cùng một mô hình SIR với $$R_0 = 0.8, 1.5, 3$$, bắt đầu với 3% người nhiễm. Dưới 1 dịch tắt dần; trên 1 dịch tăng tới một đỉnh, và $$R_0$$ càng lớn thì đỉnh càng cao, càng sớm và tổng số người nhiễm càng nhiều.


### Tự tay thử: Đổi R₀ và xem dịch bệnh

<div class="mex-explainer" data-mex="sir" data-lang="vi"></div>

## 1. Quần thể và các ngăn: mô hình ODE

Mô hình logistic:

$$
\frac{dN}{dt}=rN\Bigl(1-\frac{N}{K}\Bigr).
$$

mô tả tăng trưởng bị giới hạn bởi sức chứa $$K$$: khi $$N \ll K$$, quần thể tăng gần như theo hàm mũ với tốc độ $$r$$; khi $$N$$ tiến gần $$K$$, nguồn lực cạn dần khiến tốc độ tăng chậm lại và dừng ở $$K$$. Mô hình **SIR** chia quần thể thành ba nhóm: nhạy cảm (susceptible), nhiễm (infected), hồi phục (recovered), với lây nhiễm theo định luật tác dụng khối lượng (tỷ lệ gặp gỡ giữa người nhạy cảm và người nhiễm tỉ lệ với tích $$SI$$):

$$
\dot S=-\beta SI,\quad
\dot I=\beta SI-\gamma I,\quad
\dot R=\gamma I.
$$

$$R_0$$ xuất hiện khi tuyến tính hóa tại điểm cân bằng không có bệnh: nếu $$R_0>1$$ thì dịch có thể xâm nhập, trong mô hình đã được lý tưởng hóa. Hãy thử một con số cụ thể để có cảm giác: nếu trung bình một người nhiễm mất 5 ngày để hồi phục ($$\gamma = 0.2$$ mỗi ngày) và tốc độ lây $$\beta = 0.6$$ mỗi ngày, thì $$R_0 = \beta/\gamma = 3$$. Khi quần thể ban đầu gần như hoàn toàn nhạy cảm ($$S \approx 1$$), số ca nhiễm tăng vọt cho tới khi tỷ lệ người chưa miễn dịch tụt xuống dưới ngưỡng $$S = 1/R_0 = 1/3$$ — lúc đó $$\dot I = 0$$ và dịch đạt đỉnh!

**Phần là định lý:** tiêu chí ổn định địa phương cho điểm cân bằng của ODE trơn; các định lý ngưỡng trong mô hình dịch có cấu trúc với giả thiết nêu rõ. **Phần là phán đoán khi xây mô hình:** chọn các ngăn, cấu trúc tiếp xúc, tham số thay đổi theo thời gian, phản ứng hành vi của con người. Truyền thông về dịch bệnh (thời COVID) dễ trộn các lớp này với nhau. Người đọc cần tách hệ quả toán học của mô hình khỏi việc khớp số liệu và khỏi chính sách.

---

## 2. Mạng sinh hóa: ma trận hợp thức

Với nồng độ $$x\in\mathbb{R}^n_{\ge 0}$$ và ma trận hợp thức (stoichiometry) $$\Gamma$$:

$$
\dot x=\Gamma\, v(x),
$$

trong đó $$v(x)$$ là tốc độ phản ứng (đa thức theo định luật tác dụng khối lượng, Michaelis–Menten, Hill, …). Trực giác của ma trận $$\Gamma$$ rất gọn: mỗi cột là một phản ứng hóa học, ghi rõ phản ứng đó tiêu thụ bao nhiêu phân tử chất nào (số âm) và sinh ra bao nhiêu phân tử chất nào (số dương). Lý thuyết mạng phản ứng hóa học (CRNT, lý thuyết deficiency) cho những kết quả cấu trúc về sự tồn tại và duy nhất của điểm cân bằng dương, hoặc về việc không có nhiều trạng thái dừng, với một số lớp mạng. Những kết quả này đọc được một phần từ đồ thị của mạng, không phụ thuộc vào hằng số tốc độ.

Sinh học hệ thống xây dựng những mạng lớn (chuyển hóa, truyền tín hiệu). Các định luật bảo toàn và elementary flux mode là phần toán; còn dự đoán bằng số cần tham số, mà nhiều tham số lại ít được biết. Tính xác định được của tham số (identifiability) và hiện tượng “sloppiness” của mô hình nhiều tham số là vùng biên giao nhau giữa đại số, thống kê và thiết kế thí nghiệm.

---

## 3. Không gian: PDE và mẫu Turing

Khi nồng độ phụ thuộc vào vị trí, ta có phương trình phản ứng–khuếch tán:

$$
\partial_t u=D\Delta u+f(u),
$$

với ma trận khuếch tán $$D$$ và động học cục bộ $$f$$. **Turing** (1952) chỉ ra rằng khuếch tán, vốn thường được nghĩ là làm mịn (như giọt mực loang đều trong cốc nước), lại có thể **làm mất ổn định** trạng thái cân bằng đồng nhất và tạo ra mẫu không gian, nếu động học có dạng activator–inhibitor. Hãy hình dung một đám cháy nhỏ trên đồng cỏ khô: lửa là chất *kích hoạt* (activator) tự lan chậm ở cục bộ, còn đội cứu hỏa cơ động bằng xe là chất *ức chế* (inhibitor) do lửa gọi tới nhưng di chuyển nhanh hơn nhiều. Đội cứu hỏa chạy ra xa dập tắt các vùng lân cận, để lại những đốm lửa cách đều nhau — chính sự chênh lệch tốc độ khuếch tán giữa chất kích hoạt chậm và chất ức chế nhanh đã tạc nên đốm và vằn! Tuy nhiên, đây là một cơ chế dựa trên ổn định tuyến tính; nó không phải lời giải chung cho vằn ngựa vằn, phôi thai hay hình dạng đô thị.

Sinh thái học không gian, gradient morphogen và biofilm đều thuộc về vùng này. Điều kiện biên, miền đang tăng trưởng và mô hình không gian ngẫu nhiên (dựa trên từng cá thể) đều có thể làm đổi kết luận. Lý thuyết PDE (tồn tại, tính chính quy, hành vi dài hạn) cho ta định lý; còn khớp chúng với phôi thật mới cho ta khoa học.

---

## 4. Ngẫu nhiên: khi số phân tử ít

Trong tế bào, có những loài chỉ có vài chục bản sao — thậm chí chỉ có 1 hoặc 2 bản sao của một gen. Khi đó ODE liên tục có thể đánh lừa ta: nghiệm trung bình nói rằng nồng độ vẫn dương nhẹ, trong khi thực tế một quỹ đạo ngẫu nhiên có thể chạm đúng số 0 và tuyệt chủng hẳn. **Phương trình master hóa học** mô tả sự tiến hóa của $$P(n,t)$$, xác suất có $$n$$ bản sao; thuật toán Gillespie lấy mẫu các quỹ đạo. Biểu hiện gene theo kiểu “bùng nổ” (gen thỉnh thoảng mở ra sản xuất liền một mẻ lớn mRNA rồi lại đóng im lìm) tạo phân bố mRNA và protein có phương sai lớn hơn phân bố Poisson. Nhiễu có thể là một tính năng (chiến lược phòng hờ rủi ro giúp một nhóm nhỏ vi khuẩn sống sót trước kháng sinh) hoặc một lỗi (làm hệ dễ vỡ).

Về toán, đây là xích Markov thời gian liên tục trên không gian đếm được, cùng với đóng moment, các lập luận heuristic về độ lệch lớn, và mô hình lai ghép giữa công tắc rời rạc với nồng độ liên tục. **Định lý và xấp xỉ:** nghiệm chính xác của phương trình master hiếm khi có được; các xấp xỉ khuếch tán (Fokker–Planck, Langevin) kiểm soát được trong một số chế độ tỷ lệ, còn ở chế độ khác thì chỉ là kinh nghiệm.

---

## 5. Tiến hóa và trò chơi

Di truyền quần thể và lý thuyết trò chơi tiến hóa thay việc tối ưu thuần túy bằng **động lực replicator** và sự cố định ngẫu nhiên trong quần thể hữu hạn:

$$
\dot x_i=x_i\bigl((Ax)_i-x^\top Ax\bigr)
$$

với $$x$$ là tần số các chiến lược và $$A$$ là ma trận lợi ích. Đọc phương trình này bằng lời rất tự nhiên: chiến lược thứ $$i$$ tăng tỷ lệ trong quần thể đúng khi lợi ích kỳ vọng của nó $$(Ax)_i$$ cao hơn mức trung bình toàn quần thể $$x^\top Ax$$. Chẳng hạn, trong trò chơi Kéo–Búa–Bao của ba chủng vi khuẩn *E. coli* (chủng tiết độc tố, chủng kháng độc tố, chủng nhạy cảm), không chiến lược nào thống trị tuyệt đối mà ba quần thể rượt đuổi nhau theo chu kỳ.

Cảnh quan thích nghi (fitness landscape), động lực thích nghi, các mô hình đa locus nối hệ động lực với xác suất. Dữ liệu genome còn thêm vào suy luận thống kê: phát sinh loài (cây cùng mô hình Markov về thay thế), kiểm định chọn lọc, lịch sử nhân khẩu. Mỗi lớp đều có hàm hợp lý và nguy cơ chọn sai mô hình.

---

## 6. Mạng sinh học như đồ thị, và giới hạn của cách nhìn đó

Tương tác giữa các protein, điều hòa gene, connectome đều là **đồ thị** (hoặc siêu đồ thị, mạng đa lớp). Bậc của đỉnh, motif, các heuristic về khả năng điều khiển, cộng đồng là những công cụ của lý thuyết đồ thị (xem bài khoa học mạng). Nói “hub là quan trọng” mà không có động lực học hay thí nghiệm nhân quả đi kèm là một kiểu khẳng định quá đà kinh điển.

Các cạnh trong mạng sinh học thường nhiễu, thiếu và phụ thuộc ngữ cảnh (mô nào, thời điểm nào, trạng thái biến đổi sau dịch mã). Đối tượng toán học thích hợp thường là mô hình đồ thị ngẫu nhiên hoặc hệ động lực chỉ quan sát được một phần, chứ không phải sơ đồ đi dây hoàn hảo của sự sống.

---

## 7. Dữ liệu, suy luận và làn sóng AI

| Lớp | Nội dung |
|-----|----------|
| Mô hình đo đạc | Nhiễu, thiên lệch, hiệu ứng theo lô |
| Ước lượng thống kê | Cái gì xác định được từ dữ liệu? |
| Mô hình cơ chế | ODE, PDE, mô hình ngẫu nhiên |
| Mô hình thay thế bằng ML | Khớp linh hoạt; có thể thiếu cơ chế |
| Khẳng định sinh học | Quan hệ nhân quả, chức năng |

RNA-seq đơn bào, cryo-EM, dự đoán cấu trúc protein bằng học sâu đã thay đổi thực hành. Dự đoán được cấu trúc protein là thành tựu lớn (hình học protein, tối ưu, học biểu diễn), nhưng không tự động cho ta hiểu đầy đủ động lực học của một con đường tín hiệu, của quá trình phát triển hay của một hệ sinh thái. Lời thổi phồng gộp các dòng trong bảng lại; người đọc tỉnh táo giữ chúng tách riêng.

---

## 8. Một số hướng tiên phong

1. Ghép nhiều thang (phân tử → tế bào → mô → cơ thể) với sai số kiểm soát được.  
2. Tính xác định được của tham số và thiết kế thí nghiệm cho hệ động lực phi tuyến.  
3. Mô hình không gian ngẫu nhiên và giới hạn liên tục chặt chẽ.  
4. Giải tích dữ liệu tô-pô (TDA) và hình học dữ liệu trên hình dạng sinh học: công cụ đầy hứa hẹn, nhưng không phải phép màu.  
5. Điều khiển các mạch gene tổng hợp có phản hồi và nhiễu.  
6. Kết hợp cơ chế với ML khi phân phối dữ liệu dịch chuyển.

### Ví dụ $$R_0$$ như một bài đại số tuyến tính

Gần $$I=0$$ trong mô hình SIR chuẩn hóa ($$S=1$$, chưa có bệnh), ta có $$\dot I\approx(\beta-\gamma)I$$: dịch xâm nhập khi $$R_0=\beta/\gamma>1$$. Với mô hình nhiều nhóm, $$R_0$$ là bán kính phổ của ma trận thế hệ kế tiếp. Đó là một đối tượng toán học sinh ra từ mô hình tường minh, chứ không phải một “con số lây nhiễm” lơ lửng ngoài các giả thiết về trộn đều, mức nhạy cảm và hồi phục.

Với bảng theo dõi $$R_t$$, cần hỏi: khoảng cách giữa các thế hệ là bao lâu, báo cáo trễ bao nhiêu, cấu trúc tiếp xúc ra sao? Ký hiệu này đã đi từ lý thuyết tuyến tính hóa sang dịch tễ học vận hành; cả hai cách dùng đều ổn nếu được ghi rõ.

### Thói quen: không thứ nguyên hóa

Trước khi tin một mô phỏng, hãy không thứ nguyên hóa. Mô hình logistic có thang thời gian $$1/r$$ và thang kích thước $$K$$. Mô hình phản ứng–khuếch tán có thang độ dài $$\sqrt{D/\text{rate}}$$. Các nhóm không thứ nguyên cho biết phản ứng hay khuếch tán chiếm ưu thế, và giúp tránh những lỗi đơn vị trông như “hiện tượng sinh học mới”.

### Hoạt động nhóm

Chọn một phần tóm tắt bài báo kiểu “AI cho khám phá thuốc” hoặc “bản sao số của tế bào”. Điền bảng năm lớp ở Mục 7. Câu nào là số đo, câu nào là mô hình thay thế, câu nào là khẳng định về chức năng cần thêm thí nghiệm? Viết một đoạn ngắn: khẳng định nào có thể trích dẫn trong seminar, khẳng định nào cần ghi chú “chưa kiểm chứng nhân quả”.

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|-----------|
| “Mô hình chính là sinh học.” | Mô hình là một giả thuyết; cần kiểm chứng. |
| “Turing giải thích mọi quá trình tạo hình.” | Đó chỉ là một cơ chế trong nhiều cơ chế. |
| “Mạng phi tỷ lệ (scale-free) chứng tỏ tối ưu do tiến hóa.” | Phân bố bậc hiếm khi đủ để kết luận. |
| “Nhiều phương trình hơn nghĩa là gần chân lý hơn.” | Dễ bị khớp quá mức với tham số. |
| “AI đã giải xong sinh học.” | Quảng cáo; thành công ở một nhiệm vụ không phải một lý thuyết đầy đủ về sự sống. |
| “Ngẫu nhiên chỉ cần khi ODE khó giải số.” | Nhiễu rời rạc làm đổi tính chất định tính (tuyệt chủng, chuyển trạng thái). |

---

## Bài tập

1. Phác thảo đồ thị $$N(t)$$ của mô hình logistic; diễn giải ý nghĩa của $$r,K$$.
2. Tuyến tính hóa SIR tại $$(1,0,0)$$ (đã chuẩn hóa); liên hệ điều kiện xâm nhập với $$R_0=\beta/\gamma$$.
3. Với phản ứng $$A+B\to C$$ theo định luật tác dụng khối lượng, viết phần đóng góp vào ODE cho $$\dot a,\dot b,\dot c$$.
4. Vì sao các đợt bùng nổ tạo protein có thể có phương sai lớn hơn phân bố Poisson?
5. Cho một ví dụ cho thấy đỉnh có bậc cao không có nghĩa là quan trọng về chức năng.
6. Với phần tóm tắt một bài dự đoán cấu trúc protein: đâu là số đo, đâu là phương pháp, đâu là khẳng định sinh học còn cần kiểm chứng?
7. Không thứ nguyên hóa mô hình logistic hoặc SIR; nêu các nhóm không thứ nguyên.

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**Một lĩnh vực ứng dụng rộng.** Các mô hình quần thể bằng ODE và PDE là cổ điển; động học hóa học ngẫu nhiên, sự hình thành mẫu trong không gian và suy luận dựa trên dữ liệu vẫn đang được nghiên cứu sôi nổi.

### Phát biểu cốt lõi

Các mô hình ngăn kiểu SIR: $$\dot S=-\beta SI$$, $$\dot I=\beta SI-\gamma I$$, $$\dot R=\gamma I$$. Ngưỡng $$R_0=\beta/\gamma$$ quyết định việc dịch có xâm nhập được hay không. Sự hình thành mẫu qua mất ổn định Turing là một cơ chế PDE cổ điển.

### Định nghĩa cần nhớ

- **$$R_0$$.** Số ca thứ cấp kỳ vọng do một người nhiễm gây ra trong một quần thể hoàn toàn nhạy cảm.
- **Lây nhiễm theo tác dụng khối lượng.** Số hạng lây nhiễm $$\beta SI$$ trong ODE của quần thể trộn đều.

### Cần phân biệt rõ

- Coi dự báo từ ODE là dự đoán chính xác, mà bỏ qua bất định về tham số và về cấu trúc mô hình.
- Bỏ qua khả năng tuyệt chủng ngẫu nhiên trong quần thể nhỏ.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Định hướng**: 3Blue1Brown, Exponential growth and epidemics (mô hình dịch bệnh, thuộc loạt về phương trình vi phân): [https://www.youtube.com/watch?v=Kas0tIxDvrg](https://www.youtube.com/watch?v=Kas0tIxDvrg).  
2. **Nền tảng**: 3Blue1Brown, danh sách phát về phương trình vi phân: [https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs](https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs).  
3. **Định hướng**: Dr. Trefor Bazett, The MATH of Pandemics | Intro to the SIR Model: [https://www.youtube.com/watch?v=Qrp40ck3WpI](https://www.youtube.com/watch?v=Qrp40ck3WpI).  
4. **Định hướng**: Numberphile, The Coronavirus Curve (SIR): [https://www.youtube.com/watch?v=k6nLfCbAzgo](https://www.youtube.com/watch?v=k6nLfCbAzgo).  

**Lưu ý về hiện trạng:** đây là một lĩnh vực ứng dụng rộng. Các mô hình quần thể bằng ODE và PDE là cổ điển; động học hóa học ngẫu nhiên, hình thành mẫu trong không gian và suy luận từ dữ liệu vẫn đang phát triển.

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/mathematical-biology_Kas0tIxDvrg_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Murray — *Mathematical Biology*.
2. Edelstein-Keshet — *Mathematical Models in Biology*.
3. Feinberg — CRNT; van Kampen — phương trình master.
4. Turing (1952) — The chemical basis of morphogenesis.
5. [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) (để so sánh phân phối dữ liệu).

---

### Video (lộ trình gợi ý)

- 3Blue1Brown, Exponential growth and epidemics (định hướng): https://www.youtube.com/watch?v=Kas0tIxDvrg
- 3Blue1Brown, danh sách phát về phương trình vi phân (nền tảng): https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs
- Dr. Trefor Bazett, The MATH of Pandemics | Intro to the SIR Model (định hướng): https://www.youtube.com/watch?v=Qrp40ck3WpI

### Bài báo và web

- Wikipedia — Mathematical biology: https://en.wikipedia.org/wiki/Mathematical_and_theoretical_biology
- Wikipedia — Compartmental models in epidemiology: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
- Murray — Mathematical Biology (standard textbook reference): https://en.wikipedia.org/wiki/James_D._Murray
- Wikipedia — Reaction–diffusion system / Turing pattern: https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system
- Wikipedia — Lotka–Volterra equations: https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
- Wikipedia — Chemical master equation: https://en.wikipedia.org/wiki/Chemical_master_equation

## Hướng đi tiếp

- [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/) cho đồ thị ngẫu nhiên và dịch lan trên mạng.
- [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) khi khẳng định mang tính thống kê.
- Mô phỏng SIR và quá trình sinh–tử của gene; so ODE trung bình với các quỹ đạo ngẫu nhiên.
- Đọc: một chương về mô hình theo ngăn, một bài báo về gene ngẫu nhiên và một bài luận về giới hạn của mô hình.
- Luôn hỏi: *phương trình này hợp lệ ở thang đo nào?*

## Video tham khảo

- **Xem trước** — [Exponential growth and epidemics](https://www.youtube.com/watch?v=Kas0tIxDvrg) — 3Blue1Brown, tiếng Anh. Xem trước để hiểu vì sao dịch bệnh tăng theo hàm mũ và mô hình ngăn hình thành thế nào.
- [The MATH of Pandemics | Intro to the SIR Model](https://www.youtube.com/watch?v=Qrp40ck3WpI) — Dr. Trefor Bazett, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để theo dõi mô hình SIR từng bước.
- [The Coronavirus Curve - Numberphile](https://www.youtube.com/watch?v=k6nLfCbAzgo) — Numberphile, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, về đường cong dịch và việc làm phẳng nó.
