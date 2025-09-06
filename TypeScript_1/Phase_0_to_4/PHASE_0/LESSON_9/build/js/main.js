"use strict";
const userA = { name: "Nyro", age: 20 };
function getUserName(user) {
    return user.name;
}
const userName = getUserName(userA);
console.log(userName);
