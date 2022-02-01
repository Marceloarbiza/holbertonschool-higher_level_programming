#!/usr/bin/node
/* Write a script that reads and prints the content of a file */

const filename = process.argv.slice(2)[0];

const fs = require('fs');

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
