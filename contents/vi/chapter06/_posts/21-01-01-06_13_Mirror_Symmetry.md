---
layout: post
title: "Mirror Symmetry (Deep Dive)"
chapter: '06'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: deep-dive
---

**Mirror symmetry** bắt đầu như bất ngờ của lý thuyết dây: hai không gian Calabi–Yau trông khác nhau về hình học phức và symplectic có thể cho **cùng dự đoán vật lý**. Toán học hấp thụ bất ngờ đó thành hai chương trình lớn—**homological mirror symmetry (HMS)** và bức tranh hình học **Strominger–Yau–Zaslow (SYZ)**—cùng mạng dualty enumerative. Deep dive này mở rộng slogan trong [Đối ngẫu như một nguyên lý]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/); **không** chứng minh HMS hay dựng mirror bằng tay.

**Lộ trình:** nguồn vật lý → mô hình A/B → lật Hodge / enumerative → SYZ như hình học T-duality → HMS (Kontsevich) → bản đồ trạng thái → cầu Langlands → bài tập.

Gói: `research/video-research/mirror-symmetry/`.

---

## Mục tiêu học tập

Sau bài này bạn có thể:

- Phát biểu **slogan vật lý** của mirror symmetry và tách **A-model / B-model** toán học.
- Giải thích trực giác **Hodge diamond** (số moduli phức vs Kähler đổi vai).
- Phân biệt **SYZ** (T-duality hình học của fibration torus) với **HMS** (tương đương category).
- Gắn nhãn trạng thái trung thực: đảo định lý vs chương trình mở (**tính đến 2026**).
- Nối mirror với T-duality và geometric Langlands / Hitchin dual ở mức slogan.
- Tránh khẳng định “string theory chứng minh hết hình học đại số.”

**Tiên quyết.** Bài nguyên lý đối ngẫu; quen tên “đa tạp phức” và “dạng symplectic.” Derived category và Floer chỉ ở mức slogan.

---

## 1. Ý tưởng từ đâu?

Cuối thập niên 1980–90, compactification string trên Calabi–Yau ba chiều dự đoán các lý thuyết worldsheet gắn hình học khác nhau cho cùng correlator. Sự khớp gợi **mirror map**: moduli cấu trúc phức của $$X$$ cặp với moduli Kähler của dual $$\check X$$ và ngược lại. Đếm đường cong chỉnh hình một phía khớp tích phân period / variation of Hodge structure phía kia—đòn bẩy tính toán đáng kinh ngạc.

Toán hỏi: *định lý nào ẩn dưới dictionary vật lý?* Hai câu trả lời thống trị văn hóa hiện đại.

---

## 2. A-model và B-model

| Mặt | Hình học nhấn | Dữ liệu điển hình |
|-----|---------------|-------------------|
| **A-model** | Cấu trúc symplectic của $$X$$ | Đường cong giả chỉnh hình; bất biến Gromov–Witten; **Fukaya category** của Lagrangian + Floer |
| **B-model** | Cấu trúc phức của $$\check X$$ | Bundle / sheaf chỉnh hình; **derived category** $$D^b\mathrm{Coh}(\check X)$$; tích phân period |

Mirror symmetry (dạng tinh chỉnh) khẳng định A-data của $$X$$ bằng B-data của $$\check X$$. Đó là **đối ngẫu hình học**, không phải đối xứng liên tục của một đa tạp.

**Slogan Calabi–Yau.** Đa tạp phức với canonical bundle tầm thường (vật lý thường còn muốn metric Kähler Ricci-phẳng). Cặp mirror không cần diffeomorphic; cần khớp dữ liệu dual.

---

## 3. Số Hodge và đòn bẩy enumerative

Với CY ba chiều, mirror cổ điển đổi số Hodge theo mẫu đặc trưng (ví dụ $$h^{1,1}(X)$$ với $$h^{2,1}(\check X)$$)—**lật kim cương Hodge**. Sâu hơn, hàm sinh Gromov–Witten genus 0 một phía khớp Yukawa / period phía kia sau mirror map tọa độ.

