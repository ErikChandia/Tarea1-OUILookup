import getopt
import sys
import socket
import uuid
import re

def verMac(mac):
    f = open('datos.txt', encoding="utf8")
    mensaje = f.readlines()
    for i in mensaje:
        if(i.find(mac)==0):
            x = i.split('\t')
            print("\nDireccion MAC: " + mac)
            print("Vendor: " + x[2])
            sys.exit(1)
    print("\nDireccion MAC: " + mac)
    print('Dispositivo no encontrado en la base de datos')
    f.close()

def verIp(ip):
    cont = 0
    nombreEquipo = socket.gethostname()
    direccionEquipo = socket.gethostbyname(nombreEquipo)
    for numero in ip:
        if(numero != direccionEquipo[cont]):
            print("La ip no pertenece a la red")
            sys.exit(1)
        elif(cont > 7):
            break
        cont = cont + 1
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    print("\nMAC del equipo: " + mac)
    
try:
    opts, args = getopt.getopt(sys.argv[1:],"i,m",['ip=','mac='])
except:
    print("Parametros ingresados de forma erronea o no ingresados")

IP = None
MAC = None

for option, arg in opts:
    if option in ('--ip'):
        IP = arg
        verIp(IP)
        break
    elif option in ('--mac'):
        MAC = arg
        verMac(MAC)
        break

