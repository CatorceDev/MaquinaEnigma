from . import rotor

rotor1 = rotor.Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0)
rotor2 = rotor.Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 0)
rotor3 = rotor.Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BDFHJLCPRTXVZNYEIWGAKMUSQO", 0)

def cifrar_mensaje(mensaje: str) -> str:
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
    return mensaje_cifrado

def descifrar_mensaje(mensaje: str) -> str:
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
    return mensaje_descifrado