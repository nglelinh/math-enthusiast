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

Sinh học ồn ào, đa thang, từng mang tính mô tả—song mọi khẳng định định lượng thành công cuối cùng thành toán: tốc độ, cân bằng, hình học, quá trình ngẫu nhiên, suy diễn từ dữ liệu thiếu. **Sinh học toán** không phải một định lý; nó là họ ngôn ngữ mô hình hóa biến hệ sống thành đối tượng phân tích, mô phỏng, đôi khi điều khiển. Biên giới là trung thực về thang: ODE đẹp có thể đúng cho bể trộn đều và sai cho mô; mạng quy mô genome có thể thú vị cấu trúc mà vẫn underdetermined bởi đo.

Bài map các lớp mô hình cốt lõi—động lực quần thể, kinetics phản ứng, hình thành mẫu không gian, biểu hiện gene ngẫu nhiên, trò chơi tiến hóa, mạng sinh học—và luyện tách định lý / heuristic / hype trong thời “AI for biology”.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết và diễn giải ODE ngăn (logistic, SIR); nêu giả thiết “trộn đều”.
- Mô tả động học phản ứng mass-action như $$\dot x=f(x)$$; khi nào cần mô hình ngẫu nhiên.
- Nêu ý **mẫu Turing** (bất ổn định do khuếch tán) mà không gán cho mọi mẫu sinh học.
- Giải thích vì sao nhiễu phân tử quan trọng trong điều hòa gene (birth–death / master equation).
- Phân biệt thuộc tính mạng cấu trúc và dự đoán động lực cần tham số.
- Phê một tuyên bố thổi về “mô hình dự đoán sự sống” hoặc “AI giải sinh học” (**LO6**).

**Kiến thức nền.** ODE sơ cấp; xác suất cơ bản; ngôn ngữ “tốc độ biến thiên”. Đại số tuyến tính giúp hệ nhiều biến.

---

## 1. Quần thể và ngăn: ODE

Logistic:

$$
\frac{dN}{dt}=rN\Bigl(1-\frac{N}{K}\Bigr).
$$

mô hình tăng trưởng bị giới hạn bởi sức chứa $$K$$. **SIR** phân hoạch quần thể thành susceptible, infected, recovered với nhiễm mass-action:

$$
\dot S=-\beta SI,\quad
\dot I=\beta SI-\gamma I,\quad
\dot R=\gamma I.
$$

$$R_0$$ xuất hiện từ tuyến tính hóa tại cân bằng không bệnh: nếu $$R_0>1$$ thì xâm nhập khả dĩ trong mô hình lý tưởng hóa.

**Hình định lý:** tiêu chí ổn định địa phương cho cân bằng ODE trơn; định lý ngưỡng trong mô hình dịch có cấu trúc dưới giả thiết tường minh. **Phán đoán mô hình:** chọn ngăn, cấu trúc tiếp xúc, tham số biến thiên theo thời gian, phản hồi hành vi. Truyền thông dịch bệnh (thời COVID) dễ trộn các lớp này; biết đọc tách hệ quả toán của mô hình khỏi fit thực nghiệm và chính sách.

---

## 2. Mạng sinh hóa: stoichiometry

Với nồng độ $$x\in\mathbb{R}^n_{\ge 0}$$ và ma trận stoichiometry $$\Gamma$$:

$$
\dot x=\Gamma\, v(x),
$$

trong đó $$v(x)$$ là tốc độ phản ứng (đa thức mass-action, Michaelis–Menten, Hill…). Lý thuyết mạng phản ứng hóa học (CRNT, deficiency theory) cho kết quả cấu trúc về tồn tại/duy nhất cân bằng dương, hoặc vắng multistationarity, ở một số lớp mạng—đọc được một phần từ đồ thị mạng, độc lập hằng số tốc độ.

Systems biology xây mạng lớn (chuyển hóa, tín hiệu): luật bảo toàn, elementary flux mode là toán; dự đoán số cần tham số—nhiều tham số kém biết. Identifiability và “sloppiness” của mô hình nhiều tham số là biên giới giao đại số, thống kê và thiết kế thí nghiệm.

