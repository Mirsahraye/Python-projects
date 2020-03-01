import subprocess
import time
import optparse

parser = optparse.OptionParser()


def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
        parser.add_option("-m", "--new_mac", dest="new_mac", help="New media access control address")
        return parser.parse_args()

def change_mac(interface, new_mac):
        subprocess.call("ifconfig " + interface + " down", shell=True)
        time.sleep(1)
        print("[+] " + interface + " Interface is down")

        subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
        time.sleep(1)
        print("[+] " + interface + " Mac address changed to: " + new_mac)

        subprocess.call("ifconfig " + interface + " up", shell=True)
        time.sleep(1)
        print("[+] Interface is up") 

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
