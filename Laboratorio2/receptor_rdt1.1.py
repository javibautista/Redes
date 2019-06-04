from socket import *
from paquete import *
from constantes import *
from pickle import *

#RECEPTOR(SERVIDOR)

def create_UDPsocket(address, port):
    UDPsocket=socket(AF_INET, SOCK_DGRAM)
    UDPsocket.bind((address, port))
    return UDPsocket

# va de la capa de tansporte a capa de aplicación
#entrega los datos. printea por consola.
def deliver_data(datas):#5
    print (datas)

# funcion recibe packet(cap.2048), descomprime(loads)
def rdt_rcv(socket):#2
    packet = loads(socket.recv(2048))
    return packet

# extrae del paquete de rdt_rcv
def extract(packet):#4
    datas = packet.get_data()
    return datas

#da por terminado el mensaje
def close_socket(socket):
    socket.close()#6

if __name__ == "__main__":
    receptor= create_UDPsocket(RECEIVER_IP, RECEIVER_PORT)
    print('receptor corriendo')
    while 1:
        #receptor recibie paquete en var packet
        # 'instancio' rdt_rcv()
        packet = rdt_rcv(receptor) #1
        #extraigo paquete
        # 'instancio' extract()
        datas = extract(packet)#3
        #entrega a capa de aplicación
        # 'instancio' deliver_data()
        deliver_data(datas)#4
        archivo = open('DATA.txt', 'a') # a: anexa
        archivo.write(str(datas)+'\n')
        archivo.close()
    close_socket(receptor)

