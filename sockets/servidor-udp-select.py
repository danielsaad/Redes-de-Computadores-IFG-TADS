import socket
import select
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
inputs = [udp]
outputs = []
timeout = 5
while True:
    readable,writable,exceptional = select.select(inputs,
        outputs, inputs,timeout)
    if not (readable or writable or exceptional):
        print ("Pacote perdido!")
    elif (readable):
        msg, cliente = udp.recvfrom(1024)
        print (cliente, msg.decode())
udp.close()
