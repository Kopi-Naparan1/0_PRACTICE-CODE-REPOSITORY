// ===== Utility Types =====
function messageLogger(message: any): void {
  console.log(message);
}

// === Partial ===
// It is just like in the CRUD the Update. Only the changed one will be changed

interface Assignment {
  studentID: string;
  title: string;
  grade: number;
  verified?: boolean;
}

function updateAssignment(
  assign: Assignment,
  propsToUpdate: Partial<Assignment>
): Assignment {
  return { ...assign, ...propsToUpdate };
}

const assign1: Assignment = {
  studentID: "1234",
  title: "Final Project",
  grade: 0,
};

messageLogger(updateAssignment(assign1, { grade: 98 }));
const assignGraded: Assignment = updateAssignment(assign1, { grade: 95 });

// === Required & Readonly ===
// If it's required then you must fill it all up regardless if it's optional or not

function recordAssignment(assign: Required<Assignment>): Assignment {
  return assign;
}

const assignVerified: Readonly<Assignment> = {
  ...assignGraded,
  verified: true,
};

// === Record Type ===
// You can use type for the keys and the values.

const hexColorMap: Record<string, string> = {
  red: "FF0000",
  green: "00FF00",
  blue: "0000FF",
};

type Student = "Sara" | "Kelly";
type LetterGrades = "A" | "B" | "C" | "D" | "U";

// key: value of string
const finalGrades: Record<Student, LetterGrades> = {
  Sara: "C",
  Kelly: "U",
};

// key: value of object
interface Grades {
  assign1: number;
  assign2: number;
}

const gradeData: Record<Student, Grades> = {
  Sara: { assign1: 90, assign2: 99 },
  Kelly: { assign1: 75, assign2: 53 },
};

// ===== Pick and Omit =====
// Pick: you pick which object. Omit: you don't include a key of the object.
type AssignResult = Pick<Assignment, "studentID" | "grade">;

const score: AssignResult = {
  studentID: "K123",
  grade: 90,
};

type AssignPreview = Omit<Assignment, "grade" | "verified">;

const preview: AssignPreview = {
  studentID: "k123",
  title: "Final Project",
};

// === Exclude and Extract ===
// Choosing a certain kinds of variable based on exclusion and extraction

type adjustedGrade = Exclude<LetterGrades, "U">;

type HighGrades = Extract<LetterGrades, "A" | "B">;

// === Nonnullable ===
// Only include the truthy data types

type AllPossibleGrades = "Dave" | "Nyro" | null | undefined;

type NamesOnly = NonNullable<AllPossibleGrades>;

// === ReturnType ===

const createNewAssign = (title: string, points: number) => {
  return { title, points };
};

type newAssign = ReturnType<typeof createNewAssign>; // 1) Basically, whatever the return type of the function will be into the variable

const tsAssign: newAssign = createNewAssign("Utility Types", 100); //  2) The variable must be in that type

// === Paramaters ===
// What ever the type of the returned will be the type of the parameters

type AssignParams = Parameters<typeof createNewAssign>;

const assignArgs: AssignParams = ["Generics", 100];

const tsAssign2: newAssign = createNewAssign(...assignArgs);
messageLogger(tsAssign2);

// === Awaited ===
// ReturnType of a promise

interface User {
  id: number;
  name: string;
  username: string;
  email: string;
}

async function fetchUsers(): Promise<User[]> {
  const data = await fetch("https://something.com")
    .then((res) => {
      return res.json();
    })
    .catch((err) => {
      if (err instanceof Error) console.log(err.message);
    });
  return data;
}

type FetchUsersReturnType = Awaited<ReturnType<typeof fetchUsers>>;

fetchUsers().then((users) => console.log(users));
