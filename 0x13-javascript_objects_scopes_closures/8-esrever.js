#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((_, i) => list[list.length - 1 - i]);
};
