#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf8', (error) => {
    if (err) {
      console.error(error);
    }
  });
});
