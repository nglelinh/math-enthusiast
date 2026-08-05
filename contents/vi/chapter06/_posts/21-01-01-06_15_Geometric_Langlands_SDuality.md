---
layout: post
title: "Geometric Langlands & S-Duality (Deep Dive)"
chapter: '06'
order: 15
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: deep-dive
---

**Geometric Langlands** là chương trình đối ngẫu trong toán thuần túy: các category sheaf trên moduli bundle $$G$$ trên một đường cong tương ứng với dữ liệu spectral / local system cho **nhóm dual Langlands** $$G^\vee$$. Độc lập, vật lý phát triển **S-duality** (đối ngẫu điện–từ / mạnh–yếu) cho lý thuyết gauge supersymmetric bốn chiều, cũng đổi $$G$$ với $$G^\vee$$. **Kapustin–Witten (2006)** đề xuất geometric Langlands là bóng toán của S-duality của $$\mathcal N=4$$ super Yang–Mills bị twist, compact hóa trên mặt Riemann—với **mirror symmetry của hệ Hitchin** như động cơ hình học.

Deep dive nằm ở giao của:

- [Đối ngẫu như một nguyên lý]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)  
- [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) (chương trình số học; nhóm dual)  
- [Mirror symmetry]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) (văn hóa SYZ Hitchin)

**Đừng** nhầm Fundamental Lemma của Ngô với “Langlands xong,” hay dictionary vật lý với chứng minh đầy đủ mọi correspondence hình học.

Gói: `research/video-research/geometric-langlands-sduality/`.

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- Tách Langlands **số học** khỏi Langlands **hình học** (đối tượng và trường nền khác; tinh thần nhóm dual chung).
- Phát biểu geometric Langlands mức slogan: sheaf trên $$\mathrm{Bun}_G(C)$$ ↔ dữ liệu spectral cho $$G^\vee$$.
- Giải thích **S-duality** của $$\mathcal N=4$$ SYM như mạnh/yếu và $$G\leftrightarrow G^\vee$$.
- Phác bức tranh compact hóa **Kapustin–Witten** (lý thuyết 4d trên $$C\times\Sigma$$ → sigma model 2d / category brane).
- Nối **hệ Hitchin** của $$G$$ và $$G^\vee$$ với mirror symmetry.
- Giữ trạng thái trung thực; coi vật lý là **cầu và muse**, không phải chứng minh tự động.

**Tiên quyết.** Nguyên lý đối ngẫu; tổng quan Langlands Ch.2. Nhóm reductive và moduli stack xuất hiện như tên trước.

---

## 1. Hai thế giới Langlands

| | Langlands số học | Langlands hình học |
|--|------------------|--------------------|
| Nền | Trường số / adele | Đường cong đại số (thường trên $$\mathbb{C}$$) |
| Phía automorphic | Biểu diễn automorphic của $$G(\mathbb{A})$$ | Sheaf / D-module trên $$\mathrm{Bun}_G(C)$$ |
| Phía Galois / spectral | Biểu diễn Galois | Local system / Higgs / spectral cover cho $$G^\vee$$ |
| Nhóm dual | $$G^\vee$$ | $$G^\vee$$ |
| Công cụ nổi | Trace formula, endoscopy, $$L$$-hàm | Hecke eigensheaf, derived category, Hitchin |

**Công trình Fields của Ngô** mở Fundamental Lemma cho **so sánh endoscopic** trong máy trace formula số học—đó *không* phải chứng minh correspondence hình học đầy đủ, và *không* phải “chương trình Langlands xong.”

---

## 2. Slogan geometric Langlands

Cố định đường cong xạ ảnh trơn $$C$$ và nhóm reductive $$G$$. Gần đúng:

> Các category sheaf (phù hợp) trên stack moduli $$\mathrm{Bun}_G(C)$$ dual với category dựng từ $$G^\vee$$-local system (hoặc dữ liệu spectral liên quan) trên $$C$$.

Dạng cổ điển nhấn **Hecke eigensheaf**: sheaf là eigenvector của toán tử Hecke với eigenvalue cho bởi local system của $$G^\vee$$. Diễn đạt hiện đại dùng hình học đại số derived và tương đương category tinh chỉnh; phát biểu tiến hóa theo tài liệu.

**Sư phạm.** Nhớ **hình dạng**—hình học automorphic của $$G$$ dual hình học spectral của $$G^\vee$$—không định nghĩa stack đầy đủ.

---

## 3. S-duality trong lý thuyết gauge

**Maxwell** đã có dualty điện–từ. **Montonen–Olive** và sau đưa lên **S-duality** không giao hoán: coupling mạnh map sang yếu của lý thuyết dual, nhóm gauge thay bằng **Langlands dual** $$G^\vee$$.

Với $$\mathcal N=4$$ SYM bốn chiều, S-duality đặc biệt sắc: coupling $$\tau$$ biến đổi dưới kiểu $$\mathrm{SL}(2,\mathbb{Z})$$, và các lý thuyết dual chia sẻ phổ BPS trong chế độ kiểm soát.

---

## 4. Cầu Kapustin–Witten

**Kapustin–Witten** (arXiv:hep-th/0604151) lập luận, gần đúng:

