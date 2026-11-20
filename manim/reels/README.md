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
