"""Toán cho reel koch-fourier-epicycles: bông tuyết Koch bậc 4 -> mẫu đều theo độ dài cung -> FFT phức
-> N hệ số lớn nhất -> sai số. Mọi con số trên màn hình lấy từ file này (có assert)."""
import numpy as np
from scipy.spatial import cKDTree

LEVEL = 4
M = 4096                      # số điểm lấy mẫu đều theo độ dài cung (2^12, FFT nhanh)
NS = (1, 5, 20, 100, 500)     # số vòng tròn mỗi giai đoạn


def koch_vertices(level):
    pts = [complex(np.exp(1j * (np.pi / 2 + 2 * np.pi * k / 3))) for k in range(3)]   # ngược chiều kim đồng hồ
    for _ in range(level):
        new = []
        for a, b in zip(pts, pts[1:] + pts[:1]):
            d = (b - a) / 3
            p1, p2 = a + d, a + 2 * d
            peak = p1 + d * np.exp(-1j * np.pi / 3)   # đỉnh nhô ra ngoài (đa giác ngược chiều kim đồng hồ)
            new += [a, p1, peak, p2]
        pts = new
    return np.array(pts)


V = koch_vertices(LEVEL)
assert len(V) == 3 * 4 ** LEVEL == 768
E = np.roll(V, -1) - V
L = np.abs(E)
assert np.allclose(L, L[0])                                  # mọi cạnh bằng nhau
PER = L.sum()
assert abs(PER - 3 * np.sqrt(3) * (4 / 3) ** LEVEL) < 1e-9    # chu vi = 3*s*(4/3)^n, s = sqrt(3) (tam giác nội tiếp đường tròn bán kính 1)
# đa giác đơn (không tự cắt): diện tích dương theo công thức Gauss, khớp công thức đóng của bông tuyết Koch
area = 0.5 * np.sum((V.real * np.roll(V, -1).imag - np.roll(V, -1).real * V.imag))
a0 = 3 * np.sqrt(3) / 4
area_formula = (1 + (3 / 5) * (1 - (4 / 9) ** LEVEL))   # S_n = S_0 (1 + 3/5 (1 - (4/9)^n))
assert area > 0 and abs(area / a0 - area_formula) < 1e-9, (area / a0, area_formula)


def sample_uniform(V, m):
    """m điểm cách đều theo độ dài cung (cạnh bằng nhau nên nội suy theo tham số cạnh)."""
    n = len(V)
    u = np.arange(m) * n / m
    i = np.floor(u).astype(int)
    f = u - i
    return V[i] * (1 - f) + V[(i + 1) % n] * f


# dịch tâm về trọng tâm của đường biên (c_0 = trung bình các mẫu), chuẩn hóa bán kính lớn nhất = 1
Z0 = sample_uniform(V, M)
Z0 = Z0 - Z0.mean()
Z = Z0 / np.abs(Z0).max()
Vn = (V - V.mean()) / np.abs(Z0).max()
C = np.fft.fft(Z) / M                      # c_k = (1/M) sum z(t_j) e^{-2 pi i k t_j}
FREQ = np.fft.fftfreq(M, 1 / M).astype(int)  # k = 0, 1, ..., -2, -1
assert abs(C[0]) < 1e-12                     # c_0 = 0 sau khi dịch tâm
assert np.allclose(np.fft.ifft(C * M), Z)

ORDER = np.argsort(-np.abs(C), kind="stable")   # chỉ số theo |c_k| giảm dần (c_0 ~ 0 nằm cuối)
T = np.arange(M) / M
RBAR = np.abs(Z).mean()                         # bán kính trung bình

# đường biên dày đặc để đo khoảng cách hình học: mỗi cạnh chia 40 đoạn
DENSE = np.concatenate([V[i] + (V[(i + 1) % len(V)] - V[i]) * np.linspace(0, 1, 40, endpoint=False) for i in range(len(V))])
DENSE = (DENSE - V.mean()) / np.abs(Z0).max()
TREE_P = cKDTree(np.c_[DENSE.real, DENSE.imag])


def terms(n):
    return ORDER[:n]


def recon(n, t=T):
    idx = terms(n)
    return (C[idx][None, :] * np.exp(2j * np.pi * FREQ[idx][None, :] * t[:, None])).sum(axis=1)


def boundary_error(zn):
    """Sai số hai chiều (Chamfer) giữa đường dựng lại và đường Koch bậc 4, chia bán kính trung bình:
    E = [ mean_j d(zn_j, Koch) + mean_i d(Koch_i, zn) ] / 2 / RBAR."""
    a = TREE_P.query(np.c_[zn.real, zn.imag])[0].mean()
    tree_r = cKDTree(np.c_[zn.real, zn.imag])
    b = tree_r.query(np.c_[DENSE.real, DENSE.imag])[0].mean()
    return 0.5 * (a + b) / RBAR


REC = {n: recon(n) for n in NS}
ERR = {n: boundary_error(REC[n]) for n in NS}
ERRP = {n: 100 * ERR[n] for n in NS}               # phần trăm
assert all(ERR[a] > ERR[b] for a, b in zip(NS, NS[1:])), ERR   # nhiều vòng hơn -> sai số giảm
# đủ cả M hệ số thì khớp đúng các điểm mẫu (đa giác bậc 4), tức vẫn chỉ là đa giác chứ không phải fractal
assert np.allclose(recon(M), Z)

# đỉnh nhọn để phóng to (đỉnh xa tâm nhất của đa giác)
TIP = Vn[np.argmax(np.abs(Vn))]
EDGE = L[0] / np.abs(Z0).max()

if __name__ == "__main__":
    print("verts", len(V), "edge", L[0], "perimeter", PER, "area/a0", area / a0)
    print("k of top terms:", [int(FREQ[i]) for i in ORDER[:12]], [round(abs(C[i]), 4) for i in ORDER[:12]])
    for n in NS:
        print(n, "err %.3f%%" % ERRP[n], "sum |c|^2 captured %.4f" % (np.sum(np.abs(C[terms(n)]) ** 2) / np.sum(np.abs(C) ** 2)))
    print("tip", TIP, "edge", EDGE, "R-bar", RBAR)
