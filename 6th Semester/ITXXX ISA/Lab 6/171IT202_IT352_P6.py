import sys
from scapy.all import *

def main():

    sport = 2345
    dport = 80
    ip_packet = IP(dst='192.168.43.143', ttl=99)
    tcp_packet = TCP(sport=sport, dport=dport, seq=12345, ack=1000, window=1000, flags="S")
    packet = ip_packet/tcp_packet
    print("Packet Details:")
    ls(packet)
    print("Source IP Address:",packet.src)
    print("Destination IP Address:",packet.dst)
    print("Source Port",sport)
    print("Destination Port:",dport)

    print("Sending Packets in 0.03 second intervals")
    ans, unans = srloop(packet, inter=0.03, retry=2, timeout=4)

if __name__ == '__main__':
    main()
