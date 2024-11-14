#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

request(`${apiUrl}${filmId}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  body = JSON.parse(body);

  body.characters.forEach(char => {
    request(char, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
