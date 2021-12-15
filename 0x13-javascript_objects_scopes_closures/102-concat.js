#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

let info = fs.readFileSync(args[2], 'utf8');
info += fs.readFileSync(args[3], 'utf8');

fs.writeFileSync(args[4], info);
