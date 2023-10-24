#!/usr/bin/node
const request = require('request');
const host = process.argv[2];

request(host, (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', res.statusCode);
});
