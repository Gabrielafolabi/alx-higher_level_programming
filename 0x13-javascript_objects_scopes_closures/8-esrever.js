#!/usr/bin/node
// function that returns the reversed version of a list withouth reverse
exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
