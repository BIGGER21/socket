import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create the connection
s.connect(('127.0.0.1', 8086))

# receive data
buffer = []
while True:
    # the most received bytes are 1KB
    data = input('To server1>')
    s.send(data.encode('utf-8'))
    if data is not None:
        buffer.append(data)
    else:
        break

rec_data = b''.join(buffer)

# print the receive data
print(rec_data.decode('utf-8'))

# close socket
s.send(b'exit')
s.close()
