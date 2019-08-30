import socket
import threading
import time

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind ip
s.bind(('127.0.0.1', 8088))
s.listen(5)
print('Waiting for connection...Zzz')

def tcplink(sock, address):
    print('Accept a new tcp connetion from %s:%s...' % address)
#    sock.send(b'Welcome to server')
    buffer = []
    while True:
        data = sock.recv(1024)
        buffer.append(data)
        time.sleep(1)
        if len(data) < 1024:
            print((b'client1>'.join(buffer)).decode('utf-8'))
            buffer = []
# data为空的时候，not data为True
        if not data:
            break

    sock.close()


while True:
    # accept a connection
    sock, address = s.accept()
    # create a new thread to deal with the TCP connection
    t = threading.Thread(target=tcplink, args=(sock, address))
    t.start()




