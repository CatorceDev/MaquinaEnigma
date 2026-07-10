from elements import machine, cableado


indicador = True
while indicador:
    print("\n--------------------------------------------------------------\n")
    print("SIMULADOR DE LA MAQUINA ENIGMA")

    print("\nETAPA DE CONFIGURACION DE LA MÁQUINA")
    
    while True:
        if indicador == False:break
        error = True
        while error == True:
            contraseña = input("Ingresa tu contraseña de cifrado: ")
            
            print("Nombra tus rotores :)\n")
            rotor1 = input("Nombre de tu rotor 1: ")
            rotor2 = input("Nombre de tu rotor 2: ")
            rotor3 = input("Nombre de tu rotor 3: ")
            
            semilla = cableado.crearSemilla(contraseña)
            semilla_rotor1 = cableado.semilla_rotores(semilla, rotor1)
            semilla_rotor2 = cableado.semilla_rotores(semilla, rotor2)
            semilla_rotor3 = cableado.semilla_rotores(semilla, rotor3)
            
            cableado_rotor1 = cableado.crearCableado(semilla_rotor1)
            cableado_rotor2 = cableado.crearCableado(semilla_rotor2)
            cableado_rotor3 = cableado.crearCableado(semilla_rotor3)
            
            posicion_rotor1 = cableado.pos_i_rotores(semilla_rotor1)
            posicion_rotor2 = cableado.pos_i_rotores(semilla_rotor2)
            posicion_rotor3 = cableado.pos_i_rotores(semilla_rotor3)
                
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
