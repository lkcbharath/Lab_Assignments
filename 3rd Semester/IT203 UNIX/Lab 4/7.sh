#!/bin/bash

declare -A matrix1

echo "Enter size of square 2D diagonal matrix"
read num_size

echo "Enter array"


for ((i=0;i<num_size;i++)) do
    for ((j=0;j<num_size;j++)) 
    do
    	read a
		if (( i==j ))
		then
	   		if (( a == 0 ))
	    	then
            	echo "Invalid element entered"
            	exit 0
        	else
        		matrix1[$i,$j]=$a
        fi
    	else
    		if (( a != 0 ))
	    	then
            	echo "Invalid element entered"
            	exit 0
        	else
        		matrix1[$i,$j]=$a
        fi
    		matrix1[$i,$j]=0
    	fi
        
    done
done

echo "2D diagonal matrix is"

for ((i=0;i<num_size;i++)) 
do
    for ((j=0;j<num_size;j++)) 
    do
    	result[$j]=${matrix1[$i,$j]}
    done
    echo ${result[@]}
done


# for ((i=0;i<num_rows;i++)) do
#     for ((j=0;j<num_columns;j++)) 
#     do
#     	echo ${matrix2[$i,$j]}
#     done
# done
