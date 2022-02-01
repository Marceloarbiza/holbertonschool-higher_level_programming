#!/usr/bin/node
/* Write a script that reads and prints the content of a file */

const filename = process.argv.slice(2)[0];

const content = process.argv.slice(2)[1];

const fs = require('fs');

fs.writeFile(filename, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
