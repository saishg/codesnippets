import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9600))
try:
    while True:
        msg, who = s.recvfrom(256)
        print msg, who
finally:
    s.close()

'''
Battleship picture:
http://blogs-images.forbes.com/erikkain/files/2012/02/battleship-board-game.jpg
https://en.wikipedia.org/wiki/Battleship_(game)

>>> ships = {'B4', 'B5', 'B6', 'B7', 'C2', 'D2', 'D3'}
>>> guess = 'G4'
>>> 'Hit!' if guess in ships else 'Miss!'
'Miss!'
>>> guess = 'D2'
>>> 'Hit!' if guess in ships else 'Miss!'
'Hit!'

$ python battleship_server.py localhost 8600 B4 B5 B6 B6 C2 D2 E2

------------------------------------
$ python battleship_client.py localhost 8600 G4
Miss!
$ python battleship_client.py localhost 8600 B5
Hit!

'''
