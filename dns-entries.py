def generate_dns_entry(hostname, mac_address, ddns_domain):
    entry = f"host {hostname} {{\n"
    entry += f"  hardware ethernet {mac_address};\n"
    entry += f"  option host-name \"{hostname}\";\n"
    entry += f"  ddns-hostname \"{hostname}\";\n"
    entry += f"  ddns-domainname \"{ddns_domain}\";\n"
    entry += "  ddns-updates on;\n"
    entry += "}\n"
    return entry

def gather_device_info(device_num):
    print(f"\nEnter information for Device {device_num}:")
    hostname = input("Enter the hostname: ")
    mac_address = input("Enter the MAC address: ")
    return hostname, mac_address

def gather_devices_info(num_devices):
    devices_info = []
    for i in range(1, num_devices + 1):
        device_info = gather_device_info(i)
        devices_info.append(device_info)
    return devices_info

def main():
    num_devices = int(input("Enter the number of devices you want to add to DNS entries: "))
    ddns_domain = "nimblestorage.com"  # Fixed ddns-domainname

    devices_info = gather_devices_info(num_devices)

    dns_entries = []

    for device_num, device_info in enumerate(devices_info, 1):
        hostname, mac_address = device_info
        dns_entry = generate_dns_entry(hostname, mac_address, ddns_domain)
        dns_entries.append(dns_entry)

    print("\nGenerated DNS Entries:\n")
    for entry in dns_entries:
        print(entry)