---

## 3. Không gian: PDE và mẫu Turing

Khi nồng độ phụ thuộc không gian, xuất hiện reaction–diffusion:

$$
\partial_t u=D\Delta u+f(u),
$$

với ma trận khuếch tán $$D$$ và kinetics địa phương $$f$$. **Turing** (1952): khuếch tán—thường nghĩ là làm mượt—có thể **bất ổn định** cân bằng đồng nhất và tạo mẫu không gian dưới kinetics kiểu activator–inhibitor. Đây là cơ chế ổn định tuyến tính—không phải lời giải phổ quát cho sọc ngựa vằn, phôi hay đô thị.

Sinh thái không gian, gradient morphogen, biofilm sống ở đây. Điều kiện biên, miền tăng trưởng, mô hình không gian ngẫu nhiên (individual-based) đổi kết luận. Lý thuyết PDE (tồn tại, chính quy, hành vi dài hạn) cung cấp định lý; khớp chúng với phôi cung cấp khoa học.

---

## 4. Ngẫu nhiên: khi phân tử ít

Trong tế bào, một số loài chỉ vài chục bản sao. ODE liên tục có thể đánh lừa. **Phương trình master hóa học** tiến hóa $$P(n,t)$$ của số bản sao; thuật toán Gillespie lấy mẫu quỹ đạo. Biểu hiện gene “bùng nổ” tạo phân bố mRNA/protein overdispersed; nhiễu có thể là feature (bet-hedging) hoặc bug (dễ vỡ).

Toán: xích Markov thời gian liên tục trên không gian đếm được, đóng moment, large-deviation heuristic, mô hình hybrid ghép switch rời rạc với nồng độ liên tục. **Định lý vs xấp xỉ:** nghiệm CME exact hiếm; xấp xỉ khuếch tán (Fokker–Planck, Langevin) kiểm soát được theo một số scaling, và chỉ folklore ở chỗ khác.

---

## 5. Tiến hóa và trò chơi

Di truyền quần thể và evolutionary game theory thay thuần tối ưu bằng **replicator dynamics** và fixation ngẫu nhiên trong quần thể hữu hạn:

$$
\dot x_i=x_i\bigl((Ax)_i-x^\top Ax\bigr)
$$

với tần số chiến lược $$x$$ và ma trận payoff $$A$$. Fitness landscape, adaptive dynamics, mô hình đa locus nối hệ động lực và xác suất. Dữ liệu genome thêm suy diễn thống kê: phylogenetics (cây + mô hình Markov thay thế), kiểm định chọn lọc, lịch sử nhân khẩu—mỗi lớp có likelihood và nguy cơ misspecification.

---

## 6. Mạng sinh học như đồ thị—và giới hạn

Tương tác protein, điều hòa gene, connectome là **đồ thị** (hoặc hypergraph, mạng multiplex). Bậc, motif, heuristic controllability, cộng đồng là công cụ đồ thị (xem khoa học mạng). Gán “hub = quan trọng” không có động lực/thí nghiệm nhân quả là overclaim kinh điển.

Cạnh sinh học ồn, thiếu, phụ thuộc ngữ cảnh (mô, thời gian, trạng thái post-translational). Đối tượng toán thường là mô hình đồ thị ngẫu nhiên hoặc hệ động lực quan sát từng phần—không phải sơ đồ wiring hoàn hảo của sự sống.

---

## 7. Dữ liệu, suy diễn và sóng AI

| Lớp | Nội dung |
|-----|----------|
| Mô hình đo | Nhiễu, bias, batch effect |
| Ước lượng thống kê | Cái gì identifiable từ dữ liệu? |
| Mô hình cơ chế | ODE/PDE/ngẫu nhiên |
| Surrogate ML | Khớp linh hoạt; có thể thiếu cơ chế |
| Khẳng định sinh học | Nhân quả / chức năng |

Single-cell RNA-seq, cryo-EM, dự đoán cấu trúc protein bằng học sâu đổi thực hành. Thành công dự đoán cấu trúc là thành tựu lớn (hình học protein, tối ưu, representation learning)—không tự động cho hiểu động lực đầy đủ của pathway, phát triển hay hệ sinh thái. Hype gộp các hàng; biết đọc giữ chúng tách.

