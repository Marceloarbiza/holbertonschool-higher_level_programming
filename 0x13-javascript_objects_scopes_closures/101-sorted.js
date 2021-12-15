#!/usr/bin/node

const data = require('./101-data');

const dictD = data.dict;

const newDict = {};

for (const key in dictD) {
  if (!newDict[dictD[key]]) {
    newDict[dictD[key]] = [key];
  } else {
    newDict[dictD[key]].push(key);
  }
}
console.log(newDict);
