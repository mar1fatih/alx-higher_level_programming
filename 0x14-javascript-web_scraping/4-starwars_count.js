#!/usr/bin/node

const request = require('request');
let c = 0;
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const obj = JSON.parse(body);
  obj.results.forEach((ele) => {
    ele.characters.forEach((chara) => {
      if (chara.includes(18)) {
        c += 1;
      }
    });
  });
  console.log(c);
});
