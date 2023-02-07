
const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split('\n');

let num = Number(input);

let count = 0;
let temp = num;
let step = 0;
let isNotSame = true;

while (isNotSame) {
    count++;
    if (temp < 10) {
        step = temp % 10;
    } else {
        step = Math.floor(temp / 10) + (temp % 10);
    }

    temp = (temp % 10).toString() + (step % 10).toString();
    temp = Number(temp);

    if (temp === num) {
        isNotSame = false;
    }
}

console.log(count)