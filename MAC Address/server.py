import socket
import subprocess

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345

sock.bind((udp_host,udp_port))

while True:
    print("Waiting for client...")
    data,addr = sock.recvfrom(1024)
    command = "arp -a " + str(data.decode())
    p = subprocess.run(command, capture_output=True, shell=True)
    print(p.stdout)
