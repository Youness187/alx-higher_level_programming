#!/usr/bin/node
const request = require('request');
const host = process.argv[2];

request(host, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const WedgeAntilles = body.split('/people/18/').length - 1;
  console.log(WedgeAntilles);
});
