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

Đầu thập niên 1970, khi bảng mạch điện tử bắt đầu chứa hàng nghìn linh kiện nối dây chằng chịt, các kỹ sư đau đầu trước một bài toán hình học–tổ hợp sống còn: *làm sao kiểm tra thật nhanh xem một sơ đồ mạch có vẽ được lên mặt phẳng mà không có hai sợi dây nào cắt nhau hay không?* Ai cũng biết định lý Kuratowski cấm $$K_5$$ và $$K_{3,3}$$, nhưng đi dò tìm các đồ thị con ấy tốn thời gian $$O(n^6)$$ — hoàn toàn vô dụng cho mạch thật. Thế rồi hai nhà khoa học **John E. Hopcroft** và **Robert E. Tarjan** xuất hiện và tung ra một phép màu thuật toán: chỉ cần **một lượt duyệt sâu (DFS)** khéo léo, ta kiểm tra được tính phẳng trong thời gian tuyến tính **$$O(n)$$** — nhanh gần bằng đúng thời gian đọc dữ liệu vào máy!

Nhận **Giải A.M. Turing năm 1986** với lời trích dẫn:

> “for fundamental achievements in the design and analysis of algorithms and data structures.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Nếu Cook–Karp cho ta thấy bức tường của những bài toán NP-đầy đủ, thì Hopcroft–Tarjan mở ra cánh cửa rực rỡ ở phía ngược lại: những bài toán cấu trúc đồ thị có thể giải **tuyệt đẹp và gần như tức thời**. Chỉ bằng việc gắn thêm vài con số phụ vào DFS (thời điểm thăm, giá trị `low-link`, ngăn xếp), Tarjan tìm ra thành phần liên thông mạnh (SCC), cầu và khớp trong $$O(n+m)$$, rồi cùng phân tích **khấu hao (amortized)** chứng minh cấu trúc Union–Find chạy gần như hằng số $$O(\alpha(n))$$. Liên kết: [đồ thị & mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) và [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/).

---

## Mục tiêu học tập

Sau bài, bạn có thể mô tả **DFS** như quy nạp trên cây đệ quy + cạnh back/forward/cross và giải thích vì sao timestamps cho phép suy cấu trúc; phác thuật toán **Tarjan** (hoặc Kosaraju) tìm **SCC** (strongly connected components) trong $$O(n+m)$$; nêu ý **cầu (bridge)** / **khớp (articulation point)** qua giá trị low; giải thích **planarity testing** tuyến tính như thành tựu “cấu trúc phẳng = thuật toán gần tối ưu”; mô tả **union–find** với union by rank + path compression và bound gần $$\alpha(n)$$ (hàm ngược Ackermann); nối amortized analysis với thiết kế cấu trúc dữ liệu hiện đại mà không nhầm “amortized = trung bình ngẫu nhiên”.

**Kiến thức nền.** Đồ thị có hướng/vô hướng; danh sách kề; $$O$$-notation. Biết BFS/DFS mức nhập môn là đủ để nâng cấp.

---

## Bản đồ kiến thức nền: Thuật toán đồ thị và Phân tích khấu hao (Amortized Analysis) là gì, nghiên cứu những gì?

Với sinh viên đại học ngành công nghệ, **duyệt theo chiều sâu (DFS)** thường chỉ là 10 dòng đệ quy để đi thăm hết các đỉnh. Nhưng trong tay các nhà lý thuyết đồ thị thuật toán (Algorithmic Graph Theory), DFS là một chiếc **máy chụp X-quang cấu trúc**: chỉ trong đúng một lượt đi qua mỗi đỉnh và mỗi cạnh một lần ($$O(n+m)$$), nó phơi bày toàn bộ chu trình, điểm yếu sinh tử (cầu, khớp) và các cụm phụ thuộc vòng tròn (SCC) của một mạng lưới triệu nút — thứ mà trình biên dịch, trình quản lý gói (như `npm`/`pip`) và hệ thống định tuyến mạng chạy mỗi giây.

