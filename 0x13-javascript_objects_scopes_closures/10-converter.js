#!/usr/bin/node
exports.converter = function (base) {
  return function convert (num) {
    return (num.tostring(base));
  };
};
