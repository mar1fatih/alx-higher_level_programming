#!/usr/bin/node
const dict = require('./101-data').dict;
const dict2 = {
  '1' : [],
  '2' : [],
  '3' : []
};
const keys = Object.keys(dict);

keys.forEach(key => {
    if (dict[key] === 1){
      dict2['1'].push(String(key));
    }
    else if (dict[key] === 2) {
      dict2['2'].push(String(key));
    }
    else {
      dict2['3'].push(String(key));
    }
});
console.log(dict2);
