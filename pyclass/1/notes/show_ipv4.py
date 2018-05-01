''' Demonstrate how to parse column-oriented text meant for humans.
    This is typical output for Cisco IOS, and is a common case,
    but far, far from a worst case.

    # show ipv4 interfaces brief
'''

with open('notes/ipv4_int_bri.txt') as f:
    for line in f:

        # line = line.rstrip()
        # interface, ipaddr, status, protocol = line.split()

        interface = line[:31].rstrip()
        ipaddr = line[31:47].rstrip()
        status = line[47:69].rstrip()
        protocol = line[69:].rstrip()
        
        if status.lower() == 'up':
            print '%-15s %s' % (ipaddr, interface)
