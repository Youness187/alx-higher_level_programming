#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

if (argv.length < 4) process.exit(-1);

const a = fs.readFileSync(argv[2], 'utf8');
const b = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(process.argv[4], a + b);
