#!/usr/bin/node

exports.converter = function converter (base) {
  return function (num) {
    return num.toString(base);
  };
};
