---
layout: post
title: "Studio: Spectrograms, Gaussian và bất định"
chapter: '07'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Lộ trình: Nguyên lý bất định (thực hành)**  
> **1.** [Fourier ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), mục 8  
> **2.** [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/)  
> **3. Bạn đang ở đây:** tính một cặp Fourier, quan sát sự đánh đổi trong phổ đồ (spectrogram), và kiểm tra một bất đẳng thức cho qubit  
> *Thời gian:* khoảng 60–120 phút; cần numpy/scipy (hoặc bất kỳ công cụ FFT nào) và giấy bút.

Hãy lắng nghe hai âm thanh quen thuộc: một tiếng vỗ tay dứt khoát và một nốt kéo dài của cây đàn violin. Với tiếng vỗ tay, bạn chỉ ra được ngay *chính xác thời điểm* nó vang lên, nhưng lại không thể hát lại "cao độ" (tần số) của nó là nốt Đô hay nốt Son — vì một xung ngắn chứa đủ mọi tần số trải rộng. Ngược lại, với nốt đàn kéo dài, tai bạn nhận ra ngay cao độ chuẩn xác, nhưng lại chẳng thể nói nốt nhạc đó nằm tại một khoảnh khắc duy nhất nào!

Sự đánh đổi tưởng chừng rất đời thường ấy hóa ra lại là **cùng một định luật toán học sâu xa** với Nguyên lý Bất định Heisenberg trong cơ học lượng tử! Không phải do đồng hồ hay kính hiển vi của ta kém tinh xảo, mà là một giới hạn bất khả xâm phạm của cấu trúc sóng và không gian Hilbert. Trong bài thực hành này, bạn không cần chứng minh bất đẳng thức Pauli–Weyl bằng tay. Thay vào đó, bằng vài chục dòng mã FFT và vài phép nhân ma trận $$2\times 2$$, bạn sẽ **tận mắt chứng kiến** cả ba gương mặt của nguyên lý bất định: xung càng hẹp thì phổ càng rộng; độ dài cửa sổ phổ đồ luôn ép ta phải đánh đổi giữa thời gian và tần số; và hai toán tử không giao hoán (ma trận Pauli $$X, Z$$) không bao giờ có thể cùng lúc sắc nét.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Vẽ và so sánh một hàm Gauss, một hàm hộp, một tín hiệu hai tần số cùng với biến đổi Fourier rời rạc của chúng.
- Thay đổi độ dài cửa sổ của biến đổi Fourier thời gian ngắn (STFT) trên một tín hiệu chirp (tần số tăng dần theo thời gian) và mô tả trục nào trở nên sắc nét hơn.
- Tính $$\sigma_X\sigma_Z$$ cho một họ trạng thái qubit phụ thuộc một tham số và so sánh với vế phải của bất đẳng thức Robertson.
- Ghi rõ trong nhật ký đâu là quan sát, đâu là định lý.
- Nêu một cách hiểu sai (ví dụ "chọn cửa sổ tốt hơn thì vượt qua được nguyên lý bất định").

**Kiến thức nền.** Các mục 1–4 của bài [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/); số phức; biết dùng một hàm FFT.

---

## Bản đồ kiến thức nền: Giải tích thời gian–tần số và Cơ học lượng tử toán học là gì, nghiên cứu những gì?

Người học kỹ thuật điện tử gặp nguyên lý bất định trong thiết kế bộ lọc âm thanh, radar và nén ảnh; còn người học vật lý gặp nó ở hạt vi mô. Đứng sau cả hai lĩnh vực là hai nhánh toán học có chung bộ khung giải tích:

