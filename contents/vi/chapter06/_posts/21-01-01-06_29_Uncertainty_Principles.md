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

Hãy lắng nghe hai âm thanh quen thuộc: một tiếng vỗ tay sắc gọn kéo dài vài phần nghìn giây, và một tiếng sáo thổi ngân dài êm ái. Với tiếng vỗ tay, bạn biết *chính xác* nó xảy ra vào tích tắc nào, nhưng không ai có thể hát lại "nốt nhạc" của tiếng vỗ tay — nó chẳng có cao độ xác định nào cả! Ngược lại, với tiếng sáo ngân dài, bạn đọc ngay được cao độ (tần số $$440\text{ Hz}$$ — nốt La), nhưng hỏi "nốt nhạc đó nằm ở đúng khoảnh khắc nào?" thì lại trở nên vô nghĩa. Hai nhận xét âm nhạc đời thường ấy **chính là một nguyên lý bất định**, và chúng không hề cần đến một nguyên tử nào!

Khi Werner Heisenberg công bố nguyên lý bất định nổi tiếng năm 1927, nhiều người tưởng nó chỉ xuất phát từ sự "vụng về" của chiếc kính hiển vi lượng tử làm xô lệch hạt electron khi chiếu sáng. Nhưng bản chất toán học của nó sâu hơn nhiều: cơ học lượng tử thừa hưởng trực tiếp giới hạn sóng từ **giải tích Fourier**, bởi hàm sóng theo vị trí và hàm sóng theo động lượng là một **cặp biến đổi Fourier** của nhau. Hằng số Planck $$\hbar$$ chỉ làm nhiệm vụ quy đổi đơn vị; bản thân bất đẳng thức là một định lý giải tích bất biến.

Bài này thuộc nhánh Cầu nối Vật lý–Toán, đi qua bốn gương mặt của cùng một định luật: dạng **Fourier**, dạng **Heisenberg–Kennard**, cận dưới qua **giao hoán tử của Robertson**, và phiên bản **lý thuyết thông tin (entropy)**. Nên đọc sau bài [cơ học lượng tử trên không gian Hilbert]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/) và cùng lúc với bài [Fourier trong thế giới]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/). Phiên bản fractal (2025) nằm ở bài đi kèm.

---

## Bản đồ kiến thức nền: Giải tích điều hòa và Các nguyên lý bất định đứng trên ba trụ cột nào?

Nếu bạn đã quen với biến đổi Fourier trong xử lý tín hiệu và bất đẳng thức Cauchy–Schwarz trong đại số tuyến tính, hãy nhìn qua ba trụ cột của họ định lý bất định:

### 1. Giải tích điều hòa: Cặp đối ngẫu thời gian – tần số
Trong giải tích điều hòa, mọi hàm số $$f(x)$$ có hai gương mặt song song: miền vị trí/thời gian ($$|f(x)|^2$$) và miền tần số/động lượng ($$|\hat f(\xi)|^2$$). Khi đo độ trải bằng phương sai, ta có bất đẳng thức **Heisenberg–Pauli–Weyl** (và dạng lượng tử **Kennard** $$\sigma_x\sigma_p \ge \hbar/2$$), với hàm đạt cực tiểu duy nhất là đường cong hình chuông **Gauss** — một định luật độ phân giải chi phối từ radar, âm thanh đến nén tín hiệu thưa (cảm biến nén Donoho–Stark).

### 2. Đại số không giao hoán: Giao hoán tử và Cận Robertson
Trong không gian Hilbert, bất kỳ cặp đại lượng tự liên hợp nào không giao hoán ($$[A, B] \neq 0$$, như hai thành phần spin $$X, Z$$ của qubit hay cặp vị trí–động lượng $$[X,P] = i\hbar$$) đều chịu chung một cận dưới sinh trực tiếp từ bất đẳng thức Cauchy–Schwarz: **hệ thức Robertson**. Còn câu chuyện miền xác định của toán tử không bị chặn dẫn tới **dạng Weyl** và **định lý duy nhất Stone–von Neumann**.

### 3. Lý thuyết thông tin: Bất định theo entropy Shannon
Phương sai có một điểm mù: một phân phối có hai mũi nhọn hẹp nằm xa nhau có phương sai rất lớn dù gần như tập trung hoàn toàn! **Bất định entropy** (Hirschman, Beckner, Maassen–Uffink) khắc phục điểm mù này và trở thành nền tảng cho các chứng minh bảo mật trong **mật mã lượng tử** (như giao thức BB84).

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

