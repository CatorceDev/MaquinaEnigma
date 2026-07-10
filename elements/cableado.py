from sys import maxunicode
import secrets
from hashlib import sha256

N = maxunicode + 1
contraseña = "soycatorcc"

def crearCableado(mensaje: str) -> str:
    #* Esta funcion creará un cableado basado en una f(x) que 
    
    
    
    letra_cifrada = 0

def crearSemilla(contraseña) -> int:
    #* Esta funcion generará una semilla pseudoaleatoria a partir de la contraseña para la conversación que se usará para crear el cableado de los rotores, el orden de los rotores, su posicion inicial.
    
    contraseña_hash = sha256(contraseña.encode()).hexdigest()
    semilla = int(contraseña_hash, 16)
    
    return semilla

def semilla_rotores(semilla:int, nombre_rotor:str) -> int:
    #* Esta funcion generará una semilla pseudoaleatoria para cada rotor para definir la posicion inicial de cada rotor y su cableado
    
    instruccion = f"{semilla, nombre_rotor}"
    
    hash_rotor = sha256(instruccion.encode()).hexdigest()
    semilla_rotor = int(hash_rotor, 16)
    
    return semilla_rotor

def pos_i_rotores(semilla_rotor):
    posicion_rotor = semilla_rotor % N
    return posicion_rotor
