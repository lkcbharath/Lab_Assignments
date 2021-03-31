set terminal pdf
set out "graphs_without_olsr.pdf"

set title "Latency without OLSR"
set xlabel "Simulation Time (in s)"
set ylabel "Latency (in s)"
plot "exp2_metric_latency.txt" using 1:2 with lines title "Test Case 2",\
"exp3_metric_latency.txt" using 1:2 with lines title "Test Case 3",\
"exp7_metric_latency.txt" using 1:2 with lines title "Test Case 7"

set title "Packet Delivery Ratio without OLSR"
set xlabel "Simulation Time (in s)"
set ylabel "Packet Delivery Ratio"
plot "exp2_metric_pdr.txt" using 1:2 with lines title "Test Case 2",\
"exp3_metric_pdr.txt" using 1:2 with lines title "Test Case 3",\
"exp7_metric_pdr.txt" using 1:2 with lines title "Test Case 7"

set title "Throughput without OLSR"
set xlabel "Simulation Time (in s)"
set ylabel "Throughput (in bytes/s)"
plot "exp2_metric_throughput.txt" using 1:2 with lines title "Test Case 2",\
"exp3_metric_throughput.txt" using 1:2 with lines title "Test Case 3",\
"exp7_metric_throughput.txt" using 1:2 with lines title "Test Case 7"
