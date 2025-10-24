export default function totalExpenses(db) {
  let total = db.reduce((a, b) => a + b, 0);
  return total;
}
