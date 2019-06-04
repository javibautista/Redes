from paquete import *
from constantes import *
from pickle import *
from socket import *

#EMISOR(Cliente)

def create_UDPsock():
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    return UDPsocket

#va de capa de aplicación a la de transporte
def rdt_send(): #1
    data = input('Ingrese el mensaje a enviar: ')
    return data.encode('utf-8')
#generador
def make_pkt(data):
    pkt=Packet(SOURCE_PORT,RECEIVER_PORT,data) #paquetamiento, paquete.py
    return pkt

def udp_send(socket, pkt): #
    #3. Establecemos el destinatario
    #4. Enviamos el mensaje
    dato = dumps(pkt)#4mod
    socket.sendto(dato,(RECEIVER_IP,RECEIVER_PORT))#(paquete, ('localhost', 20000))#5mod

def close_socket(socket):
    UDPsocket.close()

if __name__ == "__main__":
    #1. Creamos el socket
    emisor=create_UDPsock()
    while 1:
        #2. mensaje desde teclado, inst
        data = rdt_send() # recibo, inst
        pkt = make_pkt(data) # genero, empaqueto, inst
        udp_send(emisor, pkt) # envio paquete, inst
        #prueba
        """
        pkt = Packet(2000, 2001, data) # piso y redefino pkt
        print(pkt.get_source())
        print(pkt.get_receiver())
        print(pkt.get_long())
        checksum = calculate_checksum(pkt)
        print('La primer comprobacion da: ', checksum)
        pkt.set_checksum(checksum)
        new_checksum = calculate_checksum(pkt)
        print('la segunda comprobacion da: ', new_checksum)
        """
    close_socket(emisor)

