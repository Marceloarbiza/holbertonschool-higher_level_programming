#!/usr/bin/node

const data = require('./101-data');

const dictD = data.dict;

let newDict = {};

for (let item in dictD){
	/*console.log('key:' + item + ' value:' + dictD[item]);*/
	newDict[dictD[item]] = item;
}
console.log(dictD);
console.log(newDict);
