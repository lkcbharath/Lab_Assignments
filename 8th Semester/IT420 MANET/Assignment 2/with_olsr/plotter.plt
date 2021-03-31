set terminal pdf
set out "graphs_with_olsr.pdf"

set title "Latency with OLSR"
set xlabel "Simulation Time (in s)"
set ylabel "Latency (in s)"
plot for [i=1:7] "exp".i."_metric_latency.txt" using 1:2 with lines title "Test Case ".i

set title "Packet Delivery Ratio with OLSR"
set xlabel "Simulation Time (in s)"
set ylabel "Packet Delivery Ratio"
plot for [i=1:7] "exp".i."_metric_pdr.txt" using 1:2 with lines title "Test Case ".i

set title "Throughput with OLSR"
set xlabel "Simulation Time (in s)"
set ylabel "Throughput (in bytes/s)"
plot for [i=1:7] "exp".i."_metric_throughput.txt" using 1:2 with lines title "Test Case ".i
