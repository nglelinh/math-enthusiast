---
layout: post
title: "Graph Theory → Networks"
chapter: '03'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

Roads, hyperlinks, molecules, social ties, chip wires, and dependency graphs of software packages are all the same kind of object until labels differ: **vertices** joined by **edges**. Graph theory—once a recreational cousin of combinatorics—now routes packets, ranks web pages, allocates flows, and analyzes epidemics.

**Path:** graphs as models → paths and connectivity → trees and cycles → flows and cuts → random walks and PageRank → expanders and robustness → algorithms that scale → confusions.

This lecture maps **mechanisms**: which graph ideas become which network technologies, and why linear algebra on adjacency matrices sits next to discrete algorithms.

---

## Learning objectives

After this lecture you should be able to:

- Model a real system as a graph $$G=(V,E)$$ (directed/undirected, weighted/unweighted) and state what nodes and edges represent.
- Explain connectivity, shortest paths, and why BFS/Dijkstra-style algorithms matter for routing and logistics.
- State the max-flow min-cut idea at slogan level and name one application (transport, matching, reliability).
- Describe **PageRank** as a random-walk / eigenvector idea on the web graph.
- Say what an **expander** buys you (connectivity vs few edges) at intuition level.
- Avoid “graphs are only social networks” and “PageRank is just counting in-links.”

**Prerequisites.** Basic discrete math comfort. Helpful: matrix–vector multiplication from [Linear Algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/).

**Seminar links.** [Network Science (Ch.6)]({{ site.baseurl }}/contents/en/chapter06/06_05_Network_Science/), [Four Color Theorem]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/) (planar graphs culture).

---

## 1. Graphs as the algebra of connection

A **graph** $$G=(V,E)$$ consists of a vertex set $$V$$ and an edge set $$E$$ of pairs (undirected) or ordered pairs (directed). Edges may carry **weights** (distance, capacity, affinity).

| System | Vertices | Edges |
|--------|----------|-------|
| Road map | Intersections | Road segments (length, time) |
| Web | Pages | Hyperlinks (directed) |
| Social network | People / accounts | Follows, friendships |
| Circuit | Components / nets | Wires |
| Molecule | Atoms | Bonds |
| ML computation | Tensors / ops | Data dependencies |

**Mechanism slogan.**  
*When “who connects to whom” dominates “where in Euclidean space,” graph language is the right coordinate system.*

Adjacency matrices $$A$$ with $$A_{ij}=1$$ (or weight) if $$i\to j$$ turn graph questions into linear algebra: powers $$A^k$$ count walks of length $$k$$; spectral gaps control mixing.

---

## 2. Paths, distance, and connectivity

A **path** is a walk without repeated vertices (definitions vary slightly by author; the engineering point is a route). The **distance** $$d(u,v)$$ is the length of a shortest path (unweighted hop count or weighted sum).

**Connectivity** asks whether every pair of vertices is linked by some path; directed graphs refine this into strongly/weakly connected components. Bridges and cut vertices are single points of failure—reliability engineering in combinatorial form.

**Algorithms that built industries.**

- **BFS** — unweighted shortest paths; levels in networks.  
- **Dijkstra** — nonnegative weighted shortest paths; GPS routing core (with hierarchical heuristics and contraction hierarchies in practice).  
- **A\*** — Dijkstra with a geometric heuristic when an embedding exists.  
- **Bellman–Ford / Floyd–Warshall** — more general (negative edges, all-pairs) at higher cost.

**Mechanism.**  
*Routing is optimized search on a graph; “best path” is a well-posed combinatorial optimization problem, not a map aesthetic.*

---

## 3. Trees, spanning structure, and cycles

A **tree** is a connected acyclic graph: uniquely path-connected pairs, $$|E|=|V|-1$$. **Spanning trees** of a network are backbones without redundancy; **minimum spanning trees (MST)** (Kruskal, Prim) design cheap connecting infrastructure when cycles are optional.

Cycles create redundancy (good for fault tolerance) and complexity (harder uniqueness of paths). In dependency graphs, cycles can mean deadlock or circular imports. In chemistry, cycles mean rings. In algebraic topology’s discrete cousin, cycles generate homology—optional depth for later.

**Eulerian and Hamiltonian** stories (traversing edges vs vertices) are classical; the second is NP-hard in general and sits near [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) culture when you scale to huge logistics.

---

## 4. Flows and cuts: capacity as mathematics

Assign each edge a **capacity** $$c(e)\ge 0$$. A **flow** ships material from source $$s$$ to sink $$t$$ without exceeding capacities and with conservation at intermediate nodes. The **max-flow min-cut theorem** says the maximum throughput equals the minimum total capacity of an $$s$$–$$t$$ cut (a partition separating $$s$$ from $$t$$).

$$
\max \mathrm{flow}(s,t) = \min \mathrm{cut}(s,t).
$$

