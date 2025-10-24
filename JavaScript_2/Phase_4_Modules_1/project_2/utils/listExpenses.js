export default function listExpenses(db) {
  for (let i = 0; i < db.length; i++) {
    console.log(`[${i + 1}] ${db[i]}\n`);
  }
}
