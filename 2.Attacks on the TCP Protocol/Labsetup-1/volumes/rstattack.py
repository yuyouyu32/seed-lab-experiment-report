#!/usr/bin/env python3
from scapy.all import *
ip  = IP(src="10.9.0.1",dst="10.9.0.5")
tcp = TCP(sport=54828, dport=23, flags="S", seq=4065682361)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)

