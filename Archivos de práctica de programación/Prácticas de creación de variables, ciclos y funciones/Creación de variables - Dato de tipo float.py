# Función para crear diccionarios de datos string

def creacion_dato_float():

    cancelacion = False
    cancelacion2 = False
    cancelacion3 = False
    cancelacion4 = False

    print("-" * 100)

    while not cancelacion:

        while not cancelacion2:
            
            try:
                
                dato_float = float(input("""Escriba el valor que desea definir en la variable
                (Cualquier dato escrito como número entero se definirá con el decimal '.0'): """))
                print("-" * 100)
                print("Entrada válida")
                print("-" * 100)

            except ValueError:

                print("-" * 100)
                print("Dato no válido - Favor de intentarlo nuevamente")
                print("-" * 100)
                continue

            if dato_float == 0.0:

                print("Creación de la variable cancelada")
                print("-" * 100)
                cancelacion = True
                break

            elif dato_float > 0.0 or dato_str < 0.0:

                print("Dato válido - Variable creada correctamente")
                print("-" * 100)

            while not cancelacion3:

                cambio = str(input("¿Desea cambiar el dato de la variable? (Si / No): ")).strip().capitalize()

                if cambio == "Si":
                    
                    print("-" * 100)
                    print("Entrada valida - Procediendo al cambio del dato de la variable")
                    print("-" * 100)
                    break

                elif cambio == "No":

                    print("-" * 100)
                    print("Entrada valida")
                    print("-" * 100)
                    print(dato_float)
                    print("-" * 100)

                    while not cancelacion4:

                        redondeo = input("¿Desea redondear el dato de la variable? (Si / No): ").strip().capitalize()

                        if redondeo == "No":
                            print("-" * 100)
                            print("Entrada válida - Creación de la variable terminada")
                            print("-" * 100)
                            print(dato_float)
                            cancelacion = True
                            cancelacion2 = True
                            cancelacion3 = True
                            break

                        elif redondeo == "Si":
                            print("-" * 100)
                            print("Entrada válida - Redondeando el número ")
                            print("-" * 100)

                            while True:

                                try:
                                    num_redo = int(input("Escriba la cantidad de decimales que quiera redondear: (Solamente números): "))
                                    print("Cantidad válida")
                                    print("-" * 100)

                                except ValueError:
                                    print("Entrada no válida - Favor de intentarlo de nuevo")
                                    print("-" * 100)
                                    continue

                                if num_redo == 0:
                                    print("Cantidad convertida a número entero")
                                    print("-" * 100)
                                    print(dato_float)
                                    print("-" * 100)
                                    dato_float = round(dato_float,num_redo)
                                    cancelacion = True
                                    cancelacion2 = True
                                    cancelacion3 = True
                                    cancelacion4 = True
                                    break

                                elif num_redo > 0:
                                    print(f'Cantidad redondeada a {num_redo} decimales')
                                    print("-" * 100)
                                    dato_float = round(dato_float,num_redo)
                                    print(dato_float)
                                    print("-" * 100)
                                    cancelacion = True
                                    cancelacion2 = True
                                    cancelacion3 = True
                                    cancelacion4 = True
                                    break

                                else:
                                    print("-" * 100)
                                    print("Cantidad no válida - Favor de intentarlo de nuevo")
                                    print("-" * 100)

                        else:
                            print("-" * 100)
                            print("Entrada no válida - Favor de intentarlo de nuevo")
                            print("-" * 100)

                else:
                    print("-" * 100)
                    print("Opción no válida - Favor de ingresar una opción valida")
                    print("-" * 100)
                    continue

    return print("Dato de tipo float creada en la variable 'dato_float'")

creacion_dato_float()