---

## 8. Tiên phong chọn lọc

1. Ghép đa thang (phân tử → tế bào → mô → cơ thể) với lỗi kiểm soát được.  
2. Identifiability và experimental design cho hệ động lực phi tuyến.  
3. Mô hình không gian ngẫu nhiên và giới hạn continuum chặt.  
4. TDA / hình học dữ liệu trên hình dạng sinh học—công cụ hứa hẹn, không phép màu.  
5. Điều khiển mạch gene tổng hợp có feedback và nhiễu.  
6. Ghép cơ chế + ML dưới dịch phân phối.

### Ví dụ $$R_0$$ như đại số tuyến tính

Gần $$I=0$$ trong SIR chuẩn hóa ($$S=1$$ free-disease), $$\dot I\approx(\beta-\gamma)I$$: xâm nhập khi $$R_0=\beta/\gamma>1$$. Mô hình nhiều nhóm: $$R_0$$ là bán kính phổ của ma trận thế hệ sau—đối tượng toán từ mô hình tường minh, không phải “số lây” bay lơ lửng ngoài giả thiết trộn/nhạy cảm/hồi phục.

Dashboard $$R_t$$ cần hỏi: khoảng thế hệ, trễ báo cáo, cấu trúc tiếp xúc? Ký hiệu di cư từ lý thuyết tuyến tính hóa sang dịch tễ vận hành; cả hai dùng được nếu gắn nhãn.

### Thói quen không thứ nguyên

Trước khi tin simulation, không thứ nguyên hóa. Logistic có thời gian $$1/r$$ và kích thước $$K$$. Reaction–diffusion có độ dài $$\sqrt{D/\text{rate}}$$. Nhóm không thứ nguyên cho biết chế độ phản ứng hay khuếch tán thống trị—và tránh lỗi đơn vị trông như “sinh học mới”.

### Studio seminar

Chọn một abstract “AI for drug discovery” hoặc “digital twin of the cell”. Điền bảng năm lớp Mục 7. Câu nào là đo, câu nào là surrogate, câu nào là khẳng định chức năng còn cần thí nghiệm? Viết một đoạn LO6: claim nào được phép trích dẫn ở seminar, claim nào cần gắn “chưa kiểm chứng nhân quả”.

---

## Nhầm lẫn thường gặp

| Tuyên bố | Sửa |
|----------|-----|
| “Mô hình = sinh học.” | Mô hình là giả thuyết; cần kiểm chứng. |
| “Turing giải thích mọi morphogenesis.” | Một cơ chế trong nhiều. |
| “Scale-free chứng minh tối ưu tiến hóa.” | Thống kê bậc hiếm khi đủ. |
| “Nhiều phương trình = nhiều chân lý.” | Overfit tham số. |
| “AI đã giải sinh học.” | Hype; task success ≠ lý thuyết sống đầy đủ. |
| “Ngẫu nhiên chỉ khi ODE khó số.” | Nhiễu rời rạc đổi định tính (tuyệt chủng, chuyển trạng thái). |

---

## Bài tập

1. Phác thảo $$N(t)$$ logistic; diễn giải $$r,K$$.
2. Tuyến tính hóa SIR tại $$(1,0,0)$$ (chuẩn hóa); liên hệ xâm nhập với $$R_0=\beta/\gamma$$.
3. Mass-action cho $$A+B\to C$$: đóng góp ODE cho $$\dot a,\dot b,\dot c$$.
4. Vì sao burst protein có thể overdispersed so với Poisson?
5. Ví dụ bậc cao không hàm ý quan trọng chức năng.
6. Abstract dự đoán cấu trúc protein: đo / phương pháp / khẳng định sinh học còn cần kiểm.
7. Không thứ nguyên hóa logistic hoặc SIR; nêu nhóm không thứ nguyên.

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/mathematical-biology/analysis.md`.

### Trạng thái

**Broad applied field.** ODE/PDE population models are classical; stochastic chemical kinetics, spatial pattern formation, and data-driven inference remain active.

### Phát biểu / slogan cốt lõi

SIR-type compartment models: $$\dot S=-\beta SI$$, $$\dot I=\beta SI-\gamma I$$, $$\dot R=\gamma I$$. Threshold $$R_0=\beta/\gamma$$ governs invasion. Pattern formation via Turing instability is a classical PDE mechanism.

### Định nghĩa cần cố định

- **$$R_0$$.** Expected secondary cases from one infectious in a fully susceptible population.
- **Mass-action incidence.** Infection term $$\beta SI$$ in well-mixed ODEs.

### Vệ sinh khái niệm

- Treating ODE forecasts as exact predictions without parameter/structural uncertainty.
- Ignoring stochastic extinction in small populations.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/mathematical-biology/`.