**Applications.** Traffic and logistics; bipartite matching via flow reductions; image segmentation (graph cuts); reliability (edge connectivity); some project-selection problems in OR.

**Mechanism.**  
*Bottlenecks are cuts; algorithms (Ford–Fulkerson, Dinic, push–relabel, …) search augmenting structure until a cut certifies optimality.*

This is discrete optimization with a beautiful duality certificate—sibling spirit to LP duality in the [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/) lecture.

---

## 5. Random walks, stationary distributions, and PageRank

A random walk on a directed graph moves from a node along outgoing edges (uniformly or by weight). Under mild conditions, the walk has a **stationary distribution** $$\pi$$ satisfying $$\pi^\top=\pi^\top P$$ for the transition matrix $$P$$—a left-eigenvector problem with eigenvalue $$1$$.

**PageRank** (Brin–Page) models a web surfer who usually follows links but sometimes jumps (teleportation) to a random page. The ranking vector is the stationary distribution of that process—equivalently, the solution of a linear system

$$
\pi = \alpha P^\top \pi + (1-\alpha) v,
$$

with damping $$\alpha$$ and teleport vector $$v$$. Importance is not raw in-degree: a link from a highly ranked page counts more, and strongly connected structure interacts with the walk.

**Mechanism.**  
*Global importance emerges from local link structure via an eigenvector / linear solve—not from a hand-written scorecard.*

Variants power recommendation, academic citation metrics (with caveats), and node centrality measures across network science ([Ch.6 Network Science]({{ site.baseurl }}/contents/en/chapter06/06_05_Network_Science/)). The same linear-algebraic spirit appears in personalized PageRank (teleport biased toward a seed set), which is a workhorse for local graph clustering and “related pages” features.

**Power iteration culture.** In practice one rarely forms a dense eigen-solver fantasy: repeated sparse matrix–vector products with the Google matrix (or an equivalent linear solve) compute rankings on graphs with billions of edges. Scalability is not an afterthought; it is why the eigenvector formulation won historically over more baroque scoring rules that do not admit fast iteration.

---

## 6. Spectral graph theory: Laplacians and cuts

The combinatorial **Laplacian** $$L=D-A$$ (degree matrix minus adjacency) is positive semidefinite with $$L\mathbf{1}=0$$ on undirected graphs. The second-smallest eigenvalue (algebraic connectivity, Fiedler value) controls how well-connected the graph is; its eigenvector hints at bipartitions.

Spectral clustering, graph drawing, and graph signal processing use eigenbases of $$L$$ the way Fourier analysis uses complex exponentials—indeed there is a precise analogy (graph Fourier transform). Sparsifiers approximate quadratic forms $$x^\top L x$$ with fewer edges—algorithmic graph theory meeting numerical linear algebra.

---

## 7. Expanders: sparse yet superbly connected

An **expander family** is a sequence of sparse graphs with strong connectivity: every set of vertices has a large boundary relative to its size (edge expansion). Equivalently (roughly), random walks mix fast; spectral gaps are bounded away from zero.

**Why technology cares.**

- Robust networks: few edges, hard to disconnect.  
- Derandomization and coding theory.  
- Efficient communication topologies.  
- Mixing time bounds for MCMC.

You need not memorize expander constructions (Margulis, LPS Ramanujan graphs, random regular graphs) to grasp the slogan: **expansion is a quantitative form of “no bottlenecks.”**

---

## 8. Scale, small worlds, and network science

Empirical networks often show:

- **Heavy-tailed degrees** (hubs),  
- **Small-world** distances (short paths despite clustering),  
- **Community structure** (dense inside, sparse outside).

These are probabilistic graph models (Erdős–Rényi, configuration model, preferential attachment, stochastic block models) as much as pure graph theory—probability re-enters ([Probability lecture]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/)). Epidemic thresholds, viral marketing, and cascading failures are dynamics *on* graphs.

**Graph neural networks** learn features by message passing along edges—linear algebra structured by $$E$$—tying this lecture to modern ML ([Linear Algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/)).

---

## 9. Complexity honesty

Many graph problems are easy (connectivity, MST, matching in bipartite graphs, max flow in practice with good algorithms). Many are hard (Hamiltonian cycle, max cut general, many community objectives, graph isomorphism historically subtle—now quasi-polynomial). Engineering succeeds by:

1. Using the right special case,  
2. Approximating,  
3. Exploiting structure (planarity, low treewidth, sparsity),  
4. Heuristics with validation.

Graph theory supplies both the poly-time engines and the hardness maps.

---

### Network math slogans (from video research)

