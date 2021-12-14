#!/usr/bin/node

exports.converter = function (base) {
  function theNumber (num) {
    return num.toString(base);
  }
  return theNumber;
};
