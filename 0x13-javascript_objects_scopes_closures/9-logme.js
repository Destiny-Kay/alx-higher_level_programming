#!/usr/bin/node

let argVal = 0;

function logMe (item) {
  console.log(`${argVal}: ${item}`);
  argVal++;
}

module.exports = { logMe };
