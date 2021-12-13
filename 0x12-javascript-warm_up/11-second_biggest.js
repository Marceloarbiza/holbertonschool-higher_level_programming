#!/usr/bin/node

const args = process.argv;

if (args[2] == null || parseInt(args[2]) === 1) {
  console.log(0);
} else {
  args.splice(0, 2);
  args.sort();
  console.log(parseInt(args[args.length - 2]));
}
