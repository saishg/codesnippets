import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.sendto('Now is better than never.', ('171.69.54.164', 9600))
finally:
    s.close()
