import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345 

msg = "Hey Python, This is the UDP Experiment !"
print('UDP Target IP:',udp_host)
print('UDP Target Port:',udp_port)

sock.sendto(msg.encode(),(udp_host,udp_port))
