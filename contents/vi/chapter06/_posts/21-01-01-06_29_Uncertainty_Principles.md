---
layout: post
title: "Nguyên lý bất định: Fourier, Heisenberg và thông tin"
chapter: '06'
order: 29
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Một tiếng trống ngắn không có cao độ xác định. Một nốt nhạc thuần kéo dài không có thời điểm bắt đầu xác định. Hai câu đó đã là một nguyên lý bất định, và chúng không hề nhắc đến nguyên tử. Cơ học lượng tử thừa hưởng cùng giới hạn này vì hàm sóng theo vị trí và hàm sóng theo động lượng là một **cặp Fourier**. Hằng số $$\hbar$$ chỉ đổi đơn vị; bản thân bất đẳng thức là một kết quả giải tích.

Bài này thuộc nhánh Cầu nối Vật lý–Toán. Bài trình bày dạng Fourier, dạng Heisenberg–Kennard, cận dưới qua giao hoán tử của Robertson, và một phiên bản theo lý thuyết thông tin. Nên đọc sau bài [cơ học lượng tử trên không gian Hilbert]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/) và cùng lúc với bài [Fourier trong thế giới]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/). Phiên bản fractal (2025) nằm ở bài đi kèm.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu **bất đẳng thức bất định Fourier** (Pauli–Weyl) và biết hàm Gauss là hàm đạt cực tiểu.
- Viết cận **Kennard** $$\sigma_x\sigma_p\ge\hbar/2$$ và nói rõ quy ước $$\hbar$$ đang dùng.
- Phác họa cách suy ra hệ thức **Robertson** $$\sigma_A\sigma_B\ge\tfrac12\bigl|\langle[A,B]\rangle\bigr|$$ từ bất đẳng thức Cauchy–Schwarz (với các đại lượng quan sát đã trừ trung bình).
- Phân biệt **hệ thức giao hoán chính tắc** với **dạng Weyl**, và biết phát biểu của định lý **Stone–von Neumann** về tính duy nhất (không cần tính toán đầy đủ).
- Tránh ba nhầm lẫn: coi lập luận kính hiển vi "phép đo làm xáo trộn hạt" là định lý; coi hệ thức năng lượng–thời gian là cùng một hệ thức giao hoán; coi bất định là hỗn loạn hay entropy nhiệt.
- Nêu một dạng **bất định entropy**, nối sang [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/).

**Kiến thức nền.** Tích trong; ý tưởng của biến đổi Fourier ([Chương 3]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/)); toán tử tự liên hợp đóng vai đại lượng quan sát ([Hilbert / cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/)). Không cần lý thuyết hàm suy rộng.

---

## 1. Không chỉ là chuyện lượng tử

Một sóng sin kéo dài vô hạn có tần số tuyệt đối chính xác nhưng hoàn toàn không định vị được trong thời gian. Một xung Dirac định vị thời gian hoàn hảo nhưng có phổ phẳng. Mọi tín hiệu thực tế nằm ở giữa: làm gói sóng hẹp hơn ở một miền **buộc** nó phải trải rộng ra ở miền đối ngẫu.

![Xung hẹp có phổ rộng; nốt dài có phổ sắc]({{ site.baseurl }}/img/chapter_img/uncertainty_time_freq_pairs.png)

*Hình. Không thể sắc nét đồng thời ở cả hai miền. Trên: một xung ngắn và biến đổi Fourier trải rộng của nó. Dưới: một nốt gần thuần, kéo dài, và hai đỉnh tần số (hàm cosin).*

Đây là thông điệp của video 3Blue1Brown, và là cách vào đề đúng. Xung radar, nốt nhạc, và phổ đồ dùng cửa sổ trong [bài Fourier ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/) có cùng một cấu trúc hình học. Cơ học lượng tử là trường hợp biến đối ngẫu là **động lượng**.

---

## 2. Bất đẳng thức Fourier

Chọn quy ước giữ được tính unita:

$$
\hat f(\xi)=\int_{-\infty}^{\infty} f(x)\,e^{-2\pi i x\xi}\,dx,
$$

với công thức ngược có cùng dạng (đổi dấu số mũ) trên các hàm Schwartz, rồi mở rộng sang $$L^2$$ bằng tính trù mật. Viết $$\|g\|_2^2=\int |g|^2$$. Bất đẳng thức **Heisenberg–Pauli–Weyl** nói rằng nếu $$f$$ đủ tốt để các moment tồn tại thì