Song hành với thuật toán đồ thị là một công cụ toán học cực kỳ tinh tế do Tarjan hoàn thiện: **Phân tích khấu hao (Amortized Analysis)**. Để hình dung sự khác biệt giữa *worst-case từng bước* và *amortized*, hãy nghĩ tới một chiếc mảng động (`std::vector` trong C++ hoặc `list` trong Python):
- Hầu hết các lần thêm phần tử (`append`) chỉ tốn $$O(1)$$ (ghi thẳng vào ô trống cuối mảng).
- Thỉnh thoảng khi mảng đầy, ta phải cấp phát mảng mới gấp đôi kích thước và chép toàn bộ $$n$$ phần tử sang — một bước duy nhất đó tốn $$O(n)$$.
- Nhưng nếu bạn cộng tổng chi phí của cả chuỗi $$n$$ lần thêm: $$n + (1 + 2 + 4 + \dots + n) < 3n$$, tức **chi phí khấu hao mỗi thao tác vẫn chỉ là $$O(1)$$**!

Phân tích khấu hao dùng **hàm thế năng (potential function)** — giống hệt thế năng trong vật lý: mỗi thao tác rẻ "nạp" một ít thế năng vào cấu trúc dữ liệu, để khi gặp thao tác đắt hiếm hoi (như nén đường dẫn dài trong Union–Find), thế năng tích trữ sẽ tự động "trả hóa đơn" cho nó. Nhờ đó, Tarjan chứng minh $$m$$ thao tác Union–Find trên $$n$$ phần tử chỉ tốn $$O(m\,\alpha(n))$$, trong đó hàm ngược Ackermann $$\alpha(n) \le 4$$ ngay cả khi $$n$$ lớn hơn số nguyên tử trong vũ trụ quan sát được!

---

## 1. Vì sao Turing 1986 là giải “thuật toán”

Giữa thập niên 1970–80, CS lý thuyết tách rõ hai cực: **NP-đầy đủ** (bạn không kỳ vọng poly-time tổng quát) và **thuật toán đa thức tinh xảo** (bạn *có* poly-time—và có thể gần tuyến tính). Hopcroft–Tarjan đứng cực thứ hai với chuẩn chứng minh runtime và correctness sắt đá. Citation không nói “một app”; nói **design and analysis**—phương pháp.

Khóa học này cần cả hai cực. [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) giải thích tường; Hopcroft–Tarjan giải thích **cửa sổ ánh sáng** nơi đồ thị chịu thuật toán đẹp. Thực hành phần mềm (compiler, mạng, GIS, verification) sống nhờ cửa sổ đó nhiều hơn nhờ slogan NP.

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

- **Cầu:** cạnh cây $$(u,v)$$ mà subtree của $$v$$ không có đường vòng ngược lên $$u$$ hay tổ tiên của $$u$$ (tức $$\mathrm{low}[v] > d[u]$$).  
- **Khớp:** đỉnh mà việc xóa làm tăng số thành phần liên thông—đặc trưng bằng việc có ít nhất một con $$v$$ thỏa $$\mathrm{low}[v] \ge d[u]$$ (riêng gốc cây DFS là khớp khi nó có từ 2 con trở lên).

Công thức không cần thuộc máy; cần thuộc **ý**: DFS + một vài số nguyên phụ = chứng nhận cấu trúc cắt.

---

## 3. Thành phần liên thông mạnh (SCC)

Đồ thị có hướng phân hoạch thành SCC: trong mỗi khối, mọi cặp đỉnh tới được nhau; đồ thị co các khối thành DAG. **Tarjan’s SCC algorithm** dùng một DFS, stack các đỉnh “đang mở”, và low-link để pop đúng một SCC khi root của component finish (đúng lúc $$\mathrm{low}[u] = d[u]$$). **Kosaraju**: hai DFS (một trên đồ thị ngược) cũng $$O(n+m)$$, dễ dạy hơn, hằng số khác.

Vì sao quan trọng toán–CS:

