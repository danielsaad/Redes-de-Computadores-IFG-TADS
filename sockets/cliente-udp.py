import socket
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input("Digite a sua mensagem: ")
while msg != ".":
    udp.sendto (msg.encode(), dest)
    msg = input("Digite a sua mensagem: ")
udp.close()