Một sóng sin kéo dài vô hạn có tần số tuyệt đối chính xác nhưng hoàn toàn không định vị được trong thời gian. Một xung Dirac định vị thời gian hoàn hảo nhưng có phổ phẳng trải đều mọi tần số. Mọi tín hiệu thực tế nằm ở giữa: ép gói sóng hẹp lại ở miền này **buộc** nó phải phình rộng ra ở miền đối ngẫu — một tính chất co giãn trực tiếp của tích phân Fourier: nếu co hàm $$f(x)$$ thành $$f(ax)$$ (hẹp đi $$a$$ lần), thì biến đổi Fourier của nó giãn ra thành $$\frac{1}{|a|}\hat f(\xi/a)$$ (rộng ra đúng $$a$$ lần!).

![Xung hẹp có phổ rộng; nốt dài có phổ sắc]({{ site.baseurl }}/img/chapter_img/uncertainty_time_freq_pairs.png)

*Hình. Không thể sắc nét đồng thời ở cả hai miền. Trên: một xung ngắn và biến đổi Fourier trải rộng của nó. Dưới: một nốt gần thuần, kéo dài, và hai đỉnh tần số (hàm cosin).*

Đây là thông điệp cốt lõi của video 3Blue1Brown, và là cách vào đề chuẩn xác nhất. Xung radar đo đồng thời khoảng cách và vận tốc Doppler, nốt nhạc, và phổ đồ dùng cửa sổ trong [bài Fourier ứng dụng]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/) đều có cùng một cấu trúc hình học. Cơ học lượng tử là trường hợp đặc biệt mà biến đối ngẫu tần số mang ý nghĩa vật lý là **động lượng**.

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

**Trực giác chứng minh.** Sau biến đổi Fourier, phép lấy đạo hàm theo $$x$$ trở thành phép nhân với tần số ($$f'\leftrightarrow 2\pi i\xi\hat f$$). Lấy tích phân từng phần cho thấy $$\|f\|_2^2 = -2\operatorname{Re}\langle xf, f'\rangle \le 2\|xf\|_2 \|f'\|_2$$ theo bất đẳng thức Cauchy–Schwarz — và định lý Plancherel đổi $$\|f'\|_2$$ thành $$2\pi\|\xi\hat f\|_2$$, cho ra ngay hệ số $$1/(4\pi)$$!

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

Hằng số này không phải một hệ số sai số đo trong phòng thí nghiệm. Một khi chấp nhận (i) trạng thái là vectơ đơn vị trong $$L^2$$, (ii) quy tắc Born, và (iii) hệ thức de Broglie đồng nhất động lượng với tần số, thì bất đẳng thức là một định lý toán học tất yếu.

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

không thể đúng với các toán tử bị chặn trên không gian Hilbert (trong trường hợp hữu hạn chiều, chỉ cần lấy vết hai vế: $$\operatorname{tr}(XP - PX) = 0 \neq i\hbar n$$ là thấy ngay mâu thuẫn!; trường hợp tổng quát cũng có lập luận riêng khi cả hai toán tử bị chặn). Vậy $$X$$ và $$P$$ buộc phải là **toán tử không bị chặn**, và đẳng thức trên chỉ là đẳng thức toán tử trên một miền xác định cụ thể. Cách phát biểu an toàn hơn là **dạng Weyl**: các nhóm unita một tham số $$U(a)=e^{-iaP/\hbar}$$ (tịnh tiến) và $$V(b)=e^{-ibX/\hbar}$$ (điều biến) thỏa

$$
U(a)V(b)=e^{-iab/\hbar}\,V(b)U(a).
$$

(Dấu trong số mũ phụ thuộc quy ước. Với quy ước $$U(a)$$ dịch hàm sóng sang phải một đoạn $$a$$, tính trực tiếp cho thừa số mũ với dấu cộng thay vì dấu trừ.)

**Định lý Stone–von Neumann (ý chính).** Mọi biểu diễn bất khả quy của hệ thức Weyl trên một không gian Hilbert khả ly đều tương đương unita với biểu diễn Schrödinger trên $$L^2(\mathbb{R}^n)$$. Theo nghĩa đó, "vị trí và động lượng trên đường thẳng" chỉ có một lý thuyết lượng tử duy nhất.

**Điều định lý không nói.** Với vô hạn bậc tự do (lý thuyết trường), tính duy nhất này mất đi. Đó là một lý do khiến [đại số toán tử]({{ site.baseurl }}/contents/vi/chapter06/06_24_Operator_Algebras_QM/) xuất hiện. Các vấn đề về miền xác định, tính tự liên hợp cốt yếu, và sự khác nhau giữa hệ thức giao hoán hình thức với hệ thức Weyl đúng nghĩa đã được nêu trong [bài Hilbert]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/).

