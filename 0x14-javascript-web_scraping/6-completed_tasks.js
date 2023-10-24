#!/usr/bin/node
const request = require('request');
const host = process.argv[2];

request(host, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasksCompleted = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      tasksCompleted[task.userId] = (tasksCompleted[task.userId] || 0) + 1;
    }
  }
  console.log(tasksCompleted);
});
