from . import rotor

class machine:
        
    def __init__(self, cableados:list, posiciones: list):
        self.rotor1 = rotor.Rotor(cableados[0], posiciones[0])
        self.rotor2 = rotor.Rotor(cableados[1], posiciones[1])
        self.rotor3 = rotor.Rotor(cableados[2], posiciones[2])

    def cifrar_mensaje(self, mensaje: str) -> str:
        
        self.rotor1.reiniciar()
        self.rotor2.reiniciar()
        self.rotor3.reiniciar()
        mensaje_cifrado = ""
        for letra in mensaje:
            vuelta1 = self.rotor1.avanzar()
            if vuelta1:
                vuelta2 = self.rotor2.avanzar()
                if vuelta2:
                    self.rotor3.avanzar()    
            letra_cifrada = self.rotor1.cifrar(letra)
            letra_cifrada = self.rotor2.cifrar(letra_cifrada)
            letra_cifrada = self.rotor3.cifrar(letra_cifrada)
            mensaje_cifrado += letra_cifrada
            
            print(self.rotor1.posicion, self.rotor2.posicion, self.rotor3.posicion)
        return mensaje_cifrado

    def descifrar_mensaje(self, mensaje: str) -> str:
        self.rotor1.reiniciar()
        self.rotor2.reiniciar()
        self.rotor3.reiniciar()
        mensaje_descifrado = ""
        for letra in mensaje:
            vuelta1 = self.rotor1.avanzar()
            if vuelta1:
                vuelta2 = self.rotor2.avanzar()
                if vuelta2:
                    self.rotor3.avanzar()    
            letra_descifrada = self.rotor3.descifrar(letra)
            letra_descifrada = self.rotor2.descifrar(letra_descifrada)
            letra_descifrada = self.rotor1.descifrar(letra_descifrada)
            mensaje_descifrado += letra_descifrada
            print(self.rotor1.posicion, self.rotor2.posicion, self.rotor3.posicion)
        return mensaje_descifrado