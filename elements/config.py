from . import cableado

class config:
    def __init__(self, rotor1:str, rotor2:str, rotor3:str, semilla:int):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.semilla = semilla
    
    def semillas_rotores(self):
        semilla_rotor1 = cableado.semilla_rotores(self.semilla, self.rotor1)
        semilla_rotor2 = cableado.semilla_rotores(self.semilla, self.rotor2)
        semilla_rotor3 = cableado.semilla_rotores(self.semilla, self.rotor3)
        
        return semilla_rotor1, semilla_rotor2, semilla_rotor3
    
    def posiciones_i_rotores(self):
        
        semilla_rotor1, semilla_rotor2, semilla_rotor3 = self.semillas_rotores()
        
        posicion_rotor1 = cableado.pos_i_rotores(semilla_rotor1)
        posicion_rotor2 = cableado.pos_i_rotores(semilla_rotor2)
        posicion_rotor3 = cableado.pos_i_rotores(semilla_rotor3)
        
        return posicion_rotor1, posicion_rotor2, posicion_rotor3
        
    def cableado_rotores(self):
        
        semilla_rotor1, semilla_rotor2, semilla_rotor3 = self.semillas_rotores()
        
        cableado_rotor1 = cableado.crearCableado(semilla_rotor1)
        cableado_rotor2 = cableado.crearCableado(semilla_rotor2)
        cableado_rotor3 = cableado.crearCableado(semilla_rotor3)
        
        return cableado_rotor1, cableado_rotor2, cableado_rotor3