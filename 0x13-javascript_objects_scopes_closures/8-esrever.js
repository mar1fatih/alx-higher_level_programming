#!/usr/bin/node
exports.esrever = function (list) {
  let b = list.length - 1;
  let temp;
  for (let i = 0; i < list.length / 2; i++) {
    temp = list[i];
    list[i] = list[b];
    list[b] = temp;
    b--;
  }
  return (list);
};
