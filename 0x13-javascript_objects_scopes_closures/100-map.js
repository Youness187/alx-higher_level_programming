#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((v, i) => (v * i));
console.log(list);
console.log(newList);
