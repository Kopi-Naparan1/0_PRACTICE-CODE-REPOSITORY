// ===== Learning 5: CLASS =====

function messageLogger(message: any): void {
  console.log(message);
}

// ===== Making Parent Class

// class Coder {
//   constructor(
//     public readonly name: string,
//     public music: string,
//     private age: number,
//     protected language: string = "TypeScript"
//   ) {
//     this.name = name;
//     this.music = music;
//     this.age = age;
//     this.language = language;
//   }

//   public getAge() {
//     return `Hello, I'm ${this.age}`;
//   }
// }

// const Nyro = new Coder("Nyro", "RNB", 20, "English");

// messageLogger(Nyro.getAge());

// // ===== Making Sub-Class =====
// class WebDev extends Coder {
//   constructor(
//     public computer: string,
//     name: string,
//     music: string,
//     age: number
//   ) {
//     super(name, music, age);
//     this.computer = computer;
//   }

//   public getLanguage() {
//     return `I write ${this.language}`;
//   }
// }

// const Khufraleq = new WebDev("LOQ", "Khufraleq", "RNB", 25);
// messageLogger(Khufraleq.getLanguage());
// messageLogger(Khufraleq.getAge());

// ===== Using Interface to a Class =====

// interface Musician {
//   name: string;
//   age: number;
//   instrument: string;
//   genre: string;
//   play(action: string): string;
// }

// class Guitarist implements Musician {
//   constructor(
//     public name: string,
//     public age: number,
//     public instrument: string,
//     public genre: string
//   ) {
//     this.name = name;
//     this.age = age;
//     this.instrument = instrument;
//     this.genre = genre;
//   }
//   play(action: string): string {
//     return `${this.name} ${this.age} year old ${action} the ${this.instrument}`;
//   }
// }

// const Henson = new Guitarist("Tim Henson", 20, "Electric Guitar", "Rock");

// messageLogger(Henson.play("pick"));

// ===== static number =====

class People {
  static count: number = 0;

  static getCount(): number {
    return People.count;
  }

  public id: number;

  constructor(public name: string) {
    this.name = name;
    this.id = ++People.count;
  }

  public getPersonID() {
    return `${this.name} ID: ${this.id}`;
  }
}

const personA = new People("Nyro");
const personB = new People("Khufraleq");
const personC = new People("Guveek");

messageLogger(personA.getPersonID());
messageLogger(personB.getPersonID());
messageLogger(personC.getPersonID());

// ===== Getters and Setters

class Bands {
  private dataState: string[];

  constructor() {
    this.dataState = [];
  }

  public get data(): string[] {
    return this.dataState;
  }

  public set data(value: string[]) {
    if (
      Array.isArray(value) &&
      value.every((item) => typeof item === "string")
    ) {
      this.dataState = value;
      return;
    } else throw new Error("Parameter is not an array of strings");
  }
}

const bands = new Bands();
bands.data = ["Polyphia", "Queen", "One Direction"];
messageLogger(bands.data);
