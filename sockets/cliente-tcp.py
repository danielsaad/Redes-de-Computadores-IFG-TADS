import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = input("Digite a sua mensagem: ")
while msg != ".":
    tcp.send (msg.encode())
    msg = input("Digite a sua mensagem: ")
tcp.close()
