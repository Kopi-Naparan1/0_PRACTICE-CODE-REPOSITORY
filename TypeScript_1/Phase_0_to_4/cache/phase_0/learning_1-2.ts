// ===== Lesson 01 - Data Types ======

// let myName: string = "Dave";
// let myAge: number;
// let isAlive: boolean | number;
// let album: string | number;

// myAge = 90;
// isAlive = true;
// myName = "Go";
// album = "banana";

// function add(x: number, y: number): number {
//   return x + y;
// }

// const sum1 = add(30, 10);
// console.log(sum1);

// ===== Lesson 02 - Arrays, tuples, objects, type, Enums =====

// ===== Array =====
let stringArr = ["one", "two", "three"];

let guitar = ["strat", "Les paul", 123];

let mixedData = ["EVH", 1927, true];

stringArr.push("hahah");
guitar.push(12);
mixedData.push(false);

mixedData = stringArr;

let test: (string | number)[] = [];

test.unshift("string", 19);

// ===== Tuple =====
let myTuple: [string, boolean] = ["string", true];

let testTyple: [string, string, boolean] = ["a", "b", true];

// ===== Object =====
let myObj: object;
myObj = [];
console.log(typeof myObj);

const exampleObject = {
  Name: "Nyro",
  age: 20,
  isActive: true,
};

console.log(exampleObject.Name);

// ===== type ======

type Guitarist = {
  name: string;
  age: number;
  isActive: boolean;
  songs: string[];
  wife?: string;
};

const guitarist1: Guitarist = {
  name: "Nyro Khufraleq",
  age: 22,
  isActive: false,
  songs: ["River", "flows", "you"],
  wife: "Wife A",
};

const guitarist2: Guitarist = {
  name: "Nyro KAKAKA",
  age: 26,
  isActive: true,
  songs: ["Rock", "flows", "you"],
};

console.log(
  `${guitarist1.name} ${guitarist1.age} ${guitarist1.isActive} ${guitarist1.songs} `
);

console.log(
  `${guitarist2.name} ${guitarist2.age} ${guitarist2.isActive} ${guitarist2.songs}`
);

// function try
function guitaristMaker(guitarist: Guitarist): string {
  if (!guitarist.wife) {
    return `${guitarist.name} ${guitarist.age}  ${guitarist.isActive} ${guitarist.songs}`;
  }
  return `${guitarist.name} ${guitarist.age}  ${guitarist.isActive} ${guitarist.songs} ${guitarist.wife}`;
}

console.log(guitaristMaker(guitarist1));

// ===== Enums

enum Grade {
  U = 1,
  D,
  C,
  B,
  A,
}

console.log(Grade.C);
