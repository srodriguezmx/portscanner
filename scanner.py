#!/bin/python 

import sys
import socket 
from datetime import datetime

if len(sys.argv) == 2: # Define que el comando debe de recibir dos argumentos.
    target = socket.gethostbyname(sys.argv[1]) #Define que el argumento con
                                               #indice 1 es nuetro objetivo, puede host name
else:# Imprime si no esta correcta la sintaxis. 
    print("Invalid amount of arguments.")
    print("Syntax: pynton3 scanner.py <ip>" )

#Agregar un banner 
print("-" * 50) # Imprime borde 
print(f"Analizando la Ip: {target}") # Imprime la IP
print("Tiempo de inicio es:" + str(datetime.now())) # Imprime la fecha de actual 
print("-" * 50)

try: # Permite analizar un bloque de codigo para identificar errores, da excepsion

    for port in range(50,85): #loop for para el rango de puertos
        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variable que recibe ip y puerto
        socket.setdefaulttimeout(1) # Indica solo verificar durante un segundo cada puerto
        result = s.connect_ex((target,port))# Tupla para verificar cada puerto
                                            #connect_ex muestra el error en pantalla
        if result == 0:# If si el puerto esta abierto el resultado sera 0 si esta cerrado sera 1
            print(f"Port {port} is open")# Imprimer puertos abierto
        s.close()# Si esta cerrado cierra la conexion. 

#Mensaje para presentacion de error de modulo socket  
except KeyboardInterrupt:
    print ("/n Existing Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error: 
    print("Cooud not connect to the server")
    sys.exit()



