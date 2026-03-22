#!/bin/bash

clear
figlet "RECON"

echo "======================================"
echo " MOBILE-RECON TOOLKIT v1.0"
echo "======================================"

# Target local subnet for discovery
IP_RANGE="192.168.1.0/24"

echo "[+] Scanning subnet: $IP_RANGE"
# Use unprivileged connect scan to bypass iOS kernel restrictions
nmap -sT -sn --unprivileged $IP_RANGE | grep "Nmap scan report"

echo ""
echo "[+] Scanning localhost for open services..."
nmap -sT -F --open --unprivileged localhost

echo ""
echo "======================================"
echo " SCAN COMPLETE"
