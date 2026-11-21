---
layout: post
title: "Phân bố: Làm cho Dirac trung thực"
chapter: '03'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

"Hàm $$\delta$$" của Paul Dirac, theo cách hiểu hình thức là bằng vô cùng tại 0, bằng 0 ở mọi nơi khác, và có tích phân bằng 1, đã là công cụ không thể thiếu trong cơ học lượng tử và điện từ học từ rất lâu trước khi nó trở thành một đối tượng hợp lệ của giải tích. Kỹ sư vẫn viết $$\delta(t)$$ cho một xung; nhà vật lý viết $$\langle x|x'\rangle=\delta(x-x')$$. **Lý thuyết phân bố** (còn gọi là hàm suy rộng) của Laurent Schwartz (thập niên 1940–50) biến những thao tác đó thành một mở rộng chặt chẽ của giải tích: mọi hàm khả tích địa phương đều xác định một phân bố, đạo hàm luôn tồn tại theo nghĩa yếu, và phép biến đổi Fourier được mở rộng ra ngoài lớp $$L^1$$ cổ điển.

Đây là bài đầu tiên trong mạch bài Cầu nối về chủ đề "kiểm soát cái vô hạn": **vật lý cần gì, toán học cung cấp gì, và khi thảo luận ta được phép làm gì một cách an toàn**. Nên đọc kèm [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), và [bài tổng quan về vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao $$\delta$$ không phải là một phần tử của $$L^1_{\mathrm{loc}}$$, nhưng vẫn "tác động" được lên các hàm thử trơn.
- Định nghĩa **phân bố** là một phiếm hàm tuyến tính liên tục trên không gian hàm thử (ký hiệu: $$T(\varphi)=\langle T,\varphi\rangle$$).
- Lấy đạo hàm theo nghĩa phân bố: $$\langle T',\varphi\rangle=-\langle T,\varphi'\rangle$$.
- Phát biểu ý chính về biến đổi Fourier của phân bố tăng chậm và giải thích vì sao nó quan trọng với PDE và với các lập luận gần đúng trong lý thuyết trường lượng tử.
- Phân biệt các đẳng thức Dirac hình thức (cần thêm giả thiết) với các đẳng thức phân bố chặt chẽ.
- Hiểu vai trò của phân bố như lớp nền chặt chẽ cho các ký hiệu liên tục trong cơ học lượng tử và lý thuyết trường.

**Kiến thức nền.** Giải tích một biến; tích phân từng phần. Biết giải tích nhiều biến sẽ có ích. Không cần lý thuyết độ đo để theo dõi bài này.

---

## 1. Nhu cầu từ vật lý

Lực xung, điện tích điểm, hàm Green, "trạng thái riêng" của vị trí: tất cả đều vượt quá khả năng của hàm số thông thường. Nếu $$G$$ thỏa mãn $$-\Delta G=\delta$$ trên $$\mathbb{R}^n$$ (theo nghĩa thích hợp), thì tích chập với $$G$$ giải được phương trình Laplace với nhiều loại nguồn khác nhau. Đây là xương sống của lý thuyết thế vị và PDE tuyến tính.

Ký hiệu Dirac giúp viết gọn những điều đó. Cái giá phải trả: theo nghĩa cổ điển, câu "$$\delta$$ là một hàm số" là sai. Cách sửa của toán học là **đổi loại đối tượng**, chứ không cố ép $$\delta$$ vào $$L^1$$.

---

## 2. Hàm thử và phân bố

Cố định một tập mở $$\Omega\subset\mathbb{R}^n$$. **Hàm thử** là các phần tử của $$\mathcal{D}(\Omega)=C_c^\infty(\Omega)$$, tức là các hàm trơn có giá compact. Một **phân bố** $$T\in\mathcal{D}'(\Omega)$$ là một ánh xạ tuyến tính liên tục $$T:\mathcal{D}(\Omega)\to\mathbb{C}$$.

Mọi $$f\in L^1_{\mathrm{loc}}(\Omega)$$ xác định một phân bố chính quy

$$
\langle f,\varphi\rangle = \int_\Omega f(x)\,\varphi(x)\,dx.
$$

Phân bố Dirac tại điểm $$a\in\Omega$$:

$$
\langle \delta_a,\varphi\rangle = \varphi(a).
$$

Phân bố này không cho bởi tích phân với một hàm cổ điển nào, nhưng nó là một phiếm hàm tuyến tính liên tục hoàn toàn hợp lệ.

---

## 3. Đạo hàm luôn tồn tại

Định nghĩa

$$
\langle \partial_i T,\varphi\rangle = -\langle T,\partial_i \varphi\rangle.
$$

Hệ quả: mọi phân bố đều khả vi vô hạn lần theo nghĩa yếu; hàm Heaviside $$H$$ thỏa mãn $$H'=\delta$$; nghiệm yếu của một PDE là nghiệm của phương trình trong $$\mathcal{D}'$$. Đây là ngôn ngữ đứng sau nhiều định lý tồn tại và khái niệm "nghiệm yếu" của phương trình Navier–Stokes ([bài NS]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/)).

