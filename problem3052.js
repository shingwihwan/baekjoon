const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split("\n").map(x => Number(x));

for (let i = 0; i < 10; i++) {
    console.log(input[i] % 42)
}