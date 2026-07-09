class Rotor:
    
    def __init__(self, abecedario:str, cableado: str, posicion_inicial: int):
        self.abecedario = abecedario
        self.cableado = (
            cableado[posicion_inicial:] + cableado[:posicion_inicial]
        )
        self.cableado_original = cableado
        self.posicion = posicion_inicial
        self.posicion_inicial = posicion_inicial

    def avanzar(self) -> bool:
        #logica de avance del rotor
        self.cableado = self.cableado[1:] + self.cableado[0]  # Rotar el cableado
        self.posicion = (self.posicion + 1) % len(self.abecedario)
        return self.posicion == 0  #Retorna si el rotor ha completado una vuelta completa
    
    def cifrar(self, letra: str) -> str:
        #implementar la logica del cifrado del rotor
        if letra in self.abecedario:
            index = self.abecedario.index(letra)
            letra_cifrada = self.cableado[index]
            return letra_cifrada
        return letra
    
    def descifrar(self, letra: str) -> str:
        #implentando logica de descifrado del rotor
        if letra in self.cableado:
            index = self.cableado.index(letra)
            letra_descifrada = self.abecedario[index]
            return letra_descifrada
        return letra
    
    def reiniciar(self):
        self.cableado = (
            self.cableado_original[self.posicion_inicial:] + self.cableado_original[:self.posicion_inicial]
        )
        self.posicion = self.posicion_inicial
