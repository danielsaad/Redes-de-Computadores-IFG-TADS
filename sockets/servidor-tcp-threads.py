import socket
import _thread

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
BACKLOG = 5
def conectado(con, cliente):
    print ('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg.decode())

    print ("Finalizando conexao do cliente", cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(BACKLOG)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()
