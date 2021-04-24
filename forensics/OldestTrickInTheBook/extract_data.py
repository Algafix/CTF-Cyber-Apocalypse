
# tshark -r older_trick.pcap -T fields -e data.data -Y 'icmp.type == 8' > icmp8_data.txt


import sys,os
import zipfile
import io

firma = b'P'
hidden_file = bytearray()
with open('icmp8_data.txt') as data_file:

    line = data_file.readline()
    packet = bytearray.fromhex(line.strip())

    first = packet.index(firma)
    last = packet[first+1:].index(firma) + first + 1

    hidden_file += packet[first:last]

    for line in data_file:
        packet = bytearray.fromhex(line.strip())
        hidden_file += packet[first:last]

with zipfile.ZipFile(io.BytesIO(hidden_file), 'r') as zip_ref:
    zip_ref.extractall()