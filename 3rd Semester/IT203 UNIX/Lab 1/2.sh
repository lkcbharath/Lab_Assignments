echo "Enter your base amount"
read base
dp=$(echo "0.5*$base" | bc  )
da=$(echo "0.35*($base+$dp)" | bc  ) 
hra=$(echo "0.08*($base+$dp)" | bc  ) 
ma=$(echo "0.03*($base+$dp)" | bc  ) 
pf=$(echo "0.1*($base+$dp)" | bc  )
salary=$(echo "$base+$dp+$da+$hra+$ma-$pf" | bc  )
echo "Salary = $salary" 

