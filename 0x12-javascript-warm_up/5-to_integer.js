#!/usr/bin/node
let myNum = parseInt(process.argv[2]);
if (!myNum) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
