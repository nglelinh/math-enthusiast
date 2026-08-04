---
layout: post
title: "Hopcroft, Tarjan và Thuật toán Đồ thị (Turing 1986)"
chapter: '09'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**John E. Hopcroft** và **Robert E. Tarjan** nhận **A.M. Turing Award 1986**

> “for fundamental achievements in the design and analysis of algorithms and data structures.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Nếu Cook–Karp dạy ta *độ khó*, Hopcroft–Tarjan dạy ta *cái vẫn làm được—và làm nhanh có cấu trúc*. DFS không chỉ “duyệt đồ thị trong giáo trình năm nhất”: với **đúng metadata** (discovery time, low-link, stack), nó tách thành phần liên thông mạnh, tìm khớp cầu/khớp, kiểm tra planar, dựng cây bao trùm có thứ tự. Tarjan gắn với **union–find**, **splay**, **Fibonacci heap** văn hóa amortized analysis. Hopcroft gắn với automata, matching, planarity, và chuẩn “phân tích thuật toán nghiêm”. Bài này là chân dung **thuật toán đồ thị như toán rời rạc hiệu quả**, cầu [đồ thị & mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) và [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/).

---

## Mục tiêu học tập

Sau bài, bạn có thể mô tả **DFS** như quy nạp trên cây đệ quy + cạnh back/forward/cross và giải thích vì sao timestamps cho phép suy cấu trúc; phác thuật toán **Tarjan** (hoặc Kosaraju) tìm **SCC** (strongly connected components) trong $$O(n+m)$$; nêu ý **cầu (bridge)** / **khớp (articulation point)** qua giá trị low; giải thích **planarity testing** tuyến tính như thành tựu “cấu trúc phẳng = thuật toán gần tối ưu”; mô tả **union–find** với union by rank + path compression và bound gần $$\alpha(n)$$ (hàm ngược Ackermann); nối amortized analysis với thiết kế cấu trúc dữ liệu hiện đại mà không nhầm “amortized = trung bình ngẫu nhiên”.

**Kiến thức nền.** Đồ thị có hướng/vô hướng; danh sách kề; $$O$$-notation. Biết BFS/DFS mức nhập môn là đủ để nâng cấp.

---

## 1. Vì sao Turing 1986 là giải “thuật toán”

Giữa thập niên 1970–80, CS lý thuyết tách rõ hai cực: **NP-đầy đủ** (bạn không kỳ vọng poly-time tổng quát) và **thuật toán đa thức tinh xảo** (bạn *có* poly-time—và có thể gần tuyến tính). Hopcroft–Tarjan đứng cực thứ hai với chuẩn chứng minh runtime và correctness sắt đá. Citation không nói “một app”; nói **design and analysis**—phương pháp.

Math Enthusiast cần cả hai cực. [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) giải thích tường; Hopcroft–Tarjan giải thích **cửa sổ ánh sáng** nơi đồ thị chịu thuật toán đẹp. Thực hành phần mềm (compiler, mạng, GIS, verification) sống nhờ cửa sổ đó nhiều hơn nhờ slogan NP.

---

## 2. DFS nâng cao: không chỉ “thăm đỉnh”

### Cạnh và thời gian

Chạy DFS trên đồ thị có hướng, gán $$d[v]$$ (discovery) và $$f[v]$$ (finish). Phân loại cạnh:

- **Tree edges** — rừng DFS.  
- **Back edges** — tới tổ tiên; chứng tỏ chu trình.  
- **Forward / cross** — tinh chỉnh theo intervals $$[d,f]$$.

Định lý parenthesis: các interval $$[d[v],f[v]]$$ hoặc lồng nhau hoặc rời. Đây là **cấu trúc thứ tự toàn cục** miễn phí từ một lần duyệt $$O(n+m)$$.

### Low-link và cầu/khớp

