ls()
lsc()
IP()
IP().display()
Ether()
TCP()
TCP().display()
ARP()

pa=sniff(count=10)

srloop(IP(dst="www.goog")/ICMP(), count=3)

#used for lab 2
hexdump()