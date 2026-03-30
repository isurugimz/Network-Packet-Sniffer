# Network Traffic Sniffer & Analyzer

A lightweight, Python-based network packet sniffer designed for capturing and analyzing live IP traffic. This tool intercepts network packets at the data link layer, decodes IP headers, and exports the captured data for offline Deep Packet Inspection (DPI).

## 🚀 Features
* **Real-Time Monitoring:** Captures live network traffic and displays source and destination IP addresses.
* **Protocol Identification:** Identifies underlying transport layer protocols (e.g., TCP, UDP, ICMP).
* **Automated Capture Limit:** Automatically stops sniffing after capturing a predefined number of packets (Default: 100 packets).
* **PCAP Export:** Saves the captured network traffic into a `.pcap` file, allowing for advanced analysis using industry-standard tools like **Wireshark**.

## 🛠️ Technologies & Libraries Used
* **Python 3**
* **Scapy:** For packet manipulation and network scanning.
* **Npcap / WinPcap:** Packet capture architecture for Windows.

## 📋 Prerequisites (Windows)
To run this tool on a Windows environment, ensure you have the following installed:
1. Python 3.x
2. [Npcap](https://npcap.com/#download) (Make sure to install with "WinPcap API-compatible mode" checked).
3. Install the required Python library:
   ```bash
   pip install scapy
⚙️ How to Run
Clone this repository to your local machine:

Bash
git clone [https://github.com/YOUR_USERNAME/Network-Packet-Sniffer.git](https://github.com/YOUR_USERNAME/Network-Packet-Sniffer.git)
cd Network-Packet-Sniffer
Crucial: Open your Command Prompt (CMD) or PowerShell as an Administrator.

Run the script:

Bash
python sniffer.py
Once 100 packets are captured, a my_traffic.pcap file will be generated in the same directory. Open this file with Wireshark to perform a detailed traffic analysis.

⚠️ Disclaimer
This tool is created for educational purposes and ethical network analysis only. Do not use this tool on networks where you do not have explicit permission to monitor traffic.
