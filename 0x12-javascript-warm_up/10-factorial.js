#!/usr/bin/node
const argv = process.argv;
const argn = parseInt(argv[2]);
const factorial = (num) => {
  if (num > 0) return factorial(num - 1) * num;
  return 1;
};

console.log(factorial(isNaN(argn) ? 1 : argn));
