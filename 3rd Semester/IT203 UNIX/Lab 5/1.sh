#!/bin/bash

hour=`date +"%H"`
min=`date +"%M"`

if (( hour >= 0 && hour <=11 && min >= 0 && min <= 59 ));
then
	echo "Good Morning"
elif (( hour >= 12 && hour <=17 && min >= 0 && min <= 59 ));
	then
	echo "Good Afternoon"
elif (( hour >= 18 && hour <=19 && min >= 0 && min <= 59 ));
	then
	echo "Good Evening"
else
	echo "Good Night"
fi

