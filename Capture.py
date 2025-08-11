from scapy.all import *

def packetCallback(packet):
    print(packet.summary())


def startCapture(interface, packetCount):
    print(f"Starting packet capture on {interface} for {packetCount} packets...")
    sniff(iface=interface, prn=packetCallback,count=packetCount)

