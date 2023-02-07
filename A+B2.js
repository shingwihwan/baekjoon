const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().split('\n');

let answer = "";

for (let i = 1; i <= input[0]; i++) {
    let nums = input[i].split(" ")
    answer += `Case #${i}: ${Number(nums[0]) + Number(nums[1])}` + "\n"
}

console.log(answer)
