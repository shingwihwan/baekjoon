const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split("\n").map(x => Number(x));

// const max = input.reduce((p, c) => {
//     return p > c ? p : c;
// })

// console.log(max)
// console.log((input.indexOf(max) + 1).toString());

const max = Math.max(...input);

console.log(max);
console.log(input.indexOf(max) + 1)