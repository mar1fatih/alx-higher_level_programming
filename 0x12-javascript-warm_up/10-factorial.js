#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log(1);
} else {
  fac = Factorial(Number(process.argv[2]));
  console.log(fac);
}
function Factorial (num) {
  if (num === 0) {
    return (1);
  }
  return (num * Factorial(num - 1))
}
