#!/usr/bin/node
const args = process.argv;

function len (arr) {
  let i = 0;
  let arrLength = 0;
  while (arr[i]) {
    arrLength++;
    i++;
  }
  return arrLength;
}

if (len(args) <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
