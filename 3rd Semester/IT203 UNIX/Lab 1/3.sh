echo "Enter length of set of numbers"
read n
a=0
for (( i=1; i <= $n; ++i ))
do
  echo "Enter number $i"
  read e		
  a=$(echo "$a+$e" | bc  )
  e=0 
done
a = $(echo "scale=2; $a/$n")
echo "Average of set of $n numbers: $a"
