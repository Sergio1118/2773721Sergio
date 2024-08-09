import json
import os
import time
usarios=[]

id='id'
nombre='nombre'
apellido='apellido'
nuemero='numero_telefonico'
documento='documento'
emil="emil"

def Id(usarios):
    lon=len(usarios)
    if lon==0:
        return 1
    else:
        lon-=1
        res=usarios[lon][id]+1
        return res



def agregra():
    with open('usarrios.json', 'r') as archivo:
        usarios = json.load(archivo)
    lon=Id(usarios)
    nom=input('ingrese su nombre ')
    ape=input('ingrese su apellido ')
    num=input('ingree sus numero telefonico ')
    doc=input('ingrese su numero de documento ')
    emi=input('ingrese sus correo eletronico ')
    dicinerio={id:lon, nombre: nom ,apellido: ape, nuemero: num, documento: doc, emil:emi}
    usarios.append(dicinerio)
    with open('usarrios.json', 'w') as archivo:
        json.dump(usarios, archivo, indent=4) 
    usarios.clear()


def actulizar():
    with open('usarrios.json', 'r') as archivo:
        usarios = json.load(archivo)
    doc=input("ingrese sus documento para la actulizacion ")
    opciones=int(input(" 1 nombre \n 2  apellido \n 3 numero_telefonico \n 4 documento \n 5 emil " ))
    contenoto=""
    lon=len(usarios)
    match opciones:
        case 1:
            contenoto=nombre
            p=input('ingrese su nombre ')
        case 2:
            contenoto=apellido
            p=input('ingrese su apellido ')
        case 3:
            contenoto=nuemero
            p=input('ingree sus numero telefonico ')
        case 4:
            contenoto=documento
            p=input('ingrese su numero de documento ')
        case 5:
            contenoto=emil
            p=input('ingrese sus correo eletronico ')
    for i in range(0,lon):
        if usarios[i][documento] == doc:
            usarios[i][contenoto]=p
    with open('usarrios.json', 'w') as archivo:
        json.dump(usarios, archivo, indent=4) 
    usarios.clear()


def eliniminar():
    with open('usarrios.json', 'r') as archivo:
        usarios = json.load(archivo)
    doc=input("ingrese sus documento para la eliminacion ")
    usarios = [usuario for usuario in usarios if usuario.get('documento') != doc]
    with open('usarrios.json', 'w') as archivo:
        json.dump(usarios, archivo, indent=4) 
    usarios.clear()


def mostra():
    with open('usarrios.json', 'r') as archivo:
        usarios = json.load(archivo)
    print(usarios)



while True:
    opciones=int(input(" 1 agragrra \n 2  actualizar \n 3 eleniminar \n 4 mostra \n o otro numero  para salir  " ))
    match opciones:
        case 1:
            agregra()
        case 2:
            actulizar()
        case 3:
            eliniminar()
        case 4:
            mostra()
        case _:
            print('salidad')
            break
    time.sleep(2)
    os.system('cls')