**Sư phạm.** Không cần tính một GW invariant. Cần **hình dạng**: đếm đường cong khó ↔ tích phân dạng chỉnh hình sau đổi biến.

---

## 4. SYZ — mirror như T-duality

**Strominger–Yau–Zaslow (1996)** đề xuất cơ chế hình học: cả $$X$$ và $$\check X$$ fibration trên cùng base bởi torus **special Lagrangian**, sợi mirror là torus dual (T-duality theo sợi). Sợi kỳ dị mang monodromy và dữ liệu discriminant then chốt.

| Sức mạnh SYZ | Khó của SYZ |
|--------------|-------------|
| Giải thích *vì sao* mirror tồn tại như dual torus bundle | Fibration special Lagrangian trơn toàn cục cực khó dựng |
| Nối T-duality vật lý | Cần diễn đạt tinh chỉnh (thường algebro-geometric)—Gross–Siebert, … |

**Trạng thái.** SYZ là **chương trình nghiên cứu**, không phải một định lý đóng cho mọi CY. Case địa phương / toric hiểu tốt hơn; bức tranh trơn toàn cục vẫn mong manh.

---

## 5. Homological mirror symmetry (Kontsevich)

**Kontsevich (1994)** nâng khớp enumerative thành phát biểu category—**HMS**:

$$
D^\pi\mathrm{Fuk}(X)\;\simeq\; D^b\mathrm{Coh}(\check X)
$$

(các biến thể: hoàn thành Karoubi, mô hình Landau–Ginzburg, wrapped Fukaya, …). Đối tượng A-side: Lagrangian + local system; morphism: đối đồng điều Floer. B-side: phức sheaf chỉnh hình; morphism: Ext.

**Vì sao là nguyên lý đối ngẫu.** Cả **homological algebra** khớp—mọi định lý diễn đạt được ở một derived category có song sinh dual. Case đặc biệt (đường cong elliptic, Fano toric, một số local CY, …) **đã chứng**; giả thuyết tổng quát vẫn mở.

---

## 6. Bản đồ trạng thái (đừng bỏ)

| Phát biểu | Nhãn (2026) |
|-----------|-------------|
| Nhiều dualty enumerative / mirror map cho họ cụ thể | Định lý / đã ổn định |
| HMS cho nhiều lớp ví dụ | Các đảo định lý |
| HMS đầy đủ cho CY tổng quát | Chương trình mở |
| Fibration SYZ trơn toàn cục | Mở / chương trình tinh chỉnh |
| Dự đoán từ vật lý | Muse + dictionary; toán vẫn phải chứng |

---

## 7. Cầu nối khóa học

| Láng giềng | Liên kết |
|------------|----------|
| [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/) | Bản đồ cha |
| [AdS/CFT]({{ site.baseurl }}/contents/vi/chapter06/06_14_AdS_CFT/) | Văn hóa dualty vật lý khác (holography) |
| [Geometric Langlands & S-duality]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) | Hệ Hitchin $$G$$ / $$G^\vee$$ là mirror kiểu SYZ |
| [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) | Giao diện gauge / string |
| [Pardon / symplectic]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) | Văn hóa hình học symplectic |

---

## 8. Nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Mirror = cùng đa tạp viết hai lần.” | Cặp có thể khác tôpô; *dữ liệu* dual khớp. |
| “HMS chỉ là số Hodge.” | Hodge là bóng cổ điển; HMS là categorical. |
| “SYZ đã chứng đầy đủ.” | Chương trình với kết quả từng phần. |
| “T-duality = mirror luôn.” | SYZ đề xuất T-duality như cơ chế; không mọi dual là compact circle. |
| “Vật lý đã xong phần toán.” | Vật lý cho dictionary; chứng minh là toán. |

---

## Bài tập

