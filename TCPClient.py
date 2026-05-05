import socket

def start_tcp_client():
    host = '127.0.0.1'
    port=12344
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))
    print(f"Connection started to server at : {host}, {port}")

    while True:
        message=input("Enter message to send or (type 'exit' to close connection)")
        client_socket. send(message.encode("utf-8"))

        if message.lower() == "exit":
            print(f"Connection Closed")
            break   

        response=client_socket.recv(1024).decode("utf-8")
        print(f"server response: {response}")

    client_socket.close()

start_tcp_client()