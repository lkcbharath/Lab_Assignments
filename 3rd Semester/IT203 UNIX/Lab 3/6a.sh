#!/bin/bash

echo "Enter decimal number"

read dec

echo "obase=2; $dec" | bc

# if [ -n "$dec" ] && [ "$dec" -eq "$dec" ] 2>/dev/null; then
# 	:
# else
# 	echo "Invalid decimal number entered!"
# 	exit
# fi

# i=0

# if (( dec == 0 ))
# then
# 	echo "0"
# 	exit 0
# fi

# if [[ dec -lt 0 ]] ; then
# 	echo "Invalid decimal number entered!"
# 	exit
# fi

# while [[ dec -gt 0 ]]
# do
# 	r=$(echo "$dec%2" | bc )
# 	dec=$(echo "$dec/2" | bc )
# 	arr[i]=$r
# 	i=$(echo "$i+1" | bc )
# done

# i=i=$(echo "$i-1" | bc )

# for (( j = i; j>=0; j-- ))
# do
# 	k=$(echo "$i-$j" | bc )
# 	arr2[$k]="${arr[$j]}"
# done

# #echo ${#arr2[@]}

# printf %s "${arr2[@]}" $'\n'
