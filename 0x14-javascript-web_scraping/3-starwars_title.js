#!/usr/bin/node
// Script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
