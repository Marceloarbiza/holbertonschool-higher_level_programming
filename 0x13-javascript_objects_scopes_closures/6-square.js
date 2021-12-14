#!/usr/bin/node

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    let s = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c == null) {
          s += 'X' + '';
        } else {
          s += c + '';
        }
      }
      console.log(s);
      s = '';
    }
  }
};
