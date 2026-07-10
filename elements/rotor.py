class Rotor:

    
    def __init__(self, cableado: list, posicion_inicial: int):
        self.cableado = (
            cableado[posicion_inicial:] + cableado[:posicion_inicial]
        )
        self.cableado_original = cableado
        self.posicion = posicion_inicial
        self.posicion_inicial = posicion_inicial
        
        self.N = len(cableado)

    def avanzar(self) -> bool:
        #logica de avance del rotor
        self.cableado = self.cableado[1:] + [self.cableado[0]]  # Rotar el cableado
        self.posicion = (self.posicion + 1) % self.N
        return self.posicion == 0  #Retorna si el rotor ha completado una vuelta completa
    
    def cifrar(self, letra: str) -> str:
        codigo = ord(letra)
        codigo_cifrado = self.cableado[codigo]
        return chr(codigo_cifrado)
    
    def descifrar(self, letra: str) -> str:
        #implentando logica de descifrado del rotor
        codigo_unicode = ord(letra)
        codigo_original = self.cableado.index(codigo_unicode)
        return chr(codigo_original)
        
        
    
    def reiniciar(self):
        self.cableado = (
            self.cableado_original[self.posicion_inicial:] + self.cableado_original[:self.posicion_inicial]
        )
        self.posicion = self.posicion_inicial
