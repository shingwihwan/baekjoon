const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().split('\n');

let answer = "";
for (let i = 0; i < input[0]; i++) {
    const nums = input[i + 1].split(" ");
    answer += parseInt(nums[0]) + parseInt(nums[1]) + "\n";
}
console.log(answer);