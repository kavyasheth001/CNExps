import socket

def start_tcp_server():
    host = '127.0.0.1'
    port=12344

    server_socket=socket. socket(socket.AF_INET, socket. SOCK_STREAM)

    server_socket.bind((host,port))

    print(f"Server started on {host}: {port}")
    server_socket. listen(1)
    conn, addr=server_socket. accept()
    print(f"Connection from {addr}")

    while True:
        data=conn.recv(1024).decode("utf-8")
        if not data or data.lower() == "exit":
            print("Closing connection")
            break
        print(f"received from client: {data}")
        response=f"ServerReceived : {data}"
        conn. send(response.encode("utf-8"))
    conn.close()
start_tcp_server()
