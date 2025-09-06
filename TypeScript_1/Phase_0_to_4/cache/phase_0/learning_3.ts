// ===== Lesson 3 Function =====
type stringOrNumberArray = (string | number)[]; //type

interface Guitarist {
  name: string;
  active: boolean;
  albums: stringOrNumberArray;
}

const guitarist1: Guitarist = {
  name: "Nyro",
  active: true,
  albums: ["sooong", "Yeaah"],
};

function greetGuitarist(guitarist: Guitarist): string {
  return `Hi there ${guitarist.name}!`;
}

console.log(greetGuitarist(guitarist1));

// ===== void ===== -> function that has no return

function logMessage(message: any): void {
  console.log(message);
}

function add(x: number, y: number): number {
  return x + y;
}

logMessage("Hello");
logMessage(add(5, 5));

// ===== parameter alias =====

type mathParameter = (x: number, y: number) => number;

const multipy: mathParameter = (x, y) => {
  return x * y;
};

logMessage(multipy(5, 10));

// ===== optional parameters =====

function sum(a: number, b: number, c?: number): number {
  if (c) {
    return a + b + c;
  }
  return a + b;
}

function product(a: number, b: number, c: number = 10): number {
  return a * b * c;
}

logMessage(sum(5, 10));
logMessage(product(5, 10, 100));

// ===== Rest Parameters =====

function manySum(num: number, ...nums: number[]): number {
  return num * nums.reduce((previous, current) => previous + current);
}

logMessage(manySum(10, 5, 67, 84, 532, 8));

// ===== never Type ===== -> -> functions that return errors

function createError(errorMsg: string): never {
  throw new Error(errorMsg);
}