Trên vô hướng, $$\mathrm{low}[v]$$ theo dõi discovery nhỏ nhất chạm được từ subtree $$v$$ qua tối đa một back edge. So sánh $$\mathrm{low}$$ với $$d$$ của cha cho phép nhận diện:

- **Cầu:** cạnh cây mà subtree không chạm ngược trên cha.  
- **Khớp:** đỉnh mà việc xóa làm tăng số thành phần liên thông—đặc trưng bằng con có $$\mathrm{low}$$ không đủ nhỏ.

Công thức không cần thuộc máy; cần thuộc **ý**: DFS + một vài số nguyên phụ = chứng nhận cấu trúc cắt.

---

## 3. Thành phần liên thông mạnh (SCC)

Đồ thị có hướng phân hoạch thành SCC: trong mỗi khối, mọi cặp đỉnh tới được nhau; đồ thị co các khối thành DAG. **Tarjan’s SCC algorithm** dùng một DFS, stack các đỉnh “đang mở”, và low-link để pop đúng một SCC khi root của component finish. **Kosaraju**: hai DFS (một trên đồ thị ngược) cũng $$O(n+m)$$, dễ dạy hơn, hằng số khác.

Vì sao quan trọng toán–CS:

- Mọi path queries “tồn tại đường” giảm về reachability trên DAG của SCC.  
- Model checking, dependency analysis, game graphs dùng SCC như preprocess.  
- Đây là ví dụ **cấu trúc toàn cục từ duyệt địa phương**—họ hàng tinh thần với [Euler Königsberg]({{ site.baseurl }}/contents/vi/chapter05/05_05_Euler_Konigsberg/): topology tổ hợp + thuật toán.

---

## 4. Planarity: phẳng hóa như bài toán tuyến tính

### Câu hỏi

Cho đồ thị đơn $$G=(V,E)$$, $$|V|=n$$, có nhúng mặt phẳng không cắt cạnh? Kuratowski/Wagner cho đặc trưng cấm $$K_5,K_{3,3}$$ minors—đẹp lý thuyết nhưng naive search minor không phải thuật toán tuyến tính hiển nhiên.

### Hopcroft–Tarjan planarity

Họ cho thuật toán **$$O(n)$$** kiểm tra planarity (và có thể dựng nhúng), dựa DFS và quản lý trật tự cạnh quanh đỉnh—kỹ thuật “paths và conflicts” cổ điển. Thông điệp sâu:

> **Tính chất tôpô tổ hợp “phẳng” có chứng nhận thuật toán gần đọc input.**

So với tô màu 4 sắc (chứng minh phức tạp, thuật toán poly nhưng khác câu chuyện) hay isomorphism đồ thị (lịch sử dài), planarity là chiến thắng **cấu trúc ⇒ tốc độ**. GIS, VLSI, vẽ đồ thị thừa hưởng.

### Trực giác tại sao $$O(n)$$ khả dĩ

Đồ thị phẳng đơn có $$m\le 3n-6$$ ($$n\ge 3$$) bởi Euler. Input đã thưa; thuật toán tận dụng thứ tự DFS để không trả giá $$n^2$$ so khớp. Thưa + thứ tự = bạn đồng minh runtime.

---

## 5. Union–find và amortized analysis

### Bài toán

Quản lý phân hoạch động: $$\mathrm{Find}(x)$$ trả đại diện lớp; $$\mathrm{Union}(x,y)$$ gộp lớp. Ứng dụng: Kruskal MST, processing equivalence, dynamic connectivity thô.

### Rank + path compression

Union by rank (hoặc size) giữ cây nông; path compression làm phẳng đường Find. Phân tích **amortized**: chuỗi $$m$$ thao tác trên $$n$$ phần tử tốn $$O(m\,\alpha(n))$$ với $$\alpha$$ ngược Ackermann—thực tế $$\alpha(n)\le 4$$ cho $$n$$ vũ trụ. Đây không phải “trung bình ngẫu nhiên input”; amortized là **kế toán chi phí** trên worst-case sequence.