- Mọi path queries “tồn tại đường” giảm về reachability trên DAG của SCC.  
- Model checking, dependency analysis, game graphs dùng SCC như preprocess.  
- Đây là ví dụ **cấu trúc toàn cục từ duyệt địa phương**—họ hàng tinh thần với [Euler Königsberg]({{ site.baseurl }}/contents/vi/chapter05/05_05_Euler_Konigsberg/): topology tổ hợp + thuật toán.

---

### Video ngắn: Thuật toán Tarjan tìm thành phần liên thông mạnh trong O(n + m)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/tarjan-scc_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 56 giây (có thuyết minh tiếng Việt): định nghĩa SCC và quy tắc cập nhật (disc, low), theo dõi từng bước DFS và ngăn xếp trên đồ thị 6 đỉnh, bẫy kiểm tra on_stack[v] và đồ thị DAG rút gọn.



<div class="interactive-demo" markdown="1">
<div data-demo="tarjan-explainer" data-preset="sixNode" data-lang="vi"></div>
</div>
<script src="{{ '/public/js/explainers/tarjan-explainer.js' | relative_url }}"></script>

## 4. Planarity: phẳng hóa như bài toán tuyến tính

### Câu hỏi

Cho đồ thị đơn $$G=(V,E)$$, $$\lvert V\rvert=n$$, có nhúng mặt phẳng không cắt cạnh? Kuratowski/Wagner cho đặc trưng cấm $$K_5,K_{3,3}$$ minors—đẹp lý thuyết nhưng naive search minor không phải thuật toán tuyến tính hiển nhiên.

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
| Randomized | Thuật toán tự gieo đồng xu |

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

Papers Hopcroft–Tarjan-era viết invariant rõ: stack chứa gì, low thỏa bất biến nào lúc pop. Khi code graph bug, thường do **không giữ invariant** chứ không do “big-O sai”. Khi học thuật toán, nên luyện thói quen: nêu loop invariant một câu trước khi tối ưu micro.

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
7. Đọc phần tóm tắt của bài báo Hopcroft–Karp; so brute bipartite matching $$O(VE)$$.

---


## Video và tài liệu

Các video gợi ý nằm ở phần *Video tham khảo* cuối bài. Hãy dùng video để làm quen với bối cảnh, không dùng thay cho chứng minh.

## Tài liệu tham khảo trực tuyến



1. Trang giải Turing của Hopcroft — https://amturing.acm.org/award_winners/hopcroft_1053917.cfm  
2. Trang giải Turing của Tarjan — https://amturing.acm.org/award_winners/tarjan_1092048.cfm  
3. Wikipedia — John Hopcroft — https://en.wikipedia.org/wiki/John_Hopcroft  
4. Wikipedia — Robert Tarjan — https://en.wikipedia.org/wiki/Robert_Tarjan  
5. Wikipedia — Hopcroft–Tarjan algorithm (planarity) — https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Tarjan_planarity_test  
6. Wikipedia — Depth-first search — https://en.wikipedia.org/wiki/Depth-first_search  
7. Wikipedia — Union–find / disjoint set (Tarjan) — https://en.wikipedia.org/wiki/Disjoint-set_data_structure  
8. Sách về automata của Hopcroft–Ullman — https://en.wikipedia.org/wiki/Introduction_to_Automata_Theory,_Languages,_and_Computation  

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

## Video tham khảo

- **Xem trước** — [5.2 Articulation Point and Biconnected Components](https://www.youtube.com/watch?v=jFZsDDB0-vo) — Abdul Bari, tiếng Anh. Xem trước để làm quen với chủ đề.
- [Lecture: Robert Endre Tarjan | September 19](https://www.youtube.com/watch?v=7vpTTH1_OCo) — Heidelberg Laureate Forum, tiếng Anh. Xem sau khi đã nắm ý chính.
- [Robert Tarjan: My Life with Data Structures #ICBS2025](https://www.youtube.com/watch?v=Iw486e6YKFo) — BIMSA, tiếng Anh. Góc nhìn bổ sung.
