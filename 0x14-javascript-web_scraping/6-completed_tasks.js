#!/usr/bin/node

const request = require('request');
const obj = {};

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  body.forEach((user) => {
    if (user.completed) {
      if (!obj[user.userId]) {
        obj[user.userId] = 1;
      } else {
        obj[user.userId] += 1;
      }
    }
  });
  console.log(obj);
});
