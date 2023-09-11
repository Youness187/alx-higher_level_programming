#!/usr/bin/node
const argv = process.argv;
const num = Number(argv[2]);

console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
