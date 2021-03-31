def metric_gen(exp_num):
    filename = "exp" + exp_num + "/assignment2_exp" + exp_num + ".tr"
    with open(filename, "r") as f:
        lines = f.readlines()
    no_of_packets_transmitted = 0
    no_of_packets_received = 0

    no_of_udp_packets = 0

    latencies = []
    throughputs = []
    pd_ratios = []

    tx_time = 0
    rx_time = 0

    for line in lines:
        line = line.split()
        pkt_time = float(line[1])

        print(line[0], len(line))

        if line[0] == "t":
            no_of_packets_transmitted += 1
            tx_time = pkt_time
        else:
            no_of_packets_received += 1
            rx_time = pkt_time

            if (len(line) == 52 or len(line) == 54) and line[42] == "ns3::UdpHeader":
                no_of_udp_packets += 1
                latencies.append((pkt_time,rx_time - tx_time))
        
        pdr = (no_of_packets_received / no_of_packets_transmitted)
        pd_ratios.append((pkt_time, pdr))

        size_of_udp_packet = 1008
        rxBytes = size_of_udp_packet * no_of_udp_packets
        total_time_elapsed = pkt_time - 30
        throughput = rxBytes / total_time_elapsed
        throughputs.append((pkt_time, throughput))

    return [latencies, pd_ratios, throughputs]

def main():
    for i in range(1,8):
        latencies, pd_ratios, throughputs = metric_gen(str(i))

        with open("exp" + str(i) + "_metric_latency.txt", "w+") as f:
            for latency in latencies:
                f.write(str(latency[0]) + " " + str(latency[1]) + "\n")
        
        with open("exp" + str(i) + "_metric_pdr.txt", "w+") as f:
            for pd_ratio in pd_ratios:
                f.write(str(pd_ratio[0]) + " " + str(pd_ratio[1]) + "\n")
        
        with open("exp" + str(i) + "_metric_throughput.txt", "w+") as f:
            for throughput in throughputs:
                f.write(str(throughput[0]) + " " + str(throughput[1]) + "\n")

if __name__ == '__main__':
    main()