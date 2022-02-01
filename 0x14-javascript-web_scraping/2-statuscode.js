#!/usr/bin/node
/* Write a script that display the status code of a GET request. */
/* HTTP request lo hacemos con la libreria Axios */
/* traigo el arg que será el nombre de la url */
/* el contenido a escribir en el archivo */
/* el módulo fs sirve para acceder e interactuar con el sistema de archivos *
/* utilizo el método writeFile de fs para escribir en un archivo */

const url = process.argv.slice(2)[0];

const urlLi = url.split('/');
const pathUrl = '/' + urlLi[3];

const https = require('https');
const options = {
  hostname: urlLi[2],
  port: 443,
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
