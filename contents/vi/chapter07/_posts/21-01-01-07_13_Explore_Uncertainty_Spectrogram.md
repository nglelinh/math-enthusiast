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

**Mạch bài học:** Kiến thức cần nhớ (giải tích thời gian–tần số, cơ học lượng tử toán học & bất đẳng thức Robertson) → Giải thích: tự tay tính $$\sigma_X \sigma_Z$$ cho qubit thực và qubit phức (đạt dấu bằng!) → Chuẩn bị mã FFT → Các thí nghiệm phổ đồ, chirp & qubit.

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

## Kiến thức cần nhớ: Giải tích thời gian–tần số và Cơ học lượng tử toán học là gì, nghiên cứu những gì?

Người học kỹ thuật điện tử gặp nguyên lý bất định trong thiết kế bộ lọc âm thanh, radar và nén ảnh; còn người học vật lý gặp nó ở hạt vi mô. Đứng sau cả hai lĩnh vực là ba trụ cột có chung một nền giải tích:

### 1. Giải tích thời gian–tần số (Time–Frequency Analysis) và Phổ đồ

Một bản nhạc thay đổi cao độ theo từng giây, nên lấy biến đổi Fourier trên toàn bộ bản nhạc sẽ trộn lẫn mọi nốt nhạc lại với nhau. Để biết *nốt nào vang lên lúc nào*, các kỹ sư và nhà toán học cắt tín hiệu bằng một cửa sổ trượt độ dài $$T$$ rồi tính biến đổi Fourier từng đoạn — đó là **biến đổi Fourier thời gian ngắn (STFT)** tạo nên **phổ đồ (spectrogram)**. Định lý bất định Fourier (Gabor / Heisenberg–Pauli–Weyl) khẳng định tích độ trải thời gian và độ trải tần số bị chặn dưới tuyệt đối:
$$
\Delta t \cdot \Delta \xi \ge \frac{1}{4\pi}.
$$
Điều đặc biệt là **hàm Gauss** $$f(x) = e^{-\pi x^2}$$ chính là "nhà vô địch" đạt dấu bằng tối ưu (vì biến đổi Fourier của một hàm Gauss lại là đúng một hàm Gauss!).

### 2. Cơ học lượng tử toán học và Bất đẳng thức Robertson

Trong cơ học lượng tử, mỗi đại lượng đo được là một toán tử tự liên hợp $$A, B$$ trên không gian Hilbert. Với bất kỳ trạng thái chuẩn hóa $$\psi$$ nào, **bất đẳng thức Robertson** (1929) khẳng định:
$$
\sigma_A(\psi)\,\sigma_B(\psi) \ge \frac{1}{2}\,\bigl\lvert \langle \psi \vert [A, B] \psi \rangle \bigr\rvert,
$$
trong đó giao hoán tử là $$[A, B] = AB - BA$$. Khi $$A$$ và $$B$$ **không giao hoán** ($$AB \neq BA$$), ta có một rào cản đại số ngăn không cho cả hai phép đo đồng thời sắc nét tuyệt đối.

### 3. Nguyên lý bất định rời rạc và Fractal (mở rộng hiện đại)

Ngay cả trên tín hiệu rời rạc hữu hạn (DFT cỡ $$N$$), một vectơ có $$s$$ thành phần khác 0 và phổ của nó có $$\hat s$$ thành phần khác 0 luôn phải thỏa $$s \cdot \hat s \ge N$$ (và với $$N$$ nguyên tố, Terence Tao chứng minh chặt hơn: $$s + \hat s \ge N + 1$$). Ý tưởng này là trái tim của công nghệ **nén cảm biến (Compressed Sensing)** trong chụp cộng hưởng từ MRI.

---

### Giải thích: Cầm tay kiểm chứng bất đẳng thức Robertson trên một qubit thực và phức

Hãy tự tay tính tất cả các số hạng cho hai ma trận Pauli quen thuộc:
$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.
$$
Trước hết, tính giao hoán tử $$[X, Z] = XZ - ZX$$:
$$
XZ = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad ZX = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \implies [X, Z] = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = -2iY.
$$
Chú ý $$X^2 = I$$ và $$Z^2 = I$$ nên với mọi trạng thái chuẩn hóa $$\psi$$, ta có công thức độ lệch chuẩn cực gọn: $$\sigma_X = \sqrt{1 - \langle X\rangle^2}$$ và $$\sigma_Z = \sqrt{1 - \langle Z\rangle^2}$$. Bây giờ thử trên hai trạng thái cụ thể:

1. **Trạng thái thực $$\psi_\theta = (\cos(\theta/2),\; \sin(\theta/2))^T$$:**
   - Tại $$\theta = 0$$ ($$\psi_0 = (1, 0)^T$$): $$\langle Z \rangle = 1 \implies \sigma_Z = 0$$; $$\langle X \rangle = 0 \implies \sigma_X = 1$$. Tích $$\sigma_X \sigma_Z = 0$$, và vế phải cũng bằng $$0$$.
   - Tại $$\theta = \pi/4$$: $$\langle Z \rangle = \cos(\pi/4) = \frac{\sqrt{2}}{2} \implies \sigma_Z = \frac{\sqrt{2}}{2}$$; $$\langle X \rangle = \sin(\pi/4) = \frac{\sqrt{2}}{2} \implies \sigma_X = \frac{\sqrt{2}}{2}$$, nên **vế trái $$\sigma_X \sigma_Z = 0.5$$**. Nhưng hãy tính **vế phải**: vì $$\psi_\theta$$ thuần thực nên $$\langle \psi_\theta \vert (-2iY) \psi_\theta \rangle = -2i \cdot 0 = \mathbf{0}$$! Đây là phát hiện thực nghiệm cực hay: trên vòng tròn thực $$XZ$$, bất đẳng thức vẫn đúng ($$0.5 \ge 0$$) nhưng vế phải bị triệt tiêu bằng 0!
2. **Trạng thái phức $$\tilde\psi = \frac{1}{\sqrt{2}}(1,\; i)^T$$ (trạng thái riêng của $$Y$$):**
   - $$\langle Z \rangle = \frac{1}{2}(1 - 1) = 0 \implies \sigma_Z = 1$$;
   - $$\langle X \rangle = \frac{1}{2}(1\cdot i + (-i)\cdot 1) = 0 \implies \sigma_X = 1$$;
   - **Vế trái:** $$\sigma_X \sigma_Z = 1 \times 1 = \mathbf{1}$$.
   - **Vế phải:** $$\frac{1}{2}\bigl\lvert \langle \tilde\psi \vert (-2iY)\tilde\psi \rangle \bigr\rvert = \bigl\lvert \langle \tilde\psi \vert Y \tilde\psi \rangle \bigr\rvert = \bigl\lvert \tfrac{1}{2}(1\cdot 1 + (-i)(i)) \bigr\rvert = \mathbf{1}$$!
   Ta chạm **đúng dấu bằng $$1 = 1$$** — trạng thái $$\tilde\psi$$ tối đa hóa đồng thời độ bất định của cả $$X$$ và $$Z$$ đúng bằng cận dưới Robertson!

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
