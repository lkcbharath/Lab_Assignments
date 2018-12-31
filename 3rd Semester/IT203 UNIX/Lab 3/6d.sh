#!/bin/bash

echo "Enter hexadecimal number"
read temp

echo "ibase=16; $temp" | bc

# if [[ $temp = "0x"* ]]; then
# 	:
# else
# 	echo "Invalid hexadecimal number entered!"
# 	exit
# fi


# prefix="0x"
# temp=${temp#"$prefix"}

# hexads=$(echo $temp | grep -o .)
# hexad=($hexads)
# # printf %s "${hexad[@]}" $'\n'

# i=0
# j=0
# dec=0

# n=${#hexad[@]}

# if [[ hexad[0] == 0 ]]
# then
# 	echo "0"
# 	exit 0 
# fi


# while [[ n -gt 0 ]]
# do
# 	index=$(echo "$n-1" | bc )
# 	tempr=${hexad[$index]}

# 	case $tempr in
# 			a|A)
# 				r=10
# 			;;
# 			b|B)
# 				r=11
# 			;;
# 			c|C)
# 				r=12
# 			;;
# 			d|D)
# 				r=13
# 			;;
# 			e|E)
# 				r=14
# 			;;
# 			f|F)
# 				r=15
# 			;;
# 			*)
# 				r=$tempr
# 			;;
#  		esac	
	

# 	if (( r > 16 || r < 0 ))
# 	then
# 		echo "Invalid hexadecimal number entered!!!"
# 		exit 1
# 	fi

# 	pow=$((16**i))
# 	z=$(echo "$r*$pow" | bc )
# 	dec=$(echo "$dec+$z" | bc )
# 	i=$(echo "$i+1" | bc )
# 	n=$(echo "$n-1" | bc )
# done

# echo "$dec"

# i=i=$(echo "$i-1" | bc )
