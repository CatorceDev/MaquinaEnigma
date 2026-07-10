from sys import maxunicode
from hashlib import sha256
from random import seed, shuffle

N = maxunicode + 1
contraseña = "soycatorcc"

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
    #* Esta funcion genera la posicion inicial desde donde partira cada rotor a la hora de cifrar a partir de la semilla del rotor
    
    posicion_rotor = semilla_rotor % N
    return posicion_rotor


def crearCableado(semilla_rotor) -> int:
    #* Esta funcion creará un cableado basado en la semilla del rotor de tal manera que cada rotor tendra un cableado distinto
    
    seed(semilla_rotor)
    cableado = list(range(N))
    shuffle(cableado)
    