#!/usr/bin/node
const args = process.argv;

let max = 0;
let secondMax = 0;
let i = 2;
let j = 2;
console.log(args)
while (args[i]) {
  if (args[i] > max) {
    secondMax = max;;
    max = args[i];
  } else if (args[i] > secondMax && args[i] < max) {
    secondMax = args[i];
  }
  i++;
}

console.log(secondMax);
