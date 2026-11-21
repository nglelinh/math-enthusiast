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

Bài này không yêu cầu chứng minh bất đẳng thức Pauli–Weyl. Mục đích là để bạn **tự thấy** ba điều: xung càng ngắn thì phổ càng rộng; độ dài cửa sổ phân tích không phải là chuyện tùy thích của người dùng; và hai ma trận Pauli $$X$$, $$Z$$ không thể cùng lúc có giá trị xác định.

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

Tạo ba tín hiệu thực trên cùng một lưới: hàm Gauss $$e^{-\pi x^2}$$, hàm hộp (hàm chỉ thị của $$[-0.4,0.4]$$), và tín hiệu hai tần số $$\cos(2\pi\cdot 1.2 x)+\cos(2\pi\cdot 2.3 x)$$ nhân với một đường bao Gauss rộng. Vẽ $$|f|$$ và $$|\hat f|$$.

**Viết:** cặp nào gần nhất với trường hợp "cả hai phía đều tập trung tốt nhất có thể"? Cặp nào giống ví dụ tiếng trống và nốt nhạc trong bài giảng?

### Việc B: Cửa sổ của phổ đồ (25 phút)

Tạo một chirp tuyến tính, ví dụ $$f(t)=\sin(2\pi(0.5 t + 0.15 t^2))$$. Tính phổ đồ hai lần: một lần với cửa sổ ngắn, một lần với cửa sổ dài (STFT bằng các FFT chồng lấn, hoặc dùng `scipy.signal.spectrogram`).

**Viết:** cửa sổ nào cho biết chính xác *thời điểm* xuất hiện một cao độ? Cửa sổ nào cho biết chính xác *cao độ* tại một thời điểm? Viết một câu liên hệ với mục 8 của [bài Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/).

### Việc C: Bất đẳng thức Robertson cho ma trận Pauli (20 phút)

Cho $$X,Z$$ là các ma trận Pauli và $$\psi_\theta=(\cos(\theta/2),\,\sin(\theta/2))$$. Với khoảng mười hai góc trong $$[0,\pi]$$, tính $$\sigma_X$$, $$\sigma_Z$$, tích của chúng, và $$\tfrac12\bigl|\langle\psi|[X,Z]\psi\rangle\bigr|$$.

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

Với các tín hiệu ở Việc A, sau khi dời về tâm, ước lượng mômen bậc hai của $$|f|^2$$ và $$|\hat f|^2$$. Giải thích vì sao tích của chúng sẽ không khớp với $$1/4\pi$$, trừ khi quy ước FFT và tích vô hướng rời rạc được chỉnh cho đúng với quy ước trong bài giảng.

---

## Xem thêm

- [Nguyên lý bất định]({{ site.baseurl }}/contents/vi/chapter06/06_29_Uncertainty_Principles/)  
- [Nguyên lý bất định fractal]({{ site.baseurl }}/contents/vi/chapter06/06_30_Fractal_Uncertainty/)  
- [Fourier ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/)  
- [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/)  

Bài thực hành này thuộc cùng đợt với các bài thực hành khác của nhánh Cầu nối Vật lý–Toán.
