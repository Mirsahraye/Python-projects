import subprocess
import time
import optparse
import re

def recv_args():
	parser = optparse.OptionParser()

	parser.add_option("-i", "--interface", dest="interface", help="Enter the Interface for the new Mac Address")
	parser.add_option("-m", "--new_mac", dest="new_addr", help="New Mac Address.")
	(options, args) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Specify an interface, use --help for more information.")
	elif not options.new_addr:
		parser.error("[-] Specify a MAC address, use --help for more info.")
	return options

def mac_changer(interface, new_addr):
	subprocess.call(["ifconfig", interface, "down"])
	time.sleep(1)
	subprocess.call(["ifconfig", interface, "hw", "ether", new_addr])
	time.sleep(1)
	subprocess.call(["ifconfig", interface, "up"])
	time.sleep(1)
	print("------------------------------------------------------------")

def select_mac(interface):
	ifc_output = subprocess.check_output(["ifconfig", interface])
	ifc_mac_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifc_output)

	if ifc_mac_output:
		return ifc_mac_output.group(0)
	else:
		print("[-] Could not read Mac Address.")


options = recv_args()
mac_changer(options.interface, options.new_addr)
current_mac = select_mac(options.interface)
if current_mac == options.new_addr:
	print("[+] Mac Address succesfully changed to : " + current_mac)
else:
	print("[-] Unexpected error occured.")
