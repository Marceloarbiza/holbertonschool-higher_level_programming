#!/usr/bin/node
/*  i/ script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const idFilm = process.argv.slice(2)[0];
const films = 'https://swapi-api.hbtn.io/api/films/';
const filmTitle = 'https://swapi-api.hbtn.io/api/films/' + idFilm;
const request = require('request');

request(films, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resultsJSON = JSON.parse(body).results;
    request(filmTitle, function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        const nameJSON = JSON.parse(body);
        for (const r in resultsJSON) {
          if (resultsJSON[r].title === nameJSON.title) {
            const liChar = resultsJSON[r].characters;
            for (const c in liChar) {
              request(liChar[c], function (error, response, body) {
                if (error) {
                  console.log(error);
                } else {
                  const charJSON = JSON.parse(body);
                  console.log(charJSON.name);
                }
              });
            }
          }
        }
      }
    });
  }
});
