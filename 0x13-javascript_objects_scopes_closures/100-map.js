#!/usr/bin/node

const data = require('./100-data');

const map2 = [];

for (let i = 0; i < data.list.length; i++) {
  const map1 = data.list.map(x => x * i);
  map2.push(map1[i]);
}

console.log(data.list);
console.log(map2);
