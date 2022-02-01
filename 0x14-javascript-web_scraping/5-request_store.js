#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file. */

const swUrl = process.argv.slice(2)[0];
const fileName = process.argv.slice(2)[1];

const request = require('request');
const fs = require('fs');

request(swUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const urlContent = body;
    fs.appendFile(fileName, urlContent, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
