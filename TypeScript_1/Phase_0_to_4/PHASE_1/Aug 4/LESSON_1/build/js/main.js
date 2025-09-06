"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// ===== Utility Types =====
function messageLogger(message) {
    console.log(message);
}
function updateAssignment(assign, propsToUpdate) {
    return Object.assign(Object.assign({}, assign), propsToUpdate);
}
const assign1 = {
    studentID: "1234",
    title: "Final Project",
    grade: 0,
};
messageLogger(updateAssignment(assign1, { grade: 98 }));
const assignGraded = updateAssignment(assign1, { grade: 95 });
// === Required & Readonly ===
// If it's required then you must fill it all up regardless if it's optional or not
function recordAssignment(assign) {
    return assign;
}
const assignVerified = Object.assign(Object.assign({}, assignGraded), { verified: true });
// === Record Type ===
// You can use type for the keys and the values.
const hexColorMap = {
    red: "FF0000",
    green: "00FF00",
    blue: "0000FF",
};
// key: value of string
const finalGrades = {
    Sara: "C",
    Kelly: "U",
};
const gradeData = {
    Sara: { assign1: 90, assign2: 99 },
    Kelly: { assign1: 75, assign2: 53 },
};
const score = {
    studentID: "K123",
    grade: 90,
};
const preview = {
    studentID: "k123",
    title: "Final Project",
};
// === ReturnType ===
const createNewAssign = (title, points) => {
    return { title, points };
};
const tsAssign = createNewAssign("Utility Types", 100); //  2) The variable must be in that type
const assignArgs = ["Generics", 100];
const tsAssign2 = createNewAssign(...assignArgs);
messageLogger(tsAssign2);
function fetchUsers() {
    return __awaiter(this, void 0, void 0, function* () {
        const data = yield fetch("https://something.com")
            .then((res) => {
            return res.json();
        })
            .catch((err) => {
            if (err instanceof Error)
                console.log(err.message);
        });
        return data;
    });
}
fetchUsers().then((users) => console.log(users));
