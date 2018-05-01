import socket

def urlread(url, port=80):
    'Emulate urllib.urlopen(url).read() but only for HTTP'
    if not url.startswith('http://'):
        raise ValueError('Sorry, I only support HTTP')
    host, resource = url[7:].split('/', 1)
    resource = '/' + resource
    
    request =  'GET %s HTTP/1.1\r\n' % resource
    request += 'Host: %s\r\n' % host
    #request += 'Range: bytes=0-200\r\n'                                    
    #request += 'Accept-Encoding: gzip\r\n'                                 
    #request += 'If-Modified-Since: Wed, 13 Nov 2014 23:08:27 UTC\r\n'
    request += 'Connection: close\r\n'
    request += '\r\n' 

    s = socket.socket()
    try:
        s.connect((host, port))
        s.send(request)

        blocks = []
        while True:
            block = s.recv(4096)
            if len(block) == 0:
                break
            blocks.append(block)
        page = ''.join(blocks)
       
        return page.replace('\r\n', '\n')
    finally:
        s.close()

if __name__ == '__main__':

    for url in [
        'http://www.jython.org/',
        'http://www.perl.org/',
    ]:
        print urlread(url)
