#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      request.get(character, (error, _, body) => {
        if (error) {
          console.error(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
