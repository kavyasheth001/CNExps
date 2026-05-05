import socket
client_socket=socket. socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address=('localhost' , 12345)
client_socket. sendto(b"Hello from moksh", server_address)
data, addr=client_socket.recvfrom(1024)
print("Received from server",data.decode())
client_socket.close()
