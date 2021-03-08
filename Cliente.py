import socket

print("Cliente")

ipServidor = "localhost"
puertoServidor = 9798
nombreEquipo = socket.gethostname()
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ipServidor,puertoServidor))
print("servidor", (ipServidor, puertoServidor))

while True:
    msg = input("--")
    cliente.send(msg.encode('utf-8'))
    respuesta = cliente.recv(1024)
    if msg == 'salir':
        break
    print("->", respuesta.decode('utf-8'))
cliente.close()