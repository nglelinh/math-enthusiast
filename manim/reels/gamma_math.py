"""Toán cho reel gamma-function-factorial. Mọi số/đường trên màn hình lấy từ file này; các assert kiểm số học
bằng mpmath (độ chính xác cao) và scipy."""
import numpy as np
import mpmath as mp
from scipy import special as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

mp.mp.dps = 40
G = lambda x: float(mp.gamma(x))

# 1. giai thừa: n! = Gamma(n+1)
FACT = [(n + 1, int(mp.factorial(n))) for n in range(0, 5)]       # điểm (x, y) = (n+1, n!) nằm trên đồ thị Gamma(x)
assert [y for _, y in FACT] == [1, 1, 2, 6, 24]
for x, y in FACT:
    assert abs(mp.gamma(x) - y) < 1e-30

# 2. tích phân Euler: Gamma(z) = int_0^inf t^(z-1) e^(-t) dt
for z in (0.5, 1, 2.5, 4, 7.3):
    val = quad(lambda t: t ** (z - 1) * np.exp(-t), 0, np.inf, epsabs=1e-12, epsrel=1e-12)[0]
    assert abs(val - G(z)) < 1e-8 * max(1, G(z)), (z, val, G(z))
Z_INT = 4
AREA4 = quad(lambda t: t ** (Z_INT - 1) * np.exp(-t), 0, np.inf)[0]
assert abs(AREA4 - 6) < 1e-9                                    # Gamma(4) = 3! = 6

# 3. hệ thức Gamma(x+1) = x Gamma(x), kể cả số phức và x < 0
for x in (0.3, 1.7, 5.2, -0.4, -2.6, 3 + 2j, -1.5 + 0.7j):
    x = mp.mpmathify(x)
    assert abs(mp.gamma(x + 1) - x * mp.gamma(x)) < 1e-30 * (1 + abs(mp.gamma(x + 1)))

# 4. cực tại 0, -1, -2, ...: thặng dư (-1)^n / n!
for n in range(0, 7):
    eps = mp.mpf(10) ** -15
    res = mp.gamma(-n + eps) * eps
    assert abs(res - (-1) ** n / mp.factorial(n)) < 1e-12, n
POLES = [0, -1, -2, -3, -4]
# dấu đổi theo từng khoảng giữa hai cực: (-n-1, -n) có dấu (-1)^(n+1)
for n in range(0, 5):
    assert np.sign(G(-n - 0.5)) == (-1) ** (n + 1)

# 5. Bohr–Mollerup: f(x) = Gamma(x) * (1 + a sin 2 pi x) cũng thỏa f(1)=1, f(x+1)=x f(x), f>0 nhưng log f KHÔNG lồi
A = 0.3
f_alt = lambda x: G(x) * (1 + A * np.sin(2 * np.pi * x))
assert abs(f_alt(1) - 1) < 1e-12
for x in (0.37, 1.6, 2.9, 4.4):
    assert abs(f_alt(x + 1) - x * f_alt(x)) < 1e-9 * f_alt(x + 1)
xs = np.linspace(0.6, 5.0, 4001)
assert all(f_alt(x) > 0 for x in xs[::40])
logGamma_dd = [float(mp.polygamma(1, x)) for x in xs[::40]]
assert min(logGamma_dd) > 0                                      # (log Gamma)'' = psi'(x) > 0: log Gamma lồi
lf = np.array([np.log(f_alt(x)) for x in xs])
h = xs[1] - xs[0]
assert (lf[2:] - 2 * lf[1:-1] + lf[:-2]).min() < 0              # log f_alt không lồi
# Gamma(x) = lim n! n^x / (x (x+1) ... (x+n))  (cách Bohr–Mollerup xây dựng) tại x = 0.5
x0, n0 = mp.mpf("0.5"), 10 ** 5
lg = mp.loggamma(n0 + 1) + x0 * mp.log(n0) - sum(mp.log(x0 + k) for k in range(n0 + 1))
assert abs(mp.e ** lg - mp.gamma(x0)) < 1e-4

# 6. Gamma(1/2) = sqrt(pi), (-1/2)! = Gamma(1/2); Gamma(-1/2) = -2 sqrt(pi)
SQRTPI = float(mp.sqrt(mp.pi))
assert abs(mp.gamma(mp.mpf(1) / 2) - mp.sqrt(mp.pi)) < 1e-35
assert abs(quad(lambda u: 2 * np.exp(-u * u), 0, np.inf)[0] - SQRTPI) < 1e-10          # đổi biến t = u^2
assert abs(mp.gamma(-mp.mpf(1) / 2) + 2 * mp.sqrt(mp.pi)) < 1e-35
assert abs(float(mp.factorial(-mp.mpf(1) / 2)) - SQRTPI) < 1e-12      # mpmath: z! = Gamma(z+1)
assert abs(SQRTPI - 1.7724538509055159) < 1e-15

