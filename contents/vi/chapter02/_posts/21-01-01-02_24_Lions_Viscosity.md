---
layout: post
title: "Pierre-Louis Lions: Nghiệm nhớt và PDE phi tuyến (Huy chương Fields 1994)"
chapter: '02'
order: 24
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Pierre-Louis Lions** nhận **Huy chương Fields 1994** cho một khối công trình về phương trình đạo hàm riêng phi tuyến mà, như S. R. S. Varadhan nhấn mạnh trong bài giảng ICM Zürich, “have always been motivated by applications.” Trang IMU trích sự nhấn mạnh ấy chứ không một định lý dạng đóng. Ý tưởng mang đi được mà khóa đầu tiên thực sự *dùng* được là **nghiệm nhớt** (viscosity solution) của phương trình Hamilton–Jacobi: một khái niệm nghiệm yếu dựng từ hàm thử chạm đồ thị một phía, thiết kế để uniqueness và ổn định sống sót sau khi đạo hàm cổ điển biến mất.

Bài này dành cho người đã thấy PDE cấp một và một bài toán cực tiểu, muốn nắm kiến trúc giải tích phi tuyến cuối thế kỷ XX. Bài **không** trình bày **mean field games** (Lasry–Lions, khoảng 2006–07) như trích dẫn 1994—đó là hướng đi sau. Nó giải thích khẩu hiệu cẩn thận: bất đẳng thức nhớt, concentration-compactness, lý thuyết động học DiPerna–Lions, và một lý thuyết nghiệm yếu tầm Fields sắp xếp lại cảnh quan ra sao.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu định nghĩa **viscosity** của nghiệm phương trình Hamilton–Jacobi trong một đoạn cẩn thận (hàm thử, chạm một phía, bất đẳng thức trên $$H$$).
- Giải thích vì sao nghiệm $$C^1$$ cổ điển có thể không tồn tại toàn cục dù phương trình đơn giản, và vì sao xấp xỉ vanishing viscosity gợi tên gọi.
- Mô tả **concentration-compactness** như tam phân cho dãy cực tiểu mất compactness (biến mất, tách, hoặc compact hóa sau tịnh tiến).
- Định vị **DiPerna–Lions** như lý thuyết dữ liệu lớn cho phương trình Boltzmann, không như mã chất lưu số.
- Giữ huy chương 1994 và chương trình mean field games Lasry–Lions sau này trên **hai dòng thời gian tách biệt**.

**Kiến thức nền.** Giải tích nhiều biến; PDE như tiến hóa hoặc cân bằng dừng; hàm Lipschitz và phương pháp đặc trưng ở mức khẩu hiệu. Không cần khóa nghiệm nhớt trước.

**Liên kết seminar.** LO1 / LO4 (chương trình giải tích khó; ứng dụng như nguồn định lý). Ghép [Deng / giới hạn động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) cho một chương Boltzmann sau này, [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) cho chính quy biên tự do, và [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) chỉ như câu hỏi continuum kề—không như bài Lions đã đóng.

---

## 1. Vì sao phương trình phi tuyến cấp một cần khái niệm nghiệm mới

Phương trình Hamilton–Jacobi

$$
u_t + H(x,Du)=0
$$

xuất hiện từ điều khiển tối ưu, quang hình học, và lan truyền mặt trước. Phương pháp đặc trưng chỉ cho nghiệm trơn đến khi các đặc trưng cắt nhau. Sau đó, một hàm Lipschitz vẫn có thể mô tả hàm giá trị hoặc mặt lan, nhưng $$Du$$ không tồn tại trên nếp gấp, và cách hiểu distributional ngây thơ của phương trình fully nonlinear thường quá yếu để khôi phục uniqueness.

Crandall và Lions (1983) đề xuất **nghiệm nhớt**. Giả sử hàm thử trơn $$\varphi$$ chạm $$u$$ từ phía trên tại một điểm. Khi ấy đạo hàm của $$\varphi$$ đủ tư cách thay cho đạo hàm của $$u$$, và bất đẳng thức Hamiltonian được đòi hỏi nơi $$\varphi$$:

$$
\varphi_t + H(x,D\varphi)\le 0
$$

tại điểm tiếp xúc (subsolution). Chạm từ dưới đảo bất đẳng thức (supersolution). Nghiệm nhớt là cả hai. **User’s guide** sau này của Crandall–Ishii–Lions (*Bulletin of the AMS*, 1992) mở ngôn ngữ sang phương trình elliptic degenerate fully nonlinear cấp hai và trở thành sổ tay của ngành.

