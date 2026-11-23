# Short Manim reels (1080x1920, dark background, no music)

Source for the `### Video ngắn` / `### Short video` clips in the lessons.
Render both languages: `REEL_LANG=vi|en manim -qh <file>.py <Scene>`
(9x16 frame, 1 unit = 120 px, background #10121a). Captions live in the `TX` dict of each scene; numbers are asserted inside each scene.
Compress: ffmpeg -i in.mp4 -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart -an out.mp4
Output: public/videos/reels/<slug>_<lang>.mp4

| scene file | class | slug |
|---|---|---|
| collatz.py | Collatz | collatz-orbit-97 |
| cantor.py | Cantor | cantor-diagonal |
| sqrt2.py | Sqrt2 | sqrt2-irrational-squares |
| logistic.py | Logistic | logistic-two-orbits |
| chaosgame.py | ChaosGame | chaos-game-sierpinski |
| fourier.py | Fourier | square-wave-fourier |
| packing.py | Packing | disc-packing-2d |
| konigsberg.py | Konigsberg | konigsberg-bridges |

## Batch 2 (needs `common_b.py`; same render/compress recipe)

| scene file | class | slug |
|---|---|---|
| euler.py | Euler | zeta-euler-product |
| twins.py | Twins | twin-primes-count |
| kakeya.py | Kakeya | kakeya-deltoid-needle |
| clt.py | CLT | clt-dice-bell |
| dh.py | DH | diffie-hellman-mod23 |
| hilbert.py | Hilbert | hilbert-curve |
| ball.py | Ball | ball-volume-dimensions |
| life.py | Life | life-r-pentomino |
| catenoid.py | Catenoid | soap-film-catenoid |
| sir.py | SIR | sir-r0-epidemic |
| ot.py | OT | optimal-transport-1d |
| chsh.py | CHSH | chsh-bell-game |

Every scene asserts its numbers before drawing (e.g. twin counts 8/35/205/1224/8169, deltoid area = pi/8 and chords inside the curve, 5 is a primitive root mod 23, R-pentomino has 116 cells at generation 1103, catenoid limits 0.6627 and Goldschmidt 0.528, CHSH = 2 sqrt 2 via the Phi+ state).

## Batch 3 (uses `common_b.py`; same render/compress recipe)

| scene file | class | slug |
|---|---|---|
| pagerank.py | PageRank | pagerank-markov |
| fourcolor.py | FourColor | four-color-kempe |
| zkp.py | ZKP | zkp-3color |
| tarjan.py | TarjanSCC | tarjan-scc |
