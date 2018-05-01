import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(5):
    s.sendto(time.ctime(), ('171.69.54.194', 9600))
    time.sleep(1)
s.close()

