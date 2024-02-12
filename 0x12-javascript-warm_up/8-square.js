#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
}
let side = '';

for (let i = 0; i < size; i++) {
  side += 'X';
}

for (let i = 0; i < size; i++) {
  console.log(side);
}
