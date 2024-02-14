#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const firstSrc = args[2];
const secondSrc = args[3];
const dest = args[4];

function readNcpy (file, destFile) {
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) throw err;
    fs.appendFile(destFile, data, 'utf8', (err) => {
      if (err) throw err;
    });
  });
}

readNcpy(firstSrc, dest);
readNcpy(secondSrc, dest);
