
import sys

NEGRO = 0
MARRON = 1
ROJO = 2
NARANJA = 3
AMARILLO = 4
VERDE = 5
AZUL = 6
VIOLETA = 7
GRIS = 8
BLANCO = 9

coloresvalidos = ['negro', 'marron', 'rojo', 'naranja', 'amarillo', 'verde', 'azul', 'violeta', 'gris', 'blanco']


def colores(col):
    match col:
        case 'negro':
            return NEGRO
        case 'marron':
            return MARRON
        case 'rojo':
            return ROJO
        case 'naranja':
            return NARANJA
        case 'amarillo':
            return AMARILLO
        case 'verde':
            return VERDE
        case 'azul':
            return AZUL
        case 'violeta':
            return VIOLETA
        case 'gris':
            return GRIS
        case 'blanco':
            return BLANCO


# while True:
#     print("")
#     banda1 = input("Ingrese el color de la primera banda: ").lower()
#     if banda1 not in coloresvalidos:
#         print("Opcion Invalida")
#         continue
#     banda2 = input("Ingrese el color de la segunda banda: ").lower()
#     if banda2 not in coloresvalidos:
#         print("Opcion Invalida")
#         continue
#     banda3 = input("Ingrese el color de la tercera banda (si no existe no poner nada): ").lower()
#     if banda3 not in coloresvalidos + ['', '\n']:
#         print("Opcion Invalida")
#         continue
#     bandamulti = input("Ingrese el color de la banda de multiplicador ").lower()
#     if bandamulti not in coloresvalidos:
#         print("Opcion Invalida")
#         continue
#     break

banda1 = sys.stdin.readline().strip()
if banda1 not in coloresvalidos:
        sys.stdout.write("Opcion Invalida")
        quit()
banda2 = sys.stdin.readline().strip()
if banda2 not in coloresvalidos:
        sys.stdout.write("Opcion Invalida")
        quit()
banda3 = sys.stdin.readline().strip()
if banda3 not in coloresvalidos + ['', '\n']:
        sys.stdout.write("Opcion Invalida")
        quit()
bandamulti = sys.stdin.readline().strip()
if bandamulti not in coloresvalidos:
        sys.stdout.write("Opcion Invalida")
        quit()

class resistor:
    def __init__(self, color1, color2, color3, colorm):
        self.c1 = color1
        self.c2 = color2
        self.cm = colorm
        self.c3 = color3

    def getb1(self):
        return colores(self.c1)

    def getb2(self):
        return colores(self.c2)

    def getb3(self):
        match self.c3:
            case '\n':
                return ""
            case '':
                return ""
            case _:
                ...
        return colores(self.c3)

    def getbm(self):
        match self.cm:
            case 'negro':
                return ""
            case 'marron':
                return '0'
            case 'rojo':
                return '00'
            case 'naranja':
                return '000'
            case 'amarillo':
                return '0000'
            case 'verde':
                return '00000'
            case 'azul':
                return '000000'
            case 'violeta':
                return '0000000'
            case 'gris':
                return '00000000'
            case 'blanco':
                return '000000000'


res = resistor(banda1, banda2, banda3, bandamulti)

sys.stdout.write(f"La resistencia es de {res.getb1()}{res.getb2()}{res.getb3()}{res.getbm()}ohms")
