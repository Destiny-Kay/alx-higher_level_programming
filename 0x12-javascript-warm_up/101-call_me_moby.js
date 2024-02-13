#!/usr/bin/node
function callMeMoby (x, a) {
  let i = 0;
  while (i < x) {
    a();
    i++;
  }
}

module.exports = { callMeMoby };
