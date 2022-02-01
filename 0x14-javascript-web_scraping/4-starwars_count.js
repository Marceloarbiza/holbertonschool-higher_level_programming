#!/usr/bin/node
/*  i/ script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const swUrl = process.argv.slice(2)[0];

const request = require('request');

const idU = '/18/';

request(swUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let x = 0;
    let moviesID = 0;
    const urlJSON = JSON.parse(body);
    while (urlJSON.results[x]) {
      let y = 0;
      const listCharas = urlJSON.results[x].characters;
      while (listCharas[y]) {
        if (listCharas[y].includes(idU)) {
          moviesID++;
        }
        y++;
      }
      x++;
    }
    console.log(moviesID);
  }
});
