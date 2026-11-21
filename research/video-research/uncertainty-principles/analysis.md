# Analysis — uncertainty principles

Reconstructed knowledge (not transcript dump). Cross-checked against Hall, standard Fourier conventions, Cohen arXiv:2305.05022, Quanta 2026-08-12.

## Definitions

- **Heisenberg–Kennard (QM).** For a unit vector $$\psi$$ in the domain of $$X$$ and $$P=-i\hbar\partial_x$$, $$\sigma_X(\psi)\sigma_P(\psi)\ge\hbar/2$$.
- **Fourier / Pauli–Weyl.** With $$\hat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx$$, a Schwartz $$f$$ satisfies $$\|xf\|_2\|\xi\hat f\|_2\ge(1/4\pi)\|f\|_2^2$$. Gaussians (modulo translate, modulate, chirp) are minimizers.
- **Robertson–Schrödinger.** For self-adjoint $$A,B$$, $$\sigma_A\sigma_B\ge\tfrac12\bigl|\langle[A,B]\rangle\bigr|$$ (stronger form adds a covariance term).
- **CCR / Weyl.** $$[X,P]=i\hbar$$ on a dense domain; the exponentiated **Weyl relations** are the honest uniqueness input for **Stone–von Neumann**.
- **Fractal uncertainty (slogan).** A function and its Fourier transform cannot both concentrate near fractal sets that are *line-porous*.
- **Line porosity (Cohen).** Every line meets the set in a quantitatively porous (many-holes) way. Ordinary Sierpiński carpets that contain full lines are excluded.

## Theorems vs open

| Claim | Status (2026-08) |
|-------|------------------|
| Kennard / Robertson | Theorem |
| Stone–von Neumann (Weyl form, finite degrees of freedom) | Theorem |
| Energy–time as $$[H,T]=i\hbar$$ | **Not** a theorem of that form |
| Donoho–Stark discrete UP | Theorem (1989) |
| Entropic UP (Maassen–Uffink; Beckner–Hirschman Fourier) | Theorem |
| FUP in 1D (Bourgain–Dyatlov) | Theorem (2016/17) |
| FUP in higher D under line porosity (Cohen) | Theorem (*Annals* 2025; arXiv 2023) |
| Waves on hyperbolic surfaces cannot hide (Dyatlov–Jin; Kim–Miller) | Theorem (uses FUP) |
| Quantum unique ergodicity (Rudnick–Sarnak) | **Open** |

## Confusions to kill in lessons

1. Observer-effect microscope story ≠ variance inequality.
2. Energy–time is a family of different inequalities (e.g. Mandelstam–Tamm), not CCR.
3. Not every fractal obeys FUP; line obstruction is real.
4. Heisenberg is not chaos and not the second law.

## Proof ideas (literacy, not Annals)

- Robertson: Cauchy–Schwarz on $$A\psi$$ and $$B\psi$$ after centering means.
- Fourier UP: same, because $$P$$ is Fourier-multiplication by frequency.
- FUP 1D: isolate peaks by a damping multiplier, show each piece of $$\hat f$$ spreads, so $$\hat f$$ cannot vanish on a porous set often enough.
- Cohen: higher-dimensional **Beurling–Malliavin multiplier** to build the damping function; Bourgain’s unpublished notes pointed at this complex-analysis detour.
