#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + movieId, (error, response, body) => {
  if (error) throw error;
  const bodyJSOn = JSON.parse(body);
  console.log(bodyJSOn.title);
});
