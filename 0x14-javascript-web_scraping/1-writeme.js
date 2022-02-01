#!/usr/bin/node
/* Write a script that reads and prints the content of a file */

/* traigo el arg que será el nombre del file */
const filename = process.argv.slice(2)[0];

/* el contenido a escribir en el archivo */
const content = process.argv.slice(2)[1];

/* el m�dulo fs sirve para acceder e interactuar con el sistema de archivos */
const fs = require('fs');

/* utilizo el método writeFile de fs para escribir en un archivo */
fs.writeFile(filename, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
