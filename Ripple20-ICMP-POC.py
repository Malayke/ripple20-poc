try:
    from scapy.all import *
except:
    print("Scapy not found, please install scapy: pip install scapy")

import sys


def process_packet(pkt):
    
    if pkt.haslayer(ICMP):
        # print (f"icmp type: {pkt[ICMP].type}")
        if pkt[ICMP].type == 0xa5:
            data = bytes(pkt[ICMP].payload)
            if b'\x01\x51\x35\x28\x57\x32' in data or b'\x51\x01\x28\x35\x32\x57' in data:
                print (f"Find Vulnerable device: {pkt[IP].src}")
                print (f"Recived icmp data:")
                hexdump(pkt[ICMP].payload)


def main():
    if len(sys.argv) <1:
        print(f"Usage:\n\tsudo {sys.argv[0]} eth0")
        sys.exit(1)
    interface = sys.argv[1]
    print('[*]Start sniffing ICMP packet')
    sniff(iface=interface, prn=process_packet, filter="icmp")

if __name__ == '__main__':
    main()
