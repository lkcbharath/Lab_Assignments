#!/bin/bash

check=$1

#-A n flag
if [[ -f $check ]]; then
	od -A n -b $check
else
	echo -n $check | od -A n -t o1
fi
