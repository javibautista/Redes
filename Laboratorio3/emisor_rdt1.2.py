from constants import *
from socket import *

def create_socket():
    # IMPLEMENTAR
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    return UDPsocket

def rdt_send():
    # IMPLEMENTAR
    data = input('Ingrese el mensaje a enviar: ')
    return data.encode('utf-8')

def make_pkt(data):
    # IMPLEMENTAR
    pkt=Packet(SENDER_IP,SENDER_PORT,data) #paquetamiento, paquete.py
    return pkt

def udp_send(socket, receiver, pkt):
    # IMPLEMENTAR
    dato = dumps((receiver, pkt))
    socket.sendto(dato,(NETWORK_IP,NETWORK_PORT))
"""
def recv_message(UDPsocket):
    # IMPLEMENTAR
"""

def close_socket(socket, signal, frame):
    print ("\n\rCerrando socket")
    socket.close()
    exit(0)


if __name__ == "__main__":
    # Creamos el socket
    emisor = create_socket()
    # Registramos la senial de salida
    signal.signal(signal.SIGINT, partial(close_socket, emisor))
    # Iteramos indefinidamente
    while True:
        # Leemos el mensaje desde teclado
        data = rdt_send()
        # Hacemos el paquete
        pkt = make_pkt(data)
        # Establecemos el destinatario
        receiver = (RECEIVER_IP, RECEIVER_PORT)
        # Enviamos el mensaje
        udp_send(emisor, receiver, pkt)
    close_socket(emisor)
