#!/bin/bash

sort -o sorted.txt test1.txt &
sort -o sorted.txt test1.txt &
jobs | wc -l