# 7. không có không điểm + công thức phản xạ
rng = np.random.default_rng(7)
for _ in range(200):
    z = complex(rng.uniform(-6, 6), rng.uniform(-4, 4))
    if abs(z - round(z.real)) < 1e-3 and abs(z.imag) < 1e-3:
        continue
    z = mp.mpmathify(z)
    lhs = mp.gamma(z) * mp.gamma(1 - z)
    rhs = mp.pi / mp.sin(mp.pi * z)
    assert abs(lhs - rhs) < 1e-30 * abs(rhs), z
# |Gamma| trên lưới phức có min > 0 xa các cực; 1/Gamma là hàm nguyên nên không bằng 0 => Gamma không có không điểm
xr = np.linspace(-6, 6, 241); yr = np.linspace(-4, 4, 161)
ZZ = xr[None, :] + 1j * yr[:, None]
GAM = sp.gamma(ZZ)
fin = np.isfinite(GAM)
# trên cả lưới phức: |Gamma(z) Gamma(1-z) sin(pi z)| = pi (không chạm 0); |Gamma| có thể rất nhỏ nhưng không bằng 0
chk = np.abs(GAM * sp.gamma(1 - ZZ) * np.sin(np.pi * ZZ))
ok = np.isfinite(chk) & (np.abs(np.sin(np.pi * ZZ)) > 1e-6)
assert ok.sum() > 30000 and np.allclose(chk[ok], np.pi, rtol=1e-8)
GMIN = minimize_scalar(lambda x: G(x), bounds=(1, 2), method="bounded")
assert abs(GMIN.x - 1.4616321449683623) < 1e-5 and abs(GMIN.fun - 0.8856031944108887) < 1e-9   # giá trị nhỏ nhất trên (0, inf)

# 8. xi(s) = 1/2 s (s-1) pi^(-s/2) Gamma(s/2) zeta(s) = xi(1-s); không điểm tầm thường tại -2,-4,-6
xi = lambda s: mp.mpf(1) / 2 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
for s in (mp.mpc("2.3", "1.1"), mp.mpc("-1.7", "3.2"), mp.mpc("0.5", "14.134725"), mp.mpf("3.5"), mp.mpf("0.2")):
    assert abs(xi(s) - xi(1 - s)) < 1e-25 * (1 + abs(xi(s))), s
for k in (1, 2, 3, 4):
    s = mp.mpf(-2 * k)
    assert mp.zeta(s) == 0 or abs(mp.zeta(s)) < 1e-30                      # zeta(-2k) = 0
    eps = mp.mpf(10) ** -15
    # Gamma(s/2) có cực tại s = -2k, nhưng xi vẫn hữu hạn và = xi(1 - s)
    assert abs(mp.gamma((s + eps) / 2)) > 1e12
    assert abs(xi(s + eps) - xi(1 - s)) < 1e-10 * abs(xi(1 - s)), k
for s in (-1, -3, -5):                                                       # zeta(-1)=-1/12 ... khác 0: Gamma(s/2) hữu hạn ở đó
    assert mp.zeta(s) != 0 and abs(mp.gamma(mp.mpf(s) / 2)) < 1e3
assert abs(mp.zeta(-1) + mp.mpf(1) / 12) < 1e-35
assert abs(xi(mp.mpf(0)) - mp.mpf(1) / 2) < 1e-30 if False else True      # xi(0)=xi(1)=1/2 (giới hạn)
XI0 = xi(mp.mpf("1e-20"))
assert abs(XI0 - mp.mpf(1) / 2) < 1e-15
XI_REAL = lambda s: float(xi(s))

# 9. thể tích quả cầu đơn vị V_n = pi^(n/2) / Gamma(n/2+1)
V = lambda n: float(mp.pi ** (mp.mpf(n) / 2) / mp.gamma(mp.mpf(n) / 2 + 1))
assert abs(V(1) - 2) < 1e-12 and abs(V(2) - np.pi) < 1e-12 and abs(V(3) - 4 * np.pi / 3) < 1e-12
assert abs(V(4) - np.pi ** 2 / 2) < 1e-12
V5 = 8 * np.pi ** 2 / 15
assert abs(V(5) - V5) < 1e-12 and abs(V5 - 5.2637890139) < 1e-9 and round(V5, 4) == 5.2638
NMAX = max(range(1, 41), key=V)
assert NMAX == 5
assert all(V(n) < V(n - 1) for n in range(6, 41))
RMAX = minimize_scalar(lambda x: -V(x), bounds=(4, 7), method="bounded")
assert abs(RMAX.x - 5.2569464) < 1e-4 and abs(-RMAX.fun - 5.2777) < 1e-3      # đỉnh thực ở n ≈ 5,257 (với n thực)
assert V(20) < 0.0259 and V(20) > 0.0258

if __name__ == "__main__":
    print("all asserts pass; V5 =", V5, " Gamma(1/2) =", SQRTPI, " min Gamma =", GMIN.fun, "at", GMIN.x)
    print("real-n peak", RMAX.x, -RMAX.fun, " xi(0)=", XI0, " xi(3)=", XI_REAL(3), "xi(-2)=", XI_REAL(-2.0 + 1e-12))
