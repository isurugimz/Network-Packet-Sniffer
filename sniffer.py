from scapy.all import sniff, IP, TCP, wrpcap

captured_packets = []

def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        captured_packets.append(packet)
        print(f"Captured: {packet[IP].src} --> {packet[IP].dst} | Protocol: {packet.proto}")

print("Sniffing started... (Press Ctrl+C to stop)")

try:
    # Capture 100 packets automatically
    sniff(prn=process_packet, count=100)
except KeyboardInterrupt:
    pass

# Save the captured packets to a .pcap file for Wireshark analysis
wrpcap('my_traffic.pcap', captured_packets)
print("\nDone! Results saved to 'my_traffic.pcap'")
