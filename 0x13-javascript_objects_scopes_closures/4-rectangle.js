#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
	let tmpH = this.height;
	this.height = this.width;
	this.width = tmpH;
  }

  double () {
	this.width = this.width * 2;
	this.height = this.height * 2;
  }

  print () {
    let s = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        s += 'X' + '';
      }
      console.log(s);
      s = '';
    }
  }
};
