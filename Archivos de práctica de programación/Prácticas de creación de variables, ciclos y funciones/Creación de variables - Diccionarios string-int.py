# Función para crear diccionarios de datos entradas string e información gramatical int

def creacion_dsi():

    lista_dsi = []
    numero_dsi = 1
    cancelacion = False
    cancelacion2 = False

    print("-" * 100)
    print("Función para la creación de una lista de diccionarios")
    print("-" * 100)

    while not cancelacion:

        while not cancelacion2:
            
            try:
                cant_d = int(input("¿Cuántos diccionarios desea crear? (Solamente números): "))
                print("-" * 100)
                print("Cantidad valida")
                print("-" * 100)
                
            except ValueError:
                print("-" * 100)
                print("Entrada no valida, favor de intentarlo de nuevo")
                print("-" * 100)
                continue

            if cant_d <= 0:
                print("Creación de diccionarios cancelada")
                print("-" * 100)
                break

            elif cant_d > 0:
                
                for i in range(cant_d):
                    
                    entrada_e = input("Escriba la entrada del diccionario: ").strip().capitalize()
                    
                    if entrada_e == "Cancelar":
                        print("-" * 100)
                        print("Creación del diccionario cancelada")
                        print("-" * 100)
                        cancelacion2 = True
                        break
                    
                    while True:

                        try:
                            print("-" * 100)
                            inf_gram = int(input("Escriba la información gramatical de la entrada (Solamente números enteros, excepto el 0): "))
                            print("-" * 100)

                        except ValueError:
                            print("-" * 100)
                            print("Entrada no valida - Favor de intentarlo de nuevo")
                            continue

                        if inf_gram == 0:
                            print("Creación del diccionario cancelada")
                            print("-" * 100)
                            cancelacion2 = True
                            break

                        elif inf_gram > 0 or inf_gram < 0:
                            print("Entrada valida")
                            print("-" * 100)
                            lista_dsi.append({entrada_e : inf_gram})
                            print(f'Lista número {numero_dsi} creada exitosamente')
                            print("-" * 100)
                            numero_dsi = numero_dsi + 1
                            cancelacion2 = True
                            break
    
        while True:
            continuar = str(input("¿Desea continuar con la creación de diccionarios? (Si / No): ")).strip().capitalize()

            if continuar == "No":
                print("-" * 100)
                print("Entrada valida - Creación de diccionarios terminada")
                print("-" * 100)
                for index, diccionarios in enumerate(lista_dsi, start = 1):
                    print("-" * 100)
                    print(f'El diccionario número {index} contiene: {diccionarios}')
                    print("-" * 100)
                cancelacion = True
                break

            elif continuar == "Si":
                print("-" * 100)
                print("Entrada valida - Se continuará con la creación de diccionarios")
                print("-" * 100)
                cancelacion2 = False
                break

            else:
                print("-" * 100)
                print("Opción no válida - Favor de ingresar una opción valida")
                print("-" * 100)

    return print("Diccionarios creados en la variable 'lista_dss'")

creacion_dsi()