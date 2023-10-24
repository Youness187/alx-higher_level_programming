#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
  if (err) console.log(err);
  for (const character of JSON.parse(body).characters) {
    request(character, (err, res, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  }
});
