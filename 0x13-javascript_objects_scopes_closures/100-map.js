#!/usr/bin/node
// a script that imports an array and computes a new array.

const list = require('./100-data.js').list;

const newList = list.map((x, i) => x * i);
console.log(list);
console.log(newList);
