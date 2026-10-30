const sample = new Date('2026-06-29T00:30:00+09:00');
console.log(sample.toISOString());
console.log(sample.toISOString().split('T')[0]);
const dateOnly = new Date('2026-06-29');
console.log(dateOnly.toISOString());
