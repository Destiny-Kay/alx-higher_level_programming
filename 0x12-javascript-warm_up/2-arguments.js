#!/usr/bin/node

const args = process.argv;

if (args.length <= 2) {
  console.log('No argument');
} else {
  args.length === 3
    ? console.log('Argument found')
    : console.log('Arguments found');
}
