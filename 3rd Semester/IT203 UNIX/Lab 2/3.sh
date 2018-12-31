max=0
min=10000000000000
count2=0
count3=0
count4=0
x1=1
z=0
echo "Enter 5 numbers:"

for (( i=0; i<5; ++i ))
do
  j=$(echo "$i+1" | bc )
  echo "Enter number $j"
  read z
  a[$i]=$z
  if (( max < z ));
  then
    max=$z
  fi
  if (( min > z ));
  then
    min=$z
  fi
done

echo "Max value = $max "
echo "Min value = $min "

IFS=$'\n' sorted=($(sort <<<"${a[*]}"))
unset IFS

#sorted is array

for (( i=0; i<4; ++i ))
do
  z=${sorted[$i]}
  z1=${sorted[$i+1]}
  if (( z1 == z )); 
  then
      count2=$(echo "$count2+1" | bc )
  fi
done

for (( i=0; i<3; ++i ))
do
  z=${sorted[$i]}
  z1=${sorted[$i+1]}
  z2=${sorted[$i+2]}
  if (( z1 == z && z2 == z1)); 
  then
      count3=$(echo "$count3+1" | bc )
  fi
done

for (( i=0; i<2; ++i ))
do
  z=${sorted[$i]}
  z1=${sorted[$i+1]}
  z2=${sorted[$i+2]}
  z3=${sorted[$i+3]}
  if (( z1 == z && z2 == z1 && z3 == z2 )); 
  then
      count4=$(echo "$count4+1" | bc )
  fi
done


if (( count4 >= x1 ))
then
   echo "Four elements are same"

elif (( count3 >= x1 ))
then
   echo "Three elements are same"

elif (( count2 >= x1 ))
then
   echo "Two elements are same"
fi