Tên gọi không phải tiếp thị. Nếu thêm $$\varepsilon\Delta u$$ rồi cho $$\varepsilon\to 0$$, giới hạn của các xấp xỉ parabolic—khi tồn tại—thỏa bất đẳng thức nhớt. Nhưng định nghĩa không nhắc $$\varepsilon$$: nó nội tại.

**Khẩu hiệu.** Khi đồ thị bị hàm thử trơn chạm, PDE được thử trên hàm thử.

---

## 2. Uniqueness sắp xếp lại điều gì

Một khi định nghĩa đã đặt, các định lý sâu là so sánh và ổn định. Nếu $$u$$ là subsolution và $$v$$ là supersolution, và nếu chúng được sắp trên biên hoặc ở vô hạn theo cách chính xác, thì $$u\le v$$. Uniqueness của bài toán giá trị ban đầu theo sau. Ổn định dưới giới hạn đều nghĩa là nghiệm nhớt là lớp đúng cho lược đồ số và cho việc qua giới hạn trong các xấp xỉ.

Điều này sắp xếp lại địa lý cảm xúc của PDE cấp một. Trước lý thuyết nhớt, người ta thường dừng khi đặc trưng cắt nhau, hoặc vá điều kiện entropy bằng tay trong một số định luật bảo toàn đặc biệt. Sau đó, một lớp lớn phương trình Hamilton–Jacobi và elliptic degenerate có nghiệm yếu chuẩn tắc—duy nhất, ổn định, và vẫn gắn với diễn giải điều khiển hoặc hình học đã thúc đẩy phương trình.

**Độ chính xác.** Lý thuyết nhớt không làm mọi PDE phi tuyến well posed. Định luật bảo toàn có nghiệm entropy riêng; phương trình tán sắc và chất lưu sống ở phòng thí nghiệm khác. Huy chương ghi nhận một họ phương pháp, không tuyên bố “PDE phi tuyến đã giải xong.”

---

## 3. Concentration-compactness

Máy thứ hai của Lions xử lý **mất compactness** trong phép tính biến phân. Trên $$\mathbb{R}^n$$, một dãy cực tiểu của phiếm hàm với nhúng Sobolev tới hạn có thể chạy ra vô hạn, tách thành các “bong bóng” xa nhau, hoặc—sau một tịnh tiến—vẫn compact. Nguyên lý **concentration-compactness** của Lions tổ chức các khả năng ấy và biến chúng thành định lý tồn tại: nếu vanishing và splitting bị loại nhờ đồng nhất năng lượng hoặc khối lượng, một điểm cực tiểu xuất hiện.

Nguyên lý không phải một phương trình. Đó là cách đọc dãy cực tiểu trong các bài được vật lý toán thúc đẩy—sóng đứng, độ cong cho trước, và PDE biến phân khác—khi miền không compact hoặc nhúng tới hạn.

---

## 4. DiPerna–Lions và phương trình động học

Phương trình Boltzmann theo dõi mật độ hạt trong không gian vị trí–vận tốc, với toán tử va chạm. Nghiệm yếu toàn cục cho dữ liệu lớn từng là chướng ngại nổi tiếng. DiPerna và Lions xây **nghiệm renormalized** (1989), cho lý thuyết tồn tại dữ liệu lớn đầu tiên đủ vững cho phương trình Boltzmann trong một lớp có nghĩa vật lý.

Đây là tổ tiên đúng để giữ trong tầm nhìn khi khóa học sau này bàn [các giới hạn động học của Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/). Chương trình Deng hỏi khi nào một hệ hạt hoặc sóng *suy ra* phương trình động học. DiPerna–Lions hỏi cách giải phương trình động học ấy một khi đã viết. Hai câu hỏi là anh em họ, không cùng một định lý.

---

## 5. Huy chương 1994 không phải điều gì

**Mean field games**, do Lasry và Lions phát triển khoảng 2006–07, mô tả cân bằng của nhiều tác nhân duy lý liên kết qua một trường trung bình. Chúng dùng phương trình Hamilton–Jacobi và Fokker–Planck trong một vòng đẹp, và là chương lớn sau này của sự nghiệp Lions. Chúng **không** phải lý do ủy ban 1994 họp ở Zürich. Đoạn seminar mở bằng “Lions nhận Fields vì mean field games” đảo dòng thời gian.

