echo "1"

for (( j=1; j<=9; ++j ))
do
  for (( k=0; k<=9; ++k ))
  do
    x=$(echo "($j*$j*$j)+($k*$k*$k)" | bc )
    z=$(echo "(10*$j)+$k" | bc )

    if (( z == x ));
    then
      echo $z
    fi
  done
done




for (( i=1; i<=9; ++i ))
do
  for (( j=0; j<=9; ++j ))
  do
    for (( k=0; k<=9; ++k ))
    do
      x=$(echo "($i*$i*$i)+($j*$j*$j)+($k*$k*$k)" | bc )
      z=$(echo "(100*$i)+(10*$j)+$k" | bc )

      if (( z == x ));
      then
        echo $z
      fi

    done
  done
done