---

## 6. Năng lượng–thời gian là một định lý khác

Không có **toán tử thời gian** tự liên hợp $$T$$ trên không gian Hilbert thông thường thỏa $$[H,T]=i\hbar$$ khi Hamiltonian bị chặn dưới (vì mọi hệ vật lý bền vững đều phải có mức năng lượng thấp nhất — trạng thái cơ bản). Wolfgang Pauli đã chỉ ra vật cản gọn ghẽ: hệ thức Weyl sinh ra bởi $$T$$ sẽ dịch phổ của $$H$$ đi một lượng tùy ý sang trái lẫn sang phải, buộc phổ của $$H$$ phải là toàn bộ trục thực $$\mathbb{R}$$! Do đó, công thức phổ thông $$\Delta E\,\Delta t\ge\hbar/2$$ **không** phải là hệ thức Robertson áp dụng cho cặp $$(H,T)$$.

Có những phát biểu thay thế hữu ích, và chúng là các định lý khác. Chẳng hạn, **Mandelstam–Tamm** chặn tốc độ một trạng thái trở nên trực giao với chính nó: nếu $$\tau$$ là thời gian để tích vô hướng giữa trạng thái ban đầu và trạng thái hiện tại giảm về không, thì $$\tau\,\sigma_H\ge\hbar/2$$ (hằng số tốt nhất là $$\pi\hbar/2$$). Đó là một giới hạn tốc độ tiến hóa lượng tử, không phải khẳng định về việc đo đồng thời một "đại lượng thời gian".

**Độ trải của trạng thái và nhiễu do phép đo.** Câu chuyện kính hiển vi tia γ của Heisenberg (1927) nói về việc phép đo làm xáo trộn hạt. Bất đẳng thức Kennard/Robertson nói về **độ trải nội tại của một trạng thái đã được chuẩn bị** đối với hai đại lượng quan sát không giao hoán; trong phát biểu không có máy đo nào cả. Các bất đẳng thức hiện đại về sai số và nhiễu của phép đo (Ozawa và các tác giả sau) là một chủ đề kỹ thuật riêng; khóa học này chỉ nêu tên, không chứng minh.

---

## 7. Tính bổ sung theo entropy

Phương sai có thể gây hiểu lầm. Hãy tưởng tượng một mật độ xác suất gồm hai mũi nhọn cực hẹp đặt ở $$x = -100$$ và $$x = +100$$: phương sai của nó khổng lồ ($$\sigma_x \approx 100$$), dù thực chất hạt gần như chắc chắn nằm trong hai chấm tí hon! **Entropy** đo độ bất định và kích thước miền tập trung trung thực hơn nhiều. Hirschman đưa ra phỏng đoán, Beckner và Białynicki-Birula–Mycielski chứng minh một bất đẳng thức entropy cho biến đổi Fourier: entropy vi phân của $$|\psi|^2$$ và của $$|\phi|^2$$ không thể cùng nhỏ.

Trong trường hợp hữu hạn chiều, phát biểu gọn nhất là bất đẳng thức **Maassen–Uffink**. Nếu đo một trạng thái theo hai cơ sở trực chuẩn $$\{|a_i\rangle\}$$ và $$\{|b_j\rangle\}$$, và đặt $$c=\max_{i,j}|\langle a_i|b_j\rangle|$$, thì

$$
H(A)+H(B)\ge -2\log c,
$$

trong đó $$H$$ là entropy Shannon của phân bố kết quả đo. Với một qubit đo theo cơ sở tính toán $$\{|0\rangle, |1\rangle\}$$ và cơ sở Hadamard $$\{|+\rangle, |-\rangle\}$$, mọi tích vô hướng đều có độ lớn $$c=1/\sqrt{2}$$, nên $$H(A) + H(B) \ge 1\text{ bit}$$!

### Khung giải thích: tự tay so sánh cận Robertson và cận entropy Maassen–Uffink trên một qubit (nên đọc chậm)

Hãy chọn một trạng thái qubit cụ thể: $$\psi = \begin{pmatrix} \sqrt{3}/2 \\ 1/2 \end{pmatrix}$$ (góc $$\theta = \pi/3$$ trên mặt cầu Bloch), và đo hai toán tử Pauli $$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$ và $$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$:

