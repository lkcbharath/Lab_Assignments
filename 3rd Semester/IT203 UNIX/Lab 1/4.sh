echo "Enter number n"
read n
a=0
for (( i=1; i <= $n; ++i ))
do
  a=$(echo "$a+$i" | bc  )
done
echo "Sum of $n numbers upto $n: $a"
