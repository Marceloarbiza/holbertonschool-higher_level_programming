#!/usr/bin/node

const c = 'C is fun';
const args = process.argv;

if (args[2] == null) {
  console.log('Missing number of occurrences');
} else if (parseInt(args[2]) > 0) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log(c);
  }
}
