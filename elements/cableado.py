from sys import maxunicode
import secrets
from hashlib import sha256


contraseña = "soycatorcc"

def crearCableado(mensaje: str) -> str:
    #* Esta funcion creará un cableado basado en una f(x) que toma el valor unicode de cada letra para dar el valor encriptado de los rotores
    
    
    
    letra_cifrada = 0

def crearSemilla(contraseña) -> int:
    #* Esta funcion generará una semilla pseudoaleatoria a partir de la contraseña para la conversación que se usará para crear el cableado de los rotores, el orden de los rotores, su posicion inicial.
    
    contraseña_hash = sha256(contraseña.encode()).hexdigest()
    semilla = int(contraseña_hash, 16)
    
    return semilla

def semilla_rotores(semilla:int, nombre_rotor:str) -> int:
    
    instruccion = f"{semilla, nombre_rotor}"
    
    hash_rotor = sha256(instruccion.encode()).hexdigest()
    print(hash_rotor)
    
    return hash_rotor


semilla = crearSemilla(contraseña)
semilla_rotores(semilla, "rotor3")