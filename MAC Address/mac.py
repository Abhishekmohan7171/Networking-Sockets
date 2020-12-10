import os
import getmac
import socket
hostname = socket.gethostname()



# getting IP Address
IPAddr = socket.gethostbyname(hostname)

# printing hostname
print("Your Computer Name is:" + hostname)

# printing IP Address
print("Your Computer IP Address is:" + IPAddr)
ip = ""

while ip != "exit":
    ip = input("Enter IP address [or exit]: ")
    if ip == "exit":
        continue
    os.system("ping {}".format(ip))
    msg = input("Retreive MAC address? [y/n]: ")
    if msg == "n":
        continue
    mac = getmac.get_mac_address(ip = ip)
    print("MAC address: {}".format(mac))
print("Exiting")