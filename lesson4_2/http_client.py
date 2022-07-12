import socket

request = 'GET /CScourses/03b1_minimal.html HTTP/1.1\r\nHost: industy1.org\r\n\r\n'
sock = socket.create_connection(('50.87.178.13', 80))
sock.sendall(request.encode(encoding='utf-8'))
data = sock.recv(1000)
sock.close()
print(data.decode(encoding='utf-8'))


def http_get(host, page):
    sock = socket.create_connection((host, 80))
    sock.sendall(("GET " + page + " HTTP/1.1\r\nHost: " + host + '\r\n\r\n').encode())
    print(sock.recv(1000).decode())
    sock.close()


def http_head(host, page):
    sock = socket.create_connection((host, 80))
    sock.sendall(("HEAD " + page + " HTTP/1.1\r\nHost: " + host + '\r\n\r\n').encode())
    print(sock.recv(1000).decode())
    sock.close()


http_get('50.87.178.13', '/CScourses/03b1_minimal.html')
http_head('50.87.178.13', '/CScourses/03b1_minimal.html')
