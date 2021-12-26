import scapy.all as scapy
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP address / IP range.")
	options = parser.parse_args()
	if not options.target:
		parser.error("[-] Specify target IP address / IP range, use --help for more information.")
	return options
	
def scan(ip):
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_bcast = broadcast/arp_req
	answered = scapy.srp(arp_req_bcast, timeout=1, verbose=False)[0]
	

	clients_list = []
	for x in answered:
		client_dict = {"ip": x[1].psrc, "mac": x[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list
	

def print_results(list_result):
	print("IP\t\t\t\tMac Address\n----------------------------------------------------------------")
	for client in list_result:
		print(client["ip"] + "\t\t\t" + client["mac"])
	

options = get_args()
scan_result = scan(options.target)
print_results(scan_result)
