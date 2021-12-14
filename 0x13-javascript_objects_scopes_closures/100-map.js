#!/usr/bin/node

const data = require('./100-data');

const map1 = data.list.map(function (num, index) {
  return num * index;
});

console.log(data.list);
console.log(map1);
