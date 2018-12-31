echo "Enter Two numbers : "
read a
read b

while (( a<=0 || b<=0 ))
do
  echo "Enter numbers greater than: "
  read a
  read b
done

min=0
max=0

if (( a < b ));
then
  min=$a
else
  min=$b
fi

max=$(echo "$a+$b-$min" | bc )

result=$(echo "scale=2; $min/$max" | bc )

echo "Result of division is 0$result"




