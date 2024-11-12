#!/usr/bin/node

const request = require('request');

request(
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  function (error, response, body) {
    if (error) console.error('error', error);
    const characters = JSON.parse(body).characters;

    func(characters, 0);
  }
);

function func (characters, n) {
  if (n === characters.length) return;
  request(characters[n], function (err, res, body) {
    if (err) console.error('error', err);
    console.log(JSON.parse(body).name);
    func(characters, n + 1);
  });
}
