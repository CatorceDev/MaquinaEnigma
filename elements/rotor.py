class Rotor:
    
    def __init__(self, abecedario:str, cableado: str, posicion_inicial: int):
        self.abecedario = abecedario
        self.cableado = cableado
        self.posicion = posicion_inicial

    def Avanzar(self) -> str:
        #logica de avance del rotor
        self.cableado = self.cableado[1:] + self.cableado[0]
    
    def cifrar(self, letra: str) -> str:
        #implementar la logica del cifrado del rotor
        if letra in self.abecedario:
            index = self.abecedario.index(letra)
            letra_cifrada = self.cableado[index]
            self.Avanzar()
            return letra_cifrada
        return letra