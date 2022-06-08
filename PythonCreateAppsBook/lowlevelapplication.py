import socket


def generate_response(request):
    pass


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        # print(request.decode('utf-8'), end="\n")
        print(request, end="\n")
        print(addr)

        response = generate_response(request.decode('utf-8'))
        client_socket.sendall('hello world'.encode())
        client_socket.close()


if __name__ == '__main__':
    run()
