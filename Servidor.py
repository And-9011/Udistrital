import socket

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9798))
s.listen(5)
  
print("server")
print("Servidor de chat\n")

active, addr = s.accept()


while True:
    recibido = active.recv(1024)
    print("--", recibido.decode('utf-8'))
    enviar=input("->")
    active.send(enviar.encode('utf-8'))
active.close()