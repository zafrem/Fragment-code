from ipaddress import IPv4Network
from ipaddress import IPv4Address


IPv4Address(3691907365)  # IPv4Address('220.14.9.37')
addr = IPv4Address(b"\xdc\x0e\t%")  # IPv4Address('220.14.9.37')

print(int(addr)) # 3691907365
print(addr.packed) # b'\xdc\x0e\t%'

net = IPv4Network("192.4.2.0/24")
print(net.num_addresses) # 256
print(net.prefixlen) # 24
print(net.netmask) # IPv4Address('255.255.255.0')

print(IPv4Address("192.4.2.12") in net) # True
print(IPv4Address("192.4.20.2") in net) # False

print(IPv4Network("192.4.2.0/255.255.255.0")) # IPv4Network('192.4.2.0/24')
print(net.broadcast_address) # IPv4Address('192.4.2.255')

for addr in net:
    print(addr)
'''
192.4.2.0
192.4.2.1
192.4.2.2
. . .
192.4.2.13
192.4.2.14
192.4.2.15
'''

h = net.hosts()
print(type(h)) # <class 'generator'>
print(next(h)) # IPv4Address('192.4.2.1')
print(next(h)) # IPv4Address('192.4.2.2')

small_net = IPv4Network("192.0.2.0/28")
big_net = IPv4Network("192.0.0.0/16")

print(small_net.subnet_of(big_net)) # True
print(big_net.supernet_of(small_net)) # True
if IPv4Address('192.0.0.1') in IPv4Network("192.0.0.0/16"): #True
    print("Subnet")