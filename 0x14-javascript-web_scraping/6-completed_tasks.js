#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file. */

const swUrl = process.argv.slice(2)[0];

const request = require('request');

request(swUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let x = 0;
    var dictO = {};
    const urlContent = JSON.parse(body);
    while (urlContent[x]) {
      if (urlContent[x].completed === true) {
        if (dictO[urlContent[x].userId] == null) {
          dictO[urlContent[x].userId] = 1;
        } else {
          dictO[urlContent[x].userId]++;
        }
      }
      x++;
    }
  }
  console.log(dictO);
});
