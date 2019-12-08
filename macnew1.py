import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf

ips=input("Enter range of IP's to scan: ")
conf.verb=0
ans,uans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips), timeout=2, inter=0.1)
for snd,rcv in ans:
    print (rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
    
