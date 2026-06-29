import ipaddress

ip = input("Enter IP with CIDR (Example 192.168.1.10/24): ")

network = ipaddress.ip_network(ip, strict=False)

print("\n----- Network Information -----")
print("Network Address :", network.network_address)
print("Broadcast Address :", network.broadcast_address)
print("Subnet Mask :", network.netmask)
print("Total Addresses :", network.num_addresses)