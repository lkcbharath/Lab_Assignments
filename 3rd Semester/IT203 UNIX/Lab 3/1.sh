#!/bin/bash

echo "Enter string"
read PASSED

if [ -z "$PASSED" ]; then
    echo "Nothing entered!"
    exit 0

elif [[ -d $PASSED ]]; then
    echo "$PASSED is a directory"
    ls $PASSED

elif [[ -f $PASSED ]]; then
    echo "$PASSED is a file"
    cat $PASSED

else
    echo "$PASSED is not a file or directory"
fi
