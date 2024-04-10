#!/usr/bin/node
// a script that concats 2 files.
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination

const fs = require('fs');

const firstArg = fs.readFileSync(process.argv[2]).toString();
const secondArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firstArg + secondArg);
