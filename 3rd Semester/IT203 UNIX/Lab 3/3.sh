#!/bin/bash

echo "Enter two strings"
read stra
read strb

echo "Enter number based on your checking choice:"
echo "1. Strings are non-empty"
echo "2. Strings are same"
echo "3. Strings are palindrome"

read i

if [ -n "$i" ] && [ "$i" -eq "$i" ] 2>/dev/null; then
	:
else
	echo "Invalid choice entered!"
	exit
fi

case "$i" in

1)  [[ -z "$stra" ]] && echo "First string is Empty" || echo "First string is not empty"
    [[ -z "$strb" ]] && echo "Second string is Empty" || echo "Second string is not empty"
    ;;

2)  if [ "$stra" != "$strb" ]; then
    	echo "Strings are not same"
	else
    	echo "Strings are same"
	fi
    ;;

3)  if [[ $(rev <<< "$stra") == "$stra" && ]]; then
    	echo "First string is a palindrome"
    else
    	echo "First string is not a palindrome"
	fi

	if [[ $(rev <<< "$strb") == "$strb" ]]; then
    	echo "Second string is a palindrome"
    else
    	echo "Second string is not a palindrome"
	fi
    ;;

*) echo "Invalid option entered"
   ;;
esac
