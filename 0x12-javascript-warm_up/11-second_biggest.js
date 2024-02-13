#!/usr/bin/node
const args = process.argv;

let max = 0;
let secondMax = 0;
let i = 2;
let j = 2;

while (args[i]) {
  if (args[i] > max) {
    max = args[i];
  }
  i++;
}

while (args[j]) {
  if (args[j] < max && args[j] > secondMax) {
    secondMax = args[j];
  }
  j++;
}
console.log(secondMax);