$$
\Bigl(\int x^2|f(x)|^2\,dx\Bigr)^{1/2}
\Bigl(\int \xi^2|\hat f(\xi)|^2\,d\xi\Bigr)^{1/2}
\ge \frac{1}{4\pi}\,\|f\|_2^2.
$$

Nếu $$f$$ đã được căn tâm (trung bình của $$x$$ và của $$\xi$$ đều bằng không), hai thừa số chính là độ lệch chuẩn theo thời gian và theo tần số. Hằng số $$1/4\pi$$ đến từ $$2\pi$$ trong số mũ; đổi quy ước Fourier thì hằng số đổi theo. Hiện tượng thì **không** đổi: không thể đẩy cả hai thừa số về không, trừ khi $$f=0$$.

**Hàm đạt cực tiểu.** Dấu bằng xảy ra với **hàm Gauss**. Trong cách chuẩn hóa này, $$e^{-\pi x^2}$$ là biến đổi Fourier của chính nó. Các hàm đạt cực tiểu khác thu được bằng phép tịnh tiến, phép điều biến (nhân với một sóng phẳng) và phép co giãn của hàm Gauss. Không có hàm $$L^2$$ nào khác đạt dấu bằng. (Lưu ý: nếu nhân thêm một chirp $$e^{i\alpha x^2}$$ với $$\alpha$$ khác 0, hàm thu được không còn đạt dấu bằng ở bất đẳng thức này; nó chỉ đạt dấu bằng ở dạng Schrödinger mạnh hơn, xem §4.)

![Gaussian và biến đổi Fourier cùng một hình]({{ site.baseurl }}/img/chapter_img/uncertainty_gaussian_minimizer.png)

*Hình. Các hàm Gauss (sai khác các phép biến đổi nói trên) là những hàm định vị tốt nhất mà bất đẳng thức cho phép.*

**Trực giác.** Sau biến đổi Fourier, phép lấy đạo hàm theo $$x$$ trở thành phép nhân với tần số. Bất đẳng thức Cauchy–Schwarz áp dụng cho $$xf$$ và $$f'$$ đã cho một cận dưới; đẳng thức $$f'\leftrightarrow 2\pi i\xi\hat f$$ biến nó thành bất đẳng thức ở trên.

---

## 3. Vị trí, động lượng và cận Kennard

Một hạt trên đường thẳng có hàm sóng chuẩn hóa $$\psi\in L^2(\mathbb{R})$$. Quy tắc Born coi $$|\psi(x)|^2$$ là mật độ xác suất của vị trí. Hàm sóng trong không gian động lượng là biến đổi Fourier, với tần số vật lý $$p/\hbar$$:

$$
\phi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}\psi(x)\,e^{-ipx/\hbar}\,dx.
$$

Khi đó $$|\phi(p)|^2$$ là mật độ xác suất của động lượng. Vì $$\psi$$ và $$\phi$$ là một cặp Fourier, bất đẳng thức giải tích trở thành **dạng Kennard của nguyên lý Heisenberg** (Kennard 1927, Weyl trình bày gọn lại):

$$
\sigma_x\,\sigma_p \ge \frac{\hbar}{2}.
$$

Ở đây $$\sigma_x^2=\langle X^2\rangle-\langle X\rangle^2$$, với $$X$$ là phép nhân với $$x$$; $$\sigma_p$$ được định nghĩa tương tự cho $$P=-i\hbar\frac{d}{dx}$$. Sách phổ thông đôi khi viết $$h/4\pi$$; đó là cùng một phát biểu vì $$\hbar=h/2\pi$$.

Hằng số này không phải một hệ số đo trong phòng thí nghiệm. Một khi chấp nhận (i) trạng thái là vectơ đơn vị trong $$L^2$$, (ii) quy tắc Born, và (iii) hệ thức de Broglie đồng nhất động lượng với tần số, thì bất đẳng thức là một định lý.

---

## 4. Robertson: bất định đến từ giao hoán tử

Kennard là một trường hợp riêng. Cho $$A$$ và $$B$$ tự liên hợp (trên một miền trù mật chung, với các lưu ý thông thường về miền xác định). Viết $$\sigma_A^2=\bigl\|(A-\langle A\rangle)\psi\bigr\|^2$$, và tương tự cho $$B$$. Sau khi trừ trung bình, có thể giả sử $$\langle A\rangle=\langle B\rangle=0$$. Khi đó

