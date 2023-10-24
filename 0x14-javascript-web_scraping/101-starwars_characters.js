#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const printChar = (characters) => {
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (err, res, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  }
};

request(`https://swapi-api.alx-tools.com/api/films/${id}`, async (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  printChar(characters);
});
