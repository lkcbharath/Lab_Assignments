#!/bin/bash

echo "Enter two text file names"
read atext
read btext

if [ -z "$atext" ]; then
    echo "Nothing entered!"
    exit 0

if [ -z "$btext" ]; then
    echo "Nothing entered!"
    exit 0



if [ -e $atext ]
then
	if [ -e $btext ]
	then
		cat "$atext" >> "$btext"
		cat $btext
		exit
	else
    	echo "Second filename is not of a valid text file"
	fi
else
    echo "First filename is not of a valid text file"
fi


