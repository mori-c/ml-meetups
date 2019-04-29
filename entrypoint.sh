#!/bin/sh

mongod --fork --logpath /var/log/mongod.log > /dev/null 2>&1

cd /code
npm install

/bin/sh