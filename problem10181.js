const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().trim().split('\n');

const max = input[1].split(" ").reduce((p, c) => {
    return (p * 1) > (c * 1) ? p : c;
})

const min = input[1].split(" ").reduce((p, c) => {
    return (p * 1) < (c * 1) ? p : c;
})

console.log(min + " " + max)