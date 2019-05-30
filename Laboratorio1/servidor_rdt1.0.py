from socket import *

def create_UDPsocket(address, port):
    UDPsocket=socket(AF_INET, SOCK_DGRAM)
    UDPsocket.bind((address, port))
    return UDPsocket

# va de la capa de tansporte a capa de aplicación
def deliver_data(data):
    print (data)

def rdt_rcv(socket):
    packet = socket.recv(2048)
    return packet

# extrae del paquete 
def extract(packet):
    return packet

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
    servidor= create_UDPsocket('localhost', 20000)
    print('servidor corriendo')
    while 1:
        #recibir paquete
        packet = rdt_rcv(servidor)
        #extraigo paquete
        data = extract(packet)
        #entrega a capa de aplicación
        deliver_data(data)
        archivo = open('DATA.txt', 'a') # a: anexa
        archivo.write('\n' + str(data))
        archivo.close()
    close_socket(servidor)

