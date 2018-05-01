import socket, time, os

def server(host, port, handler):
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print 'Server up, running, and waiting for call'
    try:
        while True:
            c, a = s.accept()
            pid = os.fork()
            if pid:
                # I am the parent:
                c.close()
            else:
                # I am the clone
                handler(c, a)
                os._exit(0)
    finally:
        s.close()

def time_handler(c, a):
    #print "Received connection from", a
    c.sendall("Hello %s\r\n" % a[0])
    c.sendall("The time is %s\r\n" % time.ctime())
    c.close()

def slow_time_handler(c, a):
    print "Received connection from", a
    c.sendall("Hello %s\r\n" % a[0])
    c.sendall("The time is %s\r\n" % time.ctime())
    for i in range(15):
        c.sendall("The count is %s\r\n" % i)
        time.sleep(1)
    c.close()

if __name__ == '__main__':

    server(host='', port=9600, handler=slow_time_handler)
