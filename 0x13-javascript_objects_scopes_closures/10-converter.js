#!/usr/bin/node
exports.converter = function (base) {
  return (e) => e.toString(base);
};
