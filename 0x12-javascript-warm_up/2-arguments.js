#!/usr/bin/node
const { argv } = require('process');
const n = argv.length;
if (n === 3) {
  console.log('Argument found');
} else if (n >= 4) {
  console.log('Arguments found');
} else {
  console.log('No Argument');
}