$$
\bigl|\langle\psi|[A,B]\psi\rangle\bigr|
= 2\bigl|\operatorname{Im}\langle A\psi,B\psi\rangle\bigr|
\le 2\,\|A\psi\|\,\|B\psi\|,
$$

theo bất đẳng thức Cauchy–Schwarz. Vậy

$$
\sigma_A\,\sigma_B \ge \frac12\bigl|\langle[A,B]\rangle\bigr|.
$$

Đây là **hệ thức Robertson**. Dạng **Schrödinger** mạnh hơn, có thêm số hạng hiệp phương sai ở vế phải; ta không cần đến nó.

Nếu $$[X,P]=i\hbar$$ thì vế phải bằng $$\hbar/2$$, và ta lấy lại cận Kennard. Nếu $$A$$ và $$B$$ giao hoán trên trạng thái đang xét, cận dưới bằng không: cả hai có thể cùng sắc nét (ví dụ cùng một thành phần spin đo hai lần, hoặc $$X$$ với chính nó). Bất định không có nghĩa là "mọi thứ đều mờ". Nó là **sự không giao hoán, được đo bằng số**.

![Bloch: trạng thái không thể nằm cả hai trục X và Z]({{ site.baseurl }}/img/chapter_img/uncertainty_robertson_pauli.png)

*Hình. Ví dụ với một qubit. Các ma trận Pauli thỏa $$[X,Z]=-2iY$$, nên $$\sigma_X\sigma_Z\ge|\langle Y\rangle|$$. Trạng thái riêng của $$Z$$ có $$\sigma_Z=0$$ và độ trải theo $$X$$ lớn nhất.*

---

## 5. Hệ thức giao hoán chính tắc, hệ thức Weyl, định lý Stone–von Neumann

**Hệ thức giao hoán chính tắc**

$$
[X,P]=i\hbar I
$$

không thể đúng với các toán tử bị chặn trên không gian Hilbert (trong trường hợp hữu hạn chiều, lấy vết hai vế sẽ thấy mâu thuẫn; trường hợp tổng quát cũng có lập luận riêng khi cả hai toán tử bị chặn). Vậy $$X$$ và $$P$$ là **toán tử không bị chặn**, và đẳng thức trên chỉ là đẳng thức toán tử trên một miền xác định cụ thể. Cách phát biểu an toàn hơn là **dạng Weyl**: các nhóm unita một tham số $$U(a)=e^{-iaP/\hbar}$$ (tịnh tiến) và $$V(b)=e^{-ibX/\hbar}$$ (điều biến) thỏa

$$
U(a)V(b)=e^{-iab/\hbar}\,V(b)U(a).
$$

(Dấu trong số mũ phụ thuộc quy ước. Với quy ước $$U(a)$$ dịch hàm sóng sang phải một đoạn $$a$$, tính trực tiếp cho thừa số mũ với dấu cộng thay vì dấu trừ.)

**Định lý Stone–von Neumann (ý chính).** Mọi biểu diễn bất khả quy của hệ thức Weyl trên một không gian Hilbert khả ly đều tương đương unita với biểu diễn Schrödinger trên $$L^2(\mathbb{R}^n)$$. Theo nghĩa đó, "vị trí và động lượng trên đường thẳng" chỉ có một lý thuyết lượng tử duy nhất.

**Điều định lý không nói.** Với vô hạn bậc tự do (lý thuyết trường), tính duy nhất này mất đi. Đó là một lý do khiến [đại số toán tử]({{ site.baseurl }}/contents/vi/chapter06/06_24_Operator_Algebras_QM/) xuất hiện. Các vấn đề về miền xác định, tính tự liên hợp cốt yếu, và sự khác nhau giữa hệ thức giao hoán hình thức với hệ thức Weyl đúng nghĩa đã được nêu trong [bài Hilbert]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/).

---

## 6. Năng lượng–thời gian là một định lý khác

Không có **toán tử thời gian** tự liên hợp $$T$$ trên không gian Hilbert thông thường thỏa $$[H,T]=i\hbar$$ khi Hamiltonian bị chặn dưới. Pauli đã chỉ ra vật cản: hệ thức Weyl sẽ buộc phổ của $$H$$ phải là toàn bộ $$\mathbb{R}$$. Công thức phổ thông $$\Delta E\,\Delta t\ge\hbar/2$$ **không** phải là hệ thức Robertson áp dụng cho cặp $$(H,T)$$.

