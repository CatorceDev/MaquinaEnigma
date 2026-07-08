from . import rotor

rotor1 = rotor.Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0)
rotor2 = rotor.Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 0)
rotor3 = rotor.Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BDFHJLCPRTXVZNYEIWGAKMUSQO", 0)

def cifrar_mensaje(mensaje: str) -> str:
    mensaje_cifrado = ""
    vuelta1 = rotor1.avanzar()
    if vuelta1:
        vuelta2 = rotor2.avanzar()
        if vuelta2:
            rotor3.avanzar()
            
    for letra in mensaje:
        letra_cifrada = rotor1.cifrar(letra)
        letra_cifrada = rotor2.cifrar(letra_cifrada)
        letra_cifrada = rotor3.cifrar(letra_cifrada)
        mensaje_cifrado += letra_cifrada
    return mensaje_cifrado