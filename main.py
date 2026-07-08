from elements import machine as machine

indicador = True
while indicador:
    print("\n--------------------------------------------------------------\n")
    print("SIMULADOR DE LA MAQUINA ENIGMA")
    mensaje = input("Ingrese el mensaje a cifrar: ")

    print("Mensaje original: ", mensaje)

    mensaje_cifrado = machine.cifrar_mensaje(mensaje)
    print("Mensaje cifrado: ", mensaje_cifrado)
    
    continuar = input("Para terminar el programa presione q, para continuar presione cualquier tecla: ")
    if continuar.lower() == "q": indicador = False
    else: indicador = True
