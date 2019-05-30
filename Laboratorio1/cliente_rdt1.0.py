from socket import *

def create_UDPsock():
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    return UDPsocket

#va de capa de aplicación a la de transporte
def rdt_send():
    data = input('ingrese mensaje: ')
    return data.encode('utf-8')
#generador
def make_pkt(data):
    return data

def udp_send(socket, paquete):
    #3. Establecemos el destinatario
    #4. Enviamos el mensaje
    socket.sendto(paquete, ('localhost', 20000))

def close_socket(socket):
    UDPsocket.close()

if __name__ == "__main__":
    #1. Creamos el socket
    cliente=create_UDPsock()
    while 1:
        #2. Leemos el mensaje desde teclado
        data = rdt_send() # recibo
        paquete = make_pkt(data) # genero, empaqueto
        udp_send(cliente, paquete) # envio paquete
    close_socket(cliente)

#import sys
#try:
#    UDPsocket.bind((host, port))
#except socket.error as e:
#    print(str(e))
#import ipdb; ipdb.set_trace()
#host=''
#port=20000

