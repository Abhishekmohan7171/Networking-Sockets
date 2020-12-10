import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

udp_host = socket.gethostname()
udp_port = 12345

msg = input("Enter the IP address: ")

sock.sendto(msg.encode(),(udp_host,udp_port))
