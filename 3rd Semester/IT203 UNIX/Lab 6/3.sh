#!/bin/bash

# echo "job 1"

# nohup ps aux &
# pid=$!
# jobs

# echo $pid
# kill $pid
# echo
# sleep 0.1
# jobs

# echo "job 2"

echo hello &
pid=$!
echo $pid
jobs
kill $pid
sleep 0.1
jobs
