#!/usr/bin/node
// Script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
let num = 0;

request.get(process.argv[2], (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
