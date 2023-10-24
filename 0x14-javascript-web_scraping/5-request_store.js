#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const host = process.argv[2];
const file = process.argv[3];

request(host, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, (e, dat) => {
    if (e) {
      console.log(e);
    }
  });
});
