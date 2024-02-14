#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
const occurenceList = [];
for (const id in dict) {
  if (occurenceList.includes(dict[id])) {
    newDict[dict[id]].push(id);
  } else {
    occurenceList.push(dict[id]);
    newDict[dict[id]] = [];
    newDict[dict[id]].push(id);
  }
}

console.log(newDict);
