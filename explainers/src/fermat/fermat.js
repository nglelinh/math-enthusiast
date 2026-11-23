export const PRESETS = {
  pythagoras: {
    label: { vi: 'n = 2: Bộ ba Pytago (3, 4, 5)', en: 'n = 2: Pythagorean triple (3, 4, 5)' },
    a: 3, b: 4, c: 5, n: 2,
  },
  nearmiss: {
    label: { vi: 'n = 12: Gần đúng 1782¹² + 1841¹² vs 1922¹²', en: 'n = 12: Near-miss 1782¹² + 1841¹² vs 1922¹²' },
    a: 1782, b: 1841, c: 1922, n: 12,
  },
  frey: {
    label: { vi: 'n = 5: Phản chứng Wiles (giả sử có nghiệm)', en: 'n = 5: Wiles contradiction (suppose a solution)' },
    a: 2, b: 3, c: 4, n: 5,
  },
};

export function checkFermat(a, b, c, n) {
  const lhs = BigInt(a) ** BigInt(n) + BigInt(b) ** BigInt(n);
  const rhs = BigInt(c) ** BigInt(n);
  return { eq: lhs === rhs, diff: lhs - rhs };
}

export function freyDiscriminantSign(a, b, c) {
  // Δ = 16 (abc)^{2p} > 0 for nonzero a,b,c
  return a > 0 && b > 0 && c > 0;
}

export function steps(presetKey = 'frey', lang = 'vi') {
  const p = PRESETS[presetKey] || PRESETS.frey;
  if (presetKey === 'pythagoras') {
    const chk = checkFermat(p.a, p.b, p.c, p.n);
    return [
      {
        stage: 0, ok: true,
        msg: lang === 'vi'
          ? `Với n = 2: 3² + 4² = 9 + 16 = 25 = 5² (khớp tuyệt đối!). Có vô hạn nghiệm nguyên.`
          : `For n = 2: 3² + 4² = 9 + 16 = 25 = 5² (exact match!). Infinitely many integer solutions exist.`,
      },
      {
        stage: 1, ok: true,
        msg: lang === 'vi'
          ? `Đường cong Frey chỉ dùng để phủ định nghiệm khi n ≥ 3 (vì khi đó số mũ p lẻ ≥ 3 làm biến dạng tính số học của đường cong).`
          : `The Frey curve argument targets n ≥ 3 (where odd prime p ≥ 3 forces impossible arithmetic properties).`,
      },
    ];
  }

  if (presetKey === 'nearmiss') {
    const chk = checkFermat(p.a, p.b, p.c, p.n);
    return [
      {
        stage: 0, ok: false,
        msg: lang === 'vi'
          ? `Trên máy tính bỏ túi trông như 1782¹² + 1841¹² = 1922¹², nhưng kiểm tra modulo 2 cho thấy chẵn + lẻ = lẻ ≠ chẵn!`
          : `On a calculator 1782¹² + 1841¹² looks equal to 1922¹², yet mod 2 gives even + odd = odd ≠ even!`,
      },
      {
        stage: 1, ok: false,
        msg: lang === 'vi'
          ? `Tính chính xác số nguyên lớn: hiệu ≠ 0 (lệch ở các chữ số thấp hơn). Không tồn tại nghiệm cho n ≥ 3!`
          : `Exact BigInt check: difference ≠ 0. No solutions exist for any n ≥ 3!`,
      },
    ];
  }

  // frey proof skeleton
  return [
    {
      stage: 0, ok: null,
      msg: lang === 'vi'
        ? 'Bước 1 (Giả sử phản chứng): Giả sử tồn tại aᵖ + bᵖ = cᵖ với số nguyên tố lẻ p ≥ 5.'
        : 'Step 1 (Suppose for contradiction): Suppose aᵖ + bᵖ = cᵖ for an odd prime p ≥ 5.',
    },
    {
      stage: 1, ok: null,
      msg: lang === 'vi'
        ? 'Bước 2 (Đường cong Frey): Dựng E: y² = x(x − aᵖ)(x + bᵖ). Đây là đường cong elliptic nửa ổn định.'
        : 'Step 2 (Frey curve): Build E: y² = x(x − aᵖ)(x + bᵖ), a semistable elliptic curve.',
    },
    {
      stage: 2, ok: null,
      msg: lang === 'vi'
        ? 'Bước 3 (Định lý Ribet 1986): Nếu E là modular, nó phải ứng với dạng modular bậc N = 2 — nhưng không tồn tại dạng nào như vậy!'
        : 'Step 3 (Ribet 1986): If E is modular, level-lowering forces a weight-2 modular form of level N = 2 — none exists!',
    },
    {
      stage: 3, ok: true,
      msg: lang === 'vi'
        ? 'Bước 4 (Wiles & Taylor 1995): Mọi đường cong elliptic nửa ổn định đều modular ⇒ E không thể tồn tại ⇒ Vô nghiệm!'
        : 'Step 4 (Wiles & Taylor 1995): Every semistable elliptic curve is modular ⇒ E cannot exist ⇒ QED!',
    },
  ];
}
