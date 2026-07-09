from elements import machine as machine

indicador = True
while indicador:
    print("\n--------------------------------------------------------------\n")
    print("SIMULADOR DE LA MAQUINA ENIGMA")

    print("\n ETAPA DE CONFIGURACION DE LA MÁQUINA")
    
    posicion_rotores = input("Ingrese la posicion inicial del rotor 1, 2 y 3 (ejemplo: 0,0,0): ")
    posicion_rotores = [int(x) for x in posicion_rotores.split(",")]
    machine.configurar_rotores(posicion_rotores)
    
    while True:
        
        opcion = input("Ingrese 1 para cifrar un mensaje, 2 para descifrar un mensaje: ")
        if opcion not in ["1", "2"]:
            print("La opcion ingresada no es válida. Por favor, ingrese 1 o 2.")    
            continue
        
        match opcion:
            case "1":
                
                mensaje = input("Ingrese el mensaje a cifrar: ")

                print("Mensaje original: ", mensaje)

                mensaje_cifrado = machine.cifrar_mensaje(mensaje)
                print("Mensaje cifrado: ", mensaje_cifrado)
            
            case "2":
                mensaje = input("Ingrese el mensaje a descifrar: ")
                print("Mensaje original: ", mensaje)
                mensaje_descifrado = machine.descifrar_mensaje(mensaje)
                print("Mensaje descifrado: ", mensaje_descifrado)

    continuar = input("Para terminar el programa presione q, para continuar presione cualquier tecla: ")
    if continuar.lower() == "q": indicador = False
    else: indicador = True
