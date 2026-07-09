from elements import machine as machine

indicador = True
while indicador:
    print("\n--------------------------------------------------------------\n")
    print("SIMULADOR DE LA MAQUINA ENIGMA")

    print("\nETAPA DE CONFIGURACION DE LA MÁQUINA")
    
    while True:
        if indicador == False:break
        error = True
        while error == True:
            try:
                posicion_rotores = input("Ingrese la posicion inicial del rotor 1, 2 y 3 (ejemplo: 0,0,0) o enter para salir: ")
                if posicion_rotores == "":
                    indicador = False
                    break
                posicion_rotores = [int(x) for x in posicion_rotores.split(",")]
                
                if len(posicion_rotores) != 3:
                    raise ValueError
                
                machine.configurar_rotores(posicion_rotores)
                error = False

            except ValueError: 
                print("Por favor, ingresa tres números separados por comas (ejemplo: 0,0,0)\n")
                error = True
        
        while True:
            if indicador == False: break
            opcion = input("\nIngrese 1 para cifrar un mensaje, 2 para descifrar un mensaje o enter para configurar de nuevo los rotores: ")
            
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
                
                case  _:
                    break

    continuar = input("\n\n¿Desea continuar? y/n: ")
    if continuar == "y": indicador = True
    elif continuar == "n": 
        indicador = False
        print("Saliendo del programa...")
    else: print("Opción no válida. Saliendo del programa."); indicador = False
