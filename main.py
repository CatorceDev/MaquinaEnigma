from elements import machine as machine

print("SIMULADOR DE LA MAQUINA ENIGMA")
mensaje = input("Ingrese el mensaje a cifrar: ")

print("Mensaje original: ", mensaje)

mensaje_cifrado = machine.cifrar_mensaje(mensaje)
print("Mensaje cifrado: ", mensaje_cifrado)