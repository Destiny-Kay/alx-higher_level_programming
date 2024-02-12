#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (a) {
  let fact = 1;
  if (isNaN(a)) {
    return fact;
  } else {
    for (let i = a; i > 0; i--) {
      fact *= i;
    }
    return fact;
  }
}

console.log(factorial(num));