Tarjan là tên gắn với phân tích tinh và nhiều cấu trúc (cũng gồm công trình về offline LCA, dominators, …). Văn hóa **potential method** trong sách CLRS mang dấu ấn dòng này.

### Fibonacci heaps (văn hóa)

Decrease-key amortized rẻ nuôi Dijkstra $$O(m+n\log n)$$ cổ điển với heap phù hợp—câu chuyện “cấu trúc dữ liệu tinh chỉnh hằng số và term log”. Dù thực hành hay dùng binary heap, *ý tưởng amortized* vẫn là di sản.

---

## 6. Hopcroft: automata, matching, chuẩn phân tích

Ngoài planarity và algorithms chung, Hopcroft nổi với:

- **Minimization DFA** Hopcroft: phân hoạch refine $$O(n\log n)$$—algorithmic automata theory.  
- **Matching** và thuật toán đồ thị hai phía (văn hóa Hopcroft–Karp $$O(E\sqrt{V})$$ cho bipartite matching).  
- Sách và chuẩn sư phạm: thuật toán không chỉ code mà **chứng minh invariant + runtime**.

Matching hai phía nối [tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) và lý thuyết đồ thị: luồng, dual, chứng nhận tối ưu. Turing 1986 là giải cho *phong cách* đó lan tỏa.

---

## 7. Amortized ≠ average-case; online ≠ offline

| Khái niệm | Nghĩa |
|-----------|--------|
| Worst-case một thao tác | Có thể đắt (Find nén cả chuỗi) |
| Amortized | Trung bình chi phí trên *chuỗi* adversarial |
| Average-case | Kỳ vọng trên phân phối input ngẫu nhiên |
| Randomized | Xu nội bộ thuật toán |

Nhầm amortized với average-case là lỗi phổ biến. Path compression *đắt đơn lẻ* vẫn *rẻ amortized*. Đây là toán kế toán, họ hàng potential trong vật lý nhiều hơn họ hàng Monte Carlo.

---

## 8. Đồ thị thuật toán sau Hopcroft–Tarjan

Di sản mở rộng (không gán nhầm mọi thứ cho hai ông):

- **Min-cut / max-flow** hiện đại (push-relabel, Dinic, near-linear randomized undirected cut…).  
- **Dynamic graphs** fully dynamic connectivity—vẫn nghiên cứu sôi.  
- **Fine-grained** APSP, diameter—chặn dưới có điều kiện trong P; xem [chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/).  
- **Spectral và random walks** — cầu [expander / Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).

Hopcroft–Tarjan cho chuẩn: trước khi claim “AI giải đồ thị”, hãy hỏi đã có thuật toán cấu trúc $$O(n+m)$$ chưa, hay đang heuristic instance NP-khó.

### Topological order và DAG sau SCC

Co mỗi SCC thành một đỉnh: đồ thị kết quả là DAG. Trên DAG, DFS finish times cho **topological order**; scheduling, dependency install, build systems dựa vào đó. Pipeline điển hình: (1) SCC; (2) co; (3) topo sort; (4) DP trên thứ tự. Đây là mẫu “cấu trúc toàn cục → thuật toán tuyến tính theo $$n+m$$” lặp đi lặp lại trong systems.

### Correctness culture

Papers Hopcroft–Tarjan-era viết invariant rõ: stack chứa gì, low thỏa bất biến nào lúc pop. Khi code graph bug, thường do **không giữ invariant** chứ không do “big-O sai”. Seminar algorithms nên luyện: nêu loop invariant một câu trước khi tối ưu micro.

---

