#!/usr/bin/node

const fetchPromise = fetch(
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2]
);

fetchPromise.then((res) => {
  const jsonedResponse = res.json();
  jsonedResponse
    .then((data) => {
      return data.characters;
    })
    .then(async (d) => {
      for (let i = 0; i < d.length; i++) {
        const character = await fetch(d[i]);
        const jsonedChar = await character.json();
        console.log(jsonedChar.name);
      }
    });
});
