// ===== Learning 6:  Index Signatures & keyof Assertions =====

function messageLogger(message: any): void {
  console.log(message);
}

// ===== A. Index Signatures ===== -> useful for accessing dynamically a value of an object.

// ===== Example 1 =====

interface Transactions {
  [index: string]: number; // key is string and returns a type of number
}

const todaysTransaction: Transactions = {
  Pizza: -10,
  Books: 20,
  Job: 30,
};

function todaysTotalTransaction(transactions: Transactions): number {
  let total = 0;
  for (const transaction in transactions) {
    total += transactions[transaction];
  }
  return total;
}

messageLogger(todaysTotalTransaction(todaysTransaction));

// ===== Example 2 ===== -> with optional nad arrays

interface Student {
  [index: string]: string | number | number[] | undefined;
  name: string;
  GPA: number;
  classes?: number[];
}

const student1: Student = {
  name: "Nyro",
  GPA: 1.2,
  classes: [60, 40, 60, 30],
};

messageLogger(student1.name);

// ====== Example 2.5 ===== -> looping through the object
function keyValuePairFormatter(student: Student): string | undefined {
  if (student) {
    for (const key in student) {
      messageLogger(`${key}: ${student[key]}`);
    }
  } else {
    return `Error: student doesnt exist`;
  }
}

keyValuePairFormatter(student1);

// ===== B. keyof Assertions =====

function logStudentKey(student: Student, key: keyof Student): void {
  console.log(`${key}: ${student[key]}`);
}

logStudentKey(student1, "GPA");

// ===== another one.1 =====

type Streams = "salary" | "bonus" | "sidehustle";
type Incomes = Record<Streams, number | number>;

const montlyIncomes: Incomes = {
  salary: 500,
  bonus: 100,
  sidehustle: 250,
};

for (const revenue in montlyIncomes) {
  console.log(montlyIncomes[revenue as keyof Incomes]);
}
