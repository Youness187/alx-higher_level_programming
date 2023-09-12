#!/usr/bin/node
const dict = require('./101-data').dict;
const vals = Object.values(dict);
const keys = Object.keys(dict);
const newDict = {};

for (const key of vals) {
  newDict[key] = keys.filter((val) => dict[val] === key);
}

console.log(newDict);