1. **Giải tích thời gian–tần số (Time–Frequency Analysis):** Một bản nhạc thay đổi cao độ theo từng giây, nên lấy biến đổi Fourier trên toàn bộ bản nhạc sẽ trộn lẫn mọi nốt nhạc lại với nhau. Để biết *nốt nào vang lên lúc nào*, các kỹ sư và nhà toán học cắt tín hiệu bằng một cửa sổ trượt độ dài $$T$$ rồi tính biến đổi Fourier từng đoạn — đó là **biến đổi Fourier thời gian ngắn (STFT)** tạo nên **phổ đồ (spectrogram)**. Định lý bất định Fourier (Gabor / Heisenberg–Pauli–Weyl) khẳng định tích độ trải thời gian và độ trải tần số bị chặn dưới tuyệt đối: $$\Delta t \cdot \Delta \xi \ge \frac{1}{4\pi}$$. Điều đặc biệt là **hàm Gauss** $$e^{-\pi x^2}$$ chính là "nhà vô địch" duy nhất đạt dấu bằng tối ưu!
2. **Cơ học lượng tử toán học và Toán tử không giao hoán:** Trong cơ học lượng tử, mỗi đại lượng đo được là một toán tử tuyến tính $$A, B$$. Với bất kỳ trạng thái $$\psi$$ nào, **bất đẳng thức Robertson** khẳng định:
$$
\sigma_A(\psi)\,\sigma_B(\psi) \ge \frac{1}{2}\,\bigl\lvert \langle \psi \vert [A, B] \psi \rangle \bigr\rvert,
$$
trong đó giao hoán tử là $$[A, B] = AB - BA$$. Khi hai toán tử **không giao hoán** ($$AB \neq BA$$), không tồn tại trạng thái nào đồng thời làm triệt tiêu cả hai độ bất định (trừ các trường hợp kỳ vọng giao hoán tử bằng 0).

Một **ví dụ tính tay gọn nhẹ** ngay cho Việc C: với hai ma trận Pauli $$X = \begin{pmatrix}0&1\\1&0\end{pmatrix}$$ và $$Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$, ta có $$[X, Z] = XZ - ZX = \begin{pmatrix}0&-2\\2&0\end{pmatrix} = -2iY$$. Với trạng thái thực $$\psi_\theta = (\cos(\theta/2), \sin(\theta/2))^T$$:
- Tại $$\theta = 0$$ (trạng thái riêng của $$Z$$: $$\psi_0 = (1, 0)^T$$): ta đo $$Z$$ chắc chắn ra $$+1$$ nên $$\sigma_Z = 0$$, còn đo $$X$$ ra $$\pm 1$$ với xác suất $$50\%/50\%$$ nên $$\sigma_X = 1$$. Lúc này tích $$\sigma_X \sigma_Z = 0$$, và vế phải Robertson cũng bằng $$0$$!
- Tại $$\theta = \pi/2$$ (trạng thái riêng của $$X$$: $$\psi_{\pi/2} = (1/\sqrt{2}, 1/\sqrt{2})^T$$): $$\sigma_X = 0$$ và $$\sigma_Z = 1$$.
- Còn ở giữa, ví dụ $$\theta = \pi/4$$: cả $$\sigma_X$$ và $$\sigma_Z$$ đều dương (cụ thể $$\sigma_Z = \sin(\pi/4) = \frac{\sqrt{2}}{2}$$ và $$\sigma_X = \cos(\pi/4) = \frac{\sqrt{2}}{2}$$, nên $$\sigma_X \sigma_Z = 0.5$$), trong khi vì $$\psi_\theta$$ có các thành phần hoàn toàn thực nên $$\langle \psi_\theta \vert (-2iY) \psi_\theta \rangle = 0$$! Phát hiện nhỏ này cho thấy một bài học cực hay khi làm thí nghiệm: với trạng thái thực trên vòng tròn $$XZ$$, vế phải Robertson luôn bằng $$0$$ (nếu muốn thấy vế phải khác $$0$$, bạn cần thêm pha phức như $$\psi = (\cos(\theta/2), i\sin(\theta/2))^T$$!).

---

## 1. Chuẩn bị

Bạn có thể dùng ngôn ngữ lập trình bất kỳ. Đoạn Python dưới đây chỉ là gợi ý, không bắt buộc dùng thư viện nào.

```python
import numpy as np

N = 2048
x = np.linspace(-8, 8, N, endpoint=False)
dx = x[1] - x[0]
xi = np.fft.fftshift(np.fft.fftfreq(N, d=dx))

def pair(f):
    fhat = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(f))) * dx
    return f, fhat
```

Quy ước chuẩn hóa trong `numpy.fft` **khác** quy ước unita có hệ số $$2\pi$$ dùng trong bài giảng. Đừng cố tìm đúng hằng số $$1/4\pi$$ nếu chưa chuẩn hóa cẩn thận. Bài này chỉ quan tâm đến **hình dạng và xu hướng**.

---

## 2. Việc cần làm

### Việc A: Ba cặp Fourier (30 phút)