Có những phát biểu thay thế hữu ích, và chúng là các định lý khác. Chẳng hạn, **Mandelstam–Tamm** chặn tốc độ một trạng thái trở nên trực giao với chính nó: nếu $$\tau$$ là thời gian để tích vô hướng giữa trạng thái ban đầu và trạng thái hiện tại giảm về không, thì $$\tau\,\sigma_H\ge\hbar/2$$ (hằng số tốt nhất là $$\pi\hbar/2$$). Đó là một giới hạn tốc độ, không phải khẳng định về việc đo đồng thời một "đại lượng thời gian".

**Độ trải của trạng thái và nhiễu do phép đo.** Câu chuyện kính hiển vi tia γ của Heisenberg (1927) nói về việc phép đo làm xáo trộn hạt. Bất đẳng thức Kennard/Robertson nói về **độ trải của một trạng thái đã được chuẩn bị** đối với hai đại lượng quan sát không giao hoán; trong phát biểu không có máy đo nào. Các bất đẳng thức hiện đại về sai số và nhiễu của phép đo (Ozawa và các tác giả sau) là một chủ đề kỹ thuật riêng; khóa học này chỉ nêu tên, không chứng minh.

---

## 7. Tính bổ sung theo entropy

Phương sai có thể gây hiểu lầm. Một mật độ có hai đỉnh nằm xa nhau có phương sai lớn, dù xác suất vẫn "tập trung trên một tập nhỏ". **Entropy** đo kích thước miền tập trung trung thực hơn. Hirschman đưa ra phỏng đoán, Beckner và Białynicki-Birula–Mycielski chứng minh một bất đẳng thức entropy cho biến đổi Fourier: entropy Shannon của $$|\psi|^2$$ và của $$|\phi|^2$$ không thể cùng nhỏ.

Trong trường hợp hữu hạn chiều, phát biểu gọn nhất là bất đẳng thức **Maassen–Uffink**. Nếu đo một trạng thái theo hai cơ sở trực chuẩn $$\{|a_i\rangle\}$$ và $$\{|b_j\rangle\}$$, và đặt $$c=\max_{i,j}|\langle a_i|b_j\rangle|$$, thì

$$
H(A)+H(B)\ge -2\log c,
$$

trong đó $$H$$ là entropy Shannon của phân bố kết quả đo. Với một qubit đo theo cơ sở tính toán và cơ sở Hadamard, $$c=1/\sqrt{2}$$, nên tổng hai entropy ít nhất là một bit. Đó là tính bổ sung (complementarity) phát biểu như một định lý, và là cầu nối tự nhiên sang [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) cũng như một số chứng minh trong mật mã lượng tử.

---

## 8. Các định lý họ hàng (không học thêm, chỉ để biết)

| Biến thể | Ý chính | Trạng thái |
|----------|--------|------------|
| Donoho–Stark (1989) | Tín hiệu rời rạc độ dài $$N$$ không thể tập trung trên $$n_t$$ ô thời gian và $$n_\omega$$ ô tần số, trừ khi $$n_t n_\omega\ge N$$ | Định lý; dùng trong khôi phục tín hiệu thưa |
| Hardy / Beurling–Hörmander | Nếu $$f$$ và $$\hat f$$ cùng giảm nhanh hơn hàm Gauss tới hạn thì $$f=0$$ | Định lý |
| Balian–Low | Một khung Gabor tốt không thể sinh bởi một cửa sổ sắc nét cả về thời gian lẫn tần số | Định lý |
| Landau–Pollak–Slepian | Số chiều của không gian các hàm gần như giới hạn cả về thời gian lẫn dải tần; hàm sóng cầu dẹt (prolate spheroidal) | Định lý |
| [Bất định fractal]({{ site.baseurl }}/contents/vi/chapter06/06_30_Fractal_Uncertainty/) | $$f$$ và $$\hat f$$ không thể cùng tập trung gần một tập fractal xốp | Định lý cho 1 chiều (2016), và cho nhiều chiều với điều kiện xốp theo đường thẳng (Cohen 2025) |

Đánh đổi giữa độ trơn và tốc độ giảm trong [bài Fourier/Pontryagin]({{ site.baseurl }}/contents/vi/chapter06/06_16_Pontryagin_Fourier_Duality/) là cùng hiện tượng, viết bằng ngôn ngữ nhóm. Biến đổi Fourier thời gian ngắn ở Chương 3 biến bất đẳng thức thành công cụ: bạn chọn độ trải mà mình chấp nhận được.

