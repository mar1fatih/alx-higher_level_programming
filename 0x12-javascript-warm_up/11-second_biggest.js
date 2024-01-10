#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2).map(Number);
  let secondLargest = array.sort((a, b) => b - a);
  for (let i = 1; i < array.length; i++) {
    if (array[i] !== array[0]) {
      secondLargest = array[i];
      break;
    }
  }
  console.log(secondLargest);
}