Tạo ba tín hiệu thực trên cùng một lưới: hàm Gauss $$e^{-\pi x^2}$$, hàm hộp (hàm chỉ thị của $$[-0.4,0.4]$$), và tín hiệu hai tần số $$\cos(2\pi\cdot 1.2 x)+\cos(2\pi\cdot 2.3 x)$$ nhân với một đường bao Gauss rộng. Vẽ $$\lvert f \rvert$$ và $$\lvert \hat f \rvert$$.

**Viết:** cặp nào gần nhất với trường hợp "cả hai phía đều tập trung tốt nhất có thể"? Cặp nào giống ví dụ tiếng trống (hoặc tiếng vỗ tay) và nốt nhạc trong bài giảng? Chú ý thêm: phổ của hàm hộp là hàm $$\operatorname{sinc}$$ có các "đuôi" dao động tắt rất chậm — vì sao cạnh cắt sắc nhọn trong thời gian lại đẻ ra đuôi tần số dài như vậy?

### Việc B: Cửa sổ của phổ đồ (25 phút)

Tạo một chirp tuyến tính, ví dụ $$f(t)=\sin(2\pi(0.5 t + 0.15 t^2))$$. Tính phổ đồ hai lần: một lần với cửa sổ ngắn, một lần với cửa sổ dài (STFT bằng các FFT chồng lấn, hoặc dùng `scipy.signal.spectrogram`).

**Viết:** cửa sổ nào cho biết chính xác *thời điểm* xuất hiện một cao độ? Cửa sổ nào cho biết chính xác *cao độ* tại một thời điểm? Viết một câu liên hệ với mục 8 của [bài Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/).

### Việc C: Bất đẳng thức Robertson cho ma trận Pauli (20 phút)

Cho $$X,Z$$ là các ma trận Pauli và $$\psi_\theta=(\cos(\theta/2),\,\sin(\theta/2))$$. Với khoảng mười hai góc trong $$[0,\pi]$$, tính $$\sigma_X$$, $$\sigma_Z$$, tích của chúng, và $$\tfrac12\bigl\lvert\langle\psi\vert [X,Z]\psi\rangle\bigr\rvert$$. (Khuyến khích thử thêm họ trạng thái phức $$\tilde\psi_\theta = (\cos(\theta/2),\, i\sin(\theta/2))$$ để thấy vế phải Robertson khác 0!)

**Viết:** bất đẳng thức trở thành đẳng thức ở đâu? Điều gì xảy ra tại các trạng thái riêng của $$Z$$?

### Việc D: DFT của tập Cantor (không bắt buộc, 15 phút)

Tạo một vectơ độ dài $$N=3^5$$, bằng 1 trên tập Cantor rời rạc (lặp lại việc bỏ một phần ba ở giữa của các chỉ số còn lại) và bằng 0 ở các vị trí khác. Vẽ môđun của DFT. Bạn **không** chứng minh nguyên lý bất định fractal (FUP). Bạn chỉ quan sát: phổ có những "lỗ hổng" giống như tập ban đầu không?

### Việc E: Nhật ký

Ghi lại một lỗi bạn suýt mắc, ví dụ coi hệ thức năng lượng–thời gian giống hệt bất đẳng thức Kennard, hoặc đổ lỗi "thư viện FFT bị sai" cho một độ trải phổ có thật.

---

## 3. Tiêu chí đạt

| Tiêu chí | Đạt |
|----------|-----|
| Các cặp Fourier | Ba đồ thị kèm phần so sánh bằng lời |
| Phổ đồ | Có cả hai cửa sổ; gọi tên được sự đánh đổi |
| Qubit | Có đồ thị hoặc bảng so sánh tích với vế phải Robertson |
| Nhật ký | Có ít nhất một cách hiểu sai |
| Trung thực | Không khẳng định Việc D chứng minh được FUP |

---

## 4. Mở rộng (không bắt buộc)

Với các tín hiệu ở Việc A, sau khi dời về tâm, ước lượng mômen bậc hai của $$\lvert f \rvert^2$$ và $$\lvert \hat f \rvert^2$$. Giải thích vì sao tích của chúng sẽ không khớp với $$1/4\pi$$, trừ khi quy ước FFT và tích vô hướng rời rạc được chỉnh cho đúng với quy ước trong bài giảng.

---

## Xem thêm

- [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/)  
- [Nguyên lý bất định fractal]({{ site.baseurl }}/contents/vi/chapter06/06_30_Fractal_Uncertainty/)  
- [Fourier ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/)  
- [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/)  

Bài thực hành này thuộc cùng đợt với các bài thực hành khác của nhánh Cầu nối Vật lý–Toán.