**Thứ tự gợi ý**

1. **Định hướng** — 3Blue1Brown — Epidemic modeling / differential equations (related DE series): [https://www.youtube.com/watch?v=Kas0tIxDvrg](https://www.youtube.com/watch?v=Kas0tIxDvrg).  
2. **Nền tảng** — 3Blue1Brown — Differential equations playlist entry points: [https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs](https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs).  
3. **Định hướng** — Dr. Trefor Bazett — The MATH of Pandemics | Intro to the SIR Model: [https://www.youtube.com/watch?v=Qrp40ck3WpI](https://www.youtube.com/watch?v=Qrp40ck3WpI).  
4. **Orientation** — Numberphile — The Coronavirus Curve (SIR): [https://www.youtube.com/watch?v=k6nLfCbAzgo](https://www.youtube.com/watch?v=k6nLfCbAzgo).  

**Nhắc trạng thái:** **Broad applied field.** ODE/PDE population models are classical; stochastic chemical kinetics, spatial pattern formation, and data-driven inference remain active.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/mathematical-biology/transcripts/` · trạng thái: `research/video-research/mathematical-biology/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/mathematical-biology_Kas0tIxDvrg_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo

1. Murray — *Mathematical Biology*.
2. Edelstein-Keshet — *Mathematical Models in Biology*.
3. Feinberg — CRNT; van Kampen — master equation.
4. Turing (1952) — The chemical basis of morphogenesis.
5. [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) (so phân phối dữ liệu).

---


Danh mục URL đầy đủ: `research/video-research/mathematical-biology/references.md`.

### Video (lộ trình gợi ý)

- 3Blue1Brown — Epidemic modeling / differential equations (related DE series) (ORIENTATION): https://www.youtube.com/watch?v=Kas0tIxDvrg
- 3Blue1Brown — Differential equations playlist entry points (FOUNDATION): https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs
- Dr. Trefor Bazett — The MATH of Pandemics | Intro to the SIR Model (ORIENTATION): https://www.youtube.com/watch?v=Qrp40ck3WpI

### Bài báo và web (từ gói nghiên cứu)

- Wikipedia — Mathematical biology: https://en.wikipedia.org/wiki/Mathematical_and_theoretical_biology
- Wikipedia — Compartmental models in epidemiology: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
- Murray — Mathematical Biology (standard textbook reference): https://en.wikipedia.org/wiki/James_D._Murray
- Wikipedia — Reaction–diffusion system / Turing pattern: https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system
- Wikipedia — Lotka–Volterra equations: https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
- Wikipedia — Chemical master equation: https://en.wikipedia.org/wiki/Chemical_master_equation

### Khóa học

- Gói: `research/video-research/mathematical-biology/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- [Khoa học mạng]({{ site.baseurl }}/contents/vi/chapter06/06_05_Network_Science/) cho mô hình đồ thị ngẫu nhiên và dịch trên mạng.
- [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) khi khẳng định mang tính thống kê.
- Mô phỏng SIR và birth–death gene; so ODE trung bình với quỹ đạo ngẫu nhiên.
- Đọc: một chương mô hình ngăn + một paper gene stochastic + một essay giới hạn mô hình.
- Luôn hỏi: *Phương trình này hợp lệ ở thang nào?*
