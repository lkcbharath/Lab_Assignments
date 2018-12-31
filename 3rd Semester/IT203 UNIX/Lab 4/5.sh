#!/bin/bash

declare -A matrix1
declare -A matrix2

echo "Enter size of first 2D matrix"
read num_rows
read num_columns

echo "Enter array 1"

for ((i=0;i<num_rows;i++)) do
    for ((j=0;j<num_columns;j++)) 
    do
    	read a
        matrix1[$i,$j]=$a
    done
done

echo "Enter size of second 2D matrix"
read num_rows2
read num_columns2

if (( num_rows2!= num_rows || num_columns2!=num_columns ));
then
	echo "Matrix dimensions are not same"
	exit 0
fi


echo "Enter array 2"

for ((i=0;i<num_rows;i++)) 
do
    for ((j=0;j<num_columns;j++)) 
    do
    	read b
    	a=${matrix1[$i,$j]}
    	matrix2[$i,$j]=$((a+b))
    done
done

echo "Sum of 2D arrays are"

for ((i=0;i<num_rows;i++)) 
do
    for ((j=0;j<num_columns;j++)) 
    do
    	result[$j]=${matrix2[$i,$j]}
    done
    echo ${result[@]}
done


# for ((i=0;i<num_rows;i++)) do
#     for ((j=0;j<num_columns;j++)) 
#     do
#     	echo ${matrix2[$i,$j]}
#     done
# done
