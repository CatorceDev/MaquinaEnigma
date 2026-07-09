from sys import maxunicode
import secrets
from hashlib import sha256


contraseña = "soycatorcc"

def crearCableado(mensaje: str) -> str:
    #* Esta funcion creará un cableado basado en una f(x) que toma el valor unicode de cada letra para dar el valor encriptado de los rotores
    
    
    
    letra_cifrada = 0

def crearSemilla() -> str:
    #* Esta funcion generará una semilla pseudoaleatoria a partir de la contraseña para la conversación que se usará para crear el cableado de los rotores, el orden de los rotores, su posicion inicial.
    
    contraseña_hash = sha256(contraseña.encode()).hexdigest()
    semilla = int(contraseña_hash, 16)
    
    return semilla

def semilla_rotores():
    