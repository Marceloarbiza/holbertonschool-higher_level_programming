#!/usr/bin/node
/* Write a script that reads and prints the content of a file */
/* traigo el arg que será el nombre del file */
/* el contenido a escribir en el archivo */
/* el módulo fs sirve para acceder e interactuar con el sistema de archivos *
/* utilizo el método writeFile de fs para escribir en un archivo */

const filename = process.argv.slice(2)[0];

const content = process.argv.slice(2)[1];

const fs = require('fs');

fs.writeFile(filename, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
