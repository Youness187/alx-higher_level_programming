#!/usr/bin/node
const argv = process.argv;
const nums = argv.splice(2).map((x) => parseInt(x)).sort((a, b) => (b - a));

console.log(nums.length < 2 ? 0 : nums[1]);
