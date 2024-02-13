#!/usr/bin/node

const SquareE = require('./5-square');

class Square extends SquareE {
  charPrint (c) {
    let char = '';
    c === undefined
      ? char = 'X'
      : char = c;

    for (let i = 0; i < this.height; i++) {
      let squarePrint = '';
      for (let j = 0; j < this.width; j++) {
        squarePrint += char;
      }
      console.log(squarePrint);
    }
  }
}

module.exports = Square;
