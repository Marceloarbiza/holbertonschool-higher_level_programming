#!/usr/bin/node

const args = process.argv;
let s = '';
if ((args[2] == null) || (isNaN(parseInt(args[2])))) {
  console.log('Missing size');
} else if (parseInt(args[2]) > 0) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    for (let j = 0; j < parseInt(args[2]); j++) {
      s += 'X' + '';
    }
    console.log(s);
    s = '';
  }
}
