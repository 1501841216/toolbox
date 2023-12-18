#!/usr/bin/python
# -*- coding=utf -*-
import base
import pyshark
from scapy.all import rdpcap

home = "E:\\CTF\\CTFQD\\Crypto\\ce801b8150ef424699ab977c278846aa\\"
L_flag = []
# packets = pyshark.FileCapture("fetus_pcap.pcap")
pcap = rdpcap(home + "fetus_pcap.pcap")
for pkt in pcap:
    if pkt.haslayer("ICMP"):
        if pkt["ICMP"].type != 0:
            L_flag.append(chr(len(pkt.getlayer("ICMP").load)))

print(''.join(L_flag))
print(base.myb64decoder(''.join(L_flag)))

    # for pkt in packet:
    #     if pkt.layer_name == "icmp":
    #         if int(pkt.type) != 0:
    #             L_flag.append(int(pkt.data_len))
# c = len(L_flag)
# for i in range(c):
#     L_flag[i] = chr(L_flag[i])
# print(''.join(L_flag))

