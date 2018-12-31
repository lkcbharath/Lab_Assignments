#!/bin/bash

echo "Enter decimal number"

read dec

echo "obase=16; $dec" | bc

# if [ -n "$dec" ] && [ "$dec" -eq "$dec" ] 2>/dev/null; then
# 	:
# else
# 	echo "Invalid decimal number entered!"
# 	exit
# fi

# if [[ dec -lt 0 ]] ; then
# 	echo "Invalid decimal number entered!"
# 	exit
# fi

# i=0

# if (( dec == 0 ))
# then
# 	echo "0"
# 	exit 0
# fi

# while [[ dec -gt 0 ]]
# do
# 	r=$(echo "$dec%16" | bc )
# 	dec=$(echo "$dec/16" | bc )

# 	if (( r > 9 ))
# 	then
# 		case $r in
# 			10)
# 				r=A
# 			;;
# 			11)
# 				r=B
# 			;;
# 			12)
# 				r=C
# 			;;
# 			13)
# 				r=D
# 			;;
# 			14)
# 				r=E
# 			;;
# 			15)
# 				r=F
# 			;;
# 			*)
# 				echo "Invalid integer?"
# 				exit 0
# 				;;
#  		esac
#  	fi

# 	arr[i]=$r

# 	i=$(echo "$i+1" | bc )
# done

# i=i=$(echo "$i-1" | bc )

# for (( j = i; j>=0; j-- ))
# do
# 	k=$(echo "$i-$j" | bc )
# 	arr2[$k]="${arr[$j]}"
# done

# printf %s "0x${arr2[@]}" $'\n'
