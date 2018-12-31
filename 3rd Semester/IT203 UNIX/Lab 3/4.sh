#!/bin/bash

echo "Enter marks of UNIX, Java, and DS out of 100"
read unixmarks
read javamarks
read dsmarks

hund=100.0
zero=0.0

if [ -z $unixmarks ] || [ -z $javamarks ] || [ -z $dsmarks ]
then
	echo "Invalid marks entered!!"
	exit 0
fi


if (( $(echo "$unixmarks < 0.0" |bc -l) )) || (( $(echo "$unixmarks > $hund" |bc -l) )) || (( $(echo "$javamarks < $zero" |bc -l) )) || (( $(echo "$javamarks > $hund" |bc -l) )) || (( $(echo "$dsmarks < $zero" |bc -l) )) || (( $(echo "$dsmarks > $hund" |bc -l) )); 
then
	echo "Invalid marks entered"
	exit 0
fi

sum=$(echo "$unixmarks + $javamarks + $dsmarks" | bc -l)
avg=$(echo "$sum / 3" | bc -l)

echo $avg

if (( $(echo "$avg > 70.0" |bc -l) )); then
    echo "Distinction!"

elif (( $(echo "$avg > 60.0" |bc -l) )); then
    echo "First Class."

elif (( $(echo "$avg > 50.0" |bc -l) )); then
    echo "Second Class..."

elif (( $(echo "$avg > 40.0" |bc -l) )); then
    echo "Third class..."
else
    echo "fail"
fi