1. Một đoạn: đối chiếu A-model và B-model.  
2. Lật Hodge diamond mua gì về tính toán?  
3. Phát biểu SYZ ≤3 câu; nêu một khó khăn.  
4. Viết slogan HMS như tương đương category (informal OK).  
5. **≤150 từ:** Vì sao mirror là *đối ngẫu* theo bài nguyên lý?  
6. Biết đọc trạng thái: một đảo định lý + một chương trình mở.  
7. **Tuỳ chọn:** Lướt abstract Auroux về Fukaya; liệt kê ba từ mới.

---

## Mode C — ghi chú tái dựng từ video flagship

*Tái dựng từ auto-caption Witten (Fields Medal Symposium 2012). Caption: `research/video-research/mirror-symmetry/transcripts/`. Units: `knowledge_units_mode_c.json`. Tái dựng; không dán ASR.*

### C1. Vì sao geometric Langlands “muốn” chiều 4

Witten nối ngôn ngữ **mirror symmetry** với **geometric Langlands**. QFT chiều $$d$$ gán **category điều kiện biên** cho đa tạp đóng chiều $$d-2$$. Geometric Langlands gán category cho **mặt Riemann** (2-đa tạp), nên $$d=4$$: bắt đầu từ lý thuyết bốn chiều.

### C2. $$\mathcal N=4$$ SYM là lý thuyết tự nhiên

Trong gauge 4d, lý thuyết supersymmetry tối đa—**$$\mathcal N=4$$ super Yang–Mills**—là ngôi nhà tự nhiên. Nhóm gauge $$G$$ và dual xuất hiện qua dualty; các “đối xứng lẻ” supersymmetric cung cấp vi phân đóng gói cấu trúc category.

### C3. Văn hóa mirror + Hitchin (không phải chứng minh)

Talk trộn **mirror symmetry** (brane, hình học dual) với dữ liệu **Hitchin / moduli bundle** nuôi geometric Langlands. Cho khóa này: **khí hậu nghiên cứu và dictionary**—không chứng minh bảng HMS/GLC đầy đủ. Ghép [Geometric Langlands & S-duality]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/) và [Witten mini]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/).

### C4. Vệ sinh caption

- **Witten `S02ghGCdNDo`:** đã extract EN auto-caption (2026-08-05).  
- **Chan HMS/SYZ `Kz6Dj8KSFjM`:** không có subtitle—chỉ xem hình; không bịa Mode-C từ ASR thiếu.

---

## Nguồn video (gói nghiên cứu)

Hướng định hướng, không thay survey. Gói: `research/video-research/mirror-symmetry/`.

1. **Định hướng / Mode C** — Witten: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo) · caption trong pack  
2. **Core (không caption)** — Chan HMS via SYZ: [https://www.youtube.com/watch?v=Kz6Dj8KSFjM](https://www.youtube.com/watch?v=Kz6Dj8KSFjM)  
3. **Research** — Zaslow: [https://www.youtube.com/watch?v=Y3-sw3tjZiU](https://www.youtube.com/watch?v=Y3-sw3tjZiU)  
4. **Notes** — MIT OCW Mirror Symmetry: [https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/](https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/)  

URL đầy đủ: `research/video-research/mirror-symmetry/references.md`.  
Trạng thái transcript: `research/video-research/mirror-symmetry/TRANSCRIPT_STATUS.md`.

---

## Tài liệu tham khảo

1. Kontsevich — https://arxiv.org/abs/alg-geom/9411018  
2. Strominger–Yau–Zaslow — https://arxiv.org/abs/hep-th/9606040  
3. Gross — SYZ survey — https://arxiv.org/abs/1212.4220  
4. Auroux — Fukaya — https://arxiv.org/abs/1301.7056  
5. Hori et al. — *Mirror Symmetry* (Clay)  
6. Wikipedia — Homological mirror symmetry; SYZ  
7. Gói: `research/video-research/mirror-symmetry/`  
