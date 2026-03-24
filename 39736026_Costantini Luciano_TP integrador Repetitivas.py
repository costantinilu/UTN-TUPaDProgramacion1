ejercicio = 0
while ejercicio != 6:
    print()
    print("\t\033[34mEJERCICIOS")
    print("\tEjercicio 1 - Caja de Kiosco")
    print("\tEjercicio 2 - Acceso al campus y menú seguro")
    print("\tEjercicio 3 - Agenda de turnos con nombres")
    print("\tEjercicio 4 - Escape Room: La Bóveda")
    print("\tEjercicio 5 - Escape Room: La Arena del Gladiador")
    print("\tOpción 6 - SALIR\033[0m")
    print()
    elegida = input("Ingrese la opción deseada: ")
    print()
    if elegida.isdigit():
        ejercicio = int(elegida)
        if 5 >= ejercicio >= 1:
            if ejercicio == 1:
                #PRIMER EJERCICIO
                print("\033[32m----------- EJERCICIO 1 ----------")
                while True:
                    nombre = input("Ingrese nombre: ")
                    if not nombre.isalpha():
                        print("ERROR, ingrese solo letras.")
                    else:
                        break
                while True:
                    cantidad_productos = input("Ingrese cantidad de productos: ")
                    if not cantidad_productos.isdigit():
                        print("ERROR, ingrese un número entero positivo.")
                    else:
                        cantidad_productos = int(cantidad_productos)
                        break

                productos_string = ""
                precio_total = 0
                descuento_total = 0
                for i in range(1, cantidad_productos+1):
                    while True:
                        precio = input(f"Ingrese precio del producto {i}: ")
                        if not precio.isdigit():
                            print("ERROR, ingrese un número entero positivo.")
                        else:
                            precio = int(precio)
                            break

                    while True:
                        descuento = input("Ingrese 's' o 'S' si tiene descuento - 'n' o 'N' si no tiene descuento: ")
                        if descuento not in ("s", "S", "n", "N"):
                            print("ERROR, ingrese 's' o 'S' si tiene descuento - 'n' o 'N' si no tiene descuento: ")
                        elif descuento in ("s", "S"):
                            descuento_valor = precio * 0.10
                            break
                        else:
                            descuento_valor = 0
                            break
                    precio_total += precio
                    descuento_total += descuento_valor
                    productos_string += f"Producto {i} - Precio: {precio} - Descuento (S/N): {descuento}\n"

                precio_con_descuento = precio_total - descuento_total
                promedio_por_producto = precio_con_descuento / cantidad_productos
                print(f"\nCliente: {nombre}")
                print(f"Cantidad de productos: {cantidad_productos}")
                print(productos_string)
                print(f"Total sin descuento: {precio_total}$")
                print(f"Total con descuento: {precio_con_descuento}$")
                print(f"Ahorro: {descuento_total}$")
                print(f"Promedio por producto {promedio_por_producto}$\033[0m")

            elif ejercicio == 2:
                #SEGUNDO EJERCICIO 
                print("\033[31m----------- EJERCICIO 2 ----------")
                ingreso_correcto = False
                for i in range(0, 3):
                    usuario = input("Ingrese usuario: ")
                    contraseña = input ("Ingrese contrasña: ")
                    if usuario != "alumno" or contraseña != "python123":
                        if i == 2:  
                            print("CUENTA BLOQUEADA por 3 intentos fallidos.")
                        else:
                            print("ERROR, ingrese un usuario y contraseña correcta.")
                    else:
                        ingreso_correcto = True
                        break

                if ingreso_correcto:
                    print("BIENVENIDO!")

                opcion = 0
                while (opcion != 4) and (ingreso_correcto == True):
                    print()
                    print("\tMENÚ DE OPCIONES")
                    print("\tOpción 1 - Estado de inscripción")
                    print("\tOpción 2 - Cambio de contraseña")
                    print("\tOpción 3 - Frase")
                    print("\tOpción 4 - SALIR")
                    ingreso = input("Ingrese la opción deseada: ")
                    if ingreso.isdigit():
                        opcion = int(ingreso)

                    if opcion <= 4 and opcion >= 1:
                        if opcion == 1:
                            print("\nEstado de inscripción: \t INSCRIPTO\n")
                        elif opcion == 2:
                            contraseñanueva = input ("Ingrese contrasña: ")
                            contraseñanueva2 = input ("Ingrese nuevamente la contrasña: ")
                            if (contraseñanueva == contraseñanueva2) and (len(contraseñanueva) >= 6):
                                print("\nContraseña modificada satisfactoriamente. \n")
                            else:
                                print("\nLa contraseñas no coiniciden o el número de caracteres es inferior a 6.\n")
                        elif opcion == 3:
                            print("\nSigue tu instinto, sigue tus sueños.\n")
                    else:
                        print("\nERROR, INGRESE UN NÚMERO ENTRE 1 Y 4.\033[0m")

            elif ejercicio == 3:
                #TERCER EJERCICIO
                print("\033[33m----------- EJERCICIO 3 ----------")
                operador = input("Nombre del operador: ")
                menu = 0
                turno1_1 = ""
                turno1_2 = ""
                turno1_3 = ""
                turno1_4 = ""
                turno2_1 = ""
                turno2_2 = ""
                turno2_3 = ""
                while menu != 5:
                    print()
                    print("\tMENÚ DE OPCIONES")
                    print("\tOpción 1 - Reservar turno")
                    print("\tOpción 2 - Cancelar turno por nombre")
                    print("\tOpción 3 - Ver agenda del día")
                    print("\tOpción 4 - Ver resumen general")
                    print("\tOpción 5 - Cerrar sistema")
                    ingreso = input("Ingrese la opción deseada: ")
                    if ingreso.isdigit():
                        menu = int(ingreso)
                    if menu <= 5 and menu >= 1:
                        if menu == 1:
                            while True:
                                print()
                                print("Ingresar 1 para día lunes")
                                print("Ingresar 2 para día martes")
                                dia = input("Ingresar: ")

                                if dia.isdigit():
                                    dia = int(dia) #Acá creo un dia que sea int para usarlo para comparar.
                                if dia == 1:
                                    print("Día lunes seleccionado.")
                                    paciente = input("Ingresar nombre del paciente (solo letras): ")
                                    if paciente.isalpha():
                                        if paciente not in turno1_1 and paciente not in turno1_2 and paciente not in turno1_3 and paciente not in turno1_4:
                                            if turno1_1 == "":
                                                turno1_1 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día lunes.")
                                                break
                                            elif turno1_2 == "":
                                                turno1_2 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día lunes.")
                                                break
                                            elif turno1_3 == "":
                                                turno1_3 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día lunes.")
                                                break
                                            elif turno1_4 == "":
                                                turno1_4 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día lunes.")
                                                break
                                            else:
                                                print("Todos los turnos para el día lunes están ocupados")
                                                break
                                        else:
                                            print(f"El paciente {paciente} ya tiene turno asignado el día lunes.")
                                    else:
                                        print("ERROR, ingrese solo letras")        
                                elif dia == 2:
                                    print("Día martes seleccionado.")
                                    paciente = input("Ingresar nombre del paciente (solo letras): ")
                                    if paciente.isalpha():
                                        if paciente not in turno2_1 and paciente not in turno2_2 and paciente not in turno2_3:
                                            if turno2_1 == "":
                                                turno2_1 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día martes.")
                                                break
                                            elif turno2_2 == "":
                                                turno2_2 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día martes.")
                                                break
                                            elif turno2_3 == "":
                                                turno2_3 += f"{paciente}"
                                                print(f"El turno para {paciente}, ha sido asignado para el día martes.")
                                                break
                                            else:
                                                print("Todos los turnos para el día lunes están ocupados")
                                                break
                                        else:
                                            print(f"El paciente {paciente} ya tiene turno asignado el día martes.")
                                    else:
                                        print("ERROR, ingrese solo letras")
                                else:
                                    print("ERROR, ingrese 1 para día lunes, 2 para día martes.")
                        if menu == 2:  
                            print()          
                            while True: 
                                paciente = input("Ingresar nombre del paciente (solo letras): ")
                                if (paciente.isalpha()):
                                    if paciente in turno1_1 or paciente in turno1_2 or paciente in turno1_3 or paciente in turno1_4:
                                        if paciente in turno1_1:
                                            turno1_1 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        elif paciente in turno1_2:
                                            turno1_2 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        elif paciente in turno1_3:
                                            turno1_3 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        elif paciente in turno1_4:
                                            turno1_4 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        else:
                                            print("ERROR, no se pudo eliminar el turno")
                                            break
                                    elif paciente in turno2_1 or paciente in turno2_2 or paciente in turno2_3:
                                        if paciente in turno2_1:
                                            turno2_1 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        elif paciente in turno1_2:
                                            turno2_2 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        elif paciente in turno1_3:
                                            turno2_3 = ""
                                            print("Turno eliminado con éxito.")
                                            break
                                        else:
                                            print("ERROR, no se pudo eliminar el turno")
                                            break
                                    else:
                                        print(f"El paciente {paciente} no tenía turnos asignados.")
                                else:
                                    print("INCORRECTO, el nombre debe contener solo letras.")
                        if menu == 3:  
                            print()
                            buscardia = input("Ingrese 1 para el día lunes o 2 para el día martes: ")
                            if buscardia.isdigit():
                                buscardia = int(buscardia)
                            if buscardia == 1:
                                if turno1_1 != "":
                                    t1_1 = turno1_1
                                else: 
                                    t1_1 = "(libre)"
                                if turno1_2 != "":
                                    t1_2 = turno1_2
                                else: 
                                    t1_2 = "(libre)"
                                if turno1_3 != "":
                                    t1_3 = turno1_3
                                else: 
                                    t1_3 = "(libre)"
                                if turno1_4 != "":
                                    t1_4 = turno1_4
                                else: 
                                    t1_4 = "(libre)"  
                                print(f"Turno 1: {t1_1} - Turno 2: {t1_2} - Turno 3: {t1_3} - Turno 4: {t1_4}")
                            elif buscardia == 2:
                                if turno2_1 == "":
                                    turno2_1 = "(libre)"
                                if turno2_2 == "":
                                    turno2_2 = "(libre)"
                                if turno2_3 == "":
                                    turno2_3 = "(libre)"
                                print(f"Turno 1: {turno2_1} - Turno 2: {turno2_2} - Turno 3: {turno2_3}")
                            else:
                                print("ERROR, solo podés elegir 1 o 2.")
                        if menu == 4:
                            print()
                            turnosocupados1 = 0
                            turnosocupados2 = 0
                            if turno1_1 != "":
                                turnosocupados1 += 1
                            if turno1_2 != "":
                                turnosocupados1 += 1
                            if turno1_3 != "":
                                turnosocupados1 += 1
                            if turno1_4 != "":
                                turnosocupados1 += 1
                            if turno2_1 != "":
                                turnosocupados2 += 1
                            if turno2_2 != "":
                                turnosocupados2 += 1
                            if turno2_3 != "":
                                turnosocupados2 += 1
                            
                            if turnosocupados1 > turnosocupados2:
                                print(f"El día lunes hay más turnos ocupados que el día martes.")
                            elif turnosocupados2 > turnosocupados1:
                                print(f"El día martes hay más turnos ocupados que el día lunes.")
                            else:
                                print("Hay la misma cantidad de turnos ocupados cada día.")
                            if turnosocupados1 == 1:
                                print(f"El día lunes hay {turnosocupados1} turno ocupado. ")
                            else:
                                print(f"El día lunes hay {turnosocupados1} turnos ocupado(s). ")
                            if turnosocupados2 == 1:
                                print(f"El día martes hay {turnosocupados2} turno ocupado. ")
                            else:
                                print(f"El día martes hay {turnosocupados2} turnos ocupado(s). ")
                        if menu == 5: 
                            print("DESCONECTADO EXITOSAMENTE!\033[0m") 

            elif ejercicio == 4:
                #EJERCICIO 4
                print("\033[35m----------- EJERCICIO 4 ----------")
                energia = 100
                tiempo = 12
                cerraduras_abiertas = 0
                alarma = False
                codigo_parcial = ""
                forzar_cerradura = 0
                agente = input("Ingrese nombre del agente: ")
                if agente.isalpha():
                    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
                        if alarma == True and tiempo <= 3:
                            print()
                            print("DERROTA POR BLOQUEO DE ALARMA!!!")
                            break
                        print()
                        print("1 - Forzar cerradura")
                        print("2 - Hackear panel")
                        print("3 - Descansar")
                        print()
                        op = int(input("Ingrese opción: "))
                        
                        if op == 1:
                            forzar_cerradura += 1
                            if forzar_cerradura == 3:
                                energia -= 20
                                tiempo -= 2
                                alarma = True
                            else:
                                if energia < 40:
                                    nro = input("Ingresar un numero del 1 al 3: ")
                                    if nro == 3:
                                        alarma = True
                                        print("HA COMENZADO A SONAR LA ALARMA!!!")
                                energia -= 20
                                tiempo -= 2
                                if alarma == False:
                                    cerraduras_abiertas += 1
                        elif op == 2:
                            forzar_cerradura = 0
                            energia -= 10
                            tiempo -= 3
                            for i in range (0, 4):
                                codigo_parcial += "A"
                            if len(codigo_parcial) >= 8:
                                cerraduras_abiertas += 1
                        elif op == 3:
                            forzar_cerradura = 0
                            energia += 15
                            if energia > 100:
                                energia = 100
                            tiempo -= 1
                            if alarma == True:
                                tiempo -=10 
                        print()
                        print(f"Energía: {energia} - Tiempo: {tiempo} - Cerraduras abiertas: {cerraduras_abiertas} - Alarma: {alarma}.")
                else:
                    print()
                    print("ERROR, erro en el nombre del agente, solo se aceptan letras.")

                if cerraduras_abiertas >= 3:
                    print()
                    print("FELICITACIONES, HA GANADO EL JUEGO!!!")
                elif energia <= 0 or tiempo <= 0:
                    print()
                    print("DERROTA POR FALTA DE ENERGÍA O TIEMPO")

            elif ejercicio == 5:
                #EJERCICIO 5
                print("\033[91m----------- EJERCICIO 5 ----------")
                jugador = input("Ingrese el nombre de su gladiador: ")
                while not jugador.isalpha():
                    jugador = input("Ingrese CORRECTAMENTE el nombre de su gladiador: ")
                enemigo = "Enemigo"
                jugador_vida = 100
                enemigo_vida = 100
                jugador_daño = 15
                enemigo_daño= 12
                pociones = 3
                jugador_turno = True
                while jugador_vida > 0 and enemigo_vida > 0:
                    print()
                    print("ESTADÍSTICAS")
                    print(f"Vida restante de {jugador}: {jugador_vida}")
                    print(f"Vida restante de {enemigo}: {enemigo_vida}")
                    print(f"Pociones restantes: {pociones}")
                    print()
                    input("Presioná enter para seguir")
                    print() 
                    
                    print("MENÚ DEL JUEGO")
                    print("1- Ataque Pesado")
                    print("2- Ráfaga Veloz")
                    print("3- Curar")
                    opcion = input("INGRESE LA OPCIÓN DESEADA: ")
                    print()
                    if opcion.isdigit():
                        opcion = int(opcion)
                    else:
                        opcion = input("ERROR, ingrese una opcion correcta de 1 a 3: ")
                        opcion = int(opcion)
                    if opcion == 1:
                        if enemigo_vida < 20:
                            daño = jugador_daño * 1.5
                            enemigo_vida -= daño
                            print("HA SIDO UN GOLPE CRÍTICO. ")
                        else:
                            daño = jugador_daño
                            enemigo_vida -= daño
                        print(f"¡Atacaste a {enemigo} por {daño} puntos de daño!")
                        print()
                    elif opcion == 2:
                        for i in range(3):
                            enemigo_vida -= 5
                            print("\t> Golpe conectado por 5 de daño")
                            input("Presioná enter para seguir")
                    elif opcion == 3:
                        if pociones > 0:
                            jugador_vida += 30
                            if jugador_vida > 100:
                                jugador_vida = 100
                            pociones -= 1
                            print(f"Ahora tu vida es de: {jugador_vida}")
                        else:
                            print("¡No quedan pociones!")
                    #input("Presioná enter para seguir")
                    print()
                    jugador_vida -= enemigo_daño
                    print(f"¡Te atacó {enemigo} por {enemigo_daño} puntos de daño!")
                    print()
                    input("Presioná enter para seguir")
                    print()

                if enemigo_vida < 0:
                    print("HAS GANADO!!! Derrotaste al enemigo al haber terminado con su vida.")
                else:
                    print("PERDISTE!!! El enemigo terminó con tu vida.")

        elif ejercicio == 6:
            print("SE HA DESCONECTADO EXITOSAMENTE")
            break

