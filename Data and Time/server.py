from socket import *
import time

s = socket(AF_INET,SOCK_STREAM)

hostName = gethostname()
port = 12345

s.bind((hostName,port))
s.listen(4)
client, address = s.accept()
print('Listening...')
currentTime = time.ctime(time.time()) + "\r\n"
client.send(currentTime.encode('ascii'))
