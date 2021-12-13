#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);

function factorial (b) {
  if (isNaN(x)) {
    return 1;
  }
  if (b > 0) {
    return b * factorial(b - 1);
  } else {
    return 1;
  }
}

console.log(factorial(x));
