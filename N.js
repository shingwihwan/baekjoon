const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().split('\n');

let answer = "";

for (let i = input[0]; i > 0; i--) {
    answer += i + "\n"
}

console.log(answer);