1. **Tính độ lệch chuẩn $$\sigma_Z$$ và $$\sigma_X$$:**
   - Với $$Z$$: $$\langle Z \rangle = \bigl(\frac{\sqrt{3}}{2}\bigr)^2 - \bigl(\frac{1}{2}\bigr)^2 = \frac{1}{2}$$; vì $$Z^2 = I$$ nên $$\sigma_Z = \sqrt{1 - (1/2)^2} = \frac{\sqrt{3}}{2} \approx 0.866$$.
   - Với $$X$$: $$\langle X \rangle = 2\cdot\frac{\sqrt{3}}{2}\cdot\frac{1}{2} = \frac{\sqrt{3}}{2}$$; vì $$X^2 = I$$ nên $$\sigma_X = \sqrt{1 - (\sqrt{3}/2)^2} = \frac{1}{2} = 0.5$$.
   - Tích $$\sigma_X\sigma_Z = \frac{\sqrt{3}}{4} \approx 0.433$$.
2. **Kiểm tra vế phải của Robertson $$\frac{1}{2}|\langle [X,Z]\rangle| = |\langle Y\rangle|$$:** Vì $$\psi$$ có hai tọa độ thuần thực còn $$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$ là ma trận thuần ảo phản đối xứng, ta tính ngay $$\langle \psi|Y\psi\rangle = 0$$! Như vậy tại trạng thái này, bất đẳng thức Robertson chỉ nói một điều tầm thường là $$0.433 \ge 0$$ — **cận dưới bị sụp về 0**!
3. **Bây giờ tính entropy Shannon (cơ số 2) cho cùng trạng thái đó:**
   - Phép đo $$Z$$ cho hai kết quả với xác suất $$(3/4,\ 1/4)$$:
     $$
     H(Z) = -\frac{3}{4}\log_2\frac{3}{4} - \frac{1}{4}\log_2\frac{1}{4} \approx 0.811\text{ bit}.
     $$
   - Phép đo $$X$$ (chiếu lên $$|\pm\rangle = \frac{1}{\sqrt{2}}(1, \pm 1)^T$$) cho hai xác suất $$\frac{1 \pm \sqrt{3}/2}{2} \approx (0.933,\ 0.067)$$:
     $$
     H(X) \approx -0.933\log_2(0.933) - 0.067\log_2(0.067) \approx 0.355\text{ bit}.
     $$
   - Tổng $$H(Z) + H(X) \approx 1.166\text{ bit} \ge 1\text{ bit}$$!
4. **Bài học rút ra:** Ngay tại trạng thái mà vế phải của Robertson sụp về $$0$$, bất đẳng thức **Maassen–Uffink** vẫn giữ chặt một cận dưới dương độc lập với trạng thái ($$1\text{ bit}$$)! Đó là lý do các chứng minh bảo mật trong [thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/) và mật mã lượng tử ưu ái dạng bất định entropy.

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
| "Mọi cặp đại lượng đều bất định cỡ $$h/2$$." | Sai | Chỉ các cặp không giao hoán; cận dưới là $$\tfrac12\vert\langle[A,B]\rangle\vert$$. |
| "Năng lượng–thời gian cũng là hệ thức giao hoán như $$x,p$$." | Sai | Không có toán tử thời gian tự liên hợp theo nghĩa chuẩn. Dùng Mandelstam–Tamm hoặc nói rõ biến thể nào. |
| "Bất định là hỗn loạn / định luật 2 nhiệt động học." | Sai | Sự phụ thuộc nhạy vào điều kiện ban đầu và entropy nhiệt là chủ đề khác ([hỗn loạn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/)). |
| "Hàm Gauss chỉ là một ví dụ tiện tính." | Thiếu | Chúng là các hàm **đạt cực tiểu**. |

---

## Tài liệu tham khảo

- 3Blue1Brown — [The more general uncertainty principle](https://www.youtube.com/watch?v=MBnnXbOM5S4) (2018); [trang bài](https://www.3blue1brown.com/lessons/uncertainty-principle/).
- Hall — *Quantum Theory for Mathematicians* (CCR, Robertson, miền).
- Wolff — [The uncertainty principle: variations on a theme](https://arxiv.org/html/2006.11206v3).
- Donoho–Stark — [Uncertainty principles and signal recovery](https://epubs.siam.org/doi/10.1137/0149053), *SIAM J. Appl. Math.* 1989.
- Maassen–Uffink, *Phys. Rev. Lett.* **60** (1988).
- Khóa học: [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / QM]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [QI]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [FUP]({{ site.baseurl }}/contents/vi/chapter06/06_30_Fractal_Uncertainty/), [studio]({{ site.baseurl }}/contents/vi/chapter07/07_13_Explore_Uncertainty_Spectrogram/).
- Gói: `research/video-research/uncertainty-principles/`.