- **Max-flow min-cut:** capacity is both a flow question and a cut question.
- **PageRank:** dominant eigenvector / stationary distribution of a damped walk — linear algebra on the web.
- **Expanders:** sparse graphs with excellent connectivity; spectral gap is the quantitative heart.
- Start with MIT discrete math/algorithms OCW, then the Ch.3 essay’s spectral section.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Graphs only model social media.” | Any pairwise relation is a graph: logistics, chips, molecules, code. |
| “PageRank is just counting inbound links.” | It is a global eigenvector/random-walk equilibrium with teleportation. |
| “Shortest path always means fewest hops.” | Only in unweighted graphs; weights encode time, cost, risk. |
| “Max flow is only for pipes.” | Matching, segmentation, reliability reduce to flows/cuts. |
| “More edges always improve a network.” | Cost, congestion, and attack surface grow; expanders optimize tradeoffs. |
| “If a problem is on a graph, it is easy.” | Many graph problems are NP-hard; structure matters. |

---

## Exercises

1. **Warm-up.** Draw a directed graph of 4 web pages with 6 links. Identify a node with in-degree 0.  
2. **Paths.** Explain why BFS finds unweighted shortest paths (invariant of the queue).  
3. **Flow slogan.** In two sentences, state max-flow min-cut and what a min cut certifies.  
4. **PageRank mechanism.** Why can a page with few in-links outrank a page with many low-quality in-links?  
5. **Model.** Encode a small subway map as a weighted graph; define what “shortest” should mean for a rider.  
6. **Spectral.** What does $$x^\top Lx=\sum_{ij\in E}(x_i-x_j)^2$$ measure about a function $$x$$ on vertices?  
7. **Stretch.** Look up the definition of edge expansion and interpret “good expander” in plain language.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/graph-theory-networks/`.

**Recommended order**

1. **FOUNDATION** — MIT 6.042J Mathematics for Computer Science (graphs modules): [https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/).
2. **FOUNDATION** — MIT 6.006 Introduction to Algorithms (graph algorithms): [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
3. **ORIENTATION** — Numberphile — Graph theory / networks culture (search: graphs Numberphile): [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).
4. **ORIENTATION** — Numberphile — Seven Bridges of Königsberg culture: [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).
5. **INTUITION** — 3Blue1Brown — Eigenvectors and eigenvalues (spectral seeds): [https://www.youtube.com/watch?v=PFDu9oVAE-g](https://www.youtube.com/watch?v=PFDu9oVAE-g).
6. **CORE** — PageRank: A Trillion Dollar Algorithm (popular CS explainer): [https://www.youtube.com/watch?v=JGQe4kiPnrU](https://www.youtube.com/watch?v=JGQe4kiPnrU).

Complete URL bibliography: `research/video-research/graph-theory-networks/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/graph-theory-networks/transcripts/` · status: `research/video-research/graph-theory-networks/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/graph-theory-networks_W18FDEA1jRQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/graph-theory-networks/references.md`.

### Videos (primary path)

1. MIT 6.042J Mathematics for Computer Science (graphs modules) — https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/
2. MIT 6.006 Introduction to Algorithms (graph algorithms) — https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
3. Numberphile — Graph theory / networks culture (search: graphs Numberphile) — https://www.youtube.com/watch?v=W18FDEA1jRQ
4. Numberphile — Seven Bridges of Königsberg culture — https://www.youtube.com/watch?v=W18FDEA1jRQ
5. 3Blue1Brown — Eigenvectors and eigenvalues (spectral seeds) — https://www.youtube.com/watch?v=PFDu9oVAE-g
6. PageRank: A Trillion Dollar Algorithm (popular CS explainer) — https://www.youtube.com/watch?v=JGQe4kiPnrU
7. Stanford / network science lectures (Barabási-style surveys) — https://en.wikipedia.org/wiki/Network_science
8. Spectral graph theory intro talks (Spielman culture) — https://cs-www.cs.yale.edu/homes/spielman/sagt/

### Videos (secondary finds)

9. Algorithms Illuminated / Roughgarden graph modules — https://www.algorithmsilluminated.org/

### Papers, books, OCW, and web

10. Brin & Page — The Anatomy of a Large-Scale Hypertextual Web Search Engine: http://infolab.stanford.edu/~backrub/google.html
11. Wikipedia — Graph theory: https://en.wikipedia.org/wiki/Graph_theory
12. Wikipedia — Max-flow min-cut theorem: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
13. Wikipedia — PageRank: https://en.wikipedia.org/wiki/PageRank
14. Wikipedia — Expander graph: https://en.wikipedia.org/wiki/Expander_graph
15. Spielman — Spectral Graph Theory notes: https://cs-www.cs.yale.edu/homes/spielman/sagt/

### Course

16. Course: [Network Science]({{ site.baseurl }}/contents/en/chapter06/06_05_Network_Science/), [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Linear Algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/). Pack: `research/video-research/graph-theory-networks/`.

## Further directions

- Next: [Optimization → Operations & AI]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/) (flows as special LP; discrete decisions).  
- Empirically flavored continuation: [Network Science]({{ site.baseurl }}/contents/en/chapter06/06_05_Network_Science/).  
- Pure sibling: planarity and coloring culture in [Four Color Theorem]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/).  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.
