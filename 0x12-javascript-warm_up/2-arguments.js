#!/usr/bin/node
const argv = process.argv;

if (argv.length === 2) {
  console.log('No argument');
} else {
  console.log(argv.length === 3 ? 'Argument found' : 'Arguments found');
}