1. Bắt đầu từ phiên bản twist tôpô của $$\mathcal N=4$$ SYM 4d với nhóm $$G$$.  
2. Compact hóa trên mặt Riemann $$C$$ (đường cong của geometric Langlands).  
3. Lý thuyết hiệu dụng liên quan sigma model trên moduli Higgs / Hitchin—và **category brane** trên các không gian đó.  
4. **S-duality** của lý thuyết 4d trở thành dualty của các category 2d, khớp geometric Langlands cho $$G$$ và $$G^\vee$$.  
5. Dọc đường, **mirror symmetry** của hệ Hitchin (A-brane ↔ B-brane) xuất hiện như động cơ hình học—nối bài này với deep dive mirror.

**Biết đọc.** Đây là **dictionary và động lực từ vật lý** định hình chương trình nghiên cứu toán. Không thay chứng minh toán học thuần túy.

---

## 5. Hệ Hitchin như mirror

**Fibration Hitchin** trình bày moduli Higgs bundle như hệ tích phân trên base đa thức đặc trưng. Với nhóm dual $$G$$ và $$G^\vee$$, sợi là abelian variety dual (generic)—cặp **mirror kiểu SYZ** (Hausel–Thaddeus và liên quan). Vậy:

```text
S-duality (gauge 4d)
    ↓ compact hóa
Mirror symmetry của hệ Hitchin
    ↓ category brane
Geometric Langlands correspondence
```

Sơ đồ đó là trái tim seminar của văn hóa Kapustin–Witten.

---

## 6. Bản đồ trạng thái (2026)

| Phát biểu | Nhãn |
|-----------|------|
| Nhóm dual tổ chức chương trình số học & hình học | Nguyên lý thiết kế đã ổn định |
| Fundamental Lemma (Ngô et al.) | **Định lý** (công cụ endoscopy số học) |
| Geometric Langlands (các diễn đạt) | Tiến bộ lớn; vẫn là chương trình sống |
| Dictionary Kapustin–Witten | Ảnh hưởng lớn; cầu vật lý ↔ toán |
| Functoriality Langlands số học đầy đủ | Phần lớn **mở** |

---

## 7. Bản đồ khóa học

| Bài | Liên kết |
|-----|----------|
| [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/) | Chương trình số học + Fundamental Lemma |
| [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/) | Bản đồ cha |
| [Mirror symmetry]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) | HMS / SYZ; mirror Hitchin |
| [AdS/CFT]({{ site.baseurl }}/contents/vi/chapter06/06_14_AdS_CFT/) | Dualty khác (holography) |
| [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/) | Văn hóa chỉ số / lớp đặc trưng |
| [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/) | Hạ tầng phân tích gauge |

---

## 8. Nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Geometric = arithmetic Langlands.” | Cùng tinh thần nhóm dual; đối tượng toán khác. |
| “Ngô chứng geometric Langlands.” | Ngô: Fundamental Lemma cho endoscopy / trace formula. |
| “Vật lý chứng minh Langlands.” | Vật lý cho dictionary S-duality; toán chứng phát biểu toán. |
| “S-duality chỉ có string.” | Sống trong QFT ($$\mathcal N=4$$ SYM) trước full string. |
| “Hitchin = HMS cho mọi CY.” | Mirror Hitchin là họ hình học then chốt đặc biệt. |

---

## Bài tập

1. Hai cột: Langlands số học vs hình học—nền, đối tượng, nhóm dual.  
2. Geometric Langlands ≤3 câu.  
3. S-duality đổi gì (coupling và nhóm)?  
4. Phác compact hóa Kapustin–Witten 4 gạch đầu dòng.  
5. Vì sao hệ Hitchin $$G$$ / $$G^\vee$$ quan trọng với mirror?  
6. **≤150 từ:** Vì sao “cầu, không chứng minh” đúng cho vật lý → geometric Langlands?  
7. **Tuỳ chọn:** Mở abstract Kapustin–Witten; năm từ khóa.

---

## Nguồn video

Gói: `research/video-research/geometric-langlands-sduality/`.

1. **Core** — Kapustin: [https://www.youtube.com/watch?v=oJRD3PshFjY](https://www.youtube.com/watch?v=oJRD3PshFjY)  
2. **Core** — Gukov: [https://www.youtube.com/watch?v=bCpVL6flCxo](https://www.youtube.com/watch?v=bCpVL6flCxo)  
3. **Orientation** — Frenkel: [https://www.youtube.com/watch?v=8Pkw25J-Bg0](https://www.youtube.com/watch?v=8Pkw25J-Bg0)  
4. **Bridge** — Witten: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo)  

URL đầy đủ: `research/video-research/geometric-langlands-sduality/references.md`.

---

## Tài liệu tham khảo

1. Kapustin–Witten — https://arxiv.org/abs/hep-th/0604151  
2. Frenkel — https://arxiv.org/abs/hep-th/0512172  
3. Gukov–Witten — https://arxiv.org/abs/hep-th/0612073  
4. Hausel–Thaddeus — https://arxiv.org/abs/math/0205236  
5. Khóa: [Langlands / Ngô]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/)  
6. Gói: `research/video-research/geometric-langlands-sduality/`  
