''' Goal:   Show how event loops work.
            Understand callback style programming
            Learn patterns of callback programming in event loops
            Practice with heaps, named tuples, partial, and the time module.
            Develop an into insight into the core of Twisted, Tornado, Diesel, sched and other event loops
'''

# http://golubenco.org/understanding-the-code-inside-tornado-the-asynchronous-web-server-powering-friendfeed.html

from pprint import pprint
from time import time, sleep
from heapq import heappush, heappop
from collections import namedtuple
from functools import partial

Event = namedtuple('Event', ['event_time', 'task'])

events = []

def add_event(event_time, task):
    heappush(events, Event(event_time, task))

def call_later(delay, task):
    add_event(time() + delay, task)

def call_periodic(delay, interval, task):
    def inner():
        task()
        call_later(interval, inner)
    call_later(delay, inner)

def event_loop():
    while events:
        # for socket in poll(sockets):
        #    data = socket.recv()
        #    callbacks[socket]()
        while events[0].event_time > time():
            sleep(0.01)
        event_time, task = heappop(events)
        task()

##########################################################################

def show_msg(msg):
    print msg

def show_two():
    print 'Two'

def show_five():
    print 'Five'

def show_ten():
    print 'Ten'

def show_heartbeat():
    print 'I am alive!'

def schedule_five_three_times():
    call_later(2, show_five)
    call_later(4, show_five)
    call_later(6, show_five)

call_later(8, show_two)
call_later(2, show_ten)
call_later(1, show_two)
call_later(0, partial(show_msg, 'Howdy!'))
call_later(10, partial(show_msg, "C'ya!"))
call_later(3, schedule_five_three_times)
call_periodic(1, 3, show_heartbeat)
pprint(events)
event_loop()
    

