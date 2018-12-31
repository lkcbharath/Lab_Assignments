#!/bin/bash

echo "Enter binary number"

read bin

echo "ibase=2; $bin" | bc

# if [ -n "$bin" ] && [ "$bin" -eq "$bin" ] 2>/dev/null; then
# 	:
# else
# 	echo "Invalid binary number entered!"
# 	exit
# fi

# if [[ bin -lt 0 ]] ; then
# 	echo "Invalid binary number entered!"
# 	exit
# fi

# i=0
# dec=0

# if (( bin == 0 ))
# then
# 	echo "0"
# 	exit 0 
# fi

# while [[ bin -gt 0 ]]
# do
# 	r=$(echo "$bin%10" | bc )

# 	if (( r > 1 ))
# 	then
# 		echo "Invalid binary number entered!!!"
# 		exit 1
# 	fi

# 	pow=$((2**i))
# 	z=$(echo "$r*$pow" | bc )
# 	dec=$(echo "$dec+$z" | bc )
# 	bin=$(echo "$bin/10" | bc)
# 	i=$(echo "$i+1" | bc )
# done

# echo "$dec"












# i=i=$(echo "$i-1" | bc )

# for (( j = i; j>=0; j-- ))
# do
# 	k=$(echo "$i-$j" | bc )
# 	arr2[$k]="${arr[$j]}"
# done

# printf %s "${arr2[@]}" $'\n'
