from . import rotor
from . import cableado as cab

cableado = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def configurar_rotores(posiciones: list):
    global rotor1, rotor2, rotor3
    rotor1 = rotor.Rotor(cableado, posiciones[0])
    rotor2 = rotor.Rotor(cableado, posiciones[1])
    rotor3 = rotor.Rotor(cableado, posiciones[2])

def cifrar_mensaje(mensaje: str) -> str:
    
    rotor1.reiniciar()
    rotor2.reiniciar()
    rotor3.reiniciar()
    mensaje_cifrado = ""
    for letra in mensaje:
        vuelta1 = rotor1.avanzar()
        if vuelta1:
            vuelta2 = rotor2.avanzar()
            if vuelta2:
                rotor3.avanzar()    
        letra_cifrada = rotor1.cifrar(letra)
        letra_cifrada = rotor2.cifrar(letra_cifrada)
        letra_cifrada = rotor3.cifrar(letra_cifrada)
        mensaje_cifrado += letra_cifrada
        
        print(rotor1.posicion, rotor2.posicion, rotor3.posicion)
    return mensaje_cifrado

def descifrar_mensaje(mensaje: str) -> str:
    rotor1.reiniciar()
    rotor2.reiniciar()
    rotor3.reiniciar()
    mensaje_descifrado = ""
    for letra in mensaje:
        vuelta1 = rotor1.avanzar()
        if vuelta1:
            vuelta2 = rotor2.avanzar()
            if vuelta2:
                rotor3.avanzar()    
        letra_descifrada = rotor3.descifrar(letra)
        letra_descifrada = rotor2.descifrar(letra_descifrada)
        letra_descifrada = rotor1.descifrar(letra_descifrada)
        mensaje_descifrado += letra_descifrada
        print(rotor1.posicion, rotor2.posicion, rotor3.posicion)
    return mensaje_descifrado