type WorkoutLevel = "easy" | "moderate" | "intense";

type WorkoutPlan = {
  title: string;
  level: WorkoutLevel;
  duration: number;
};
