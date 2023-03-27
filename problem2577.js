const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split("\n").map(x => Number(x));

const one = input[0];
const two = input[1];
const three = input[2];

const cons = (one * two * three).toString().split('');

for (let i = 0; i < 10; i++) {
    console.log(cons.filter((v) => v === i.toString()).length)
}