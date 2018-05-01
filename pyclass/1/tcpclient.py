
import socket

host = 'www.jython.org'
port = 80
resource = '/'

request =  'GET %s HTTP/1.1\r\n' % resource
request += 'Host: %s\r\n' % host
#request += 'Range: bytes=0-200\r\n'                                    
#request += 'Accept-Encoding: gzip\r\n'                                 
#request += 'If-Modified-Since: Wed, 13 Nov 2013 23:08:27 UTC\r\n'
request += 'Connection: close\r\n'
request += '\r\n' 

s = socket.socket()
try:
    s.connect((host, port))
    s.send(request)
    page = s.recv(4096)
    print len(page)
#    print page.replace('\r\n', '\n')
finally:
    s.close()
