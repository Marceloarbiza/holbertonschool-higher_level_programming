#!/usr/bin/node
/* Write a script that display the status code of a GET request. */
/* HTTP request lo hacemos con la libreria Axios */
/* traigo el arg que será el nombre de la url */

const url = process.argv.slice(2)[0];

const urlLi = url.split('/');
const pathUrl = '/' + urlLi[3];
const hostUrl = urlLi[2];

const https = require('https');
const options = {
  hostname: hostUrl,
  path: pathUrl,
  method: 'GET'
};

const req = https.request(options, res => {
  console.log(`code: ${res.statusCode}`);
});

req.on('error', error => {
  console.error(error);
});

req.end();