---

## 9. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Chỉnh lại |
|------------|------|-----|
| "Đo vị trí làm xáo trộn hạt, nên $$\sigma_x\sigma_p\ge\hbar/2$$." | Sai lý do | Bất đẳng thức nói về hai độ trải của một trạng thái đã chuẩn bị. Nhiễu do phép đo là một định lý khác. |
| "Mọi cặp đại lượng đều bất định cỡ $$h/2$$." | Sai | Chỉ các cặp không giao hoán; cận dưới là $$\tfrac12|\langle[A,B]\rangle|$$. |
| "Năng lượng–thời gian cũng là hệ thức giao hoán như $$x,p$$." | Sai | Không có toán tử thời gian tự liên hợp theo nghĩa chuẩn. Dùng Mandelstam–Tamm hoặc nói rõ biến thể nào. |
| "Bất định là hỗn loạn / định luật 2 nhiệt động học." | Sai | Sự phụ thuộc nhạy vào điều kiện ban đầu và entropy nhiệt là chủ đề khác ([hỗn loạn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/)). |
| "Hàm Gauss chỉ là một ví dụ tiện tính." | Thiếu | Chúng là các hàm **đạt cực tiểu**. |

---

## Bài tập

1. **Quy ước.** Từ $$\hbar=h/2\pi$$, kiểm tra $$\hbar/2=h/4\pi$$. Viết cận Kennard theo cả hai cách.
2. **Hàm Gauss (giải tích).** Với $$f(x)=e^{-\pi x^2}$$, chứng tỏ (tra cứu hoặc tính biến đổi đã biết) rằng $$\hat f=f$$ theo quy ước ở §2, và tích Pauli–Weyl đạt đúng $$1/4\pi$$ sau khi tính các moment bậc hai.
3. **Robertson cho qubit.** Cho $$X,Z$$ là các ma trận Pauli và $$\psi=(\cos(\theta/2),\sin(\theta/2))$$. Tính $$\sigma_X$$, $$\sigma_Z$$ và $$\tfrac12|\langle[X,Z]\rangle|$$ theo $$\theta$$. Với trạng thái này, khi nào dấu bằng xảy ra?
4. **Vì sao không có toán tử thời gian.** Viết ba câu: nếu $$T$$ tự liên hợp và thỏa hệ thức Weyl với Hamiltonian $$H$$, phổ của $$H$$ bị buộc phải thế nào, và vì sao điều đó mâu thuẫn với một Hamiltonian thông thường có trạng thái liên kết?
5. **Entropy và phương sai.** Phác họa một mật độ xác suất trên $$\mathbb{R}$$ có hai đỉnh hẹp nằm xa nhau. Vì sao phương sai lớn, trong khi câu hỏi "xác suất nằm ở đâu?" vẫn có câu trả lời khá định vị? Bất đẳng thức nào phản ánh đúng điều này?
6. **Đoạn nối.** Nối bài này với sự đánh đổi khi chọn cửa sổ trong biến đổi Fourier thời gian ngắn (bài Fourier ứng dụng) *và* với phần thảo luận về tính tự liên hợp trong bài Hilbert / cơ học lượng tử.

---

## Tài liệu tham khảo

- 3Blue1Brown — [The more general uncertainty principle](https://www.youtube.com/watch?v=MBnnXbOM5S4) (2018); [trang bài](https://www.3blue1brown.com/lessons/uncertainty-principle/).
- Hall — *Quantum Theory for Mathematicians* (CCR, Robertson, miền).
- Wolff — [The uncertainty principle: variations on a theme](https://arxiv.org/html/2006.11206v3).
- Donoho–Stark — [Uncertainty principles and signal recovery](https://epubs.siam.org/doi/10.1137/0149053), *SIAM J. Appl. Math.* 1989.
- Maassen–Uffink, *Phys. Rev. Lett.* **60** (1988).
- Khóa học: [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / QM]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [QI]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [FUP]({{ site.baseurl }}/contents/vi/chapter06/06_30_Fractal_Uncertainty/), [studio]({{ site.baseurl }}/contents/vi/chapter07/07_13_Explore_Uncertainty_Spectrogram/).
- Gói: `research/video-research/uncertainty-principles/`.
