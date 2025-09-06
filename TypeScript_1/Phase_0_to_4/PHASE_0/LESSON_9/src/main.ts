type User = {
  name: string;
  age: number;
};

const userA: User = { name: "Nyro", age: 20 };

function getUserName(user: User): string {
  return user.name;
}

const userName: string = getUserName(userA);
console.log(userName);
