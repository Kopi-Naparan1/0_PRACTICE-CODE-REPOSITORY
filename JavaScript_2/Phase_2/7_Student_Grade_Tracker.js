function studentMaker(name, age, grade1, grade2, grade3) {
  const grades = [grade1, grade2, grade3];
  return {
    name: name,
    age: age,
    grade: grades,
    average: grades.reduce((a, b) => a + b, 0) / grades.length,
  };
}

function main() {
  const s1 = studentMaker("A", 19, 95, 96, 91);
  const s2 = studentMaker("B", 19, 95, 92, 91);
  const s3 = studentMaker("C", 19, 87, 89, 91);

  const students = [s1, s2, s3];

  for (let i = 0; i < students.length; i++) {
    console.log(students[i].name);
    console.log(students[i].age);
    console.log(students[i].grade);
    console.log(
      `${students[i].name} has an average grade of ${students[
        i
      ].average.toFixed(2)}`
    );
    console.log("\n");
  }
}

main();
