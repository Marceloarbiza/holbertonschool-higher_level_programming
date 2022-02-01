#!/usr/bin/node
/*  i/ script that prints the title of a Star Wars movie
where the episode number matches a given integer. */

const episode = process.argv.slice(2)[0];

const swUrl = 'https://swapi-api.hbtn.io/api/films/' + episode;

const request = require('request');

request(swUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
