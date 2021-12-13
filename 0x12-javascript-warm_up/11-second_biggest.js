#!/usr/bin/node

const args = process.argv;

if (args.length > 3) {
  const li = [];
  for (let i = 2; i < args.length; i++) {
    li.push(parseInt(args[i]));
  }
  li.sort(function (a, b) { return a - b; });
  console.log(parseInt(li[li.length - 2]));
} else {
  console.log(0);
}
