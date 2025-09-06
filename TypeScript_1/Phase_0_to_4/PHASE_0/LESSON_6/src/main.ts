// Array
type Exercise = {
  name: string;
  reps: number;
};

const circuit: Exercise[] = [
  { name: "Running", reps: 10 },
  { name: "Swimming", reps: 5 },
];

// Tuple

type TimerRange = [number, number];
const timer: TimerRange[] = [
  [1, 10],
  [11, 20],
  [21, 30],
];
