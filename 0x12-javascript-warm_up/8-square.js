#!/usr/bin/node
const argv = process.argv;
const x = parseInt(argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let c = '';
  for (let i = 0; i < x; i++) c += 'X';
  for (let j = 0; j < x; j++) console.log(c);
}
