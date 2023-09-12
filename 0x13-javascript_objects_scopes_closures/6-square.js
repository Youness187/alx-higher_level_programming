#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let w = new Array(this.width);
    w = w.fill(c).join('');
    for (let i = 0; i < this.height; i++) console.log(w);
  }
}
module.exports = Square;
