# 🕵️‍♂️ Network Traffic Sniffer & Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A lightweight, Python-based network packet sniffer designed for capturing and analyzing live IP traffic. This tool intercepts network packets, decodes IP headers, and exports the captured data for offline Deep Packet Inspection (DPI). 

This project demonstrates core concepts in network security, socket programming, and protocol analysis.

## ✨ Key Features
* **Live Traffic Monitoring:** Captures network packets in real-time and extracts Source/Destination IP addresses.
* **Protocol Identification:** Identifies underlying transport layer protocols (TCP, UDP, ICMP).
* **Automated Capture Limit:** Automatically stops sniffing after capturing exactly **100 packets** (Customizable in the code).
* **PCAP File Export:** Saves the captured network traffic into a `my_traffic.pcap` file. This allows for advanced analysis using industry-standard tools like **Wireshark**.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Core Library:** `scapy` (For packet manipulation and network scanning)
* **Driver:** Npcap / WinPcap (Packet capture architecture for Windows)

## 🚀 Getting Started (Windows)

### Prerequisites
1. Install [Python 3.x](https://www.python.org/downloads/)
2. Install [Npcap](https://npcap.com/#download) (Make sure to check **"Install Npcap in WinPcap API-compatible mode"** during installation).
3. Install the required Python library via your terminal:
   ```bash
   pip install scapy
Installation & Execution
Clone this repository to your local machine:

Bash
git clone [https://github.com/isurugimz/Network-Packet-Sniffer.git](https://github.com/isurugimz/Network-Packet-Sniffer.git)
cd Network-Packet-Sniffer
Crucial Step: Open Command Prompt (CMD) or PowerShell as an Administrator.

Run the sniffer script:

Bash
python sniffer.py
Once 100 packets are successfully captured, check the project folder for the newly generated my_traffic.pcap file. Open this file with Wireshark to view the detailed packet data!

⚠️ Disclaimer
This tool was developed for educational purposes and ethical network analysis only. Do not use this tool on networks where you do not have explicit permission to monitor traffic. The developer is not responsible for any misuse or illegal activities conducted with this script.
