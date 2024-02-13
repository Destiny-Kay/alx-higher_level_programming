#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectDrawing = '';
      for (let j = 0; j < this.width; j++) {
        rectDrawing += 'X';
      }
      console.log(rectDrawing);
    }
  }

  rotate () {
    const height = this.height;
    const width = this.width;
    this.height = width;
    this.width = height;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
