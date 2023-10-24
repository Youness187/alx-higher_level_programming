#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const printChar = (characters, i) => {
  request(characters[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (i + 1 < characters.length) {
      printChar(characters, i + 1);
    }
  });
};

request(`https://swapi-api.alx-tools.com/api/films/${id}`, async (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  printChar(characters, 0);
});
