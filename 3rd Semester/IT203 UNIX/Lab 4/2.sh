#!/bin/bash

echo "Enter string 1"
read a
echo "Enter string 2"
read b

a=$(echo $(printf "%s\n" $a | sort -n))

b=$(echo $(printf "%s\n" $b | sort -n))

echo 

echo $a >> 2a.txt
echo $b >> 2b.txt

sort -o 2a.txt 2a.txt
sort -o 2b.txt 2b.txt

echo "Unique elements"

echo "in file 1:"
comm -13 2a.txt 2b.txt

echo "in file 2:"
comm -13 2b.txt 2a.txt

echo "Common elements to both files"
comm -12 2a.txt 2b.txt
comm -12 2a.txt 2b.txt > 2c.txt

echo
echo "To make them identical, remove unique elements both files or use common elements"

echo "file a:"
cat 2c.txt
echo "file b"
cat 2c.txt

rm -f 2c.txt


