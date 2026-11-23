export const PRESETS = {
  safeFlip: {
    label: { vi: 'Danh sách 6 số thực (lật an toàn 1 / 2)', en: '6 real numbers (safe flip 1 / 2)' },
    rows: [
      [3, 1, 4, 1, 5, 9],
      [2, 7, 1, 8, 2, 8],
      [1, 4, 1, 4, 2, 1],
      [0, 5, 7, 7, 2, 1],
      [6, 1, 8, 0, 3, 3],
      [9, 9, 9, 1, 2, 4],
    ],
  },
  pitfall09: {
    label: { vi: 'Bẫy 0,999... = 1,000... (cần tránh 0 và 9)', en: 'Pitfall 0.999... = 1.000... (avoid 0 & 9)' },
    rows: [
      [2, 0, 0, 0, 0, 0],
      [8, 9, 9, 9, 9, 9],
      [1, 1, 9, 9, 9, 9],
      [4, 2, 3, 9, 9, 9],
      [5, 6, 7, 8, 9, 9],
      [7, 3, 2, 4, 5, 9],
    ],
  },
};

export function diagonalDigits(rows) {
  return rows.map((r, i) => (r[i] === 1 ? 2 : 1));
}

export function steps(presetKey = 'safeFlip', lang = 'vi') {
  const pr = PRESETS[presetKey] || PRESETS.safeFlip;
  const rows = pr.rows;
  const y = diagonalDigits(rows);
  const out = [
    {
      activeRow: -1,
      built: [],
      msg: lang === 'vi'
        ? 'Giả sử liệt kê được mọi số trong (0, 1) thành một danh sách đếm được. Ta sẽ dựng số y nằm ngoài danh sách!'
        : 'Suppose we listed every number in (0, 1). We will construct y missing from the list!',
    },
  ];
  for (let i = 0; i < rows.length; i++) {
    const d = rows[i][i];
    const yi = y[i];
    out.push({
      activeRow: i,
      built: y.slice(0, i + 1),
      msg: lang === 'vi'
        ? `Hàng ${i + 1}: chữ số đường chéo là ${d} ⇒ chọn y[${i + 1}] = ${yi} (≠ ${d}). Vậy y ≠ hàng ${i + 1}!`
        : `Row ${i + 1}: diagonal digit is ${d} ⇒ pick y[${i + 1}] = ${yi} (≠ ${d}). So y ≠ row ${i + 1}!`,
    });
  }
  out.push({
    activeRow: rows.length,
    built: y.slice(),
    msg: lang === 'vi'
      ? `Hoàn tất: y = 0,${y.join('')}... chỉ dùng chữ số {1, 2} (tránh đuôi 000.../999...) nên thực sự khác mọi hàng!`
      : `Done: y = 0.${y.join('')}... uses only {1, 2} (avoids 000.../999... ambiguity), so y differs from every row!`,
  });
  return out;
}
