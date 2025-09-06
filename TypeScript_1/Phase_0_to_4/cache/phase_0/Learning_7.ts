// ===== Learning 7: Generics =====

function messageLogger(message: any): void {
  console.log(message);
}

// ===== Example 1 =====

// Only object are true
function Test<out>(argument: out): boolean {
  return (
    typeof argument === "object" &&
    !Array.isArray(argument) &&
    argument !== null
  );
}

// ===== Example 2 =====

// Get only the boolean 'true'
// The <Type> is a generic. "Whatever the type of the argument will be remembered"
function isTrue<Type>(argument: Type): { argument: Type; is: boolean } {
  if (Array.isArray(argument) && !argument.length) {
    return { argument, is: false };
  }
  if (
    Test(argument) &&
    // Record<keys, type> -> they keys must only what you passed and the type is the value of the key
    Object.keys(argument as Record<string, unknown>).length === 0
  ) {
    return { argument, is: false };
  }
  return { argument, is: !!argument };
}

// ===== Example 3 using extends 1.0 =====

interface HasID {
  id: number;
}

function processUser<T extends HasID>(user: T): T {
  return user;
}

// ===== Example 4 using extends 2.0 =====

// The idea is you type check each of the keys and values in the array o
function getUsersProperty<T extends HasID, K extends keyof T>(
  users: T[],
  key: K
): T[K][] {
  return users.map((user) => user[key]);
}


messageLogger(isTrue(false));
messageLogger(isTrue(true));
messageLogger(isTrue("John"));
messageLogger(isTrue([1, 2, 3]));
messageLogger(isTrue({ name: "John" }));
messageLogger(isTrue(null));

messageLogger(processUser({ id: 1, name: "nyro" }));
messageLogger(processUser({ id: 2, name: "nyrao" }));
