def generate_dns_commands(num_devices):
    forward_dns_commands = []
    reverse_dns_commands = []

    for i in range(1, num_devices + 1):
        device_name = input(f"Enter the name of device {i}: ")
        ip_address = input(f"Enter the IP address for device {i}: ")

        # Generate forward DNS command
        forward_command = f"update add {device_name}.mip.nimblestorage.com 86400 IN A {ip_address}"
        forward_dns_commands.append(forward_command)

        # Generate reverse DNS command
        ip_octets = ip_address.split('.')
        reverse_ip = ".".join(reversed(ip_octets))
        reverse_command = f"update add {reverse_ip}.in-addr.arpa 86400 PTR {device_name}.mip.nimblestorage.com"
        reverse_dns_commands.append(reverse_command)

    return forward_dns_commands, reverse_dns_commands

def main():
    num_devices = int(input("Enter the number of devices: "))
    forward_commands, reverse_commands = generate_dns_commands(num_devices)

    print("\nForward DNS Commands:\n")
    for command in forward_commands:
        print(command)

    print("\nReverse DNS Commands:\n")
    for command in reverse_commands:
        print(command)

if __name__ == "__main__":
    main()
