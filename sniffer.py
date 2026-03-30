import socket
import struct

def main():
    # Make raw socket (Need linux root privileges )
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    print("Sniffing packets... (Press Ctrl+C to stop)")

    while True:
        raw_data, addr = conn.recvfrom(65535)
        
        # 1. Ethernet Frame decode  (MAC Addresses)
        dest_mac, src_mac, eth_proto = struct.unpack('! 6s 6s H', raw_data[:14])
        
        # IPv4 packets (Protocol 8 mean IPv4)
        if socket.htons(eth_proto) == 8:
            # 2. IPv4 Header decode 
            ip_header = raw_data[14:34]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            
            src_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])
            protocol = iph[6] # TCP=6, UDP=17, ICMP=1
            
            print(f"Protocol: {protocol} | Source IP: {src_ip} --> Destination IP: {dest_ip}")

# Run Command
if __name__ == "__main__":
    main()