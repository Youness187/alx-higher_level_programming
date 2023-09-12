#!/usr/bin/node
const sq = require('./5-square');
class Square extends sq {
  charPrint (c) {
    if (c === undefined) this.print();
    else for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
  }
}
module.exports = Square;