## 9. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “DFS chỉ để in thứ tự thăm.” | Còn SCC, cầu, planarity scaffold, topological trên DAG… |
| “Planarity NP-khó.” | Kiểm tra planarity ∈ P; thậm chí tuyến tính. |
| “Amortized = trung bình random.” | Kế toán worst-case sequence. |
| “Union–find $$O(1)$$ thật sự.” | $$O(\alpha(n))$$ amortized—thực tế hằng nhưng lý thuyết tinh. |
| “Thuật toán đồ thị = ML trên graph.” | Graph ML khác dòng combinatorial algorithms cổ điển. |
| “Turing 1986 giải P vs NP.” | Không; vinh danh design & analysis hiệu quả. |

---

## Bài tập

1. Trên đồ thị có hướng nhỏ (5–6 đỉnh), chạy DFS tay; gán $$d,f$$; liệt kê SCC.  
2. Định nghĩa cầu; giải thích một câu low-link phát hiện cầu.  
3. Chứng minh phác: đồ thị phẳng đơn $$n\ge 3$$ có $$m\le 3n-6$$ (Euler).  
4. Mô tả path compression; đưa ví dụ Find đắt một lần nhưng chuỗi rẻ.  
5. **≤200 từ:** So Kosaraju và Tarjan SCC—giống output, khác kỹ thuật.  
6. Nối [đồ thị mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/): một ứng dụng SCC hoặc cầu trong mạng thật (dependency, single point of failure).  
7. **Seminar:** Đọc Hopcroft–Karp abstract-level; so brute bipartite matching $$O(VE)$$.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/hopcroft-tarjan/`.

**Khẩu hiệu từ gói nghiên cứu**

- Hopcroft & Tarjan Turing 1986: thuật toán đồ thị nền tảng.

**Thứ tự xem gợi ý**


**Cổng chính thức / tài liệu**

- Hopcroft Turing: https://amturing.acm.org/award_winners/hopcroft_1053917.cfm  
- Tarjan Turing: https://amturing.acm.org/award_winners/tarjan_1092048.cfm  

Danh mục URL đầy đủ: `research/video-research/hopcroft-tarjan/references.md`.

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/hopcroft-tarjan/references.md`.

1. Hopcroft Turing — https://amturing.acm.org/award_winners/hopcroft_1053917.cfm  
2. Tarjan Turing — https://amturing.acm.org/award_winners/tarjan_1092048.cfm  
3. Wikipedia — John Hopcroft — https://en.wikipedia.org/wiki/John_Hopcroft  
4. Wikipedia — Robert Tarjan — https://en.wikipedia.org/wiki/Robert_Tarjan  
5. Wikipedia — Hopcroft–Tarjan algorithm (planarity) — https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Tarjan_planarity_test  
6. Wikipedia — Depth-first search — https://en.wikipedia.org/wiki/Depth-first_search  
7. Wikipedia — Union–find / disjoint set (Tarjan) — https://en.wikipedia.org/wiki/Disjoint-set_data_structure  
8. Hopcroft–Ullman automata book culture — https://en.wikipedia.org/wiki/Introduction_to_Automata_Theory,_Languages,_and_Computation  
9. Thư mục gói: `research/video-research/hopcroft-tarjan/`.

1. ACM Turing Award — Hopcroft & Tarjan (1986).  
2. Cormen, Leiserson, Rivest, Stein — *Introduction to Algorithms* (DFS, SCC, union–find, amortized).  
3. Hopcroft & Tarjan — planarity testing papers; Tarjan SCC.  
4. Ahuja, Magnanti, Orlin — *Network Flows* (bối cảnh matching/flow).  
5. Khóa: [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/); [Euler]({{ site.baseurl }}/contents/vi/chapter05/05_05_Euler_Konigsberg/); [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [Modern Themes]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/).

---

## Hướng đi tiếp

- Spectral / expander: [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/) và [Lovász–Wigderson Abel]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).  
- Tối ưu trên mạng: [optimization]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).  
- Thực hành: cài Tarjan SCC; so với NetworkX trên đồ thị random.  
- Đọc: CLRS DFS+SCC → một note planarity → Tarjan union–find analysis sketch.  
- Tiếp: [Pearl và nhân quả]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).
