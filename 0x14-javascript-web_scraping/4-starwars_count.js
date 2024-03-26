#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) throw error;
  const bodyJSON = JSON.parse(body);
  const films = bodyJSON.results;
  let numFilms = 0;
  const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  for (let i = 0; i < films.length; i++) {
    for (let j = 0; j < films[i].characters.length; j++) {
      if (films[i].characters[j] === wedgeUrl) {
        numFilms += 1;
      }
    }
  }
  console.log(numFilms);
});
