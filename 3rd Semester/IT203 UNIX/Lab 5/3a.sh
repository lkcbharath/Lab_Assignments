#!/bin/bash
for i in *
do
	if [ -f $i ]
	then
		grep -l "^\/[aeiouAEIOU]" $i
	fi
done

