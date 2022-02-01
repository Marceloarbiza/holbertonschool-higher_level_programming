#!/usr/bin/node
/* Write a script that display the status code of a GET request. */
/* HTTP request lo hacemos con la libreria Axios */
/* traigo el arg que será el nombre de la url */

const url = process.argv.slice(2)[0];

const request = require('request');

request(url, (err, res) => {
  if (err) { return console.log(err); }
  console.log(`code: ${res.statusCode}`);
});
