#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map(function mul (item, index) {
  return item * index;
});

console.log(list);
console.log(newList);
