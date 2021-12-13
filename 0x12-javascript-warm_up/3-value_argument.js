#!/usr/bin/node

const args = process.argv;

if (args[2] == null) {
  console.log('No argument');
} else {
  for (let i = 2; i < args.length; i++) {
    console.log(args[i]);
  }
}
