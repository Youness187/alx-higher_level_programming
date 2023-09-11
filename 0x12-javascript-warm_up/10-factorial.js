#!/usr/bin/node
const argv = process.argv;
const argn = parseInt(argv[2]);
function factorial (num) {
  return num > 0 ? factorial(num - 1) * num : 1;
}

console.log(factorial(isNaN(argn) ? 1 : argn));
