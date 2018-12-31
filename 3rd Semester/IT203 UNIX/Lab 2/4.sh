echo "Enter elements"
count1=0
count2=0
count3=0
x=1
for (( i=0; i<10; ++i ))
do
  echo "Enter number $i"
  read z
  a[$i]=$z

  if (( z < 0 ));
  then
    count1=$(echo "$count1+$x" | bc )
  fi

  if (( z == 0 ));
  then
    count2=$(echo "$count2+$x" | bc )
  fi

  if (( z > 0 ));
  then
    count3=$(echo "$count3+$x" | bc )
  fi
	
done

echo "Elements less than 0: $count1"
echo "Elements equal to 0: $count2"
echo "Elements greater than 0: $count3"


IFS=$'\n' sorted=($(sort <<<"${a[*]}"))
unset IFS

echo "Elements are: ${sorted[@]}"