**Chuỗi lập luận ngắn.** Nguồn điểm và bước nhảy trở nên hợp lệ khi phép lấy đạo hàm được chuyển sang **hàm thử**, chứ không tác động trực tiếp lên đối tượng kỳ dị.

---

## 4. Phép nhân, tập sóng trước và vùng nguy hiểm

Nhân một phân bố với một hàm trơn là an toàn. Nhân **hai** phân bố bất kỳ với nhau thì không phải lúc nào cũng định nghĩa được ($$\delta^2$$ là ví dụ nổi tiếng). Giải tích vi địa phương (tập sóng trước, wavefront set, của Hörmander) cho biết khi nào tích và phép hạn chế có nghĩa. Đây là lĩnh vực nâng cao mà việc tái chuẩn hóa trong lý thuyết trường lượng tử phải đụng đến khi nhân các phân bố có giá trị toán tử tại cùng một điểm.

**Quy tắc khi thảo luận.** Toán tử tuyến tính với hệ số trơn: an toàn trong khuôn khổ phân bố. Phép toán phi tuyến và tích tại điểm của các đối tượng kỳ dị: cần thêm cấu trúc.

---

## 5. Phân bố tăng chậm và biến đổi Fourier

Trên không gian Schwartz $$\mathcal{S}$$, biến đổi Fourier là một tự đẳng cấu; không gian đối ngẫu $$\mathcal{S}'$$ gồm các **phân bố tăng chậm**, trong đó có đa thức, các hàm tăng không nhanh hơn đa thức, và $$\delta$$. Nhờ vậy biến đổi Fourier áp dụng được cho những đối tượng thô hơn nhiều so với tín hiệu cổ điển ([Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/)).

---

## 6. Ký hiệu trong cơ học lượng tử và lý thuyết trường

Ket vị trí $$|x\rangle$$ và đẳng thức $$\langle x|x'\rangle=\delta(x-x')$$ là các ký hiệu hình thức. Cách hiểu chặt chẽ dùng độ đo phổ, hoặc không gian Hilbert được trang bị (rigged Hilbert space) $$\mathcal{S}\subset L^2\subset\mathcal{S}'$$ ([Hilbert / cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/)).

Trong lý thuyết trường lượng tử, các phân bố Wightman và tích sắp xếp theo thời gian cũng được viết bằng ngôn ngữ phân bố. Khó khăn giải tích thường nằm ở việc **định nghĩa các phiếm hàm phi tuyến** (tái chuẩn hóa); xem [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/) và [nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/).

---

## 7. Phân biệt chính xác và cường điệu

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "$$\delta$$ là hàm bằng vô cùng tại 0." | Chỉ là cách nói gần đúng | $$\delta$$ là một phân bố, không phải hàm số cổ điển. |
| "Lý thuyết phân bố làm cho mọi tính toán hình thức của vật lý trở nên chặt chẽ." | Sai | Phép nhân và các phép toán phi tuyến có thể không xác định. |
| "Nghiệm yếu là nghiệm giả." | Gây hiểu nhầm | Đó là nghiệm theo một nghĩa đối ngẫu chính xác; tính duy nhất và độ trơn là những câu hỏi riêng. |
| "Kỹ sư dùng $$\delta$$ là thiếu toán học." | Không công bằng | Phép tính với xung được biện minh bằng lý thuyết phân bố (hoặc biến đổi Laplace) với các giả thiết được nêu rõ. |

---

## Bài tập

1. **Định nghĩa.** Viết không quá 80 từ định nghĩa $$\delta_0$$ như một phiếm hàm, không phải như một đồ thị.  
2. **Hàm Heaviside.** Dùng định nghĩa đạo hàm theo nghĩa phân bố, chứng minh $$H'=\delta$$ trên $$\mathbb{R}$$.  
3. **Fourier.** Vì sao câu "biến đổi Fourier của $$\delta$$ bằng 1" có nghĩa trong $$\mathcal{S}'$$?  
4. **Sửa câu sai.** Viết lại câu: "Dirac bịa ra một hàm không hợp lệ mà vật lý vẫn dùng, nên vật lý mâu thuẫn."  
5. **Cầu nối.** Viết một đoạn nối lý thuyết phân bố với nghiệm yếu của PDE, hoặc với ký hiệu vị trí trong cơ học lượng tử.

---

## Tài liệu tham khảo

1. Strichartz — *A Guide to Distribution Theory and Fourier Transforms*.  
2. Khóa học: [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / QM]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).  
