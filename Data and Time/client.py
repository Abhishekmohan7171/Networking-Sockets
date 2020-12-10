from socket import *
s = socket(AF_INET,SOCK_STREAM)

hostName = gethostname()
port = 12345

s.connect((hostName,port))
tm = s.recv(1024)
print("The time got from the SERVER is %s" % tm.decode('ascii'))