Văn bản ICM của Varadhan trình bày một portfolio: PDE phi tuyến được ứng dụng thúc đẩy, nghiệm nhớt, công trình biến phân và động học. Giữ portfolio, và ghi ngày từng mảnh.

---

## 6. Vì sao Huy chương Fields

Ba lý do khóa vào nhau:

1. **Độ khó.** Phương trình fully nonlinear đánh bại nhiều lý thuyết distributional; phát minh một khái niệm yếu vẫn còn uniqueness là hiếm.
2. **Vị trí trung tâm.** Phương trình Hamilton–Jacobi nằm dưới lý thuyết điều khiển, lan mặt trước, và phần lớn lý thuyết elliptic phi tuyến hiện đại.
3. **Khẩu hiệu rõ, phương pháp sâu.** “Thử PDE trên hàm chạm đồ thị” là câu học viên cao học nhớ được; chứng minh so sánh và user’s guide là công trình lớn của giải tích.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Nghiệm nhớt nghĩa là phương trình có thêm độ nhớt.” | Tên gọi gợi một xấp xỉ; định nghĩa là bất đẳng thức hàm thử nội tại. |
| “Lions nhận Fields vì mean field games.” | Mean field games là hướng đi sau (khoảng 2006–07); huy chương 1994 nói về PDE phi tuyến sớm hơn. |
| “Nghiệm nhớt luôn trơn.” | Điểm chính là cho phép nếp gấp; chính quy là câu hỏi riêng. |
| “DiPerna–Lions giải Navier–Stokes.” | Đó là lý thuyết tồn tại Boltzmann / động học, không phải bài chính quy Thiên niên kỷ. |
| “Concentration-compactness là định lý compact như Rellich.” | Đó là lưỡng phân (hoặc tam phân) *phân tích* sự thất bại của compactness. |

---

## Bài tập

1. Bằng lời của bạn: định nghĩa nhớt **quên** và **giữ** điều gì về nghiệm cổ điển của $$u_t+H(Du)=0$$?
2. Vì sao đặc trưng cắt nhau gợi ý rằng nghiệm $$C^1$$ xác định toàn cục có thể là lớp sai?
3. Viết bất đẳng thức subsolution khi hàm thử chạm $$u$$ từ trên. Rồi viết bất đẳng thức supersolution.
4. Cho tam phân mức khẩu hiệu của concentration-compactness (vanish / split / compactify).
5. **Luyện độ chính xác.** Tìm một câu phổ thông gắn mean field games với huy chương 1994. Viết lại thành hai câu chính xác.
6. **Seminar mở rộng.** So DiPerna–Lions (giải Boltzmann) với [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (suy ra Boltzmann). Mỗi bên trả lời câu hỏi nào?

---

## Nguồn video và đọc thêm

1. **Trích dẫn IMU** — Fields Medals 1994, Pierre-Louis Lions (Varadhan, ICM Proc. 1994): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994).
2. **User’s guide** — M. G. Crandall, H. Ishii, P.-L. Lions, *User’s guide to viscosity solutions of second order partial differential equations*, Bull. Amer. Math. Soc. **27** (1992).
3. **Định hướng** — S. R. S. Varadhan, *The work of Pierre-Louis Lions*, ICM Zürich 1994 Proceedings.

**Nhắc trạng thái:** Nghiệm nhớt, concentration-compactness, và tồn tại động học—**không** phải mean field games như trích dẫn huy chương, và không giải quyết chính quy Navier–Stokes.

---

## Tài liệu tham khảo

1. IMU Fields Medal 1994 — Pierre-Louis Lions; S. R. S. Varadhan, ICM Proceedings, Zürich 1994.
2. **M. G. Crandall and P.-L. Lions**, Viscosity solutions of Hamilton–Jacobi equations (1983).
3. **M. G. Crandall, H. Ishii, P.-L. Lions**, User’s guide (Bull. AMS, 1992).
4. **P.-L. Lions**, các bài concentration-compactness (thập niên 1980); **R. J. DiPerna and P.-L. Lions** về phương trình Boltzmann (1989).
5. Bài kề: [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/).

---

## Hướng đi tiếp

- Làm một bài tập nguyên lý so sánh từ user’s guide ở mức đọc lần đầu.
- So nghiệm nhớt với nghiệm entropy của định luật bảo toàn vô hướng: anh em họ, không cùng một lý thuyết.
- Tùy chọn seminar A3: một trang ghi ngày công trình mean field games sau này của Lions thành thật như chương hậu-Fields—không viết lại 1994.
